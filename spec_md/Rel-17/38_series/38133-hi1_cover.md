+----------------------------------+----------------------------------+
| 3GPP TS 38.133 V17.18.1          |                                  |
| (2025-06)                        |                                  |
+==================================+==================================+
| Technical Specification          |                                  |
+----------------------------------+----------------------------------+
| 3rd Generation Partnership       |                                  |
| Project;                         |                                  |
|                                  |                                  |
| Technical Specification Group    |                                  |
| Radio Access Network;            |                                  |
|                                  |                                  |
| NR;                              |                                  |
|                                  |                                  |
| Requirements for support of      |                                  |
| radio resource management        |                                  |
|                                  |                                  |
| (Release 17)                     |                                  |
+----------------------------------+----------------------------------+
|                                  |                                  |
+----------------------------------+----------------------------------+
| ![](./media/image1.jp            | ![](./media/image2.p             |
| eg){width="1.2881944444444444in" | ng){width="1.7680555555555555in" |
| height="0.9277777777777778in"}   | height="1.0722222222222222in"}   |
+----------------------------------+----------------------------------+
|                                  |                                  |
+----------------------------------+----------------------------------+
| The present document has been    |                                  |
| developed within the 3rd         |                                  |
| Generation Partnership Project   |                                  |
| (3GPP ^TM^) and may be further   |                                  |
| elaborated for the purposes of   |                                  |
| 3GPP.\                           |                                  |
| The present document has not     |                                  |
| been subject to any approval     |                                  |
| process by the 3GPP              |                                  |
| Organizational Partners and      |                                  |
| shall not be implemented.\       |                                  |
| This Specification is provided   |                                  |
| for future development work      |                                  |
| within 3GPP only. The            |                                  |
| Organizational Partners accept   |                                  |
| no liability for any use of this |                                  |
| Specification.\                  |                                  |
| Specifications and Reports for   |                                  |
| implementation of the 3GPP ^TM^  |                                  |
| system should be obtained via    |                                  |
| the 3GPP Organizational          |                                  |
| Partners\' Publications Offices. |                                  |
+----------------------------------+----------------------------------+

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

Foreword 1201 Scope 1222 References 1223 Definitions, symbols and
abbreviations 1233.1 Definitions 1233.2 Symbols 1253.3 Abbreviations
1263.4 Test tolerances 1283.5 Frequency bands grouping 1283.5.1
Introduction 1283.5.2 NR operating bands in FR1 1293.5.2A NR operating
bands for satellite access in FR1 1293.5.3 NR operating bands in FR2
1303.6 Applicability of requirements in this specification version
1303.6.1 RRC connected state requirements in DRX 1313.6.2 Number of
serving carriers 1313.6.2.1 Number of serving carriers for SA 1313.6.2.2
Number of serving carriers for EN-DC 1313.6.2.3 Number of serving
carriers for NE-DC 1313.6.2.4 Number of serving carriers for NR-DC
1323.6.3 Applicability for intra-band FR2 1323.6.4 Applicability for FR2
UE power classes 1323.6.5 Applicability for SDL bands 1323.6.6
Applicability of requirements for NGEN-DC operation 1323.6.7
Applicability of QCL 1323.6.9 Applicability of requirements for
scheduling availability 1333.6.10 Applicability of requirements for
measurement restrictions 1333.6.11 Applicability of requirements for
Redcap UEs 1333.6.11.1 RRC connected state requirements in DRX
1333.6.11.2 Applicability for FR2 Redcap UE power classes 1333.6.11.3
Applicability of QCL 1333.6.12 Applicability of requirements for
Satellite Access 1343.6.13 Applicability of requirements for FR2
1343.6.14 Applicability of requirements for FR2 Power Class 6 1343.6.15
Applicability of requirements for per-FR gap 1344 SA: RRC\_IDLE state
mobility 1344.1 Cell Selection 1344.2 Cell Re-selection 1354.2.1
Introduction 1354.2.2 Requirements 1354.2.2.1 UE measurement capability
1354.2.2.2 Measurement and evaluation of serving cell 1354.2.2.3
Measurements of intra-frequency NR cells 1384.2.2.4 Measurements of
inter-frequency NR cells 1414.2.2.5 Measurements of inter-RAT E-UTRAN
cells 1464.2.2.6 Maximum interruption in paging reception 1494.2.2.7
General requirements 1504.2.2.8 Minimum requirement at transitions
1504.2.2.9 Measurements of intra-frequency NR cells for UE configured
with relaxed measurement criterion 1504.2.2.9.1 Introduction
1504.2.2.9.2 Measurements for UE fulfilling low mobility criterion
1514.2.2.9.3 Measurements for UE fulfilling not-at-cell edge criterion
1534.2.2.9.4 Measurements for UE fulfilling low mobility and not-at-cell
edge criteria 1554.2.2.10 Measurements of inter-frequency NR cells for
UE configured with relaxed measurement criterion 1564.2.2.10.1
Introduction 1564.2.2.10.2 Measurements for UE fulfilling low mobility
criterion 1564.2.2.10.3 Measurements for UE fulfilling not-at-cell edge
criterion 1594.2.2.10.4 Measurements for UE fulfilling low mobility and
not-at-cell edge criterion 1624.2.2.11 Measurements of inter-RAT E-UTRAN
cells for UE configured with relaxed measurement criterion 1624.2.2.11.1
Introduction 1624.2.2.11.2 Measurements for UE fulfilling low mobility
criterion 1634.2.2.11.3 Measurements for UE fulfilling with not-at-cell
edge criterion 1654.2.2.11.4 Measurements for UE fulfilling low mobility
and not-at-cell edge criterion 1664.2A Cell Re-selection when subject to
CCA 1674.2A.1 Introduction 1674.2A.2 Requirements 1674.2A.2.1 UE
measurement capability 1674.2A.2.2 Measurement and evaluation when
subject to CCA on the serving cell 1684.2A.2.3 Measurements of
intra-frequency NR cells when subject to CCA on the serving cell and
target cell 1684.2A.2.4 Measurements of inter-frequency NR cells when
subject to CCA on the target cell 1704.2A.2.5 Measurements of inter-RAT
E-UTRAN cells when subject to CCA on the serving cell 1724.2A.2.6
Maximum interruption in paging reception when subject to CCA on the
target cell 1724.2A.2.7 General requirements 1724.2B Cell Re-selection
for RedCap 1734.2B.1 Introduction 1734.2B.2 Requirements 1734.2B.2.1 UE
measurement capability for RedCap 1734.2B.2.1.1 UE measurement
capability for 1 Rx RedCap 1734.2B.2.1.2 UE measurement capability for 2
Rx RedCap 1734.2B.2.2 Measurement and evaluation of serving cell for
RedCap UE 1734.2B.2.3 Measurements of intra-frequency NR cells for
RedCap UE 1754.2B.2.4 Measurements of inter-frequency NR cells for
RedCap UE 1784.2B.2.5 Measurements of inter-RAT E-UTRAN cells for RedCap
UE 1814.2B.2.6 Maximum interruption in paging reception for RedCap
1834.2B.2.7 General requirements for RedCap 1834.2B.2.8 Minimum
requirement at transitions 1834.2B.2.9 Measurements of intra-frequency
NR cells for UE configured with relaxed measurement criterion for RedCap
1844.2B.2.9.1 Introduction 1844.2B.2.9.2 Measurements for UE fulfilling
stationary criterion 1854.2B.2.9.3 Measurements for a UE fulfilling
not-at-cell edge while stationary criterion 1884.2B.2.9.3A Measurements
for a UE fulfilling stationary and not-at-cell-edge criteria
1884.2B.2.9.4 Measurements for a UE fulfilling low mobility and
stationary criteria 1884.2B.2.9.5 Measurements for a UE fulfilling low
mobility and not-at-cell-edge while stationary criteria 1894.2B.2.9.6
Measurements for a UE fulfilling not-at-cell edge and not-at-cell edge
while stationary criteria 1894.2B.2.9.7 Measurements for a UE fulfilling
low mobility and not-at-cell edge criteria and not-at-cell-edge while
stationary criteria 1894.2B.2.9.8 Measurements for a UE fulfilling low
mobility, not-at-cell edge and stationary criterion 1894.2B.2.9.9
Measurements for UE fulfilling low mobility criterion 1904.2B.2.9.10
Measurements for UE fulfilling not-at-cell edge criterion 1934.2B.2.9.11
Measurements for UE fulfilling low mobility and not-at-cell edge
criteria 1954.2B.2.10 Measurements of inter-frequency NR cells for UE
configured with relaxed measurement criterion 1954.2B.2.10.1
Introduction 1954.2B.2.10.2 Measurements for UE fulfilling stationary
criterion 1964.2B.2.10.3 Measurements for a UE fulfilling not-at-cell
edge while stationary criterion 1984.2B.2.10.3A Measurements for a UE
fulfilling stationary and not-at-cell-edge-criterion 1994.2B.2.10.4
Measurements for a UE fulfilling low mobility and stationary criteria
1994.2B.2.10.5 Measurements for a UE fulfilling low mobility and
not-at-cell-edge while stationary criteria 2004.2B.2.10.6 Measurements
for a UE fulfilling not-at-cell edge and not-at-cell edge while
stationary criteria 2004.2B.2.10.7 Measurements for a UE fulfilling low
mobility and not-at-cell edge criteria and not-at-cell-edge while
stationary criteria 2004.2B.2.10.8 Measurements for a UE fulfilling low
mobility, not-at-cell edge and stationary criteria 2004.2B.2.10.9
Measurements for UE fulfilling low mobility criterion 2014.2B.2.10.10
Measurements for UE fulfilling not-at-cell edge criterion
2034.2B.2.10.11 Measurements for UE fulfilling low mobility and
not-at-cell edge criterion 2064.2B.2.11 Measurements of inter-RAT
E-UTRAN cells for UE configured with relaxed measurement criterion
2064.2B.2.11.1 Introduction 2064.2B.2.11.2 Measurements for UE
fulfilling stationary criterion 2074.2B.2.11.3 Measurements for a UE
not-at-cell edge while stationary criterion 2084.2B.2.11.3A Measurements
for a UE fulfilling stationary and not-at-cell-edge criterion
2084.2B.2.11.4 Measurements for a UE fulfilling low mobility and
stationary criteria 2094.2B.2.11.5 Measurements for a UE fulfilling low
mobility and stationary not-at-cell-edge while stationary criteria
2094.2B.2.11.6 Measurements for a UE fulfilling not-at-cell edge and
not-at-cell edge while stationary criteria 2094.2B.2.11.7 Measurements
for a UE fulfilling low mobility and not-at-cell edge criteria and
not-at-cell-edge while stationary criteria 2104.2B.2.11.8 Measurements
for a UE fulfilling low mobility, not-at-cell edge and stationary
criteria 2104.2B.2.11.9 Measurements for UE fulfilling low mobility
criterion 2104.2B.2.11.10 Measurements for UE fulfilling with
not-at-cell edge criterion 2124.2B.2.11.11 Measurements for UE
fulfilling low mobility and not-at-cell edge criterion 2134.2C Cell
Re-selection for NR UE for Satellite Access 2134.2C.1 Introduction
2134.2C.2 Requirements 2144.2C.2.1 UE measurement capability 2144.2C.2.2
Measurement and evaluation of serving cell 2144.2C.2.3 Measurements of
intra-frequency NR cells 2154.2C.2.4 Measurements of inter-frequency NR
cells 2174.2C.2.5 Maximum interruption in paging reception 2204.2C.2.6
Minimum requirement at transitions 2214.2C.2.7 Measurements of
intra-frequency NR cells for UE configured with relaxed measurement
criterion 2214.2C.2.8 Measurements of inter-frequency NR cells for UE
configured with relaxed measurement criterion 2214.2C.2.9 General
requirements 2214.3 Minimization of Drive Tests (MDT) 2214.3.1
Introduction 2214.3.2 Measurement Requirements 2224.3.3 Requirements for
Relative Time Stamp Accuracy 2224.3.4 Requirements for Relative Time
Stamp Accuracy for RRC Connection Establishment Failure Log Reporting
2224.3.5 Requirements for Relative Time Stamp Accuracy for Radio Link
Failure and Handover Failure Log Reporting 2234.3C Minimization of Drive
Tests (MDT) for Satellite Access 2234.3C.1 Introduction 2234.3C.2
Measurement Requirements 2234.3C.3 Requirements for Relative Time Stamp
Accuracy 2244.3C.4 Requirements for Relative Time Stamp Accuracy for RRC
Connection Establishment Failure Log Reporting 2244.3C.5 Requirements
for Relative Time Stamp Accuracy for Radio Link Failure and Handover
Failure Log Reporting 2244.4 Idle Mode CA/DC Measurements 2254.4.1
Introduction 2254.4.2 Measurement Requirements 2254.4.2.1 Detected cell
requirement during state transition and Idle mode 2254.4.2.2
Measurements of inter-frequency CA/DC candidate cells 2254.4.2.3
Measurements on serving cell 2274.4.2.4 Measurements of E-UTRAN
inter-RAT DC candidate cells 2275 SA: RRC\_INACTIVE state mobility
2285.1 Cell Re-selection 2285.1.1 Introduction 2285.1.2 Requirements
2285.1.2.1 UE measurement capability 2285.1.2.2 Measurement and
evaluation of serving cell 2285.1.2.3 Measurements of intra-frequency NR
cells 2295.1.2.4 Measurements of inter-frequency NR cells 2305.1.2.5
Measurements of inter-RAT E-UTRAN cells 2315.1.2.6 Maximum interruption
in paging reception 2325.1.2.7 General requirements 2325.1.2.8 Minimum
requirement at transitions 2325.1.2.9 Measurements of intra-frequency NR
cells for UE configured with relaxed measurement criterion 2325.1.2.10
Measurements of inter-frequency NR cells for UE configured with relaxed
measurement criterion 2335.1.2.11 Measurements of inter-RAT E-UTRAN
cells for UE configured with relaxed measurement criterion 2345.1A Cell
Re-selection with CCA 2355.1A.1 Introduction 2355.1A.2 Requirements
2355.1A.2.1 UE measurement capability 2355.1A.2.2 Measurement and
evaluation when CCA is used on the serving cell 2355.1A.2.3 Measurements
of intra-frequency NR cells when CCA is used on the serving cell and
target cell 2355.1A.2.4 Measurements of inter-frequency NR cells when
CCA is used on the target cell 2355.1A.2.5 Measurements of inter-RAT
E-UTRAN cells when CCA is used on the serving cell 2355.1A.2.6 Maximum
interruption in paging reception when CCA is used on the target cell
2355.1A.2.7 General requirements 2355.1B Cell Re-selection for RedCap
2355.1B.1 Introduction 2355.1B.2 Requirements 2365.1B.2.1 UE measurement
capability 2365.1B.2.2 Measurement and evaluation of serving cell
2365.1B.2.3 Measurements of intra-frequency NR cells 2375.1B.2.4
Measurements of inter-frequency NR cells 2385.1B.2.5 Measurements of
inter-RAT E-UTRAN cells 2385.1B.2.6 Maximum interruption in paging
reception 2395.1B.2.7 General requirements 2395.1B.2.8 Minimum
requirement at transitions 2395.1B.2.9 Measurements of intra-frequency
NR cells for UE configured with relaxed measurement criterion
2395.1B.2.10 Measurements of inter-frequency NR cells for UE configured
with relaxed measurement criterion 2405.1B.2.11 Measurements of
inter-RAT E-UTRAN cells for UE configured with relaxed measurement
criterion 2415.1C Cell Re-selection 2425.1C.1 Introduction 2425.1C.2
Requirements 2425.1C.2.1 UE measurement capability 2425.1C.2.2
Measurement and evaluation of serving cell 2425.1C.2.3 Measurements of
intra-frequency NR cells 2425.1C.2.4 Measurements of inter-frequency NR
cells 2435.1C.2.5 Maximum interruption in paging reception 2435.1C.2.6
General requirements 2435.2 Void 2435.2B Configured Grant based Small
Data Transmissions (CG-SDT) for RedCap 2435.2B.1 Introduction 2435.2B.2
Requirements on UE synchronization for small data transmissions for
RedCap 2435.2B.2.1 Void 2435.2B.3 TA validation requirements for RedCap
2435.2B.3.1 Void 2445.2B.3.2 Void 2445.2B.4 Scheduling restriction
2445.2B.5 Applicability conditions for CG-SDT for RedCap 2455.3
Minimization of Drive Tests (MDT) 2455.3.1 Introduction 2455.3.2
Measurement Requirements 2455.3.3 Requirements for Relative Time Stamp
Accuracy 2455.3.4 Requirements for Relative Time Stamp Accuracy for RRC
Connection Establishment Failure Log Reporting 2455.3.5 Requirements for
Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure
Log Reporting 2455.3.6 Requirements for Relative Time Stamp Accuracy for
RRC Resume Failure Log Reporting 2465.3C Minimization of Drive Tests
(MDT) for Satellite Access 2465.3C.1 Introduction 2465.3C.2 Measurement
Requirements 2465.3C.3 Requirements for Relative Time Stamp Accuracy
2465.3C.4 Requirements for Relative Time Stamp Accuracy for RRC
Connection Establishment Failure Log Reporting 2465.3C.5 Requirements
for Relative Time Stamp Accuracy for Radio Link Failure and Handover
Failure Log Reporting 2465.3C.6 Requirements for Relative Time Stamp
Accuracy for RRC Resume Failure Log Reporting 2475.4 Inactive Mode CA/DC
Measurements 2475.4.1 Introduction 2475.4.2 Measurement Requirements
2475.4.2.1 Detected cell requirement during state transition and
inactive mode 2475.4.2.2 Measurements of inter-frequency CA/DC candidate
cells 2475.4.2.3 Measurements on serving cell 2475.4.2.4 Measurements on
E-UTRAN inter-RAT DC candidate cells 2475.5 Configured Grant based Small
Data Transmissions (CG-SDT) 2475.5.1 Introduction 2475.5.2 Requirements
on UE synchronization for small data transmissions 2475.5.3 TA
validation requirements 2485.5.4 Scheduling restriction 2495.5.4.1
Scheduling availability of UE performing measurements in TDD bands on
FR1 2495.5.4.2 Scheduling availability of UE performing measurements
with a different subcarrier spacing than PDSCH/PDCCH on FR1 2495.5.4.3
Scheduling availability of UE performing measurements on FR2 2495.5.5
Applicability conditions for SDT 2505.6 NR measurements for positioning
2505.6.1 Introduction 2505.6.2 RSTD measurements 2515.6.2.1 Introduction
2515.6.2.2 Requirements Applicability 2515.6.2.3 Measurement Capability
2515.6.2.5 Measurements Period Requirements 2525.6.3 PRS-RSRP
measurements 2545.6.3.1 Introduction 2545.6.3.2 Requirements
applicability 2545.6.3.3 Measurement Capability 2555.6.3.4 Measurement
Reporting Requirements 2555.6.3.5 Measurement Period Requirements
2555.6.4 UE Rx-Tx time difference measurements 2575.6.4.1 Introduction
2575.6.4.2 Requirements Applicability 2575.6.4.3 Measurement Capability
2585.6.4.4 Measurement Reporting Requirements 2585.6.4.5 Measurement
Period Requirements 2585.6.5 PRS-RSRPP measurements 2615.6.5.1
Introduction 2615.6.5.2 Requirements Applicability 2615.6.5.3
Measurement Capability 2615.6.5.4 Measurement Reporting Requirements
2615.6.5.5 Measurement Period Requirements 2625.7 Random access based
Small Data Transmissions (RA-SDT) 2635.7.1 Introduction 2635.7.2
Requirements for small data transmissions based on 2-step RA 2635.7.3
Requirements for small data transmissions based on 4-step RA 2635.7.4
Applicability conditions for SDT 2635.7B Random access based Small Data
Transmissions (RA-SDT) for RedCap 2635.7B.1 Introduction 2635.7B.2
Requirements for small data transmissions based on 2-step RA 2635.7B.3
Requirements for small data transmissions based on 4-step RA 2645.7B.4
Applicability conditions for RA-SDT for RedCap 2646 RRC\_CONNECTED state
mobility 2646.1 Handover 2646.1.1 NR Handover 2646.1.1.1 Introduction
2646.1.1.2 NR FR1 - NR FR1 Handover 2646.1.1.2.1 Handover delay
2646.1.1.2.2 Interruption time 2646.1.1.3 NR FR2- NR FR1 Handover
2656.1.1.3.1 Handover delay 2656.1.1.3.2 Interruption time 2656.1.1.4 NR
FR2- NR FR2 Handover 2666.1.1.4.1 Handover delay 2666.1.1.4.2
Interruption time 2666.1.1.5 NR FR1- NR FR2 Handover 2676.1.1.5.1
Handover delay 2676.1.1.5.2 Interruption time 2676.1.2 NR Handover to
other RATs 2686.1.2.1 NR -- E-UTRAN Handover 2686.1.2.1.1 Introduction
2686.1.2.1.2 Handover delay 2686.1.2.1.3 Interruption time 2686.1.2.2 NR
-- UTRAN Handover 2696.1.2.2.1 Introduction 2696.1.2.2.2 Handover delay
2696.1.2.2.3 Interruption time 2696.1.3 NR DAPS Handover 2706.1.3.1
Introduction 2706.1.3.2 NR FR1 - NR FR1 DAPS Handover 2706.1.3.2.1 DAPS
handover delay 2716.1.3.2.2 Interruption time 2716.1.3.3 NR FR2- NR FR1
DAPS Handover 2736.1.3.3.1 DAPS handover delay 2736.1.3.3.2 Interruption
time 2746.1.3.4 NR FR1- NR FR2 DAPS Handover 2746.1.3.4.1 DAPS handover
delay 2746.1.3.4.2 Interruption time 2756.1.4 NR Conditional Handover
2756.1.4.1 Introduction 2756.1.4.2 NR FR1 -- NR FR1 conditional handover
2756.1.4.3 NR FR2 -- NR FR1 conditional handover 2776.1.4.4 NR FR2 -- NR
FR2 conditional handover 2776.1.4.4.1 Handover delay 2776.1.4.4.2
Measurement time 2776.1.4.4.3 Preparation time 2786.1.4.4.4 Interruption
time 2786.1.4.5 NR FR1 -- NR FR2 conditional handover 2786.1.5 NR
Handover with PSCell 2786.1.5.1 Introduction 2786.1.5.2 Handover with
PSCell from NR SA to EN-DC 2796.1.5.2.1 Interruption time for inter-RAT
HO from NR to E-UTRAN 2796.1.5.2.2 PSCell addition in HO with PSCell for
NR SA to EN-DC 2796.1.5.3 HO with PSCell from NE-DC to NE-DC
2806.1.5.3.1 Handover delay 2806.1.5.3.2 HO with PSCell - PCell
Interruption time 2806.1.5.3.3 PSCell addition/change in NE-DC to NE-DC
HO with PSCell 2806.1.5.4 HO with PSCell from NR-DC to NR-DC 2816.1.5.5
Handover with PSCell from NR SA to EN-DC with PSCell using CCA
2826.1.5.5.1 Introduction 2826.1.5.5.2 NR SA to EN-DC HO with PSCell- NR
to E-UTRA HO Interruption time 2826.1.5.5.3 NR SA to EN-DC HO with
PSCell - NR PSCell Addition Delay requirements 2836.1A Void 2846.1A.1
Void 2846.1A.1.1 Void 2846.1A.1.2 Void 2846.1A.1.2.1 Void 2846.1A.1.2.2
Void 2846.1B Handover to target cell using CCA 2846.1B.1 NR Handover
2846.1B.1.1 Introduction 2846.1B.1.2 NR FR1 - NR FR1 Handover
2846.1B.1.2.1 Handover delay 2846.1B.1.2.2 Interruption time 2846.1B.1.3
NR FR2-2 NR FR2-2 Handover 2856.1B.1.3.1 Handover delay 2856.1B.1.3.2
Interruption time 2856.1B.1.4 NR FR1- NR FR2-2 Handover 2866.1B.1.4.1
Handover delay 2866.1B.1.4.2 Interruption time 2876.1C Handover for SAN
2886.1C.1 NR SAN Handover 2886.1C.1.1 Introduction 2886.1C.1.2 NR SAN
FR1 -- NR SAN FR1 Handover 2886.1C.1.2.1 Handover delay 2886.1C.1.2.2
Interruption time 2886.1C.2 NR SAN Conditional Handover 2896.1C.2.1
Introduction 2896.1C.2.2 NR SAN FR1 -- NR SAN FR1 conditional handover
2896.1C.2.2.1 Handover delay 2896.1C.2.2.2 Measurement time
2896.1C.2.2.3 Preparation time 2916.1C.2.2.4 Interruption time 2916.1D
Handover for RedCap 2916.1D.1 NR Handover 2916.1D.1.1 Introduction
2916.1D.1.2 NR FR1 - NR FR1 Handover 2926.1D.1.2.1 Handover delay
2926.1D.1.2.2 Interruption time 2926.1D.1.3 NR FR2- NR FR2 Handover
2936.1D.1.3.1 Handover delay 2936.1D.1.3.2 Interruption time 2936.1D.2
NR Handover to other RATs 2956.1D.2.1 NR -- E-UTRAN Handover 2956.2 RRC
Connection Mobility Control 2956.2.1 SA: RRC Re-establishment 2956.2.1.1
Introduction 2956.2.1.2 Requirements 2956.2.1.2.1 UE Re-establishment
delay requirement 2956.2.1A RRC Re-establishment with CCA 2976.2.1A.1
Introduction 2976.2.1A.2 Requirements 2976.2.1A.2.1 UE Re-establishment
with CCA delay requirement 2986.2.1B SA: RRC Re-establishment for RedCap
2996.2.1B.1 Introduction 2996.2.1B.2 Requirements 3006.2.2 Random access
3006.2.2.1 Introduction 3006.2.2.2 Requirements for 4-step RA type
3006.2.2.2.1 Contention based random access 3016.2.2.2.1.1 Correct
behaviour when transmitting Random Access Preamble 3016.2.2.2.1.2
Correct behaviour when receiving Random Access Response 3016.2.2.2.1.3
Correct behaviour when not receiving Random Access Response
3016.2.2.2.1.4 Correct behaviour when receiving an UL grant for msg3
retransmission 3016.2.2.2.1.5 SA: Correct behaviour when receiving a
message over Temporary C-RNTI 3016.2.2.2.1.6 Correct behaviour when
contention Resolution timer expires 3016.2.2.2.2 Non-Contention based
random access 3016.2.2.2.2.1 Correct behaviour when transmitting Random
Access Preamble 3016.2.2.2.2.2 Correct behaviour when receiving Random
Access Response 3026.2.2.2.2.3 Correct behaviour when not receiving
Random Access Response 3026.2.2.2.3 UE behaviour when configured with
supplementary UL 3026.2.2.3 Requirements for 2-step RA type 3026.2.2.3.1
Contention based random access 3036.2.2.3.1.1 Correct behaviour when
transmitting MsgA 3036.2.2.3.1.2 Correct behaviour when receiving MsgB
3036.2.2.3.1.3 Correct behaviour when not receiving MsgB 3036.2.2.3.2
Non-Contention based random access 3046.2.2.3.2.1 Correct behaviour when
transmitting MsgA 3046.2.2.3.2.2 Correct behaviour when receiving MsgB
3046.2.2.3.2.3 Correct behaviour when not receiving MsgB 3046.2.2.3.3 UE
behaviour when configured with supplementary UL 3046.2.2A Random access
when CCA is used on target frequency 3046.2.2A.1 Introduction
3046.2.2A.2 Requirements for 4-step RA type 3056.2.2A.2.1 Contention
based random access 3056.2.2A.2.1.1 Correct behaviour when transmitting
Random Access Preamble 3056.2.2A.2.1.2 Correct behaviour when receiving
Random Access Response 3056.2.2A.2.1.3 Correct behaviour when not
receiving Random Access Response 3056.2.2A.2.1.4 Correct behaviour when
receiving an UL grant for msg3 retransmission 3066.2.2A.2.1.6 Correct
behaviour when contention Resolution timer expires 3066.2.2A.2.2
Non-Contention based random access 3066.2.2A.2.2.1 Correct behaviour
when transmitting Random Access Preamble 3066.2.2A.2.2.2 Correct
behaviour when receiving Random Access Response 3066.2.2A.2.2.3 Correct
behaviour when not receiving Random Access Response 3076.2.2A.3
Requirements for 2-step RA type 3076.2.2A.3.1 Contention based random
access 3076.2.2A.3.1.1 Correct behaviour when transmitting MsgA
3076.2.2A.3.1.2 Correct behaviour when receiving MsgB 3086.2.2A.3.1.3
Correct behaviour when not receiving MsgB 3086.2.2A.3.2 Non-Contention
based random access 3086.2.2A.3.2.1 Correct behaviour when transmitting
MsgA 3086.2.2A.3.2.2 Correct behaviour when receiving MsgB
3096.2.2A.3.2.3 Correct behaviour when not receiving MsgB 3096.2.2B
Random access for RedCap 3096.2.2B.1 Introduction 3096.2.2B.2
Requirements 3106.2.3 SA: RRC Connection Release with Redirection
3106.2.3.1 Introduction 3106.2.3.2 Requirements 3106.2.3.2.1 RRC
connection release with redirection to NR 3106.2.3.2.2 RRC connection
release with redirection to E-UTRAN 3116.2.3.2.3 RRC connection release
with redirection to NR carrier subject to CCA 3126.2.3A SA: RRC
Connection Release with Redirection for RedCap 3136.2.3A.1 Introduction
3136.2.3A.2 Requirements 3136.2.3A.2.1 RRC connection release with
redirection to NR 3136.2.3A.2.2 RRC connection release with redirection
to E-UTRAN 3136.2C RRC Connection Mobility Control for Satellite Access
3136.2C.1 SA: RRC Re-establishment for Satellite Access 3136.2C.1.1
Introduction 3136.2C.1.2 Requirements 3146.2C.1.2.1 UE Re-establishment
delay requirement 3146.2C.2 Random access for satellite access
3156.2C.2.1 Introduction 3156.2C.2.2 Requirements for 4-step RA type
3156.2C.2.2.1 Contention based random access 3166.2C.2.2.1.1 Correct
behaviour when transmitting Random Access Preamble 3166.2C.2.2.1.2
Correct behaviour when receiving Random Access Response 3166.2C.2.2.1.3
Correct behaviour when not receiving Random Access Response
3166.2C.2.2.1.4 Correct behaviour when receiving an UL grant for msg3
retransmission 3166.2C.2.2.1.5 SA: Correct behaviour when receiving a
message over Temporary C-RNTI 3166.2C.2.2.1.6 Correct behaviour when
contention Resolution timer expires 3166.2C.2.2.2 Non-Contention based
random access 3166.2C.2.2.2.1 Correct behaviour when transmitting Random
Access Preamble 3166.2C.2.2.2.2 Correct behaviour when receiving Random
Access Response 3176.2C.2.2.2.3 Correct behaviour when not receiving
Random Access Response 3176.2C.2.3 Requirements for 2-step RA type
3176.2C.2.3.1 Contention based random access 3186.2C.2.3.1.1 Correct
behaviour when transmitting MsgA 3186.2C.2.3.1.2 Correct behaviour when
receiving MsgB 3186.2C.2.3.1.3 Correct behaviour when not receiving MsgB
3186.2C.2.3.2 Non-Contention based random access 3186.2C.2.3.2.1 Correct
behaviour when transmitting MsgA 3186.2C.2.3.2.2 Correct behaviour when
receiving MsgB 3196.2C.2.3.2.3 Correct behaviour when not receiving MsgB
3196.2C.3 SA: RRC Connection Release with Redirection for Satellite
Access 3196.2C.3.1 Introduction 3196.2C.3.2 Requirements 3196.2C.3.2.1
RRC connection release with redirection to NR 3197 Timing 3207.1 UE
transmit timing 3207.1.1 Introduction 3207.1.2 Requirements 3207.1.2.1
Gradual timing adjustment 3227.1.2.2 Void 3237.1.2.3 One shot large UL
timing adjustment for FR2 Power Class 6 UE 3237.1A UE transmit timing
for RedCap 3237.1A.1 Introduction 3237.1A.2 Requirements 3247.1A.2.1
Gradual timing adjustment 3257.1C UE transmit timing for Satellite
Access 3257.1C.1 Introduction 3257.1C.2 Requirements 3257.1C.2.1 Gradual
timing adjustment 3267.2 UE timer accuracy 3277.2.1 Introduction
3277.2.2 Requirements 3277.2A UE timer accuracy for RedCap 3277.2A.1
Introduction 3277.2A.2 Requirements 3277.2C UE timer accuracy for
satellite access 3277.2C.1 Introduction 3277.2C.2 Requirements 3287.3
Timing advance 3287.3.1 Introduction 3287.3.2 Requirements 3287.3.2.1
Timing Advance adjustment delay 3287.3.2.2 Timing Advance adjustment
accuracy 3287.3A Timing Advance for RedCap 3287.3A.1 Introduction
3287.3A.2 Requirements 3297.3A.2.1 Timing Advance adjustment delay
3297.3A.2.2 Timing Advance adjustment accuracy 3297.3C Timing advance
for satellite access 3297.3C.1 Introduction 3297.3C.2 Requirements
3297.3C.2.1 Timing Advance adjustment delay 3297.3C.2.2 Timing Advance
adjustment accuracy 3297.4 Cell phase synchronization accuracy 3307.4.1
Definition 3307.4.2 Minimum requirements 3307.5 Maximum Transmission
Timing Difference 3307.5.1 Introduction 3307.5.2 Minimum Requirements
for inter-band EN-DC 3307.5.2.1 Minimum Requirements for inter-band
synchronous EN-DC 3317.5.3 Minimum Requirements for intra-band EN-DC
3317.5.4 Minimum Requirements for NR Carrier Aggregation 3327.5.5
Minimum Requirements for inter-band NE-DC 3327.5.5.1 Minimum
Requirements for inter-band synchronous NE-DC 3337.5.6 Minimum
Requirements for inter-band NR DC 3337.6 Maximum Receive Timing
Difference 3347.6.1 Introduction 3347.6.2 Minimum Requirements for
inter-band EN-DC 3347.6.2.1 Minimum Requirements for inter-band
synchronous EN-DC 3357.6.3 Minimum Requirements for intra-band EN-DC
3357.6.4 Minimum Requirements for NR Carrier Aggregation 3367.6.5
Minimum Requirements for inter-band NE-DC 3377.6.5.1 Minimum
Requirements for inter-band synchronous NE-DC 3377.6.6 Minimum
Requirements for inter-band NR DC 3377.7 *deriveSSB-IndexFromCell*
tolerance 3387.7.1 Minimum requirements 3387.7A deriveSSB-IndexFromCell
tolerance for RedCap 3397.7A.1 Minimum requirements 3397.8 Void 3397.9
*deriveSSB-IndexFromCellInter-r17* tolerance 3397.9.1 Minimum
requirements 3398 Signalling characteristics 3408.1 Radio Link
Monitoring 3408.1.1 Introduction 3408.1.1.1 Introduction of Requirement
on Radio Link Monitoring for UE Configured with Relaxed Measurement
Criteria 3418.1.2 Requirements for SSB based radio link monitoring
3418.1.2.1 Introduction 3428.1.2.2 Minimum requirement 3428.1.2.3
Measurement restrictions for SSB based RLM 3468.1.2.4 Minimum
requirement of SSB based radio link monitoring for UE fulfilling relaxed
measurement criteria 3468.1.3 Requirements for CSI-RS based radio link
monitoring 3478.1.3.1 Introduction 3478.1.3.2 Minimum requirement
3488.1.3.3 Measurement restrictions for CSI-RS based RLM 3518.1.3.4
Minimum requirement of CSI-RS based radio link monitoring for UE
fulfilling relaxed measurement criteria 3528.1.4 Minimum requirement at
transitions 3538.1.5 Minimum requirement for UE turning off the
transmitter 3538.1.6 Minimum requirement for L1 indication 3538.1.7
Scheduling availability of UE during radio link monitoring 3548.1.7.1
Scheduling availability of UE performing radio link monitoring with a
same subcarrier spacing as PDSCH/PDCCH on FR1 3548.1.7.2 Scheduling
availability of UE performing radio link monitoring with a different
subcarrier spacing than PDSCH/PDCCH on FR1 3548.1.7.3 Scheduling
availability of UE performing radio link monitoring on FR2 3548.1.7.4
Scheduling availability of UE performing radio link monitoring on FR1 or
FR2 in case of FR1-FR2 inter-band CA and NR-DC 3558.1A Radio Link
Monitoring with CCA on Target Frequency 3558.1A.1 Introduction 3558.1A.2
Requirements for SSB Based Radio Link Monitoring 3568.1A.2.1
Introduction 3568.1A.2.2 Minimum Requirement 3578.1A.3 Minimum
requirement at transitions 3608.1A.4 Minimum requirement for UE turning
off the transmitter 3618.1A.5 Minimum requirement for L1 indication
3618.1A.6 Scheduling availability of UE during radio link monitoring
3618.1A.6.3 Scheduling availability of UE performing radio link
monitoring on FR2-2 3618.1A.6.4 Scheduling availability of UE performing
radio link monitoring on FR1 or FR2-2 in case of FR1-FR2-2 inter-band CA
and NR-DC 3628.1B Radio Link Monitoring for RedCap 3628.1B.1
Introduction 3628.1B.2 Requirements for SSB based radio link monitoring
3638.1B.2.1 Introduction 3638.1B.2.2 Minimum requirement 3648.1B.2.3
Measurement restrictions for SSB based RLM 3668.1B.3 Requirements for
CSI-RS based radio link monitoring 3678.1B.3.1 Introduction 3678.1B.3.2
Minimum requirement 3678.1B.3.3 Measurement restrictions for CSI-RS
based RLM 3708.1B.4 Minimum requirement at transitions 3718.1B.5 Minimum
requirement for UE turning off the transmitter 3718.1B.6 Minimum
requirement for L1 indication 3718.1B.7 Scheduling availability of UE
during radio link monitoring 3718.1B.7.1 Scheduling availability of UE
performing radio link monitoring with a same subcarrier spacing as
PDSCH/PDCCH on FR1 3728.1B.7.2 Scheduling availability of UE performing
radio link monitoring with a different subcarrier spacing than
PDSCH/PDCCH on FR1 3728.1B.7.3 Scheduling availability of UE performing
radio link monitoring on FR2 3728.1C Radio Link Monitoring for Satellite
Access 3728.1C.1 Introduction 3728.1C.2 Requirements for SSB based radio
link monitoring 3738.1C.2.1 Introduction 3738.1C.2.2 Minimum requirement
3748.1C.2.3 Measurement restrictions for SSB based RLM 3758.1C.3
Requirements for CSI-RS based radio link monitoring 3758.1C.3.1
Introduction 3758.1C.3.2 Minimum requirement 3768.1C.3.3 Measurement
restrictions for CSI-RS based RLM 3778.1C.4 Minimum requirement at
transitions 3788.1C.5 Minimum requirement for UE turning off the
transmitter 3788.1C.6 Minimum requirement for L1 indication 3788.1C.7
Scheduling availability of UE during radio link monitoring 3788.1C.7.1
Scheduling availability of UE performing radio link monitoring with a
same subcarrier spacing as PDSCH/PDCCH on FR1 3798.1C.7.2 Scheduling
availability of UE performing radio link monitoring with a different
subcarrier spacing than PDSCH/PDCCH on FR1 3798.2 Interruption 3798.2.1
EN-DC Interruption 3798.2.1.1 Introduction 3798.2.1.2 Requirements
3808.2.1.2.1 Interruptions at transitions between active and non-active
during DRX 3808.2.1.2.2 Interruptions at transitions from non-DRX to DRX
3808.2.1.2.3 Interruptions at SCell addition/release 3808.2.1.2.4
Interruptions at SCell activation/deactivation 3818.2.1.2.5
Interruptions during measurements on SCC 3838.2.1.2.5.1 Interruptions
during measurements on deactivated NR SCC 3838.2.1.2.5.2 Interruptions
during measurements on deactivated E-UTRAN SCC 3838.2.1.2.5.3
Interruptions during CQI measurements on dormant E-UTRAN SCell
3838.2.1.2.5.4 Interruptions during RRM measurements on dormant E-UTRAN
SCC 3848.2.1.2.6 Interruptions at UL carrier RRC reconfiguration
3848.2.1.2.7 Interruptions due to Active BWP switching Requirement
3858.2.1.2.8 Interruptions at direct SCell activation and hibernation
3868.2.1.2.8.1 Interruptions during direct SCell activation and
hibernation of E-UTRA SCell 3868.2.1.2.8.2 Interruptions during direct
SCell activation 3868.2.1.2.9 Interruptions at SCell hibernation
3868.2.1.2.10 Interruptions at SCell activation/deactivation with
multiple downlink SCells 3878.2.1.2.11 Interruptions due to UE-specific
CBW change 3878.2.1.2.12 Interruptions at NR SRS carrier based switching
3878.2.1.2.13 Interruptions at E-UTRA SRS carrier based switching
3898.2.1.2.14 DL Interruptions at switching between two uplink carriers
3908.2.1.2.15 Interruptions due to SCell dormancy 3908.2.1.2.15.1
Interruptions due to SCell dormancy switch 3908.2.1.2.15.2 Interruptions
due to CQI measurements during SCell dormancy 3908.2.1.2.15.3
Interruptions due to RRM measurements during SCell dormancy
3918.2.1.2.16 Interruptions when identifying CGI of an NR cell with
autonomous gaps 3918.2.1.2.17 Interruptions when identifying CGI of an
E-UTRA cell with autonomous gaps 3918.2.1.2.18 Interruptions at NR SRS
antenna port switching 3928.2.1.2.19 Interruptions at fast SCell
activation 3938.2.1.2.20 Interruptions due to PUCCH SCell
activation/deactivation 3948.2.2 SA: Interruptions with Standalone NR
Carrier Aggregation 3948.2.2.1 Introduction 3948.2.2.2 Requirements
3958.2.2.2.1 Interruptions at SCell addition/release 3958.2.2.2.2
Interruptions at SCell activation/deactivation 3968.2.2.2.3
Interruptions during measurements on deactivated SCC 3978.2.2.2.4
Interruptions at UL carrier RRC reconfiguration 3988.2.2.2.5
Interruptions due to Active BWP switching Requirement 3988.2.2.2.6
Interruptions at inter-frequency SFTD measurement 3998.2.2.2.7
Interruptions at SCell activation/deactivation with multiple downlink
SCells 4018.2.2.2.8 Interruptions due to UE-specific CBW change
4018.2.2.2.9 Interruptions at NR SRS carrier based switching
4018.2.2.2.10 DL Interruptions at UE switching between two uplink
carriers 4038.2.2.2.10A DL Interruptions at UE switching between two
uplink carriers with two transmit antenna connectors 4038.2.2.2.10B DL
Interruptions at UE switching between one uplink band with one transmit
antenna connector and one uplink band with two transmit antenna
connectors 4048.2.2.2.10C DL Interruptions at UE switching between two
uplink bands with two transmit antenna connectors 4048.2.2.2.11
Interruptions at direct SCell activation 4048.2.2.2.12 Interruptions due
to SCell dormancy 4058.2.2.2.12.1 Interruptions due to SCell dormancy
switch 4058.2.2.2.12.2 Interruptions due to CQI measurements during
SCell dormancy 4058.2.2.2.12.3 Interruptions due to RRM measurements
during SCell dormancy 4058.2.2.2.13 Interruptions at transitions between
active and non-active during DRX 4058.2.2.2.14 Interruptions when
identifying CGI of an NR cell with autonomous gaps 4058.2.2.2.15
Interruptions when identifying CGI of an E-UTRA cell with autonomous
gaps 4068.2.2.2.16 Interruptions at NR SRS antenna port switching
4068.2.2.2.17 Interruptions at fast SCell activation 4078.2.2.2.18
Interruptions due to PUCCH SCell activation/deactivation 4088.2.3 NE-DC
Interruptions 4088.2.3.1 Introduction 4088.2.3.2 Requirements
4098.2.3.2.1 Interruptions at transitions between active and non-active
during DRX 4098.2.3.2.2 Interruptions at transitions from non-DRX to DRX
4098.2.3.2.3 Interruptions at PSCell/SCell addition/release 4098.2.3.2.4
Interruptions at SCell activation/deactivation 4108.2.3.2.5
Interruptions during measurements on SCC 4128.2.3.2.5.1 Interruptions
during measurements on deactivated NR SCC 4128.2.3.2.5.2 Interruptions
during measurements on deactivated E-UTRAN SCC 4128.2.3.2.5.3
Interruptions during CQI measurements on dormant E-UTRAN SCC
4128.2.3.2.5.4 Interruptions during RRM measurements on dormant E-UTRAN
SCC 4128.2.3.2.6 Interruptions at UL carrier RRC reconfiguration
4138.2.3.2.7 Interruptions due to Active BWP switching Requirement
4138.2.3.2.8 Interruptions at direct SCell activation and hibernation
4138.2.3.2.9 Interruptions at SCell hibernation 4148.2.3.2.10
Interruptions at SCell activation/deactivation with multiple downlink
SCells 4148.2.3.2.11 Interruptions at NR SRS carrier based switching
4148.2.3.2.12 Interruptions at E-UTRA SRS carrier based switching
4168.2.3.2.13 Interruptions due to SCell dormancy 4168.2.3.2.14
Interruptions when identifying CGI of an NR cell with autonomous gaps
4178.2.3.2.15 Interruptions when identifying CGI of an E-UTRA cell with
autonomous gaps 4178.2.3.2.17 Interruptions at fast SCell activation
4198.2.3.2.18 Interruptions due to UE-specific CBW change 4208.2.3.2.19
Interruptions due to PUCCH SCell activation/deactivation 4208.2.4 NR-DC:
Interruptions 4208.2.4.1 Introduction 4208.2.4.2 Requirements
4218.2.4.2.1 Interruptions at PSCell/SCell addition/release 4218.2.4.2.2
Interruptions at SCell activation/deactivation 4228.2.4.2.3
Interruptions during measurements on SCC 4238.2.4.2.4 Interruptions at
UL carrier RRC reconfiguration 4238.2.4.2.5 Interruptions due to Active
BWP switching Requirement 4248.2.4.2.6 Interruptions at transitions
between active and non-active during DRX 4248.2.4.2.7 Interruptions at
transitions from non-DRX to DRX 4248.2.4.2.8 Interruptions at SCell
activation/deactivation with multiple downlink SCells 4258.2.4.2.9
Interruptions at NR SRS carrier based switching 4258.2.4.2.10
Interruptions at direct SCell activation 4268.2.4.2.11 Interruptions
when identifying CGI of an NR cell with autonomous gaps 4278.2.4.2.12
Interruptions when identifying CGI of an E-UTRA cell with autonomous
gaps 4278.2.4.2.13 Interruptions due to SCell dormancy 4288.2.4.2.14
Interruptions at NR SRS antenna port switching 4288.2.4.2.15
Interruptions at fast SCell activation 4298.2.4.2.16 Interruptions at
SCG activation/deactivation 4308.2.4.2.17 Interruptions due to RRM
measurements on deactivated SCG 4308.2.4.2.18 Interruptions during
RLM/BFD measurements on deactivated PSCell 4318.2.4.2.19 Interruptions
due to UE-specific CBW change 4318.2.4.2A Void 4318.2.4.2A.1 Void
4318.2.4.2A.2 Void 4318.2.4.2A.3 Void 4318.3 SCell Activation and
Deactivation Delay 4318.3.1 Introduction 4318.3.2 SCell Activation Delay
Requirement for Deactivated SCell 4318.3.3 SCell Deactivation Delay
Requirement for Activated SCell 4368.3.4 Direct SCell Activation at
SCell addition 4368.3.5 Direct SCell Activation at Handover 4388.3.7
SCell Activation Delay Requirement for Deactivated SCell with Multiple
Downlink SCells 4408.3.8 SCell Deactivation Delay Requirement for
Activated SCell with Multiple Downlink SCells 4448.3.9 Direct SCell
Activation of Multiple Downlink SCells at SCell addition 4448.3.10
Direct SCell Activation of Multiple Downlink SCells at Handover
4458.3.12 SCell Activation Delay Requirement for Deactivated PUCCH SCell
4478.3.13 SCell activation delay Requirement for Deactivated PUCCH SCell
with Multiple SCells 4498.3.14 SCell Deactivation Delay Requirement for
Activated PUCCH SCell 4518.3.15 SCell Deactivation Delay Requirement for
Activated PUCCH SCell with Multiple Downlink SCells 4528.3.16 Fast SCell
Activation Delay Requirement for Deactivated SCell 4528.3A SCell
Activation and Deactivation Delay in Carriers with CCA 4558.3A.1
Introduction 4558.3A.2 SCell Activation Delay Requirement for
Deactivated SCell 4558.3A.3 SCell Deactivation Delay Requirement for
Activated SCell 4608.4 UE UL carrier RRC reconfiguration delay 4608.4.1
Introduction 4608.4.2 UE UL carrier configuration delay requirement
4608.4.3 UE UL carrier deconfiguration delay requirement 4608.5 Link
Recovery Procedures 4618.5.1 Introduction 4618.5.1.1 Introduction of
Requirement on Link Recovery Procedures for UE configured with relaxed
measurement criteria 4628.5.2 Requirements for SSB based beam failure
detection 4638.5.2.1 Introduction 4638.5.2.2 Minimum requirement
4638.5.2.3 Measurement restriction for SSB based beam failure detection
4668.5.2.4 Minimum requirement of SSB based beam failure detection for
UE fulfilling relaxed measurement criteria 4678.5.3 Requirements for
CSI-RS based beam failure detection 4688.5.3.1 Introduction 4688.5.3.2
Minimum requirement 4688.5.3.3 Measurement restrictions for CSI-RS beam
failure detection 4718.5.3.4 Minimum requirement of CSI-RS based beam
failure detection for UE fulfilling relaxed measurement criteria
4728.5.4 Minimum requirement for L1 indication 4738.5.5 Requirements for
SSB based candidate beam detection 4748.5.5.1 Introduction 4748.5.5.2
Minimum requirement 4748.5.5.3 Measurement restriction for SSB based
candidate beam detection 4778.5.6 Requirements for CSI-RS based
candidate beam detection 4778.5.6.1 Introduction 4778.5.6.2 Minimum
requirement 4778.5.6.3 Measurement restriction for CSI-RS based
candidate beam detection 4808.5.7 Scheduling availability of UE during
beam failure detection 4818.5.7.1 Scheduling availability of UE
performing beam failure detection with a same subcarrier spacing as
PDSCH/PDCCH on FR1 4818.5.7.2 Scheduling availability of UE performing
beam failure detection with a different subcarrier spacing than
PDSCH/PDCCH on FR1 4818.5.7.3 Scheduling availability of UE performing
beam failure detection on FR2 4828.5.7.4 Scheduling availability of UE
performing beam failure detection on FR1 or FR2 in case of FR1-FR2
inter-band CA and NR DC 4828.5.8 Scheduling availability of UE during
candidate beam detection 4828.5.8.1 Scheduling availability of UE
performing L1-RSRP measurement with a same subcarrier spacing as
PDSCH/PDCCH on FR1 4838.5.8.2 Scheduling availability of UE performing
L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH
on FR1 4838.5.8.3 Scheduling availability of UE performing L1-RSRP
measurement on FR2 4838.5.8.4 Scheduling availability of UE performing
L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA and
NR-DC 4848.5.9 Requirements for Beam Failure Recovery in SCell
4848.5.9.1 Introduction 4848.5.9.2 Requirement 4848.5.10 Minimum
requirement at transitions for beam failure detection 4848.5A Link
Recovery Procedures when CCA is used on target frequency 4858.5A.1
Introduction 4858.5A.2 Requirements for SSB based beam failure detection
4858.5A.2.1 Introduction 4858.5A.2.2 Minimum requirement 4868.5A.2.3
Measurement restriction for SSB based beam failure detection 4888.5A.3
Void 4888.5A.4 Minimum requirement for L1 indication 4888.5A.5
Requirements for SSB based candidate beam detection 4898.5A.5.1
Introduction 4898.5A.5.2 Minimum requirement 4898.5A.5.3 Measurement
restriction for SSB based candidate beam detection 4918.5A.6 Void
4928.5A.7 Scheduling availability of UE during beam failure detection
4928.5A.7.1 Scheduling availability of UE performing beam failure
detection with a same subcarrier spacing as PDSCH/PDCCH 4928.5A.7.2
Scheduling availability of UE performing beam failure detection with a
different subcarrier spacing than PDSCH/PDCCH 4928.5A.7.3 Scheduling
availability of UE performing beam failure detection on FR2-2
4928.5A.7.4 Scheduling availability of UE performing beam failure
detection on FR1 or FR2-2 in case of FR1-FR2-2 inter-band CA and NR DC
4928.5A.8 Scheduling availability of UE during candidate beam detection
4928.5A.8.3 Scheduling availability of UE performing L1-RSRP measurement
on FR2-2 4928.5A.8.4 Scheduling availability of UE performing L1-RSRP
measurement on FR1 or FR2-2 in case of FR1-FR2-2 inter-band CA and NR-DC
4928.5B Link Recovery Procedures for Redcap 4938.5B.1 Introduction
4938.5B.2 Requirements for SSB based beam failure detection for Redcap
4938.5B.2.1 Introduction 4938.5B.2.2 Minimum requirement 4948.5B.2.3
Measurement restriction for SSB based beam failure detection 4958.5B.3
Requirements for CSI-RS based beam failure detection for Redcap
4968.5B.3.1 Introduction 4968.5B.3.2 Minimum requirement 4968.5B.3.3
Measurement restrictions for CSI-RS beam failure detection 4988.5B.4
Minimum requirement for L1 indication for Redcap 4998.5B.5 Requirements
for SSB based candidate beam detection for Redcap 5008.5B.5.1
Introduction 5008.5B.5.2 Minimum requirement 5008.5B.5.3 Measurement
restriction for SSB based candidate beam detection 5028.5B.6
Requirements for CSI-RS based candidate beam detection for Redcap
5028.5B.6.1 Introduction 5028.5B.6.2 Minimum requirement 5028.5B.6.3
Measurement restriction for CSI-RS based candidate beam detection
5048.5B.7 Scheduling availability of UE during beam failure detection
for Redcap 5058.5B.7.1 Scheduling availability of UE performing beam
failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1
5058.5B.7.2 Scheduling availability of UE performing beam failure
detection with a different subcarrier spacing than PDSCH/PDCCH on FR1
5058.5B.7.3 Scheduling availability of UE performing beam failure
detection on FR2 5058.5B.8 Scheduling availability of UE during
candidate beam detection for Redcap 5068.5B.8.1 Scheduling availability
of UE performing L1-RSRP measurement with a same subcarrier spacing as
PDSCH/PDCCH on FR1 5068.5B.8.2 Scheduling availability of UE performing
L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH
on FR1 5068.5B.8.3 Scheduling availability of UE performing L1-RSRP
measurement on FR2 5068.5B.9 Minimum requirement at transitions for beam
failure detection for Redcap 5068.5C Link Recovery Procedures for
Satellite Access 5078.5C.1 Introduction 5078.5C.2 Requirements for SSB
based beam failure detection 5078.5C.2.1 Introduction 5078.5C.2.2
Minimum requirement 5088.5C.2.3 Measurement restriction for SSB based
beam failure detection 5088.5C.3 Requirements for CSI-RS based beam
failure detection 5098.5C.3.1 Introduction 5098.5C.3.2 Minimum
requirement 5098.5C.3.3 Measurement restrictions for CSI-RS beam failure
detection 5108.5C.4 Minimum requirement for L1 indication 5118.5C.5
Requirements for SSB based candidate beam detection 5118.5C.5.1
Introduction 5118.5C.5.2 Minimum requirement 5118.5C.5.3 Measurement
restriction for SSB based candidate beam detection 5128.5C.6
Requirements for CSI-RS based candidate beam detection 5138.5C.6.1
Introduction 5138.5C.6.2 Minimum requirement 5138.5C.6.3 Measurement
restriction for CSI-RS based candidate beam detection 5148.5C.7
Scheduling availability of UE during beam failure detection 5148.5C.7.1
Scheduling availability of UE performing beam failure detection with a
same subcarrier spacing as PDSCH/PDCCH on FR1 5148.5C.7.2 Scheduling
availability of UE performing beam failure detection with a different
subcarrier spacing than PDSCH/PDCCH on FR1 5148.5C.8 Scheduling
availability of UE during candidate beam detection 5158.5C.8.1
Scheduling availability of UE performing L1-RSRP measurement with a same
subcarrier spacing as PDSCH/PDCCH on FR1 5158.5C.8.2 Scheduling
availability of UE performing L1-RSRP measurement with a different
subcarrier spacing than PDSCH/PDCCH on FR1 5158.5C.9 Minimum requirement
at transitions for beam failure detection 5158.6 Active BWP switch delay
5158.6.1 Introduction 5158.6.2 DCI and timer based BWP switch delay on a
single CC 5168.6.2A DCI based BWP switch delay on multiple CCs
5178.6.2A.1 Simultaneous DCI based BWP switch delay on multiple CCs
5178.6.2A.2 Non-simultaneous DCI based BWP switch delay on multiple CCs
5198.6.2B Timer based BWP switch delay on multiple CCs 5198.6.2B.1
Simultaneous timer based BWP switch delay on multiple CCs 5198.6.2B.2
Non-simultaneous timer based BWP switch delay on multiple CCs 5198.6.3
RRC based BWP switch delay on a single CC 5208.6.3A RRC based BWP switch
delay on multiple CCs 5218.6.3A.1 Simultaneous RRC based BWP switch
delay on multiple CCs 5218.6.3A.2 Non-simultaneous RRC based BWP switch
delay on multiple CCs 5218.6.4 BWP switch delay on Consistent UL CCA
recovery 5228.6A Active BWP switch delay for RedCap 5228.6A.1
Introduction 5228.6A.2 DCI and timer based BWP switch delay on a single
CC 5228.6A.3 RRC based BWP switch delay on a single CC 5248.6C Active
BWP switch delay for satellite access 5248.6C.1 Introduction 5248.6C.2
DCI and timer based BWP switch delay on a single CC 5248.6C.3 RRC based
BWP switch delay on a single CC 5268.7 Void 5268.8 NE-DC: E-UTRAN PSCell
Addition and Release Delay 5268.8.1 Introduction 5268.8.2 E-UTRAN PSCell
Addition Delay Requirement 5268.8.3 E-UTRAN PSCell Release Delay
Requirement 5278.9 NR-DC: PSCell Addition and Release Delay 5278.9.1
Introduction 5278.9.2 PSCell Addition Delay Requirement 5278.9.3 PSCell
Release Delay Requirement 5288.9A Conditional PSCell Addition Delay
5288.9A.1 Introduction 5288.9A.2 Conditional PSCell Addition Delay
Requirement 5288.9A.2.1 Measurement time 5298.9B NR-DC: PSCell Addition
and Release Delay in Carriers with CCA 5298.9B.1 Introduction 5298.9B.2
PSCell Addition Delay Requirement 5308.9B.3 PSCell Release Delay
Requirement 5308.10 Active TCI state switching delay 5318.10.3A MAC-CE
based TCI state switch delay in HST FR2 scenarios 5328.10.4 DCI based
TCI state switch delay 5328.10.5 RRC based TCI state switch delay
5338.10.6 Active TCI state list update delay 5338.10A Active TCI state
switching delay with CCA 5338.10A.1 Introduction 5338.10A.2 Known
conditions for TCI state 5348.10A.3 MAC-CE based TCI state switch delay
5348.10A.4 DCI based TCI state switch delay 5358.10A.5 RRC based TCI
state switch delay 5358.10A.6 Active TCI state list update delay
5368.10B Active TCI state switching delay for RedCap 5368.10B.1
Introduction 5368.10B.2 Known conditions for TCI state 5368.10B.3 MAC-CE
based TCI state switch delay 5378.10B.4 DCI based TCI state switch delay
5388.10B.5 RRC based TCI state switch delay 5388.10B.6 Active TCI state
list update delay 5388.10C Active TCI state switching delay for
satellite access 5398.10C.1 Introduction 5398.10C.2 MAC-CE based TCI
state switch delay 5398.10C.4 DCI based TCI state switch delay
5398.10C.5 RRC based TCI state switch delay 5398.10C.6 Active TCI state
list update delay 5398.11 PSCell Change 5408.11A PSCell Change in
Carriers with CCA 5408.11B Conditional PSCell Change 5408.11B.1
Introduction 5408.11B.2 Conditoinal PSCell Change delay 5418.11B.2.1
Measurement time 5418.11D Conditional PSCell Change in Carriers with CCA
5428.11D.1 Introduction 5428.11D.2 Conditional PSCell Change delay
5428.11D.2.1 Measurement time 5438.12 Uplink spatial relation switch
delay 5438.12.1 Introduction 5438.12.2 Known conditions for spatial
relation when associated with DL-RS 5438.12.3 MAC-CE based spatial
relation switch delay 5448.12.4 DCI based spatial relation switch delay
5448.12.5 RRC based spatial relation switch delay 5458.12A Uplink
spatial relation switch delay for RedCap 5458.12A.1 Introduction
5458.12A.2 Known conditions for spatial relation when associated with
DL-RS 5458.12A.3 MAC-CE based spatial relation switch delay 5468.12A.4
DCI based spatial relation switch delay 5468.12A.5 RRC based spatial
relation switch delay 5478.12C Uplink spatial relation switch delay for
satellite access 5478.12C.1 Void 5488.12C.2 Void 5488.12C.3 Void
5488.12C.4 Void 5488.12C.5 Void 5488.13 UE-specific CBW change 5488.13.1
Introduction 5488.13.2 UE-specific CBW change delay 5488.13A UE-specific
CBW change for RedCap 5488.13A.1 Introduction 5488.13A.2 UE-specific CBW
change delay 5488.13C UE-specific CBW change for satellite access
5498.13C.1 Introduction 5498.13C.2 UE-specific CBW change delay 5498.14
Pathloss reference signal switching delay 5498.14.1 Introduction
5498.14.2 Known conditions for pathloss reference signal 5508.14.3
MAC-CE based pathloss reference signal switch delay 5508.14C Pathloss
reference signal switching delay for satellite access 5518.14C.1
Introduction 5518.14C.2 Known conditions for pathloss reference signal
5518.14C.3 MAC-CE based pathloss reference signal switch delay 5518.15
Active downlink TCI state switching delay for unified TCI 5528.15.1
Introduction 5528.15.4 DCI based downlink TCI state switch delay
5548.15.5 Active Downlink TCI state list update delay 5548.16 Active
uplink TCI state switching delay for unified TCI 5558.16.1 Introduction
5558.16.4 DCI based uplink TCI state switch delay 5578.16.5 Active
Uplink TCI state list update delay 5588.17 SCG Activation and
Deactivation Delay 5598.17.1 Introduction 5598.17.2 SCG Activation Delay
Requirement 5598.17.3 SCG Deactivation Delay Requirement 5608.18 TRP
specific Link Recovery Procedures 5618.18.1 Introduction 5618.18.2
Requirements for TRP specific SSB based beam failure detection
5618.18.2.1 Introduction 5618.18.2.2 Minimum requirement 5628.18.2.3
Measurement restriction for SSB based beam failure detection 5648.18.3
Requirements for CSI-RS based beam failure detection 5648.18.3.1
Introduction 5648.18.3.2 Minimum requirement 5658.18.3.3 Measurement
restrictions for CSI-RS beam failure detection 5678.18.4 Minimum
requirement for L1 indication 5688.18.5 Requirements for SSB based
candidate beam detection 5688.18.5.1 Introduction 5688.18.5.2 Minimum
requirement 5688.18.5.3 Measurement restriction for SSB based candidate
beam detection 5708.18.6 Requirements for CSI-RS based candidate beam
detection 5718.18.6.1 Introduction 5718.18.6.2 Minimum requirement
5718.18.6.3 Measurement restriction for CSI-RS based candidate beam
detection 5738.18.7 Requirements for TRP specific Beam Failure Recovery
5748.18.7.1 Introduction 5748.18.7.2 Requirement 5748.18.8 Scheduling
availability of UE during TRP specific beam failure detection
5748.18.8.1 Scheduling availability of UE performing TRP specific beam
failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1
5748.18.8.2 Scheduling availability of UE performing TRP specific beam
failure detection with a different subcarrier spacing than PDSCH/PDCCH
on FR1 5758.18.8.3 Scheduling availability of UE performing TRP specific
beam failure detection on FR2 5758.18.8.4 Scheduling availability of UE
performing TRP specific beam failure detection on FR1 or FR2 in case of
FR1-FR2 inter-band CA and NR DC 5758.18.9 Scheduling availability of UE
during TRP specific candidate beam detection 5768.18.9.1 Scheduling
availability of UE performing L1-RSRP measurement with a same subcarrier
spacing as PDSCH/PDCCH on FR1 5768.18.9.2 Scheduling availability of UE
performing L1-RSRP measurement with a different subcarrier spacing than
PDSCH/PDCCH on FR1 5768.18.9.3 Scheduling availability of UE performing
L1-RSRP measurement on FR2 5768.18.9.4 Scheduling availability of UE
performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2
inter-band CA and NR-DC 5778.19 Pre-configured measurement gap
activation/deactivation delay 5778.19.1 Introduction 5778.19.2
Pre-configured measurement gap activation/deactivation upon
DCI/timer-based BWP switch 5778.19.2.1 Activation/deactivation upon
DCI/timer-based BWP switch delay on a single CC 5778.19.3 Pre-configured
measurement gap activation/deactivation upon SCell
activation/deactivation 5778.19.4 Pre-configured measurement gap
activation/deactivation upon RRC reconfiguration 5789 Measurement
Procedure 5799.1 General measurement requirement 5799.1.1 Introduction
5799.1.2 Measurement gap 5799.1.2.1 EN-DC: Measurement Gap Sharing
5919.1.2.1a SA: Measurement Gap Sharing 5929.1.2.1b NE-DC: Measurement
Gap Sharing 5939.1.2.1c NR-DC: Measurement Gap Sharing 5949.1.3 UE
Measurement capability 5959.1.3.1 EN-DC: Monitoring of multiple layers
using gaps 5959.1.3.1a SA: Monitoring of multiple layers using gaps
5959.1.3.1b NE-DC: Monitoring of multiple layers using gaps 5969.1.3.1c
NR-DC: Monitoring of multiple layers using gaps 5969.1.3.2 EN-DC:
Maximum allowed layers for multiple monitoring 5979.1.3.2a SA: Maximum
allowed layers for multiple monitoring 5989.1.3.2b NE-DC: Maximum
allowed layers for multiple monitoring 5989.1.3.2c NR-DC: Maximum
allowed layers for multiple monitoring 5999.1A.3.2 Void 6009.1.3A UE
Measurement capability under operation mode with CCA 6009.1.3A.1 EN-DC:
Monitoring of multiple layers using gaps under CCA 6009.1.3A.1a SA:
Monitoring of multiple layers using gaps under CCA 6009.1.3A.2 EN-DC:
Maximum allowed layers for multiple monitoring under CCA 6009.1.3A.2a
SA: Maximum allowed layers for multiple monitoring under CCA 6019.1.3C
UE Measurement capability under operation mode with satellite access
6019.1.3C.1a SA: Monitoring of multiple layers using gaps under
satellite access 6019.1.3C.2a SA: Maximum allowed layers for multiple
monitoring for SAN 6029.1.4 Capabilities for Support of Event Triggering
and Reporting Criteria 6029.1.4.1 Introduction 6029.1.4.2 Requirements
6029.1.5 Carrier-specific scaling factor 6069.1.5.1 Monitoring of
multiple layers outside gaps 6079.1.5.1.1 EN-DC mode: carrier-specific
scaling factor for SSB-based, CSI-RS based L3 measurements and RSSI and
channel occupancy measurements performed outside gaps 6099.1.5.1.2 SA
mode: carrier-specific scaling factor for SSB-based, CSI-RS based L3
measurements and RSSI and channel occupancy measurements performed
outside gaps 6109.1.5.1.3 NR-DC mode: carrier-specific scaling factor
for SSB-based and CSI-RS based L3 measurements performed outside gaps
6119.1.5.1.4 NE-DC mode: carrier-specific scaling factor for SSB-based
and CSI-RS based measurements performed outside gaps 6119.1.5.2
Monitoring of multiple layers within gaps 6129.1.5.2.1 EN-DC mode:
carrier-specific scaling factor for SSB, CSI-RS-based L3 measurements
and RSSI and channel occupancy measurements performed within gaps
6149.1.5.2.2 SA mode: carrier-specific scaling factor for SSB,
CSI-RS-based L3 measurements and RSSI and channel occupancy measurements
performed within gaps 6169.1.5.2.3 NE-DC: carrier-specific scaling
factor for SSB-based and CSI-RS based L3 measurements performed within
gaps 6189.1.5.2.4 NR-DC: carrier-specific scaling factor for SSB-based
and CSI-RS-based L3 measurements performed within gaps 6209.1.5.2.5 SA
mode: carrier-specific scaling factor for PRS-based measurements
performed within gaps 6219.1.5.2.6 NE-DC: carrier-specific scaling
factor for PRS-based measurements performed within gaps 6229.1.5.2.7
NR-DC: carrier-specific scaling factor for PRS-based measurements
performed within gaps 6229.1.5.3 Monitoring of multiple layers within
NCSG 6229.1.5.3.1 SA mode: carrier-specific scaling factor for
measurements performed within NCSG 6239.1.6 Minimum requirement at
transitions 6239.1.7 Pre-configured measurement gap 6249.1.7.1
Introduction 6249.1.7.2 Requirements applicability 6249.1.7.3
Requirements 6259.1.7.3.1 Requirements for autonomous
activation/deactivation mechanism 6259.1.7.3.2 Requirements for
network-controlled activation/deactivation mechanism 6269.1.7.3.3
Requirements for reception/transmission during activation/deactivation
6269.1.8 Concurrent measurement gaps 6269.1.8.1 Introduction 6269.1.8.2
Requirements 6269.1.8.3 Collision between concurrent measurement gaps
6289.1.8.4 Measurement gap related requirements of concurrent
measurement gaps 6289.1.9 Network controlled small gap 6289.1.9.1
Introduction 6289.1.9.2 Requirements applicability 6299.1.10 MUSIM gaps
6329.1.11 UL gap for Tx power management 6339.1A General measurement
requirement for RedCap 6349.1A.1 Introduction 6349.1A.2 Measurement gap
6349.1A.2.1 SA: Measurement Gap Sharing 6389.1A.3 UE Measurement
capability 6399.1A.3.1 SA: Monitoring of multiple layers using gaps
6399.1A.3.2 SA: Maximum allowed layers for multiple monitoring 6399.1A.4
Capabilities for Support of Event Triggering and Reporting Criteria
6399.1A.4.1 Introduction 6399.1A.4.2 Requirements 6409.1A.5
Carrier-specific scaling factor 6409.1A.5.1 Monitoring of multiple
layers outside gaps 6409.1A.5.1.1 SA mode: carrier-specific scaling
factor for SSB-based measurements performed outside gaps 6419.1A.5.2
Monitoring of multiple layers within gaps 6419.1A.5.2.1 SA mode:
carrier-specific scaling factor for SSB measurements performed within
gaps 6419.1A.6 Minimum requirement at transitions 6429.1C General
measurement requirement for SAN 6439.1C.1 Introduction 6439.1C.2
Measurement gap 6439.1C.8 Concurrent measurement gaps for SAN
6459.1C.8.1 Introduction 6459.1C.8.2 Requirements 6459.1C.8.3 Collision
between concurrent measurement gaps 6459.1C.8.4 Measurement gap related
requirements of concurrent measurement gaps 6469.1C.9 Collision between
SMTC and measurement gap for SAN 6469.1C.9.1 Introduction 6469.1C.9.2
Collision between SMTCs and measurement gap 6469.1C.9.3 Collision
between multiple SMTCs on a SAN carrier 6469.2 NR intra-frequency
measurements 6479.2.1 Introduction 6479.2.2 Requirements applicability
6499.2.3 Number of cells and number of SSB 6499.2.3.1 Requirements for
FR1 6499.2.3.2 Requirements for FR2 6499.2.4 Measurement Reporting
Requirements 6499.2.4.1 Periodic Reporting 6499.2.4.2 Event-triggered
Periodic Reporting 6509.2.4.3 Event Triggered Reporting 6509.2.5
Intrafrequency measurements without measurement gaps 6509.2.5.1
Intrafrequency cell identification 6509.2.5.2 Measurement period
6559.2.5.3 Scheduling availability of UE during intra-frequency
measurements 6589.2.5.3.1 Scheduling availability of UE performing
measurements in TDD bands on FR1 6589.2.5.3.2 Scheduling availability of
UE performing measurements with a different subcarrier spacing than
PDSCH/PDCCH on FR1 6589.2.5.3.3 Scheduling availability of UE performing
measurements on FR2 6599.2.5.3.4 Scheduling availability of UE
performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA
6609.2.5.4 SFTD Measurements between PCell and PSCell 6619.2.5.4.1
Introduction 6619.2.5.4.2 SFTD Measurement delay 6619.2.5.4.3 SFTD
Measurement Reporting Delay 6619.2.6 Intra-frequency measurements with
measurement gaps 6629.2.6.1 Void 6629.2.6.2 Intra-frequency cell
identification 6629.2.6.3 Intrafrequency Measurement Period 6649.2.7
Intra-frequency measurements with NCSG 6669.2.7.1 Intra-frequency cell
identification 6669.2.7.2 Measurement period 6689.2.7.3 Scheduling
availability during intra-frequency measurement with NCSG 6699.2A NR
intra-frequency measurements with CCA 6699.2A.1 Introduction 6699.2A.2
Requirements applicability 6709.2A.3 Number of cells and number of SSB
6709.2A.3.1 Requirements for FR1 6709.2A.3.2 Requirements for FR2-2
6719.2A.4 Measurement Reporting Requirements 6719.2A.5 Intra-frequency
measurements without measurement gaps 6729.2A.5.2 Measurement period
6769.2A.5.3 Scheduling availability of UE during intra-frequency
measurements 6789.2A.5.3.1 Scheduling availability of UE performing
measurements in TDD bands on FR1 6799.2A.5.3.2 Scheduling availability
of UE performing measurements with a different subcarrier spacing than
PDSCH/PDCCH on FR1 6799.2A.5.3.3 Scheduling availability of UE
performing measurements in TDD bands on FR2-2 6799.2A.6 Intra-frequency
measurements with measurement gaps 6799.2A.6.1 Intra-frequency cell
identification 6799.2A.6.2 Intra-frequency Measurement Period 6829.2A.7
Intra-frequency RSSI and Channel occupancy measurements 6839.2A.7.1
Intra-frequency RSSI measurements 6839.2A.7.2 Intra-frequency Channel
occupancy measurements 6859.2A.7.3 Scheduling restriction during RSSI
and Channel Occupancy measurements in FR1 6869.2A.7.4 Scheduling
restriction during RSSI measurements in FR2-2 6869.2B NR intra-frequency
measurements for RedCap 6879.2B.1 Introduction 6879.2B.2 Requirements
applicability 6879.2B.3 Number of cells and number of SSB 6889.2B.3.1
Requirements for FR1 6889.2B.3.2 Requirements for FR2 6889.2B.4
Measurement Reporting Requirements 6889.2B.4.1 Periodic Reporting
6889.2B.4.2 Event-triggered Periodic Reporting 6889.2B.4.3 Event
Triggered Reporting 6889.2B.5 Intra-frequency measurements without
measurement gaps 6899.2B.5.1 Intra-frequency cell identification
6899.2B.5.2 Measurement period 6919.2B.5.3 Scheduling availability of UE
during intra-frequency measurements 6929.2B.5.3.1 Scheduling
availability of UE performing measurements in TDD bands on FR1
6929.2B.5.3.2 Scheduling availability of UE performing measurements with
a different subcarrier spacing than PDSCH/PDCCH on FR1 6929.2B.5.3.3
Scheduling availability of UE performing measurements on FR2
6939.2B.5.3.4 Scheduling availability of HD-FDD UE performing
measurements on FR1 6939.2B.6 Intra-frequency measurements with
measurement gaps 6949.2B.6.1 Intra-frequency cell identification
6949.2B.6.2 Intra-frequency Measurement Period 6959.2C NR
intra-frequency measurements for SAN 6969.2C.1 Introduction 6969.2C.2
Requirements applicability 6979.2C.3 Number of cells and number of SSB
6989.2C.3.1 Requirements for FR1 6989.2C.4 Measurement Reporting
Requirements 6989.2C.4.1 Periodic Reporting 6989.2C.4.2 Event-triggered
Periodic Reporting 6989.2C.4.3 Event Triggered Reporting 6989.2C.5 Intra
frequency measurements without measurement gaps 6999.2C.5.1 Intra
frequency cell identification 6999.2C.5.2 Measurement period 7019.2C.5.3
Scheduling availability of UE during intra-frequency measurements
7019.2C.5.3.1 Scheduling availability of UE performing measurements with
a different subcarrier spacing than PDSCH/PDCCH on FR1 7019.2C.5.3.2
Scheduling availability of UE performing measurements on a neighbor cell
served by a different satellite in LEO 7029.2C.6 Intra-frequency
measurements with measurement gaps 7029.2C.6.1 Intra-frequency cell
identification 7029.2C.6.3 Intrafrequency Measurement Period 7049.3 NR
inter-frequency measurements 7049.3.1 Introduction 7049.3.2 Requirements
applicability 7069.3.2.1 Void 7069.3.2.2 Void 7069.3.3 Number of cells
and number of SSB 7069.3.3.1 Requirements for FR1 7069.3.3.2
Requirements for FR2 7069.3.4 Inter-frequency measurement with
measurement gaps 7069.3.4.1 Void 7109.3.4.2 Void 7109.3.5
Inter-frequency measurements 7109.3.5.1 Void 7119.3.5.2 Void 7119.3.5.3
Void 7119.3.6 Inter-frequency measurements reporting requirements
7119.3.6.1 Periodic Reporting 7119.3.6.2 Event-triggered Periodic
Reporting 7119.3.6.3 Event-triggered Reporting 7119.3.7 Void 7129.3.8
Inter-frequency SFTD measurement requirements 7129.3.8.1 Introduction
7129.3.8.2 SFTD Measurement delay 7129.3.8.3 SFTD Measurement reporting
delay 7139.3.9 Inter frequency measurements without measurement gaps
7139.3.9.1 Inter frequency Cell identification 7139.3.9.2 Measurement
period 7169.3.9.3 Scheduling availability of UE during inter-frequency
measurements when the SSB is completely contained in the active BWP of
the UE 7189.3.9.3.1 Scheduling availability of UE performing
measurements in TDD bands on FR1 7189.3.9.3.2 Scheduling availability of
UE performing measurements with a different subcarrier spacing than
PDSCH/PDCCH on FR1 7189.3.9.3.3 Scheduling availability of UE performing
measurements on FR2 7199.3.9.3.4 Scheduling availability of UE
performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA
7199.3.9.4 Scheduling availability of UE during inter-frequency
measurements when the SSB is not completely contained in the active BWP
of the UE 7199.3.9.4.1 Scheduling availability of UE performing
measurements in TDD bands on FR1 7209.3.9.4.2 Scheduling availability of
UE performing measurements with a different subcarrier spacing than
PDSCH/PDCCH on FR1 7209.3.9.4.3 Scheduling availability of UE performing
measurements on FR2 7219.3.9.4.4 Scheduling availability of UE
performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA
7229.3.10 Inter-frequency measurement with NCSG 7239.3.10.1
Inter-frequency cell identification 7239.3.10.2 Measurement period
7249.3.10.3 Scheduling availability during inter-frequency measurement
with NCSG 7249.3.10.3.1 Scheduling availability of UE performing
measurements in TDD bands on FR1 7259.3.10.3.2 Scheduling availability
of UE performing measurements with a different subcarrier spacing than
PDSCH/PDCCH on FR1 7259.3.10.3.3 Scheduling availability of UE
performing measurements on FR2 7269.3.10.3.4 Scheduling availability of
UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band
CA 7279.3A NR inter-frequency measurements in carrier frequencies with
CCA 7289.3A.1 Introduction 7289.3A.2 Requirements applicability
7289.3A.3 Number of cells and number of SSB 7299.3A.3.1 Requirements for
FR1 7299.3A.3.2 Requirements for FR2-2 7299.3A.4 Inter-frequency cell
identification 7299.3A.5 Inter-frequency measurements 7319.3A.6 NR
Inter-frequency measurements reporting requirements 7339.3A.6.1 Periodic
Reporting 7339.3A.6.2 Event-triggered Periodic Reporting 7339.3A.6.3
Event-triggered Reporting 7339.3A.8 Inter-frequency RSSI measurements
7339.3A.9 Inter-frequency channel occupancy measurements 7349.3B NR
inter-frequency measurements for RedCap 7359.3B.1 Introduction 7359.3B.2
Requirements applicability 7359.3B.3 Number of cells and number of SSB
7369.3B.3.1 Requirements for FR1 7369.3B.3.2 Requirements for FR2
7369.3B.4 Inter-frequency measurement with measurement gaps 7369.3B.5
Inter-frequency measurements 7379.3B.6 Inter-frequency measurements
reporting requirements 7389.3B.6.1 Periodic Reporting 7389.3B.6.2
Event-triggered Periodic Reporting 7389.3B.6.3 Event-triggered Reporting
7389.3B.7 Inter frequency measurements without measurement gaps
7399.3B.7.1 Inter frequency Cell identification 7399.3B.7.2 Measurement
period 7419.3B.7.3 Scheduling availability of UE during inter-frequency
measurements 7429.3B.7.3.1 Scheduling availability of UE performing
measurements in TDD bands on FR1 7429.3B.7.3.2 Scheduling availability
of UE performing measurements with a different subcarrier spacing than
PDSCH/PDCCH on FR1 7439.3B.7.3.3 Scheduling availability of UE
performing measurements on FR2 7439.3B.7.3.4 Scheduling availability of
HD-FDD UE performing measurements on FR1 7439.3C NR inter-frequency
measurements for SAN 7449.3C.1 Introduction 7449.3C.2 Requirements
applicability 7459.3C.3 Number of cells and number of SSB 7459.3C.3.1
Requirements for FR1 7459.3C.4 Inter-frequency measurement with
measurement gaps 7459.3C.5 Inter-frequency measurements 7479.3C.6
Inter-frequency measurements reporting requirements 7479.3C.6.1 Periodic
Reporting 7479.3C.6.2 Event-triggered Periodic Reporting 7479.3C.6.3
Event-triggered Reporting 7479.3C.7 Inter frequency measurements without
measurement gaps 7489.3C.7.1 Inter frequency Cell identification
7489.3C.7.2 Measurement period 7499.3C.7.3 Scheduling availability of UE
during inter-frequency measurements 7499.3C.7.3.1 Void 7509.3C.7.3.2
Scheduling availability of UE performing measurements with a different
subcarrier spacing than PDSCH/PDCCH on FR1 7509.4 Inter-RAT measurements
7509.4.1 Introduction 7509.4.2 NR − E-UTRAN FDD measurements 7529.4.2.1
Introduction 7529.4.2.2 Requirements when no DRX is used 7529.4.2.3
Requirements when DRX is used 7539.4.2.4 Measurement reporting
requirements 7559.4.2.4.1 Periodic Reporting 7559.4.2.4.2
Event-Triggered Periodic Reporting 7559.4.2.4.3 Event-Triggered
Reporting 7569.4.2.5 Scheduling Availability During NR − E-UTRAN FDD
measurements with NCSG 7569.4.3 NR − E-UTRAN TDD measurements 7569.4.3.1
Introduction 7569.4.3.2 Requirements when no DRX is used 7569.4.3.3
Requirements when DRX is used 7589.4.3.4 Measurement reporting
requirements 7599.4.3.4.1 Periodic Reporting 7599.4.3.4.2
Event-Triggered Periodic Reporting 7609.4.3.4.3 Event-Triggered
Reporting 7609.4.3.5 Scheduling Availability During NR − E-UTRAN TDD
measurements with NCSG 7609.4.4 Inter-RAT RSTD measurements 7609.4.4.1
NR − E-UTRAN FDD RSTD measurements 7609.4.4.1.1 Introduction
7609.4.4.1.2 Requirements 7619.4.4.2 NR − E-UTRAN TDD RSTD measurements
7649.4.4.2.1 Introduction 7649.4.4.2.2 Requirements 7659.4.5 Inter-RAT
E-CID measurements 7689.4.5.1 NR−E-UTRAN FDD E-CID RSRP and RSRQ
measurements 7689.4.5.1.1 Introduction 7689.4.5.1.2 Requirements
7689.4.5.1.3 Measurement Reporting Delay 7689.4.5.2 NR−E-UTRAN TDD E-CID
RSRP and RSRQ measurements 7699.4.5.2.1 Introduction 7699.4.5.2.2
Requirements 7699.4.5.2.3 Measurement Reporting Delay 7699.4.6 NR −
UTRAN FDD measurements 7699.4.6.1 Introduction 7699.4.6.2 Requirements
when no DRX is used 7699.4.6.3 Requirements when DRX is used 7709.4.7 NR
-- E-UTRAN measurements with autonomous gaps 7729.4.7.1 CGI
identification of an E-UTRA cell with autonomous gaps 7729.4.7.2 CGI
reporting delay 7729.4A Inter-RAT measurements for RedCap 7739.4A.1
Introduction 7739.4A.2 NR − E-UTRAN FDD measurements 7749.4A.2.1
Introduction 7749.4A.2.2 Requirements when no DRX is used 7749.4A.2.3
Requirements when DRX is used 7759.4A.2.4 Measurement reporting
requirements 7769.4A.2.4.1 Periodic Reporting 7769.4A.2.4.2
Event-Triggered Periodic Reporting 7769.4A.2.4.3 Event-Triggered
Reporting 7769.4A.3 NR − E-UTRAN TDD measurements 7779.4A.3.1
Introduction 7779.4A.3.2 Requirements when no DRX is used 7779.4A.3.3
Requirements when DRX is used 7799.4A.3.4 Measurement reporting
requirements 7809.4A.3.4.1 Periodic Reporting 7809.4A.3.4.2
Event-Triggered Periodic Reporting 7809.4A.3.4.3 Event-Triggered
Reporting 7809.4A.4 NR -- E-UTRAN measurements with autonomous gaps
7819.4A.4.1 CGI identification of an E-UTRA cell with autonomous gaps
7819.4A.4.2 CGI reporting delay 7819.4A.4.3 CGI reporting scheduling
restriction 7819.5 L1-RSRP measurements for Reporting 7829.5.1
Introduction 7829.5.2 Requirements applicability 7829.5.3 Measurement
Reporting Requirements 7839.5.3.1 Periodic Reporting 7839.5.3.2
Semi-Persistent Reporting 7839.5.3.3 Aperiodic Reporting 7839.5.4
L1-RSRP measurement requirements 7849.5.4.1 SSB based L1-RSRP Reporting
7849.5.4.2 CSI-RS based L1-RSRP Reporting 7879.5.4A Void 7909.5.4A.1
Void 7909.5.5 Measurement restriction for CSI-RS and SSB for L1-RSRP
measurement 7909.5.5.1 Measurement restriction for SSB based L1-RSRP
7909.5.5.2 Measurement restriction for CSI-RS based L1-RSRP 7919.5.6
Scheduling availability of UE during L1-RSRP measurement 7929.5.6.1
Scheduling availability of UE performing L1-RSRP measurement with a same
subcarrier spacing as PDSCH/PDCCH on FR1 7929.5.6.2 Scheduling
availability of UE performing L1-RSRP measurement with a different
subcarrier spacing than PDSCH/PDCCH on FR1 7929.5.6.3 Scheduling
availability of UE performing L1-RSRP measurement on FR2 7929.5.6.4
Scheduling availability of UE performing L1-RSRP measurement on FR1 or
FR2 in case of FR1-FR2 inter-band CA 7949.5A L1-RSRP measurements for
Reporting under CCA 7949.5A.1 Introduction 7949.5A.2 Requirements
applicability 7949.5A.3 Measurement Reporting Requirements 7949.5A.3.1
Periodic Reporting 7959.5A.3.2 Semi-Persistent Reporting 7959.5A.3.3
Aperiodic Reporting 7959.5A.4 L1-RSRP measurement requirements
7959.5A.4.1 SSB based L1-RSRP Reporting 7959.5A.5 Measurement
restriction for L1-RSRP measurement 7989.5A.5.1 Measurement restriction
for SSB based L1-RSRP 7989.5A.6 Scheduling availability of UE during
L1-RSRP measurement 7989.5A.6.1 Scheduling availability of UE performing
L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1
7989.5A.6.2 Scheduling availability of UE performing L1-RSRP measurement
with a different subcarrier spacing than PDSCH/PDCCH on FR1 7999.5A.6.3
(Void) 7999.5A.6.3A Scheduling availability of UE performing L1-RSRP
measurement in case of FR1-FR2 inter-band CA 7999.5A.6.3B Scheduling
availability of UE performing L1-RSRP measurement on FR2-2 7999.5A.6.4
Scheduling availability of UE performing L1-RSRP measurement on FR1 or
FR2 in case of FR1-FR2 inter-band CA 8009.5B L1-RSRP measurements for
Reporting for RedCap 8009.5B.1 Introduction 8009.5B.2 Requirements
applicability 8009.5B.3 Measurement Reporting Requirements 8019.5B.3.1
Periodic Reporting 8019.5B.3.2 Semi-Persistent Reporting 8019.5B.3.3
Aperiodic Reporting 8019.5B.4 L1-RSRP measurement requirements
8029.5B.4.1 SSB based L1-RSRP Reporting 8029.5B.4.2 CSI-RS based L1-RSRP
Reporting 8039.5B.5 Measurement restriction for CSI-RS and SSB for
L1-RSRP measurement 8069.5B.5.1 Measurement restriction for SSB based
L1-RSRP 8069.5B.5.2 Measurement restriction for CSI-RS based L1-RSRP
8079.5B.6 Scheduling availability of UE during L1-RSRP measurement
8079.5B.6.1 Scheduling availability of UE performing L1-RSRP measurement
with a same subcarrier spacing as PDSCH/PDCCH on FR1 8079.5B.6.2
Scheduling availability of UE performing L1-RSRP measurement with a
different subcarrier spacing than PDSCH/PDCCH on FR1 8079.5B.6.3
Scheduling availability of UE performing L1-RSRP measurement on FR2
8089.5C L1-RSRP measurements for Reporting for satellite access
8089.5C.1 Introduction 8089.5C.3 Measurement Reporting Requirements
8099.5C.3.1 Periodic Reporting 8099.5C.3.2 Semi-Persistent Reporting
8099.5C.3.3 Aperiodic Reporting 8109.5C.4 L1-RSRP measurement
requirements 8109.5C.4.1 SSB based L1-RSRP Reporting 8109.5C.5
Measurement restriction for L1-RSRP measurement 8129.5C.5.1 Measurement
restriction for SSB based L1-RSRP 8129.5C.5.2 Measurement restriction
for CSI-RS based L1-RSRP 8129.5C.6 Scheduling availability of UE during
L1-RSRP measurement 8139.5C.6.1 Scheduling availability of UE performing
L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1
8139.5C.6.2 Scheduling availability of UE performing L1-RSRP measurement
with a different subcarrier spacing than PDSCH/PDCCH on FR1 8139.6
NE-DC: Measurements 8139.6.1 Introduction 8139.6.2 SFTD Measurements
8139.6.2.1 Introduction 8139.6.2.2 SFTD Measurement requirements 8139.7
Cross Link Interference measurements 8149.7.1 Introduction 8149.7.2
SRS-RSRP measurements 8149.7.2.1 Introduction 8149.7.2.2 Requirements
applicability 8159.7.2.3 Measurement Reporting Requirements 8159.7.2.3.1
Periodic Reporting 8159.7.2.3.2 Event-triggered Periodic Reporting
8159.7.2.3.3 Event Triggered Reporting 8159.7.2.4 Measurement capability
8159.7.2.5 SRS-RSRP measurement period 8169.7.3 CLI-RSSI measurements
8169.7.3.1 Introduction 8169.7.3.2 Requirements applicability 8169.7.3.3
Measurement Reporting Requirements 8169.7.3.3.1 Periodic Reporting
8169.7.3.3.2 Event-triggered Periodic Reporting 8169.7.3.3.3 Event
Triggered Reporting 8179.7.3.4 Measurement capability 8179.7.3.5
CLI-RSSI measurement period 8179.7.4 Scheduling availability of UE
during CLI measurements 8179.7.4.1 Scheduling availability of UE
performing measurement on FR1 8179.7.4.2 Scheduling availability of UE
performing measurement on FR2 8189.8 L1-SINR measurements for Reporting
8189.8.1 Introduction 8189.8.2 Requirements applicability 8199.8.3
Measurement Reporting Requirements 8199.8.3.1 Periodic Reporting
8199.8.3.2 Semi-Persistent Reporting 8209.8.4 L1-SINR measurement
requirements 8209.8.4.1 L1-SINR reporting with CSI-RS based CMR and no
dedicated IMR configured 8209.8.4.3 L1-SINR reporting with CSI-RS based
CMR and dedicated IMR configured 8259.8.5 Measurement restriction for
L1-SINR measurement 8269.8.5.1 Measurement restriction if SSB configured
for L1-SINR Measurement 8279.8.5.2 Measurement restriction if CSI-RS
configured for L1-SINR measurement 8279.8.5.3 Measurement restriction if
CSI-IM configured for L1-SINR measurement 8289.8.6 Scheduling
availability of UE during L1-SINR measurement 8289.8.6.1 Scheduling
availability of UE performing L1-SINR measurement with a same subcarrier
spacing as PDSCH/PDCCH on FR1 8289.8.6.2 Scheduling availability of UE
performing L1-SINR measurement with a different subcarrier spacing than
PDSCH/PDCCH on FR1 8289.8.6.4 Scheduling availability of UE performing
L1-SINR measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA
8299.9 NR measurements for positioning 8309.9.1 Introduction 8309.9.1.1
General Aspects of Gap-based Measurement 8309.9.1.2 General Aspects of
Gapless Measurement 8309.9.1.3 Scheduling Availability of UE during PRS
Measurement without Measurement Gaps 8319.9.2 RSTD measurements
8329.9.2.1 Introduction 8329.9.2.2 Requirements Applicability 8329.9.2.3
Measurement Capability 8339.9.2.4 Measurement Reporting Requirements
8339.9.2.4.1 Void 8339.9.2.4.2 Void 8339.9.2.4.3 Void 8339.9.2.5
Measurements Period Requirements 8339.9.2.6 Void 8369.9.2.7 Measurements
Period Requirements without Measurement Gaps 8369.9.2.8 Void 8399.9.2.9
Measurements Period Requirements with both MG and PPW 8399.9.3 PRS-RSRP
measurements 8409.9.3.1 Introduction 8409.9.3.2 Requirements
applicability 8409.9.3.3 Measurement Capability 8409.9.3.4 Measurement
Reporting Requirements 8409.9.3.5 Measurement Period Requirements
8409.9.3.6 Measurement Period Requirements without Measurement Gaps
8439.9.3.7 Void 8459.9.3.8 Measurements Period Requirements with both MG
and PPW 8459.9.4 UE Rx-Tx time difference measurements 8469.9.4.1
Introduction 8469.9.4.2 Requirements Applicability 8469.9.4.3
Measurement Capability 8469.9.4.4 Measurement Reporting Requirements
8469.9.4.5 Measurement Period Requirements 8469.9.4.6 Measurement Period
Requirements without Measurement Gaps 8509.9.4.7 Void 8539.9.4.8
Measurements Period Requirements with both MG and PPW 8539.9.5 E-CID
measurements 8549.9.5.1 Introduction 8549.9.5.2 Measurement Requirements
8549.9.5.2.1 Intra-frequency Measurement Requirements 8549.9.5.2.2
Inter-frequency Measurement Requirements 8549.9.5.2.3 Measurement
Reporting Delay 8559.9.6 PRS-RSRPP measurements 8559.9.6.1 Introduction
8559.9.6.2 Requirements applicability 8559.9.6.3 Measurement capability
8559.9.6.4 Measurement reporting requirements 8559.9.6.5 Measurement
period requirements 8569.9.6.6 Measurement Period Requirements without
Measurement Gaps 8569.9.6.7 Void 8569.9.6.8 Measurements Period
Requirements with both MG and PPW 8569.10 CSI-RS based L3 measurements
8569.10.1 Introduction 8569.10.2 CSI-RS based intra-frequency
measurements 8569.10.2.1 Introduction 8569.10.2.2 Requirements
applicability 8579.10.2.3 Number of cells and number of CSI-RS
8589.10.2.3.1 Requirements for FR1 8589.10.2.3.2 Requirements for FR2
8589.10.2.4 Measurement Reporting Requirements 8589.10.2.4.1 Periodic
Reporting 8599.10.2.4.2 Event-triggered Periodic Reporting 8599.10.2.4.3
Event Triggered Reporting 8599.10.2.5 Intra-frequency measurements
without measurement gaps 8599.10.2.6 Scheduling availability of UE
during CSI-RS based intra-frequency measurements 8619.10.2.6.1
Scheduling availability of UE performing CSI-RS based measurements in
TDD bands 8619.10.2.6.2 Scheduling availability of UE performing CSI-RS
based measurements in FR2 8619.10.3 CSI-RS based Inter-frequency
measurements 8619.10.3.1 Introduction 8619.10.3.2 Requirements
applicability 8629.10.3.3 Number of cells and number of CSI-RS resources
8629.10.3.3.1 Requirements for FR1 8629.10.3.3.2 Requirements for FR2
8639.10.3.4 Measurements reporting requirements 8639.10.3.4.1 Periodic
Reporting 8639.10.3.4.2 Event-triggered Periodic Reporting 8639.10.3.4.3
Event-triggered Reporting 8639.10.3.5 Inter frequency measurements with
measurement gaps 8639.11 NR measurements with autonomous gaps 8659.11.1
Introduction 8659.11.2 CGI identification of an NR cell with autonomous
gaps 8659.11.3 CGI reporting delay 8669.11A NR measurements with
autonomous gaps for RedCap 8669.11A.1 Introduction 8669.11A.2 CGI
identification of an NR cell with autonomous gaps 8679.11A.3 CGI
reporting delay 8689.11A.4 CGI reporting scheduling restriction 8689.12
Measurement for Propagation Delay Compensation 8689.12.1 Introduction
8689.12.2 Requirements Applicability 8689.12.3 Measurement Capability
8699.12.4 Measurement period requirements 8699.12.4.1 PRS Measurement
Period 8699.12.4.2 TRS Measurement Period 8709.12.5 Measurement
Reporting Requirements 8719.12.6 Scheduling availability during
measurement for Propagation Delay Compensation 8719.12.7 Measurement
restriction for measurement for Propagation Delay Compensation 8719.13
L1-RSRP measurements for a cell with different PCI from serving cell
8719.13.1 Introduction 8719.13.2 Requirements Applicability 8729.13.3
Measurement Reporting Requirements 8729.13.3.1 Periodic Reporting
8739.13.3.2 Semi-Persistent Reporting 8739.13.3.3 Aperiodic Reporting
8739.13.4 L1-RSRP measurement requirements 8739.13.4.1 Inter-cell SSB
based L1-RSRP Reporting 8739.13.5 Measurement restriction for L1-RSRP
measurement 8759.13.5.1 Measurement restriction for SSB based L1-RSRP
8769.13.6 Scheduling availability of UE during L1-RSRP measurement
8769.13.6.1 Scheduling availability of UE performing L1-RSRP measurement
with a same subcarrier spacing as PDSCH/PDCCH on FR1 8779.13.6.2
Scheduling availability of UE performing L1-RSRP measurement with a
different subcarrier spacing than PDSCH/PDCCH on FR1 8779.13.6.3
Scheduling availability of UE performing L1-RSRP measurement on FR2
8779.13.6.4 Scheduling availability of UE performing L1-RSRP measurement
on FR1 or FR2 in case of FR1-FR2 inter-band CA 8779.13.6.5 Scheduling
availability of UE performing L1-RSRP measurement in TDD bands on FR1
87810 Measurement Performance requirements 87910.1 NR measurements
87910.1.1 Introduction 87910.1.2 Intra-frequency RSRP accuracy
requirements for FR1 87910.1.2.1 Intra-frequency SS-RSRP accuracy
requirements 87910.1.2.1.1 Absolute SS-RSRP Accuracy 87910.1.2.1.2
Relative SS-RSRP Accuracy 88010.1.2.2 Void 88110.1.2.3 Intra-frequency
CSI-RSRP accuracy requirements 88110.1.2.3.1 Absolute CSI-RSRP Accuracy
88110.1.2.3.2 Relative CSI-RSRP Accuracy 88210.1.2B Intra-frequency RSRP
accuracy requirements for FR1 for CA/DC Idle Mode Measurements
88310.1.2B.1 Intra-frequency SS-RSRP accuracy requirements
88310.1.2B.1.1 Absolute SS-RSRP Accuracy 88310.1.2C Intra-frequency RSRP
accuracy requirements for FR1 SAN 88410.1.2C.1 Intra-frequency SS-RSRP
accuracy requirements 88410.1.2C.1.1 Absolute SS-RSRP Accuracy
88410.1.2C.1.2 Relative SS-RSRP Accuracy 88510.1.3 Intra-frequency RSRP
accuracy requirements for FR2 88510.1.3.1 Intra-frequency SS-RSRP
accuracy requirements 88510.1.3.1.1 Absolute SS-RSRP Accuracy
88510.1.3.1.2 Relative SS-RSRP Accuracy 88610.1.3.2 Void 88710.1.3.3
Intra-frequency CSI-RSRP accuracy requirements 88710.1.3.3.1 Absolute
CSI-RSRP Accuracy 88710.1.3.3.2 Relative CSI-RSRP Accuracy 88810.1.3B
Intra-frequency RSRP accuracy requirements for FR2 for CA/DC Idle Mode
Measurements 88910.1.3B.1 Intra-frequency SS-RSRP accuracy requirements
88910.1.3B.1.1 Absolute SS-RSRP Accuracy 88910.1.4 Inter-frequency RSRP
accuracy requirements for FR1 89010.1.4.1 Inter-frequency SS-RSRP
accuracy requirements 89010.1.4.1.1 Absolute Accuracy of SS-RSRP in FR1
89010.1.4.1.2 Relative Accuracy of SS-RSRP in FR1 89110.1.4.2 Void
89210.1.4.3 Inter-frequency CSI-RSRP accuracy requirements 89210.1.4.3.1
Absolute Accuracy of CSI-RSRP in FR1 89210.1.4.3.2 Relative Accuracy of
CS-RSRP in FR1 89310.1.4B Inter-frequency RSRP accuracy requirements for
FR1 for CA/DC Idle Mode Measurements 89410.1.4B.1 Inter-frequency
SS-RSRP accuracy requirements 89410.1.4B.1.1 Absolute Accuracy of
SS-RSRP in FR1 89410.1.4C Inter-frequency RSRP accuracy requirements for
FR1 SAN 89510.1.4C.1 Inter-frequency SS-RSRP accuracy requirements
89510.1.4C.1.1 Absolute Accuracy of SS-RSRP in FR1 89510.1.4C.1.2
Relative Accuracy of SS-RSRP in FR1 89610.1.5 Inter-frequency RSRP
accuracy requirements for FR2 89710.1.5.1 Inter-frequency SS-RSRP
accuracy requirements 89710.1.5.1.1 Absolute SS-RSRP Accuracy
89710.1.5.1.2 Relative SS-RSRP Accuracy 89710.1.5.2 Void 89810.1.5.3
Inter-frequency CSI-RSRP accuracy requirements 89810.1.5.3.1 Absolute
CSI-RSRP Accuracy 89810.1.5.3.2 Relative CSI-RSRP Accuracy 89910.1.5B
Inter-frequency RSRP accuracy requirements for FR2 for CA/DC Idle Mode
Measurements 90010.1.5B.1 Inter-frequency SS-RSRP accuracy requirements
90010.1.5B.1.1 Absolute SS-RSRP Accuracy 90010.1.6 RSRP Measurement
Report Mapping 90110.1.7 Intra-frequency RSRQ accuracy requirements for
FR1 90310.1.7.1 Intra-frequency SS-RSRQ accuracy requirements in FR1
90310.1.7.1.1 Absolute SS-RSRQ Accuracy in FR1 90310.1.7.2
Intra-frequency CSI-RSRQ accuracy requirements 90410.1.7.2.1 Absolute
CSI-RSRQ Accuracy 90410.1.7B Intra-frequency RSRQ accuracy requirements
for FR1 for CA/DC Idle Mode Measurements 90510.1.7B.1 Intra-frequency
SS-RSRQ accuracy requirements in FR1 90510.1.7B.1.1 Absolute SS-RSRQ
Accuracy in FR1 90510.1.7C Intra-frequency RSRQ accuracy requirements
for FR1 SAN 90610.1.7C.1 Intra-frequency SS-RSRQ accuracy requirements
in FR1 90610.1.7C.1.1 Absolute SS-RSRQ Accuracy in FR1 90610.1.8
Intra-frequency RSRQ accuracy requirements for FR2 90710.1.8.1
Intra-frequency SS-RSRQ accuracy requirements in FR2 90710.1.8.1.1
Absolute SS-RSRQ Accuracy in FR2 90710.1.8.2 Intra-frequency CSI-RSRQ
accuracy requirements 90810.1.8.2.1 Absolute CSI-RSRQ Accuracy
90810.1.8B Intra-frequency RSRQ accuracy requirements for FR2 for CA/DC
Idle Mode Measurements 90810.1.8B.1 Intra-frequency SS-RSRQ accuracy
requirements in FR2 90810.1.8B.1.1 Absolute SS-RSRQ Accuracy in FR2
90910.1.9 Inter-frequency RSRQ accuracy requirements for FR1 90910.1.9.1
Inter-frequency SS-RSRQ accuracy requirements in FR1 90910.1.9.1.1
Absolute Accuracy of SS-RSRQ in FR1 90910.1.9.1.2 Relative Accuracy of
SS-RSRQ in FR1 91010.1.9.2 Inter-frequency CSI-RSRQ accuracy
requirements 91110.1.9.2.1 Absolute CSI-RSRQ Accuracy 91110.1.9.2.2
Relative CSI-RSRQ Accuracy 91210.1.9B Inter-frequency RSRQ accuracy
requirements for FR1 for CA/DC Idle Mode Measurements 91310.1.9B.1
Inter-frequency SS-RSRQ accuracy requirements in FR1 91310.1.9B.1.1
Absolute Accuracy of SS-RSRQ in FR1 91310.1.9C Inter-frequency RSRQ
accuracy requirements for FR1 SAN 91410.1.9C.1 Inter-frequency SS-RSRQ
accuracy requirements in FR1 91410.1.9C.1.1 Absolute Accuracy of SS-RSRQ
in FR1 91410.1.9C.1.2 Relative Accuracy of SS-RSRQ in FR1 91510.1.10
Inter-frequency RSRQ accuracy requirements for FR2 91610.1.10.1
Inter-frequency SS-RSRQ accuracy requirements in FR2 91610.1.10.1.1
Absolute Accuracy of SS-RSRQ in FR2 91610.1.10.1.2 Relative Accuracy of
SS-RSRQ in FR2 91610.1.10.2 Inter-frequency CSI-RSRQ accuracy
requirements 91710.1.10.2.1 Absolute CSI-RSRQ Accuracy 91710.1.10.2.2
Relative CSI-RSRQ Accuracy 91810.1.10B Inter-frequency RSRQ accuracy
requirements for FR2 for CA/DC Idle Mode Measurements 91910.1.10B.1
Inter-frequency SS-RSRQ accuracy requirements in FR2 91910.1.10B.1.1
Absolute Accuracy of SS-RSRQ in FR2 91910.1.11 RSRQ report mapping
92010.1.12 Intra-frequency SINR accuracy requirements for FR1
92010.1.12.1 Intra-frequency SS-SINR accuracy requirements in FR1
92010.1.12.1.1 Absolute SS-SINR Accuracy in FR1 92010.1.12.2
Intra-frequency CSI-SINR accuracy requirements in FR1 92110.1.12.2.1
Absolute CSI-SINR Accuracy in FR1 92110.1.12C Intra-frequency SINR
accuracy requirements for FR1 SAN 92210.1.12C.1 Intra-frequency SS-SINR
accuracy requirements in FR1 92210.1.12C.1.1 Absolute SS-SINR Accuracy
in FR1 92210.1.13 Intra-frequency SINR accuracy requirements for FR2
92310.1.13.1 Intra-frequency SS-SINR accuracy requirements in FR2
92310.1.13.1.1 Absolute SS-SINR Accuracy in FR2 92310.1.13.2
Intra-frequency CSI-SINR accuracy requirements in FR2 92410.1.13.2.1
Absolute CSI-SINR Accuracy in FR2 92410.1.14 Inter-frequency SINR
accuracy requirements for FR1 92410.1.14.1 Inter-frequency SS-SINR
accuracy requirements in FR1 92410.1.14.1.1 Aboslute Accuracy of SS-SINR
in FR1 92410.1.14.1.2 Relative Accuracy of SS-SINR in FR1 92510.1.14.2
Inter-frequency CSI-SINR accuracy requirements in FR1 92610.1.14.2.1
Aboslute Accuracy of CSI-SINR in FR1 92610.1.14.2.2 Relative Accuracy of
CSI-SINR in FR1 92710.1.14C Inter-frequency SINR accuracy requirements
for FR1 SAN 92810.1.14C.1 Inter-frequency SS-SINR accuracy requirements
in FR1 92810.1.14C.1.1 Aboslute Accuracy of SS-SINR in FR1
92810.1.14C.1.2 Relative Accuracy of SS-SINR in FR1 92910.1.15
Inter-frequency SINR accuracy requirements for FR2 93010.1.15.1
Inter-frequency SS-SINR accuracy requirements in FR2 93010.1.15.1.1
Aboslute Accuracy of SS-SINR in FR2 93010.1.15.1.2 Relative Accuracy of
SS-SINR in FR2 93010.1.15.2 Inter-frequency CSI-SINR accuracy
requirements in FR2 93110.1.15.2.1 Aboslute Accuracy of CSI-SINR in FR2
93110.1.15.2.2 Relative Accuracy of CSI-SINR in FR2 93210.1.16 SINR
report mapping 93310.1.16.1 SS-SINR and CSI-SINR measurement report
mapping 93310.1.17 Power Headroom 93410.1.17.1 Power Headroom Report
93410.1.17.1.1 Power Headroom Report Mapping 93410.1.18 P~CMAX,c,f~
93510.1.18.1 Report Mapping 93510.1.19 L1-RSRP accuracy requirements for
FR1 93510.1.19.1 SSB based L1-RSRP accuracy requirements 93510.1.19.1.1
Absolute Accuracy 93510.1.19.1.2 Relative Accuracy 93610.1.19.2 CSI-RS
based L1-RSRP accuracy requirements 93710.1.19.2.1 Absolute Accuracy
93710.1.19.2.2 Relative Accuracy 93810.1.19C L1-RSRP accuracy
requirements for FR1 SAN 93910.1.19C.1 SSB based L1-RSRP accuracy
requirements 93910.1.19C.1.1 Absolute Accuracy 93910.1.19C.1.2 Relative
Accuracy 94010.1.19C.2 CSI-RS based L1-RSRP accuracy requirements
94010.1.19C.2.1 Absolute Accuracy 94010.1.19C.2.2 Relative Accuracy
94110.1.20 L1-RSRP accuracy requirements for FR2 94210.1.20.1 SSB based
L1-RSRP accuracy requirements 94210.1.20.1.1 Absolute Accuracy
94210.1.20.1.2 Relative Accuracy 94210.1.20.2 CSI-RS based L1-RSRP
accuracy requirements 94310.1.20.2.1 Absolute Accuracy 94310.1.20.2.2
Relative Accuracy 94410.1.21 SFTD accuracy requirements 94510.1.21.1
SFTD acuracy requirements for NE-DC 94510.1.21.2 SFTD acuracy
requirements for NR-DC 94710.1.21.3 Inter frequency SFTD acuracy
requirements 94810.1.22 CLI measurement accuracy requirements
94910.1.22.1 SRS-RSRP 94910.1.22.1.1 SRS-RSRP Accuracy 94910.1.22.1.2
SRS-RSRP report mapping 95110.1.22.2 CLI-RSSI 95110.1.22.2.1 CLI-RSSI
Accuracy 95110.1.22.2.2 CLI-RSSI report mapping 95210.1.23 RSTD
Measurements 95310.1.23.1 Introduction 95310.1.23.2 Measurement Accuracy
Requirements 95310.1.23.3 Report mapping 96310.1.23.3.1 Absolute DL RSTD
Measurement Reporting 96310.1.23.3.2 Differential Reporting for DL RSTD
Measurement 96510.1.23.3.3 Additional Path Report Mapping for DL RSTD
96710.1.24 PRS-RSRP Measurements 96910.1.24.1 Introduction 96910.1.24.2
Measurement Accuracy Requirements 96910.1.24.2.1 Absolute PRS RSRP
accuracy 96910.1.24.2.2 Relative PRS RSRP accuracy 97310.1.24.3 Report
mapping 97710.1.24.3.1 Absolute PRS-RSRP Measurement Report Mapping
97710.1.24.3.2 Differential Report Mapping for PRS-RSRP Measurement
97810.1.25 UE Rx-Tx Time Difference Measurements 98010.1.25.1
Introduction 98010.1.25.2 Measurement Accuracy Requirements 98010.1.25.3
Report mapping 99310.1.25.3.1 Absolute UE Rx-Tx Measurement Report
Mapping 99310.1.25.3.2 Differential UE Rx-Tx Measurement Report Mapping
99510.1.25.3.3 Additional Path Report Mapping for UE Rx-Tx Time
Difference 99610.1.26 FR2 P-MPR report 99810.1.26.1 Report mapping
99810.1.27 L1-SINR accuracy requirements for FR1 99810.1.27.1 L1-SINR
accuracy requirements with CSI-RS based CMR and no dedicated IMR
configured 99810.1.27.1.1 Absolute Accuracy 99810.1.27.1.2 Relative
Accuracy 99910.1.27.2 L1-SINR accuracy requirements with SSB based CMR
and dedicated IMR configured 100010.1.27.2.1 Absolute Accuracy
100010.1.27.2.2 Relative Accuracy 100210.1.27.3 L1-SINR accuracy
requirements with CSI-RS based CMR and dedicated IMR configured
100410.1.27.3.1 Absolute Accuracy 100410.1.27.3.2 Relative Accuracy
100610.1.28 L1-SINR accuracy requirements for FR2 100810.1.29
Intra-frequency RSRQ accuracy requirements under CCA 101510.1.29.1
Intra-frequency SS-RSRQ accuracy requirements in FR1 101510.1.29.1.1
Absolute SS-RSRQ Accuracy 101510.1.30 Inter-frequency RSRQ accuracy
requirements under CCA 101510.1.30.1 Inter-frequency SS-RSRQ accuracy
requirements in FR1 101510.1.30.1.1 Aboslute Accuracy of SS-RSRQ
101510.1.30.1.2 Relative Accuracy of SS-RSRQ 101610.1.31 Intra-frequency
SINR accuracy requirements under CCA 101710.1.31.1 Intra-frequency
SS-SINR accuracy requirements in FR1 101710.1.31.1.1 Absolute SS-SINR
Accuracy 101710.1.32 Inter-frequency SINR accuracy requirements under
CCA 101710.1.32.1 Inter-frequency SS-SINR accuracy requirements in FR1
101710.1.32.1.1 Aboslute Accuracy of SS-SINR 101710.1.32.1.2 Relative
Accuracy of SS-SINR 101810.1.33 L1-RSRP accuracy requirements under CCA
101910.1.33.1 SSB based L1-RSRP accuracy requirements in FR1
101910.1.33.1.1 Absolute Accuracy 101910.1.33.1.2 Relative Accuracy
101910.1.34 RSSI measurements under CCA 102010.1.34.1 Intra-frequency
absolute RSSI measurement accuracy requirements in FR1 102010.1.34.2
Inter-frequency absolute RSSI measurement accuracy requirements in FR1
102010.1.34.3 RSSI measurement report mapping 102010.1.35 Channel
occupancy measurements under CCA 102110.1.35.1 Intra-frequency channel
occupancy measurement accuracy requirements in FR1 102110.1.35.2
Inter-frequency channel occupancy measurement accuracy requirements in
FR1 102110.1.36 Intra-frequency RSRP accuracy requirements under CCA
102110.1.36.1 Intra-frequency SS-RSRP accuracy requirements in FR1
102110.1.36.1.1 Absolute SS-RSRP Accuracy 102110.1.36.1.2 Relative
SS-RSRP Accuracy 102210.1.37 Inter-frequency RSRP accuracy requirements
under CCA 102310.1.37.1 Inter-frequency SS-RSRP accuracy requirements in
FR1 102310.1.37.1.1 Absolute Accuracy of SS-RSRP 102310.1.37.1.2
Relative Accuracy of SS-RSRP 102310.1.38 PRS-RSRPP Measurements
102410.1.38.1 Introduction 102410.1.38.2 Measurement Accuracy
Requirements 102410.1.38.2.1 Absolute PRS RSRPP accuracy 102410.1.38.3
Report mapping 102910.1.38.3.1 Absolute PRS-RSRPP Measurement Report
Mapping 102910.1.38.3.2 Differential Report Mapping for PRS-RSRPP
Measurement 1030*10.1.39* UE Rx-Tx time difference measurements for
RTT-based PDC 103110.1.39.1 *Void* 103110.1.39.2 Measurement Accuracy
Requirements for PRS 103110.1.39.3 Measurement Accuracy Requirements for
TRS 103610.1.40 Void 104010.1A NR measurements for RedCap 104010.1A.1
Introduction 104010.1A.2 Intra-frequency RSRP accuracy requirements for
FR1 104010.1A.2.1 Intra-frequency SS-RSRP accuracy requirements
104010.1A.2.1.1 Absolute SS-RSRP Accuracy 104010.1A.2.1.2 Relative
SS-RSRP Accuracy 104110.1A.3 Intra-frequency RSRP accuracy requirements
for FR2 104210.1A.3.1 Intra-frequency SS-RSRP accuracy requirements
104210.1A.3.1.1 Absolute SS-RSRP Accuracy 104210.1A.3.1.2 Relative
SS-RSRP Accuracy 104210.1A.4 Inter-frequency RSRP accuracy requirements
for FR1 104210.1A.4.1 Inter-frequency SS-RSRP accuracy requirements
104210.1A.4.1.1 Absolute Accuracy of SS-RSRP in FR1 104210.1A.4.1.2
Relative Accuracy of SS-RSRP in FR1 104310.1A.5 Inter-frequency RSRP
accuracy requirements for FR2 104410.1A.5.1 Inter-frequency SS-RSRP
accuracy requirements 104410.1A.5.1.1 Absolute SS-RSRP Accuracy
104410.1A.5.1.2 Relative SS-RSRP Accuracy 104410.1A.6 Intra-frequency
RSRQ accuracy requirements for FR1 104410.1A.6.1 Intra-frequency SS-RSRQ
accuracy requirements in FR1 104410.1A.6.1.1 Absolute SS-RSRQ Accuracy
in FR1 104410.1A.7 Intra-frequency RSRQ accuracy requirements for FR2
104510.1A.7.1 Intra-frequency SS-RSRQ accuracy requirements in FR2
104510.1A.7.1.1 Absolute SS-RSRQ Accuracy in FR2 104510.1A.8
Inter-frequency RSRQ accuracy requirements for FR1 104510.1A.8.1
Inter-frequency SS-RSRQ accuracy requirements in FR1 104510.1A.8.1.1
Absolute Accuracy of SS-RSRQ in FR1 104510.1A.8.1.2 Relative Accuracy of
SS-RSRQ in FR1 104610.1A.9 Inter-frequency RSRQ accuracy requirements
for FR2 104710.1A.9.1 Inter-frequency SS-RSRQ accuracy requirements in
FR2 104710.1A.9.1.1 Absolute Accuracy of SS-RSRQ in FR2 104710.1A.9.1.2
Relative Accuracy of SS-RSRQ in FR2 104710.1A.10 Intra-frequency SINR
accuracy requirements for FR1 104710.1A.10.1 Intra-frequency SS-SINR
accuracy requirements in FR1 104710.1A.10.1.1 Absolute SS-SINR Accuracy
in FR1 104710.1A.11 Intra-frequency SINR accuracy requirements for FR2
104810.1A.11.1 Intra-frequency SS-SINR accuracy requirements in FR2
104810.1A.11.1.1 Absolute SS-SINR Accuracy in FR2 104810.1A.12
Inter-frequency SINR accuracy requirements for FR1 104810.1A.12.1
Inter-frequency SS-SINR accuracy requirements in FR1 104810.1A.12.1.1
Aboslute Accuracy of SS-SINR in FR1 104810.1A.12.1.2 Relative Accuracy
of SS-SINR in FR1 104910.1A.13 Inter-frequency SINR accuracy
requirements for FR2 105010.1A.13.1 Inter-frequency SS-SINR accuracy
requirements in FR2 105010.1A.13.1.1 Aboslute Accuracy of SS-SINR in FR2
105010.1A.13.1.2 Relative Accuracy of SS-SINR in FR2 105010.1A.14
L1-RSRP accuracy requirements for FR1 105010.1A.14.1 SSB based L1-RSRP
accuracy requirements 105010.1A.14.1.1 Absolute Accuracy
105010.1A.14.1.2 Relative Accuracy 105110.1A.14.2 CSI-RS based L1-RSRP
accuracy requirements 105210.1A.14.2.1 Absolute Accuracy
105210.1A.14.2.2 Relative Accuracy 105310.1A.15 L1-RSRP accuracy
requirements for FR2 105410.1A.15.1 SSB based L1-RSRP accuracy
requirements 105410.1A.15.1.1 Absolute Accuracy 105410.1A.15.1.2
Relative Accuracy 105410.1A.15.2 CSI-RS based L1-RSRP accuracy
requirements 105410.1A.15.2.1 Absolute Accuracy 105410.1A.15.2.2
Relative Accuracy 105410.2 E-UTRAN measurements 105510.2.1 Introduction
105510.2.2 E-UTRAN RSRP measurements 105510.2.3 E-UTRAN RSRQ
measurements 105510.2.4 E-UTRAN RSTD measurements 105510.2.5 E-UTRAN
RS-SINR measurements 105610.2.6 E-UTRAN RSRP measurements for CA/DC Idle
Mode Measurements 105610.2.7 E-UTRAN RSRQ measurements for CA/DC Idle
Mode Measurements 105610.2A E-UTRAN measurements for RedCap 105710.2A.1
Introduction 105710.2A.2 E-UTRAN RSRP measurements 105710.2A.3 E-UTRAN
RSRQ measurements 105710.2A.4 E-UTRAN RS-SINR measurements 105810.3
UTRAN FDD Measurements 105810.3.1 UTRAN FDD CPICH RSCP 105810.3.2 UTRAN
FDD CPICH Ec/No 105910.4 V2X measurements 105910.4.1 Introduction
105910.4.2 Intra-frequency PSBCH-RSRP accuracy requirements for FR1
105910.4.2.1 PSBCH-RSRP Absolute Accuracy 105910.4.2.2 PSBCH-RSRP
Relative Accuracy 106010.4.3 Intra-Frequency SL-RSSI Measurement
Accuracy Requirements for FR1 106110.4.3.1 Absolute SL-RSSI Accuracy
106110.4.4 Intra-Frequency L1 SL-RSRP Measurement Accuracy Requirements
for FR1 106110.4.4.1 Absolute L1 SL-RSRP Accuracy 106110.4.5
Intra-Frequency Discovery Signal Measurement Accuracy Requirements
106210.4.5.1 Absolute Discovery Signal Measurement Accuracy 106211 Void
106312 V2X Requirements 105912.1 Introduction 105912.2 UE Transmit
Timing 105912.2.1 Introduction 105912.2.2 GNSS as synchronization
reference source 105912.2.3 NR Cell as synchronization reference source
106012.2.4 E-URTAN Cell as synchronization reference source 106012.2.5
SyncRef UE as synchronization reference source 106112.3 Initiation/Cease
of SLSS Transmissions 106112.3.1 Introduction 106112.3.1.1
Initiation/Cease of SLSS transmissions with NR cell as synchronization
reference source 106112.3.1.2 Initiation/Cease of SLSS transmissions
with EUTRAN cell as synchronization reference source 106212.3.1.3
Initiation/Cease of SLSS transmissions with GNSS as synchronization
reference source 106312.3.1.4 Initiation/Cease of SLSS transmissions
with SyncRef UE as synchronization reference source 106312.4 Selection /
Reselection of V2X Synchronization Reference Source 106412.5 L1 SL-RSRP
measurements 106512.5.1 Introduction 106512.5.2 SL-RSRP measurements
106612.6 Congestion Control measurements 106612.7 Interruption
106612.7.1 Interruptions to WAN due to V2X Sidelink Communication
106612.7.2 V2X Sidelink Communication Dropping due to synchronization
source change 106712.7.3 Interruptions to WAN due to switching between
E-UTRA V2X Sidelink and NR V2X Sidelink 106812.7.4 Interruptions to WAN
at transitions between active and non-active during SL-DRX 106912.7.5
Interruptions to V2X sidelink at transitions between active and
non-active during DRX 106912.7.6 Interruptions to V2X sidelink due to
Active BWP switching Requirement 107012.7.7 Interruptions to WAN due to
SyncRef UE detection and/or Sensing during SL DRX off duration
107012.7.8 Interruptions at NR sidelink discovery configuration 107012.8
Reliability of GNSS signal 107112.9 Scheduling availability 107112.9.1
Scheduling availability of UE switching between E-UTRA sidelink and NR
sidelink 107112.9.2 Scheduling availability of UE switching between Uu
uplink and V2X sidelink 107112.10 Selection / Reselection of relay UE
107212.10.1 Introduction 107212.10.2 Selection / Reselection of relay UE
107213 Measurement Performance Requirements for NR gNB 107213.1 UL-RTOA
107213.1.1 Report mapping 107213.1.1A Additional Path Report Mapping for
UL-RTOA 107413.2 gNB Rx-Tx time difference 107613.2.1 Report mapping
107613.2.1A Additional Path Report Mapping for gNB Rx-Tx 107813.2.2
Measurement Accuracy Requirements 108013.2.2.1 Introduction 108013.3 UL
SRS RSRP measurement 108113.3.1 Report mapping 108113.3.2 Measurement
accuracy requirements 108213.3.2.1 Introduction 108213.3.2.2
Requirements 108213.4 AoA/ZoA 108313.4.1 Report mapping 108313.5 Timing
advance (T~ADV~) 108413.5.1 Report mapping 108413.6 UL SRS RSRPP
measurement 108513.6.1 Report mapping 108513.7 gNB Rx-Tx time difference
measurements for RTT-based PDC 108713.7.1 Report mapping 108713.7.2
Measurement Accuracy Requirements 108713.7.2.1 Introduction 108713.7.2.2
Requirements 1087Annex A (normative): Test Cases 1089A.1 Purpose of
annex 1089A.2 Requirement classification for statistical testing
1089A.2.1 Types of requirements in TS 38.133 1089A.2.1.1 Time and delay
requirements on UE higher layer actions 1089A.2.1.2 Measurements of
power levels, relative powers and time 1089A.2.1.3 Implementation
requirements 1090A.2.1.4 Physical layer timing requirements 1090A.2.1.5
Requirements under CCA 1090A.3 RRM test configurations 1091A.3.1
Reference measurement channels 1091A.3.1.1 PDSCH 1091A.3.1.1.1 FDD
1091A.3.1.1.2 TDD 1092A.3.1.2 CORESET for RMSI scheduling 1095A.3.1.2.1
FDD 1095A.3.1.2.2 TDD 1096A.3.1.3 CORESET for RMC scheduling
1099A.3.1.3.1 FDD 1099A.3.1.3.2 TDD 1101A.3.1.4 TDD UL/DL configuration
1106A.3.1A Reference measurement channels under CCA 1108A.3.1A.1 PDSCH
1108A.3.1A.1.1 TDD 1108A.3.1A.2 CORESET for RMSI scheduling
1109A.3.1A.2.1 TDD 1109A.3.1A.3 CORESET for RMC scheduling
1110A.3.1A.3.1 TDD 1110A.3.1A.4 TDD UL/DL configuration 1111A.3.1A.5 RMC
burst transmission model 1111A.3.2 OFDMA channel noise generator (OCNG)
1111A.3.2.1 Generic OFDMA Channel Noise Generator (OCNG) 1111A.3.2.1.1
OCNG pattern 1: Generic OCNG pattern for all unused REs 1112A.3.2.1.2
OCNG pattern 2: Generic OCNG pattern for all unused REs for 2AoA setup
1112A.3.2.1.3 OCNG pattern 3: Generic OCNG pattern for unused REs in the
same bandwidth as CORESET 1113A.3.2.1.4 OCNG pattern 4: Generic OCNG
pattern for all unused REs outside SSB slot(s) 1113A.3.2.2 Void
1114A.3.3 Reference DRX configurations 1114A.3.3.1 DRX Configuration 1:
DRX cycle = 40 ms and TAT = 500 ms 1114A.3.3.2 DRX Configuration 2: DRX
cycle = 640 ms and TAT = 500 ms 1115A.3.3.3 DRX Configuration 3: DRX
cycle = 40 ms and TAT = Infinity 1115A.3.3.4 DRX Configuration 4: DRX
cycle = 160 ms and TAT = Infinity 1115A.3.3.5 DRX Configuration 5: DRX
cycle = 320 ms and TAT = Infinity 1116A.3.3.6 DRX Configuration 6: DRX
cycle = 320 ms and TAT = 500 ms 1116A.3.3.7 DRX Configuration 7: DRX
cycle = 640 ms and TAT = Infinity 1116A.3.3.8 DRX Configuration 8: DRX
cycle = 320 ms and TAT = Infinity 1117A.3.3.9 DRX Configuration 9: DRX
cycle = 40 ms and TAT = 500 ms 1117A.3.3.10 DRX Configuration 10: DRX
cycle = 640 ms and TAT = 500 ms 1117A.3.3.11 DRX Configuration 11: DRX
cycle = 20 ms and TAT = Infinity 1118A.3.3.12 DRX Configuration 12: DRX
cycle = 640 ms and TAT = Infinity 1118A.3.3.13 DRX Configuration X1: DRX
cycle = 80 ms and TAT = Infinity 1118A.3.3.14 DRX Configuration 14: DRX
cycle = 160 ms and TAT = Infinity 1119A.3.4 Test Cases with Different
Channel Bandwidths 1119A.3.4.1 Test Cases with Different E-UTRA Channel
Bandwidths 1119A.3.4.1.1 Introduction 1119A.3.4.1.2 Principle of testing
1119A.3.5 Test Cases for Synchronous and Asynchronous DC Operations
1119A.3.5.1 EN-DC Test Cases for Synchronous and Asynchronous EN-DC
Operations 1119A.3.5.1.1 Introduction 1119A.3.5.1.2 Principle of Testing
1119A.3.6 Antenna configurations 1120A.3.6.1 Antenna configurations for
FR1 1120A.3.6.1.1 Antenna connection for 4 Rx capable UEs
1120A.3.6.1.1.1 Introduction 1120A.3.6.1.1.2 Principle of testing
1120A.3.6.2 Antenna configurations for FR2 1123A.3.6A Antenna
configurations with unlicensed bands 1123A.3.6A.1 Antenna configurations
for FR1 1123A.3.6A.1.1 Antenna connection for 4 Rx capable UEs
1123A.3.6A.1.1.1 Introduction 1123A.3.6A.1.1.2 Principle of testing
1123A.3.7 EN-DC test setup 1125A.3.7.1 Introduction 1125A.3.7.2 E-UTRAN
Serving Cell Parameters 1125A.3.7.2.1 E-UTRAN Serving Cell Parameters
for Tests with NR Cell(s) in FR1 1125A.3.7.2.2 E-UTRAN Serving Cell
Parameters for Tests with NR Cell(s) in FR2 1126A.3.7A NR FR1-FR2 test
setup 1127A.3.7B EN-DC test setup with unlicensed bands 1128A.3.7B.1
Introduction 1128A.3.7B.2 E-UTRAN Serving Cell Parameters 1128A.3.7B.2.1
E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) under CCA in
FR1 1128A.3.7C LTE-FR1/FR2 test setup 1129A.3.7D NE-DC test setup
1129A.3.7D.1 Introduction 1129A.3.7D.2 E-UTRAN Serving Cell Parameters
1129A.3.7D.2.1 E-UTRAN Serving Cell Parameters for Tests with NR Cell(s)
in FR1 1129A.3.7D.2.2 E-UTRAN Serving Cell Parameters for Tests with NR
Cell(s) in FR2 1129A.3.8 PRACH configurations 1129A.3.8.1 Introduction
1129A.3.8.2 PRACH configurations in FR1 1130A.3.8.2.1 FR1 PRACH
configuration 1 1130A.3.8.2.2 FR1 PRACH configuration 2 1130A.3.8.2.3
FR1 PRACH configuration 3 1131A.3.8.2.4 FR1 PRACH configuration 4
1132A.3.8.3 PRACH configurations in FR2 1133A.3.8.3.1 FR2 PRACH
configuration 1 1133A.3.8.3.2 FR2 PRACH configuration 2 1134A.3.8.3.3
FR2 PRACH configuration 3 1135A.3.8.3.4 FR2 PRACH configuration 4
1136A.3.8A PRACH configurations under CCA 1137A.3.8A.1 Introduction
1137A.3.8A.2 PRACH configurations in FR1 1137A.3.8A.2.1 FR1 PRACH
configuration 1 under CCA 1137A.3.8A.2.2 FR1 PRACH configuration 2 under
CCA 1138A.3.9 BWP configurations 1139A.3.9.1 Introduction 1139A.3.9.2
Downlink BWP configurations 1140A.3.9.2.1 Initial BWP 1140A.3.9.2.2
Dedicated BWP 1140A.3.9.3 Uplink BWP configurations 1141A.3.9.3.1
Initial BWP 1141A.3.9.3.2 Dedicated BWP 1141A.3.9A BWP configurations
for RedCap 1141A.3.9A.1 Introduction 1141A.3.9A.2 Downlink BWP
configurations 1142A.3.9A.2.1 Dedicated BWP 1142A.3.9A.3 Uplink BWP
configurations 1142A.3.9A.3.1 Dedicated BWP 1142A.3.10 SSB
Configurations 1143A.3.10.1 SSB Configurations for FR1 1143A.3.10.1.1
SSB pattern 1 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz
1143A.3.10.1.2 SSB pattern 2 in FR1: SSB allocation for SSB SCS=30 kHz
in 40 MHz 1143A.3.10.1.3 SSB pattern 3 in FR1: SSB allocation for SSB
SCS=15 kHz in 10 MHz 1144A.3.10.1.4 SSB pattern 4 in FR1: SSB allocation
for SSB SCS=30 kHz in 40 MHz 1144A.3.10.1.5 SSB pattern 5 in FR1: SSB
allocation for SSB SCS=15 kHz starting from odd SFN in 10 MHz
1145A.3.10.1.6 SSB pattern 6 in FR1: SSB allocation for SSB SCS=30 kHz
starting from odd SFN in 40 MHz 1145A.3.10.1.7 SSB pattern 7 in FR1: SSB
allocation for SSB SCS=15 kHz in 10 MHz 1146A.3.10.1.8 SSB pattern 8 in
FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz 1146A.3.10.2 SSB
Configurations for FR2 1147A.3.10.2.1 SSB pattern 1 in FR2: SSB
allocation for SSB SCS=120 kHz in 100 MHz 1147A.3.10.2.2 SSB pattern 2
in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz 1147A.3.10.2.3 SSB
pattern 3 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz
1148A.3.10.2.4 SSB pattern 4 in FR2: SSB allocation for SSB SCS=240 kHz
in 100 MHz 1148A.3.10.2.5 SSB pattern 5 in FR2: SSB allocation for SSB
SCS=120 kHz in 100 MHz 1149A.3.10.2.6 SSB pattern 6 in FR2: SSB
allocation for SSB SCS=240 kHz in 100 MHz 1149A.3.10.2.7 SSB pattern 7
in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz 1150A.3.10.2.8 SSB
pattern 8 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz
1150A.3.10.2.9 SSB pattern 9 in FR2: SSB allocation for SSB SCS=120 kHz
in 100 MHz 1151A.3.10.2.10 SSB pattern 10 in FR2: SSB allocation for SSB
SCS=240 kHz in 100 MHz 1151A.3.10.2.11 SSB pattern 11 in FR2: SSB
allocation for SSB SCS=480 kHz in 400 MHz 1152A.3.10.2.12 SSB pattern 12
in FR2: SSB allocation for SSB SCS=960 kHz in 400 MHz 1152A.3.10.2.13
SSB pattern 13 in FR2: SSB allocation for SSB SCS=480 kHz in 400 MHz
1153A.3.10.2.14 SSB pattern 14 in FR2: SSB allocation for SSB SCS=960
kHz in 400 MHz 1153A.3.10.2.15 SSB pattern 15 in FR2: SSB allocation for
SSB SCS=480 kHz in 400 MHz 1154A.3.10.2.16 SSB pattern 16 in FR2: SSB
allocation for SSB SCS=960 kHz in 400 MHz 1154A.3.10.2.17 SSB pattern 17
in FR2: SSB allocation for SSB SCS=480 kHz in 400 MHz 1155A.3.10.2.18
SSB pattern 18 in FR2: SSB allocation for SSB SCS=960 kHz in 400 MHz
1155A.3.10A SSB Configurations under CCA 1156A.3.10A.1 SSB
Configurations under CCA for FR1 1156A.3.10A.1.1 SSB pattern 1 under CCA
for semi-static channel access: SSB allocation for SSB SCS=30kHz in
40MHz 1156A.3.10A.1.2 SSB pattern 2 under CCA for dynamic channel
access: SSB allocation for SSB SCS=30kHz in 40MHz 1156A.3.10A.1.3 SSB
pattern 3 under CCA for semi-static channel access: SSB allocation for
SSB SCS=30 kHz in 40 MHz 1157A.3.10A.1.4 SSB pattern 4 under CCA for
dynamic channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz
1157A.3.10B SSB Configurations for RedCap 1158A.3.10B.1 SSB
Configurations for FR1 1158A.3.10B.1.1 SSB pattern 1 for RedCap in FR1:
SSB allocation for SSB SCS=30 kHz in 20 MHz 1158A.3.10B.1.2 SSB pattern
2 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz
1158A.3.10B.1.3 SSB pattern 3 for RedCap in FR1: SSB allocation for SSB
SCS=30 kHz starting from odd SFN in 20 MHz 1159A.3.10B.1.4 SSB pattern 4
for RedCap in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz
1159A.3.10B.1.5 SSB pattern 5 for RedCap in FR1: SSB allocation for SSB
SCS=30 kHz in 20 MHz 1160A.3.10B.1.6 SSB pattern 6 for RedCap in FR1:
SSB allocation for SSB SCS=15 kHz in 10 MHz 1160A.3.10B.1.7 SSB pattern
7 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz
1161A.3.10B.2 SSB Configurations for FR2 1161A.3.10B.2.1 SSB pattern 1
for RedCap in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz
1161A.3.10B.2.2 SSB pattern 2 for RedCap in FR2: SSB allocation for SSB
SCS=120 kHz in 100 MHz 1162A.3.10B.2.3 SSB pattern 3 for RedCap in FR2:
SSB allocation for SSB SCS=120 kHz in 100 MHz 1162A.3.10B.2.4 SSB
pattern 4 for RedCap in FR2: SSB allocation for SSB SCS=240 kHz in 100
MHz 1163A.3.10B.2.5 SSB pattern 5 for RedCap in FR2: SSB allocation for
SSB SCS=240 kHz in 100 MHz 1163A.3.11 SMTC Configurations 1164A.3.11.1
SMTC pattern 1: SMTC period = 20 ms with SMTC duration = 1 ms
1164A.3.11.2 SMTC pattern 2: SMTC period = 20 ms with SMTC duration = 5
ms 1164A.3.11.3 SMTC pattern 3: SMTC period = 160 ms with SMTC duration
= 1 ms 1164A.3.11.4 SMTC pattern 4: SMTC period = 20 ms with SMTC
duration = 1 ms 1164A.3.11.5 SMTC pattern 5: SMTC period = 20 ms with
SMTC duration = 5 ms 1165A.3.11.6 SMTC pattern 6: SMTC period = 20 ms
with SMTC duration = 5 ms 1165A.3.11.7 SMTC pattern 7: SMTC period = 20
ms with SMTC duration = 5 ms 1165A.3.11.8 SMTC pattern 8: SMTC period =
10 ms with SMTC duration = 1 ms 1165A.3.11.9 SMTC pattern 9: SMTC period
= 20 ms with SMTC duration = 1 ms 1165A.3.11A SMTC Configurations for
RedCap 1166A.3.11A.1 SMTC pattern 1 for RedCap: SMTC period = 40 ms with
SMTC duration = 1 ms 1166A.3.11A.2 SMTC pattern 2 for RedCap: SMTC
period = 80 ms with SMTC duration = 1 ms 1166A.3.11A.3 SMTC pattern 3
for RedCap: SMTC period = 40 ms with SMTC duration = 1 ms 1166A.3.11A.4
SMTC pattern 4 for RedCap: SMTC period = 80 ms with SMTC duration = 5 ms
1166A.3.11.12 SMTC pattern 12: SMTC period = 20 ms with SMTC duration =
5 ms 1166A.3.12 Test Cases with Different CC Configurations 1167A.3.12.1
EN-DC Test Cases with Different EN-DC Configurations 1167A.3.12.1.1
Introduction 1167A.3.12.1.2 Principle of testing 1167A.3.12.2 Carrier
Aggregation Test Cases with Different CA Configurations 1167A.3.12.2.1
Introduction 1167A.3.12.2.2 Principle of testing 1167A.3.13 Test Cases
in SA and EN-DC Operations 1167A.3.13.1 Introduction 1167A.3.13.2
Principle of Testing 1168A.3.13A Test Cases involving E-UTRA/FR1 and FR2
carriers 1168A.3.13A.1 Introduction 1168A.3.13A.2 Principle of Testing
in EN-DC 1168A.3.13A.3 Principle of Testing in SA 1169A.3.13A.4
Principle of Testing in E-UTRA 1170A.3.13B Test Cases for EN-DC and
NE-DC Operations 1171A.3.13B.1 Active BWP switch Test Cases for EN-DC
and NE-DC Operations 1171A.3.13B.1.1 Introduction 1171A.3.13B.1.2
Principle of Testing 1171A.3.13B.2 SFTD accuracy Test Cases for EN-DC
and NE-DC Operations 1171A.3.13B.2.1 Introduction 1171A.3.13B.2.2
Principle of Testing 1171A.3.14 CSI-RS configurations 1172A.3.14.1 FDD
1172A.3.14.2 TDD 1174A.3.15 Angle of Arrival (AoA) for FR2 RRM test
cases 1180A.3.15.1 Setup 1: Single AoA in Rx beam peak direction
1180A.3.15.2 Setup 2: Single AoA in non Rx beam peak direction
1180A.3.15.2.1 Setup 2a: Single AoA in non Rx beam peak direction
without change in direction 1180A.3.15.2.2 Setup 2b: Single AoA in non
Rx beam peak direction with change in direction 1181A.3.15.3 Setup 3: 2
AoAs 1181A.3.15.4 Setup 4: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in
non Rx beam peak 1181A.3.15.4.1 Setup 4a: 2 AoAs, 1 AoA in Rx beam peak
direction, 1 in non Rx beam peak without change in direction
1181A.3.15.4.2 Setup 4b: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in
non Rx beam peak with change in direction 1181A.3.16 TCI State
Configuration 1182A.3.16.1 Introduction 1182A.3.16.2 TCI states
1182A.3.16A Unified TCI State Configuration 1182A.3.16A.1 Introduction
1182A.3.16A.2 DLorJoint TCI states 1183A.3.16A.3 UL TCI states
1183A.3.17 Configurations of CSI-RS for tracking 1184A.3.17.1
Configuration of CSI-RS for tracking for FR1 1184A.3.17.1.1 FDD
1184A.3.17.1.2 TDD 1186A.3.17.2 Configuration of CSI-RS for tracking for
FR2 1188A.3.17.2.1 TDD 1188A.3.18 Additional definitions related to OTA
testing for FR2 RRM test cases 1189A.3.18.1 Introduction 1189A.3.18.2
PRACH Power Measurement 1189A.3.19 Test applicability for DAPS handover
1189A.3.19.1 Introduction 1189A.3.19.2 Principle of testing 1189A.3.20
MsgA configurations 1190A.3.20.1 Introduction 1190A.3.20.2 MsgA
configurations in FR1 1190A.3.20.2.1 FR1 MsgA configuration 1
1190A.3.20.2.2 FR1 MsgA configuration 2 1191A.3.20.3 MsgA configurations
in FR2 1193A.3.20.3.1 FR2 MsgA configuration 1 1193A.3.20.3.2 FR2 MsgA
configuration 2 1194A.3.20A MsgA configurations under CCA 1196A.3.20A.1
Introduction 1196A.3.20A.2 MsgA configurations in FR1 1196A.3.20A.2.1
FR1 MsgA configuration 1 under CCA 1196A.3.20A.2.2 FR1 MsgA
configuration 2 under CCA 1197A.**3.21** V2X sidelink communication
1200A.3.21.1 Introduction 1200A.3.21.2 Reference resource pool
configurations for V2X Sidelink Communication 1200A.3.21.3 Reference
measurement channels for V2X Sidelink Communication 1204A.3.21.4
Reference SL-DRX configurations 1205A.3.21.4.1 SL-DRX Configuration 1:
SL-DRX cycle = 40 ms 1205A.3.21.4.2 SL-DRX Configuration 2: SL-DRX cycle
= 320 ms 1205A.3.21.4.3 SL-DRX Configuration 3: SL-DRX cycle = 640 ms
1205A.3.22 CSI-IM configurations 1205A.3.22.1 FDD 1205A.3.22.2 TDD
1206A.3.23 Spatial Relation Configuration 1207A.3.23.1 Introduction
1207A.3.23.2 Spatial Relation 1208A.3.24 SRS configuration 1209A.3.25
Channel bandwidth (CBW) configurations 1211A.3.25.1 DL UE specific CBW
1211A.3.25.2 UL UE specific CBW 1212A.3.26 CCA model 1212A.3.26.1
Introduction 1212A.3.26.2 CCA model for operation on a carrier frequency
with CCA in FR1 1212A.3.26.2.1 DL CCA model 1212A.3.26.2.2 UL CCA model
1214A.3.26.3 CCA model for operation on a carrier frequency with CCA in
FR2-2 1214A.3.26.3.1 DL CCA model 1214A.3.26.3.2 UL CCA model 1215A.3.27
Test Cases with at Least One Cell on a Carrier Frequency with CCA
1215A.3.27.1 Introduction 1215A.3.27.2 NR Standalone Tests with NR SCell
under CCA and All Other NR Cells in FR1 1215A.3.27.3 EN-DC Tests with NR
PSCell under CCA and Other NR Cells in FR1 1216A.3.27.4 NR Standalone
Tests with NR PCell under CCA and Other NR Cells in FR1 1216A.3.27.5
E-UTRA Standalone Tests with at Least One NR Cell under CCA 1216A.3.28
Discovery Burst Transmission Window configuration under CCA 1216A.3.28.1
DBT Window pattern 1: DBT Window period = 20 ms with DBT Window duration
= 1 ms 1216A.3.29 Testing principles for UE capable of only NR bands
with shared spectrum access 1216A.3.29.1 Introduction 1216A.3.29.2
Principle of testing for UE capable of EN-DC with only NR bands with
shared spectrum access 1216A.3.29.3 Principle of testing for UE capable
of SA operation with only NR bands with shared spectrum access
1217A.3.30 CSI-RS configurations for RRM 1218A.3.30.1 FDD 1218A.3.30.2
TDD 1219A.3.31 PRS Configurations 1221A.3.31.1. PRS Configurations for
FR1 1221A.3.31.1.1. PRS pattern 1 in FR1: SCS=15 KHz 1221A.3.31.1.2. PRS
pattern 2 in FR1: SCS=30 KHz 1222A.3.31.2. PRS Configurations for FR2
1222A.3.31.2.1. PRS pattern 1 in FR2: SCS=120 KHz 1222A.3.32 NR sidelink
discovery 1222A.3.32.1 Introduction 1222A.3.32.2 Reference resource pool
configurations for NR Sidelink Discovery 1222A.3.32.3 Principle of
Testing 1223A.3.33 PRS Processing Window (PPW) configurations 1223A.3.34
Testing principles for test cases related to PRS measurements
1223A.3.34.1 Introduction 1223A.3.34.2 Test cases in RRC\_INACTIVE state
1224A.3.34.3 Test cases for PRS measurements with gaps in RRC\_CONNECTED
state 1224A.3.34.4 Test cases for PRS measurements without gaps in
RRC\_CONNECTED state 1224A.3.35 Testing principle for RedCap UE
1225A.3.35.1 Introduction 1225A.3.35.2 Principle of testing for FR1
1225A.3.35.3 Principle of testing for FR2 1225A.3.36 Testing related to
Satellite access 1225A.3.36.1 Introduction 1225A.3.36.2 Principle of
testing GSO and NGSO scenarios 1225A.3.36.2 Principle of testing
different RRM requirements 1226A.3.36.3 Principle of testing different
ephemeris formats 1226A.3.36.4 General setup for SIB19 1228A.3.36.5
Satellite specific parameters configuration 1229A.3.36.5.1 Satellite
specific configuration for serving cell 1229A.3.36.5.2 Satellite
specific configuration for neighbour cell 1230A.4 EN-DC tests with all
NR cells in FR1 1227A.4.1 Void 1227A.4.2 Void 1227A.4.3 RRC\_CONNECTED
state mobility 1227A.4.3.1 Void 1227A.4.3.2 RRC Connection Mobility
Control 1227A.4.3.2.1 Void 1227A.4.3.2.2 Random Access 1227A.4.3.2.2.1
4-step RA type contention based random access test in FR1 for PSCell in
EN-DC 1227A.4.3.2.2.2 4-step RA type n on-contention based random access
test in FR1 for PSCell in EN-DC 1231A.4.3.2.2.3 2-step RA type
contention based random access test in FR1 for PSCell in EN-DC
1235A.4.3.2.2.4 2-step RA type n on-contention based random access test
in FR1 for PSCell in EN-DC 1239A.4.3.2.3 Void 1243A.4.3.3 Handover with
PSCell from EN-DC to EN-DC with known target PSCell in FR1 1243A.4.3.3.1
Test Purpose and Environment 1243A.4.3.3.2 Test Requirements 1249A.4.4
Timing 1250A.4.4.1 UE transmit timing 1250A.4.4.1.1 NR UE Transmit
Timing Test for FR1 1250A.4.4.1.1.1 Test Purpose and environment
1250A.4.4.1.1.2 Test requirements 1254A.4.4.2 UE timer accuracy
1254A.4.4.3 Timing advance 1254A.4.4.3.1 EN-DC FR1 timing advance
adjustment accuracy 1254A.4.4.3.1.1 Test Purpose and Environment
1254A.4.4.3.1.2 Test Parameters 1254A.4.4.3.1.3 Test Requirements
1258A.4.5 Signaling characteristics 1258A.4.5.1 Radio link Monitoring
1258A.4.5.1.1 Radio Link Monitoring Out-of-sync Test for FR1 PSCell
configured with SSB-based RLM RS in non-DRX mode 1259A.4.5.1.1.1 Test
Purpose and Environment 1259A.4.5.1.1.2 Test Requirements 1263A.4.5.1.2
Radio Link Monitoring In-sync Test for FR1 PSCell configured with
SSB-based RLM RS in non-DRX mode 1263A.4.5.1.2.1 Test Purpose and
Environment 1263A.4.5.1.2.2 Test Requirements 1269A.4.5.1.3 Radio Link
Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM
RS in DRX mode 1269A.4.5.1.3.1 Test Purpose and Environment
1269A.4.5.1.3.2 Test Requirements 1274A.4.5.1.4 Radio Link Monitoring
In-sync Test for FR1 PSCell configured with SSB-based RLM RS in DRX mode
1274A.4.5.1.4.1 Test Purpose and Environment 1274A.4.5.1.4.2 Test
Requirements 1280A.4.5.1.5 EN-DC Radio Link Monitoring Out-of-sync Test
for FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode
1280A.4.5.1.5.1 Test Purpose and Environment 1280A.4.5.1.5.2 Test
Requirements 1285A.4.5.1.6 EN-DC Radio Link Monitoring In-sync Test for
FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode
1285A.4.5.1.6.1 Test Purpose and Environment 1285A.4.5.1.6.2 Test
Requirements 1291A.4.5.1.7 EN-DC Radio Link Monitoring Out-of-sync Test
for FR1 PSCell configured with CSI-RS-based RLM in DRX mode
1291A.4.5.1.7.1 Test Purpose and Environment 1291A.4.5.1.7.2 Test
Requirements 1296A.4.5.1.8 EN-DC Radio Link Monitoring In-sync Test for
FR1 PSCell configured with CSI-RS-based RLM in DRX mode 1297A.4.5.1.8.1
Test Purpose and Environment 1297A.4.5.1.8.2 Test Requirements
1302A.4.5.1.9 Radio Link Monitoring Out-of-sync Test for FR1 PSCell
configured with SSB-based RLM RS for UE fulfilling relaxed measurement
criterion 1302A.4.5.1.9.1 Test Purpose and Environment 1302A.4.5.2
Interruption 1308**A.4.5.2.1** E-UTRAN -- NR FR1 interruptions at
transitions between active and non-active during DRX in synchronous
EN-DC 1308A.4.5.2.1.1 Test Purpose and Environment 1308A.4.5.2.1.2 Test
Requirements 1312**A.4.5.2.2** E-UTRAN -- NR FR1 interruptions at
transitions between active and non-active during DRX in asynchronous
EN-DC 1312A.4.5.2.2.1 Test Purpose and Environment 1312A.4.5.2.2.2 Test
Requirements 1316**A.4.5.2.3** E-UTRAN -- NR FR1 interruptions during
measurements on deactivated NR SCC in synchronous EN-DC 1316A.4.5.2.3.1
Test Purpose and Environment 1316A.4.5.2.3.2 Test Requirements
1323A.4.5.2.4 E-UTRAN -- NR FR1 interruptions during measurements on
deactivated NR SCC in asynchronous EN-DC 1324A.4.5.2.4.1 Test Purpose
and Environment 1324A.4.5.2.4.2 Test Requirements 1328**A.4.5.2.5**
E-UTRAN -- NR FR1 interruptions during measurements on deactivated
E-UTRAN SCC in synchronous EN-DC 1329A.4.5.2.5.1 Test Purpose and
Environment 1329A.4.5.2.5.2 Test Requirements 1332**A.4.5.2.6** E-UTRAN
-- NR FR1 interruptions during measurements on deactivated E-UTRAN SCC
in asynchronous EN-DC 1332A.4.5.2.6.1 Test Purpose and Environment
1332A.4.5.2.6.2 Test Requirements 1336A.4.5.2.7 Void 1336**A.4.5.2.8**
**E-UTRAN - NR FR1 i**nterruptions at NR SRS carrier based switching in
asynchronous EN-DC 1336A.4.5.2.8.1 Test Purpose and Environment
1336A.4.5.2.8.2 Test Requirements 1339**A.4.5.2.9** E-UTRAN -- NR
interruptions at E-UTRA SRS carrier based switching 1340A.4.5.2.9.1 Test
Purpose and Environment 1340A.4.5.2.9.2 Test Requirements
1343**A.4.5.2.10** E-UTRAN -- NR FR1 interruptions due to RRM and
RLM/BFD measurements on deactivated NR PSCell 1344A.4.5.2.10.1 Test
Purpose and Environment 1344A.4.5.2.10.2 Test Requirements
1347**A.4.5.2.11** **E-UTRAN - NR FR1 i**nterruptions at NR SRS antenna
port switching with 1 SRS symbol in a slot in synchronous EN-DC
1347A.4.5.2.11.1 Test Purpose and Environment 1347A.4.5.2.11.2 Test
Requirements 1352**A.4.5.2.12** **E-UTRAN - NR FR1 i**nterruptions at NR
SRS antenna port switching in asynchronous EN-DC 1353A.4.5.2.12.1 Test
Purpose and Environment 1353A.4.5.3 SCell Activation and Deactivation
Delay 1361A.4.5.3.1 SCell Activation and deactivation of known SCell in
FR1 for 160ms SCell measurement cycle 1361A.4.5.3.1.1 Test Purpose and
Environment 1361A.4.5.3.1.2 Test Requirements 1367A.4.5.3.2 SCell
Activation and deactivation of known SCell in FR1 for 640ms SCell
measurement cycle 1368A.4.5.3.2.1 Test Purpose and Environment
1368A.4.5.3.2.2 Test Requirements 1368A.4.5.3.3 SCell Activation and
deactivation of unknown SCell in FR1 1368A.4.5.3.3.1 Test Purpose and
Environment 1368A.4.5.3.3.2 Test Requirements 1369A.4.5.3.4 SCell
Activation and deactivation of multiple unknown SCells in FR1 with
single activation/deactivation command 1370A.4.5.3.4.1 Test Purpose and
Environment 1370A.4.5.3.4.2 Test Requirements 1372A.4.5.3.5 Direct SCell
activation at SCell addition of known SCell in FR1 1373A.4.5.3.5.1 Test
Purpose and Environment 1373A.4.5.3.5.2 Test Requirements 1380A.4.5.3.6
Fast SCell Activation of known SCell in FR1 for 160ms SCell measurement
cycle 1381A.4.5.3.6.1 Test Purpose and Environment 1381A.4.5.3.6.2 Test
Requirements 1385A.4.5.3.7 Fast SCell Activation of known SCell in FR1
for 640 ms SCell measurement cycle 1386A.4.5.3.7.1 Test Purpose and
Environment 1386A.4.5.3.7.2 Test Requirements 1386A.4.5.4 UE UL carrier
RRC reconfiguration Delay 1387A.4.5.4.1 UE UL carrier RRC
reconfiguration Delay 1387A.4.5.4.1.1 Test Purpose and Environment
1387A.4.5.4.1.2 Test Requirements 1395A.4.5.5 Beam Failure Detection and
Link recovery procedures 1395A.4.5.5.1 EN-DC Beam Failure Detection and
Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR
in non-DRX mode 1395A.4.5.5.1.1 Test Purpose and Environment
1395A.4.5.5.1.2 Test Requirements 1401A.4.5.5.2 EN-DC Beam Failure
Detection and Link Recovery Test for FR1 PSCell configured with
SSB-based BFD and LR in DRX mode 1402A.4.5.5.2.1 Test Purpose and
Environment 1402A.4.5.5.2.2 Test Requirements 1407A.4.5.5.3 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 PSCell configured with
CSI-RS-based BFD and LR in non-DRX mode 1408A.4.5.5.3.1 Test Purpose and
Environment 1408A.4.5.5.3.2 Test Requirements 1413A.4.5.5.4 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 PSCell configured with
CSI-RS-based BFD and LR in DRX mode 1414A.4.5.5.4.1 Test Purpose and
Environment 1414A.4.5.5.4.2 Test Requirements 1419A.4.5.5.5 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 SCell configured with
CSI-RS-based BFD and SSB-based LR in non-DRX mode 1420A.4.5.5.5.1 Test
Purpose and Environment 1420A.4.5.5.5.2 Test Requirements 1425A.4.5.5.6
EN-DC Beam Failure Detection and Link Recovery Test for FR1 SCell
configured with CSI-RS-based BFD and SSB-based LR in DRX mode
1426A.4.5.5.6.1 Test Purpose and Environment 1426A.4.5.5.6.2 Test
Requirements 1432A.4.5.5.7 EN-DC TRP specific Beam Failure Detection and
Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR
in non-DRX mode 1433A.4.5.5.7.1 Test Purpose and Environment
1433A.4.5.5.7.2 Test Requirements 1438A.4.5.5.8 EN-DC TRP specific Beam
Failure Detection and Link Recovery Test for FR1 SCell configured with
CSI-RS-based BFD and SSB-based LR in non-DRX mode 1439A.4.5.5.8.1 Test
Purpose and Environment 1439A.4.5.5.8.2 Test Requirements 1445A.4.5.6
Active BWP switch 1446A.4.5.6.1 DCI-based and Timer-based Active BWP
Switch 1446A.4.5.6.1.1 E-UTRAN -- NR PSCell FR1 DL active BWP switch in
non-DRX in synchronous EN-DC 1446A.4.5.6.1.2 E-UTRAN -- NR PSCell FR1 DL
active BWP switch with FR1 SCell in non-DRX in synchronous EN-DC
1451A.4.5.6.2 RRC-based Active BWP Switch 1457A.4.5.6.3 Simultaneous
DCI-based and Timer-based Active BWP Switch on multiple CCs
1461A.4.5.6.3.1 Simultaneous E-UTRAN -- NR PSCell FR1 DL active BWP
switch in non-DRX in EN-DC on multiple CCs 1461A.4.5.6.3.1.1 Test
Purpose and Environment 1461A.4.5.6.4 Simultaneous RRC-based Active BWP
Switch on multiple CCs 1467A.4.5.6.4.1 E-UTRAN -- NR PSCell FR1 DL
active BWP switch in non-DRX in synchronous EN-DC on multiple CCs
1467A.4.5.6.4.1.1 Test Purpose and Environment 1467A.4.5.6.4.1.2 Test
Requirements 1474A.4.5.6.4.2 E-UTRAN -- NR FR1 PSCell SCell dormancy
switch of two FR1 SCells inside active time 1474A.4.5.6.4.2.1 Test
Purpose and Environment 1474A.4.5.6.4.2.2 Test Requirements
1484A.4.5.6.5 SCell dormancy switch 1485A.4.5.6.5.1 E-UTRAN -- NR FR1
PSCell SCell dormancy switch of single FR1 SCell outside active time
1485A.4.5.6.5.2 E-UTRAN -- NR FR1 PSCell SCell dormancy switch of two
FR1 SCells inside active time 1490A.4.5.6.5.2.1 Test Purpose and
Environment 1490A.4.5.6.5.2.2 Test Requirements 1496A.4.5.7 PSCell
addition and release delay 1496A.4.5.7.1 Addition and Release Delay of
known NR PSCell 1496A.4.5.7.1.1 Test purpose and environment
1496A.4.5.7.1.2 Test Requirements 1501A.4.5.8 DL Interruptions at
switching between two uplink carriers 1502A.4.5.8.1 Test Purpose and
Environment 1502A.4.5.8.2 Test Requirements 1505A.4.5.9 UE specific CBW
change 1506A.4.5.9.1 UE specific CBW change on FR1 NR PSCell with
non-DRX in synchronous EN- DC 1506A.4.5.9.1.1 Test Purpose and
Environment 1506A.4.5.9.1.2 Test Requirements 1510A.4.5.10 PSCell
activation and deactivation delay 1510A.4.5.10.1 PSCell activation and
deactivation delay 1510A.4.5.10.1.1 Test purpose and environment
1510A.4.5.10.1.2 Test Requirements 1514A.4.5.11 Conditional PSCell
addition and release delay (FR1 EN-DC) 1515A.4.5.11.1 Conditional PSCell
Addition and Release Delay 1515A.4.5.11.1.1 Test purpose and environment
1515A.4.5.11.1.2 Test Parameters 1515A.4.5.11.1.3 Test Requirements
1519A.4.6 Measurement procedure 1519A.4.6.1 Intra-frequency Measurements
1519A.4.6.1.1 EN-DC event triggered reporting tests without gap under
non-DRX 1519A.4.6.1.1.1 Test purpose and Environment 1519A.4.6.1.1.2
Test parameters 1519A.4.6.1.1.3 Test Requirements 1523A.4.6.1.2 EN-DC
event triggered reporting tests without gap under DRX 1523A.4.6.1.2.1
Test purpose and Environment 1523A.4.6.1.2.2 Test parameters
1523A.4.6.1.2.2 Test Requirements 1527A.4.6.1.3 EN-DC event triggered
reporting tests with per-UE gaps under non-DRX 1527A.4.6.1.3.1 Test
purpose and Environment 1527A.4.6.1.3.2 Test parameters 1527A.4.6.1.3.3
Test Requirements 1531A.4.6.1.4 EN-DC event triggered reporting tests
with per-UE gaps under DRX 1531A.4.6.1.4.1 Test purpose and Environment
1531A.4.6.1.4.2 Test parameters 1531A.4.6.1.4.3 Test Requirements
1535A.4.6.1.5 EN-DC event triggered reporting tests without gap under
non-DRX with SSB index reading 1535A.4.6.1.5.1 Test purpose and
Environment 1535A.4.6.1.5.2 Test parameters 1535A.4.6.1.5.3 Test
Requirements 1537A.4.6.1.6 EN-DC event triggered reporting tests with
SSB index reading with per-UE gaps 1538A.4.6.1.6.1 Test purpose and
Environment 1538A.4.6.1.6.2 Test parameters 1538A.4.6.1.6.3 Test
Requirements 1540A.4.6.1.7 EN-DC event triggered reporting tests under
DRX for UE configured with highSpeedMeasFlag-r16 1541A.4.6.1.7.1 Test
purpose and Environment 1541A.4.6.1.7.2 Test parameters 1541A.4.6.1.7.3
Test Requirements 1545A.4.6.1.8 EN-DC event triggered reporting tests
for FR1 cell without SSB time index detection when DRX is used for UE
configured with ***highSpeedMeasCA-Scell-r17*** 1545A.4.6.1.8.1 Test
Purpose and Environment 1545A.4.6.1.8.2 Test Requirements 1550A.4.6.2
Inter-frequency Measurements 1551A.4.6.2.1 EN-DC event triggered
reporting tests for FR1 cell without SSB time index detection when DRX
is not used 1551A.4.6.2.1.1 Test Purpose and Environment 1551A.4.6.2.1.2
Test Requirements 1555A.4.6.2.2 EN-DC event triggered reporting tests
for FR1 cell without SSB time index detection when DRX is used
1555A.4.6.2.2.1 Test Purpose and Environment 1555A.4.6.2.2.2 Test
Requirements 1559A.4.6.2.3 Void 1559A.4.6.2.4 Void 1559A.4.6.2.5 EN-DC
event triggered reporting tests for FR1 cell with SSB time index
detection when DRX is not used 1559A.4.6.2.5.1 Test Purpose and
Environment 1559A.4.6.2.5.2 Test Requirements 1564A.4.6.2.6 EN-DC event
triggered reporting tests for FR1 cell with SSB time index detection
when DRX is used 1564A.4.6.2.6.1 Test Purpose and Environment
1564A.4.6.2.6.2 Test Requirements 1569A.4.6.2.7 Void 1569A.4.6.2.8 Void
1569A.4.6.2.9 EN-DC event triggered reporting tests for FR1 cell without
SSB time index detection when DRX is used for UE configured with
highSpeedMeasInterFreq-r17 1570A.4.6.2.9.1 Test Purpose and Environment
1570A.4.6.2.9.2 Test Requirements 1573A.4.6.3 Void 1573A.4.6.4 L1-RSRP
measurement for beam reporting 1573A.4.6.4.1 SSB based L1-RSRP
measurement when DRX is not used 1573A.4.6.4.1.1 Test Purpose and
Environment 1573A.4.6.4.1.2 Test parameters 1574A.4.6.4.1.3 Test
Requirements 1577A.4.6.4.2 SSB based L1-RSRP measurement when DRX is
used 1577A.4.6.4.2.1 Test Purpose and Environment 1577A.4.6.4.2.2 Test
parameters 1578A.4.6.4.2.3 Test Requirements 1581A.4.6.4.3 CSI-RS based
L1-RSRP measurement when DRX is not used 1581A.4.6.4.3.1 Test Purpose
and Environment 1581A.4.6.4.3.2 Test parameters 1582A.4.6.4.3.3 Test
Requirements 1585A.4.6.4.4 CSI-RS based L1-RSRP measurement when DRX is
used 1585A.4.6.4.4.1 Test Purpose and Environment 1585A.4.6.4.4.2 Test
parameters 1586A.4.6.4.4.3 Test Requirements 1588A.4.6.4.5 SSB based
L1-RSRP measurement when DRX is used for UE configured with
*highSpeedMeasFlag-r16* 1588A.4.6.4.5.1 Test Purpose and Environment
1588A.4.6.4.5.2 Test parameters 1589A.4.6.4.5.3 Test Requirements
1592A.4.6.5 CLI measurements 1592A.4.6.5.1 SRS-RSRP measurement with
non-DRX 1592A.4.6.5.1.1 Test Purpose and Environment 1592A.4.6.5.1.2
Test Parameters 1593A.4.6.5.1.3 Test Requirements 1596A.4.6.5.2 CLI-RSSI
measurement with non-DRX 1596A.4.6.5.2.1 Test Purpose and Environment
1596A.4.6.5.2.2 Test Parameters 1597A.4.6.5.2.3 Test Requirements
1598A.4.6.6.1.2 Test Requirements 1603A.4.6.7 L1-SINR measurement for
beam reporting 1604A.4.6.7.2 L1-SINR measurement with SSB based CMR and
dedicated IMR when DRX is used 1606A.4.6.7.2.1 Test Purpose and
Environment 1606A.4.6.7.2.2 Test parameters 1607A.4.6.7.2.3 Test
Requirements 1609A.4.6.7.3 L1-SINR measurement with CSI-RS based CMR and
dedicated IMR configured when DRX is used 1609A.4.6.7.3.1 Test Purpose
and Environment 1609A.4.6.7.3.2 Test parameters 1609A.4.6.7.3.3 Test
Requirements 1611A.4.6.8 CSI-RS based intra-frequency Measurement
1612A.4.6.8.1 EN-DC event triggered reporting tests without gap under
DRX 1612A.4.6.8.1.1 Test purpose and Environment 1612A.4.6.8.1.2 Test
Requirements 1616A.4.6.9 CSI-RS based inter-frequency Measurement
1616A.4.6.9.1 EN-DC event triggered reporting tests for FR1 cell when
non-DRX is used 1616A.4.6.9.1.1 Test Purpose and Environment
1616A.4.6.9.1.2 Test Requirements 1620A.4.7 Measurement Performance
requirements 1621A.4.7.1 SS-RSRP 1621A.4.7.1.1 EN-DC Intra-frequency
measurement accuracy with FR1 serving cell and FR1 target cell
1621A.4.7.1.1.1 Test Purpose and Environment 1621A.4.7.1.1.2 Test
parameters 1621A.4.7.1.1.3 Test Requirements 1625A.4.7.1.2 EN-DC
inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell 1625A.4.7.1.2.1 Test Purpose and Environment 1625A.4.7.1.2.2
Test parameters 1626A.4.7.1.2.3 Test Requirements 1630A.4.7.1.3 Void
1630A.4.7.2 SS-RSRQ 1630**A.4.7.2.1** **EN-DC Intra-frequency
measurement accuracy with FR1 serving cell and FR1 target cell**
1630A.4.7.2.1.1 Test Purpose and Environment 1630A.4.7.2.1.2 Test
Parameters 1631A.4.7.2.1.3 Test Requirements 1635A.4.7.2.2 EN-DC
Inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell 1635A.4.7.2.2.1 Test Purpose and Environment 1635A.4.7.2.2.2
Test Parameters 1635A.4.7.2.2.3 Test Requirements 1640A.4.7.3 SS-SINR
1640A.4.7.3.1 EN-DC Intra-frequency measurement accuracy with FR1
serving cell and FR1 target cell 1640A.4.7.3.1.1 Test Purpose and
Environment 1640A.4.7.3.1.2 Test Parameters 1640A.4.7.3.1.3 Test
Requirements 1643A.4.7.3.2 EN-DC Inter-frequency measurement accuracy
with FR1 serving cell and FR1 target cell 1643A.4.7.3.2.1 Test Purpose
and Environment 1643A.4.7.3.2.2 Test Parameters 1643A.4.7.3.2.3 Test
Requirements 1648A.4.7.4 L1-RSRP measurement for beam reporting
1648A.4.7.4.1 SSB based L1-RSRP measurement 1648A.4.7.4.1.1 Test Purpose
and Environment 1648A.4.7.4.1.2 Test parameters 1649A.4.7.4.1.3 Test
Requirements 1652A.4.7.4.2 CSI-RS based L1-RSRP measurement on resource
set with repetition off 1652A.4.7.4.2.1 Test Purpose and Environment
1652A.4.7.4.2.2 Test parameters 1653A.4.7.4.2.3 Test Requirements
1656A.4.7.5 SFTD accuracy 1656A.4.7.5.1 SFTD accuracy 1656A.4.7.5.1.1
Test Purpose and Environment 1656A.4.7.5.1.2 Test Parameters
1656A.4.7.5.1.3 Test Requirements 1661A.4.7.5.2 Void 1661A.4.7.5.3 Void
1661A.4.7.6 CLI measurements 1661A.4.7.6.1 EN-DC SRS-RSRP measurement
accuracy with FR1 serving cell 1661A.4.7.6.1.1 Test Purpose and
Environment 1661A.4.7.6.1.2 Test parameters 1662A.4.7.6.1.3 Test
Requirements 1667A.4.7.6.2 EN-DC CLI-RSSI measurement accuracy with FR1
serving cell 1667A.4.7.6.2.1 Test Purpose and Environment
1667A.4.7.6.2.2 Test parameters 1668A.4.7.6.2.3 Test Requirements
1671A.4.7.7 L1-SINR measurement for beam reporting 1671A.4.7.7.2 L1-SINR
measurement with SSB based CMR and dedicated IMR 1675A.4.7.7.2.1 Test
Purpose and Environment 1675A.4.7.7.2.2 Test parameters 1675A.4.7.7.2.3
Test Requirements 1679A.4.7.7.3 L1-SINR measurement with CSI-RS based
CMR and dedicated IMR 1679A.4.7.7.3.1 Test Purpose and Environment
1679A.4.7.7.3.2 Test parameters 1679A.4.7.7.3.3 Test Requirements
1682A.4.7.8 CSI-RSRP 1682A.4.7.8.1 EN-DC Intra-frequency measurement
accuracy with FR1 serving cell and FR1 target cell 1682A.4.7.8.1.1 Test
Purpose and Environment 1682A.4.7.8.1.2 Test parameters 1683A.4.7.8.1.3
Test Requirements 1688A.4.7.8.2 EN-DC inter-frequency measurement
accuracy with FR1 serving cell and FR1 target cell 1688A.4.7.8.2.1 Test
Purpose and Environment 1688A.4.7.8.2.2 Test parameters 1688A.4.7.8.2.3
Test Requirements 1693A.4.7.9 CSI-RSRQ 1693A.4.7.9.1 EN-DC
Intra-frequency measurement accuracy with FR1 serving cell and FR1
target cell 1693A.4.7.9.1.1 Test Purpose and Environment 1693A.4.7.9.1.2
Test Parameters 1693A.4.7.9.1.3 Test Requirements 1698A.4.7.9.2 EN-DC
Inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell 1698A.4.7.9.2.1 Test Purpose and Environment 1698A.4.7.9.2.2
Test Parameters 1698A.4.7.9.2.3 Test Requirements 1703A.4.7.10 CSI-SINR
1703A.4.7.10.1 EN-DC Intra-frequency measurement accuracy with FR1
serving cell and FR1 target cell 1703A.4.7.10.1.1 Test Purpose and
Environment 1703A.4.7.10.1.2 Test Parameters 1704A.4.7.10.1.3 Test
Requirements 1708A.4.7.10.2 EN-DC Inter-frequency measurement accuracy
with FR1 serving cell and FR1 target cell 1709A.4.7.10.2.1 Test Purpose
and Environment 1709A.4.7.10.2.2 Test Parameters 1709A.4.7.10.2.3 Test
Requirements 1713A.4.8 Void 1714A.4A NE-DC test with all NR cells in FR1
1714A.4A.1 Signaling characteristics 1714A.4A.1.1 E-UTRAN PSCell
addition 1714A.4A.1.1.1 Test purpose and environment 1714A.4A.1.1.2 Test
Requirements 1718A.4A.1.2 Active BWP switch 1719A.4A.1.2.1 E-UTRAN
PSCell -- NR PCell FR1 DCI-based and Timer-based DL active BWP switch in
non-DRX in synchronous NE-DC 1719A.4A.1.2.1.1 Test Purpose and
Environment 1719A.4A.1.2.1.2 Test Requirements 1723A.4A.1.3
Intra-frequency handover with E-UTRAN PSCell 1724A.4A.1.3.1 Test purpose
and environment 1724A.4A.1.3.2 Test Requirements 1728A.4A.1.4 Handover
with PSCell from NE-DC to NE-DC with unknown target PSCell
1729A.4A.1.4.1 Test Purpose and Environment 1729A.4A.1.4.2 Test
Parameters 1729A.4A.1.4.3 Test Requirements 1734A.4A.1.4.3.1 Test
Requirements for NR HO 1734A.4A.1.4.3.2 Test Requirements for LTE PSCell
Change 1734A.4A.2 Measurement performance 1735A.4A.2.1 SFTD accuracy
1735A.4A.2.1.1 SFTD accuracy 1735A.4A.2.1.1.1 Test Purpose
1735A.4A.2.1.1.2 Test Environment 1735A.4A.2.1.1.3 Test Requirements
1739A.5 EN-DC tests with one or more NR cells in FR2 1740A.5.1 Void
1740A.5.2 Void 1740A.5.3 RRC\_CONNECTED state mobility 1740A.5.3.1 Void
1740A.5.3.2 RRC Connection Mobility Control 1740A.5.3.2.1 Void
1740A.5.3.2.2 Random Access 1740A.5.3.2.2.1 4-step RA type c ontention
based random access test in FR2 for PSCell/SCell in EN-DC
1740A.5.3.2.2.2 4-step RA type non-contention based random access test
in FR2 for PSCell/SCell in EN-DC 1743A.5.3.2.2.3 2-step RA type
contention based random access test in FR2 for PSCell/SCell in EN-DC
1749A.5.3.2.2.4 2-step RA type non-contention based random access test
in FR2 for PSCell/SCell in EN-DC 1752A.5.3.2.3 Void 1756A.5.3.3 Handover
with PSCell with known FR2 target PSCell 1756A.5.3.3.1 Test purpose and
environment 1756A.5.3.3.2 Test Requirements 1761A.5.5.3.3 void
1762A.5.5.3.4 void 1762A.5.5.3.5 void 1762A.5.5.3.6 void 1762A.5.4
Timing 1762A.5.4.1 UE transmit timing 1762A.5.4.1.1 NR UE Transmit
Timing Test for FR2 1762A.5.4.1.1.1 Test Purpose and environment
1762A.5.4.1.1.2 Test requirements 1765A.5.4.2 UE timer accuracy
1766A.5.4.3 Timing advance 1766A.5.4.3.1 EN-DC FR2 timing advance
adjustment accuracy 1766A.5.4.3.1.1 Test Purpose and Environment
1766A.5.4.3.1.2 Test Parameters 1766A.5.4.3.1.3 Test Requirements
1770A.5.5 Signaling characteristics 1770A.5.5.1 Radio link Monitoring
1770A.5.5.1.1 Radio Link Monitoring Out-of-sync Test for FR2 PSCell
configured with SSB-based RLM RS in non-DRX mode 1770A.5.5.1.1.1 Test
Purpose and Environment 1770A.5.5.1.1.2 Test Requirements 1774A.5.5.1.2
Radio Link Monitoring In-sync Test for FR2 PSCell configured with
SSB-based RLM RS in non-DRX mode 1775A.5.5.1.2.1 Test Purpose and
Environment 1775A.5.5.1.2.2 Test Requirements 1778A.5.5.1.3 Radio Link
Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM
RS in DRX mode 1779A.5.5.1.3.1 Test Purpose and Environment
1779A.5.5.1.3.2 Test Requirements 1783A.5.5.1.4 Radio Link Monitoring
In-sync Test for FR2 PSCell configured with SSB-based RLM RS in DRX mode
1783A.5.5.1.4.1 Test Purpose and Environment 1783A.5.5.1.4.2 Test
Requirements 1787A.5.5.1.5 EN-DC Radio Link Monitoring Out-of-sync Test
for FR2 PSCell configured with CSI-RS-based RLM in non-DRX mode
1787A.5.5.1.6 EN-DC Radio Link Monitoring In-sync Test for FR2 PSCell
configured with CSI-RS-based RLM in non-DRX mode 1791A.5.5.1.7 EN-DC
Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with
CSI-RS-based RLM in DRX mode 1795A.5.5.1.8 EN-DC Radio Link Monitoring
In-sync Test for FR2 PSCell configured with CSI-RS-based RLM in DRX mode
1800A.5.5.1.8.2 Test Requirements 1804A.5.5.1.9 EN-DC Radio Link
Monitoring UE Scheduling Restrictions on FR2 1805A.5.5.1.9.1 Test
Purpose and Environment 1805A.5.5.1.9.2 Test Requirements 1807A.5.5.1.10
Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with
SSB-based RLM RS for UE fulfilling relaxed measurement criterion
1807A.5.5.1.10.1 Test Purpose and Environment 1807A.5.5.1.10.2 Test
Requirements 1810A.5.5.2 Interruption 1810A.5.5.2.1 E-UTRAN -- NR FR2
interruptions at transitions between active and non-active during DRX in
synchronous EN-DC 1810A.5.5.2.1.1 Test Purpose and Environment
1810A.5.5.2.1.2 Test Requirements 1813A.5.5.2.2 E-UTRAN -- NR FR2
interruptions at transitions between active and non-active during DRX in
asynchronous EN-DC 1813A.5.5.2.2.1 Test Purpose and Environment
1813A.5.5.2.2.2 Test Requirements 1816**A.5.5.2.3** E-UTRAN -- NR FR2
interruptions during measurements on deactivated NR SCC in synchronous
EN-DC 1816A.5.5.2.3.1 Test Purpose and Environment 1816A.5.5.2.**3.2**
Test Requirements 1820**A.5.5.2.4** E-UTRAN -- NR FR2 interruptions
during measurements on deactivated NR SCC in asynchronous EN-DC
1820A.5.5.2.4.1 Test Purpose and Environment 1820A.5.5.2.**4.2** Test
Requirements 1823**A.5.5.2.5** E-UTRAN -- NR FR2 interruptions during
measurements on deactivated E-UTRAN SCC in synchronous EN-DC
1824A.5.5.2.5.1 Test Purpose and Environment 1824A.5.5.2.**5.2** Test
Requirements 1827**A.5.5.2.6** E-UTRAN -- NR FR2 interruptions during
measurements on deactivated E-UTRAN SCC in asynchronous EN-DC
1827A.5.5.2.6.1 Test Purpose and Environment 1827A.5.5.2.**6.2** Test
Requirements 1830**A.5.5.2.7** E-UTRAN -- NR FR2 interruptions at E-UTRA
SRS carrier based switching 1830A.5.5.2.7.1 Test Purpose and Environment
1830A.5.5.2.7.2 Test Requirements 1834A.5.5.2.8 E-UTRAN -- NR FR2
interruptions at NR SRS carrier based switching 1834A.5.5.2.8.1 Test
Purpose and Environment 1834A.5.5.2.8.3 Test Requirements 1836A.5.5.3
SCell Activation and Deactivation Delay 1836A.5.5.3.1 SCell Activation
and deactivation of SCell in FR2 intra-band 1836A.5.5.3.1.1 Test Purpose
and Environment 1836A.5.5.3.1.2 Test Requirements 1838A.5.5.3.2 SCell
Activation and deactivation of known SCell in FR1 for 160ms SCell
measurement cycle 1838A.5.5.3.2.1 Test Purpose and Environment
1838A.5.5.3.2.2 Test Requirements 1842A.5.5.3.3 Void 1842A.5.5.3.4 Void
1842A.5.5.3.5 SCell Activation and deactivation of SCell in FR2
1842A.5.5.3.5.1 Test Purpose and Environment 1842A.5.5.3.5.2 Test
Requirements 1845A.5.5.3.6 Multiple SCell Activation and deactivation of
one unknown SCell and one known SCell in FR2 1846A.5.5.3.6.1 Test
Purpose and Environment 1846A.5.5.3.6.2 Test Requirements 1850A.5.5.3.7
Direct SCell activation at SCell addition of known SCell in FR2
1851A.5.5.3.7.1 Test Purpose and Environment 1851A.5.5.3.7.2 Test
Requirements 1854A.5.5.3.8 Fast SCell Activation of SCell in FR2
intra-band 1854A.5.5.3.8.1 Test Purpose and Environment 1854A.5.5.3.8.2
Test Requirements 1858A.5.5.3.9 PUCCH SCell Activation and deactivation
of known SCell in FR2 1859A.5.5.3.9.1 Test Purpose and Environment
1859A.5.5.3.9.2 Test Requirements 1862A.5.5.3.10 PUCCH SCell Activation
and deactivation of unknown SCell in FR2 1863A.5.5.3.10.1 Test Purpose
and Environment 1863A.5.5.3.10.2 Test Requirements 1866A.5.5.3.11
Multiple SCell activation and deactivation of one known PUCCH SCell and
one unknown SCell in FR2 1867A.5.5.3.11.1 Test Purpose and Environment
1867A.5.5.3.11.2 Test Requirements 1870A.5.5.3.12 SCell Activation and
deactivation of unknown PUCCH SCell and unknown DL SCell in FR2 in
non-DRX 1871A.5.5.3.12.1 Test Purpose and Environment 1871A.5.5.3.12.2
Test Requirements 1874A.5.5.4 Void 1875A.5.5.5 Beam Failure Detection
and Link recovery procedures 1875A.5.5.5.1 EN-DC Beam Failure Detection
and Link Recovery Test for FR2 PSCell configured with SSB-based BFD and
LR in non-DRX mode 1875A.5.5.5.1.1 Test Purpose and Environment
1875A.5.5.5.1.2 Test Requirements 1879A.5.5.5.2 EN-DC Beam Failure
Detection and Link Recovery Test for FR2 PSCell configured with
SSB-based BFD and LR in DRX mode 1880A.5.5.5.2.1 Test Purpose and
Environment 1880A.5.5.5.2.2 Test Requirements 1884A.5.5.5.3 EN-DC Beam
Failure Detection and Link Recovery Test for FR2 PSCell configured with
CSI-RS-based BFD and LR in non-DRX mode 1885A.5.5.5.3.1 Test Purpose and
Environment 1885A.5.5.5.3.2 Test Requirements 1889A.5.5.5.4 EN-DC Beam
Failure Detection and Link Recovery Test for FR2 PSCell configured with
CSI-RS-based BFD and LR in DRX mode 1890A.5.5.5.4.1 Test Purpose and
Environment 1890A.5.5.5.4.2 Test Requirements 1894A.5.5.5.5 EN-DC
scheduling availability restriction during Beam Failure Detection and
Link Recovery for FR2 PSCell configured with SSB-based BFD and LR in
non-DRX mode 1895A.5.5.5.5.1 Test Purpose and Environment
1895A.5.5.5.5.2 Test Requirements 1899A.5.5.5.6 EN-DC Beam Failure
Detection and Link Recovery Test for FR2 SCell configured with
CSI-RS-based BFD and LR in non-DRX mode 1900A.5.5.5.6.1 Test Purpose and
Environment 1900A.5.5.5.6.2 Test Requirements 1904A.5.5.5.7 EN-DC Beam
Failure Detection and Link Recovery Test for FR2 SCell configured with
CSI-RS-based BFD and LR in DRX mode 1905A.5.5.5.7.1 Test Purpose and
Environment 1905A.5.5.5.7.2 Test Requirements 1909A.5.5.5.8 EN-DC TRP
specific Beam Failure Detection and Link Recovery Test for FR2 PSCell
configured with CSI-RS-based BFD and LR in DRX mode 1910A.5.5.5.8.1 Test
Purpose and Environment 1910A.5.5.5.8.2 Test Requirements 1915A.5.5.5.9
Beam Failure Detection and Link Recovery Test for FR2 PSCell configured
with SSB-based BFD and LR in DRX mode for UE fulfilling relaxed
measurement criterion 1915A.5.5.5.9.1 Test Purpose and Environment
1915A.5.5.5.9.2 Test Requirements 1919A.5.5.6 Active BWP switch
1919A.5.5.6.1 DCI-based and Timer-based Active BWP Switch
1919A.5.5.6.1.1 E-UTRAN -- NR PSCell FR2 DL active BWP switch with
non-DRX in synchronous EN-DC 1919A.5.5.6.1.1.1 Test Purpose and
Environment 1919A.**5.5.6.1.1**.2 Test Requirements 1923A.5.5.6.1.2
E-UTRAN -- NR PSCell FR2 with FR2 SCell DL active BWP switch in non-DRX
in synchronous EN-DC 1923A.5.5.6.2 RRC-based Active BWP Switch
1928A.5.5.6.2.1 E-UTRAN -- NR PSCell FR2 DL active BWP switch with
non-DRX in synchronous EN-DC 1928A.5.5.6.3 Simultaneous DCI-based and
Timer-based Active BWP Switch on multiple CCs 1932A.5.5.6.3.1 E-UTRAN --
NR PSCell FR2 and NR SCell FR2 DL active BWP switch on multiple CCs in
synchronous EN-DC 1932A.5.5.6.4 SCell dormancy switch 1936A.5.5.6.4.1
E-UTRAN -- NR FR2 PSCell SCell dormancy switch of single FR2 SCell
inside active time 1936A.5.5.6.4.1.1 Test Purpose and Environment
1936A.5.5.6.4.1.2 Test Requirements 1940A.5.5.6.4.2 E-UTRAN -- NR FR1
PSCell SCell dormancy switch of two FR2 SCells outside active time
1940A.5.5.6.4.2.1 Test Purpose and Environment 1940A.5.5.6.4.2.2 Test
Requirements 1947A.5.5.6.5 Simultaneous RRC-based Active BWP Switch on
multiple CCs 1947A.5.5.6.5.1 E-UTRAN -- NR PSCell FR2 and NR SCell FR2
DL active BWP switch on multiple CCs with non-DRX in synchronous EN-DC
1947A.5.5.7 PSCell addition and release delay 1950A.5.5.7.1 Addition and
Release Delay of NR PSCell 1950A.5.5.7.1.1 Test purpose and environment
1950A.5.5.7.1.2 Test Requirements 1953A.5.5.8 Active TCI state switch
delay 1954A.5.5.8.1 MAC-CE based active TCI state switch 1954A.5.5.8.1.1
E-UTRAN -- NR PSCell FR2 active TCI state switch for a known TCI state
1954A.5.5.8.1.1.1 Test Purpose and Environment 1954A.5.5.8**.1.1**.2
Test Requirements 1958A.5.5.8.2 RRC based active TCI state switch
1958A.5.5.8.2.1 E-UTRAN -- NR PSCell FR2 active TCI state switch for a
known TCI state 1958A.5.5.8.2.1.1 Test Purpose and Environment
1958A.5.5.8.2**.1**.2 Test Requirements 1962A.5.5.9 Uplink spatial
relation switch delay 1962A.5.5.9.1 MAC-CE based uplink spatial relation
switch 1962A.5.5.9.1.1 E-UTRAN -- NR PSCell FR2 uplink spatial relation
switch for a known spatial relation 1962A.5.5.9.1.1.1 Test Purpose and
Environment 1962A.5.5.9**.1.1**.2 Test Requirements 1965A.5.5.9.2 RRC
based spatial relation switch 1965A.5.5.9.2.1 E-UTRAN -- NR PSCell FR2
spatial relation switch associated with a known DL-RS 1965A.5.5.9.2.1.1
Test Purpose and Environment 1965A.5.5.9.2**.1**.2 Test Requirements
1968A.5.5.10 UE specific CBW change 1968A.5.5.10.1 UE specific CBW
change on FR2 NR PSCell 1968A.5.5.10.1.1 Test Purpose and Environment
1968A.5.5.10.1.2 Test Requirements 1971A.5.5.11 Unified TCI state switch
delay 1972A.5.5.11.1 MAC-CE based active joint TCI state switch
1972A.5.5.11.1.1 E-UTRAN -- NR PSCell FR2 active joint TCI state switch
for a known TCI state 1972A.5.5.11.1.1.1 Test Purpose and Environment
1972A.5.5.11.1.1.2 Test parameters 1972A.5.5.11.1.1.3 Test Requirements
1975A.5.5.11.2 MAC-CE based active uplink TCI state switch
1975A.5.5.11.2.1 E-UTRAN -- NR PSCell FR2 active uplink TCI state switch
for a known TCI state 1975A.5.5.11.2.1.1 Test Purpose and Environment
1975A.5.5.11.2.1.2 Test parameters 1976A.5.5.11.2.1.3 Test Requirements
1978A.5.5.11.3 MAC-CE based active downlink TCI state switch
1978A.5.5.11.3.1 E-UTRAN -- NR PSCell FR2 downlink TCI state switch to
cell with additional PCI for a known TCI state 1978A.5.5.11.3.1.1 Test
Purpose and Environment 1978A.5.5.11.3.1.2 Test Parameters
1979A.5.5.11.3**.1**.3 Test Requirements 1983A.5.5.12 PSCell activation
and deactivation delay 1983A.5.5.12.1 PSCell activation and deactivation
delay 1983A.5.5.12.1.1 Test purpose and environment 1983A.5.5.12.1.2
Test Requirements 1986A.5.5.13 Conditional PSCell addition and release
delay 1987A.5.5.13.1 Addition and Release Delay of NR PSCell
1987A.5.5.13.1.1 Test purpose and environment 1987A.5.5.13.1.2 Test
Requirements 1990**A.5.5.13.2** E-UTRAN -- NR FR2 interruptions during
measurements on deactivated NR PSCell 1991A.5.5.13.2.1 Test Purpose and
Environment 1991A.5.5.13.2**.2** Test Requirements 1994A.5.6 Measurement
procedure 1994A.5.6.1 Intra-frequency Measurements 1994A.5.6.1.1 EN-DC
event triggered reporting test without gap under non-DRX 1994A.5.6.1.1.1
Test purpose and Environment 1994A.5.6.1.1.2 Test Requirements
1998A.5.6.1.2 EN-DC event triggered reporting test without gap under DRX
1998A.5.6.1.2.1 Test purpose and Environment 1998A.5.6.1.2.2 Test
Requirements 2000A.5.6.1.3 EN-DC event triggered reporting test with
per-UE gaps under non-DRX 2001A.5.6.1.3.1 Test purpose and Environment
2001A.5.6.1.3.2 Test Requirements 2005A.5.6.1.4 EN-DC event triggered
reporting test with per-UE gaps under DRX 2005A.5.6.1.4.1 Test purpose
and Environment 2005A.5.6.1.4.2 Test Requirements 2008A.5.6.2
Inter-frequency Measurements 2009A.5.6.2.1 EN-DC event triggered
reporting tests for FR2 cell without SSB time index detection when DRX
is not used 2009A.5.6.2.1.1 Test Purpose and Environment 2009A.5.6.2.1.2
Test Requirements 2012A.5.6.2.2 EN-DC event triggered reporting tests
for FR2 cell without SSB time index detection when DRX is used
2012A.5.6.2.2.1 Test Purpose and Environment 2012A.5.6.2.2.2 Test
Requirements 2016A.5.6.2.3 EN-DC event triggered reporting tests for FR2
cell with SSB time index detection when DRX is not used 2016A.5.6.2.3.1
Test Purpose and Environment 2016A.5.6.2.3.2 Test Requirements
2020A.5.6.2.4 EN-DC event triggered reporting tests for FR2 cell with
SSB time index detection when DRX is used 2020A.5.6.2.4.1 Test Purpose
and Environment 2020A.5.6.2.4.2 Test Requirements 2024A.5.6.2.5 EN-DC
event triggered reporting tests for FR2 cell without SSB time index
detection when DRX is not used 2024A.5.6.2.5.1 Test Purpose and
Environment 2024A.5.6.2.5.2 Test Requirements 2029A.5.6.2.6 EN-DC event
triggered reporting tests for FR2 cell without SSB time index detection
when DRX is used 2029A.5.6.2.6.1 Test Purpose and Environment
2029A.5.6.2.6.2 Test Requirements 2033A.5.6.2.7 EN-DC event triggered
reporting tests for FR2 cell with SSB time index detection when DRX is
not used 2033A.5.6.2.7.1 Test Purpose and Environment 2033A.5.6.2.7.2
Test Requirements 2038A.5.6.2.8 EN-DC event triggered reporting tests
for FR2 cell with SSB time index detection when DRX is used
2038A.5.6.2.8.1 Test Purpose and Environment 2038A.5.6.2.8.2 Test
Requirements 2043A.5.6.3 L1-RSRP measurement for beam reporting
2044A.5.6.3.1 SSB based L1-RSRP measurement when DRX is not used
2044A.5.6.3.1.1 Test Purpose and Environment 2044A.5.6.3.1.2 Test
parameters 2044A.5.6.3.1.3 Test Requirements 2046A.5.6.3.2 SSB based
L1-RSRP measurement when DRX is used 2046A.5.6.3.2.1 Test Purpose and
Environment 2046A.5.6.3.2.2 Test parameters 2047A.5.6.3.2.3 Test
Requirements 2049A.5.6.3.3 CSI-RS based L1-RSRP measurement when DRX is
not used 2049A.5.6.3.3.1 Test Purpose and Environment 2049A.5.6.3.3.2
Test parameters 2050A.5.6.3.3.3 Test Requirements 2052A.5.6.3.4 CSI-RS
based L1-RSRP measurement when DRX is used 2052A.5.6.3.4.1 Test Purpose
and Environment 2052A.5.6.3.4.2 Test parameters 2053A.5.6.3.4.3 Test
Requirements 2055A.5.6.4 CLI measurements 2056A.5.6.4.1 SRS-RSRP
measurement with DRX 2056A.5.6.4.1.1 Test Purpose and Environment
2056A.5.6.4.1.2 Test Parameters 2056A.5.6.4.1.3 Test Requirements
2058A.5.6.4.2 CLI-RSSI measurement with DRX 2058A.5.6.4.2.1 Test Purpose
and Environment 2058A.5.6.4.2.2 Test Parameters 2059A.5.6.4.2.3 Test
Requirements 2061A.5.6.5 Measurements with autonomous gaps 2061A.5.6.5.1
EN-DC inter-frequency CGI identification of NR neighbor cell in FR2
2061A.5.6.5.1.1 Test Purpose and Environment 2061A.5.6.5.1.2 Test
Requirements 2064A.5.6.6 L1-SINR measurement for beam reporting
2065A.5.6.6.2 L1-SINR measurement with SSB based CMR and dedicated IMR
when DRX is not used 2067A.5.6.6.2.1 Test Purpose and Environment
2067A.5.6.6.2.2 Test parameters 2068A.5.6.6.2.3 Test Requirements
2071A.5.6.6.3 L1-SINR measurement with CSI-RS based CMR and dedicated
IMR configured when DRX is not used 2071A.5.6.6.3.1 Test Purpose and
Environment 2071A.5.6.6.3.2 Test parameters 2072A.5.6.6.3.3 Test
Requirements 2074A.5.6.7 CSI-RS based Intra-frequency Measurements
2074A.5.6.7.1 EN-DC event triggered reporting test without gap under
non-DRX 2074A.5.6.7.1.1 Test purpose and Environment 2074A.5.6.7.1.2
Test Requirements 2077A.5.6.8 CSI-RS based Inter-frequency Measurements
2078A.5.6.8.1 EN-DC event triggered reporting tests for NR FR2 cell when
DRX is used 2078A.5.6.8.1.1 Test Purpose and Environment 2078A.5.6.8.1.2
Test Requirements 2082A.5.7 Measurement Performance requirements
2082A.5.7.1 SS-RSRP 2082A.5.7.1.1 EN-DC intra-frequency case measurement
accuracy with FR2 serving cell and FR2 target cell 2082A.5.7.1.1.1 Test
Purpose and Environment 2082A.5.7.1.1.2 Test parameters 2083A.5.7.1.1.3
Test Requirements 2085A.5.7.1.2 EN-DC inter-frequency case measurement
accuracy with FR2 serving cell and FR2 target cell 2086A.5.7.1.2.1 Test
Purpose and Environment 2086A.5.7.1.2.2 Test parameters 2086A.5.7.1.2.3
Test Requirements 2090A.5.7.1.3 EN-DC inter-frequency measurement
accuracy with FR1 serving cell and FR2 target cell 2091A.5.7.1.3.1 Test
Purpose and Environment 2091A.5.7.1.3.2 Test parameters 2091A.5.7.1.3.3
Test Requirements 2094A.5.7.2 SS-RSRQ 2095A.5.7.2.1 EN-DC
Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 2095A.5.7.2.1.1 Test Purpose and Environment 2095A.5.7.2.1.2
Test Parameters 2095A.5.7.2.1.3 Test Requirements 2098A.5.7.2.2 EN-DC
Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 2098A.5.7.2.2.1 Test Purpose and Environment 2098A.5.7.2.2.2
Test Parameters 2098A.5.7.2.2.3 Test Requirements 2100A.5.7.3 SS-SINR
2101A.5.7.3.1 EN-DC Intra-frequency measurement accuracy with FR2
serving cell and FR2 TDD target cell 2101A.5.7.3.1.1 Test Purpose and
Environment 2101A.5.7.3.1.2 Test Parameters 2101A.5.7.3.1.3 Test
Requirements 2104A.5.7.3.2 EN-DC Inter-frequency measurement accuracy
with FR2 serving cell and FR2 TDD target cell 2104A.5.7.3.2.1 Test
Purpose and Environment 2104A.5.7.3.2.2 Test Parameters 2104A.5.7.3.2.3
Test Requirements 2106A.5.7.4 L1-RSRP measurement for beam reporting
2106A.5.7.4.1 SSB based L1-RSRP measurement 2106A.5.7.4.1.1 Test Purpose
and Environment 2106A.5.7.4.1.2 Test parameters 2107A.5.7.4.1.3 Test
Requirements 2109A.5.7.4.2 CSI-RS based L1-RSRP measurement on resource
set with repetition off 2110A.5.7.4.2.1 Test Purpose and Environment
2110A.5.7.4.2.2 Test parameters 2110A.5.7.4.2.3 Test Requirements
2112A.5.7.5 CLI measurements 2113A.5.7.5.1 EN-DC SRS-RSRP measurement
accuracy with FR2 serving cell 2113A.5.7.5.1.1 Test Purpose and
Environment 2113A.5.7.5.1.2 Test parameters 2113A.5.7.5.1.3 Test
Requirements 2116A.5.7.5.2 EN-DC CLI-RSSI measurement accuracy with FR2
serving cell 2117A.5.7.5.2.1 Test Purpose and Environment
2117A.5.7.5.2.2 Test parameters 2117A.5.7.5.2.3 Test Requirements
2119A.5.7.6 L1-SINR measurement for beam reporting 2120A.5.7.6.2 L1-SINR
measurement with SSB based CMR and dedicated IMR 2123A.5.7.6.2.1 Test
Purpose and Environment 2123A.5.7.6.2.2 Test parameters 2123A.5.7.6.2.3
Test Requirements 2125A.5.7.6.3 L1-SINR measurement with CSI-RS based
CMR and dedicated IMR 2126A.5.7.6.3.1 Test Purpose and Environment
2126A.5.7.6.3.2 Test parameters 2126A.5.7.6.3.3 Test Requirements
2128A.5.7.7 CSI-RSRP 2129A.5.7.7.1 EN-DC intra-frequency case
measurement accuracy with FR2 serving cell and FR2 target cell
2129A.5.7.7.1.1 Test Purpose and Environment 2129A.5.7.7.1.2 Test
parameters 2129A.5.7.7.1.3 Test Requirements 2133A.5.7.7.2 EN-DC
inter-frequency case measurement accuracy with FR2 serving cell and FR2
target cell 2134A.5.7.7.2.1 Test Purpose and Environment 2134A.5.7.7.2.2
Test parameters 2134A.5.7.7.2.3 Test Requirements 2138A.5.7.8 CSI-RSRQ
2139A.5.7.8.1 EN-DC Intra-frequency measurement accuracy with FR2
serving cell and FR2 target cell 2139A.5.7.8.1.1 Test Purpose and
Environment 2139A.5.7.8.1.2 Test Parameters 2139A.5.7.8.1.3 Test
Requirements 2141A.5.7.8.2 EN-DC Inter-frequency measurement accuracy
with FR2 serving cell and FR2 TDD target cell 2141A.5.7.8.2.1 Test
Purpose and Environment 2141A.5.7.8.2.2 Test Parameters 2141A.5.7.8.2.3
Test Requirements 2143A.5.7.9 CSI-SINR 2143A.5.7.9.1 EN-DC
Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 2143A.5.7.9.1.1 Test Purpose and Environment 2143A.5.7.9.1.2
Test Parameters 2144A.5.7.9.1.3 Test Requirements 2146A.5.7.9.2 EN-DC
Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 2146A.5.7.9.2.1 Test Purpose and Environment 2146A.5.7.9.2.2
Test Parameters 2147A.5.7.9.2.3 Test Requirements 2149A.5.8 Void 2149A.6
NR standalone tests with all NR cells in FR1 2151A.6.1 SA: RRC\_IDLE
state mobility 2151A.6.1.1 Cell re-selection to NR 2151A.6.1.1.1 Cell
reselection to FR1 intra-frequency NR case 2151A.6.1.1.1.1 Test Purpose
and Environment 2151A.6.1.1.1.2 Test Parameters 2151A.6.1.1.1.3 Test
Requirements 2155A.6.1.1.2 Cell reselection to FR1 inter-frequency NR
case 2155A.6.1.1.2.1 Test Purpose and Environment 2155A.6.1.1.2.2 Test
Parameters 2155A.6.1.1.2.3 Test Requirements 2159A.6.1.1.3 Cell
reselection to FR1 intra-frequency NR case for UE fulfilling low
mobility relaxed measurement criterion 2159A.6.1.1.3.1 Test Purpose and
Environment 2159A.6.1.1.3.2 Test Parameters 2159A.6.1.1.3.3 Test
Requirements 2164A.6.1.1.4 Cell reselection to FR1 intra-frequency NR
case for UE fulfilling not-at-cell edge relaxed measurement criterion
2164A.6.1.1.4.1 Test Purpose and Environment 2164A.6.1.1.4.2 Test
Parameters 2164A.6.1.1.4.3 Test Requirements 2167A.6.1.1.5 Cell
reselection to FR1 inter-frequency NR case for UE fulfilling low
mobility relaxed measurement criterion 2167A.6.1.1.5.1 Test Purpose and
Environment 2167A.6.1.1.5.2 Test Parameters 2167A.6.1.1.5.3 Test
Requirements 2172A.6.1.1.6 Cell reselection to FR1 inter-frequency NR
case for UE fulfilling not-at-cell edge relaxed measurement criterion
2173A.6.1.1.6.1 Test Purpose and Environment 2173A.6.1.1.6.2 Test
Parameters 2173A.6.1.1.6.3 Test Requirements 2177A.6.1.1.7 Cell
reselection to FR1 intra-frequency NR case for UE configured with
***highSpeedMeasFlag-r16*** 2178A.6.1.1.7.1 Test Purpose and Environment
2178A.6.1.1.7.2 Test Parameters 2178A.6.1.1.7.3 Test Requirements
2181A.6.1.1.8 Cell reselection to FR1 inter-frequency NR case for UE
configured with *highSpeedMeasInterFreq-r17* 2181A.6.1.1.8.1 Test
Purpose and Environment 2181A.6.1.1.8.2 Test Parameters 2181A.6.1.1.8.3
Test Requirements 2185A.6.1.2 Inter-RAT E-UTRAN cell re-selection
2185A.6.1.2.1 Cell reselection to higher priority E-UTRAN
2185A.6.1.2.1.1 Test Purpose and Environment 2185A.6.1.2.1.2 Test
Parameters 2185A.6.1.2.1.3 Test Requirements 2188A.6.1.2.2 Cell
reselection to lower priority E-UTRAN 2189A.6.1.2.2.1 Test Purpose and
Environment 2189A.6.1.2.2.2 Test Parameters 2189A.6.1.2.2.3 Test
Requirements 2192A.6.1.2.3 Cell reselection to lower priority E-UTRAN
for UE fulfilling low mobility relaxed measurement criterion
2193A.6.1.2.3.1 Test Purpose and Environment 2193A.6.1.2.3.2 Test
Parameters 2193A.6.1.2.3.3 Test Requirements 2196A.6.1.2.4 Cell
reselection to lower priority E-UTRAN for UE fulfilling not-at-cell edge
relaxed measurement criterion 2197A.6.1.2.4.1 Test Purpose and
Environment 2197A.6.1.2.4.2 Test Parameters 2197A.6.1.2.4.3 Test
Requirements 2200A.6.1.2.5 Cell reselection to lower priority E-UTRAN
cell for UE configured with highSpeedMeasFlag-r16 2201A.6.1.2.5.1 Test
Purpose and Environment 2201A.6.1.2.5.2 Test Parameters 2201A.6.1.2.5.3
Test Requirements 2205A.6.1.1.7 **Void** 2206A.6.2 SA: RRC\_INACTIVE
state mobility 2206A.6.2.1 Configured Grant based Small Data
Transmissions (CG-SDT) 2206A.6.2.1.1 Test purpose and Environment
2206A.6.2.1.2 Test Parameters 2208A.6.2.1.3 Test requirements 2210A.6.3
RRC\_CONNECTED state mobility 2210A.6.3.1 Handover 2210A.6.3.1.1
Intra-frequency handover from FR1 to FR1; known target cell
2210A.6.3.1.1.1 Test Purpose and Environment 2210A.6.3.1.1.2 Test
Parameters 2210A.6.3.1.1.3 Test Requirements 2214A.6.3.1.2
Intra-frequency handover from FR1 to FR1; unknown target cell
2214A.6.3.1.2.1 Test Purpose and Environment 2214A.6.3.1.2.2 Test
Parameters 2214A.6.3.1.2.3 Test Requirements 2218A.6.3.1.3
Inter-frequency handover from FR1 to FR1; unknown target cell
2218A.6.3.1.3.1 Test Purpose and Environment 2218A.6.3.1.3.2 Test
Parameters 2218A.6.3.1.3.3 Test Requirements 2222A.6.3.1.4 SA NR -
E-UTRAN handover 2222A.6.3.1.4.1 Test Purpose and Environment
2222A.6.3.1.4.2 Test Requirements 2228A.6.3.1.5 SA NR - E-UTRAN handover
with unknown target cell 2228A.6.3.1.5.1 Test Purpose and Environment
2228A.6.3.1.5.2 Test Requirements 2234A.6.3.1.6 SA NR - UTRAN FDD
handover 2234A.6.3.1.6.1 Test Purpose and Environment 2234A.6.3.1.6.2
Test Requirements 2238A.6.3.1.7 Intra-frequency synchronous DAPS
handover in FR1 2238A.6.3.1.7.1 Test Purpose and Environment
2238A.6.3.1.7.2 Test Parameters 2238A.6.3.1.7.3 Test Requirements
2242A.6.3.1.8 Intra-frequency asynchronous DAPS handover in FR1
2243A.6.3.1.8.1 Test Purpose and Environment 2243A.6.3.1.8.2 Test
Parameters 2243A.6.3.1.8.3 Test Requirements 2247A.6.3.1.9 Intra-band
inter-frequency synchronous DAPS handover test in SA for FR1
2248A.6.3.1.9.1 Test Purpose and Environment 2248A.6.3.1.9.2 Test
Parameters 2248A.6.3.1.9.3 Test Requirements 2252A.6.3.1.10 Intra-band
inter-frequency asynchronous DAPS handover test in SA for FR1
2252A.6.3.1.10.1 Test Purpose and Environment 2252A.6.3.1.10.2 Test
Parameters 2252A.6.3.1.10.3 Test Requirements 2255A.6.3.1.11 Inter-band
inter-frequency synchronous DAPS handover from FR1 to FR1
2255A.6.3.1.11.1 Test Purpose and Environment 2255A.6.3.1.11.2 Test
Parameters 2255A.6.3.1.11.3 Test Requirements 2262A.6.3.1.12 Inter-band
inter-frequency asynchronous DAPS handover from FR1 to FR1
2262A.6.3.1.12.1 Test Purpose and Environment 2262A.6.3.1.12.2 Test
Parameters 2262A.6.3.1.12.3 Test Requirements 2270A.6.3.1.13 SA NR -
E-UTRAN with NR PSCell addition in FR1 2270A.6.3.1.13.1 Test Purpose and
Environment 2270A.6.3.1.13.2 Test Requirements 2279A.6.3.1.14 SA NR -
E-UTRAN handover with NR FR1 PScell addition 2279A.6.3.1.14.1 Test
Purpose and Environment 2279A.6.3.1.14.2 Test Requirements 2288A.6.3.2
RRC Connection Mobility Control 2289A.6.3.2.1 SA: RRC Re-establishment
2289A.6.3.2.1.1 Intra-frequency RRC Re-establishment in FR1
2289A.6.3.2.1.2 Inter-frequency RRC Re-establishment in FR1
2293A.6.3.2.1.3 Intra-frequency RRC Re-establishment in FR1 without
serving cell timing 2297A.6.3.2.2 Random Access 2300A.6.3.2.2.1 4-step
RA type contention based random access test in FR1 for NR standalone
2300A.6.3.2.2.2 4-step RA type non-contention based random access test
in FR1 for NR standalone 2304A.6.3.2.2.3 2-step RA type contention based
random access test in FR1 for NR standalone 2309A.6.3.2.2.4 2-step RA
type non-contention based test in FR1 for NR standalone 2314A.6.3.2.3
SA: RRC Connection Release with Redirection 2318A.6.3.2.3.1 Redirection
from NR in FR1 to NR in FR1 2318A.6.3.2.3.2 Redirection from NR in FR1
to E-UTRAN 2322A.6.3.3 Conditional handover 2329A.6.3.3.1
Intra-frequency conditional handover from FR1 to FR1 2329A.6.3.3.1.1
Test Purpose and Environment 2329A.6.3.3.1.2 Test Parameters
2329A.6.3.3.1.3 Test Requirements 2333A.6.3.3.2 Inter-frequency
conditional handover from FR1 to FR1 2333A.6.3.3.2.1 Test Purpose and
Environment 2333A.6.3.3.2.2 Test Parameters 2333A.6.3.3.2.3 Test
Requirements 2337A.6.4 Timing 2337A.6.4.1 UE transmit timing
2337A.6.4.1.1 NR UE Transmit Timing Test for FR1 2337A.6.4.1.1.1 Test
Purpose and environment 2337A.6.4.1.1.2 Test requirements 2341A.6.4.2 UE
timer accuracy 2341A.6.4.3 Timing advance 2341A.6.4.3.1 SA FR1 timing
advance adjustment accuracy 2341A.6.4.3.1.1 Test Purpose and Environment
2341A.6.4.3.1.2 Test Parameters 2341A.6.4.3.1.3 Test Requirements
2345A.6.5 Signalling characteristics 2345A.6.5.1 Radio link Monitoring
2345A.6.5.1.1 Radio Link Monitoring Out-of-sync Test for FR1 PCell
configured with SSB-based RLM RS in non-DRX mode 2346A.6.5.1.1.1 Test
Purpose and Environment 2346A.6.5.1.1.2 Test Requirements 2351A.6.5.1.2
Radio Link Monitoring In-sync Test for FR1 PCell configured with
SSB-based RLM RS in non-DRX mode 2351A.6.5.1.2.1 Test Purpose and
Environment 2351A.6.5.1.2.2 Test Requirements 2357A.6.5.1.3 Radio Link
Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM
RS in DRX mode 2357A.6.5.1.3.1 Test Purpose and Environment
2357A.6.5.1.3.2 Test Requirements 2363A.6.5.1.4 Radio Link Monitoring
In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode
2363A.6.5.1.4.1 Test Purpose and Environment 2363A.6.5.1.4.2 Test
Requirements 2369A.6.5.1.5 Radio Link Monitoring Out-of-sync Test for
FR1 PCell configured with CSI-RS-based RLM in non-DRX mode
2369A.6.5.1.5.1 Test Purpose and Environment 2369A.6.5.1.5.2 Test
Requirements 2375A.6.5.1.6 Radio Link Monitoring In-sync Test for FR1
PCell configured with CSI-RS-based RLM in non-DRX mode 2375A.6.5.1.6.1
Test Purpose and Environment 2375A.6.5.1.6.2 Test Requirements
2380A.6.5.1.7 Radio Link Monitoring Out-of-sync Test for FR1 PCell
configured with CSI-RS-based RLM in DRX mode 2380A.6.5.1.7.1 Test
Purpose and Environment 2380A.6.5.1.7.2 Test Requirements 2384A.6.5.1.8
Radio Link Monitoring In-sync Test for FR1 PCell configured with
CSI-RS-based RLM in DRX mode 2384A.6.5.1.8.1 Test Purpose and
Environment 2384A.6.5.1.8.2 Test Requirements 2390A.6.5.1.9 Radio Link
Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based
RLM for UE fulfilling relaxed measurement criterion 2390A.6.5.1.9.1 Test
Purpose and Environment 2390A.6.5.1.9.2 Test Requirements 2396A.6.5.2
Interruption 2396**A.6.5.2.1** Interruptions during measurements on
deactivated NR SCC in FR1 2396**A.6.5.2.1**.2 Test Requirements
2400A.6.5.2.2 SA interruptions at NR SRS carrier based switching
2401A.6.5.2.2.1 Test Purpose and Environment 2401A.6.5.2.2.2 Test
Parameters 2401A.6.5.2.2.3 Test Requirements 2403A.6.5.2.3 SA
interruptions at NR SRS antenna port switching with 1 SRS symbol in a
slot in NR-CA 2404A.6.5.2.3.1 Test Purpose and Environment
2404A.6.5.2.3.2 Test Parameters 2404A.6.5.2.3.3 Test Requirements
2406A.6.5.2.4 SA interruptions at NR SRS antenna port switching
2407A.6.5.2.4.1 Test Purpose and Environment 2407A.6.5.2.4.2 Test
Parameters 2407A.6.5.2.4.3 Test Requirements 2409A.6.5.3 SCell
Activation and Deactivation Delay 2410A.6.5.3.1 SCell Activation and
deactivation of known SCell in FR1 in non-DRX for 160ms SCell
measurement cycle 2410A.6.5.3.1.1 Test Purpose and Environment
2410A.6.5.3.1.2 Test Requirements 2415A.6.5.3.2 SCell Activation and
deactivation of known SCell in FR1 in non-DRX for 640 ms SCell
measurement cycle 2416A.6.5.3.2.1 Test Purpose and Environment
2416A.6.5.3.2.2 Test Requirements 2416A.6.5.3.3 SCell Activation and
deactivation of unknown SCell in FR1 in non-DRX 2416A.6.5.3.3.1 Test
Purpose and Environment 2416A.6.5.3.3.2 Test Requirements 2417A.6.5.3.4
Direct SCell activation at SCell addition of known SCell in FR1
2417A.6.5.3.4.1 Test Purpose and Environment 2417A.6.5.3.4.2 Test
Requirements 2424A.6.5.3.5 Direct SCell activation at handover with
known SCell in FR1 2424A.6.5.3.5.1 Test Purpose and Environment
2424A.6.5.3.5.2 Test Requirements 2429A.6.5.3.6 PUCCH SCell Activation
and deactivation of known SCell in FR1 2429A.6.5.3.6.1 Test Purpose and
Environment 2429A.6.5.3.6.2 Test Requirements 2433A.6.5.3.7 SCell
Activation and deactivation of unknown SCell in FR1 in non-DRX
2434A.6.5.3.7.1 Test Purpose and Environment 2434A.6.5.3.7.2 Test
Requirements 2438A.6.5.3.8 SCell Activation and Deactivation of one FR1
known PUCCH SCell and one FR1 unknown SCell with single
activation/deactivation command 2439A.6.5.3.8.1 Test Purpose and
Environment 2439A.6.5.3.8.2 Test Requirements 2443A.6.5.3.9 SCell
Activation and deactivation of unknown PUCCH SCell and unknown DL SCell
in FR1 in non-DRX 2444A.6.5.3.9.1 Test Purpose and Environment
2444A.6.5.3.9.2 Test Requirements 2448A.6.5.3.10 Fast SCell Activation
of known SCell in FR1 in non-DRX for 160ms SCell measurement cycle
2449A.6.5.3.10.1 Test Purpose and Environment 2449A.6.5.3.10.2 Test
Requirements 2452A.6.5.3.11 SCell Activation of known SCell in FR1 in
non-DRX for 640 ms SCell measurement cycle 2452A.6.5.3.11.1 Test Purpose
and Environment 2452A.6.5.3.11.2 Test Requirements 2453A.6.5.4 UE UL
carrier RRC reconfiguration Delay 2453A.6.5.4.1 UE UL carrier RRC
reconfiguration Delay 2453A.6.5.4.1.1 Test Purpose and Environment
2453A.6.5.4.1.2 Test Requirements 2462A.6.5.4.2 Void 2463A.6.5.5 Beam
Failure Detection and Link recovery procedures 2463A.6.5.5.1 Beam
Failure Detection and Link Recovery Test for FR1 PCell configured with
SSB-based BFD and LR in non-DRX mode 2463A.6.5.5.1.1 Test Purpose and
Environment 2463A.6.5.5.2 Beam Failure Detection and Link Recovery Test
for FR1 PCell configured with SSB-based BFD and LR in DRX mode
2469A.6.5.5.2.1 Test Purpose and Environment 2469A.6.5.5.2.2 Test
Requirements 2475A.6.5.5.3 Beam Failure Detection and Link Recovery Test
for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode
2476A.6.5.5.3.1 Test Purpose and Environment 2476A.6.5.5.3.2 Test
Requirements 2481A.6.5.5.4 Beam Failure Detection and Link Recovery Test
for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode
2482A.6.5.5.4.1 Test Purpose and Environment 2482A.6.5.5.4.2 Test
Requirements 2487A.6.5.5.5 Beam Failure Detection and Link Recovery Test
for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in
non-DRX mode 2488A.6.5.5.5.1 Test Purpose and Environment
2488A.6.5.5.5.2 Test Requirements 2492A.6.5.5.6 Beam Failure Detection
and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD
and SSB-based LR in DRX mode 2492A.6.5.5.6.1 Test Purpose and
Environment 2492A.6.5.5.6.2 Test Requirements 2497A.6.5.5.7 TRP Specific
Beam Failure Detection and Link Recovery Test for FR1 PCell configured
with CSI-RS-based BFD and LR in DRX mode 2497A.6.5.5.7.1 Test Purpose
and Environment 2497A.6.5.5.7.2 Test Requirements 2503A.6.5.6 Active BWP
switch 2504A.6.5.6.1 DCI-based and Timer-based Active BWP Switch
2504A.6.5.6.1.1 NR FR1- NR FR1 DL active BWP switch of SCell with
non-DRX in SA 2504A.6.5.6.1.2 NR FR1 DL active BWP switch with non-DRX
in SA 2510A.6.5.6.2 RRC-based Active BWP Switch 2515A.6.5.6.2.1 NR FR1
DL active BWP switch of Cell with non-DRX in SA 2515A.6.5.6.3
Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs
2519A.6.5.6.3.1 NR FR1- NR FR1 DL active BWP switch on multiple CCs with
non-DRX in SA 2519A.6.5.6.4 SCell dormancy switch 2526A.6.5.6.4.1 NR FR1
PCell SCell dormancy switch of single FR1 SCell outside active time
2526A.6.5.6.4.1.1 Test Purpose and Environment 2526A.6.5.6.4.1.2 Test
Requirements 2532A.6.5.6.4.2 NR FR1 PCell SCell dormancy switch of two
FR1 SCells inside active time 2532A.6.5.6.4.2.1 Test Purpose and
Environment 2532A.6.5.6.4.2.2 Test Requirements 2539A.6.5.6.5
Simultaneous RRC-based Active BWP Switch on multiple CCs 2539A.6.5.6.5.1
NR FR1- NR FR1 DL active BWP switch on multiple CCs with non-DRX in SA
2539A.6.5.7 DL interruptions at switching between two uplink carriers
2544A.6.5.7.1 DL interruptions at switching between two uplink carriers
in FDD-TDD CA 2544A.6.5.7.1.1 Test Purpose and Environment
2544A.6.5.7.1.2 Test Requirements 2548A.6.5.7.2 DL interruptions at
switching between two uplink carriers in TDD-TDD CA 2548A.6.5.7.2.1 Test
Purpose and Environment 2548A.6.5.7.2.2 Test Requirements 2552A.6.5.7A
DL interruptions at switching between two uplink carriers with two
transmit antenna connectors 2552A.6.5.7A.1 DL interruptions at switching
between two uplink carriers in FDD-TDD CA 2552A.6.5.7A.1.1 Test Purpose
and Environment 2552A.6.5.7A.1.2 Test Requirements 2556A.6.5.7A.2 DL
interruptions at switching between two uplink carriers in TDD-TDD CA
2556A.6.5.7A.2.1 Test Purpose and Environment 2556A.6.5.7A.2.2 Test
Requirements 2560A.6.5.7B DL interruptions at switching between one
uplink band with one transmit antenna connector and one uplink band with
two transmit antenna connectors 2560A.6.5.7B.1 DL interruptions at
switching between two uplink bands in FDD-TDD CA 2560A.6.5.7B.1.1 Test
Purpose and Environment 2560A.6.5.7B.1.2 Test Requirements
2564A.6.5.7B.2 DL interruptions at switching between two uplink bands in
TDD-TDD CA 2564A.6.5.7B.2.1 Test Purpose and Environment
2564A.6.5.7B.2.2 Test Requirements 2568A.6.5.7C DL interruptions at
switching between two uplink bands with two transmit antenna connectors
2568A.6.5.7C.1 DL interruptions at switching between two uplink bands
with two transmit antenna connectors in FDD-TDD CA 2568A.6.5.7C.1.1 Test
Purpose and Environment 2568A.6.5.7C.1.2 Test Requirements
2572A.6.5.7C.2 DL interruptions at switching between two uplink bands
with two transmit antenna connectors in TDD-TDD CA 2573A.6.5.7C.2.1 Test
Purpose and Environment 2573A.6.5.7C.2.2 Test Requirements 2577A.6.5.8
UE specific CBW change 2578A.6.5.8.1 UE specific CBW change on PCell in
FR1 in non-DRX 2578A.6.5.8.1.1 Test Purpose and Environment
2578A.6.5.8.1.2 Test Requirements 2582A.6.5.9 Pathloss reference signal
switching delay 2582A.6.5.9.1 MAC-CE based pathloss reference signal
switch delay 2582A.6.5.9.1.1 Test Purpose and Environment
2582A.6.5.9.1.2 Test Requirements 2585A.6.6 Measurement procedure
2586A.6.6.1 Intra-frequency Measurements 2586A.6.6.1.1 SA event
triggered reporting tests without gap under non-DRX 2586A.6.6.1.1.1 Test
purpose and Environment 2586A.6.6.1.1.2 Test parameters 2586A.6.6.1.1.3
Test Requirements 2590A.6.6.1.2 SA event triggered reporting tests
without gap under DRX 2590A.6.6.1.2.1 Test purpose and Environment
2590A.6.6.1.2.2 Test parameters 2590A.6.6.1.2.3 Test Requirements
2594A.6.6.1.3 SA event triggered reporting tests with per-UE gaps under
non-DRX 2594A.6.6.1.3.1 Test purpose and Environment 2594A.6.6.1.3.2
Test parameters 2594A.6.6.1.3.3 Test Requirements 2598A.6.6.1.4 SA event
triggered reporting tests with per-UE gaps under DRX 2598A.6.6.1.4.1
Test purpose and Environment 2598A.6.6.1.4.2 Test parameters
2598A.6.6.1.4.3 Test Requirements 2602A.6.6.1.5 SA event triggered
reporting tests without gap under non-DRX with SSB index reading
2602A.6.6.1.5.1 Test purpose and Environment 2602A.6.6.1.5.2 Test
parameters 2602A.6.6.1.5.3 Test Requirements 2604A.6.6.1.6 SA event
triggered reporting tests with per-UE gaps under non-DRX with SSB index
reading 2605A.6.6.1.6.1 Test purpose and Environment 2605A.6.6.1.6.2
Test parameters 2605A.6.6.1.6.3 Test Requirements 2606A.6.6.1.7 SA event
triggered reporting tests under DRX for UE configured with
highSpeedMeasFlag-r16 2607A.6.6.1.7.1 Test purpose and Environment
2607A.6.6.1.7.2 Test parameters 2607A.6.6.1.7.3 Test Requirements
2611A.6.6.1.8 SA event triggered reporting tests without gap under DRX
for UE configured with highSpeedMeasCA-Scell-r17 2611A.6.6.1.8.1 Test
purpose and Environment 2611A.6.6.1.8.2 Test parameters 2611A.6.6.1.8.3
Test Requirements 2616A.6.6.2 Inter-frequency Measurements 2616A.6.6.2.1
SA event triggered reporting tests for FR1 without SSB time index
detection when DRX is not used 2616A.6.6.2.1.1 Test Purpose and
Environment 2616A.6.6.2.1.2 Test Requirements 2620A.6.6.2.2 SA event
triggered reporting tests for FR1 without SSB time index detection when
DRX is used 2620A.6.6.2.2.1 Test Purpose and Environment 2620A.6.6.2.2.2
Test Requirements 2624A.6.6.2.3 Void 2625A.6.6.2.4 Void 2625A.6.6.2.5 SA
event triggered reporting tests for FR1 with SSB time index detection
when DRX is not used 2625A.6.6.2.5.1 Test Purpose and Environment
2625A.6.6.2.5.2 Test Requirements 2629A.6.6.2.6 SA event triggered
reporting tests for FR1 with SSB time index detection when DRX is used
2629A.6.6.2.6.1 Test Purpose and Environment 2629A.6.6.2.6.2 Test
Requirements 2633A.6.6.2.7 Void 2633A.6.6.2.8 Void 2633A.6.6.2.9 SA
event triggered reporting tests with additional mandatory gap pattern
2633A.6.6.2.9.1 Test Purpose and Environment 2633A.6.6.2.9.2 Test
Requirements 2637A.6.6.2.10 SA event triggered reporting tests for FR1
when DRX is used 2637A.6.6.2.10.1 Test Purpose and Environment
2637A.6.6.2.10.2 Test Requirements 2641A.6.6.2.12 SA event triggered
reporting tests for FR1 without SSB time index detection when DRX is
used for UE configured with highSpeedMeasInterFreq-r17 2645A.6.6.2.12.1
Test Purpose and Environment 2645A.6.6.2.12.2 Test Requirements
2649A.6.6.3 Inter-RAT Measurements 2649A.6.6.3.1 SA NR - E-UTRAN
event-triggered reporting in non-DRX in FR1 2649A.6.6.3.1.1 Test Purpose
and Environment 2649A.6.6.3.1.2 Test Requirements 2655A.6.6.3.2 SA NR -
E-UTRAN event-triggered reporting in DRX in FR1 2655A.6.6.3.2.1 Test
Purpose and Environment 2655A.6.6.3.2.2 Test Requirements 2662A.6.6.3.3
SA NR - E-UTRAN event-triggered reporting in DRX in FR1 for UE
configured with highSpeedMeasFlag-r16 2662A.6.6.3.3.1 Test Purpose and
Environment 2662A.6.6.3.3.2 Test Requirements 2669A.6.6.4 L1-RSRP
measurement for beam reporting 2669A.6.6.4.1 SSB based L1-RSRP
measurement when DRX is not used 2669A.6.6.4.1.1 Test Purpose and
Environment 2669A.6.6.4.1.2 Test parameters 2669A.6.6.4.1.3 Test
Requirements 2672A.6.6.4.2 SSB based L1-RSRP measurement when DRX is
used 2672A.6.6.4.2.1 Test Purpose and Environment 2672A.6.6.4.2.2 Test
parameters 2673A.6.6.4.2.3 Test Requirements 2676A.6.6.4.3 CSI-RS based
L1-RSRP measurement when DRX is not used 2676A.6.6.4.3.1 Test Purpose
and Environment 2676A.6.6.4.3.2 Test parameters 2677A.6.6.4.3.3 Test
Requirements 2680A.6.6.4.4 CSI-RS based L1-RSRP measurement when DRX is
used 2680A.6.6.4.4.1 Test Purpose and Environment 2680A.6.6.4.4.2 Test
parameters 2681A.6.6.4.4.3 Test Requirements 2684A.6.6.4.5 SSB based
L1-RSRP measurement when DRX is used for UE configured with
*highSpeedMeasFlag-r16* 2684A.6.6.4.5.1 Test Purpose and Environment
2684A.6.6.4.5.2 Test parameters 2685A.6.6.4.5.3 Test Requirements
2688A.6.6.4.6 Inter-cell SSB based L1-RSRP measurements on FR1 PCell
when DRX is used 2688A.6.6.4.6.1 Test Purpose and Environment
2688A.6.6.4.6.2 Test parameters 2689A.6.6.4.6.3 Test Requirements
2692A.6.6.5 Inter-RAT UTRAN FDD measurements 2693A.6.6.5.1 SA NR - UTRAN
FDD event-triggered reporting in non-DRX in FR1 2693A.6.6.5.1.1 Test
Purpose and Environment 2693A.6.6.5.1.2 Test Requirements 2696A.6.6.6
CLI measurements 2696A.6.6.6.1 SRS-RSRP measurement with DRX
2696A.6.6.6.1.1 Test Purpose and Environment 2696A.6.6.6.1.2 Test
Parameters 2697A.6.6.6.1.3 Test Requirements 2700A.6.6.6.2 CLI-RSSI
measurement with DRX 2700A.6.6.6.2.1 Test Purpose and Environment
2700A.6.6.6.2.2 Test Parameters 2701A.6.6.6.2.3 Test Requirements
2703A.6.6.7 NR measurements with autonomous gaps 2703A.6.6.7.1 SA
intra-frequency CGI identification of NR neighbor cell in FR1
2703A.6.6.7.1.1 Test Purpose and Environment 2703A.6.6.7.1.2 Test
Parameters 2703A.6.6.7.1.3 Test Requirements 2707A.6.6.7.2
Identification of a new CGI of inter-RAT E-UTRA cell using autonomous
gaps in NR SA 2707A.6.6.7.2.1 Test Purpose and Environment
2707A.6.6.7.2.2 Test Requirements 2710A.6.6.8 L1-SINR measurement for
beam reporting 2711A.6.6.8.2 L1-SINR measurement with SSB based CMR and
dedicated IMR when DRX is not used 2713A.6.6.8.2.1 Test Purpose and
Environment 2713A.6.6.8.2.2 Test parameters 2714A.6.6.8.2.3 Test
Requirements 2718A.6.6.8.3 L1-SINR measurement with CSI-RS based CMR and
dedicated IMR configured when DRX is not used 2718A.6.6.8.3.1 Test
Purpose and Environment 2718A.6.6.8.3.2 Test parameters 2719A.6.6.8.3.3
Test Requirements 2721A.6.6.9 Idle Mode CA/DC Measurements 2721A.6.6.9.1
SA Idle mode CA/DC measurement for FR1 2721A.6.6.9.1.1 Test Purpose and
Environment 2721A.6.6.9.1.2 Test Requirements 2728A.6.6.10 CSI-RS based
intra-frequency Measurements 2728A.6.6.10.1 SA event triggered reporting
tests without gap under non-DRX 2728A.6.6.10.1.1 Test purpose and
Environment 2728A.6.6.10.1.2 Test Requirements 2732A.6.6.11 CSI-RS based
inter-frequency Measurements 2732A.6.6.11.1 SA event triggered reporting
tests with gap under DRX 2732A.6.6.11.1.1 Test Purpose and Environment
2732A.6.6.11.1.2 Test Requirements 2736A.6.6.12 RSTD measurements
2736A.6.6.12.1 NR RSTD measurement reporting delay test case for single
positioning frequency layer in FR1 SA 2736A.6.6.12.1.1 Test Purpose and
Environment 2736A.6.6.12.1.2 Test Requirements 2743A.6.6.12.2 NR RSTD
measurement reporting delay test case for dual positioning frequency
layers in FR1 SA 2744A.6.6.12.2.1 Test Purpose and Environment
2744A.6.6.12.2.2 Test Requirements 2750A.6.6.12.3 NR RSTD measurement
reporting delay test case for single positioning frequency layer with
reduced number of samples in FR1 SA 2750A.6.6.12.3.1 Test Purpose and
Environment 2750A.6.6.12.3.2 Test Requirements 2756A.6.6.12.4 NR RSTD
measurement reporting delay test case for single positioning frequency
layer in FR1 SA without measurement gap 2757A.6.6.12.4.1 Test Purpose
and Environment 2757A.6.6.12.4.2 Test Requirements 2760A.6.6.12.5 NR
RSTD measurement reporting delay test case for single positioning
frequency layer in FR1 SA in RRC\_CONNECTED state with Rx TEG
2761A.6.6.12.5.1 Test Purpose and Environment 2761A.6.6.12.5.2 Test
Requirements 2765A.6.6.13 PRS-RSRP measurements 2765A.6.6.13.1 PRS-RSRP
reporting delay test case for single positioning frequency layer
2765A.6.6.13.1.1 Test purpose and Environment 2765A.6.6.13.1.2 Test
Requirements 2769A.6.6.13.2 PRS-RSRP reporting delay test case for dual
positioning frequency layer 2769A.6.6.13.2.1 Test purpose and
Environment 2769A.6.6.13.2.2 Test Requirements 2773A.6.6.13.3 PRS-RSRP
reporting delay test case for reduced number of samples 2773A.6.6.13.3.1
Test purpose and Environment 2773A.6.6.13.3.2 Test Requirements
2776A.6.6.13.4 PRS-RSRP reporting delay test case for single positioning
frequency layer outside MG 2776A.6.6.13.4.1 Test purpose and Environment
2776A.6.6.14 UE Rx-Tx time difference measurements 2781A.6.6.14.1 UE
Rx-Tx time difference measurement for single positioning frequency layer
in FR1 SA 2781A.6.6.14.1.1 Test purpose and environment 2781A.6.6.14.1.2
Test requirements 2785A.6.6.14.2 UE Rx-Tx time difference measurement
for dual positioning frequency layers in FR1 SA 2785A.6.6.14.2.1 Test
purpose and environment 2785A.6.6.14.2.2 Test requirements
2790A.6.6.14.3 UE Rx-Tx time difference measurement for single
positioning frequency layer in FR1 SA with reduced sample number
2790A.6.6.14.3.1 Test purpose and environment 2790A.6.6.14.3.2 Test
requirements 2793A.6.6.14.4 UE Rx-Tx time difference measurement without
gaps in FR1 SA 2794A.6.6.14.4.1 Test purpose and environment
2794A.6.6.14.4.2 Test requirements 2796A.6.6.14.5 UE Rx-Tx time
difference measurement for single positioning frequency layer in FR1 SA
with multiple RxTx TEGs 2797A.6.6.14.4.1 Test purpose and environment
2797A.6.6.14.4.2 Test requirements 2801A.6.6.15 Idle Mode measurements
of inter-RAT DC candidate cells for early reporting 2801A.6.6.15.1 Test
Purpose and Environment 2801A.6.6.15.2 Test Requirements 2808A.6.6.16
PRS-RSRPP measurements 2809A.6.6.16.1 PRS-RSRPP reporting delay test
case for single positioning frequency layer in FR1 in RRC\_CONNECTED
state 2809A.6.6.16.1.1 Test purpose and Environment 2809A.6.6.16.1.2
Test Requirements 2811A.6.6.16.2 PRS-RSRPP reporting delay test case
with reduced number of samples for single positioning frequency layer in
FR1 in RRC\_CONNECTED state 2811A.6.6.16.2.1 Test purpose and
Environment 2811A.6.6.16.2.2 Test Requirements 2814A.6.6.16.3 PRS-RSRPP
reporting delay test case for single positioning frequency layer in FR1
in RRC\_CONNECTED state without measurement gap 2814A.6.6.16.3.1 Test
purpose and Environment 2814A.6.6.16.3.2 Test Requirements 2817A.6.6.17
SA event triggered reporting tests with Pre-MG 2817A.6.6.17.1 SA event
triggered reporting tests with autonomous activation/deactivation Pre-MG
2817A.6.6.17.1.1 Test purpose and Environment 2817A.6.6.17.1.2 Test
parameters 2817A.6.6.17.1.3 Test Requirements 2821A.6.6.17.2 SA event
triggered reporting tests with pre-configured measurement gaps and
network-controlled activation/deactivation 2821A.6.6.17.2.1 Test purpose
and Environment 2821A.6.6.17.2.2 Test parameters 2821A.6.6.17.2.3 Test
Requirements 2826A.6.6.17.3 Void 2826A.6.6.17.3.1 Void 2826A.6.6.17.3.2
Void 2826A.6.6.17.3.3 Void 2826A.6.6.18 SA event triggered reporting
tests with concurrent gaps 2826A.6.6.18.1 SA event triggered reporting
tests for FR1 concurrent gaps with non-overalpping scenario for
SSB-based measurements in both inter-frequency layers 2826A.6.6.18.1.1
Test Purpose and Environment 2826A.6.6.18.1.2 Test Requirements
2830A.6.6.18.2 SA event triggered reporting tests for FR1 concurrent gap
with partially partial overalpping scenario for SSB-based measurements
in both inter-frequency layers 2830A.6.6.18.2.1 Test Purpose and
Environment 2830A.6.6.18.2.2 Test Requirements 2834A.6.6.18.3 SA NR -
E-UTRAN and NR FR1 concurrent event-triggered reporting in non-DRX in
FR1 2834A.6.6.18.3.1 Test Purpose and Environment 2834A.6.6.18.3.2 Test
Requirements 2841A.6.6.18.4 SA event triggered reporting tests for PRS
and SSB measurement in FR1 without SSB time index detection when DRX is
not used 2841A.6.6.18.4.1 Test Purpose and Environment 2841A.6.6.18.4.2
Test Requirements 2845A.6.6.19 SA event triggered reporting tests with
NCSG 2846A.6.6.19.1 SA event triggered reporting tests with NCSG under
non-DRX in FR1 2846A.6.6.19.1.1 Test purpose and Environment
2846A.6.6.19.1.2 Test parameters 2846A.6.6.19.1.3 Test Requirements
2850A.6.6.19.2 SA event triggered reporting tests for FR1 with NCSG for
inter-frequency measurement 2850A.6.6.19.2.1 Test Purpose and
Environment 2850A.6.6.19.2.2 Test parameters 2850A.6.6.19.2.3 Test
Requirements 2854A.6.6.19.3 SA NR - E-UTRAN event-triggered reporting in
non-DRX in FR1 with NCSG 2854A.6.6.19.3.1 Test Purpose and Environment
2854A.6.6.19.3.2 Test parameters 2855A.6.6.19.3.3 Test Requirements
2860A.6.6.19.4 Event triggered reporting on SCC with deactivated SCell
test with per-UE NCSG under non-DRX 2860A.6.6.19.4.1 Test purpose and
Environment 2860A.6.6.19.4.2 Test parameters 2860A.6.6.19.4.3 Test
Requirements 2863A.6.6.20 UE Rx-Tx time difference measurement for
propagation delay compensation 2863A.6.6.20.1 Test purpose and
environment 2863A.6.6.20.2 Test requirements 2867A.6.6.21 UE Rx-Tx time
difference measurement with TRS for RTT-based PDC in FR1 SA
2867A.6.6.21.1 Test purpose and environment 2867A.6.6.21.2 Test
requirements 2869A.6.7 Measurement Performance requirements 2870A.6.7.1
SS-RSRP 2870A.6.7.1.1 SA: intra-frequency case measurement accuracy with
FR1 serving cell and FR1 target cell 2870A.6.7.1.1.1 Test Purpose and
Environment 2870A.6.7.1.1.2 Test parameters 2870A.6.7.1.1.3 Test
Requirements 2875A.6.7.1.2 SA inter-frequency case measurement accuracy
with FR1 serving cell and FR1 target cell 2875A.6.7.1.2.1 Test Purpose
and Environment 2875A.6.7.1.2.2 Test parameters 2875A.6.7.1.2.3 Test
Requirements 2879A.6.7.1.3 Void 2879A.6.7.2 SS-RSRQ 2879A.6.7.2.1 SA:
Intra-frequency measurement accuracy with FR1 serving cell and FR1
target cell 2879A.6.7.2.1.1 Test Purpose and Environment 2879A.6.7.2.1.2
Test Parameters 2880A.6.7.2.1.3 Test Requirements 2884A.6.7.2.2 SA
Inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell 2884A.6.7.2.2.1 Test Purpose and Environment 2884A.6.7.2.2.2
Test Parameters 2884A.6.7.2.2.3 Test Requirements 2889A.6.7.3 SS-SINR
2889A.6.7.3.1 SA intra-frequency measurement accuracy with FR1 serving
cell and FR1 target cell 2889A.6.7.3.1.1 Test Purpose and Environment
2889A.6.7.3.1.2 Test Parameters 2890A.6.7.3.1.3 Test Requirements
2894A.6.7.3.2 SA Inter-frequency measurement accuracy with FR1 serving
cell and FR1 target cell 2895A.6.7.3.2.1 Test Purpose and Environment
2895A.6.7.3.2.2 Test Parameters 2895A.6.7.3.2.3 Test Requirements
2899A.6.7.4 L1-RSRP measurement for beam reporting 2900A.6.7.4.1 SSB
based L1-RSRP measurement 2900A.6.7.4.1.1 Test Purpose and Environment
2900A.6.7.4.1.2 Test parameters 2900A.6.7.4.1.3 Test Requirements
2904A.6.7.4.2 CSI-RS based L1-RSRP measurement on resource set with
repetition off 2904A.6.7.4.2.1 Test Purpose and Environment
2904A.6.7.4.2.2 Test parameters 2905A.6.7.4.2.3 Test Requirements
2909A.6.7.5 E-UTRAN RSRP 2909A.6.7.5.1 SA: inter-RAT measurement
accuracy with FR1 serving cell 2909A.6.7.5.1.1 Test Purpose and
Environment 2909A.6.7.5.1.2 Test parameters 2910A.6.7.5.1.3 Test
Requirements 2916A.6.7.6 E-UTRAN RSRQ 2917A.6.7.6.1 SA: inter-RAT
measurement accuracy with FR1 serving cell 2917A.6.7.6.1.1 Test Purpose
and Environment 2917A.6.7.6.1.2 Test parameters 2917A.6.7.6.1.3 Test
Requirements 2922A.6.7.7 E-UTRAN RS-SINR 2923A.6.7.7.1 SA: inter-RAT
measurement accuracy with FR1 serving cell 2923A.6.7.7.1.1 Test Purpose
and Environment 2923A.6.7.7.1.2 Test parameters 2923A.6.7.7.1.3 Test
Requirements 2929A.6.7.8 CLI measurements 2930A.6.7.8.1 SA SRS-RSRP
measurement accuracy with FR1 serving cell 2930A.6.7.8.1.1 Test Purpose
and Environment 2930A.6.7.8.1.2 Test parameters 2930A.6.7.8.1.3 Test
Requirements 2936A.6.7.8.2 SA CLI-RSSI measurement accuracy with FR1
serving cell 2936A.6.7.8.2.1 Test Purpose and Environment
2936A.6.7.8.2.2 Test parameters 2937A.6.7.8.2.3 Test Requirements
2940A.6.7.9 L1-SINR measurement for beam reporting 2941A.6.7.9.2 L1-SINR
measurement with SSB based CMR and dedicated IMR 2945A.6.7.9.2.1 Test
Purpose and Environment 2945A.6.7.9.2.2 Test parameters 2946A.6.7.9.2.3
Test Requirements 2951A.6.7.9.3 L1-SINR measurement with CSI-RS based
CMR and dedicated IMR 2951A.6.7.9.3.1 Test Purpose and Environment
2951A.6.7.9.3.2 Test parameters 2951A.6.7.9.3.3 Test Requirements
2956A.6.7.10 CSI-RSRP 2956A.6.7.10.1 SA: intra-frequency case
measurement accuracy with FR1 serving cell and FR1 target cell
2956A.6.7.9.10.1 Test Purpose and Environment 2956A.6.7.9.10.2 Test
parameters 2957A.6.7.10.1.3 Test Requirements 2962A.6.7.10.2 SA
inter-frequency case measurement accuracy with FR1 serving cell and FR1
target cell 2962A.6.7.9.10.1 Test Purpose and Environment
2962A.6.7.10.2.2 Test parameters 2962A.6.7.10.2.3 Test Requirements
2968A.6.7.11 CSI-RSRQ 2968A.6.7.11.1 SA: Intra-frequency measurement
accuracy with FR1 serving cell and FR1 target cell 2968A.6.7.11.1.1 Test
Purpose and Environment 2968A.6.7.11.1.2 Test Parameters
2968A.6.7.11.1.3 Test Requirements 2973A.6.7.11.2 SA Inter-frequency
measurement accuracy with FR1 serving cell and FR1 target cell
2973A.6.7.11.2.1 Test Purpose and Environment 2973A.6.7.11.2.2 Test
Parameters 2973A.6.7.11.2.3 Test Requirements 2980A.6.7.12 CSI-SINR
2980A.6.7.12.1 SA intra-frequency measurement accuracy with FR1 serving
cell and FR1 target cell 2980A.6.7.12.1.1 Test Purpose and Environment
2980A.6.7.12.1.2 Test Parameters 2980A.6.7.12.1.3 Test Requirements
2985A.6.7.12.2 SA Inter-frequency measurement accuracy with FR1 serving
cell and FR1 target cell 2985A.6.7.12.2.1 Test Purpose and Environment
2985A.6.7.12.2.2 Test Parameters 2985A.6.7.12.2.3 Test Requirements
2991A.6.7.13 RSTD measurements 2991A.6.7.13.1 RSTD measurement accuracy
test case for single positioning frequency layer 2991A.6.7.13.1.1 Test
purpose and Environment 2991A.6.7.13.1.2 Test Requirements
2994A.6.7.13.2 RSTD measurement accuracy test case for dual positioning
frequency layer 2994A.6.7.13.2.1 Test purpose and Environment
2994A.6.7.13.2.2 Test Requirements 2998A.6.7.13.3 RSTD measurement
accuracy test case with reduced number of samples for single positioning
frequency layer in FR1 in RRC\_CONNECTED state 2998A.6.7.13.3.1 Test
purpose and Environment 2998A.6.7.13.3.2 Test Requirements
3000A.6.7.13.4 RSTD measurement accuracy test case with Rx TEG
3001A.6.7.14 PRS-RSRP measurements 3003A.6.7.14.1 SA: measurement
accuracy with PRS in FR1 3003A.6.7.14.1.1 Test Purpose and Environment
3003A.6.7.14.1.2 Test parameters 3003A.6.7.14.1.3 Test Requirements
3007A.6.7.14.2 SA: measurement accuracy with PRS in FR1 with reduced
sample number 3007A.6.7.14.2.1 Test Purpose and Environment
3007A.6.7.14.2.2 Test parameters 3007A.6.7.14.2.3 Test Requirements
3010A.6.7.14.3 Void 3010A.6.7.14.3.1 Void 3010A.6.7.14.3.2 Void
3010A.6.7.14.3.3 Void 3010A.6.7.15 UE Rx-Tx time difference measurements
3010A.6.7.15.1 UE Rx-Tx time difference measurement accuracy for single
positioning frequency layer in FR1 SA 3010A.6.7.15.1.1 Test purpose and
environment 3010A.6.7.15.1.2 Test parameters 3011A.6.7.15.1.3 Test
requirements 3014A.6.7.15.2 UE Rx-Tx time difference measurement
accuracy with reduced number of samples in FR1 SA 3015A.6.7.15.2.1 Test
purpose and environment 3015A.6.7.15.2.2 Test parameters
3015A.6.7.15.2.3 Test requirements 3017A.6.7.15.3 UE Rx-Tx time
difference measurement accuracy with RxTx TEG 3017A.6.7.15.3.1 Test
purpose and environment 3017A.6.7.15.3.2 Test parameters
3018A.6.7.15.3.3 Test requirements 3021A.6.7.16 PRS-RSRPP measurements
3021A.6.7.16.1 SA: measurement accuracy with PRS in FR1 3021A.6.7.16.1.1
Test Purpose and Environment 3021A.6.7.16.1.2 Test parameters
3022A.6.7.16.1.3 Test Requirements 3026A.6.7.16.2 SA: measurement
accuracy with reduced PRS samples in FR1 3026A.6.7.16.2.1 Test Purpose
and Environment 3026A.6.7.16.2.2 Test parameters 3026A.6.8 Measurement
procedure in RRC\_INACTIVE 3030A.6.8.1 RSTD measurements 3030A.6.8.1.1
NR RSTD measurement reporting delay test case for single positioning
frequency layer in FR1 SA in RRC\_INACTIVE state 3030A.6.8.1.1.1 Test
Purpose and Environment 3030A.6.8.1.1.2 Test Requirements 3033A.6.8.1.2
NR RSTD measurement reporting delay test case with reduced number of
samples in RRC\_INACTIVE, FR1 SA 3033A.6.8.1.2.1 Test Purpose and
Environment 3033A.6.8.1.2.2 Test Requirements 3038A.6.8.2 PRS-RSRP
measurements 3038A.6.8.2.1 PRS-RSRP reporting delay test case for single
positioning frequency layer in RRC\_INACTIVE 3038A.6.8.2.1.1 Test
purpose and Environment 3038A.6.8.2.1.2 Test Requirements 3040A.6.8.2.2
PRS-RSRP reporting delay test case with reduced number of samples in
RRC\_INACTIVE 3041A.6.8.2.2.1 Test purpose and Environment
3041A.6.**8.2.2**.2 Test Requirements 3045A.6.8.3 UE Rx-Tx time
difference measurements 3045A.6.8.3.1 UE Rx-Tx time difference
measurement for single positioning frequency layer in FR1 SA
3045A.6.8.3.1.1 Test purpose and environment 3045A.6.8.3.1.2 Test
requirements 3049A.6.8.3.2 UE Rx-Tx time difference measurement with
reduced number of samples in RRC\_INACTIVE, FR1 SA 3049A.6.8.3.2.1 Test
purpose and environment 3049A.6.**8.3.2**.2 Test requirements
3052A.6.8.4 PRS-RSRPP measurements 3052A.6.8.4.1 PRS-RSRPP reporting
delay test case for single positioning frequency layer in FR1 in
RRC\_INACTIVE state 3052A.6.8.4.1.1 Test purpose and Environment
3052A.6.8.4.1.2 Test Requirements 3055A.6.8.4.2 PRS-RSRPP reporting
delay test case for single positioning frequency layer in FR1 in
RRC\_INACTIVE state for reduced number of samples 3055A.6.8.4.2.1 Test
purpose and Environment 3055A.6.8.4.2.2 Test Requirements 3057A.6.9
Measurement performance requirements in RRC\_INACTIVE 3058A.6.9.1 RSTD
measurements 3058A.6.9.1.1 RSTD measurement accuracy test case for
single positioning frequency layer in FR1 in RRC\_INACTIVE state
3058A.6.9.1.1.1 Test purpose and Environment 3058A.6.9.1.1.2 Test
Requirements 3060A.6.9.1.2 RSTD measurement accuracy test case with
reduced number of samples for single positioning frequency layer in FR1
in RRC\_INACTIVE state 3060A.6.9.1.2.1 Test purpose and Environment
3060A.6.9.1.2.2 Test Requirements 3062A.6.9.2 PRS-RSRP measurements
3062A.6.9.2.1 SA: measurement accuracy with PRS in FR1 in RRC\_INACTIVE
3062A.6.9.2.1.1 Test Purpose and Environment 3062A.6.9.2.1.2 Test
parameters 3062A.6.9.2.1.3 Test Requirements 3066A.6.9.2.2 SA:
measurement accuracy with PRS in FR1 with reduced number of samples in
RRC\_INACTIVE state 3066A.6.9.2.2.1 Test Purpose and Environment
3066A.6.9.2.2.2 Test parameters 3066A.6.9.2.2.3 Test Requirements
3068A.6.9.3 UE Rx-Tx time difference measurements 3069A.6.9.3.1.1 UE
Rx-Tx time difference measurement accuracy in FR1 SA 3069A.6.9.3.1.1.1
Test purpose and environment 3069A.6.9.3.1.1.2 Test parameters
3069A.6.9.3.1.1.3 Test requirements 3071A.6.9.3.2 UE Rx-Tx time
difference measurement accuracy with reduced number of samples
3071A.6.9.3.2.1 Test purpose and environment 3071A.6.9.3.2.2 Test
parameters 3071A.6.9.3.2.3 Test requirements 3074A.6.9.4 PRS-RSRPP
measurements 3074A.6.9.4.1 SA: PRS-RSRPP measurement accuracy in FR1 in
RRC INACTIVE 3074A.6.9.4.1.1 Test Purpose and Environment
3074A.6.9.4.1.2 Test parameters 3074A.6.9.4.1.3 Test Requirements
3078A.6.9.4.2 SA: measurement accuracy with reduced PRS samples in FR1
in RRC INACTIVE 3078A.6.9.4.2.1 Test Purpose and Environment
3078A.6.9.4.2.2 Test parameters 3078A.6.9.4.2.3 Test Requirements
3080A.7 NR standalone tests with one or more NR cells in FR2 3076A.7.1
SA: RRC\_IDLE state mobility 3076A.7.1.1 Cell re-selection to NR
3076A.7.1.1.1 Cell reselection to FR2 intra-frequency NR case
3076A.7.1.1.1.1 Test Purpose and Environment 3076A.7.1.1.1.2 Test
Parameters 3076A.7.1.1.1.3 Test Requirements 3079A.7.1.1.2 Cell
reselection to FR2 inter-frequency NR case 3080A.7.1.1.2.1 Test Purpose
and Environment 3080A.7.1.1.2.2 Test Parameters 3080A.7.1.1.2.3 Test
Requirements 3082A.7.1.1.3 Cell reselection to FR2 intra-frequency NR
case for UE fulfilling low mobility relaxed measurement criterion
3083A.7.1.1.3.1 Test Purpose and Environment 3083A.7.1.1.3.2 Test
Parameters 3083A.7.1.1.3.3 Test Requirements 3086A.7.1.1.4 Cell
reselection to FR2 intra-frequency NR case for UE fulfilling not-at-cell
edge relaxed measurement criterion 3086A.7.1.1.4.1 Test Purpose and
Environment 3086A.7.1.1.4.2 Test Parameters 3086A.7.1.1.4.3 Test
Requirements 3089A.7.1.1.5 Cell reselection to FR2 inter-frequency NR
case for UE fulfilling low mobility relaxed measurement criterion
3089A.7.1.1.5.1 Test Purpose and Environment 3089A.7.1.1.5.2 Test
Parameters 3089A.7.1.1.5.3 Test Requirements 3092A.7.1.1.6 Cell
reselection to FR2 inter-frequency NR case for UE fulfilling not-at-cell
edge relaxed measurement criterion 3093A.7.1.1.6.1 Test Purpose and
Environment 3093A.7.1.1.6.2 Test Parameters 3093A.7.1.1.6.3 Test
Requirements 3096A.7.1.1.7 Cell reselection to FR2 intra-frequency NR
case for FR2 power class 6 UE configured with *highSpeedMeasFlagFR2-r17*
3097A.7.1.1.7.1 Test Purpose and Environment 3097A.7.1.1.7.2 Test
Parameters 3097A.7.1.1.7.3 Test Requirements 3101A.7.2 SA: RRC\_INACTIVE
state mobility 3101A.7.2.1 Small Data Transmission 3101A.7.2.1.1 TA
validation for CG-SDT in FR2 3101A.7.2.1.1.1 Test Purpose and
Environment 3101A.7.2.1.1.2 Test Requirements 3105A.7.3 RRC\_CONNECTED
state mobility 3105A.7.3.1 Handover 3105A.7.3.1.1 Inter-frequency
handover from FR1 to FR2; unknown target cell 3105A.7.3.1.1.1 Test
Purpose and Environment 3105A.7.3.1.1.2 Test Parameters 3105A.7.3.1.1.3
Test Requirements 3109A.7.3.1.2 Intra-frequency handover from FR2 to
FR2; unknown target cell 3109A.7.3.1.2.1 Test Purpose and Environment
3109A.7.3.1.2.2 Test Parameters 3109A.7.3.1.2.3 Test Requirements
3112A.7.3.1.3 Inter-frequency handover from FR2 to FR2; unknown target
cell 3112A.7.3.1.3.1 Test Purpose and Environment 3112A.7.3.1.3.2 Test
Parameters 3112A.7.3.1.3.3 Test Requirements 3113A.7.3.1.4 Inter-band
inter-frequency synchronous DAPS handover from FR1 to FR2
3114A.7.3.1.4.1 Test Purpose and Environment 3114A.7.3.1.4.2 Test
Parameters 3114A.7.3.1.4.3 Test Requirements 3121A.7.3.1.5 Inter-band
inter-frequency asynchronous DAPS handover from FR1 to FR2
3121A.7.3.1.5.1 Test Purpose and Environment 3121A.7.3.1.5.2 Test
Parameters 3121A.7.3.1.5.3 Test Requirements 3128A.7.3.1.6 Handover with
PSCell from SA to EN-DC with; unknown FR2 target PScell 3128A.7.3.1.6.1
Test Purpose and Environment 3128A.7.3.1.6.2 Test Parameters
3128A.7.3.1.6.3 Test Requirements 3137A.7.3.1.7 HO with PSCell from FR1
NR-SA to EN-DC with known E-UTRA PCell and known FR2 PSCell
3138A.7.3.1.7.1 Test purpose and environment 3138A.7.3.1.7.2 Test
Requirements 3143A.7.3.1.8 NR PSCell change delay in HO with PSCell from
NR-DC to NR-DC 3144A.7.3.1.8.1 Test Purpose and Environment
3144A.7.3.1.8.2 Test Requirements 3149A.7.3.1.9 Intra-frequency handover
from FR2-2 to FR2-2; unknown target cell 3149A.7.3.1.9.1 Test Purpose
and Environment 3149A.7.3.1.9.2 Test Parameters 3149A.7.3.1.9.3 Test
Requirements 3152A.7.3.1.10 Inter-frequency handover from FR2-2 to
FR2-2; unknown target cell 3152A.7.3.1.10.1 Test Purpose and Environment
3152A.7.3.1.10.2 Test Parameters 3152A.7.3.1.10.3 Test Requirements
3156A.7.3.1.11 Inter-frequency handover from FR1 to FR2-2; unknown
target cell 3156A.7.3.1.11.1 Test Purpose and Environment
3156A.7.3.1.11.2 Test Parameters 3156A.7.3.1.11.3 Test Requirements
3160A.7.3.2 RRC Connection Mobility Control 3160A.7.3.2.1 SA: RRC
Re-establishment 3160A.7.3.2.1.1 Intra-frequency RRC Re-establishment in
FR2 3160A.7.3.2.1.2 Inter-frequency RRC Re-establishment in FR2
3163A.7.3.2.1.3 Intra-frequency RRC Re-establishment in FR2 without
serving cell timing 3166A.7.3.2.1.3.1 Test Purpose and Environment
3166A.7.3.2.1.3.2 Test Requirements 3168A.7.3.2.1.4 Intra-frequency RRC
Re-establishment in FR2-2 3169A.7.3.2.1.4.1 Test Purpose and Environment
3169A.7.3.2.1.4.2 Test Requirements 3171A.7.3.2.1.5 Inter-frequency RRC
Re-establishment in FR2-2 3172A.7.3.2.1.5.1 Test Purpose and Environment
3172A.7.3.2.1.5.2 Test Requirements 3175A.7.3.2.1.6 Intra-frequency RRC
Re-establishment in FR2-2 without serving cell timing 3175A.7.3.2.1.6.1
Test Purpose and Environment 3175A.7.3.2.1.6.2 Test Requirements
3177A.7.3.2.2 Random Access 3178A.7.3.2.2.1 4-step RA type c ontention
based random access test in FR2 for NR Standalone 3178A.7.3.2.2.2 4-step
RA type n on-contention based random access test in FR2 for NR
Standalone 3182A.7.3.2.2.3 2-step RA type contention based random access
test in FR2 for NR Standalone 3186A.7.3.2.2.4 2-step RA type n
on-contention based random access test in FR2 for NR Standalone
3189A.7.3.2.3 SA: RRC Connection Release with Redirection
3192A.7.3.2.3.1 Redirection from NR in FR2 to NR in FR2 3192A.7.3.3
Conditional Handover 3196A.7.3.3.1 Intra-frequency conditional handover
from FR2 to FR2 3196A.7.3.3.1.1 Test Purpose and Environment
3196A.7.3.3.1.2 Test Parameters 3196A.7.3.3.1.2.3 Test Requirements
3199A.7.3.3.2 Inter-frequency conditional handover from FR2 to FR2;
unknown target cell 3199A.7.3.3.2.1 Test Purpose and Environment
3199A.7.3.3.2.2 Test Parameters 3199A.7.3.3.2.3 Test Requirements
3201A.7.4 Timing 3201A.7.4.1 UE transmit timing 3201A.7.4.1.1 NR UE
Transmit Timing Test for FR2 3201A.7.4.1.1.1 Test Purpose and
environment 3201A.7.4.1.1.2 Test requirements 3204A.7.4.1.2 NR UE
Transmit Timing Test for FR2-2 3204A.7.4.1.2.1 Test Purpose and
environment 3204A.7.4.1.2.2 Test requirements 3209A.7.4.2 UE timer
accuracy 3210A.7.4.3 Timing advance 3210A.7.4.3.1 SA FR2 timing advance
adjustment accuracy 3210A.7.4.3.1.1 Test Purpose and Environment
3210A.7.4.3.1.2 Test Parameters 3210A.7.4.3.1.3 Test Requirements
3213A.7.4.3.2 SA FR2-2 timing advance adjustment accuracy
3214A.7.4.3.2.1 Test Purpose and Environment 3214A.7.4.3.2.2 Test
Parameters 3214A.7.4.3.2.3 Test Requirements 3218A.7.5 Signaling
characteristics 3218A.7.5.1 Radio link Monitoring 3218A.7.5.1.1 Radio
Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based
RLM RS in non-DRX mode 3218A.7.5.1.1.1 Test Purpose and Environment
3218A.7.5.1.1.2 Test Requirements 3221A.7.5.1.2 Radio Link Monitoring
In-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX
mode 3222A.7.5.1.2.1 Test Purpose and Environment 3222A.7.5.1.2.2 Test
Requirements 3226A.7.5.1.3 Radio Link Monitoring Out-of-sync Test for
FR2 PCell configured with SSB-based RLM RS in DRX mode 3227A.7.5.1.3.1
Test Purpose and Environment 3227A.7.5.1.3.2 Test Requirements
3231A.7.5.1.4 Radio Link Monitoring In-sync Test for FR2 PCell
configured with SSB-based RLM RS in DRX mode 3231A.7.5.1.4.1 Test
Purpose and Environment 3231A.7.5.1.4.2 Test Requirements 3236A.7.5.1.5
Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with
CSI-RS-based RLM in non-DRX mode 3236A.7.5.1.5.1 Test Purpose and
Environment 3236A.7.5.1.5.2 Test Requirements 3241A.7.5.1.6 Radio Link
Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM
in non-DRX mode 3241A.7.5.1.6.1 Test Purpose and Environment
3241A.7.5.1.6.2 Test Requirements 3245A.7.5.1.7 Radio Link Monitoring
Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX
mode 3245A.7.5.1.7.1 Test Purpose and Environment 3245A.7.5.1.7.2 Test
Requirements 3249A.7.5.1.8 Radio Link Monitoring In-sync Test for FR2
PCell configured with CSI-RS-based RLM in DRX mode 3249A.7.5.1.8.1 Test
Purpose and Environment 3249A.7.5.1.8.2 Test Requirements 3254A.7.5.1.9
UE Radio Link Monitoring Scheduling Restrictions on FR2 3254A.7.5.1.9.1
Test Purpose and Environment 3254A.7.5.1.9.2 Test Requirements
3257A.7.5.2 Interruption 3257**A.7.5.2.1** Interruptions during
measurements on deactivated NR SCC in FR2 3257A.7.5.2.1.1 Test Purpose
and Environment 3257**A.7.5.2.1**.2 Test Requirements 3260A.7.5.2.2 SA
interruptions at NR SRS carrier-based switching 3261A.7.5.2.2.1 Test
Purpose and Environment 3261A.7.5.2.2.2 Test Parameters 3261A.7.5.2.2.3
Test Requirements 3263A.7.5.3 SCell Activation and Deactivation Delay
3263A.7.5.3.1 SCell Activation and deactivation for SCell in FR2
intra-band in non-DRX 3263A.7.5.3.1.1 Test Purpose and Environment
3263A.7.5.3.1.2 Test Requirements 3265A.7.5.3.2 SCell Activation and
deactivation for FR1+FR2 inter-band with target SCell in FR2
3265A.7.5.3.2.1 Test Purpose and Environment 3265A.7.5.3.2.2 Test
Requirements 3269A.7.5.3.3 SCell Activation and deactivation for SCell
in FR2 inter-band in non-DRX 3270A.7.5.3.3.1 Test Purpose and
Environment 3270A.7.5.3.3.2 Test Requirements 3273A.7.5.3.4 Direct SCell
activation at SCell addition of known SCell in FR2 3274A.7.5.3.4.1 Test
Purpose and Environment 3274A.7.5.3.4.2 Test Requirements 3277A.7.5.3.5
Direct SCell activation at handover with known SCell in FR2
3278A.7.5.3.5.1 Test Purpose and Environment 3278A.7.5.3.5.2 Test
Requirements 3281A.7.5.3.6 PUCCH SCell activation and deactivation for
FR1+FR2 inter-band with target SCell in FR2 and known 3282A.7.5.3.6.1
Test Purpose and Environment 3282A.7.5.3.6.2 Test Requirements
3286A.7.5.3.7 PUCCH SCell activation and deactivation delay requirements
of FR2 unknown cell with FR1 PCell 3287A.7.5.3.7.1 Test Purpose and
Environment 3287A.7.5.3.7.2 Test Requirements 3291A.7.5.3.8 SCell
Activation and deactivation for known PUCCH SCell in FR2 inter-band in
non-DRX 3292A.7.5.3.8.1 Test Purpose and Environment 3292A.7.5.3.8.2
Test Requirements 3296A.7.5.3.9 PUCCH SCell Activation and deactivation
of unknown SCell in FR2 3297A.7.5.3.9.1 Test Purpose and Environment
3297A.7.5.3.9.2 Test Requirements 3300A.7.5.3.10 SCell Activation and
deactivation of FR2 known PUCCH SCell and one FR2 unknown SCell with FR2
PCell 3301A.7.5.3.10.1 Test Purpose and Environment 3301A.7.5.3.10.2
Test Requirements 3305A.7.5.3.11 PUCCH SCell activation and deactivation
delay requirements of FR2 unknown cell with FR2 PCell 3306A.7.5.3.11.1
PUCCH SCell activation with non-PUCCH SCell in a secondary PUCCH Group
3306A.7.5.3.11.1.1 Test Purpose and Environment 3306A.7.5.3.11.1.2 Test
Requirements 3310A.7.5.3.11.2 PUCCH SCell activation with non-PUCCH
SCell in a primary PUCCH Group 3311A.7.5.3.11.2.1 Test Purpose and
Environment 3311A.7.5.3.11.2.2 Test Requirements 3315A.7.5.3.12 Void
3316A.7.5.3.13 SCell Activation for SCell in FR2 intra-band in non-DRX
3316A.7.5.3.13.1 Test Purpose and Environment 3316A.7.5.3.13.2 Test
Requirements 3318A.7.5.3.14 SCell Activation for known SCell in FR2
inter-band 3319A.7.5.3.14.1 Test Purpose and Environment
3319A.7.5.3.14.2 Test Requirements 3322A.7.5.15 Void 3323A.7.5.4 Void
3323A.7.5.5 Beam Failure Detection and Link recovery procedures
3323A.7.5.5.1 Beam Failure Detection and Link Recovery Test for FR2
PCell configured with SSB-based BFD and LR in non-DRX mode
3323A.7.5.5.1.1 Test Purpose and Environment 3323A.7.5.5.1.2 Test
Requirements 3327A.7.5.5.2 Beam Failure Detection and Link Recovery Test
for FR2 PCell configured with SSB-based BFD and LR in DRX mode
3328A.7.5.5.2.1 Test Purpose and Environment 3328A.7.5.5.2.2 Test
Requirements 3331A.7.5.5.3 Beam Failure Detection and Link Recovery Test
for FR2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode
3332A.7.5.5.3.1 Test Purpose and Environment 3332A.7.5.5.3.2 Test
Requirements 3336A.7.5.5.4 Beam Failure Detection and Link Recovery Test
for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode
3337A.7.5.5.4.1 Test Purpose and Environment 3337A.7.5.5.4.2 Test
Requirements 3341A.7.5.5.5 Scheduling availability restriction during
Beam Failure Detection and Link Recovery for FR2 PCell configured with
SSB-based BFD and LR in non-DRX mode 3342A.7.5.5.5.1 Test Purpose and
Environment 3342A.7.5.5.5.2 Test Requirements 3345A.7.5.5.6 Beam Failure
Detection and Link Recovery Test for FR2 SCell configured with
CSI-RS-based BFD and LR in non-DRX mode 3346A.7.5.5.6.1 Test Purpose and
Environment 3346A.7.5.5.6.2 Test Requirements 3350A.7.5.5.7 Beam Failure
Detection and Link Recovery Test for FR2 SCell configured with
CSI-RS-based BFD and LR in DRX mode 3351A.7.5.5.7.1 Test Purpose and
Environment 3351A.7.5.5.7.2 Test Requirements 3355A.7.5.5.8 Beam Failure
Detection and Link Recovery Test for FR2 PCell configured with
CSI-RS-based BFD and LR in DRX mode for UE fulfilling relaxed
measurement criterion 3356A.7.5.5.8.1 Test Purpose and Environment
3356A.7.5.5.8.2 Test Requirements 3360A.7.5.5.9 TRP specific Beam
Failure Detection and Link Recovery Test for FR2 SCell configured with
CSI-RS-based BFD and LR in DRX mode 3360A.7.5.5.9.1 Test Purpose and
Environment 3360A.7.5.5.9.2 Test Requirements 3366A.7.5.5.10 TRP
specific Beam Failure Detection and Link Recovery Test for FR2 PCell
configured with SSB-based BFD and LR in non-DRX mode 3366A.7.5.5.10.1
Test Purpose and Environment 3366A.7.5.5.10.2 Test Requirements
3372A.7.5.5.11 Beam Failure Detection and Link Recovery Test for FR2-2
PCell configured with CSI-RS-based BFD and LR in non-DRX mode
3372A.7.5.5.11.1 Test Purpose and Environment 3372A.7.5.5.11.2 Test
Requirements 3377A.7.5.5.12 Beam Failure Detection and Link Recovery
Test for FR2-2 PCell configured with CSI-RS-based BFD and LR in DRX mode
3377A.7.5.5.12.1 Test Purpose and Environment 3377A.7.5.5.12.2 Test
Requirements 3382A.7.5.5.13 Scheduling availability restriction during
Beam Failure Detection and Link Recovery for FR2-2 PCell configured with
SSB-based BFD and LR in non-DRX mode 3382A.7.5.5.13.1 Test Purpose and
Environment 3382A.7.5.5.13.2 Test Requirements 3386A.7.5.6 Active BWP
switch 3386A.7.5.6.1 DCI-based and Timer-based Active BWP Switch
3386A.7.5.6.1.1 NR FR2- NR FR2 DL active BWP switch of SCell with
non-DRX in SA 3386A.7.5.6.1.2 NR FR1- NR FR2 DL active BWP switch of
SCell with non-DRX in SA 3391A.7.5.6.1.3 NR FR2 DL active BWP switch
with non-DRX in SA 3396A.7.5.6.1.3.1 Test Purpose and Environment
3396A.7.5.6.1.3.2 Test Requirements 3399A.7.5.6.1.4 NR FR2-2- NR FR2-2
DL active BWP switch of SCell with non-DRX in SA 3399A.7.5.6.1.4.1 Test
Purpose and Environment 3399A.7.5.6.1.4.2 Test Requirements
3404A.7.5.6.2 RRC-based Active BWP Switch 3405A.7.5.6.2.1.1 Test Purpose
and Environment 3405A.7.5.6.2.1.2 Test Requirements 3408A.7.5.6.2.2 NR
FR2-2 DL active BWP switch of PCell with non-DRX in SA 3409A.7.5.6.2.2.1
Test Purpose and Environment 3409A.7.5.6.2.2.2 Test Requirements
3413A.7.5.6.3 Simultaneous DCI-based and Timer-based Active BWP Switch
on multiple CCs 3414A.7.5.6.3.1.1 Test Purpose and Environment
3414A.7.5.6.3.1.2 Test Requirements 3417A.7.5.6.4 SCell dormancy switch
3417A.7.5.6.4.1 NR FR2 PCell SCell dormancy switch of single FR2 SCell
inside active time 3417A.7.5.6.4.1.1 Test Purpose and Environment
3417A.7.5.6.4.1.2 Test Requirements 3422A.7.5.6.4.2 NR FR1 PCell SCell
dormancy switch of two FR2 SCells outside active time 3422A.7.5.6.4.2.1
Test Purpose and Environment 3422A.7.5.6.4.2.2 Test Requirements
3427A.7.5.6.5 Simultaneous RRC-based Active BWP Switch on multiple CCs
3427A.7.5.6.5.1 Active BWP switch on multiple SCells with non-DRX in SA
3427A.7.5.6.5.2 NR FR2-2 Active BWP switch on multiple SCells with
non-DRX in SA 3430A.7.5.6.5.2.1 Test Purpose and Environment
3430A.7.5.6.5.2**.**2 Test Requirements 3434A.7.5.7 PSCell addition and
release delay 3435A.7.5.7.1 Addition and Release Delay of known NR
PSCell 3435A.7.5.7.1.1 Test Purpose and Environment 3435A.7.5.7.1.2 Test
Requirements 3438A.7.5.7.2 Addition and Release Delay of unknown NR
PSCell in 3438A.7.5.7.2.1 Test Purpose and Environment 3438A.7.5.7.2.2
Test Requirements 3441A.7.5.7.3 Addition and Release Delay of known NR
PSCell in FR2-2 3441A.7.5.7.3.1 Test Purpose and Environment
3441A.7.5.7.3.2 Test Requirements 3444A.7.5.7.4 Addition and Release
Delay of unknown NR PSCell in FR2-2 3444A.7.5.7.4.1 Test Purpose and
Environment 3444A.7.5.7.4.2 Test Requirements 3447A.7.5.8 Active TCI
state switch delay 3447A.7.5.8.1 MAC-CE based active TCI state switch
3447A.7.5.8.2 RRC based active TCI state switch 3451A.7.5.8.3 *MAC-CE
based active TCI state switch for HST FR2 scenario* 3455A.7.5.8.3.1 NR
PCell FR2 HST active TCI state switch for a known TCI state
3455A.7.5.8.3.1.1 Test Purpose and Environment 3455A.7.5.8**.3.1**.2
Test Requirements 3459A.7.5.9 Uplink spatial relation switch delay
3460A.7.5.9.1.1.1 Test Purpose and Environment 3460A.7.5.9.1.1.2 Test
Requirements 3463A.7.5.9.2 RRC based spatial relation switch
3463A.7.5.9.2.1 NR PCell FR2 spatial relation switch associated with a
known DL-RS 3463A.7.5.9.2.1.1 Test Purpose and Environment
3463A.7.5.9.2**.1**.2 Test Requirements 3466A.7.5.10 UE specific CBW
change 3466A.7.5.10.1 NR FR2 UE specific CBW change of PCell with
non-DRX in SA 3466A.7.5.10.1.1 Test Purpose and Environment
3466A.7.5.10.1.2 Test Requirements 3469A.7.5.11 UE UL carrier RRC
reconfiguration Delay 3470A.7.5.11.1 UE UL carrier RRC reconfiguration
Delay 3470A.7.5.11.1.1 Test Purpose and Environment 3470A.7.5.11.1.2
Test Requirements 3473A.7.5.12 Conditional PSCell addition and release
delay (FR2 SA) 3473A.7.5.12.1 Addition and Release Delay of PSCell
3473A.7.5.12.1.1 Test purpose and environment 3473A.7.5.12.1.2 Test
Parameters 3473A.7.5.12.1.3 Test Requirements 3476A.7.5.13 Unified TCI
state switching delay 3476A.7.5.13.1 MAC-CE based active joint TCI state
switching 3476A.7.5.13.1.1 NR PCell FR2 active joint TCI state switch
for a known TCI state 3476A.7.5.13.1.1.1 Test Purpose and Environment
3476A.7.5.13.1.1.2 Test parameters 3477A.7.5.13**.1.1**.3 Test
Requirements 3479A.7.5.13.2 MAC-CE based active uplink TCI state switch
3479A.7.5.13.2.1 NR FR2 PCell uplink TCI state switch for a known TCI
state 3479A.7.5.13.2.1.1 Test Purpose and Environment 3479A.7.5.13.2.1.2
Test parameters 3480A.7.5.13.2.1.3 Test Requirements 3482A.7.5.13.3
MAC-CE based active downlink TCI state switch 3482A.7.5.13.3.1 NR PCell
FR2 active downlink TCI state switch to cell with additional PCI for a
known TCI state 3482A.7.5.13.3.1.1 Test Purpose and Environment
3482A.7.5.13.3.1.2 Test Parameters 3483A.7.5.13.3.1.3 Test Requirements
3486A.7.5.14 PSCell RACH-less based Activation and deactivation for
FR1+FR2 inter-band with target PSCell in FR2 3486A.7.5.14.1 Test Purpose
and Environment 3486A.7.5.14.2 Test Requirements 3489A.7.6 Measurement
procedure 3490A.7.6.1 Intra-frequency Measurements 3490A.7.6.1.1 SA
event triggered reporting test without gap under non-DRX 3490A.7.6.1.1.1
Test purpose and Environment 3490A.7.6.1.1.2 Test Requirements
3493A.7.6.1.2 SA event triggered reporting test without gap under DRX
3493A.7.6.1.2.1 Test purpose and Environment 3493A.7.6.1.2.2 Test
Requirements 3496A.7.6.1.3 SA event triggered reporting test with per-UE
gaps under non-DRX 3497A.7.6.1.3.1 Test purpose and Environment
3497A.7.6.1.3.2 Test Requirements 3500A.7.6.1.4 SA event triggered
reporting test with per-UE gaps under DRX 3500A.7.6.1.4.1 Test purpose
and Environment 3500A.7.6.1.4.2 Test Requirements 3503A.7.6.1.5 SA event
triggered reporting test without gap under non-DRX for UE configured
with *highSpeedMeasFlagFR2-r17* 3504A.7.6.1.5.1 Test purpose and
Environment 3504A.7.6.1.5.2 Test Requirements 3507A.7.6.1.6 SA event
triggered reporting test without gap under non-DRX for FR2-2
3507A.7.6.1.6.1 Test purpose and Environment 3507A.7.6.1.6.2 Test
Requirements 3510A.7.6.1.7 SA event triggered reporting test without gap
under DRX for FR2-2 3511A.7.6.1.7.1 Test purpose and Environment
3511A.7.6.1.7.2 Test Requirements 3513A.7.6.1.8 SA event triggered
reporting test with per-UE gaps under non-DRX for FR2-2 3514A.7.6.1.8.1
Test purpose and Environment 3514A.7.6.1.8.2 Test Requirements
3517A.7.6.1.9 SA event triggered reporting test with per-UE gaps under
DRX for FR2-2 3518A.7.6.1.9.1 Test purpose and Environment
3518A.7.6.1.9.2 Test Requirements 3520A.7.6.1.10 SA event triggered
reporting test with SSB time index detection without gap under non-DRX
for FR2-2 3521A.7.6.1.10.1 Test purpose and Environment 3521A.7.6.1.10.2
Test Requirements 3525A.7.6.1.11 SA event triggered reporting test with
SSB time index detection with per-UE gaps under non-DRX for FR2-2
3525A.7.6.1.11.1 Test purpose and Environment 3525A.7.6.1.11.2 Test
Requirements 3528A.7.6.2 Inter-frequency Measurements 3528A.7.6.2.1 SA
event triggered reporting tests for FR2 without SSB time index detection
when DRX is not used (PCell in FR2) 3528A.7.6.2.1.1 Test Purpose and
Environment 3528A.7.6.2.1.2 Test Requirements 3532A.7.6.2.2 SA event
triggered reporting tests for FR2 without SSB time index detection when
DRX is used (Pcell in FR2) 3532A.7.6.2.2.1 Test Purpose and Environment
3532A.7.6.2.2.2 Test Requirements 3536A.7.6.2.3 SA event triggered
reporting tests for FR2 with SSB time index detection when DRX is not
used (PCell in FR2) 3536A.7.6.2.3.1 Test Purpose and Environment
3536A.7.6.2.3.2 Test Requirements 3540A.7.6.2.4 SA event triggered
reporting tests for FR2 with SSB time index detection when DRX is used
(Pcell in FR2) 3540A.7.6.2.4.1 Test Purpose and Environment
3540A.7.6.2.4.2 Test Requirements 3544A.7.6.2.5 SA event triggered
reporting tests for FR2 without SSB time index detection when DRX is not
used (PCell in FR1) 3544A.7.6.2.5.1 Test Purpose and Environment
3544A.7.6.2.5.2 Test Requirements 3548A.7.6.2.6 SA event triggered
reporting tests for FR2 without SSB time index detection when DRX is
used (Pcell in FR1) 3549A.7.6.2.6.1 Test Purpose and Environment
3549A.7.6.2.6.2 Test Requirements 3553A.7.6.2.7 SA event triggered
reporting tests for FR2 with SSB time index detection when DRX is not
used (PCell in FR1) 3554A.7.6.2.7.1 Test Purpose and Environment
3554A.7.6.2.7.2 Test Requirements 3558A.7.6.2.8 SA event triggered
reporting tests for FR2 with SSB time index detection when DRX is used
(PCell in FR1) 3559A.7.6.2.8.1 Test Purpose and Environment
3559A.7.6.2.8.2 Test Requirements 3563A.7.6.2.9 SA event triggered
reporting tests For FR2 without SSB time index detection when DRX is not
used (PCell in FR2) (rel16 additional mandatory gap pattern 17)
3564A.7.6.2.9.1 Test Purpose and Environment 3564A.7.6.2.9.2 Test
Requirements 3568A.7.6.2.10 SA event triggered reporting test without
gap under non-DRX 3568A.7.6.2.10.1 Test Purpose and Environment
3568A.7.6.2.10.2 Test Requirements 3570A.7.6.2.11 SA event triggered
reporting test without gap under DRX 3571A.7.6.2.11.1 Test Purpose and
Environment 3571A.7.6.2.11.2 Test Requirements 3573A.7.6.2.12 SA event
triggered reporting tests for FR2-2 without SSB time index detection
when DRX is not used (PCell in FR2-2) 3574A.7.6.2.12.1 Test Purpose and
Environment 3574A.7.6.2.12.2 Test Requirements 3577A.7.6.2.13 SA event
triggered reporting tests for FR2-2 without SSB time index detection
when DRX is used (PCell in FR2-2) 3578A.7.6.2.13.1 Test Purpose and
Environment 3578A.7.6.2.13.2 Test Requirements 3582A.7.6.2.14 SA event
triggered reporting tests for FR2-2 with SSB time index detection when
DRX is not used (PCell in FR2-2) 3583A.7.6.2.14.1 Test Purpose and
Environment 3583A.7.6.2.14.2 Test Requirements 3587A.7.6.2.15 SA event
triggered reporting tests for FR2-2 with SSB time index detection when
DRX is used (PCell in FR2-2) 3588A.7.6.2.15.1 Test Purpose and
Environment 3588A.7.6.2.15.2 Test Requirements 3592A.7.6.2.16 SA event
triggered reporting tests for FR2-2 without SSB time index detection
when DRX is not used (PCell in FR1) 3593A.7.6.2.16.1 Test Purpose and
Environment 3593A.7.6.2.16.2 Test Requirements 3599A.7.6.2.17 SA event
triggered reporting tests for FR2-2 without SSB time index detection
when DRX is used (PCell in FR1) 3599A.7.6.2.17.1 Test Purpose and
Environment 3599A.7.6.2.17.2 Test Requirements 3606A.7.6.2.18 SA event
triggered reporting tests for FR2-2 with SSB time index detection when
DRX is not used (PCell in FR1) 3607A.7.6.2.18.1 Test Purpose and
Environment 3607A.7.6.2.18.2 Test Requirements 3613A.7.6.2.19 SA event
triggered reporting tests for FR2-2 with SSB time index detection when
DRX is used (PCell in FR1) 3613A.7.6.2.19.1 Test Purpose and Environment
3613A.7.6.2.19.2 Test Requirements 3621A.7.6.3 L1-RSRP measurement for
beam reporting 3622A.7.6.3.1 SSB based L1-RSRP measurement when DRX is
not used 3622A.7.6.3.1.1 Test Purpose and Environment 3622A.7.6.3.1.2
Test parameters 3622A.7.6.3.1.3 Test Requirements 3624A.7.6.3.2 SSB
based L1-RSRP measurement when DRX is used 3624A.7.6.3.2.1 Test Purpose
and Environment 3624A.7.6.3.2.2 Test parameters 3625A.7.6.3.2.3 Test
Requirements 3627A.7.6.3.3 CSI-RS based L1-RSRP measurement when DRX is
not used 3627A.7.6.3.3.1 Test Purpose and Environment 3627A.7.6.3.3.2
Test parameters 3628A.7.6.3.3.3 Test Requirements 3630A.7.6.3.4 CSI-RS
based L1-RSRP measurement when DRX is used 3631A.7.6.3.4.1 Test Purpose
and Environment 3631A.7.6.3.4.2 Test parameters 3631A.7.6.3.3.3 Test
Requirements 3633A.7.6.3.5 SSB based L1-RSRP measurement when DRX is
used for power class 6 UE configured with *highSpeedMeasFlagFR2-r17*
3634A.7.6.3.5.1 Test Purpose and Environment 3634A.7.6.3.5.2 Test
parameters 3634A.7.6.3.5.3 Test Requirements 3636A.7.6.3.6 Inter-cell
SSB based L1-RSRP measurements on FR2 SCell when DRX is not used
3636A.7.6.3.6.1 Test Purpose and Environment 3636A.7.6.3.6.2 Test
parameters 3637A.7.6.3.6.3 Test Requirements 3640A.7.6.3.7 SSB based
L1-RSRP measurement for FR2-2 when DRX is used 3640A.7.6.3.7.1 Test
Purpose and Environment 3640A.7.6.3.7.2 Test parameters 3641A.7.6.3.7.3
Test Requirements 3644A.7.6.4 CLI measurements 3645A.7.6.4.1 SRS-RSRP
measurement with non-DRX 3645A.7.6.4.1.1 Test Purpose and Environment
3645A.7.6.4.1.2 Test Parameters 3645A.7.6.4.1.3 Test Requirements
3647A.7.6.4.2 CLI-RSSI measurement with non-DRX 3647A.7.6.4.2.1 Test
Purpose and Environment 3647A.7.6.4.2.2 Test Parameters 3648A.7.6.4.2.3
Test Requirements 3649A.7.6.5.1 SA interfrequency CGI reporting in
autonomous gaps test (PCell in FR2) 3650A.7.6.5.1.1 Test Purpose and
Environment 3650A.7.6.5.1.2 Test Requirements 3653A.7.6.6 L1-SINR
measurement for beam reporting 3653A.7.6.6.2 L1-SINR measurement with
SSB based CMR and dedicated IMR when DRX is used 3655A.7.6.6.2.1 Test
Purpose and Environment 3655A.7.6.6.2.2 Test parameters 3656A.7.6.6.2.3
Test Requirements 3658A.7.6.6.3 L1-SINR measurement with CSI-RS based
CMR and dedicated IMR configured when DRX is used 3658A.7.6.6.3.1 Test
Purpose and Environment 3658A.7.6.6.3.2 Test parameters 3659A.7.6.6.3.3
Test Requirements 3661A.7.6.7 CSI-RS based intra-frequency Measurements
3661A.7.6.7.1 SA event triggered reporting test without gap under DRX
for CSI-RS based intra-frequency measurement 3661A.7.6.7.1.1 Test
purpose and Environment 3661A.7.6.7.1.2 Test Requirements 3664A.7.6.8
CSI-RS based inter-frequency Measurements 3665A.7.6.8.1 SA event
triggered reporting tests for FR2 CSI-RS based measurement when non-DRX
is used (PCell in FR2) 3665A.7.6.8.1.1 Test Purpose and Environment
3665A.7.6.8.1.2 Test Requirements 3668A.7.6.9 RSTD measurements
3668A.7.6.9.1 NR RSTD measurement reporting delay test case for single
positioning frequency layer in FR2 SA 3668A.7.6.9.1.1 Test Purpose and
Environment 3668A.7.6.9.1.2 Test Requirements 3676A.7.6.9.2 NR RSTD
measurement reporting delay test case for dual positioning frequency
layers in FR2 SA 3676A.7.6.9.2.1 Test Purpose and Environment
3676A.7.6.9.2.2 Test Requirements 3684A.7.6.9.3 NR RSTD measurement
reporting delay test case for single positioning frequency layer with
reduced number of samples in FR2 SA 3684A.7.6.9.3.1 Test Purpose and
Environment 3684A.7.6.9.3.2 Test Requirements 3690A.7.6.9.4 NR RSTD
measurement reporting delay test case for single positioning frequency
layer in FR2 SA without measurement gap 3691A.7.6.9.4.1 Test Purpose and
Environment 3691A.7.6.9.4.2 Test Requirements 3694A.7.6.9.5 NR RSTD
measurement reporting delay test case for single positioning frequency
layer in FR2 SA in RRC\_CONNECTED state with Rx TEG 3695A.7.6.9.5.1 Test
Purpose and Environment 3695A.7.6.9.5.2 Test Requirements 3698A.7.6.10
PRS-RSRP measurements 3699A.7.6.10.1 PRS-RSRP reporting delay test case
for single positioning frequency layer 3699A.7.6.10.1.1 Test Purpose and
Environment 3699A.7.6.10.1.2 Test Requirements 3703A.7.6.10.2 PRS-RSRP
reporting delay test case for dual positioning frequency layer
3703A.7.6.10.2.1 Test Purpose and Environment 3703A.7.6.10.2.2 Test
Requirements 3707A.7.6.10.3 PRS-RSRP reporting delay test case for
reduced number of samples 3707A.7.6.10.3.1 Test Purpose and Environment
3707A.7.6.10.3.2 Test Requirements 3712A.7.6.10.4 PRS-RSRP reporting
delay test case for single positioning frequency layer outside MG
3712A.7.6.10.4.1 Test Purpose and Environment 3712A.7.6.10.4.2 Test
Requirements 3717A.7.6.11 UE Rx-Tx time difference measurements
3717A.7.6.11.1 UE Rx-Tx time difference measurements for single
positioning frequency layer in FR2 SA 3717A.7.6.11.1.1 Test purpose and
environment 3717A.7.6.11.1.2 Test requirements 3721A.7.6.11.2 UE Rx-Tx
time difference measurement period for dual positioning frequency layers
in FR2 SA 3721A.7.6.11.2.1 Test purpose and environment 3721A.7.6.11.2.2
Test requirements 3725A.7.6.11.3 UE Rx-Tx time difference measurements
for single positioning frequency layer in FR2 SA with reduced sample
number 3725A.7.6.11.3.1 Test purpose and environment 3725A.7.6.11.3.2
Test requirements 3727A.7.6.11.4 UE Rx-Tx time difference measurements
without gaps in FR2 SA 3728A.7.6.11.4.1 Test purpose and environment
3728A.7.6.11.4.2 Test requirements 3730A.7.6.11.5 UE Rx-Tx time
difference measurements for single positioning frequency layer in FR2 SA
with RxTx TEG 3731A.7.6.11.5.1 Test purpose and environment
3731A.7.6.11.5.2 Test requirements 3733A.7.6.12 PRS-RSRPP measurements
3734A.7.6.12.1 PRS-RSRPP reporting delay test case for single
positioning frequency layer in FR2 in RRC\_CONNECTED state
3734A.7.6.12.1.1 Test Purpose and Environment 3734A.7.6.12.1.2 Test
Requirements 3737A.7.6.12.2 PRS-RSRPP reporting delay test case for
reduced number of samples for single positioning frequency layer in FR2
in RRC\_CONNECTED state 3737A.7.6.12.2.1 Test Purpose and Environment
3737A.7.6.12.2.2 Test Requirements 3740A.7.6.12.3 PRS-RSRPP reporting
delay test case for gapless measurement in FR2 3740A.7.6.12.3.1 Test
Purpose and Environment 3740A.7.6.12.3.2 Test Requirements 3743A.7.6.13
UE Rx-Tx time difference measurements for PDC 3744A.7.6.13.1 UE Rx-Tx
time difference measurement for propagation delay compensation using PRS
in FR2 3744A.7.6.13.1.1 Test purpose and environment 3744A.7.6.13.1.2
Test requirements 3745A.7.6.13.2 UE Rx-Tx time difference measurement
for propagation delay compensation using TRS in FR2 3746A.7.6.13.2.1
Test purpose and environment 3746A.7.6.13.2.2 Test requirements
3747A.7.6.14 SA event triggered reporting tests with Pre-MG
3748A.7.6.14.1 Intra-frequency measurement test with SA event triggered
reporting tests: with **autonomous** activation/deactivation of Pre-MG
in FR2 3748A.7.6.14.1.1 Test purpose and Environment 3748A.7.6.14.1.2
Test parameters 3748A.7.6.14.1.3 Test Requirements 3751A.7.6.14.2
Intra-frequency measurement test with SA event triggered reporting
tests: with network-controlled activation/deactivation of Pre-MG in FR2
3751A.7.6.14.2.1 Test purpose and Environment 3751A.7.6.14.2.2 Test
parameters 3751A.7.6.14.2.3 Test Requirements 3754A.7.6.15 SA event
triggered reporting tests with concurrent gaps 3754A.7.6.15.1 SA event
triggered reporting tests For FR2 with fully non-overlapping concurrent
MGs for SSB-based inter-frequency measurements 3754A.7.6.15.1.1 Test
Purpose and Environment 3754A.7.6.15.1.2 Test Requirements
3757A.7.6.15.2 SA event triggered reporting tests For FR2 with
concurrent measurement gaps without SSB time index detection when DRX is
not used (PCell in FR2) 3757A.7.6.15.2.1 Test Purpose and Environment
3757A.7.6.15.2.2 Test Requirements 3760A.7.6.15.3 SA event triggered
reporting tests for FR2 concurrent gap with partially partial
overlapping scenario for SSB-based measurements and PRS-based
measurement 3760A.7.6.15.3.1 Test Purpose and Environment
3760A.7.6.15.3.2 Test Requirements 3764A.7.6.16 SA event triggered
reporting tests with NCSG 3764A.7.6.16.1 SA event triggered reporting
test with per-UE NCSG under non-DRX 3764A.7.6.16.1.1 Test purpose and
Environment 3764A.7.6.16.1.2 Test Requirements 3768A.7.6.16.2 SA event
triggered reporting tests on inter-frequency measurement with NCSG for
FR2 when DRX is not used (PCell in FR2) 3768A.7.6.16.2.1 Test Purpose
and Environment 3768A.7.6.16.2.2 Test Requirements 3771A.7.6.16.3 Event
triggered reporting test on deactivated Scell measurement via NCSG in
FR2 in non-DRX 3771A.7.6.16.3.1 Test Purpose and Environment
3771A.7.6.16.3.2 Test Requirements 3774A.7.7 Measurement Performance
requirements 3774A.7.7.1 SS-RSRP 3775A.7.7.1.1 SA intra-frequency case
measurement accuracy with FR2 serving cell and FR2 target cell
3775A.7.7.1.1.1 Test Purpose and Environment 3775A.7.7.1.1.2 Test
parameters 3775A.7.7.1.1.3 Test Requirements 3779A.7.7.1.2 SA
inter-frequency case measurement accuracy with FR2 serving cell and FR2
target cell 3780A.7.7.1.2.1 Test Purpose and Environment 3780A.7.7.1.2.2
Test parameters 3780A.7.7.1.2.3 Test Requirements 3784A.7.7.1.3 SA
inter-frequency measurement accuracy with FR1 serving cell and FR2
target cell 3785A.7.7.1.3.1 Test Purpose and Environment 3785A.7.7.1.3.2
Test parameters 3785A.7.7.1.3.3 Test Requirements 3789A.7.7.2 SS-RSRQ
3789A.7.7.2.1 SA intra-frequency measurement accuracy with FR2 serving
cell and FR2 target cell 3789A.7.7.2.1.1 Test Purpose and Environment
3789A.7.7.2.1.2 Test Parameters 3789A.7.7.2.1.3 Test Requirements
3791A.7.7.2.2 SA Inter-frequency measurement accuracy with FR2 serving
cell and FR2 TDD target cell 3791A.7.7.2.2.1 Test Purpose and
Environment 3791A.7.7.2.2.2 Test Parameters 3791A.7.7.2.2.3 Test
Requirements 3793A.7.7.3 SS-SINR 3793A.7.7.3.1 SA intra-frequency case
measurement accuracy with FR2 serving cell and FR2 target cell
3793A.7.7.3.1.1 Test Purpose and Environment 3793A.7.7.3.1.2 Test
Parameters 3793A.7.7.3.1.3 Test Requirements 3795A.7.7.3.2 SA
Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 3795A.7.7.3.2.1 Test Purpose and Environment 3795A.7.7.3.2.2
Test Parameters 3795A.7.7.3.2.3 Test Requirements 3797A.7.7.4 L1-RSRP
measurement for beam reporting 3797A.7.7.4.1 SSB based L1-RSRP
measurement 3797A.7.7.4.1.1 Test Purpose and Environment 3797A.7.7.4.1.2
Test parameters 3798A.7.7.4.1.3 Test Requirements 3800A.7.7.4.2 CSI-RS
based L1-RSRP measurement on resource set with repetition off
3801A.7.7.4.2.1 Test Purpose and Environment 3801A.7.7.4.2.2 Test
parameters 3801A.7.7.4.2.3 Test Requirements 3803A.7.7.5 CLI
measurements 3804A.7.7.5.1 SA SRS-RSRP measurement accuracy with FR2
serving cell 3804A.7.7.5.1.1 Test Purpose and Environment
3804A.7.7.5.1.2 Test parameters 3804A.7.7.5.1.3 Test Requirements
3807A.7.7.5.2 SA CLI-RSSI measurement accuracy with FR2 serving cell
3808A.7.7.5.2.1 Test Purpose and Environment 3808A.7.7.5.2.2 Test
parameters 3808A.7.7.5.2.3 Test Requirements 3810A.7.7.6 L1-SINR
measurement for beam reporting 3811A.7.7.6.1.1 Test Purpose and
Environment 3811A.7.7.6.1.2 Test parameters 3811A.7.7.6.1.3 Test
Requirements 3813A.7.7.6.2 L1-SINR measurement with SSB based CMR and
dedicated IMR 3814A.7.7.6.2.1 Test Purpose and Environment
3814A.7.7.6.2.2 Test parameters 3814A.7.7.6.2.3 Test Requirements
3816A.7.7.6.3 L1-SINR measurement with CSI-RS based CMR and dedicated
IMR 3817A.7.7.6.3.1 Test Purpose and Environment 3817A.7.7.6.3.2 Test
parameters 3817A.7.7.6.3.3 Test Requirements 3819A.7.7.7 CSI-RSRP
3820A.7.7.7.1 SA intra-frequency case measurement accuracy with FR2
serving cell and FR2 target cell 3820A.7.7.7.1.1 Test Purpose and
Environment 3820A.7.7.7.1.2 Test parameters 3820A.7.7.7.1.3 Test
Requirements 3825A.7.7.7.2 SA inter-frequency case measurement accuracy
with FR2 serving cell and FR2 target cell 3825A.7.7.7.2.1 Test Purpose
and Environment 3825A.7.7.7.2.2 Test parameters 3826A.7.7.7.2.3 Test
Requirements 3830A.7.7.8 CSI-RSRQ 3831A.7.7.8.1 SA intra-frequency
measurement accuracy with FR2 serving cell and FR2 target cell
3831A.7.7.8.1.1 Test Purpose and Environment 3831A.7.7.8.1.2 Test
Parameters 3831A.7.7.8.1.3 Test Requirements 3833A.7.7.8.2 SA
Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 3833A.7.7.8.2.1 Test Purpose and Environment 3833A.7.7.8.2.2
Test Parameters 3834A.7.7.8.2.3 Test Requirements 3835A.7.7.9 CSI-SINR
3835A.7.7.9.1 SA intra-frequency case measurement accuracy with FR2
serving cell and FR2 target cell 3835A.7.7.9.1.1 Test Purpose and
Environment 3835A.7.7.9.1.2 Test Parameters 3836A.7.7.9.1.3 Test
Requirements 3838A.7.7.9.2 SA Inter-frequency measurement accuracy with
FR2 serving cell and FR2 TDD target cell 3839A.7.7.9.2.1 Test Purpose
and Environment 3839A.7.7.9.2.2 Test Parameters 3839A.7.7.9.2.3 Test
Requirements 3841A.7.7.10 RSTD measurements 3842A.7.7.10.1 RSTD
measurement accuracy test case for single positioning frequency layer
3842A.7.7.10.1.1 Test purpose and Environment 3842A.7.7.10.1.2 Test
Requirements 3844A.7.7.10.2 RSTD measurement accuracy test case for dual
positioning frequency layer 3844A.7.7.10.2.1 Test purpose and
Environment 3844A.7.7.10.2.2 Test Requirements 3848A.7.7.10.3 RSTD
measurement accuracy test case with reduced number of samples for single
positioning frequency layer in FR2 in RRC\_CONNECTED state
3849A.7.7.10.3.1 Test purpose and Environment 3849A.7.7.10.3.2 Test
Requirements 3850A.7.7.10.4 RSTD measurement accuracy test case with Rx
TEG 3851A.7.7.10.4.1 Test purpose and Environment 3851A.7.7.10.4.2 Test
Requirements 3853A.7.7.11 PRS-RSRP measurements 3853A.7.7.11.1 SA
measurement accuracy with PRS in FR2 3853A.7.7.11.1.1 Test Purpose and
Environment 3853A.7.7.11.1.2 Test parameters 3853A.7.7.11.1.3 Test
Requirements 3857A.7.7.11.2 SA measurement accuracy with PRS in FR2 with
reduced sample number 3858A.7.7.11.2.1 Test Purpose and Environment
3858A.7.7.11.2.2 Test parameters 3858A.7.7.11.2.3 Test Requirements
3860A.7.7.12 UE Rx-Tx time difference measurements 3861A.7.7.12.1 UE
Rx-Tx time difference measurement accuracy for single positioning
frequency layer in FR2 SA 3861A.7.7.12.1.1 Test purpose and environment
3861A.7.7.12.1.2 Test parameters 3861A.7.7.12.1.3 Test requirements
3864A.7.7.12.2 UE Rx-Tx time difference measurement accuracy with
reduced number of samples in FR2 SA 3865A.7.7.12.2.1 Test purpose and
environment 3865A.7.7.12.2.2 Test parameters 3865A.7.7.12.2.3 Test
requirements 3868A.7.7.12.3 UE Rx-Tx time difference measurement
accuracy with RxTx TEG 3868A.7.7.12.3.1 Test purpose and environment
3868A.7.7.12.3.2 Test parameters 3868A.7.7.12.3.3 Test requirements
3871A.7.7.13 PRS-RSRPP measurements 3871A.7.7.13.1 SA measurement
accuracy with PRS in FR2 3871A.7.7.13.1.1 Test Purpose and Environment
3871A.7.7.13.1.2 Test parameters 3872A.7.7.13.1.3 Test Requirements
3874A.7.7.13.2 SA measurement accuracy with reduced PRS samples in FR2
3875A.7.7.13.2.1 Test Purpose and Environment 3875A.7.7.13.2.2 Test
parameters 3875A.7.7.13.2.3 Test Requirements 3877A.7.8 Measurement
procedure in RRC\_INACTIVE 3878A.7.8.1 RSTD measurements 3878A.7.8.1.1
NR RSTD measurement reporting delay test case for single positioning
frequency layer in FR2 SA in RRC\_INACTIVE state 3878A.7.8.1.1.1 Test
Purpose and Environment 3878A.7.8.1.1.2 Test Requirements 3881A.7.8.1.2
NR RSTD measurement reporting delay test case with reduced number of
samples in RRC\_INACTIVE, FR1 SA 3881A.7.8.1.2.1 Test Purpose and
Environment 3881A.7.8.1.2.2 Test Requirements 3887A.7.8.2 PRS-RSRP
measurements 3888A.7.8.2.1 PRS-RSRP reporting delay test case for single
positioning frequency layer in RRC\_INACTIVE 3888A.7.8.2.1.1 Test
Purpose and Environment 3888A.7.8.2.1.2 Test Requirements 3892A.7.8.2.2
PRS-RSRP reporting delay test case with reduced number of samples in
RRC\_INACTIVE 3892A.7.8.2.2.1 Test purpose and Environment
3892A.7.**8.2.2**.2 Test Requirements 3896A.7.8.3 UE Rx-Tx time
difference measurements 3896A.7.8.3.1 UE Rx-Tx time difference
measurements for single positioning frequency layer in FR2 SA
3896A.7.8.3.1.1 Test purpose and environment 3896A.7.8.3.1.2 Test
requirements 3900A.7.8.3.2 UE Rx-Tx time difference measurement with
reduced number of samples in RRC\_INACTIVE, FR2 SA 3900A.7.8.3.2.1 Test
purpose and environment 3900A.7.**8.3.2**.2 Test requirements
3902A.7.8.4 PRS-RSRPP measurements 3903A.7.8.4.1 PRS-RSRPP reporting
delay test case for single positioning frequency layer in FR2 in
RRC\_INACTIVE state 3903A.7.8.4.1.1 Test Purpose and Environment
3903A.7.8.4.1.2 Test Requirements 3905A.7.8.4.2 PRS-RSRPP reporting
delay test with reduced number of samples for single positioning
frequency layer in FR2 in RRC\_INACTIVE state 3906A.7.8.4.2.1 Test
Purpose and Environment 3906A.7.8.4.2.2 Test Requirements 3908A.7.9
Measurement performance requirements in RRC\_INACTIVE 3909A.7.9.1 RSTD
measurements 3909A.7.9.1.1 RSTD measurement accuracy test case for
single positioning frequency layer in FR2 in RRC\_INACTIVE state
3909A.7.9.1.1.1 Test purpose and Environment 3909A.7.9.1.1.2 Test
Requirements 3911A.7.9.1.2 RSTD measurement accuracy test case with
reduced number of samples for single positioning frequency layer in FR2
in RRC\_INACTIVE state 3911A.7.9.1.2.1 Test purpose and Environment
3911A.7.9.1.2.2 Test Requirements 3913A.7.9.2 PRS-RSRP measurements
3913A.7.9.2.1 SA measurement accuracy with PRS in FR2 in RRC\_INACTIVE
3913A.7.9.2.1.1 Test Purpose and Environment 3913A.7.9.2.1.2 Test
parameters 3913A.7.9.2.1.3 Test Requirements 3915A.7.9.2.2 PRS-RSRP
measurements with reduced number of sample in RRC\_INACTIVE
3916A.7.9.2.2.1 Test Purpose and Environment 3916A.7.9.2.2.2 Test
parameters 3916A.7.9.2.2.3 Test Requirements 3918A.7.9.3 UE Rx-Tx time
difference measurements 3919A.7.9.3.1 UE Rx-Tx time difference
measurements in RRC\_INACTIVE 3919A.7.9.3.1.1 Test purpose and
environment 3919A.7.9.3.1.2 Test parameters 3919A.7.9.3.1.3 Test
requirements 3922A.7.9.3.2 UE Rx-Tx time difference measurement accuracy
with reduced number of samples in FR2 SA 3922A.7.9.3.2.1 Test purpose
and environment 3922A.7.9.3.2.2 Test parameters 3922A.7.9.3.2.3 Test
requirements 3925A.7.9.4 PRS-RSRPP measurements 3925A.7.9.4.1 SA
measurement accuracy in FR2 in RRC INACTIVE 3925A.7.9.4.1.1 Test Purpose
and Environment 3925A.7.9.4.1.2 Test parameters 3925A.7.9.4.1.3 Test
Requirements 3927A.7.9.4.2 SA measurement accuracy with reduced PRS
samples in FR2 in RRC INACTIVE 3928A.7.9.4.2.1 Test Purpose and
Environment 3928A.7.9.4.2.2 Test parameters 3928A.7.9.4.2.3 Test
Requirements 3930A.8 E-UTRA standalone tests for NR RRM 3928A.8.1 Void
3928A.8.2 RRC\_IDLE state mobility 3928A.8.2.1 Inter-RAT NR Cell
re-selection 3928A.8.2.1.1 E-UTRA Cell reselection to higher priority NR
target Cell in FR1 3928A.8.2.1.1.1 Test Purpose and Environment
3928A.8.2.1.1.2 Test Requirements 3933A.8.2.1.2 E-UTRA Cell reselection
to lower priority NR target Cell in FR1 for UE configured with
highSpeedInterRAT-NR-r16 3934A.8.2.1.2.1 Test Purpose and Environment
3934A.8.2.1.2.2 Test Requirements 3938A.8.2.2 E-UTRA -- NR Inter-RAT
Early Measruement Reporting 3939A.8.2.2.1 E-UTRA -- NR Early Measurement
Reporting for NR in FR1 3939A.8.2.2.1.1 Test Purpose and Environment
3939A.8.2.2.1.2 Test Requirements 3943A.8.2.2.2 E-UTRA -- NR Early
Measurement Reporting for NR in FR2 3943A.8.2.2.2.1 Test Purpose and
Environment 3943A.8.2.2.2.2 Test Requirements 3946A.8.3 RRC\_CONNECTED
state mobility 3947A.8.3.1 Handover 3947A.8.3.1.1 E-UTRAN - NR handover
in FR1 3947A.8.3.1.1.1 Test Purpose and Environment 3947A.8.3.1.1.2 Test
Requirements 3952A.8.4 Measurement procedure 3952A.8.4.1 E-UTRA -- NR
Inter-RAT SFTD Measurement Delay 3952A.8.4.1.1 E-UTRA -- NR Inter-RAT
SFTD Measurement Delay in non-DRX 3952A.8.4.1.1.1 Test Purpose and
Environment 3952A.8.4.1.1.2 Test Requirements 3954A.8.4.1.2 E-UTRA -- NR
Inter-RAT SFTD Measurement Delay in DRX 3955A.8.4.1.2.1 Test Purpose and
Environment 3955A.8.4.1.2.2 Test Requirements 3956A.8.4.2 E-UTRA -- NR
Inter-RAT Measurements 3956A.8.4.2.1 NR Inter-RAT event triggered
reporting tests for FR1 without SSB time index detection when DRX is not
used 3956A.8.4.2.1.1 Test Purpose and Environment 3956A.8.4.2.1.2 Test
Requirements 3961A.8.4.2.2 NR Inter-RAT event triggered reporting tests
for FR1 without SSB time index detection when DRX is used
3961A.8.4.2.2.1 Test Purpose and Environment 3961A.8.4.2.2.2 Test
Requirements 3965A.8.4.2.3 NR Inter-RAT event triggered reporting tests
for FR1 with SSB time index detection when DRX is not used
3965A.8.4.2.3.1 Test Purpose and Environment 3965A.8.4.2.3.2 Test
Requirements 3969A.8.4.2.4 NR Inter-RAT event triggered reporting tests
for FR1 with SSB time index detection when DRX is used 3969A.8.4.2.4.1
Test Purpose and Environment 3969A.8.4.2.4.2 Test Requirements
3973A.8.4.2.5 NR Inter-RAT event triggered reporting tests for FR2
without SSB time index detection when DRX is not used 3973A.8.4.2.5.1
Test Purpose and Environment 3973A.8.4.2.5.2 Test Requirements
3975A.8.4.2.6 NR Inter-RAT event triggered reporting tests for FR2
without SSB time index detection when DRX is used 3976A.8.4.2.6.1 Test
Purpose and Environment 3976A.8.4.2.6.2 Test Requirements 3978A.8.4.2.7
NR Inter-RAT event triggered reporting tests for FR2 with SSB time index
detection when DRX is not used 3979A.8.4.2.7.1 Test Purpose and
Environment 3979A.8.4.2.7.2 Test Requirements 3981A.8.4.2.8 NR Inter-RAT
event triggered reporting tests for FR2 with SSB time index detection
when DRX is used 3982A.8.4.2.8.1 Test Purpose and Environment
3982A.8.4.2.8.2 Test Requirements 3984A.8.4.2.9 NR Inter-RAT event
triggered reporting tests for FR1 with SSB time index detection in DRX
for UE configured with highSpeedInterRAT-NR-r16 3985A.8.4.2.9.1 Test
Purpose and Environment 3985A.8.4.2.9.2 Test Requirements 3990A.8.5
Measurement performance 3990A.8.5.1 SFTD accuracy 3990A.8.5.1.1 SFTD
accuracy 3990A.8.5.1.1.1 Test Purpose 3990A.8.5.1.1.2 Test Environment
3990A.8.5.1.1.3 Test Requirements 3996A.8.5.2 E-UTRA -- NR Inter-RAT
Measurement Performance requirements 3996A.8.5.2.1.1 E-UTRAN -- NR
inter-RAT measurements with FR1 target cell 3996A.8.5.2.1.2 E-UTRAN --
NR inter-RAT measurements with FR2 target cell 4001A.8.5.2.1.2.1 Test
Purpose and Environment 4001A.8.5.2.1.2.2 Test Parameters
4001A.8.5.2.1.2.3 Test Requirements 4003A.8.5.2.2 SS-RSRQ
4003A.8.5.2.2.1 E-UTRAN -- NR inter-RAT measurements with FR1 target
cell 4003A.8.5.2.2.2 E-UTRAN -- NR inter-RAT measurements with FR2
target cell 4008A.8.5.2.2.2.1 Test Purpose and Environment
4008A.8.5.2.2.2.2 Test Parameters 4008A.8.5.2.2.2.3 Test Requirements
4010A.8.5.2.3 SS-SINR 4010A.8.5.2.3.1 E-UTRAN -- NR inter-RAT
measurements with FR1 target cell 4010A.8.5.2.3.2 E-UTRAN -- NR
inter-RAT measurements with FR2 target cell 4014A.8.5.2.3.2.1 Test
Purpose and Environment 4014A.8.5.2.3.2.2 Test Parameters
4014A.8.5.2.3.2.3 Test Requirements 4016A.9 V2X Tests 4017A.9.1 V2X
Tests in FR1 4017A.9.1.1 Test for V2X UE Transmit Timing 4017A.9.1.1.1
Test for GNSS as Synchronization Reference Source 4017A.9.1.1.1.1 Test
Purpose and Environment 4017A.9.1.1.1.2 Test requirements 4017A.9.1.1.2
Test for SyncRef UE as Synchronization Reference Source 4017A.9.1.1.2.1
Test Purpose and Environment 4017A.9.1.1.2.2 Test requirements
4018A.9.1.1.3 Test for FR1 NR Cell as Synchronization Reference Source
4018A.9.1.1.3.1 Test Purpose and Environment 4018A.9.1.1.3.2 Test
requirements 4021A.9.1.2 Test for Initiation/Cease of S-SSB Transmission
with V2X Sidelink Communication 4021A.9.1.2.1 Test for FR1 NR Cell as
synchronization reference source without gap under non-DRX
4021A.9.1.2.1.1 Test Purpose and Environment 4021A.9.1.2.1.2 Test
Requirements 4024A.9.1.2.2 Test for SyncRef UE as synchronization
reference source 4024A.9.1.2.2.1 Test Purpose and Environment
4024A.9.1.2.2.2 Test Requirements 4026A.9.1.2.3 Test for SyncRef UE as
synchronization reference source when SL-DRX is used 4026A.9.1.2.3.1
Test Purpose and Environment 4026A.9.1.2.3.2 Test Requirements
4028A.9.1.3 Test for V2X Synchronization Reference Selection/Reselection
4028A.9.1.3.1 Test for GNSS configured as the highest priority
4028A.9.1.3.1.1 Test Purpose and Environment 4028A.9.1.3.1.2 Test
Requirements 4030A.9.1.3.2 Test for FR1 NR Cell configured as the
highest priority 4031A.9.1.3.2.1 Test Purpose and Environment
4031A.9.1.3.2.2 Test Requirements 4033A.9.1.3.3 Test for GNSS configured
as the highest priority under SL-DRX 4034A.9.1.3.3.1 Test Purpose and
Environment 4034A.9.1.3.3.2 Test Requirements 4036A.9.1.3.4 Test for FR1
NR Cell configured as the highest priority under SL-DRX 4037A.9.1.3.4.1
Test Purpose and Environment 4037A.9.1.3.4.2 Test Requirements
4039A.9.1.4 Test for L1 SL-RSRP Measurement 4040A.9.1.4.1 Test for V2X
UE Autonomous Resource Selection/Reselection 4040A.9.1.4.1.1 Test
Purpose and Environment 4040A.9.1.4.1.2 Test Requirements 4043A.9.1.4.2
Test for V2X UE Resource Pre-emption 4043A.9.1.4.2.1 Test Purpose and
Environment 4043A.9.1.4.2.2 Test Requirements 4047A.9.1.4.3 Test for V2X
UE Resource Re-evaluation 4047A.9.1.4.3.1 Test Purpose and Environment
4047A.9.1.4.3.2 Test Requirements 4054A.9.1.4.4 Test for V2X UE
Autonomous Resource Selection/Reselection with Periodic Sensing
4054A.9.1.4.4.1 Test Purpose and Environment 4054A.9.1.4.4.2 Test
Requirements 4058A.9.1.4.5 Test for V2X UE Autonomous Resource
Selection/Reselection with Contiguous Sensing 4058A.9.1.4.5.1 Test
Purpose and Environment 4058A.9.1.4.5.2 Test Requirements 4061A.9.1.4.6
Test for V2X UE Autonomous Resource Selection/Reselection in SL-DRX
4061A.9.1.4.6.1 Test Purpose and Environment 4061A.9.1.4.6.2 Test
Requirements 4065A.9.1.5 Test for Congestion Control Measurement
4065A.9.1.5.1 Test Purpose and Environment 4065A.9.1.5.2 Test
Requirements 4071A.9.1.6 Test for Interruption 4071A.9.1.6.1 Test for
Interruption to WAN due to V2X Sidelink Communication 4071A.9.1.6.1.1
Test Purpose and Environment 4071A.9.1.6.1.2 Test Requirements
4074A.9.1.6.2 Test for interruption to WAN at transitions between active
and non-active during SL-DRX in asynchronous case 4074A.9.1.6.2.1 Test
Purpose and Environment 4074A.9.1.6.2.2 Test Requirements 4078A.9.1.6.3
Test for Interruption at NR Sidelink Diccovery Configuration
4078A.9.1.6.3.1 Test Purpose and Environment 4078A.9.1.6.3.2 Test
Requirements 4081A.9.1.7 Selection / Reselection of relay UE
4081A.9.1.7.1 Test Purpose and Environment 4081A.9.1.7.2 Test
Requirements 4087A.10 EN-DC Tests with NR PSCell under CCA and Other NR
Cells in FR1 4089A.10.1 RRC\_CONNECTED state mobility 4089A.10.1.1 RRC
connection mobility control 4089A.10.1.1.1 Random Access
4089A.10.1.1.1.1 4-step RA type contention-based random access for NR
PSCell with CCA 4089A.10.1.1.1.1.1 Test Purpose and Environment
4089A.10.1.1.1.1.2 Test Requirements 4092A.10.1.1.1.1.2.1 Random Access
Preamble Transmission 4092A.10.1.1.1.1.2.2 Random Access Response
Reception 4092A.10.1.1.1.1.2.3 No Random Access Response Reception
4093A.10.1.1.1.1.2.4 Receiving an UL grant for msg3 retransmission
4093A.10.1.1.1.1.2.5 Contention Resolution Timer expiry 4093A.10.1.1.1.2
4-step RA type non-contention based random access for NR PSCell with CCA
4094A.10.1.1.1.2.1 Test Purpose and Environment 4094A.10.1.1.1.2.2 Test
Requirements 4097A.10.1.1.1.2.2.1 SSB-based Random Access Preamble
Transmission 4097A.10.1.1.1.2.2.2 Random Access Response Reception
4098A.10.1.1.1.2.2.3 No Random Access Response Reception
4098A.10.1.1.1.3 2-step RA type contention-based random access for NR
PSCell with CCA 4098A.10.1.1.1.3.1 Test Purpose and Environment
4098A.10.1.1.1.3.2 Test Requirements 4102A.10.1.1.1.3.2.1 MsgA
Transmission 4102A.10.1.1.1.3.2.2 MsgB Reception 4102A.10.1.1.1.3.2.3 No
MsgB Reception 4103A.10.1.1.1.4 2-step RA type non-contention based
random access for NR PSCell with CCA 4103A.10.1.1.1.4.1 Test Purpose and
Environment 4103A.10.1.1.1.4.2 Test Requirements 4107A.10.1.1.1.4.2.1
MsgA Transmission 4107A.10.1.1.1.4.2.2 MsgB Reception
4108A.10.1.1.1.4.2.3 No MsgB Reception 4108**A.10.1.2** **Handover with
PSCell from EN-DC to EN-DC with known target PSCell using CCA**
4108A.10.1.2.1 Test Purpose and Environment 4108A.**10.1**.2.2 Test
Requirements 4115A.10.2 Timing 4116A.10.2.1 UE transmit timing
4116A.10.2.1.1 UE Transmit Timing Test with PSCell under DL CCA
4116A.10.2.1.1.1 Test Purpose and environment 4116A.10.2.1.1.2 Test
requirements 4119A.10.2.2 UE timing advance 4120A.10.2.2.1 UE Timing
Advance Adjustment Accuracy with PSCell under DL CCA 4120A.10.2.2.1.1
Test Purpose and Environment 4120A.10.2.2.1.2 Test Parameters
4120A.10.2.2.1.3 Test Requirements 4124A.10.3 Signalling characteristics
4124A.10.3.1 Radio link monitoring 4124A.10.3.1.1 Introduction
4124A.10.3.1.2 Radio link monitoring out-of-sync test for PSCell
configured with SSB-based RLM RS in non-DRX mode 4125A.10.3.1.2.1 Test
purpose and environment 4125A.10.3.1.2.2 Test requirements
4129A.10.3.1.3 Radio link monitoring in-sync test for PSCell configured
with SSB-based RLM RS in non-DRX mode 4130A.10.3.1.3.1 Test purpose and
environment 4130A.10.3.1.3.2 Test requirements 4135A.10.3.1.4 Void
4135A.10.3.1.4.1 Void 4135A.10.3.1.4.2 Void 4135A.10.3.1.5 Void
4135A.10.3.1.5.1 Void 4135A.10.3.1.5.2 Void 4135A.10.3.2 Void
4135A.10.3.3 SCell activation and deactivation delay 4135A.10.3.3.1
SCell Activation and Deactivation of known NR SCell with NR PSCell and
NR SCell under CCA, 160 ms SCell measurement cycle 4135A.10.3.3.1.1 Test
Purpose and Environment 4135A.10.3.3.1.2 Test Requirements
4140A.10.3.3.2 SCell Activation and Deactivation of known NR SCell with
NR PSCell and NR SCell under CCA, 640 ms SCell measurement cycle
4140A.10.3.3.2.1 Test Purpose and Environment 4140A.10.3.3.2.2 Test
Requirements 4141A.10.3.3.3 SCell Activation and Deactivation of unknown
NR SCell with NR PSCell and NR SCell under CCA 4141A.10.3.3.3.1 Test
Purpose and Environment 4141A.10.3.3.3.2 Test Requirements 4142A.10.3.4
Beam failure detection and link recovery procedures 4142A.10.3.4.1 EN-DC
Beam Failure Detection and Link Recovery Test for FR1 PSCell configured
with SSB-based BFD and LR in non-DRX mode 4142A.10.3.4.1.1 Test Purpose
and Environment 4142A.10.3.4.1.2 Test Requirements 4147A.10.3.4.2 EN-DC
Beam Failure Detection and Link Recovery Test for FR1 PSCell configured
with SSB-based BFD and LR in DRX mode 4147A.10.3.4.2.1 Test Purpose and
Environment 4147A.10.3.4.2.2 Test Requirements 4153A.10.3.5 Active BWP
switching 4153A.10.3.5.1 UL active BWP switch delay with consistent UL
LBT failure on PSCell subject to UL CCA in EN-DC 4153A.10.3.5.1.2 Test
Requirements 4158A.10.3.5.2 DCI-based and Timer-based Active BWP Switch
4159A.10.3.5.2.1 E-UTRAN -- NR PSCell FR1 DL active BWP switch in
non-DRX in synchronous EN-DC 4159A.10.3.5.2.2 E-UTRAN -- NR PSCell FR1
DL active BWP switch with FR1 SCell in non-DRX in synchronous EN-DC
4162A.10.3.5.3 RRC-based Active BWP Switch 4166A.10.3.5.3.1 E-UTRAN --
NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC
4166A.10.3.6 PSCell addition and release delay 4170A.10.3.6.1 Addition
and Release Delay of known NR PSCell on the carrier under CCA
4170A.10.3.6.1.1 Test purpose and environment 4170A.10.3.6.1.2 Test
Requirements 4175A.10.3.7 Void 4176A.10.4 Measurement procedure
4176A.10.4.1 Intra-frequency measurements 4176A.10.4.1.1 Event-triggered
reporting tests on PSCC without gaps under non-DRX 4176A.10.4.1.1.1 Test
purpose and environment 4176A.10.4.1.1.2 Test parameters
4176A.10.4.1.1.3 Test Requirements 4179A.10.4.1.2 Void 4179A.10.4.1.3
Void 4179A.10.4.1.4 Event-triggered reporting tests on PSCC with per-UE
gaps under DRX 4179A.10.4.1.4.1 Test purpose and environment
4179A.10.4.1.4.2 Test parameters 4180A.10.4.1.4.3 Test Requirements
4184A.10.4.1.5 Void 4185A.10.4.1.6 Void 4185A.10.4.1.7 Void
4185A.10.4.1.8 Void 4185A.10.4.1.9 Void 4185A.10.4.1.10 Void
4185A.10.4.1.11 Void 4185A.10.4.1.12 Void 4185A.10.4.2 Inter-frequency
measurements 4185A.10.4.2.1 Void 4185A.10.4.2.2 Void 4185A.10.4.2.3
EN-DC event triggered reporting tests for FR1 with CCA cell without SSB
time index detection when DRX is not used 4185A.10.4.2.3.1 Test Purpose
and Environment 4185A.10.4.2.3.2 Test Requirements 4189A.10.4.2.4 EN-DC
event triggered reporting tests for FR1 cell with CCA without SSB time
index detection when DRX is used 4190A.10.4.2.4.1 Test Purpose and
Environment 4190A.10.4.2.4.2 Test Requirements 4195A.10.4.2.5 EN-DC
event triggered reporting tests for FR1 cell with CCA with SSB time
index detection when DRX is not used 4195A.10.4.2.5.1 Test Purpose and
Environment 4195A.10.4.2.5.2 Test Requirements 4199A.10.4.2.6 EN-DC
event triggered reporting tests for FR1 cell with CCA with SSB time
index detection when DRX is used 4200A.10.4.2.6.1 Test Purpose and
Environment 4200A.10.4.2.6.2 Test Requirements 4205A.10.4.2.7 EN-DC
event triggered reporting tests for FR1 cell without SSB time index
detection when DRX is not used 4205A.10.4.2.7.1 Test Purpose and
Environment 4205A.10.4.2.7.2 Test Requirements 4211A.10.4.2.8 EN-DC
event triggered reporting tests for FR1 cell without SSB time index
detection when DRX is used 4211A.10.4.2.8.1 Test Purpose and Environment
4211A.10.4.2.8.2 Test Requirements 4217A.10.4.2.9 EN-DC event triggered
reporting tests for FR1 cell with SSB time index detection when DRX is
not used 4217A.10.4.2.9.1 Test Purpose and Environment 4217A.10.4.2.9.2
Test Requirements 4223A.10.4.2.10 EN-DC event triggered reporting tests
for FR1 cell with SSB time index detection when DRX is used
4223A.10.4.2.10.1 Test Purpose and Environment 4223A.10.4.2.10.2 Test
Requirements 4229A.10.4.3 L1-RSRP measurements for beam reporting
4230A.10.4.3.1 SSB based L1-RSRP measurement on PSCC when DRX is not
used 4230A.10.4.3.1.1 Test Purpose and Environment 4230A.10.4.3.1.2 Test
parameters 4230A.10.4.3.1.3 Test Requirements 4232A.10.4.3.2 SSB based
L1-RSRP measurement on PSCC when DRX is used 4233A.10.4.3.2.1 Test
Purpose and Environment 4233A.10.4.3.2.2 Test parameters
4233A.10.4.3.2.3 Test Requirements 4235A.10.4.3.3 SSB based L1-RSRP
measurement on SCC when DRX is not used 4236A.10.4.3.3.1 Test Purpose
and Environment 4236A.10.4.3.3.2 Test parameters 4236A.10.4.3.3.3 Test
Requirements 4239A.10.4.3.4 SSB based L1-RSRP measurement on SCC when
DRX is used 4240A.10.4.3.4.1 Test Purpose and Environment
4240A.10.4.3.4.2 Test parameters 4240A.10.4.3.4.3 Test Requirements
4243A.10.4.4 E-UTRAN−NR inter-RAT measurements on NR carrier frequency
under CCA 4244A.10.4.4.1 E-UTRA-NR inter-RAT event triggered reporting
tests for FR1 without SSB time index detection when DRX is not used
4244A.10.4.4.1.1 Test Purpose and Environment 4244A.10.4.4.1.2 Test
Requirements 4251A.10.4.4.2 E-UTRA-NR inter-RAT event triggered
reporting tests for FR1 without SSB time index detection when DRX is
used 4251A.10.4.4.2.1 Test Purpose and Environment 4251A.10.4.4.2.2 Test
Requirements 4258A.10.4.4.3 NR Inter-RAT event triggered reporting tests
for FR1 with SSB time index detection when DRX is not used
4258A.10.4.4.3.1 Test Purpose and Environment 4258A.10.4.4.3.2 Test
Requirements 4266A.10.4.4.4 NR Inter-RAT event triggered reporting tests
for FR1 with SSB time index detection when DRX is used 4266A.10.4.4.4.1
Test Purpose and Environment 4266A.10.4.4.4.2 Test Requirements
4274A.10.5 Measurement performance 4274A.10.5.1 SS-RSRP 4274A.10.5.1.1
Intra-frequency measurement accuracy on a CCA serving cell
4274A.10.5.1.1.1 Test Purpose and Environment 4274A.10.5.1.1.2 Test
parameters 4274A.10.5.1.1.3 Test Requirements 4277A.10.5.1.2
Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1
CCA target cell 4277A.10.5.1.2.1 Test Purpose and Environment
4277A.10.5.1.2.2 Test parameters 4277A.10.5.1.2.3 Test Requirements
4280A.10.5.2 SS-RSRQ 4280**A.10.5.2.1** **Intra-frequency measurement
accuracy with FR1 CCA serving cell and FR1 CCA target cell**
4280A.10.5.2.1.1 Test Purpose and Environment 4280A.10.5.2.1.2 Test
Parameters 4280A.10.5.2.1.3 Test Requirements 4283**A.10.5.2.2**
**Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1
CCA target cell** 4283A.10.5.2.2.1 Test Purpose and Environment
4283A.10.5.2.2.2 Test Parameters 4283A.10.5.2.2.3 Test Requirements
4286A.10.5.3 SS-SINR 4286A.10.5.3.1 Intra-frequency measurement accuracy
on PSCC 4286A.10.5.3.1.1 Test Purpose and Environment 4286A.10.5.3.1.2
Test Parameters 4286A.10.5.3.1.3 Test Requirements 4289A.10.5.3.2
Inter-frequency measurement accuracy on PSCC 4289A.10.5.3.2.1 Test
Purpose and Environment 4289A.10.5.3.2.2 Test Parameters
4289A.10.5.3.2.3 Test Requirements 4292A.10.5.3.3 Intra-frequency
measurement accuracy on SCC 4292A.10.5.3.3.1 Test Purpose and
Environment 4292A.10.5.3.3.2 Test Parameters 4292A.10.5.3.3.3 Test
Requirements 4295A.10.5.4 L1-RSRP measurement for beam reporting with
CCA serving cell 4295A.10.5.4.1 SSB based L1-RSRP measurement
4295A.10.5.4.1.1 Test Purpose and Environment 4295A.10.5.4.1.2 Test
parameters 4296A.10.5.4.1.3 Test Requirements 4298A.10.5.5 RSSI
4298A.10.5.5.1 RSSI measurement accuracy on PSCC with CCA
4298A.10.5.5.1.1 Test Purpose and Environment 4298A.10.5.5.1.2 Test
parameters 4298A.10.5.5.1.3 Test Requirements 4301A.10.5.5.2 RSSI
measurement accuracy on SCC with CCA 4301A.10.5.5.2.1 Test Purpose and
Environment 4301A.10.5.5.2.2 Test parameters 4301A.10.5.5.2.3 Test
Requirements 4304A.10.5.5.3 Inter-frequency RSSI measurement accuracy on
a carrier with CCA 4304A.10.5.5.3.1 Test Purpose and Environment
4304A.10.5.5.3.2 Test parameters 4304A.10.5.5.3.3 Test Requirements
4308A.10.5.6 Channel occupancy 4308A.10.5.6.1 Channel occupancy
measurement accuracy on PSCC with CCA 4308A.10.5.6.1.1 Test Purpose and
Environment 4308A.10.5.6.1.2 Test parameters 4308A.10.5.6.1.3 Test
Requirements 4312A.10.5.6.2 Channel occupancy measurement accuracy on
SCC with CCA 4312A.10.5.6.2.1 Test Purpose and Environment
4312A.10.5.6.2.2 Test parameters 4312A.10.5.6.2.3 Test Requirements
4315A.10.5.6.3 Inter-frequency channel occupancy measurement accuracy on
a carrier with CCA 4315A.10.5.6.3.1 Test Purpose and Environment
4315A.10.5.6.3.2 Test parameters 4315A.10.5.6.3.3 Test Requirements
4319A.11 NR Standalone Tests with NR PCell under CCA and Other NR Cells
in FR1 4317A.11.1 RRC\_IDLE state mobility 4317A.11.1.1 Cell
re-selection with both source and target NR carrier frequencies under
CCA 4317A.11.1.1.1 Cell reselection to FR1 intra-frequency NR cells when
subject to CCA on the serving and target cell 4317A.11.1.1.1.1 Test
Purpose and Environment 4317A.11.1.1.1.2 Test Parameters
4317A.11.1.1.1.3 Test Requirements 4320A.11.1.1.2 Cell reselection to
FR1 inter-frequency NR case when subject to CCA on the serving and
target cell 4320A.11.1.1.2.1 Test Purpose and Environment
4320A.11.1.1.2.2 Test Parameters 4320A.11.1.1.2.3 Test Requirements
4324A.11.1.2 Cell re-selection to NR with source NR carrier frequency
under CCA 4324A.11.1.2.1 Cell reselection to FR1 inter-frequency NR case
when serving cell is subject to CCA 4324A.11.1.2.1.1 Test Purpose and
Environment 4324A.11.1.2.1.2 Test Parameters 4325A.11.1.2.1.3 Test
Requirements 4330A.11.1.3 Cell re-selection from NR carrier with target
NR carrier frequency under CCA 4331A.11.1.3.1 Cell reselection to FR1
inter-frequency NR case when target cell is subject to CCA
4331A.11.1.3.1.1 Test Purpose and Environment 4331A.11.1.3.1.2 Test
Parameters 4331A.11.1.3.1.3 Test Requirements 4337A.11.1.4 Inter-RAT
cell re-selection to E-UTRAN with source NR carrier frequency under CCA
4338A.11.1.4.1 Cell reselection to higher priority E-UTRAN when serving
cell is subject to CCA 4338A.11.1.4.1.1 Test Purpose and Environment
4338A.11.1.4.1.2 Test Parameters 4338A.11.1.4.1.3 Test Requirements
4341A.11.1.4.2 Cell reselection to lower priority E-UTRAN when serving
cell is subject to CCA 4342A.11.1.4.2.1 Test Purpose and Environment
4342A.11.1.4.2.2 Test Requirements 4345A.11.2 RRC\_CONNECTED state
mobility 4346A.11.2.1 Handover 4346A.11.2.1.1 Intra-frequency handover
from FR1 carrier under CCA to FR1 carrier under CCA; known target cell
4346A.11.2.1.1.1 Test Purpose and Environment 4346A.11.2.1.1.2 Test
Parameters 4346A.11.2.1.1.3 Test Requirements 4349A.11.2.1.2
Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under
CCA; unknown target cell 4349A.11.2.1.2.1 Test Purpose and Environment
4349A.11.2.1.2.2 Test Parameters 4349A.11.2.1.2.3 Test Requirements
4352A.11.2.1.3 Inter-frequency handover from FR1 carrier under CCA to
FR1 carrier under CCA; unknown target cell 4352A.11.2.1.3.1 Test Purpose
and Environment 4352A.11.2.1.3.2 Test Parameters 4352A.11.2.1.3.3 Test
Requirements 4355A.11.2.1.4 Inter-frequency handover from FR1 carrier
under CCA to FR1; known target cell 4355A.11.2.1.4.1 Test Purpose and
Environment 4355A.11.2.1.4.2 Test Parameters 4355A.11.2.1.4.3 Test
Requirements 4359A.11.2.1.5 Inter-frequency handover from FR1 carrier
under CCA to FR1; unknown target cell 4360A.11.2.1.5.1 Test Purpose and
Environment 4360A.11.2.1.5.2 Test Parameters 4360A.11.2.1.5.3 Test
Requirements 4363A.11.2.1.6 Inter-frequency handover from FR1 to FR1
carrier under CCA; unknown target cell 4364A.11.2.1.6.1 Test Purpose and
Environment 4364A.11.2.1.6.2 Test Parameters 4364A.11.2.1.6.3 Test
Requirements 4368A.11.2.1.7 SA NR FR1 carrier under CCA - E-UTRAN
handover with known target cell 4369A.11.2.1.7.1 Test Purpose and
Environment 4369A.11.2.1.7.2 Test Requirements 4375A.11.2.1.8 SA NR FR1
carrier under CCA - E-UTRAN handover with unknown target cell
4375A.11.2.1.8.1 Test Purpose and Environment 4375A.11.2.1.8.2 Test
Requirements 4380A.11.2.1.9 Handover with PSCell from NR SA to EN-DC
with known target PSCell using CCA 4380A.11.2.1.9.1 Test Purpose and
Environment 4380A.11.2.1.9.2 Test Requirements 4389A.11.2.2 RRC
connection mobility control 4390A.11.2.2.1 RRC re-establishment
4390A.11.2.2.1.1 Intra-frequency RRC Re-establishment with CCA in FR1
4390A.11.2.2.1.2 Inter-frequency RRC Re-establishment with CCA in FR1
4393A.11.2.2.1.4 Inter-frequency RRC Re-establishment from NR FR1
carrier without CCA to NR FR1 carrier under CCA 4400A.11.2.2.2 Random
Access 4406A.11.2.2.2.1 4-step RA type contention-based random access
for NR PCell with CCA 4406A.11.2.2.2.1.1 Test Purpose and Environment
4406A.11.2.2.2.1.2 Test Requirements 4409A.11.2.2.2.1.2.1 Random Access
Preamble Transmission 4409A.11.2.2.2.1.2.2 Random Access Response
Reception 4409A.11.2.2.2.1.2.3 No Random Access Response Reception
4410A.11.2.2.2.1.2.4 Receiving an UL grant for msg3 retransmission
4410A.11.2.2.2.1.2.5 Reception of an Incorrect Message over Temporary
C-RNTI 4410A.11.2.2.2.1.2.6 Reception of a Correct Message over
Temporary C-RNTI 4411A.11.2.2.2.1.2.7 Contention Resolution Timer expiry
4411A.11.2.2.2.2 4-step RA type non-contention based random access for
NR PSCell with CCA 4411A.11.2.2.2.2.1 Test Purpose and Environment
4411A.11.2.2.2.2.2 Test Requirements 4414A.11.2.2.2.2.2.1 SSB-based
Random Access Preamble Transmission 4414A.11.2.2.2.2.2.2 Random Access
Response Reception 4415A.11.2.2.2.2.2.3 No Random Access Response
Reception 4415A.11.2.2.2.3 2-step RA type contention-based random access
for NR PCell with CCA 4415A.11.2.2.2.3.1 Test Purpose and Environment
4415A.11.2.2.2.3.2 Test Requirements 4419A.11.2.2.2.3.2.1 MsgA
Transmission 4419A.11.2.2.2.3.2.2 MsgB Reception 4419A.11.2.2.2.3.2.3 No
MsgB Reception 4420A.11.2.2.2.4 2-step RA type non-contention-based
random access for NR PCell with CCA 4420A.11.2.2.2.4.1 Test Purpose and
Environment 4420A.11.2.2.2.4.2 Test Requirements 4424A.11.2.2.2.4.2.1
MsgA Transmission 4424A.11.2.2.2.4.2.2 MsgB Reception
4425A.11.2.2.2.4.2.3 No MsgB Reception 4425A.11.2.2.3 RRC connection
release with redirection 4426A.11.2.2.3.1 Redirection from NR FR1
carrier under CCA to NR FR1 carrier under CCA 4426A.11.2.2.3.2
Redirection from NR FR1 carrier without CCA to NR FR1 carrier with CCA
4430A.11.3 Timing 4435A.11.3.1 UE transmit timing 4435A.11.3.1.1 UE
Transmit Timing Test with PCell under DL CCA 4435A.11.3.1.1.1 Test
Purpose and environment 4435A.11.3.1.1.2 Test requirements 4438A.11.3.2
UE timing advance 4439A.11.3.2.1 UE Timing Advance Adjustment Accuracy
with PCell under DL CCA 4439A.11.3.2.1.1 Test Purpose and Environment
4439A.11.3.2.1.2 Test Parameters 4439A.11.3.2.1.3 Test Requirements
4443A.11.4 Signalling characteristics 4443A.11.4.1 Radio link monitoring
4443A.11.4.1.1 Introduction 4443A.11.4.1.2 Radio link monitoring
out-of-sync test for PCell configured with SSB-based RLM RS in non-DRX
mode 4444A.11.4.1.2.1 Test purpose and environment 4444A.11.4.1.2.2 Test
requirements 4448A.11.4.1.3 Radio link monitoring in-sync test for PCell
configured with SSB-based RLM RS in non-DRX mode 4448A.11.4.1.3.1 Test
purpose and environment 4448A.11.4.1.3.2 Test requirements
4454A.11.4.1.4 Void 4455A.11.4.1.4.1 Void 4455A.11.4.1.4.2 Void
4455A.11.4.1.5 Void 4455A.11.4.1.5.1 Void 4455A.11.4.1.5.2 Void
4455A.11.4.2 Void 4455A.11.4.3 SCell activation and deactivation delay
4455A.11.4.3.1 SCell Activation and Deactivation of known SCell with
PCell and SCell under CCA, 160 ms SCell measurement cycle
4455A.11.4.3.1.1 Test Purpose and Environment 4455A.11.4.3.1.2 Test
Requirements 4459A.11.4.3.2 SCell Activation and Deactivation of known
SCell with PCell and SCell under CCA, 640 ms SCell measurement cycle
4459A.11.4.3.2.1 Test Purpose and Environment 4459A.11.4.3.2.2 Test
Requirements 4460A.11.4.3.3 SCell Activation and Deactivation of unknown
SCell with PCell and SCell under CCA 4460A.11.4.3.3.1 Test Purpose and
Environment 4460A.11.4.3.3.2 Test Requirements 4461A.11.4.4 Beam failure
detection and link recovery procedures 4461A.11.4.4.1 Beam Failure
Detection and Link Recovery Test for FR1 PCell configured with SSB-based
BFD and LR in non-DRX mode 4461A.11.4.4.1.1 Test Purpose and Environment
4461A.11.4.4.1.2 Test Requirements 4466A.11.4.4.2 Beam Failure Detection
and Link Recovery Test for FR1 PCell configured with SSB-based BFD and
LR in DRX mode 4466A.11.4.4.2.1 Test Purpose and Environment
4466A.11.4.4.2.2 Test Requirements 4472A.11.4.5 Active BWP switching
4472A.11.4.5.1 UL active BWP switch delay with consistent UL LBT failure
on PCell subject to UL CCA 4472A.11.4.5.1.1 Test Purpose and Environment
4472A.11.4.5.1.2 Test Requirements 4476A.11.4.5.2 DCI-based and
Timer-based Active BWP Switch 4477A.11.4.5.2.1 NR FR1- NR FR1 DL active
BWP switch of PCell with non-DRX in SA 4477A.11.4.5.2.2 NR FR1 DL active
BWP switch with non-DRX in SA 4480A.11.4.5.3 RRC-based Active BWP Switch
4483A.11.4.5.3.1 NR FR1 DL active BWP switch of Cell with non-DRX in SA
4483A.11.4.6 Void 4486A.11.5 Measurement procedure 4486A.11.5.1
Intra-frequency measurements 4486A.11.5.1.1 Event-triggered reporting
tests on PCC without gaps under non-DRX 4486A.11.5.1.1.1 Test purpose
and environment 4486A.11.5.1.1.2 Test parameters 4486A.11.5.1.1.3 Test
Requirements 4490A.11.5.1.2 Event-triggered reporting tests on PCC
without gaps under DRX 4490A.11.5.1.2.1 Test purpose and environment
4490A.11.5.1.2.2 Test parameters 4490A.11.5.1.2.3 Test Requirements
4493A.11.5.1.3 Void 4494A.11.5.1.4 Void 4494A.11.5.1.5 Void
4494A.11.5.1.6 Void 4494A.11.5.1.7 Void 4494A.11.5.1.8 Void
4494A.11.5.1.9 Void 4494A.11.5.1.10 Void 4494A.11.5.1.11 Void
4494A.11.5.1.12 Void 4494A.11.5.2 Inter-frequency measurements
4494A.11.5.2.1 Void 4494A.11.5.2.2 Void 4494A.11.5.2.3 Event triggered
reporting tests for FR1 with CCA without SSB time index detection when
DRX is not used 4494A.11.5.2.3.1 Test Purpose and Environment
4494A.11.5.2.3.2 Test Requirements 4498A.11.5.2.4 Event triggered
reporting tests for FR1 with CCA without SSB time index detection when
DRX is used 4499A.11.5.2.4.1 Test Purpose and Environment
4499A.11.5.2.4.2 Test Requirements 4504A.11.5.2.5 Event triggered
reporting tests for FR1 with CCA with SSB time index detection when DRX
is not used 4504A.11.5.2.5.1 Test Purpose and Environment
4504A.11.5.2.5.2 Test Requirements 4508A.11.5.2.6 Event triggered
reporting tests for FR1 with CCA with SSB time index detection when DRX
is used 4509A.11.5.2.6.1 Test Purpose and Environment 4509A.11.5.2.6.2
Test Requirements 4514A.11.5.2.7 Event triggered reporting tests for FR1
without SSB time index detection when DRX is not used 4514A.11.5.2.7.1
Test Purpose and Environment 4514A.11.5.2.7.2 Test Requirements
4518A.11.5.2.8 Event triggered reporting tests for FR1 without SSB time
index detection when DRX is used 4519A.11.5.2.8.1 Test Purpose and
Environment 4519A.11.5.2.8.2 Test Requirements 4524A.11.5.2.9 Event
triggered reporting tests for FR1 with SSB time index detection when DRX
is not used 4524A.11.5.2.9.1 Test Purpose and Environment
4524A.11.5.2.9.2 Test Requirements 4528A.11.5.2.10 Event triggered
reporting tests for FR1 with SSB time index detection when DRX is used
4529A.11.5.2.10.1 Test Purpose and Environment 4529A.11.5.2.10.2 Test
Requirements 4534A.11.5.3 Inter-RAT E-UTRAN measurements 4534A.11.5.3.1
SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1
4534A.11.5.3.1.1 Test Purpose and Environment 4534A.11.5.3.1.2 Test
Requirements 4540A.11.5.3.2 SA NR - E-UTRAN event-triggered reporting in
DRX in FR1 4540A.11.5.3.2.1 Test Purpose and Environment
4540A.11.5.3.2.2 Test Requirements 4546A.11.5.4 L1-RSRP measurements for
beam reporting 4546A.11.5.4.1 SSB based L1-RSRP measurement when DRX is
not used 4546A.11.5.4.1.1 Test Purpose and Environment 4546A.11.5.4.1.2
Test parameters 4546A.11.5.4.1.3 Test Requirements 4548A.11.5.4.2 SSB
based L1-RSRP measurement when DRX is used 4548A.11.5.4.2.1 Test Purpose
and Environment 4548A.11.5.4.2.2 Test parameters 4549A.11.5.4.2.3 Test
Requirements 4551A.11.5.4.3 SSB based L1-RSRP measurement on SCC when
DRX is not used 4551A.11.5.4.3.1 Test Purpose and Environment
4551A.11.5.4.3.2 Test parameters 4552A.11.5.4.3.3 Test Requirements
4555A.11.5.4.4 SSB based L1-RSRP measurement on SCC when DRX is used
4556A.11.5.4.4.1 Test Purpose and Environment 4556A.11.5.4.4.2 Test
parameters 4556A.11.5.4.4.3 Test Requirements 4559A.11.6 Measurement
performance 4560A.11.6.1 SS-RSRP 4560A.11.6.1.1 Intra-frequency
measurement accuracy on a carrier frequency with CCA 4560A.11.6.1.1.1
Test Purpose and Environment 4560A.11.6.1.1.2 Test parameters
4560A.11.6.1.1.3 Test Requirements 4562A.11.6.1.2 Intra-frequency
measurement accuracy on SCC on a carrier frequency with CCA
4562A.11.6.1.2.1 Test Purpose and Environment 4562A.11.6.1.2.2 Test
parameters 4562A.11.6.1.2.3 Test Requirements 4565A.11.6.2 SS-RSRQ
4565A.11.6.2.1 Intra-frequency measurement accuracy 4565A.11.6.2.1.1
Test Purpose and Environment 4565A.11.6.2.1.2 Test Parameters
4565A.11.6.2.1.3 Test Requirements 4568A.11.6.2.2 Inter-frequency
measurement accuracy 4568A.11.6.2.2.1 Test Purpose and Environment
4568A.11.6.2.2.2 Test Parameters 4568A.11.6.2.2.3 Test Requirements
4571A.11.6.2.3 Intra-frequency measurement accuracy on SCC
4571A.11.6.2.3.1 Test Purpose and Environment 4571A.11.6.2.3.2 Test
Parameters 4571A.11.6.2.3.3 Test Requirements 4574A.11.6.2.4
Inter-frequency measurement accuracy 4574A.11.6.2.4.1 Test Purpose and
Environment 4574A.11.6.2.4.2 Test Parameters 4574A.11.6.2.4.3 Test
Requirements 4581A.11.6.3 SS-SINR 4581A.11.6.3.1 Intra-frequency
measurement accuracy 4581A.11.6.3.1.1 Test Purpose and Environment
4581A.11.6.3.1.2 Test Parameters 4581A.11.6.3.1.3 Test Requirements
4584A.11.6.3.2 Inter-frequency measurement accuracy 4584A.11.6.3.2.1
Test Purpose and Environment 4584A.11.6.3.2.2 Test Parameters
4584A.11.6.3.2.3 Test Requirements 4587A.11.6.3.3 Intra-frequency
measurement accuracy on SCC 4587A.11.6.3.3.1 Test Purpose and
Environment 4587A.11.6.3.3.2 Test Parameters 4587A.11.6.3.3.3 Test
Requirements 4590A.11.6.3.4 Inter-frequency measurement accuracy
4590A.11.6.3.4.1 Test Purpose and Environment 4590A.11.6.3.4.2 Test
Parameters 4590A.11.6.3.4.3 Test Requirements 4598A.11.6.4 L1-RSRP
measurement for beam reporting with CCA serving cell 4598A.11.6.4.1 SSB
based L1-RSRP measurement 4598A.11.6.4.1.1 Test Purpose and Environment
4598A.11.6.4.1.2 Test parameters 4599A.11.6.4.1.3 Test Requirements
4602A.11.6.5 RSSI 4602A.11.6.5.1 Intra-frequency RSSI measurement
accuracy on PCC with CCA 4602A.11.6.5.1.1 Test Purpose and Environment
4602A.11.6.5.1.2 Test parameters 4602A.11.6.5.1.3 Test Requirements
4605A.11.6.5.2 Intra-frequency RSSI measurement accuracy on SCC with CCA
4605A.11.6.5.2.1 Test Purpose and Environment 4605A.11.6.5.2.2 Test
parameters 4605A.11.6.5.2.3 Test Requirements 4608A.11.6.5.3
Inter-frequency RSSI measurement accuracy on a carrier with CCA
4608A.11.6.5.3.1 Test Purpose and Environment 4608A.11.6.5.3.2 Test
parameters 4608A.11.6.5.3.3 Test Requirements 4612A.11.6.6 Channel
occupancy 4612A.11.6.6.1 Intra-frequency channel occupancy measurement
accuracy on PCC with CCA 4612A.11.6.6.1.1 Test Purpose and Environment
4612A.11.6.6.1.2 Test parameters 4612A.11.6.6.1.3 Test Requirements
4616A.11.6.6.2 Intra-frequency channel occupancy measurement accuracy on
SCC with CCA 4616A.11.6.6.2.1 Test Purpose and Environment
4616A.11.6.6.2.2 Test parameters 4616A.11.6.6.2.3 Test Requirements
4619A.11.6.6.3 Inter-frequency channel occupancy measurement accuracy on
a carrier with CCA 4619A.11.6.6.3.1 Test Purpose and Environment
4619A.11.6.6.3.2 Test parameters 4619A.11.6.6.3.3 Test Requirements
4623A.11.6.7 E-UTRAN RSRP 4624A.11.6.8 E-UTRAN RSRQ 4624A.11.6.9 E-UTRAN
SINR 4624A.12 E-UTRA Standalone Tests with at Least One NR Cell under
CCA 4624A.12.1 RRC\_IDLE state mobility 4624A.12.1.1 Inter-RAT cell
re-selection to NR on a carrier frequency with CCA 4624A.12.1.1.1 E-UTRA
Cell reselection to higher priority NR target Cell in FR1 when target
cell is subject to CCA 4624A.12.1.1.1.1 Test Purpose and Environment
4624A.12.1.1.1.2 Test Requirements 4629A.12.2 RRC\_CONNECTED state
mobility 4630A.12.2.1 Handover 4630A.12.2.1.1 E-UTRAN - NR with CCA
handover 4630A.12.2.1.1.1 Test Purpose and Environment 4630A.12.2.1.1.2
Test Requirements 4635A.12.3 Void 4636A.12.4 Measurement procedure
4636A.12.4.1 E-UTRAN−NR inter-RAT SFTD measurements 4636A.12.4.1.1
E-UTRA -- NR Inter-RAT SFTD Measurement Delay with NR under CCA in
non-DRX 4636A.12.4.1.1.1 Test Purpose and Environment 4636A.12.4.1.1.2
Test Requirements 4640A.12.4.2 E-UTRAN−NR inter-RAT measurements on NR
carrier frequency under CCA 4640A.12.4.2.1 E-UTRA-NR inter-RAT event
triggered reporting tests for FR1 without SSB time index detection when
DRX is not used 4640A.12.4.2.1.1 Test Purpose and Environment
4640A.12.4.2.1.2 Test Requirements 4646A.12.4.2.2 E-UTRA-NR inter-RAT
event triggered reporting tests for FR1 without SSB time index detection
when DRX is used 4646A.12.4.2.2.1 Test Purpose and Environment
4646A.12.4.2.2.2 Test Requirements 4652A.12.4.2.3 NR Inter-RAT event
triggered reporting tests for FR1 with SSB time index detection when DRX
is not used 4652A.12.4.2.3.1 Test Purpose and Environment
4652A.12.4.2.3.2 Test Requirements 4657A.12.4.2.4 NR Inter-RAT event
triggered reporting tests for FR1 with SSB time index detection when DRX
is used 4657A.12.4.2.4.1 Test Purpose and Environment 4657A.12.4.2.4.2
Test Requirements 4662A.12.4.2.5 Void 4662A.12.4.2.6 Void 4662A.12.5
Measurement performance 4662A.12.5.1 E-UTRAN−NR SFTD 4662A.12.5.1.1
Inter-RAT SFTD accuracy with NR target cell under CCA 4662A.12.5.1.1.1
Test Purpose 4662A.12.5.1.1.2 Test Environment 4662A.12.5.1.1.3 Test
Requirements 4667A.12.5.2 Void 4667A.12.5.3 Void 4667A.12.5.4 Void
4667A.12.5.5 Void 4667A.12.5.6 Void 4667A.13 NR Standalone Tests with NR
SCell under CCA and All Other NR Cells in FR1 4671A.13.1 Void 4671A.13.2
Signalling characteristics 4671A.13.2.1 Void 4671A.13.2.2 SCell
activation and deactivation delay 4671A.13.2.2.1 SCell Activation and
Deactivation of known SCell under CCA, 160 ms SCell measurement cycle
4671A.13.2.2.1.1 Test Purpose and Environment 4671A.13.2.2.1.2 Test
Requirements 4675A.13.2.2.2 SCell Activation and Deactivation of known
SCell under CCA, 640 ms SCell measurement cycle 4675A.13.2.2.2.1 Test
Purpose and Environment 4675A.13.2.2.2.2 Test Requirements
4676A.13.2.2.3 SCell Activation and Deactivation of unknown SCell under
CCA 4676A.13.2.2.3.1 Test Purpose and Environment 4676A.13.2.2.3.2 Test
Requirements 4677A.13.2.3 Void 4677A.13.3 Measurement procedure
4677A.13.3.1 Intra-frequency measurements 4677A.13.3.1.1 Event-triggered
reporting tests on SCC without gaps under non-DRX 4677A.13.3.1.1.1 Test
purpose and environment 4677A.13.3.1.1.2 Test parameters
4677A.13.3.1.1.3 Test Requirements 4682A.13.3.1.2 Event-triggered
reporting tests on SCC without gaps under DRX 4682A.13.3.1.2.1 Test
purpose and environment 4682A.13.3.1.2.2 Test parameters
4682A.13.3.1.2.3 Test Requirements 4687A.13.3.1.3 Event-triggered
reporting tests on SCC with per-UE gaps under non-DRX 4687A.13.3.1.3.1
Test purpose and environment 4687A.13.3.1.3.2 Test parameters
4687A.13.3.1.3.3 Test Requirements 4692A.13.3.1.4 Event-triggered
reporting tests on SCC with per-UE gaps under DRX 4692A.13.3.1.4.1 Test
purpose and environment 4692A.13.3.1.4.2 Test parameters
4692A.13.3.1.4.3 Test Requirements 4698A.13.3.1.5 Void 4698A.13.3.1.6
Void 4698A.13.3.2 Inter-frequency measurements 4698A.13.3.2.1 Void
4698A.13.3.2.2 Void 4698A.13.3.2.3 Event triggered reporting tests for
FR1 with CCA without SSB time index detection when DRX is not used
4698A.13.3.2.3.1 Test Purpose and Environment 4698A.13.3.2.3.2 Test
Requirements 4703A.13.3.2.4 Event triggered reporting tests for FR1 with
CCA without SSB time index detection when DRX is used 4703A.13.3.2.4.1
Test Purpose and Environment 4703A.13.3.2.4.2 Test Requirements
4708A.13.3.2.5 Event triggered reporting tests for FR1 with CCA with SSB
time index detection when DRX is not used 4709A.13.3.2.5.1 Test Purpose
and Environment 4709A.13.3.2.5.2 Test Requirements 4714A.13.3.2.6 Event
triggered reporting tests for FR1 with CCA with SSB time index detection
when DRX is used 4714A.13.3.2.6.1 Test Purpose and Environment
4714A.13.3.2.6.2 Test Requirements 4719A.13.3.3 L1-RSRP measurements for
beam reporting 4720A.13.3.3.1 SSB based L1-RSRP measurement when DRX is
not used 4720A.13.3.3.1.1 Test Purpose and Environment 4720A.13.3.3.1.2
Test parameters 4720A.13.3.3.1.3 Test Requirements 4724A.13.3.3.2 SSB
based L1-RSRP measurement when DRX is used 4724A.13.3.3.2.1 Test Purpose
and Environment 4724A.13.3.3.2.2 Test parameters 4724A.13.3.3.2.3 Test
Requirements 4728A.13.4 Measurement performance 4728A.13.4.1 SS-RSRP
4728A.13.4.1.1 Intra-frequency measurement accuracy on a carrier
frequency with CCA 4728A.13.4.1.1.1 Test Purpose and Environment
4728A.13.4.1.1.2 Test parameters 4728A.13.4.1.1.3 Test Requirements
4731A.13.4.2 SS-RSRQ 4731A.13.4.2.1 Intra-frequency measurement accuracy
on SCC 4731A.13.4.2.1.1 Test Purpose and Environment 4731A.13.4.2.1.2
Test Parameters 4731A.13.4.2.1.3 Test Requirements 4738A.13.4.3 SS-SINR
4738A.13.4.3.1 Intra-frequency measurement accuracy on SCC
4738A.13.4.3.1.1 Test Purpose and Environment 4738A.13.4.3.1.2 Test
Parameters 4738A.13.4.3.1.3 Test Requirements 4746A.13.4.4 L1-RSRP
measurement for beam reporting with CCA serving cell 4746A.13.4.4.1 SSB
based L1-RSRP measurement 4746A.13.4.4.1.1 Test Purpose and Environment
4746A.13.4.4.1.2 Test parameters 4746A.13.4.4.1.3 Test Requirements
4750A.13.4.5 RSSI 4750A.13.4.5.1 Intra-frequency RSSI measurement
accuracy on a carrier with CCA 4750A.13.4.5.1.1 Test Purpose and
Environment 4750A.13.4.5.1.2 Test parameters 4750A.13.4.5.1.3 Test
Requirements 4754A.13.4.5.2 Inter-frequency RSSI measurement accuracy on
a carrier with CCA 4754A.13.4.5.2.1 Test Purpose and Environment
4754A.13.4.5.2.2 Test parameters 4754A.13.4.5.2.3 Test Requirements
4758A.13.4.6 Channel occupancy 4758A.13.4.6.1 Intra-frequency channel
occupancy measurement accuracy on SCC with CCA 4758A.13.4.6.1.1 Test
Purpose and Environment 4758A.13.4.6.1.2 Test parameters
4758A.13.4.6.1.3 Test Requirements 4762A.13.4.6.2 Inter-frequency
channel occupancy measurement accuracy on a carrier with CCA
4762A.13.4.6.2.1 Test Purpose and Environment 4762A.13.4.6.2.2 Test
parameters 4762A.13.4.6.2.3 Test Requirements 4766A.14 NR standalone
tests for Satellite access 4766A.14.1 RRC\_IDLE state mobility
4766A.14.1.1 Cell reselection to FR1 intra-frequency NR case
4766A.14.1.1.1 Test Purpose and Environment 4766A.14.1.1.2 Test
Parameters 4766A.14.1.1.3 Test Requirements 4768A.14.1.2 Cell
reselection to FR1 intra-frequency NR cell for UE configured with the
feature for enhanced requirements 4769A.14.1.2.1 Test Purpose and
Environment 4769A.14.1.2.2 Test Parameters 4769A.14.1.2.3 Test
Requirements 4771A.14.1.3 Time-based measurement initiation to FR1
intra-frequency NR cell reselection 4772A.14.1.3.1 Test Purpose and
Environment 4772A.14.1.3.2 Test Parameters 4772A.14.1.3.3 Test
Requirements 4774A.14.1.4 Location-based cell measurement initiation to
FR1 intra-frequency NR cell reselection 4775A.14.1.4.1 Test Purpose and
Environment 4775A.14.1.4.2 Test Parameters 4775A.14.1.4.3 Test
Requirements 4777A.14.1.5 Cell reselection to FR1 inter-frequency NR
case 4778A.14.1.5.1 Test Purpose and Environment 4778A.14.1.5.2 Test
Parameters 4778A.14.1.5.3 Test Requirements 4780A.14.1.6 Cell
reselection to FR1 inter-frequency NR cell for UE configured with
feature for enhanced requirements 4781A.14.1.6.1 Test Purpose and
Environment 4781A.14.1.6.2 Test Parameters 4781A.14.1.6.3 Test
Requirements 4783A.14.1.7 Time-based Cell measurement initiation to FR1
inter-frequency cell reselection 4784A.14.1.7.1 Test Purpose and
Environment 4784A.14.1.7.2 Test Parameters 4784A.14.1.7.3 Test
Requirements 4786A.14.1.8 Location-based measurement initiation to FR1
inter-frequency NR cell reselection 4787A.14.1.8.1 Test Purpose and
Environment 4787A.14.1.8.2 Test Parameters 4787A.14.1.8.3 Test
Requirements 4789A.14.1.9 Cell reselection to FR1 inter-frequency NR
case for UE fulfilling low mobility relaxed measurement criterion
4790A.14.1.9.1 Test Purpose and Environment 4790A.14.1.9.2 Test
Parameters 4790A.14.1.9.3 Test Requirements 4793A.14.1.10 Cell
reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell
edge relaxed measurement criterion 4793A.14.1.10.1 Test Purpose and
Environment 4793A.14.1.10.2 Test Parameters 4793A.14.1.10.3 Test
Requirements 4795A.14.2 RRC\_CONNECTED state mobility 4796A.14.2.1
Handover 4796A.14.2.1.1 Intra-frequency SAN Handover from FR1 to FR1
4796A.14.2.1.1.1 Test Purpose and Environment 4796A.14.2.1.1.2 Test
Parameters 4796A.14.2.1.1.3 Test Requirements 4798A.14.2.1.2
Inter-frequency SAN Handover from FR1 to FR1 4799A.14.2.1.2.1 Test
Purpose and Environment 4799A.14.2.1.2.2 Test Parameters
4799A.14.2.1.2.3 Test Requirements 4801A.14.2.1.3 Intra-frequency SAN
time-based conditional Handover from FR1 to FR1 4801A.14.2.1.3.1 Test
Purpose and Environment 4801A.14.2.1.3.2 Test Parameters
4801A.14.2.1.3.3 Test Requirements 4805A.14.2.1.4 Inter-frequency SAN
time-based conditional Handover from FR1 to FR1 4805A.14.2.1.4.1 Test
Purpose and Environment 4805A.14.2.1.4.2 Test Parameters
4805A.14.2.1.4.3 Test Requirements 4807A.14.2.1.5 Intra-frequency SAN
distance-based conditional Handover from FR1 to FR1 4807A.14.2.1.5.1
Test Purpose and Environment 4807A.14.2.1.5.2 Test Parameters
4808A.14.2.1.5.3 Test Requirements 4811A.14.2.1.6 Inter-frequency SAN
distance-based conditional Handover from FR1 to FR1 4811A.14.2.1.6.1
Test Purpose and Environment 4811A.14.2.1.6.2 Test Parameters
4811A.14.2.1.6.3 Test Requirements 4815A.14.2.2 RRC Connection Mobility
Control 4815A.14.2.2.1 SA: RRC Re-establishment for SAN 4815A.14.2.2.1.1
Intra-frequency RRC Re-establishment in FR1 4815A.14.2.2.1.2
Inter-frequency RRC Re-establishment in FR1 4818A.14.2.2.2 Random Access
4821A.14.2.2.2.1 4-step RA type contention based random access test in
FR1 for NR standalone 4821A.14.2.2.2.1.1 Test Purpose and Environment
4821A.14.2.2.2.1.2 Test Requirements 4824A.14.2.2.2.2 4-step RA type
non-contention based random access test in FR1 for NR standalone
4825A.14.2.2.2.2.1 Test Purpose and Environment 4825A.14.2.2.2.2.2 Test
Requirements 4829A.14.2.2.3 RRC Connection Release with Redirection
4830A.14.2.2.3.1 Redirection from NR in FR1 to NR in FR1
4830A.14.2.2.3.1.1 Test Purpose and Environment 4830A.14.2.2.3.1.2 Test
Parameters 4830A.14.2.2.3.1.3 Test Requirements 4834A.14.3 Timing for
Satellite Access 4834A.14.3.1 UE transmit timing for Satellite Access
4834A.14.3.1.1 NR UE Transmit Timing Test for FR1 4834A.14.3.1.1.1 Test
Purpose and environment 4834A.14.3.1.1.2 Test requirements 4836A.14.3.2
Timing advance for satellite access 4837A.14.3.2.1 SA FR1 timing advance
adjustment accuracy 4837A.14.3.2.1.1 Test Purpose and Environment
4837A.14.3.2.1.2 Test Parameters 4837A.14.3.2.1.3 Test Requirements
4840A.14.4 Signalling characteristics 4840A.14.4.1 Radio link Monitoring
4840A.14.4.1.1 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell
configured with SSB-based RLM RS in non-DRX mode 4840A.14.4.1.1.1 Test
Purpose and Environment 4840A.14.4.1.1.2 Test Requirements
4845A.14.4.1.2 Radio Link Monitoring In-sync Test for FR1 SAN PCell
configured with SSB-based RLM RS in non-DRX mode 4845A.14.4.1.2.1 Test
Purpose and Environment 4845A.14.4.1.2.2 Test Requirements
4851A.14.4.1.3 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell
configured with SSB-based RLM RS in DRX mode 4851A.14.4.1.3.1 Test
Purpose and Environment 4851A.14.4.1.3.2 Test Requirements
4855A.14.4.1.4 Radio Link Monitoring In-sync Test for FR1 SAN PCell
configured with SSB-based RLM RS in DRX mode 4855A.14.4.1.4.1 Test
Purpose and Environment 4855A.14.4.1.4.2 Test Requirements
4860A.14.4.1.5 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell
configured with CSI-RS-based RLM in non-DRX mode 4860A.14.4.1.5.1 Test
Purpose and Environment 4860A.14.4.1.5.2 Test Requirements
4865A.14.4.1.6 Radio Link Monitoring In-sync Test for FR1 SAN PCell
configured with CSI-RS-based RLM in non-DRX mode 4865A.14.4.1.6.1 Test
Purpose and Environment 4865A.14.4.1.6.2 Test Requirements
4869A.14.4.1.7 Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell
configured with CSI-RS-based RLM in DRX mode 4869A.14.4.1.7.1 Test
Purpose and Environment 4869A.14.4.1.7.2 Test Requirements
4874A.14.4.1.8 Radio Link Monitoring In-sync Test for FR1 SAN PCell
configured with CSI-RS-based RLM in DRX mode 4874A.14.4.1.8.1 Test
Purpose and Environment 4874A.14.4.1.8.2 Test Requirements 4879A.14.4.2
Beam Failure Detection and Link recovery procedures for satellite access
4879A.14.4.2.1 Beam Failure Detection and Link Recovery Test for FR1
PCell for satellite access configured with SSB-based BFD and LR in
non-DRX mode 4879A.14.4.2.1.1 Test Purpose and Environment
4879A.14.4.2.1.2 Test Requirements 4885A.14.4.2.2 Beam Failure Detection
and Link Recovery Test for FR1 PCell for satellite access configured
with SSB-based BFD and LR in DRX mode 4885A.14.4.2.2.1 Test Purpose and
Environment 4885A.14.4.2.2.2 Test Requirements 4890A.14.4.2.3 Beam
Failure Detection and Link Recovery Test for FR1 PCell for satellite
access configured with CSI-RS-based BFD and LR in non-DRX mode
4890A.14.4.2.3.1 Test Purpose and Environment 4890A.14.4.2.3.2 Test
Requirements 4895A.14.4.2.4 Beam Failure Detection and Link Recovery
Test for FR1 PCell for satellite access configured with CSI-RS-based BFD
and LR in DRX mode 4896A.14.4.2.4.1 Test Purpose and Environment
4896A.14.4.2.4.2 Test Requirements 4901A.14.4.2.5 Void 4901A.14.4.2.6
Void 4901A.14.4.3 Active BWP switch for satellite access 4901A.14.4.3.1
DCI-based and Timer-based Active BWP Switch 4901A.14.4.3.1.1 NR FR1 DL
active BWP switch with non-DRX in SA 4901A.14.4.3.1.1.1 Test Purpose and
Environment 4901A.14.4.3.1.1.2 Test Requirements 4906A.14.4.3.2
RRC-based Active BWP Switch 4906A.14.4.3.2.1 NR FR1 DL active BWP switch
of Cell with non-DRX in SA 4906A.14.4.3.2.1.1 Test Purpose and
Environment 4906A.14.4.3.2.1.2 Test Requirements 4910A.14.4.4 UE
specific CBW change for satellite access 4910A.14.4.4.1 UE specific CBW
change on PCell in FR1 in non-DRX 4910A.14.4.4.1.1 Test Purpose and
Environment 4910A.14.4.4.1.2 Test Requirements 4914A.14.4.5 Pathloss
reference signal switching delay 4914A.14.4.5.1 MAC-CE based pathloss
reference signal switch delay 4914A.14.4.5.1.1 Test Purpose and
Environment 4914A.14.4.5.1.2 Test Requirements 4917A.14.5 Measurement
procedure 4918A.14.5.1 Intra-frequency Measurements 4918A.14.5.1.1 SA
event triggered reporting tests without gap under non-DRX
4918A.14.5.1.1.1 Test purpose and Environment 4918A.14.5.1.1.2 Test
parameters 4918A.14.5.1.1.3 Test Requirements 4920A.14.5.1.2 SA event
triggered reporting tests without gap under DRX 4921A.14.5.1.2.1 Test
purpose and Environment 4921A.14.5.1.2.2 Test parameters
4921A.14.5.1.2.3 Test Requirements 4922A.14.5.1.3 SA event triggered
reporting tests without gap under non-DRX with SSB index reading
4923A.14.5.1.3.1 Test purpose and Environment 4923A.14.5.1.3.2 Test
parameters 4923A.14.5.1.3.3 Test Requirements 4925A.14.5.1.4 SA event
triggered reporting tests with single measurement gap under non-DRX for
satellite access 4926A.14.5.1.4.1 Test purpose and Environment
4926A.14.5.1.4.2 Test parameters 4926A.14.5.1.4.3 Test Requirements
4928A.14.5.1.5 SA event triggered reporting tests with FNO concurrent
gaps under DRX for satellite access 4929A.14.5.1.5.1 Test purpose and
Environment 4929A.14.5.1.5.2 Test parameters 4929A.15.5.1.5.3 Test
Requirements 4932A.14.5.1.6 SA event triggered reporting tests with PPO
concurrent gaps under non-DRX with SSB index reading for satellite
access 4932A.14.5.1.6.1 Test purpose and Environment 4932A.14.5.1.6.2
Test parameters 4932A.14.5.1.6.3 Test Requirements 4934A.14.5.2
Inter-frequency Measurements 4935A.14.5.2.1 SA event triggered reporting
tests for FR1 without SSB time index detection when DRX is not used with
single gap for satellite access 4935A.14.5.2.1.1 Test Purpose and
Environment 4935A.14.5.2.1.2 Test Requirements 4939A.14.5.2.2 SA event
triggered reporting tests for FR1 without SSB time index detection when
DRX is used with single gap for satellite access 4939A.14.5.2.2.1 Test
Purpose and Environment 4939A.14.5.2.2.2 Test Requirements
4943A.14.5.2.3 SA event triggered reporting tests for FR1 with SSB time
index detection when DRX is not used with single gap for satellite
access 4943A.14.5.2.3.1 Test Purpose and Environment 4943A.14.5.2.3.2
Test Requirements 4947A.14.5.2.4 SA event triggered reporting tests for
FR1 without SSB time index detection when DRX is not used with two gaps
in fully non-overlapped for satellite access 4947A.14.5.2.4.1 Test
Purpose and Environment 4947A.14.5.2.4.2 Test Requirements
4951A.14.5.2.5 void 4951A.14.5.2.5.1 void 4951A.14.5.2.5.2 void
4951A.14.5.2.6 SA event triggered reporting tests for FR1 without SSB
time index detection when DRX is not used with two gaps in partially
partial overalpping for satellite access 4951A.14.5.2.6.1 Test Purpose
and Environment 4951A.14.5.2.6.2 Test Requirements 4955A.14.5.2.7 Event
triggered reporting test without gap under non-DRX 4955A.14.5.2.7.1 Test
purpose and Environment 4955A.14.5.2.7.2 Test parameters
4955A.14.5.2.7.3 Test Requirements 4957A.14.5.2.8 Event triggered
reporting tests without gap under DRX 4958A.14.5.2.8.1 Test purpose and
Environment 4958A.14.5.2.8.2 Test parameters 4958A.14.5.2.8.3 Test
Requirements 4960A.14.5.3 L1-RSRP measurement for beam reporting for
satellite access 4961A.14.5.3.1 SSB based L1-RSRP measurement for
satellite access when DRX is not used 4961A.14.5.3.1.1 Test Purpose and
Environment 4961A.14.5.3.1.2 Test parameters 4961A.14.5.3.1.3 Test
Requirements 4964A.14.5.3.2 SSB based L1-RSRP measurement for satellite
access when DRX is used 4964A.14.5.3.2.1 Test Purpose and Environment
4964A.14.5.3.2.2 Test parameters 4964A.14.5.3.2.3 Test Requirements
4968A.14.5.3.3 CSI-RS based L1-RSRP measurement for satellite access
when DRX is not used 4968A.14.5.3.3.1 Test Purpose and Environment
4968A.14.5.3.3.2 Test parameters 4968A.14.5.3.3.3 Test Requirements
4970A.14.5.3.4 CSI-RS based L1-RSRP measurement for satellite access
when DRX is used 4970A.14.5.3.4.1 Test Purpose and Environment
4970A.14.5.3.4.2 Test parameters 4970A.14.5.3.4.3 Test Requirements
4974A.14.6 Measurement Performance requirements 4974A.14.6.1 SS-RSRP for
SAN 4974A.14.6.1.1 SA: intra-frequency case measurement accuracy with
FR1 serving cell and FR1 target cell 4974A.14.6.1.1.1 Test Purpose and
Environment 4974A.14.6.1.1.2 Test parameters 4975A.14.6.1.1.3 Test
Requirements 4978A.14.6.1.2 SA inter-frequency case measurement accuracy
with FR1 serving cell and FR1 target cell 4978A.14.6.1.2.1 Test Purpose
and Environment 4978A.14.6.1.2.2 Test parameters 4978A.14.6.1.2.3 Test
Requirements 4981A.14.6.2 SS-RSRQ 4981A.14.6.2.1 SA: Intra-frequency
measurement accuracy with FR1 serving cell and FR1 target cell for
satellite access 4981A.14.6.2.1.1 Test Purpose and Environment
4981A.14.6.2.1.2 Test Parameters 4981A.14.6.2.1.3 Test Requirements
4984A.14.6.2.2 SA Inter-frequency measurement accuracy with FR1 serving
cell and FR1 target cell for satellite access 4984A.14.6.2.2.1 Test
Purpose and Environment 4984A.14.6.2.2.2 Test Parameters
4984A.14.6.2.2.3 Test Requirements 4987A.14.6.3 SS-SINR 4987A.14.6.3.1
SA intra-frequency measurement accuracy with FR1 serving cell and FR1
target cell 4987A.14.6.3.1.1 Test Purpose and Environment
4987A.14.6.3.1.2 Test Parameters 4987A.14.6.3.1.3 Test Requirements
4990A.14.6.3.2 SA Inter-frequency measurement accuracy with FR1 serving
cell and FR1 target cell 4990A.14.6.3.2.1 Test Purpose and Environment
4990A.14.6.3.2.2 Test Parameters 4990A.14.6.3.2.3 Test Requirements
4993A.14.6.4 L1-RSRP measurement for beam reporting 4993A.14.6.4.1 SSB
based L1-RSRP measurement 4993A.14.6.4.1.1 Test Purpose and Environment
4993A.14.6.4.1.2 Test parameters 4993A.14.6.4.1.3 Test Requirements
4996A.14.6.4.2 CSI-RS based L1-RSRP measurement on resource set with
repetition off 4996A.14.6.4.2.1 Test Purpose and Environment
4996A.14.6.4.2.2 Test parameters 4996A.14.6.4.2.3 Test Requirements
4999A.15 NR standalone tests with one or more NR cells in FR2-2
5012A.15.1 SA: RRC\_IDLE state mobility 5012A.15.1.1 Cell re-selection
to NR 5012A.15.1.1.1 Cell reselection to FR2-2 intra-frequency NR case
5012A.15.1.1.1.1 Test Purpose and Environment 5012A.15.1.1.1.2 Test
Parameters 5012A.15.1.1.1.3 Test Requirements 5016A.15.1.2 Cell
reselection to FR2-2 inter-frequency NR case 5016A.15.1.2.1 Test Purpose
and Environment 5016A.15.1.2.2 Test Parameters 5016A.15.1.2.3 Test
Requirements 5020A.15.1.3 Cell reselection to FR2-2 intra-frequency NR
case for UE fulfilling low mobility relaxed measurement criterion
5020A.15.1.3.1 Test Purpose and Environment 5020A.15.1.3.2 Test
Parameters 5020A.15.1.3.3 Test Requirements 5023A.15.1.4 Cell
reselection to FR2-2 intra-frequency NR case for UE fulfilling
not-at-cell edge relaxed measurement criterion 5023A.15.1.4.1 Test
Purpose and Environment 5023A.15.1.4.2 Test Parameters 5023A.15.1.4.3
Test Requirements 5026A.15.1.5 Cell reselection to FR2-2 inter-frequency
NR case for UE fulfilling low mobility relaxed measurement criterion
5026A.15.1.5.1 Test Purpose and Environment 5026A.15.1.5.2 Test
Parameters 5026A.15.1.5.3 Test Requirements 5030A.15.1.6 Cell
reselection to FR2-2 inter-frequency NR case for UE fulfilling
not-at-cell edge relaxed measurement criterion 5030A.15.1.6.1 Test
Purpose and Environment 5030A.15.1.6.2 Test Parameters 5030A.15.1.6.3
Test Requirements 5033A.15.2 Signaling characteristics 5033A.15.2.1
SCell Activation and Deactivation Delay 5033A.15.2.1.1 SCell Activation
and deactivation for SCell in FR2-2 intra-band in non-DRX
5033A.15.2.1.1.1 Test Purpose and Environment 5033A.15.2.1.1.2 Test
Requirements 5036A.15.2.1.2 SCell Activation and deactivation for
FR1+FR2-2 inter-band with target SCell in FR2-2 5036A.15.2.1.2.1 Test
Purpose and Environment 5036A.15.2.1.2.2 Test Requirements
5041A.15.2.1.3 SCell Activation and deactivation for SCell in FR2-2
inter-band in non-DRX 5042A.15.2.1.3.1 Test Purpose and Environment
5042A.15.2.1.3.2 Test Requirements 5045A.15.2.1.4 Direct SCell
activation at SCell addition of known SCell in FR2-2 5046A.15.2.1.4.1
Test Purpose and Environment 5046A.15.2.1.4.2 Test Requirements
5049A.15.2.1.5 Direct SCell activation at handover with known SCell in
FR2-2 5050A.15.2.1.5.1 Test Purpose and Environment 5050A.15.2.1.5.2
Test Requirements 5054A.15.3 RRC\_CONNECTED state mobility 5055A.15.3.1
Handover 5055A.15.3.1.1 Intra-frequency handover from FR2-2 carrier with
CCA to FR2-2 carrier with CCA; unknown target cell 5055A.15.3.1.1.1 Test
Purpose and Environment 5055A.15.3.1.1.2 Test Parameters
5055A.15.3.1.1.3 Test Requirements 5059A.15.3.1.2 Inter-frequency
handover from FR1 to FR2-2 carrier with CCA; unknown target cell
5059A.15.3.1.2.1 Test Purpose and Environment 5059A.15.3.1.2.2 Test
Parameters 5059A.15.3.1.2.3 Test Requirements 5063A.15.4 Measurement
procedure 5064A.15.4.1 Intra-frequency Measurements 5064A.15.4.1.1 SA
event triggered reporting test without gap under non-DRX for FR2-2 with
CCA 5064A.15.4.1.1.1 Test purpose and Environment 5064A.15.4.1.1.2 Test
Requirements 5066A.15.4.2 Inter-frequency Measurements 5067A.15.4.2.1 SA
event triggered reporting tests for FR2-2 with CCA without SSB time
index detection when DRX is not used (PCell in FR2-2) 5067A.15.4.2.1.1
Test Purpose and Environment 5067A.15.4.2.1.2 Test Requirements 5070A.16
NR standalone tests with all NR cells in FR1 for RedCap 5071A.16.1 SA:
RRC\_IDLE state mobility for RedCap 5071A.16.1.1 Cell re-selection to NR
5071A.16.1.1.1 Cell reselection to FR1 intra-frequency NR case for 1 Rx
UE 5071A.16.1.1.1.1 Test Purpose and Environment 5071A.16.1.1.1.2 Test
Parameters 5071A.16.1.1.1.3 Test Requirements 5075A.16.1.1.2 Cell
reselection to FR1 intra-frequency NR case for 2 Rx UE 5075A.16.1.1.2.1
Test Purpose and Environment 5075A.16.1.1.2.2 Test Parameters
5075A.16.1.1.2.3 Test Requirements 5079A.16.1.1.3 Cell reselection to
FR1 inter-frequency NR case for 1 Rx UE 5079A.16.1.1.3.1 Test Purpose
and Environment 5079A.16.1.1.3.2 Test Parameters 5079A.16.1.1.3.3 Test
Requirements 5084A.16.1.1.4 Cell reselection to FR1 inter-frequency NR
case for 2 Rx UE 5084A.16.1.1.4.1 Test Purpose and Environment
5084A.16.1.1.4.2 Test Parameters 5084A.16.1.1.4.3 Test Requirements
5089A.16.1.1.5 Cell reselection to FR1 intra-frequency NR case for UE
fulfilling stationary relaxed measurement criterion for 1 Rx UE
5089A.16.1.1.5.1 Test Purpose and Environment 5089A.16.1.1.5.2 Test
Parameters 5089A.16.1.1.5.3 Test Requirements 5094A.16.1.1.6 Cell
reselection to FR1 intra-frequency NR case for UE fulfilling stationary
relaxed measurement criterion for 2 Rx UE 5094A.16.1.1.6.1 Test Purpose
and Environment 5094A.16.1.1.6.2 Test Parameters 5094A.16.1.1.6.3 Test
Requirements 5099A.16.1.1.7 Cell reselection to FR1 inter-frequency NR
case for UE fulfilling stationary relaxed measurement criterion for 1 Rx
UE 5099A.16.1.1.7.1 Test Purpose and Environment 5099A.16.1.1.7.2 Test
Parameters 5099A.16.1.1.7.3 Test Requirements 5104A.16.1.1.8 Cell
reselection to FR1 inter-frequency NR case for UE fulfilling stationary
relaxed measurement criterion for 2 Rx UE 5105A.16.1.1.8.1 Test Purpose
and Environment 5105A.16.1.1.8.2 Test Parameters 5105A.16.1.1.8.3 Test
Requirements 5109A.16.1.2 Inter-RAT E-UTRAN cell re-selection for RedCap
5110A.16.1.2.1 Cell reselection to higher priority E-UTRAN for 1RX
5110A.16.1.2.1.1 Test Purpose and Environment 5110A.16.1.2.1.2 Test
Parameters 5110A.16.1.2.1.3 Test Requirements 5113A.16.1.2.2 Cell
reselection to higher priority E-UTRAN for 2RX 5114A.16.1.2.2.1 Test
Purpose and Environment 5114A.16.1.2.2.2 Test Parameters
5114A.16.1.2.2.3 Test Requirements 5117A.16.1.2.3.1 Test Purpose and
Environment 5118A. 16.1.2.3.2 Test Parameters 5118A.16.1.2.3.3 Test
Requirements 5121A.16.1.2.4.1 Test Purpose and Environment
5122A.16.1.2.4.2 Test Parameters 5122A.16.1.3.1.3 Test Requirements
5125A.16.1.2.5 Cell reselection to lower priority E-UTRAN for UE
fulfilling stationary relaxed measurement criterion for 1 Rx UE
5126A.16.1.2.5.1 Test Purpose and Environment 5126A.16.1.2.5.2 Test
Parameters 5126A.16.1.2.5.3 Test Requirements 5129A.16.1.2.6 Cell
reselection to lower priority E-UTRAN for UE fulfilling stationary
relaxed measurement criterion for 2 Rx UE 5130A.16.1.2.6.1 Test Purpose
and Environment 5130A.16.1.2.6.2 Test Parameters 5130A.16.1.2.6.3 Test
Requirements 5133A.16.2 SA: RRC\_INACTIVE state mobility for RedCap
5134A.16.2.1 Configured Grant based Small Data Transmissions (CG-SDT)
for RedCap 5134A.16.2.1.1 NR UE CG-SDT Test in FR1 for 1Rx RedCap UE
5134A.16.2.1.1.1 Test purpose and Environment 5134A.16.2.1.1.2 Test
Parameters 5135A.16.2.1.1.3 Test requirements 5139A.16.2.1.2 NR UE
CG-SDT Test in FR1 for 2Rx RedCap UE 5139A.16.2.1.2.1 Test purpose and
Environment 5139A.16.2.1.2.2 Test Parameters 5141A.16.2.1.2.3 Test
requirements 5144A.16.3 RRC\_CONNECTED state mobility for RedCap
5144A.16.3.1 Handover 5144A.16.3.1.1 Intra-frequency handover from FR1
to FR1; known target cell for 1 Rx UE 5144A.16.3.1.1.1 Test Purpose and
Environment 5144A.16.3.1.1.2 Test Parameters 5145A.16.3.1.1.3 Test
Requirements 5148A.16.3.1.2 Intra-frequency handover from FR1 to FR1;
known target cell for 2 Rx UE 5148A.16.3.1.2.1 Test Purpose and
Environment 5148A.16.3.1.2.2 Test Parameters 5148A.16.3.1.2.3 Test
Requirements 5152A.16.3.1.3 Intra-frequency handover from FR1 to FR1;
unknown target cell for 1 Rx UE 5152A.16.3.1.3.1 Test Purpose and
Environment 5152A.16.3.1.3.2 Test Parameters 5152A.16.3.1.3.3 Test
Requirements 5156A.16.3.1.4 Intra-frequency handover from FR1 to FR1;
unknown target cell for 2 Rx UE 5156A.16.3.1.4.1 Test Purpose and
Environment 5156A.16.3.1.4.2 Test Parameters 5156A.16.3.1.5
Inter-frequency handover from FR1 to FR1; unknown target cell for 1 Rx
UE 5160A.16.3.1.5.1 Test Purpose and Environment 5160A.16.3.1.5.2 Test
Parameters 5160A.16.3.1.5.3 Test Requirements 5164A.16.3.1.6
Inter-frequency handover from FR1 to FR1; unknown target cell for 2 Rx
UE 5164A.16.3.1.6.1 Test Purpose and Environment 5164A.16.3.1.6.2 Test
Parameters 5164A.16.3.1.6.3 Test Requirements 5168A.16.3.1.7 SA NR -
E-UTRAN handover for 1Rx UE 5168A.16.3.1.7.1 Test Purpose and
Environment 5168A.16.3.1.7.2 Test Requirements 5174A.16.3.1.8 SA NR -
E-UTRAN handover for 2Rx UE 5174A.16.3.1.8.1 Test Purpose and
Environment 5174A.16.3.1.8.2 Test Requirements 5180A.16.3.1.9 SA NR -
E-UTRAN handover with unknown target cell for 1 Rx UE 5180A.16.3.1.9.1
Test Purpose and Environment 5180A.16.3.1.9.2 Test Requirements
5187A.16.3.1.10 SA NR - E-UTRAN handover with unknown target cell for 2
Rx UE 5187A.16.3.1.10.1 Test Purpose and Environment 5187A.16.3.1.10.2
Test Requirements 5193A.16.3.2 RRC Connection Mobility Control
5193A.16.3.2.1 SA: RRC Re-establishment 5193A.16.3.2.1.1 Intra-frequency
RRC Re-establishment in FR1 for 1 Rx UE 5193A.16.3.2.1.2 Intra-frequency
RRC Re-establishment in FR1 for 2 Rx UE 5197A.16.3.2.1.3 Inter-frequency
RRC Re-establishment in FR1 for 1 Rx UE 5201A.16.3.2.1.4 Inter-frequency
RRC Re-establishment in FR1 for 2 Rx UE 5206A.16.3.2.1.5 Intra-frequency
RRC Re-establishment in FR1 for 1 Rx UE without serving cell timing
5211A.16.3.2.1.6 Intra-frequency RRC Re-establishment in FR1 for 2 Rx UE
without serving cell timing 5215A.16.3.2.2 Random Access
5219A.16.3.2.2.1 4-step RA type contention based random access test in
FR1 for NR standalone for 1 Rx UE 5219A.16.3.2.2.2 4-step RA type
contention based random access test in FR1 for NR standalone for 2 Rx UE
5225A.16.3.2.2.3 4-step RA type non-contention based random access test
in FR1 for NR standalone for 1 Rx UE 5230A.16.3.2.2.5 2-step RA type
contention based random access test in FR1 for NR standalone for 1 Rx UE
5240A.16.3.2.2.6 2-step RA type contention based random access test in
FR1 for NR standalone for 2 Rx UE 5244A.16.3.2.2.7 2-step RA type
non-contention based test in FR1 for NR standalone for 1 RX UE
5248A.16.3.2.2.8 2-step RA type non-contention based test in FR1 for NR
standalone for 2 RX UE 5252A.16.3.2.3 SA: RRC Connection Release with
Redirection 5256A.16.3.2.3.1 Redirection from NR in FR1 to NR in FR1 for
1 Rx UE 5256A.16.3.2.3.2 Redirection from NR in FR1 to NR in FR1 for 2
Rx UE 5260A.16.3.2.3.3 Redirection from NR in FR1 to E-UTRAN for 1 Rx UE
5264A.16.3.2.3.4 Redirection from NR in FR1 to E-UTRAN for 2 Rx UE
5271A.16.4 Timing for RedCap 5278A.16.4.1 UE transmit timing
5278A.16.4.1.1 NR UE Transmit Timing Test for FR1 for 1Rx RedCap UE
5278A.16.4.1.1.1 Test Purpose and environment 5278A.16.4.1.1.2 Test
requirements 5283A.16.4.1.2 NR UE Transmit Timing Test for FR1 for 2Rx
RedCap UE 5283A.16.4.1.2.1 Test Purpose and environment 5283A.16.4.1.2.2
Test requirements 5286A.16.4.2 UE timer accuracy 5286A.16.4.3 Timing
advance 5286A.16.4.3.1 SA FR1 timing advance adjustment accuracy for 1
Rx UE 5286A.16.4.3.1.1 Test Purpose and Environment 5286A.16.4.3.1.2
Test Parameters 5286A.16.4.3.1.3 Test Requirements 5290A.16.4.3.2 SA FR1
timing advance adjustment accuracy for 2 Rx UE 5290A.16.4.3.2.1 Test
Purpose and Environment 5290A.16.4.3.2.2 Test Parameters
5291A.16.4.3.2.3 Test Requirements 5294A.16.5 Signalling characteristics
for RedCap 5295A.16.5.1 Radio link Monitoring 5295A.16.5.1.1 Radio Link
Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM
RS in non-DRX mode for 1 Rx UE 5295A.16.5.1.1.1 Test Purpose and
Environment 5295A.16.5.1.1.2 Test Requirements 5300A.16.5.1.2 Radio Link
Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM
RS in non-DRX mode for 2 Rx UE 5300A.16.5.1.2.1 Test Purpose and
Environment 5300A.16.5.1.2.2 Test Requirements 5306A.16.5.1.3 Radio Link
Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS
in non-DRX mode for 1 Rx UE 5306A.16.5.1.3.1 Test Purpose and
Environment 5306A.16.5.1.3.2 Test Requirements 5312A.16.5.1.4 Radio Link
Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS
in non-DRX mode for 2 Rx UE 5312A.16.5.1.4.1 Test Purpose and
Environment 5312A.16.5.1.4.2 Test Requirements 5318A.16.5.1.5 Radio Link
Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM
RS in DRX mode for 1 Rx UE 5318A.16.5.1.5.1 Test Purpose and Environment
5318A.16.5.1.5.2 Test Requirements 5324A.16.5.1.6 Radio Link Monitoring
Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX
mode for 2 Rx UE 5324A.16.5.1.6.1 Test Purpose and Environment
5324A.16.5.1.6.2 Test Requirements 5329A.16.5.1.7 Radio Link Monitoring
In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode
for 1 Rx UE 5329A.16.5.1.7.1 Test Purpose and Environment
5329A.16.5.1.7.2 Test Requirements 5334A.16.5.1.8 Radio Link Monitoring
In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode
for 2 Rx UE 5334A.16.5.1.8.1 Test Purpose and Environment
5334A.16.5.1.8.2 Test Requirements 5340A.16.5.1.9 Radio Link Monitoring
Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in
non-DRX mode for 1 Rx UE 5340A.16.5.1.9.1 Test Purpose and Environment
5340A.16.5.1.9.2 Test Requirements 5346A.16.5.1.10 Radio Link Monitoring
Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in
non-DRX mode for 2 Rx UE 5346A.16.5.1.10.1 Test Purpose and Environment
5346A.16.5.1.10.2 Test Requirements 5352A.16.5.1.11 Radio Link
Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM
in non-DRX mode for 1 Rx UE 5352A.16.5.1.11.1 Test Purpose and
Environment 5352A.16.5.1.11.2 Test Requirements 5358A.16.5.1.12 Radio
Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based
RLM in non-DRX mode for 2 Rx UE 5358A.16.5.1.12.1 Test Purpose and
Environment 5358A.16.5.1.12.2 Test Requirements 5364A.16.5.1.13 Radio
Link Monitoring Out-of-sync Test for FR1 PCell configured with
CSI-RS-based RLM in DRX mode for 1 Rx UE 5364A.16.5.1.13.1 Test Purpose
and Environment 5364A.16.5.1.13.2 Test Requirements 5369A.16.5.1.14
Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with
CSI-RS-based RLM in DRX mode for 2 Rx UE 5369A.16.5.1.14.1 Test Purpose
and Environment 5369A.16.5.1.14.2 Test Requirements 5375A.16.5.1.15
Radio Link Monitoring In-sync Test for FR1 PCell configured with
CSI-RS-based RLM in DRX mode for 1 Rx UE 5375A.16.5.1.15.1 Test Purpose
and Environment 5375A.16.5.1.15.2 Test Requirements 5381A.16.5.1.16
Radio Link Monitoring In-sync Test for FR1 PCell configured with
CSI-RS-based RLM in DRX mode for 2 Rx UE 5381A.16.5.1.16.1 Test Purpose
and Environment 5381A.16.5.1.16.2 Test Requirements 5387A.16.5.2 Beam
Failure Detection and Link recovery procedures 5387A.16.5.2.1 Beam
Failure Detection and Link Recovery Test for FR1 PCell configured with
SSB-based BFD and LR in non-DRX mode for 1 Rx UE 5387A.16.5.2.1.1 Test
Purpose and Environment 5387A.16.5.2.1.2 Test Requirements
5393A.16.5.2.2 Beam Failure Detection and Link Recovery Test for FR1
PCell configured with SSB-based BFD and LR in non-DRX mode for 2 Rx UE
5393A.16.5.2.2.1 Test Purpose and Environment 5393A.16.5.2.2.2 Test
Requirements 5399A.16.5.2.3 Beam Failure Detection and Link Recovery
Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode for
1 Rx UE 5399A.16.5.2.3.1 Test Purpose and Environment 5399A.16.5.2.3.2
Test Requirements 5406A.16.5.2.4 Beam Failure Detection and Link
Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX
mode for 2 Rx UE 5406A.16.5.2.4.1 Test Purpose and Environment
5406A.16.5.2.4.2 Test Requirements 5412A.16.5.2.5 Beam Failure Detection
and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD
and LR in non-DRX mode for 1 Rx UE 5412A.16.5.2.5.1 Test Purpose and
Environment 5412A.16.5.2.5.2 Test Requirements 5418A.16.5.2.6 Beam
Failure Detection and Link Recovery Test for FR1 PCell configured with
CSI-RS-based BFD and LR in non-DRX mode for 2 Rx UE 5418A.16.5.2.6.1
Test Purpose and Environment 5418A.16.5.2.6.2 Test Requirements
5424A.16.5.2.7 Beam Failure Detection and Link Recovery Test for FR1
PCell configured with CSI-RS-based BFD and LR in DRX mode for 1 Rx UE
5424A.16.5.2.7.1 Test Purpose and Environment 5424A.16.5.2.7.2 Test
Requirements 5430A.16.5.2.8 Beam Failure Detection and Link Recovery
Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode
for 2 Rx UE 5430A.16.5.2.8.1 Test Purpose and Environment
5430A.16.5.2.8.2 Test Requirements 5436A.16.5.3 Active BWP switch
5436A.16.5.3.1 DCI-based and Timer-based Active BWP Switch
5436A.16.5.3.1.1 NR FR1 DL active BWP switch with non-DRX in SA for 1 Rx
UE 5436A.16.5.3.1.1.1 Test Purpose and Environment 5436A.16.5.3.1.2.1
Test Requirements 5441A.16.5.3.1.2 NR FR1 DL active BWP switch with
non-DRX in SA for 2 Rx UE 5441A.16.5.3.1.2.1 Test Purpose and
Environment 5441A.1**6.5.3.1.2.**2 Test Requirements 5446A.16.5.3.2
RRC-based Active BWP Switch 5446A.16.5.3.2.1 NR FR1 DL active BWP switch
of Cell with non-DRX in SA for 1 Rx UE 5446A.16.5.3.2.1.1 Test Purpose
and Environment 5446A.16.5.3.2.1.2 Test Requirements 5450A.16.5.3.2.2 NR
FR1 DL active BWP switch of Cell with non-DRX in SA for 2 Rx UE
5450A.16.5.3.2.2.1 Test Purpose and Environment 5450A.16.5.3.2.2.2 Test
Requirements 5454A.16.5.4 UE specific CBW change 5454A.16.5.4.1 UE
specific CBW change on PCell in FR1 in non-DRX for 1 Rx UE
5454A.16.5.4.1.1 Test Purpose and Environment 5454A.16.5.4.1.2 Test
Requirements 5458A.16.5.4.2 UE specific CBW change on PCell in FR1 in
non-DRX for 2 Rx UE 5458A.16.5.4.2.1 Test Purpose and Environment
5458A.16.5.4.2.2 Test Requirements 5462A.16.6 Measurement procedure for
RedCap 5462A.16.6.1 Intra-frequency Measurements 5462A.16.6.1.1 SA event
triggered reporting tests without gap under non-DRX for 1 Rx UE
5462A.16.6.1.1.1 Test purpose and Environment 5462A.16.6.1.1.2 Test
parameters 5462A.16.6.1.1.3 Test Requirements 5466A.16.6.1.2 SA event
triggered reporting tests without gap under non-DRX for 2 Rx UE
5466A.16.6.1.2.1 Test purpose and Environment 5466A.16.6.1.2.2 Test
parameters 5466A.16.6.1.2.3 Test Requirements 5470A.16.6.1.3 SA event
triggered reporting tests without gap under DRX for 1 Rx UE
5470A.16.6.1.3.1 Test purpose and Environment 5470A.16.6.1.3.2 Test
parameters 5470A.16.6.1.3.3 Test Requirements 5474A.16.6.1.4 SA event
triggered reporting tests without gap under DRX for 2 Rx UE
5474A.16.6.1.4.1 Test purpose and Environment 5474A.16.6.1.4.2 Test
parameters 5474A.16.6.1.4.3 Test Requirements 5478A.16.6.1.5 SA event
triggered reporting tests with per-UE gaps under non-DRX for 1 Rx UE
5478A.16.6.1.5.1 Test purpose and Environment 5478A.16.6.1.5.2 Test
parameters 5478A.16.6.1.5.3 Test Requirements 5482A.16.6.1.6 SA event
triggered reporting tests with per-UE gaps under non-DRX for 2 Rx UE
5482A.16.6.1.6.1 Test purpose and Environment 5482A.16.6.1.6.2 Test
parameters 5482A.16.6.1.6.3 Test Requirements 5486A.16.6.1.7 SA event
triggered reporting tests with per-UE gaps under DRX for 1 Rx UE
5486A.16.6.1.7.1 Test purpose and Environment 5486A.16.6.1.7.2 Test
parameters 5486A.16.6.1.7.3 Test Requirements 5490A.16.6.1.8 SA event
triggered reporting tests with per-UE gaps under DRX for 2 Rx UE
5490A.16.6.1.8.1 Test purpose and Environment 5490A.16.6.1.8.2 Test
parameters 5490A.16.6.1.8.3 Test Requirements 5494A.16.6.1.9 SA event
triggered reporting tests without gap under non-DRX with SSB index
reading for 1 Rx UE 5494A.16.6.1.9.1 Test purpose and Environment
5494A.16.6.1.9.2 Test parameters 5494A.16.6.1.9.3 Test Requirements
5496A.16.6.1.10 SA event triggered reporting tests without gap under
non-DRX with SSB index reading for 2 Rx UE 5497A.16.6.1.10.1 Test
purpose and Environment 5497A.16.6.1.10.2 Test parameters
5497A.16.6.1.10.3 Test Requirements 5498A.16.6.1.11 SA event triggered
reporting tests with per-UE gaps under non-DRX with SSB index reading
for 1 Rx UE 5499A.16.6.1.11.1 Test purpose and Environment
5499A.16.6.1.11.2 Test parameters 5499A.16.6.1.11.3 Test Requirements
5501A.16.6.1.12 SA event triggered reporting tests with per-UE gaps
under non-DRX with SSB index reading for 2 Rx UE 5502A.16.6.1.12.1 Test
purpose and Environment 5502A.16.6.1.12.2 Test parameters
5502A.16.6.1.12.3 Test Requirements 5504A.16.6.2 Inter-frequency
Measurements 5505A.16.6.2.1 SA event triggered reporting tests for FR1
without SSB time index detection when DRX is used for 1 Rx UE
5505A.16.6.2.1.1 Test Purpose and Environment 5505A.16.6.2.1.2 Test
Requirements 5510A.16.6.2.2 SA event triggered reporting tests for FR1
without SSB time index detection when DRX is used for 2 Rx UE
5510A.16.6.2.2.1 Test Purpose and Environment 5510A.16.6.2.2.2 Test
Requirements 5515A.16.6.2.3 SA event triggered reporting tests for FR1
without SSB time index detection when DRX is not used for 1 Rx UE
5515A.16.6.2.3.1 Test Purpose and Environment 5515A.16.6.2.3.2 Test
Requirements 5518A.16.6.2.4 SA event triggered reporting tests for FR1
without SSB time index detection when DRX is not used for 2 Rx UE
5519A.16.6.2.4.1 Test Purpose and Environment 5519A.16.6.2.4.2 Test
Requirements 5522A.16.6.2.5 SA event triggered reporting tests for FR1
with SSB time index detection when DRX is not used for 1 Rx UE
5523A.16.6.2.5.1 Test Purpose and Environment 5523A.16.6.2.5.2 Test
Requirements 5526A.16.6.2.6 SA event triggered reporting tests for FR1
with SSB time index detection when DRX is not used for 2 Rx UE
5527A.16.6.2.6.1 Test Purpose and Environment 5527A.16.6.2.6.2 Test
Requirements 5530A.16.6.2.7 SA event triggered reporting tests for FR1
with SSB time index detection when DRX is used for 1 Rx UE
5531A.16.6.2.7.1 Test Purpose and Environment 5531A.16.6.2.7.2 Test
Requirements 5535A.16.6.2.8 SA event triggered reporting tests for FR1
with SSB time index detection when DRX is used for 2 Rx UE
5536A.16.6.2.8.1 Test Purpose and Environment 5536A.16.6.2.8.2 Test
Requirements 5539A.16.6.2.9 SA event triggered reporting tests with
additional mandatory gap pattern for 1 Rx UE 5540A.16.6.2.9.1 Test
Purpose and Environment 5540A.16.6.2.9.2 Test Requirements
5543A.16.6.2.10 SA event triggered reporting tests with additional
mandatory gap pattern for 2 Rx UE 5543A.16.6.2.10.1 Test Purpose and
Environment 5543A.16.6.2.10.2 Test Requirements 5546A.16.6.2.11 SA event
triggered reporting tests for FR1 when DRX is used for 1 Rx UE
5546A.16.6.2.11.1 Test Purpose and Environment 5546A.16.6.2.11.2 Test
Requirements 5549A.16.6.2.12 SA event triggered reporting tests for FR1
when DRX is used for 2 Rx UE 5549A.16.6.2.12.1 Test Purpose and
Environment 5549A.16.6.2.12.2 Test Requirements 5553A.16.6.3 Inter-RAT
Measurements 5554A.16.6.3.1 SA NR - E-UTRAN event-triggered reporting in
non-DRX in FR1 for 1 Rx UE 5554A.16.6.3.1.1 Test purpose and Environment
5554A.16.6.3.1.2 Test Requirements 5559A.16.6.3.2 SA NR - E-UTRAN
event-triggered reporting in non-DRX in FR1 for 2 Rx UE 5559A.16.6.3.2.1
Test purpose and Environment 5559A.16.6.3.2.2 Test Requirements
5564A.16.6.3.3 SA NR - E-UTRAN event-triggered reporting in DRX in FR1
for 1 Rx UE 5564A.16.6.3.3.1 Test purpose and Environment
5564A.16.6.3.3.2 Test Requirements 5569A.16.6.3.4 SA NR - E-UTRAN
event-triggered reporting in DRX in FR1 for 2 Rx UE 5569A.16.6.3.4.1
Test purpose and Environment 5569A.16.6.3.4.2 Test Requirements
5574A.16.6.4 L1-RSRP measurement for beam reporting 5574A.16.6.4.1 SSB
based L1-RSRP measurement when DRX is not used for 1 Rx UE
5574A.16.6.4.1.1 Test Purpose and Environment 5574A.16.6.4.1.2 Test
parameters 5574A.16.6.4.1.3 Test Requirements 5578A.16.6.4.2 SSB based
L1-RSRP measurement when DRX is not used for 2 Rx UE 5578A.16.6.4.2.1
Test Purpose and Environment 5578A.16.6.4.2.2 Test parameters
5579A.16.6.4.2.3 Test Requirements 5582A.16.6.4.3 SSB based L1-RSRP
measurement when DRX is used for 1 Rx UE 5582A.16.6.4.3.1 Test Purpose
and Environment 5582A.16.6.4.3.2 Test parameters 5583A.16.6.4.3.3 Test
Requirements 5586A.16.6.4.4 SSB based L1-RSRP measurement when DRX is
used for 2 Rx UE 5586A.16.6.4.4.1 Test Purpose and Environment
5586A.16.6.4.4.2 Test parameters 5587A.16.6.4.4.3 Test Requirements
5590A.16.6.4.5 CSI-RS based L1-RSRP measurement when DRX is not used for
1 Rx UE 5590A.16.6.4.5.1 Test Purpose and Environment 5590A.16.6.4.5.2
Test parameters 5591A.16.6.4.5.3 Test Requirements 5594A.16.6.4.6 CSI-RS
based L1-RSRP measurement when DRX is not used for 2 Rx UE
5594A.16.6.4.6.1 Test Purpose and Environment 5594A.16.6.4.6.2 Test
parameters 5595A.16.6.4.6.3 Test Requirements 5598A.16.6.4.7 CSI-RS
based L1-RSRP measurement when DRX is used for 1 Rx UE 5598A.16.6.4.7.1
Test Purpose and Environment 5598A.16.6.4.7.2 Test parameters
5599A.16.6.4.7.3 Test Requirements 5602A.16.6.4.8 CSI-RS based L1-RSRP
measurement when DRX is used for 2 Rx UE 5602A.16.6.4.8.1 Test Purpose
and Environment 5602A.16.6.4.8.2 Test parameters 5603A.16.6.4.8.3 Test
Requirements 5606A.16.6.5 NR measurements with autonomous gaps
5606A.16.6.5.1 SA intra-frequency CGI identification of NR neighbor cell
in FR1 for 1 Rx UE 5606A.16.6.5.1.1 Test Purpose and Environment
5606A.16.6.5.1.2 Test Parameters 5606A.16.6.5.1.3 Test Requirements
5609A.16.6.5.2 SA intra-frequency CGI identification of NR neighbor cell
in FR1 for 2 Rx UE 5609A.16.6.5.2.1 Test Purpose and Environment
5609A.16.6.5.2.2 Test Parameters 5609A.16.6.5.2.3 Test Requirements
5612A.16.6.5.3 Identification of a new CGI of inter-RAT E-UTRA cell
using autonomous gaps in NR SA for 1 Rx UE 5612A.16.6.5.3.1 Test Purpose
and Environment 5612A.16.6.5.3.2 Test Requirements 5617A.16.6.5.4
Identification of a new CGI of inter-RAT E-UTRA cell using autonomous
gaps in NR SA for 2 Rx UE 5618A.16.6.5.4.1 Test Purpose and Environment
5618A.16.6.5.4.2 Test Requirements 5623A.16.7 Measurement Performance
requirements for RedCap 5624A.16.7.1 SS-RSRP 5624A.16.7.1.1 SA:
intra-frequency case measurement accuracy with FR1 serving cell and FR1
target cell for 1 Rx UE 5624A.16.7.1.1.1 Test Purpose and Environment
5624A.16.7.1.1.2 Test parameters 5624A.16.7.1.1.3 Test Requirements
5629A.16.7.1.2 SA: intra-frequency case measurement accuracy with FR1
serving cell and FR1 target cell for 2Rx UE 5629A.16.7.1.2.1 Test
Purpose and Environment 5629A.16.7.1.2.2 Test parameters
5629A.16.7.1.2.3 Test Requirements 5634A.16.7.1.3 SA inter-frequency
case measurement accuracy with FR1 serving cell and FR1 target cell for
1 Rx UE 5634A.16.7.1.3.1 Test Purpose and Environment 5634A.16.7.1.3.2
Test parameters 5634A.16.7.1.3.3 Test Requirements 5638A.16.7.1.4 SA
inter-frequency case measurement accuracy with FR1 serving cell and FR1
target cell for 2 Rx UE 5638A.16.7.1.4.1 Test Purpose and Environment
5638A.16.7.1.4.2 Test parameters 5639A.16.7.1.4.3 Test Requirements
5643A.16.7.2 SS-RSRQ 5643A.16.7.2.1 SA: Intra-frequency measurement
accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE
5643A.16.7.2.1.1 Test Purpose and Environment 5643A.16.7.2.1.2 Test
Parameters 5644A.16.7.2.1.3 Test Requirements 5648A.16.7.2.2 SA:
Intra-frequency measurement accuracy with FR1 serving cell and FR1
target cell for 2 Rx UE 5648A.16.7.2.2.1 Test Purpose and Environment
5648A.16.7.2.2.2 Test Parameters 5648A.16.7.2.2.3 Test Requirements
5652A.16.7.2.3 SA Inter-frequency measurement accuracy with FR1 serving
cell and FR1 target cell for 1 Rx UE 5652A.16.7.2.3.1 Test Purpose and
Environment 5652A.16.7.2.3.2 Test parameters 5652A.16.7.2.3.3 Test
Requirements 5657A.16.7.2.4 SA Inter-frequency measurement accuracy with
FR1 serving cell and FR1 target cell for 2 Rx UE 5657A.16.7.2.4.1 Test
Purpose and Environment 5657A.16.7.2.4.2 Test parameters
5657A.16.7.2.4.3 Test Requirements 5663A.16.7.3 SS-SINR 5663A.16.7.3.1
SA intra-frequency measurement accuracy with FR1 serving cell and FR1
target cell for 1 Rx UE 5663A.16.7.3.1.1 Test Purpose and Environment
5663A.16.7.3.1.2 Test parameters 5664A.16.7.3.1.3 Test Requirements
5668A.16.7.3.2 SA intra-frequency measurement accuracy with FR1 serving
cell and FR1 target cell for 2 Rx UE 5668A.16.7.3.2.1 Test Purpose and
Environment 5668A.16.7.3.2.2 Test parameters 5669A.16.7.3.3 SA
Inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell for 1 Rx UE 5673A.16.7.3.3.1 Test Purpose and Environment
5673A.16.7.3.3.2 Test parameters 5673A.16.7.3.3.3 Test Requirements
5678A.16.7.3.4 SA Inter-frequency measurement accuracy with FR1 serving
cell and FR1 target cell for 2 Rx UE 5679A.16.7.3.4.1 Test Purpose and
Environment 5679A.16.7.3.4.2 Test parameters 5679A.16.7.3.4.3 Test
Requirements 5683A.16.7.4 L1-RSRP measurement for beam reporting
5684A.16.7.4.1 SSB based L1-RSRP measurement for 1 Rx UE
5684A.16.7.4.1.1 Test Purpose and Environment 5684A.16.7.4.1.2 Test
parameters 5684A.16.7.4.1.3 Test Requirements 5688A.16.7.4.2 SSB based
L1-RSRP measurement for 2 Rx UE 5688A.16.7.4.2.1 Test Purpose and
Environment 5688A.16.7.4.2.2 Test parameters 5688A.16.7.4.2.3 Test
Requirements 5689A.16.7.4.3 CSI-RS based L1-RSRP measurement on resource
set with repetition off for 1 Rx UE 5689A.16.7.4.3.1 Test Purpose and
Environment 5689A.16.7.4.3.2 Test parameters 5689A.16.7.4.3.3 Test
Requirements 5693A.16.7.4.4 CSI-RS based L1-RSRP measurement on resource
set with repetition off for 2 Rx UE 5693A.16.7.4.4.1 Test Purpose and
Environment 5693A.16.7.4.4.2 Test parameters 5694A.16.7.4.4.3 Test
Requirements 5694A.16.7.5 E-UTRAN RSRP 5694A.16.7.5.1 SA: inter-RAT
measurement accuracy with FR1 serving cell for 1 Rx UE 5694A.16.7.5.1.1
Test Purpose and Environment 5694A.16.7.5.1.2 Test parameters
5694A.16.7.5.1.3 Test Requirements 5700A.16.7.5.2 SA: inter-RAT
measurement accuracy with FR1 serving cell for 2 Rx UE 5701A.16.7.5.2.1
Test Purpose and Environment 5701A.16.7.5.2.2 Test parameters
5701A.16.7.5.2.3 Test Requirements 5707A.16.7.6 E-UTRAN RSRQ
5708A.16.7.6.1 SA: inter-RAT measurement accuracy with FR1 serving cell
for 1 Rx UE 5708A.16.7.6.1.1 Test Purpose and Environment
5708A.16.7.6.1.2 Test parameters 5708A.16.7.6.1.3 Test Requirements
5714A.16.7.6.2 SA: inter-RAT measurement accuracy with FR1 serving cell
for 2 Rx UE 5715A.16.7.6.2.1 Test Purpose and Environment
5715A.16.7.6.2.2 Test parameters 5715A.16.7.6.2.3 Test Requirements
5721A.17 NR standalone tests with one or more NR cells in FR2 for RedCap
5722A.17.1 SA: RRC\_IDLE state mobility for RedCap 5722A.17.1.1 Cell
re-selection to NR 5722A.17.1.1.1 Cell reselection to FR2
intra-frequency NR case for 2 Rx 5722A.17.1.1.1.1 Test Purpose and
Environment 5722A.17.1.1.1.2 Test Parameters 5722A.17.1.1.1.3 Test
Requirements 5726A.17.1.1.2 Cell reselection to FR2 inter-frequency NR
case 5726A.17.1.1.2.1 Test Purpose and Environment 5726A.17.1.1.2.2 Test
Parameters 5726A.17.1.1.2.3 Test Requirements 5730A.17.1.1.3 Cell
reselection to FR2 intra-frequency NR case for UE fulfilling stationary
relaxed measurement criterion for 2 Rx UE 5730A.17.1.1.3.1 Test Purpose
and Environment 5730A.17.1.1.3.2 Test Parameters 5730A.17.1.1.3.3 Test
Requirements 5733A.17.1.1.4 Cell reselection to FR2 inter-frequency NR
case for UE fulfilling stationary mobility relaxed measurement criterion
for 2 Rx UE 5733A.17.1.1.4.1 Test Purpose and Environment
5733A.17.1.1.4.2 Test Parameters 5733A.17.1.1.4.3 Test Requirements
5737A.17.2 SA: RRC\_INACTIVE state mobility for RedCap 5737A.17.2.1
Configured Grant based Small Data Transmissions (CG-SDT) for RedCap
5737A.17.2.1.1 TA validation for CG-SDT in FR2 for RedCap
5737A.17.2.1.1.1 Test Purpose and Environment 5737A.17.2.1.1.2 Test
Requirements 5741A.17.3 RRC\_CONNECTED state mobility for RedCap
5742A.17.3.1 Handover for RedCap 5742A.17.3.1.1 Intra-frequency handover
from FR2 to FR2; unknown target cell for 2 Rx 5742A.17.3.1.1.1 Test
Purpose and Environment 5742A.17.3.1.1.2 Test Parameters
5742A.17.3.1.1.3 Test Requirements 5744A.17.3.1.2 Inter-frequency
handover from FR2 to FR2; unknown target cell for 2 Rx 5744A.17.3.1.2.1
Test Purpose and Environment 5744A.17.3.1.2.2 Test Parameters
5744A.17.3.1.2.3 Test Requirements 5747A.17.3.2 RRC Connection Mobility
Control for RedCap 5747A.17.3.2.1 SA: RRC Re-establishment
5747A.17.3.2.1.1 Intra-frequency RRC Re-establishment in FR2
5747A.17.3.2.1.1.1 Test Purpose and Environment 5747A.17.3.2.1.2
Inter-frequency RRC Re-establishment in FR2 5750A.17.3.2.1.2.1 Test
Purpose and Environment 5750A.17.3.2.1.3 Intra-frequency RRC
Re-establishment in FR2 without serving cell timing 5753A.17.3.2.1.3.1
Test Purpose and Environment 5753A.17.3.2.1.3.2 Test Requirements
5755A.17.3.2.2 Random Access 5756A.17.3.2.2.1 4-step RA type contention
based random access test in FR2 for NR Standalone 5756A.17.3.2.2.1.1
Test Purpose and Environment 5756A.17.3.2.2.1.2 Test Requirements
5758A.17.3.2.2.2 4-step RA type non-contention based random access test
in FR2 for NR Standalone 5760A.17.3.2.2.2.1 Test Purpose and Environment
5760A.17.3.2.2.2.2 Test Requirements 5762A.17.3.2.2.3 2-step RA type
contention based random access test in FR2 for NR Standalone
5764A.17.3.2.2.3.1 Test Purpose and Environment 5764A.17.3.2.2.3.2 Test
Requirements 5766A.17.3.2.2.4 2-step RA type non-contention based random
access test in FR2 for NR Standalone 5767A.17.3.2.2.4.1 Test Purpose and
Environment 5767A.17.3.2.2.4.2 Test Requirements 5769A.17.3.2.3 SA: RRC
Connection Release with Redirection 5770A.17.3.2.3.1 Redirection from NR
in FR2 to NR in FR2 5770A.17.3.2.3.1.1 Test Purpose and Environment
5770A.17.3.2.3.1.2 Test Parameters 5770A.17.3.2.3.1.3 Test Requirements
5774A.17.4 Timing 5774A.17.4.1 UE transmit timing 5774A.17.4.1.1 NR UE
Transmit Timing Test for FR2 5774A.17.4.1.1.1 Test Purpose and
environment 5774A.17.4.1.1.2 Test requirements 5777A.17.4.2 UE timer
accuracy 5778A.17.4.3 Timing advance 5778A.17.4.3.1 SA FR2 timing
advance adjustment accuracy 5778A.17.4.3.1.1 Test Purpose and
Environment 5778A.17.4.3.1.2 Test Parameters 5778A.17.4.3.1.3 Test
Requirements 5781A.17.5 Signaling characteristics for RedCap
5781A.17.5.1 Radio link Monitoring for RedCap 5781A.17.5.1.1 Radio Link
Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM
RS in non-DRX mode 5781A.17.5.1.1.1 Test Purpose and Environment
5781A.17.5.1.1.2 Test Requirements 5784A.17.5.1.2 Radio Link Monitoring
In-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX
mode 5785A.17.5.1.2.1 Test Purpose and Environment 5785A.17.5.1.2.2 Test
Requirements 5789A.17.5.1.3 Radio Link Monitoring Out-of-sync Test for
FR2 PCell configured with SSB-based RLM RS in DRX mode 5790A.17.5.1.3.1
Test Purpose and Environment 5790A.17.5.1.3.2 Test Requirements
5794A.17.5.1.4 Radio Link Monitoring In-sync Test for FR2 PCell
configured with SSB-based RLM RS in DRX mode 5794A.17.5.1.4.1 Test
Purpose and Environment 5794A.17.5.1.4.2 Test Requirements
5799A.17.5.1.5 Radio Link Monitoring Out-of-sync Test for FR2 PCell
configured with CSI-RS-based RLM in non-DRX mode 5799A.17.5.1.5.1 Test
Purpose and Environment 5799A.17.5.1.5.2 Test Requirements
5804A.17.5.1.6 Radio Link Monitoring In-sync Test for FR2 PCell
configured with CSI-RS-based RLM in non-DRX mode 5804A.17.5.1.6.1 Test
Purpose and Environment 5804A.17.5.1.6.2 Test Requirements
5808A.17.5.1.7 Radio Link Monitoring Out-of-sync Test for FR2 PCell
configured with CSI-RS-based RLM in DRX mode 5808A.17.5.1.7.1 Test
Purpose and Environment 5808A.17.5.1.7.2 Test Requirements
5812A.17.5.1.8 Radio Link Monitoring In-sync Test for FR2 PCell
configured with CSI-RS-based RLM in DRX mode 5812A.17.5.1.8.1 Test
Purpose and Environment 5812A.17.5.1.8.2 Test Requirements
5817A.17.5.1.9 UE Radio Link Monitoring Scheduling Restrictions on FR2
5817A.17.5.1.9.1 Test Purpose and Environment 5817A.17.5.1.9.2 Test
Requirements 5820A.17.5.2 Beam Failure Detection and Link recovery
procedures 5820A.17.5.2.1 Beam Failure Detection and Link Recovery Test
for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode
5820A.17.5.2.1.1 Test Purpose and Environment 5820A.17.5.2.1.2 Test
Requirements 5824A.17.5.2.2 Beam Failure Detection and Link Recovery
Test for FR2 PCell configured with SSB-based BFD and LR in DRX mode
5824A.17.5.2.2.1 Test Purpose and Environment 5824A.17.5.2.2.2 Test
Requirements 5828A.17.5.2.3 Beam Failure Detection and Link Recovery
Test for FR2 PCell configured with CSI-RS-based BFD and LR in non-DRX
mode 5828A.17.5.2.3.1 Test Purpose and Environment 5828A.17.5.2.3.2 Test
Requirements 5832A.17.5.2.4 Beam Failure Detection and Link Recovery
Test for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode
5832A.17.5.2.4.1 Test Purpose and Environment 5832A.17.5.2.4.2 Test
Requirements 5836A.17.5.2.5 Scheduling availability restriction during
Beam Failure Detection and Link Recovery for FR2 PCell configured with
SSB-based BFD and LR in non-DRX mode for 2 Rx UE 5836A.17.5.2.5.1 Test
Purpose and Environment 5836A.17.5.2.5.2 Test Requirements 5840A.17.5.3
Active BWP switch for RedCap 5840A.17.5.3.1 DCI-based and Timer-based
Active BWP Switch 5840A.17.5.3.1.1 NR FR2 DL active BWP switch with
non-DRX in SA 5840A.17.5.3.1.1.1 Test Purpose and Environment
5840A.17.5.3.1.1.2 Test Requirements 5843A.17.5.3.2 RRC-based Active BWP
Switch 5843A.17.5.3.2.1 NR FR2 DL active BWP switch of PCell with
non-DRX in SA 5843A.17.5.3.2.1.1 Test Purpose and Environment
5843A.17.5.3.2.1.2 Test Requirements 5846A.17.5.4 Active TCI state
switch delay 5847A.17.5.4.1 MAC-CE based active TCI state switch
5847A.17.5.4.1.1 NR PCell FR2 active TCI state switch for a known TCI
state 5847A.17.5.4.1.1.1 Test Purpose and Environment 5847A.17.5.4.1.1.2
Test Requirements 5850A.17.5.4.2 RRC based active TCI state switch
5850A.17.5.4.2.1 NR PCell FR2 active TCI state switch for a known TCI
state 5850A.17.5.4.2.1.1 Test Purpose and Environment 5850A.17.5.4.2.1.2
Test Requirements 5854A.17.5.5 Uplink spatial relation switch delay
5854A.17.5.5.1 MAC-CE based Spatial Relation switch 5854A.17.5.5.1.1 NR
PCell FR2 spatial relation associated with known DL-RS
5854A.17.5.5.1.1.1 Test Purpose and Environment 5854A.17.5.5.1.1.2 Test
Requirements 5857A.17.5.5.2 RRC based spatial relation switch
5857A.17.5.5.2.1 NR PCell FR2 spatial relation switch associated with a
known DL-RS 5857A.17.5.5.2.1.2 Test Requirements 5860A.17.5.6 UE
specific CBW change 5860A.17.5.6.1 NR FR2 UE specific CBW change of
PCell with non-DRX in SA 5860A.17.5.6.1.1 Test Purpose and Environment
5860A.17.5.6.1.2 Test Requirements 5863A.17.6 Measurement procedure for
RedCap 5864A.17.6.1 Intra-frequency Measurements 5864A.17.6.1.1 SA event
triggered reporting test without gap under non-DRX 5864A.17.6.1.1.1 Test
purpose and Environment 5864A.17.6.1.1.2 Test Requirements
5867A.17.6.1.2 SA event triggered reporting test without gap under DRX
5867A.17.6.1.2.1 Test purpose and Environment 5867A.7.6.1.2.2 Test
Requirements 5867A.17.6.1.3 SA event triggered reporting test with
per-UE gaps under non-DRX 5868A.17.6.1.3.1 Test purpose and Environment
5868A.17.6.1.3.2 Test Requirements 5872A.17.6.1.4 SA event triggered
reporting test with per-UE gaps under DRX 5872A.17.6.1.4.1 Test purpose
and Environment 5872A.17.6.1.4.2 Test Requirements 5875A.17.6.2
Inter-frequency Measurements 5876A.17.6.2.1 SA event triggered reporting
tests For FR2 without SSB time index detection when DRX is not used
(PCell in FR2) 5876A.17.6.2.1.1 Test Purpose and Environment
5876A.17.6.2.1.2 Test Requirements 5879A.17.6.2.2 SA event triggered
reporting tests For FR2 without SSB time index detection when DRX is
used (PCell in FR2) 5879A.17.6.2.2.1 Test Purpose and Environment
5879A.17.6.2.2.2 Test Requirements 5883A.17.6.2.3 SA event triggered
reporting tests For FR2 with SSB time index detection when DRX is not
used (PCell in FR2) 5883A.17.6.2.3.1 Test Purpose and Environment
5883A.17.6.2.3.2 Test Requirements 5887A.17.6.2.4 SA event triggered
reporting tests For FR2 with SSB time index detection when DRX is used
(PCell in FR2) for 2 RX UE 5887A.17.6.2.4.1 Test Purpose and Environment
5887A.17.6.2.4.2 Test Requirements 5891A.17.6.3 L1-RSRP measurement for
beam reporting 5892A.17.6.3.1 SSB based L1-RSRP measurement when DRX is
not used 5892A.17.6.3.1.1 Test Purpose and Environment 5892A.17.6.3.1.2
Test parameters 5892A.17.6.3.1.3 Test Requirements 5892A.17.6.3.2 SSB
based L1-RSRP measurement when DRX is used 5892A.17.6.3.2.1 Test Purpose
and Environment 5892A.17.6.3.2.2 Test parameters 5892A.17.6.3.2.3 Test
Requirements 5894A.17.6.3.3 CSI-RS based L1-RSRP measurement when DRX is
not used 5894A.17.6.3.3.1 Test Purpose and Environment 5894A.17.6.3.3.2
Test parameters 5895A.17.6.3.3.3 Test Requirements 5897A.17.6.3.4 CSI-RS
based L1-RSRP measurement when DRX is used 5898A.17.6.3.4.1 Test Purpose
and Environment 5898A.17.6.3.4.2 Test parameters 5898A.7.6.3.3.3 Test
Requirements 5900A.17.6.4 NR Measurements with autonomous gaps
5901A.17.6.4.1 SA interfrequency CGI reporting in autonomous gaps test
(PCell in FR2) for 2 RX UE 5901A.17.6.4.1.1 Test Purpose and Environment
5901A.17.6.4.1.2 Test Requirements 5904A.17.7 Measurement Performance
requirements 5904A.17.7.1 SS-RSRP 5904A.17.7.1.1 SA intra-frequency case
measurement accuracy with FR2 serving cell and FR2 target cell
5904A.17.7.1.1.1 Test Purpose and Environment 5904A.17.7.1.1.2 Test
parameters 5904A.17.7.1.1.3 Test Requirements 5908A.17.7.1.2 SA
inter-frequency case measurement accuracy with FR2 serving cell and FR2
target cell 5909A.17.7.1.2.1 Test Purpose and Environment
5909A.17.7.1.2.2 Test parameters 5909A.17.7.1.2.3 Test Requirements
5913A.17.7.2 SS-RSRQ 5914A.17.7.2.1 SA intra-frequency measurement
accuracy with FR2 serving cell and FR2 target cell 5914A.17.7.2.1.1 Test
Purpose and Environment 5914A.17.7.2.1.2 Test Parameters
5914A.17.7.2.1.3 Test Requirements 5916A.17.7.2.2 SA Inter-frequency
measurement accuracy with FR2 serving cell and FR2 TDD target cell for 2
Rx UE 5916A.17.7.2.2.1 Test Purpose and Environment 5916A.17.7.2.2.2
Test parameters 5916A.17.7.2.2.3 Test Requirements 5918A.17.7.3 L1-RSRP
measurement for beam reporting 5918A.17.7.3.1 SSB based L1-RSRP
measurement 5918A.17.7.3.1.1 Test Purpose and Environment
5918A.17.7.3.1.2 Test parameters 5919A.17.7.3.1.3 Test Requirements
5919A.17.7.3.2 CSI-RS based L1-RSRP measurement on resource set with
repetition off 5919A.17.7.3.2.1 Test Purpose and Environment
5919A.17.7.3.2.2 Test parameters 5919A.17.7.3.2.3 Test Requirements
5919A.17.7.4 SS-SINR 5920A.17.7.4.1 SA intra-frequency case measurement
accuracy with FR2 serving cell and FR2 target cell for 2Rx UE
5920A.17.7.4.1.1 Test Purpose and Environment 5920A.17.7.4.1.2 Test
parameters 5920A.17.7.4.1.3 Test Requirements 5922A.17.7.4.2 SA
inter-frequency case measurement accuracy with FR2 serving cell and FR2
target cell for 2Rx UE 5922A.17.7.4.2.1 Test Purpose and Environment
5922A.17.7.4.2.2 Test Parameters 5922A.17.7.4.2.3 Test Requirements
5924A.18 E-UTRA standalone tests for NR RRM for RedCap 5924A.18.1
RRC\_IDLE state mobility 5924A.18.1.1 Inter-RAT NR Cell re-selection
5924A.18.1.1.1 E-UTRA Cell reselection to higher priority NR target Cell
in FR1 5924A.18.1.1.1.1 Test Purpose and Environment 5924A.18.1.1.1.2
Test Requirements 5929A.18.2 RRC\_CONNECTED state mobility 5929A.18.2.1
Handover 5929A.18.2.1.1 E-UTRAN - NR handover in FR1 5929A.18.2.1.1.1
Test Purpose and Environment 5929A.18.2.1.1.2 Test Requirements
5934A.18.2.2 RRC connection release with redirection 5934A.18.2.2.1
Redirection from E-UTRA to NR FR1 for redcap UE 5934A.18.2.2.1.1 Test
Purpose and Environment 5934A.18.2.2.1.2 Test Parameters
5934A.18.2.2.1.3 Test Requirements 5941A.18.3 Measurement procedure
5941A.18.3.1 E-UTRA -- NR Inter-RAT Measurements 5941A.18.3.1.1 NR
Inter-RAT event triggered reporting tests for FR1 without SSB time index
detection when DRX is not used 5941A.18.3.1.1.1 Test Purpose and
Environment 5941A.18.3.1.1.2 Test Requirements 5946A.18.3.1.2 NR
Inter-RAT event triggered reporting tests for FR1 without SSB time index
detection when DRX is used 5946A.18.3.1.2.1 Test Purpose and Environment
5946A.18.3.1.2.2 Test Requirements 5952A.18.3.1.3 NR Inter-RAT event
triggered reporting tests for FR1 with SSB time index detection when DRX
is not used 5952A.18.3.1.3.1 Test Purpose and Environment
5952A.18.3.1.3.2 Test Requirements 5958A.18.3.1.4 NR Inter-RAT event
triggered reporting tests for FR1 with SSB time index detection when DRX
is used 5958A.18.3.1.4.1 Test Purpose and Environment 5958A.18.3.1.4.2
Test Requirements 5964A.18.3.1.5 NR Inter-RAT event triggered reporting
tests for FR2 without SSB time index detection when DRX is not used
5964A.18.3.1.5.1 Test Purpose and Environment 5964A.18.3.1.5.2 Test
Requirements 5966A.18.3.1.6 NR Inter-RAT event triggered reporting tests
for FR2 without SSB time index detection when DRX is used
5967A.18.3.1.6.1 Test Purpose and Environment 5967A.18.3.1.6.2 Test
Requirements 5969A.18.3.1.7 NR Inter-RAT event triggered reporting tests
for FR2 with SSB time index detection when DRX is not used
5970A.18.3.1.7.1 Test Purpose and Environment 5970A.18.3.1.7.2 Test
Requirements 5972A.18.3.1.8 NR Inter-RAT event triggered reporting tests
for FR2 with SSB time index detection when DRX is used 5973A.18.3.1.8.1
Test Purpose and Environment 5973A.18.3.1.8.2 Test Requirements
5975Annex B (normative): Conditions for RRM requirements applicability
for operating bands 5976B.1 Conditions for NR RRC\_IDLE state mobility
5976B.1.1 Introduction 5976B.1.2 Conditions for measurements on NR
intra-frequency cells for cell re-selection 5976B.1.2A Conditions for
measurements on NR intra-frequency cells under CCA for cell re-selection
5977B.1.3 Conditions for measurements on NR inter-frequency cells for
cell re-selection 5978B.1.3A Conditions for measurements on NR
inter-frequency cells under CCA for cell re-selection 5978B.1.4
Conditions for measurements on NR intra-frequency cells for cell
re-selection for RedCap 5978B.1.5 Conditions for measurements on NR
inter-frequency cells for cell re-selection for RedCap 5979B.1.6
Conditions for measurements on NR intra-frequency cells for cell
re-selection for satellite access 5980B.1.7 Conditions for measurements
on NR inter-frequency cells for cell re-selection for satellite access
5980B.2 Conditions for UE measurements procedures and performance
requirements in RRC\_CONNECTED state 5980B.2.1 Introduction 5980B.2.1.1
General 5980B.2.1.2 Derivation of Minimum SSB\_RP values for FR1
5980B.2.1.3 Derivation of Minimum SSB\_RP values for FR2 5981B.2.1.3.1
Minimum SSB\_RP values for Rx Beam Peak angle of arrival 5981B.2.1.3.2
Minimum SSB\_RP values for angle of arrival within Spherical coverage
5981B.2.1.4 Gain to SS-RSRP and CSI-RSRP measurement point for FR1
5982B.2.1.5 Gain to SS-RSRP and CSI-RSRP measurement point for FR2
5982B.2.1.5.1 Gain to SS-RSRP and CSI-RSRP measurement point for Rx Beam
Peak angle of arrival 5982B.2.1.5.2 Gain to SS-RSRP measurement point
for different frequency 5983B.2.1.5.3 Alignment of Rough beam to Rx beam
Peak 5983B.2.1.6 Gain to PRS-RSRP measurement point for FR2
5984B.2.1.6.1 Gain to PRS-RSRP measurement point for Rx Beam Peak angle
of arrival 5984B.2.2 Conditions for NR intra-frequency measurements
5984B.2.3 Conditions for NR inter-frequency measurements 5986B.2.4
Conditions for NR L1-RSRP reporting 5987B.2.4.1 Conditions for SSB based
L1-RSRP reporting 5987B.2.4.2 Conditions for CSI-RS based L1-RSRP
reporting 5988B.2.5 Conditions for RRC connection release with
redirection to NR 5990B.2.6 Void 5991B.2.6.1 Void 5991B.2.6.2 Void
5991B.2.7 Conditions for SRS-RSRP measurements 5991B.2.8 Conditions for
NR L1-SINR reporting 5992B.2.8.1 Conditions for L1-SINR reporting with
CSI-RS based CMR and no dedicated IMR configured 5992B.2.8.2 Conditions
for L1-SINR reporting with SSB based CMR and dedicated IMR configured
5993B.2.8.2.1 L1-SINR reporting with SSB based CMR and dedicated ZP-IMR
configured 5993B.2.8.2.2 L1-SINR reporting with SSB based CMR and
dedicated NZP-IMR configured 5993B.2.8.3 Conditions for L1-SINR
reporting with CSI-RS based CMR and dedicated IMR configured
5995B.2.8.3.1 L1-SINR reporting with CSI-RS based CMR and dedicated
ZP-IMR configured 5995B.2.8.3.2 L1-SINR reporting with CSI-RS based CMR
and dedicated NZP-IMR configured 5996B.2.9 Conditions for NR
intra-frequency measurements under CCA 5997B.2.10 Conditions for NR
inter-frequency measurements under CCA 5997B.2.11 Conditions for NR
L1-RSRP reporting under CCA 5997B.2.11.1 Conditions for SSB based
L1-RSRP reporting 5997B.2.12 Conditions for NR CSI-RS based
intra-frequency measurements 5998B.2.13 Conditions for NR CSI-RS based
inter-frequency measurements 5999B.2.14 Conditions for NR PRS-based
measurements 6001B.2.15 Conditions for NR intra-frequency measurements
for RedCap 6003B.2.16 Conditions for NR inter-frequency measurements for
RedCap 6004B.2.17 Conditions for NR intra-frequency measurements for
satellite access 6006B.2.18 Conditions for NR inter-frequency
measurements for satellite access 6007B.2.19 Conditions for NR L1-RSRP
reporting for satellite access 6007B.2.19.1 Conditions for SSB based
L1-RSRP reporting for satellite access 6007B.2.19.2 Conditions for
CSI-RS based L1-RSRP reporting for satellite access 6007B.2.20
Conditions for RRC connection release with redirection to NR for
satellite access 6008B.3 RRM Requirements Exceptions 6008B.3.1
Introduction 6008B.3.2 Receiver sensitivity relaxation for CA
6008B.3.2.1 Receiver sensitivity relaxation for UE supporting CA in FR1
6008B.3.2.2 Receiver sensitivity relaxation for UE configured with CA in
FR1 6008B.3.2.2.1 Inter-band carrier aggregation 6008B.3.2.2.2 Reference
sensitivity exceptions due to UL harmonic interference for CA
6008B.3.2.2.3 Reference sensitivity exceptions due to intermodulation
interference due to 2UL CA 6009B.3.2.3 Receiver sensitivity relaxation
for UE supporting CA in FR2 6009B.3.2.4 Receiver sensitivity relaxation
for UE configured with CA in FR2 6009B.3.2.4.1 Intra-band contiguous
carrier aggregation 6009B.3.2.4.2 Intra-band non-contiguous carrier
aggregation 6009B.3.3 Receiver sensitivity relaxation for DC 6009B.3.3.1
Receiver sensitivity relaxation for EN-DC 6009B.3.3.2 Receiver
sensitivity relaxation for NE-DC 6009B.3.4 Receiver sensitivity
relaxation for SUL 6009B.3.4.1 Receiver sensitivity relaxation for UE
supporting SUL in FR1 6009B.3.4.2 Receiver sensitivity relaxation for UE
configured with SUL in FR1 6010B.3.4.2.1 Reference sensitivity
exceptions due to UL harmonic interference for SUL 6010B.4 Conditions
for V2X 6010B.4.1 Test parameters for GNSS signals 6010B.4.2 Conditions
for PSBCH-RSRP Accuracy Requirements 6010B.4.3 Conditions for
Selection/Reselection to Intra-frequency SyncRef UE 6011B.4.4 Conditions
for L1 SL-RSRP Accuracy Requirements 6011B.5 High level test procedure
for SAN RRM tests 6011Annex C (informative): Change history 6013
