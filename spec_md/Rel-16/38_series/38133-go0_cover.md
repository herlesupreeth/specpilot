+-------------------------------------------+-------------------------+
| 3GPP TS 38.133 V16.24.0 (2025-06)         |                         |
+===========================================+=========================+
| Technical Specification                   |                         |
+-------------------------------------------+-------------------------+
| 3rd Generation Partnership Project;       |                         |
|                                           |                         |
| Technical Specification Group Radio       |                         |
| Access Network;                           |                         |
|                                           |                         |
| NR;                                       |                         |
|                                           |                         |
| Requirements for support of radio         |                         |
| resource management                       |                         |
|                                           |                         |
| (Release 16)                              |                         |
+-------------------------------------------+-------------------------+
|                                           |                         |
+-------------------------------------------+-------------------------+
| ![](./media/image1.jpeg)                  | ![](./media/image2.png) |
+-------------------------------------------+-------------------------+
|                                           |                         |
+-------------------------------------------+-------------------------+
| The present document has been developed   |                         |
| within the 3rd Generation Partnership     |                         |
| Project (3GPP ^TM^) and may be further    |                         |
| elaborated for the purposes of 3GPP.\     |                         |
| The present document has not been subject |                         |
| to any approval process by the 3GPP       |                         |
| Organizational Partners and shall not be  |                         |
| implemented.\                             |                         |
| This Specification is provided for future |                         |
| development work within 3GPP only. The    |                         |
| Organizational Partners accept no         |                         |
| liability for any use of this             |                         |
| Specification.\                           |                         |
| Specifications and Reports for            |                         |
| implementation of the 3GPP ^TM^ system    |                         |
| should be obtained via the 3GPP           |                         |
| Organizational Partners\' Publications    |                         |
| Offices.                                  |                         |
+-------------------------------------------+-------------------------+

