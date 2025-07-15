
# Specpilot

This repository aims to provide the tools to deploy an AI-powered assistant for 3GPP specification, combining two main components:

1. **3GPP Specification Extraction (Python Script):**
   - Downloads official 3GPP specifications
   - Extracts and converts them to markdown format for easy processing and search
   - Output is organized by release in the `spec_md/` directory

2. **ChatGPT-like Features (Ollama + AnythingLLM):**
   - Runs Ollama locally to provide LLM inference (e.g., mistral, deepseek-r1)
   - Deploys AnythingLLM via Docker to enable a chat interface over your documents
   - Allows advanced querying, context window management

---

## Features
- Automated download and conversion of configured 3GPP specifications to markdown
- Local LLM inference using Ollama
- ChatGPT-like interface for document Q&A via AnythingLLM

---

## Installation & Setup

### Prerequisites
- Docker
- Docker Compose
- Python 3.8+
- Ollama (for local LLMs)
- Pandoc

### Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/herlesupreeth/specpilot.git
   cd specpilot
   mkdir -p llm_storage
   ```

2. **Install Ollama and Download Models:**
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ollama pull deepseek-r1
   ollama pull nomic-embed-text
   # You can use other Ollama models as well. See https://ollama.com/library for available models.
   ```

---

## 3GPP Specification Extraction (Python Script)

Currently, the repository contains 38 series specifications from Release 15-18 already downloaded and converted to markdown.

If you want to download additional specifications modify below two parameters in `3gpp_extraction.py`:

```python
# Add more releases as needed
RELEASES = ["Rel-15", "Rel-16", "Rel-17", "Rel-18"]
# Add more series as needed
SERIES = ["38_series"]
```

Then run:

```bash
sudo apt-get install -y pandoc
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 3gpp_extraction.py
```

This will download, extract, and convert 3GPP specs to markdown in `spec_md/`.

---

## Deployment of ChatGPT-like Features (Ollama + AnythingLLM)

1. (Optional) Configure environment variables in `.env` as needed.

2. Run Ollama:

   **Note:** If Ollama is already running, you can skip this step.
   ```bash
   ollama serve deepseek-r1
   # Replace 'deepseek-r1' with any other model you have pulled if desired.
   ```
   Visit http://localhost:11434 to verify Ollama is running.

3. Ensure Docker and Docker Compose are installed.

4. Start AnythingLLM:
   ```bash
   source .env
   docker-compose up -d
   ```

5. Access the UI at http://localhost:3001.

---

## Directory Structure
- `llm_storage/` - Persistent storage for models, documents, and context
- `spec_md/` - 3GPP specification markdown files
- `3gpp_extraction.py` - Extraction and processing script
- `docker-compose.yml` - Deployment configuration

---

## Contributing
Pull requests and issues are welcome! Please see the LICENSE for details.

## License
BSD 2-Clause License

---

## Troubleshooting

### Common Issues

- **Ollama not running:**  
   Ensure Ollama is installed and the model is served. Run `ollama serve <model>` and check http://localhost:11434.

- **Ollama model not found:**  
   Make sure you have pulled the model using `ollama pull <model_name>`. Check available models with `ollama list`.

- **Ollama not accessible:**  
   If Ollama is running but not accessible, check if the port (default 11434) is blocked by a firewall or if Ollama is configured to use a different port. To allow access in firewall run `sudo ufw allow 11434`.

- **Docker Compose errors:**  
   Verify Docker and Docker Compose are installed and running. Use `docker --version` and `docker-compose --version` to check.

- **Missing Python dependencies:**  
   Run `pip install -r requirements.txt` to install required packages.

- **Pandoc not found:**  
   Install Pandoc with `sudo apt-get install -y pandoc`.

- **Specs not downloading:**  
   Check your internet connection and verify the `RELEASES` and `SERIES` parameters in `3gpp_extraction.py`.

- **UI not accessible:**  
   Ensure Docker is running and the container is up. Check logs with `docker-compose logs` for any errors. Ensure `SERVER_PORT` in `.env` is open and not blocked by firewall. To allow access in firewall run `sudo ufw allow ${SERVER_PORT}`.

- **Port conflicts:**  
   If the specified ports are already in use, change the `SERVER_PORT` in `.env` and redeploy.

If encounter other issues, please open an issue in the repository with error details.
