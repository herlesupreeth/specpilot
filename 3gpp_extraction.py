# 3GPP Document Extraction and Conversion Script
# This script downloads 3GPP documents from specified releases,
# converts them to Markdown format, and saves them locally.

import os
import shutil
import subprocess
import zipfile

import requests
from bs4 import BeautifulSoup
from abc import ABC, abstractmethod

BASE_URL = "https://www.3gpp.org/ftp/Specs/latest/"
# Add more releases as needed
RELEASES = ["Rel-15", "Rel-16", "Rel-17", "Rel-18"]
# Add more series as needed
SERIES = ["38_series"]
DOWNLOAD_DIR = "spec_md"
CONVERTER = "docling"


class DocxToMarkdownConverter(ABC):
    DOCLING = "docling"

    @abstractmethod
    def convert(self, doc_path, md_path):
        pass


class DoclingConverter(DocxToMarkdownConverter):
    def convert(self, doc_path, md_path):
        try:
            subprocess.run(
                [
                    "docling",
                    "--from",
                    "docx",
                    "--to",
                    "md",
                    "--output",
                    os.path.dirname(md_path),
                    doc_path,
                ],
                capture_output=True,
                check=True,
            )
        except subprocess.CalledProcessError as e:
            print(f"Error converting {doc_path} to Markdown with Docling: {e}")
        except Exception as e:
            print(f"Unexpected error during Docling conversion of {doc_path}: {e}")


def unzip_and_convert(zip_path, zip_extract_dir, md_file_dir, converter):
    """
    Extract a zip file and convert docs to markdown using the specified converter.

    Args:
        zip_path: Path to the zip file
        zip_extract_dir: Directory to extract zip contents
        md_file_dir: Directory to save markdown files
        converter: DocxToMarkdownConverter instance
    """

    print(f"Unzipping: {zip_path}")
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(zip_extract_dir)
    # Walk through extracted files and convert .doc to .docx to .md
    for root, dirs, files in os.walk(zip_extract_dir):
        for file in files:
            if file.lower().endswith(".doc") and not file.lower().endswith(".docx"):
                doc_path = os.path.join(root, file)
                try:
                    # Use LibreOffice to convert .doc to .docx
                    subprocess.run(
                        [
                            "libreoffice",
                            "--headless",
                            "--convert-to",
                            "docx",
                            "--outdir",
                            root,
                            doc_path,
                        ],
                        capture_output=True,
                        check=True,
                    )
                except subprocess.CalledProcessError as e:
                    print(f"Error converting {file} to .docx: {e}")
                    continue

    # Walk through extracted files and convert .docx to .md
    for root, dirs, files in os.walk(zip_extract_dir):
        for file in files:
            if not file.lower().endswith(".docx"):
                continue

            doc_path = os.path.join(root, file)
            print(f"Converting to Markdown: {doc_path}")
            md_file_path = os.path.join(md_file_dir, file.rsplit(".", 1)[0] + ".md")
            converter.convert(doc_path, md_file_path)

    # Clean up extracted files and zip file
    shutil.rmtree(zip_extract_dir)
    os.remove(zip_path)


def download_file(url, save_path):
    if os.path.exists(save_path):
        print(f"File already exists: {save_path}")
        return True
    print(f"Downloading: {url}")
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Failed to download {url}, status code: {response.status_code}")
        return False
    with open(save_path, "wb") as f:
        f.write(response.content)
    return True


def download_and_process(release, spec_series, converter):
    download_url = BASE_URL + release + "/" + spec_series + "/"
    print(f"Processing: {download_url}")
    page = requests.get(download_url)
    if page.status_code != 200:
        print(f"Failed to retrieve {download_url}, status code: {page.status_code}")
        return
    soup = BeautifulSoup(page.text, "html.parser")
    if soup is None:
        print(f"Failed to parse HTML for {download_url}")
        return
    download_dir = os.path.join(DOWNLOAD_DIR, release, spec_series)
    if not os.path.exists(download_dir):
        print(f"Creating directory: {download_dir}")
        os.makedirs(download_dir)
    for link in soup.find_all("a"):
        file_url = link.get("href")
        if not file_url or file_url in ("../", "./"):
            continue
        if file_url.lower().endswith(".zip"):
            zip_file_name = file_url.rsplit("/")[-1]
            zip_file_name_without_extension = zip_file_name.rsplit(".", 1)[0]
            if any(
                f.startswith(zip_file_name_without_extension) and f.endswith(".md")
                for f in os.listdir(download_dir)
            ):
                print(
                    f"Markdown file already exists for {zip_file_name_without_extension}, skipping conversion."
                )
                continue
            zip_file_download_path = os.path.join(download_dir, zip_file_name)
            zip_file_extraction_dir = os.path.join(
                download_dir, zip_file_name_without_extension
            )
            if not download_file(file_url, zip_file_download_path):
                continue
            md_file_dir = download_dir
            unzip_and_convert(
                zip_file_download_path, zip_file_extraction_dir, md_file_dir, converter
            )


if __name__ == "__main__":
    print("Starting 3GPP document extraction and conversion...")
    if not os.path.exists(DOWNLOAD_DIR):
        print(f"Creating download directory: {DOWNLOAD_DIR}")
        os.makedirs(DOWNLOAD_DIR)
    for rel in RELEASES:
        for series in SERIES:
            download_and_process(rel, series, DoclingConverter())
    print("Processing complete.")