+----------------------------------------------------------------------+
|                                                                      |
+======================================================================+
| > ***3GPP***                                                         |
| >                                                                    |
| > Postal address                                                     |
| >                                                                    |
| > 3GPP support office address                                        |
| >                                                                    |
| > 650 Route des Lucioles - Sophia Antipolis                          |
| >                                                                    |
| > Valbonne - FRANCE                                                  |
| >                                                                    |
| > Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16                     |
| >                                                                    |
| > Internet                                                           |
| >                                                                    |
| > http://www.3gpp.org                                                |
+----------------------------------------------------------------------+
| ***Copyright Notification***                                         |
|                                                                      |
| No part may be reproduced except as authorized by written            |
| permission.\                                                         |
| The copyright and the foregoing restriction extend to reproduction   |
| in all media.                                                        |
|                                                                      |
| © 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, |
| TTA, TTC).                                                           |
|                                                                      |
| All rights reserved.                                                 |
|                                                                      |
| UMTS™ is a Trade Mark of ETSI registered for the benefit of its      |
| members                                                              |
|                                                                      |
| 3GPP™ is a Trade Mark of ETSI registered for the benefit of its      |
| Members and of the 3GPP Organizational Partners\                     |
| LTE™ is a Trade Mark of ETSI registered for the benefit of its       |
| Members and of the 3GPP Organizational Partners                      |
|                                                                      |
| GSM® and the GSM logo are registered and owned by the GSM            |
| Association                                                          |
+----------------------------------------------------------------------+

 Contents {#contents .TT}
========

Foreword 691 Scope 712 References 713 Definitions, symbols and
abbreviations 723.1 Definitions 723.2 Symbols 733.3 Abbreviations 743.4
Test tolerances 773.5 Frequency bands grouping 773.5.1 Introduction
773.5.2 NR operating bands in FR1 773.5.3 NR operating bands in FR2
783.6 Applicability of requirements in this specification version
783.6.1 RRC connected state requirements in DRX 793.6.2 Number of
serving carriers 793.6.2.1 Number of serving carriers for SA 793.6.2.2
Number of serving carriers for EN-DC 793.6.2.3 Number of serving
carriers for NE-DC 793.6.2.4 Number of serving carriers for NR-DC
803.6.3 Applicability for intra-band FR2 803.6.4 Applicability for FR2
UE power classes 803.6.5 Applicability for SDL bands 803.6.6
Applicability of requirements for NGEN-DC operation 803.6.7
Applicability of QCL 803.6.9 Applicability of requirements for
scheduling availability 813.6.10 Applicability of requirements for
measurement restrictions 814 SA: RRC\_IDLE state mobility 814.1 Cell
Selection 814.2 Cell Re-selection 814.2.1 Introduction 814.2.2
Requirements 824.2.2.1 UE measurement capability 824.2.2.2 Measurement
and evaluation of serving cell 824.2.2.3 Measurements of intra-frequency
NR cells 834.2.2.4 Measurements of inter-frequency NR cells 844.2.2.5
Measurements of inter-RAT E-UTRAN cells 864.2.2.6 Maximum interruption
in paging reception 884.2.2.7 General requirements 884.2.2.8 Minimum
requirement at transitions 884.2.2.9 Measurements of intra-frequency NR
cells for UE configured with relaxed measurement criterion 894.2.2.9.1
Introduction 894.2.2.9.2 Measurements for UE fulfilling low mobility
criterion 894.2.2.9.3 Measurements for UE fulfilling not-at-cell edge
criterion 904.2.2.9.4 Measurements for UE fulfilling low mobility and
not-at-cell edge criteria 914.2.2.10 Measurements of inter-frequency NR
cells for UE configured with relaxed measurement criterion 914.2.2.10.1
Introduction 914.2.2.10.2 Measurements for UE fulfilling low mobility
criterion 914.2.2.10.3 Measurements for UE fulfilling not-at-cell edge
criterion 924.2.2.10.4 Measurements for UE fulfilling low mobility and
not-at-cell edge criterion 934.2.2.11 Measurements of inter-RAT E-UTRAN
cells for UE configured with relaxed measurement criterion 944.2.2.11.1
Introduction 944.2.2.11.2 Measurements for UE fulfilling low mobility
criterion 944.2.2.11.3 Measurements for UE fulfilling with not-at-cell
edge criterion 954.2.2.11.4 Measurements for UE fulfilling low mobility
and not-at-cell edge criterion 964.2A Cell Re-selection when subject to
CCA 964.2A.1 Introduction 964.2A.2 Requirements 974.2A.2.1 UE
measurement capability 974.2A.2.2 Measurement and evaluation when
subject to CCA on the serving cell 974.2A.2.3 Measurements of
intra-frequency NR cells when subject to CCA on the serving cell and
target cell 984.2A.2.4 Measurements of inter-frequency NR cells when
subject to CCA on the target cell 994.2A.2.5 Measurements of inter-RAT
E-UTRAN cells when subject to CCA on the serving cell 1014.2A.2.6
Maximum interruption in paging reception when subject to CCA on the
target cell 1014.2A.2.7 General requirements 1014.3 Minimization of
Drive Tests (MDT) 1024.3.1 Introduction 1024.3.2 Measurement
Requirements 1024.3.3 Requirements for Relative Time Stamp Accuracy
1024.3.4 Requirements for Relative Time Stamp Accuracy for RRC
Connection Establishment Failure Log Reporting 1034.3.5 Requirements for
Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure
Log Reporting 1034.4 Idle Mode CA/DC Measurements 1034.4.1 Introduction
1034.4.2 Measurement Requirements 1034.4.2.1 Detected cell requirement
during state transition and Idle mode 1034.4.2.2 Measurements of
inter-frequency CA/DC candidate cells 1044.4.2.3 Measurements on serving
cell 1054.4.2.4 Measurements of E-UTRAN inter-RAT DC candidate cells
1055 SA: RRC\_INACTIVE state mobility 1075.1 Cell Re-selection 1075.1.1
Introduction 1075.1.2 Requirements 1075.1.2.1 UE measurement capability
1075.1.2.2 Measurement and evaluation of serving cell 1075.1.2.3
Measurements of intra-frequency NR cells 1075.1.2.4 Measurements of
inter-frequency NR cells 1075.1.2.5 Measurements of inter-RAT E-UTRAN
cells 1075.1.2.6 Maximum interruption in paging reception 1075.1.2.7
General requirements 1075.1A Cell Re-selection with CCA 1075.1A.1
Introduction 1075.1A.2 Requirements 1085.1A.2.1 UE measurement
capability 1085.1A.2.2 Measurement and evaluation when CCA is used on
the serving cell 1085.1A.2.3 Measurements of intra-frequency NR cells
when CCA is used on the serving cell and target cell 1085.1A.2.4
Measurements of inter-frequency NR cells when CCA is used on the target
cell 1085.1A.2.5 Measurements of inter-RAT E-UTRAN cells when CCA is
used on the serving cell 1085.1A.2.6 Maximum interruption in paging
reception when CCA is used on the target cell 1085.1A.2.7 General
requirements 1085.2 Void 1085.3 Minimization of Drive Tests (MDT)
1085.3.1 Introduction 1085.3.2 Measurement Requirements 1095.3.3
Requirements for Relative Time Stamp Accuracy 1095.3.4 Requirements for
Relative Time Stamp Accuracy for RRC Connection Establishment Failure
Log Reporting 1095.3.5 Requirements for Relative Time Stamp Accuracy for
Radio Link Failure and Handover Failure Log Reporting 1095.3.6
Requirements for Relative Time Stamp Accuracy for RRC Resume Failure Log
Reporting 1095.4 Inactive Mode CA/DC Measurements 1095.4.1 Introduction
1095.4.2 Measurement Requirements 1095.4.2.1 Detected cell requirement
during state transition and inactive mode 1105.4.2.2 Measurements of
inter-frequency CA/DC candidate cells 1105.4.2.3 Measurements on serving
cell 1105.4.2.4 Measurements on E-UTRAN inter-RAT DC candidate cells
1106 RRC\_CONNECTED state mobility 1106.1 Handover 1106.1.1 NR Handover
1106.1.1.1 Introduction 1106.1.1.2 NR FR1 - NR FR1 Handover 1106.1.1.2.1
Handover delay 1106.1.1.2.2 Interruption time 1106.1.1.3 NR FR2- NR FR1
Handover 1116.1.1.3.1 Handover delay 1116.1.1.3.2 Interruption time
1116.1.1.4 NR FR2- NR FR2 Handover 1126.1.1.4.1 Handover delay
1126.1.1.4.2 Interruption time 1126.1.1.5 NR FR1- NR FR2 Handover
1136.1.1.5.1 Handover delay 1136.1.1.5.2 Interruption time 1136.1.2 NR
Handover to other RATs 1146.1.2.1 NR -- E-UTRAN Handover 1146.1.2.1.1
Introduction 1146.1.2.1.2 Handover delay 1146.1.2.1.3 Interruption time
1146.1.2.2 NR -- UTRAN Handover 1156.1.2.2.1 Introduction 1156.1.2.2.2
Handover delay 1156.1.2.2.3 Interruption time 1156.1.3 NR DAPS Handover
1166.1.3.1 Introduction 1166.1.3.2 NR FR1 - NR FR1 DAPS Handover
1166.1.3.2.1 DAPS handover delay 1166.1.3.2.2 Interruption time
1176.1.3.3 NR FR2- NR FR1 DAPS Handover 1196.1.3.3.1 DAPS handover delay
1196.1.3.3.2 Interruption time 1196.1.3.4 NR FR1- NR FR2 DAPS Handover
1206.1.3.4.1 DAPS handover delay 1206.1.3.4.2 Interruption time 1206.1.4
NR Conditional Handover 1216.1.4.1 Introduction 1216.1.4.2 NR FR1 -- NR
FR1 conditional handover 1216.1.4.3 NR FR2 -- NR FR1 conditional
handover 1226.1.4.4 NR FR2 -- NR FR2 conditional handover 1236.1.4.4.1
Handover delay 1236.1.4.4.2 Measurement time 1236.1.4.4.3 Preparation
time 1236.1.4.4.4 Interruption time 1236.1.4.5 NR FR1 -- NR FR2
conditional handover 1246.1A Void 1246.1A.1 Void 1246.1A.1.1 Void
1246.1A.1.2 Void 1246.1A.1.2.1 Void 1246.1A.1.2.2 Void 1246.1B Handover
to target cell using CCA 1246.1B.1 NR Handover 1246.1B.1.1 Introduction
1246.1B.1.2 NR FR1 - NR FR1 Handover 1256.1B.1.2.1 Handover delay
1256.1B.1.2.2 Interruption time 1256.2 RRC Connection Mobility Control
1266.2.1 SA: RRC Re-establishment 1266.2.1.1 Introduction 1266.2.1.2
Requirements 1266.2.1.2.1 UE Re-establishment delay requirement
1266.2.1A RRC Re-establishment with CCA 1276.2.1A.1 Introduction
1276.2.1A.2 Requirements 1286.2.1A.2.1 UE Re-establishment with CCA
delay requirement 1286.2.2 Random access 1306.2.2.1 Introduction
1306.2.2.2 Requirements for 4-step RA type 1306.2.2.2.1 Contention based
random access 1306.2.2.2.2 Non-Contention based random access
1316.2.2.2.3 UE behaviour when configured with supplementary UL
1326.2.2.3 Requirements for 2-step RA type 1326.2.2.3.1 Contention based
random access 1326.2.2.3.2 Non-Contention based random access
1336.2.2.3.3 UE behaviour when configured with supplementary UL
1346.2.2A Random access when CCA is used on target frequency 1346.2.2A.1
Introduction 1346.2.2A.2 Requirements for 4-step RA type 1346.2.2A.2.1
Contention based random access 1346.2.2A.2.2 Non-Contention based random
access 1356.2.2A.3 Requirements for 2-step RA type 1366.2.2A.3.1
Contention based random access 1376.2.2A.3.2 Non-Contention based random
access 1386.2.3 SA: RRC Connection Release with Redirection 1396.2.3.1
Introduction 1396.2.3.2 Requirements 1396.2.3.2.1 RRC connection release
with redirection to NR 1396.2.3.2.2 RRC connection release with
redirection to E-UTRAN 1406.2.3.2.3 RRC connection release with
redirection to NR carrier subject to CCA 1407 Timing 1417.1 UE transmit
timing 1417.1.1 Introduction 1417.1.2 Requirements 1427.1.2.1 Gradual
timing adjustment 1437.1.2.2 Void 1437.2 UE timer accuracy 1437.2.1
Introduction 1437.2.2 Requirements 1447.3 Timing advance 1447.3.1
Introduction 1447.3.2 Requirements 1447.3.2.1 Timing Advance adjustment
delay 1447.3.2.2 Timing Advance adjustment accuracy 1447.4 Cell phase
synchronization accuracy 1447.4.1 Definition 1447.4.2 Minimum
requirements 1447.5 Maximum Transmission Timing Difference 1457.5.1
Introduction 1457.5.2 Minimum Requirements for inter-band EN-DC
1457.5.2.1 Minimum Requirements for inter-band synchronous EN-DC
1457.5.3 Minimum Requirements for intra-band EN-DC 1467.5.4 Minimum
Requirements for NR Carrier Aggregation 1467.5.5 Minimum Requirements
for inter-band NE-DC 1477.5.5.1 Minimum Requirements for inter-band
synchronous NE-DC 1477.5.6 Minimum Requirements for inter-band NR DC
1487.6 Maximum Receive Timing Difference 1487.6.1 Introduction 1487.6.2
Minimum Requirements for inter-band EN-DC 1497.6.2.1 Minimum
Requirements for inter-band synchronous EN-DC 1497.6.3 Minimum
Requirements for intra-band EN-DC 1497.6.4 Minimum Requirements for NR
Carrier Aggregation 1507.6.5 Minimum Requirements for inter-band NE-DC
1517.6.5.1 Minimum Requirements for inter-band synchronous NE-DC
1517.6.6 Minimum Requirements for inter-band NR DC 1517.7
*deriveSSB-IndexFromCell* tolerance 1527.7.1 Minimum requirements 1527.8
Void 1528 Signalling characteristics 1528.1 Radio Link Monitoring
1528.1.1 Introduction 1528.1.2 Requirements for SSB based radio link
monitoring 1538.1.2.1 Introduction 1538.1.2.2 Minimum requirement
1548.1.2.3 Measurement restrictions for SSB based RLM 1568.1.3
Requirements for CSI-RS based radio link monitoring 1568.1.3.1
Introduction 1568.1.3.2 Minimum requirement 1578.1.3.3 Measurement
restrictions for CSI-RS based RLM 1598.1.4 Minimum requirement at
transitions 1608.1.5 Minimum requirement for UE turning off the
transmitter 1608.1.6 Minimum requirement for L1 indication 1608.1.7
Scheduling availability of UE during radio link monitoring 1618.1.7.1
Scheduling availability of UE performing radio link monitoring with a
same subcarrier spacing as PDSCH/PDCCH on FR1 1618.1.7.2 Scheduling
availability of UE performing radio link monitoring with a different
subcarrier spacing than PDSCH/PDCCH on FR1 1618.1.7.3 Scheduling
availability of UE performing radio link monitoring on FR2 1618.1.7.4
Scheduling availability of UE performing radio link monitoring on FR1 or
FR2 in case of FR1-FR2 inter-band CA and NR-DC 1628.1A Radio Link
Monitoring with CCA on Target Frequency 1628.1A.1 Introduction 1628.1A.2
Requirements for SSB Based Radio Link Monitoring 1638.1A.2.1
Introduction 1638.1A.2.2 Minimum Requirement 1648.1A.3 Minimum
requirement at transitions 1658.1A.4 Minimum requirement for UE turning
off the transmitter 1668.1A.5 Minimum requirement for L1 indication
1668.1A.6 Scheduling availability of UE during radio link monitoring
1668.1A.6.1 Scheduling availability of UE performing radio link
monitoring with the same subcarrier spacing as PDSCH/PDCCH 1668.1A.6.2
Scheduling availability of UE performing radio link monitoring with a
different subcarrier spacing than PDSCH/PDCCH 1668.2 Interruption
1678.2.1 EN-DC Interruption 1678.2.1.1 Introduction 1678.2.1.2
Requirements 1678.2.1.2.1 Interruptions at transitions between active
and non-active during DRX 1678.2.1.2.2 Interruptions at transitions from
non-DRX to DRX 1688.2.1.2.3 Interruptions at SCell addition/release
1688.2.1.2.4 Interruptions at SCell activation/deactivation 1698.2.1.2.5
Interruptions during measurements on SCC 1708.2.1.2.6 Interruptions at
UL carrier RRC reconfiguration 1728.2.1.2.7 Interruptions due to Active
BWP switching Requirement 1728.2.1.2.8 Interruptions at direct SCell
activation and hibernation 1738.2.1.2.9 Interruptions at SCell
hibernation 1748.2.1.2.10 Interruptions at SCell activation/deactivation
with multiple downlink SCells 1748.2.1.2.11 Interruptions due to
UE-specific CBW change 1748.2.1.2.12 Interruptions at NR SRS carrier
based switching 1758.2.1.2.13 Interruptions at E-UTRA SRS carrier based
switching 1768.2.1.2.14 DL Interruptions at switching between two uplink
carriers 1778.2.1.2.15 Interruptions due to SCell dormancy 1778.2.1.2.16
Interruptions when identifying CGI of an NR cell with autonomous gaps
1788.2.1.2.17 Interruptions when identifying CGI of an E-UTRA cell with
autonomous gaps 1788.2.2 SA: Interruptions with Standalone NR Carrier
Aggregation 1798.2.2.1 Introduction 1798.2.2.2 Requirements 1808.2.2.2.1
Interruptions at SCell addition/release 1808.2.2.2.2 Interruptions at
SCell activation/deactivation 1818.2.2.2.3 Interruptions during
measurements on deactivated SCC 1828.2.2.2.4 Interruptions at UL carrier
RRC reconfiguration 1828.2.2.2.5 Interruptions due to Active BWP
switching Requirement 1838.2.2.2.6 Interruptions at inter-frequency SFTD
measurement 1848.2.2.2.7 Interruptions at SCell activation/deactivation
with multiple downlink SCells 1858.2.2.2.8 Interruptions due to
UE-specific CBW change 1858.2.2.2.9 Interruptions at NR SRS carrier
based switching 1858.2.2.2.10 DL Interruptions at UE switching between
two uplink carriers 1878.2.2.2.11 Interruptions at direct SCell
activation 1878.2.2.2.12 Interruptions due to SCell dormancy
1888.2.2.2.13 Interruptions at transitions between active and non-active
during DRX 1888.2.2.2.14 Interruptions when identifying CGI of an NR
cell with autonomous gaps 1888.2.2.2.15 Interruptions when identifying
CGI of an E-UTRA cell with autonomous gaps 1898.2.3 NE-DC Interruptions
1898.2.3.1 Introduction 1898.2.3.2 Requirements 1908.2.3.2.1
Interruptions at transitions between active and non-active during DRX
1908.2.3.2.2 Interruptions at transitions from non-DRX to DRX
1908.2.3.2.3 Interruptions at PSCell/SCell addition/release 1908.2.3.2.4
Interruptions at SCell activation/deactivation 1928.2.3.2.5
Interruptions during measurements on SCC 1938.2.3.2.6 Interruptions at
UL carrier RRC reconfiguration 1948.2.3.2.7 Interruptions due to Active
BWP switching Requirement 1948.2.3.2.8 Interruptions at direct SCell
activation and hibernation 1958.2.3.2.9 Interruptions at SCell
hibernation 1958.2.3.2.10 Interruptions at SCell activation/deactivation
with multiple downlink SCells 1958.2.3.2.11 Interruptions at NR SRS
carrier based switching 1958.2.3.2.12 Interruptions at E-UTRA SRS
carrier based switching 1978.2.3.2.13 Interruptions due to SCell
dormancy 1988.2.3.2.14 Interruptions when identifying CGI of an NR cell
with autonomous gaps 1988.2.3.2.15 Interruptions when identifying CGI of
an E-UTRA cell with autonomous gaps 1998.2.3.2.16 Interruptions due to
UE-specific CBW change 1998.2.4 NR-DC: Interruptions 2008.2.4.1
Introduction 2008.2.4.2 Requirements 2008.2.4.2.1 Interruptions at
PSCell/SCell addition/release 2008.2.4.2.3 Interruptions during
measurements on SCC 2028.2.4.2.4 Interruptions at UL carrier RRC
reconfiguration 2028.2.4.2.5 Interruptions due to Active BWP switching
Requirement 2038.2.4.2.6 Interruptions at transitions between active and
non-active during DRX 2038.2.4.2.7 Interruptions at transitions from
non-DRX to DRX 2038.2.4.2.8 Interruptions at SCell
activation/deactivation with multiple downlink SCells 2038.2.4.2.9
Interruptions at NR SRS carrier based switching 2048.2.4.2.10
Interruptions at direct SCell activation 2058.2.4.2.11 Interruptions
when identifying CGI of an NR cell with autonomous gaps 2058.2.4.2.12
Interruptions when identifying CGI of an E-UTRA cell with autonomous
gaps 2068.2.4.2.13 Interruptions due to SCell dormancy 2078.2.4.2.14
Interruptions due to UE-specific CBW change 2078.2.4.2A Void
2078.2.4.2A.1 Void 2078.2.4.2A.2 Void 2078.2.4.2A.3 Void 2078.3 SCell
Activation and Deactivation Delay 2078.3.1 Introduction 2078.3.2 SCell
Activation Delay Requirement for Deactivated SCell 2088.3.3 SCell
Deactivation Delay Requirement for Activated SCell 2128.3.4 Direct SCell
Activation at SCell addition 2128.3.5 Direct SCell Activation at
Handover 2148.3.7 SCell Activation Delay Requirement for Deactivated
SCell with Multiple Downlink SCells 2168.3.8 SCell Deactivation Delay
Requirement for Activated SCell with Multiple Downlink SCells 2198.3.9
Direct SCell Activation of Multiple Downlink SCells at SCell addition
2208.3.10 Direct SCell Activation of Multiple Downlink SCells at
Handover 2218.3A SCell Activation and Deactivation Delay in Carriers
with CCA 2228.3A.1 Introduction 2228.3A.2 SCell Activation Delay
Requirement for Deactivated SCell 2238.3A.3 SCell Deactivation Delay
Requirement for Activated SCell 2258.4 UE UL carrier RRC reconfiguration
delay 2268.4.1 Introduction 2268.4.2 UE UL carrier configuration delay
requirement 2268.4.3 UE UL carrier deconfiguration delay requirement
2268.5 Link Recovery Procedures 2268.5.1 Introduction 2268.5.2
Requirements for SSB based beam failure detection 2278.5.2.1
Introduction 2278.5.2.2 Minimum requirement 2288.5.2.3 Measurement
restriction for SSB based beam failure detection 2298.5.3 Requirements
for CSI-RS based beam failure detection 2308.5.3.1 Introduction
2308.5.3.2 Minimum requirement 2308.5.3.3 Measurement restrictions for
CSI-RS beam failure detection 2328.5.4 Minimum requirement for L1
indication 2338.5.5 Requirements for SSB based candidate beam detection
2348.5.5.1 Introduction 2348.5.5.2 Minimum requirement 2348.5.5.3
Measurement restriction for SSB based candidate beam detection 2368.5.6
Requirements for CSI-RS based candidate beam detection 2368.5.6.1
Introduction 2368.5.6.2 Minimum requirement 2368.5.6.3 Measurement
restriction for CSI-RS based candidate beam detection 2398.5.7
Scheduling availability of UE during beam failure detection 2398.5.7.1
Scheduling availability of UE performing beam failure detection with a
same subcarrier spacing as PDSCH/PDCCH on FR1 2398.5.7.2 Scheduling
availability of UE performing beam failure detection with a different
subcarrier spacing than PDSCH/PDCCH on FR1 2398.5.7.3 Scheduling
availability of UE performing beam failure detection on FR2 2408.5.7.4
Scheduling availability of UE performing beam failure detection on FR1
or FR2 in case of FR1-FR2 inter-band CA and NR DC 2408.5.8 Scheduling
availability of UE during candidate beam detection 2408.5.8.1 Scheduling
availability of UE performing L1-RSRP measurement with a same subcarrier
spacing as PDSCH/PDCCH on FR1 2408.5.8.2 Scheduling availability of UE
performing L1-RSRP measurement with a different subcarrier spacing than
PDSCH/PDCCH on FR1 2418.5.8.3 Scheduling availability of UE performing
L1-RSRP measurement on FR2 2418.5.8.4 Scheduling availability of UE
performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2
inter-band CA and NR-DC 2418.5.9 Requirements for Beam Failure Recovery
in SCell 2428.5.9.1 Introduction 2428.5.9.2 Requirement 2428.5.10
Minimum requirement at transitions for beam failure detection 2428.5A
Link Recovery Procedures when CCA is used on target frequency 2438.5A.1
Introduction 2438.5A.2 Requirements for SSB based beam failure detection
2438.5A.2.1 Introduction 2438.5A.2.2 Minimum requirement 2448.5A.2.3
Measurement restriction for SSB based beam failure detection 2448.5A.4
Minimum requirement for L1 indication 2458.5A.5 Requirements for SSB
based candidate beam detection 2458.5A.5.1 Introduction 2458.5A.5.2
Minimum requirement 2458.5A.5.3 Measurement restriction for SSB based
candidate beam detection 2468.5A.7 Scheduling availability of UE during
beam failure detection 2468.5A.7.1 Scheduling availability of UE
performing beam failure detection with a same subcarrier spacing as
PDSCH/PDCCH 2468.5A.7.2 Scheduling availability of UE performing beam
failure detection with a different subcarrier spacing than PDSCH/PDCCH
2468.5A.8 Scheduling availability of UE during candidate beam detection
2468.5A.8.1 Scheduling availability of UE performing L1-RSRP measurement
with a same subcarrier spacing as PDSCH/PDCCH 2478.5A.8.2 Scheduling
availability of UE performing L1-RSRP measurement with a different
subcarrier spacing than PDSCH/PDCCH 2478.6 Active BWP switch delay
2478.6.1 Introduction 2478.6.2 DCI and timer based BWP switch delay on a
single CC 2478.6.2A DCI based BWP switch delay on multiple CCs
2488.6.2A.1 Simultaneous DCI based BWP switch delay on multiple CCs
2488.6.2A.2 Non-simultaneous DCI based BWP switch delay on multiple CCs
2508.6.2B Timer based BWP switch delay on multiple CCs 2508.6.2B.1
Simultaneous timer based BWP switch delay on multiple CCs 2508.6.2B.2
Non-simultaneous timer based BWP switch delay on multiple CCs 2518.6.3
RRC based BWP switch delay on a single CC 2518.6.3A RRC based BWP switch
delay on multiple CCs 2528.6.3A.1 Simultaneous RRC based BWP switch
delay on multiple CCs 2528.6.3A.2 Non-simultaneous RRC based BWP switch
delay on multiple CCs 2528.6.4 BWP switch delay on Consistent UL CCA
recovery 2538.7 Void 2538.8 NE-DC: E-UTRAN PSCell Addition and Release
Delay 2538.8.1 Introduction 2538.8.2 E-UTRAN PSCell Addition Delay
Requirement 2538.8.3 E-UTRAN PSCell Release Delay Requirement 2548.9
NR-DC: PSCell Addition and Release Delay 2548.9.1 Introduction 2548.9.2
PSCell Addition Delay Requirement 2548.9.3 PSCell Release Delay
Requirement 2558.10 Active TCI state switching delay 2558.10.4 DCI based
TCI state switch delay 2578.10.5 RRC based TCI state switch delay
2578.10.6 Active TCI state list update delay 2578.10A Active TCI state
switching delay with CCA 2588.10A.1 Introduction 2588.10A.2 Known
conditions for TCI state 2588.10A.3 MAC-CE based TCI state switch delay
2588.10A.4 DCI based TCI state switch delay 2598.10A.5 RRC based TCI
state switch delay 2598.10A.6 Active TCI state list update delay 2608.11
PSCell Change 2608.11A void 2618.11B Conditional PSCell Change
2618.11B.1 Introduction 2618.11B.2 Conditoinal PSCell Change delay
2618.11B.2.1 Measurement time 2618.12 Uplink spatial relation switch
delay 2628.12.1 Introduction 2628.12.2 Known conditions for spatial
relation when associated with DL-RS 2628.12.3 MAC-CE based spatial
relation switch delay 2628.12.4 DCI based spatial relation switch delay
2638.12.5 RRC based spatial relation switch delay 2638.13 UE-specific
CBW change 2648.13.1 Introduction 2648.13.2 UE-specific CBW change delay
2648.14 Pathloss reference signal switching delay 2648.14.1 Introduction
2648.14.2 Known conditions for pathloss reference signal 2648.14.3
MAC-CE based pathloss reference signal switch delay 2659 Measurement
Procedure 2669.1 General measurement requirement 2669.1.1 Introduction
2669.1.2 Measurement gap 2669.1.2.1 EN-DC: Measurement Gap Sharing
2779.1.2.1a SA: Measurement Gap Sharing 2779.1.2.1b NE-DC: Measurement
Gap Sharing 2789.1.2.1c NR-DC: Measurement Gap Sharing 2799.1.3 UE
Measurement capability 2809.1.3.1 EN-DC: Monitoring of multiple layers
using gaps 2809.1.3.1a SA: Monitoring of multiple layers using gaps
2809.1.3.1b NE-DC: Monitoring of multiple layers using gaps 2819.1.3.1c
NR-DC: Monitoring of multiple layers using gaps 2819.1.3.2 EN-DC:
Maximum allowed layers for multiple monitoring 2829.1.3.2a SA: Maximum
allowed layers for multiple monitoring 2839.1.3.2b NE-DC: Maximum
allowed layers for multiple monitoring 2839.1.3.2c NR-DC: Maximum
allowed layers for multiple monitoring 2849.1A.3.2 Void 2859.1.3A UE
Measurement capability under operation mode with CCA 2859.1.3A.1 EN-DC:
Monitoring of multiple layers using gaps under CCA 2859.1.3A.1A SA:
Monitoring of multiple layers using gaps under CCA 2859.1.3A.2 EN-DC:
Maximum allowed layers for multiple monitoring under CCA 2859.1A.3.2a
Void 2869.1.3A.2A SA: Maximum allowed layers for multiple monitoring
under CCA 2869.1.4 Capabilities for Support of Event Triggering and
Reporting Criteria 2869.1.4.1 Introduction 2869.1.4.2 Requirements
2869.1.5 Carrier-specific scaling factor 2909.1.5.1 Monitoring of
multiple layers outside gaps 2909.1.5.1.1 EN-DC mode: carrier-specific
scaling factor for SSB-based, CSI-RS based L3 measurements and RSSI and
channel occupancy measurements performed outside gaps 2929.1.5.1.2 SA
mode: carrier-specific scaling factor for SSB-based, CSI-RS based L3
measurements and RSSI and channel occupancy measurements performed
outside gaps 2939.1.5.1.3 NR-DC mode: carrier-specific scaling factor
for SSB-based and CSI-RS based L3 measurements performed outside gaps
2949.1.5.1.4 NE-DC mode: carrier-specific scaling factor for SSB-based
and CSI-RS based measurements performed outside gaps 2959.1.5.2
Monitoring of multiple layers within gaps 2969.1.5.2.1 EN-DC mode:
carrier-specific scaling factor for SSB, CSI-RS-based L3 measurements
and RSSI and channel occupancy measurements performed within gaps
2979.1.5.2.2 SA mode: carrier-specific scaling factor for SSB,
CSI-RS-based L3 measurements and RSSI and channel occupancy measurements
performed within gaps 2999.1.5.2.3 NE-DC: carrier-specific scaling
factor for SSB-based and CSI-RS based L3 measurements performed within
gaps 3019.1.5.2.4 NR-DC: carrier-specific scaling factor for SSB-based
and CSI-RS-based L3 measurements performed within gaps 3039.1.5.2.5 SA
mode: carrier-specific scaling factor for PRS-based measurements
performed within gaps 3049.1.5.2.6 NE-DC: carrier-specific scaling
factor for PRS-based measurements performed within gaps 3059.1.5.2.7
NR-DC: carrier-specific scaling factor for PRS-based measurements
performed within gaps 3059.1.6 Minimum requirement at transitions 3059.2
NR intra-frequency measurements 3059.2.1 Introduction 3059.2.2
Requirements applicability 3069.2.3 Number of cells and number of SSB
3069.2.3.1 Requirements for FR1 3069.2.3.2 Requirements for FR2 3069.2.4
Measurement Reporting Requirements 3079.2.4.1 Periodic Reporting
3079.2.4.2 Event-triggered Periodic Reporting 3079.2.4.3 Event Triggered
Reporting 3079.2.5 Intrafrequency measurements without measurement gaps
3089.2.5.1 Intrafrequency cell identification 3089.2.5.2 Measurement
period 3109.2.5.3 Scheduling availability of UE during intra-frequency
measurements 3129.2.5.3.1 Scheduling availability of UE performing
measurements in TDD bands on FR1 3129.2.5.3.2 Scheduling availability of
UE performing measurements with a different subcarrier spacing than
PDSCH/PDCCH on FR1 3129.2.5.3.3 Scheduling availability of UE performing
measurements on FR2 3139.2.5.3.4 Scheduling availability of UE
performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA
3149.2.5.4 SFTD Measurements between PCell and PSCell 3149.2.5.4.1
Introduction 3149.2.5.4.2 SFTD Measurement delay 3149.2.5.4.3 SFTD
Measurement Reporting Delay 3159.2.6 Intra-frequency measurements with
measurement gaps 3159.2.6.1 Void 3159.2.6.2 Intra-frequency cell
identification 3159.2.6.3 Intrafrequency Measurement Period 3179.2A NR
intra-frequency measurements with CCA 3189.2A.1 Introduction 3189.2A.2
Requirements applicability 3189.2A.3 Number of cells and number of SSB
3199.2A.4 Measurement Reporting Requirements 3199.2A.5 Intra-frequency
measurements without measurement gaps 3199.2A.5.2 Measurement period
3229.2A.5.3 Scheduling availability of UE during intra-frequency
measurements 3239.2A.5.3.1 Scheduling availability of UE performing
measurements in TDD bands 3239.2A.5.3.2 Scheduling availability of UE
performing measurements with a different subcarrier spacing than
PDSCH/PDCCH 3239.2A.6 Intra-frequency measurements with measurement gaps
3249.2A.6.1 Intra-frequency cell identification 3249.2A.6.2
Intra-frequency Measurement Period 3259.2A.7 Intra-frequency RSSI and
Channel occupancy measurements 3269.2A.7.1 Intra-frequency RSSI
measurements 3269.2A.7.2 Intra-frequency Channel occupancy measurements
3279.2A.7.3 Scheduling restriction during RSSI and Channel Occupancy
measurements 3279.3 NR inter-frequency measurements 3289.3.1
Introduction 3289.3.2 Requirements applicability 3289.3.2.1 Void
3299.3.2.2 Void 3299.3.3 Number of cells and number of SSB 3299.3.3.1
Requirements for FR1 3299.3.3.2 Requirements for FR2 3299.3.4
Inter-frequency measurement with measurement gaps 3299.3.4.1 Void
3309.3.4.2 Void 3309.3.5 Inter-frequency measurements 3309.3.5.1 Void
3319.3.5.2 Void 3319.3.5.3 Void 3319.3.6 Inter-frequency measurements
reporting requirements 3319.3.6.1 Periodic Reporting 3319.3.6.2
Event-triggered Periodic Reporting 3319.3.6.3 Event-triggered Reporting
3319.3.7 Void 3329.3.8 Inter-frequency SFTD measurement requirements
3329.3.8.1 Introduction 3329.3.8.2 SFTD Measurement delay 3329.3.8.3
SFTD Measurement reporting delay 3339.3.9 Inter frequency measurements
without measurement gaps 3339.3.9.1 Inter frequency Cell identification
3339.3.9.2 Measurement period 3359.3.9.3 Scheduling availability of UE
during inter-frequency measurements 3369.3.9.3.1 Scheduling availability
of UE performing measurements in TDD bands on FR1 3369.3.9.3.2
Scheduling availability of UE performing measurements with a different
subcarrier spacing than PDSCH/PDCCH on FR1 3369.3.9.3.3 Scheduling
availability of UE performing measurements on FR2 3379.3.9.3.4
Scheduling availability of UE performing measurements on FR1 or FR2 in
case of FR1-FR2 inter-band CA 3379.3A NR inter-frequency measurements in
carrier frequencies with CCA 3379.3A.1 Introduction 3379.3A.2
Requirements applicability 3389.3A.3 Number of cells and number of SSB
3389.3A.3.1 Requirements 3389.3A.4 Inter-frequency cell identification
3389.3A.5 Inter-frequency measurements 3409.3A.6 NR Inter-frequency
measurements reporting requirements 3409.3A.6.1 Periodic Reporting
3409.3A.6.2 Event-triggered Periodic Reporting 3409.3A.6.3
Event-triggered Reporting 3409.3A.8 Inter-frequency RSSI measurements
3419.3A.9 Inter-frequency channel occupancy measurements 3419.4
Inter-RAT measurements 3429.4.1 Introduction 3429.4.2 NR − E-UTRAN FDD
measurements 3439.4.2.1 Introduction 3439.4.2.2 Requirements when no DRX
is used 3449.4.2.3 Requirements when DRX is used 3449.4.2.4 Measurement
reporting requirements 3459.4.2.4.1 Periodic Reporting 3459.4.2.4.2
Event-Triggered Periodic Reporting 3469.4.2.4.3 Event-Triggered
Reporting 3469.4.3 NR − E-UTRAN TDD measurements 3469.4.3.1 Introduction
3469.4.3.2 Requirements when no DRX is used 3469.4.3.3 Requirements when
DRX is used 3479.4.3.4 Measurement reporting requirements 3499.4.3.4.1
Periodic Reporting 3499.4.3.4.2 Event-Triggered Periodic Reporting
3499.4.3.4.3 Event-Triggered Reporting 3499.4.4 Inter-RAT RSTD
measurements 3499.4.4.1 NR − E-UTRAN FDD RSTD measurements 3499.4.4.1.1
Introduction 3499.4.4.1.2 Requirements 3509.4.4.2 NR − E-UTRAN TDD RSTD
measurements 3539.4.4.2.1 Introduction 3539.4.4.2.2 Requirements
3549.4.5 Inter-RAT E-CID measurements 3579.4.5.1 NR−E-UTRAN FDD E-CID
RSRP and RSRQ measurements 3579.4.5.1.1 Introduction 3579.4.5.1.2
Requirements 3579.4.5.1.3 Measurement Reporting Delay 3579.4.5.2
NR−E-UTRAN TDD E-CID RSRP and RSRQ measurements 3579.4.5.2.1
Introduction 3579.4.5.2.2 Requirements 3579.4.5.2.3 Measurement
Reporting Delay 3589.4.6 NR − UTRAN FDD measurements 3589.4.6.1
Introduction 3589.4.6.2 Requirements when no DRX is used 3589.4.6.3
Requirements when DRX is used 3599.4.7 NR -- E-UTRAN measurements with
autonomous gaps 3619.4.7.1 CGI identification of an E-UTRA cell with
autonomous gaps 3619.4.7.2 CGI reporting delay 3619.5 L1-RSRP
measurements for Reporting 3629.5.1 Introduction 3629.5.2 Requirements
applicability 3629.5.3 Measurement Reporting Requirements 3629.5.3.1
Periodic Reporting 3639.5.3.2 Semi-Persistent Reporting 3639.5.3.3
Aperiodic Reporting 3639.5.4 L1-RSRP measurement requirements 3639.5.4.1
SSB based L1-RSRP Reporting 3639.5.4.2 CSI-RS based L1-RSRP Reporting
3659.5.4A Void 3689.5.4A.1 Void 3689.5.5 Measurement restriction for
CSI-RS and SSB for L1-RSRP measurement 3689.5.5.1 Measurement
restriction for SSB based L1-RSRP 3689.5.5.2 Measurement restriction for
CSI-RS based L1-RSRP 3689.5.6 Scheduling availability of UE during
L1-RSRP measurement 3699.5.6.1 Scheduling availability of UE performing
L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1
3699.5.6.2 Scheduling availability of UE performing L1-RSRP measurement
with a different subcarrier spacing than PDSCH/PDCCH on FR1 3699.5.6.3
Scheduling availability of UE performing L1-RSRP measurement on FR2
3709.5.6.4 Scheduling availability of UE performing L1-RSRP measurement
on FR1 or FR2 in case of FR1-FR2 inter-band CA 3709.5A L1-RSRP
measurements for Reporting under CCA 3719.5A.1 Introduction 3719.5A.2
Requirements applicability 3719.5A.3 Measurement Reporting Requirements
3719.5A.3.1 Periodic Reporting 3719.5A.3.2 Semi-Persistent Reporting
3729.5A.3.3 Aperiodic Reporting 3729.5A.4 L1-RSRP measurement
requirements 3729.5A.4.1 SSB based L1-RSRP Reporting 3729.5A.5
Measurement restriction for L1-RSRP measurement 3739.5A.5.1 Measurement
restriction for SSB based L1-RSRP 3739.5A.6 Scheduling availability of
UE during L1-RSRP measurement 3739.5A.6.1 Scheduling availability of UE
performing L1-RSRP measurement with a same subcarrier spacing as
PDSCH/PDCCH 3739.5A.6.2 Scheduling availability of UE performing L1-RSRP
measurement with a different subcarrier spacing than PDSCH/PDCCH
3749.5A.6.3 Scheduling availability of UE performing L1-RSRP measurement
in case of FR1-FR2 inter-band CA 3749.6 NE-DC: Measurements 3749.6.1
Introduction 3749.6.2 SFTD Measurements 3749.6.2.1 Introduction
3749.6.2.2 SFTD Measurement requirements 3749.7 Cross Link Interference
measurements 3759.7.1 Introduction 3759.7.2 SRS-RSRP measurements
3759.7.2.1 Introduction 3759.7.2.2 Requirements applicability 3759.7.2.3
Measurement Reporting Requirements 3769.7.2.3.1 Periodic Reporting
3769.7.2.3.2 Event-triggered Periodic Reporting 3769.7.2.3.3 Event
Triggered Reporting 3769.7.2.4 Measurement capability 3769.7.2.5
SRS-RSRP measurement period 3769.7.3 CLI-RSSI measurements 3779.7.3.1
Introduction 3779.7.3.2 Requirements applicability 3779.7.3.3
Measurement Reporting Requirements 3779.7.3.3.1 Periodic Reporting
3779.7.3.3.2 Event-triggered Periodic Reporting 3779.7.3.3.3 Event
Triggered Reporting 3779.7.3.4 Measurement capability 3789.7.3.5
CLI-RSSI measurement period 3789.7.4 Scheduling availability of UE
during CLI measurements 3789.7.4.1 Scheduling availability of UE
performing measurement on FR1 3789.7.4.2 Scheduling availability of UE
performing measurement on FR2 3789.8 L1-SINR measurements for Reporting
3799.8.1 Introduction 3799.8.2 Requirements applicability 3799.8.3
Measurement Reporting Requirements 3809.8.3.1 Periodic Reporting
3809.8.3.2 Semi-Persistent Reporting 3809.8.3.3 Aperiodic Reporting
3819.8.4 L1-SINR measurement requirements 3819.8.4.1 L1-SINR reporting
with CSI-RS based CMR and no dedicated IMR configured 3819.8.4.3 L1-SINR
reporting with CSI-RS based CMR and dedicated IMR configured 3849.8.5
Measurement restriction for L1-SINR measurement 3869.8.5.1 Measurement
restriction if SSB configured for L1-SINR Measurement 3869.8.5.2
Measurement restriction if CSI-RS configured for L1-SINR measurement
3879.8.5.3 Measurement restriction if CSI-IM configured for L1-SINR
measurement 3879.8.6 Scheduling availability of UE during L1-SINR
measurement 3889.8.6.1 Scheduling availability of UE performing L1-SINR
measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1
3889.8.6.2 Scheduling availability of UE performing L1-SINR measurement
with a different subcarrier spacing than PDSCH/PDCCH on FR1 3889.8.6.4
Scheduling availability of UE performing L1-SINR measurement on FR1 or
FR2 in case of FR1-FR2 inter-band CA 3899.9 NR measurements for
positioning 3899.9.1 Introduction 3899.9.2 RSTD measurements 3909.9.2.1
Introduction 3909.9.2.2 Requirements Applicability 3909.9.2.3
Measurement Capability 3909.9.2.4 Measurement Reporting Requirements
3909.9.2.4.1 Void 3909.9.2.4.2 Void 3909.9.2.4.3 Void 3909.9.2.5
Measurements Period Requirements 3909.9.2.6 Void 3929.9.3 PRS-RSRP
measurements 3929.9.3.1 Introduction 3929.9.3.2 Requirements
applicability 3929.9.3.3 Measurement Capability 3939.9.3.4 Measurement
Reporting Requirements 3939.9.3.5 Measurement Period Requirements
3939.9.4 UE Rx-Tx time difference measurements 3959.9.4.1 Introduction
3959.9.4.2 Requirements Applicability 3959.9.4.3 Measurement Capability
3959.9.4.4 Measurement Reporting Requirements 3959.9.4.5 Measurement
Period Requirements 3959.9.5 NR E-CID measurements 3989.9.5.1
Introduction 3989.9.5.2 Measurement Requirements 3989.9.5.2.1
Intra-frequency Measurement Requirements 3989.9.5.2.2 Inter-frequency
Measurement Requirements 3989.9.5.2.3 Measurement Reporting Delay
3999.10 CSI-RS based L3 measurements 3999.10.1 Introduction 3999.10.2
CSI-RS based intra-frequency measurements 3999.10.2.1 Introduction
3999.10.2.2 Requirements applicability 4009.10.2.3 Number of cells and
number of CSI-RS 4019.10.2.3.1 Requirements for FR1 4019.10.2.3.2
Requirements for FR2 4019.10.2.4 Measurement Reporting Requirements
4019.10.2.4.1 Periodic Reporting 4029.10.2.4.2 Event-triggered Periodic
Reporting 4029.10.2.4.3 Event Triggered Reporting 4029.10.2.5
Intra-frequency measurements without measurement gaps 4029.10.2.6
Scheduling availability of UE during CSI-RS based intra-frequency
measurements 4039.10.2.6.1 Scheduling availability of UE performing
CSI-RS based measurements in TDD bands 4039.10.2.6.2 Scheduling
availability of UE performing CSI-RS based measurements in FR2 4049.10.3
CSI-RS based Inter-frequency measurements 4049.10.3.1 Introduction
4049.10.3.2 Requirements applicability 4049.10.3.3 Number of cells and
number of CSI-RS resources 4059.10.3.3.1 Requirements for FR1
4059.10.3.3.2 Requirements for FR2 4059.10.3.4 Measurements reporting
requirements 4059.10.3.4.1 Periodic Reporting 4059.10.3.4.2
Event-triggered Periodic Reporting 4059.10.3.4.3 Event-triggered
Reporting 4069.10.3.5 Inter frequency measurements with measurement gaps
4069.11 NR measurements with autonomous gaps 4079.11.1 Introduction
4079.11.2 CGI identification of an NR cell with autonomous gaps
4079.11.3 CGI reporting delay 40810 Measurement Performance requirements
40810.1 NR measurements 40810.1.1 Introduction 40810.1.2 Intra-frequency
RSRP accuracy requirements for FR1 40910.1.2.1 Intra-frequency SS-RSRP
accuracy requirements 40910.1.2.1.1 Absolute SS-RSRP Accuracy
40910.1.2.1.2 Relative SS-RSRP Accuracy 41010.1.2.2 Void 41110.1.2.3
Intra-frequency CSI-RSRP accuracy requirements 41110.1.2.3.1 Absolute
CSI-RSRP Accuracy 41110.1.2.3.2 Relative CSI-RSRP Accuracy 41210.1.2B
Intra-frequency RSRP accuracy requirements for FR1 for CA/DC Idle Mode
Measurements 41310.1.2B.1 Intra-frequency SS-RSRP accuracy requirements
41310.1.2B.1.1 Absolute SS-RSRP Accuracy 41310.1.3 Intra-frequency RSRP
accuracy requirements for FR2 41410.1.3.1 Intra-frequency SS-RSRP
accuracy requirements 41410.1.3.1.1 Absolute SS-RSRP Accuracy
41410.1.3.1.2 Relative SS-RSRP Accuracy 41510.1.3.2 Void 41610.1.3.3
Intra-frequency CSI-RSRP accuracy requirements 41610.1.3.3.1 Absolute
CSI-RSRP Accuracy 41610.1.3.3.2 Relative CSI-RSRP Accuracy 41610.1.3B
Intra-frequency RSRP accuracy requirements for FR2 for CA/DC Idle Mode
Measurements 41710.1.3B.1 Intra-frequency SS-RSRP accuracy requirements
41710.1.3B.1.1 Absolute SS-RSRP Accuracy 41810.1.4 Inter-frequency RSRP
accuracy requirements for FR1 41810.1.4.1 Inter-frequency SS-RSRP
accuracy requirements 41810.1.4.1.1 Absolute Accuracy of SS-RSRP in FR1
41810.1.4.1.2 Relative Accuracy of SS-RSRP in FR1 41910.1.4.2 Void
42010.1.4.3 Inter-frequency CSI-RSRP accuracy requirements 42010.1.4.3.1
Absolute Accuracy of CSI-RSRP in FR1 42010.1.4.3.2 Relative Accuracy of
CS-RSRP in FR1 42110.1.4B Inter-frequency RSRP accuracy requirements for
FR1 for CA/DC Idle Mode Measurements 42210.1.4B.1 Inter-frequency
SS-RSRP accuracy requirements 42210.1.4B.1.1 Absolute Accuracy of
SS-RSRP in FR1 42210.1.5 Inter-frequency RSRP accuracy requirements for
FR2 42310.1.5.1 Inter-frequency SS-RSRP accuracy requirements
42310.1.5.1.1 Absolute SS-RSRP Accuracy 42310.1.5.1.2 Relative SS-RSRP
Accuracy 42410.1.5.2 Void 42510.1.5.3 Inter-frequency CSI-RSRP accuracy
requirements 42510.1.5.3.1 Absolute CSI-RSRP Accuracy 42510.1.5.3.2
Relative CSI-RSRP Accuracy 42510.1.5B Inter-frequency RSRP accuracy
requirements for FR2 for CA/DC Idle Mode Measurements 42610.1.6 RSRP
Measurement Report Mapping 42710.1.7 Intra-frequency RSRQ accuracy
requirements for FR1 42910.1.7.1 Intra-frequency SS-RSRQ accuracy
requirements in FR1 42910.1.7.1.1 Absolute SS-RSRQ Accuracy in FR1
42910.1.7.2 Intra-frequency CSI-RSRQ accuracy requirements 43010.1.7.2.1
Absolute CSI-RSRQ Accuracy 43010.1.7B Intra-frequency RSRQ accuracy
requirements for FR1 for CA/DC Idle Mode Measurements 43110.1.7B.1
Intra-frequency SS-RSRQ accuracy requirements in FR1 43110.1.7B.1.1
Absolute SS-RSRQ Accuracy in FR1 43110.1.8 Intra-frequency RSRQ accuracy
requirements for FR2 43210.1.8.1 Intra-frequency SS-RSRQ accuracy
requirements in FR2 43210.1.8.1.1 Absolute SS-RSRQ Accuracy in FR2
43210.1.8.2 Intra-frequency CSI-RSRQ accuracy requirements 43310.1.8.2.1
Absolute CSI-RSRQ Accuracy 43310.1.8B Intra-frequency RSRQ accuracy
requirements for FR2 for CA/DC Idle Mode Measurements 43410.1.8B.1
Intra-frequency SS-RSRQ accuracy requirements in FR2 43410.1.8B.1.1
Absolute SS-RSRQ Accuracy in FR2 43410.1.9 Inter-frequency RSRQ accuracy
requirements for FR1 43510.1.9.1 Inter-frequency SS-RSRQ accuracy
requirements in FR1 43510.1.9.1.1 Absolute Accuracy of SS-RSRQ in FR1
43510.1.9.1.2 Relative Accuracy of SS-RSRQ in FR1 43610.1.9.2
Inter-frequency CSI-RSRQ accuracy requirements 43710.1.9.2.1 Absolute
CSI-RSRQ Accuracy 43710.1.9.2.2 Relative CSI-RSRQ Accuracy 43810.1.9B
Inter-frequency RSRQ accuracy requirements for FR1 for CA/DC Idle Mode
Measurements 43910.1.9B.1 Inter-frequency SS-RSRQ accuracy requirements
in FR1 43910.1.9B.1.1 Absolute Accuracy of SS-RSRQ in FR1 43910.1.10
Inter-frequency RSRQ accuracy requirements for FR2 44010.1.10.2
Inter-frequency CSI-RSRQ accuracy requirements 44210.1.10.2.1 Absolute
CSI-RSRQ Accuracy 44210.1.10.2.2 Relative CSI-RSRQ Accuracy 44210.1.10B
Inter-frequency RSRQ accuracy requirements for FR2 for CA/DC Idle Mode
Measurements 44310.1.10B.1 Inter-frequency SS-RSRQ accuracy requirements
in FR2 44310.1.10B.1.1 Absolute Accuracy of SS-RSRQ in FR2 44310.1.11
RSRQ report mapping 44410.1.12 Intra-frequency SINR accuracy
requirements for FR1 44510.1.12.2 Intra-frequency CSI-SINR accuracy
requirements in FR1 44510.1.12.2.1 Absolute CSI-SINR Accuracy in FR1
44510.1.13 Intra-frequency SINR accuracy requirements for FR2
44610.1.13.2 Intra-frequency CSI-SINR accuracy requirements in FR2
44710.1.13.2.1 Absolute CSI-SINR Accuracy in FR2 44710.1.14
Inter-frequency SINR accuracy requirements for FR1 44810.1.14.2
Inter-frequency CSI-SINR accuracy requirements in FR1 45010.1.14.2.1
Aboslute Accuracy of CSI-SINR in FR1 45010.1.15 Inter-frequency SINR
accuracy requirements for FR2 45210.1.15.2 Inter-frequency CSI-SINR
accuracy requirements in FR2 45410.1.15.2.1 Aboslute Accuracy of
CSI-SINR in FR2 45410.1.15.2.2 Relative Accuracy of CSI-SINR in FR2
45410.1.16 SINR report mapping 45510.1.17 Power Headroom 45610.1.18
P~CMAX,c,f~ 45710.1.19 L1-RSRP accuracy requirements for FR1 45710.1.20
L1-RSRP accuracy requirements for FR2 46110.1.21 SFTD accuracy
requirements 46410.1.22 CLI measurement accuracy requirements
46810.1.24.3.1 Absolute PRS-RSRP Measurement Report Mapping
47210.1.24.3.2 Differential Report Mapping for PRS-RSRP Measurement
47210.1.23 RSTD Measurements 47410.1.23.1 Introduction 47410.1.23.2
Measurement Accuracy Requirements 47510.1.23.3 Report mapping
48110.1.23.3.1 Absolute DL RSTD Measurement Reporting 48110.1.23.3.2
Differential Reporting for DL RSTD Measurement 48310.1.23.3.3 Additional
Path Report Mapping for DL RSTD 48510.1.24 PRS-RSRP Measurements
48710.1.24.1 Introduction 48710.1.24.2 Measurement Accuracy Requirements
48710.1.24.2.1 Absolute PRS RSRP accuracy 48710.1.24.3 Report mapping
49110.1.24.3.1 Absolute PRS-RSRP Measurement Report Mapping
49110.1.24.3.2 Differential Report Mapping for PRS-RSRP Measurement
49210.1.25 UE Rx-Tx Time Difference Measurements 49410.1.25.1
Introduction 49410.1.25.2 Measurement Accuracy Requirements 49510.1.25.3
Report mapping 50110.1.25.3.1 Absolute UE Rx-Tx Measurement Report
Mapping 50110.1.25.3.2 Differential UE Rx-Tx Measurement Report Mapping
50310.1.25.3.3 Additional Path Report Mapping for UE Rx-Tx Time
Difference 50410.1.26 FR2 P-MPR report 50610.1.26.1 Report mapping
50610.1.27 L1-SINR accuracy requirements for FR1 50610.1.27.1 L1-SINR
accuracy requirements with CSI-RS based CMR and no dedicated IMR
configured 50610.1.27.1.1 Absolute Accuracy 50610.1.27.1.2 Relative
Accuracy 50710.1.27.2 L1-SINR accuracy requirements with SSB based CMR
and dedicated IMR configured 50810.1.27.2.1 Absolute Accuracy
50810.1.27.2.2 Relative Accuracy 50910.1.27.3 L1-SINR accuracy
requirements with CSI-RS based CMR and dedicated IMR configured
51110.1.27.3.1 Absolute Accuracy 51110.1.27.3.2 Relative Accuracy
51310.1.28 L1-SINR accuracy requirements for FR2 51410.1.28.1 L1-SINR
accuracy requirements with CSI-RS based CMR and no dedicated IMR
configured 51410.1.28.1.1 Absolute Accuracy 51410.1.28.1.2 Relative
Accuracy 51510.1.28.2 L1-SINR accuracy requirements with SSB based CMR
and dedicated IMR configured 51610.1.28.2.1 Absolute Accuracy
51610.1.28.2.2 Relative Accuracy 51710.1.28.3 L1-SINR accuracy
requirements with CSI-RS based CMR and dedicated IMR configured
51810.1.28.3.1 Absolute Accuracy 51810.1.28.3.2 Relative Accuracy
51910.1.29 Intra-frequency RSRQ accuracy requirements under CCA
52110.1.29.1 Intra-frequency SS-RSRQ accuracy requirements in FR1
52110.1.29.1.1 Absolute SS-RSRQ Accuracy 52110.1.30 Inter-frequency RSRQ
accuracy requirements under CCA 52210.1.30.1 Inter-frequency SS-RSRQ
accuracy requirements in FR1 52210.1.30.1.1 Aboslute Accuracy of SS-RSRQ
52210.1.30.1.2 Relative Accuracy of SS-RSRQ 52210.1.31 Intra-frequency
SINR accuracy requirements under CCA 52310.1.32 Inter-frequency SINR
accuracy requirements under CCA 52410.1.33 L1-RSRP accuracy requirements
under CCA 52510.1.34 RSSI measurements under CCA 52610.1.34.1
Intra-frequency absolute RSSI measurement accuracy requirements in FR1
52610.1.34.2 Inter-frequency absolute RSSI measurement accuracy
requirements in FR1 52710.1.34.3 RSSI measurement report mapping
52710.1.35 Channel occupancy measurements under CCA 52710.1.35.1
Intra-frequency channel occupancy measurement accuracy requirements in
FR1 52710.1.35.2 Inter-frequency channel occupancy measurement accuracy
requirements in FR1 52810.1.36 Intra-frequency RSRP accuracy
requirements under CCA 52810.1.36.1 Intra-frequency SS-RSRP accuracy
requirements in FR1 52810.1.36.1.1 Absolute SS-RSRP Accuracy
52810.1.36.1.2 Relative SS-RSRP Accuracy 52910.1.37 Inter-frequency RSRP
accuracy requirements under CCA 52910.1.37.1 Inter-frequency SS-RSRP
accuracy requirements in FR1 52910.1.37.1.1 Absolute Accuracy of SS-RSRP
52910.1.37.1.2 Relative Accuracy of SS-RSRP 53010.2 E-UTRAN measurements
53010.2.1 Introduction 53010.2.2 E-UTRAN RSRP measurements 53110.2.3
E-UTRAN RSRQ measurements 53110.2.4 E-UTRAN RSTD measurements 53110.2.5
E-UTRAN RS-SINR measurements 53210.2.6 E-UTRAN RSRP measurements for
CA/DC Idle Mode Measurements 53210.2.7 E-UTRAN RSRQ measurements for
CA/DC Idle Mode Measurements 53210.3 UTRAN FDD Measurements 53210.3.1
UTRAN FDD CPICH RSCP 53310.3.2 UTRAN FDD CPICH Ec/No 53310.4 V2X
measurements 53410.4.1 Introduction 53410.4.2 Intra-frequency PSBCH-RSRP
accuracy requirements for FR1 53410.4.2.1 PSBCH-RSRP Absolute Accuracy
53410.4.2.2 PSBCH-RSRP Relative Accuracy 53410.4.3 Intra-Frequency
SL-RSSI Measurement Accuracy Requirements for FR1 53510.4.3.1 Absolute
SL-RSSI Accuracy 53510.4.4 Intra-Frequency L1 SL-RSRP Measurement
Accuracy Requirements for FR1 53610.4.4.1 Absolute L1 SL-RSRP Accuracy
53611 Void 53712 V2X Requirements 53712.1 Introduction 53712.2 UE
Transmit Timing 53712.2.1 Introduction 53712.2.2 GNSS as synchronization
reference source 53712.2.3 NR Cell as synchronization reference source
53812.2.4 E-URTAN Cell as synchronization reference source 53812.2.5
SyncRef UE as synchronization reference source 53812.3 Initiation/Cease
of SLSS Transmissions 53912.3.1 Introduction 53912.3.1.1
Initiation/Cease of SLSS transmissions with NR cell as synchronization
reference source 53912.3.1.2 Initiation/Cease of SLSS transmissions with
EUTRAN cell as synchronization reference source 54012.3.1.3
Initiation/Cease of SLSS transmissions with GNSS as synchronization
reference source 54112.3.1.4 Initiation/Cease of SLSS transmissions with
SyncRef UE as synchronization reference source 54112.4 Selection /
Reselection of V2X Synchronization Reference Source 54112.5 L1 SL-RSRP
measurements 54212.5.1 Introduction 54212.5.2 SL-RSRP measurements
54212.6 Congestion Control measurements 54312.7 Interruption 54312.7.1
Interruptions to WAN due to V2X Sidelink Communication 54312.7.2 V2X
Sidelink Communication Dropping due to synchronization source change
54312.7.3 Interruptions to WAN due to switching between E-UTRA V2X
Sidelink and NR V2X Sidelink 54512.8 Reliability of GNSS signal 54512.9
Scheduling availability 54612.9.1 Scheduling availability of UE
switching between E-UTRA sidelink and NR sidelink 54613 Measurement
Performance Requirements for NR gNB 54613.1 UL-RTOA 54613.1.1 Report
mapping 54613.2 gNB Rx-Tx time difference 54813.2.1 Report mapping
54813.2.2 Measurement Accuracy Requirements 55013.2.2.1 Introduction
55013.2.2.2 Requirements 55113.3 UL SRS RSRP measurement 55213.3.1
Report mapping 55213.3.2 Measurement accuracy requirements 55213.3.2.1
Introduction 55213.3.2.2 Requirements 55313.4 AoA/ZoA 55413.4.1 Report
mapping 554Annex A (normative): Test Cases 555A.1 Purpose of annex
555A.2 Requirement classification for statistical testing 555A.2.1 Types
of requirements in TS 38.133 555A.2.1.1 Time and delay requirements on
UE higher layer actions 555A.2.1.2 Measurements of power levels,
relative powers and time 555A.2.1.3 Implementation requirements
556A.2.1.4 Physical layer timing requirements 556A.2.1.5 Requirements
under CCA 556A.3 RRM test configurations 557A.3.1 Reference measurement
channels 557A.3.1.1 PDSCH 557A.3.1.1.1 FDD 557A.3.1.1.2 TDD 558A.3.1A
Reference measurement channels under CCA 561A.3.1A.1 PDSCH 561A.3.1A.1.1
TDD 561A.3.1A.2 CORESET for RMSI scheduling 562A.3.1A.2.1 TDD
562A.3.1A.3 CORESET for RMC scheduling 563A.3.1A.3.1 TDD 563A.3.1A.4 TDD
UL/DL configuration 564A.3.1A.5 RMC burst transmission model 564A.3.1.2
CORESET for RMSI scheduling 565A.3.1.2.1 FDD 565A.3.1.2.2 TDD 566A.3.1.3
CORESET for RMC scheduling 569A.3.1.3.1 FDD 569A.3.1.3.2 TDD 570A.3.1.4
TDD UL/DL configuration 573A.3.2 OFDMA channel noise generator (OCNG)
574A.3.2.1 Generic OFDMA Channel Noise Generator (OCNG) 574A.3.2.1.1
OCNG pattern 1: Generic OCNG pattern for all unused REs 574A.3.2.1.2
OCNG pattern 2: Generic OCNG pattern for all unused REs for 2AoA setup
575A.3.2.1.3 OCNG pattern 3: Generic OCNG pattern for unused REs in the
same bandwidth as CORESET 575A.3.2.1.4 OCNG pattern 4: Generic OCNG
pattern for all unused REs outside SSB slot(s) 576A.3.2.2 Void 577A.3.3
Reference DRX configurations 577A.3.3.1 DRX Configuration 1: DRX cycle =
40 ms and TAT = 500 ms 577A.3.3.2 DRX Configuration 2: DRX cycle = 640
ms and TAT = 500 ms 577A.3.3.3 DRX Configuration 3: DRX cycle = 40 ms
and TAT = Infinity 577A.3.3.4 DRX Configuration 4: DRX cycle = 160 ms
and TAT = Infinity 578A.3.3.5 DRX Configuration 5: DRX cycle = 320 ms
and TAT = Infinity 578A.3.3.6 DRX Configuration 6: DRX cycle = 320 ms
and TAT = 500 ms 578A.3.3.7 DRX Configuration 7: DRX cycle = 640 ms and
TAT = Infinity 579A.3.3.8 DRX Configuration 8: DRX cycle = 320 ms and
TAT = Infinity 579A.3.3.9 DRX Configuration 9: DRX cycle = 40 ms and TAT
= 500 ms 579A.3.3.10 DRX Configuration 10: DRX cycle = 640 ms and TAT =
500 ms 580A.3.3.11 DRX Configuration 11: DRX cycle = 20 ms and TAT =
Infinity 580A.3.3.12 DRX Configuration 12: DRX cycle = 640 ms and TAT =
Infinity 580A.3.4 Test Cases with Different Channel Bandwidths
580A.3.4.1 Test Cases with Different E-UTRA Channel Bandwidths
580A.3.4.1.1 Introduction 580A.3.4.1.2 Principle of testing 581A.3.5
Test Cases for Synchronous and Asynchronous DC Operations 581A.3.5.1
EN-DC Test Cases for Synchronous and Asynchronous EN-DC Operations
581A.3.5.1.1 Introduction 581A.3.5.1.2 Principle of Testing 581A.3.6
Antenna configurations 581A.3.6.1 Antenna configurations for FR1
581A.3.6.1.1 Antenna connection for 4 Rx capable UEs 581A.3.6.1.1.1
Introduction 581A.3.6.1.1.2 Principle of testing 581A.3.6.2 Antenna
configurations for FR2 584A.3.6A Antenna configurations with unlicensed
bands 584A.3.6A.1 Antenna configurations for FR1 584A.3.6A.1.1 Antenna
connection for 4 Rx capable UEs 584A.3.6A.1.1.1 Introduction
584A.3.6A.1.1.2 Principle of testing 584A.3.7 EN-DC test setup
586A.3.7.1 Introduction 586A.3.7.2 E-UTRAN Serving Cell Parameters
586A.3.7.2.1 E-UTRAN Serving Cell Parameters for Tests with NR Cell(s)
in FR1 586A.3.7.2.2 E-UTRAN Serving Cell Parameters for Tests with NR
Cell(s) in FR2 587A.3.7A NR FR1-FR2 test setup 588A.3.7B EN-DC test
setup with unlicensed bands 589A.3.7B.1 Introduction 589A.3.7B.2 E-UTRAN
Serving Cell Parameters 589A.3.7B.2.1 E-UTRAN Serving Cell Parameters
for Tests with NR Cell(s) under CCA in FR1 589A.3.7C LTE-FR1/FR2 test
setup 590A.3.7D NE-DC test setup 590A.3.7D.1 Introduction 590A.3.7D.2
E-UTRAN Serving Cell Parameters 590A.3.7D.2.1 E-UTRAN Serving Cell
Parameters for Tests with NR Cell(s) in FR1 590A.3.7D.2.2 E-UTRAN
Serving Cell Parameters for Tests with NR Cell(s) in FR2 590A.3.8 PRACH
configurations 590A.3.8.1 Introduction 590A.3.8.2 PRACH configurations
in FR1 591A.3.8.2.1 FR1 PRACH configuration 1 591A.3.8.2.2 FR1 PRACH
configuration 2 591A.3.8.2.3 FR1 PRACH configuration 3 592A.3.8.2.4 FR1
PRACH configuration 4 593A.3.8.3 PRACH configurations in FR2
594A.3.8.3.1 FR2 PRACH configuration 1 594A.3.8.3.2 FR2 PRACH
configuration 2 595A.3.8.3.3 FR2 PRACH configuration 3 596A.3.8.3.4 FR2
PRACH configuration 4 597A.3.8A PRACH configurations under CCA
598A.3.8A.1 Introduction 598A.3.8A.2 PRACH configurations in FR1
598A.3.8A.2.1 FR1 PRACH configuration 1 under CCA 598A.3.8A.2.2 FR1
PRACH configuration 2 under CCA 599A.3.9 BWP configurations 600A.3.9.1
Introduction 600A.3.9.2 Downlink BWP configurations 601A.3.9.2.1 Initial
BWP 601A.3.9.2.2 Dedicated BWP 601A.3.9.3 Uplink BWP configurations
602A.3.9.3.1 Initial BWP 602A.3.9.3.2 Dedicated BWP 602A.3.10 SSB
Configurations 603A.3.10.1 SSB Configurations for FR1 603A.3.10.1.1 SSB
pattern 1 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz
603A.3.10.1.5 SSB pattern 5 in FR1: SSB allocation for SSB SCS=15 kHz
starting from odd SFN in 10 MHz 605A.3.10A SSB Configurations under CCA
610A.3.10A.1 SSB Configurations under CCA for FR1 610A.3.10A.1.1 SSB
pattern 1 under CCA for semi-static channel access: SSB allocation for
SSB SCS=30kHz in 40MHz 610A.3.10A.1.2 SSB pattern 2 under CCA for
dynamic channel access: SSB allocation for SSB SCS=30kHz in 40MHz
610A.3.10A.1.3 SSB pattern 3 under CCA for semi-static channel access:
SSB allocation for SSB SCS=30 kHz in 40 MHz 611A.3.10A.1.4 SSB pattern 4
under CCA for dynamic channel access: SSB allocation for SSB SCS=30 kHz
in 40 MHz 611A.3.11 SMTC Configurations 612A.3.11.1 SMTC pattern 1: SMTC
period = 20 ms with SMTC duration = 1 ms 612A.3.11.2 SMTC pattern 2:
SMTC period = 20 ms with SMTC duration = 5 ms 612A.3.11.3 SMTC pattern
3: SMTC period = 160 ms with SMTC duration = 1 ms 612A.3.11.4 SMTC
pattern 4: SMTC period = 20 ms with SMTC duration = 1 ms 612A.3.11.5
SMTC pattern 5: SMTC period = 20 ms with SMTC duration = 5 ms
613A.3.11.6 SMTC pattern 6: SMTC period = 20 ms with SMTC duration = 5
ms 613A.3.11.7 Void 613A.3.11.8 Void 613A.3.11.9 SMTC pattern 9: SMTC
period = 20 ms with SMTC duration = 1 ms 613A.3.12 Test Cases with
Different CC Configurations 613A.3.12.1 EN-DC Test Cases with Different
EN-DC Configurations 613A.3.12.1.1 Introduction 613A.3.12.1.2 Principle
of testing 613A.3.12.2 Carrier Aggregation Test Cases with Different CA
Configurations 614A.3.12.2.1 Introduction 614A.3.12.2.2 Principle of
testing 614A.3.13 Test Cases in SA and EN-DC Operations 614A.3.13.1
Introduction 614A.3.13.2 Principle of Testing 614A.3.13A Test Cases
involving E-UTRA/FR1 and FR2 carriers 614A.3.13A.1 Introduction
614A.3.13A.2 Principle of Testing in EN-DC 615A.3.13A.3 Principle of
Testing in SA 615A.3.13B Test Cases for EN-DC and NE-DC Operations
616A.3.13B.1 Active BWP switch Test Cases for EN-DC and NE-DC Operations
616A.3.13B.1.1 Introduction 616A.3.13B.1.2 Principle of Testing
617A.3.13B.2 SFTD accuracy Test Cases for EN-DC and NE-DC Operations
617A.3.13B.2.1 Introduction 617A.3.13B.2.2 Principle of Testing
617A.3.14 CSI-RS configurations 617A.3.14.1 FDD 617A.3.14.2 TDD
619A.3.15 Angle of Arrival (AoA) for FR2 RRM test cases 624A.3.15.1
Setup 1: Single AoA in Rx beam peak direction 624A.3.15.2 Setup 2:
Single AoA in non Rx beam peak direction 624A.3.15.2.1 Setup 2a: Single
AoA in non Rx beam peak direction without change in direction
624A.3.15.2.2 Setup 2b: Single AoA in non Rx beam peak direction with
change in direction 625A.3.15.3 Setup 3: 2 AoAs 625A.3.15.4 Setup 4: 2
AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak
625A.3.15.4.1 Setup 4a: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in
non Rx beam peak without change in direction 625A.3.15.4.2 Setup 4b: 2
AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak with change
in direction 625A.3.16 TCI State Configuration 626A.3.16.1 Introduction
626A.3.16.2 TCI states 626A.3.17 Configurations of CSI-RS for tracking
626A.3.17.1 Configuration of CSI-RS for tracking for FR1 626A.3.17.1.1
FDD 626A.3.17.1.2 TDD 627A.3.17.2 Configuration of CSI-RS for tracking
for FR2 628A.3.17.2.1 TDD 628A.3.18 Additional definitions related to
OTA testing for FR2 RRM test cases 629A.3.18.1 Introduction 629A.3.18.2
PRACH Power Measurement 629A.3.19 Test applicability for DAPS handover
629A.3.19.1 Introduction 629A.3.19.2 Principle of testing 629A.3.20 MsgA
configurations 630A.3.20.1 Introduction 630A.3.20.2 MsgA configurations
in FR1 630A.3.20.2.1 FR1 MsgA configuration 1 630A.3.20.2.2 FR1 MsgA
configuration 2 631A.3.20.3 MsgA configurations in FR2 633A.3.20.3.1 FR2
MsgA configuration 1 633A.3.20.3.2 FR2 MsgA configuration 2 634A.3.20A
MsgA configurations under CCA 636A.3.20A.1 Introduction 636A.3.20A.2
MsgA configurations in FR1 636A.3.20A.2.1 FR1 MsgA configuration 1 under
CCA 636A.3.20A.2.2 FR1 MsgA configuration 2 under CCA 637A.3.21 V2X
sidelink communication 640A.3.21.1 Introduction 640A.3.21.2 Reference
resource pool configurations for V2X Sidelink Communication 640A.3.21.3
Reference measurement channels for V2X Sidelink Communication 644A.3.22
CSI-IM configurations 644A.3.22.1 FDD 644A.3.22.2 TDD 645A.3.23 Spatial
Relation Configuration 647A.3.23.1 Introduction 647A.3.23.2 Spatial
Relation 647A.3.24 SRS configuration 648A.3.25 Channel bandwidth (CBW)
configurations 650A.3.25.1 DL UE specific CBW 651A.3.26 CCA model
651A.3.26.1 Introduction 651A.3.26.2 CCA model for operation on a
carrier frequency with CCA in FR1 651A.3.26.2.1 DL CCA model
651A.3.26.2.2 UL CCA model 653A.3.27 Test Cases with at Least One Cell
on a Carrier Frequency with CCA 653A.3.27.1 Introduction 654A.3.27.2 NR
Standalone Tests with NR SCell under CCA and All Other NR Cells in FR1
654A.3.27.3 EN-DC Tests with NR PSCell under CCA and Other NR Cells in
FR1 654A.3.27.4 NR Standalone Tests with NR PCell under CCA and Other NR
Cells in FR1 654A.3.27.5 E-UTRA Standalone Tests with at Least One NR
Cell under CCA 654A.3.28 Discovery Burst Transmission Window
configuration under CCA 654A.3.28.1 DBT Window pattern 1: DBT Window
period = 20 ms with DBT Window duration = 1 ms 654A.3.29 Testing
principles for UE capable of only NR bands with shared spectrum access
654A.3.29.1 Introduction 654A.3.29.2 Principle of testing for UE capable
of EN-DC with only NR bands with shared spectrum access 655A.3.29.3
Principle of testing for UE capable of SA operation with only NR bands
with shared spectrum access 655A.3.30 CSI-RS configurations for RRM
656A.3.30.1 FDD 656A.3.30.2 TDD 657A.3.31 PRS Configurations
659A.3.31.1. PRS Configurations for FR1 659A.3.31.1.1. PRS pattern 1 in
FR1: SCS=15 KHz 659A.3.31.1.2. PRS pattern 2 in FR1: SCS=30 KHz
660A.3.31.2. PRS Configurations for FR2 660A.3.31.2.1. PRS pattern 1 in
FR2: SCS=120 KHz 660A.4 EN-DC tests with all NR cells in FR1 661A.4.1
Void 661A.4.2 Void 661A.4.3 RRC\_CONNECTED state mobility 661A.4.3.1
Void 661A.4.3.2 RRC Connection Mobility Control 661A.4.3.2.1 Void
661A.4.3.2.2 Random Access 661A.4.3.2.2.1 4-step RA type contention
based random access test in FR1 for PSCell in EN-DC 661A.4.3.2.2.2
4-step RA type non-contention based random access test in FR1 for PSCell
in EN-DC 665A.4.3.2.2.3 2-step RA type contention based random access
test in FR1 for PSCell in EN-DC 669A.4.3.2.2.4 2-step RA type
non-contention based random access test in FR1 for PSCell in EN-DC
673A.4.3.2.3 Void 677A.4.4 Timing 677A.4.4.1 UE transmit timing
677A.4.4.1.1 NR UE Transmit Timing Test for FR1 677A.4.4.1.1.1 Test
Purpose and environment 677A.4.4.1.1.2 Test requirements 681A.4.4.2 UE
timer accuracy 681A.4.4.3 Timing advance 681A.4.4.3.1 EN-DC FR1 timing
advance adjustment accuracy 681A.4.4.3.1.1 Test Purpose and Environment
681A.4.4.3.1.2 Test Parameters 682A.4.4.3.1.3 Test Requirements 685A.4.5
Signaling characteristics 685A.4.5.1 Radio link Monitoring 685A.4.5.1.1
Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with
SSB-based RLM RS in non-DRX mode 686A.4.5.1.1.1 Test Purpose and
Environment 686A.4.5.1.1.2 Test Requirements 690A.4.5.1.2 Radio Link
Monitoring In-sync Test for FR1 PSCell configured with SSB-based RLM RS
in non-DRX mode 690A.4.5.1.2.1 Test Purpose and Environment
690A.4.5.1.2.2 Test Requirements 696A.4.5.1.3 Radio Link Monitoring
Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in DRX
mode 696A.4.5.1.3.1 Test Purpose and Environment 696A.4.5.1.3.2 Test
Requirements 702A.4.5.1.4 Radio Link Monitoring In-sync Test for FR1
PSCell configured with SSB-based RLM RS in DRX mode 702A.4.5.1.4.1 Test
Purpose and Environment 702A.4.5.1.4.2 Test Requirements 708A.4.5.1.5
EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured
with CSI-RS-based RLM in non-DRX mode 708A.4.5.1.5.1 Test Purpose and
Environment 708A.4.5.1.5.2 Test Requirements 714A.4.5.1.6 EN-DC Radio
Link Monitoring In-sync Test for FR1 PSCell configured with CSI-RS-based
RLM in non-DRX mode 714A.4.5.1.6.1 Test Purpose and Environment
714A.4.5.1.6.2 Test Requirements 720A.4.5.1.7 EN-DC Radio Link
Monitoring Out-of-sync Test for FR1 PSCell configured with CSI-RS-based
RLM in DRX mode 720A.4.5.1.7.1 Test Purpose and Environment
720A.4.5.1.7.2 Test Requirements 725A.4.5.1.8 EN-DC Radio Link
Monitoring In-sync Test for FR1 PSCell configured with CSI-RS-based RLM
in DRX mode 726A.4.5.1.8.1 Test Purpose and Environment 726A.4.5.1.8.2
Test Requirements 731A.4.5.2 Interruption 731**A.4.5.2.1** E-UTRAN -- NR
FR1 interruptions at transitions between active and non-active during
DRX in synchronous EN-DC 731A.4.5.2.1.1 Test Purpose and Environment
731A.4.5.2.1.2 Test Requirements 735**A.4.5.2.2** E-UTRAN -- NR FR1
interruptions at transitions between active and non-active during DRX in
asynchronous EN-DC 735A.4.5.2.2.1 Test Purpose and Environment
735A.4.5.2.2.2 Test Requirements 739**A.4.5.2.3** E-UTRAN -- NR FR1
interruptions during measurements on deactivated NR SCC in synchronous
EN-DC 739A.4.5.2.3.1 Test Purpose and Environment 739A.4.5.2.3.2 Test
Requirements 744A.4.5.2.4 E-UTRAN -- NR FR1 interruptions during
measurements on deactivated NR SCC in asynchronous EN-DC 745A.4.5.2.4.1
Test Purpose and Environment 745A.4.5.2.4.2 Test Requirements
749**A.4.5.2.5** E-UTRAN -- NR FR1 interruptions during measurements on
deactivated E-UTRAN SCC in synchronous EN-DC 750A.4.5.2.5.1 Test Purpose
and Environment 750A.4.5.2.5.2 Test Requirements 754**A.4.5.2.6**
E-UTRAN -- NR FR1 interruptions during measurements on deactivated
E-UTRAN SCC in asynchronous EN-DC 754A.4.5.2.6.1 Test Purpose and
Environment 754A.4.5.2.6.2 Test Requirements 758A.4.5.2.7 Void
758**A.4.5.2.8** **E-UTRAN - NR FR1 i**nterruptions at NR SRS carrier
based switching in asynchronous EN-DC 758A.4.5.2.8.1 Test Purpose and
Environment 758A.4.5.2.8.2 Test Requirements 761**A.4.5.2.9** E-UTRAN --
NR interruptions at E-UTRA SRS carrier based switching 762A.4.5.2.9.1
Test Purpose and Environment 762A.4.5.2.9.2 Test Requirements 766A.4.5.3
SCell Activation and Deactivation Delay 767A.4.5.3.1 SCell Activation
and deactivation of known SCell in FR1 for 160ms SCell measurement cycle
767A.4.5.3.1.1 Test Purpose and Environment 767A.4.5.3.1.2 Test
Requirements 773A.4.5.3.2 SCell Activation and deactivation of known
SCell in FR1 for 640ms SCell measurement cycle 774A.4.5.3.2.1 Test
Purpose and Environment 774A.4.5.3.2.2 Test Requirements 774A.4.5.3.3
SCell Activation and deactivation of unknown SCell in FR1 774A.4.5.3.3.1
Test Purpose and Environment 774A.4.5.3.3.2 Test Requirements
775A.4.5.3.4 SCell Activation and deactivation of multiple unknown
SCells in FR1 with single activation/deactivation command 776A.4.5.3.4.1
Test Purpose and Environment 776A.4.5.3.4.2 Test Requirements
780A.4.5.3.5 Direct SCell activation at SCell addition of known SCell in
FR1 780A.4.5.3.5.1 Test Purpose and Environment 780A.4.5.3.5.2 Test
Requirements 788A.4.5.4 UE UL carrier RRC reconfiguration Delay
789A.4.5.4.1 UE UL carrier RRC reconfiguration Delay 789A.4.5.4.1.1 Test
Purpose and Environment 789A.4.5.4.1.2 Test Requirements 796A.4.5.5 Beam
Failure Detection and Link recovery procedures 796A.4.5.5.1 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 PSCell configured with
SSB-based BFD and LR in non-DRX mode 796A.4.5.5.1.1 Test Purpose and
Environment 796A.4.5.5.1.2 Test Requirements 802A.4.5.5.2 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 PSCell configured with
SSB-based BFD and LR in DRX mode 803A.4.5.5.2.1 Test Purpose and
Environment 803A.4.5.5.2.2 Test Requirements 808A.4.5.5.3 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 PSCell configured with
CSI-RS-based BFD and LR in non-DRX mode 809A.4.5.5.3.1 Test Purpose and
Environment 809A.4.5.5.3.2 Test Requirements 814A.4.5.5.4 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 PSCell configured with
CSI-RS-based BFD and LR in DRX mode 815A.4.5.5.4.1 Test Purpose and
Environment 815A.4.5.5.4.2 Test Requirements 820A.4.5.5.5 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 SCell configured with
CSI-RS-based BFD and SSB-based LR in non-DRX mode 821A.4.5.5.5.1 Test
Purpose and Environment 821A.4.5.5.5.2 Test Requirements 826A.4.5.5.6
EN-DC Beam Failure Detection and Link Recovery Test for FR1 SCell
configured with CSI-RS-based BFD and SSB-based LR in DRX mode
827A.4.5.5.6.1 Test Purpose and Environment 827A.4.5.5.6.2 Test
Requirements 833A.4.5.6 Active BWP switch 834A.4.5.6.1 DCI-based and
Timer-based Active BWP Switch 834A.4.5.6.1.1 E-UTRAN -- NR PSCell FR1 DL
active BWP switch in non-DRX in synchronous EN-DC 834A.4.5.6.1.2 E-UTRAN
-- NR PSCell FR1 DL active BWP switch with FR1 SCell in non-DRX in
synchronous EN-DC 839A.4.5.6.2 RRC-based Active BWP Switch 845A.4.5.6.3
Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs
849A.4.5.6.3.1 Simultaneous E-UTRAN -- NR PSCell FR1 DL active BWP
switch in non-DRX in EN-DC on multiple CCs 849A.4.5.6.3.1.2 Test
Requirements 855A.4.5.6.4 SCell dormancy switch 855A.4.5.6.4.1 E-UTRAN
-- NR FR1 PSCell SCell dormancy switch of single FR1 SCell outside
active time 855A.4.5.6.4.1.1 Test Purpose and Environment
855A.4.5.6.4.1.2 Test Requirements 863A.4.5.6.4.2 E-UTRAN -- NR FR1
PSCell SCell dormancy switch of two FR1 SCells inside active time
863A.4.5.6.4.2.1 Test Purpose and Environment 863A.4.5.6.4.2.2 Test
Requirements 875A.4.5.6.5 Simultaneous RRC-based Active BWP Switch on
multiple CCs 876A.4.5.6.5.1 E-UTRAN -- NR PSCell FR1 DL active BWP
switch in non-DRX in synchronous EN-DC on multiple CCs 876A.4.5.7 PSCell
addition and release delay 880A.4.5.7.1 Addition and Release Delay of
known NR PSCell 880A.4.5.7.1.1 Test purpose and environment
880A.4.5.7.1.2 Test Requirements 884A.4.5.8 DL Interruptions at
switching between two uplink carriers 885A.4.5.8.1 Test Purpose and
Environment 885A.4.5.8.2 Test Requirements 888A.4.5.9 UE specific CBW
change 889A.4.5.9.1 UE specific CBW change on FR1 NR PSCell with non-DRX
in synchronous EN- DC 889A.4.5.9.1.1 Test Purpose and Environment
889A.4.5.9.1.2 Test Requirements 893A.4.6 Measurement procedure
893A.4.6.1 Intra-frequency Measurements 893A.4.6.1.1 EN-DC event
triggered reporting tests without gap under non-DRX 893A.4.6.1.1.1 Test
purpose and Environment 893A.4.6.1.1.2 Test parameters 893A.4.6.1.1.3
Test Requirements 897A.4.6.1.2 EN-DC event triggered reporting tests
without gap under DRX 897A.4.6.1.2.1 Test purpose and Environment
897A.4.6.1.2.2 Test parameters 897A.4.6.1.2.2 Test Requirements
901A.4.6.1.3 EN-DC event triggered reporting tests with per-UE gaps
under non-DRX 901A.4.6.1.3.1 Test purpose and Environment 901A.4.6.1.3.2
Test parameters 901A.4.6.1.3.3 Test Requirements 905A.4.6.1.4 EN-DC
event triggered reporting tests with per-UE gaps under DRX
905A.4.6.1.4.1 Test purpose and Environment 905A.4.6.1.4.2 Test
parameters 905A.4.6.1.4.3 Test Requirements 909A.4.6.1.5 EN-DC event
triggered reporting tests without gap under non-DRX with SSB index
reading 909A.4.6.1.5.1 Test purpose and Environment 909A.4.6.1.5.2 Test
parameters 909A.4.6.1.5.3 Test Requirements 911A.4.6.1.6 EN-DC event
triggered reporting tests with SSB index reading with per-UE gaps
912A.4.6.1.6.1 Test purpose and Environment 912A.4.6.1.6.2 Test
parameters 912A.4.6.1.6.3 Test Requirements 914A.4.6.1.7 EN-DC event
triggered reporting tests under DRX for UE configured with
highSpeedMeasFlag-r16 915A.4.6.1.7.1 Test purpose and Environment
915A.4.6.1.7.2 Test parameters 915A.4.6.1.7.3 Test Requirements
919A.4.6.2 Inter-frequency Measurements 919A.4.6.2.1 EN-DC event
triggered reporting tests for FR1 cell without SSB time index detection
when DRX is not used 919A.4.6.2.1.1 Test Purpose and Environment
919A.4.6.2.1.2 Test Requirements 923A.4.6.2.2 EN-DC event triggered
reporting tests for FR1 cell without SSB time index detection when DRX
is used 923A.4.6.2.2.1 Test Purpose and Environment 923A.4.6.2.2.2 Test
Requirements 927A.4.6.2.3 Void 927A.4.6.2.4 Void 927A.4.6.2.5 EN-DC
event triggered reporting tests for FR1 cell with SSB time index
detection when DRX is not used 927A.4.6.2.5.1 Test Purpose and
Environment 927A.4.6.2.5.2 Test Requirements 932A.4.6.2.6 EN-DC event
triggered reporting tests for FR1 cell with SSB time index detection
when DRX is used 932A.4.6.2.6.1 Test Purpose and Environment
932A.4.6.2.6.2 Test Requirements 937A.4.6.2.7 Void 938A.4.6.2.8 Void
938A.4.6.3 Void 938A.4.6.4 L1-RSRP measurement for beam reporting
938A.4.6.4.1 SSB based L1-RSRP measurement when DRX is not used
938A.4.6.4.1.1 Test Purpose and Environment 938A.4.6.4.1.2 Test
parameters 938A.4.6.4.1.3 Test Requirements 941A.4.6.4.2 SSB based
L1-RSRP measurement when DRX is used 941A.4.6.4.2.1 Test Purpose and
Environment 941A.4.6.4.2.2 Test parameters 942A.4.6.4.2.3 Test
Requirements 945A.4.6.4.3 CSI-RS based L1-RSRP measurement when DRX is
not used 945A.4.6.4.3.1 Test Purpose and Environment 945A.4.6.4.3.2 Test
parameters 946A.4.6.4.3.3 Test Requirements 949A.4.6.4.4 CSI-RS based
L1-RSRP measurement when DRX is used 949A.4.6.4.4.1 Test Purpose and
Environment 949A.4.6.4.4.2 Test parameters 950A.4.6.4.4.3 Test
Requirements 952A.4.6.4.5 SSB based L1-RSRP measurement when DRX is used
for UE configured with *highSpeedMeasFlag-r16* 952A.4.6.4.5.1 Test
Purpose and Environment 952A.4.6.4.5.2 Test parameters 953A.4.6.4.5.3
Test Requirements 956A.4.6.5 CLI measurements 956A.4.6.5.1 SRS-RSRP
measurement with non-DRX 956A.4.6.5.1.1 Test Purpose and Environment
956A.4.6.5.1.2 Test Parameters 957A.4.6.5.1.3 Test Requirements
960A.4.6.5.2 CLI-RSSI measurement with non-DRX 960A.4.6.5.2.1 Test
Purpose and Environment 960A.4.6.5.2.2 Test Parameters 961A.4.6.5.2.3
Test Requirements 962A.4.6.6 Measurements with autonomous gaps
963A.4.6.6.1 EN-DC intra-frequency CGI identification of NR FR1 cell
with autonomous gaps in synchronous EN-DC 963A.4.6.6.1.1 Test Purpose
and Environment 963A.4.6.6.1.2 Test Requirements 967A.4.6.7 L1-SINR
measurement for beam reporting 967A.4.6.7.1 L1-SINR measurement with
CSI-RS based CMR and no dedicated IMR when DRX is not used
967A.4.6.7.1.1 Test Purpose and Environment 967A.4.6.7.1.2 Test
parameters 968A.4.6.7.1.3 Test Requirements 971A.4.6.7.2 L1-SINR
measurement with SSB based CMR and dedicated IMR when DRX is used
971A.4.6.7.2.1 Test Purpose and Environment 971A.4.6.7.2.2 Test
parameters 972A.4.6.7.2.3 Test Requirements 975A.4.6.7.3 L1-SINR
measurement with CSI-RS based CMR and dedicated IMR configured when DRX
is used 975A.4.6.7.3.1 Test Purpose and Environment 975A.4.6.7.3.2 Test
parameters 976A.4.6.7.3.3 Test Requirements 979A.4.6.8 CSI-RS based
intra-frequency Measurement 979A.4.6.8.1 EN-DC event triggered reporting
tests without gap under DRX 979A.4.6.8.1.1 Test purpose and Environment
979A.4.6.8.1.2 Test Requirements 983A.4.6.9 CSI-RS based inter-frequency
Measurement 984A.4.6.9.1 EN-DC event triggered reporting tests for FR1
cell when non-DRX is used 984A.4.6.9.1.1 Test Purpose and Environment
984A.4.6.9.1.2 Test Requirements 988A.4.7 Measurement Performance
requirements 989A.4.7.1 SS-RSRP 989A.4.7.1.1 EN-DC Intra-frequency
measurement accuracy with FR1 serving cell and FR1 target cell
989A.4.7.1.1.1 Test Purpose and Environment 989A.4.7.1.1.2 Test
parameters 989A.4.7.1.1.3 Test Requirements 993A.4.7.1.2 EN-DC
inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell 993A.4.7.1.2.1 Test Purpose and Environment 993A.4.7.1.2.2
Test parameters 994A.4.7.1.2.3 Test Requirements 998A.4.7.1.3 Void
998A.4.7.2 SS-RSRQ 998**A.4.7.2.1** **EN-DC Intra-frequency measurement
accuracy with FR1 serving cell and FR1 target cell** 998A.4.7.2.1.1 Test
Purpose and Environment 998A.4.7.2.1.2 Test Parameters 999A.4.7.2.1.3
Test Requirements 1004A.4.7.2.2 EN-DC Inter-frequency measurement
accuracy with FR1 serving cell and FR1 target cell 1004A.4.7.2.2.1 Test
Purpose and Environment 1004A.4.7.2.2.2 Test Parameters 1004A.4.7.2.2.3
Test Requirements 1009A.4.7.3 SS-SINR 1009A.4.7.3.1 EN-DC
Intra-frequency measurement accuracy with FR1 serving cell and FR1
target cell 1009A.4.7.3.1.1 Test Purpose and Environment 1009A.4.7.3.1.2
Test Parameters 1009A.4.7.3.1.3 Test Requirements 1013A.4.7.3.2 EN-DC
Inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell 1013A.4.7.3.2.1 Test Purpose and Environment 1013A.4.7.3.2.2
Test Parameters 1013A.4.7.3.2.3 Test Requirements 1018A.4.7.4 L1-RSRP
measurement for beam reporting 1018A.4.7.4.1 SSB based L1-RSRP
measurement 1018A.4.7.4.1.1 Test Purpose and Environment 1018A.4.7.4.1.2
Test parameters 1019A.4.7.4.1.3 Test Requirements 1022A.4.7.4.2 CSI-RS
based L1-RSRP measurement on resource set with repetition off
1022A.4.7.4.2.1 Test Purpose and Environment 1022A.4.7.4.2.2 Test
parameters 1023A.4.7.4.2.3 Test Requirements 1026A.4.7.5 SFTD accuracy
1026A.4.7.5.1 SFTD accuracy 1026A.4.7.5.1.1 Test Purpose and Environment
1026A.4.7.5.1.2 Test Parameters 1026A.4.7.5.1.3 Test Requirements
1031A.4.7.5.2 Void 1031A.4.7.5.3 Void 1031A.4.7.6 CLI measurements
1031A.4.7.6.1 EN-DC SRS-RSRP measurement accuracy with FR1 serving cell
1031A.4.7.6.1.1 Test Purpose and Environment 1031A.4.7.6.1.2 Test
parameters 1032A.4.7.6.1.3 Test Requirements 1037A.4.7.6.2 EN-DC
CLI-RSSI measurement accuracy with FR1 serving cell 1037A.4.7.6.2.1 Test
Purpose and Environment 1037A.4.7.6.2.2 Test parameters 1038A.4.7.6.2.3
Test Requirements 1041A.4.7.7 L1-SINR measurement for beam reporting
1041A.4.7.7.1 L1-SINR measurement with CSI-RS based CMR and no dedicated
IMR configured and CSI-RS resource set with repetition off
1041A.4.7.7.1.1 Test Purpose and Environment 1041A.4.7.7.1.2 Test
parameters 1042A.4.7.7.1.3 Test Requirements 1046A.4.7.7.2 L1-SINR
measurement with SSB based CMR and dedicated IMR 1046A.4.7.7.2.1 Test
Purpose and Environment 1046A.4.7.7.2.2 Test parameters 1047A.4.7.7.2.3
Test Requirements 1051A.4.7.7.3 L1-SINR measurement with CSI-RS based
CMR and dedicated IMR 1051A.4.7.7.3.1 Test Purpose and Environment
1051A.4.7.7.3.2 Test parameters 1052A.4.7.7.3.3 Test Requirements
1055A.4.7.8 CSI-RSRP 1055A.4.7.8.1 EN-DC Intra-frequency measurement
accuracy with FR1 serving cell and FR1 target cell 1055A.4.7.8.1.1 Test
Purpose and Environment 1055A.4.7.8.1.2 Test parameters 1056A.4.7.8.1.3
Test Requirements 1059A.4.7.8.2 EN-DC inter-frequency measurement
accuracy with FR1 serving cell and FR1 target cell 1060A.4.7.8.2.1 Test
Purpose and Environment 1060A.4.7.8.2.2 Test parameters 1060A.4.7.8.2.3
Test Requirements 1064A.4.7.9 CSI-RSRQ 1064A.4.7.9.1 EN-DC
Intra-frequency measurement accuracy with FR1 serving cell and FR1
target cell 1064A.4.7.9.1.1 Test Purpose and Environment 1064A.4.7.9.1.2
Test Parameters 1064A.4.7.9.1.3 Test Requirements 1069A.4.7.9.2 EN-DC
Inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell 1069A.4.7.9.2.1 Test Purpose and Environment 1069A.4.7.9.2.2
Test Parameters 1069A.4.7.2.2.3 Test Requirements 1074A.4.7.10 CSI-SINR
1074A.4.7.10.1 EN-DC Intra-frequency measurement accuracy with FR1
serving cell and FR1 target cell 1074A.4.7.10.1.1 Test Purpose and
Environment 1074A.4.7.10.1.2 Test Parameters 1075A.4.7.10.1.3 Test
Requirements 1079A.4.7.10.2 EN-DC Inter-frequency measurement accuracy
with FR1 serving cell and FR1 target cell 1079A.4.7.10.2.1 Test Purpose
and Environment 1079A.4.7.10.2.2 Test Parameters 1080A.4.7.10.2.3 Test
Requirements 1084A.4.8 Void 1085A.4A NE-DC test with all NR cells in FR1
1085A.4A.1 Signaling characteristics 1085A.4A.1.1 E-UTRAN PSCell
addition 1085A.4A.1.1.1 Test purpose and environment 1085A.4A.1.1.2 Test
Requirements 1089A.4A.1.2 Active BWP switch 1090A.4A.1.2.1 E-UTRAN
PSCell -- NR PCell FR1 DCI-based and Timer-based DL active BWP switch in
non-DRX in synchronous NE-DC 1090A.4A.1.2.1.1 Test Purpose and
Environment 1090A.4A.1.2.1.2 Test Requirements 1094A.4A.2 Measurement
performance 1095A.4A.2.1 SFTD accuracy 1095A.4A.2.1.1 SFTD accuracy
1095A.4A.2.1.1.1 Test Purpose 1095A.4A.2.1.1.2 Test Environment
1095A.4A.2.1.1.3 Test Requirements 1099A.5 EN-DC tests with one or more
NR cells in FR2 1100A.5.1 Void 1100A.5.2 Void 1100A.5.3 RRC\_CONNECTED
state mobility 1100A.5.3.1 Void 1100A.5.3.2 RRC Connection Mobility
Control 1100A.5.3.2.1 Void 1100A.5.3.2.2 Random Access 1100A.5.3.2.2.1
4-step RA type contention based random access test in FR2 for
PSCell/SCell in EN-DC 1100A.5.3.2.2.2 4-step RA type non-contention
based random access test in FR2 for PSCell/SCell in EN-DC
1103A.5.3.2.2.3 2-step RA type contention based random access test in
FR2 for PSCell/SCell in EN-DC 1109A.5.3.2.2.4 2-step RA type
non-contention based random access test in FR2 for PSCell/SCell in EN-DC
1112A.5.3.2.3 Void 1116A.5.4 Timing 1116A.5.4.1 UE transmit timing
1116A.5.4.1.1 NR UE Transmit Timing Test for FR2 1116A.5.4.1.1.1 Test
Purpose and environment 1116A.5.4.1.1.2 Test requirements 1119A.5.4.2 UE
timer accuracy 1120A.5.4.3 Timing advance 1120A.5.4.3.1 EN-DC FR2 timing
advance adjustment accuracy 1120A.5.4.3.1.1 Test Purpose and Environment
1120A.5.4.3.1.2 Test Parameters 1120A.5.4.3.1.3 Test Requirements
1124A.5.5 Signaling characteristics 1124A.5.5.1 Radio link Monitoring
1124A.5.5.1.1 Radio Link Monitoring Out-of-sync Test for FR2 PSCell
configured with SSB-based RLM RS in non-DRX mode 1124A.5.5.1.1.1 Test
Purpose and Environment 1124A.5.5.1.1.2 Test Requirements 1128A.5.5.1.2
Radio Link Monitoring In-sync Test for FR2 PSCell configured with
SSB-based RLM RS in non-DRX mode 1129A.5.5.1.2.1 Test Purpose and
Environment 1129A.5.5.1.2.2 Test Requirements 1132A.5.5.1.3 Radio Link
Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM
RS in DRX mode 1133A.5.5.1.3.1 Test Purpose and Environment
1133A.5.5.1.3.2 Test Requirements 1137A.5.5.1.4 Radio Link Monitoring
In-sync Test for FR2 PSCell configured with SSB-based RLM RS in DRX mode
1137A.5.5.1.4.1 Test Purpose and Environment 1137A.5.5.1.4.2 Test
Requirements 1141A.5.5.1.5 EN-DC Radio Link Monitoring Out-of-sync Test
for FR2 PSCell configured with CSI-RS-based RLM in non-DRX mode
1141A.5.5.1.6 EN-DC Radio Link Monitoring In-sync Test for FR2 PSCell
configured with CSI-RS-based RLM in non-DRX mode 1145A.5.5.1.7 EN-DC
Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with
CSI-RS-based RLM in DRX mode 1149A.5.5.1.8 EN-DC Radio Link Monitoring
In-sync Test for FR2 PSCell configured with CSI-RS-based RLM in DRX mode
1154A.5.5.1.8.2 Test Requirements 1158A.5.5.1.9 EN-DC Radio Link
Monitoring UE Scheduling Restrictions on FR2 1159A.5.5.1.9.1 Test
Purpose and Environment 1159A.5.5.1.9.2 Test Requirements 1161A.5.5.2
Interruption 1161A.5.5.2.1 E-UTRAN -- NR FR2 interruptions at
transitions between active and non-active during DRX in synchronous
EN-DC 1161A.5.5.2.1.1 Test Purpose and Environment 1161A.5.5.2.1.2 Test
Requirements 1164A.5.5.2.2 E-UTRAN -- NR FR2 interruptions at
transitions between active and non-active during DRX in asynchronous
EN-DC 1164A.5.5.2.2.1 Test Purpose and Environment 1164A.5.5.2.2.2 Test
Requirements 1167**A.5.5.2.3** E-UTRAN -- NR FR2 interruptions during
measurements on deactivated NR SCC in synchronous EN-DC 1167A.5.5.2.3.1
Test Purpose and Environment 1167A.5.5.2.**3.2** Test Requirements
1171**A.5.5.2.4** E-UTRAN -- NR FR2 interruptions during measurements on
deactivated NR SCC in asynchronous EN-DC 1171A.5.5.2.4.1 Test Purpose
and Environment 1171A.5.5.2.**4.2** Test Requirements 1174**A.5.5.2.5**
E-UTRAN -- NR FR2 interruptions during measurements on deactivated
E-UTRAN SCC in synchronous EN-DC 1175A.5.5.2.5.1 Test Purpose and
Environment 1175A.5.5.2.**5.2** Test Requirements 1178**A.5.5.2.6**
E-UTRAN -- NR FR2 interruptions during measurements on deactivated
E-UTRAN SCC in asynchronous EN-DC 1179A.5.5.2.6.1 Test Purpose and
Environment 1179A.5.5.2.**6.2** Test Requirements 1181**A.5.5.2.7**
E-UTRAN -- NR FR2 interruptions at E-UTRA SRS carrier based switching
1182A.5.5.2.7.1 Test Purpose and Environment 1182A.5.5.2.7.2 Test
Requirements 1185A.5.5.2.8 E-UTRAN -- NR FR2 interruptions at NR SRS
carrier based switching 1185A.5.5.2.8.1 Test Purpose and Environment
1185A.5.5.2.8.3 Test Requirements 1188A.5.5.3 SCell Activation and
Deactivation Delay 1188A.5.5.3.1 SCell Activation and deactivation of
SCell in FR2 intra-band 1188A.5.5.3.1.1 Test Purpose and Environment
1188A.5.5.3.1.2 Test Requirements 1191A.5.5.3.2 SCell Activation and
deactivation of known SCell in FR1 for 160ms SCell measurement cycle
1191A.5.5.3.2.1 Test Purpose and Environment 1191A.5.5.3.2.2 Test
Requirements 1195A.5.5.3.3 Void 1195A.5.5.3.4 Void 1195A.5.5.3.5 SCell
Activation and deactivation of SCell in FR2 1195A.5.5.3.5.1 Test Purpose
and Environment 1195A.5.5.3.5.2 Test Requirements 1199A.5.5.3.6 Multiple
SCell Activation and deactivation of one unknown SCell and one known
SCell in FR2 1200A.5.5.3.6.1 Test Purpose and Environment
1200A.5.5.3.6.2 Test Requirements 1203A.5.5.3.7 Direct SCell activation
at SCell addition of known SCell in FR2 1204A.5.5.3.7.1 Test Purpose and
Environment 1204A.5.5.3.7.2 Test Requirements 1207A.5.5.4 Void
1207A.5.5.5 Beam Failure Detection and Link recovery procedures
1207A.5.5.5.1 EN-DC Beam Failure Detection and Link Recovery Test for
FR2 PSCell configured with SSB-based BFD and LR in non-DRX mode
1207A.5.5.5.1.1 Test Purpose and Environment 1207A.5.5.5.1.2 Test
Requirements 1211A.5.5.5.2 EN-DC Beam Failure Detection and Link
Recovery Test for FR2 PSCell configured with SSB-based BFD and LR in DRX
mode 1212A.5.5.5.2.1 Test Purpose and Environment 1212A.5.5.5.2.2 Test
Requirements 1216A.5.5.5.3 EN-DC Beam Failure Detection and Link
Recovery Test for FR2 PSCell configured with CSI-RS-based BFD and LR in
non-DRX mode 1217A.5.5.5.3.1 Test Purpose and Environment
1217A.5.5.5.3.2 Test Requirements 1221A.5.5.5.4 EN-DC Beam Failure
Detection and Link Recovery Test for FR2 PSCell configured with
CSI-RS-based BFD and LR in DRX mode 1222A.5.5.5.4.1 Test Purpose and
Environment 1222A.5.5.5.4.2 Test Requirements 1226A.5.5.5.5 EN-DC
scheduling availability restriction during Beam Failure Detection and
Link Recovery for FR2 PSCell configured with SSB-based BFD and LR in
non-DRX mode 1227A.5.5.5.5.1 Test Purpose and Environment
1227A.5.5.5.5.2 Test Requirements 1231A.5.5.5.6 EN-DC Beam Failure
Detection and Link Recovery Test for FR2 SCell configured with
CSI-RS-based BFD and LR in non-DRX mode 1231A.5.5.5.6.1 Test Purpose and
Environment 1231A.5.5.5.6.2 Test Requirements 1236A.5.5.5.7 EN-DC Beam
Failure Detection and Link Recovery Test for FR2 SCell configured with
CSI-RS-based BFD and LR in DRX mode 1237A.5.5.5.7.1 Test Purpose and
Environment 1237A.5.5.5.7.2 Test Requirements 1241A.5.5.6 Active BWP
switch 1242A.5.5.6.1 DCI-based and Timer-based Active BWP Switch
1242A.5.5.6.1.1 E-UTRAN -- NR PSCell FR2 DL active BWP switch with
non-DRX in synchronous EN-DC 1242A.5.5.6.1.1.1 Test Purpose and
Environment 1242A.**5.5.6.1.1**.2 Test Requirements 1245A.5.5.6.1.2
E-UTRAN -- NR PSCell FR2 with FR2 SCell DL active BWP switch in non-DRX
in synchronous EN-DC 1245A.5.5.6.2 RRC-based Active BWP Switch
1250A.5.5.6.3 Simultaneous DCI-based and Timer-based Active BWP Switch
on multiple CCs 1254A.5.5.6.3.1 E-UTRAN -- NR PSCell FR2 and NR SCell
FR2 DL active BWP switch on multiple CCs in synchronous EN-DC
1254A.5.5.6.3.1.1 Test Purpose and Environment 1254A.5.5.6.4 SCell
dormancy switch 1258A.5.5.6.4.1 E-UTRAN -- NR FR2 PSCell SCell dormancy
switch of single FR2 SCell inside active time 1258A.5.5.6.4.1.1 Test
Purpose and Environment 1258A.5.5.6.4.1.2 Test Requirements
1262A.5.5.6.4.2 E-UTRAN -- NR FR1 PSCell SCell dormancy switch of two
FR2 SCells outside active time 1262A.5.5.6.4.2.1 Test Purpose and
Environment 1262A.5.5.6.4.2.2 Test Requirements 1269A.5.5.6.5
Simultaneous RRC-based Active BWP Switch on multiple CCs 1269A.5.5.7
PSCell addition and release delay 1272A.5.5.7.1 Addition and Release
Delay of NR PSCell 1272A.5.5.7.1.1 Test purpose and environment
1272A.5.5.7.1.2 Test Requirements 1276A.5.5.8 Active TCI state switch
delay 1277A.5.5.8.1 MAC-CE based active TCI state switch 1277A.5.5.8.1.1
E-UTRAN -- NR PSCell FR2 active TCI state switch for a known TCI state
1277A.5.5.8.1.1.1 Test Purpose and Environment 1277A.5.5.8**.1.1**.2
Test Requirements 1281A.5.5.8.2 RRC based active TCI state switch
1281A.5.5.8.2.1 E-UTRAN -- NR PSCell FR2 active TCI state switch for a
known TCI state 1281A.5.5.8.2.1.1 Test Purpose and Environment
1281A.5.5.8.2**.1**.2 Test Requirements 1285A.5.5.9 Uplink spatial
relation switch delay 1285A.5.5.9.1 MAC-CE based uplink spatial relation
switch 1285A.5.5.9.1.1 E-UTRAN -- NR PSCell FR2 uplink spatial relation
switch for a known spatial relation 1285A.5.5.9.1.1.1 Test Purpose and
Environment 1285A.5.5.9**.1.1**.2 Test Requirements 1288A.5.5.9.2 RRC
based spatial relation switch 1288A.5.5.9.2.1 E-UTRAN -- NR PSCell FR2
spatial relation switch associated with a known DL-RS 1288A.5.5.9.2.1.1
Test Purpose and Environment 1288A.5.5.9.2**.1**.2 Test Requirements
1291A.5.5.10 UE specific CBW change 1291A.5.5.10.1 UE specific CBW
change on FR2 NR PSCell 1291A.5.5.10.1.1 Test Purpose and Environment
1291A.5.5.10.1.2 Test Requirements 1294A.5.6 Measurement procedure
1295A.5.6.1 Intra-frequency Measurements 1295A.5.6.1.1 EN-DC event
triggered reporting test without gap under non-DRX 1295A.5.6.1.1.1 Test
purpose and Environment 1295A.5.6.1.1.2 Test Requirements 1298A.5.6.1.2
EN-DC event triggered reporting test without gap under DRX
1298A.5.6.1.2.1 Test purpose and Environment 1298A.5.6.1.2.2 Test
Requirements 1300A.5.6.1.3 EN-DC event triggered reporting test with
per-UE gaps under non-DRX 1301A.5.6.1.3.1 Test purpose and Environment
1301A.5.6.1.3.2 Test Requirements 1305A.5.6.1.4 EN-DC event triggered
reporting test with per-UE gaps under DRX 1305A.5.6.1.4.1 Test purpose
and Environment 1305A.5.6.1.4.2 Test Requirements 1308A.5.6.2
Inter-frequency Measurements 1309A.5.6.2.1 EN-DC event triggered
reporting tests for FR2 cell without SSB time index detection when DRX
is not used 1309A.5.6.2.1.1 Test Purpose and Environment 1309A.5.6.2.1.2
Test Requirements 1312A.5.6.2.2 EN-DC event triggered reporting tests
for FR2 cell without SSB time index detection when DRX is used
1312A.5.6.2.2.1 Test Purpose and Environment 1312A.5.6.2.2.2 Test
Requirements 1316A.5.6.2.3 EN-DC event triggered reporting tests for FR2
cell with SSB time index detection when DRX is not used 1316A.5.6.2.3.1
Test Purpose and Environment 1316A.5.6.2.3.2 Test Requirements
1320A.5.6.2.4 EN-DC event triggered reporting tests for FR2 cell with
SSB time index detection when DRX is used 1320A.5.6.2.4.1 Test Purpose
and Environment 1320A.5.6.2.4.2 Test Requirements 1324A.5.6.2.5 EN-DC
event triggered reporting tests for FR2 cell without SSB time index
detection when DRX is not used 1324A.5.6.2.5.1 Test Purpose and
Environment 1324A.5.6.2.5.2 Test Requirements 1329A.5.6.2.6 EN-DC event
triggered reporting tests for FR2 cell without SSB time index detection
when DRX is used 1330A.5.6.2.6.1 Test Purpose and Environment
1330A.5.6.2.6.2 Test Requirements 1333A.5.6.2.7 EN-DC event triggered
reporting tests for FR2 cell with SSB time index detection when DRX is
not used 1334A.5.6.2.7.1 Test Purpose and Environment 1334A.5.6.2.7.2
Test Requirements 1338A.5.6.2.8 EN-DC event triggered reporting tests
for FR2 cell with SSB time index detection when DRX is used
1338A.5.6.2.8.1 Test Purpose and Environment 1338A.5.6.2.8.2 Test
Requirements 1343A.5.6.3 L1-RSRP measurement for beam reporting
1343A.5.6.3.1 SSB based L1-RSRP measurement when DRX is not used
1343A.5.6.3.1.1 Test Purpose and Environment 1343A.5.6.3.1.2 Test
parameters 1343A.5.6.3.1.3 Test Requirements 1345A.5.6.3.2 SSB based
L1-RSRP measurement when DRX is used 1345A.5.6.3.2.1 Test Purpose and
Environment 1345A.5.6.3.2.2 Test parameters 1346A.5.6.3.2.3 Test
Requirements 1348A.5.6.3.3 CSI-RS based L1-RSRP measurement when DRX is
not used 1348A.5.6.3.3.1 Test Purpose and Environment 1348A.5.6.3.3.2
Test parameters 1349A.5.6.3.3.3 Test Requirements 1351A.5.6.3.4 CSI-RS
based L1-RSRP measurement when DRX is used 1352A.5.6.3.4.1 Test Purpose
and Environment 1352A.5.6.3.4.2 Test parameters 1352A.5.6.3.4.3 Test
Requirements 1354A.5.6.4 CLI measurements 1355A.5.6.4.1 SRS-RSRP
measurement with DRX 1355A.5.6.4.1.1 Test Purpose and Environment
1355A.5.6.4.1.2 Test Parameters 1355A.5.6.4.1.3 Test Requirements
1357A.5.6.4.2 CLI-RSSI measurement with DRX 1357A.5.6.4.2.1 Test Purpose
and Environment 1357A.5.6.4.2.2 Test Parameters 1358A.5.6.4.2.3 Test
Requirements 1360A.5.6.5 Measurements with autonomous gaps 1360A.5.6.5.1
EN-DC inter-frequency CGI identification of NR neighbor cell in FR2
1360A.5.6.5.1.1 Test Purpose and Environment 1360A.5.6.5.1.2 Test
Requirements 1363A.5.6.6 L1-SINR measurement for beam reporting
1364A.5.6.6.1 L1-SINR measurement with CSI-RS based CMR and no dedicated
IMR configured when DRX is used 1364A.5.6.6.1.1 Test Purpose and
Environment 1364A.5.6.6.1.2 Test parameters 1364A.5.6.6.1.3 Test
Requirements 1366A.5.6.6.2 L1-SINR measurement with SSB based CMR and
dedicated IMR when DRX is not used 1366A.5.6.6.2.1 Test Purpose and
Environment 1366A.5.6.6.2.2 Test parameters 1367A.5.6.6.2.3 Test
Requirements 1370A.5.6.6.3 L1-SINR measurement with CSI-RS based CMR and
dedicated IMR configured when DRX is not used 1370A.5.6.6.3.1 Test
Purpose and Environment 1370A.5.6.6.3.2 Test parameters 1371A.5.6.6.3.3
Test Requirements 1373A.5.6.7 CSI-RS based Intra-frequency Measurements
1373A.5.6.7.1 EN-DC event triggered reporting test without gap under
non-DRX 1373A.5.6.7.1.1 Test purpose and Environment 1373A.5.6.7.1.2
Test Requirements 1376A.5.6.8 CSI-RS based Inter-frequency Measurements
1377A.5.6.8.1 EN-DC event triggered reporting tests for NR FR2 cell when
DRX is used 1377A.5.6.8.1.1 Test Purpose and Environment 1377A.5.6.8.1.2
Test Requirements 1380A.5.7 Measurement Performance requirements
1380A.5.7.1 SS-RSRP 1381A.5.7.1.1 EN-DC intra-frequency case measurement
accuracy with FR2 serving cell and FR2 target cell 1381A.5.7.1.1.1 Test
Purpose and Environment 1381A.5.7.1.1.2 Test parameters 1381A.5.7.1.1.3
Test Requirements 1383A.5.7.1.2 EN-DC inter-frequency case measurement
accuracy with FR2 serving cell and FR2 target cell 1384A.5.7.1.2.1 Test
Purpose and Environment 1384A.5.7.1.2.2 Test parameters 1384A.5.7.1.2.3
Test Requirements 1389A.5.7.1.3 EN-DC inter-frequency measurement
accuracy with FR1 serving cell and FR2 target cell 1390A.5.7.1.3.1 Test
Purpose and Environment 1390A.5.7.1.3.2 Test parameters 1390A.5.7.1.3.3
Test Requirements 1393A.5.7.2 SS-RSRQ 1394A.5.7.2.1 EN-DC
Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 1394A.5.7.2.1.1 Test Purpose and Environment 1394A.5.7.2.1.2
Test Parameters 1394A.5.7.2.1.3 Test Requirements 1396A.5.7.2.2 EN-DC
Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 1397A.5.7.2.2.1 Test Purpose and Environment 1397A.5.7.2.2.2
Test Parameters 1397A.5.7.2.2.3 Test Requirements 1399A.5.7.3 SS-SINR
1399A.5.7.3.1 EN-DC Intra-frequency measurement accuracy with FR2
serving cell and FR2 TDD target cell 1399A.5.7.3.1.1 Test Purpose and
Environment 1399A.5.7.3.1.2 Test Parameters 1399A.5.7.3.1.3 Test
Requirements 1401A.5.7.3.2 EN-DC Inter-frequency measurement accuracy
with FR2 serving cell and FR2 TDD target cell 1401A.5.7.3.2.1 Test
Purpose and Environment 1401A.5.7.3.2.2 Test Parameters 1401A.5.7.3.2.3
Test Requirements 1403A.5.7.4 L1-RSRP measurement for beam reporting
1403A.5.7.4.1 SSB based L1-RSRP measurement 1403A.5.7.4.1.1 Test Purpose
and Environment 1403A.5.7.4.1.2 Test parameters 1404A.5.7.4.1.3 Test
Requirements 1406A.5.7.4.2 CSI-RS based L1-RSRP measurement on resource
set with repetition off 1407A.5.7.4.2.1 Test Purpose and Environment
1407A.5.7.4.2.2 Test parameters 1407A.5.7.4.2.3 Test Requirements
1409A.5.7.5 CLI measurements 1410A.5.7.5.1 EN-DC SRS-RSRP measurement
accuracy with FR2 serving cell 1410A.5.7.5.1.1 Test Purpose and
Environment 1410A.5.7.5.1.2 Test parameters 1410A.5.7.5.1.3 Test
Requirements 1413A.5.7.5.2 EN-DC CLI-RSSI measurement accuracy with FR2
serving cell 1414A.5.7.5.2.1 Test Purpose and Environment
1414A.5.7.5.2.2 Test parameters 1414A.5.7.5.2.3 Test Requirements
1416A.5.7.6 L1-SINR measurement for beam reporting 1417A.5.7.6.1 L1-SINR
measurement with CSI-RS based CMR and no dedicated IMR configured and
CSI-RS resource set with repetition off 1417A.5.7.6.1.1 Test Purpose and
Environment 1417A.5.7.6.1.2 Test parameters 1417A.5.7.6.1.3 Test
Requirements 1419A.5.7.6.2 L1-SINR measurement with SSB based CMR and
dedicated IMR 1420A.5.7.6.2.1 Test Purpose and Environment
1420A.5.7.6.2.2 Test parameters 1420A.5.7.6.2.3 Test Requirements
1422A.5.7.6.3 L1-SINR measurement with CSI-RS based CMR and dedicated
IMR 1423A.5.7.6.3.1 Test Purpose and Environment 1423A.5.7.6.3.2 Test
parameters 1423A.5.7.6.3.3 Test Requirements 1425A.5.7.7 CSI-RSRP
1426A.5.7.7.1 EN-DC intra-frequency case measurement accuracy with FR2
serving cell and FR2 target cell 1426A.5.7.7.1.2 Test parameters
1426A.5.7.7.1.3 Test Requirements 1430A.5.7.7.2 EN-DC inter-frequency
case measurement accuracy with FR2 serving cell and FR2 target cell
1431A.5.7.7.2.1 Test Purpose and Environment 1431A.5.7.7.2.2 Test
parameters 1431A.5.7.7.2.3 Test Requirements 1435A.5.7.8 CSI-RSRQ
1436A.5.7.8.1 EN-DC Intra-frequency measurement accuracy with FR2
serving cell and FR2 target cell 1436A.5.7.8.1.1 Test Purpose and
Environment 1436A.5.7.8.1.2 Test Parameters 1436A.5.7.8.1.3 Test
Requirements 1438A.5.7.8.2 EN-DC Inter-frequency measurement accuracy
with FR2 serving cell and FR2 TDD target cell 1438A.5.7.8.2.1 Test
Purpose and Environment 1438A.5.7.8.2.2 Test Parameters 1438A.5.7.9
CSI-SINR 1440A.5.7.9.1 EN-DC Intra-frequency measurement accuracy with
FR2 serving cell and FR2 TDD target cell 1440A.5.7.9.1.1 Test Purpose
and Environment 1440A.5.7.9.1.2 Test Parameters 1441Table A.5.7.9.1.2-1:
CSI-SINR Intra frequency CSI-SINR supported test configurations
1441A.5.7.9.1.3 Test Requirements 1443A.5.7.9.2 EN-DC Inter-frequency
measurement accuracy with FR2 serving cell and FR2 TDD target cell
1443A.5.7.9.2.1 Test Purpose and Environment 1443A.5.7.9.2.2 Test
Parameters 1443A.5.7.9.2.3 Test Requirements 1446A.5.8 Void 1446A.6 NR
standalone tests with all NR cells in FR1 1446A.6.1 SA: RRC\_IDLE state
mobility 1446A.6.1.1 Cell re-selection to NR 1446A.6.1.1.1 Cell
reselection to FR1 intra-frequency NR case 1446A.6.1.1.1.1 Test Purpose
and Environment 1446A.6.1.1.1.2 Test Parameters 1446A.6.1.1.1.3 Test
Requirements 1450A.6.1.1.2 Cell reselection to FR1 inter-frequency NR
case 1450A.6.1.1.2.1 Test Purpose and Environment 1450A.6.1.1.2.2 Test
Parameters 1450A.6.1.1.2.3 Test Requirements 1454A.6.1.1.3 Cell
reselection to FR1 intra-frequency NR case for UE fulfilling low
mobility relaxed measurement criterion 1454A.6.1.1.3.1 Test Purpose and
Environment 1454A.6.1.1.3.2 Test Parameters 1454A.6.1.1.3.3 Test
Requirements 1459A.6.1.1.4 Cell reselection to FR1 intra-frequency NR
case for UE fulfilling not-at-cell edge relaxed measurement criterion
1459A.6.1.1.4.1 Test Purpose and Environment 1459A.6.1.1.4.2 Test
Parameters 1459A.6.1.1.4.3 Test Requirements 1463A.6.1.1.5 Cell
reselection to FR1 inter-frequency NR case for UE fulfilling low
mobility relaxed measurement criterion 1463A.6.1.1.5.1 Test Purpose and
Environment 1463A.6.1.1.5.2 Test Parameters 1463A.6.1.1.5.3 Test
Requirements 1467A.6.1.1.6 Cell reselection to FR1 inter-frequency NR
case for UE fulfilling not-at-cell edge relaxed measurement criterion
1467A.6.1.1.6.1 Test Purpose and Environment 1467A.6.1.1.6.2 Test
Parameters 1468A.6.1.1.6.3 Test Requirements 1472A.6.1.1.7 Cell
reselection to FR1 intra-frequency NR case for UE configured with
***highSpeedMeasFlag-r16*** 1473A.6.1.1.7.1 Test Purpose and Environment
1473A.6.1.1.7.2 Test Parameters 1473A.6.1.1.7.3 Test Requirements
1477A.6.1.2 Inter-RAT E-UTRAN cell re-selection 1477A.6.1.2.1 Cell
reselection to higher priority E-UTRAN 1477A.6.1.2.1.1 Test Purpose and
Environment 1477A.6.1.2.1.2 Test Parameters 1477A.6.1.2.1.3 Test
Requirements 1480A.6.1.2.2 Cell reselection to lower priority E-UTRAN
1481A.6.1.2.2.1 Test Purpose and Environment 1481A.6.1.2.2.2 Test
Parameters 1481A.6.1.2.2.3 Test Requirements 1484A.6.1.2.3 Cell
reselection to lower priority E-UTRAN for UE fulfilling low mobility
relaxed measurement criterion 1485A.6.1.2.3.1 Test Purpose and
Environment 1485A.6.1.2.3.2 Test Parameters 1485A.6.1.2.3.3 Test
Requirements 1488A.6.1.2.4 Cell reselection to lower priority E-UTRAN
for UE fulfilling not-at-cell edge relaxed measurement criterion
1489A.6.1.2.4.1 Test Purpose and Environment 1489A.6.1.2.4.2 Test
Parameters 1489A.6.1.2.4.3 Test Requirements 1492A.6.1.2.5.3 Test
Requirements 1496A.6.2 SA: RRC\_INACTIVE state mobility 1497A.6.3
RRC\_CONNECTED state mobility 1497A.6.3.1 Handover 1497A.6.3.1.1
Intra-frequency handover from FR1 to FR1; known target cell
1497A.6.3.1.1.1 Test Purpose and Environment 1497A.6.3.1.1.2 Test
Parameters 1497A.6.3.1.1.3 Test Requirements 1501A.6.3.1.2
Intra-frequency handover from FR1 to FR1; unknown target cell
1501A.6.3.1.2.1 Test Purpose and Environment 1501A.6.3.1.2.2 Test
Parameters 1501A.6.3.1.2.3 Test Requirements 1505A.6.3.1.3
Inter-frequency handover from FR1 to FR1; unknown target cell
1505A.6.3.1.3.1 Test Purpose and Environment 1505A.6.3.1.3.2 Test
Parameters 1505A.6.3.1.3.3 Test Requirements 1509A.6.3.1.4 SA NR -
E-UTRAN handover 1509A.6.3.1.4.1 Test Purpose and Environment
1509A.6.3.1.4.2 Test Requirements 1515A.6.3.1.5 SA NR - E-UTRAN handover
with unknown target cell 1515A.6.3.1.5.1 Test Purpose and Environment
1515A.6.3.1.5.2 Test Requirements 1521A.6.3.1.6 SA NR - UTRAN FDD
handover 1521A.6.3.1.6.1 Test Purpose and Environment 1521A.6.3.1.6.2
Test Requirements 1525A.6.3.1.7 Intra-frequency synchronous DAPS
handover in FR1 1525A.6.3.1.7.1 Test Purpose and Environment
1525A.6.3.1.7.2 Test Parameters 1525A.6.3.1.7.3 Test Requirements
1529A.6.3.1.8 Intra-frequency asynchronous DAPS handover in FR1
1530A.6.3.1.8.1 Test Purpose and Environment 1530A.6.3.1.8.2 Test
Parameters 1530A.6.3.1.8.3 Test Requirements 1534A.6.3.1.9 Intra-band
inter-frequency synchronous DAPS handover test in SA for FR1
1535A.6.3.1.9.1 Test Purpose and Environment 1535A.6.3.1.9.2 Test
Parameters 1535A.6.3.1.9.3 Test Requirements 1539A.6.3.1.10 Intra-band
inter-frequency asynchronous DAPS handover test in SA for FR1
1539A.6.3.1.10.1 Test Purpose and Environment 1539A.6.3.1.10.2 Test
Parameters 1539A.6.3.1.10.3 Test Requirements 1542A.6.3.1.11 Inter-band
inter-frequency synchronous DAPS handover from FR1 to FR1
1542A.6.3.1.11.1 Test Purpose and Environment 1542A.6.3.1.11.2 Test
Parameters 1542A.6.3.1.11.3 Test Requirements 1549A.6.3.1.12 Inter-band
inter-frequency asynchronous DAPS handover from FR1 to FR1
1549A.6.3.1.12.1 Test Purpose and Environment 1549A.6.3.1.12.2 Test
Parameters 1549A.6.3.1.12.3 Test Requirements 1557A.6.3.2 RRC Connection
Mobility Control 1557A.6.3.2.1 SA: RRC Re-establishment 1557A.6.3.2.1.1
Intra-frequency RRC Re-establishment in FR1 1557A.6.3.2.1.2
Inter-frequency RRC Re-establishment in FR1 1561A.6.3.2.1.3
Intra-frequency RRC Re-establishment in FR1 without serving cell timing
1565A.6.3.2.2 Random Access 1569A.6.3.2.2.1 4-step RA type contention
based random access test in FR1 for NR standalone 1569A.6.3.2.2.2 4-step
RA type non-contention based random access test in FR1 for NR standalone
1574A.6.3.2.2.3 2-step RA type contention based random access test in
FR1 for NR standalone 1578A.6.3.2.2.4 2-step RA type non-contention
based test in FR1 for NR standalone 1583A.6.3.2.3 SA: RRC Connection
Release with Redirection 1587A.6.3.2.3.1 Redirection from NR in FR1 to
NR in FR1 1587A.6.3.2.3.2 Redirection from NR in FR1 to E-UTRAN
1591A.6.3.3 Conditional handover 1598A.6.3.3.1 Intra-frequency
conditional handover from FR1 to FR1 1598A.6.3.3.1.1 Test Purpose and
Environment 1598A.6.3.3.1.2 Test Parameters 1598A.6.3.3.1.3 Test
Requirements 1602A.6.3.3.2 Inter-frequency conditional handover from FR1
to FR1 1602A.6.3.3.2.1 Test Purpose and Environment 1602A.6.3.3.2.2 Test
Parameters 1602A.6.3.3.2.3 Test Requirements 1606A.6.4 Timing
1606A.6.4.1 UE transmit timing 1606A.6.4.1.1 NR UE Transmit Timing Test
for FR1 1606A.6.4.1.1.1 Test Purpose and environment 1606A.6.4.1.1.2
Test requirements 1610A.6.4.2 UE timer accuracy 1610A.6.4.3 Timing
advance 1610A.6.4.3.1 SA FR1 timing advance adjustment accuracy
1610A.6.4.3.1.1 Test Purpose and Environment 1610A.6.4.3.1.2 Test
Parameters 1610A.6.4.3.1.3 Test Requirements 1614A.6.5 Signalling
characteristics 1614A.6.5.1 Radio link Monitoring 1614A.6.5.1.1 Radio
Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based
RLM RS in non-DRX mode 1615A.6.5.1.1.1 Test Purpose and Environment
1615A.6.5.1.1.2 Test Requirements 1620A.6.5.1.2 Radio Link Monitoring
In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX
mode 1620A.6.5.1.2.1 Test Purpose and Environment 1620A.6.5.1.2.2 Test
Requirements 1626A.6.5.1.3 Radio Link Monitoring Out-of-sync Test for
FR1 PCell configured with SSB-based RLM RS in DRX mode 1626A.6.5.1.3.1
Test Purpose and Environment 1626A.6.5.1.3.2 Test Requirements
1632A.6.5.1.4 Radio Link Monitoring In-sync Test for FR1 PCell
configured with SSB-based RLM RS in DRX mode 1632A.6.5.1.4.1 Test
Purpose and Environment 1632A.6.5.1.4.2 Test Requirements 1638A.6.5.1.5
Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with
CSI-RS-based RLM in non-DRX mode 1638A.6.5.1.5.1 Test Purpose and
Environment 1638A.6.5.1.5.2 Test Requirements 1644A.6.5.1.6 Radio Link
Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM
in non-DRX mode 1644A.6.5.1.6.1 Test Purpose and Environment
1644A.6.5.1.6.2 Test Requirements 1649A.6.5.1.7 Radio Link Monitoring
Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX
mode 1649A.6.5.1.7.1 Test Purpose and Environment 1649A.6.5.1.7.2 Test
Requirements 1653A.6.5.1.8 Radio Link Monitoring In-sync Test for FR1
PCell configured with CSI-RS-based RLM in DRX mode 1653A.6.5.1.8.1 Test
Purpose and Environment 1653A.6.5.1.8.2 Test Requirements 1659A.6.5.2
Interruption 1659**A.6.5.2.1** Interruptions during measurements on
deactivated NR SCC in FR1 1659**A.6.5.2.1**.2 Test Requirements
1663A.6.5.2.2 SA interruptions at NR SRS carrier based switching
1664A.6.5.2.2.1 Test Purpose and Environment 1664A.6.5.2.2.2 Test
Parameters 1664A.6.5.2.2.3 Test Requirements 1666A.6.5.3 SCell
Activation and Deactivation Delay 1667A.6.5.3.1 SCell Activation and
deactivation of known SCell in FR1 in non-DRX for 160ms SCell
measurement cycle 1667A.6.5.3.1.1 Test Purpose and Environment
1667A.6.5.3.1.2 Test Requirements 1672A.6.5.3.2 SCell Activation and
deactivation of known SCell in FR1 in non-DRX for 640 ms SCell
measurement cycle 1673A.6.5.3.2.1 Test Purpose and Environment
1673A.6.5.3.2.2 Test Requirements 1673A.6.5.3.3 SCell Activation and
deactivation of unknown SCell in FR1 in non-DRX 1673A.6.5.3.3.1 Test
Purpose and Environment 1673A.6.5.3.3.2 Test Requirements 1674A.6.5.3.4
Direct SCell activation at SCell addition of known SCell in FR1
1674A.6.5.3.4.1 Test Purpose and Environment 1674A.6.5.3.4.2 Test
Requirements 1679A.6.5.3.5 Direct SCell activation at handover with
known SCell in FR1 1679A.6.5.3.5.1 Test Purpose and Environment
1679A.6.5.3.5.2 Test Requirements 1684A.6.5.4 UE UL carrier RRC
reconfiguration Delay 1685A.6.5.4.1 UE UL carrier RRC reconfiguration
Delay 1685A.6.5.4.1.1 Test Purpose and Environment 1685A.6.5.4.1.2 Test
Requirements 1693A.6.5.4.2 Void 1694A.6.5.5 Beam Failure Detection and
Link recovery procedures 1694A.6.5.5.1 Beam Failure Detection and Link
Recovery Test for FR1 PCell configured with SSB-based BFD and LR in
non-DRX mode 1694A.6.5.5.1.1 Test Purpose and Environment
1694A.6.5.5.1.2 Test Requirements 1699A.6.5.5.2 Beam Failure Detection
and Link Recovery Test for FR1 PCell configured with SSB-based BFD and
LR in DRX mode 1700A.6.5.5.2.1 Test Purpose and Environment
1700A.6.5.5.2.2 Test Requirements 1706A.6.5.5.3 Beam Failure Detection
and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD
and LR in non-DRX mode 1707A.6.5.5.3.1 Test Purpose and Environment
1707A.6.5.5.3.2 Test Requirements 1712A.6.5.5.4 Beam Failure Detection
and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD
and LR in DRX mode 1713A.6.5.5.4.1 Test Purpose and Environment
1713A.6.5.5.4.2 Test Requirements 1718A.6.5.5.5 Beam Failure Detection
and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD
and SSB-based LR in non-DRX mode 1719A.6.5.5.5.1 Test Purpose and
Environment 1719A.6.5.5.5.2 Test Requirements 1723A.6.5.5.6 Beam Failure
Detection and Link Recovery Test for FR1 SCell configured with
CSI-RS-based BFD and SSB-based LR in DRX mode 1723A.6.5.5.6.1 Test
Purpose and Environment 1723A.6.5.5.6.2 Test Requirements 1727A.6.5.6
Active BWP switch 1728A.6.5.6.1 DCI-based and Timer-based Active BWP
Switch 1728A.6.5.6.1.1 NR FR1- NR FR1 DL active BWP switch of SCell with
non-DRX in SA 1728A.6.5.6.1.2 NR FR1 DL active BWP switch with non-DRX
in SA 1735A.6.5.6.2 RRC-based Active BWP Switch 1739A.6.5.6.2.1 NR FR1
DL active BWP switch of Cell with non-DRX in SA 1739A.6.5.6.3
Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs
1743A.6.5.6.3.1 NR FR1- NR FR1 DL active BWP switch on multiple CCs with
non-DRX in SA 1743A.6.5.6.4 SCell dormancy switch 1750A.6.5.6.4.1 NR FR1
PCell SCell dormancy switch of single FR1 SCell outside active time
1750A.6.5.6.4.2 NR FR1 PCell SCell dormancy switch of two FR1 SCells
inside active time 1756A.6.5.6.5 Simultaneous RRC-based Active BWP
Switch on multiple CCs 1763A.6.5.6.5.1 NR FR1- NR FR1 DL active BWP
switch on multiple CCs with non-DRX in SA 1763A.6.5.7 DL interruptions
at switching between two uplink carriers 1768A.6.5.7.1 DL interruptions
at switching between two uplink carriers in FDD-TDD CA 1768A.6.5.7.1.1
Test Purpose and Environment 1768A.6.5.7.1.2 Test Requirements
1772A.6.5.7.2 DL interruptions at switching between two uplink carriers
in TDD-TDD CA 1772A.6.5.7.2.1 Test Purpose and Environment
1772A.6.5.7.2.2 Test Requirements 1776A.6.5.8 UE specific CBW change
1776A.6.5.8.1 UE specific CBW change on PCell in FR1 in non-DRX
1776A.6.5.8.1.1 Test Purpose and Environment 1776A.6.5.8.1.2 Test
Requirements 1780A.6.5.9 Pathloss reference signal switching delay
1780A.6.5.9.1 MAC-CE based pathloss reference signal switch delay
1780A.6.5.9.1.1 Test Purpose and Environment 1780A.6.5.9.1.2 Test
Requirements 1783A.6.6 Measurement procedure 1784A.6.6.1 Intra-frequency
Measurements 1784A.6.6.1.1 SA event triggered reporting tests without
gap under non-DRX 1784A.6.6.1.1.1 Test purpose and Environment
1784A.6.6.1.1.2 Test parameters 1784A.6.6.1.1.3 Test Requirements
1788A.6.6.1.2 SA event triggered reporting tests without gap under DRX
1788A.6.6.1.2.1 Test purpose and Environment 1788A.6.6.1.2.2 Test
parameters 1788A.6.6.1.2.3 Test Requirements 1792A.6.6.1.3 SA event
triggered reporting tests with per-UE gaps under non-DRX 1792A.6.6.1.3.1
Test purpose and Environment 1792A.6.6.1.3.2 Test parameters
1792A.6.6.1.3.3 Test Requirements 1796A.6.6.1.4 SA event triggered
reporting tests with per-UE gaps under DRX 1796A.6.6.1.4.1 Test purpose
and Environment 1796A.6.6.1.4.2 Test parameters 1796A.6.6.1.4.3 Test
Requirements 1800A.6.6.1.5 SA event triggered reporting tests without
gap under non-DRX with SSB index reading 1800A.6.6.1.5.1 Test purpose
and Environment 1800A.6.6.1.5.2 Test parameters 1800A.6.6.1.5.3 Test
Requirements 1802A.6.6.1.6 SA event triggered reporting tests with
per-UE gaps under non-DRX with SSB index reading 1803A.6.6.1.6.1 Test
purpose and Environment 1803A.6.6.1.6.2 Test parameters 1803A.6.6.1.6.3
Test Requirements 1804A.6.6.1.7 SA event triggered reporting tests under
DRX for UE configured with highSpeedMeasFlag-r16 1805A.6.6.1.7.1 Test
purpose and Environment 1805A.6.6.1.7.2 Test parameters 1805A.6.6.1.7.3
Test Requirements 1809A.6.6.2 Inter-frequency Measurements 1809A.6.6.2.1
SA event triggered reporting tests for FR1 without SSB time index
detection when DRX is not used 1809A.6.6.2.1.1 Test Purpose and
Environment 1809A.6.6.2.1.2 Test Requirements 1813A.6.6.2.2 SA event
triggered reporting tests for FR1 without SSB time index detection when
DRX is used 1813A.6.6.2.2.1 Test Purpose and Environment 1813A.6.6.2.2.2
Test Requirements 1817A.6.6.2.3 Void 1818A.6.6.2.4 Void 1818A.6.6.2.5 SA
event triggered reporting tests for FR1 with SSB time index detection
when DRX is not used 1818A.6.6.2.5.1 Test Purpose and Environment
1818A.6.6.2.5.2 Test Requirements 1822A.6.6.2.6 SA event triggered
reporting tests for FR1 with SSB time index detection when DRX is used
1822A.6.6.2.6.1 Test Purpose and Environment 1822A.6.6.2.6.2 Test
Requirements 1826A.6.6.2.7 Void 1827A.6.6.2.8 Void 1827A.6.6.2.9 SA
event triggered reporting tests with additional mandatory gap pattern
1827A.6.6.2.9.1 Test Purpose and Environment 1827A.6.6.2.9.2 Test
Requirements 1830A.6.6.2.10 SA event triggered reporting tests for FR1
when DRX is used 1830A.6.6.2.10.1 Test Purpose and Environment
1830A.6.6.2.10.2 Test Requirements 1834A.6.6.2.11 SA event triggered
reporting tests for FR1 without gap when DRX is not used
1835A.6.6.2.11.1 Test Purpose and Environment 1835A.6.6.2.11.2 Test
Requirements 1838A.6.6.3 Inter-RAT Measurements 1838A.6.6.3.1 SA NR -
E-UTRAN event-triggered reporting in non-DRX in FR1 1838A.6.6.3.1.1 Test
Purpose and Environment 1838A.6.6.3.1.2 Test Requirements 1844A.6.6.3.2
SA NR - E-UTRAN event-triggered reporting in DRX in FR1 1844A.6.6.3.2.1
Test Purpose and Environment 1844A.6.6.3.2.2 Test Requirements
1851A.6.6.3.3 SA NR - E-UTRAN event-triggered reporting in DRX in FR1
for UE configured with highSpeedMeasFlag-r16 1851A.6.6.3.3.1 Test
Purpose and Environment 1851A.6.6.3.3.2 Test Requirements 1858A.6.6.4
L1-RSRP measurement for beam reporting 1858A.6.6.4.1 SSB based L1-RSRP
measurement when DRX is not used 1858A.6.6.4.1.1 Test Purpose and
Environment 1858A.6.6.4.1.2 Test parameters 1858A.6.6.4.1.3 Test
Requirements 1861A.6.6.4.2 SSB based L1-RSRP measurement when DRX is
used 1861A.6.6.4.2.1 Test Purpose and Environment 1861A.6.6.4.2.2 Test
parameters 1862A.6.6.4.2.3 Test Requirements 1865A.6.6.4.3 CSI-RS based
L1-RSRP measurement when DRX is not used 1865A.6.6.4.3.1 Test Purpose
and Environment 1865A.6.6.4.3.2 Test parameters 1866A.6.6.4.3.3 Test
Requirements 1869A.6.6.4.4 CSI-RS based L1-RSRP measurement when DRX is
used 1869A.6.6.4.4.1 Test Purpose and Environment 1869A.6.6.4.4.2 Test
parameters 1870A.6.6.4.4.3 Test Requirements 1873A.6.6.4.5 SSB based
L1-RSRP measurement when DRX is used for UE configured with
*highSpeedMeasFlag-r16* 1873A.6.6.4.5.1 Test Purpose and Environment
1873A.6.6.4.5.2 Test parameters 1874A.6.6.4.5.3 Test Requirements
1877A.6.6.5 1877A.6.6.5.1 SA NR - UTRAN FDD event-triggered reporting in
non-DRX in FR1 1877A.6.6.5.1.1 Test Purpose and Environment
1877A.6.6.5.1.2 Test Requirements 1881A.6.6.6 CLI measurements
1881A.6.6.6.1 SRS-RSRP measurement with DRX 1881A.6.6.6.1.1 Test Purpose
and Environment 1881A.6.6.6.1.2 Test Parameters 1882A.6.6.6.1.3 Test
Requirements 1885A.6.6.6.2 CLI-RSSI measurement with DRX 1885A.6.6.6.2.1
Test Purpose and Environment 1885A.6.6.6.2.2 Test Parameters
1886A.6.6.6.2.3 Test Requirements 1888A.6.6.7 NR measurements with
autonomous gaps 1888A.6.6.7.1 SA intra-frequency CGI identification of
NR neighbor cell in FR1 1888A.6.6.7.1.1 Test Purpose and Environment
1888A.6.6.7.1.2 Test Parameters 1888A.6.6.7.1.3 Test Requirements
1891A.6.6.7.2 Identification of a new CGI of inter-RAT E-UTRA cell using
autonomous gaps in NR SA 1891A.6.6.7.2.1 Test Purpose and Environment
1891A.6.6.7.2.2 Test Requirements 1894A.6.6.8 L1-SINR measurement for
beam reporting 1895A.6.6.8.1 L1-SINR measurement with CSI-RS based CMR
and no dedicated IMR configured when DRX is used 1895A.6.6.8.1.1 Test
Purpose and Environment 1895A.6.6.8.2 L1-SINR measurement with SSB based
CMR and dedicated IMR when DRX is not used 1898A.6.6.8.2.1 Test Purpose
and Environment 1898A.6.6.8.2.2 Test parameters 1899A.6.6.8.2.3 Test
Requirements 1903A.6.6.8.3 L1-SINR measurement with CSI-RS based CMR and
dedicated IMR configured when DRX is not used 1903A.6.6.8.3.1 Test
Purpose and Environment 1903A.6.6.8.3.2 Test parameters 1904A.6.6.8.3.3
Test Requirements 1907A.6.6.9 Idle Mode CA/DC Measurements 1907A.6.6.9.1
SA Idle mode CA/DC measurement for FR1 1907A.6.6.9.1.1 Test Purpose and
Environment 1907A.6.6.9.1.2 Test Requirements 1914A.6.6.10 CSI-RS based
intra-frequency Measurements 1914A.6.6.10.1 SA event triggered reporting
tests without gap under non-DRX 1914A.6.6.10.1.1 Test purpose and
Environment 1914A.6.6.10.1.2 Test Requirements 1918A.6.6.11 CSI-RS based
inter-frequency Measurements 1918A.6.6.11.1 SA event triggered reporting
tests with gap under DRX 1918A.6.6.11.1.1 Test Purpose and Environment
1918A.6.6.11.1.2 Test Requirements 1922A.6.6.12 RSTD measurements 1922A.
6.6.12.1 NR RSTD measurement reporting delay test case for single
positioning frequency layer in FR1 SA 1922A. 6.6.12.1.1 Test Purpose and
Environment 1922A.6.6.12.1.2 Test Requirements 1930A. 6.6.12.2 NR RSTD
measurement reporting delay test case for dual positioning frequency
layers in FR1 SA 1930A. 6.6.12.2.1 Test Purpose and Environment
1930A.6.6.12.2.2 Test Requirements 1937A.6.6.13 PRS-RSRP measurements
1937A.6.6.13.1 PRS-RSRP reporting delay test case for single positioning
frequency layer 1937A.6.6.13.1.1 Test purpose and Environment
1937A.6.6.13.1.2 Test Requirements 1941A.6.6.13.2 PRS-RSRP reporting
delay test case for dual positioning frequency layer 1941A.6.6.13.2.1
Test purpose and Environment 1941A.6.6.13.2.2 Test Requirements
1945A.6.6.14 UE Rx-Tx time difference measurements 1945A.6.6.14.1 UE
Rx-Tx time difference measurement for single positioning frequency layer
in FR1 SA 1945A.6.6.14.1.1 Test purpose and environment 1945A.6.6.14.1.2
Test requirements 1949A.6.6.14.2 UE Rx-Tx time difference measurement
for dual positioning frequency layers in FR1 SA 1949A.6.6.14.2.1 Test
purpose and environment 1949A.6.6.14.2.2 Test requirements 1953A.6.6.15
Idle Mode measurements of inter-RAT DC candidate cells for early
reporting 1953A.6.6.15.1 Test Purpose and Environment 1953A.6.6.15.2
Test Requirements 1961A.6.7 Measurement Performance requirements
1962A.6.7.1 SS-RSRP 1962A.6.7.1.1 SA: intra-frequency case measurement
accuracy with FR1 serving cell and FR1 target cell 1962A.6.7.1.1.1 Test
Purpose and Environment 1962A.6.7.1.1.2 Test parameters 1962A.6.7.1.1.3
Test Requirements 1967A.6.7.1.2 SA inter-frequency case measurement
accuracy with FR1 serving cell and FR1 target cell 1967A.6.7.1.2.1 Test
Purpose and Environment 1967A.6.7.1.2.2 Test parameters 1967A.6.7.1.2.3
Test Requirements 1971A.6.7.1.3 Void 1971A.6.7.2 SS-RSRQ 1971A.6.7.2.1
SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1
target cell 1971A.6.7.2.1.1 Test Purpose and Environment 1971A.6.7.2.1.2
Test Parameters 1972A.6.7.2.1.3 Test Requirements 1977A.6.7.2.2 SA
Inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell 1977A.6.7.2.2.1 Test Purpose and Environment 1977A.6.7.2.2.2
Test Parameters 1977A.6.7.2.2.3 Test Requirements 1982A.6.7.3 SS-SINR
1982A.6.7.3.1 SA intra-frequency measurement accuracy with FR1 serving
cell and FR1 target cell 1982A.6.7.3.1.1 Test Purpose and Environment
1982A.6.7.3.1.2 Test Parameters 1982A.6.7.3.1.3 Test Requirements
1986A.6.7.3.2 SA Inter-frequency measurement accuracy with FR1 serving
cell and FR1 target cell 1986A.6.7.3.2.1 Test Purpose and Environment
1986A.6.7.3.2.2 Test Parameters 1987A.6.7.3.2.3 Test Requirements
1991A.6.7.4 L1-RSRP measurement for beam reporting 1992A.6.7.4.1 SSB
based L1-RSRP measurement 1992A.6.7.4.1.1 Test Purpose and Environment
1992A.6.7.4.1.2 Test parameters 1992A.6.7.4.1.3 Test Requirements
1996A.6.7.4.2 CSI-RS based L1-RSRP measurement on resource set with
repetition off 1996A.6.7.4.2.1 Test Purpose and Environment
1996A.6.7.4.2.2 Test parameters 1997A.6.7.4.2.3 Test Requirements
2001A.6.7.5 E-UTRAN RSRP 2001A.6.7.5.1 SA: inter-RAT measurement
accuracy with FR1 serving cell 2001A.6.7.5.1.1 Test Purpose and
Environment 2001A.6.7.5.1.2 Test parameters 2002A.6.7.5.1.3 Test
Requirements 2008A.6.7.6 E-UTRAN RSRQ 2009A.6.7.6.1 SA: inter-RAT
measurement accuracy with FR1 serving cell 2009A.6.7.6.1.1 Test Purpose
and Environment 2009A.6.7.6.1.2 Test parameters 2009A.6.7.6.1.3 Test
Requirements 2014A.6.7.7 E-UTRAN RS-SINR 2015A.6.7.7.1 SA: inter-RAT
measurement accuracy with FR1 serving cell 2015A.6.7.7.1.1 Test Purpose
and Environment 2015A.6.7.7.1.2 Test parameters 2015A.6.7.7.1.3 Test
Requirements 2021A.6.7.8 CLI measurements 2022A.6.7.8.1 SA SRS-RSRP
measurement accuracy with FR1 serving cell 2022A.6.7.8.1.1 Test Purpose
and Environment 2022A.6.7.8.1.2 Test parameters 2022A.6.7.8.1.3 Test
Requirements 2028A.6.7.8.2 SA CLI-RSSI measurement accuracy with FR1
serving cell 2028A.6.7.8.2.1 Test Purpose and Environment
2028A.6.7.8.2.2 Test parameters 2029A.6.7.8.2.3 Test Requirements
2032A.6.7.9 L1-SINR measurement for beam reporting 2033A.6.7.9.1 L1-SINR
measurement with CSI-RS based CMR and no dedicated IMR configured and
CSI-RS resource set with repetition off 2033A.6.7.9.1.1 Test Purpose and
Environment 2033A.6.7.9.1.2 Test parameters 2033A.6.7.9.1.3 Test
Requirements 2037A.6.7.9.2 L1-SINR measurement with SSB based CMR and
dedicated IMR 2037A.6.7.9.2.1 Test Purpose and Environment
2037A.6.7.9.2.2 Test parameters 2038A.6.7.9.2.3 Test Requirements
2043A.6.7.9.3 L1-SINR measurement with CSI-RS based CMR and dedicated
IMR 2043A.6.7.9.3.1 Test Purpose and Environment 2043A.6.7.9.3.2 Test
parameters 2043A.6.7.9.3.3 Test Requirements 2048A.6.7.10 CSI-RSRP
2048A.6.7.10.1 SA: intra-frequency case measurement accuracy with FR1
serving cell and FR1 target cell 2048A.6.7.10.1.1 Test Purpose and
Environment 2048A.6.7.10.1.2 Test parameters 2049A.6.7.10.1.3 Test
Requirements 2054A.6.7.10.2 SA inter-frequency case measurement accuracy
with FR1 serving cell and FR1 target cell 2054A.6.7.10.2.1 Test Purpose
and Environment 2054A.6.7.10.2.2 Test parameters 2054A.6.7.10.2.3 Test
Requirements 2060A.6.7.11 CSI-RSRQ 2060A.6.7.11.1 SA: Intra-frequency
measurement accuracy with FR1 serving cell and FR1 target cell
2060A.6.7.11.1.1 Test Purpose and Environment 2060A.6.7.11.1.2 Test
Parameters 2060A.6.7.11.1.3 Test Requirements 2065A.6.7.11.2 SA
Inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell 2065A.6.7.11.2.1 Test Purpose and Environment
2065A.6.7.11.2.2 Test Parameters 2065A.6.7.11.2.3 Test Requirements
2070A.6.7.12 CSI-SINR 2070A.6.7.12.1 SA intra-frequency measurement
accuracy with FR1 serving cell and FR1 target cell 2070A.6.7.12.1.1 Test
Purpose and Environment 2070A.6.7.12.1.2 Test Parameters
2071A.6.7.12.1.3 Test Requirements 2076A.6.7.12.2 SA Inter-frequency
measurement accuracy with FR1 serving cell and FR1 target cell
2076A.6.7.12.2.1 Test Purpose and Environment 2076A.6.7.12.2.2 Test
Parameters 2076A.6.7.12.2.3 Test Requirements 2082A.6.7.13 RSTD
measurements 2082A.6.7.13.1 RSTD measurement accuracy test case for
single positioning frequency layer 2082A.6.7.13.1.1 Test purpose and
Environment 2082A.6.7.13.1.2 Test Requirements 2085A.6.7.13.2 RSTD
measurement accuracy test case for dual positioning frequency layer
2085A.6.7.13.2.1 Test purpose and Environment 2085A.6.7.13.2.2 Test
Requirements 2089A.6.7.14 PRS-RSRP measurements 2089A.6.7.14.1 SA:
measurement accuracy with PRS in FR1 2089A.6.7.14.1.1 Test Purpose and
Environment 2089A.6.7.14.1.2 Test parameters 2090A.6.7.14.1.3 Test
Requirements 2094A.6.7.15 UE Rx-Tx time difference measurements
2094A.6.7.15.1 UE Rx-Tx time difference measurement accuracy for single
positioning frequency layer in FR1 SA 2094A.6.7.15.1.1 Test purpose and
environment 2094A.6.7.15.1.2 Test parameters 2095A.6.7.15.1.3 Test
requirements 2098A.7 NR standalone tests with one or more NR cells in
FR2 2099A.7.1 SA: RRC\_IDLE state mobility 2099A.7.1.1 Cell re-selection
to NR 2099A.7.1.1.1 Cell reselection to FR2 intra-frequency NR case
2099A.7.1.1.1.1 Test Purpose and Environment 2099A.7.1.1.1.2 Test
Parameters 2099A.7.1.1.1.3 Test Requirements 2102A.7.1.1.2 Cell
reselection to FR2 inter-frequency NR case 2103A.7.1.1.2.1 Test Purpose
and Environment 2103A.7.1.1.2.2 Test Parameters 2103A.7.1.1.2.3 Test
Requirements 2105A.7.1.1.3 Cell reselection to FR2 intra-frequency NR
case for UE fulfilling low mobility relaxed measurement criterion
2106A.7.1.1.3.1 Test Purpose and Environment 2106A.7.1.1.3.2 Test
Parameters 2106A.7.1.1.3.3 Test Requirements 2109A.7.1.1.4 Cell
reselection to FR2 intra-frequency NR case for UE fulfilling not-at-cell
edge relaxed measurement criterion 2109A.7.1.1.4.1 Test Purpose and
Environment 2109A.7.1.1.4.2 Test Parameters 2109A.7.1.1.4.3 Test
Requirements 2112A.7.1.1.5 Cell reselection to FR2 inter-frequency NR
case for UE fulfilling low mobility relaxed measurement criterion
2112A.7.1.1.5.1 Test Purpose and Environment 2112A.7.1.1.5.2 Test
Parameters 2112A.7.1.1.5.3 Test Requirements 2115A.7.1.1.6 Cell
reselection to FR2 inter-frequency NR case for UE fulfilling not-at-cell
edge relaxed measurement criterion 2115A.7.1.1.6.1 Test Purpose and
Environment 2115A.7.1.1.6.2 Test Parameters 2115A.7.1.1.6.3 Test
Requirements 2118A.7.2 SA: RRC\_INACTIVE state mobility 2118A.7.3
RRC\_CONNECTED state mobility 2118A.7.3.1 Handover 2118A.7.3.1.1
Inter-frequency handover from FR1 to FR2; unknown target cell
2118A.7.3.1.1.1 Test Purpose and Environment 2118A.7.3.1.1.2 Test
Parameters 2118A.7.3.1.1.3 Test Requirements 2122A.7.3.1.2
Intra-frequency handover from FR2 to FR2; unknown target cell
2122A.7.3.1.2.1 Test Purpose and Environment 2122A.7.3.1.2.2 Test
Parameters 2122A.7.3.1.2.3 Test Requirements 2125A.7.3.1.3
Inter-frequency handover from FR2 to FR2; unknown target cell
2125A.7.3.1.3.1 Test Purpose and Environment 2125A.7.3.1.3.2 Test
Parameters 2125A.7.3.1.3.3 Test Requirements 2126A.7.3.1.4 Inter-band
inter-frequency synchronous DAPS handover from FR1 to FR2
2127A.7.3.1.4.1 Test Purpose and Environment 2127A.7.3.1.4.2 Test
Parameters 2127A.7.3.1.4.3 Test Requirements 2134A.7.3.1.5 Inter-band
inter-frequency asynchronous DAPS handover from FR1 to FR2
2134A.7.3.1.5.1 Test Purpose and Environment 2134A.7.3.1.5.2 Test
Parameters 2134A.7.3.1.5.3 Test Requirements 2141A.7.3.2 RRC Connection
Mobility Control 2141A.7.3.2.1 SA: RRC Re-establishment 2141A.7.3.2.1.1
Intra-frequency RRC Re-establishment in FR2 2141A.7.3.2.1.2
Inter-frequency RRC Re-establishment in FR2 2144A.7.3.2.1.3
Intra-frequency RRC Re-establishment in FR2 without serving cell timing
2147A.7.3.2.1.3.1 Test Purpose and Environment 2147A.7.3.2.1.3.2 Test
Requirements 2149A.7.3.2.2 Random Access 2150A.7.3.2.2.1 4-step RA type
contention based random access test in FR2 for NR Standalone
2150A.7.3.2.2.2 4-step RA type non-contention based random access test
in FR2 for NR Standalone 2154A.7.3.2.2.3 2-step RA type contention based
random access test in FR2 for NR Standalone 2159A.7.3.2.2.4 2-step RA
type non-contention based random access test in FR2 for NR Standalone
2162A.7.3.2.3 SA: RRC Connection Release with Redirection
2165A.7.3.2.3.1 Redirection from NR in FR2 to NR in FR2 2165A.7.3.3
Conditional Handover 2169A.7.3.3.1 Intra-frequency conditional handover
from FR2 to FR2 2169A.7.3.3.1.1 Test Purpose and Environment
2169A.7.3.3.1.2 Test Parameters 2169A.7.3.3.1.2.3 Test Requirements
2172A.7.3.3.2 Inter-frequency conditional handover from FR2 to FR2;
unknown target cell 2172A.7.3.3.2.1 Test Purpose and Environment
2172A.7.3.3.2.2 Test Parameters 2172A.7.3.3.2.3 Test Requirements
2175A.7.4 Timing 2175A.7.4.1 UE transmit timing 2175A.7.4.1.1 NR UE
Transmit Timing Test for FR2 2175A.7.4.1.1.1 Test Purpose and
environment 2175A.7.4.1.1.2 Test requirements 2178A.7.4.2 UE timer
accuracy 2179A.7.4.3 Timing advance 2179A.7.4.3.1 SA FR2 timing advance
adjustment accuracy 2179A.7.4.3.1.1 Test Purpose and Environment
2179A.7.4.3.1.2 Test Parameters 2179A.7.4.3.1.3 Test Requirements
2182A.7.5 Signaling characteristics 2183A.7.5.1 Radio link Monitoring
2183A.7.5.1.1 Radio Link Monitoring Out-of-sync Test for FR2 PCell
configured with SSB-based RLM RS in non-DRX mode 2183A.7.5.1.1.1 Test
Purpose and Environment 2183A.7.5.1.1.2 Test Requirements 2186A.7.5.1.2
Radio Link Monitoring In-sync Test for FR2 PCell configured with
SSB-based RLM RS in non-DRX mode 2187A.7.5.1.2.1 Test Purpose and
Environment 2187A.7.5.1.2.2 Test Requirements 2191A.7.5.1.3 Radio Link
Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM
RS in DRX mode 2192A.7.5.1.3.1 Test Purpose and Environment
2192A.7.5.1.3.2 Test Requirements 2196A.7.5.1.4 Radio Link Monitoring
In-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode
2196A.7.5.1.4.1 Test Purpose and Environment 2196A.7.5.1.4.2 Test
Requirements 2201A.7.5.1.5 Radio Link Monitoring Out-of-sync Test for
FR2 PCell configured with CSI-RS-based RLM in non-DRX mode
2201A.7.5.1.5.1 Test Purpose and Environment 2201A.7.5.1.5.2 Test
Requirements 2206A.7.5.1.6 Radio Link Monitoring In-sync Test for FR2
PCell configured with CSI-RS-based RLM in non-DRX mode 2206A.7.5.1.6.1
Test Purpose and Environment 2206A.7.5.1.6.2 Test Requirements
2210A.7.5.1.7 Radio Link Monitoring Out-of-sync Test for FR2 PCell
configured with CSI-RS-based RLM in DRX mode 2210A.7.5.1.7.1 Test
Purpose and Environment 2210A.7.5.1.7.2 Test Requirements 2214A.7.5.1.8
Radio Link Monitoring In-sync Test for FR2 PCell configured with
CSI-RS-based RLM in DRX mode 2214A.7.5.1.8.1 Test Purpose and
Environment 2214A.7.5.1.8.2 Test Requirements 2219A.7.5.1.9 UE Radio
Link Monitoring Scheduling Restrictions on FR2 2219A.7.5.1.9.1 Test
Purpose and Environment 2219A.7.5.1.9.2 Test Requirements 2222A.7.5.2
Interruption 2222**A.7.5.2.1** Interruptions during measurements on
deactivated NR SCC in FR2 2222A.7.5.2.2 SA interruptions at NR SRS
carrier-based switching 2226A.7.5.2.2.1 Test Purpose and Environment
2226A.7.5.2.2.2 Test Parameters 2226A.7.5.2.2.3 Test Requirements
2228A.7.5.3 SCell Activation and Deactivation Delay 2228A.7.5.3.1 SCell
Activation and deactivation for SCell in FR2 intra-band in non-DRX
2228A.7.5.3.1.1 Test Purpose and Environment 2228A.7.5.3.1.2 Test
Requirements 2230A.7.5.3.2 SCell Activation and deactivation for FR1+FR2
inter-band with target SCell in FR2 2230A.7.5.3.2.1 Test Purpose and
Environment 2230A.7.5.3.2.2 Test Requirements 2234A.7.5.3.3 SCell
Activation and deactivation for SCell in FR2 inter-band in non-DRX
2235A.7.5.3.3.1 Test Purpose and Environment 2235A.7.5.3.3.2 Test
Requirements 2238A.7.5.3.4 Direct SCell activation at SCell addition of
known SCell in FR2 2239A.7.5.3.4.1 Test Purpose and Environment
2239A.7.5.3.4.2 Test Requirements 2242A.7.5.3.5 Direct SCell activation
at handover with known SCell in FR2 2243A.7.5.3.5.1 Test Purpose and
Environment 2243A.7.5.3.5.2 Test Requirements 2246A.7.5.4 Void
2247A.7.5.5 Beam Failure Detection and Link recovery procedures
2247A.7.5.5.1 Beam Failure Detection and Link Recovery Test for FR2
PCell configured with SSB-based BFD and LR in non-DRX mode
2247A.7.5.5.1.1 Test Purpose and Environment 2247A.7.5.5.1.2 Test
Requirements 2251A.7.5.5.2 Beam Failure Detection and Link Recovery Test
for FR2 PCell configured with SSB-based BFD and LR in DRX mode
2252A.7.5.5.2.1 Test Purpose and Environment 2252A.7.5.5.2.2 Test
Requirements 2255A.7.5.5.3 Beam Failure Detection and Link Recovery Test
for FR2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode
2256A.7.5.5.3.1 Test Purpose and Environment 2256A.7.5.5.3.2 Test
Requirements 2260A.7.5.5.4 Beam Failure Detection and Link Recovery Test
for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode
2261A.7.5.5.4.1 Test Purpose and Environment 2261A.7.5.5.4.2 Test
Requirements 2265A.7.5.5.5 Scheduling availability restriction during
Beam Failure Detection and Link Recovery for FR2 PCell configured with
SSB-based BFD and LR in non-DRX mode 2266A.7.5.5.5.1 Test Purpose and
Environment 2266A.7.5.5.5.2 Test Requirements 2269A.7.5.5.6 Beam Failure
Detection and Link Recovery Test for FR2 SCell configured with
CSI-RS-based BFD and LR in non-DRX mode 2270A.7.5.5.6.1 Test Purpose and
Environment 2270A.7.5.5.6.2 Test Requirements 2274A.7.5.5.7 Beam Failure
Detection and Link Recovery Test for FR2 SCell configured with
CSI-RS-based BFD and LR in DRX mode 2275A.7.5.5.7.1 Test Purpose and
Environment 2275A.7.5.5.7.2 Test Requirements 2279A.7.5.6 Active BWP
switch 2280A.7.5.6.1 DCI-based and Timer-based Active BWP Switch
2280A.7.5.6.1.1 NR FR2- NR FR2 DL active BWP switch of SCell with
non-DRX in SA 2280A.7.5.6.1.2 NR FR1- NR FR2 DL active BWP switch of
SCell with non-DRX in SA A.7.5.6.1.2.1 Test Purpose and Environment
2284A.7.5.6.1.3 NR FR2 DL active BWP switch with non-DRX in SA
2289A.7.5.6.1.3.1 Test Purpose and Environment 2289A.7.5.6.1.3.2 Test
Requirements 2292A.7.5.6.2 RRC-based Active BWP Switch 2292A.7.5.6.3
Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs
2296A.7.5.6.3.1 Active BWP switch on multiple SCells with non-DRX in SA
2296A.7.5.6.4 SCell dormancy switch 2299A.7.5.6.4.1 NR FR2 PCell SCell
dormancy switch of single FR2 SCell inside active time 2299A.7.5.6.4.2
NR FR1 PCell SCell dormancy switch of two FR2 SCells outside active time
2304A.7.5.6.4.2.2 Test Requirements 2309A.7.5.6.5 Simultaneous RRC-based
Active BWP Switch on multiple CCs 2309A.7.5.6.5.1 Active BWP switch on
multiple SCells with non-DRX in SA 2309A.7.5.7 PSCell addition and
release delay 2312A.7.5.7.1 Addition and Release Delay of known NR
PSCell 2312A.7.5.7.1.1 Test Purpose and Environment 2312A.7.5.7.2
Addition and Release Delay of unknown NR PSCell 2316A.7.5.7.2.1 Test
Purpose and Environment 2316A.7.5.7.2.2 Test Requirements 2319A.7.5.8
Active TCI state switch delay 2319A.7.5.8.1 MAC-CE based active TCI
state switch 2319A.7.5.8.2 RRC based active TCI state switch 2323A.7.5.9
Uplink spatial relation switch delay 2327A.7.5.9.1 MAC-CE based Spatial
Relation switch 2327A.7.5.9.1.1 NR PCell FR2 spatial relation associated
with known DL-RS 2327A.7.5.9.1.1.2 Test Requirements 2330A.7.5.9.2 RRC
based spatial relation switch 2330A.7.5.9.2.1 NR PCell FR2 spatial
relation switch associated with a known DL-RS 2330A.7.5.9.2.1.1 Test
Purpose and Environment 2330A.7.5.9.2**.1**.2 Test Requirements
2333A.7.5.10 UE specific CBW change 2333A.7.5.10.1 NR FR2 UE specific
CBW change of PCell with non-DRX in SA 2333A.7.5.10.1.1 Test Purpose and
Environment 2333A.7.5.10.1.2 Test Requirements 2336A.7.6 Measurement
procedure 2337A.7.6.1 Intra-frequency Measurements 2337A.7.6.1.1 SA
event triggered reporting test without gap under non-DRX 2337A.7.6.1.1.1
Test purpose and Environment 2337A.7.6.1.1.2 Test Requirements
2339A.7.6.1.2 SA event triggered reporting test without gap under DRX
2340A.7.6.1.2.1 Test purpose and Environment 2340A.7.6.1.2.2 Test
Requirements 2342A.7.6.1.3 SA event triggered reporting test with per-UE
gaps under non-DRX 2343A.7.6.1.3.1 Test purpose and Environment
2343A.7.6.1.3.2 Test Requirements 2345A.7.6.1.4 SA event triggered
reporting test with per-UE gaps under DRX 2346A.7.6.1.4.1 Test purpose
and Environment 2346A.7.6.1.4.2 Test Requirements 2349A.7.6.2
Inter-frequency Measurements 2350A.7.6.2.1 SA event triggered reporting
tests For FR2 without SSB time index detection when DRX is not used
(PCell in FR2) 2350A.7.6.2.1.1 Test Purpose and Environment
2350A.7.6.2.1.2 Test Requirements 2353A.7.6.2.2 SA event triggered
reporting tests For FR2 without SSB time index detection when DRX is
used (PCell in FR2) 2353A.7.6.2.2.1 Test Purpose and Environment
2353A.7.6.2.2.2 Test Requirements 2357A.7.6.2.3 SA event triggered
reporting tests For FR2 with SSB time index detection when DRX is not
used (PCell in FR2) 2357A.7.6.2.3.1 Test Purpose and Environment
2357A.7.6.2.3.2 Test Requirements 2361A.7.6.2.4 SA event triggered
reporting tests For FR2 with SSB time index detection when DRX is used
(PCell in FR2) 2361A.7.6.2.4.1 Test Purpose and Environment
2361A.7.6.2.4.2 Test Requirements 2365A.7.6.2.5 SA event triggered
reporting tests for FR2 without SSB time index detection when DRX is not
used (PCell in FR1) 2365A.7.6.2.5.1 Test Purpose and Environment
2365A.7.6.2.5.2 Test Requirements 2369A.7.6.2.6 SA event triggered
reporting tests for FR2 without SSB time index detection when DRX is
used (PCell in FR1) 2370A.7.6.2.6.1 Test Purpose and Environment
2370A.7.6.2.6.2 Test Requirements 2374A.7.6.2.7 SA event triggered
reporting tests for FR2 with SSB time index detection when DRX is not
used (PCell in FR1) 2375A.7.6.2.7.1 Test Purpose and Environment
2375A.7.6.2.7.2 Test Requirements 2379A.7.6.2.8 SA event triggered
reporting tests for FR2 with SSB time index detection when DRX is used
(PCell in FR1) 2380A.7.6.2.8.1 Test Purpose and Environment
2380A.7.6.2.8.2 Test Requirements 2384A.7.6.2.9 SA event triggered
reporting tests For FR2 without SSB time index detection when DRX is not
used (PCell in FR2) (rel16 additional mandatory gap pattern 17)
2385A.7.6.2.9.1 Test Purpose and Environment 2385A.7.6.2.9.2 Test
Requirements 2388A.7.6.2.10 SA event triggered reporting test without
gap under non-DRX 2388A.7.6.2.10.1 Test Purpose and Environment
2388A.7.6.2.10.2 Test Requirements 2390A.7.6.2.11 SA event triggered
reporting test without gap under DRX 2390A.7.6.2.11.1 Test Purpose and
Environment 2390A.7.6.2.11.2 Test Requirements 2393A.7.6.3 L1-RSRP
measurement for beam reporting 2394A.7.6.3.1 SSB based L1-RSRP
measurement when DRX is not used 2394A.7.6.3.1 SSB based L1-RSRP
measurement when DRX is not used 2394A.7.6.3.1.1 Test Purpose and
Environment 2394A.7.6.3.1.2 Test parameters 2394A.7.6.3.1.3 Test
Requirements 2396A.7.6.3.2 SSB based L1-RSRP measurement when DRX is
used 2396A.7.6.3.2.1 Test Purpose and Environment 2396A.7.6.3.2.2 Test
parameters 2397A.7.6.3.2.3 Test Requirements 2399A.7.6.3.3 CSI-RS based
L1-RSRP measurement when DRX is not used 2399A.7.6.3.3.1 Test Purpose
and Environment 2399A.7.6.3.3.2 Test parameters 2400A.7.6.3.3.3 Test
Requirements 2402A.7.6.3.4 CSI-RS based L1-RSRP measurement when DRX is
used 2403A.7.6.3.4.1 Test Purpose and Environment 2403A.7.6.3.4.2 Test
parameters 2403A.7.6.3.3.3 Test Requirements 2405A.7.6.4 CLI
measurements 2406A.7.6.4.1 SRS-RSRP measurement with non-DRX
2406A.7.6.4.1.1 Test Purpose and Environment 2406A.7.6.4.1.2 Test
Parameters 2406A.7.6.4.1.3 Test Requirements 2408A.7.6.4.2 CLI-RSSI
measurement with non-DRX 2408A.7.6.4.2.1 Test Purpose and Environment
2408A.7.6.4.2.2 Test Parameters 2409A.7.6.4.2.3 Test Requirements
2410A.7.6.5 NR Measurements with autonomous gaps 2411A.7.6.5.1 SA
interfrequency CGI reporting in autonomous gaps test (PCell in FR2)
2411A.7.6.5.1.1 Test Purpose and Environment 2411A.7.6.5.1.2 Test
Requirements 2414A.7.6.6 L1-SINR measurement for beam reporting
2414A.7.6.6.1 L1-SINR measurement with CSI-RS based CMR and no dedicated
IMR configured when DRX is not used 2414A.7.6.6.1.1 Test Purpose and
Environment 2414A.7.6.6.1.2 Test parameters 2414A.7.6.6.1.3 Test
Requirements 2416A.7.6.6.2 L1-SINR measurement with SSB based CMR and
dedicated IMR when DRX is used 2416A.7.6.6.2.1 Test Purpose and
Environment 2416A.7.6.6.2.2 Test parameters 2417A.7.6.6.2.3 Test
Requirements 2419A.7.6.6.3 L1-SINR measurement with CSI-RS based CMR and
dedicated IMR configured when DRX is used 2419A.7.6.6.3.1 Test Purpose
and Environment 2419A.7.6.6.3.2 Test parameters 2420A.7.6.6.3.3 Test
Requirements 2422A.7.6.7 CSI-RS based intra-frequency Measurements
2422A.7.6.7.1 SA event triggered reporting test without gap under DRX
for CSI-RS based intra-frequency measurement 2422A.7.6.7.1.1 Test
purpose and Environment 2422A.7.6.7.1.2 Test Requirements 2425A.7.6.8
CSI-RS based inter-frequency Measurements 2426A.7.6.8.1 SA event
triggered reporting tests for FR2 CSI-RS based measurement when non-DRX
is used (PCell in FR2) 2426A.7.6.8.1.1 Test Purpose and Environment
2426A.7.6.2.2.2 Test Requirements 2430A.7.6.9 RSTD measurements
2430A.7.6.9.1 NR RSTD measurement reporting delay test case for single
positioning frequency layer in FR2 SA 2430A.7.6.9.1.1 Test Purpose and
Environment 2430A.7.6.9.1.2 Test Requirements 2436A.7.6.9.2 NR RSTD
measurement reporting delay test case for dual positioning frequency
layers in FR2 SA 2436A.7.6.9.2.1 Test Purpose and Environment
2436A.7.6.9.2.2 Test Requirements 2443A.7.6.10 PRS-RSRP measurements
2443A.7.6.10.1 PRS-RSRP reporting delay test case for single positioning
frequency layer 2443A.7.6.10.1.1 Test Purpose and Environment
2443A.7.6.10.1.2 Test Requirements 2447A.7.6.10.2 PRS-RSRP reporting
delay test case for dual positioning frequency layer 2447A.7.6.10.2.1
Test Purpose and Environment 2447A.7.6.10.2.2 Test Requirements
2450A.7.6.11 UE Rx-Tx time difference measurements 2450A.7.6.11.1 UE
Rx-Tx time difference measurements for single positioning frequency
layer in FR2 SA 2450A.7.6.11.1.1 Test purpose and environment
2450A.7.6.11.1.2 Test requirements 2454A.7.6.11.2 UE Rx-Tx time
difference measurement period for dual positioning frequency layers in
FR2 SA 2454A.7.6.11.2.1 Test purpose and environment 2454A.7.6.11.2.2
Test requirements 2458A.7.7 Measurement Performance requirements
2458A.7.7.1 SS-RSRP 2459A.7.7.1.1 SA intra-frequency case measurement
accuracy with FR2 serving cell and FR2 target cell 2459A.7.7.1.1.1 Test
Purpose and Environment 2459A.7.7.1.1.2 Test parameters 2459A.7.7.1.1.3
Test Requirements 2463A.7.7.1.2 SA inter-frequency case measurement
accuracy with FR2 serving cell and FR2 target cell 2463A.7.7.1.2.1 Test
Purpose and Environment 2463A.7.7.1.2.2 Test parameters 2464A.7.7.1.2.3
Test Requirements 2468A.7.7.1.3 SA inter-frequency measurement accuracy
with FR1 serving cell and FR2 target cell 2469A.7.7.1.3.1 Test Purpose
and Environment 2469A.7.7.1.3.2 Test parameters 2469A.7.7.1.3.3 Test
Requirements 2473A.7.7.2 SS-RSRQ 2473A.7.7.2.1 SA intra-frequency
measurement accuracy with FR2 serving cell and FR2 target cell
2473A.7.7.2.1.1 Test Purpose and Environment 2473A.7.7.2.1.2 Test
Parameters 2473A.7.7.2.1.3 Test Requirements 2475A.7.7.2.2 SA
Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 2475A.7.7.2.2.1 Test Purpose and Environment 2475A.7.7.2.2.2
Test Parameters 2475A.7.7.2.2.3 Test Requirements 2477A.7.7.3 SS-SINR
2477A.7.7.3.1 SA intra-frequency case measurement accuracy with FR2
serving cell and FR2 target cell 2477A.7.7.3.1.1 Test Purpose and
Environment 2477A.7.7.3.1.2 Test Parameters 2477A.7.7.3.1.3 Test
Requirements 2480A.7.7.3.2 SA Inter-frequency measurement accuracy with
FR2 serving cell and FR2 TDD target cell 2480A.7.7.3.2.1 Test Purpose
and Environment 2480A.7.7.3.2.2 Test Parameters 2480A.7.7.3.2.3 Test
Requirements 2482A.7.7.4 L1-RSRP measurement for beam reporting
2482A.7.7.4.1 SSB based L1-RSRP measurement 2482A.7.7.4.1.1 Test Purpose
and Environment 2482A.7.7.4.1.2 Test parameters 2483A.7.7.4.1.3 Test
Requirements 2485A.7.7.4.2 CSI-RS based L1-RSRP measurement on resource
set with repetition off 2486A.7.7.4.2.1 Test Purpose and Environment
2486A.7.7.4.2.2 Test parameters 2486A.7.7.4.2.3 Test Requirements
2488A.7.7.5 CLI measurements 2489A.7.7.5.1 SA SRS-RSRP measurement
accuracy with FR2 serving cell 2489A.7.7.5.1.1 Test Purpose and
Environment 2489A.7.7.5.1.2 Test parameters 2489A.7.7.5.1.3 Test
Requirements 2492A.7.7.5.2 SA CLI-RSSI measurement accuracy with FR2
serving cell 2493A.7.7.5.2.1 Test Purpose and Environment
2493A.7.7.5.2.2 Test parameters 2493A.7.7.5.2.3 Test Requirements
2495A.7.7.6 L1-SINR measurement for beam reporting 2496A.7.7.6.1 L1-SINR
measurement with CSI-RS based CMR and no dedicated IMR configured and
CSI-RS resource set with repetition off 2496A.7.7.6.1.1 Test Purpose and
Environment 2496A.7.7.6.1.2 Test parameters 2496A.7.7.6.1.3 Test
Requirements 2498A.7.7.6.2 L1-SINR measurement with SSB based CMR and
dedicated IMR 2499A.7.7.6.2.1 Test Purpose and Environment
2499A.7.7.6.2.2 Test parameters 2499A.7.7.6.2.3 Test Requirements
2501A.7.7.6.3 L1-SINR measurement with CSI-RS based CMR and dedicated
IMR 2502A.7.7.6.3.1 Test Purpose and Environment 2502A.7.7.6.3.2 Test
parameters 2502A.7.7.6.3.3 Test Requirements 2504A.7.7.7 CSI-RSRP
2505A.7.7.7.1 SA intra-frequency case measurement accuracy with FR2
serving cell and FR2 target cell 2505A.7.7.7.1.1 Test Purpose and
Environment 2505A.7.7.7.1.2 Test parameters 2505A.7.7.7.1.3 Test
Requirements 2510A.7.7.7.2 SA inter-frequency case measurement accuracy
with FR2 serving cell and FR2 target cell 2510A.7.7.7.2.1 Test Purpose
and Environment 2510A.7.7.7.2.2 Test parameters 2511A.7.7.7.2.3 Test
Requirements 2515A.7.7.8 CSI-RSRQ 2516A.7.7.8.1 SA intra-frequency
measurement accuracy with FR2 serving cell and FR2 target cell
2516A.7.7.8.1.1 Test Purpose and Environment 2516A.7.7.8.1.2 Test
Parameters 2516A.7.7.8.1.3 Test Requirements 2518A.7.7.8.2 SA
Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 2518A.7.7.8.2.1 Test Purpose and Environment 2518A.7.7.8.2.2
Test Parameters 2519A.7.7.8.2.3 Test Requirements 2520A.7.7.9 CSI-SINR
2520A.7.7.9.1 SA intra-frequency case measurement accuracy with FR2
serving cell and FR2 target cell 2520A.7.7.9.1.1 Test Purpose and
Environment 2520A.7.7.9.1.2 Test Parameters 2521A.7.7.9.1.3 Test
Requirements 2523A.7.7.9.2 SA Inter-frequency measurement accuracy with
FR2 serving cell and FR2 TDD target cell 2523A.7.7.9.2.2 Test Parameters
2524A.7.7.9.2.3 Test Requirements 2525A.7.7.10 RSTD measurements
2526A.7.7.10.1 RSTD measurement accuracy test case for single
positioning frequency layer 2526A.7.7.10.1.1 Test purpose and
Environment 2526A.7.7.10.1.2 Test Requirements 2528A.7.7.10.2 RSTD
measurement accuracy test case for dual positioning frequency layer
2528A.7.7.10.2.1 Test purpose and Environment 2528A.7.7.10.2.2 Test
Requirements 2531A.7.7.11 PRS-RSRP measurements 2531A.7.7.11.1 SA
measurement accuracy with PRS in FR2 2531A.7.7.11.1.1 Test Purpose and
Environment 2531A.7.7.11.1.2 Test parameters 2531A.7.7.11.1.3 Test
Requirements 2535A.7.7.12 UE Rx-Tx time difference measurements
2536A.7.7.12.1 UE Rx-Tx time difference measurement accuracy for single
positioning frequency layer in FR2 SA 2536A.7.7.12.1.1 Test purpose and
environment 2536A.7.7.12.1.2 Test parameters 2536A.7.7.12.1.3 Test
requirements 2539A.8 E-UTRA standalone tests for NR RRM 2540A.8.1 Void
2540A.8.2 RRC\_IDLE state mobility 2540A.8.2.1 Inter-RAT NR Cell
re-selection 2540A.8.2.1.1 E-UTRA Cell reselection to higher priority NR
target Cell in FR1 2540A.8.2.1.1.1 Test Purpose and Environment
2540A.8.2.1.1.2 Test Requirements 2545A.8.2.1.2 E-UTRA Cell reselection
to lower priority NR target Cell in FR1 for UE configured with
highSpeedInterRAT-NR-r16 2546A.8.2.1.2.1 Test Purpose and Environment
2546A.8.2.1.2.2 Test Requirements 2551A.8.2.2 E-UTRA -- NR Inter-RAT
Early Measruement Reporting 2552A.8.2.2.1 E-UTRA -- NR Early Measurement
Reporting for NR in FR1 2552A.8.2.2.1.1 Test Purpose and Environment
2552A.8.2.2.1.2 Test Requirements 2557A.8.2.2.2 E-UTRA -- NR Early
Measurement Reporting for NR in FR2 2557A.8.2.2.2.1 Test Purpose and
Environment 2557A.8.2.2.2.2 Test Requirements 2560A.8.3 RRC\_CONNECTED
state mobility 2561A.8.3.1 Handover 2561A.8.3.1.1 E-UTRAN - NR handover
in FR1 2561A.8.3.1.1.1 Test Purpose and Environment 2561A.8.3.1.1.2 Test
Requirements 2566A.8.4 Measurement procedure 2566A.8.4.1 E-UTRA -- NR
Inter-RAT SFTD Measurement Delay 2566A.8.4.1.1 E-UTRA -- NR Inter-RAT
SFTD Measurement Delay in non-DRX 2566A.8.4.1.1.1 Test Purpose and
Environment 2566A.8.4.1.1.2 Test Requirements 2568A.8.4.1.2 E-UTRA -- NR
Inter-RAT SFTD Measurement Delay in DRX 2569A.8.4.1.2.1 Test Purpose and
Environment 2569A.8.4.1.2.2 Test Requirements 2570A.8.4.2 E-UTRA -- NR
Inter-RAT Measurements 2570A.8.4.2.1 NR Inter-RAT event triggered
reporting tests for FR1 without SSB time index detection when DRX is not
used 2570A.8.4.2.1.1 Test Purpose and Environment 2570A.8.4.2.1.2 Test
Requirements 2575A.8.4.2.2 NR Inter-RAT event triggered reporting tests
for FR1 without SSB time index detection when DRX is used
2575A.8.4.2.2.1 Test Purpose and Environment 2575A.8.4.2.2.2 Test
Requirements 2579A.8.4.2.3 NR Inter-RAT event triggered reporting tests
for FR1 with SSB time index detection when DRX is not used
2579A.8.4.2.3.1 Test Purpose and Environment 2579A.8.4.2.3.2 Test
Requirements 2583A.8.4.2.4 NR Inter-RAT event triggered reporting tests
for FR1 with SSB time index detection when DRX is used 2583A.8.4.2.4.1
Test Purpose and Environment 2583A.8.4.2.4.2 Test Requirements
2587A.8.4.2.5 NR Inter-RAT event triggered reporting tests for FR2
without SSB time index detection when DRX is not used 2587A.8.4.2.5.1
Test Purpose and Environment 2587A.8.4.2.5.2 Test Requirements
2589A.8.4.2.6 NR Inter-RAT event triggered reporting tests for FR2
without SSB time index detection when DRX is used 2590A.8.4.2.6.1 Test
Purpose and Environment 2590A.8.4.2.6.2 Test Requirements 2592A.8.4.2.7
NR Inter-RAT event triggered reporting tests for FR2 with SSB time index
detection when DRX is not used 2593A.8.4.2.7.1 Test Purpose and
Environment 2593A.8.4.2.7.2 Test Requirements 2595A.8.4.2.8 NR Inter-RAT
event triggered reporting tests for FR2 with SSB time index detection
when DRX is used 2596A.8.4.2.8.1 Test Purpose and Environment
2596A.8.4.2.8.2 Test Requirements 2598A.8.4.2.9 NR Inter-RAT event
triggered reporting tests for FR1 with SSB time index detection in DRX
for UE configured with highSpeedInterRAT-NR-r16 2599A.8.4.2.9.1 Test
Purpose and Environment 2599A.8.4.2.9.2 Test Requirements 2604A.8.5
Measurement performance 2604A.8.5.1 SFTD accuracy 2604A.8.5.1.1 SFTD
accuracy 2604A.8.5.1.1.1 Test Purpose 2604A.8.5.1.1.2 Test Environment
2604A.8.5.1.1.3 Test Requirements 2610A.8.5.2 E-UTRA -- NR Inter-RAT
Measurement Performance requirements 2610A.8.5.2.1.1 E-UTRAN -- NR
inter-RAT measurements with FR1 target cell 2610A.8.5.2.1.2 E-UTRAN --
NR inter-RAT measurements with FR2 target cell 2615A.8.5.2.1.2.1 Test
Purpose and Environment 2615A.8.5.2.1.2.2 Test Parameters
2615A.8.5.2.1.2.3 Test Requirements 2617A.8.5.2.2 SS-RSRQ
2617A.8.5.2.2.1 E-UTRAN -- NR inter-RAT measurements with FR1 target
cell 2617A.8.5.2.2.2 E-UTRAN -- NR inter-RAT measurements with FR2
target cell 2622A.8.5.2.2.2.1 Test Purpose and Environment
2622A.8.5.2.2.2.2 Test Parameters 2622A.8.5.2.2.2.3 Test Requirements
2624A.8.5.2.3 SS-SINR 2624A.8.5.2.3.1 E-UTRAN -- NR inter-RAT
measurements with FR1 target cell 2624A.8.5.2.3.2 E-UTRAN -- NR
inter-RAT measurements with FR2 target cell 2628A.8.5.2.3.2.1 Test
Purpose and Environment 2628A.8.5.2.3.2.2 Test Parameters
2628A.8.5.2.3.2.3 Test Requirements 2630A.9 V2X Tests 2631A.9.1 V2X
Tests in FR1 2631A.9.1.1 Test for V2X UE Transmit Timing 2631A.9.1.1.1
Test for GNSS as Synchronization Reference Source 2631A.9.1.1.1.1 Test
Purpose and Environment 2631A.9.1.1.1.2 Test requirements 2631A.9.1.1.2
Test for SyncRef UE as Synchronization Reference Source 2631A.9.1.1.2.1
Test Purpose and Environment 2631A.9.1.1.2.2 Test requirements
2632A.9.1.1.3 Test for FR1 NR Cell as Synchronization Reference Source
2632A.9.1.1.3.1 Test Purpose and Environment 2632A.9.1.1.3.2 Test
requirements 2635A.9.1.2 Test for Initiation/Cease of S-SSB Transmission
with V2X Sidelink Communication 2635A.9.1.2.1 Test for FR1 NR Cell as
synchronization reference source without gap under non-DRX
2635A.9.1.2.1.1 Test Purpose and Environment 2635A.9.1.2.1.2 Test
Requirements 2639A.9.1.2.2 Test for SyncRef UE as synchronization
reference source 2639A.9.1.2.2.1 Test Purpose and Environment
2639A.9.1.2.2.2 Test Requirements 2640A.9.1.3 Test for V2X
Synchronization Reference Selection/Reselection 2641A.9.1.3.1 Test for
GNSS configured as the highest priority 2641A.9.1.3.1.1 Test Purpose and
Environment 2641A.9.1.3.1.2 Test Requirements 2643A.9.1.3.2 Test for FR1
NR Cell configured as the highest priority 2645A.9.1.3.2.1 Test Purpose
and Environment 2645A.9.1.3.2.2 Test Requirements 2647A.9.1.4 Test for
L1 SL-RSRP Measurement 2648A.9.1.4.1 Test for V2X UE Autonomous Resource
Selection/Reselection 2648A.9.1.4.1.1 Test Purpose and Environment
2648A.9.1.4.1.2 Test Requirements 2651A.9.1.4.2 Test for V2X UE Resource
Pre-emption 2652A.9.1.4.2.1 Test Purpose and Environment 2652A.9.1.4.2.2
Test Requirements 2655A.9.1.4.3 Test for V2X UE Resource Re-evaluation
2655A.9.1.4.3.1 Test Purpose and Environment 2655A.9.1.4.3.2 Test
Requirements 2662A.9.1.5 Test for Congestion Control Measurement
2662A.9.1.5.1 Test Purpose and Environment 2662A.9.1.5.2 Test
Requirements 2668A.9.1.6 Test for Interruption 2668A.9.1.6.1 Test for
Interruption to WAN due to V2X Sidelink Communication 2668A.9.1.6.1.1
Test Purpose and Environment 2668A.9.1.6.1.2 Test Requirements 2671A.10
EN-DC Tests with NR PSCell under CCA and Other NR Cells in FR1
2671A.10.1 RRC\_CONNECTED state mobility 2671A.10.1.1 RRC connection
mobility control 2671A.10.1.1.1 Random Access 2671A.10.1.1.1.1 4-step RA
type contention-based random access for NR PSCell with CCA
2671A.10.1.1.1.1.1 Test Purpose and Environment 2671A.10.1.1.1.1.2 Test
Requirements 2674A.10.1.1.1.1.2.1 Random Access Preamble Transmission
2674A.10.1.1.1.1.2.2 Random Access Response Reception
2674A.10.1.1.1.1.2.3 No Random Access Response Reception
2675A.10.1.1.1.1.2.4 Receiving an UL grant for msg3 retransmission
2675A.10.1.1.1.1.2.5 Contention Resolution Timer expiry 2675A.10.1.1.1.2
4-step RA type non-contention based random access for NR PSCell with CCA
2676A.10.1.1.1.2.1 Test Purpose and Environment 2676A.10.1.1.1.2.2 Test
Requirements 2679A.10.1.1.1.2.2.1 SSB-based Random Access Preamble
Transmission 2679A.10.1.1.1.2.2.2 Random Access Response Reception
2680A.10.1.1.1.2.2.3 No Random Access Response Reception
2680A.10.1.1.1.3 2-step RA type contention-based random access for NR
PSCell with CCA 2680A.10.1.1.1.3.1 Test Purpose and Environment
2680A.10.1.1.1.3.2 Test Requirements 2684A.10.1.1.1.3.2.1 MsgA
Transmission 2684A.10.1.1.1.3.2.2 MsgB Reception 2684A.10.1.1.1.3.2.3 No
MsgB Reception 2685A.10.1.1.1.4 2-step RA type non-contention based
random access for NR PSCell with CCA 2685A.10.1.1.1.4.1 Test Purpose and
Environment 2685A.10.1.1.1.4.2 Test Requirements 2689A.10.1.1.1.4.2.1
MsgA Transmission 2689A.10.1.1.1.4.2.2 MsgB Reception
2690A.10.1.1.1.4.2.3 No MsgB Reception 2690A.10.2 Timing 2691A.10.2.1 UE
transmit timing 2691A.10.2.2 UE timing advance 2695A.10.3 Signalling
characteristics 2698A.10.3.1 Radio link monitoring 2698A.10.3.1.1
Introduction 2698A.10.3.1.2 Radio link monitoring out-of-sync test for
PSCell configured with SSB-based RLM RS in non-DRX mode 2699A.10.3.1.2.1
Test purpose and environment 2699A.10.3.1.2.2 Test requirements
2704A.10.3.1.3 Radio link monitoring in-sync test for PSCell configured
with SSB-based RLM RS in non-DRX mode 2704A.10.3.1.3.1 Test purpose and
environment 2704A.10.3.1.3.2 Test requirements 2710A.10.3.1.4 Void
2710A.10.3.1.4.1 Void 2710A.10.3.1.4.2 Void 2710A.10.3.1.5 Void
2710A.10.3.1.5.1 Void 2710A.10.3.1.5.2 Void 2710A.10.3.2 Void
2711A.10.3.3 SCell activation and deactivation delay 2711A.10.3.3.2
SCell Activation and Deactivation of known NR SCell with NR PSCell and
NR SCell under CCA, 640 ms SCell measurement cycle 2715A.10.3.3.2.1 Test
Purpose and Environment 2715A.10.3.3.2.2 Test Requirements
2716A.10.3.3.3 SCell Activation and Deactivation of unknown NR SCell
with NR PSCell and NR SCell under CCA 2716A.10.3.3.3.1 Test Purpose and
Environment 2716A.10.3.3.3.2 Test Requirements 2717A.10.3.4 Beam failure
detection and link recovery procedures 2717A.10.3.4.1 EN-DC Beam Failure
Detection and Link Recovery Test for FR1 PSCell configured with
SSB-based BFD and LR in non-DRX mode 2717A.10.3.4.1.1 Test Purpose and
Environment 2717A.10.3.4.1.2 Test Requirements 2722A.10.3.4.2 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 PSCell configured with
SSB-based BFD and LR in DRX mode 2722A.10.3.4.2.1 Test Purpose and
Environment 2722A.10.3.4.2.2 Test Requirements 2728A.10.3.5 Active BWP
switching 2728A.10.3.5.1 UL active BWP switch delay with consistent UL
LBT failure on PSCell subject to UL CCA in EN-DC 2728A.10.3.5.1.1 Test
Purpose and Environment 2728A.10.3.5.1.2 Test Requirements
2733A.10.3.5.2 DCI-based and Timer-based Active BWP Switch
2734A.10.3.5.2.1 E-UTRAN -- NR PSCell FR1 DL active BWP switch in
non-DRX in synchronous EN-DC 2734A.10.3.5.2.2 E-UTRAN -- NR PSCell FR1
DL active BWP switch with FR1 SCell in non-DRX in synchronous EN-DC
2737A.10.3.5.3 RRC-based Active BWP Switch 2741A.10.3.6 PSCell addition
and release delay 2745A.10.3.6.1 Addition and Release Delay of known NR
PSCell on the carrier under CCA 2745A.10.3.6.1.1 Test purpose and
environment 2745A.10.3.6.1.2 Test Requirements 2750A.10.3.7 Void
2751A.10.4 Measurement procedure 2751A.10.4.1 Intra-frequency
measurements 2751A.10.4.1.1 Event-triggered reporting tests on PSCC
without gaps under non-DRX 2751A.10.4.1.1.1 Test purpose and environment
2751A.10.4.1.1.2 Test parameters 2751A.10.4.1.1.3 Test Requirements
2755A.10.4.1.2 Void 2755A.10.4.1.3 Void 2755A.10.4.1.4 Event-triggered
reporting tests on PSCC with per-UE gaps under DRX 2755A.10.4.1.4.1 Test
purpose and environment 2755A.10.4.1.4.2 Test parameters
2756A.10.4.1.4.3 Test Requirements 2760A.10.4.1.5 Void 2761A.10.4.1.6
Void 2761A.10.4.1.7 Void 2761A.10.4.1.8 Void 2761A.10.4.1.9 Void
2761A.10.4.1.10 Void 2761A.10.4.1.11 Void 2761A.10.4.1.12 Void
2761A.10.4.2 Inter-frequency measurements 2761A.10.4.2.1 Void
2761A.10.4.2.2 Void 2761A.10.4.2.3 EN-DC event triggered reporting tests
for FR1 with CCA cell without SSB time index detection when DRX is not
used 2761A.10.4.2.3.1 Test Purpose and Environment 2761A.10.4.2.3.2 Test
Requirements 2765A.10.4.2.4 EN-DC event triggered reporting tests for
FR1 cell with CCA without SSB time index detection when DRX is used
2766A.10.4.2.4.1 Test Purpose and Environment 2766A.10.4.2.4.2 Test
Requirements 2770A.10.4.2.5 EN-DC event triggered reporting tests for
FR1 cell with CCA with SSB time index detection when DRX is not used
2771A.10.4.2.5.1 Test Purpose and Environment 2771A.10.4.2.5.2 Test
Requirements 2775A.10.4.2.6 EN-DC event triggered reporting tests for
FR1 cell with CCA with SSB time index detection when DRX is used
2776A.10.4.2.6.1 Test Purpose and Environment 2776A.10.4.2.6.2 Test
Requirements 2780A.10.4.2.7 EN-DC event triggered reporting tests for
FR1 cell without SSB time index detection when DRX is not used
2781A.10.4.2.7.1 Test Purpose and Environment 2781A.10.4.2.7.2 Test
Requirements 2787A.10.4.2.8 EN-DC event triggered reporting tests for
FR1 cell without SSB time index detection when DRX is used
2787A.10.4.2.8.1 Test Purpose and Environment 2787A.10.4.2.8.2 Test
Requirements 2793A.10.4.2.9 EN-DC event triggered reporting tests for
FR1 cell with SSB time index detection when DRX is not used
2794A.10.4.2.9.1 Test Purpose and Environment 2794A.10.4.2.9.2 Test
Requirements 2799A.10.4.2.10 EN-DC event triggered reporting tests for
FR1 cell with SSB time index detection when DRX is used
2799A.10.4.2.10.1 Test Purpose and Environment 2799A.10.4.2.10.2 Test
Requirements 2805A.10.4.3 L1-RSRP measurements for beam reporting
2806A.10.4.3.1 SSB based L1-RSRP measurement on PSCC when DRX is not
used 2806A.10.4.3.1.1 Test Purpose and Environment 2806A.10.4.3.1.2 Test
parameters 2806A.10.4.3.1.3 Test Requirements 2808A.10.4.3.2 SSB based
L1-RSRP measurement on PSCC when DRX is used 2809A.10.4.3.2.1 Test
Purpose and Environment 2809A.10.4.3.2.2 Test parameters
2809A.10.4.3.2.3 Test Requirements 2811A.10.4.3.3 SSB based L1-RSRP
measurement on SCC when DRX is not used 2812A.10.4.3.3.1 Test Purpose
and Environment 2812A.10.4.3.3.2 Test parameters 2812A.10.4.3.3.3 Test
Requirements 2815A.10.4.3.4 SSB based L1-RSRP measurement on SCC when
DRX is used 2816A.10.4.3.4.1 Test Purpose and Environment
2816A.10.4.3.4.2 Test parameters 2816A.10.4.3.4.3 Test Requirements
2819A.10.4.4 E-UTRAN−NR inter-RAT measurements on NR carrier frequency
under CCA 2820A.10.4.4.1 E-UTRA-NR inter-RAT event triggered reporting
tests for FR1 without SSB time index detection when DRX is not used
2820A.10.4.4.1.1 Test Purpose and Environment 2820A.10.4.4.1.2 Test
Requirements 2827A.10.4.4.2 E-UTRA-NR inter-RAT event triggered
reporting tests for FR1 without SSB time index detection when DRX is
used 2827A.10.4.4.2.1 Test Purpose and Environment 2827A.10.4.4.2.2 Test
Requirements 2834A.10.4.4.3 NR Inter-RAT event triggered reporting tests
for FR1 with SSB time index detection when DRX is not used
2834A.10.4.4.3.1 Test Purpose and Environment 2834A.10.4.4.3.2 Test
Requirements 2841A.10.4.4.4 NR Inter-RAT event triggered reporting tests
for FR1 with SSB time index detection when DRX is used 2841A.10.4.4.4.1
Test Purpose and Environment 2841A.10.4.4.4.2 Test Requirements
2849A.10.5 Measurement performance 2849A.10.5.1 SS-RSRP 2849A.10.5.1.1
Intra-frequency measurement accuracy on a CCA serving cell
2849A.10.5.1.1.1 Test Purpose and Environment 2849A.10.5.1.1.2 Test
parameters 2849A.10.5.1.1.3 Test Requirements 2852A.10.5.1.2
Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1
CCA target cell 2852A.10.5.1.2.1 Test Purpose and Environment
2852A.10.5.1.2.2 Test parameters 2852A.10.5.1.2.3 Test Requirements
2856A.10.5.2 SS-RSRQ 2856**A.10.5.2.1** **Intra-frequency measurement
accuracy with FR1 CCA serving cell and FR1 CCA target cell**
2856A.10.5.2.1.1 Test Purpose and Environment 2856A.10.5.2.1.2 Test
Parameters 2856A.10.5.2.1.3 Test Requirements 2859**A.10.5.2.2**
**Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1
CCA target cell** 2859A.10.5.2.2.1 Test Purpose and Environment
2859A.10.5.2.2.2 Test Parameters 2859A.10.5.2.2.3 Test Requirements
2862A.10.5.3 SS-SINR 2862A.10.5.3.1 Intra-frequency measurement accuracy
on PSCC 2862A.10.5.3.1.1 Test Purpose and Environment 2862A.10.5.3.1.2
Test Parameters 2862A.10.5.3.1.3 Test Requirements 2865A.10.5.3.2
Inter-frequency measurement accuracy on PSCC 2865A.10.5.3.2.1 Test
Purpose and Environment 2865A.10.5.3.2.2 Test Parameters
2865A.10.5.3.2.3 Test Requirements 2869A.10.5.3.3 Intra-frequency
measurement accuracy on SCC 2869A.10.5.3.3.1 Test Purpose and
Environment 2869A.10.5.3.3.2 Test Parameters 2869A.10.5.3.3.3 Test
Requirements 2872A.10.5.4 L1-RSRP measurement for beam reporting with
CCA serving cell 2872A.10.5.4.1 SSB based L1-RSRP measurement
2872A.10.5.4.1.1 Test Purpose and Environment 2872A.10.5.4.1.2 Test
parameters 2873A.10.5.4.1.3 Test Requirements 2875A.10.5.5 RSSI
2875A.10.5.5.1 RSSI measurement accuracy on PSCC with CCA
2875A.10.5.5.1.1 Test Purpose and Environment 2875A.10.5.5.1.2 Test
parameters 2875A.10.5.5.1.3 Test Requirements 2878A.10.5.5.2 RSSI
measurement accuracy on SCC with CCA 2878A.10.5.5.2.1 Test Purpose and
Environment 2878A.10.5.5.2.2 Test parameters 2878A.10.5.5.2.3 Test
Requirements 2881A.10.5.5.3 Inter-frequency RSSI measurement accuracy on
a carrier with CCA 2881A.10.5.5.3.1 Test Purpose and Environment
2881A.10.5.5.3.2 Test parameters 2881A.10.5.5.3.3 Test Requirements
2885A.10.5.6 Channel occupancy 2885A.10.5.6.1 Channel occupancy
measurement accuracy on PSCC with CCA 2885A.10.5.6.1.1 Test Purpose and
Environment 2885A.10.5.6.1.2 Test parameters 2885A.10.5.6.1.3 Test
Requirements 2889A.10.5.6.2 Channel occupancy measurement accuracy on
SCC with CCA 2889A.10.5.6.2.1 Test Purpose and Environment
2889A.10.5.6.2.2 Test parameters 2889A.10.5.6.2.3 Test Requirements
2892A.10.5.6.3 Inter-frequency channel occupancy measurement accuracy on
a carrier with CCA 2892A.10.5.6.3.1 Test Purpose and Environment
2892A.10.5.6.3.2 Test parameters 2892A.10.5.6.3.3 Test Requirements
2896A.11 NR Standalone Tests with NR PCell under CCA and Other NR Cells
in FR1 2896A.11.1 RRC\_IDLE state mobility 2897A.11.1.1 Cell
re-selection with both source and target NR carrier frequencies under
CCA 2897A.11.1.1.1 Cell reselection to FR1 intra-frequency NR cells when
subject to CCA on the serving and target cell 2897A.11.1.1.1.1 Test
Purpose and Environment 2897A.11.1.1.1.2 Test Parameters
2897A.11.1.1.1.3 Test Requirements 2900A.11.1.1.2 Cell reselection to
FR1 inter-frequency NR case when subject to CCA on the serving and
target cell 2900A.11.1.1.2.1 Test Purpose and Environment
2900A.11.1.1.2.2 Test Parameters 2900A.11.1.1.2.3 Test Requirements
2904A.11.1.2 Cell re-selection to NR with source NR carrier frequency
under CCA 2904A.11.1.2.1 Cell reselection to FR1 inter-frequency NR case
when serving cell is subject to CCA 2904A.11.1.2.1.1 Test Purpose and
Environment 2904A.11.1.2.1.2 Test Parameters 2905A.11.1.2.1.3 Test
Requirements 2911A.11.1.3 Cell re-selection from NR carrier with target
NR carrier frequency under CCA 2912A.11.1.3.1 Cell reselection to FR1
inter-frequency NR case when target cell is subject to CCA
2912A.11.1.3.1.1 Test Purpose and Environment 2912A.11.1.3.1.2 Test
Parameters 2912A.11.1.3.1.3 Test Requirements 2917A.11.1.4 Inter-RAT
cell re-selection to E-UTRAN with source NR carrier frequency under CCA
2918A.11.1.4.1 Cell reselection to higher priority E-UTRAN when serving
cell is subject to CCA 2918A.11.1.4.1.1 Test Purpose and Environment
2918A.11.1.4.1.2 Test Parameters 2918A.11.1.4.1.3 Test Requirements
2921A.11.1.4.2 Cell reselection to lower priority E-UTRAN when serving
cell is subject to CCA 2922A.11.1.4.2.1 Test Purpose and Environment
2922A.11.1.4.2.2 Test Requirements 2924A.11.2 RRC\_CONNECTED state
mobility 2925A.11.2.1 Handover 2925A.11.2.1.1 Intra-frequency handover
from FR1 carrier under CCA to FR1 carrier under CCA; known target cell
2925A.11.2.1.1.1 Test Purpose and Environment 2925A.11.2.1.1.2 Test
Parameters 2925A.11.2.1.1.3 Test Requirements 2928A.11.2.1.2
Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under
CCA; unknown target cell 2928A.11.2.1.2.1 Test Purpose and Environment
2928A.11.2.1.2.2 Test Parameters 2928A.11.2.1.2.3 Test Requirements
2931A.11.2.1.3 Inter-frequency handover from FR1 carrier under CCA to
FR1 carrier under CCA; unknown target cell 2931A.11.2.1.3.1 Test Purpose
and Environment 2931A.11.2.1.3.2 Test Parameters 2931A.11.2.1.3.3 Test
Requirements 2934A.11.2.1.4 Inter-frequency handover from FR1 carrier
under CCA to FR1; known target cell 2934A.11.2.1.4.1 Test Purpose and
Environment 2934A.11.2.1.4.2 Test Parameters 2934A.11.2.1.4.3 Test
Requirements 2938A.11.2.1.5 Inter-frequency handover from FR1 carrier
under CCA to FR1; unknown target cell 2939A.11.2.1.5.1 Test Purpose and
Environment 2939A.11.2.1.5.2 Test Parameters 2939A.11.2.1.5.3 Test
Requirements 2942A.11.2.1.6 Inter-frequency handover from FR1 to FR1
carrier under CCA; unknown target cell 2943A.11.2.1.6.1 Test Purpose and
Environment 2943A.11.2.1.6.2 Test Parameters 2943A.11.2.1.6.3 Test
Requirements 2948A.11.2.1.7 SA NR FR1 carrier under CCA - E-UTRAN
handover with known target cell 2948A.11.2.1.7.1 Test Purpose and
Environment 2948A.11.2.1.7.2 Test Requirements 2954A.11.2.1.8 SA NR FR1
carrier under CCA - E-UTRAN handover with unknown target cell
2954A.11.2.1.8.1 Test Purpose and Environment 2954A.11.2.1.8.2 Test
Requirements 2959A.11.2.2 RRC connection mobility control 2959A.11.2.2.1
RRC re-establishment 2959A.11.2.2.1.1 Intra-frequency RRC
Re-establishment with CCA in FR1 2959A.11.2.2.1.2 Inter-frequency RRC
Re-establishment with CCA in FR1 2962A.11.2.2.1.3 Intra-frequency RRC
Re-establishment with CCA in FR1 without serving cell timing
2968A.11.2.2.1.4 Inter-frequency RRC Re-establishment from NR FR1
carrier without CCA to NR FR1 carrier under CCA 2972A.11.2.2.2 Random
Access 2977A.11.2.2.2.1 4-step RA type contention-based random access
for NR PCell with CCA 2977A.11.2.2.2.1.1 Test Purpose and Environment
2977A.11.2.2.2.1.2 Test Requirements 2980A.11.2.2.2.1.2.1 Random Access
Preamble Transmission 2980A.11.2.2.2.1.2.2 Random Access Response
Reception 2980A.11.2.2.2.1.2.3 No Random Access Response Reception
2981A.11.2.2.2.1.2.4 Receiving an UL grant for msg3 retransmission
2981A.11.2.2.2.1.2.5 Reception of an Incorrect Message over Temporary
C-RNTI 2981A.11.2.2.2.1.2.6 Reception of a Correct Message over
Temporary C-RNTI 2982A.11.2.2.2.1.2.7 Contention Resolution Timer expiry
2982A.11.2.2.2.2 4-step RA type non-contention based random access for
NR PSCell with CCA 2982A.11.2.2.2.2.1 Test Purpose and Environment
2982A.11.2.2.2.2.2 Test Requirements 2985A.11.2.2.2.2.2.1 SSB-based
Random Access Preamble Transmission 2985A.11.2.2.2.2.2.2 Random Access
Response Reception 2986A.11.2.2.2.2.2.3 No Random Access Response
Reception 2986A.11.2.2.2.3 2-step RA type contention-based random access
for NR PCell with CCA 2986A.11.2.2.2.3.1 Test Purpose and Environment
2986A.11.2.2.2.3.2 Test Requirements 2990A.11.2.2.2.3.2.1 MsgA
Transmission 2990A.11.2.2.2.3.2.2 MsgB Reception 2990A.11.2.2.2.3.2.3 No
MsgB Reception 2991A.11.2.2.2.4 2-step RA type non-contention-based
random access for NR PCell with CCA 2991A.11.2.2.2.4.1 Test Purpose and
Environment 2991A.11.2.2.2.4.2 Test Requirements 2995A.11.2.2.2.4.2.1
MsgA Transmission 2995A.11.2.2.2.4.2.2 MsgB Reception
2996A.11.2.2.2.4.2.3 No MsgB Reception 2996A.11.2.2.3 RRC connection
release with redirection 2997A.11.2.2.3.1 Redirection from NR FR1
carrier under CCA to NR FR1 carrier under CCA 2997A.11.3 Timing
3005A.11.3.1 UE transmit timing 3005A.11.3.2 UE timing advance
3009A.11.3.2.1 UE Timing Advance Adjustment Accuracy with PCell under DL
CCA 3009A.11.3.2.1.1 Test Purpose and Environment 3009A.11.3.2.1.2 Test
Parameters 3009A.11.3.2.1.3 Test Requirements 3013A.11.4 Signalling
characteristics 3013A.11.4.1 Radio link monitoring 3013A.11.4.1.1
Introduction 3013A.11.4.1.2 Radio link monitoring out-of-sync test for
PCell configured with SSB-based RLM RS in non-DRX mode 3014A.11.4.1.2.1
Test purpose and environment 3014A.11.4.1.2.2 Test requirements
3018A.11.4.1.3 Radio link monitoring in-sync test for PCell configured
with SSB-based RLM RS in non-DRX mode 3018A.11.4.1.3.1 Test purpose and
environment 3018A.11.4.1.3.2 Test requirements 3024A.11.4.1.4 Void
3024A.11.4.1.4.1 Void 3024A.11.4.1.4.2 Void 3024A.11.4.1.5 Void
3024A.11.4.1.5.1 Void 3024A.11.4.1.5.2 Void 3024A.11.4.2 Void
3025A.11.4.3 SCell activation and deactivation delay 3025A.11.4.3.2
SCell Activation and Deactivation of known SCell with PCell and SCell
under CCA, 640 ms SCell measurement cycle 3029A.11.4.3.2.1 Test Purpose
and Environment 3029A.11.4.3.2.2 Test Requirements 3030A.11.4.4 Beam
failure detection and link recovery procedures 3031A.11.4.4.1 Beam
Failure Detection and Link Recovery Test for FR1 PCell configured with
SSB-based BFD and LR in non-DRX mode 3031A.11.4.4.1.1 Test Purpose and
Environment 3031A.11.4.4.1.2 Test Requirements 3037A.11.4.4.2 Beam
Failure Detection and Link Recovery Test for FR1 PCell configured with
SSB-based BFD and LR in DRX mode 3037A.11.4.4.2.1 Test Purpose and
Environment 3037A.11.4.4.2.2 Test Requirements 3043A.11.4.5 Active BWP
switching 3043A.11.4.5.1 UL active BWP switch delay with consistent UL
LBT failure on PCell subject to UL CCA 3043A.11.4.5.1.1 Test Purpose and
Environment 3043A.11.4.5.1.2 Test Requirements 3047A.11.4.6 Void
3057A.11.5 Measurement procedure 3057A.11.5.1 Intra-frequency
measurements 3057A.11.5.1.1 Event-triggered reporting tests on PCC
without gaps under non-DRX 3057A.11.5.1.1.1 Test purpose and environment
3057A.11.5.1.1.2 Test parameters 3057A.11.5.1.1.3 Test Requirements
3061A.11.5.1.2 Event-triggered reporting tests on PCC without gaps under
DRX 3061A.11.5.1.2.1 Test purpose and environment 3061A.11.5.1.2.2 Test
parameters 3061A.11.5.1.2.3 Test Requirements 3065A.11.5.1.3 Void
3065A.11.5.1.4 Void 3065A.11.5.1.5 Void 3065A.11.5.1.6 Void
3065A.11.5.1.7 Void 3065A.11.5.1.8 Void 3065A.11.5.1.9 Void
3065A.11.5.1.10 Void 3065A.11.5.1.11 Void 3065A.11.5.1.12 Void
3065A.11.5.2 Inter-frequency measurements 3066A.11.5.2.1 Void
3066A.11.5.2.2 Void 3066A.11.5.2.3 Event triggered reporting tests for
FR1 with CCA without SSB time index detection when DRX is not used
3066A.11.5.2.3.1 Test Purpose and Environment 3066A.11.5.2.3.2 Test
Requirements 3070A.11.5.2.4 Event triggered reporting tests for FR1 with
CCA without SSB time index detection when DRX is used 3071A.11.5.2.4.1
Test Purpose and Environment 3071A.11.5.2.4.2 Test Requirements
3076A.11.5.2.5 Event triggered reporting tests for FR1 with CCA with SSB
time index detection when DRX is not used 3076A.11.5.2.5.1 Test Purpose
and Environment 3076A.11.5.2.5.2 Test Requirements 3080A.11.5.2.6 Event
triggered reporting tests for FR1 with CCA with SSB time index detection
when DRX is used 3081A.11.5.2.6.1 Test Purpose and Environment
3081A.11.5.2.6.2 Test Requirements 3086A.11.5.2.7 Event triggered
reporting tests for FR1 without SSB time index detection when DRX is not
used 3086A.11.5.2.7.1 Test Purpose and Environment 3086A.11.5.2.7.2 Test
Requirements 3090A.11.5.2.8 Event triggered reporting tests for FR1
without SSB time index detection when DRX is used 3091A.11.5.2.8.1 Test
Purpose and Environment 3091A.11.5.2.8.2 Test Requirements
3096A.11.5.2.9 Event triggered reporting tests for FR1 with SSB time
index detection when DRX is not used 3096A.11.5.2.9.1 Test Purpose and
Environment 3096A.11.5.2.9.2 Test Requirements 3100A.11.5.2.10 Event
triggered reporting tests for FR1 with SSB time index detection when DRX
is used 3101A.11.5.2.10.1 Test Purpose and Environment 3101A.11.5.2.10.2
Test Requirements 3106A.11.5.3 Inter-RAT E-UTRAN measurements
3106A.11.5.3.1 SA NR - E-UTRAN event-triggered reporting in non-DRX in
FR1 3106A.11.5.3.1.1 Test Purpose and Environment 3106A.11.5.3.1.2 Test
Requirements 3112A.11.5.3.2 SA NR - E-UTRAN event-triggered reporting in
DRX in FR1 3112A.11.5.3.2.1 Test Purpose and Environment
3112A.11.5.3.2.2 Test Requirements 3118A.11.5.4 L1-RSRP measurements for
beam reporting 3118A.11.5.4.1 SSB based L1-RSRP measurement when DRX is
not used 3118A.11.5.4.1.1 Test Purpose and Environment 3118A.11.5.4.1.2
Test parameters 3118A.11.5.4.1.3 Test Requirements 3120A.11.5.4.2 SSB
based L1-RSRP measurement when DRX is used 3120A.11.5.4.2.1 Test Purpose
and Environment 3120A.11.5.4.2.2 Test parameters 3121A.11.5.4.2.3 Test
Requirements 3123A.11.5.4.3 SSB based L1-RSRP measurement on SCC when
DRX is not used 3123A.11.5.4.3.1 Test Purpose and Environment
3123A.11.5.4.3.2 Test parameters 3124A.11.5.4.3.3 Test Requirements
3127A.11.5.4.4 SSB based L1-RSRP measurement on SCC when DRX is used
3128A.11.5.4.4.1 Test Purpose and Environment 3128A.11.5.4.4.2 Test
parameters 3128A.11.5.4.4.3 Test Requirements 3131A.11.6 Measurement
performance 3132A.11.6.1 SS-RSRP 3132A.11.6.1.1 Intra-frequency
measurement accuracy on a carrier frequency with CCA 3132A.11.6.1.1.1
Test Purpose and Environment 3132A.11.6.1.1.2 Test parameters
3132A.11.6.1.1.3 Test Requirements 3134A.11.6.1.2 Intra-frequency
measurement accuracy on SCC on a carrier frequency with CCA
3134A.11.6.1.2.1 Test Purpose and Environment 3134A.11.6.1.2.2 Test
parameters 3134A.11.6.1.2.3 Test Requirements 3136A.11.6.2 SS-RSRQ
3136A.11.6.2.1 Intra-frequency measurement accuracy 3136A.11.6.2.1.1
Test Purpose and Environment 3136A.11.6.2.1.2 Test Parameters
3136A.11.6.2.1.3 Test Requirements 3139A.11.6.2.2 Inter-frequency
measurement accuracy 3139A.11.6.2.2.1 Test Purpose and Environment
3139A.11.6.2.2.2 Test Parameters 3139A.11.6.2.2.3 Test Requirements
3142A.11.6.2.3 Intra-frequency measurement accuracy on SCC
3142A.11.6.2.3.1 Test Purpose and Environment 3142A.11.6.2.3.2 Test
Parameters 3142A.11.6.2.3.3 Test Requirements 3145A.11.6.2.4
Inter-frequency measurement accuracy 3145A.11.6.2.4.1 Test Purpose and
Environment 3145A.11.6.2.4.2 Test Parameters 3145A.11.6.2.4.3 Test
Requirements 3152A.11.6.3 SS-SINR 3152A.11.6.3.1 Intra-frequency
measurement accuracy 3152A.11.6.3.1.1 Test Purpose and Environment
3152A.11.6.3.1.2 Test Parameters 3152A.11.6.3.1.3 Test Requirements
3155A.11.6.3.2 Inter-frequency measurement accuracy 3155A.11.6.3.2.1
Test Purpose and Environment 3155A.11.6.3.2.2 Test Parameters
3155A.11.6.3.2.3 Test Requirements 3158A.11.6.3.3 Intra-frequency
measurement accuracy on SCC 3158A.11.6.3.3.1 Test Purpose and
Environment 3158A.11.6.3.3.2 Test Parameters 3158A.11.6.3.3.3 Test
Requirements 3161A.11.6.3.4 Inter-frequency measurement accuracy
3161A.11.6.3.4.1 Test Purpose and Environment 3161A.11.6.3.4.2 Test
Parameters 3161A.11.6.3.4.3 Test Requirements 3169A.11.6.4 L1-RSRP
measurement for beam reporting with CCA serving cell 3169A.11.6.4.1 SSB
based L1-RSRP measurement 3169A.11.6.4.1.1 Test Purpose and Environment
3169A.11.6.4.1.2 Test parameters 3170A.11.6.4.1.3 Test Requirements
3173A.11.6.5 RSSI 3173A.11.6.5.1 Intra-frequency RSSI measurement
accuracy on PCC with CCA 3173A.11.6.5.1.1 Test Purpose and Environment
3173A.11.6.5.1.2 Test parameters 3173A.11.6.5.1.3 Test Requirements
3176A.11.6.5.2 Intra-frequency RSSI measurement accuracy on SCC with CCA
3176A.11.6.5.2.1 Test Purpose and Environment 3176A.11.6.5.2.2 Test
parameters 3176A.11.6.5.2.3 Test Requirements 3179A.11.6.5.3
Inter-frequency RSSI measurement accuracy on a carrier with CCA
3179A.11.6.5.3.1 Test Purpose and Environment 3179A.11.6.5.3.2 Test
parameters 3179A.11.6.5.3.3 Test Requirements 3183A.11.6.6 Channel
occupancy 3183A.11.6.6.1 Intra-frequency channel occupancy measurement
accuracy on PCC with CCA 3183A.11.6.6.1.1 Test Purpose and Environment
3183A.11.6.6.1.2 Test parameters 3183A.11.6.6.1.3 Test Requirements
3187A.11.6.6.2 Intra-frequency channel occupancy measurement accuracy on
SCC with CCA 3187A.11.6.6.2.1 Test Purpose and Environment
3187A.11.6.6.2.2 Test parameters 3187A.11.6.6.2.3 Test Requirements
3190A.11.6.6.3 Inter-frequency channel occupancy measurement accuracy on
a carrier with CCA 3190A.11.6.6.3.1 Test Purpose and Environment
3190A.11.6.6.3.2 Test parameters 3190A.11.6.6.3.3 Test Requirements
3194A.11.6.7 E-UTRAN RSRP 3195A.11.6.8 E-UTRAN RSRQ 3195A.11.6.9 E-UTRAN
SINR 3195A.12 E-UTRA Standalone Tests with at Least One NR Cell under
CCA 3195A.12.1 RRC\_IDLE state mobility 3195A.12.1.1 Inter-RAT cell
re-selection to NR on a carrier frequency with CCA 3195A.12.1.1.1 E-UTRA
Cell reselection to higher priority NR target Cell in FR1 when target
cell is subject to CCA 3195A.12.1.1.1.1 Test Purpose and Environment
3195A.12.1.1.1.2 Test Requirements 3200A.12.2 RRC\_CONNECTED state
mobility 3201A.12.2.1 Handover 3201A.12.2.1.1 E-UTRAN - NR with CCA
handover 3201A.12.2.1.1.1 Test Purpose and Environment 3201A.12.2.1.1.2
Test Requirements 3206A.12.3 Void 3207A.12.4 Measurement procedure
3207A.12.4.1 E-UTRAN−NR inter-RAT SFTD measurements 3207A.12.4.1.1
E-UTRA -- NR Inter-RAT SFTD Measurement Delay with NR under CCA in
non-DRX 3207A.12.4.1.1.1 Test Purpose and Environment 3207A.12.4.1.1.2
Test Requirements 3211A.12.4.2 E-UTRAN−NR inter-RAT measurements on NR
carrier frequency under CCA 3211A.12.4.2.1 E-UTRA-NR inter-RAT event
triggered reporting tests for FR1 without SSB time index detection when
DRX is not used 3211A.12.4.2.1.1 Test Purpose and Environment
3211A.12.4.2.1.2 Test Requirements 3217A.12.4.2.2 E-UTRA-NR inter-RAT
event triggered reporting tests for FR1 without SSB time index detection
when DRX is used 3217A.12.4.2.2.1 Test Purpose and Environment
3217A.12.4.2.2.2 Test Requirements 3222A.12.4.2.3 NR Inter-RAT event
triggered reporting tests for FR1 with SSB time index detection when DRX
is not used 3222A.12.4.2.3.1 Test Purpose and Environment
3222A.12.4.2.3.2 Test Requirements 3227A.12.4.2.4 NR Inter-RAT event
triggered reporting tests for FR1 with SSB time index detection when DRX
is used 3227A.12.4.2.4.1 Test Purpose and Environment 3227A.12.4.2.4.2
Test Requirements 3232A.12.4.2.5 Void 3232A.12.4.2.6 Void 3232A.12.5
Measurement performance 3232A.12.5.1 E-UTRAN−NR SFTD 3232A.12.5.2 Void
3239A.12.5.3 Void 3239A.12.5.4 Void 3239A.12.5.5 Void 3239A.12.5.6 Void
3239A.13 NR Standalone Tests with NR SCell under CCA and All Other NR
Cells in FR1 3239A.13.1 Void 3239A.13.1.1 Void 3239A.13.1.2 Void
3239A.13.2 Signalling characteristics 3239A.13.2.1 Void 3239A.13.2.2
SCell activation and deactivation delay 3239A.13.2.2.2 SCell Activation
and Deactivation of known SCell under CCA, 640 ms SCell measurement
cycle 3244A.13.2.2.2.1 Test Purpose and Environment 3244A.13.2.2.2.2
Test Requirements 3245A.13.2.2.3 SCell Activation and Deactivation of
unknown SCell under CCA 3245A.13.2.2.3.1 Test Purpose and Environment
3245A.13.2.2.3.2 Test Requirements 3246A.13.2.3 Void 3246A.13.3
Measurement procedure 3246A.13.3.1 Intra-frequency measurements
3246A.13.3.1.1 Event-triggered reporting tests on SCC without gaps under
non-DRX 3246A.13.3.1.1.1 Test purpose and environment 3246A.13.3.1.1.2
Test parameters 3246A.13.3.1.1.3 Test Requirements 3251A.13.3.1.2
Event-triggered reporting tests on SCC without gaps under DRX
3251A.13.3.1.2.1 Test purpose and environment 3251A.13.3.1.2.2 Test
parameters 3251A.13.3.1.2.3 Test Requirements 3256A.13.3.1.3
Event-triggered reporting tests on SCC with per-UE gaps under non-DRX
3256A.13.3.1.3.1 Test purpose and environment 3256A.13.3.1.3.2 Test
parameters 3256A.13.3.1.3.3 Test Requirements 3261A.13.3.1.4
Event-triggered reporting tests on SCC with per-UE gaps under DRX
3261A.13.3.1.4.1 Test purpose and environment 3261A.13.3.1.4.2 Test
parameters 3261A.13.3.1.4.3 Test Requirements 3267A.13.3.1.5 Void
3267A.13.3.1.6 Void 3267A.13.3.2 Inter-frequency measurements
3267A.13.3.2.1 Void 3267A.13.3.2.2 Void 3267A.13.3.2.3 Event triggered
reporting tests for FR1 with CCA without SSB time index detection when
DRX is not used 3267A.13.3.2.3.1 Test Purpose and Environment
3267A.13.3.2.3.2 Test Requirements 3272A.13.3.2.4 Event triggered
reporting tests for FR1 with CCA without SSB time index detection when
DRX is used 3272A.13.3.2.4.1 Test Purpose and Environment
3272A.13.3.2.4.2 Test Requirements 3277A.13.3.2.5 Event triggered
reporting tests for FR1 with CCA with SSB time index detection when DRX
is not used 3278A.13.3.2.5.1 Test Purpose and Environment
3278A.13.3.2.5.2 Test Requirements 3283A.13.3.2.6 Event triggered
reporting tests for FR1 with CCA with SSB time index detection when DRX
is used 3283A.13.3.2.6.1 Test Purpose and Environment 3283A.13.3.2.6.2
Test Requirements 3288A.13.3.3 L1-RSRP measurements for beam reporting
3289A.13.3.3.1 SSB based L1-RSRP measurement when DRX is not used
3289A.13.3.3.1.1 Test Purpose and Environment 3289A.13.3.3.1.2 Test
parameters 3289A.13.3.3.1.3 Test Requirements 3293A.13.3.3.2 SSB based
L1-RSRP measurement when DRX is used 3294A.13.3.3.2.1 Test Purpose and
Environment 3294A.13.3.3.2.2 Test parameters 3294A.13.3.3.2.3 Test
Requirements 3298A.13.4 Measurement performance 3299A.13.4.1 SS-RSRP
3299A.13.4.1.1 Intra-frequency measurement accuracy on a carrier
frequency with CCA 3299A.13.4.1.1.1 Test Purpose and Environment
3299A.13.4.1.1.2 Test parameters 3299A.13.4.1.1.3 Test Requirements
3301A.13.4.2 SS-RSRQ 3301A.13.4.2.1 Intra-frequency measurement accuracy
on SCC 3301A.13.4.2.1.1 Test Purpose and Environment 3301A.13.4.2.1.2
Test Parameters 3301A.13.4.2.1.3 Test Requirements 3308A.13.4.3 SS-SINR
3308A.13.4.3.1 Intra-frequency measurement accuracy on SCC
3308A.13.4.3.1.1 Test Purpose and Environment 3308A.13.4.3.1.2 Test
Parameters 3308A.13.4.3.1.3 Test Requirements 3315A.13.4.4 L1-RSRP
measurement for beam reporting with CCA serving cell 3315A.13.4.4.1 SSB
based L1-RSRP measurement 3315A.13.4.4.1.1 Test Purpose and Environment
3315A.13.4.4.1.2 Test parameters 3316A.13.4.4.1.3 Test Requirements
3320A.13.4.5 RSSI 3320A.13.4.5.1 Intra-frequency RSSI measurement
accuracy on a carrier with CCA 3320A.13.4.5.1.1 Test Purpose and
Environment 3320A.13.4.5.1.2 Test parameters 3320A.13.4.5.1.3 Test
Requirements 3324A.13.4.5.2 Inter-frequency RSSI measurement accuracy on
a carrier with CCA 3324A.13.4.5.2.1 Test Purpose and Environment
3324A.13.4.5.2.2 Test parameters 3324A.13.4.5.2.3 Test Requirements
3328A.13.4.6 Channel occupancy 3328A.13.4.6.1 Intra-frequency channel
occupancy measurement accuracy on SCC with CCA 3328A.13.4.6.1.1 Test
Purpose and Environment 3328A.13.4.6.1.2 Test parameters
3328A.13.4.6.1.3 Test Requirements 3332A.13.4.6.2 Inter-frequency
channel occupancy measurement accuracy on a carrier with CCA
3332A.13.4.6.2.1 Test Purpose and Environment 3332A.13.4.6.2.2 Test
parameters 3332A.13.4.6.2.3 Test Requirements 3336Annex B (normative):
Conditions for RRM requirements applicability for operating bands
3328B.1 Conditions for NR RRC\_IDLE state mobility 3328B.1.1
Introduction 3328B.1.2 Conditions for measurements on NR intra-frequency
cells for cell re-selection 3328B.1.2A Conditions for measurements on NR
intra-frequency cells under CCA for cell re-selection 3329B.1.3
Conditions for measurements on NR inter-frequency cells for cell
re-selection 3330B.1.3A Conditions for measurements on NR
inter-frequency cells under CCA for cell re-selection 3330B.2 Conditions
for UE measurements procedures and performance requirements in
RRC\_CONNECTED state 3330B.2.1 Introduction 3330B.2.1.1 General
3330B.2.1.2 Derivation of Minimum SSB\_RP values for FR1 3330B.2.1.3
Derivation of Minimum SSB\_RP values for FR2 3330B.2.1.3.1 Minimum
SSB\_RP values for Rx Beam Peak angle of arrival 3331B.2.1.3.2 Minimum
SSB\_RP values for angle of arrival within Spherical coverage
3331B.2.1.4 Gain to SS-RSRP and CSI-RSRP measurement point for FR1
3332B.2.1.5 Gain to SS-RSRP and CSI-RSRP measurement point for FR2
3332B.2.1.5.1 Gain to SS-RSRP and CSI-RSRP measurement point for Rx Beam
Peak angle of arrival 3332B.2.1.5.2 Gain to SS-RSRP measurement point
for different frequency 3333B.2.1.5.3 Alignment of Rough beam to Rx beam
Peak 3333B.2.1.6 Gain to PRS-RSRP measurement point for FR2
3333B.2.1.6.1 Gain to PRS-RSRP measurement point for Rx Beam Peak angle
of arrival 3333B.2.2 Conditions for NR intra-frequency measurements
3334B.2.3 Conditions for NR inter-frequency measurements 3335B.2.4
Conditions for NR L1-RSRP reporting 3337B.2.4.1 Conditions for SSB based
L1-RSRP reporting 3337B.2.4.2 Conditions for CSI-RS based L1-RSRP
reporting 3338B.2.5 Conditions for RRC connection release with
redirection to NR 3339B.2.6 Void 3341B.2.6.1 Void 3341B.2.6.2 Void
3341B.2.7 Conditions for SRS-RSRP measurements 3341B.2.8 Conditions for
NR L1-SINR reporting 3342B.2.8.1 Conditions for L1-SINR reporting with
CSI-RS based CMR and no dedicated IMR configured 3342B.2.8.2 Conditions
for L1-SINR reporting with SSB based CMR and dedicated IMR configured
3343B.2.8.2.1 L1-SINR reporting with SSB based CMR and dedicated ZP-IMR
configured 3343B.2.8.2.2 L1-SINR reporting with SSB based CMR and
dedicated NZP-IMR configured 3343B.2.8.3 Conditions for L1-SINR
reporting with CSI-RS based CMR and dedicated IMR configured
3345B.2.8.3.1 L1-SINR reporting with CSI-RS based CMR and dedicated
ZP-IMR configured 3345B.2.8.3.2 L1-SINR reporting with CSI-RS based CMR
and dedicated NZP-IMR configured 3346B.2.9 Conditions for NR
intra-frequency measurements under CCA 3347B.2.10 Conditions for NR
inter-frequency measurements under CCA 3347B.2.11 Conditions for NR
L1-RSRP reporting under CCA 3347B.2.11.1 Conditions for SSB based
L1-RSRP reporting 3347B.2.12 Conditions for NR CSI-RS based
intra-frequency measurements 3348B.2.13 Conditions for NR CSI-RS based
inter-frequency measurements 3349B.2.14 Conditions for NR PRS-based
measurements 3351B.3 RRM Requirements Exceptions 3352B.3.1 Introduction
3352B.3.2 Receiver sensitivity relaxation for CA 3352B.3.2.1 Receiver
sensitivity relaxation for UE supporting CA in FR1 3352B.3.2.2 Receiver
sensitivity relaxation for UE configured with CA in FR1 3353B.3.2.2.1
Inter-band carrier aggregation 3353B.3.2.2.2 Reference sensitivity
exceptions due to UL harmonic interference for CA 3353B.3.2.2.3
Reference sensitivity exceptions due to intermodulation interference due
to 2UL CA 3353B.3.2.3 Receiver sensitivity relaxation for UE supporting
CA in FR2 3353B.3.2.4 Receiver sensitivity relaxation for UE configured
with CA in FR2 3353B.3.2.4.1 Intra-band contiguous carrier aggregation
3353B.3.2.4.2 Intra-band non-contiguous carrier aggregation 3354B.3.3
Receiver sensitivity relaxation for DC 3354B.3.3.1 Receiver sensitivity
relaxation for EN-DC 3354B.3.3.2 Receiver sensitivity relaxation for
NE-DC 3354B.3.4 Receiver sensitivity relaxation for SUL 3354B.3.4.1
Receiver sensitivity relaxation for UE supporting SUL in FR1 3354B.3.4.2
Receiver sensitivity relaxation for UE configured with SUL in FR1
3354B.3.4.2.1 Reference sensitivity exceptions due to UL harmonic
interference for SUL 3354B.4 Conditions for V2X 3354B.4.1 Test
parameters for GNSS signals 3354B.4.2 Conditions for PSBCH-RSRP Accuracy
Requirements 3355B.4.3 Conditions for Selection/Reselection to
Intra-frequency SyncRef UE 3355B.4.4 Conditions for L1 SL-RSRP Accuracy
Requirements 3355Annex C (informative): Change history 3357
