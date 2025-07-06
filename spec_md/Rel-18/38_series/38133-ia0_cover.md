+-------------------------------------------+-------------------------+
| 3GPP TS 38.133 V18.10.0 (2025-06)         |                         |
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
| (Release 18)                              |                         |
+-------------------------------------------+-------------------------+
|                                           |                         |
+-------------------------------------------+-------------------------+
|                                           | ![](./media/image2.png) |
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

Foreword 1491 Scope 1512 References 1513 Definitions, symbols and
abbreviations 1533.1 Definitions 1533.2 Symbols 1543.3 Abbreviations
1553.4 Test tolerances 1583.5 Frequency bands grouping 1583.5.1
Introduction 1583.5.2 NR operating bands in FR1 1593.5.2A NR operating
bands for satellite access in FR1 1483.5.3 NR operating bands in FR2
1483.6 Applicability of requirements in this specification version
1493.6.1 RRC connected state requirements in DRX 1493.6.2 Number of
serving carriers 1503.6.2.1 Number of serving carriers for SA 1503.6.2.2
Number of serving carriers for EN-DC 1503.6.2.3 Number of serving
carriers for NE-DC 1503.6.2.4 Number of serving carriers for NR-DC
1503.6.3 Applicability for intra-band FR2 1503.6.4 Applicability for FR2
UE power classes 1503.6.5 Applicability for SDL bands 1513.6.6
Applicability of requirements for NGEN-DC operation 1513.6.7
Applicability of QCL 1513.6.9 Applicability of requirements for
scheduling availability 1523.6.10 Applicability of requirements for
measurement restrictions 1523.6.11 Applicability of requirements for
Redcap UEs 1523.6.11.1 RRC connected state requirements in DRX
1523.6.11.2 Applicability for FR2 Redcap UE power classes 1523.6.11.3
Applicability of QCL 1523.6.12 Applicability of requirements for
Satellite Access 1523.6.13 Applicability of requirements for FR2
1523.6.14 Applicability of requirements for FR2 Power Class 6 1533.6.15
Applicability of requirements for per-FR gap 1533.6.16 Applicability of
requirements for ATG 1533.6.17 Applicability of requirements for MUSIM
gaps 1533.6.18 Applicability of requirements for a UE operating on a
cell with less than 5 MHz BW 1533.6.19 Applicability of requirements for
multi-Rx operation in FR2-1 1534 SA: RRC\_IDLE state mobility 1534.1
Cell Selection 1534.2 Cell Re-selection 1544.2.1 Introduction 1544.2.2
Requirements 1544.2.2.1 UE measurement capability 1544.2.2.2 Measurement
and evaluation of serving cell 1544.2.2.3 Measurements of
intra-frequency NR cells 1564.2.2.4 Measurements of inter-frequency NR
cells 1604.2.2.5 Measurements of inter-RAT E-UTRAN cells 1654.2.2.6
Maximum interruption in paging reception 1674.2.2.7 General requirements
1684.2.2.8 Minimum requirement at transitions 1684.2.2.9 Measurements of
intra-frequency NR cells for UE configured with relaxed measurement
criterion 1694.2.2.9.1 Introduction 1694.2.2.9.2 Measurements for UE
fulfilling low mobility criterion 1694.2.2.9.3 Measurements for UE
fulfilling not-at-cell edge criterion 1714.2.2.9.4 Measurements for UE
fulfilling low mobility and not-at-cell edge criteria 1734.2.2.10
Measurements of inter-frequency NR cells for UE configured with relaxed
measurement criterion 1744.2.2.10.1 Introduction 1744.2.2.10.2
Measurements for UE fulfilling low mobility criterion 1744.2.2.10.3
Measurements for UE fulfilling not-at-cell edge criterion 1764.2.2.10.4
Measurements for UE fulfilling low mobility and not-at-cell edge
criterion 1794.2.2.11 Measurements of inter-RAT E-UTRAN cells for UE
configured with relaxed measurement criterion 1794.2.2.11.1 Introduction
1794.2.2.11.2 Measurements for UE fulfilling low mobility criterion
1804.2.2.11.3 Measurements for UE fulfilling with not-at-cell edge
criterion 1814.2.2.11.4 Measurements for UE fulfilling low mobility and
not-at-cell edge criterion 1834.2.2.12 Measurements of inter-frequency
NR cells with NTN carrier 1834.2A Cell Re-selection when subject to CCA
1864.2A.1 Introduction 1864.2A.2 Requirements 1874.2A.2.1 UE measurement
capability 1874.2A.2.2 Measurement and evaluation when subject to CCA on
the serving cell 1874.2A.2.3 Measurements of intra-frequency NR cells
when subject to CCA on the serving cell and target cell 1884.2A.2.4
Measurements of inter-frequency NR cells when subject to CCA on the
target cell 1894.2A.2.5 Measurements of inter-RAT E-UTRAN cells when
subject to CCA on the serving cell 1914.2A.2.6 Maximum interruption in
paging reception when subject to CCA on the target cell 1914.2A.2.7
General requirements 1924.2B Cell Re-selection for RedCap 1924.2B.1
Introduction 1924.2B.2 Requirements 1924.2B.2.1 UE measurement
capability for RedCap 1924.2B.2.1.1 UE measurement capability for 1 Rx
RedCap 1924.2B.2.1.2 UE measurement capability for 2 Rx RedCap
1924.2B.2.2 Measurement and evaluation of serving cell for RedCap UE
1924.2B.2.3 Measurements of intra-frequency NR cells for RedCap UE
1944.2B.2.4 Measurements of inter-frequency NR cells for RedCap UE
1964.2B.2.5 Measurements of inter-RAT E-UTRAN cells for RedCap UE
1994.2B.2.6 Maximum interruption in paging reception for RedCap
2014.2B.2.7 General requirements for RedCap 2014.2B.2.8 Minimum
requirement at transitions 2014.2B.2.9 Measurements of intra-frequency
NR cells for UE configured with relaxed measurement criterion for RedCap
2024.2B.2.9.1 Introduction 2024.2B.2.9.2 Measurements for UE fulfilling
stationary criterion 2034.2B.2.9.3 Measurements for a UE fulfilling
not-at-cell edge while stationary criterion 2054.2B.2.9.3A Measurements
for a UE fulfilling stationary and not-at-cell-edge criteria
2064.2B.2.9.4 Measurements for a UE fulfilling low mobility and
stationary criteria 2064.2B.2.9.5 Measurements for a UE fulfilling low
mobility and not-at-cell-edge while stationary criteria 2064.2B.2.9.6
Measurements for a UE fulfilling not-at-cell edge and not-at-cell edge
while stationary criteria 2074.2B.2.9.7 Measurements for a UE fulfilling
low mobility and not-at-cell edge criteria and not-at-cell-edge while
stationary criteria 2074.2B.2.9.8 Measurements for a UE fulfilling low
mobility, not-at-cell edge and stationary criterion 2074.2B.2.9.9
Measurements for UE fulfilling low mobility criterion 2074.2B.2.9.10
Measurements for UE fulfilling not-at-cell edge criterion 2104.2B.2.9.11
Measurements for UE fulfilling low mobility and not-at-cell edge
criteria 2124.2B.2.10 Measurements of inter-frequency NR cells for UE
configured with relaxed measurement criterion 2134.2B.2.10.1
Introduction 2134.2B.2.10.2 Measurements for UE fulfilling stationary
criterion 2134.2B.2.10.3 Measurements for a UE fulfilling not-at-cell
edge while stationary criterion 2154.2B.2.10.3A Measurements for a UE
fulfilling stationary and not-at-cell-edge criterion 2164.2B.2.10.4
Measurements for a UE fulfilling low mobility and stationary criteria
2164.2B.2.10.5 Measurements for a UE fulfilling low mobility and
not-at-cell-edge while stationary criteria 2164.2B.2.10.6 Measurements
for a UE fulfilling not-at-cell edge and not-at-cell edge while
stationary criteria 2174.2B.2.10.7 Measurements for a UE fulfilling low
mobility and not-at-cell edge criteria and not-at-cell-edge while
stationary criteria 2174.2B.2.10.8 Measurements for a UE fulfilling low
mobility, not-at-cell edge and stationary criteria 2174.2B.2.10.9
Measurements for UE fulfilling low mobility criterion 2174.2B.2.10.10
Measurements for UE fulfilling not-at-cell edge criterion
2204.2B.2.10.11 Measurements for UE fulfilling low mobility and
not-at-cell edge criterion 2224.2B.2.11 Measurements of inter-RAT
E-UTRAN cells for UE configured with relaxed measurement criterion
2224.2B.2.11.1 Introduction 2224.2B.2.11.2 Measurements for UE
fulfilling stationary criterion 2234.2B.2.11.3 Measurements for a UE
fulfilling not-at-cell edge while stationary criterion 2244.2B.2.11.3A
Measurements for a UE fulfilling stationary and not-at-cell-edge
criterion 2244.2B.2.11.4 Measurements for a UE fulfilling low mobility
and stationary criteria 2254.2B.2.11.5 Measurements for a UE fulfilling
low mobility and not-at-cell-edge while stationary criteria
2254.2B.2.11.6 Measurements for a UE fulfilling not-at-cell edge and
not-at-cell edge while stationary criteria 2254.2B.2.11.7 Measurements
for a UE fulfilling low mobility and not-at-cell edge criteria and
not-at-cell-edge while stationary criteria 2254.2B.2.11.8 Measurements
for a UE fulfilling low mobility, not-at-cell edge and stationary
criteria 2264.2B.2.11.9 Measurements for UE fulfilling low mobility
criterion 2264.2B.2.11.10 Measurements for UE fulfilling with
not-at-cell edge criterion 2274.2B.2.11.11 Measurements for UE
fulfilling low mobility and not-at-cell edge criterion 2284.2C Cell
Re-selection for NR UE for Satellite Access 2294.2C.1 Introduction
2294.2C.2 Requirements 2294.2C.2.1 UE measurement capability 2294.2C.2.2
Measurement and evaluation of serving cell 2294.2C.2.3 Measurements of
intra-frequency NR cells 2304.2C.2.4 Measurements of inter-frequency NR
cells 2334.2C.2.5 Maximum interruption in paging reception 2364.2C.2.6
Minimum requirement at transitions 2374.2C.2.7 Measurements of
intra-frequency NR cells for UE configured with relaxed measurement
criterion 2374.2C.2.8 Measurements of inter-frequency NR cells for UE
configured with relaxed measurement criterion 2374.2C.2.9 General
requirements 2374.2C.2.10 Measurements of inter-frequency NR cells with
TN carrier 2374.2C.2.11 Measurements of inter-RAT E-UTRAN cells with TN
carrier 2404.2C.3 Void 2414.2C.4 Void 2414.2D Cell Re-selection for ATG
2414.2D.1 Introduction 2414.2D.2 Requirements 2424.2D.2.1 UE measurement
capability 2424.2D.2.2 Measurement and evaluation of serving cell
2424.2D.2.3 Measurements of intra-frequency NR cells 2424.2D.2.4
Measurements of inter-frequency NR cells 2434.2D.2.5 Maximum
interruption in paging reception 2454.2D.2.6 General requirements 2454.3
Minimization of Drive Tests (MDT) 2464.3.1 Introduction 2464.3.2
Measurement Requirements 2464.3.3 Requirements for Relative Time Stamp
Accuracy 2464.3.4 Requirements for Relative Time Stamp Accuracy for RRC
Connection Establishment Failure Log Reporting 2474.3.5 Requirements for
Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure
Log Reporting 2474.3C Minimization of Drive Tests (MDT) for Satellite
Access 2474.3C.1 Introduction 2474.3C.2 Measurement Requirements
2484.3C.3 Requirements for Relative Time Stamp Accuracy 2484.3C.4
Requirements for Relative Time Stamp Accuracy for RRC Connection
Establishment Failure Log Reporting 2484.3C.5 Requirements for Relative
Time Stamp Accuracy for Radio Link Failure and Handover Failure Log
Reporting 2484.4 Idle Mode CA/DC Measurements 2494.4.1 Introduction
2494.4.2 Measurement Requirements 2494.4.2.1 Detected cell requirement
during state transition and Idle mode 2494.4.2.2 Measurements of
inter-frequency CA/DC candidate cells 2504.4.2.3 Measurements on serving
cell 2514.4.2.4 Measurements of E-UTRAN inter-RAT DC candidate cells
2514.5 NR measurements for positioning 2514.5.1 Introduction 2514.5.2
RSTD measurements 2524.5.2.1 Introduction 2524.5.2.2 Requirements
Applicability 2524.5.2.3 Measurement Capability 2524.5.2.4 Measurement
Reporting Requirements 2524.5.2.5 Measurements Period Requirements
2524.5.2.6 Measurements Period Requirements with Bandwidth Aggregation
2564.5.3 PRS-RSRP measurements 2594.5.3.1 Introduction 2594.5.3.2
Requirements applicability 2594.5.3.3 Measurement Capability 2594.5.3.4
Measurement Reporting Requirements 2594.5.3.5 Measurement Period
Requirements 2604.5.4 PRS-RSRPP measurements 2624.5.4.1 Introduction
2624.5.4.2 Requirements Applicability 2624.5.4.3 Measurement Capability
2624.5.4.4 Measurement Reporting Requirements 2634.5.4.5 Measurement
Period Requirements 2634.5.5 Measurement requirements for DL RSCPD
reported with RSTD 2634.5.5.1 Introduction 2634.5.5.2 Requirements
Applicability 2634.5.5.3 Measurement Capability 2634.5.5.4 Measurement
Reporting Requirements 2634.5.5.5 Measurements Period Requirements
2644.6 NR measurements for positioning for RedCap 2684.6.1 Introduction
2684.6.2 RSTD measurements for RedCap 2684.6.2.1 Introduction 2684.6.2.2
Requirements Applicability 2694.6.2.3 Measurement Capability 2694.6.2.4
Measurement Reporting Requirements 2694.6.2.5 Measurements Period
Requirements without RX FH 2694.6.2.6 Measurement Period Requirements
with RX FH 2704.6.3 PRS-RSRP measurements for RedCap 2724.6.3.1
Introduction 2724.6.3.2 Requirements applicability 2724.6.3.3
Measurement Capability 2724.6.3.4 Measurement Reporting Requirements
2724.6.3.5 Measurement Period Requirements without RX FH 2734.6.3.6
Measurement Period Requirements with RX FH 2754.6.4 PRS-RSRPP
measurements for RedCap 2774.6.4.1 Introduction 2774.6.4.2 Requirements
Applicability 2774.6.4.3 Measurement Capability 2774.6.4.4 Measurement
Reporting Requirements 2774.6.4.5 Measurement Period Requirements
without RX FH 2784.6.4.6 Measurement Period Requirements with RX FH
2784.7 Measurement report for fast CA/DC setup 2784.7.1 Introduction
2784.7.2 Void 2784.7.3 Measurement Report Requirements 2785 SA:
RRC\_INACTIVE state mobility 2795.1 Cell Re-selection 2795.1.1
Introduction 2795.1.2 Requirements 2795.1.2.1 UE measurement capability
2795.1.2.2 Measurement and evaluation of serving cell 2795.1.2.3
Measurements of intra-frequency NR cells 2815.1.2.4 Measurements of
inter-frequency NR cells 2835.1.2.5 Measurements of inter-RAT E-UTRAN
cells 2855.1.2.6 Maximum interruption in paging reception 2865.1.2.7
General requirements 2865.1.2.8 Measurement of inter-frequency NR cells
with NTN carrier 2875.1.2.9 Minimum requirement at transitions
2875.1.2.10 Measurements of intra-frequency NR cells for UE configured
with relaxed measurement criterion 2875.1.2.11 Measurements of
inter-frequency NR cells for UE configured with relaxed measurement
criterion 2885.1.2.12 Measurements of inter-RAT E-UTRAN cells for UE
configured with relaxed measurement criterion 2895.1A Cell Re-selection
with CCA 2895.1A.1 Introduction 2895.1A.2 Requirements 2905.1A.2.1 UE
measurement capability 2905.1A.2.2 Measurement and evaluation when CCA
is used on the serving cell 2905.1A.2.3 Measurements of intra-frequency
NR cells when CCA is used on the serving cell and target cell
2905.1A.2.4 Measurements of inter-frequency NR cells when CCA is used on
the target cell 2905.1A.2.5 Measurements of inter-RAT E-UTRAN cells when
CCA is used on the serving cell 2905.1A.2.6 Maximum interruption in
paging reception when CCA is used on the target cell 2905.1A.2.7 General
requirements 2905.1B Cell Re-selection for RedCap 2905.1B.1 Introduction
2905.1B.2 Requirements 2905.1B.2.1 UE measurement capability 2905.1B.2.2
Measurement and evaluation of serving cell 2905.1B.2.3 Measurements of
intra-frequency NR cells 2935.1B.2.4 Measurements of inter-frequency NR
cells 2955.1B.2.5 Measurements of inter-RAT E-UTRAN cells 2975.1B.2.6
Maximum interruption in paging reception 2985.1B.2.7 General
requirements 2985.1B.2.8 Minimum requirement at transitions 2985.1B.2.9
Measurements of intra-frequency NR cells for UE configured with relaxed
measurement criterion 2985.1B.2.10 Measurements of inter-frequency NR
cells for UE configured with relaxed measurement criterion 3005.1B.2.11
Measurements of inter-RAT E-UTRAN cells for UE configured with relaxed
measurement criterion 3035.1C Cell Re-selection for Satellite Access
3045.1C.1 Introduction 3045.1C.2 Requirements 3045.1C.2.1 UE measurement
capability 3045.1C.2.2 Measurement and evaluation of serving cell
3045.1C.2.3 Measurements of intra-frequency NR cells 3045.1C.2.4
Measurements of inter-frequency NR cells 3055.1C.2.5 Maximum
interruption in paging reception 3055.1C.2.6 General requirements
3055.1C.2.7 Measurements of inter-frequency NR cells with TN carrier
3055.1C.2.8 Measurements of inter-RAT E-UTRAN cells with TN carrier
3055.1C.3 Void 3055.1C.4 Void 3055.1D Cell Re-selection for ATG
3055.1D.1 Introduction 3055.1D.2 Requirements 3055.1D.2.1 UE measurement
capability 3055.1D.2.2 Measurement and evaluation of serving cell
3055.1D.2.3 Measurements of intra-frequency NR cells 3055.1D.2.4
Measurements of inter-frequency NR cells 3055.1D.2.5 Maximum
interruption in paging reception 3065.1D.2.6 General requirements 3065.2
Void 3065.2B Configured Grant based Small Data Transmissions (CG-SDT)
for RedCap 3065.2B.1 Introduction 3065.2B.2 Requirements on UE
synchronization for small data transmissions for RedCap 3065.2B.2.1 Void
3065.2B.3 TA validation requirements for RedCap 3065.2B.3.1 Void
3075.2B.3.2 Void 3075.2B.4 Scheduling restriction 3075.2B.5
Applicability conditions for CG-SDT for RedCap 3085.3 Minimization of
Drive Tests (MDT) 3085.3.1 Introduction 3085.3.2 Measurement
Requirements 3085.3.3 Requirements for Relative Time Stamp Accuracy
3085.3.4 Requirements for Relative Time Stamp Accuracy for RRC
Connection Establishment Failure Log Reporting 3085.3.5 Requirements for
Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure
Log Reporting 3085.3.6 Requirements for Relative Time Stamp Accuracy for
RRC Resume Failure Log Reporting 3085.3C Minimization of Drive Tests
(MDT) for Satellite Access 3095.3C.1 Introduction 3095.3C.2 Measurement
Requirements 3095.3C.3 Requirements for Relative Time Stamp Accuracy
3095.3C.4 Requirements for Relative Time Stamp Accuracy for RRC
Connection Establishment Failure Log Reporting 3095.3C.5 Requirements
for Relative Time Stamp Accuracy for Radio Link Failure and Handover
Failure Log Reporting 3095.3C.6 Requirements for Relative Time Stamp
Accuracy for RRC Resume Failure Log Reporting 3095.4 Inactive Mode CA/DC
Measurements 3105.4.1 Introduction 3105.4.2 Measurement Requirements
3105.4.2.1 Detected cell requirement during state transition and
inactive mode 3105.4.2.2 Measurements of inter-frequency CA/DC candidate
cells 3105.4.2.3 Measurements on serving cell 3105.4.2.4 Measurements on
E-UTRAN inter-RAT DC candidate cells 3105.5 Configured Grant based Small
Data Transmissions (CG-SDT) 3105.5.1 Introduction 3105.5.2 Requirements
on UE synchronization for small data transmissions 3105.5.3 TA
validation requirements 3105.5.4 Scheduling restriction 3125.5.4.1
Scheduling availability of UE performing measurements in TDD bands on
FR1 3125.5.4.2 Scheduling availability of UE performing measurements
with a different subcarrier spacing than PDSCH/PDCCH on FR1 3125.5.4.3
Scheduling availability of UE performing measurements on FR2 3125.5.5
Applicability conditions for SDT 3135.5D Configured Grant based Small
Data Transmissions (CG-SDT) for ATG 3135.6 NR measurements for
positioning 3135.6.1 Introduction 3135.6.1A Cell re-selection for
positioning 3145.6.1A.1 Measurement and evaluation of serving cell
3145.6.1A.2 Measurements of intra-frequency NR cells 3155.6.2 RSTD
measurements 3165.6.2.1 Introduction 3165.6.2.2 Requirements
Applicability 3165.6.2.3 Measurement Capability 3165.6.2.5 Measurements
Period Requirements 3175.6.2.6 Measurements Period Requirements with
Bandwidth Aggregation 3205.6.3 PRS-RSRP measurements 3235.6.3.1
Introduction 3235.6.3.2 Requirements applicability 3235.6.3.3
Measurement Capability 3235.6.3.4 Measurement Reporting Requirements
3235.6.3.5 Measurement Period Requirements 3245.6.4 UE Rx-Tx time
difference measurements 3275.6.4.1 Introduction 3275.6.4.2 Requirements
Applicability 3275.6.4.3 Measurement Capability 3275.6.4.4 Measurement
Reporting Requirements 3275.6.4.5 Measurement Period Requirements
3275.6.4.6 Measurement Period Requirements with Bandwidth Aggregation
3315.6.5 PRS-RSRPP measurements 3345.6.5.1 Introduction 3345.6.5.2
Requirements Applicability 3345.6.5.3 Measurement Capability 3345.6.5.4
Measurement Reporting Requirements 3345.6.5.5 Measurement Period
Requirements 3355.6.6 TA validation requirements for positioning
3355.6.6.1 Introduction 3355.6.6.2 TA validation requirements 3355.6.6.3
TA validation requirements when configured with validity area 3365.6.7
Measurement requirements for DL RSCPD reported with RSTD 3375.6.7.1
Introduction 3375.6.7.2 Requirements Applicability 3375.6.7.3
Measurement Capability 3375.6.7.4 Measurement Reporting Requirements
3375.6.7.5 Measurements Period Requirements 3375.6.8 Measurement
requirements for DL RSCP reported with UE Rx-Tx time difference
3405.6.8.1 Introduction 3405.6.8.2 Requirements Applicability 3405.6.8.3
Measurement Capability 3405.6.8.4 Measurement Reporting Requirements
3405.6.8.5 Measurement Period Requirements 3415.6A NR measurements for
positioning for RedCap 3435.6A.1 Introduction 3435.6A.2 Cell
re-selection for positioning 3445.6A.2.1 Measurement and evaluation of
serving cell 3445.6A.2.2 Measurements of intra-frequency NR cells
3455.6A.3 TA validation requirements for positioning SRS 3465.6A.3.1
Introduction 3465.6A.3.2 TA validation requirements 3465.6A.3.3 TA
validation requirements when configured with validity area 3465.6A.4
RSTD measurements for RedCap 3465.6A.4.1 Introduction 3465.6A.4.2
Requirements applicability 3465.6A.4.3 Measurement Capability
3475.6A.4.4 Measurement Reporting Requirements 3475.6A.4.5 Measurement
Period Requirement without RX FH 3475.6A.4.6 Measurement Period
Requirement with RX FH 3515.6A.5 PRS-RSRP measurements for RedCap
3525.6A.5.1 Introduction 3525.6A.5.2 Requirements applicability
3535.6A.5.3 Measurement Capability 3535.6A.5.4 Measurement Reporting
Requirements 3535.6A.5.5 Measurement Period Requirements without RX FH
3545.6A.5.6 Measurement Period Requirement with RX FH 3565.6A.6 UE Rx-Tx
time difference measurements for RedCap 3585.6A.6.1 Introduction
3585.6A.6.2 Requirements Applicability 3585.6A.6.3 Measurement
Capability 3595.6A.6.4 Measurement Reporting Requirements 3595.6A.6.5
Measurement Period Requirements without RX FH 3595.6A.6.6 Measurement
Period Requirements with RX FH 3605.6A.7 PRS-RSRPP measurements for
RedCap 3625.6A.7.1 Introduction 3625.6A.7.2 Requirements applicability
3625.6A.7.3 Measurement Capability 3625.6A.7.4 Measurement Reporting
Requirements 3625.6A.7.5 Measurement Period Requirements without FH
3635.6A.7.6 Measurement period requirement with FH 3635.7 Random access
based Small Data Transmissions (RA-SDT) 3635.7.1 Introduction 3635.7.2
Requirements for small data transmissions based on 2-step RA 3635.7.3
Requirements for small data transmissions based on 4-step RA 3635.7.4
Applicability conditions for SDT 3635.7B Random access based Small Data
Transmissions (RA-SDT) for RedCap 3645.7B.1 Introduction 3645.7B.2
Requirements for small data transmissions based on 2-step RA 3645.7B.3
Requirements for small data transmissions based on 4-step RA 3645.7B.4
Applicability conditions for RA-SDT for RedCap 3645.7D Random access
based Small Data Transmissions (RA-SDT) for ATG 3645.8 Measurement
report for fast CA/DC setup 3645.8.1 Introduction 3645.8.2 Void 3655.8.3
Measurement Report Requirements 3656 RRC\_CONNECTED state mobility
3656.1 Handover 3656.1.1 NR Handover 3656.1.1.1 Introduction 3656.1.1.2
NR FR1 - NR FR1 Handover 3656.1.1.2.1 Handover delay 3656.1.1.2.2
Interruption time 3656.1.1.3 NR FR2- NR FR1 Handover 3676.1.1.3.1
Handover delay 3676.1.1.3.2 Interruption time 3676.1.1.4 NR FR2- NR FR2
Handover 3686.1.1.4.1 Handover delay 3686.1.1.4.2 Interruption time
3686.1.1.5 NR FR1- NR FR2 Handover 3696.1.1.5.1 Handover delay
3696.1.1.5.2 Interruption time 3696.1.2 NR Handover to other RATs
3716.1.2.1 NR -- E-UTRAN Handover 3716.1.2.1.1 Introduction 3716.1.2.1.2
Handover delay 3716.1.2.1.3 Interruption time 3716.1.2.2 NR -- UTRAN
Handover 3716.1.2.2.1 Introduction 3716.1.2.2.2 Handover delay
3726.1.2.2.3 Interruption time 3726.1.3 NR DAPS Handover 3726.1.3.1
Introduction 3726.1.3.2 NR FR1 - NR FR1 DAPS Handover 3736.1.3.2.1 DAPS
handover delay 3736.1.3.2.2 Interruption time 3746.1.3.3 NR FR2- NR FR1
DAPS Handover 3756.1.3.3.1 DAPS handover delay 3766.1.3.3.2 Interruption
time 3766.1.3.4 NR FR1- NR FR2 DAPS Handover 3766.1.3.4.1 DAPS handover
delay 3776.1.3.4.2 Interruption time 3776.1.4 NR Conditional Handover
3786.1.4.1 Introduction 3786.1.4.2 NR FR1 -- NR FR1 conditional handover
3786.1.4.2.2 Measurement time 3786.1.4.3 NR FR2 -- NR FR1 conditional
handover 3806.1.4.4 NR FR2 -- NR FR2 conditional handover 3806.1.4.4.1
Handover delay 3806.1.4.4.2 Measurement time 3816.1.4.4.3 Preparation
time 3826.1.4.4.4 Interruption time 3826.1.4.5 NR FR1 -- NR FR2
conditional handover 3826.1.5 NR Handover with PSCell 3826.1.5.1
Introduction 3826.1.5.2 Handover with PSCell from NR SA to EN-DC
3836.1.5.2.1 Interruption time for inter-RAT HO from NR to E-UTRAN
3836.1.5.2.2 PSCell addition in HO with PSCell for NR SA to EN-DC
3836.1.5.3 HO with PSCell from NE-DC to NE-DC 3846.1.5.3.1 Handover
delay 3846.1.5.3.2 HO with PSCell - PCell Interruption time 3846.1.5.3.3
PSCell addition/change in NE-DC to NE-DC HO with PSCell 3846.1.5.4 HO
with PSCell from NR-DC to NR-DC 3856.1.5.5 Handover with PSCell from NR
SA to EN-DC with PSCell using CCA 3866.1.5.5.1 Introduction 3866.1.5.5.2
NR SA to EN-DC HO with PSCell- NR to E-UTRA HO Interruption time
3866.1.5.5.3 NR SA to EN-DC HO with PSCell - NR PSCell Addition Delay
requirements 3876.1.6.1 Conditional handover including target MCG in FR1
and target SCG in FR1 in NR-DC 3886.1.6.1.1 CHO with PSCell -- PCell
Interruption time 3886.1.6.1.2 CHO with PSCell -- PSCell change delay
3896.1.6.2 Conditional handover including target MCG in FR1 and target
SCG in FR2 in NR-DC 3896.1.6.2.2 CHO with PSCell -- PSCell change delay
3906.1.7.1.2 PSCell conditional change delay 3936.1.7.2 Conditional
handover including target MCG in FR1 and Candidate SCG for CPC in FR2 in
NR-DC 3946.1.7.2.1 PCell handover delay 3946.1.7.2.1.1 Measurement time
3956.1.7.2.2 PSCell conditional change delay 3956.1A Void 3976.1A.1 Void
3976.1A.1.1 Void 3976.1A.1.2 Void 3976.1A.1.2.1 Void 3976.1A.1.2.2 Void
3976.1B Handover to target cell using CCA 3976.1B.1 NR Handover
3976.1B.1.1 Introduction 3976.1B.1.2 NR FR1 - NR FR1 Handover
3976.1B.1.2.1 Handover delay 3976.1B.1.2.2 Interruption time 3976.1B.1.3
NR FR2-2 NR FR2-2 Handover 3986.1B.1.3.1 Handover delay 3986.1B.1.3.2
Interruption time 3986.1B.1.4 NR FR1- NR FR2-2 Handover 3996.1B.1.4.1
Handover delay 3996.1B.1.4.2 Interruption time 4006.1C Handover for SAN
4016.1C.1 NR SAN Handover 4016.1C.1.1 Introduction 4016.1C.1.2 NR SAN
FR1 -- NR SAN FR1 Handover 4016.1C.1.2.1 Handover delay 4016.1C.1.2.2
Interruption time 4016.1C.1.3 NR SAN FR2-NTN -- NR SAN FR2-NTN Handover
4026.1C.1.3.1 Handover delay 4026.1C.1.3.2 Interruption time 4036.1C.2
NR SAN Conditional Handover 4036.1C.2.1 Introduction 4036.1C.2.2 NR SAN
FR1 -- NR SAN FR1 conditional handover 4036.1C.2.2.1 Handover delay
4046.1C.2.2.2 Measurement time 4046.1C.2.2.3 Preparation time
4056.1C.2.2.4 Interruption time 4056.1C.2.3 NR SAN FR1 -- NR SAN FR1
conditional handover without L3 measurement criteria 4066.1C.2.3.1
Handover delay 4066.1C.2.3.2 Preparation time 4076.1C.2.3.3 Interruption
time 4076.1C.2.4 NR SAN FR2-NTN -- NR SAN FR2-NTN conditional handover
4076.1C.3 NR SAN Satellite switching with re-synchronization 4086.1C.3.1
Introduction 4086.1C.3.2 NR SAN FR1 -- NR SAN FR1 Satellite switching
with re-synchronization 4086.1C.3.2.1 Satellite switching delay
4086.1C.3.2.2 Interruption time for hard satellite switch with re-sync
4086.1D Handover for RedCap 4096.1D.1 NR Handover 4096.1D.1.1
Introduction 4096.1D.1.2 NR FR1 - NR FR1 Handover 4106.1D.1.2.1 Handover
delay 4106.1D.1.2.2 Interruption time 4106.1D.1.3 NR FR2- NR FR2
Handover 4116.1D.1.3.1 Handover delay 4116.1D.1.3.2 Interruption time
4126.1D.2 NR Handover to other RATs 4136.1D.2.1 NR -- E-UTRAN Handover
4136.1E Handover for ATG 4136.1E.1 NR Handover 4136.1E.1.1 Introduction
4136.1E.1.2 NR FR1 - NR FR1 Handover 4136.1E.1.2.1 Handover delay
4136.1E.1.2.2 Interruption time 4136.1E.2 NR Conditional Handover
4146.1E.2.1 Introduction 4146.1E.2.2 NR FR1 -- NR FR1 conditional
handover 4146.1E.2.2.1 Handover delay 4146.1E.2.2.2 Measurement time
4156.1E.2.2.3 Preparation time 4156.1E.2.2.4 Interruption time 4166.2
RRC Connection Mobility Control 4166.2.1 SA: RRC Re-establishment
4166.2.1.1 Introduction 4166.2.1.2 Requirements 4166.2.1.2.1 UE
Re-establishment delay requirement 4166.2.1A RRC Re-establishment with
CCA 4186.2.1A.1 Introduction 4186.2.1A.2 Requirements 4186.2.1A.2.1 UE
Re-establishment with CCA delay requirement 4186.2.1B SA: RRC
Re-establishment for RedCap 4206.2.1B.1 Introduction 4206.2.1B.2
Requirements 4206.2.2 Random access 4216.2.2.1 Introduction 4216.2.2.2
Requirements for 4-step RA type 4216.2.2.2.1 Contention based random
access 4216.2.2.2.1.1 Correct behaviour when transmitting Random Access
Preamble 4216.2.2.2.1.2 Correct behaviour when receiving Random Access
Response 4226.2.2.2.1.3 Correct behaviour when not receiving Random
Access Response 4226.2.2.2.1.4 Correct behaviour when receiving an UL
grant for msg3 retransmission 4226.2.2.2.1.5 SA: Correct behaviour when
receiving a message over Temporary C-RNTI 4226.2.2.2.1.6 Correct
behaviour when contention Resolution timer expires 4226.2.2.2.2
Non-Contention based random access 4226.2.2.2.2.1 Correct behaviour when
transmitting Random Access Preamble 4226.2.2.2.2.2 Correct behaviour
when receiving Random Access Response 4236.2.2.2.2.3 Correct behaviour
when not receiving Random Access Response 4236.2.2.2.3 UE behaviour when
configured with supplementary UL 4236.2.2.3 Requirements for 2-step RA
type 4236.2.2.3.1 Contention based random access 4246.2.2.3.1.1 Correct
behaviour when transmitting MsgA 4246.2.2.3.1.2 Correct behaviour when
receiving MsgB 4246.2.2.3.1.3 Correct behaviour when not receiving MsgB
4246.2.2.3.2 Non-Contention based random access 4246.2.2.3.2.1 Correct
behaviour when transmitting MsgA 4246.2.2.3.2.2 Correct behaviour when
receiving MsgB 4256.2.2.3.2.3 Correct behaviour when not receiving MsgB
4256.2.2.3.3 UE behaviour when configured with supplementary UL
4256.2.2A Random access when CCA is used on target frequency 4256.2.2A.1
Introduction 4256.2.2A.2 Requirements for 4-step RA type 4256.2.2A.2.1
Contention based random access 4266.2.2A.2.1.1 Correct behaviour when
transmitting Random Access Preamble 4266.2.2A.2.1.2 Correct behaviour
when receiving Random Access Response 4266.2.2A.2.1.3 Correct behaviour
when not receiving Random Access Response 4266.2.2A.2.1.4 Correct
behaviour when receiving an UL grant for msg3 retransmission
4266.2.2A.2.1.6 Correct behaviour when contention Resolution timer
expires 4276.2.2A.2.2 Non-Contention based random access 4276.2.2A.2.2.1
Correct behaviour when transmitting Random Access Preamble
4276.2.2A.2.2.2 Correct behaviour when receiving Random Access Response
4276.2.2A.2.2.3 Correct behaviour when not receiving Random Access
Response 4286.2.2A.3 Requirements for 2-step RA type 4286.2.2A.3.1
Contention based random access 4286.2.2A.3.1.1 Correct behaviour when
transmitting MsgA 4286.2.2A.3.1.2 Correct behaviour when receiving MsgB
4296.2.2A.3.1.3 Correct behaviour when not receiving MsgB 4296.2.2A.3.2
Non-Contention based random access 4296.2.2A.3.2.1 Correct behaviour
when transmitting MsgA 4296.2.2A.3.2.2 Correct behaviour when receiving
MsgB 4306.2.2A.3.2.3 Correct behaviour when not receiving MsgB 4306.2.2B
Random access for RedCap 4306.2.2B.1 Introduction 4306.2.2B.2
Requirements 4306.2.2C PDCCH ordered Random Access for LTM 4316.2.2C.1
Introduction 4316.2.2C.2 PDCCH ordered Random Access delay 4316.2.3 SA:
RRC Connection Release with Redirection 4326.2.3.1 Introduction
4326.2.3.2 Requirements 4326.2.3.2.1 RRC connection release with
redirection to NR 4326.2.3.2.2 RRC connection release with redirection
to E-UTRAN 4336.2.3.2.3 RRC connection release with redirection to NR
carrier subject to CCA 4336.2.3A SA: RRC Connection Release with
Redirection for RedCap 4346.2.3A.1 Introduction 4346.2.3A.2 Requirements
4356.2.3A.2.1 RRC connection release with redirection to NR
4356.2.3A.2.2 RRC connection release with redirection to E-UTRAN 4356.2C
RRC Connection Mobility Control for Satellite Access 4356.2C.1 SA: RRC
Re-establishment for Satellite Access 4356.2C.1.1 Introduction
4356.2C.1.2 Requirements 4356.2C.1.2.1 UE Re-establishment delay
requirement 4366.2C.1.2.2 UE Re-establishment delay requirement for VSAT
4376.2C.2 Random access for satellite access 4376.2C.2.1 Introduction
4376.2C.2.2 Requirements for 4-step RA type 4376.2C.2.2.1 Contention
based random access 4386.2C.2.2.1.1 Correct behaviour when transmitting
Random Access Preamble 4386.2C.2.2.1.2 Correct behaviour when receiving
Random Access Response 4386.2C.2.2.1.3 Correct behaviour when not
receiving Random Access Response 4386.2C.2.2.1.4 Correct behaviour when
receiving an UL grant for msg3 retransmission 4386.2C.2.2.1.5 SA:
Correct behaviour when receiving a message over Temporary C-RNTI
4386.2C.2.2.1.6 Correct behaviour when Contention Resolution Timer
expires 4386.2C.2.2.2 Non-Contention based random access 4396.2C.2.2.2.1
Correct behaviour when transmitting Random Access Preamble
4396.2C.2.2.2.2 Correct behaviour when receiving Random Access Response
4396.2C.2.2.2.3 Correct behaviour when not receiving Random Access
Response 4396.2C.2.3 Requirements for 2-step RA type 4406.2C.2.3.1
Contention based random access 4406.2C.2.3.1.1 Correct behaviour when
transmitting MsgA 4406.2C.2.3.1.2 Correct behaviour when receiving MsgB
4406.2C.2.3.1.3 Correct behaviour when not receiving MsgB 4416.2C.2.3.2
Non-Contention based random access 4416.2C.2.3.2.1 Correct behaviour
when transmitting MsgA 4416.2C.2.3.2.2 Correct behaviour when receiving
MsgB 4416.2C.2.3.2.3 Correct behaviour when not receiving MsgB 4416.2C.3
SA: RRC Connection Release with Redirection for Satellite Access
4416.2C.3.1 Introduction 4416.2C.3.2 Requirements 4416.2C.3.2.1 RRC
connection release with redirection to NR 4416.2D RRC Connection
Mobility Control for ATG 4426.2D.1 SA: RRC Re-establishment 4426.2D.1.1
Introduction 4426.2D.1.2 Requirements 4436.2D.1.2.1 UE Re-establishment
delay requirement 4436.2D.2 Random access 4446.2D.2.1 Introduction
4446.2D.2.2 Requirements for 4-step RA type 4446.2D.2.3 Requirements for
2-step RA type 4446.2D.3 SA: RRC Connection Release with Redirection
4446.2D.3.1 Introduction 4446.2D.3.2 Requirements 4456.2D.3.2.1 RRC
connection release with redirection to NR 4456.3 L1/L2-Triggered
Mobility 4456.3.1 LTM PCell Cell Switch 4456.3.1.1 Introduction
4456.3.1.2 LTM Cell Switch delay 4476.3.1.3 Interruption time 4477
Timing 4497.1 UE transmit timing 4497.1.1 Introduction 4497.1.2
Requirements 4507.1.2.1 Gradual timing adjustment 4527.1.2.2 Void
4527.1.2.3 One shot large UL timing adjustment for FR2 Power Class 6 UE
4527.1.2.4 UE transmit timing for positioning measurements 4537.1A UE
transmit timing for RedCap 4537.1A.1 Introduction 4537.1A.2 Requirements
4547.1A.2.1 Gradual timing adjustment 4557.1A.2.2 UE transmit timing for
positioning measurements 4557.1C UE transmit timing for Satellite Access
4557.1C.1 Introduction 4557.1C.2 Requirements 4557.1C.2.1 Gradual timing
adjustment 4577.1D UE transmit timing for ATG 4577.1D.1 Introduction
4577.1D.2 Requirements 4577.1D.2.1 Gradual timing adjustment 4587.2 UE
timer accuracy 4597.2.1 Introduction 4597.2.2 Requirements 4597.2A UE
timer accuracy for RedCap 4597.2A.1 Introduction 4597.2A.2 Requirements
4597.2C UE timer accuracy for satellite access 4597.2C.1 Introduction
4597.2C.2 Requirements 4607.2D UE timer accuracy for ATG 4607.2D.1
Introduction 4607.2D.2 Requirements 4607.3 Timing advance 4607.3.1
Introduction 4607.3.2 Requirements 4617.3.2.1 Timing Advance adjustment
delay 4617.3.2.2 Timing Advance adjustment accuracy 4617.3A Timing
Advance for RedCap 4617.3A.1 Introduction 4617.3A.2 Requirements
4617.3A.2.1 Timing Advance adjustment delay 4617.3A.2.2 Timing Advance
adjustment accuracy 4617.3C Timing advance for satellite access
4617.3C.1 Introduction 4617.3C.2 Requirements 4627.3C.2.1 Timing Advance
adjustment delay 4627.3C.2.2 Timing Advance adjustment accuracy 4627.3D
Timing advance for ATG 4627.3D.1 Introduction 4627.3D.2 Requirements
4627.3D.2.1 Timing Advance adjustment delay 4627.3D.2.2 Timing Advance
adjustment accuracy 4627.4 Cell phase synchronization accuracy 4637.4.1
Definition 4637.4.2 Minimum requirements 4637.5 Maximum Transmission
Timing Difference 4637.5.1 Introduction 4637.5.2 Minimum requirements
for inter-band EN-DC 4637.5.2.1 Minimum requirements for inter-band
synchronous EN-DC 4647.5.3 Minimum requirements for intra-band EN-DC
4647.5.4 Minimum requirements for NR Carrier Aggregation 4657.5.5
Minimum requirements for inter-band NE-DC 4657.5.5.1 Minimum
requirements for inter-band synchronous NE-DC 4667.5.6 Minimum
requirements for inter-band NR-DC 4667.5.7 Minimum requirements for
multi-TRP 4677.6 Maximum Receive Timing Difference 4677.6.1 Introduction
4677.6.2 Minimum requirements for inter-band EN-DC 4687.6.2.1 Minimum
requirements for inter-band synchronous EN-DC 4687.6.3 Minimum
requirements for intra-band EN-DC 4697.6.4 Minimum requirements for NR
Carrier Aggregation 4697.6.5 Minimum requirements for inter-band NE-DC
4707.6.5.1 Minimum requirements for inter-band synchronous NE-DC
4707.6.6 Minimum requirements for inter-band NR-DC 4717.6.7 Minimum
requirements for PC6 UE in FR2 4727.6.8 Minimum requirements for
Multi-TRPs 4727.7 *deriveSSB-IndexFromCell* tolerance 4737.7.1 Minimum
requirements 4737.7A deriveSSB-IndexFromCell tolerance for RedCap
4737.7A.1 Minimum requirements 4737.7D DeriveSSB-IndexFromCell tolerance
for ATG 4737.7D.1 Minimum requirements 4737.8 Void 4747.9
*deriveSSB-IndexFromCellInter-r17* tolerance 4747.9.1 Minimum
requirements 4747.9D *DeriveSSB-IndexFromCellInter-r17* tolerance for
ATG 4747.9D.1 Minimum requirements 4748 Signalling characteristics
4768.1 Radio Link Monitoring 4768.1.1 Introduction 4768.1.1.1
Introduction of Requirement on Radio Link Monitoring for UE Configured
with Relaxed Measurement Criteria 4778.1.2 Requirements for SSB based
radio link monitoring 4788.1.2.1 Introduction 4788.1.2.2 Minimum
requirement 4798.1.2.3 Measurement restrictions for SSB based RLM
4838.1.2.4 Minimum requirement of SSB based radio link monitoring for UE
fulfilling relaxed measurement criteria 4848.1.3 Requirements for CSI-RS
based radio link monitoring 4858.1.3.1 Introduction 4858.1.3.2 Minimum
requirement 4858.1.3.3 Measurement restrictions for CSI-RS based RLM
4898.1.3.4 Minimum requirement of CSI-RS based radio link monitoring for
UE fulfilling relaxed measurement criteria 4908.1.4 Minimum requirement
at transitions 4918.1.5 Minimum requirement for UE turning off the
transmitter 4928.1.6 Minimum requirement for L1 indication 4928.1.7
Scheduling availability of UE during radio link monitoring 4928.1.7.1
Scheduling availability of UE performing radio link monitoring with a
same subcarrier spacing as PDSCH/PDCCH on FR1 4928.1.7.2 Scheduling
availability of UE performing radio link monitoring with a different
subcarrier spacing than PDSCH/PDCCH on FR1 4928.1.7.3 Scheduling
availability of UE performing radio link monitoring on FR2 4938.1.7.4
Scheduling availability of UE performing radio link monitoring on FR1 or
FR2 in case of FR1-FR2 inter-band CA and NR-DC 4948.1.8 Minimum
requirement under IDC Interference 4948.1A Radio Link Monitoring with
CCA on Target Frequency 4948.1A.1 Introduction 4948.1A.2 Requirements
for SSB Based Radio Link Monitoring 4958.1A.2.1 Introduction 4958.1A.2.2
Minimum Requirement 4968.1A.3 Minimum requirement at transitions
4998.1A.4 Minimum requirement for UE turning off the transmitter
4998.1A.5 Minimum requirement for L1 indication 4998.1A.6 Scheduling
availability of UE during radio link monitoring 5008.1A.6.3 Scheduling
availability of UE performing radio link monitoring on FR2-2 5008.1A.6.4
Scheduling availability of UE performing radio link monitoring on FR1 or
FR2-2 in case of FR1-FR2-2 inter-band CA and NR-DC 5018.1B Radio Link
Monitoring for RedCap 5018.1B.1 Introduction 5018.1B.2 Requirements for
SSB based radio link monitoring 5028.1B.2.1 Introduction 5028.1B.2.2
Minimum requirement 5028.1B.2.3 Measurement restrictions for SSB based
RLM 5048.1B.3 Requirements for CSI-RS based radio link monitoring
5058.1B.3.1 Introduction 5058.1B.3.2 Minimum requirement 5058.1B.3.3
Measurement restrictions for CSI-RS based RLM 5088.1B.4 Minimum
requirement at transitions 5088.1B.5 Minimum requirement for UE turning
off the transmitter 5098.1B.6 Minimum requirement for L1 indication
5098.1B.7 Scheduling availability of UE during radio link monitoring
5098.1B.7.1 Scheduling availability of UE performing radio link
monitoring with a same subcarrier spacing as PDSCH/PDCCH on FR1
5098.1B.7.2 Scheduling availability of UE performing radio link
monitoring with a different subcarrier spacing than PDSCH/PDCCH on FR1
5098.1B.7.3 Scheduling availability of UE performing radio link
monitoring on FR2 5108.1C Radio Link Monitoring for Satellite Access
5108.1C.1 Introduction 5108.1C.2 Requirements for SSB based radio link
monitoring 5118.1C.2.1 Introduction 5118.1C.2.2 Minimum requirement
5128.1C.2.3 Measurement restrictions for SSB based RLM 5138.1C.3
Requirements for CSI-RS based radio link monitoring 5138.1C.3.1
Introduction 5138.1C.3.2 Minimum requirement 5148.1C.3.3 Measurement
restrictions for CSI-RS based RLM 5158.1C.4 Minimum requirement at
transitions 5168.1C.5 Minimum requirement for UE turning off the
transmitter 5168.1C.6 Minimum requirement for L1 indication 5168.1C.7
Scheduling availability of UE during radio link monitoring 5178.1C.7.1
Scheduling availability of UE performing radio link monitoring with a
same subcarrier spacing as PDSCH/PDCCH on FR1 and FR2-NTN 5178.1C.7.2
Scheduling availability of UE performing radio link monitoring with a
different subcarrier spacing than PDSCH/PDCCH on FR1 and FR2-NTN 5178.1D
Radio Link Monitoring for ATG 5178.1D.1 Introduction 5178.1D.2
Requirements for SSB based radio link monitoring 5188.1D.2.1
Introduction 5188.1D.2.2 Minimum requirement 5188.1D.2.3 Measurement
restrictions for SSB based RLM 5198.1D.3 Requirements for CSI-RS based
radio link monitoring 5208.1D.3.1 Introduction 5208.1D.3.2 Minimum
requirement 5208.1D.3.3 Measurement restrictions for CSI-RS based RLM
5218.1D.4 Minimum requirement at transitions 5218.1D.5 Minimum
requirement for UE turning off the transmitter 5218.1D.6 Minimum
requirement for L1 indication 5218.1D.7 Scheduling availability of UE
during radio link monitoring 5228.1D.7.1 Scheduling availability of UE
performing radio link monitoring with a same subcarrier spacing as
PDSCH/PDCCH on FR1 5228.1D.7.2 Scheduling availability of UE performing
radio link monitoring with a different subcarrier spacing than
PDSCH/PDCCH on FR1 5228.2 Interruption 5228.2.1 EN-DC Interruption
5228.2.1.1 Introduction 5228.2.1.2 Requirements 5238.2.1.2.1
Interruptions at transitions between active and non-active during DRX
5238.2.1.2.2 Interruptions at transitions from non-DRX to DRX
5238.2.1.2.3 Interruptions at SCell addition/release 5238.2.1.2.4
Interruptions at SCell activation/deactivation 5258.2.1.2.5
Interruptions during measurements on SCC 5278.2.1.2.5.1 Interruptions
during measurements on deactivated NR SCC 5278.2.1.2.5.2 Interruptions
during measurements on deactivated E-UTRAN SCC 5278.2.1.2.5.3
Interruptions during CQI measurements on dormant E-UTRAN SCell
5278.2.1.2.5.4 Interruptions during RRM measurements on dormant E-UTRAN
SCC 5288.2.1.2.6 Interruptions at UL carrier RRC reconfiguration
5288.2.1.2.7 Interruptions due to Active BWP switching Requirement
5298.2.1.2.8 Interruptions at direct SCell activation and hibernation
5308.2.1.2.8.1 Interruptions during direct SCell activation and
hibernation of E-UTRA SCell 5308.2.1.2.8.2 Interruptions during direct
SCell activation 5308.2.1.2.9 Interruptions at SCell hibernation
5308.2.1.2.10 Interruptions at SCell activation/deactivation with
multiple downlink SCells 5318.2.1.2.11 Interruptions due to UE-specific
CBW change 5318.2.1.2.12 Interruptions at NR SRS carrier based switching
5318.2.1.2.13 Interruptions at E-UTRA SRS carrier based switching
5338.2.1.2.14 DL Interruptions at switching between two uplink carriers
5348.2.1.2.15 Interruptions due to SCell dormancy 5348.2.1.2.15.1
Interruptions due to SCell dormancy switch 5348.2.1.2.15.2 Interruptions
due to CQI measurements during SCell dormancy 5348.2.1.2.15.3
Interruptions due to RRM measurements during SCell dormancy
5358.2.1.2.16 Interruptions when identifying CGI of an NR cell with
autonomous gaps 5358.2.1.2.17 Interruptions when identifying CGI of an
E-UTRA cell with autonomous gaps 5358.2.1.2.18 Interruptions at NR SRS
antenna port switching 5368.2.1.2.19 Interruptions at fast SCell
activation 5378.2.1.2.20 Interruptions due to PUCCH SCell
activation/deactivation 5378.2.2 SA: Interruptions with Standalone NR
Carrier Aggregation 5388.2.2.1 Introduction 5388.2.2.2 Requirements
5398.2.2.2.1 Interruptions at SCell addition/release 5398.2.2.2.2
Interruptions at SCell activation/deactivation 5408.2.2.2.3
Interruptions during measurements on deactivated SCC 5418.2.2.2.4
Interruptions at UL carrier RRC reconfiguration 5428.2.2.2.5
Interruptions due to Active BWP switching Requirement 5428.2.2.2.6
Interruptions at inter-frequency SFTD measurement 5438.2.2.2.7
Interruptions at SCell activation/deactivation with multiple downlink
SCells 5448.2.2.2.8 Interruptions due to UE-specific CBW change
5458.2.2.2.9 Interruptions at NR SRS carrier based switching
5458.2.2.2.10 DL Interruptions at UE switching between two uplink
carriers 5468.2.2.2.10A DL Interruptions at UE switching between two
uplink carriers with two transmit antenna connectors 5478.2.2.2.10B DL
Interruptions at UE switching between one uplink band with one transmit
antenna connector and one uplink band with two transmit antenna
connectors 5478.2.2.2.10C DL Interruptions at UE switching between two
uplink bands with two transmit antenna connectors 5488.2.2.2.10D DL
Interruptions at UE switching across three or four uplink bands
5488.2.2.2.11 Interruptions at direct SCell activation 5498.2.2.2.12
Interruptions due to SCell dormancy 5498.2.2.2.12.1 Interruptions due to
SCell dormancy switch 5498.2.2.2.12.2 Interruptions due to CQI
measurements during SCell dormancy 5498.2.2.2.12.3 Interruptions due to
RRM measurements during SCell dormancy 5508.2.2.2.13 Interruptions at
transitions between active and non-active during DRX 5508.2.2.2.14
Interruptions when identifying CGI of an NR cell with autonomous gaps
5508.2.2.2.15 Interruptions when identifying CGI of an E-UTRA cell with
autonomous gaps 5508.2.2.2.16 Interruptions at NR SRS antenna port
switching 5518.2.2.2.17 Interruptions at fast SCell activation
5528.2.2.2.18 Interruptions due to PUCCH SCell activation/deactivation
5528.2.2.2.19 Interruptions due to measurements without gap carried out
by UE supporting *NeedForInterruptionInfoNR* 5538.2.2.2.20 Interruptions
due to PDCCH ordered RACH on target LTM cell 5548.2.2.2.21 Interruptions
at NR SRS bandwidth aggregation for positioning 5548.2.3 NE-DC
Interruptions 5568.2.3.1 Introduction 5568.2.3.2 Requirements
5578.2.3.2.1 Interruptions at transitions between active and non-active
during DRX 5578.2.3.2.2 Interruptions at transitions from non-DRX to DRX
5578.2.3.2.3 Interruptions at PSCell/SCell addition/release 5578.2.3.2.4
Interruptions at SCell activation/deactivation 5588.2.3.2.5
Interruptions during measurements on SCC 5598.2.3.2.5.1 Interruptions
during measurements on deactivated NR SCC 5598.2.3.2.5.2 Interruptions
during measurements on deactivated E-UTRAN SCC 5598.2.3.2.5.3
Interruptions during CQI measurements on dormant E-UTRAN SCC
5608.2.3.2.5.4 Interruptions during RRM measurements on dormant E-UTRAN
SCC 5608.2.3.2.6 Interruptions at UL carrier RRC reconfiguration
5608.2.3.2.7 Interruptions due to Active BWP switching Requirement
5618.2.3.2.8 Interruptions at direct SCell activation and hibernation
5618.2.3.2.9 Interruptions at SCell hibernation 5618.2.3.2.10
Interruptions at SCell activation/deactivation with multiple downlink
SCells 5628.2.3.2.11 Interruptions at NR SRS carrier based switching
5628.2.3.2.12 Interruptions at E-UTRA SRS carrier based switching
5638.2.3.2.13 Interruptions due to SCell dormancy 5648.2.3.2.14
Interruptions when identifying CGI of an NR cell with autonomous gaps
5648.2.3.2.15 Interruptions when identifying CGI of an E-UTRA cell with
autonomous gaps 5658.2.3.2.17 Interruptions at fast SCell activation
5678.2.3.2.18 Interruptions due to UE-specific CBW change 5678.2.3.2.19
Interruptions due to PUCCH SCell activation/deactivation 5678.2.4 NR-DC:
Interruptions 5688.2.4.1 Introduction 5688.2.4.2 Requirements
5688.2.4.2.1 Interruptions at PSCell/SCell addition/release 5688.2.4.2.2
Interruptions at SCell activation/deactivation 5698.2.4.2.3
Interruptions during measurements on SCC 5708.2.4.2.4 Interruptions at
UL carrier RRC reconfiguration 5708.2.4.2.5 Interruptions due to Active
BWP switching Requirement 5718.2.4.2.6 Interruptions at transitions
between active and non-active during DRX 5718.2.4.2.7 Interruptions at
transitions from non-DRX to DRX 5718.2.4.2.8 Interruptions at SCell
activation/deactivation with multiple downlink SCells 5728.2.4.2.9
Interruptions at NR SRS carrier based switching 5728.2.4.2.10
Interruptions at direct SCell activation 5738.2.4.2.11 Interruptions
when identifying CGI of an NR cell with autonomous gaps 5748.2.4.2.12
Interruptions when identifying CGI of an E-UTRA cell with autonomous
gaps 5748.2.4.2.13 Interruptions due to SCell dormancy 5758.2.4.2.14
Interruptions at NR SRS antenna port switching 5758.2.4.2.15
Interruptions at fast SCell activation 5768.2.4.2.16 Interruptions at
SCG activation/deactivation 5778.2.4.2.17 Interruptions due to RRM
measurements on deactivated SCG 5778.2.4.2.18 Interruptions during
RLM/BFD measurements on deactivated PSCell 5778.2.4.2.19 Interruptions
due to UE-specific CBW change 5778.2.4.2.20 Interruptions due to PDCCH
ordered RACH on target LTM cell 5788.2.4.2.21 Interruptions at PSCell
Cell switch 5788.2.4.2A Void 5798.2.4.2A.1 Void 5798.2.4.2A.2 Void
5798.2.4.2A.3 Void 5798.3 SCell Activation and Deactivation Delay
5798.3.1 Introduction 5798.3.2 SCell Activation Delay Requirement for
Deactivated SCell 5798.3.3 SCell Deactivation Delay Requirement for
Activated SCell 5868.3.4 Direct SCell Activation at SCell addition
5868.3.5 Direct SCell Activation at Handover 5888.3.7 SCell Activation
Delay Requirement for Deactivated SCell with Multiple Downlink SCells
5908.3.8 SCell Deactivation Delay Requirement for Activated SCell with
Multiple Downlink SCells 5948.3.9 Direct SCell Activation of Multiple
Downlink SCells at SCell addition 5948.3.10 Direct SCell Activation of
Multiple Downlink SCells at Handover 5968.3.12 SCell Activation Delay
Requirement for Deactivated PUCCH SCell 5978.3.13 SCell activation delay
Requirement for Deactivated PUCCH SCell with Multiple SCells 6008.3.14
SCell Deactivation Delay Requirement for Activated PUCCH SCell 6038.3.15
SCell Deactivation Delay Requirement for Activated PUCCH SCell with
Multiple Downlink SCells 6038.3.16 Fast SCell Activation Delay
Requirement for Deactivated SCell 6038.3.17 SCell Activation Delay
Requirement for Deactivated SCell with the L3 reporting during
activation 6068.3.18 SCell Activation Delay Requirement for Deactivated
SCell with Multiple Downlink SCells with L3 reporting 6098.3A SCell
Activation and Deactivation Delay in Carriers with CCA 6128.3A.1
Introduction 6128.3A.2 SCell Activation Delay Requirement for
Deactivated SCell 6128.3A.3 SCell Deactivation Delay Requirement for
Activated SCell 6178.4 UE UL carrier RRC reconfiguration delay 6178.4.1
Introduction 6178.4.2 UE UL carrier configuration delay requirement
6178.4.3 UE UL carrier deconfiguration delay requirement 6188.5 Link
Recovery Procedures 6188.5.1 Introduction 6188.5.1.1 Introduction of
Requirement on Link Recovery Procedures for UE configured with relaxed
measurement criteria 6198.5.2 Requirements for SSB based beam failure
detection 6208.5.2.1 Introduction 6208.5.2.2 Minimum requirement
6218.5.2.3 Measurement restriction for SSB based beam failure detection
6248.5.2.4 Minimum requirement of SSB based beam failure detection for
UE fulfilling relaxed measurement criteria 6258.5.3 Requirements for
CSI-RS based beam failure detection 6268.5.3.1 Introduction 6268.5.3.2
Minimum requirement 6268.5.3.3 Measurement restrictions for CSI-RS beam
failure detection 6308.5.3.4 Minimum requirement of CSI-RS based beam
failure detection for UE fulfilling relaxed measurement criteria
6328.5.4 Minimum requirement for L1 indication 6328.5.5 Requirements for
SSB based candidate beam detection 6338.5.5.1 Introduction 6338.5.5.2
Minimum requirement 6338.5.5.3 Measurement restriction for SSB based
candidate beam detection 6368.5.6 Requirements for CSI-RS based
candidate beam detection 6378.5.6.1 Introduction 6378.5.6.2 Minimum
requirement 6378.5.6.3 Measurement restriction for CSI-RS based
candidate beam detection 6418.5.7 Scheduling availability of UE during
beam failure detection 6428.5.7.1 Scheduling availability of UE
performing beam failure detection with a same subcarrier spacing as
PDSCH/PDCCH on FR1 6428.5.7.2 Scheduling availability of UE performing
beam failure detection with a different subcarrier spacing than
PDSCH/PDCCH on FR1 6428.5.7.3 Scheduling availability of UE performing
beam failure detection on FR2 6428.5.7.4 Scheduling availability of UE
performing beam failure detection on FR1 or FR2 in case of FR1-FR2
inter-band CA and NR-DC 6438.5.8 Scheduling availability of UE during
candidate beam detection 6438.5.8.1 Scheduling availability of UE
performing L1-RSRP measurement with a same subcarrier spacing as
PDSCH/PDCCH on FR1 6438.5.8.2 Scheduling availability of UE performing
L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH
on FR1 6448.5.8.3 Scheduling availability of UE performing L1-RSRP
measurement on FR2 6448.5.8.4 Scheduling availability of UE performing
L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA and
NR-DC 6458.5.9 Requirements for Beam Failure Recovery in SCell
6458.5.9.1 Introduction 6458.5.9.2 Requirement 6458.5.10 Minimum
requirement at transitions for beam failure detection 6458.5.11 Minimum
requirement under IDC Interference 6468.5A Link Recovery Procedures when
CCA is used on target frequency 6468.5A.1 Introduction 6468.5A.2
Requirements for SSB based beam failure detection 6478.5A.2.1
Introduction 6478.5A.2.2 Minimum requirement 6478.5A.2.3 Measurement
restriction for SSB based beam failure detection 6498.5A.3 Void
6508.5A.4 Minimum requirement for L1 indication 6508.5A.5 Requirements
for SSB based candidate beam detection 6508.5A.5.1 Introduction
6508.5A.5.2 Minimum requirement 6508.5A.5.3 Measurement restriction for
SSB based candidate beam detection 6528.5A.6 Void 6538.5A.7 Scheduling
availability of UE during beam failure detection 6538.5A.7.1 Scheduling
availability of UE performing beam failure detection with a same
subcarrier spacing as PDSCH/PDCCH 6538.5A.7.2 Scheduling availability of
UE performing beam failure detection with a different subcarrier spacing
than PDSCH/PDCCH 6538.5A.7.3 Scheduling availability of UE performing
beam failure detection on FR2-2 6538.5A.7.4 Scheduling availability of
UE performing beam failure detection on FR1 or FR2-2 in case of
FR1-FR2-2 inter-band CA and NR-DC 6538.5A.8 Scheduling availability of
UE during candidate beam detection 6538.5A.8.3 Scheduling availability
of UE performing L1-RSRP measurement on FR2-2 6548.5.8A.4 Scheduling
availability of UE performing L1-RSRP measurement on FR1 or FR2-2 in
case of FR1-FR2-2 inter-band CA and NR-DC 6548.5B Link Recovery
Procedures for Redcap 6548.5B.1 Introduction 6548.5B.2 Requirements for
SSB based beam failure detection for Redcap 6548.5B.2.1 Introduction
6548.5B.2.2 Minimum requirement 6558.5B.2.3 Measurement restriction for
SSB based beam failure detection 6568.5B.3 Requirements for CSI-RS based
beam failure detection for Redcap 6578.5B.3.1 Introduction 6578.5B.3.2
Minimum requirement 6578.5B.3.3 Measurement restrictions for CSI-RS beam
failure detection 6598.5B.4 Minimum requirement for L1 indication for
Redcap 6608.5B.5 Requirements for SSB based candidate beam detection for
Redcap 6608.5B.5.1 Introduction 6608.5B.5.2 Minimum requirement
6608.5B.5.3 Measurement restriction for SSB based candidate beam
detection 6628.5B.6 Requirements for CSI-RS based candidate beam
detection for Redcap 6628.5B.6.1 Introduction 6628.5B.6.2 Minimum
requirement 6638.5B.6.3 Measurement restriction for CSI-RS based
candidate beam detection 6658.5B.7 Scheduling availability of UE during
beam failure detection for Redcap 6658.5B.7.1 Scheduling availability of
UE performing beam failure detection with a same subcarrier spacing as
PDSCH/PDCCH on FR1 6658.5B.7.2 Scheduling availability of UE performing
beam failure detection with a different subcarrier spacing than
PDSCH/PDCCH on FR1 6658.5B.7.3 Scheduling availability of UE performing
beam failure detection on FR2 6658.5B.8 Scheduling availability of UE
during candidate beam detection for Redcap 6668.5B.8.1 Scheduling
availability of UE performing L1-RSRP measurement with a same subcarrier
spacing as PDSCH/PDCCH on FR1 6668.5B.8.2 Scheduling availability of UE
performing L1-RSRP measurement with a different subcarrier spacing than
PDSCH/PDCCH on FR1 6668.5B.8.3 Scheduling availability of UE performing
L1-RSRP measurement on FR2 6668.5B.9 Minimum requirement at transitions
for beam failure detection for Redcap 6678.5C Link Recovery Procedures
for Satellite Access 6678.5C.1 Introduction 6678.5C.2 Requirements for
SSB based beam failure detection 6678.5C.2.1 Introduction 6678.5C.2.2
Minimum requirement 6688.5C.2.3 Measurement restriction for SSB based
beam failure detection 6698.5C.3 Requirements for CSI-RS based beam
failure detection 6698.5C.3.1 Introduction 6698.5C.3.2 Minimum
requirement 6698.5C.3.3 Measurement restrictions for CSI-RS beam failure
detection 6708.5C.4 Minimum requirement for L1 indication 6718.5C.5
Requirements for SSB based candidate beam detection 6718.5C.5.1
Introduction 6718.5C.5.2 Minimum requirement 6718.5C.5.3 Measurement
restriction for SSB based candidate beam detection 6728.5C.6
Requirements for CSI-RS based candidate beam detection 6738.5C.6.1
Introduction 6738.5C.6.2 Minimum requirement 6738.5C.6.3 Measurement
restriction for CSI-RS based candidate beam detection 6748.5C.7
Scheduling availability of UE during beam failure detection 6748.5C.7.1
Scheduling availability of UE performing beam failure detection with a
same subcarrier spacing as PDSCH/PDCCH on FR1 6748.5C.7.2 Scheduling
availability of UE performing beam failure detection with a different
subcarrier spacing than PDSCH/PDCCH on FR1 6748.5C.8 Scheduling
availability of UE during candidate beam detection 6748.5C.8.1
Scheduling availability of UE performing L1-RSRP measurement with a same
subcarrier spacing as PDSCH/PDCCH on FR1 6758.5C.8.2 Scheduling
availability of UE performing L1-RSRP measurement with a different
subcarrier spacing than PDSCH/PDCCH on FR1 6758.5C.9 Minimum requirement
at transitions for beam failure detection 6758.5D Link Recovery
Procedures for ATG 6758.5D.1 Introduction 6758.5D.2 Requirements for SSB
based beam failure detection 6768.5D.2.1 Introduction 6768.5D.2.2
Minimum requirement 6768.5D.2.3 Measurement restriction for SSB based
beam failure detection 6778.5D.3 Requirements for CSI-RS based beam
failure detection 6778.5D.3.1 Introduction 6778.5D.3.2 Minimum
requirement 6778.5D.3.3 Measurement restrictions for CSI-RS beam failure
detection 6788.5D.4 Minimum requirement for L1 indication 6798.5D.5
Requirements for SSB based candidate beam detection 6798.5D.5.1
Introduction 6798.5D.5.2 Minimum requirement 6798.5D.5.3 Measurement
restriction for SSB based candidate beam detection 6808.5D.6
Requirements for CSI-RS based candidate beam detection 6808.5D.6.1
Introduction 6808.5D.6.2 Minimum requirement 6808.5D.6.3 Measurement
restriction for CSI-RS based candidate beam detection 6818.5D.7
Scheduling availability of UE during beam failure detection 6818.5D.7.1
Scheduling availability of UE performing beam failure detection with a
same subcarrier spacing as PDSCH/PDCCH on FR1 6828.5D.7.2 Scheduling
availability of UE performing beam failure detection with a different
subcarrier spacing than PDSCH/PDCCH on FR1 6828.5D.8 Scheduling
availability of UE during candidate beam detection 6828.5D.8.1
Scheduling availability of UE performing L1-RSRP measurement with a same
subcarrier spacing as PDSCH/PDCCH on FR1 6828.5D.8.2 Scheduling
availability of UE performing L1-RSRP measurement with a different
subcarrier spacing than PDSCH/PDCCH on FR1 6828.5D.9 Minimum requirement
at transitions for beam failure detection 6828.6 Active BWP switch delay
6828.6.1 Introduction 6828.6.2 DCI and timer based BWP switch delay on a
single CC 6838.6.2A DCI based BWP switch delay on multiple CCs
6848.6.2A.1 Simultaneous DCI based BWP switch delay on multiple CCs
6848.6.2A.2 Non-simultaneous DCI based BWP switch delay on multiple CCs
6868.6.2B Timer based BWP switch delay on multiple CCs 6868.6.2B.1
Simultaneous timer based BWP switch delay on multiple CCs 6868.6.2B.2
Non-simultaneous timer based BWP switch delay on multiple CCs 6868.6.3
RRC based BWP switch delay on a single CC 6878.6.3A RRC based BWP switch
delay on multiple CCs 6888.6.3A.1 Simultaneous RRC based BWP switch
delay on multiple CCs 6888.6.3A.2 Non-simultaneous RRC based BWP switch
delay on multiple CCs 6888.6.4 BWP switch delay on Consistent UL CCA
recovery 6898.6A Active BWP switch delay for RedCap 6898.6A.1
Introduction 6898.6A.2 DCI and timer based BWP switch delay on a single
CC 6898.6A.3 RRC based BWP switch delay on a single CC 6918.6C Active
BWP switch delay for satellite access 6918.6C.1 Introduction 6918.6C.2
DCI and timer based BWP switch delay on a single CC 6918.6C.3 RRC based
BWP switch delay on a single CC 6938.6D Active BWP switch delay for ATG
6938.6D.1 Introduction 6938.6D.2 DCI and timer based BWP switch delay
6938.6D.3 RRC based BWP switch delay on a single CC 6948.7 Void 6958.8
NE-DC: E-UTRAN PSCell Addition and Release Delay 6958.8.1 Introduction
6958.8.2 E-UTRAN PSCell Addition Delay Requirement 6958.8.3 E-UTRAN
PSCell Release Delay Requirement 6958.9 NR-DC: PSCell Addition and
Release Delay 6968.9.1 Introduction 6968.9.2 PSCell Addition Delay
Requirement 6968.9.3 PSCell Release Delay Requirement 6978.9A
Conditional PSCell Addition Delay 6978.9A.1 Introduction 6978.9A.2
Conditional PSCell Addition Delay Requirement 6978.9A.2.1 Measurement
time 6988.9B NR-DC: PSCell Addition and Release Delay in Carriers with
CCA 6988.9B.1 Introduction 6988.9B.2 PSCell Addition Delay Requirement
6988.9B.3 PSCell Release Delay Requirement 6998.9C Subsequent
Conditional PSCell Addition Delay 6998.9C.1 Introduction 6998.9C.2
Subsequent Conditional PSCell Addition Delay Requirement 6998.9C.2.1
Measurement time 7008.10 Active TCI state switching delay 7008.10.3A
MAC-CE based TCI state switch delay in HST FR2 scenarios 7018.10.4 DCI
based TCI state switch delay 7028.10.5 RRC based TCI state switch delay
7028.10.6 Active TCI state list update delay 7038.10A Active TCI state
switching delay with CCA 7038.10A.1 Introduction 7038.10A.2 Known
conditions for TCI state 7038.10A.3 MAC-CE based TCI state switch delay
7038.10A.4 DCI based TCI state switch delay 7048.10A.5 RRC based TCI
state switch delay 7058.10A.6 Active TCI state list update delay
7058.10B Active TCI state switching delay for RedCap 7068.10B.1
Introduction 7068.10B.2 Known conditions for TCI state 7068.10B.3 MAC-CE
based TCI state switch delay 7068.10B.4 DCI based TCI state switch delay
7078.10B.5 RRC based TCI state switch delay 7078.10B.6 Active TCI state
list update delay 7088.10C Active TCI state switching delay for
satellite access 7088.10C.1 Introduction 7088.10C.2 MAC-CE based TCI
state switch delay 7088.10C.4 DCI based TCI state switch delay
7088.10C.5 RRC based TCI state switch delay 7098.10C.6 Active TCI state
list update delay 7098.10D Active TCI state switching delay for ATG
7098.10D.2 Void 7098.10D.6 Active TCI state list update delay 7108.10E
Active TCI state switching delay for UE operating in FR2-1 and
configured with groupBasedBeamReporting-r17 7108.10E.1 Introduction
7108.10E.2 Known conditions for TCI state 7108.10E.3 MAC-CE based dual
DL TCI state switch delay 7118.10E.3.1 MAC-CE based dual DL TCI state
switching delay for sDCI 7118.10E.3.2 MAC-CE based dual DL TCI state
switching delay for mDCI 7118.10E.4 DCI based dual DL TCI state switch
delay for sDCI and mDCI 7118.10E.4.1 DCI based dual DL TCI state
switching delay for sDCI 7118.10E.4.2 DCI based dual DL TCI state
switching delay for mDCI 7128.10E.5 RRC based dual DL TCI state switch
delay 7128.10E.6 Active DL TCI state list update delay 7128.10E.6.1
Active DL TCI state list update delay for sDCI 7128.10E.6.2 Active DL
TCI state list update delay for mDCI 7128.11 PSCell Change 7128.11A
PSCell Change in Carriers with CCA 7138.11B Conditional PSCell Change
7138.11B.1 Introduction 7138.11B.2 Conditional PSCell Change delay
7138.11B.2.1 Measurement time 7148.11D Conditional PSCell Change in
Carriers with CCA 7148.11D.1 Introduction 7148.11D.2 Conditional PSCell
Change delay 7158.11D.2.1 Measurement time 7158.11E Subsequent
Conditional PSCell Change 7168.11E.1 Introduction 7168.11E.2 Subsequent
Conditional PSCell Change delay 7168.11E.2.1 Measurement time 7178.12
Uplink spatial relation switch delay 7178.12.1 Introduction 7178.12.2
Known conditions for spatial relation when associated with DL-RS
7178.12.3 MAC-CE based spatial relation switch delay 7178.12.4 DCI based
spatial relation switch delay 7188.12.5 RRC based spatial relation
switch delay 7188.12A Uplink spatial relation switch delay for RedCap
7198.12A.1 Introduction 7198.12A.2 Known conditions for spatial relation
when associated with DL-RS 7198.12A.3 MAC-CE based spatial relation
switch delay 7198.12A.4 DCI based spatial relation switch delay
7208.12A.5 RRC based spatial relation switch delay 7208.12C Uplink
spatial relation switch delay for satellite access 7218.12C.1 Void
7218.12C.2 Void 7218.12C.3 Void 7218.12C.4 Void 7218.12C.5 Void 7218.13
UE-specific CBW change 7218.13.1 Introduction 7218.13.2 UE-specific CBW
change delay 7218.13A UE-specific CBW change for RedCap 7228.13A.1
Introduction 7228.13A.2 UE-specific CBW change delay 7228.13C
UE-specific CBW change for satellite access 7228.13C.1 Introduction
7228.13C.2 UE-specific CBW change delay 7228.13D UE-specific CBW change
for ATG 7238.13D.1 Introduction 7238.13D.2 UE-specific CBW change delay
7238.14 Pathloss reference signal switching delay 7238.14.1 Introduction
7238.14.2 Known conditions for pathloss reference signal 7238.14.3
MAC-CE based pathloss reference signal switch delay 7248.14C Pathloss
reference signal switching delay for satellite access 7248.14C.1
Introduction 7248.14C.2 Known conditions for pathloss reference signal
7248.14C.3 MAC-CE based pathloss reference signal switch delay 7258.14D
Pathloss reference signal switching delay for ATG 7258.14D.1
Introduction 7258.14D.2 Known conditions for pathloss reference signal
7258.14D.3 MAC-CE based pathloss reference signal switch delay 7258.15
Active downlink TCI state switching delay for unified TCI 7268.15.1
Introduction 7268.15.4 DCI based downlink TCI state switch delay
7278.15.5 Active Downlink TCI state list update delay 7288.15D Active
downlink TCI state switching delay for unified TCI for ATG 7298.15D.1
Introduction 7298.15D.2 Void 7298.15D.4 DCI based downlink TCI state
switch delay 7298.15D.5 Active Downlink TCI state list update delay
7298.16 Active uplink TCI state switching delay for unified TCI
7308.16.1 Introduction 7308.16.4 DCI based uplink TCI state switch delay
7328.16.5 Active Uplink TCI state list update delay 7328.16D Active
uplink TCI state switching delay for unified TCI for ATG 7348.16D.1
Introduction 7348.16D.2 Void 7348.16D.3 MAC-CE based uplink TCI state
switch delay 7348.16D.4 DCI based uplink TCI state switch delay
7358.16D.5 Active Uplink TCI state list update delay 7358.17 SCG
Activation and Deactivation Delay 7368.17.1 Introduction 7368.17.2 SCG
Activation Delay Requirement 7368.17.3 SCG Deactivation Delay
Requirement 7378.18 TRP specific Link Recovery Procedures 7378.18.1
Introduction 7378.18.2 Requirements for TRP specific SSB based beam
failure detection 7388.18.2.1 Introduction 7388.18.2.2 Minimum
requirement 7388.18.2.3 Measurement restriction for SSB based beam
failure detection 7408.18.3 Requirements for CSI-RS based beam failure
detection 7418.18.3.1 Introduction 7418.18.3.2 Minimum requirement
7418.18.3.3 Measurement restrictions for CSI-RS beam failure detection
7458.18.4 Minimum requirement for L1 indication 7468.18.5 Requirements
for SSB based candidate beam detection 7468.18.5.1 Introduction
7468.18.5.2 Minimum requirement 7468.18.5.3 Measurement restriction for
SSB based candidate beam detection 7498.18.6 Requirements for CSI-RS
based candidate beam detection 7508.18.6.1 Introduction 7508.18.6.2
Minimum requirement 7508.18.6.3 Measurement restriction for CSI-RS based
candidate beam detection 7528.18.7 Requirements for TRP specific Beam
Failure Recovery 7538.18.7.1 Introduction 7538.18.7.2 Requirement
7548.18.8 Scheduling availability of UE during TRP specific beam failure
detection 7548.18.8.1 Scheduling availability of UE performing TRP
specific beam failure detection with a same subcarrier spacing as
PDSCH/PDCCH on FR1 7548.18.8.2 Scheduling availability of UE performing
TRP specific beam failure detection with a different subcarrier spacing
than PDSCH/PDCCH on FR1 7548.18.8.3 Scheduling availability of UE
performing TRP specific beam failure detection on FR2 7548.18.8.4
Scheduling availability of UE performing TRP specific beam failure
detection on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC
7558.18.9 Scheduling availability of UE during TRP specific candidate
beam detection 7558.18.9.1 Scheduling availability of UE performing
L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1
7558.18.9.2 Scheduling availability of UE performing L1-RSRP measurement
with a different subcarrier spacing than PDSCH/PDCCH on FR1 7568.18.9.3
Scheduling availability of UE performing L1-RSRP measurement on FR2
7568.18.9.4 Scheduling availability of UE performing L1-RSRP measurement
on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC 7568.19
Pre-configured measurement gap activation/deactivation delay 7578.19.1
Introduction 7578.19.2 Pre-configured measurement gap
activation/deactivation upon DCI/timer-based BWP switch 7578.19.2.1
Activation/deactivation upon DCI/timer-based BWP switch delay on a
single CC 7578.19.3 Pre-configured measurement gap
activation/deactivation upon SCell activation/deactivation 7578.19.4
Pre-configured measurement gap activation/deactivation upon RRC
reconfiguration 7578.19.5 Activation/deactivation delay requirements for
concurrent measurement gaps with Pre-MG 7578.19.5.1
Activation/deactivation delay requirements for non-overlapped
activation/deactivation of concurrent measurement gaps with Pre- MG
7588.19.5.2 Activation/deactivation delay requirements for fully
overlapped activation/deactivation of concurrent measurement gaps with
Pre- MG 7588.19.5.3 Pre-MG activation/deactivation delay when colliding
with a concurrent measurement gap 7588.19D Pre-configured measurement
gap activation/deactivation delay for ATG 7588.19D.1 Introduction
7588.19D.2 Pre-configured measurement gap activation/deactivation upon
DCI/timer-based BWP switch 7588.19D.2.1 Activation/deactivation upon
DCI/timer-based BWP switch delay on a single CC 7588.19D.3
Pre-configured measurement gap activation/deactivation upon RRC
reconfiguration 7598.20 LTM PSCell Cell Switch 7598.20.1 Introduction
7598.20.2 LTM Cell Switch delay 7608.20.3 Void 7608.21 Active downlink
TCI state switching delay for unified TCI for single-DCI mTRP 7608.21.1
Introduction 7608.21.2 Known conditions for downlink TCI state 7608.21.3
MAC-CE based downlink TCI state switch delay 7618.21.4 DCI based
downlink TCI state switch delay 7628.21.5 Active Downlink TCI state list
update delay 7628.22 Active downlink TCI state switching delay for
unified TCI for multi-DCI mTRP 7638.22.1 Introduction 7638.22.2 Known
conditions for downlink TCI state 7638.22.3 MAC-CE based downlink TCI
state switch delay 7638.22.4 DCI based downlink TCI state switch delay
7658.22.5 Active Downlink TCI state list update delay 7658.23 Active
uplink TCI state switching delay for unified TCI for single-DCI mTRP
7668.23.1 Introduction 7668.23.2 Known conditions for uplink TCI state
7668.23.3 MAC-CE based uplink TCI state switch delay 7668.23.4 DCI based
uplink TCI state switch delay 7688.23.5 Active uplink TCI state list
update delay 7688.24 Active uplink TCI state switching delay for unified
TCI for multi-DCI mTRP 7698.24.1 Introduction 7698.24.2 Known conditions
for uplink TCI state 7698.24.3 MAC-CE based uplink TCI state switch
delay 7708.24.4 DCI based uplink TCI state switch delay 7718.24.5 Active
Uplink TCI state list update delay 7718.25 TCI state activation for LTM
candidate cell 7728.25.1 Introduction 7728.25.2 Known TCI state
conditions 7728.25.3 SSB based TCI state activation delay 7739
Measurement Procedure 7749.1 General measurement requirement 7749.1.1
Introduction 7749.1.2 Measurement gap 7749.1.2.1 EN-DC: Measurement Gap
Sharing 7849.1.2.1a SA: Measurement Gap Sharing 7849.1.2.1b NE-DC:
Measurement Gap Sharing 7859.1.2.1c NR-DC: Measurement Gap Sharing
7869.1.3 UE Measurement capability 7879.1.3.1 EN-DC: Monitoring of
multiple layers using gaps 7879.1.3.1a SA: Monitoring of multiple layers
using gaps 7889.1.3.1b NE-DC: Monitoring of multiple layers using gaps
7889.1.3.1c NR-DC: Monitoring of multiple layers using gaps 7899.1.3.2
EN-DC: Maximum allowed layers for multiple monitoring 7899.1.3.2a SA:
Maximum allowed layers for multiple monitoring 7909.1.3.2b NE-DC:
Maximum allowed layers for multiple monitoring 7919.1.3.2c NR-DC:
Maximum allowed layers for multiple monitoring 7919.1A.3.2 Void
7929.1.3A UE Measurement capability under operation mode with CCA
7929.1.3A.1 EN-DC: Monitoring of multiple layers using gaps under CCA
7929.1.3A.1a SA: Monitoring of multiple layers using gaps under CCA
7929.1.3A.2 EN-DC: Maximum allowed layers for multiple monitoring under
CCA 7929.1.3A.2a SA: Maximum allowed layers for multiple monitoring
under CCA 7939.1.3C UE Measurement capability under operation mode with
satellite access 7939.1.3C.1a SA: Monitoring of multiple layers using
gaps under satellite access 7939.1.3C.2a SA: Maximum allowed layers for
multiple monitoring for SAN 7949.1.4 Capabilities for Support of Event
Triggering and Reporting Criteria 7949.1.4.1 Introduction 7949.1.4.2
Requirements 7949.1.5 Carrier-specific scaling factor 7979.1.5.1
Monitoring of multiple layers outside gaps 7979.1.5.1.1 EN-DC mode:
carrier-specific scaling factor for SSB-based, CSI-RS based L3
measurements and RSSI and channel occupancy measurements performed
outside gaps 8009.1.5.1.2 SA mode: carrier-specific scaling factor for
SSB-based, CSI-RS based L3 measurements and RSSI and channel occupancy
measurements performed outside gaps 8029.1.5.1.3 NR-DC mode:
carrier-specific scaling factor for SSB-based and CSI-RS based L3
measurements performed outside gaps 8039.1.5.1.4 NE-DC mode:
carrier-specific scaling factor for SSB-based and CSI-RS based
measurements performed outside gaps 8039.1.5.2 Monitoring of multiple
layers within gaps 8059.1.5.2.1 EN-DC mode: carrier-specific scaling
factor for SSB, CSI-RS-based L3 measurements and RSSI and channel
occupancy measurements performed within gaps 8079.1.5.2.2 SA mode:
carrier-specific scaling factor for SSB, CSI-RS-based L3 measurements
and RSSI and channel occupancy measurements performed within gaps
8099.1.5.2.3 NE-DC: carrier-specific scaling factor for SSB-based and
CSI-RS based L3 measurements performed within gaps 8119.1.5.2.4 NR-DC:
carrier-specific scaling factor for SSB-based and CSI-RS-based L3
measurements performed within gaps 8139.1.5.2.5 SA mode:
carrier-specific scaling factor for PRS-based measurements performed
within gaps 8159.1.5.2.6 NE-DC: carrier-specific scaling factor for
PRS-based measurements performed within gaps 8159.1.5.2.7 NR-DC:
carrier-specific scaling factor for PRS-based measurements performed
within gaps 8159.1.5.3 Monitoring of multiple layers within NCSG
8169.1.5.3.1 SA mode: carrier-specific scaling factor for measurements
performed within NCSG 8179.1.5.4 L1-RSRP measurements within measurement
gap 8189.1.5.4.1 SA mode: carrier-specific scaling factor for L1-RSRP
measurements performed within measurement gap 8199.1.5.4.2 NR-DC:
carrier-specific scaling factor for L1-RSRP measurements performed
within measurement gap 8209.1.6 Minimum requirement at transitions
8229.1.7 Pre-configured measurement gap 8239.1.7.1 Introduction
8239.1.7.2 Requirements applicability 8239.1.7.3 Requirements
8239.1.7.3.1 Requirements for autonomous activation/deactivation
mechanism 8239.1.7.3.2 Requirements for network-controlled
activation/deactivation mechanism 8249.1.7.3.3 Requirements for
reception/transmission during activation/deactivation 8259.1.8
Concurrent measurement gaps 8259.1.8.1 Introduction 8259.1.8.2
Requirements 8259.1.8.3 Collision between concurrent measurement gaps
8269.1.8.4 Measurement gap related requirements of concurrent
measurement gaps 8279.1.9 Network controlled small gap 8279.1.9.1
Introduction 8279.1.9.2 Requirements applicability 8289.1.10 MUSIM gaps
8309.1.10.1 Introduction 8319.1.10.2 Priorities for MUSIM gaps
8319.1.10.3 Keep solution for MUSIM gaps 8329.1.10.4 Collisions between
different MUSIM gaps 8329.1.10.5 Collisions between MUSIM gaps and
measurement gaps 8329.1.10.6 MUSIM gap related requirements 8339.1.11 UL
gap for Tx power management 8339.1.12 Concurrent measurement gaps with
Pre-MG 8339.1.12.1 Introduction 8339.1.12.2 Requirements 8339.1.12.3
Collisions involving Pre-MG(s) 8349.1.12.4 Collision between Pre-MG
activation/deactivation and measurement gap 8359.1.12.5 Pre-MG related
requirements 8359.1.13 Concurrent measurement gaps with NCSG 8359.1.13.1
Introduction 8359.1.13.2 Requirements 8359.1.13.3 Collision involving
NCSGs 8379.1A General measurement requirement for RedCap 8379.1A.1
Introduction 8379.1A.2 Measurement gap 8379.1A.2.1 SA: Measurement Gap
Sharing 8419.1A.3 UE Measurement capability 8429.1A.3.1 SA: Monitoring
of multiple layers using gaps 8429.1A.3.2 SA: Maximum allowed layers for
multiple monitoring 8429.1A.4 Capabilities for Support of Event
Triggering and Reporting Criteria 8429.1A.4.1 Introduction 8429.1A.4.2
Requirements 8439.1A.5 Carrier-specific scaling factor 8439.1A.5.1
Monitoring of multiple layers outside gaps 8439.1A.5.1.1 SA mode:
carrier-specific scaling factor for SSB-based measurements performed
outside gaps 8449.1A.5.2 Monitoring of multiple layers within gaps
8449.1A.5.2.1 SA mode: carrier-specific scaling factor for SSB
measurements performed within gaps 8449.1A.6 Minimum requirement at
transitions 8469.1C General measurement requirement for SAN 8469.1C.1
Introduction 8469.1C.2 Measurement gap 8479.1C.8 Concurrent measurement
gaps for SAN 8499.1C.8.1 Introduction 8499.1C.8.2 Requirements
8499.1C.8.3 Collision between concurrent measurement gaps 8509.1C.8.4
Measurement gap related requirements of concurrent measurement gaps
8509.1C.9 Collision between SMTC and measurement gap for SAN 8509.1C.9.1
Introduction 8509.1C.9.2 Collision between SMTCs and measurement gap
8509.1C.9.3 Collision between multiple SMTCs on a SAN carrier 8519.1D
General measurement requirement for ATG 8519.1D.1 Introduction 8519.1D.2
Measurement gap 8519.1D.2.1a SA: Measurement Gap Sharing 8539.1D.3 UE
Measurement capability 8549.1D.3.1 SA: Monitoring of multiple layers
using gaps 8549.1D.3.2 SA: Maximum allowed layers for multiple
monitoring 8549.1D.4 Void 8549.1D.5 Carrier-specific scaling factor
8549.1D.5.1 Monitoring of multiple layers outside gaps 8549.1D.5.1.1
Void 8559.1D.5.1.2 SA mode: carrier-specific scaling factor for
SSB-based, CSI-RS based L3 measurements performed outside gaps
8559.1D.5.2 Monitoring of multiple layers within gaps 8559.1D.5.2.1 Void
8569.1D.5.2.2 SA mode: carrier-specific scaling factor for SSB,
CSI-RS-based L3 measurements performed within gaps 8569.1D.6 Void
8579.1D.7 Pre-configured measurement gap 8579.1D.7.1 Introduction
8579.1D.7.2 Requirements applicability 8579.1D.7.3 Requirements
8579.1D.7.3.1 Requirements for autonomous activation/deactivation
mechanism 8589.1D.7.3.2 Requirements for network-controlled
activation/deactivation mechanism 8589.1D.7.3.3 Requirements for
reception/transmission during activation/deactivation 8589.1D.8
Capabilities for Support of Event Triggering and Reporting Criteria
8599.1D.8.1 Introduction 8599.1D.8.2 Requirements 8599.1D.9 Minimum
requirement at transitions 8599.2 NR intra-frequency measurements
8609.2.1 Introduction 8609.2.2 Requirements applicability 8639.2.3
Number of cells and number of SSB 8639.2.3.1 Requirements for FR1
8639.2.3.2 Requirements for FR2 8649.2.4 Measurement Reporting
Requirements 8649.2.4.1 Periodic Reporting 8649.2.4.2 Event-triggered
Periodic Reporting 8649.2.4.3 Event Triggered Reporting 8649.2.4.4 SCell
activation Triggered Reporting 8659.2.5 Intrafrequency measurements
without measurement gaps 8659.2.5.1 Intrafrequency cell identification
8659.2.5.2 Measurement period 8729.2.5.3 Scheduling availability of UE
during intra-frequency measurements 8769.2.5.3.1 Scheduling availability
of UE performing measurements in TDD bands on FR1 8769.2.5.3.2
Scheduling availability of UE performing measurements with a different
subcarrier spacing than PDSCH/PDCCH on FR1 8779.2.5.3.3 Scheduling
availability of UE performing measurements on FR2 8779.2.5.3.4
Scheduling availability of UE performing measurements on FR1 or FR2 in
case of FR1-FR2 inter-band CA 8799.2.5.4 SFTD Measurements between PCell
and PSCell 8799.2.5.4.1 Introduction 8799.2.5.4.2 SFTD Measurement delay
8799.2.5.4.3 SFTD Measurement Reporting Delay 8809.2.6 Intra-frequency
measurements with measurement gaps 8809.2.6.1 Void 8809.2.6.2
Intra-frequency cell identification 8809.2.6.3 Intra-frequency
Measurement Period 8839.2.7 Intra-frequency measurements with NCSG
8849.2.7.1 Intra-frequency cell identification 8849.2.7.2 Measurement
period 8869.2.7.3 Scheduling availability during intra-frequency
measurement with NCSG 8879.2A NR intra-frequency measurements with CCA
8879.2A.1 Introduction 8879.2A.2 Requirements applicability 8889.2A.3
Number of cells and number of SSB 8899.2A.3.1 Requirements for FR1
8899.2A.3.2 Requirements for FR2-2 8899.2A.4 Measurement Reporting
Requirements 8899.2A.5 Intra-frequency measurements without measurement
gaps 8909.2A.5.2 Measurement period 8949.2A.5.3 Scheduling availability
of UE during intra-frequency measurements 8969.2A.5.3.1 Scheduling
availability of UE performing measurements in TDD bands on FR1
8979.2A.5.3.2 Scheduling availability of UE performing measurements with
a different subcarrier spacing than PDSCH/PDCCH on FR1 8979.2A.5.3.3
Scheduling availability of UE performing measurements in TDD bands on
FR2-2 8979.2A.6 Intra-frequency measurements with measurement gaps
8989.2A.6.1 Intra-frequency cell identification 8989.2A.6.2
Intra-frequency Measurement Period 9009.2A.7 Intra-frequency RSSI and
Channel occupancy measurements 9019.2A.7.1 Intra-frequency RSSI
measurements 9019.2A.7.2 Intra-frequency Channel occupancy measurements
9039.2A.7.3 Scheduling restriction during RSSI and Channel Occupancy
measurements in FR1 9059.2A.7.4 Scheduling restriction during RSSI
measurements in FR2-2 9059.2B NR intra-frequency measurements for RedCap
9059.2B.1 Introduction 9059.2B.2 Requirements applicability 9069.2B.3
Number of cells and number of SSB 9069.2B.3.1 Requirements for FR1
9069.2B.3.2 Requirements for FR2 9069.2B.4 Measurement Reporting
Requirements 9079.2B.4.1 Periodic Reporting 9079.2B.4.2 Event-triggered
Periodic Reporting 9079.2B.4.3 Event Triggered Reporting 9079.2B.5
Intra-frequency measurements without measurement gaps 9089.2B.5.1
Intra-frequency cell identification 9089.2B.5.2 Measurement period
9109.2B.5.3 Scheduling availability of UE during intra-frequency
measurements 9119.2B.5.3.1 Scheduling availability of UE performing
measurements in TDD bands on FR1 9119.2B.5.3.2 Scheduling availability
of UE performing measurements with a different subcarrier spacing than
PDSCH/PDCCH on FR1 9119.2B.5.3.3 Scheduling availability of UE
performing measurements on FR2 9129.2B.5.3.4 Scheduling availability of
HD-FDD UE performing measurements on FR1 9129.2B.6 Intra-frequency
measurements with measurement gaps 9139.2B.6.1 Intra-frequency cell
identification 9139.2B.6.2 Intra-frequency Measurement Period 9149.2C NR
intra-frequency measurements for SAN 9159.2C.1 Introduction 9159.2C.2
Requirements applicability 9169.2C.3 Number of cells and number of SSB
9169.2C.3.1 Requirements for FR1 9169.2C.4 Measurement Reporting
Requirements 9179.2C.4.1 Periodic Reporting 9179.2C.4.2 Event-triggered
Periodic Reporting 9179.2C.4.3 Event Triggered Reporting 9179.2C.5
Intra-frequency measurements without measurement gaps 9179.2C.5.1
Intra-frequency cell identification 9179.2C.5.2 Measurement period
9199.2C.5.3 Scheduling availability of UE during intra-frequency
measurements 9209.2C.5.3.1 Scheduling availability of UE performing
measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1
9209.2C.5.3.2 Scheduling availability of UE performing measurements on a
neighbor cell served by a different satellite in LEO 9209.2C.6
Intra-frequency measurements with measurement gaps 9219.2C.6.1
Intra-frequency cell identification 9219.2C.6.3 Intrafrequency
Measurement Period 9229.2C.7 Intra-frequency measurements without
measurement gaps for NTN band above 10 GHz 9229.2C.7.1 Intra-frequency
cell identification 9229.2C.7.2 Measurement period 9249.2C.7.3
Scheduling availability of UE during intra-frequency measurements
9249.2C.7.3.1 Scheduling availability of UE performing measurements with
a different subcarrier spacing than PDSCH/PDCCH on NTN bands above 10
GHz 9249.2C.8 Intra-frequency measurements with measurement gaps for NTN
band above 10 GHz 9259.2C.8.1 Intra-frequency cell identification
9259.2C.8.3 Intra-frequency Measurement Period 9269.2D NR
intra-frequency measurements for ATG 9269.2D.1 Introduction 9269.2D.2
Requirements applicability 9269.2D.3 Number of cells and number of SSB
9279.2D.3.1 Requirements for FR1 9279.2D.4 Measurement Reporting
Requirements 9279.2D.4.1 Periodic Reporting 9279.2D.4.2 Event-triggered
Periodic Reporting 9279.2D.4.3 Event Triggered Reporting 9279.2D.5
Intra-frequency measurements without measurement gaps 9289.2D.5.1
Intra-frequency cell identification 9289.2D.5.2 Measurement period
9299.2D.5.3 Scheduling availability of UE during intra-frequency
measurements 9309.2D.5.3.1 Scheduling availability of UE performing
measurements on FR1 9309.2D.5.3.2 Scheduling availability of UE
performing measurements with a different subcarrier spacing than
PDSCH/PDCCH on FR1 9319.2D.6 Intra-frequency measurements with
measurement gaps 9319.2D.6.1 Void 9319.2D.6.2 Intra-frequency cell
identification 9319.2D.6.3 Intra-frequency Measurement Period 9339.3 NR
inter-frequency measurements 9339.3.1 Introduction 9339.3.2 Requirements
applicability 9369.3.2.1 Void 9379.3.2.2 Void 9379.3.3 Number of cells
and number of SSB 9379.3.3.1 Requirements for FR1 9379.3.3.2
Requirements for FR2 9379.3.4 Inter-frequency measurement with
measurement gaps 9379.3.4.1 Void 9429.3.4.2 Void 9429.3.5
Inter-frequency measurements 9429.3.5.1 Void 9439.3.5.2 Void 9439.3.5.3
Void 9439.3.6 Inter-frequency measurements reporting requirements
9439.3.6.1 Periodic Reporting 9439.3.6.2 Event-triggered Periodic
Reporting 9439.3.6.3 Event-triggered Reporting 9439.3.7 Void 9449.3.8
Inter-frequency SFTD measurement requirements 9449.3.8.1 Introduction
9449.3.8.2 SFTD Measurement delay 9449.3.8.3 SFTD Measurement reporting
delay 9459.3.9 Inter-frequency measurements without measurement gaps
9469.3.9.1 Inter-frequency Cell identification 9469.3.9.2 Measurement
period 9519.3.9.3 Scheduling availability of UE during inter-frequency
measurements when the SSB is completely contained in the active BWP of
the UE 9539.3.9.3.1 Scheduling availability of UE performing
measurements in TDD bands on FR1 9539.3.9.3.2 Scheduling availability of
UE performing measurements with a different subcarrier spacing than
PDSCH/PDCCH on FR1 9549.3.9.3.3 Scheduling availability of UE performing
measurements on FR2 9549.3.9.3.4 Scheduling availability of UE
performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA
9559.3.9.4 Scheduling availability of UE during inter-frequency
measurements when the SSB is not completely contained in the active BWP
of the UE 9559.3.9.4.1 Scheduling availability of UE performing
measurements in TDD bands on FR1 9559.3.9.4.2 Scheduling availability of
UE performing measurements with a different subcarrier spacing than
PDSCH/PDCCH on FR1 9569.3.9.4.3 Scheduling availability of UE performing
measurements on FR2 9569.3.9.4.4 Scheduling availability of UE
performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA
9589.3.10 Inter-frequency measurement with NCSG 9589.3.10.1
Inter-frequency cell identification 9589.3.10.2 Measurement period
9609.3.10.3 Scheduling availability during inter-frequency measurement
with NCSG 9609.3.10.3.1 Scheduling availability of UE performing
measurements in TDD bands on FR1 9619.3.10.3.2 Scheduling availability
of UE performing measurements with a different subcarrier spacing than
PDSCH/PDCCH on FR1 9619.3.10.3.3 Scheduling availability of UE
performing measurements on FR2 9629.3.10.3.4 Scheduling availability of
UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band
CA 9639.3A NR inter-frequency measurements in carrier frequencies with
CCA 9649.3A.1 Introduction 9649.3A.2 Requirements applicability
9649.3A.3 Number of cells and number of SSB 9659.3A.3.1 Requirements for
FR1 9659.3A.3.2 Requirements for FR2-2 9659.3A.4 Inter-frequency cell
identification 9659.3A.5 Inter-frequency measurements 9679.3A.6
Inter-frequency measurements reporting requirements 9699.3A.6.1 Periodic
Reporting 9699.3A.6.2 Event-triggered Periodic Reporting 9699.3A.6.3
Event-triggered Reporting 9699.3A.8 Inter-frequency RSSI measurements
9699.3A.9 Inter-frequency channel occupancy measurements 9709.3B NR
inter-frequency measurements for RedCap 9719.3B.1 Introduction 9719.3B.2
Requirements applicability 9719.3B.3 Number of cells and number of SSB
9729.3B.3.1 Requirements for FR1 9729.3B.3.2 Requirements for FR2
9729.3B.4 Inter-frequency measurement with measurement gaps 9729.3B.5
Inter-frequency measurements 9749.3B.6 Inter-frequency measurements
reporting requirements 9749.3B.6.1 Periodic Reporting 9749.3B.6.2
Event-triggered Periodic Reporting 9749.3B.6.3 Event-triggered Reporting
9759.3B.7 Inter-frequency measurements without measurement gaps
9759.3B.7.1 Inter-frequency Cell identification 9759.3B.7.2 Measurement
period 9779.3B.7.3 Scheduling availability of UE during inter-frequency
measurements 9789.3B.7.3.1 Scheduling availability of UE performing
measurements in TDD bands on FR1 9789.3B.7.3.2 Scheduling availability
of UE performing measurements with a different subcarrier spacing than
PDSCH/PDCCH on FR1 9789.3B.7.3.3 Scheduling availability of UE
performing measurements on FR2 9799.3B.7.3.4 Scheduling availability of
HD-FDD UE performing measurements on FR1 9799.3C NR inter-frequency
measurements for SAN 9799.3C.1 Introduction 9799.3C.2 Requirements
applicability 9809.3C.3 Number of cells and number of SSB 9819.3C.3.1
Requirements for FR1 9819.3C.4 Inter-frequency measurement with
measurement gaps 9819.3C.5 Inter-frequency measurements 9829.3C.6
Inter-frequency measurements reporting requirements 9839.3C.6.1 Periodic
Reporting 9839.3C.6.2 Event-triggered Periodic Reporting 9839.3C.6.3
Event-triggered Reporting 9839.3C.7 Inter-frequency measurements without
measurement gaps 9849.3C.7.1 Inter-frequency Cell identification
9849.3C.7.2 Measurement period 9859.3C.7.3 Scheduling availability of UE
during inter-frequency measurements 9859.3C.7.3.1 Void 9859.3C.7.3.2
Scheduling availability of UE performing measurements with a different
subcarrier spacing than PDSCH/PDCCH on FR1 9859.3C.8 Inter-frequency
measurement with measurement gaps for NTN band above 10 GHz 9869.3C.9
Inter-frequency measurements for NTN band above 10 GHz 9879.3C.10
Inter-frequency measurements without measurement gaps for NTN band above
10 GHz 9879.3C.10.1 Inter-frequency Cell identification 9879.3C.10.2
Measurement period 9889.3C.10.3 Scheduling availability of UE during
inter-frequency measurements 9889.3C.10.3.1 Scheduling availability of
UE performing measurements with a different subcarrier spacing than
PDSCH/PDCCH on NTN bands above 10 GHz 9899.3D NR inter-frequency
measurements for ATG 9899.3D.1 Introduction 9899.3D.2 Requirements
applicability 9899.3D.3 Number of cells and number of SSB 9909.3D.3.1
Requirements for FR1 9909.3D.4 Inter-frequency measurement with
measurement gaps 9909.3D.5 Inter-frequency measurements 9919.3D.6
Inter-frequency measurements reporting requirements 9919.3D.6.1 Periodic
Reporting 9919.3D.6.2 Event-triggered Periodic Reporting 9929.3D.6.3
Event-triggered Reporting 9929.3D.7 Void 9929.3D.8 Void 9929.3D.9
Inter-frequency measurements without measurement gaps 9929.3D.9.1
Inter-frequency Cell identification 9929.3D.9.2 Measurement period
9949.3D.9.3 Scheduling availability of UE during inter-frequency
measurements 9959.3D.9.3.1 Scheduling availability of UE performing
measurements in TDD bands on FR1 9959.3D.9.3.2 Scheduling availability
of UE performing measurements with a different subcarrier spacing than
PDSCH/PDCCH on FR1 9959.4 Inter-RAT measurements 9969.4.1 Introduction
9969.4.2 NR − E-UTRAN FDD measurements 9989.4.2.1 Introduction
9989.4.2.2 Requirements when no DRX is used 9999.4.2.3 Requirements when
DRX is used 10009.4.2.4 Measurement reporting requirements 10019.4.2.4.1
Periodic Reporting 10019.4.2.4.2 Event-Triggered Periodic Reporting
10019.4.2.4.3 Event-Triggered Reporting 10029.4.2.5 Scheduling
Availability During NR − E-UTRAN FDD measurements with NCSG 10029.4.3 NR
− E-UTRAN TDD measurements 10029.4.3.1 Introduction 10029.4.3.2
Requirements when no DRX is used 10029.4.3.3 Requirements when DRX is
used 10049.4.3.4 Measurement reporting requirements 10059.4.3.4.1
Periodic Reporting 10059.4.3.4.2 Event-Triggered Periodic Reporting
10059.4.3.4.3 Event-Triggered Reporting 10069.4.3.5 Scheduling
Availability During NR − E-UTRAN TDD measurements with NCSG 10069.4.4
Inter-RAT RSTD measurements 10069.4.4.1 NR − E-UTRAN FDD RSTD
measurements 10069.4.4.1.1 Introduction 10069.4.4.1.2 Requirements
10079.4.4.2 NR − E-UTRAN TDD RSTD measurements 10099.4.4.2.1
Introduction 10099.4.4.2.2 Requirements 10109.4.5 Inter-RAT E-CID
measurements 10139.4.5.1 NR−E-UTRAN FDD E-CID RSRP and RSRQ measurements
10139.4.5.1.1 Introduction 10139.4.5.1.2 Requirements 10139.4.5.1.3
Measurement Reporting Delay 10139.4.5.2 NR−E-UTRAN TDD E-CID RSRP and
RSRQ measurements 10149.4.5.2.1 Introduction 10149.4.5.2.2 Requirements
10149.4.5.2.3 Measurement Reporting Delay 10149.4.6 NR − UTRAN FDD
measurements 10149.4.6.1 Introduction 10149.4.6.2 Requirements when no
DRX is used 10149.4.6.3 Requirements when DRX is used 10159.4.7 NR --
E-UTRAN measurements with autonomous gaps 10179.4.7.1 CGI identification
of an E-UTRA cell with autonomous gaps 10179.4.7.2 CGI reporting delay
10179.4.8 NR -- E-UTRAN measurements without measurement gaps
10189.4.8.1 Introduction 10189.4.8.2 General requirements 10189.4.8.3 NR
− E-UTRAN FDD measurements 10199.4.8.3.1 Introduction 10199.4.8.3.2
Requirements when no DRX is used 10199.4.8.3.3 Requirements when DRX is
used 10209.4.8.3.4 Measurement reporting requirements 10209.4.8.3.5
Scheduling availability during NR − E-UTRAN FDD measurements 10219.4.8.4
NR − E-UTRAN TDD measurements 10219.4.8.4.1 Introduction 10219.4.8.4.2
Requirements when no DRX is used 10229.4.8.4.3 Requirements when DRX is
used 10239.4.8.4.4 Measurement reporting requirements 10249.4.8.4.5
Scheduling availability during NR − E-UTRAN TDD measurements 10249.4A
Inter-RAT measurements for RedCap 10259.4A.1 Introduction 10259.4A.2 NR
− E-UTRAN FDD measurements 10269.4A.2.1 Introduction 10269.4A.2.2
Requirements when no DRX is used 10269.4A.2.3 Requirements when DRX is
used 10279.4A.2.4 Measurement reporting requirements 10289.4A.2.4.1
Periodic Reporting 10289.4A.2.4.2 Event-Triggered Periodic Reporting
10289.4A.2.4.3 Event-Triggered Reporting 10289.4A.3 NR − E-UTRAN TDD
measurements 10299.4A.3.1 Introduction 10299.4A.3.2 Requirements when no
DRX is used 10299.4A.3.3 Requirements when DRX is used 10319.4A.3.4
Measurement reporting requirements 10329.4A.3.4.1 Periodic Reporting
10329.4A.3.4.2 Event-Triggered Periodic Reporting 10329.4A.3.4.3
Event-Triggered Reporting 10329.4A.4 NR -- E-UTRAN measurements with
autonomous gaps 10339.4A.4.1 CGI identification of an E-UTRA cell with
autonomous gaps 10339.4A.4.2 CGI reporting delay 10339.4A.4.3 CGI
reporting scheduling restriction 10339.5 L1-RSRP measurements for
Reporting 10349.5.1 Introduction 10349.5.2 Requirements applicability
10349.5.3 Measurement Reporting Requirements 10359.5.3.1 Periodic
Reporting 10359.5.3.2 Semi-Persistent Reporting 10369.5.3.3 Aperiodic
Reporting 10369.5.4 L1-RSRP measurement requirements 10369.5.4.1 SSB
based L1-RSRP Reporting 10369.5.4.2 CSI-RS based L1-RSRP Reporting
10429.5.4A Void 10469.5.4A.1 Void 10469.5.5 Measurement restriction for
CSI-RS and SSB for L1-RSRP measurement 10469.5.5.1 Measurement
restriction for SSB based L1-RSRP 10469.5.5.2 Measurement restriction
for CSI-RS based L1-RSRP 10479.5.6 Scheduling availability of UE during
L1-RSRP measurement 10489.5.6.1 Scheduling availability of UE performing
L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1
10489.5.6.2 Scheduling availability of UE performing L1-RSRP measurement
with a different subcarrier spacing than PDSCH/PDCCH on FR1 10489.5.6.3
Scheduling availability of UE performing L1-RSRP measurement on FR2
10499.5.6.4 Scheduling availability of UE performing L1-RSRP measurement
on FR1 or FR2 in case of FR1-FR2 inter-band CA 10519.5.7 Minimum
requirement at transitions 10519.5A L1-RSRP measurements for Reporting
under CCA 10519.5A.1 Introduction 10519.5A.2 Requirements applicability
10519.5A.3 Measurement Reporting Requirements 10529.5A.3.1 Periodic
Reporting 10529.5A.3.2 Semi-Persistent Reporting 10529.5A.3.3 Aperiodic
Reporting 10529.5A.4 L1-RSRP measurement requirements 10539.5A.4.1 SSB
based L1-RSRP Reporting 10539.5A.5 Measurement restriction for L1-RSRP
measurement 10559.5A.5.1 Measurement restriction for SSB based L1-RSRP
10559.5A.6 Scheduling availability of UE during L1-RSRP measurement
10569.5A.6.1 Scheduling availability of UE performing L1-RSRP
measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1
10569.5A.6.2 Scheduling availability of UE performing L1-RSRP
measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1
10569.5A.6.3 Void 10569.5A.6.3A Scheduling availability of UE performing
L1-RSRP measurement in case of FR1-FR2 inter-band CA 10569.5A.6.3B
Scheduling availability of UE performing L1-RSRP measurement on FR2-2
10569.5A.6.4 Scheduling availability of UE performing L1-RSRP
measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA 10579.5B
L1-RSRP measurements for Reporting for RedCap 10579.5B.1 Introduction
10579.5B.2 Requirements applicability 10579.5B.3 Measurement Reporting
Requirements 10589.5B.3.1 Periodic Reporting 10589.5B.3.2
Semi-Persistent Reporting 10589.5B.3.3 Aperiodic Reporting 10599.5B.4
L1-RSRP measurement requirements 10599.5B.4.1 SSB based L1-RSRP
Reporting 10599.5B.4.2 CSI-RS based L1-RSRP Reporting 10619.5B.5
Measurement restriction for CSI-RS and SSB for L1-RSRP measurement
10649.5B.5.1 Measurement restriction for SSB based L1-RSRP 10649.5B.5.2
Measurement restriction for CSI-RS based L1-RSRP 10649.5B.6 Scheduling
availability of UE during L1-RSRP measurement 10649.5B.6.1 Scheduling
availability of UE performing L1-RSRP measurement with a same subcarrier
spacing as PDSCH/PDCCH on FR1 10659.5B.6.2 Scheduling availability of UE
performing L1-RSRP measurement with a different subcarrier spacing than
PDSCH/PDCCH on FR1 10659.5B.6.3 Scheduling availability of UE performing
L1-RSRP measurement on FR2 10659.5C L1-RSRP measurements for Reporting
for satellite access 10669.5C.1 Introduction 10669.5C.3 Measurement
Reporting Requirements 10669.5C.3.1 Periodic Reporting 10679.5C.3.2
Semi-Persistent Reporting 10679.5C.3.3 Aperiodic Reporting 10679.5C.4
L1-RSRP measurement requirements 10679.5C.4.1 SSB based L1-RSRP
Reporting 10679.5C.5 Measurement restriction for L1-RSRP measurement
10699.5C.5.1 Measurement restriction for SSB based L1-RSRP 10699.5C.5.2
Measurement restriction for CSI-RS based L1-RSRP 10699.5C.6 Scheduling
availability of UE during L1-RSRP measurement 10709.5C.6.1 Scheduling
availability of UE performing L1-RSRP measurement with a same subcarrier
spacing as PDSCH/PDCCH on FR1 10709.5C.6.2 Scheduling availability of UE
performing L1-RSRP measurement with a different subcarrier spacing than
PDSCH/PDCCH on FR1 10709.5C.7 L1-RSRP measurement requirements for NTN
band above 10 GHz 10709.5C.7.1 SSB based L1-RSRP Reporting 10709.5C.7.2
CSI-RS based L1-RSRP Reporting 10719.5C.8 Measurement restriction for
L1-RSRP measurement for NTN band above 10 GHz 10729.5C.8.1 Measurement
restriction for SSB based L1-RSRP 10729.5C.8.2 Measurement restriction
for CSI-RS based L1-RSRP 10729.5C.9 Scheduling availability of UE during
L1-RSRP measurement for NTN band above 10 GHz 10739.5C.9.1 Scheduling
availability of UE performing L1-RSRP measurement with a same subcarrier
spacing as PDSCH/PDCCH on NTN bands above 10 GHz 10739.5C.9.2 Scheduling
availability of UE performing L1-RSRP measurement with a different
subcarrier spacing than PDSCH/PDCCH on NTN bands above 10 GHz 10739.5D
L1-RSRP measurements for Reporting for ATG 10739.5D.1 Introduction
10739.5D.2 Requirements applicability 10739.5D.3 Measurement Reporting
Requirements 10749.5D.3.1 Periodic Reporting 10749.5D.3.2
Semi-Persistent Reporting 10749.5D.3.3 Aperiodic Reporting 10749.5D.4
L1-RSRP measurement requirements 10749.5D.4.1 SSB based L1-RSRP
Reporting 10749.5D.4.2 CSI-RS based L1-RSRP Reporting 10769.5D.5
Measurement restriction for CSI-RS and SSB for L1-RSRP measurement
10779.5D.5.1 Measurement restriction for SSB based L1-RSRP 10779.5D.5.2
Measurement restriction for CSI-RS based L1-RSRP 10779.5D.6 Scheduling
availability of UE during L1-RSRP measurement 10789.5D.6.1 Scheduling
availability of UE performing L1-RSRP measurement with a same subcarrier
spacing as PDSCH/PDCCH on FR1 10789.5D.6.2 Scheduling availability of UE
performing L1-RSRP measurement with a different subcarrier spacing than
PDSCH/PDCCH on FR1 10789.6 NE-DC: Measurements 10789.6.1 Introduction
10789.6.2 SFTD Measurements 10789.6.2.1 Introduction 10789.6.2.2 SFTD
Measurement requirements 10799.7 Cross Link Interference measurements
10799.7.1 Introduction 10799.7.2 SRS-RSRP measurements 10809.7.2.1
Introduction 10809.7.2.2 Requirements applicability 10809.7.2.3
Measurement Reporting Requirements 10809.7.2.3.1 Periodic Reporting
10809.7.2.3.2 Event-triggered Periodic Reporting 10809.7.2.3.3 Event
Triggered Reporting 10809.7.2.4 Measurement capability 10819.7.2.5
SRS-RSRP measurement period 10819.7.3 CLI-RSSI measurements 10819.7.3.1
Introduction 10819.7.3.2 Requirements applicability 10819.7.3.3
Measurement Reporting Requirements 10819.7.3.3.1 Periodic Reporting
10819.7.3.3.2 Event-triggered Periodic Reporting 10829.7.3.3.3 Event
Triggered Reporting 10829.7.3.4 Measurement capability 10829.7.3.5
CLI-RSSI measurement period 10829.7.4 Scheduling availability of UE
during CLI measurements 10829.7.4.1 Scheduling availability of UE
performing measurement on FR1 10829.7.4.2 Scheduling availability of UE
performing measurement on FR2 10839.8 L1-SINR measurements for Reporting
10849.8.1 Introduction 10849.8.2 Requirements applicability 10849.8.3
Measurement Reporting Requirements 10859.8.3.1 Periodic Reporting
10859.8.3.2 Semi-Persistent Reporting 10859.8.4 L1-SINR measurement
requirements 10869.8.4.1 L1-SINR reporting with CSI-RS based CMR and no
dedicated IMR configured 10869.8.4.3 L1-SINR reporting with CSI-RS based
CMR and dedicated IMR configured 10919.8.5 Measurement restriction for
L1-SINR measurement 10929.8.5.1 Measurement restriction if SSB
configured for L1-SINR Measurement 10939.8.5.2 Measurement restriction
if CSI-RS configured for L1-SINR measurement 10939.8.5.3 Measurement
restriction if CSI-IM configured for L1-SINR measurement 10959.8.6
Scheduling availability of UE during L1-SINR measurement 10959.8.6.1
Scheduling availability of UE performing L1-SINR measurement with a same
subcarrier spacing as PDSCH/PDCCH on FR1 10959.8.6.2 Scheduling
availability of UE performing L1-SINR measurement with a different
subcarrier spacing than PDSCH/PDCCH on FR1 10969.8.6.4 Scheduling
availability of UE performing L1-SINR measurement on FR1 or FR2 in case
of FR1-FR2 inter-band CA 10979.8.7 Minimum requirement at transitions
10979.8D L1-SINR measurements for Reporting for ATG 10979.8D.1
Introduction 10979.8D.2 Requirements applicability 10989.8D.3
Measurement Reporting Requirements 10989.8D.3.1 Periodic Reporting
10989.8D.3.2 Semi-Persistent Reporting 10989.8D.3.3 Aperiodic Reporting
10999.8D.4 L1-SINR measurement requirements 10999.8D.4.1 L1-SINR
reporting with CSI-RS based CMR and no dedicated IMR configured
10999.8D.4.2 L1-SINR reporting with SSB based CMR and dedicated IMR
configured 11009.8D.4.3 L1-SINR reporting with CSI-RS based CMR and
dedicated IMR configured 11019.8D.5 Measurement restriction for L1-SINR
measurement 11029.8D.5.1 Measurement restriction if SSB configured for
L1-SINR Measurement 11029.8D.5.2 Measurement restriction if CSI-RS
configured for L1-SINR measurement 11039.8D.5.3 Measurement restriction
if CSI-IM configured for L1-SINR measurement 11039.8D.6 Scheduling
availability of UE during L1-SINR measurement 11039.8D.6.1 Scheduling
availability of UE performing L1-SINR measurement with a same subcarrier
spacing as PDSCH/PDCCH on FR1 11039.8D.6.2 Scheduling availability of UE
performing L1-SINR measurement with a different subcarrier spacing than
PDSCH/PDCCH on FR1 11039.9 NR measurements for positioning 11049.9.1
Introduction 11049.9.1.1 General Aspects of Gap-based Measurement
11049.9.1.2 General Aspects of Gapless Measurement 11059.9.1.3
Scheduling Availability of UE during PRS Measurement without Measurement
Gaps 11069.9.2 RSTD measurements 11079.9.2.1 Introduction 11079.9.2.2
Requirements Applicability 11079.9.2.3 Measurement Capability
11079.9.2.4 Measurement Reporting Requirements 11079.9.2.4.1 Void
11079.9.2.4.2 Void 11079.9.2.4.3 Void 11079.9.2.5 Measurements Period
Requirements 11079.9.2.6 Void 11109.9.2.7 Measurements Period
Requirements without Measurement Gaps 11109.9.2.8 Void 11139.9.2.9
Measurements Period Requirements with both MG and PPW 11139.9.2.10
Measurements Period Requirements with Bandwidth Aggregation 11149.9.3
PRS-RSRP measurements 11179.9.3.1 Introduction 11179.9.3.2 Requirements
applicability 11189.9.3.3 Measurement Capability 11189.9.3.4 Measurement
Reporting Requirements 11189.9.3.5 Measurement Period Requirements
11189.9.3.6 Measurement Period Requirements without Measurement Gaps
11219.9.3.7 Void 11239.9.3.8 Measurements Period Requirements with both
MG and PPW 11239.9.4 UE Rx-Tx time difference measurements 11249.9.4.1
Introduction 11249.9.4.2 Requirements Applicability 11249.9.4.3
Measurement Capability 11249.9.4.4 Measurement Reporting Requirements
11249.9.4.5 Measurement Period Requirements 11249.9.4.6 Measurement
Period Requirements without Measurement Gaps 11289.9.4.7 Void
11319.9.4.8 Measurements Period Requirements with both MG and PPW
11319.9.4.9 Measurements Period Requirements with Bandwidth Aggregation
11329.9.5 E-CID measurements 11369.9.5.1 Introduction 11369.9.5.2
Measurement Requirements 11369.9.5.2.1 Intra-frequency Measurement
Requirements 11369.9.5.2.2 Inter-frequency Measurement Requirements
11369.9.5.2.3 Measurement Reporting Delay 11379.9.6 PRS-RSRPP
measurements 11379.9.6.1 Introduction 11379.9.6.2 Requirements
applicability 11379.9.6.3 Measurement capability 11379.9.6.4 Measurement
reporting requirements 11379.9.6.5 Measurement period requirements
11379.9.6.6 Measurement Period Requirements without Measurement Gaps
11389.9.6.7 Void 11389.9.6.8 Measurements Period Requirements with both
MG and PPW 11389.9.7 Measurement requirements for DL RSCPD reported with
RSTD 11389.9.7.1 Introduction 11389.9.7.2 Requirements Applicability
11389.9.7.3 Measurement Capability 11389.9.7.4 Measurement Reporting
Requirements 11389.9.7.5 Measurements Period Requirements for DL RSCPD
reported with RSTD 11399.9.8 Measurement requirements for DL RSCP
reported with UE Rx-Tx time difference 11419.9.8.1 Introduction
11419.9.8.2 Requirements Applicability 11429.9.8.3 Measurement
Capability 11429.9.8.4 Measurement Reporting Requirements 11429.9.8.5
Measurement Period Requirements for DL RSCP and UE Rx-Tx time difference
11429.9A NR measurements for positioning for RedCap 11469.9A.1
Introduction 11469.9A.1.1 General Aspects of Gap-based Measurement
11469.9A.1.2 General Aspects of Gapless Measurement for RedCap
positioning without FH 11479.9A.1.3 Scheduling Availability of UE during
PRS Measurement without Measurement Gaps for RedCap positioning without
FH 11489.9A.2 RSTD measurements for RedCap 11499.9A.2.1 Introduction
11499.9A.2.2 Requirements Applicability 11499.9A.2.3 Measurement
Capability 11499.9A.2.4 Measurement Reporting Requirements 11499.9A.2.5
Measurements Period Requirements without FH 11499.9A.2.5.1 Measurements
Period Requirements without FH with MG 11499.9A.2.5.2 Measurements
Period Requirements without FH without MG 11529.9A.2.5.3 Measurements
Period Requirements without FH with both MG and PPW 11559.9A.2.6
Measurements Period Requirements with FH 11569.9A.2.6.1 Measurements
Period Requirements with FH with MG 11569.9A.3 PRS-RSRP measurements for
RedCap 11589.9A.3.1 Introduction 11589.9A.3.2 Requirements applicability
11589.9A.3.3 Measurement Capability 11589.9A.3.4 Measurement Reporting
Requirements 11589.9A.3.5 Measurements Period Requirements without FH
11589.9A.3.5.1 Measurement Period Requirements without FH with MG
11589.9A.3.5.2 Measurement Period Requirements without FH without MG
11619.9A.3.5.3 Measurements Period Requirements without FH with both MG
and PPW 11639.9A.3.6 Measurements Period Requirements with FH
11649.9A.3.6.1 Measurements Period Requirements with FH with MG
11649.9A.4 UE Rx-Tx time difference measurements for RedCap 11669.9A.4.1
Introduction 11669.9A.4.2 Requirements Applicability 11669.9A.4.3
Measurement Capability 11669.9A.4.4 Measurement Reporting Requirements
11669.9A.4.5 Measurement Period Requirements without FH with MG
11669.9A.4.6 Measurement Period Requirements without FH without MG
11669.9A.4.7 Measurements Period Requirements without FH with both MG
and PPW 11669.9A.4.8 Measurements Period Requirements with FH 11669.9A.5
PRS-RSRPP measurements for RedCap 11689.9A.5.1 Introduction 11689.9A.5.2
Requirements Applicability 11689.9A.5.3 Measurement Capability
11689.9A.5.4 Measurement Reporting Requirements 11699.9A.5.5 Measurement
Period Requirements without FH with MG 11699.9A.5.6 Measurement Period
Requirements without FH without MG 11699.9A.5.7 Measurements Period
Requirements without FH with both MG and PPW 11699.9A.5.8 Measurements
Period Requirements with FH 11699.9C NR measurements for positioning in
Satellite Access 11699.9C.1 Introduction 11699.9C.1.1 General Aspects of
Gap-based Measurement 11699.9C.1.2 General Aspects of Gapless
Measurement 11709.9C.1.3 Scheduling Availability of UE during PRS
Measurement without Measurement Gaps 11719.9C.2 Void 11719.9C.3 Void
11719.9C.4 UE Rx-Tx time difference measurements 11719.9C.4.1
Introduction 11719.9C.4.2 Requirements Applicability 11719.9C.4.3
Measurement Capability 11719.9C.4.4 Measurement Reporting Requirements
11719.9C.4.5 Measurement Period Requirements 11729.9C.4.6 Measurement
Period Requirements without Measurement Gaps 11749.10 CSI-RS based L3
measurements 11769.10.1 Introduction 11769.10.2 CSI-RS based
intra-frequency measurements 11769.10.2.1 Introduction 11769.10.2.2
Requirements applicability 11779.10.2.3 Number of cells and number of
CSI-RS 11789.10.2.3.1 Requirements for FR1 11789.10.2.3.2 Requirements
for FR2 11789.10.2.4 Measurement Reporting Requirements 11789.10.2.4.1
Periodic Reporting 11799.10.2.4.2 Event-triggered Periodic Reporting
11799.10.2.4.3 Event Triggered Reporting 11799.10.2.5 Intra-frequency
measurements without measurement gaps 11799.10.2.6 Scheduling
availability of UE during CSI-RS based intra-frequency measurements
11819.10.2.6.1 Scheduling availability of UE performing CSI-RS based
measurements in TDD bands 11819.10.2.6.2 Scheduling availability of UE
performing CSI-RS based measurements in FR2 11819.10.3 CSI-RS based
Inter-frequency measurements 11829.10.3.1 Introduction 11829.10.3.2
Requirements applicability 11829.10.3.3 Number of cells and number of
CSI-RS resources 11839.10.3.3.1 Requirements for FR1 11839.10.3.3.2
Requirements for FR2 11839.10.3.4 Measurements reporting requirements
11839.10.3.4.1 Periodic Reporting 11839.10.3.4.2 Event-triggered
Periodic Reporting 11839.10.3.4.3 Event-triggered Reporting 11839.10.3.5
Inter-frequency measurements with measurement gaps 11849.10D CSI-RS
based L3 measurements for ATG 11859.10D.1 Introduction 11859.10D.2
CSI-RS based intra-frequency measurements 11869.10D.2.1 Introduction
11869.10D.2.2 Requirements applicability 11869.10D.2.3 Number of cells
and number of CSI-RS 11879.10D.2.3.1 Requirements for FR1 11879.10D.2.4
Measurement Reporting Requirements 11879.10D.2.4.1 Periodic Reporting
11879.10D.2.4.2 Event-triggered Periodic Reporting 11879.10D.2.4.3 Event
Triggered Reporting 11889.10D.2.5 Intra-frequency measurements without
measurement gaps 11889.10D.2.6 Scheduling availability of UE during
CSI-RS based intra-frequency measurements 11899.10D.2.6.1 Scheduling
availability of UE performing CSI-RS based measurements in TDD bands
11909.10D.3 CSI-RS based Inter-frequency measurements 11909.10D.3.1
Introduction 11909.10D.3.2 Requirements applicability 11909.10D.3.3
Number of cells and number of CSI-RS resources 11919.10D.3.3.1
Requirements for FR1 11919.10D.3.4 Measurements reporting requirements
11919.10D.3.4.1 Periodic Reporting 11919.10D.3.4.2 Event-triggered
Periodic Reporting 11919.10D.3.4.3 Event-triggered Reporting
11919.10D.3.5 Inter-frequency measurements with measurement gaps
11919.11 NR measurements with autonomous gaps 11939.11.1 Introduction
11939.11.2 CGI identification of an NR cell with autonomous gaps
11939.11.3 CGI reporting delay 11949.11A NR measurements with autonomous
gaps for RedCap 11959.11A.1 Introduction 11959.11A.2 CGI identification
of an NR cell with autonomous gaps 11959.11A.3 CGI reporting delay
11969.11A.4 CGI reporting scheduling restriction 11969.11D NR
measurements with autonomous gaps for ATG 11969.11D.1 Introduction
11979.11D.2 CGI identification of an NR cell with autonomous gaps
11979.11D.3 CGI reporting delay 11989.12 Measurement for Propagation
Delay Compensation 11989.12.1 Introduction 11989.12.2 Requirements
Applicability 11989.12.3 Measurement Capability 11989.12.4 Measurement
period requirements 11989.12.4.1 PRS Measurement Period 11989.12.4.2 TRS
Measurement Period 11999.12.5 Measurement Reporting Requirements
12009.12.6 Scheduling availability during measurement for Propagation
Delay Compensation 12009.12.7 Measurement restriction for measurement
for Propagation Delay Compensation 12019.12.8 Measurement requirement
for Propagation Delay Compensation with MUSIM gaps 12019.13 L1-RSRP
measurements for a cell with different PCI from serving cell 12019.13.1
Introduction 12019.13.2 Requirements Applicability 12019.13.3
Measurement Reporting Requirements 12029.13.3.1 Periodic Reporting
12029.13.3.2 Semi-Persistent Reporting 12029.13.3.3 Aperiodic Reporting
12039.13.4 L1-RSRP measurement requirements 12039.13.4.1 Inter-cell SSB
based L1-RSRP Reporting 12039.13.5 Measurement restriction for L1-RSRP
measurement 12069.13.5.1 Measurement restriction for SSB based L1-RSRP
12069.13.6 Scheduling availability of UE during L1-RSRP measurement
12079.13.6.1 Scheduling availability of UE performing L1-RSRP
measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1
12079.13.6.2 Scheduling availability of UE performing L1-RSRP
measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1
12079.13.6.3 Scheduling availability of UE performing L1-RSRP
measurement on FR2 12089.13.6.4 Scheduling availability of UE performing
L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA
12089.13.6.5 Scheduling availability of UE performing L1-RSRP
measurement in TDD bands on FR1 12089.14 NR intra-frequency L1-RSRP
measurements for neighbor cell 12099.14.1 Introduction 12099.14.2
Requirements Applicability 12099.14.3 Measurement Reporting Requirements
12099.14.3.1 Periodic Reporting 12109.14.3.2 Semi-Persistent Reporting
12109.14.3.3 Aperiodic Reporting 12109.14.4 Number of SSB frequency
layers, number of cells and number of SSBs 12109.14.5 L1-RSRP
intra-frequency measurement requirements without measurement gaps
12109.14.5.1 Intra-frequency SSB based L1-RSRP reporting 12109.14.6
Measurement restriction for L1-RSRP measurement 12139.14.6.1 Measurement
restriction for SSB based L1-RSRP 12139.14.7 Scheduling availability of
UE during L1-RSRP measurement 12149.14.7.1 Scheduling availability of UE
performing L1-RSRP measurement with a same subcarrier spacing as
PDSCH/PDCCH on FR1 12149.14.7.2 Scheduling availability of UE performing
L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH
on FR1 12149.14.7.3 Scheduling availability of UE performing L1-RSRP
measurement on FR2 12159.14.7.4 Scheduling availability of UE performing
L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA
12159.14.7.5 Scheduling availability of UE performing L1-RSRP
measurement in TDD bands on FR1 12159.15 NR inter-frequency L1-RSRP
measurements for neighbor cell 12169.15.1 Introduction 12169.15.2
Requirements Applicability 12169.15.3 Measurement Reporting Requirements
12169.15.3.1 Periodic Reporting 12179.15.3.2 Semi-Persistent Reporting
12179.15.3.3 Aperiodic Reporting 12179.15.4 Number of SSB frequency
layers, number of cells and number of SSBs 12179.15.5 L1-RSRP
inter-frequency measurement requirements with measurement gaps
12179.15.5.1 Inter-frequency SSB based L1-RSRP reporting 12179.15.6
L1-RSRP inter-frequency L1-RSRP measurement requirements without
measurement gaps 12199.15.6.1 Inter-frequency L1-RSRP measurement
requirements 12199.15.6.1.1 Inter-frequency SSB based L1-RSRP
measurement 12199.15.6.2 Measurement restriction for inter-frequency
L1-RSRP measurement 12229.15.6.2.1 Measurement restriction for SSB based
L1-RSRP 12229.15.6.3 Scheduling availability of UE during
inter-frequency L1-RSRP measurements 12229.15.6.3.1 Scheduling
availability of UE performing L1-RSRP measurement with a same subcarrier
spacing as PDSCH/PDCCH on FR1 12229.15.6.3.2 Scheduling availability of
UE performing L1-RSRP measurement with a different subcarrier spacing
than PDSCH/PDCCH on FR1 12239.15.6.3.3 Scheduling availability of UE
performing L1-RSRP measurement on FR2 12239.15.6.3.4 Scheduling
availability of UE performing L1-RSRP measurement on FR1 or FR2 in case
of FR1-FR2 inter-band CA 12239.15.6.3.5 Scheduling availability of UE
performing L1-RSRP measurement in TDD bands on FR1 122410 Measurement
Performance requirements 122310.1 NR measurements 122310.1.1
Introduction 122310.1.2 Intra-frequency RSRP accuracy requirements for
FR1 122310.1.2.1 Intra-frequency SS-RSRP accuracy requirements
122310.1.2.1.1 Absolute SS-RSRP Accuracy 122310.1.2.1.2 Relative SS-RSRP
Accuracy 122410.1.2.2 Void 122510.1.2.3 Intra-frequency CSI-RSRP
accuracy requirements 122510.1.2.3.1 Absolute CSI-RSRP Accuracy
122510.1.2.3.2 Relative CSI-RSRP Accuracy 122610.1.2B Intra-frequency
RSRP accuracy requirements for FR1 for CA/DC Idle Mode Measurements
122710.1.2B.1 Intra-frequency SS-RSRP accuracy requirements
122710.1.2B.1.1 Absolute SS-RSRP Accuracy 122710.1.2C Intra-frequency
RSRP accuracy requirements for FR1 SAN 122810.1.2C.1 Intra-frequency
SS-RSRP accuracy requirements 122810.1.2C.1.1 Absolute SS-RSRP Accuracy
122810.1.2C.1.2 Relative SS-RSRP Accuracy 122910.1.3 Intra-frequency
RSRP accuracy requirements for FR2 123010.1.3.1 Intra-frequency SS-RSRP
accuracy requirements 123010.1.3.1.1 Absolute SS-RSRP Accuracy
123010.1.3.1.2 Relative SS-RSRP Accuracy 123010.1.3.2 Void 123110.1.3.3
Intra-frequency CSI-RSRP accuracy requirements 123110.1.3.3.1 Absolute
CSI-RSRP Accuracy 123110.1.3.3.2 Relative CSI-RSRP Accuracy 123210.1.3B
Intra-frequency RSRP accuracy requirements for FR2 for CA/DC Idle Mode
Measurements 123310.1.3B.1 Intra-frequency SS-RSRP accuracy requirements
123310.1.3B.1.1 Absolute SS-RSRP Accuracy 123310.1.3C Intra-frequency
RSRP accuracy requirements for FR2-NTN 123310.1.3C.1 Intra-frequency
SS-RSRP accuracy requirements 123310.1.3C.1.1 Absolute SS-RSRP Accuracy
123310.1.3C.1.2 Relative SS-RSRP Accuracy 123410.1.4 Inter-frequency
RSRP accuracy requirements for FR1 123510.1.4.1 Inter-frequency SS-RSRP
accuracy requirements 123510.1.4.1.1 Absolute SS-RSRP Accuracy in FR1
123510.1.4.1.2 Relative SS-RSRP Accuracy in FR1 123610.1.4.2 Void
123710.1.4.3 Inter-frequency CSI-RSRP accuracy requirements
123710.1.4.3.1 Absolute CSI-RSRP Accuracy in FR1 123710.1.4.3.2 Relative
CSI-RSRP Accuracy in FR1 123810.1.4B Inter-frequency RSRP accuracy
requirements for FR1 for CA/DC Idle Mode Measurements 123910.1.4B.1
Inter-frequency SS-RSRP accuracy requirements 123910.1.4B.1.1 Absolute
SS-RSRP Accuracy in FR1 124010.1.4C Inter-frequency RSRP accuracy
requirements for FR1 SAN 124110.1.4C.1 Inter-frequency SS-RSRP accuracy
requirements 124110.1.4C.1.1 Absolute SS-RSRP Accuracy in FR1
124110.1.4C.1.2 Relative SS-RSRP Accuracy in FR1 124110.1.5
Inter-frequency RSRP accuracy requirements for FR2 124210.1.5.1
Inter-frequency SS-RSRP accuracy requirements 124210.1.5.1.1 Absolute
SS-RSRP Accuracy 124210.1.5.1.2 Relative SS-RSRP Accuracy 124210.1.5.2
Void 124310.1.5.3 Inter-frequency CSI-RSRP accuracy requirements
124310.1.5.3.1 Absolute CSI-RSRP Accuracy 124310.1.5.3.2 Relative
CSI-RSRP Accuracy 124410.1.5B Inter-frequency RSRP accuracy requirements
for FR2 for CA/DC Idle Mode Measurements 124510.1.5B.1 Inter-frequency
SS-RSRP accuracy requirements 124510.1.5B.1.1 Absolute SS-RSRP Accuracy
124510.1.5C Inter-frequency RSRP accuracy requirements for FR2-NTN
124610.1.5C.1 Inter-frequency SS-RSRP accuracy requirements
124610.1.5C.1.1 Absolute SS-RSRP Accuracy 124610.1.5C.1.2 Relative
SS-RSRP Accuracy 124610.1.6 RSRP Measurement Report Mapping 124710.1.7
Intra-frequency RSRQ accuracy requirements for FR1 124910.1.7.1
Intra-frequency SS-RSRQ accuracy requirements in FR1 124910.1.7.1.1
Absolute SS-RSRQ Accuracy in FR1 124910.1.7.2 Intra-frequency CSI-RSRQ
accuracy requirements 125010.1.7.2.1 Absolute CSI-RSRQ Accuracy
125010.1.7B Intra-frequency RSRQ accuracy requirements for FR1 for CA/DC
Idle Mode Measurements 125110.1.7B.1 Intra-frequency SS-RSRQ accuracy
requirements in FR1 125110.1.7B.1.1 Absolute SS-RSRQ Accuracy in FR1
125110.1.7C Intra-frequency RSRQ accuracy requirements for FR1 SAN
125210.1.7C.1 Intra-frequency SS-RSRQ accuracy requirements in FR1
125210.1.7C.1.1 Absolute SS-RSRQ Accuracy in FR1 125210.1.8
Intra-frequency RSRQ accuracy requirements for FR2 125310.1.8.1
Intra-frequency SS-RSRQ accuracy requirements in FR2 125310.1.8.1.1
Absolute SS-RSRQ Accuracy in FR2 125310.1.8.2 Intra-frequency CSI-RSRQ
accuracy requirements 125310.1.8.2.1 Absolute CSI-RSRQ Accuracy
125310.1.8B Intra-frequency RSRQ accuracy requirements for FR2 for CA/DC
Idle Mode Measurements 125410.1.8B.1 Intra-frequency SS-RSRQ accuracy
requirements in FR2 125410.1.8B.1.1 Absolute SS-RSRQ Accuracy in FR2
125410.1.8C Intra-frequency RSRQ accuracy requirements for FR2-NTN
125510.1.8C.1 Intra-frequency SS-RSRQ accuracy requirements in FR2-NTN
125510.1.8C.1.1 Absolute SS-RSRQ Accuracy in FR2-NTN 125510.1.9
Inter-frequency RSRQ accuracy requirements for FR1 125610.1.9.1
Inter-frequency SS-RSRQ accuracy requirements in FR1 125610.1.9.1.1
Absolute SS-RSRQ Accuracy in FR1 125610.1.9.1.2 Relative SS-RSRQ
Accuracy in FR1 125610.1.9.2 Inter-frequency CSI-RSRQ accuracy
requirements 125710.1.9.2.1 Absolute CSI-RSRQ Accuracy 125710.1.9.2.2
Relative CSI-RSRQ Accuracy 125810.1.9B Inter-frequency RSRQ accuracy
requirements for FR1 for CA/DC Idle Mode Measurements 125910.1.9B.1
Inter-frequency SS-RSRQ accuracy requirements in FR1 125910.1.9B.1.1
Absolute SS-RSRQ Accuracy in FR1 125910.1.9C Inter-frequency RSRQ
accuracy requirements for FR1 SAN 126010.1.9C.1 Inter-frequency SS-RSRQ
accuracy requirements in FR1 126010.1.9C.1.1 Absolute SS-RSRQ Accuracy
in FR1 126010.1.9C.1.2 Relative SS-RSRQ Accuracy in FR1 126110.1.10
Inter-frequency RSRQ accuracy requirements for FR2 126110.1.10.1
Inter-frequency SS-RSRQ accuracy requirements in FR2 126110.1.10.1.1
Absolute SS-RSRQ Accuracy in FR2 126110.1.10.1.2 Relative SS-RSRQ
Accuracy in FR2 126210.1.10.2 Inter-frequency CSI-RSRQ accuracy
requirements 126310.1.10.2.1 Absolute CSI-RSRQ Accuracy 126310.1.10.2.2
Relative CSI-RSRQ Accuracy 126410.1.10B Inter-frequency RSRQ accuracy
requirements for FR2 for CA/DC Idle Mode Measurements 126510.1.10B.1
Inter-frequency SS-RSRQ accuracy requirements in FR2 126510.1.10B.1.1
Absolute SS-RSRQ Accuracy in FR2 126510.1.10C Inter-frequency RSRQ
accuracy requirements for FR2-NTN 126610.1.10C.1 Inter-frequency SS-RSRQ
accuracy requirements in FR2-NTN 126610.1.10C.1.1 Absolute SS-RSRQ
Accuracy in FR2-NTN 126610.1.10C.1.2 Relative SS-RSRQ Accuracy in
FR2-NTN 126610.1.11 RSRQ report mapping 126710.1.12 Intra-frequency SINR
accuracy requirements for FR1 126810.1.12.1 Intra-frequency SS-SINR
accuracy requirements in FR1 126810.1.12.1.1 Absolute SS-SINR Accuracy
in FR1 126810.1.12.2 Intra-frequency CSI-SINR accuracy requirements in
FR1 126810.1.12.2.1 Absolute CSI-SINR Accuracy in FR1 126810.1.12C
Intra-frequency SINR accuracy requirements for FR1 SAN 126910.1.12C.1
Intra-frequency SS-SINR accuracy requirements in FR1 126910.1.12C.1.1
Absolute SS-SINR Accuracy in FR1 126910.1.13 Intra-frequency SINR
accuracy requirements for FR2 127010.1.13.1 Intra-frequency SS-SINR
accuracy requirements in FR2 127010.1.13.1.1 Absolute SS-SINR Accuracy
in FR2 127010.1.13.2 Intra-frequency CSI-SINR accuracy requirements in
FR2 127110.1.13.2.1 Absolute CSI-SINR Accuracy in FR2 127110.1.13C
Intra-frequency SINR accuracy requirements for FR2-NTN 127110.1.13C.1
Intra-frequency SS-SINR accuracy requirements in FR2-NTN
127110.1.13C.1.1 Absolute SS-SINR Accuracy in FR2-NTN 127110.1.14
Inter-frequency SINR accuracy requirements for FR1 127210.1.14.1
Inter-frequency SS-SINR accuracy requirements in FR1 127210.1.14.1.1
Absolute SS-SINR Accuracy in FR1 127210.1.14.1.2 Relative SS-SINR
Accuracy in FR1 127310.1.14.2 Inter-frequency CSI-SINR accuracy
requirements in FR1 127410.1.14.2.1 Absolute CSI-SINR Accuracy in FR1
127410.1.14.2.2 Relative CSI-SINR Accuracy in FR1 127510.1.14C
Inter-frequency SINR accuracy requirements for FR1 SAN 127610.1.14C.1
Inter-frequency SS-SINR accuracy requirements in FR1 127610.1.14C.1.1
Absolute SS-SINR Accuracy in FR1 127610.1.14C.1.2 Relative SS-SINR
Accuracy in FR1 127710.1.15 Inter-frequency SINR accuracy requirements
for FR2 127810.1.15.1 Inter-frequency SS-SINR accuracy requirements in
FR2 127810.1.15.1.1 Absolute SS-SINR Accuracy in FR2 127810.1.15.1.2
Relative SS-SINR Accuracy in FR2 127810.1.15.2 Inter-frequency CSI-SINR
accuracy requirements in FR2 127910.1.15.2.1 Absolute CSI-SINR Accuracy
in FR2 127910.1.15.2.2 Relative CSI-SINR Accuracy in FR2 128010.1.15C
Inter-frequency SINR accuracy requirements for FR2-NTN 128110.1.15C.1
Inter-frequency SS-SINR accuracy requirements in FR2-NTN
128110.1.15C.1.1 Absolute SS-SINR Accuracy in FR2-NTN 128110.1.15C.1.2
Relative SS-SINR Accuracy in FR2-NTN 128110.1.16 SINR report mapping
128210.1.16.1 SS-SINR and CSI-SINR measurement report mapping
128210.1.17 Power Headroom 128310.1.17.1 Power Headroom Report
128310.1.17.1.1 Power Headroom Report Mapping 128310.1.18 P~CMAX,c,f~
128310.1.18.1 Report Mapping 128310.1.19 L1-RSRP accuracy requirements
for FR1 128410.1.19.1 SSB based L1-RSRP accuracy requirements
128410.1.19.1.1 Absolute Accuracy 128410.1.19.1.2 Relative Accuracy
128510.1.19.2 CSI-RS based L1-RSRP accuracy requirements 128610.1.19.2.1
Absolute Accuracy 128610.1.19.2.2 Relative Accuracy 128710.1.19C L1-RSRP
accuracy requirements for FR1 SAN 128810.1.19C.1 SSB based L1-RSRP
accuracy requirements 128810.1.19C.1.1 Absolute Accuracy
128810.1.19C.1.2 Relative Accuracy 128910.1.19C.2 CSI-RS based L1-RSRP
accuracy requirements 128910.1.19C.2.1 Absolute Accuracy
128910.1.19C.2.2 Relative Accuracy 129010.1.19D LTM Intra-frequency
L1-RSRP accuracy requirements for FR1 129110.1.19D.1 SSB based
intra-frequency L1-RSRP accuracy requirements 129110.1.19D.1.1 Absolute
Accuracy 129110.1.19D.1.2 Relative Accuracy 129210.1.19E LTM
Inter-frequency L1-RSRP accuracy requirements for FR1 129210.1.19E.1 SSB
based Inter-frequency L1-RSRP accuracy requirements 129210.1.19E.1.1
Absolute Accuracy 129210.1.19E.1.2 Relative Accuracy 129310.1.20 L1-RSRP
accuracy requirements for FR2 129410.1.20.1 SSB based L1-RSRP accuracy
requirements 129410.1.20.1.1 Absolute Accuracy 129410.1.20.1.2 Relative
Accuracy 129510.1.20.2 CSI-RS based L1-RSRP accuracy requirements
129610.1.20.2.1 Absolute Accuracy 129610.1.20.2.2 Relative Accuracy
129610.1.20A LTM Intra-frequency L1-RSRP accuracy requirements for FR2
129710.1.20A.1 SSB based intra-frequency L1-RSRP accuracy requirements
129710.1.20A.1.1 Absolute Accuracy 129710.1.20A.1.2 Relative Accuracy
129810.1.20B LTM Inter-frequency L1-RSRP accuracy requirements for FR2
129910.1.20B.1 SSB based inter-frequency L1-RSRP accuracy requirements
129910.1.20B.1.1 Absolute Accuracy 129910.1.20B.1.2 Relative Accuracy
129910.1.20C L1-RSRP accuracy requirements for FR2-NTN 130010.1.20C.1
SSB based L1-RSRP accuracy requirements 130010.1.20C.1.1 Absolute
Accuracy 130010.1.20C.1.2 Relative Accuracy 130110.1.20C.2 CSI-RS based
L1-RSRP accuracy requirements 130110.1.20C.2.1 Absolute Accuracy
130110.1.20C.2.2 Relative Accuracy 130210.1.21 SFTD accuracy
requirements 130310.1.21.1 SFTD acuracy requirements for NE-DC
130310.1.21.2 SFTD acuracy requirements for NR-DC 130410.1.21.3
Inter-frequency SFTD acuracy requirements 130510.1.22 CLI measurement
accuracy requirements 130710.1.22.1 SRS-RSRP 130710.1.22.1.1 SRS-RSRP
Accuracy 130710.1.22.1.2 SRS-RSRP report mapping 130810.1.22.2 CLI-RSSI
130910.1.22.2.1 CLI-RSSI Accuracy 130910.1.22.2.2 CLI-RSSI report
mapping 131010.1.23 RSTD Measurements 131010.1.23.1 Introduction
131010.1.23.2 Measurement Accuracy Requirements 131010.1.23.3 Report
mapping 131810.1.23.3.1 Absolute DL RSTD Measurement Reporting
131810.1.23.3.2 Differential Reporting for DL RSTD Measurement
132110.1.23.3.3 Additional Path Report Mapping for DL RSTD 132410.1.23A
RSTD Measurements Based on PRS Aggregation 132810.1.23A.1 Introduction
132810.1.23A.3 Report Mapping 133510.1.23A.3.1 Absolute DL RSTD
Measurement Reporting 133510.1.23A.3.2 Differential Reporting for DL
RSTD Measurement 133510.1.23A.3.3 Additional Path Report Mapping for DL
RSTD 133510.1.24 PRS-RSRP Measurements 133510.1.24.1 Introduction
133510.1.24.2 Measurement Accuracy Requirements 133610.1.24.2.1 Absolute
PRS-RSRP accuracy 133610.1.24.2.2 Relative PRS RSRP accuracy
134010.1.24.3 Report mapping 134410.1.24.3.1 Absolute PRS-RSRP
Measurement Report Mapping 134410.1.24.3.2 Differential Report Mapping
for PRS-RSRP Measurement 134510.1.24A PRS-RSRP Measurements Based on PRS
Aggregation 134710.1.24A.1 Introduction 134710.1.24A.2 Measurement
Accuracy Requirements 134810.1.24A.2.1 Absolute PRS RSRP Accuracy
Requirement 134810.1.24A.2.2 Relative PRS RSRP Accuracy Requirement
134810.1.24A.3 Report Mapping 134810.1.24A.3.1 Absolute PRS-RSRP
Measurement Report Mapping 134810.1.24A.3.2 Differential Report Mapping
for PRS-RSRP Measurement 134810.1.25 UE Rx-Tx Time Difference
Measurements 134810.1.25.1 Introduction 134810.1.25.2 Measurement
Accuracy Requirements 134810.1.25.3 Report mapping 136010.1.25.3.1
Absolute UE Rx-Tx Measurement Report Mapping 136010.1.25.3.2
Differential UE Rx-Tx Measurement Report Mapping 136310.1.25.3.3
Additional Path Report Mapping for UE Rx-Tx Time Difference 136610.1.25A
UE Rx-Tx Time Difference Measurement Based on PRS Aggregation
136910.1.25A.1 Introduction 136910.1.25A.2 Measurement Accuracy
Requirements 137010.1.25A.3 Report mapping 138610.1.25C UE Rx-Tx Time
Difference Measurements in Satellite Accesss 138610.1.25C.1 Introduction
138610.1.25C.2 Measurement Accuracy Requirements 138610.1.25C.3 Report
mapping 138710.1.26 FR2 P-MPR report 138710.1.26.1 Report mapping
138710.1.27 L1-SINR accuracy requirements for FR1 138810.1.27.1 L1-SINR
accuracy requirements with CSI-RS based CMR and no dedicated IMR
configured 138810.1.27.1.1 Absolute Accuracy 138810.1.27.1.2 Relative
Accuracy 138910.1.27.2 L1-SINR accuracy requirements with SSB based CMR
and dedicated IMR configured 139010.1.27.2.1 Absolute Accuracy
139010.1.27.2.2 Relative Accuracy 139210.1.27.3 L1-SINR accuracy
requirements with CSI-RS based CMR and dedicated IMR configured
139410.1.27.3.1 Absolute Accuracy 139410.1.27.3.2 Relative Accuracy
139610.1.28 L1-SINR accuracy requirements for FR2 139810.1.29
Intra-frequency RSRQ accuracy requirements under CCA 140510.1.29.1
Intra-frequency SS-RSRQ accuracy requirements in FR1 140510.1.29.1.1
Absolute SS-RSRQ Accuracy 140510.1.30 Inter-frequency RSRQ accuracy
requirements under CCA 140510.1.30.1 Inter-frequency SS-RSRQ accuracy
requirements in FR1 140510.1.30.1.1 Absolute SS-RSRQ Accuracy
140510.1.30.1.2 Relative SS-RSRQ Accuracy 140610.1.31 Intra-frequency
SINR accuracy requirements under CCA 140710.1.31.1 Intra-frequency
SS-SINR accuracy requirements in FR1 140710.1.31.1.1 Absolute SS-SINR
Accuracy 140710.1.32 Inter-frequency SINR accuracy requirements under
CCA 140710.1.32.1 Inter-frequency SS-SINR accuracy requirements in FR1
140710.1.32.1.1 Absolute SS-SINR Accuracy 140710.1.32.1.2 Relative
SS-SINR Accuracy 140810.1.33 L1-RSRP accuracy requirements under CCA
140910.1.33.1 SSB based L1-RSRP accuracy requirements in FR1
140910.1.33.1.1 Absolute Accuracy 140910.1.33.1.2 Relative Accuracy
140910.1.34 RSSI measurements under CCA 141010.1.34.1 Intra-frequency
absolute RSSI measurement accuracy requirements in FR1 141010.1.34.2
Inter-frequency absolute RSSI measurement accuracy requirements in FR1
141010.1.34.3 RSSI measurement report mapping 141010.1.35 Channel
occupancy measurements under CCA 141110.1.35.1 Intra-frequency channel
occupancy measurement accuracy requirements in FR1 141110.1.35.2
Inter-frequency channel occupancy measurement accuracy requirements in
FR1 141110.1.36 Intra-frequency RSRP accuracy requirements under CCA
141110.1.36.1 Intra-frequency SS-RSRP accuracy requirements in FR1
141110.1.36.1.1 Absolute SS-RSRP Accuracy 141110.1.36.1.2 Relative
SS-RSRP Accuracy 141210.1.37 Inter-frequency RSRP accuracy requirements
under CCA 141210.1.37.1 Inter-frequency SS-RSRP accuracy requirements in
FR1 141210.1.37.1.1 Absolute SS-RSRP 141210.1.37.1.2 Relative SS-RSRP
Accuracy 141310.1.38 PRS-RSRPP Measurements 141410.1.38.1 Introduction
141410.1.38.2 Measurement Accuracy Requirements 141410.1.38.2.1 Absolute
PRS RSRPP accuracy 141410.1.38.3 Report mapping 141810.1.38.3.1 Absolute
PRS-RSRPP Measurement Report Mapping 141810.1.38.3.2 Differential Report
Mapping for PRS-RSRPP Measurement 141910.1.38A PRS-RSRPP Measurements
Based on PRS Aggregation 142010.1. 38A.1 Introduction 142010.1.38A.2
Measurement Accuracy Requirements 142110.1.38A.2.1 Absolute PRS RSRPP
accuracy 142110.1.38A.3 Report mapping 142110.1.38A.3.1 Absolute
PRS-RSRPP Measurement Report Mapping 142110.1.38A.3.2 Differential
Report Mapping for PRS-RSRPP Measurement 142110.1.39 UE Rx-Tx time
difference measurements for RTT-based PDC 142110.1.39.1 *Void*
142110.1.39.2 Measurement Accuracy Requirements for PRS 142110.1.39.3
Measurement Accuracy Requirements for TRS 142410.1.40 Void 142810.1.41
FR1 DPC report 142810.1.41.1 Report mapping 142810.1.42 TDCP Measurement
Report Mapping 142810.1.43 DL-RSCPD Measurements 143010.1.43.1
Introduction 143010.1.43.2.1 Measurement Accuracy Requirements
143010.1.43.3 Report Mapping 143710.1.43.3.1 Absolute DL RSCPD
Measurement Reporting 143710.1.44 DL-RSCP Measurements 143810.1.44.1
Introduction 143810.1.44.2 Measurement Accuracy Requirements
143810.1.44.3 Report Mapping 144610.1.44.3.1 Relative DL RSCP
Measurement Reporting 144610.1A NR measurements for RedCap 144710.1A.1
Introduction 144710.1A.2 Intra-frequency RSRP accuracy requirements for
FR1 144710.1A.2.1 Intra-frequency SS-RSRP accuracy requirements
144710.1A.2.1.1 Absolute SS-RSRP Accuracy 144710.1A.2.1.2 Relative
SS-RSRP Accuracy 144810.1A.3 Intra-frequency RSRP accuracy requirements
for FR2 144910.1A.3.1 Intra-frequency SS-RSRP accuracy requirements
144910.1A.3.1.1 Absolute SS-RSRP Accuracy 144910.1A.3.1.2 Relative
SS-RSRP Accuracy 144910.1A.4 Inter-frequency RSRP accuracy requirements
for FR1 144910.1A.4.1 Inter-frequency SS-RSRP accuracy requirements
144910.1A.4.1.1 Absolute SS-RSRP Accuracy in FR1 144910.1A.4.1.2
Relative SS-RSRP Accuracy in FR1 145010.1A.5 Inter-frequency RSRP
accuracy requirements for FR2 145110.1A.5.1 Inter-frequency SS-RSRP
accuracy requirements 145110.1A.5.1.1 Absolute SS-RSRP Accuracy
145110.1A.5.1.2 Relative SS-RSRP Accuracy 145110.1A.6 Intra-frequency
RSRQ accuracy requirements for FR1 145110.1A.6.1 Intra-frequency SS-RSRQ
accuracy requirements in FR1 145110.1A.6.1.1 Absolute SS-RSRQ Accuracy
in FR1 145110.1A.7 Intra-frequency RSRQ accuracy requirements for FR2
145210.1A.7.1 Intra-frequency SS-RSRQ accuracy requirements in FR2
145210.1A.7.1.1 Absolute SS-RSRQ Accuracy in FR2 145210.1A.8
Inter-frequency RSRQ accuracy requirements for FR1 145210.1A.8.1
Inter-frequency SS-RSRQ accuracy requirements in FR1 145210.1A.8.1.1
Absolute SS-RSRQ in FR1 145210.1A.8.1.2 Relative SS-RSRQ Accuracy in FR1
145310.1A.9 Inter-frequency RSRQ accuracy requirements for FR2
145410.1A.9.1 Inter-frequency SS-RSRQ accuracy requirements in FR2
145410.1A.9.1.1 Absolute SS-RSRQ Accuracy in FR2 145410.1A.9.1.2
Relative SS-RSRQ Accuracy in FR2 145410.1A.10 Intra-frequency SINR
accuracy requirements for FR1 145410.1A.10.1 Intra-frequency SS-SINR
accuracy requirements in FR1 145410.1A.10.1.1 Absolute SS-SINR Accuracy
in FR1 145410.1A.11 Intra-frequency SINR accuracy requirements for FR2
145510.1A.11.1 Intra-frequency SS-SINR accuracy requirements in FR2
145510.1A.11.1.1 Absolute SS-SINR Accuracy in FR2 145510.1A.12
Inter-frequency SINR accuracy requirements for FR1 145510.1A.12.1
Inter-frequency SS-SINR accuracy requirements in FR1 145510.1A.12.1.1
Absolute SS-SINR Accuracy in FR1 145510.1A.12.1.2 Relative SS-SINR
Accuracy in FR1 145610.1A.13 Inter-frequency SINR accuracy requirements
for FR2 145710.1A.13.1 Inter-frequency SS-SINR accuracy requirements in
FR2 145710.1A.13.1.1 Absolute SS-SINR Accuracy in FR2 145710.1A.13.1.2
Relative SS-SINR Accuracy in FR2 145710.1A.14 L1-RSRP accuracy
requirements for FR1 145710.1A.14.1 SSB based L1-RSRP accuracy
requirements 145710.1A.14.1.1 Absolute Accuracy 145710.1A.14.1.2
Relative Accuracy 145810.1A.14.2 CSI-RS based L1-RSRP accuracy
requirements 145910.1A.14.2.1 Absolute Accuracy 145910.1A.14.2.2
Relative Accuracy 146010.1A.15 L1-RSRP accuracy requirements for FR2
146110.1A.15.1 SSB based L1-RSRP accuracy requirements 146110.1A.15.1.1
Absolute Accuracy 146110.1A.15.1.2 Relative Accuracy 146110.1A.15.2
CSI-RS based L1-RSRP accuracy requirements 146110.1A.15.2.1 Absolute
Accuracy 146110.1A.15.2.2 Relative Accuracy 146110.1A.16 RSTD
Measurements for RedCap Positioning 146210.1A.16.1 Introduction
146210.1A.16.2 Measurement Accuracy Requirements 146210.1A.16.2.1
Accuracy requirement for RSTD measurement without RX FH 146210.1A.16.2.2
Accuracy requirement for RSTD measurement with RX FH 146910.1A.16.3
Report Mapping 148010.1A.16.3.1 Absolute DL RSTD Measurement Reporting
148010.1A.16.3.2 Differential Reporting for DL RSTD Measurement
148010.1A.16.3.3 Additional Path Report Mapping for DL RSTD 148010.1A.17
PRS-RSRP Measurements for RedCap positioning 148010.1A.17.1 Introduction
148010.1A.17.2 Measurement Accuracy Requirements 148010.1A.17.2.1
Absolute PRS RSRP Accuracy Requirement 148010.1A.17.2.2 Relative PRS
RSRP Accuracy Requirement 148310.1A.17.3 Report Mapping 148310.1A.17.3.1
Absolute PRS-RSRP Measurement Report Mapping 148310.1A.17.3.2
Differential Report Mapping for PRS-RSRP Measurement 148310.1A.18 UE
Rx-Tx Time Difference Measurements for RedCap Positioning 148410.1A.18.1
Introduction 148410.1A.18.2 Measurement Accuracy Requirements
148410.1A.18.2.1 UE Rx-Tx Accuracy Requirement for 2RX RedCap UE without
FH 148410.1A.18.2.2 UE Rx-Tx Accuracy Requirement for 1RX RedCap UE
without FH 148510.1A.18.2.3 UE Rx-Tx Accuracy Requirement for 2RX RedCap
UE with FH 149010.1A.18.3 Report mapping 150010.1A.18.3.1 Absolute UE
Rx-Tx Measurement Report Mapping 150010.1A.18.3.2 Differential UE Rx-Tx
Measurement Report Mapping 150010.1A.18.3.3 Additional Path Report
Mapping for UE Rx-Tx Time Difference 150010.1A.19 PRS-RSRPP Measurements
for RedCap Positioning 150010.1A.19.1 Introduction 150010.1A.19.2
Measurement Accuracy Requirements 150110.1A.19.2.1 Absolute PRS RSRPP
accuracy 150110.1A.19.3 Report mapping 150310.1A.19.3.1 Absolute
PRS-RSRPP Measurement Report Mapping 150310.1A.19.3.2 Differential
Report Mapping for PRS-RSRPP Measurement 150410.2 E-UTRAN measurements
150410.2.1 Introduction 150410.2.2 E-UTRAN RSRP measurements 150410.2.3
E-UTRAN RSRQ measurements 150410.2.4 E-UTRAN RSTD measurements
150410.2.5 E-UTRAN RS-SINR measurements 150510.2.6 E-UTRAN RSRP
measurements for CA/DC Idle Mode Measurements 150510.2.7 E-UTRAN RSRQ
measurements for CA/DC Idle Mode Measurements 150510.2A E-UTRAN
measurements for RedCap 150610.2A.1 Introduction 150610.2A.2 E-UTRAN
RSRP measurements 150610.2A.3 E-UTRAN RSRQ measurements 150610.2A.4
E-UTRAN RS-SINR measurements 150710.3 UTRAN FDD Measurements 150710.3.1
UTRAN FDD CPICH RSCP 150710.3.2 UTRAN FDD CPICH Ec/No 150810.4 V2X
measurements 150810.4.1 Introduction 150810.4.2 Intra-frequency
PSBCH-RSRP accuracy requirements for FR1 150810.4.2.1 PSBCH-RSRP
Absolute Accuracy 150810.4.2.2 PSBCH-RSRP Relative Accuracy 150910.4.2A
Intra-frequency PSBCH-RSRP accuracy requirements for FR1 under CCA
151010.4.2A.1 PSBCH-RSRP Absolute Accuracy 151010.4.2A.2 PSBCH-RSRP
Relative Accuracy 151010.4.3 Intra-Frequency SL-RSSI Measurement
Accuracy Requirements for FR1 151110.4.3.1 Absolute SL-RSSI Accuracy
151110.4.3A Intra-Frequency SL-RSSI Measurement Accuracy Requirements
for FR1 under CCA 151110.4.3A.1 Absolute SL-RSSI Accuracy 151110.4.4
Intra-Frequency L1 SL-RSRP Measurement Accuracy Requirements for FR1
151210.4.4.1 Absolute L1 SL-RSRP Accuracy 151210.4.4A Intra-Frequency L1
SL-RSRP Measurement Accuracy Requirements for FR1 under CCA
151210.4.4A.1 Absolute L1 SL-RSRP Accuracy 151210.4.5 Intra-Frequency
Discovery Signal Measurement Accuracy Requirements 151310.4.5.1 Absolute
Discovery Signal Measurement Accuracy 151310.4A NR Sidelink Measurements
for Positioning 151410.4A.1 Introduction 151410.4A.2 SL RSTD
measurements 151410.4A.2.1 Measurement Report Mapping 151410.4A.2.1.1
Absolute SL RSTD Measurement Reporting 151410.4A.2.2 Measurement
Accuracy Requirements 151510.4A.3 SL PRS-RSRP measurements 151710.4A.3.1
Measurement Report Mapping 151710.4A.3.1.1 Absolute SL PRS-RSRP
Measurement Report Mapping 151710.4A.3.2 Measurement Accuracy
Requirements 151810.4A.3.2.1 Absolute SL PRS-RSRP accuracy 151810.4A.4
SL Rx-Tx measurements 151910.4A.4.1 Measurement Report Mapping
151910.4A.4.1.1 Absolute SL Rx-Tx Measurement Report Mapping
151910.4A.4.2 Measurement Accuracy 152110.4A.5 SL PRS-RSRPP measurements
152210.4A.5.1 Measurement Report Mapping 152210.4A.5.1.1 Absolute SL
PRS-RSRPP Measurement Report Mapping 152210.4A.5.2 Measurement Accuracy
152310.4A.5.2.1 Introduction 152310.4A.5.2.2 Measurement Accuracy
Requirements 152410.4A.5.2.2.2 Absolute SL PRS-RSRPP accuracy
152410.4A.6 SL AoA measurements 152510.4A.6.1 Measurement Report Mapping
152510.4A.6.1.1 Absolute SL AoA Measurement Report Mapping 152510.4A.7
SL RTOA measurements 152610.4A.7.1 Measurement Report Mapping
152610.4A.7.1.1 Absolute SL RTOA Measurement Report Mapping 152611 Void
152812 V2X Requirements 151612.1 Introduction 151612.2 UE Transmit
Timing 151612.2.1 Introduction 151612.2.2 GNSS as synchronization
reference source 151712.2.3 NR Cell as synchronization reference source
151712.2.4 E-URTAN Cell as synchronization reference source 151712.2.5
SyncRef UE as synchronization reference source 151812.3 Initiation/Cease
of SLSS Transmissions 151812.3.1 Introduction 151812.3.1.1
Initiation/Cease of SLSS transmissions with NR cell as synchronization
reference source 151812.3.1.2 Initiation/Cease of SLSS transmissions
with EUTRAN cell as synchronization reference source 151912.3.1.3
Initiation/Cease of SLSS transmissions with GNSS as synchronization
reference source 152012.3.1.4 Initiation/Cease of SLSS transmissions
with SyncRef UE as synchronization reference source 152012.3A
Initiation/Cease of SLSS Transmissions with CCA 152112.3A.1 Introduction
152112.3A.1.1 Initiation/Cease of SLSS transmissions with NR cell as
synchronization reference source 152112.3A.1.2 Initiation/Cease of SLSS
transmissions with EUTRAN cell as synchronization reference source
152112.3A.1.3 Initiation/Cease of SLSS transmissions with GNSS as
synchronization reference source 152112.3A.1.4 Initiation/Cease of SLSS
transmissions with SyncRef UE as synchronization reference source
152212.4 Selection / Reselection of V2X Synchronization Reference Source
152212.4A Selection / Reselection of Sidelink Synchronization Reference
Source with CCA 152412.5 L1 SL-RSRP measurements 152612.5.1 Introduction
152612.5.2 SL-RSRP measurements 152612.6 Congestion Control measurements
152712.7 Interruption 152712.7.1 Interruptions to WAN due to V2X
Sidelink Communication 152712.7.2 V2X Sidelink Communication Dropping
due to synchronization source change 152712.7.3 Interruptions to WAN due
to switching between E-UTRA V2X Sidelink and NR V2X Sidelink 152912.7.4
Interruptions to WAN at transitions between active and non-active during
SL-DRX 152912.7.5 Interruptions to V2X sidelink at transitions between
active and non-active during DRX 153012.7.6 Interruptions to V2X
sidelink due to Active BWP switching Requirement 153012.7.7
Interruptions to WAN due to SyncRef UE detection and/or Sensing during
SL DRX off duration 153112.7.8 Interruptions at NR sidelink discovery
configuration 153112.7.9 Interruptions to WAN due to sidelink carrier
addition/release 153112.8 Reliability of GNSS signal 153212.9 Scheduling
availability 153212.9.1 Scheduling availability of UE switching between
E-UTRA sidelink and NR sidelink 153212.9.2 Scheduling availability of UE
switching between Uu uplink and V2X sidelink 153212.10 Selection /
Reselection of relay UE 153312.10.1 Introduction 153312.10.2 Selection /
Reselection of relay UE 153312.11 Component Carrier Addition and Release
Delay for Sidelink Carrier Aggregation 153312.12 Selection / Reselection
of Synchronization Reference Source for NR SL Carrier Aggregation
153412A NR Sidelink Measurements for Positioning 153512A.1 Introduction
153512A.2 SL RSTD measurements 153612A.2.1 Introduction 153612A.2.3
Measurement Capability 153612A.2.4 Measurement Reporting Requirements
153612A.2.5 Measurements Period Requirements 153612A.3 SL PRS-RSRP
measurements 153712A.3.1 Introduction 153712A.3.2 Requirements
Applicability 153812A.3.4 Measurement Reporting Requirements 153812A.3.5
Measurements Period Requirements 153812A.4 SL Rx-Tx measurements
153912A.4.1 Introduction 153912A.4.2 Requirements Applicability
153912A.4.3 Measurement Capability 153912A.4.4 Measurement Reporting
Requirements 153912A.4.5 Measurement Period Requirements 154012A.5 SL
PRS-RSRPP measurements 154112A.5.1 Introduction 154112A.5.2 Requirements
Applicability 154112A.5.3 Measurement Capability 154112A.5.4 Measurement
Reporting Requirements 154112A.5.5 Measurement Period Requirements
154112A.6 SL AoA measurements 154212A.6.1 Introduction 154212A.6.2
Requirements Applicability 154212A.6.3 Measurement Capability
154212A.6.4 Measurement Reporting Requirements 154212A.6.5 Measurement
Period Requirements 154312A.7 SL RTOA measurements 154312A.7.1
Introduction 154312A.7.2 Requirements Applicability 154412A.7.3
Measurement Capability 154412A.7.4 Measurement Reporting Requirements
154412A.7.5 Measurement Period Requirements 154413 Measurement
Performance Requirements for NR gNB 154513.1 UL-RTOA 154513.1.1 Report
mapping 154513.1.1A Additional Path Report Mapping for UL-RTOA 154913.2
gNB Rx-Tx time difference 155213.2.1 Report mapping 155213.2.1A
Additional Path Report Mapping for gNB Rx-Tx 155613.2.2 Measurement
Accuracy Requirements 155913.2.2.1 Introduction 155913.3 UL SRS RSRP
measurement 156113.3.1 Report mapping 156113.3.2 Measurement accuracy
requirements 156113.3.2.1 Introduction 156113.3.2.2 Requirements
156213.4 AoA/ZoA 156213.4.1 Report mapping 156213.5 Timing advance
(T~ADV~) 156313.5.1 Report mapping 156313.6 UL SRS RSRPP measurement
156413.6.1 Report mapping 156413.7 gNB Rx-Tx time difference
measurements for RTT-based PDC 156413.7.1 Report mapping 156413.7.2
Measurement Accuracy Requirements 156513.7.2.1 Introduction 156513.7.2.2
Requirements 156513.8 UL-RSCP measurement 156613.8.1 Report mapping
1566Annex A (normative): Test Cases 1567A.1 Purpose of annex 1567A.2
Requirement classification for statistical testing 1567A.2.1 Types of
requirements in TS 38.133 1567A.2.1.1 Time and delay requirements on UE
higher layer actions 1567A.2.1.2 Measurements of power levels, relative
powers and time 1568A.2.1.3 Implementation requirements 1568A.2.1.4
Physical layer timing requirements 1568A.2.1.5 Requirements under CCA
1568A.3 RRM test configurations 1569A.3.1 Reference measurement channels
1569A.3.1.1 PDSCH 1569A.3.1.1.1 FDD 1569A.3.1.1.2 TDD 1570A.3.1.2
CORESET for RMSI scheduling 1573A.3.1.2.1 FDD 1573A.3.1.2.2 TDD
1574A.3.1.3 CORESET for RMC scheduling 1576A.3.1.3.1 FDD 1576A.3.1.3.2
TDD 1578A.3.1.4 TDD UL/DL configuration 1582A.3.1A Reference measurement
channels under CCA 1584A.3.1A.1 PDSCH 1584A.3.1A.1.1 TDD 1584A.3.1A.2
CORESET for RMSI scheduling 1585A.3.1A.2.1 TDD 1585A.3.1A.3 CORESET for
RMC scheduling 1586A.3.1A.3.1 TDD 1586A.3.1A.4 TDD UL/DL configuration
1586A.3.1A.5 RMC burst transmission model 1587A.3.2.1 Generic OFDMA
Channel Noise Generator (OCNG) 1587A.3.2.1.1 OCNG pattern 1: Generic
OCNG pattern for all unused REs 1587A.3.2.1.2 OCNG pattern 2: Generic
OCNG pattern for all unused REs for 2AoA setup 1588A.3.2.1.3 OCNG
pattern 3: Generic OCNG pattern for unused REs in the same bandwidth as
CORESET 1588A.3.2.1.4 OCNG pattern 4: Generic OCNG pattern for all
unused REs outside SSB slot(s) 1589A.3.2.2 Void 1590A.3.3 Reference DRX
configurations 1590A.3.3.1 DRX Configuration 1: DRX cycle = 40 ms and
TAT = 500 ms 1590A.3.3.2 DRX Configuration 2: DRX cycle = 640 ms and TAT
= 500 ms 1590A.3.3.3 DRX Configuration 3: DRX cycle = 40 ms and TAT =
Infinity 1590A.3.3.4 DRX Configuration 4: DRX cycle = 160 ms and TAT =
Infinity 1591A.3.3.5 DRX Configuration 5: DRX cycle = 320 ms and TAT =
Infinity 1591A.3.3.6 DRX Configuration 6: DRX cycle = 320 ms and TAT =
500 ms 1591A.3.3.7 DRX Configuration 7: DRX cycle = 640 ms and TAT =
Infinity 1591A.3.3.8 DRX Configuration 8: DRX cycle = 320 ms and TAT =
Infinity 1592A.3.3.9 DRX Configuration 9: DRX cycle = 40 ms and TAT =
500 ms 1592A.3.3.10 DRX Configuration 10: DRX cycle = 640 ms and TAT =
500 ms 1592A.3.3.11 DRX Configuration 11: DRX cycle = 20 ms and TAT =
Infinity 1592A.3.3.12 DRX Configuration 12: DRX cycle = 640 ms and TAT =
Infinity 1593A.3.3.13 DRX Configuration X1: DRX cycle = 80 ms and TAT =
Infinity 1593A.3.3.14 DRX Configuration 14: DRX cycle = 160 ms and TAT =
Infinity 1593A.3.4 Test Cases with Different Channel Bandwidths
1593A.3.4.1 Test Cases with Different E-UTRA Channel Bandwidths
1593A.3.4.1.1 Introduction 1593A.3.4.1.2 Principle of testing 1594A.3.5
Test Cases for Synchronous and Asynchronous DC Operations 1594A.3.5.1
EN-DC Test Cases for Synchronous and Asynchronous EN-DC Operations
1594A.3.5.1.1 Introduction 1594A.3.5.1.2 Principle of Testing 1594A.3.6
Antenna configurations 1594A.3.6.1 Antenna configurations for FR1
1594A.3.6.1.1 Antenna connection for 4 Rx capable UEs 1594A.3.6.1.1.1
Introduction 1594A.3.6.1.1.2 Principle of testing 1594A.3.6.1.2 Antenna
connection for 8 Rx capable UEs 1597A.3.6.1.2.1 Introduction
1597A.3.6.1.2.2 Principle of testing 1597A.3.6.2 Antenna configurations
for FR2 1599A.3.6A Antenna configurations with unlicensed bands
1599A.3.6A.1 Antenna configurations for FR1 1599A.3.6A.1.1 Antenna
connection for 4 Rx capable UEs 1599A.3.6A.1.1.1 Introduction
1599A.3.6A.1.1.2 Principle of testing 1599A.3.7 EN-DC test setup
1601A.3.7.1 Introduction 1601A.3.7.2 E-UTRAN Serving Cell Parameters
1601A.3.7.2.1 E-UTRAN Serving Cell Parameters for Tests with NR Cell(s)
in FR1 1601A.3.7.2.2 E-UTRAN Serving Cell Parameters for Tests with NR
Cell(s) in FR2 1602A.3.7A NR FR1-FR2 test setup 1603A.3.7B EN-DC test
setup with unlicensed bands 1603A.3.7B.1 Introduction 1603A.3.7B.2
E-UTRAN Serving Cell Parameters 1603A.3.7B.2.1 E-UTRAN Serving Cell
Parameters for Tests with NR Cell(s) under CCA in FR1 1603A.3.7C
LTE-FR1/FR2 test setup 1604A.3.7D NE-DC test setup 1604A.3.7D.1
Introduction 1604A.3.7D.2 E-UTRAN Serving Cell Parameters 1604A.3.7D.2.1
E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR1
1604A.3.7D.2.2 E-UTRAN Serving Cell Parameters for Tests with NR Cell(s)
in FR2 1604A.3.8 PRACH configurations 1605A.3.8.1 Introduction
1605A.3.8.2 PRACH configurations in FR1 1605A.3.8.2.1 FR1 PRACH
configuration 1 1605A.3.8.2.2 FR1 PRACH configuration 2 1605A.3.8.2.3
FR1 PRACH configuration 3 1606A.3.8.2.4 FR1 PRACH configuration 4
1607A.3.8.2.5 FR1 PRACH configuration 5 1607A.3.8.2.6 FR1 PRACH
configuration 6 1608A.3.8.3 PRACH configurations in FR2 1608A.3.8.3.1
FR2 PRACH configuration 1 1608A.3.8.3.2 FR2 PRACH configuration 2
1609A.3.8.3.3 FR2 PRACH configuration 3 1610A.3.8.3.4 FR2 PRACH
configuration 4 1610A.3.8.3.5 FR2 PRACH configuration 5 1611A.3.8.3.6
FR2 PRACH configuration 6 1611A.3.8A PRACH configurations under CCA
1612A.3.8A.1 Introduction 1612A.3.8A.2 PRACH configurations in FR1
1612A.3.8A.2.1 FR1 PRACH configuration 1 under CCA 1612A.3.8A.2.2 FR1
PRACH configuration 2 under CCA 1613A.3.9 BWP configurations 1614A.3.9.1
Introduction 1614A.3.9.2 Downlink BWP configurations 1614A.3.9.2.1
Initial BWP 1614A.3.9.2.2 Dedicated BWP 1615A.3.9.3 Uplink BWP
configurations 1615A.3.9.3.1 Initial BWP 1615A.3.9.3.2 Dedicated BWP
1616A.3.9A BWP configurations for RedCap 1616A.3.9A.1 Introduction
1616A.3.9A.2 Downlink BWP configurations 1616A.3.9A.2.1 Dedicated BWP
1616A.3.9A.3 Uplink BWP configurations 1617A.3.9A.3.1 Dedicated BWP
1617A.3.10 SSB Configurations 1617A.3.10.1 SSB Configurations for FR1
1617A.3.10.1.1 SSB pattern 1 in FR1: SSB allocation for SSB SCS=15 kHz
in 10 MHz 1617A.3.10.1.5 SSB pattern 5 in FR1: SSB allocation for SSB
SCS=15 kHz starting from odd SFN in 10 MHz 1619A.3.10.1.6 SSB pattern 6
in FR1: SSB allocation for SSB SCS=30 kHz starting from odd SFN in 40
MHz 1619A.3.10.1.7 SSB pattern 7 in FR1: SSB allocation for SSB SCS=15
kHz in 10 MHz 1619A.3.10.1.8 SSB pattern 8 in FR1: SSB allocation for
SSB SCS=30 kHz in 40 MHz 1620A.3.10.1.9 SSB pattern 9 in FR1: SSB
allocation for SSB SCS=15 kHz in 10 MHz 1620A.3.10.1.10 SSB pattern 10
in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz 1620A.3.10.1.11 SSB
pattern 11 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz
1621A.3.10.1.12 SSB pattern 12 in FR1: SSB allocation for SSB SCS=30 kHz
in 40 MHz 1621A.3.10.1.13 SSB pattern 13 in FR1: SSB allocation for SSB
SCS=15 kHz in 3 MHz 1621A.3.10.2 SSB Configurations for FR2
1622A.3.10.2.1 SSB pattern 1 in FR2: SSB allocation for SSB SCS=120 kHz
in 100 MHz 1622A.3.10.2.2 SSB pattern 2 in FR2: SSB allocation for SSB
SCS=240 kHz in 100 MHz 1622A.3.10.2.3 SSB pattern 3 in FR2: SSB
allocation for SSB SCS=120 kHz in 100 MHz 1623A.3.10.2.4 SSB pattern 4
in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz 1623A.3.10.2.5 SSB
pattern 5 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz
1623A.3.10.2.6 SSB pattern 6 in FR2: SSB allocation for SSB SCS=240 kHz
in 100 MHz 1624A.3.10.2.7 SSB pattern 7 in FR2: SSB allocation for SSB
SCS=120 kHz in 100 MHz 1624A.3.10.2.8 SSB pattern 8 in FR2: SSB
allocation for SSB SCS=240 kHz in 100 MHz 1624A.3.10.2.9 SSB pattern 9
in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz 1625A.3.10.2.10
SSB pattern 10 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz
1625A.3.10.2.19 SSB pattern 19 in FR2: SSB allocation for SSB SCS=120
kHz in 100 MHz 1629A.3.10.2.20 SSB pattern 20 in FR2: SSB allocation for
SSB SCS=240 kHz in 100 MHz 1630A.3.10.2.21 SSB pattern 21 in FR2: SSB
allocation for SSB SCS=120 kHz in 100 MHz 1630A.3.10.2.22 SSB pattern 22
in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz 1631A.3.10.2.23
SSB pattern 23 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz
1631A.3.10.2.24 SSB pattern 24 in FR2: SSB allocation for SSB SCS=240
kHz in 100 MHz 1631A.3.10.2.25 SSB pattern 25 in FR2: SSB allocation for
SSB SCS=120 kHz in 100 MHz 1632A.3.10.2.26 SSB pattern 26 in FR2: SSB
allocation for SSB SCS=120 kHz in 100 MHz 1632A.3.10.2.27 SSB pattern 27
in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz 1633A.3.10A SSB
Configurations under CCA 1633A.3.10A.1 SSB Configurations under CCA for
FR1 1633A.3.10A.1.1 SSB pattern 1 under CCA for semi-static channel
access: SSB allocation for SSB SCS=30 kHz in 40 MHz 1633A.3.10A.1.2 SSB
pattern 2 under CCA for dynamic channel access: SSB allocation for SSB
SCS=30 kHz in 40 MHz 1634A.3.10A.1.3 SSB pattern 3 under CCA for
semi-static channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz
1634A.3.10A.1.4 SSB pattern 4 under CCA for dynamic channel access: SSB
allocation for SSB SCS=30 kHz in 40 MHz 1635A.3.10B SSB Configurations
for RedCap 1635A.3.10B.1 SSB Configurations for FR1 1635A.3.10B.1.1 SSB
pattern 1 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz
1635A.3.10B.1.2 SSB pattern 2 for RedCap in FR1: SSB allocation for SSB
SCS=30 kHz in 20 MHz 1636A.3.10B.1.3 SSB pattern 3 for RedCap in FR1:
SSB allocation for SSB SCS=30 kHz starting from odd SFN in 20 MHz
1636A.3.10B.1.4 SSB pattern 4 for RedCap in FR1: SSB allocation for SSB
SCS=15 kHz in 10 MHz 1637A.3.10B.1.5 SSB pattern 5 for RedCap in FR1:
SSB allocation for SSB SCS=30 kHz in 20 MHz 1637A.3.10B.1.6 SSB pattern
6 for RedCap in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz
1638A.3.10B.1.7 SSB pattern 7 for RedCap in FR1: SSB allocation for SSB
SCS=30 kHz in 20 MHz 1638A.3.10B.2 SSB Configurations for FR2
1639A.3.10B.2.1 SSB pattern 1 for RedCap in FR2: SSB allocation for SSB
SCS=120 kHz in 100 MHz 1639A.3.10B.2.2 SSB pattern 2 for RedCap in FR2:
SSB allocation for SSB SCS=120 kHz in 100 MHz 1639A.3.10B.2.3 SSB
pattern 3 for RedCap in FR2: SSB allocation for SSB SCS=120 kHz in 100
MHz 1640A.3.10B.2.4 SSB pattern 4 for RedCap in FR2: SSB allocation for
SSB SCS=240 kHz in 100 MHz 1640A.3.10B.2.5 SSB pattern 5 for RedCap in
FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz 1641A.3.11 SMTC
Configurations 1641A.3.11.1 SMTC pattern 1: SMTC period = 20 ms with
SMTC duration = 1 ms 1641A.3.11.2 SMTC pattern 2: SMTC period = 20 ms
with SMTC duration = 5 ms 1641A.3.11.3 SMTC pattern 3: SMTC period = 160
ms with SMTC duration = 1 ms 1641A.3.11.4 SMTC pattern 4: SMTC period =
20 ms with SMTC duration = 1 ms 1642A.3.11.5 SMTC pattern 5: SMTC period
= 20 ms with SMTC duration = 5 ms 1642A.3.11.6 SMTC pattern 6: SMTC
period = 20 ms with SMTC duration = 5 ms 1642A.3.11.7 SMTC pattern 7:
SMTC period = 20 ms with SMTC duration = 5 ms 1642A.3.11.8 SMTC pattern
8: SMTC period = 10 ms with SMTC duration = 1 ms 1642A.3.11.9 SMTC
pattern 9: SMTC period = 20 ms with SMTC duration = 1 ms 1642A.3.11.10
SMTC pattern 10: SMTC period = 80 ms with SMTC duration = 1 ms
1643A.3.11.11 SMTC pattern 11: SMTC period = 80 ms with SMTC duration =
5 ms 1643A.3.11.12 SMTC pattern 12: SMTC period = 20 ms with SMTC
duration = 5 ms 1643A.3.11A SMTC Configurations for RedCap 1643A.3.11A.0
Introduction 1643A.3.11A.1 SMTC pattern 1 for RedCap: SMTC period = 40
ms with SMTC duration = 1 ms 1644A.3.11A.2 SMTC pattern 2 for RedCap:
SMTC period = 80 ms with SMTC duration = 1 ms 1644A.3.11A.3 SMTC pattern
3 for RedCap: SMTC period = 40 ms with SMTC duration = 1 ms
1644A.3.11A.4 SMTC pattern 4 for RedCap: SMTC period = 80 ms with SMTC
duration = 5 ms 1644A.3.12 Test Cases with Different CC Configurations
1644A.3.12.1 EN-DC Test Cases with Different EN-DC Configurations
1644A.3.12.1.1 Introduction 1644A.3.12.1.2 Principle of testing
1644A.3.12.2 Carrier Aggregation Test Cases with Different CA
Configurations 1645A.3.12.2.1 Introduction 1645A.3.12.2.2 Principle of
testing 1645A.3.13 Test Cases in SA and EN-DC Operations 1645A.3.13.1
Introduction 1645A.3.13.2 Principle of Testing 1645A.3.13A Test Cases
involving E-UTRA/FR1 and FR2 carriers 1645A.3.13A.1 Introduction
1645A.3.13A.2 Principle of Testing in EN-DC 1646A.3.13A.3 Principle of
Testing in SA 1646A.3.13A.4 Principle of Testing in E-UTRA 1646A.3.13A.5
Principle of Testing in NR-DC 1647A.3.13B Test Cases for EN-DC and NE-DC
Operations 1647A.3.13B.1 Active BWP switch Test Cases for EN-DC and
NE-DC Operations 1647A.3.13B.1.1 Introduction 1647A.3.13B.1.2 Principle
of Testing 1647A.3.13B.2 SFTD accuracy Test Cases for EN-DC and NE-DC
Operations 1647A.3.13B.2.1 Introduction 1647A.3.13B.2.2 Principle of
Testing 1647A.3.14 CSI-RS configurations 1648A.3.14.1 FDD 1648A.3.14.2
TDD 1650A.3.15 Angle of Arrival (AoA) for FR2 RRM test cases
1655A.3.15.1 Setup 1: Single AoA in Rx beam peak direction 1655A.3.15.2
Setup 2: Single AoA in non Rx beam peak direction 1655A.3.15.2.1 Setup
2a: Single AoA in non Rx beam peak direction without change in direction
1655A.3.15.2.2 Setup 2b: Single AoA in non Rx beam peak direction with
change in direction 1656A.3.15.3 Setup 3: 2 AoAs 1656A.3.15.4 Setup 4: 2
AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak
1656A.3.15.4.1 Setup 4a: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in
non Rx beam peak without change in direction 1656A.3.15.4.2 Setup 4b: 2
AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak with change
in direction 1656A.3.15.4.3 Setup 4c: 2 AoAs, 1 AoA in Rx beam peak
direction, 1 in non Rx beam peak for power class 6 UE supporting
simultaneous reception from multiple directions 1656A.3.15.5 Setup 5: 2
AoAs for simultaneous reception with QCL Type-D 1657A.3.15.6 Setup 6: 3
AoAs for simultaneous reception with different QCL Type-D 1657A.3.15.7
Setup 7: 3 AoAs 1657A.3.15C Angle of Arrival (AoA) for FR2-NTN RRM test
cases 1657A.3.15C.1 Setup 1: Single AoA 1657A.3.15C.2 Setup 2: 2 AoAs
1658A.3.16 TCI State Configuration 1658A.3.16.1 Introduction
1658A.3.16.2 TCI states 1658A.3.16A Unified TCI State Configuration
1658A.3.16A.1 Introduction 1658A.3.16A.2 DLorJoint TCI states
1659A.3.16A.3 UL TCI states 1660A.3.16B LTM Candidate TCI State
Configuration 1660A.3.16B.1 Introduction 1660A.3.16B.2 LTM candidate
DLorJoint TCI states 1661A.3.16B.3 LTM candidate UL TCI states
1661A.3.17 Configurations of CSI-RS for tracking 1662A.3.17.1
Configuration of CSI-RS for tracking for FR1 1662A.3.17.1.1 FDD
1662A.3.17.1.2 TDD 1665A.3.17.2 Configuration of CSI-RS for tracking for
FR2 1669A.3.17.2.1 TDD 1669A.3.17.2.2 FDD 1672A.3.18 Additional
definitions related to OTA testing for FR2 RRM test cases 1672A.3.18.1
Introduction 1672A.3.18.2 PRACH Power Measurement 1672A.3.19 Test
applicability for DAPS handover 1672A.3.19.1 Introduction 1672A.3.19.2
Principle of testing 1672A.3.20 MsgA configurations 1673A.3.20.1
Introduction 1673A.3.20.2 MsgA configurations in FR1 1673A.3.20.2.1 FR1
MsgA configuration 1 1673A.3.20.2.2 FR1 MsgA configuration 2
1674A.3.20.3 MsgA configurations in FR2 1675A.3.20.3.1 FR2 MsgA
configuration 1 1675A.3.20.3.2 FR2 MsgA configuration 2 1676A.3.20A MsgA
configurations under CCA 1677A.3.20A.1 Introduction 1677A.3.20A.2 MsgA
configurations in FR1 1677A.3.20A.2.1 FR1 MsgA configuration 1 under CCA
1677A.3.20A.2.2 FR1 MsgA configuration 2 under CCA 1678A.**3.21** V2X
sidelink communication 1679A.3.21.1 Introduction 1679A.3.21.2 Reference
resource pool configurations for V2X Sidelink Communication 1679A.3.21.3
Reference measurement channels for V2X Sidelink Communication
1682A.3.21.4 Reference SL-DRX configurations 1683A.3.21.4.1 SL-DRX
Configuration 1: SL-DRX cycle = 40 ms 1683A.3.21.4.2 SL-DRX
Configuration 2: SL-DRX cycle = 320 ms 1683A.3.21.4.3 SL-DRX
Configuration 3: SL-DRX cycle = 640 ms 1683A.**3.21A** NR Sidelink
Measurements for Positioning 1683A.3.21A.1 Introduction 1683A.3.21A.2 NR
SL-PRS configurations 1684A.3.21A.2.1 NR SL-PRS configurations for FR1
1684A.3.22 CSI-IM configurations 1684A.3.22.1 FDD 1684A.3.22.2 TDD
1684A.3.23 Spatial Relation Configuration 1685A.3.23.1 Introduction
1685A.3.23.2 Spatial Relation 1686A.3.24 SRS configuration 1686A.3.25
Channel bandwidth (CBW) configurations 1688A.3.25.1 DL UE specific CBW
1688A.3.25.2 UL UE specific CBW 1689A.3.26 CCA model 1689A.3.26.1
Introduction 1689A.3.26.2 CCA model for operation on a carrier frequency
with CCA in FR1 1689A.3.26.2.1 DL CCA model 1689A.3.26.2.2 UL CCA model
1690A.3.26.3 CCA model for operation on a carrier frequency with CCA in
FR2-2 1691A.3.26.3.1 DL CCA model 1691A.3.26.3.2 UL CCA model
1691A.3.26.4 CCA model for operation on a sidelink carrier frequency
with CCA 1692A.3.26.4.1 CCA model for SyncRef UE 1692A.3.27 Void
1693A.3.27.1 Void 1693A.3.27.2 Void 1693A.3.27.3 Void 1693A.3.27.4 Void
1693A.3.27.5 Void 1693A.3.28 Discovery Burst Transmission Window
configuration under CCA 1693A.3.28.1 DBT Window pattern 1: DBT Window
period = 20 ms with DBT Window duration = 1 ms 1693A.3.29 Testing
principles for UE capable of only NR bands with shared spectrum access
1693A.3.29.1 Introduction 1693A.3.29.2 Principle of testing for UE
capable of EN-DC with only NR bands with shared spectrum access
1694A.3.29.3 Principle of testing for UE capable of SA operation with
only NR bands with shared spectrum access 1694A.3.30 CSI-RS
configurations for RRM 1695A.3.30.1 FDD 1695A.3.30.2 TDD 1695A.3.31 PRS
Configurations 1697A.3.31.1 PRS Configurations for FR1 1697A.3.31.1.1
PRS pattern 1 in FR1: SCS=15 kHz 1697A.3.31.1.2 PRS pattern 2 in FR1:
SCS=30 kHz 1698A.3.31.2 PRS Configurations for FR2 1699A.3.31.2.1 PRS
pattern 1 in FR2: SCS=120 kHz 1699A.3.32 NR sidelink discovery
1699A.3.32.1 Introduction 1699A.3.32.2 Reference resource pool
configurations for NR Sidelink Discovery 1699A.3.32.3 Principle of
Testing 1700A.3.33 PRS Processing Window (PPW) configurations 1700A.3.34
Testing principles for test cases related to PRS measurements
1700A.3.34.1 Introduction 1700A.3.34.2 Test cases in RRC\_INACTIVE state
1700A.3.34.3 Test cases for PRS measurements with gaps in RRC\_CONNECTED
state 1701A.3.34.4 Test cases for PRS measurements without gaps in
RRC\_CONNECTED state 1701A.3.34.5 Testing principles for positioning
measurements by aggregating PRS resources from multiple PFLs
1701A.3.34.6 Testing principles for carrier phase measurement for
positioning 1702A.3.34.7 Test cases in RRC\_IDLE state 1702A.3.35
Testing principle for RedCap UE 1702A.3.35.1 Introduction 1702A.3.35.2
Principle of testing for FR1 1702A.3.35.3 Principle of testing for FR2
1702A.3.35.4 Principle of testing for PRS measurement 1702A.3.36 Testing
related to Satellite access 1703A.3.36.1 Introduction 1703A.3.36.1
Introduction 1703A.3.36.2 Principle of testing GSO and NGSO scenarios
1703A.3.36.2 Principle of testing different RRM requirements
1703A.3.36.3 Principle of testing different ephemeris formats
1704A.3.36.4 General setup for SIB19 1706A.3.36.5 Satellite specific
parameters configuration 1707A.3.36.5.1 Satellite specific configuration
for serving cell 1707A.3.36.5.2 Satellite specific configuration for
neighbour cell 1707A.3.37 Reference Cell DTX configurations 1708A.3.37.1
Cell DTX Configuration 1: Cell DTX cycle = 160 ms and TAT = Infinity
1708A.3.38 DL-PRS Measurement Time Window configurations 1708A.4 EN-DC
tests with all NR cells in FR1 1709A.4.1 Void 1709A.4.2 Void 1709A.4.3
RRC\_CONNECTED state mobility 1709A.4.3.1 Void 1709A.4.3.2 RRC
Connection Mobility Control 1709A.4.3.2.1 Void 1709A.4.3.2.2 Random
Access 1709A.4.3.2.2.1 4-step RA type contention based random access
test in FR1 for PSCell in EN-DC 1709A.4.3.2.2.2 4-step RA type n
on-contention based random access test in FR1 for PSCell in EN-DC
1712A.4.3.2.2.3 2-step RA type contention based random access test in
FR1 for PSCell in EN-DC 1714A.4.3.2.2.4 2-step RA type non-contention
based random access test in FR1 for PSCell in EN-DC 1717A.4.3.2.3 Void
1719A.4.3.3 Handover with PSCell from EN-DC to EN-DC with known target
PSCell in FR1 1719A.4.3.3.1 Test Purpose and Environment 1719A.4.3.3.2
Test Requirements 1722A.4.4 Timing 1723A.4.4.1 UE transmit timing
1723A.4.4.1.1 NR UE Transmit Timing Test for FR1 1723A.4.4.1.1.1 Test
Purpose and environment 1723A.4.4.1.1.2 Test requirements 1725A.4.4.1.2
NR UE Transmit Timing Test for two TRPs in FR1 1726A.4.4.1.2.1 Test
Purpose and environment 1726A.4.4.1.2.2 Test requirements 1729A.4.4.2 UE
timer accuracy 1730A.4.4.3 Timing advance 1730A.4.4.3.1 EN-DC FR1 timing
advance adjustment accuracy 1730A.4.4.3.1.1 Test Purpose and Environment
1730A.4.4.3.1.2 Test Parameters 1730A.4.4.3.1.3 Test Requirements
1733A.4.5 Signaling characteristics 1733A.4.5.1 Radio link Monitoring
1733A.4.5.1.1 Radio Link Monitoring Out-of-sync Test for FR1 PSCell
configured with SSB-based RLM RS in non-DRX mode 1733A.4.5.1.1.1 Test
Purpose and Environment 1733A.4.5.1.1.2 Test Requirements 1737A.4.5.1.2
Radio Link Monitoring In-sync Test for FR1 PSCell configured with
SSB-based RLM RS in non-DRX mode 1737A.4.5.1.2.1 Test Purpose and
Environment 1737A.4.5.1.2.2 Test Requirements 1740A.4.5.1.3 Radio Link
Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM
RS in DRX mode 1740A.4.5.1.3.1 Test Purpose and Environment
1740A.4.5.1.3.2 Test Requirements 1743A.4.5.1.4 Radio Link Monitoring
In-sync Test for FR1 PSCell configured with SSB-based RLM RS in DRX mode
1743A.4.5.1.4.1 Test Purpose and Environment 1743A.4.5.1.4.2 Test
Requirements 1746A.4.5.1.5 EN-DC Radio Link Monitoring Out-of-sync Test
for FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode
1746A.4.5.1.5.1 Test Purpose and Environment 1746A.4.5.1.5.2 Test
Requirements 1749A.4.5.1.6 EN-DC Radio Link Monitoring In-sync Test for
FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode
1750A.4.5.1.6.1 Test Purpose and Environment 1750A.4.5.1.6.2 Test
Requirements 1752A.4.5.1.7 EN-DC Radio Link Monitoring Out-of-sync Test
for FR1 PSCell configured with CSI-RS-based RLM in DRX mode
1753A.4.5.1.7.1 Test Purpose and Environment 1753A.4.5.1.7.2 Test
Requirements 1755A.4.5.1.8 EN-DC Radio Link Monitoring In-sync Test for
FR1 PSCell configured with CSI-RS-based RLM in DRX mode 1756A.4.5.1.8.1
Test Purpose and Environment 1756A.4.5.1.8.2 Test Requirements
1759A.4.5.1.9 Radio Link Monitoring Out-of-sync Test for FR1 PSCell
configured with SSB-based RLM RS for UE fulfilling relaxed measurement
criterion 1759A.4.5.1.9.1 Test Purpose and Environment 1759A.4.5.1.10
EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured
with CSI-RS-based RLM in non-DRX mode when CD-SSB is outside active BWP
1762A.4.5.1.10.1 Test Purpose and Environment 1762A.4.5.1.11 Radio Link
Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM
RS in non-DRX mode when CD-SSB is outside active BWP 1762A.4.5.1.11.1
Test Purpose and Environment 1762A.4.5.1.11.2 Test Requirements
1763A.4.5.1.12 EN-DC Radio Link Monitoring Out-of-sync Test for FR1
PSCell configured with SSB-based RLM RS in non-DRX mode for UE
supporting NCD-SSB based measurement outside active BWP 1763A.4.5.1.12.1
Test Purpose and Environment 1763A.4.5.1.12.2 Test Requirements
1766A.4.5.2 Interruption 1766**A.4.5.2.1** E-UTRAN -- NR FR1
interruptions at transitions between active and non-active during DRX in
synchronous EN-DC 1766A.4.5.2.1.1 Test Purpose and Environment
1766A.4.5.2.1.2 Test Requirements 1768**A.4.5.2.2** E-UTRAN -- NR FR1
interruptions at transitions between active and non-active during DRX in
asynchronous EN-DC 1768A.4.5.2.2.1 Test Purpose and Environment
1768A.4.5.2.2.2 Test Requirements 1770**A.4.5.2.3** E-UTRAN -- NR FR1
interruptions during measurements on deactivated NR SCC in synchronous
EN-DC 1770A.4.5.2.3.1 Test Purpose and Environment 1770A.4.5.2.3.2 Test
Requirements 1774A.4.5.2.4 E-UTRAN -- NR FR1 interruptions during
measurements on deactivated NR SCC in asynchronous EN-DC 1775A.4.5.2.4.1
Test Purpose and Environment 1775A.4.5.2.4.2 Test Requirements
1779**A.4.5.2.5** E-UTRAN -- NR FR1 interruptions during measurements on
deactivated E-UTRAN SCC in synchronous EN-DC 1779A.4.5.2.5.1 Test
Purpose and Environment 1779A.4.5.2.5.2 Test Requirements
1781**A.4.5.2.6** E-UTRAN -- NR FR1 interruptions during measurements on
deactivated E-UTRAN SCC in asynchronous EN-DC 1782A.4.5.2.6.1 Test
Purpose and Environment 1782A.4.5.2.6.2 Test Requirements 1784A.4.5.2.7
Void 1784**A.4.5.2.8** **E-UTRAN - NR FR1 i**nterruptions at NR SRS
carrier based switching in asynchronous EN-DC 1784A.4.5.2.8.1 Test
Purpose and Environment 1784A.4.5.2.8.2 Test Requirements
1787**A.4.5.2.9** E-UTRAN -- NR interruptions at E-UTRA SRS carrier
based switching 1787A.4.5.2.9.1 Test Purpose and Environment
1787A.4.5.2.9.2 Test Requirements 1790**A.4.5.2.10** E-UTRAN -- NR FR1
interruptions due to RRM and RLM/BFD measurements on deactivated NR
PSCell 1790A.4.5.2.10.1 Test Purpose and Environment 1790A.4.5.2.10.2
Test Requirements 1792**A.4.5.2.11** **E-UTRAN - NR FR1 i**nterruptions
at NR SRS antenna port switching with 1 SRS symbol in a slot in
synchronous EN-DC 1792A.4.5.2.11.1 Test Purpose and Environment
1792A.4.5.2.11.2 Test Requirements 1795**A.4.5.2.12** **E-UTRAN - NR FR1
i**nterruptions at NR SRS antenna port switching in asynchronous EN-DC
1795A.4.5.2.12.1 Test Purpose and Environment 1795A.4.5.3 SCell
Activation and Deactivation Delay 1799A.4.5.3.1 SCell Activation and
deactivation of known SCell in FR1 for 160 ms SCell measurement cycle
1799A.4.5.3.1.1 Test Purpose and Environment 1799A.4.5.3.1.2 Test
Requirements 1805A.4.5.3.2 SCell Activation and deactivation of known
SCell in FR1 for 640 ms SCell measurement cycle 1805A.4.5.3.2.1 Test
Purpose and Environment 1805A.4.5.3.2.2 Test Requirements 1805A.4.5.3.3
SCell Activation and deactivation of unknown SCell in FR1
1806A.4.5.3.3.1 Test Purpose and Environment 1806A.4.5.3.3.2 Test
Requirements 1806A.4.5.3.4 SCell Activation and deactivation of multiple
unknown SCells in FR1 with single activation/deactivation command
1806A.4.5.3.4.1 Test Purpose and Environment 1807A.4.5.3.4.2 Test
Requirements 1809A.4.5.3.5 Direct SCell activation at SCell addition of
known SCell in FR1 1809A.4.5.3.5.1 Test Purpose and Environment
1809A.4.5.3.5.2 Test Requirements 1814A.4.5.3.6 Fast SCell Activation of
known SCell in FR1 for 160 ms SCell measurement cycle 1814A.4.5.3.6.1
Test Purpose and Environment 1814A.4.5.3.6.2 Test Requirements
1817A.4.5.3.7 Fast SCell Activation of known SCell in FR1 for 640 ms
SCell measurement cycle 1818A.4.5.3.7.1 Test Purpose and Environment
1818A.4.5.3.7.2 Test Requirements 1818A.4.5.3.8 SCell Activation and
deactivation of unknown SCell in FR1 for UE capable of short measurement
interval 1818A.4.5.3.8.1 Test Purpose and Environment 1818A.4.5.3.8.2
Test Requirements 1819A.4.5.3.9 SCell Activation of unknown SCell with
valid L3 measurement results in FR1 for 160 ms SCell measurement cycle
1820A.4.5.3.9.1 Test Purpose and Environment 1820A.4.5.3.9.2 Test
Requirements 1825A.4.5.3.10 SCell Activation of multiple unknown SCells
in FR1 with L3 reporting with single activation/deactivation command in
non-DRX 1826A.4.5.3.10.1 Test Purpose and Environment 1826A.4.5.3.10.2
Test Requirements 1828A.4.5.3.11 TRS-based SCell Activation of SSB-less
SCell in FR1 collocated inter-band 1829A.4.5.3.11.1 Test Purpose and
Environment 1829A.4.5.3.11.2 Test Requirements 1832A.4.5.3.12 Inter-band
SSB-less Scell activation using A-TRS 1833A.4.5.3.12.1 Test Purpose and
Environment 1833A.4.5.3.12.2 Test Requirements 1836A.4.5.4 UE UL carrier
RRC reconfiguration Delay 1836A.4.5.4.1 UE UL carrier RRC
reconfiguration Delay 1836A.4.5.4.1.1 Test Purpose and Environment
1836A.4.5.4.1.2 Test Requirements 1841A.4.5.5 Beam Failure Detection and
Link recovery procedures 1841A.4.5.5.1 EN-DC Beam Failure Detection and
Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR
in non-DRX mode 1841A.4.5.5.1.1 Test Purpose and Environment
1841A.4.5.5.1.2 Test Requirements 1845A.4.5.5.2 EN-DC Beam Failure
Detection and Link Recovery Test for FR1 PSCell configured with
SSB-based BFD and LR in DRX mode 1845A.4.5.5.2.1 Test Purpose and
Environment 1845A.4.5.5.2.2 Test Requirements 1848A.4.5.5.3 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 PSCell configured with
CSI-RS-based BFD and LR in non-DRX mode 1849A.4.5.5.3.1 Test Purpose and
Environment 1849A.4.5.5.3.2 Test Requirements 1852A.4.5.5.4 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 PSCell configured with
CSI-RS-based BFD and LR in DRX mode 1853A.4.5.5.4.1 Test Purpose and
Environment 1853A.4.5.5.4.2 Test Requirements 1856A.4.5.5.5 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 SCell configured with
CSI-RS-based BFD and SSB-based LR in non-DRX mode 1857A.4.5.5.5.1 Test
Purpose and Environment 1857A.4.5.5.5.2 Test Requirements 1860A.4.5.5.6
EN-DC Beam Failure Detection and Link Recovery Test for FR1 SCell
configured with CSI-RS-based BFD and SSB-based LR in DRX mode
1861A.4.5.5.6.1 Test Purpose and Environment 1861A.4.5.5.6.2 Test
Requirements 1864A.4.5.5.7 EN-DC TRP specific Beam Failure Detection and
Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR
in non-DRX mode 1865A.4.5.5.7.1 Test Purpose and Environment
1865A.4.5.5.7.2 Test Requirements 1868A.4.5.5.8 EN-DC TRP specific Beam
Failure Detection and Link Recovery Test for FR1 SCell configured with
CSI-RS-based BFD and SSB-based LR in non-DRX mode 1869A.4.5.5.8.1 Test
Purpose and Environment 1869A.4.5.5.8.2 Test Requirements 1873A.4.5.6
Active BWP switch 1873A.4.5.6.1 DCI-based and Timer-based Active BWP
Switch 1873A.4.5.6.1.1 E-UTRAN -- NR PSCell FR1 DL active BWP switch in
non-DRX in synchronous EN-DC 1873A.4.5.6.1.2 E-UTRAN -- NR PSCell FR1 DL
active BWP switch with FR1 SCell in non-DRX in synchronous EN-DC
1877A.4.5.6.2 RRC-based Active BWP Switch 1882A.4.5.6.3 Simultaneous
DCI-based and Timer-based Active BWP Switch on multiple CCs
1885A.4.5.6.3.1 Simultaneous E-UTRAN -- NR PSCell FR1 DL active BWP
switch in non-DRX in EN-DC on multiple CCs 1885A.4.5.6.4 Simultaneous
RRC-based Active BWP Switch on multiple CCs 1890A.4.5.6.4.1 E-UTRAN --
NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC on
multiple CCs 1890A.4.5.6.4.1.1 Test Purpose and Environment
1890A.4.5.6.4.1.2 Test Requirements 1894A.4.5.6.4.2 E-UTRAN -- NR FR1
PSCell SCell dormancy switch of two FR1 SCells inside active time
1894A.4.5.6.4.2.1 Test Purpose and Environment 1894A.4.5.6.4.2.2 Test
Requirements 1900A.4.5.6.5 SCell dormancy switch 1900A.4.5.6.5.1 E-UTRAN
-- NR FR1 PSCell SCell dormancy switch of single FR1 SCell outside
active time 1900A.4.5.6.5.2 E-UTRAN -- NR FR1 PSCell SCell dormancy
switch of two FR1 SCells inside active time 1905A.4.5.6.5.2.1 Test
Purpose and Environment 1905A.4.5.6.5.2.2 Test Requirements 1909A.4.5.7
PSCell addition and release delay 1909A.4.5.7.1 Addition and Release
Delay of known NR PSCell 1909A.4.5.7.1.1 Test purpose and environment
1909A.4.5.7.1.2 Test Requirements 1912A.4.5.8 DL Interruptions at
switching between two uplink carriers 1912A.4.5.8.1 Test Purpose and
Environment 1912A.4.5.8.2 Test Requirements 1915A.4.5.9 UE specific CBW
change 1915A.4.5.9.1 UE specific CBW change on FR1 NR PSCell with
non-DRX in synchronous EN- DC 1915A.4.5.9.1.1 Test Purpose and
Environment 1915A.4.5.9.1.2 Test Requirements 1917A.4.5.10 PSCell
activation and deactivation delay 1917A.4.5.10.1 PSCell activation and
deactivation delay 1917A.4.5.10.1.1 Test purpose and environment
1917A.4.5.10.1.2 Test Requirements 1920A.4.5.11 Conditional PSCell
addition and release delay (FR1 EN-DC) 1920A.4.5.11.1 Conditional PSCell
Addition and Release Delay 1920A.4.5.11.1.1 Test purpose and environment
1920A.4.5.11.1.2 Test Parameters 1920A.4.5.11.1.3 Test Requirements
1923A.4.6 Measurement procedure 1923A.4.6.1 Intra-frequency Measurements
1923A.4.6.1.1 EN-DC event triggered reporting tests without gap under
non-DRX 1923A.4.6.1.1.1 Test purpose and Environment 1923A.4.6.1.1.2
Test parameters 1923A.4.6.1.1.3 Test Requirements 1925A.4.6.1.2 EN-DC
event triggered reporting tests without gap under DRX 1925A.4.6.1.2.1
Test purpose and Environment 1925A.4.6.1.2.2 Test parameters
1925A.4.6.1.2.2 Test Requirements 1927A.4.6.1.3 EN-DC event triggered
reporting tests with per-UE gaps under non-DRX 1927A.4.6.1.3.1 Test
purpose and Environment 1927A.4.6.1.3.2 Test parameters 1928A.4.6.1.3.3
Test Requirements 1930A.4.6.1.4 EN-DC event triggered reporting tests
with per-UE gaps under DRX 1930A.4.6.1.4.1 Test purpose and Environment
1930A.4.6.1.4.2 Test parameters 1930A.4.6.1.4.3 Test Requirements
1932A.4.6.1.5 EN-DC event triggered reporting tests without gap under
non-DRX with SSB index reading 1932A.4.6.1.5.1 Test purpose and
Environment 1932A.4.6.1.5.2 Test parameters 1932A.4.6.1.5.3 Test
Requirements 1934A.4.6.1.6 EN-DC event triggered reporting tests with
SSB index reading with per-UE gaps 1934A.4.6.1.6.1 Test purpose and
Environment 1934A.4.6.1.6.2 Test parameters 1934A.4.6.1.6.3 Test
Requirements 1935A.4.6.1.7 EN-DC event triggered reporting tests under
DRX for UE configured with highSpeedMeasFlag-r16 1936A.4.6.1.7.1 Test
purpose and Environment 1936A.4.6.1.7.2 Test parameters 1936A.4.6.1.7.3
Test Requirements 1938A.4.6.1.8 EN-DC event triggered reporting tests
for FR1 cell without SSB time index detection when DRX is used for UE
configured with ***highSpeedMeasCA-Scell-r17*** 1938A.4.6.1.8.1 Test
Purpose and Environment 1938A.4.6.1.8.2 Test Requirements 1941A.4.6.1.9
EN-DC event triggered reporting tests without gap under non-DRX with
NCD-SSB 1941A.4.6.1.9.1 Test purpose and Environment 1941A.4.6.1.9.2
Test parameters 1942A.4.6.1.9.3 Test Requirements 1943A.4.6.1.10 EN-DC
event triggered reporting tests without gap under non-DRX when CD-SSB is
outside active BWP 1944A.4.6.110.1 Test purpose and Environment
1944A.4.6.1.10.2 Test Requirements 1944A.4.6.2 Inter-frequency
Measurements 1944A.4.6.2.1 EN-DC event triggered reporting tests for FR1
cell without SSB time index detection when DRX is not used
1944A.4.6.2.1.1 Test Purpose and Environment 1944A.4.6.2.1.2 Test
Requirements 1947A.4.6.2.2 EN-DC event triggered reporting tests for FR1
cell without SSB time index detection when DRX is used 1947A.4.6.2.2.1
Test Purpose and Environment 1947A.4.6.2.2.2 Test Requirements
1949A.4.6.2.3 Void 1950A.4.6.2.4 Void 1950A.4.6.2.5 EN-DC event
triggered reporting tests for FR1 cell with SSB time index detection
when DRX is not used 1950A.4.6.2.5.1 Test Purpose and Environment
1950A.4.6.2.5.2 Test Requirements 1952A.4.6.2.6 EN-DC event triggered
reporting tests for FR1 cell with SSB time index detection when DRX is
used 1952A.4.6.2.6.1 Test Purpose and Environment 1952A.4.6.2.6.2 Test
Requirements 1955A.4.6.2.7 Void 1955A.4.6.2.8 Void 1955A.4.6.2.9 EN-DC
event triggered reporting tests for FR1 cell without SSB time index
detection when DRX is used for UE configured with
highSpeedMeasInterFreq-r17 1955A.4.6.2.9.1 Test Purpose and Environment
1955A.4.6.2.9.2 Test Requirements 1958A.4.6.3 Void 1958A.4.6.4 L1-RSRP
measurement for beam reporting 1958A.4.6.4.1 SSB based L1-RSRP
measurement when DRX is not used 1958A.4.6.4.1.1 Test Purpose and
Environment 1958A.4.6.4.1.2 Test parameters 1959A.4.6.4.1.3 Test
Requirements 1960A.4.6.4.2 SSB based L1-RSRP measurement when DRX is
used 1960A.4.6.4.2.1 Test Purpose and Environment 1960A.4.6.4.2.2 Test
parameters 1961A.4.6.4.2.3 Test Requirements 1962A.4.6.4.3 CSI-RS based
L1-RSRP measurement when DRX is not used 1962A.4.6.4.3.1 Test Purpose
and Environment 1962A.4.6.4.3.2 Test parameters 1963A.4.6.4.3.3 Test
Requirements 1964A.4.6.4.4 CSI-RS based L1-RSRP measurement when DRX is
used 1964A.4.6.4.4.1 Test Purpose and Environment 1964A.4.6.4.4.2 Test
parameters 1965A.4.6.4.4.3 Test Requirements 1966A.4.6.4.5 SSB based
L1-RSRP measurement when DRX is used for UE configured with
*highSpeedMeasFlag-r16* 1966A.4.6.4.5.1 Test Purpose and Environment
1966A.4.6.4.5.2 Test parameters 1967A.4.6.4.5.3 Test Requirements
1968A.4.6.4.6 CSI-RS based L1-RSRP measurement when DRX is not used when
CD-SSB is outside active BWP 1968A.4.6.4.6.1 Test Purpose and
Environment 1968A.4.6.4.7 SSB based L1-RSRP measurement when DRX is not
used when CD-SSB is outside active BWP 1969A.4.6.4.7.1 Test Purpose and
Environment 1969A.4.6.4.7.2 Test Requirements 1969A.4.6.4.8 SSB based
L1-RSRP measurement for UE supporting NCD-SSB based L1 measurement
outside active BWP when DRX is not used 1969A.4.6.4.8.1 Test Purpose and
Environment 1969A.4.6.4.8.2 Test parameters 1969A.4.6.4.8.3 Test
Requirements 1971A.4.6.5 CLI measurements 1971A.4.6.5.1 SRS-RSRP
measurement with non-DRX 1971A.4.6.5.1.1 Test Purpose and Environment
1971A.4.6.5.1.2 Test Parameters 1971A.4.6.5.1.3 Test Requirements
1974A.4.6.5.2 CLI-RSSI measurement with non-DRX 1974A.4.6.5.2.1 Test
Purpose and Environment 1974A.4.6.5.2.2 Test Parameters 1974A.4.6.5.2.3
Test Requirements 1975A.4.6.6.1.2 Test Requirements 1979A.4.6.7 L1-SINR
measurement for beam reporting 1979A.4.6.7.2 L1-SINR measurement with
SSB based CMR and dedicated IMR when DRX is used 1981A.4.6.7.2.1 Test
Purpose and Environment 1981A.4.6.7.2.2 Test parameters 1982A.4.6.7.2.3
Test Requirements 1983A.4.6.7.3 L1-SINR measurement with CSI-RS based
CMR and dedicated IMR configured when DRX is used 1983A.4.6.7.3.1 Test
Purpose and Environment 1984A.4.6.7.3.2 Test parameters 1984A.4.6.7.3.3
Test Requirements 1985A.4.6.8 CSI-RS based intra-frequency Measurement
1986A.4.6.8.1 EN-DC event triggered reporting tests without gap under
DRX 1986A.4.6.8.1.1 Test purpose and Environment 1986A.4.6.8.1.2 Test
Requirements 1988A.4.6.9 CSI-RS based inter-frequency Measurement
1988A.4.6.9.1 EN-DC event triggered reporting tests for FR1 cell when
non-DRX is used 1988A.4.6.9.1.1 Test Purpose and Environment
1988A.4.6.9.1.2 Test Requirements 1990A.4.7 Measurement Performance
requirements 1992A.4.7.1 SS-RSRP 1992A.4.7.1.1 EN-DC Intra-frequency
measurement accuracy with FR1 serving cell and FR1 target cell
1992A.4.7.1.1.1 Test Purpose and Environment 1992A.4.7.1.1.2 Test
parameters 1992A.4.7.1.1.3 Test Requirements 1996A.4.7.1.2 EN-DC
inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell 1997A.4.7.1.2.1 Test Purpose and Environment 1997A.4.7.1.2.2
Test parameters 1997A.4.7.1.2.3 Test Requirements 1999A.4.7.1.3 Void
1999A.4.7.2 SS-RSRQ 2000**A.4.7.2.1** **EN-DC Intra-frequency
measurement accuracy with FR1 serving cell and FR1 target cell**
2000A.4.7.2.1.1 Test Purpose and Environment 2000A.4.7.2.1.2 Test
Parameters 2000A.4.7.2.1.3 Test Requirements 2003A.4.7.2.2 EN-DC
Inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell 2003A.4.7.2.2.1 Test Purpose and Environment 2003A.4.7.2.2.2
Test Parameters 2003A.4.7.2.2.3 Test Requirements 2007A.4.7.3 SS-SINR
2007A.4.7.3.1 EN-DC Intra-frequency measurement accuracy with FR1
serving cell and FR1 target cell 2007A.4.7.3.1.1 Test Purpose and
Environment 2007A.4.7.3.1.2 Test Parameters 2007A.4.7.3.1.3 Test
Requirements 2010A.4.7.3.2 EN-DC Inter-frequency measurement accuracy
with FR1 serving cell and FR1 target cell 2010A.4.7.3.2.1 Test Purpose
and Environment 2010A.4.7.3.2.2 Test Parameters 2010A.4.7.3.2.3 Test
Requirements 2013A.4.7.4 L1-RSRP measurement for beam reporting
2013A.4.7.4.1 SSB based L1-RSRP measurement 2013A.4.7.4.1.1 Test Purpose
and Environment 2013A.4.7.4.1.2 Test parameters 2014A.4.7.4.1.3 Test
Requirements 2016A.4.7.4.2 CSI-RS based L1-RSRP measurement on resource
set with repetition off 2016A.4.7.4.2.1 Test Purpose and Environment
2016A.4.7.4.2.2 Test parameters 2017A.4.7.4.2.3 Test Requirements
2019A.4.7.5 SFTD accuracy 2020A.4.7.5.1 SFTD accuracy 2020A.4.7.5.1.1
Test Purpose and Environment 2020A.4.7.5.1.2 Test Parameters
2020A.4.7.5.1.3 Test Requirements 2022A.4.7.5.2 Void 2022A.4.7.5.3 Void
2023A.4.7.6 CLI measurements 2023A.4.7.6.1 EN-DC SRS-RSRP measurement
accuracy with FR1 serving cell 2023A.4.7.6.1.1 Test Purpose and
Environment 2023A.4.7.6.1.2 Test parameters 2023A.4.7.6.1.3 Test
Requirements 2026A.4.7.6.2 EN-DC CLI-RSSI measurement accuracy with FR1
serving cell 2026A.4.7.6.2.1 Test Purpose and Environment
2026A.4.7.6.2.2 Test parameters 2026A.4.7.6.2.3 Test Requirements
2028A.4.7.7 L1-SINR measurement for beam reporting 2028A.4.7.7.2 L1-SINR
measurement with SSB based CMR and dedicated IMR 2031A.4.7.7.2.1 Test
Purpose and Environment 2031A.4.7.7.2.2 Test parameters 2032A.4.7.7.2.3
Test Requirements 2034A.4.7.7.3 L1-SINR measurement with CSI-RS based
CMR and dedicated IMR 2034A.4.7.7.3.1 Test Purpose and Environment
2034A.4.7.7.3.2 Test parameters 2035A.4.7.7.3.3 Test Requirements
2037A.4.7.8 CSI-RSRP 2038A.4.7.8.1 EN-DC Intra-frequency measurement
accuracy with FR1 serving cell and FR1 target cell 2038A.4.7.8.1.1 Test
Purpose and Environment 2038A.4.7.8.1.2 Test parameters 2038A.4.7.8.1.3
Test Requirements 2042A.4.7.8.2 EN-DC inter-frequency measurement
accuracy with FR1 serving cell and FR1 target cell 2042A.4.7.8.2.1 Test
Purpose and Environment 2042A.4.7.8.2.2 Test parameters 2042A.4.7.8.2.3
Test Requirements 2045A.4.7.9 CSI-RSRQ 2045A.4.7.9.1 EN-DC
Intra-frequency measurement accuracy with FR1 serving cell and FR1
target cell 2045A.4.7.9.1.1 Test Purpose and Environment 2045A.4.7.9.1.2
Test Parameters 2045A.4.7.9.1.3 Test Requirements 2049A.4.7.9.2 EN-DC
Inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell 2049A.4.7.9.2.1 Test Purpose and Environment 2049A.4.7.9.2.2
Test Parameters 2049A.4.7.9.2.3 Test Requirements 2052A.4.7.10 CSI-SINR
2052A.4.7.10.1 EN-DC Intra-frequency measurement accuracy with FR1
serving cell and FR1 target cell 2052A.4.7.10.1.1 Test Purpose and
Environment 2053A.4.7.10.1.2 Test Parameters 2053A.4.7.10.1.3 Test
Requirements 2056A.4.7.10.2 EN-DC Inter-frequency measurement accuracy
with FR1 serving cell and FR1 target cell 2056A.4.7.10.2.1 Test Purpose
and Environment 2056A.4.7.10.2.2 Test Parameters 2056A.4.7.10.2.3 Test
Requirements 2059A.4.7.11 TDCP amplitude measurement accuracy
2059A.4.7.11.1 TDCP amplitude measurement accuracy in EN-DC
2059A.4.7.11.1.1 Test Purpose and Environment 2059A.4.7.11.1.2 Test
parameters 2059A.4.7.11.1.3 Test Requirements 2061A.4.8 Void 2061A.4A
NE-DC test with all NR cells in FR1 2061A.4A.1 Signaling characteristics
2061A.4A.1.1 E-UTRAN PSCell addition 2061A.4A.1.1.1 Test purpose and
environment 2061A.4A.1.1.2 Test Requirements 2064A.4A.1.2 Active BWP
switch 2065A.4A.1.2.1 E-UTRAN PSCell -- NR PCell FR1 DCI-based and
Timer-based DL active BWP switch in non-DRX in synchronous NE-DC
2065A.4A.1.2.1.1 Test Purpose and Environment 2065A.4A.1.2.1.2 Test
Requirements 2068A.4A.1.3 Intra-frequency handover with E-UTRAN PSCell
2068A.4A.1.3.1 Test purpose and environment 2068A.4A.1.3.2 Test
Requirements 2072A.4A.1.4 Handover with PSCell from NE-DC to NE-DC with
unknown target PSCell 2072A.4A.1.4.1 Test Purpose and Environment
2072A.4A.1.4.2 Test Parameters 2072A.4A.1.4.3 Test Requirements
2076A.4A.1.4.3.1 Test Requirements for NR HO 2076A.4A.1.4.3.2 Test
Requirements for LTE PSCell Change 2077A.4A.2 Measurement performance
2077A.4A.2.1 SFTD accuracy 2077A.4A.2.1.1 SFTD accuracy 2077A.4A.2.1.1.1
Test Purpose 2077A.4A.2.1.1.2 Test Environment 2077A.4A.2.1.1.3 Test
Requirements 2080A.5 EN-DC tests with one or more NR cells in FR2
2080A.5.1 Void 2080A.5.2 Void 2081A.5.3 RRC\_CONNECTED state mobility
2081A.5.3.1 Void 2081A.5.3.2 RRC Connection Mobility Control
2081A.5.3.2.1 Void 2081A.5.3.2.2 Random Access 2081A.5.3.2.2.1 4-step RA
type c ontention based random access test in FR2 for PSCell/SCell in
EN-DC 2081A.5.3.2.2.2 4-step RA type non-contention based random access
test in FR2 for PSCell/SCell in EN-DC 2084A.5.3.2.2.3 2-step RA type
contention based random access test in FR2 for PSCell/SCell in EN-DC
2087A.5.3.2.2.4 2-step RA type non-contention based random access test
in FR2 for PSCell/SCell in EN-DC 2090A.5.3.2.3 Void 2092A.5.3.3 Handover
with PSCell with known FR2 target PSCell 2092A.5.3.3.1 Test purpose and
environment 2092A.5.3.3.2 Test Requirements 2095A.5.3.3.3 Void
2095A.5.3.3.4 Void 2095A.5.3.3.5 Void 2095A.5.3.3.6 Void 2096A.5.4
Timing 2096A.5.4.1 UE transmit timing 2096A.5.4.1.1 NR UE Transmit
Timing Test for FR2 2096A.5.4.1.1.1 Test Purpose and environment
2096A.5.4.1.1.2 Test requirements 2098A.5.4.1.2 NR UE Transmit Timing
Test with 2-TA for FR2 UE supporting
*multiDCI-IntraCellMultiTRP-TwoTA-r18* 2098A.5.4.1.2.1 Test Purpose and
environment 2098A.5.4.1.2.2 Test requirements 2103A.5.4.2 UE timer
accuracy 2103A.5.4.3 Timing advance 2103A.5.4.3.1 EN-DC FR2 timing
advance adjustment accuracy 2103A.5.4.3.1.1 Test Purpose and Environment
2103A.5.4.3.1.2 Test Parameters 2103A.5.4.3.1.3 Test Requirements
2106A.5.5 Signaling characteristics 2106A.5.5.1 Radio link Monitoring
2106A.5.5.1.1 Radio Link Monitoring Out-of-sync Test for FR2 PSCell
configured with SSB-based RLM RS in non-DRX mode 2106A.5.5.1.1.1 Test
Purpose and Environment 2106A.5.5.1.1.2 Test Requirements 2109A.5.5.1.2
Radio Link Monitoring In-sync Test for FR2 PSCell configured with
SSB-based RLM RS in non-DRX mode 2109A.5.5.1.2.1 Test Purpose and
Environment 2109A.5.5.1.2.2 Test Requirements 2112A.5.5.1.3 Radio Link
Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM
RS in DRX mode 2113A.5.5.1.3.1 Test Purpose and Environment
2113A.5.5.1.3.2 Test Requirements 2115A.5.5.1.4 Radio Link Monitoring
In-sync Test for FR2 PSCell configured with SSB-based RLM RS in DRX mode
2115A.5.5.1.4.1 Test Purpose and Environment 2115A.5.5.1.4.2 Test
Requirements 2118A.5.5.1.5 EN-DC Radio Link Monitoring Out-of-sync Test
for FR2 PSCell configured with CSI-RS-based RLM in non-DRX mode
2118A.5.5.1.6 EN-DC Radio Link Monitoring In-sync Test for FR2 PSCell
configured with CSI-RS-based RLM in non-DRX mode 2121A.5.5.1.7 EN-DC
Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with
CSI-RS-based RLM in DRX mode 2124A.5.5.1.8 EN-DC Radio Link Monitoring
In-sync Test for FR2 PSCell configured with CSI-RS-based RLM in DRX mode
2127A.5.5.1.8.2 Test Requirements 2131A.5.5.1.9 EN-DC Radio Link
Monitoring UE Scheduling Restrictions on FR2 2131A.5.5.1.9.1 Test
Purpose and Environment 2131A.5.5.1.9.2 Test Requirements 2132A.5.5.1.10
Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with
SSB-based RLM RS for UE fulfilling relaxed measurement criterion
2133A.5.5.1.10.1 Test Purpose and Environment 2133A.5.5.1.10.2 Test
Requirements 2135A.5.5.1.11 Radio Link Monitoring Out-of-sync Test for
FR2 PSCell configured with SSB-based RLM RS in non-DRX mode for UE
supporting fast beam sweeping in multi-Rx 2135A.5.5.1.11.1 Test Purpose
and Environment 2135A.5.5.1.11.2 Test Requirements 2138A.5.5.1.12 EN-DC
Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with
CSI-RS-based RLM in non-DRX mode when CD-SSB is outside active BWP
2139A.5.5.1.12.1 Test Purpose and Environment 2139A.5.5.1.13 Radio Link
Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM
RS in non-DRX mode when CD-SSB is outside active BWP 2139A.5.5.1.13.1
Test Purpose and Environment 2139A.5.5.1.13.2 Test Requirements
2139A.5.5.1.14 EN-DC Radio Link Monitoring Out-of-sync Test for FR2
PSCell configured with SSB-based RLM RS in non-DRX mode for UE
supporting NCD-SSB based measurement outside active BWP 2139A.5.5.1.14.1
Test Purpose and Environment 2139A.5.5.1.14.2 Test Requirements
2142A.5.5.2 Interruption 2143A.5.5.2.1 E-UTRAN -- NR FR2 interruptions
at transitions between active and non-active during DRX in synchronous
EN-DC 2143A.5.5.2.1.1 Test Purpose and Environment 2143A.5.5.2.1.2 Test
Requirements 2145A.5.5.2.2 E-UTRAN -- NR FR2 interruptions at
transitions between active and non-active during DRX in asynchronous
EN-DC 2145A.5.5.2.2.1 Test Purpose and Environment 2145A.5.5.2.2.2 Test
Requirements 2147**A.5.5.2.3** E-UTRAN -- NR FR2 interruptions during
measurements on deactivated NR SCC in synchronous EN-DC 2147A.5.5.2.3.1
Test Purpose and Environment 2147A.5.5.2.**3.2** Test Requirements
2149**A.5.5.2.4** E-UTRAN -- NR FR2 interruptions during measurements on
deactivated NR SCC in asynchronous EN-DC 2150A.5.5.2.4.1 Test Purpose
and Environment 2150A.5.5.2.**4.2** Test Requirements 2152**A.5.5.2.5**
E-UTRAN -- NR FR2 interruptions during measurements on deactivated
E-UTRAN SCC in synchronous EN-DC 2153A.5.5.2.5.1 Test Purpose and
Environment 2153A.5.5.2.**5.2** Test Requirements 2155**A.5.5.2.6**
E-UTRAN -- NR FR2 interruptions during measurements on deactivated
E-UTRAN SCC in asynchronous EN-DC 2155A.5.5.2.6.1 Test Purpose and
Environment 2155A.5.5.2.**6.2** Test Requirements 2157**A.5.5.2.7**
E-UTRAN -- NR FR2 interruptions at E-UTRA SRS carrier based switching
2158A.5.5.2.7.1 Test Purpose and Environment 2158A.5.5.2.7.2 Test
Requirements 2160A.5.5.2.8 E-UTRAN -- NR FR2 interruptions at NR SRS
carrier based switching 2160A.5.5.2.8.1 Test Purpose and Environment
2160A.5.5.2.8.3 Test Requirements 2162**A.5.5.2.9** E-UTRAN -- NR FR2
interruptions during measurements on deactivated NR PSCell
2162A.5.5.2.9.1 Test Purpose and Environment 2162A.5.5.2.9**.2** Test
Requirements 2165A.5.5.3 SCell Activation and Deactivation Delay
2165A.5.5.3.1 SCell Activation and deactivation of SCell in FR2
intra-band 2165A.5.5.3.1.1 Test Purpose and Environment 2165A.5.5.3.1.2
Test Requirements 2166A.5.5.3.2 SCell Activation and deactivation of
known SCell in FR1 for 160 ms SCell measurement cycle 2167A.5.5.3.2.1
Test Purpose and Environment 2167A.5.5.3.2.2 Test Requirements
2169A.5.5.3.3 Void 2169A.5.5.3.4 Void 2169A.5.5.3.5 SCell Activation and
deactivation of SCell in FR2 2169A.5.5.3.5.1 Test Purpose and
Environment 2169A.5.5.3.5.2 Test Requirements 2172A.5.5.3.6 Multiple
SCell Activation and deactivation of one unknown SCell and one known
SCell in FR2 2172A.5.5.3.6.1 Test Purpose and Environment
2172A.5.5.3.6.2 Test Requirements 2175A.5.5.3.7 Direct SCell activation
at SCell addition of known SCell in FR2 2175A.5.5.3.7.1 Test Purpose and
Environment 2175A.5.5.3.7.2 Test Requirements 2178A.5.5.3.8 Fast SCell
Activation of SCell in FR2 intra-band 2178A.5.5.3.8.1 Test Purpose and
Environment 2178A.5.5.3.8.2 Test Requirements 2181A.5.5.3.9 PUCCH SCell
Activation and deactivation of known SCell in FR2 2181A.5.5.3.9.1 Test
Purpose and Environment 2181A.5.5.3.9.2 Test Requirements 2184A.5.5.3.10
PUCCH SCell Activation and deactivation of unknown SCell in FR2
2184A.5.5.3.10.1 Test Purpose and Environment 2184A.5.5.3.10.2 Test
Requirements 2187A.5.5.3.11 Multiple SCell activation and deactivation
of one known PUCCH SCell and one unknown SCell in FR2 2187A.5.5.3.11.1
Test Purpose and Environment 2187A.5.5.3.11.2 Test Requirements
2190A.5.5.3.12 SCell Activation and deactivation of unknown PUCCH SCell
and unknown DL SCell in FR2 in non-DRX 2191A.5.5.3.12.1 Test Purpose and
Environment 2191A.5.5.3.12.2 Test Requirements 2193A.5.5.3.13 SCell
Activation and deactivation of unknown SCell in FR2 for UE in DRX,
capable of small beam sweeping factors and/or short measurement interval
2194A.5.5.3.13.1 Test Purpose and Environment 2194A.5.5.3.13.2 Test
Requirements 2197A.5.5.3.14 PUCCH SCell activation and deactivation with
FR1 PSCell based on L3 reporting after SCell activation command
2199A.5.5.3.14.1 Test Purpose and Environment 2199A.5.5.3.14.2 Test
Requirements 2203A.5.5.3.15 SCell Activation of unknown SCell in FR2 in
non-DRX for 160 ms SCell measurement cycle with the L3 reporting during
activation 2203A.5.5.3.15.1 Test Purpose and Environment
2203A.5.5.3.15.2 Test Requirements 2207A.5.5.4 Void 2208A.5.5.5 Beam
Failure Detection and Link recovery procedures 2208A.5.5.5.1 EN-DC Beam
Failure Detection and Link Recovery Test for FR2 PSCell configured with
SSB-based BFD and LR in non-DRX mode 2208A.5.5.5.1.1 Test Purpose and
Environment 2208A.5.5.5.1.2 Test Requirements 2211A.5.5.5.2 EN-DC Beam
Failure Detection and Link Recovery Test for FR2 PSCell configured with
SSB-based BFD and LR in DRX mode 2211A.5.5.5.2.1 Test Purpose and
Environment 2211A.5.5.5.2.2 Test Requirements 2215A.5.5.5.3 EN-DC Beam
Failure Detection and Link Recovery Test for FR2 PSCell configured with
CSI-RS-based BFD and LR in non-DRX mode 2215A.5.5.5.3.1 Test Purpose and
Environment 2215A.5.5.5.3.2 Test Requirements 2218A.5.5.5.4 EN-DC Beam
Failure Detection and Link Recovery Test for FR2 PSCell configured with
CSI-RS-based BFD and LR in DRX mode 2219A.5.5.5.4.1 Test Purpose and
Environment 2219A.5.5.5.4.2 Test Requirements 2222A.5.5.5.5 EN-DC
scheduling availability restriction during Beam Failure Detection and
Link Recovery for FR2 PSCell configured with SSB-based BFD and LR in
non-DRX mode 2222A.5.5.5.5.1 Test Purpose and Environment
2222A.5.5.5.5.2 Test Requirements 2225A.5.5.5.6 EN-DC Beam Failure
Detection and Link Recovery Test for FR2 SCell configured with
CSI-RS-based BFD and LR in non-DRX mode 2225A.5.5.5.6.1 Test Purpose and
Environment 2225A.5.5.5.6.2 Test Requirements 2229A.5.5.5.7 EN-DC Beam
Failure Detection and Link Recovery Test for FR2 SCell configured with
CSI-RS-based BFD and LR in DRX mode 2229A.5.5.5.7.1 Test Purpose and
Environment 2229A.5.5.5.7.2 Test Requirements 2232A.5.5.5.8 EN-DC TRP
specific Beam Failure Detection and Link Recovery Test for FR2 PSCell
configured with CSI-RS-based BFD and LR in DRX mode 2233A.5.5.5.8.1 Test
Purpose and Environment 2233A.5.5.5.8.2 Test Requirements 2236A.5.5.5.9
Beam Failure Detection and Link Recovery Test for FR2 PSCell configured
with SSB-based BFD and LR in DRX mode for UE fulfilling relaxed
measurement criterion 2236A.5.5.5.9.1 Test Purpose and Environment
2236A.5.5.5.9.2 Test Requirements 2239A.5.5.6 Active BWP switch
2240A.5.5.6.1 DCI-based and Timer-based Active BWP Switch
2240A.5.5.6.1.1 E-UTRAN -- NR PSCell FR2 DL active BWP switch with
non-DRX in synchronous EN-DC 2240A.5.5.6.1.1.1 Test Purpose and
Environment 2240A.**5.5.6.1.1**.2 Test Requirements 2242A.5.5.6.1.2
E-UTRAN -- NR PSCell FR2 with FR2 SCell DL active BWP switch in non-DRX
in synchronous EN-DC 2243A.5.5.6.2 RRC-based Active BWP Switch
2246A.5.5.6.2.1 E-UTRAN -- NR PSCell FR2 DL active BWP switch with
non-DRX in synchronous EN-DC 2246A.5.5.6.3 Simultaneous DCI-based and
Timer-based Active BWP Switch on multiple CCs 2249A.5.5.6.3.1 E-UTRAN --
NR PSCell FR2 and NR SCell FR2 DL active BWP switch on multiple CCs in
synchronous EN-DC 2249A.5.5.6.4 SCell dormancy switch 2252A.5.5.6.4.1
E-UTRAN -- NR FR2 PSCell SCell dormancy switch of single FR2 SCell
inside active time 2252A.5.5.6.4.1.1 Test Purpose and Environment
2252A.5.5.6.4.1.2 Test Requirements 2255A.5.5.6.4.2 E-UTRAN -- NR FR1
PSCell SCell dormancy switch of two FR2 SCells outside active time
2256A.5.5.6.4.2.1 Test Purpose and Environment 2256A.5.5.6.4.2.2 Test
Requirements 2260A.5.5.6.5 Simultaneous RRC-based Active BWP Switch on
multiple CCs 2260A.5.5.6.5.1 E-UTRAN -- NR PSCell FR2 and NR SCell FR2
DL active BWP switch on multiple CCs with non-DRX in synchronous EN-DC
2260A.5.5.7 PSCell addition and release delay 2263A.5.5.7.1 Addition and
Release Delay of NR PSCell 2263A.5.5.7.1.1 Test purpose and environment
2263A.5.5.7.1.2 Test Requirements 2265A.5.5.8 Active TCI state switch
delay 2265A.5.5.8.1 MAC-CE based active TCI state switch 2266A.5.5.8.1.1
E-UTRAN -- NR PSCell FR2 active TCI state switch for a known TCI state
2266A.5.5.8.1.1.1 Test Purpose and Environment 2266A.5.5.8**.1.1**.2
Test Requirements 2268A.5.5.8.2 RRC based active TCI state switch
2269A.5.5.8.2.1 E-UTRAN -- NR PSCell FR2 active TCI state switch for a
known TCI state 2269A.5.5.8.2.1.1 Test Purpose and Environment
2269A.5.5.8.2**.1**.2 Test Requirements 2272A.5.5.9 Uplink spatial
relation switch delay 2272A.5.5.9.1 MAC-CE based uplink spatial relation
switch 2272A.5.5.9.1.1 E-UTRAN -- NR PSCell FR2 uplink spatial relation
switch for a known spatial relation 2272A.5.5.9.1.1.1 Test Purpose and
Environment 2272A.5.5.9**.1.1**.2 Test Requirements 2274A.5.5.9.2 RRC
based spatial relation switch 2274A.5.5.9.2.1 E-UTRAN -- NR PSCell FR2
spatial relation switch associated with a known DL-RS 2274A.5.5.9.2.1.1
Test Purpose and Environment 2275A.5.5.9.2**.1**.2 Test Requirements
2276A.5.5.10 UE specific CBW change 2277A.5.5.10.1 UE specific CBW
change on FR2 NR PSCell 2277A.5.5.10.1.1 Test Purpose and Environment
2277A.5.5.10.1.2 Test Requirements 2279A.5.5.11 Unified TCI state switch
delay 2280A.5.5.11.1 MAC-CE based active joint TCI state switch
2280A.5.5.11.1.1 E-UTRAN -- NR PSCell FR2 active joint TCI state switch
for a known TCI state 2280A.5.5.11.1.1.1 Test Purpose and Environment
2280A.5.5.11.1.1.2 Test parameters 2280A.5.5.11.1.1.3 Test Requirements
2282A.5.5.11.2 MAC-CE based active uplink TCI state switch
2282A.5.5.11.2.1 E-UTRAN -- NR PSCell FR2 active uplink TCI state switch
for a known TCI state 2282A.5.5.11.2.1.1 Test Purpose and Environment
2282A.5.5.11.2.1.2 Test parameters 2283A.5.5.11.2.1.3 Test Requirements
2284A.5.5.11.3 MAC-CE based active downlink TCI state switch
2285A.5.5.11.3.1 E-UTRAN -- NR PSCell FR2 downlink TCI state switch to
cell with additional PCI for a known TCI state 2285A.5.5.11.3.1.1 Test
Purpose and Environment 2285A.5.5.11.3.1.2 Test Parameters
2285A.5.5.11.3**.1**.3 Test Requirements 2288A.5.5.12 PSCell activation
and deactivation delay 2288A.5.5.12.1 PSCell activation and deactivation
delay 2288A.5.5.12.1.1 Test purpose and environment 2288A.5.5.12.1.2
Test Requirements 2290A.5.5.13 Conditional PSCell addition and release
delay 2291A.5.5.13.1 Addition and Release Delay of NR PSCell
2291A.5.5.13.1.1 Test purpose and environment 2291A.5.5.13.1.2 Test
Requirements 2293A.5.6 Measurement procedure 2293A.5.6.1 Intra-frequency
Measurements 2293A.5.6.1.1 EN-DC event triggered reporting test without
gap under non-DRX 2293A.5.6.1.1.1 Test purpose and Environment
2293A.5.6.1.1.2 Test Requirements 2296A.5.6.1.2 EN-DC event triggered
reporting test without gap under DRX 2296A.5.6.1.2.1 Test purpose and
Environment 2296A.5.6.1.2.2 Test Requirements 2298A.5.6.1.3 EN-DC event
triggered reporting test with per-UE gaps under non-DRX 2299A.5.6.1.3.1
Test purpose and Environment 2299A.5.6.1.3.2 Test Requirements
2301A.5.6.1.4 EN-DC event triggered reporting test with per-UE gaps
under DRX 2301A.5.6.1.4.1 Test purpose and Environment 2301A.5.6.1.4.2
Test Requirements 2304A.5.6.1.5 EN-DC event triggered reporting test
without gap under non-DRX when CD-SSB is outside active BWP
2304A.5.6.1.5.1 Test purpose and Environment 2304A.5.6.1.5.2 Test
Requirements 2304A.5.6.1.6 EN-DC event triggered reporting test without
gap under non-DRX 2304A.5.6.1.6.1 Test purpose and Environment
2304A.5.6.1.6.2 Test Requirements 2307A.5.6.2 Inter-frequency
Measurements 2307A.5.6.2.1 EN-DC event triggered reporting tests for FR2
cell without SSB time index detection when DRX is not used
2307A.5.6.2.1.1 Test Purpose and Environment 2307A.5.6.2.1.2 Test
Requirements 2310A.5.6.2.2 EN-DC event triggered reporting tests for FR2
cell without SSB time index detection when DRX is used 2310A.5.6.2.2.1
Test Purpose and Environment 2310A.5.6.2.2.2 Test Requirements
2312A.5.6.2.3 EN-DC event triggered reporting tests for FR2 cell with
SSB time index detection when DRX is not used 2313A.5.6.2.3.1 Test
Purpose and Environment 2313A.5.6.2.3.2 Test Requirements 2315A.5.6.2.4
EN-DC event triggered reporting tests for FR2 cell with SSB time index
detection when DRX is used 2315A.5.6.2.4.1 Test Purpose and Environment
2315A.5.6.2.4.2 Test Requirements 2318A.5.6.2.5 EN-DC event triggered
reporting tests for FR2 cell without SSB time index detection when DRX
is not used 2318A.5.6.2.5.1 Test Purpose and Environment 2318A.5.6.2.5.2
Test Requirements 2321A.5.6.2.6 EN-DC event triggered reporting tests
for FR2 cell without SSB time index detection when DRX is used
2321A.5.6.2.6.1 Test Purpose and Environment 2321A.5.6.2.6.2 Test
Requirements 2324A.5.6.2.7 EN-DC event triggered reporting tests for FR2
cell with SSB time index detection when DRX is not used 2325A.5.6.2.7.1
Test Purpose and Environment 2325A.5.6.2.7.2 Test Requirements
2327A.5.6.2.8 EN-DC event triggered reporting tests for FR2 cell with
SSB time index detection when DRX is used 2328A.5.6.2.8.1 Test Purpose
and Environment 2328A.5.6.2.8.2 Test Requirements 2331A.5.6.3 L1-RSRP
measurement for beam reporting 2331A.5.6.3.1 SSB based L1-RSRP
measurement when DRX is not used 2331A.5.6.3.1.1 Test Purpose and
Environment 2331A.5.6.3.1.2 Test parameters 2332A.5.6.3.1.3 Test
Requirements 2333A.5.6.3.2 SSB based L1-RSRP measurement when DRX is
used 2333A.5.6.3.2.1 Test Purpose and Environment 2333A.5.6.3.2.2 Test
parameters 2334A.5.6.3.2.3 Test Requirements 2335A.5.6.3.3 CSI-RS based
L1-RSRP measurement when DRX is not used 2335A.5.6.3.3.1 Test Purpose
and Environment 2335A.5.6.3.3.2 Test parameters 2335A.5.6.3.3.3 Test
Requirements 2337A.5.6.3.4 CSI-RS based L1-RSRP measurement when DRX is
used 2337A.5.6.3.4.1 Test Purpose and Environment 2337A.5.6.3.4.2 Test
parameters 2338A.5.6.3.4.3 Test Requirements 2339A.5.6.3.5 CSI-RS based
L1-RSRP measurement when DRX is not used and when CD-SSB is outside
active BWP 2339A.5.6.3.5.1 Test Purpose and Environment 2339A.5.6.3.6
SSB based L1-RSRP measurement when DRX is not used when CD-SSB is
outside active BWP 2340A.5.6.3.6.1 Test Purpose and Environment
2340A.5.6.3.6.2 Test Requirements 2340A.5.6.3.7 SSB based L1-RSRP
measurement for UE supporting NCD-SSB based L1 measurement outside
active BWP when DRX is not used 2340A.5.6.3.7.1 Test Purpose and
Environment 2340A.5.6.3.7.2 Test parameters 2340A.5.6.3.7.3 Test
Requirements 2342A.5.6.4 CLI measurements 2342A.5.6.4.1 SRS-RSRP
measurement with DRX 2342A.5.6.4.1.1 Test Purpose and Environment
2342A.5.6.4.1.2 Test Parameters 2342A.5.6.4.1.3 Test Requirements
2344A.5.6.4.2 CLI-RSSI measurement with DRX 2345A.5.6.4.2.1 Test Purpose
and Environment 2345A.5.6.4.2.2 Test Parameters 2345A.5.6.4.2.3 Test
Requirements 2346A.5.6.5 Measurements with autonomous gaps 2346A.5.6.5.1
EN-DC inter-frequency CGI identification of NR neighbor cell in FR2
2346A.5.6.5.1.1 Test Purpose and Environment 2346A.5.6.5.1.2 Test
Requirements 2349A.5.6.6 L1-SINR measurement for beam reporting
2349A.5.6.6.2 L1-SINR measurement with SSB based CMR and dedicated IMR
when DRX is not used 2351A.5.6.6.2.1 Test Purpose and Environment
2351A.5.6.6.2.2 Test parameters 2351A.5.6.6.2.3 Test Requirements
2353A.5.6.6.3 L1-SINR measurement with CSI-RS based CMR and dedicated
IMR configured when DRX is not used 2353A.5.6.6.3.1 Test Purpose and
Environment 2353A.5.6.6.3.2 Test parameters 2354A.5.6.6.3.3 Test
Requirements 2355A.5.6.7 CSI-RS based Intra-frequency Measurements
2355A.5.6.7.1 EN-DC event triggered reporting test without gap under
non-DRX 2355A.5.6.7.1.1 Test purpose and Environment 2355A.5.6.7.1.2
Test Requirements 2357A.5.6.8 CSI-RS based Inter-frequency Measurements
2357A.5.6.8.1 EN-DC event triggered reporting tests for NR FR2 cell when
DRX is used 2357A.5.6.8.1.1 Test Purpose and Environment 2357A.5.6.8.1.2
Test Requirements 2359A.5.7 Measurement Performance requirements
2360A.5.7.1 SS-RSRP 2360A.5.7.1.1 EN-DC intra-frequency case measurement
accuracy with FR2 serving cell and FR2 target cell 2360A.5.7.1.1.1 Test
Purpose and Environment 2360A.5.7.1.1.2 Test parameters 2360A.5.7.1.1.3
Test Requirements 2362A.5.7.1.2 EN-DC inter-frequency case measurement
accuracy with FR2 serving cell and FR2 target cell 2362A.5.7.1.2.1 Test
Purpose and Environment 2362A.5.7.1.2.2 Test parameters 2363A.5.7.1.2.3
Test Requirements 2365A.5.7.1.3 EN-DC inter-frequency measurement
accuracy with FR1 serving cell and FR2 target cell 2366A.5.7.1.3.1 Test
Purpose and Environment 2366A.5.7.1.3.2 Test parameters 2366A.5.7.1.3.3
Test Requirements 2368A.5.7.2 SS-RSRQ 2368A.5.7.2.1 EN-DC
Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 2368A.5.7.2.1.1 Test Purpose and Environment 2368A.5.7.2.1.2
Test Parameters 2369A.5.7.2.1.3 Test Requirements 2370A.5.7.2.2 EN-DC
Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 2370A.5.7.2.2.1 Test Purpose and Environment 2370A.5.7.2.2.2
Test Parameters 2370A.5.7.2.2.3 Test Requirements 2372A.5.7.3 SS-SINR
2372A.5.7.3.1 EN-DC Intra-frequency measurement accuracy with FR2
serving cell and FR2 TDD target cell 2372A.5.7.3.1.1 Test Purpose and
Environment 2372A.5.7.3.1.2 Test Parameters 2372A.5.7.3.1.3 Test
Requirements 2374A.5.7.3.2 EN-DC Inter-frequency measurement accuracy
with FR2 serving cell and FR2 TDD target cell 2374A.5.7.3.2.1 Test
Purpose and Environment 2374A.5.7.3.2.2 Test Parameters 2374A.5.7.3.2.3
Test Requirements 2375A.5.7.4 L1-RSRP measurement for beam reporting
2375A.5.7.4.1 SSB based L1-RSRP measurement 2376A.5.7.4.1.1 Test Purpose
and Environment 2376A.5.7.4.1.2 Test parameters 2376A.5.7.4.1.3 Test
Requirements 2377A.5.7.4.2 CSI-RS based L1-RSRP measurement on resource
set with repetition off 2378A.5.7.4.2.1 Test Purpose and Environment
2378A.5.7.4.2.2 Test parameters 2378A.5.7.4.2.3 Test Requirements
2379A.5.7.5 CLI measurements 2380A.5.7.5.1 EN-DC SRS-RSRP measurement
accuracy with FR2 serving cell 2380A.5.7.5.1.1 Test Purpose and
Environment 2380A.5.7.5.1.2 Test parameters 2380A.5.7.5.1.3 Test
Requirements 2382A.5.7.5.2 EN-DC CLI-RSSI measurement accuracy with FR2
serving cell 2382A.5.7.5.2.1 Test Purpose and Environment
2382A.5.7.5.2.2 Test parameters 2382A.5.7.5.2.3 Test Requirements
2384A.5.7.6 L1-SINR measurement for beam reporting 2384A.5.7.6.2 L1-SINR
measurement with SSB based CMR and dedicated IMR 2386A.5.7.6.2.1 Test
Purpose and Environment 2387A.5.7.6.2.2 Test parameters 2387A.5.7.6.2.3
Test Requirements 2388A.5.7.6.3 L1-SINR measurement with CSI-RS based
CMR and dedicated IMR 2389A.5.7.6.3.1 Test Purpose and Environment
2389A.5.7.6.3.2 Test parameters 2389A.5.7.6.3.3 Test Requirements
2391A.5.7.7 CSI-RSRP 2391A.5.7.7.1 EN-DC intra-frequency case
measurement accuracy with FR2 serving cell and FR2 target cell
2391A.5.7.7.1.1 Test Purpose and Environment 2391A.5.7.7.1.2 Test
parameters 2391A.5.7.7.1.3 Test Requirements 2393A.5.7.7.2 EN-DC
inter-frequency case measurement accuracy with FR2 serving cell and FR2
target cell 2394A.5.7.7.2.1 Test Purpose and Environment 2394A.5.7.7.2.2
Test parameters 2394A.5.7.7.2.3 Test Requirements 2396A.5.7.8 CSI-RSRQ
2397A.5.7.8.1 EN-DC Intra-frequency measurement accuracy with FR2
serving cell and FR2 target cell 2397A.5.7.8.1.1 Test Purpose and
Environment 2397A.5.7.8.1.2 Test Parameters 2397A.5.7.8.1.3 Test
Requirements 2399A.5.7.8.2 EN-DC Inter-frequency measurement accuracy
with FR2 serving cell and FR2 TDD target cell 2399A.5.7.8.2.1 Test
Purpose and Environment 2399A.5.7.8.2.2 Test Parameters 2399A.5.7.8.2.3
Test Requirements 2401A.5.7.9 CSI-SINR 2401A.5.7.9.1 EN-DC
Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 2401A.5.7.9.1.1 Test Purpose and Environment 2401A.5.7.9.1.2
Test Parameters 2401A.5.7.9.1.3 Test Requirements 2403A.5.7.9.2 EN-DC
Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 2403A.5.7.9.2.1 Test Purpose and Environment 2403A.5.7.9.2.2
Test Parameters 2403A.5.7.9.2.3 Test Requirements 2405A.5.8 Void 2405A.6
NR standalone tests with all NR cells in FR1 2407A.6.1 SA: RRC\_IDLE
state mobility 2407A.6.1.1 Cell re-selection to NR 2407A.6.1.1.1 Cell
reselection to FR1 intra-frequency NR case 2407A.6.1.1.1.1 Test Purpose
and Environment 2407A.6.1.1.1.2 Test Parameters 2407A.6.1.1.1.3 Test
Requirements 2409A.6.1.1.2 Cell reselection to FR1 inter-frequency NR
case 2409A.6.1.1.2.1 Test Purpose and Environment 2409A.6.1.1.2.2 Test
Parameters 2410A.6.1.1.2.3 Test Requirements 2412A.6.1.1.3 Cell
reselection to FR1 intra-frequency NR case for UE fulfilling low
mobility relaxed measurement criterion 2412A.6.1.1.3.1 Test Purpose and
Environment 2412A.6.1.1.3.2 Test Parameters 2412A.6.1.1.3.3 Test
Requirements 2415A.6.1.1.4 Cell reselection to FR1 intra-frequency NR
case for UE fulfilling not-at-cell edge relaxed measurement criterion
2415A.6.1.1.4.1 Test Purpose and Environment 2415A.6.1.1.4.2 Test
Parameters 2415A.6.1.1.4.3 Test Requirements 2417A.6.1.1.5 Cell
reselection to FR1 inter-frequency NR case for UE fulfilling low
mobility relaxed measurement criterion 2418A.6.1.1.5.1 Test Purpose and
Environment 2418A.6.1.1.5.2 Test Parameters 2418A.6.1.1.5.3 Test
Requirements 2420A.6.1.1.6 Cell reselection to FR1 inter-frequency NR
case for UE fulfilling not-at-cell edge relaxed measurement criterion
2421A.6.1.1.6.1 Test Purpose and Environment 2421A.6.1.1.6.2 Test
Parameters 2421A.6.1.1.6.3 Test Requirements 2423A.6.1.1.7 Cell
reselection to FR1 intra-frequency NR case for UE configured with
***highSpeedMeasFlag-r16*** 2424A.6.1.1.7.1 Test Purpose and Environment
2424A.6.1.1.7.2 Test Parameters 2424A.6.1.1.7.3 Test Requirements
2427A.6.1.1.8 Cell reselection to FR1 inter-frequency NR case for UE
configured with *highSpeedMeasInterFreq-r17* 2427A.6.1.1.8.1 Test
Purpose and Environment 2427A.6.1.1.8.2 Test Parameters 2427A.6.1.1.8.3
Test Requirements 2430A.6.1.1.9 Cell reselection to FR1 intra-frequency
NR case for UE operating on a cell with less than 5 MHz BW
2430A.6.1.1.9.1 Test Purpose and Environment 2430A.6.1.1.9.3 Test
Requirements 2431A.6.1.2 Inter-RAT E-UTRAN cell re-selection
2431A.6.1.2.1 Cell reselection to higher priority E-UTRAN
2431A.6.1.2.1.1 Test Purpose and Environment 2431A.6.1.2.1.2 Test
Parameters 2432A.6.1.2.1.3 Test Requirements 2434A.6.1.2.2 Cell
reselection to lower priority E-UTRAN 2434A.6.1.2.2.1 Test Purpose and
Environment 2434A.6.1.2.2.2 Test Parameters 2434A.6.1.2.2.3 Test
Requirements 2437A.6.1.2.3 Cell reselection to lower priority E-UTRAN
for UE fulfilling low mobility relaxed measurement criterion
2437A.6.1.2.3.1 Test Purpose and Environment 2437A.6.1.2.3.2 Test
Parameters 2437A.6.1.2.3.3 Test Requirements 2440A.6.1.2.4 Cell
reselection to lower priority E-UTRAN for UE fulfilling not-at-cell edge
relaxed measurement criterion 2440A.6.1.2.4.1 Test Purpose and
Environment 2440A.6.1.2.4.2 Test Parameters 2441A.6.1.2.4.3 Test
Requirements 2443A.6.1.2.5 Cell reselection to lower priority E-UTRAN
cell for UE configured with highSpeedMeasFlag-r16 2443A.6.1.2.5.1 Test
Purpose and Environment 2444A.6.1.2.5.2 Test Parameters 2444A.6.1.2.5.3
Test Requirements 2446A.6.1.1.7 **Void** 2446A.6.2 SA: RRC\_INACTIVE
state mobility 2447A.6.2.1 Configured Grant based Small Data
Transmissions (CG-SDT) 2447A.6.2.1.1 Test purpose and Environment
2447A.6.2.1.2 Test Parameters 2448A.6.2.1.3 Test requirements
2449A.6.2.2 Cell reselection for positioning 2450A.6.2.2.1 Cell
reselection to FR1 intra-frequency NR case with RRC\_ INACTIVE eDRX and
positioning SRS 2450A.6.2.2.1.1 Test Purpose and Environment
2450A.6.2.2.1.2 Test Parameters 2450A.6.2.2.1.3 Test Requirements
2454A.6.3 RRC\_CONNECTED state mobility 2454A.6.3.1 Handover
2454A.6.3.1.1 Intra-frequency handover from FR1 to FR1; known target
cell 2454A.6.3.1.1.1 Test Purpose and Environment 2454A.6.3.1.1.2 Test
Parameters 2454A.6.3.1.1.3 Test Requirements 2456A.6.3.1.2
Intra-frequency handover from FR1 to FR1; unknown target cell
2456A.6.3.1.2.1 Test Purpose and Environment 2456A.6.3.1.2.2 Test
Parameters 2456A.6.3.1.2.3 Test Requirements 2458A.6.3.1.3
Inter-frequency handover from FR1 to FR1; unknown target cell
2458A.6.3.1.3.1 Test Purpose and Environment 2458A.6.3.1.3.2 Test
Parameters 2458A.6.3.1.3.3 Test Requirements 2460A.6.3.1.4 SA NR -
E-UTRAN handover 2460A.6.3.1.4.1 Test Purpose and Environment
2460A.6.3.1.4.2 Test Requirements 2463A.6.3.1.5 SA NR - E-UTRAN handover
with unknown target cell 2464A.6.3.1.5.1 Test Purpose and Environment
2464A.6.3.1.5.2 Test Requirements 2467A.6.3.1.6 SA NR - UTRAN FDD
handover 2467A.6.3.1.6.1 Test Purpose and Environment 2467A.6.3.1.6.2
Test Requirements 2469A.6.3.1.7 Intra-frequency synchronous DAPS
handover in FR1 2469A.6.3.1.7.1 Test Purpose and Environment
2469A.6.3.1.7.2 Test Parameters 2469A.6.3.1.7.3 Test Requirements
2472A.6.3.1.8 Intra-frequency asynchronous DAPS handover in FR1
2472A.6.3.1.8.1 Test Purpose and Environment 2472A.6.3.1.8.2 Test
Parameters 2473A.6.3.1.8.3 Test Requirements 2475A.6.3.1.9 Intra-band
inter-frequency synchronous DAPS handover test in SA for FR1
2475A.6.3.1.9.1 Test Purpose and Environment 2475A.6.3.1.9.2 Test
Parameters 2476A.6.3.1.9.3 Test Requirements 2478A.6.3.1.10 Intra-band
inter-frequency asynchronous DAPS handover test in SA for FR1
2478A.6.3.1.10.1 Test Purpose and Environment 2478A.6.3.1.10.2 Test
Parameters 2478A.6.3.1.10.3 Test Requirements 2480A.6.3.1.11 Inter-band
inter-frequency synchronous DAPS handover from FR1 to FR1
2480A.6.3.1.11.1 Test Purpose and Environment 2480A.6.3.1.11.2 Test
Parameters 2480A.6.3.1.11.3 Test Requirements 2484A.6.3.1.12 Inter-band
inter-frequency asynchronous DAPS handover from FR1 to FR1
2485A.6.3.1.12.1 Test Purpose and Environment 2485A.6.3.1.12.2 Test
Parameters 2485A.6.3.1.12.3 Test Requirements 2489A.6.3.1.13 SA NR -
E-UTRAN with NR PSCell addition in FR1 2489A.6.3.1.13.1 Test Purpose and
Environment 2489A.6.3.1.13.2 Test Requirements 2494A.6.3.1.14 SA NR -
E-UTRAN handover with NR FR1 PSCell addition 2494A.6.3.1.14.1 Test
Purpose and Environment 2494A.6.3.1.14.2 Test Requirements
2499A.6.3.1.15 Intra-frequency handover from FR1 to FR1; known target
cell configured with NCD-SSB 2500A.6.3.1.15.1 Test Purpose and
Environment 2500A.6.3.1.15.2 Test Parameters 2500A.6.3.1.15.3 Test
Requirements 2503A.6.3.1.16 Inter-frequency handover from FR1 to FR1;
known target cell configured with NCD-SSB 2503A.6.3.1.16.1 Test Purpose
and Environment 2503A.6.3.1.16.2 Test Parameters 2503A.6.3.1.16.3 Test
Requirements 2505A.6.3.1.17 Handover with PSCell change delay from NR-DC
(FR1-FR1) to NR-DC (FR1-FR1) 2505A.6.3.1.17.1 Test Purpose and
Environment 2505A.6.3.1.17.2 Test Requirements 2509A.6.3.1.18
Intra-frequency handover from FR1 to FR1; unknown target cell operating
with 12 PRB SSB bandwidth 2509A.6.3.1.18.2 Test Parameters
2509A.6.3.1.18.3 Test Requirements 2510A.6.3.2 RRC Connection Mobility
Control 2511A.6.3.2.1 SA: RRC Re-establishment 2511A.6.3.2.1.1
Intra-frequency RRC Re-establishment in FR1 2511A.6.3.2.1.2
Inter-frequency RRC Re-establishment in FR1 2513A.6.3.2.1.3
Intra-frequency RRC Re-establishment in FR1 without serving cell timing
2516A.6.3.2.2 Random Access 2518A.6.3.2.2.1 4-step RA type contention
based random access test in FR1 for NR standalone 2518A.6.3.2.2.2 4-step
RA type non-contention based random access test in FR1 for NR standalone
2521A.6.3.2.2.3 2-step RA type contention based random access test in
FR1 for NR standalone 2524A.6.3.2.2.4 2-step RA type non-contention
based test in FR1 for NR standalone 2527A.6.3.2.3 SA: RRC Connection
Release with Redirection 2529A.6.3.2.3.1 Redirection from NR in FR1 to
NR in FR1 2529A.6.3.2.3.2 Redirection from NR in FR1 to E-UTRAN
2531A.6.3.2.4 LTM PDCCH-order Random Access 2534A.6.3.2.4.1 PDCCH-order
RACH on neighbor cell in FR1 when RACH BW is within active UL BWP
2534A.6.3.2.4.2 PDCCH-ordered RACH to an inter-frequency candidate cell
in FR1 for LTM 2538A.6.3.2.4.3 PDCCH-order RACH on neighbor cell without
L1-RSRP measurement in FR1 when RACH BW is within active UL BWP
2542A.6.3.3 Conditional handover 2545A.6.3.3.1 Intra-frequency
conditional handover from FR1 to FR1 2545A.6.3.3.1.1 Test Purpose and
Environment 2545A.6.3.3.1.2 Test Parameters 2545A.6.3.3.1.3 Test
Requirements 2547A.6.3.3.2 Inter-frequency conditional handover from FR1
to FR1 2547A.6.3.3.2.1 Test Purpose and Environment 2547A.6.3.3.2.2 Test
Parameters 2547A.6.3.3.2.3 Test Requirements 2549A.6.3.3.3 NR
conditional handover including target MCG and target SCG from FR1-FR1
NR-DC to FR1-FR1 NR-DC 2549A.6.3.3.3.1 Test Purpose and Environment
2549A.6.3.3.3.2 Test Requirements 2553A.6.3.3.4 NR conditional handover
including target MCG and candidate SCG from FR1-FR1 NR-DC to FR1-FR1
NR-DC 2553A.6.3.3.4.1 Test Purpose and Environment 2553A.6.3.3.4.2 Test
Parameters 2553A.6.3.3.4.3 Test Requirements 2557A.6.3.3.5 NR
conditional handover including target MCG and candidate SCG from FR1-FR1
NR-DC to FR1-FR1 NR-DC with complementary conditional handover
configuration 2557A.6.3.3.5.1 Test Purpose and Environment
2557A.6.3.3.5.2 Test Parameters 2558A.6.3.3.5.3 Test Requirements
2561A.6.3.3.6 NES triggering intra-frequency conditional handover from
FR1 to FR1 2561A.6.3.3.6.1 Test Purpose and Environment 2561A.6.3.3.6.2
Test Parameters 2561A.6.3.3.6.3 Test Requirements 2563A.6.3.3.7
NES-based Inter-frequency conditional handover from FR1 to FR1
2563A.6.3.3.7.1 Test Purpose and Environment 2563A.6.3.3.7.2 Test
Parameters 2563A.6.3.3.7.3 Test Requirements 2565A.6.3.4 LTM PCell
Switch 2565A.6.3.4.1 RACH-based Intra-frequency PCell switch from FR1 to
FR1 2566A.6.3.4.1.1 Test Purpose and Environment 2566A.6.3.4.1.2 Test
Parameters 2566A.6.3.4.1.3 Test Requirements 2568A.6.3.4.2 RACH based
Inter-frequency LTM PCell switch from FR1 to FR1 2569A.6.3.4.2.1 Test
Purpose and Environment 2569A.6.3.4.2.2 Test Parameters 2569A.6.3.4.2.3
Test Requirements 2572A.6.3.4.3 RACH-less Intra-frequency PCell switch
from FR1 to FR1 2573A.6.3.4.3.1 Test Purpose and Environment
2573A.6.3.4.3.2 Test Parameters 2573A.6.3.4.3.3 Test Requirements
2577A.6.3.4.4 RACH-less Intra-frequency PCell switch from FR1 to FR1
without L1-RSRP measurement 2577A.6.3.4.4.1 Test Purpose and Environment
2577A.6.3.4.4.2 Test Parameters 2577A.6.3.4.4.3 Test Requirements
2581A.6.3.5 LTM PSCell Switch 2581A.6.3.5.1 RACH-based intra-frequency
LTM PSCell switch from FR1 to FR1 2581A.6.3.5.1.1 Test Purpose and
Environment 2581A.6.3.5.1.2 Test Parameters 2581A.6.3.5.1.3 Test
Requirements 2586A.6.4 Timing 2586A.6.4.1 UE transmit timing
2586A.6.4.1.1 NR UE Transmit Timing Test for FR1 2586A.6.4.1.1.1 Test
Purpose and environment 2586A.6.4.1.1.2 Test requirements 2588A.6.4.1.2
NR UE Transmit Timing Test for two TRPs in FR1 2589A.6.4.1.2.1 Test
Purpose and environment 2589A.6.4.1.2.2 Test requirements 2591A.6.4.2 UE
timer accuracy 2592A.6.4.3 Timing advance 2592A.6.4.3.1 SA FR1 timing
advance adjustment accuracy 2592A.6.4.3.1.1 Test Purpose and Environment
2592A.6.4.3.1.2 Test Parameters 2592A.6.4.3.1.3 Test Requirements
2595A.6.5 Signalling characteristics 2595A.6.5.1 Radio link Monitoring
2595A.6.5.1.1 Radio Link Monitoring Out-of-sync Test for FR1 PCell
configured with SSB-based RLM RS in non-DRX mode 2595A.6.5.1.1.1 Test
Purpose and Environment 2595A.6.5.1.1.2 Test Requirements 2598A.6.5.1.2
Radio Link Monitoring In-sync Test for FR1 PCell configured with
SSB-based RLM RS in non-DRX mode 2598A.6.5.1.2.1 Test Purpose and
Environment 2598A.6.5.1.2.2 Test Requirements 2601A.6.5.1.3 Radio Link
Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM
RS in DRX mode 2601A.6.5.1.3.1 Test Purpose and Environment
2601A.6.5.1.3.2 Test Requirements 2604A.6.5.1.4 Radio Link Monitoring
In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode
2604A.6.5.1.4.1 Test Purpose and Environment 2604A.6.5.1.4.2 Test
Requirements 2607A.6.5.1.5 Radio Link Monitoring Out-of-sync Test for
FR1 PCell configured with CSI-RS-based RLM in non-DRX mode
2607A.6.5.1.5.1 Test Purpose and Environment 2607A.6.5.1.5.2 Test
Requirements 2610A.6.5.1.6 Radio Link Monitoring In-sync Test for FR1
PCell configured with CSI-RS-based RLM in non-DRX mode 2610A.6.5.1.6.1
Test Purpose and Environment 2610A.6.5.1.6.2 Test Requirements
2613A.6.5.1.7 Radio Link Monitoring Out-of-sync Test for FR1 PCell
configured with CSI-RS-based RLM in DRX mode 2613A.6.5.1.7.1 Test
Purpose and Environment 2613A.6.5.1.7.2 Test Requirements 2616A.6.5.1.8
Radio Link Monitoring In-sync Test for FR1 PCell configured with
CSI-RS-based RLM in DRX mode 2617A.6.5.1.8.1 Test Purpose and
Environment 2617A.6.5.1.8.2 Test Requirements 2620A.6.5.1.9 Radio Link
Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based
RLM for UE fulfilling relaxed measurement criterion 2620A.6.5.1.9.1 Test
Purpose and Environment 2620A.6.5.1.9.2 Test Requirements 2623A.6.5.1.10
Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with
CSI-RS-based RLM in non-DRX mode when CD-SSB is outside active BWP
2623A.6.5.1.10.1 Test Purpose and Environment 2623A.6.5.1.11 Radio Link
Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM
RS in non-DRX mode when CD-SSB is outside active BWP 2624A.6.5.1.11.1
Test Purpose and Environment 2624A.6.5.1.11.2 Test Requirements
2624A.6.5.1.12 Radio Link Monitoring Out-of-sync Test for FR1 PCell
configured with SSB-based RLM RS in non-DRX mode for UE supporting
NCD-SSB based measurement outside active BWP 2624A.6.5.1.12.1 Test
Purpose and Environment 2624A.6.5.1.12.2 Test Requirements
2627A.6.5.1.13 Radio Link Monitoring Out-of-sync Test for FR1 PCell
configured with SSB-based RLM RS in DRX mode for UE operating on a cell
with less than 5 MHz BW 2627A.6.5.1.13.1 Test Purpose and Environment
2627A.6.5.1.13.2 Test Requirements 2628A.6.5.1.14 Radio Link Monitoring
Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in
non-DRX mode for UE operating on a cell with less than 5 MHz BW
2628A.6.5.1.14.1 Test Purpose and Environment 2628A.6.5.1.14.2 Test
Requirements 2629A.6.5.1.15 Radio Link Monitoring In-sync Test for FR1
PCell with 3 MHz Channel Bandwidth configured with SSB-based RLM RS in
non-DRX mode 2629A.6.5.1.15.1 Test Purpose and Environment
2629A.6.5.1.15.2 Test Requirements 2630A.6.5.1.16 Radio Link Monitoring
In-sync Test for FR1 PCell with 3MHz Channel Bandwidth configured with
SSB-based RLM RS in DRX mode 2630A.6.5.1.16.1 Test Purpose and
Environment 2630A.6.5.1.16.2 Test Requirements 2631A.6.5.2 Interruption
2632**A.6.5.2.1** Interruptions during measurements on deactivated NR
SCC in FR1 2632**A.6.5.2.1**.2 Test Requirements 2635A.6.5.2.2 SA
interruptions at NR SRS carrier based switching 2636A.6.5.2.2.1 Test
Purpose and Environment 2636A.6.5.2.2.2 Test Parameters 2636A.6.5.2.2.3
Test Requirements 2638A.6.5.2.3 SA interruptions at NR SRS antenna port
switching with 1 SRS symbol in a slot in NR-CA 2638A.6.5.2.3.1 Test
Purpose and Environment 2638A.6.5.2.3.2 Test Parameters 2638A.6.5.2.3.3
Test Requirements 2640A.6.5.2.4 SA interruptions at NR SRS antenna port
switching 2640A.6.5.2.4.1 Test Purpose and Environment 2640A.6.5.2.4.2
Test Parameters 2640A.6.5.2.4.3 Test Requirements 2642A.6.5.3 SCell
Activation and Deactivation Delay 2642A.6.5.3.1 SCell Activation and
deactivation of known SCell in FR1 in non-DRX for 160 ms SCell
measurement cycle 2642A.6.5.3.1.1 Test Purpose and Environment
2642A.6.5.3.1.2 Test Requirements 2647A.6.5.3.2 SCell Activation and
deactivation of known SCell in FR1 in non-DRX for 640 ms SCell
measurement cycle 2647A.6.5.3.2.1 Test Purpose and Environment
2647A.6.5.3.2.2 Test Requirements 2648A.6.5.3.3 SCell Activation and
deactivation of unknown SCell in FR1 in non-DRX 2648A.6.5.3.3.1 Test
Purpose and Environment 2648A.6.5.3.3.2 Test Requirements 2649A.6.5.3.4
Direct SCell activation at SCell addition of known SCell in FR1
2649A.6.5.3.4.1 Test Purpose and Environment 2649A.6.5.3.4.2 Test
Requirements 2652A.6.5.3.5 Direct SCell activation at handover with
known SCell in FR1 2653A.6.5.3.5.1 Test Purpose and Environment
2653A.6.5.3.5.2 Test Requirements 2657A.6.5.3.6 PUCCH SCell Activation
and deactivation of known SCell in FR1 2658A.6.5.3.6.1 Test Purpose and
Environment 2658A.6.5.3.6.2 Test Requirements 2661A.6.5.3.7 SCell
Activation and deactivation of unknown SCell in FR1 in non-DRX
2661A.6.5.3.7.1 Test Purpose and Environment 2661A.6.5.3.7.2 Test
Requirements 2664A.6.5.3.8 SCell Activation and Deactivation of one FR1
known PUCCH SCell and one FR1 unknown SCell with single
activation/deactivation command 2665A.6.5.3.8.1 Test Purpose and
Environment 2665A.6.5.3.8.2 Test Requirements 2668A.6.5.3.9 SCell
Activation and deactivation of unknown PUCCH SCell and unknown DL SCell
in FR1 in non-DRX 2669A.6.5.3.9.1 Test Purpose and Environment
2669A.6.5.3.9.2 Test Requirements 2672A.6.5.3.10 Fast SCell Activation
of known SCell in FR1 in non-DRX for 160 ms SCell measurement cycle
2672A.6.5.3.10.1 Test Purpose and Environment 2672A.6.5.3.10.2 Test
Requirements 2675A.6.5.3.11 SCell Activation of known SCell in FR1 in
non-DRX for 640 ms SCell measurement cycle 2676A.6.5.3.11.1 Test Purpose
and Environment 2676A.6.5.3.11.2 Test Requirements 2676A.6.5.3.12 SCell
Activation and deactivation of unknown SCell in FR1 in DRX for UE
capable of short measurement interval 2676A.6.5.3.12.1 Test Purpose and
Environment 2676A.6.5.3.12.2 Test Requirements 2679A.6.5.3.13 SCell
Activation of multiple unknown SCells in FR1 with L3 reporting with
single activation/deactivation commandin non-DRX 2679A.6.5.3.13.1 Test
Purpose and Environment 2679A.6.5.3.13.2 Test Requirements
2684A.6.5.3.14 SCell Activation of unknown SCell with valid L3
measurement results in FR1 in non-DRX for 160 ms SCell measurement cycle
2684A.6.5.3.14.1 Test Purpose and Environment 2684A.6.5.3.14.2 Test
Requirements 2689A.6.5.3.15 TRS based SCell Activation of SSB-less SCell
in FR1 inter-band CA in non-DRX 2690A.6.5.3.15.1 Test Purpose and
Environment 2690A.6.5.3.15.2 Test Requirements 2694A.6.5.3.16 Inter-band
SSB-less SCell Activation based on A-TRS 2694A.6.5.3.16.1 Test Purpose
and Environment 2694A.6.5.3.16.2 Test Requirements 2698A.6.5.4 UE UL
carrier RRC reconfiguration Delay 2699A.6.5.4.1 UE UL carrier RRC
reconfiguration Delay 2699A.6.5.4.1.1 Test Purpose and Environment
2699A.6.5.4.1.2 Test Requirements 2704A.6.5.4.2 Void 2704A.6.5.5 Beam
Failure Detection and Link recovery procedures 2704A.6.5.5.1 Beam
Failure Detection and Link Recovery Test for FR1 PCell configured with
SSB-based BFD and LR in non-DRX mode 2704A.6.5.5.1.1 Test Purpose and
Environment 2704A.6.5.5.1.2 Test Requirements 2708A.6.5.5.2 Beam Failure
Detection and Link Recovery Test for FR1 PCell configured with SSB-based
BFD and LR in DRX mode 2708A.6.5.5.2.1 Test Purpose and Environment
2708A.6.5.5.2.2 Test Requirements 2712A.6.5.5.3 Beam Failure Detection
and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD
and LR in non-DRX mode 2712A.6.5.5.3.1 Test Purpose and Environment
2712A.6.5.5.3.2 Test Requirements 2715A.6.5.5.4 Beam Failure Detection
and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD
and LR in DRX mode 2716A.6.5.5.4.1 Test Purpose and Environment
2716A.6.5.5.4.2 Test Requirements 2720A.6.5.5.5 Beam Failure Detection
and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD
and SSB-based LR in non-DRX mode 2720A.6.5.5.5.1 Test Purpose and
Environment 2720A.6.5.5.5.2 Test Requirements 2723A.6.5.5.6 Beam Failure
Detection and Link Recovery Test for FR1 SCell configured with
CSI-RS-based BFD and SSB-based LR in DRX mode 2724A.6.5.5.6.1 Test
Purpose and Environment 2724A.6.5.5.6.2 Test Requirements 2727A.6.5.5.7
TRP Specific Beam Failure Detection and Link Recovery Test for FR1 PCell
configured with CSI-RS-based BFD and LR in DRX mode 2728A.6.5.5.7.1 Test
Purpose and Environment 2728A.6.5.5.7.2 Test Requirements 2731A.6.5.5.8
Beam Failure Detection and Link Recovery Test for FR1 PCell configured
with SSB-based BFD and LR in non-DRX mode for a UE operating on a cell
with less than 5 MHz BW 2732A.6.5.5.8.1 Test Purpose and Environment
2732A.6.5.5.8.2 Test Requirements 2733A.6.5.6 Active BWP switch
2733A.6.5.6.1 DCI-based and Timer-based Active BWP Switch
2733A.6.5.6.1.1 NR FR1- NR FR1 DL active BWP switch of SCell with
non-DRX in SA 2733A.6.5.6.1.2 NR FR1 DL active BWP switch with non-DRX
in SA 2738A.6.5.6.2 RRC-based Active BWP Switch 2741A.6.5.6.2.1 NR FR1
DL active BWP switch of Cell with non-DRX in SA 2741A.6.5.6.3
Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs
2743A.6.5.6.3.1 NR FR1- NR FR1 DL active BWP switch on multiple CCs with
non-DRX in SA 2743A.6.5.6.4 SCell dormancy switch 2749A.6.5.6.4.1 NR FR1
PCell SCell dormancy switch of single FR1 SCell outside active time
2749A.6.5.6.4.1.1 Test Purpose and Environment 2749A.6.5.6.4.1.2 Test
Requirements 2753A.6.5.6.4.2 NR FR1 PCell SCell dormancy switch of two
FR1 SCells inside active time 2754A.6.5.6.4.2.1 Test Purpose and
Environment 2754A.6.5.6.4.2.2 Test Requirements 2759A.6.5.6.5
Simultaneous RRC-based Active BWP Switch on multiple CCs 2759A.6.5.6.5.1
NR FR1- NR FR1 DL active BWP switch on multiple CCs with non-DRX in SA
2759A.6.5.7 DL interruptions at switching between two uplink carriers
2763A.6.5.7.1 DL interruptions at switching between two uplink carriers
in FDD-TDD CA 2763A.6.5.7.1.1 Test Purpose and Environment
2763A.6.5.7.1.2 Test Requirements 2766A.6.5.7.2 DL interruptions at
switching between two uplink carriers in TDD-TDD CA 2766A.6.5.7.2.1 Test
Purpose and Environment 2766A.6.5.7.2.2 Test Requirements 2768A.6.5.7A
DL interruptions at switching between two uplink carriers with two
transmit antenna connectors 2768A.6.5.7A.1 DL interruptions at switching
between two uplink carriers in FDD-TDD CA 2768A.6.5.7A.1.1 Test Purpose
and Environment 2768A.6.5.7A.1.2 Test Requirements 2771A.6.5.7A.2 DL
interruptions at switching between two uplink carriers in TDD-TDD CA
2771A.6.5.7A.2.1 Test Purpose and Environment 2771A.6.5.7A.2.2 Test
Requirements 2773A.6.5.7B DL interruptions at switching between one
uplink band with one transmit antenna connector and one uplink band with
two transmit antenna connectors 2773A.6.5.7B.1 DL interruptions at
switching between two uplink bands in FDD-TDD CA 2773A.6.5.7B.1.1 Test
Purpose and Environment 2773A.6.5.7B.1.2 Test Requirements
2777A.6.5.7B.2 DL interruptions at switching between two uplink bands in
TDD-TDD CA 2777A.6.5.7B.2.1 Test Purpose and Environment
2777A.6.5.7B.2.2 Test Requirements 2781A.6.5.7C DL interruptions at
switching between two uplink bands with two transmit antenna connectors
2781A.6.5.7C.1 DL interruptions at switching between two uplink bands
with two transmit antenna connectors in FDD-TDD CA 2781A.6.5.7C.1.1 Test
Purpose and Environment 2781A.6.5.7C.1.2 Test Requirements
2785A.6.5.7C.2 DL interruptions at switching between two uplink bands
with two transmit antenna connectors in TDD-TDD CA 2785A.6.5.7C.2.1 Test
Purpose and Environment 2785A.6.5.7C.2.2 Test Requirements 2789A.6.5.7D
DL interruptions at UE switching across three or four uplink bands
2789A.6.5.7D.1 DL interruptions at switching across three uplink bands
in TDD-TDD CA for single TAG 2789A.6.5.7D.1.1 Test Purpose and
Environment 2789A.6.5.7D.1.2 Test Requirements 2793A.6.5.7D.2 DL
interruptions at switching across four uplink bands in FDD-TDD CA for
single TAG 2793A.6.5.7D.2.1 Test Purpose and Environment
2793A.6.5.7D.2.2 Test Requirements 2797A.6.5.7D.3 DL interruptions at
switching across three uplink bands in FDD-TDD CA for two TAGs
2797A.6.5.7D.3.1 Test Purpose and Environment 2797A.6.5.7D.3.2 Test
Requirements 2801A.6.5.7D.4 DL interruptions at switching across four
uplink bands in TDD-TDD CA for two TAGs 2801A.6.5.7D.4.1 Test Purpose
and Environment 2801A.6.5.7D.7.2 Test Requirements 2805A.6.5.8 UE
specific CBW change 2805A.6.5.8.1 UE specific CBW change on PCell in FR1
in non-DRX 2805A.6.5.8.1.1 Test Purpose and Environment 2805A.6.5.8.1.2
Test Requirements 2807A.6.5.9 Pathloss reference signal switching delay
2807A.6.5.9.1 MAC-CE based pathloss reference signal switch delay
2807A.6.5.9.1.1 Test Purpose and Environment 2807A.6.5.9.1.2 Test
Requirements 2810A.6.5.10 Conditional PSCell addition and release delay
(FR1 NR-DC) 2810A.6.5.10.1 Conditional PSCell Addition and Release Delay
2810A.6.5.10.1.1 Test purpose and environment 2810A.6.5.10.1.2 Test
Parameters 2810A.6.5.10.1.3 Test Requirements 2813A.6.5.11 PSCell
addition and release delay 2813A.6.5.11.1 Addition and Release Delay of
unknown NR FR1 PSCell 2813A.6.5.11.1.1 Test purpose and environment
2813A.6.5.11.1.2 Test Requirements 2815A.6.5.12 Subsequent conditional
PSCell addition/change 2816A.6.5.12.1 Intra-frequency subsequent CPC
from FR1-FR1 NR-DC to FR1-FR1 NR-DC 2816A.6.5.12.1.1 Test purpose and
environment 2816A.6.5.12.1.2 Test Parameters 2816A.6.5.12.1.3 Test
Requirements 2818A.6.5.12.2 Inter-frequency subsequent CPA from FR1-FR1
NR-DC to FR1-FR1 NR-DC 2819A.6.5.12.2.1 Test purpose and environment
2819A.6.5.12.2.2 Test Parameters 2819A.6.5.12.2.3 Test Requirements
2822A.6.5.13 Active TCI state switch delay 2822A.6.5.13.1 MAC-CE based
joint TCI state switch for mDCI with two TA when RTD is larger than CP
2822A.6.5.13.1.1 Test Purpose and Environment 2822A.6.5.13.1.2 Test
Requirements 2824A.6.6 Measurement procedure 2827A.6.6.1 Intra-frequency
Measurements 2827A.6.6.1.1 SA event triggered reporting tests without
gap under non-DRX 2827A.6.6.1.1.1 Test purpose and Environment
2827A.6.6.1.1.2 Test parameters 2827A.6.6.1.1.3 Test Requirements
2829A.6.6.1.2 SA event triggered reporting tests without gap under DRX
2829A.6.6.1.2.1 Test purpose and Environment 2829A.6.6.1.2.2 Test
parameters 2829A.6.6.1.2.3 Test Requirements 2831A.6.6.1.3 SA event
triggered reporting tests with per-UE gaps under non-DRX 2831A.6.6.1.3.1
Test purpose and Environment 2831A.6.6.1.3.2 Test parameters
2831A.6.6.1.3.3 Test Requirements 2833A.6.6.1.4 SA event triggered
reporting tests with per-UE gaps under DRX 2833A.6.6.1.4.1 Test purpose
and Environment 2833A.6.6.1.4.2 Test parameters 2834A.6.6.1.4.3 Test
Requirements 2836A.6.6.1.5 SA event triggered reporting tests without
gap under non-DRX with SSB index reading 2836A.6.6.1.5.1 Test purpose
and Environment 2836A.6.6.1.5.2 Test parameters 2836A.6.6.1.5.3 Test
Requirements 2837A.6.6.1.6 SA event triggered reporting tests with
per-UE gaps under non-DRX with SSB index reading 2837A.6.6.1.6.1 Test
purpose and Environment 2837A.6.6.1.6.2 Test parameters 2838A.6.6.1.6.3
Test Requirements 2839A.6.6.1.7 SA event triggered reporting tests under
DRX for UE configured with highSpeedMeasFlag-r16 2839A.6.6.1.7.1 Test
purpose and Environment 2839A.6.6.1.7.2 Test parameters 2839A.6.6.1.7.3
Test Requirements 2841A.6.6.1.8 SA event triggered reporting tests
without gap under DRX for UE configured with highSpeedMeasCA-Scell-r17
2842A.6.6.1.8.1 Test purpose and Environment 2842A.6.6.1.8.2 Test
parameters 2842A.6.6.1.8.3 Test Requirements 2844A.6.6.1.9 SA event
triggered reporting tests with MUSIM gap configured 2844A.6.6.1.9.1 Test
purpose and Environment 2844**A.6.6.1.9.2** Test parameters
2844**A.6.6.1.9.3** Test requirements 2846A.6.6.1.10 SA event triggered
reporting tests without gap under non-DRX when CD-SSB is outside active
BWP 2846A.6.6.1.10.1 Test purpose and Environment 2846A.6.6.1.10.2 Test
Requirements 2847A.6.6.1.11 SA event triggered reporting tests without
gap under non-DRX with NCD-SSB 2847A.6.6.1.11.1 Test purpose and
Environment 2847A.6.6.1.11.2 Test parameters 2847A.6.6.1.11.3 Test
Requirements 2848A.6.6.1.12 SA event triggered reporting tests without
gap under non-DRX with SSB index reading and 12 PRB SSB 2849A.6.6.1.12.1
Test purpose and Environment 2849A.6.6.1.12.2 Test parameters
2849A.6.6.1.12.3 Test Requirements 2849A.6.6.1.13 SA event triggered
reporting tests without gap under Cell DTX 2849A.6.6.1.13.1 Test purpose
and Environment 2850A.6.6.1.13.2 Test parameters 2850A.6.6.1.13.3 Test
Requirements 2851A.6.6.2 Inter-frequency Measurements 2852A.6.6.2.1 SA
event triggered reporting tests for FR1 without SSB time index detection
when DRX is not used 2852A.6.6.2.1.1 Test Purpose and Environment
2852A.6.6.2.1.2 Test Requirements 2854A.6.6.2.2 SA event triggered
reporting tests for FR1 without SSB time index detection when DRX is
used 2854A.6.6.2.2.1 Test Purpose and Environment 2854A.6.6.2.2.2 Test
Requirements 2857A.6.6.2.3 Void 2857A.6.6.2.4 Void 2857A.6.6.2.5 SA
event triggered reporting tests for FR1 with SSB time index detection
when DRX is not used 2857A.6.6.2.5.1 Test Purpose and Environment
2857A.6.6.2.5.2 Test Requirements 2860A.6.6.2.6 SA event triggered
reporting tests for FR1 with SSB time index detection when DRX is used
2860A.6.6.2.6.1 Test Purpose and Environment 2860A.6.6.2.6.2 Test
Requirements 2862A.6.6.2.7 Void 2863A.6.6.2.8 Void 2863A.6.6.2.9 SA
event triggered reporting tests with additional mandatory gap pattern
2863A.6.6.2.9.1 Test Purpose and Environment 2863A.6.6.2.9.2 Test
Requirements 2865A.6.6.2.10 SA event triggered reporting tests for FR1
when DRX is used 2865A.6.6.2.10.1 Test Purpose and Environment
2865A.6.6.2.10.2 Test Requirements 2867A.6.6.2.12 SA event triggered
reporting tests for FR1 without SSB time index detection when DRX is
used for UE configured with highSpeedMeasInterFreq-r17 2870A.6.6.2.12.1
Test Purpose and Environment 2870A.6.6.2.12.2 Test Requirements
2872A.6.6.2.13 SA event triggered reporting tests for FR1 with
measurement gap with priority and periodic MUSIM gap configured
2873A.6.6.2.13.1 Test Purpose and Environment 2873A.6.6.2.13.2 Test
Requirements 2875A.6.6.2.14 SA event triggered reporting tests for FR1
with measurement gap without priority and periodic MUSIM gapconfigured
2875A.6.6.2.14.1 Test Purpose and Environment 2875A.6.6.2.14.2 Test
Requirements 2878A.6.6.2.15 SA event triggered reporting tests for FR1
with 3 MHz Channel Bandwidth configured without SSB time index detection
when DRX is used 2878A.6.6.2.15.1 Test Purpose and Environment
2878A.6.6.2.15.2 Test Requirements 2879A.6.6.3 Inter-RAT Measurements
2879A.6.6.3.1 SA NR - E-UTRAN event-triggered reporting in non-DRX in
FR1 2879A.6.6.3.1.1 Test Purpose and Environment 2879A.6.6.3.1.2 Test
Requirements 2882A.6.6.3.2 SA NR - E-UTRAN event-triggered reporting in
DRX in FR1 2882A.6.6.3.2.1 Test Purpose and Environment 2882A.6.6.3.2.2
Test Requirements 2885A.6.6.3.3 SA NR - E-UTRAN event-triggered
reporting in DRX in FR1 for UE configured with highSpeedMeasFlag-r16
2886A.6.6.3.3.1 Test Purpose and Environment 2886A.6.6.3.3.2 Test
Requirements 2889A.6.6.4 L1-RSRP measurement for beam reporting
2889A.6.6.4.1 SSB based L1-RSRP measurement when DRX is not used
2889A.6.6.4.1.1 Test Purpose and Environment 2889A.6.6.4.1.2 Test
parameters 2889A.6.6.4.1.3 Test Requirements 2891A.6.6.4.2 SSB based
L1-RSRP measurement when DRX is used 2891A.6.6.4.2.1 Test Purpose and
Environment 2891A.6.6.4.2.2 Test parameters 2891A.6.6.4.2.3 Test
Requirements 2893A.6.6.4.3 CSI-RS based L1-RSRP measurement when DRX is
not used 2893A.6.6.4.3.1 Test Purpose and Environment 2893A.6.6.4.3.2
Test parameters 2893A.6.6.4.3.3 Test Requirements 2895A.6.6.4.4 CSI-RS
based L1-RSRP measurement when DRX is used 2895A.6.6.4.4.1 Test Purpose
and Environment 2895A.6.6.4.4.2 Test parameters 2895A.6.6.4.4.3 Test
Requirements 2896A.6.6.4.5 SSB based L1-RSRP measurement when DRX is
used for UE configured with *highSpeedMeasFlag-r16* 2897A.6.6.4.5.1 Test
Purpose and Environment 2897A.6.6.4.5.2 Test parameters 2897A.6.6.4.5.3
Test Requirements 2898A.6.6.4.6 Inter-cell SSB based L1-RSRP
measurements on FR1 PCell when DRX is used 2899A.6.6.4.6.1 Test Purpose
and Environment 2899A.6.6.4.6.2 Test parameters 2899A.6.6.4.6.3 Test
Requirements 2900A.6.6.4.7 SSB based L1-RSRP measurement when DRX is not
used when CD-SSB is outside active BWP 2901A.6.6.4.7.1 Test Purpose and
Environment 2901A.6.6.4.7.2 Test Requirements 2901A.6.6.4.8 CSI-RS based
L1-RSRP measurement when DRX is not used when CD-SSB is outside active
BWP 2901A.6.6.4.8.1 Test Purpose and Environment 2901A.6.6.4.9 SSB based
L1-RSRP measurement for UE supporting NCD-SSB based L1 measurement
outside active BWP when DRX is not used 2901A.6.6.4.9.1 Test Purpose and
Environment 2901A.6.6.4.9.2 Test parameters 2902A.6.6.4.9.3 Test
Requirements 2903A.6.6.5 Inter-RAT UTRAN FDD measurements 2903A.6.6.5.1
SA NR - UTRAN FDD event-triggered reporting in non-DRX in FR1
2903A.6.6.5.1.1 Test Purpose and Environment 2903A.6.6.5.1.2 Test
Requirements 2906A.6.6.6 CLI measurements 2906A.6.6.6.1 SRS-RSRP
measurement with DRX 2906A.6.6.6.1.1 Test Purpose and Environment
2906A.6.6.6.1.2 Test Parameters 2906A.6.6.6.1.3 Test Requirements
2908A.6.6.6.2 CLI-RSSI measurement with DRX 2908A.6.6.6.2.1 Test Purpose
and Environment 2908A.6.6.6.2.2 Test Parameters 2909A.6.6.6.2.3 Test
Requirements 2910A.6.6.7 NR measurements with autonomous gaps
2910A.6.6.7.1 SA intra-frequency CGI identification of NR neighbor cell
in FR1 2910A.6.6.7.1.1 Test Purpose and Environment 2910A.6.6.7.1.2 Test
Parameters 2910A.6.6.7.1.3 Test Requirements 2913A.6.6.7.2
Identification of a new CGI of inter-RAT E-UTRA cell using autonomous
gaps in NR SA 2913A.6.6.7.2.1 Test Purpose and Environment
2913A.6.6.7.2.2 Test Requirements 2915A.6.6.8 L1-SINR measurement for
beam reporting 2916A.6.6.8.1 L1-SINR measurement with CSI-RS based CMR
and no dedicated IMR configured when DRX is used 2916A.6.6.8.1.1 Test
Purpose and Environment 2916A.6.6.8.1.2 Test parameters 2916A.6.6.8.1.3
Test Requirements 2918A.6.6.8.2 L1-SINR measurement with SSB based CMR
and dedicated IMR when DRX is not used 2918A.6.6.8.2.1 Test Purpose and
Environment 2918A.6.6.8.2.2 Test parameters 2918A.6.6.8.2.3 Test
Requirements 2920A.6.6.8.3 L1-SINR measurement with CSI-RS based CMR and
dedicated IMR configured when DRX is not used 2920A.6.6.8.3.1 Test
Purpose and Environment 2920A.6.6.8.3.2 Test parameters 2921A.6.6.8.3.3
Test Requirements 2922A.6.6.9 Idle Mode CA/DC Measurements 2922A.6.6.9.1
SA Idle mode CA/DC measurement for FR1 2922A.6.6.9.1.1 Test Purpose and
Environment 2922A.6.6.9.1.2 Test Requirements 2926A.6.6.9.2 Idle mode
fast CA/DC eEMR measurement for FR1 without valid reporting
2926A.6.6.9.2.1 Test Purpose and Environment 2926A.6.6.9.2.2 Test
Requirements 2929A.6.6.9.3 Idle mode fast CA/DC cell reselection
measurement for FR1 without valid reporting 2929A.6.6.9.3.1 Test Purpose
and Environment 2929A.6.6.9.3.2 Test Requirements 2932A.6.6.9.4 Idle
mode fast CA/DC cell reselection measurement for FR1 with valid
reporting 2932A.6.6.9.4.1 Test Purpose and Environment 2932A.6.6.9.4.2
Test Requirements 2935A.6.6.10 CSI-RS based intra-frequency Measurements
2935A.6.6.10.1 SA event triggered reporting tests without gap under
non-DRX 2935A.6.6.10.1.1 Test purpose and Environment 2935A.6.6.10.1.2
Test Requirements 2937A.6.6.11 CSI-RS based inter-frequency Measurements
2938A.6.6.11.1 SA event triggered reporting tests with gap under DRX
2938A.6.6.11.1.1 Test Purpose and Environment 2938A.6.6.11.1.2 Test
Requirements 2940A.6.6.12 RSTD measurements 2940A.6.6.12.1 NR RSTD
measurement reporting delay test case for single positioning frequency
layer in FR1 SA 2940A.6.6.12.1.1 Test Purpose and Environment
2940A.6.6.12.1.2 Test Requirements 2944A.6.6.12.2 NR RSTD measurement
reporting delay test case for dual positioning frequency layers in FR1
SA 2944A.6.6.12.2.1 Test Purpose and Environment 2944A.6.6.12.2.2 Test
Requirements 2947A.6.6.12.3 NR RSTD measurement reporting delay test
case for single positioning frequency layer with reduced number of
samples in FR1 SA 2948A.6.6.12.3.1 Test Purpose and Environment
2948A.6.6.12.3.2 Test Requirements 2951A.6.6.12.4 NR RSTD measurement
reporting delay test case for single positioning frequency layer in FR1
SA without measurement gap 2951A.6.6.12.4.1 Test Purpose and Environment
2951A.6.6.12.4.2 Test Requirements 2954A.6.6.12.5 NR RSTD measurement
reporting delay test case for single positioning frequency layer in FR1
SA in RRC\_CONNECTED state with Rx TEG 2954A.6.6.12.5.1 Test Purpose and
Environment 2954A.6.6.12.5.2 Test Requirements 2958A.6.6.12.6 NR RSTD
measurement reporting delay test case for PRS aggregation in FR1 SA in
RRC\_CONNECTED mode 2958A.6.6.12.6.1 Test Purpose and Environment
2958A.6.6.12.6.2 Test Requirements 2964A.6.6.13 PRS-RSRP measurements
2964A.6.6.13.1 PRS-RSRP reporting delay test case for single positioning
frequency layer 2964A.6.6.13.1.1 Test purpose and Environment
2964A.6.6.13.1.2 Test Requirements 2966A.6.6.13.2 PRS-RSRP reporting
delay test case for dual positioning frequency layer 2966A.6.6.13.2.1
Test purpose and Environment 2966A.6.6.13.2.2 Test Requirements
2969A.6.6.13.3 PRS-RSRP reporting delay test case for reduced number of
samples 2969A.6.6.13.3.1 Test purpose and Environment 2969A.6.6.13.3.2
Test Requirements 2971A.6.6.13.4 PRS-RSRP reporting delay test case for
single positioning frequency layer outside MG 2971A.6.6.13.4.1 Test
purpose and Environment 2971A.6.6.14 UE Rx-Tx time difference
measurements 2974A.6.6.14.1 UE Rx-Tx time difference measurement for
single positioning frequency layer in FR1 SA 2974A.6.6.14.1.1 Test
purpose and environment 2974A.6.6.14.1.2 Test requirements
2976A.6.6.14.2 UE Rx-Tx time difference measurement for dual positioning
frequency layers in FR1 SA 2976A.6.6.14.2.1 Test purpose and environment
2976A.6.6.14.2.2 Test requirements 2978A.6.6.14.3 UE Rx-Tx time
difference measurement for single positioning frequency layer in FR1 SA
with reduced sample number 2979A.6.6.14.3.1 Test purpose and environment
2979A.6.6.14.3.2 Test requirements 2981A.6.6.14.4 UE Rx-Tx time
difference measurement without gaps in FR1 SA 2981A.6.6.14.4.1 Test
purpose and environment 2981A.6.6.14.4.2 Test requirements
2983A.6.6.14.5 UE Rx-Tx time difference measurement for single
positioning frequency layer in FR1 SA with multiple RxTx TEGs
2983A.6.6.14.4.1 Test purpose and environment 2983A.6.6.14.4.2 Test
requirements 2985A.6.6.14.6 UE Rx-Tx time difference measurements with
PRS bandwidth aggregation in FR1 SA 2986A.6.6.14.6.1 Test purpose and
environment 2986A.6.6.14.6.2 Test requirements 2989A.6.6.15 Idle Mode
measurements of inter-RAT DC candidate cells for early reporting
2989A.6.6.15.1 Test Purpose and Environment 2989A.6.6.15.2 Test
Requirements 2993A.6.6.16 PRS-RSRPP measurements 2994A.6.6.16.1
PRS-RSRPP reporting delay test case for single positioning frequency
layer in FR1 in RRC\_CONNECTED state 2994A.6.6.16.1.1 Test purpose and
Environment 2994A.6.6.16.1.2 Test Requirements 2996A.6.6.16.2 PRS-RSRPP
reporting delay test case with reduced number of samples for single
positioning frequency layer in FR1 in RRC\_CONNECTED state
2996A.6.6.16.2.1 Test purpose and Environment 2996A.6.6.16.2.2 Test
Requirements 2998A.6.6.16.3 PRS-RSRPP reporting delay test case for
single positioning frequency layer in FR1 in RRC\_CONNECTED state
without measurement gap 2998A.6.6.16.3.1 Test purpose and Environment
2998A.6.6.16.3.2 Test Requirements 3000A.6.6.17 SA event triggered
reporting tests with Pre-MG 3001A.6.6.17.1 SA event triggered reporting
tests with autonomous activation/deactivation Pre-MG 3001A.6.6.17.1.1
Test purpose and Environment 3001A.6.6.17.1.2 Test parameters
3001A.6.6.17.1.3 Test Requirements 3003A.6.6.17.2 SA event triggered
reporting tests with pre-configured measurement gaps and
network-controlled activation/deactivation 3004A.6.6.17.2.1 Test purpose
and Environment 3004A.6.6.17.2.2 Test parameters 3004A.6.6.17.2.3 Test
Requirements 3006A.6.6.17.3 Void 3007A.6.6.17.3.1 Void 3007A.6.6.17.3.2
Void 3007A.6.6.17.3.3 Void 3007A.6.6.18 SA event triggered reporting
tests with concurrent gaps 3007A.6.6.18.1 SA event triggered reporting
tests for FR1 concurrent gaps with non-overalpping scenario for
SSB-based measurements in both inter-frequency layers 3007A.6.6.18.1.1
Test Purpose and Environment 3007A.6.6.18.1.2 Test Requirements
3009A.6.6.18.2 SA event triggered reporting tests for FR1 concurrent gap
with partially partial overalpping scenario for SSB-based measurements
in both inter-frequency layers 3009A.6.6.18.2.1 Test Purpose and
Environment 3009A.6.6.18.2.2 Test Requirements 3012A.6.6.18.3 SA NR -
E-UTRAN and NR FR1 concurrent event-triggered reporting in non-DRX in
FR1 3012A.6.6.18.3.1 Test Purpose and Environment 3012A.6.6.18.3.2 Test
Requirements 3016A.6.6.18.4 SA event triggered reporting tests for PRS
and SSB measurement in FR1 without SSB time index detection when DRX is
not used 3017A.6.6.18.4.1 Test Purpose and Environment 3017A.6.6.18.4.2
Test Requirements 3019A.6.6.19 SA event triggered reporting tests with
NCSG 3020A.6.6.19.1 SA event triggered reporting tests with NCSG under
non-DRX in FR1 3020A.6.6.19.1.1 Test purpose and Environment
3020A.6.6.19.1.2 Test parameters 3020A.6.6.19.1.3 Test Requirements
3022A.6.6.19.2 SA event triggered reporting tests for FR1 with NCSG for
inter-frequency measurement 3022A.6.6.19.2.1 Test Purpose and
Environment 3022A.6.6.19.2.2 Test parameters 3022A.6.6.19.2.3 Test
Requirements 3025A.6.6.19.3 SA NR - E-UTRAN event-triggered reporting in
non-DRX in FR1 with NCSG 3025A.6.6.19.3.1 Test Purpose and Environment
3025A.6.6.19.3.2 Test parameters 3025A.6.6.19.3.3 Test Requirements
3028A.6.6.19.4 Event triggered reporting on SCC with deactivated SCell
test with per-UE NCSG under non-DRX 3029A.6.6.19.4.1 Test purpose and
Environment 3029A.6.6.19.4.2 Test parameters 3029A.6.6.19.4.3 Test
Requirements 3031A.6.6.20 UE Rx-Tx time difference measurement for
propagation delay compensation 3031A.6.6.20.1 Test purpose and
environment 3031A.6.6.20.2 Test requirements 3033A.6.6.21 UE Rx-Tx time
difference measurement with TRS for RTT-based PDC in FR1 SA
3033A.6.6.21.1 Test purpose and environment 3033A.6.6.21.2 Test
requirements 3035A.6.6.22 SA event triggered reporting tests for
concurrent measurement gaps with Pre-MG 3035A.6.6.22.1 SA event
triggered reporting tests for FR1 concurrent gap with Pre-MG with
partially partial overalpping scenario for SSB-based measurements in
both intra-frequency and inter-frequency layers 3035A.6.6.22.1.1 Test
Purpose and Environment 3035A.6.6.22.1.2 Test Requirements
3038A.6.6.22.2 SA event triggered reporting tests for concurrent gap
with pre-configured gaps and network-controlled activation/deactivation
3039A.6.6.22.2.1 Test purpose and Environment 3039A.6.6.22.2.2 Test
parameters 3039A.6.6.22.2.3 Test Requirements 3041A.6.6.23 SA event
triggered reporting tests for concurrent measurement gaps with NCSG
3042A.6.6.23.1 SA event triggered reporting tests for FR1 concurrent
gaps with NCSG for partially partial overalpping scenario for SSB-based
measurements in both inter-frequency layers \[one MG + one NCSG\]
3042A.6.6.23.1.1 Test Purpose and Environment 3042A.6.6.23.1.2 Test
Requirements 3044A.6.6.23.2 SA event triggered reporting tests for FR1
concurrent gaps with NCSG for partially partial overalpping scenario for
SSB-based measurements in both inter-frequency layers \[two NCSG\]
3045A.6.6.23.2.1 Test Purpose and Environment 3045A.6.6.23.2.2 Test
Requirements 3047A.6.6.23.3 Event triggered reporting on SCC with
deactivated SCell test with per-UE Con-NCSG under non-DRX
3047A.6.6.23.3.1 Test purpose and Environment 3047A.6.6.23.3.2 Test
parameters 3048A.6.6.23.3.3 Test Requirements 3050A.6.6.24 SA event
triggered reporting tests with NeedForGap in FR1 3050A.6.6.24.1 SA event
triggered reporting tests without gaps, with interruptions, under
non-DRX 3050A.6.6.24.1.1 Test purpose and Environment 3050A.6.6.24.1.2
Test parameters 3050A.6.6.24.1.3 Test Requirements 3052A.6.6.24.2 SA
event triggered reporting tests for FR1 without gap with interruption
for inter-frequency measurement with SSB time index detection when DRX
is not used 3052A.6.6.24.2.1 Test Purpose and Environment
3052A.6.6.24.2.2 Test parameters 3052A.6.6.24.2.3 Test Requirements
3055A.6.6.24.3 SA event triggered reporting tests for FR1 with
'no-gap-with-interruption', without measurement gap or DRX
3055A.6.6.24.3.1 Test Purpose and Environment 3055A.6.6.24.3.2 Test
Requirements 3057A.6.6.24.4 SA event triggered reporting tests for FR1
NeedForGaps without gap without interruption when DRX is not used
3057A.6.6.24.4.1 Test Purpose and Environment 3057A.6.6.24.4.2 Test
parameters 3058A.6.6.24.4.3 Test Requirements 3060A.6.6.24.5 SA event
triggered reporting tests without gap under non-DRX for UE indicating
*no-gap-no-interruption* 3060A.6.6.24.5.1 Test purpose and Environment
3060A.6.6.24.5.2 Test parameters 3060A.6.6.24.5.3 Test Requirements
3062A.6.6.25 SA NR - E-UTRAN event-triggered without measurement gaps
3062A.6.6.25.1 SA NR - E-UTRAN event-triggered reporting in non-DRX in
FR1 3062A.6.6.25.1.1 Test Purpose and Environment 3062A.6.6.25.1.2 Test
Requirements 3065A.6.6.25.2 SA NR - E-UTRAN event-triggered reporting
without gap under non-DRX in FR1 3066A.6.6.25.2.1 Test Purpose and
Environment 3066A.6.6.25.2.2 Test parameters 3066A.6.6.25.2.3 Test
Requirements 3067A.6.6.25.3 SA NR - E-UTRAN event-triggered reporting in
non-DRX in FR1 for UE capable of inter-RAT EUTRAN measurement without
gap when CRS is contained within UE's active DL BWP 3067A.6.6.25.3.1
Test Purpose and Environment 3067A.6.6.25.3.2 Test Requirements
3070A.6.6.26 LTM Intra-frequency L1-RSRP measurement 3070A.6.6.26.1
Intra-frequency SSB based L1-RSRP measurement in FR1 3070A.6.6.26.1.1
Test Purpose and Environment 3070A.6.6.26.1.2 Test Parameters
3071A.6.6.26.1.3 Test Requirements 3073A.6.6.27 LTM Inter-frequency
L1-RSRP measurement with measurement gap 3073A.6.6.27.1 Inter-frequency
SSB based L1-RSRP measurement with measurement gap 3073A.6.6.27.1.1 Test
Purpose and Environment 3073A.6.6.27.1.2 Test parameters
3073A.6.6.27.1.3 Test Requirements 3075A.6.6.28 LTM Inter-frequency
L1-RSRP measurement without measurement gap 3075A.6.6.28.1
Inter-frequency SSB based L1-RSRP measurement without measurement gap
3075A.6.6.28.1.1 Test Purpose and Environment 3075A.6.6.28.1.2 Test
parameters 3076A.6.6.28.1.3 Test Requirements 3078A.6.6.29 RSCPD
Measurements 3078A.6.6.29.1 NR RSCPD with RSTD measurement reporting
delay test case for single positioning frequency layer in FR1 SA in
RRC\_CONNECTED state 3078A.6.6.29.1.1 Test Purpose and Environment
3078A.6.6.29.1.2 Test Requirements 3086A.6.6.30 RSCP Measurements
3086A.6.6.30.1 DL RSCP with UE Rx-Tx time difference measurement for
single positioning frequency layer in FR1 SA 3086A.6.6.30.1.1 Test
purpose and environment 3086A.6.6.30.1.2 Test requirements 3090A.6.7
Measurement Performance requirements 3090A.6.7.1 SS-RSRP 3090A.6.7.1.1
SA: intra-frequency case measurement accuracy with FR1 serving cell and
FR1 target cell 3090A.6.7.1.1.1 Test Purpose and Environment
3090A.6.7.1.1.2 Test parameters 3090A.6.7.1.1.3 Test Requirements
3094A.6.7.1.2 SA inter-frequency case measurement accuracy with FR1
serving cell and FR1 target cell 3094A.6.7.1.2.1 Test Purpose and
Environment 3094A.6.7.1.2.2 Test parameters 3094A.6.7.1.2.3 Test
Requirements 3097A.6.7.1.3 Void 3097A.6.7.2 SS-RSRQ 3097A.6.7.2.1 SA:
Intra-frequency measurement accuracy with FR1 serving cell and FR1
target cell 3097A.6.7.2.1.1 Test Purpose and Environment 3097A.6.7.2.1.2
Test Parameters 3097A.6.7.2.1.3 Test Requirements 3100A.6.7.2.2 SA
Inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell 3101A.6.7.2.2.1 Test Purpose and Environment 3101A.6.7.2.2.2
Test Parameters 3101A.6.7.2.2.3 Test Requirements 3104A.6.7.3 SS-SINR
3104A.6.7.3.1 SA intra-frequency measurement accuracy with FR1 serving
cell and FR1 target cell 3104A.6.7.3.1.1 Test Purpose and Environment
3104A.6.7.3.1.2 Test Parameters 3104A.6.7.3.1.3 Test Requirements
3107A.6.7.3.2 SA Inter-frequency measurement accuracy with FR1 serving
cell and FR1 target cell 3107A.6.7.3.2.1 Test Purpose and Environment
3107A.6.7.3.2.2 Test Parameters 3108A.6.7.3.2.3 Test Requirements
3111A.6.7.4 L1-RSRP measurement for beam reporting 3111A.6.7.4.1 SSB
based L1-RSRP measurement 3111A.6.7.4.1.1 Test Purpose and Environment
3111A.6.7.4.1.2 Test parameters 3111A.6.7.4.1.3 Test Requirements
3114A.6.7.4.2 CSI-RS based L1-RSRP measurement on resource set with
repetition off 3114A.6.7.4.2.1 Test Purpose and Environment
3114A.6.7.4.2.2 Test parameters 3114A.6.7.4.2.3 Test Requirements
3117A.6.7.5 E-UTRAN RSRP 3117A.6.7.5.1 SA: inter-RAT measurement
accuracy with FR1 serving cell 3117A.6.7.5.1.1 Test Purpose and
Environment 3117A.6.7.5.1.2 Test parameters 3117A.6.7.5.1.3 Test
Requirements 3120A.6.7.6 E-UTRAN RSRQ 3120A.6.7.6.1 SA: inter-RAT
measurement accuracy with FR1 serving cell 3120A.6.7.6.1.1 Test Purpose
and Environment 3120A.6.7.6.1.2 Test parameters 3120A.6.7.6.1.3 Test
Requirements 3123A.6.7.7 E-UTRAN RS-SINR 3124A.6.7.7.1 SA: inter-RAT
measurement accuracy with FR1 serving cell 3124A.6.7.7.1.1 Test Purpose
and Environment 3124A.6.7.7.1.2 Test parameters 3124A.6.7.7.1.3 Test
Requirements 3127A.6.7.8 CLI measurements 3127A.6.7.8.1 SA SRS-RSRP
measurement accuracy with FR1 serving cell 3127A.6.7.8.1.1 Test Purpose
and Environment 3127A.6.7.8.1.2 Test parameters 3127A.6.7.8.1.3 Test
Requirements 3130A.6.7.8.2 SA CLI-RSSI measurement accuracy with FR1
serving cell 3130A.6.7.8.2.1 Test Purpose and Environment
3130A.6.7.8.2.2 Test parameters 3131A.6.7.8.2.3 Test Requirements
3132A.6.7.9 L1-SINR measurement for beam reporting 3132A.6.7.9.2 L1-SINR
measurement with SSB based CMR and dedicated IMR 3135A.6.7.9.2.1 Test
Purpose and Environment 3135A.6.7.9.2.2 Test parameters 3136A.6.7.9.2.3
Test Requirements 3139A.6.7.9.3 L1-SINR measurement with CSI-RS based
CMR and dedicated IMR 3139A.6.7.9.3.1 Test Purpose and Environment
3139A.6.7.9.3.2 Test parameters 3139A.6.7.9.3.3 Test Requirements
3142A.6.7.10 CSI-RSRP 3142A.6.7.10.1 SA: intra-frequency case
measurement accuracy with FR1 serving cell and FR1 target cell
3142A.6.7.9.10.1 Test Purpose and Environment 3142A.6.7.9.10.2 Test
parameters 3142A.6.7.10.1.3 Test Requirements 3145A.6.7.10.2 SA
inter-frequency case measurement accuracy with FR1 serving cell and FR1
target cell 3145A.6.7.9.10.1 Test Purpose and Environment
3145A.6.7.10.2.2 Test parameters 3146A.6.7.10.2.3 Test Requirements
3148A.6.7.11 CSI-RSRQ 3149A.6.7.11.1 SA: Intra-frequency measurement
accuracy with FR1 serving cell and FR1 target cell 3149A.6.7.11.1.1 Test
Purpose and Environment 3149A.6.7.11.1.2 Test Parameters
3149A.6.7.11.1.3 Test Requirements 3152A.6.7.11.2 SA Inter-frequency
measurement accuracy with FR1 serving cell and FR1 target cell
3152A.6.7.11.2.1 Test Purpose and Environment 3152A.6.7.11.2.2 Test
Parameters 3152A.6.7.11.2.3 Test Requirements 3156A.6.7.12 CSI-SINR
3156A.6.7.12.1 SA intra-frequency measurement accuracy with FR1 serving
cell and FR1 target cell 3156A.6.7.12.1.1 Test Purpose and Environment
3156A.6.7.12.1.2 Test Parameters 3156A.6.7.12.1.3 Test Requirements
3159A.6.7.12.2 SA Inter-frequency measurement accuracy with FR1 serving
cell and FR1 target cell 3159A.6.7.12.2.1 Test Purpose and Environment
3159A.6.7.12.2.2 Test Parameters 3159A.6.7.12.2.3 Test Requirements
3162A.6.7.13 RSTD measurements 3162A.6.7.13.1 RSTD measurement accuracy
test case for single positioning frequency layer 3162A.6.7.13.1.1 Test
purpose and Environment 3162A.6.7.13.1.2 Test Requirements
3164A.6.7.13.2 RSTD measurement accuracy test case for dual positioning
frequency layer 3164A.6.7.13.2.1 Test purpose and Environment
3164A.6.7.13.2.2 Test Requirements 3166A.6.7.13.3 RSTD measurement
accuracy test case with reduced number of samples for single positioning
frequency layer in FR1 in RRC\_CONNECTED state 3166A.6.7.13.3.1 Test
purpose and Environment 3166A.6.7.13.3.2 Test Requirements
3168A.6.7.13.4 RSTD measurement accuracy test case with Rx TEG
3168A.6.7.13.5 NR RSTD measurement accuracy test case for PRS
aggregation in FR1 SA in RRC\_CONNECTED mode 3170A.6.7.13.5.1 Test
purpose and Environment 3170A.6.7.13.5.2 Test Requirements 3173A.6.7.14
PRS-RSRP measurements 3173A.6.7.14.1 SA: measurement accuracy with PRS
in FR1 3173A.6.7.14.1.1 Test Purpose and Environment 3173A.6.7.14.1.2
Test parameters 3173A.6.7.14.1.3 Test Requirements 3175A.6.7.14.2 SA:
measurement accuracy with PRS in FR1 with reduced sample number
3175A.6.7.14.2.1 Test Purpose and Environment 3175A.6.7.14.2.2 Test
parameters 3175A.6.7.14.2.3 Test Requirements 3177A.6.7.14.3 Void
3177A.6.7.14.3.1 Void 3177A.6.7.14.3.2 Void 3177A.6.7.14.3.3 Void
3177A.6.7.15 UE Rx-Tx time difference measurements 3177A.6.7.15.1 UE
Rx-Tx time difference measurement accuracy for single positioning
frequency layer in FR1 SA 3177A.6.7.15.1.1 Test purpose and environment
3177A.6.7.15.1.2 Test parameters 3178A.6.7.15.1.3 Test requirements
3179A.6.7.15.2 UE Rx-Tx time difference measurement accuracy with
reduced number of samples in FR1 SA 3179A.6.7.15.2.1 Test purpose and
environment 3179A.6.7.15.2.2 Test parameters 3180A.6.7.15.2.3 Test
requirements 3181A.6.7.15.3 UE Rx-Tx time difference measurement
accuracy with RxTx TEG 3181A.6.7.15.3.1 Test purpose and environment
3181A.6.7.15.3.2 Test parameters 3182A.6.7.15.3.3 Test requirements
3184A.6.7.15.4 UE Rx-Tx time difference measurement accuracy with PRS
bandwidth aggregation in FR1 SA 3184A.6.7.15.4.1 Test purpose and
environment 3184A.6.7.15.4.2 Test requirements 3187A.6.7.16 PRS-RSRPP
measurements 3187A.6.7.16.1 SA: measurement accuracy with PRS in FR1
3187A.6.7.16.1.1 Test Purpose and Environment 3187A.6.7.16.1.2 Test
parameters 3187A.6.7.16.1.3 Test Requirements 3189A.6.7.16.2 SA:
measurement accuracy with reduced PRS samples in FR1 3189A.6.7.16.2.1
Test Purpose and Environment 3189A.6.7.16.2.2 Test parameters
3190A.6.7.17 LTM L1-RSRP measurement 3191A.6.7.17.1 Inter-frequency
L1-RSRP accuracy requirements for neighbour cell in FR1 3191A.6.7.17.1.1
Test Purpose and Environment 3191A.6.7.17.1.2 Test parameters
3192A.6.7.17.1.3 Test Requirements 3195A.6.7.18 TDCP amplitude
measurement accuracy 3195A.6.7.18.1 TDCP amplitude measurement accuracy
in FR1 3195A.6.7.18.1.1 Test Purpose and Environment 3195A.6.7.18.1.2
Test parameters 3195A.6.7.18.1.3 Test Requirements 3196A.6.7.19 RSCPD
Measurements 3197A.6.7.19.1 RSCPD with RSTD measurement accuracy in FR1
SA in RRC\_CONNECTED 3197A.6.7.19.1.1 Test purpose and environment
3197A.6.7.19.1.2 Test parameters 3197A.6.7.19.1.3 Test requirements
3200A.6.7.20 RSCP Measurements 3200A.6.7.20.1 RSCP with UE Rx-Tx time
difference measurement accuracy in FR1 SA 3200A.6.7.20.1.1 Test purpose
and environment 3200A.6.7.20.1.2 Test parameters 3201A.6.7.20.1.3 Test
requirements 3204A.6.8 Measurement procedure in RRC\_INACTIVE
3204A.6.8.1 RSTD measurements 3204A.6.8.1.1 NR RSTD measurement
reporting delay test case for single positioning frequency layer in FR1
SA in RRC\_INACTIVE state 3204A.6.8.1.1.1 Test Purpose and Environment
3204A.6.8.1.1.2 Test Requirements 3207A.6.8.1.2 NR RSTD measurement
reporting delay test case with reduced number of samples in
RRC\_INACTIVE, FR1 SA 3207A.6.8.1.2.1 Test Purpose and Environment
3207A.6.8.1.2.1 Test Purpose and Environment 3207A.6.8.1.2.2 Test
Requirements 3210A.6.8.1.3 NR RSTD measurement reporting delay test case
for PRS aggregation in FR1 SA in RRC\_INACTIVE state 3211A.6.8.1.3.1
Test purpose and environment 3211A.6.8.1.3.2 Test requirements
3214A.6.8.1.4 NR RSTD measurement reporting delay test case for single
positioning frequency layer in FR1 SA in RRC\_INACTIVE state when eDRX
cycle \> 10.24s for non-RedCap UE 3215A.6.8.1.4.1 Test Purpose and
Environment 3215A.6.8.1.4.2 Test Requirements 3218A.6.8.2 PRS-RSRP
measurements 3218A.6.8.2.1 PRS-RSRP reporting delay test case for single
positioning frequency layer in RRC\_INACTIVE 3218A.6.8.2.1.1 Test
purpose and Environment 3218A.6.8.2.1.2 Test Requirements 3220A.6.8.2.2
PRS-RSRP reporting delay test case with reduced number of samples in
RRC\_INACTIVE 3220A.6.8.2.2.1 Test purpose and Environment
3220A.6.**8.2.2**.2 Test Requirements 3222A.6.8.2.3 PRS-RSRP reporting
delay test case in RRC\_INACTIVE state in FR1 with eDRX cycle \> 10.24s
3223A.6.8.2.3.1 Test purpose and Environment 3223A.6.8.2.3.2 Test
Requirements 3225A.6.8.3 UE Rx-Tx time difference measurements
3226A.6.8.3.1 UE Rx-Tx time difference measurement for single
positioning frequency layer in FR1 SA 3226A.6.8.3.1.1 Test purpose and
environment 3226A.6.8.3.1.2 Test requirements 3228A.6.8.3.2 UE Rx-Tx
time difference measurement with reduced number of samples in
RRC\_INACTIVE, FR1 SA 3228A.6.8.3.2.1 Test purpose and environment
3228A.6.**8.3.2**.2 Test requirements 3230A.6.8.3.3 UE Rx-Tx time
difference measurement for single positioning frequency layer with eDRX
\> 10.24s in FR1 SA 3231A.6.8.3.3.1 Test purpose and environment
3231A.6.8.3.3.2 Test requirements 3235A.6.8.3.4 UE Rx-Tx time difference
measurements with PRS bandwidth aggregation in FR1 SA 3235A.6.8.3.4.1
Test purpose and environment 3235A.6.8.3.4.2 Test requirements
3238A.6.8.4 PRS-RSRPP measurements 3238A.6.8.4.1 PRS-RSRPP reporting
delay test case for single positioning frequency layer in FR1 in
RRC\_INACTIVE state 3238A.6.8.4.1.1 Test purpose and Environment
3239A.6.8.4.1.2 Test Requirements 3240A.6.8.4.2 PRS-RSRPP reporting
delay test case for single positioning frequency layer in FR1 in
RRC\_INACTIVE state for reduced number of samples 3241A.6.8.4.2.1 Test
purpose and Environment 3241A.6.8.4.2.2 Test Requirements 3243A.6.8.4.3
PRS-RSRPP reporting delay in RRC\_INACTIVE with eDRX 3243A.6.8.4.3.1
Test purpose and Environment 3243A.6.8.4.3.2 Test Requirements
3246A.6.8.5 RSCPD Measurements 3246A.6.8.5.1 DL RSCPD reported with RSTD
measurement reporting delay test case for single positioning frequency
layer in FR1 SA in RRC\_INACTIVE state 3246A.6.8.5.1.1 Test Purpose and
Environment 3246A.6.8.5.1.2 Test Requirements 3246A.6.8.6 RSCP
Measurements 3247A.6.8.6.1 DL RSCP with UE Rx-Tx time difference
measurement for single positioning frequency layer in FR1 SA
3247A.6.8.6.1.1 Test purpose and environment 3247A.6.8.6.1.2 Test
requirements 3251A.6.9 Measurement performance requirements in
RRC\_INACTIVE 3251A.6.9.1 RSTD measurements 3251A.6.9.1.1 RSTD
measurement accuracy test case for single positioning frequency layer in
FR1 in RRC\_INACTIVE state 3251A.6.9.1.1.1 Test purpose and Environment
3251A.6.9.1.1.2 Test Requirements 3253A.6.9.1.2 RSTD measurement
accuracy test case with reduced number of samples for single positioning
frequency layer in FR1 in RRC\_INACTIVE state 3253A.6.9.1.2.1 Test
purpose and Environment 3253A.6.9.1.2.2 Test Requirements 3255A.6.9.1.3
RSTD measurement accuracy for PRS aggregation in FR1 in RRC\_INACTIVE
state 3255A.6.9.1.3.1 Test purpose and Environment 3255A.6.9.1.3.2 Test
Requirements 3258A.6.9.2 PRS-RSRP measurements 3258A.6.9.2.1 SA:
measurement accuracy with PRS in FR1 in RRC\_INACTIVE 3258A.6.9.2.1.1
Test Purpose and Environment 3258A.6.9.2.1.2 Test parameters
3258A.6.9.2.1.3 Test Requirements 3260A.6.9.2.2 SA: measurement accuracy
with PRS in FR1 with reduced number of samples in RRC\_INACTIVE state
3260A.6.9.2.2.1 Test Purpose and Environment 3260A.6.9.2.2.2 Test
parameters 3260A.6.9.2.2.3 Test Requirements 3262A.6.9.3 UE Rx-Tx time
difference measurements 3262A.6.9.3.1.1 UE Rx-Tx time difference
measurement accuracy in FR1 SA 3262A.6.9.3.1.1.1 Test purpose and
environment 3262A.6.9.3.1.1.2 Test parameters 3263A.6.9.3.1.1.3 Test
requirements 3264A.6.9.3.2 UE Rx-Tx time difference measurement accuracy
with reduced number of samples 3264A.6.9.3.2.1 Test purpose and
environment 3264A.6.9.3.2.2 Test parameters 3264A.6.9.3.2.3 Test
requirements 3266A.6.9.3.3 UE Rx-Tx time difference measurement accuracy
with PRS bandwidth aggregation in FR1 SA 3266A.6.9.3.3.1 Test purpose
and environment 3266A.6.9.3.3.2 Test requirements 3269A.6.9.4 PRS-RSRPP
measurements 3269A.6.9.4.1 SA: PRS-RSRPP measurement accuracy in FR1 in
RRC INACTIVE 3269A.6.9.4.1.1 Test Purpose and Environment
3269A.6.9.4.1.2 Test parameters 3269A.6.9.4.1.3 Test Requirements
3271A.6.9.4.2 SA: measurement accuracy with reduced PRS samples in FR1
in RRC INACTIVE 3271A.6.9.4.2.1 Test Purpose and Environment
3271A.6.9.4.2.2 Test parameters 3272A.6.9.4.2.3 Test Requirements
3273A.6.9.5 RSCPD Measurements 3274A.6.9.5.1 RSCPD with RSTD measurement
accuracy in FR1 SA in RRC\_INACTIVE 3274A.6.9.5.1.1 Test purpose and
environment 3274A.6.9.5.1.2 Test parameters 3274A.6.9.5.1.3 Test
requirements 3277A.6.9.6 RSCP Measurements 3277A.6.9.6.1 RSCP with UE
Rx-Tx time difference measurement accuracy in FR1 SA 3277A.6.9.6.1.1
Test purpose and environment 3277A.6.9.6.1.2 Test parameters
3278A.6.9.6.1.3 Test requirements 3281A.6.10 Measurement Procedure in
RRC\_IDLE 3281A.6.10.1 RSTD Measurements 3281A.6.10.1.1 NR RSTD
measurement reporting delay test case for single positioning frequency
layer in FR1 SA in RRC\_IDLE state for non-RedCap UE 3281A.6.10.1.1.1
Test purpose and environment 3281A.6.10.1.1.2 Test requirements
3284A.6.10.1.2 NR RSTD measurement reporting delay test case for single
positioning frequency layer in FR1 SA in RRC\_IDLE state with eDRX cycle
\> 10.24s for non-RedCap UE 3285A.6.10.1.2.1 Test Purpose and
Environment 3285A.6.10.1.2.2 Test Requirements 3288A.6.10.1.3 NR RSTD
measurement reporting delay test case for PRS aggregation in FR1 SA in
RRC\_IDLE state 3288A.6.10.1.3.1 Test purpose and environment
3288A.6.10.1.3.2 Test requirements 3288A.6.10.2 PRS-RSRP Measurements
3289A.6.10.2.1 PRS-RSRP reporting delay test case for single positioning
frequency layer in RRC\_IDLE state for non-RedCap UE in FR1
3289A.6.10.2.1.1 Test purpose and Environment 3289A.6.10.2.1.2 Test
Requirements 3291A.6.10.2.2 PRS-RSRP reporting delay test case in
RRC\_IDLE state in FR1 when eDRX cycle \> 10.24s 3292A.6.10.2.2.1 Test
purpose and Environment 3292A.6.10.2.2.2 Test Requirements 3292A.6.10.3
RSCPD Measurements 3292A.6.10.3.1 DL RSCPD reported with RSTD
measurement reporting delay test case for single positioning frequency
layer in FR1 SA in RRC\_IDLE state 3292A.6.10.3.1.1 Test Purpose and
Environment 3292A.6.10.3.1.2 Test Requirements 3293A.6.11 Measurement
Performance Requirements in RRC\_IDLE 3293A.6.11.1 RSTD Measurements
3293A.6.11.1.1 NR RSTD measurement accuracy test case for single
positioning frequency layer in FR1 SA in RRC\_IDLE state for non-RedCap
UE 3293A.6.11.1.1.1 Test purpose and environment 3293A.6.11.1.1.2 Test
requirements 3295A.6.11.1.2 RSTD measurement accuracy test case for
single positioning frequency layer in FR1 in RRC\_IDLE state with
eDRX\>10.24s for non-RedCap UE 3295A.6.11.1.2.1 Test purpose and
Environment 3295A.6.11.1.2.2 Test Requirements 3297A.6.11.1.3 NR RSTD
measurement accuracy test case for PRS aggregation in FR1 SA in
RRC\_IDLE state 3297A.6.11.1.3.1 Test purpose and environment
3297A.6.11.1.3.2 Test requirements 3297A.6.11.2 PRS-RSRP measurements
3297A.6.11.2.1 PRS-RSRP measurement accuracy test case for non-RedCap UE
in FR1 in RRC\_IDLE state 3297A.6.11.2.1.1 Test Purpose and Environment
3297A.6.11.2.1.2 Test parameters 3298A.6.11.2.1.3 Test Requirements
3300A.6.11.2.2 PRS-RSRP measurement accuracy test case in RRC\_IDLE
state in FR1 when eDRX cycle \> 10.24s 3300A.6.11.2.2.1 Test purpose and
Environment 3300A.6.11.2.2.2 Test parameters 3300A.6.11.2.2.3 Test
Requirements 3301A.6.11.3 RSCPD Measurements 3301A.6.11.3.1 RSCPD with
RSTD measurement accuracy in FR1 SA in RRC\_IDLE 3301A.6.11.3.1.1 Test
purpose and environment 3301A.6.11.3.1.2 Test parameters 3301A.6.
11.3.1.3 Test requirements 3304A.7 NR standalone tests with one or more
NR cells in FR2 3307A.7.1 SA: RRC\_IDLE state mobility 3307A.7.1.1 Cell
re-selection to NR 3307A.7.1.1.1 Cell reselection to FR2 intra-frequency
NR case 3307A.7.1.1.1.1 Test Purpose and Environment 3307A.7.1.1.1.2
Test Parameters 3307A.7.1.1.1.3 Test Requirements 3309A.7.1.1.2 Cell
reselection to FR2 inter-frequency NR case 3309A.7.1.1.2.1 Test Purpose
and Environment 3310A.7.1.1.2.2 Test Parameters 3310A.7.1.1.2.3 Test
Requirements 3311A.7.1.1.3 Cell reselection to FR2 intra-frequency NR
case for UE fulfilling low mobility relaxed measurement criterion
3312A.7.1.1.3.1 Test Purpose and Environment 3312A.7.1.1.3.2 Test
Parameters 3312A.7.1.1.3.3 Test Requirements 3314A.7.1.1.4 Cell
reselection to FR2 intra-frequency NR case for UE fulfilling not-at-cell
edge relaxed measurement criterion 3314A.7.1.1.4.1 Test Purpose and
Environment 3314A.7.1.1.4.2 Test Parameters 3315A.7.1.1.4.3 Test
Requirements 3316A.7.1.1.5 Cell reselection to FR2 inter-frequency NR
case for UE fulfilling low mobility relaxed measurement criterion
3317A.7.1.1.5.1 Test Purpose and Environment 3317A.7.1.1.5.2 Test
Parameters 3317A.7.1.1.5.3 Test Requirements 3319A.7.1.1.6 Cell
reselection to FR2 inter-frequency NR case for UE fulfilling not-at-cell
edge relaxed measurement criterion 3319A.7.1.1.6.1 Test Purpose and
Environment 3319A.7.1.1.6.2 Test Parameters 3320A.7.1.1.6.3 Test
Requirements 3321A.7.1.1.7 Cell reselection to FR2 intra-frequency NR
case for FR2 power class 6 UE configured with *highSpeedMeasFlagFR2-r17*
3322A.7.1.1.7.1 Test Purpose and Environment 3322A.7.1.1.7.2 Test
Parameters 3322A.7.1.1.7.3 Test Requirements 3324A.7.1.1.8 Cell
reselection to FR2 inter-frequency NR case for UE configured with
*highSpeedMeasFlagFR2-r17* 3325A.7.1.1.8.1 Test Purpose and Environment
3325A.7.1.1.8.2 Test Parameters 3325A.7.1.1.8.3 Test Requirements
3327A.7.2 SA: RRC\_INACTIVE state mobility 3327A.7.2.1 Small Data
Transmission 3327A.7.2.1.1 TA validation for CG-SDT in FR2
3327A.7.2.1.1.1 Test Purpose and Environment 3327A.7.2.1.1.2 Test
Requirements 3330A.7.2.2 Cell reselection for positioning 3331A.7.2.2.1
Cell reselection to FR2 intra-frequency NR case with RRC\_ INACTIVE eDRX
and positioning SRS 3331A.7.2.2.1.1 Test Purpose and Environment
3331A.7.2.2.1.2 Test Parameters 3331A.7.2.2.1.3 Test Requirements
3333A.7.3 RRC\_CONNECTED state mobility 3333A.7.3.1 Handover
3333A.7.3.1.1 Inter-frequency handover from FR1 to FR2; unknown target
cell 3333A.7.3.1.1.1 Test Purpose and Environment 3333A.7.3.1.1.2 Test
Parameters 3333A.7.3.1.1.3 Test Requirements 3335A.7.3.1.2
Intra-frequency handover from FR2 to FR2; unknown target cell
3336A.7.3.1.2.1 Test Purpose and Environment 3336A.7.3.1.2.2 Test
Parameters 3336A.7.3.1.2.3 Test Requirements 3337A.7.3.1.3
Inter-frequency handover from FR2 to FR2; unknown target cell
3337A.7.3.1.3.1 Test Purpose and Environment 3337A.7.3.1.3.2 Test
Parameters 3337A.7.3.1.3.3 Test Requirements 3339A.7.3.1.4 Inter-band
inter-frequency synchronous DAPS handover from FR1 to FR2
3339A.7.3.1.4.1 Test Purpose and Environment 3339A.7.3.1.4.2 Test
Parameters 3339A.7.3.1.4.3 Test Requirements 3342A.7.3.1.5 Inter-band
inter-frequency asynchronous DAPS handover from FR1 to FR2
3343A.7.3.1.5.1 Test Purpose and Environment 3343A.7.3.1.5.2 Test
Parameters 3343A.7.3.1.5.3 Test Requirements 3346A.7.3.1.6 Handover with
PSCell from SA to EN-DC with unknown FR2 target PScell 3347A.7.3.1.6.1
Test Purpose and Environment 3347A.7.3.1.6.2 Test Parameters
3347A.7.3.1.6.3 Test Requirements 3352A.7.3.1.7 HO with PSCell from FR1
NR-SA to EN-DC with known E-UTRA PCell and known FR2 PSCell
3352A.7.3.1.7.1 Test purpose and environment 3352A.7.3.1.7.2 Test
Requirements 3356A.7.3.1.8 NR PSCell change delay in HO with PSCell from
NR-DC to NR-DC 3357A.7.3.1.8.1 Test Purpose and Environment
3357A.7.3.1.8.2 Test Requirements 3360A.7.3.1.9 Intra-frequency handover
from FR2-2 to FR2-2; unknown target cell 3360A.7.3.1.9.1 Test Purpose
and Environment 3360A.7.3.1.9.2 Test Parameters 3360A.7.3.1.9.3 Test
Requirements 3362A.7.3.1.10 Inter-frequency handover from FR2-2 to
FR2-2; unknown target cell 3363A.7.3.1.10.1 Test Purpose and Environment
3363A.7.3.1.10.2 Test Parameters 3363A.7.3.1.10.3 Test Requirements
3365A.7.3.1.11 Inter-frequency handover from FR1 to FR2-2; unknown
target cell 3365A.7.3.1.11.1 Test Purpose and Environment
3365A.7.3.1.11.2 Test Parameters 3365A.7.3.1.11.3 Test Requirements
3367A.7.3.1.12 Intra-frequency handover from FR2 to FR2; known target
cell configured with NCD-SSB 3368A.7.3.1.12.1 Test Purpose and
Environment 3368A.7.3.1.12.2 Test Parameters 3368A.7.3.1.12.3 Test
Requirements 3369A.7.3.1.13 Inter-frequency handover from FR2 to FR2;
known target cell configured with NCD-SSB 3370A.7.3.1.13.1 Test Purpose
and Environment 3370A.7.3.1.13.2 Test Parameters 3370A.7.3.1.13.3 Test
Requirements 3372A.7.3.1.14 Handover with PSCell from FR1-FR2 NR-DC to
FR1-FR1 NR-DC with target PSCell in FR1 3372A.7.3.1.14.1 Test Purpose
and Environment 3372A.7.3.1.14.2 Test Requirements 3376A.7.3.1.15 HO
with PSCell from FR1-FR1 NR-DC to FR1-FR2 NR-DC 3376A.7.3.1.15.1 Test
Purpose and Environment 3376A.7.3.1.15.2 Test Requirements 3381A.7.3.2
RRC Connection Mobility Control 3381A.7.3.2.1 SA: RRC Re-establishment
3381A.7.3.2.1.1 Intra-frequency RRC Re-establishment in FR2
3381A.7.3.2.1.2 Inter-frequency RRC Re-establishment in FR2
3383A.7.3.2.1.3 Intra-frequency RRC Re-establishment in FR2 without
serving cell timing 3386A.7.3.2.1.3.1 Test Purpose and Environment
3386A.7.3.2.1.3.2 Test Requirements 3387A.7.3.2.1.4 Intra-frequency RRC
Re-establishment in FR2-2 3388A.7.3.2.1.4.1 Test Purpose and Environment
3388A.7.3.2.1.4.2 Test Requirements 3390A.7.3.2.1.5 Inter-frequency RRC
Re-establishment in FR2-2 3390A.7.3.2.1.5.1 Test Purpose and Environment
3390A.7.3.2.1.5.2 Test Requirements 3392A.7.3.2.1.6 Intra-frequency RRC
Re-establishment in FR2-2 without serving cell timing 3393A.7.3.2.1.6.1
Test Purpose and Environment 3393A.7.3.2.1.6.2 Test Requirements
3394A.7.3.2.2 Random Access 3395A.7.3.2.2.1 4-step RA type c ontention
based random access test in FR2 for NR Standalone 3395A.7.3.2.2.2 4-step
RA type n on-contention based random access test in FR2 for NR
Standalone 3398A.7.3.2.2.3 2-step RA type contention based random access
test in FR2 for NR Standalone 3401A.7.3.2.2.4 2-step RA type n
on-contention based random access test in FR2 for NR Standalone
3404A.7.3.2.3 SA: RRC Connection Release with Redirection
3407A.7.3.2.3.1 Redirection from NR in FR2 to NR in FR2 3407A.7.3.2.4
LTM PDCCH-order Random Access 3409A.7.3.2.4.1 PDCCH-order RACH on
neighbor cell in FR2 when RACH BW is within active BWP 3409A.7.3.2.4.2
PDCCH-order RACH on inter-frequency neighbor cell in FR2 3412A.7.3.3
Conditional Handover 3415A.7.3.3.1 Intra-frequency conditional handover
from FR2 to FR2 3415A.7.3.3.1.1 Test Purpose and Environment
3415A.7.3.3.1.2 Test Parameters 3415A.7.3.3.1.2.3 Test Requirements
3416A.7.3.3.2 Inter-frequency conditional handover from FR2 to FR2;
unknown target cell 3417A.7.3.3.2.1 Test Purpose and Environment
3417A.7.3.3.2.2 Test Parameters 3417A.7.3.3.2.3Test Requirements
3418A.7.3.3.3 NES triggering intra-frequency target CHO delay From FR2
to FR2 3418A.7.3.3.3.1 Test Purpose and Environment 3418A.7.3.3.3.2 Test
Parameters 3419A.7.3.3.3.2.3 Test Requirements 3420A.7.3.3.4 NES
triggering inter-frequency conditional handover from FR2 to FR1
3420A.7.3.3.4.1 Test Purpose and Environment 3420A.7.3.3.4.2 Test
Parameters 3420A.7.3.3.4.3 Test Requirements 3422A.7.3.3.5 NR
conditional handover including target MCG and target SCG from FR1-FR2
NR-DC to FR1-FR2 NR-DC 3423A.7.3.3.5.1 Test Purpose and Environment
3423A.7.3.3.5.2 Test Requirements 3426A.7.3.3.5.2.1 Test Requirements
for NR conditional handover 3426A.7.3.3.5.2.2 Test Requirements for NR
PSCell change 3426A.7.3.3.6 NR conditional Handover including target MCG
and candidate SCG from FR1-FR2 NR-DC to FR1-FR2 NR-DC 3426A.7.3.3.6.1
Test Purpose and Environment 3426A.7.3.3.6.2 Test Parameters
3426A.7.3.3.6.3 Test Requirements 3430A.7.3.4 LTM PCell Switch
3430A.7.3.4.1 RACH based Intra-frequency PCell switch from FR2 to FR2
3430A.7.3.4.1.1 Test Purpose and Environment 3430A.7.3.4.1.2 Test
Parameters 3430A.7.3.4.1.3 Test Requirements 3433A.7.3.4.2 RACH-less
Intra-frequency PCell switch from FR2 to FR2 3434A.7.3.4.2.1 Test
Purpose and Environment 3434A.7.3.4.2.2 Test Parameters 3434A.7.3.4.2.3
Test Requirements 3438A.7.3.4.3 RACH-based Inter-frequency LTM PCell
switch from FR2 to FR2 3438A.7.3.4.3.1 Test Purpose and Environment
3438A.7.3.4.3.2 Test Parameters 3438A.7.3.4.3.3 Test Requirements
3441A.7.3.5 LTM PSCell Switch 3442A.7.3.5.1 RACH-based Intra-frequency
LTM PSCell switch from FR2 to FR2 3442A.7.3.5.1.1 Test Purpose and
Environment 3442A.7.3.5.1.2 Test Parameters 3442A.7.3.5.1.3 Test
Requirements 3446A.7.4 Timing 3447A.7.4.1 UE transmit timing
3447A.7.4.1.1 NR UE Transmit Timing Test for FR2 3447A.7.4.1.1.1 Test
Purpose and environment 3447A.7.4.1.1.2 Test requirements 3449A.7.4.1.2
NR UE Transmit Timing Test for FR2-2 3449A.7.4.1.2.1 Test Purpose and
environment 3450A.7.4.1.2.2 Test requirements 3452A.7.4.1.3 NR UE
Transmit Timing Test with 2-TA for FR2 UE supporting
*multiDCI-IntraCellMultiTRP-TwoTA-r18* 3452A.7.4.1.3.1 Test Purpose and
environment 3452A.7.4.1.3.2 Test requirements 3456A.7.4.2 UE timer
accuracy 3456A.7.4.3 Timing advance 3456A.7.4.3.1 SA FR2 timing advance
adjustment accuracy 3456A.7.4.3.1.1 Test Purpose and Environment
3456A.7.4.3.1.2 Test Parameters 3457A.7.4.3.1.3 Test Requirements
3459A.7.4.3.2 SA FR2-2 timing advance adjustment accuracy
3459A.7.4.3.2.1 Test Purpose and Environment 3459A.7.4.3.2.2 Test
Parameters 3459A.7.4.3.2.3 Test Requirements 3461A.7.5 Signaling
characteristics 3465A.7.5.1 Radio link Monitoring 3465A.7.5.1.1 Radio
Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based
RLM RS in non-DRX mode 3465A.7.5.1.1.1 Test Purpose and Environment
3465A.7.5.1.1.2 Test Requirements 3468A.7.5.1.2 Radio Link Monitoring
In-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX
mode 3468A.7.5.1.2.1 Test Purpose and Environment 3468A.7.5.1.2.2 Test
Requirements 3471A.7.5.1.3 Radio Link Monitoring Out-of-sync Test for
FR2 PCell configured with SSB-based RLM RS in DRX mode 3471A.7.5.1.3.1
Test Purpose and Environment 3471A.7.5.1.3.2 Test Requirements
3473A.7.5.1.4 Radio Link Monitoring In-sync Test for FR2 PCell
configured with SSB-based RLM RS in DRX mode 3474A.7.5.1.4.1 Test
Purpose and Environment 3474A.7.5.1.4.2 Test Requirements 3476A.7.5.1.5
Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with
CSI-RS-based RLM in non-DRX mode 3476A.7.5.1.5.1 Test Purpose and
Environment 3476A.7.5.1.5.2 Test Requirements 3479A.7.5.1.6 Radio Link
Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM
in non-DRX mode 3479A.7.5.1.6.1 Test Purpose and Environment
3479A.7.5.1.6.2 Test Requirements 3481A.7.5.1.7 Radio Link Monitoring
Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX
mode 3482A.7.5.1.7.1 Test Purpose and Environment 3482A.7.5.1.7.2 Test
Requirements 3484A.7.5.1.8 Radio Link Monitoring In-sync Test for FR2
PCell configured with CSI-RS-based RLM in DRX mode 3484A.7.5.1.8.1 Test
Purpose and Environment 3484A.7.5.1.8.2 Test Requirements 3487A.7.5.1.9
UE Radio Link Monitoring Scheduling Restrictions on FR2 3488A.7.5.1.9.1
Test Purpose and Environment 3488A.7.5.1.9.2 Test Requirements
3489A.7.5.1.10 Radio Link Monitoring Out-of-sync Test for FR2 PCell
configured with SSB-based RLM RS in non-DRX mode for UE supporting fast
beam sweeping in multi-Rx 3489A.7.5.1.10.1 Test Purpose and Environment
3489A.7.5.1.10.2 Test Requirements 3492A.7.5.1.11 Radio Link Monitoring
Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in
non-DRX mode when CD-SSB is outside active BWP 3493A.7.5.1.11.1 Test
Purpose and Environment 3493A.7.5.1.12 Radio Link Monitoring Out-of-sync
Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode when
CD-SSB is outside active BWP 3493A.7.5.1.12.1 Test Purpose and
Environment 3493A.7.5.1.12.2 Test Requirements 3493A.7.5.1.13 Radio Link
Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM
RS in non-DRX mode for UE supporting NCD-SSB based measurement outside
active BWP 3493A.7.5.1.13.1 Test Purpose and Environment
3493A.7.5.1.13.2 Test Requirements 3496A.7.5.2 Interruption
3496**A.7.5.2.1** Interruptions during measurements on deactivated NR
SCC in FR2 3496A.7.5.2.1.1 Test Purpose and Environment
3496**A.7.5.2.1**.2 Test Requirements 3499A.7.5.2.2 SA interruptions at
NR SRS carrier-based switching 3499A.7.5.2.2.1 Test Purpose and
Environment 3499A.7.5.2.2.2 Test Parameters 3499A.7.5.2.2.3 Test
Requirements 3501A.7.5.3 SCell Activation and Deactivation Delay
3501A.7.5.3.1 SCell Activation and deactivation for SCell in FR2
intra-band in non-DRX 3501A.7.5.3.1.1 Test Purpose and Environment
3501A.7.5.3.1.2 Test Requirements 3503A.7.5.3.2 SCell Activation and
deactivation for FR1+FR2 inter-band with target SCell in FR2
3503A.7.5.3.2.1 Test Purpose and Environment 3503A.7.5.3.2.2 Test
Requirements 3505A.7.5.3.3 SCell Activation and deactivation for SCell
in FR2 inter-band in non-DRX 3506A.7.5.3.3.1 Test Purpose and
Environment 3506A.7.5.3.3.2 Test Requirements 3508A.7.5.3.4 Direct SCell
activation at SCell addition of known SCell in FR2 3509A.7.5.3.4.1 Test
Purpose and Environment 3509A.7.5.3.4.2 Test Requirements 3511A.7.5.3.5
Direct SCell activation at handover with known SCell in FR2
3512A.7.5.3.5.1 Test Purpose and Environment 3512A.7.5.3.5.2 Test
Requirements 3514A.7.5.3.6 PUCCH SCell activation and deactivation for
FR1+FR2 inter-band with target SCell in FR2 and known 3515A.7.5.3.6.1
Test Purpose and Environment 3515A.7.5.3.6.2 Test Requirements
3517A.7.5.3.7 PUCCH SCell activation and deactivation delay requirements
of FR2 unknown cell with FR1 PCell 3518A.7.5.3.7.1 Test Purpose and
Environment 3518A.7.5.3.7.2 Test Requirements 3521A.7.5.3.8 SCell
Activation and deactivation for known PUCCH SCell in FR2 inter-band in
non-DRX 3522A.7.5.3.8.1 Test Purpose and Environment 3522A.7.5.3.8.2
Test Requirements 3525A.7.5.3.9 PUCCH SCell Activation and deactivation
of unknown SCell in FR2 3526A.7.5.3.9.1 Test Purpose and Environment
3526A.7.5.3.9.2 Test Requirements 3528A.7.5.3.10 SCell Activation and
deactivation of FR2 known PUCCH SCell and one FR2 unknown SCell with FR2
PCell 3529A.7.5.3.10.1 Test Purpose and Environment 3529A.7.5.3.10.2
Test Requirements 3532A.7.5.3.11 PUCCH SCell activation and deactivation
delay requirements of FR2 unknown cell with FR2 PCell 3533A.7.5.3.11.1
PUCCH SCell activation with non-PUCCH SCell in a secondary PUCCH Group
3533A.7.5.3.11.1.1 Test Purpose and Environment 3533A.7.5.3.11.1.2 Test
Requirements 3536A.7.5.3.11.2 PUCCH SCell activation with non-PUCCH
SCell in a primary PUCCH Group 3537A.7.5.3.11.2.1 Test Purpose and
Environment 3537A.7.5.3.11.2.2 Test Requirements 3540A.7.5.3.12 Void
3541A.7.5.3.13 SCell Activation for SCell in FR2 intra-band in non-DRX
3541A.7.5.3.13.1 Test Purpose and Environment 3541A.7.5.3.13.2 Test
Requirements 3543A.7.5.3.14 SCell Activation for known SCell in FR2
inter-band 3543A.7.5.3.14.1 Test Purpose and Environment
3543A.7.5.3.14.2 Test Requirements 3545A.7.5.3.15 PUCCH SCell activation
and deactivation with FR1 PCell based on L3 reporting after SCell
activation command 3546A.7.5.3.15.1 Test Purpose and Environment
3546A.7.5.3.15.2 Test Requirements 3550A.7.5.3.16 PUCCH SCell activation
and deactivation with FR2 PCell based on L3 reporting after SCell
activation command 3550A.7.5.3.16.1 Test Purpose and Environment
3550A.7.5.3.16.2 Test Requirements 3553A.7.5.3.17 SCell Activation and
deactivation for SCell in FR2 inter-band in DRX for UE capable of small
beam sweeping factors and/or short measurement interval 3554A.7.5.3.17.1
Test Purpose and Environment 3554A.7.5.3.17.2 Test Requirements
3556A.7.5.3.18 SCell Activation and deactivation for FR1+FR2 inter-band
with target SCell in FR2, in DRX, for UE capable of small beam sweeping
factors and/or short measurement interval 3558A.7.5.3.18.1 Test Purpose
and Environment 3558A.7.5.3.18.2 Test Requirements 3561A.7.5.3.19 SCell
Activation and deactivation of FR2 unknown SCell with FR1 PCell in
non-DRX with L3 reporting during activation 3563A.7.5.3.19.1 Test
Purpose and Environment 3563A.7.5.3.19.2 Test Requirements
3566A.7.5.3.20 SCell Activation and Deactivation of FR2 unkown SCell
with FR2 PCell in non-DRX with L3 reporting during activation
3566A.7.5.3.20.1 Test Purpose and Environment 3567A.7.5.3.20.2 Test
Requirements 3569A.7.5.4 Void 3570A.7.5.5 Beam Failure Detection and
Link recovery procedures 3570A.7.5.5.1 Beam Failure Detection and Link
Recovery Test for FR2 PCell configured with SSB-based BFD and LR in
non-DRX mode 3570A.7.5.5.1.1 Test Purpose and Environment
3570A.7.5.5.1.2 Test Requirements 3573A.7.5.5.2 Beam Failure Detection
and Link Recovery Test for FR2 PCell configured with SSB-based BFD and
LR in DRX mode 3574A.7.5.5.2.1 Test Purpose and Environment
3574A.7.5.5.2.2 Test Requirements 3577A.7.5.5.3 Beam Failure Detection
and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD
and LR in non-DRX mode 3577A.7.5.5.3.1 Test Purpose and Environment
3577A.7.5.5.3.2 Test Requirements 3580A.7.5.5.4 Beam Failure Detection
and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD
and LR in DRX mode 3580A.7.5.5.4.1 Test Purpose and Environment
3580A.7.5.5.4.2 Test Requirements 3583A.7.5.5.5 Scheduling availability
restriction during Beam Failure Detection and Link Recovery for FR2
PCell configured with SSB-based BFD and LR in non-DRX mode
3584A.7.5.5.5.1 Test Purpose and Environment 3584A.7.5.5.5.2 Test
Requirements 3587A.7.5.5.6 Beam Failure Detection and Link Recovery Test
for FR2 SCell configured with CSI-RS-based BFD and LR in non-DRX mode
3587A.7.5.5.6.1 Test Purpose and Environment 3587A.7.5.5.6.2 Test
Requirements 3590A.7.5.5.7 Beam Failure Detection and Link Recovery Test
for FR2 SCell configured with CSI-RS-based BFD and LR in DRX mode
3590A.7.5.5.7.1 Test Purpose and Environment 3590A.7.5.5.7.2 Test
Requirements 3593A.7.5.5.8 Beam Failure Detection and Link Recovery Test
for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode for UE
fulfilling relaxed measurement criterion 3594A.7.5.5.8.1 Test Purpose
and Environment 3594A.7.5.5.8.2 Test Requirements 3597A.7.5.5.9 TRP
specific Beam Failure Detection and Link Recovery Test for FR2 SCell
configured with CSI-RS-based BFD and LR in DRX mode 3597A.7.5.5.9.1 Test
Purpose and Environment 3597A.7.5.5.9.2 Test Requirements 3600A.7.5.5.10
TRP specific Beam Failure Detection and Link Recovery Test for FR2 PCell
configured with SSB-based BFD and LR in non-DRX mode 3601A.7.5.5.10.1
Test Purpose and Environment 3601A.7.5.5.10.2 Test Requirements
3604A.7.5.5.11 Beam Failure Detection and Link Recovery Test for FR2-2
PCell configured with CSI-RS-based BFD and LR in non-DRX mode
3604A.7.5.5.11.1 Test Purpose and Environment 3604A.7.5.5.11.2 Test
Requirements 3607A.7.5.5.12 Beam Failure Detection and Link Recovery
Test for FR2-2 PCell configured with CSI-RS-based BFD and LR in DRX mode
3607A.7.5.5.12.1 Test Purpose and Environment 3607A.7.5.5.12.2 Test
Requirements 3610A.7.5.5.13 Scheduling availability restriction during
Beam Failure Detection and Link Recovery for FR2-2 PCell configured with
SSB-based BFD and LR in non-DRX mode 3611A.7.5.5.13.1 Test Purpose and
Environment 3611A.7.5.5.13.2 Test Requirements 3613A.7.5.5.14 TRP
specific Beam Failure Detection and Link Recovery for FR2 PCell
configured with CSI-RS-based BFD and LR and multi-Rx operation in DRX
mode 3613A.7.5.5.14.1 Test Purpose and Environment 3613A.7.5.5.14.2 Test
Requirements 3617A.7.5.6 Active BWP switch 3617A.7.5.6.1 DCI-based and
Timer-based Active BWP Switch 3617A.7.5.6.1.1 NR FR2- NR FR2 DL active
BWP switch of SCell with non-DRX in SA 3617A.7.5.6.1.2 NR FR1- NR FR2 DL
active BWP switch of SCell with non-DRX in SA 3621A.7.5.6.1.3 NR FR2 DL
active BWP switch with non-DRX in SA 3625A.7.5.6.1.3.1 Test Purpose and
Environment 3625A.7.5.6.1.3.2 Test Requirements 3627A.7.5.6.1.4 NR
FR2-2- NR FR2-2 DL active BWP switch of SCell with non-DRX in SA
3627A.7.5.6.1.4.1 Test Purpose and Environment 3627A.7.5.6.1.4.2 Test
Requirements 3630A.7.5.6.2 RRC-based Active BWP Switch 3631A.7.5.6.2.1.1
Test Purpose and Environment 3631A.7.5.6.2.1.2 Test Requirements
3634A.7.5.6.2.2 NR FR2-2 DL active BWP switch of PCell with non-DRX in
SA 3634A.7.5.6.2.2.1 Test Purpose and Environment 3634A.7.5.6.2.2.2 Test
Requirements 3636A.7.5.6.3 Simultaneous DCI-based and Timer-based Active
BWP Switch on multiple CCs 3637A.7.5.6.3.1.1 Test Purpose and
Environment 3637A.7.5.6.3.1.2 Test Requirements 3639A.7.5.6.4 SCell
dormancy switch 3640A.7.5.6.4.1 NR FR2 PCell SCell dormancy switch of
single FR2 SCell inside active time 3640A.7.5.6.4.1.1 Test Purpose and
Environment 3640A.7.5.6.4.1.2 Test Requirements 3642A.7.5.6.4.2 NR FR1
PCell SCell dormancy switch of two FR2 SCells outside active time
3643A.7.5.6.4.2.1 Test Purpose and Environment 3643A.7.5.6.4.2.2 Test
Requirements 3646A.7.5.6.5 Simultaneous RRC-based Active BWP Switch on
multiple CCs 3646A.7.5.6.5.1 Active BWP switch on multiple SCells with
non-DRX in SA 3646A.7.5.6.5.2 NR FR2-2 Active BWP switch on multiple
SCells with non-DRX in SA 3648A.7.5.6.5.2.1 Test Purpose and Environment
3648A.7.5.6.5.2**.**2 Test Requirements 3651A.7.5.7 PSCell addition and
release delay 3651A.7.5.7.1 Addition and Release Delay of known NR
PSCell 3651A.7.5.7.1.1 Test Purpose and Environment 3651A.7.5.7.1.2 Test
Requirements 3654A.7.5.7.2 Addition and Release Delay of unknown NR
PSCell in 3654A.7.5.7.2.1 Test Purpose and Environment 3654A.7.5.7.2.2
Test Requirements 3656A.7.5.7.3 Addition and Release Delay of known NR
PSCell in FR2-2 3656A.7.5.7.3.1 Test Purpose and Environment
3656A.7.5.7.3.2 Test Requirements 3659A.7.5.7.4 Addition and Release
Delay of unknown NR PSCell in FR2-2 3659A.7.5.7.4.1 Test Purpose and
Environment 3659A.7.5.7.4.2 Test Requirements 3661A.7.5.8 Active TCI
state switch delay 3662A.7.5.8.1 MAC-CE based active TCI state switch
3662A.7.5.8.2 RRC based active TCI state switch 3665A.7.5.8.3 *MAC-CE
based active TCI state switch for HST FR2 scenario* 3668A.7.5.8.3.1 NR
PCell FR2 HST active TCI state switch for a known TCI state
3668A.7.5.8.3.1.1 Test Purpose and Environment 3668A.7.5.8**.3.1**.2
Test Requirements 3671A.7.5.8.3.2 NR PCell FR2 HST active TCI state
switch for PC6 UE supporting *tci‑StateSwitchInd‑r18* for a known TCI
state 3672A.7.5.8.3.2.1 Test Purpose and Environment 3672A.7.5.8.3.2.2
Test Requirements 3675A.7.5.8.4 DCI based active TCI state switch with
m-DCI for simultaneous reception 3675A.7.5.8.4.1 Test Purpose and
Environment 3675A.7.5.8.4.2 Test Requirements 3678A.7.5.8.5 Single-DCI
FR2 DCI based active TCI state switch with known target TCI states for
simultaneous reception 3678A.7.5.8.5.1 Test Purpose and Environment
3678A.7.5.8.5**.1**.2 Test Requirements 3680A.7.5.9 Uplink spatial
relation switch delay 3681A.7.5.9.1.1.1 Test Purpose and Environment
3681A.7.5.9.1.1.2 Test Requirements 3683A.7.5.9.2 RRC based spatial
relation switch 3683A.7.5.9.2.1 NR PCell FR2 spatial relation switch
associated with a known DL-RS 3683A.7.5.9.2.1.1 Test Purpose and
Environment 3683A.7.5.9.2**.1**.2 Test Requirements 3685A.7.5.10 UE
specific CBW change 3685A.7.5.10.1 NR FR2 UE specific CBW change of
PCell with non-DRX in SA 3685A.7.5.10.1.1 Test Purpose and Environment
3685A.7.5.10.1.2 Test Requirements 3687A.7.5.11 UE UL carrier RRC
reconfiguration Delay 3688A.7.5.11.1 UE UL carrier RRC reconfiguration
Delay 3688A.7.5.11.1.1 Test Purpose and Environment 3688A.7.5.11.1.2
Test Requirements 3690A.7.5.12 Conditional PSCell addition and release
delay (FR2 SA) 3690A.7.5.12.1 Addition and Release Delay of PSCell
3690A.7.5.12.1.1 Test purpose and environment 3690A.7.5.12.1.2 Test
Parameters 3690A.7.5.12.1.3 Test Requirements 3692A.7.5.13 Unified TCI
state switching delay 3692A.7.5.13.1 MAC-CE based active joint TCI state
switching 3692A.7.5.13.1.1 NR PCell FR2 active joint TCI state switch
for a known TCI state 3692A.7.5.13.1.1.1 Test Purpose and Environment
3692A.7.5.13.1.1.2 Test parameters 3693A.7.5.13**.1.1**.3 Test
Requirements 3694A.7.5.13.2 MAC-CE based active uplink TCI state switch
3695A.7.5.13.2.1 NR FR2 PCell uplink TCI state switch for a known TCI
state 3695A.7.5.13.2.1.1 Test Purpose and Environment 3695A.7.5.13.2.1.2
Test parameters 3695A.7.5.13.2.1.3 Test Requirements 3697A.7.5.13.3
MAC-CE based active downlink TCI state switch 3697A.7.5.13.3.1 NR PCell
FR2 active downlink TCI state switch to cell with additional PCI for a
known TCI state 3697A.7.5.13.3.1.1 Test Purpose and Environment
3697A.7.5.13.3.1.2 Test Parameters 3697A.7.5.13.3.1.3 Test Requirements
3700A.7.5.13.4 sDCI MAC-CE based joint TCI state switching
3701A.7.5.13.4.1 NR PCell FR2 dual downlink and uplink TCI state switch
in sDCI for known case 3701A.7.5.13.4.1.1 Test Purpose and Environment
3701A.7.5.13.4.1.2 Test parameters 3701A.7.5.13.4.1.3 Test Requirements
3703A.7.5.13.5 MAC-CE based dual downlink TCI state switching delay for
unified TCI for single-DCI mTRP 3703A.7.5.13.5.1 NR PCell FR2 dual
downlink TCI state switch in sDCI for known case 3703A.7.5.13.5.1.1 Test
Purpose and Environment 3703A.7.5.13.5.1.2 Test Parameters
3704A.7.5.13.5.1.3 Test Requirements 3706A.7.5.13.6 MAC-CE based active
uplink TCI state switch for single-DCI mTRP 3706A.7.5.13.6.1 NR FR2
PCell uplink TCI state switch for two known TCI states
3706A.7.5.13.6.1.1 Test Purpose and Environment 3706A.7.5.13.6.1.2 Test
parameters 3707A.7.5.13.6.1.3 Test Requirements 3708A.7.5.14 PSCell
RACH-less based Activation and deactivation for FR1+FR2 inter-band with
target PSCell in FR2 3709A.7.5.14.1 Test Purpose and Environment
3709A.7.5.14.2 Test Requirements 3711A.7.5.15 Void 3712A.7.5.16 UE
L1-RSRP Scheduling and Measurement Restrictions on FR2-1 3712A.7.5.16.1
Test Purpose and Environment 3712A.7.5.16.2 Test Requirements
3714A.7.5.17 SCG Activation and deactivation for FR1+FR1 inter-band with
target PSCell in FR1 3715A.7.5.17.1 Test Purpose and Environment
3715A.7.5.17.2 Test Requirements 3717A.7.5.18 Subsequent conditional
PSCell addition/change 3718A.7.5.18.1 Intra-frequency subsequent CPC
from FR1-FR2 NR-DC to FR1-FR2 NR-DC 3718A.7.5.18.1.1 Test purpose and
environment 3718A.7.5.18.1.2 Test Requirements 3721A.7.5.18.2
Inter-frequency subsequent CPA from FR1-FR2 NR-DC to FR1-FR2 NR-DC
3721A.7.5.18.2.1 Test Purpose and Environment 3721A.7.5.18.2.2 Test
Requirements 3724A.7.6 Measurement procedure 3727A.7.6.1 Intra-frequency
Measurements 3727A.7.6.1.1 SA event triggered reporting test without gap
under non-DRX 3727A.7.6.1.1.1 Test purpose and Environment
3727A.7.6.1.1.2 Test Requirements 3729A.7.6.1.2 SA event triggered
reporting test without gap under DRX 3729A.7.6.1.2.1 Test purpose and
Environment 3729A.7.6.1.2.2 Test Requirements 3731A.7.6.1.3 SA event
triggered reporting test with per-UE gaps under non-DRX 3731A.7.6.1.3.1
Test purpose and Environment 3731A.7.6.1.3.2 Test Requirements
3734A.7.6.1.4 SA event triggered reporting test with per-UE gaps under
DRX 3734A.7.6.1.4.1 Test purpose and Environment 3734A.7.6.1.4.2 Test
Requirements 3736A.7.6.1.5 SA event triggered reporting test without gap
under non-DRX for UE configured with *highSpeedMeasFlagFR2-r17*
3737A.7.6.1.5.1 Test purpose and Environment 3737A.7.6.1.5.2 Test
Requirements 3739A.7.6.1.6 SA event triggered reporting test without gap
under non-DRX for FR2-2 3739A.7.6.1.6.1 Test purpose and Environment
3739A.7.6.1.6.2 Test Requirements 3741A.7.6.1.7 SA event triggered
reporting test without gap under DRX for FR2-2 3742A.7.6.1.7.1 Test
purpose and Environment 3742A.7.6.1.7.2 Test Requirements 3744A.7.6.1.8
SA event triggered reporting test with per-UE gaps under non-DRX for
FR2-2 3745A.7.6.1.8.1 Test purpose and Environment 3745A.7.6.1.8.2 Test
Requirements 3747A.7.6.1.9 SA event triggered reporting test with per-UE
gaps under DRX for FR2-2 3748A.7.6.1.9.1 Test purpose and Environment
3748A.7.6.1.9.2 Test Requirements 3750A.7.6.1.10 SA event triggered
reporting test with SSB time index detection without gap under non-DRX
for FR2-2 3751A.7.6.1.10.1 Test purpose and Environment 3751A.7.6.1.10.2
Test Requirements 3753A.7.6.1.11 SA event triggered reporting test with
SSB time index detection with per-UE gaps under non-DRX for FR2-2
3753A.7.6.1.11.1 Test purpose and Environment 3753A.7.6.1.11.2 Test
Requirements 3755A.7.6.1.12 SA event triggered reporting test without
gap under non-DRX when CD-SSB is outside active BWP 3756A.7.6.1.12.1
Test purpose and Environment 3756A.7.6.1.12.2 Test Requirements
3756A.7.6.1.13 SA event triggered reporting test without gap under
non-DRX with NCD-SSB 3756A.7.6.1.13.1 Test purpose and Environment
3756A.7.6.1.13.2 Test Requirements 3758A.7.6.1.14 SA event triggered
reporting test without gap under non-DRX for power class 6 UE supporting
measEnhCAInterFreqFR2-r18 3759A.7.6.1.14.1 Test Purpose and Environment
3759A.7.6.1.14.2 Test Requirements 3760A.7.6.2 Inter-frequency
Measurements 3760A.7.6.2.1 SA event triggered reporting tests for FR2
without SSB time index detection when DRX is not used (PCell in FR2)
3760A.7.6.2.1.1 Test Purpose and Environment 3760A.7.6.2.1.2 Test
Requirements 3762A.7.6.2.2 SA event triggered reporting tests for FR2
without SSB time index detection when DRX is used (PCell in FR2)
3763A.7.6.2.2.1 Test Purpose and Environment 3763A.7.6.2.2.2 Test
Requirements 3765A.7.6.2.3 SA event triggered reporting tests for FR2
with SSB time index detection when DRX is not used (PCell in FR2)
3765A.7.6.2.3.1 Test Purpose and Environment 3765A.7.6.2.3.2 Test
Requirements 3767A.7.6.2.4 SA event triggered reporting tests for FR2
with SSB time index detection when DRX is used (PCell in FR2)
3768A.7.6.2.4.1 Test Purpose and Environment 3768A.7.6.2.4.2 Test
Requirements 3770A.7.6.2.5 SA event triggered reporting tests for FR2
without SSB time index detection when DRX is not used (PCell in FR1)
3770A.7.6.2.5.1 Test Purpose and Environment 3770A.7.6.2.5.2 Test
Requirements 3773A.7.6.2.6 SA event triggered reporting tests for FR2
without SSB time index detection when DRX is used (PCell in FR1)
3773A.7.6.2.6.1 Test Purpose and Environment 3773A.7.6.2.6.2 Test
Requirements 3776A.7.6.2.7 SA event triggered reporting tests for FR2
with SSB time index detection when DRX is not used (PCell in FR1)
3776A.7.6.2.7.1 Test Purpose and Environment 3776A.7.6.2.7.2 Test
Requirements 3779A.7.6.2.8 SA event triggered reporting tests for FR2
with SSB time index detection when DRX is used (PCell in FR1)
3779A.7.6.2.8.1 Test Purpose and Environment 3779A.7.6.2.8.2 Test
Requirements 3782A.7.6.2.9 SA event triggered reporting tests For FR2
without SSB time index detection when DRX is not used (PCell in FR2)
(rel16 additional mandatory gap pattern 17) 3782A.7.6.2.9.1 Test Purpose
and Environment 3782A.7.6.2.9.2 Test Requirements 3784A.7.6.2.10 SA
event triggered reporting test without gap under non-DRX
3785A.7.6.2.10.1 Test Purpose and Environment 3785A.7.6.2.10.2 Test
Requirements 3786A.7.6.2.11 SA event triggered reporting test without
gap under DRX 3786A.7.6.2.11.1 Test Purpose and Environment
3787A.7.6.2.11.2 Test Requirements 3788A.7.6.2.12 SA event triggered
reporting tests for FR2-2 without SSB time index detection when DRX is
not used (PCell in FR2-2) 3789A.7.6.2.12.1 Test Purpose and Environment
3789A.7.6.2.12.2 Test Requirements 3791A.7.6.2.13 SA event triggered
reporting tests for FR2-2 without SSB time index detection when DRX is
used (PCell in FR2-2) 3791A.7.6.2.13.1 Test Purpose and Environment
3791A.7.6.2.13.2 Test Requirements 3794A.7.6.2.14 SA event triggered
reporting tests for FR2-2 with SSB time index detection when DRX is not
used (PCell in FR2-2) 3795A.7.6.2.14.1 Test Purpose and Environment
3795A.7.6.2.14.2 Test Requirements 3797A.7.6.2.15 SA event triggered
reporting tests for FR2-2 with SSB time index detection when DRX is used
(PCell in FR2-2) 3798A.7.6.2.15.1 Test Purpose and Environment
3798A.7.6.2.15.2 Test Requirements 3800A.7.6.2.16 SA event triggered
reporting tests for FR2-2 without SSB time index detection when DRX is
not used (PCell in FR1) 3801A.7.6.2.16.1 Test Purpose and Environment
3801A.7.6.2.16.2 Test Requirements 3805A.7.6.2.17 SA event triggered
reporting tests for FR2-2 without SSB time index detection when DRX is
used (PCell in FR1) 3805A.7.6.2.17.1 Test Purpose and Environment
3805A.7.6.2.17.2 Test Requirements 3809A.7.6.2.18 SA event triggered
reporting tests for FR2-2 with SSB time index detection when DRX is not
used (PCell in FR1) 3810A.7.6.2.18.1 Test Purpose and Environment
3810A.7.6.2.18.2 Test Requirements 3813A.7.6.2.19 SA event triggered
reporting tests for FR2-2 with SSB time index detection when DRX is used
(PCell in FR1) 3814A.7.6.2.19.1 Test Purpose and Environment
3814A.7.6.2.19.2 Test Requirements 3818A.7.6.2.20 SA event triggered
reporting tests for FR2 with measurement gap with priority and two
periodic MUSIM gaps configured 3819A.7.6.2.20.1 Test Purpose and
Environment 3819A.7.6.2.20.2 Test Requirements 3821A.7.6.2.21 SA event
triggered reporting tests for FR2 with measurement gap without priority
and periodic MUSIM gap configured 3821A.7.6.2.21.1 Test Purpose and
Environment 3821A.7.6.2.21.2 Test Requirements 3823A.7.6.2.22 SA event
triggered reporting tests with SSB time index detection when DRX is not
used (PCell in FR2) for FR2 power class 6 UE configured with
*highSpeedMeasFlagFR2-r17* 3824A.7.6.2.22.1 Test Purpose and Environment
3824A.7.6.2.22.2 Test Requirements 3826A.7.6.2.23 SA event triggered
reporting tests without SSB time index detection when DRX is not used
(PCell in FR2) for FR2 power class 6 UE configured with
*highSpeedMeasFlagFR2-r17* 3826A.7.6.2.23.1 Test Purpose and Environment
3826A.7.6.2.23.2 Test Requirements 3828A.7.6.3 L1-RSRP measurement for
beam reporting 3828A.7.6.3.1 SSB based L1-RSRP measurement when DRX is
not used 3828A.7.6.3.1.1 Test Purpose and Environment 3828A.7.6.3.1.2
Test parameters 3828A.7.6.3.1.3 Test Requirements 3830A.7.6.3.2 SSB
based L1-RSRP measurement when DRX is used 3830A.7.6.3.2.1 Test Purpose
and Environment 3830A.7.6.3.2.2 Test parameters 3830A.7.6.3.2.3 Test
Requirements 3831A.7.6.3.3 CSI-RS based L1-RSRP measurement when DRX is
not used 3832A.7.6.3.3.1 Test Purpose and Environment 3832A.7.6.3.3.2
Test parameters 3832A.7.6.3.3.3 Test Requirements 3833A.7.6.3.4 CSI-RS
based L1-RSRP measurement when DRX is used 3833A.7.6.3.4.1 Test Purpose
and Environment 3833A.7.6.3.4.2 Test parameters 3834A.7.6.3.3.3 Test
Requirements 3835A.7.6.3.5 SSB based L1-RSRP measurement when DRX is
used for power class 6 UE configured with *highSpeedMeasFlagFR2-r17*
3835A.7.6.3.5.1 Test Purpose and Environment 3835A.7.6.3.5.2 Test
parameters 3836A.7.6.3.5.3 Test Requirements 3837A.7.6.3.6 Inter-cell
SSB based L1-RSRP measurements on FR2 SCell when DRX is not used
3837A.7.6.3.6.1 Test Purpose and Environment 3837A.7.6.3.6.2 Test
parameters 3838A.7.6.3.6.3 Test Requirements 3840A.7.6.3.7 SSB based
L1-RSRP measurement for FR2-2 when DRX is used 3840A.7.6.3.7.1 Test
Purpose and Environment 3840A.7.6.3.7.2 Test parameters 3841A.7.6.3.7.3
Test Requirements 3842A.7.6.3.8 CSI-RS based L1-RSRP measurement when
DRX is not used and when CD-SSB is outside active BWP 3842A.7.6.3.8.1
Test Purpose and Environment 3842A.7.6.3.9 SSB based L1-RSRP measurement
when DRX is not used when CD-SSB is outside active BWP 3843A.7.6.3.9.1
Test Purpose and Environment 3843A.7.6.3.9.2 Test Requirements
3843A.7.6.3.10 SSB based L1-RSRP measurement for UE supporting NCD-SSB
based L1 measurement outside active BWP when DRX is not used
3843A.7.6.3.10.1 Test Purpose and Environment 3843A.7.6.3.10.2 Test
parameters 3843A.7.6.3.10.3 Test Requirements 3845A.7.6.3.11 SSB based
L1-RSRP measurement when DRX is used for power class 6 UE supporting
simultaneousReceptionTwoQCL-r18 3845A.7.6.3.11.1 Test Purpose and
Environment 3845A.7.6.3.11.2 Test parameters 3845A.7.6.3.11.3 Test
Requirements 3847A.7.6.4 CLI measurements 3847A.7.6.4.1 SRS-RSRP
measurement with non-DRX 3847A.7.6.4.1.1 Test Purpose and Environment
3847A.7.6.4.1.2 Test Parameters 3847A.7.6.4.1.3 Test Requirements
3849A.7.6.4.2 CLI-RSSI measurement with non-DRX 3849A.7.6.4.2.1 Test
Purpose and Environment 3849A.7.6.4.2.2 Test Parameters 3850A.7.6.4.2.3
Test Requirements 3851A.7.6.5.1 SA interfrequency CGI reporting in
autonomous gaps test (PCell in FR2) 3851A.7.6.5.1.1 Test Purpose and
Environment 3851A.7.6.5.1.2 Test Requirements 3854A.7.6.6 L1-SINR
measurement for beam reporting 3854A.7.6.6.2 L1-SINR measurement with
SSB based CMR and dedicated IMR when DRX is used 3856A.7.6.6.2.1 Test
Purpose and Environment 3856A.7.6.6.2.2 Test parameters 3856A.7.6.6.2.3
Test Requirements 3857A.7.6.6.3 L1-SINR measurement with CSI-RS based
CMR and dedicated IMR configured when DRX is used 3858A.7.6.6.3.1 Test
Purpose and Environment 3858A.7.6.6.3.2 Test parameters 3858A.7.6.6.3.3
Test Requirements 3859A.7.6.7 CSI-RS based intra-frequency Measurements
3860A.7.6.7.1 SA event triggered reporting test without gap under DRX
for CSI-RS based intra-frequency measurement 3860A.7.6.7.1.1 Test
purpose and Environment 3860A.7.6.7.1.2 Test Requirements 3861A.7.6.8
CSI-RS based inter-frequency Measurements 3862A.7.6.8.1 SA event
triggered reporting tests for FR2 CSI-RS based measurement when non-DRX
is used (PCell in FR2) 3862A.7.6.8.1.1 Test Purpose and Environment
3862A.7.6.8.1.2 Test Requirements 3864A.7.6.9 RSTD measurements
3864A.7.6.9.1 NR RSTD measurement reporting delay test case for single
positioning frequency layer in FR2 SA 3864A.7.6.9.1.1 Test Purpose and
Environment 3864A.7.6.9.1.2 Test Requirements 3868A.7.6.9.2 NR RSTD
measurement reporting delay test case for dual positioning frequency
layers in FR2 SA 3868A.7.6.9.2.1 Test Purpose and Environment
3868A.7.6.9.2.2 Test Requirements 3871A.7.6.9.3 NR RSTD measurement
reporting delay test case for single positioning frequency layer with
reduced number of samples in FR2 SA 3872A.7.6.9.3.1 Test Purpose and
Environment 3872A.7.6.9.3.2 Test Requirements 3874A.7.6.9.4 NR RSTD
measurement reporting delay test case for single positioning frequency
layer in FR2 SA without measurement gap 3875A.7.6.9.4.1 Test Purpose and
Environment 3875A.7.6.9.4.2 Test Requirements 3877A.7.6.9.5 NR RSTD
measurement reporting delay test case for single positioning frequency
layer in FR2 SA in RRC\_CONNECTED state with Rx TEG 3878A.7.6.9.5.1 Test
Purpose and Environment 3878A.7.6.9.5.2 Test Requirements 3881A.7.6.9.6
NR RSTD measurement reporting delay test case for PRS aggregation in FR2
SA in RRC\_CONNECTED mode 3881A.7.6.9.6.1 Test Purpose and Environment
3881A.7.6.9.6.2 Test Requirements 3889A.7.6.10 PRS-RSRP measurements
3889A.7.6.10.1 PRS-RSRP reporting delay test case for single positioning
frequency layer 3889A.7.6.10.1.1 Test Purpose and Environment
3889A.7.6.10.1.2 Test Requirements 3891A.7.6.10.2 PRS-RSRP reporting
delay test case for dual positioning frequency layer 3892A.7.6.10.2.1
Test Purpose and Environment 3892A.7.6.10.2.2 Test Requirements
3894A.7.6.10.3 PRS-RSRP reporting delay test case for reduced number of
samples 3894A.7.6.10.3.1 Test Purpose and Environment 3894A.7.6.10.3.2
Test Requirements 3896A.7.6.10.4 PRS-RSRP reporting delay test case for
single positioning frequency layer outside MG 3897A.7.6.10.4.1 Test
Purpose and Environment 3897A.7.6.10.4.2 Test Requirements 3899A.7.6.11
UE Rx-Tx time difference measurements 3899A.7.6.11.1 UE Rx-Tx time
difference measurements for single positioning frequency layer in FR2 SA
3899A.7.6.11.1.1 Test purpose and environment 3899A.7.6.11.1.2 Test
requirements 3901A.7.6.11.2 UE Rx-Tx time difference measurement period
for dual positioning frequency layers in FR2 SA 3901A.7.6.11.2.1 Test
purpose and environment 3901A.7.6.11.2.2 Test requirements
3903A.7.6.11.3 UE Rx-Tx time difference measurements for single
positioning frequency layer in FR2 SA with reduced sample number
3904A.7.6.11.3.1 Test purpose and environment 3904A.7.6.11.3.2 Test
requirements 3905A.7.6.11.4 UE Rx-Tx time difference measurements
without gaps in FR2 SA 3906A.7.6.11.4.1 Test purpose and environment
3906A.7.6.11.4.2 Test requirements 3907A.7.6.11.5 UE Rx-Tx time
difference measurements for single positioning frequency layer in FR2 SA
with RxTx TEG 3908A.7.6.11.5.1 Test purpose and environment
3908A.7.6.11.5.2 Test requirements 3909A.7.6.11.6 UE Rx-Tx time
difference measurements with PRS bandwidth aggregation in FR2 SA
3910A.7.6.11.6.1 Test purpose and environment 3910A.7.6.11.6.2 Test
requirements 3913A.7.6.12 PRS-RSRPP measurements 3913A.7.6.12.1
PRS-RSRPP reporting delay test case for single positioning frequency
layer in FR2 in RRC\_CONNECTED state 3913A.7.6.12.1.1 Test Purpose and
Environment 3913A.7.6.12.1.2 Test Requirements 3916A.7.6.12.2 PRS-RSRPP
reporting delay test case for reduced number of samples for single
positioning frequency layer in FR2 in RRC\_CONNECTED state
3916A.7.6.12.2.1 Test Purpose and Environment 3916A.7.6.12.2.2 Test
Requirements 3918A.7.6.12.3 PRS-RSRPP reporting delay test case for
gapless measurement in FR2 3918A.7.6.12.3.1 Test Purpose and Environment
3918A.7.6.12.3.2 Test Requirements 3921A.7.6.13 UE Rx-Tx time difference
measurements for PDC 3921A.7.6.13.1 UE Rx-Tx time difference measurement
for propagation delay compensation using PRS in FR2 3921A.7.6.13.1.1
Test purpose and environment 3921A.7.6.13.1.2 Test requirements
3922A.7.6.13.2 UE Rx-Tx time difference measurement for propagation
delay compensation using TRS in FR2 3923A.7.6.13.2.1 Test purpose and
environment 3923A.7.6.13.2.2 Test requirements 3924A.7.6.14 SA event
triggered reporting tests with Pre-MG 3924A.7.6.14.1 Intra-frequency
measurement test with SA event triggered reporting tests: with
**autonomous** activation/deactivation of Pre-MG in FR2 3924A.7.6.14.1.1
Test purpose and Environment 3924A.7.6.14.1.2 Test parameters
3925A.7.6.14.1.3 Test Requirements 3926A.7.6.14.2 Intra-frequency
measurement test with SA event triggered reporting tests: with
network-controlled activation/deactivation of Pre-MG in FR2
3927A.7.6.14.2.1 Test purpose and Environment 3927A.7.6.14.2.2 Test
parameters 3927A.7.6.14.2.3 Test Requirements 3929A.7.6.15 SA event
triggered reporting tests with concurrent gaps 3929A.7.6.15.1 SA event
triggered reporting tests For FR2 with fully non-overlapping concurrent
MGs for SSB-based inter-frequency measurements 3929A.7.6.15.1.1 Test
Purpose and Environment 3929A.7.6.15.1.2 Test Requirements
3931A.7.6.15.2 SA event triggered reporting tests For FR2 with
concurrent measurement gaps without SSB time index detection when DRX is
not used (PCell in FR2) 3932A.7.6.15.2.1 Test Purpose and Environment
3932A.7.6.15.2.2 Test Requirements 3934A.7.6.15.3 SA event triggered
reporting tests for FR2 concurrent gap with partially partial
overlapping scenario for SSB-based measurements and PRS-based
measurement 3934A.7.6.15.3.1 Test Purpose and Environment
3934A.7.6.15.3.2 Test Requirements 3937A.7.6.16 SA event triggered
reporting tests with NCSG 3937A.7.6.16.1 SA event triggered reporting
test with per-UE NCSG under non-DRX 3937A.7.6.16.1.1 Test purpose and
Environment 3937A.7.6.16.1.2 Test Requirements 3940A.7.6.16.2 SA event
triggered reporting tests on inter-frequency measurement with NCSG for
FR2 when DRX is not used (PCell in FR2) 3940A.7.6.16.2.1 Test Purpose
and Environment 3940A.7.6.16.2.2 Test Requirements 3942A.7.6.16.3 Event
triggered reporting test on deactivated SCell measurement via NCSG in
FR2 in non-DRX 3943A.7.6.16.3.1 Test Purpose and Environment
3943A.7.6.16.3.2 Test Requirements 3945A.7.6.17 SA event triggered
reporting tests for concurrent measurement gaps with Pre-MG in FR2
3945A.7.6.17.1 SA event triggered reporting test for FR2 with one
pre-configured gap and one measurement gap 3945A.7.6.17.1.1 Test Purpose
and Environment 3945A.7.6.17.1.2 Test Requirements 3947A.7.6.17.2
Inter-frequency measurement test with SA event triggered reporting
tests: with **autonomous** activation/deactivation of Pre-MGs in FR2
3948A.7.6.17.2.1 Test purpose and Environment 3948A.7.6.17.2.2 Test
parameters 3948A.7.6.17.2.3 Test Requirements 3950A.7.6.18 SA event
triggered reporting tests with concurrent gaps and NCSG 3951A.7.6.18.1
SA event triggered reporting tests For FR2 with concurrent measurement
gaps and NCSG without SSB time index detection when DRX is not used
(PCell in FR2) 3951A.7.6.18.1.1 Test Purpose and Environment
3951A.7.6.18.1.2 Test Requirements 3953A.7.6.19 SA event triggered
reporting tests with NeedForGap in FR2 3954A.7.6.19.1 SA event triggered
reporting test for UE indicating *NeedforInterruptionInfoNR* under
non-DRX and no interruption outside configured measurement gaps
3954A.7.6.19.1.1 Test purpose and Environment 3954A.7.6.19.1.2 Test
Requirements 3956A.7.6.19.2 SA event triggered reporting test without
gap under non-DRX 3956A.7.6.19.2.1 Test purpose and Environment
3956A.7.6.19.2.2 Test Requirements 3958A.7.6.19.3 SA event triggered
reporting test without gap without interruption under non-DRX
3959A.7.6.19.3.1 Test Purpose and Environment 3959A.7.6.19.3.2 Test
Requirements 3961A.7.6.20 LTM Intra-frequency L1-RSRP measurement
3961A.7.6.20.1 Intra-frequency SSB based L1-RSRP measurement in FR2
3961A.7.6.20.1.1 Test Purpose and Environment 3961A.7.6.20.1.2 Test
parameters 3962A.7.6.20.1.3 Test Requirements 3964A.7.6.21 LTM
Inter-frequency L1-RSRP measurement with measurement gap 3964A.7.6.21.1
Inter-frequency SSB-based L1-RSRP measurement with measurement gap for
LTM in FR2 3964A.7.6.21.1.1 Test Purpose and Environment
3964A.7.6.21.1.2 Test parameters 3964A.7.6.21.1.3 Test Requirements
3966A.7.6.22 LTM Inter-frequency L1-RSRP measurement without measurement
gap 3966A.7.6.22.1 Inter-frequency SSB based L1-RSRP measurement without
measurement gap in FR2 3966A.7.6.22.1.1 Test Purpose and Environment
3966A.7.6.22.1.2 Test parameters 3967A.7.6.22.1.3 Test Requirements
3969A.7.6.23 Idle Mode CA/DC Measurements 3969A.7.6.23.1 Test case for
Idle mode fast CA/DC eEMR measurement for FR2 without valid reporting
3969A.7.6.23.1.1 Test Purpose and Environment 3969A.7.6.23.1.2 Test
Requirements 3972A.7.6.23.2 Test case for Idle mode fast CA/DC cell
reselection measurement for FR2 without valid reporting 3972A.7.6.23.2.1
Test Purpose and Environment 3973A.7.6.23.2.2 Test Requirements
3976A.7.6.23.3 Test case for Idle mode fast CA/DC cell reselection
measurement for FR2 with valid reporting 3976A.7.6.23.3.1 Test Purpose
and Environment 3976A.7.6.23.3.2 Test Requirements 3979A.7.6.24 RSCPD
measurements 3980A.7.6.24.1 NR RSCPD with RSTD measurement reporting
delay test case for single positioning frequency layer in FR2 SA in
RRC\_CONNECTED state 3980A.7.6.24.1.1 Test Purpose and Environment
3980A.7.6.24.1.2 Test Requirements 3987A.7.6.25 RSCP measurements
3987A.7.6.25.1 DL RSCP with UE Rx-Tx time difference measurements for
single positioning frequency layer in FR2 SA 3987A.7.6.25.1.1 Test
purpose and environment 3987A.7.6.25.1.2 Test requirements 3991A.7.7
Measurement Performance requirements 3991A.7.7.1 SS-RSRP 3991A.7.7.1.1
SA intra-frequency case measurement accuracy with FR2 serving cell and
FR2 target cell 3991A.7.7.1.1.1 Test Purpose and Environment
3991A.7.7.1.1.2 Test parameters 3991A.7.7.1.1.3 Test Requirements
3993A.7.7.1.2 SA inter-frequency case measurement accuracy with FR2
serving cell and FR2 target cell 3994A.7.7.1.2.1 Test Purpose and
Environment 3994A.7.7.1.2.2 Test parameters 3994A.7.7.1.2.3 Test
Requirements 3996A.7.7.1.3 SA inter-frequency measurement accuracy with
FR1 serving cell and FR2 target cell 3997A.7.7.1.3.1 Test Purpose and
Environment 3997A.7.7.1.3.2 Test parameters 3997A.7.7.1.3.3 Test
Requirements 3999A.7.7.2 SS-RSRQ 4000A.7.7.2.1 SA intra-frequency
measurement accuracy with FR2 serving cell and FR2 target cell
4000A.7.7.2.1.1 Test Purpose and Environment 4000A.7.7.2.1.2 Test
Parameters 4000A.7.7.2.1.3 Test Requirements 4001A.7.7.2.2 SA
Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 4002A.7.7.2.2.1 Test Purpose and Environment 4002A.7.7.2.2.2
Test Parameters 4002A.7.7.2.2.3 Test Requirements 4003A.7.7.3 SS-SINR
4003A.7.7.3.1 SA intra-frequency case measurement accuracy with FR2
serving cell and FR2 target cell 4003A.7.7.3.1.1 Test Purpose and
Environment 4003A.7.7.3.1.2 Test Parameters 4003A.7.7.3.1.3 Test
Requirements 4005A.7.7.3.2 SA Inter-frequency measurement accuracy with
FR2 serving cell and FR2 TDD target cell 4005A.7.7.3.2.1 Test Purpose
and Environment 4005A.7.7.3.2.2 Test Parameters 4005A.7.7.3.2.3 Test
Requirements 4007A.7.7.4 L1-RSRP measurement for beam reporting
4007A.7.7.4.1 SSB based L1-RSRP measurement 4007A.7.7.4.1.1 Test Purpose
and Environment 4007A.7.7.4.1.2 Test parameters 4007A.7.7.4.1.3 Test
Requirements 4008A.7.7.4.2 CSI-RS based L1-RSRP measurement on resource
set with repetition off 4009A.7.7.4.2.1 Test Purpose and Environment
4009A.7.7.4.2.2 Test parameters 4009A.7.7.4.2.3 Test Requirements
4010A.7.7.5 CLI measurements 4011A.7.7.5.1 SA SRS-RSRP measurement
accuracy with FR2 serving cell 4011A.7.7.5.1.1 Test Purpose and
Environment 4011A.7.7.5.1.2 Test parameters 4011A.7.7.5.1.3 Test
Requirements 4013A.7.7.5.2 SA CLI-RSSI measurement accuracy with FR2
serving cell 4013A.7.7.5.2.1 Test Purpose and Environment
4013A.7.7.5.2.2 Test parameters 4014A.7.7.5.2.3 Test Requirements
4015A.7.7.6 L1-SINR measurement for beam reporting 4016A.7.7.6.1.1 Test
Purpose and Environment 4016A.7.7.6.1.2 Test parameters 4016A.7.7.6.1.3
Test Requirements 4017A.7.7.6.2 L1-SINR measurement with SSB based CMR
and dedicated IMR 4018A.7.7.6.2.1 Test Purpose and Environment
4018A.7.7.6.2.2 Test parameters 4018A.7.7.6.2.3 Test Requirements
4019A.7.7.6.3 L1-SINR measurement with CSI-RS based CMR and dedicated
IMR 4020A.7.7.6.3.1 Test Purpose and Environment 4020A.7.7.6.3.2 Test
parameters 4020A.7.7.6.3.3 Test Requirements 4021A.7.7.7 CSI-RSRP
4022A.7.7.7.1 SA intra-frequency case measurement accuracy with FR2
serving cell and FR2 target cell 4022A.7.7.7.1.1 Test Purpose and
Environment 4022A.7.7.7.1.2 Test parameters 4022A.7.7.7.1.3 Test
Requirements 4024A.7.7.7.2 SA inter-frequency case measurement accuracy
with FR2 serving cell and FR2 target cell 4025A.7.7.7.2.1 Test Purpose
and Environment 4025A.7.7.7.2.2 Test parameters 4025A.7.7.7.2.3 Test
Requirements 4026A.7.7.8 CSI-RSRQ 4027A.7.7.8.1 SA intra-frequency
measurement accuracy with FR2 serving cell and FR2 target cell
4027A.7.7.8.1.1 Test Purpose and Environment 4027A.7.7.8.1.2 Test
Parameters 4027A.7.7.8.1.3 Test Requirements 4029A.7.7.8.2 SA
Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 4029A.7.7.8.2.1 Test Purpose and Environment 4029A.7.7.8.2.2
Test Parameters 4029A.7.7.8.2.3 Test Requirements 4031A.7.7.9 CSI-SINR
4031A.7.7.9.1 SA intra-frequency case measurement accuracy with FR2
serving cell and FR2 target cell 4031A.7.7.9.1.1 Test Purpose and
Environment 4031A.7.7.9.1.2 Test Parameters 4031A.7.7.9.1.3 Test
Requirements 4033A.7.7.9.2 SA Inter-frequency measurement accuracy with
FR2 serving cell and FR2 TDD target cell 4033A.7.7.9.2.1 Test Purpose
and Environment 4033A.7.7.9.2.2 Test Parameters 4033A.7.7.9.2.3 Test
Requirements 4034A.7.7.10 RSTD measurements 4035A.7.7.10.1 RSTD
measurement accuracy test case for single positioning frequency layer
4035A.7.7.10.1.1 Test purpose and Environment 4035A.7.7.10.1.2 Test
Requirements 4036A.7.7.10.2 RSTD measurement accuracy test case for dual
positioning frequency layer 4036A.7.7.10.2.1 Test purpose and
Environment 4036A.7.7.10.2.2 Test Requirements 4038A.7.7.10.3 RSTD
measurement accuracy test case with reduced number of samples for single
positioning frequency layer in FR2 in RRC\_CONNECTED state
4038A.7.7.10.3.1 Test purpose and Environment 4038A.7.7.10.3.2 Test
Requirements 4040A.7.7.10.4 RSTD measurement accuracy test case with Rx
TEG 4040A.7.7.10.4.1 Test purpose and Environment 4040A.7.7.10.4.2 Test
Requirements 4041A.7.7.10.5 NR RSTD measurement accuracy test case for
PRS aggregation in FR2 SA in RRC\_CONNECTED mode 4041A.7.7.10.5.1 Test
purpose and Environment 4041A.7.7.10.5.2 Test Requirements 4043A.7.7.11
PRS-RSRP measurements 4043A.7.7.11.1 SA measurement accuracy with PRS in
FR2 4043A.7.7.11.1.1 Test Purpose and Environment 4043A.7.7.11.1.2 Test
parameters 4043A.7.7.11.1.3 Test Requirements 4045A.7.7.11.2 SA
measurement accuracy with PRS in FR2 with reduced sample number
4045A.7.7.11.2.1 Test Purpose and Environment 4045A.7.7.11.2.2 Test
parameters 4045A.7.7.11.2.3 Test Requirements 4047A.7.7.12 UE Rx-Tx time
difference measurements 4047A.7.7.12.1 UE Rx-Tx time difference
measurement accuracy for single positioning frequency layer in FR2 SA
4047A.7.7.12.1.1 Test purpose and environment 4047A.7.7.12.1.2 Test
parameters 4048A.7.7.12.1.3 Test requirements 4049A.7.7.12.2 UE Rx-Tx
time difference measurement accuracy with reduced number of samples in
FR2 SA 4050A.7.7.12.2.1 Test purpose and environment 4050A.7.7.12.2.2
Test parameters 4050A.7.7.12.2.3 Test requirements 4051A.7.7.12.3 UE
Rx-Tx time difference measurement accuracy with RxTx TEG
4051A.7.7.12.3.1 Test purpose and environment 4051A.7.7.12.3.2 Test
parameters 4052A.7.7.12.3.3 Test requirements 4053A.7.7.12.4 UE Rx-Tx
time difference measurement accuracy with PRS bandwidth aggregation in
FR2 SA 4054A.7.7.12.4.1 Test purpose and environment 4054A.7.7.12.4.2
Test requirements 4058A.7.7.13 PRS-RSRPP measurements 4058A.7.7.13.1 SA
measurement accuracy with PRS in FR2 4058A.7.7.13.1.1 Test Purpose and
Environment 4058A.7.7.13.1.2 Test parameters 4058A.7.7.13.1.3 Test
Requirements 4060A.7.7.13.2 SA measurement accuracy with reduced PRS
samples in FR2 4060A.7.7.13.2.1 Test Purpose and Environment
4060A.7.7.13.2.2 Test parameters 4060A.7.7.13.2.3 Test Requirements
4062A.7.7.14 L1-RSRP measurement for group-based beam reporting
4062A.7.7.14.1 SSB based L1-RSRP measurement 4062A.7.7.14.1.1 Test
Purpose and Environment 4062A.7.7.14.1.2 Test parameters
4062A.7.7.14.1.3 Test Requirements 4064A.7.7.14.2 CSI-RS based L1-RSRP
measurement on resource set with repetition off 4064A.7.7.14.2.1 Test
Purpose and Environment 4064A.7.7.14.2.2 Test parameters
4064A.7.7.14.2.3 Test Requirements 4066A.7.7.15 LTM L1-RSRP measurement
4066A.7.7.15.1 SSB based inter-frequency L1-RSRP measurement
4066A.7.7.15.1.1 Test Purpose and Environment 4066A.7.7.15.1.2 Test
parameters 4067A.7.7.15.1.3 Test Requirements 4068A.7.7.16 RSCPD
Measurements 4069A.7.7.16.1 RSCPD with RSTD measurement accuracy in FR2
SA in RRC\_CONNECTED 4069A.7.7.16.1.1 Test purpose and environment
4069A.7.7.16.1.2 Test parameters 4069A.7.7.16.1.3 Test requirements
4071A.7.7.17 RSCP with UE Rx-Tx time difference measurements
4071A.7.7.17.1 RSCP with UE Rx-Tx time difference measurement accuracy
in FR2 SA 4071A.7.7.17.1.1 Test purpose and environment 4071A.7.7.17.1.2
Test parameters 4072A.7.7.17.1.3 Test requirements 4075A.7.8 Measurement
procedure in RRC\_INACTIVE 4075A.7.8.1 RSTD measurements 4075A.7.8.1.1
NR RSTD measurement reporting delay test case for single positioning
frequency layer in FR2 SA in RRC\_INACTIVE state 4075A.7.8.1.1.1 Test
Purpose and Environment 4075A.7.8.1.1.2 Test Requirements 4078A.7.8.1.2
NR RSTD measurement reporting delay test case with reduced number of
samples in RRC\_INACTIVE, FR1 SA 4078A.7.8.1.2.1 Test Purpose and
Environment 4078A.7.8.1.2.2 Test Requirements 4081A.7.8.1.3 NR RSTD
measurement reporting delay test case for PRS aggregation in FR2 SA in
RRC\_INACTIVE state 4081A.7.8.1.3.1 Test purpose and environment
4081A.7.8.1.3.2 Test requirements 4085A.7.8.1.4 NR RSTD measurement
reporting delay test case for single positioning frequency layer in FR2
SA in RRC\_INACTIVE state with eDRX \> 10.24s 4085A.7.8.1.4.1 Test
purpose and environment 4085A.7.8.1.4.2 Test requirements 4088A.7.8.2
PRS-RSRP measurements 4088A.7.8.2.1 PRS-RSRP reporting delay test case
for single positioning frequency layer in RRC\_INACTIVE 4088A.7.8.2.1.1
Test Purpose and Environment 4088A.7.8.2.1.2 Test Requirements
4090A.7.8.2.2 PRS-RSRP reporting delay test case with reduced number of
samples in RRC\_INACTIVE 4091A.7.8.2.2.1 Test purpose and Environment
4091A.7.**8.2.2**.2 Test Requirements 4093A.7.8.2.3 PRS-RSRP reporting
delay in RRC\_INACTIVE with eDRX 4093A.7.8.2.3.1 Test Purpose and
Environment 4093A.7.8.2.3.2 Test Requirements 4097A.7.8.3 UE Rx-Tx time
difference measurements 4097A.7.8.3.1 UE Rx-Tx time difference
measurements for single positioning frequency layer in FR2 SA
4097A.7.8.3.1.1 Test purpose and environment 4097A.7.8.3.1.2 Test
requirements 4099A.7.8.3.2 UE Rx-Tx time difference measurement with
reduced number of samples in RRC\_INACTIVE, FR2 SA 4099A.7.8.3.2.1 Test
purpose and environment 4099A.7.**8.3.2**.2 Test requirements
4101A.7.8.3.3 UE Rx-Tx time difference measurements with PRS bandwidth
aggregation in FR2 SA 4101A.7.8.3.3.1 Test purpose and environment
4101A.7.8.3.3.2 Test requirements 4104A.7.8.3.4 UE Rx-Tx time difference
measurements for single positioning frequency layer with eDRX \> 10.24s
in FR2 SA 4104A.7.8.3.4.1 Test purpose and environment 4104A.7.8.3.4.2
Test requirements 4107A.7.8.4 PRS-RSRPP measurements 4107A.7.8.4.1
PRS-RSRPP reporting delay test case for single positioning frequency
layer in FR2 in RRC\_INACTIVE state 4107A.7.8.4.1.1 Test Purpose and
Environment 4107A.7.8.4.1.2 Test Requirements 4110A.7.8.4.2 PRS-RSRPP
reporting delay test with reduced number of samples for single
positioning frequency layer in FR2 in RRC\_INACTIVE state
4110A.7.8.4.2.1 Test Purpose and Environment 4110A.7.8.4.2.2 Test
Requirements 4112A.7.8.4.3 PRS-RSPP reporting delay in RRC\_INACTIVE
state with eDRX \> 10.24s in FR2 4113A.7.8.4.3.1 Test purpose and
environment 4113A.7.8.4.3.2 Test requirements 4116A.7.8.5 RSCPD
Measurements 4116A.7.8.5.1 DL RSCPD reported with RSTD measurement
reporting delay test case for single positioning frequency layer in FR2
SA in RRC\_INACTIVE state 4116A.7.8.5.1.1 Test Purpose and Environment
4116A.7.8.5.1.2 Test Requirements 4117A.7.8.6 RSCP Measurements
4117A.7.8.6.1 DL RSCP with UE Rx-Tx time difference measurements in
RRC\_INACTIVE for single positioning frequency layer in FR2 SA
4117A.7.8.6.1.1 Test purpose and environment 4117A.7.8.6.1.2 Test
requirements 4121A.7.9 Measurement performance requirements in
RRC\_INACTIVE 4121A.7.9.1 RSTD measurements 4121A.7.9.1.1 RSTD
measurement accuracy test case for single positioning frequency layer in
FR2 in RRC\_INACTIVE state 4121A.7.9.1.1.1 Test purpose and Environment
4121A.7.9.1.1.2 Test Requirements 4123A.7.9.1.2 RSTD measurement
accuracy test case with reduced number of samples for single positioning
frequency layer in FR2 in RRC\_INACTIVE state 4123A.7.9.1.2.1 Test
purpose and Environment 4123A.7.9.1.2.2 Test Requirements 4125A.7.9.2
PRS-RSRP measurements 4127A.7.9.2.1 SA measurement accuracy with PRS in
FR2 in RRC\_INACTIVE 4127A.7.9.2.1.1 Test Purpose and Environment
4127A.7.9.2.1.2 Test parameters 4127A.7.9.2.1.3 Test Requirements
4128A.7.9.2.2 PRS-RSRP measurements with reduced number of sample in
RRC\_INACTIVE 4129A.7.9.2.2.1 Test Purpose and Environment
4129A.7.9.2.2.2 Test parameters 4129A.7.9.2.2.3 Test Requirements
4130A.7.9.3 UE Rx-Tx time difference measurements 4131A.7.9.3.1 UE Rx-Tx
time difference measurements in RRC\_INACTIVE 4131A.7.9.3.1.1 Test
purpose and environment 4131A.7.9.3.1.2 Test parameters 4131A.7.9.3.1.3
Test requirements 4132A.7.9.3.2 UE Rx-Tx time difference measurement
accuracy with reduced number of samples in FR2 SA 4132A.7.9.3.2.1 Test
purpose and environment 4132A.7.9.3.2.2 Test parameters 4133A.7.9.3.2.3
Test requirements 4134A.7.9.3.3 UE Rx-Tx time difference measurement
accuracy with PRS bandwidth aggregation in FR2 SA in RRC\_INACTIVE state
4134A.7.9.3.3.1 Test purpose and environment 4134A.7.9.3.3.2 Test
requirements 4138A.7.9.4 PRS-RSRPP measurements 4138A.7.9.4.1 SA
measurement accuracy in FR2 in RRC INACTIVE 4138A.7.9.4.1.1 Test Purpose
and Environment 4138A.7.9.4.1.2 Test parameters 4138A.7.9.4.1.3 Test
Requirements 4140A.7.9.4.2 SA measurement accuracy with reduced PRS
samples in FR2 in RRC INACTIVE 4140A.7.9.4.2.1 Test Purpose and
Environment 4140A.7.9.4.2.2 Test parameters 4140A.7.9.4.2.3 Test
Requirements 4142A.7.9.5 RSCPD Measurements 4142A.7.9.5.1 RSCPD with
RSTD measurement accuracy in FR2 SA in RRC\_INACTIVE 4142A.7.9.5.1.1
Test purpose and environment 4142A.7.9.5.1.2 Test parameters
4142A.7.9.5.1.3 Test requirements 4144A.7.9.6 RSCP Measurements
4144A.7.9.6.1 RSCP with UE Rx-Tx time difference measurement accuracy in
FR2 SA 4144A.7.9.6.1.1 Test purpose and environment 4144A.7.9.6.1.2 Test
parameters 4145A.7.9.6.1.3 Test requirements 4146A.7.10 Measurement
Procedure in RRC\_IDLE 4146A.7.10.1 RSTD Measurements 4146A.7.10.1.1 NR
RSTD measurement reporting delay test case for single positioning
frequency layer in FR2 SA in RRC\_IDLE state for non-RedCap UE
4146A.7.10.1.1.1 Test purpose and environment 4146A.7.10.1.1.2 Test
requirements 4149A.7.10.1.2 NR RSTD measurement reporting delay test
case for single positioning frequency layer in FR2 SA in RRC\_IDLE state
with eDRX \> 10.24s 4149A.7.10.1.2.1 Test purpose and environment
4149A.7.10.1.2.2 Test requirements 4152A.7.10.1.3 NR RSTD measurement
reporting delay test case for PRS aggregation in FR2 SA in RRC\_IDLE
state 4152A.7.10.1.3.1 Test purpose and environment 4152A.7.10.1.3.2
Test requirements 4153A.7.10.2 PRS-RSRP Measurements 4153A.7.10.2.1
PRS-RSRP reporting delay test case for single positioning frequency
layer in RRC\_IDLE state for non-RedCap UE in FR2 4153A.7.10.2.1.1 Test
Purpose and Environment 4153A.7.10.2.1.2 Test Requirements
4157A.7.10.2.2 PRS-RSRP reporting delay test case in RRC\_IDLE state in
FR2 when eDRX cycle \> 10.24s 4157A.7.10.2.2.1 Test Purpose and
Environment 4157A.7.10.2.2.2 Test Requirements 4157A.7.10.3 RSCPD
Measurements 4158A.7.10.3.1 DL RSCPD reported with RSTD measurement
reporting delay test case for single positioning frequency layer in FR2
SA in RRC\_IDLE state 4158A.7.10.3.1.1 Test Purpose and Environment
4158A.7.10.3.1.2 Test Requirements 4158A.7.11 Measurement Performance
Requirements in RRC\_IDLE 4159A.7.11.1 RSTD Measurements 4159A.7.11.1.1
NR RSTD measurement accuracy test case for single positioning frequency
layer in FR2 SA in RRC\_IDLE state for non-RedCap UE 4159A.7.11.1.1.1
Test purpose and environment 4159A.7.11.1.1.2 Test requirements
4160A.7.11.1.2 RSTD measurement accuracy test case for single
positioning frequency layer in FR2 SA in RRC\_IDLE state with eDRX \>
10.24s 4161A.7.11.1.2.1 Test purpose and environment 4161A.7.11.1.2.2
Test requirements 4162A.7.11.1.3 NR RSTD measurement accuracy test case
for PRS aggregation in FR2 SA in RRC\_IDLE state 4163A.7.11.1.3.1 Test
purpose and environment 4163A.7.11.1.3.2 Test requirements 4163A.7.11.2
PRS-RSRP measurements 4163A.7.11.2.1 PRS-RSRP measurement accuracy test
case for non-RedCap UE in FR2 in RRC\_IDLE state 4163A.7.11.2.1.1 Test
Purpose and Environment 4163A.7.11.2.1.2 Test parameters
4163A.7.11.2.1.3 Test Requirements 4165A.7.11.2.2 PRS-RSRP measurement
accuracy test case in RRC\_IDLE state in FR2 for case 2 when eDRX cycle
\> 10.24s 4165A.7.11.2.2.1 Test purpose and Environment 4165A.7.11.2.2.1
Test parameters 4166A.7.11.2.2.2 Test Requirements 4166A.7.11.3 RSCPD
measurements 4166A.7.11.3.1 RSCPD with RSTD measurement accuracy in FR2
SA in RRC\_IDLE 4166A.7.11.3.1.1 Test purpose and environment
4166A.7.11.3.1.2 Test parameters 4166A.7.11.3.1.3 Test requirements
4168A.8 E-UTRA standalone tests for NR RRM 4170A.8.1 Void 4170A.8.2
RRC\_IDLE state mobility 4170A.8.2.1 Inter-RAT NR Cell re-selection
4170A.8.2.1.1 E-UTRA Cell reselection to higher priority NR target Cell
in FR1 4170A.8.2.1.1.1 Test Purpose and Environment 4170A.8.2.1.1.2 Test
Requirements 4173A.8.2.1.2 E-UTRA Cell reselection to lower priority NR
target Cell in FR1 for UE configured with highSpeedInterRAT-NR-r16
4173A.8.2.1.2.1 Test Purpose and Environment 4173A.8.2.1.2.2 Test
Requirements 4176A.8.2.2 E-UTRA -- NR Inter-RAT Early Measruement
Reporting 4177A.8.2.2.1 E-UTRA -- NR Early Measurement Reporting for NR
in FR1 4177A.8.2.2.1.1 Test Purpose and Environment 4177A.8.2.2.1.2 Test
Requirements 4179A.8.2.2.2 E-UTRA -- NR Early Measurement Reporting for
NR in FR2 4180A.8.2.2.2.1 Test Purpose and Environment 4180A.8.2.2.2.2
Test Requirements 4182A.8.3 RRC\_CONNECTED state mobility 4182A.8.3.1
Handover 4182A.8.3.1.1 E-UTRAN - NR handover in FR1 4182A.8.3.1.1.1 Test
Purpose and Environment 4182A.8.3.1.1.2 Test Requirements 4186A.8.4
Measurement procedure 4186A.8.4.1 E-UTRA -- NR Inter-RAT SFTD
Measurement Delay 4186A.8.4.1.1 E-UTRA -- NR Inter-RAT SFTD Measurement
Delay in non-DRX 4186A.8.4.1.1.1 Test Purpose and Environment
4186A.8.4.1.1.2 Test Requirements 4188A.8.4.1.2 E-UTRA -- NR Inter-RAT
SFTD Measurement Delay in DRX 4188A.8.4.1.2.1 Test Purpose and
Environment 4188A.8.4.1.2.2 Test Requirements 4189A.8.4.2 E-UTRA -- NR
Inter-RAT Measurements 4189A.8.4.2.1 NR Inter-RAT event triggered
reporting tests for FR1 without SSB time index detection when DRX is not
used 4189A.8.4.2.1.1 Test Purpose and Environment 4189A.8.4.2.1.2 Test
Requirements 4192A.8.4.2.2 NR Inter-RAT event triggered reporting tests
for FR1 without SSB time index detection when DRX is used
4192A.8.4.2.2.1 Test Purpose and Environment 4192A.8.4.2.2.2 Test
Requirements 4195A.8.4.2.3 NR Inter-RAT event triggered reporting tests
for FR1 with SSB time index detection when DRX is not used
4196A.8.4.2.3.1 Test Purpose and Environment 4196A.8.4.2.3.2 Test
Requirements 4199A.8.4.2.4 NR Inter-RAT event triggered reporting tests
for FR1 with SSB time index detection when DRX is used 4199A.8.4.2.4.1
Test Purpose and Environment 4199A.8.4.2.4.2 Test Requirements
4202A.8.4.2.5 NR Inter-RAT event triggered reporting tests for FR2
without SSB time index detection when DRX is not used 4202A.8.4.2.5.1
Test Purpose and Environment 4202A.8.4.2.5.2 Test Requirements
4204A.8.4.2.6 NR Inter-RAT event triggered reporting tests for FR2
without SSB time index detection when DRX is used 4205A.8.4.2.6.1 Test
Purpose and Environment 4205A.8.4.2.6.2 Test Requirements 4206A.8.4.2.7
NR Inter-RAT event triggered reporting tests for FR2 with SSB time index
detection when DRX is not used 4207A.8.4.2.7.1 Test Purpose and
Environment 4207A.8.4.2.7.2 Test Requirements 4209A.8.4.2.8 NR Inter-RAT
event triggered reporting tests for FR2 with SSB time index detection
when DRX is used 4209A.8.4.2.8.1 Test Purpose and Environment
4209A.8.4.2.8.2 Test Requirements 4211A.8.4.2.9 NR Inter-RAT event
triggered reporting tests for FR1 with SSB time index detection in DRX
for UE configured with highSpeedInterRAT-NR-r16 4211A.8.4.2.9.1 Test
Purpose and Environment 4211A.8.4.2.9.2 Test Requirements 4214A.8.4.3
E-UTRAN - NR Inter-RAT event-triggered without measurement gaps
4215A.8.4.3.1 NR Inter-RAT event triggered reporting tests for FR2
without MG nor DRX 4215A.8.4.3.1.1 Test Purpose and Environment
4215A.8.4.3.1.2 Test Requirements 4216A.8.4.3.2 NR Inter-RAT event
triggered reporting tests for FR1 without gaps when DRX is not used
4217A.8.4.3.2.1 Test Purpose and Environment 4217A.8.4.3.2.2 Test
Requirements 4220A.8.5 Measurement performance 4220A.8.5.1 SFTD accuracy
4220A.8.5.1.1 SFTD accuracy 4220A.8.5.1.1.1 Test Purpose 4220A.8.5.1.1.2
Test Environment 4220A.8.5.1.1.3 Test Requirements 4224A.8.5.2 E-UTRA --
NR Inter-RAT Measurement Performance requirements 4224A.8.5.2.1.1
E-UTRAN -- NR inter-RAT measurements with FR1 target cell
4224A.8.5.2.1.2 E-UTRAN -- NR inter-RAT measurements with FR2 target
cell 4227A.8.5.2.1.2.1 Test Purpose and Environment 4227A.8.5.2.1.2.2
Test Parameters 4227A.8.5.2.1.2.3 Test Requirements 4228A.8.5.2.2
SS-RSRQ 4228A.8.5.2.2.1 E-UTRAN -- NR inter-RAT measurements with FR1
target cell 4228A.8.5.2.2.2 E-UTRAN -- NR inter-RAT measurements with
FR2 target cell 4231A.8.5.2.2.2.1 Test Purpose and Environment
4231A.8.5.2.2.2.2 Test Parameters 4231A.8.5.2.2.2.3 Test Requirements
4233A.8.5.2.3 SS-SINR 4233A.8.5.2.3.1 E-UTRAN -- NR inter-RAT
measurements with FR1 target cell 4233A.8.5.2.3.2 E-UTRAN -- NR
inter-RAT measurements with FR2 target cell 4236A.8.5.2.3.2.1 Test
Purpose and Environment 4236A.8.5.2.3.2.2 Test Parameters
4236A.8.5.2.3.2.3 Test Requirements 4238A.9 V2X Tests 4238A.9.1 V2X
Tests in FR1 4238A.9.1.1 Test for V2X UE Transmit Timing 4238A.9.1.1.1
Test for GNSS as Synchronization Reference Source 4238A.9.1.1.1.1 Test
Purpose and Environment 4238A.9.1.1.1.2 Test requirements 4238A.9.1.1.2
Test for SyncRef UE as Synchronization Reference Source 4238A.9.1.1.2.1
Test Purpose and Environment 4238A.9.1.1.2.2 Test requirements
4239A.9.1.1.3 Test for FR1 NR Cell as Synchronization Reference Source
4239A.9.1.1.3.1 Test Purpose and Environment 4239A.9.1.1.3.2 Test
requirements 4241A.9.1.2 Test for Initiation/Cease of S-SSB Transmission
with V2X Sidelink Communication 4241A.9.1.2.1 Test for FR1 NR Cell as
synchronization reference source without gap under non-DRX
4241A.9.1.2.1.1 Test Purpose and Environment 4241A.9.1.2.1.2 Test
Requirements 4243A.9.1.2.2 Test for SyncRef UE as synchronization
reference source 4243A.9.1.2.2.1 Test Purpose and Environment
4243A.9.1.2.2.2 Test Requirements 4244A.9.1.2.3 Test for SyncRef UE as
synchronization reference source when SL-DRX is used 4245A.9.1.2.3.1
Test Purpose and Environment 4245A.9.1.2.3.2 Test Requirements
4246A.9.1.2.4 Test for SyncRef UE as synchronization reference source
with CCA 4246A.9.1.2.4.1 Test Purpose and Environment 4247A.9.1.2.4.2
Test Requirements 4248A.9.1.3 Test for V2X Synchronization Reference
Selection/Reselection 4248A.9.1.3.1 Test for GNSS configured as the
highest priority 4248A.9.1.3.1.1 Test Purpose and Environment
4248A.9.1.3.1.2 Test Requirements 4250A.9.1.3.2 Test for FR1 NR Cell
configured as the highest priority 4251A.9.1.3.2.1 Test Purpose and
Environment 4251A.9.1.3.2.2 Test Requirements 4252A.9.1.3.3 Test for
GNSS configured as the highest priority under SL-DRX 4253A.9.1.3.3.1
Test Purpose and Environment 4253A.9.1.3.3.2 Test Requirements
4254A.9.1.3.4 Test for FR1 NR Cell configured as the highest priority
under SL-DRX 4255A.9.1.3.4.1 Test Purpose and Environment
4255A.9.1.3.4.2 Test Requirements 4257A.9.1.4 Test for L1 SL-RSRP
Measurement 4257A.9.1.4.1 Test for V2X UE Autonomous Resource
Selection/Reselection 4257A.9.1.4.1.1 Test Purpose and Environment
4257A.9.1.4.1.2 Test Requirements 4259A.9.1.4.2 Test for V2X UE Resource
Pre-emption 4260A.9.1.4.2.1 Test Purpose and Environment 4260A.9.1.4.2.2
Test Requirements 4261A.9.1.4.3 Test for V2X UE Resource Re-evaluation
4262A.9.1.4.3.1 Test Purpose and Environment 4262A.9.1.4.3.2 Test
Requirements 4265A.9.1.4.4 Test for V2X UE Autonomous Resource
Selection/Reselection with Periodic Sensing 4265A.9.1.4.4.1 Test Purpose
and Environment 4265A.9.1.4.4.2 Test Requirements 4267A.9.1.4.5 Test for
V2X UE Autonomous Resource Selection/Reselection with Contiguous Sensing
4267A.9.1.4.5.1 Test Purpose and Environment 4267A.9.1.4.5.2 Test
Requirements 4269A.9.1.4.6 Test for V2X UE Autonomous Resource
Selection/Reselection in SL-DRX 4270A.9.1.4.6.1 Test Purpose and
Environment 4270A.9.1.4.6.2 Test Requirements 4272A.9.1.5 Test for
Congestion Control Measurement 4272A.9.1.5.1 Test Purpose and
Environment 4272A.9.1.5.2 Test Requirements 4275A.9.1.6 Test for
Interruption 4275A.9.1.6.1 Test for Interruption to WAN due to V2X
Sidelink Communication 4275A.9.1.6.1.1 Test Purpose and Environment
4275A.9.1.6.1.2 Test Requirements 4278A.9.1.6.2 Test for interruption to
WAN at transitions between active and non-active during SL-DRX in
asynchronous case 4278A.9.1.6.2.1 Test Purpose and Environment
4278A.9.1.6.2.2 Test Requirements 4279A.9.1.6.3 Test for Interruption at
NR Sidelink Diccovery Configuration 4280A.9.1.6.3.1 Test Purpose and
Environment 4280A.9.1.6.3.2 Test Requirements 4282A.9.1.7 Selection /
Reselection of relay UE 4282A.9.1.7.1 Test Purpose and Environment
4282A.9.1.7.2 Test Requirements 4286A.9A Tests for NR Sidelink
Measurements for Positioning 4287A.9A.1 Tests for NR Sidelink
Measurements for Positioning in FR1 4287A.9A.1.1 Measurement delay tests
4287A.9A.1.1.1 NR SL RSTD measurement reporting delay test case in FR1
SA 4287A.9A.1.1.1.1 Test Purpose and Environment 4287A.9A.1.1.1.2 Test
Requirements 4292A.9A.1.1.2 SL Rx-Tx measurement delay tests
4292A.9A.1.1.2.1 Test Purpose and Environment 4292A.9A.1.1.2.2 Test
Requirements 4295A.9A.1.1.3 NR SL AoA measurements reporting delay test
in FR1 SA 4296A.9A.1.1.3.1 Test Purpose and Environment 4296A.9A.1.1.3.2
Test Requirements 4299A.9A.1.1.4 NR SL RTOA measurements reporting delay
test in FR1 SA 4300A.9A.1.1.4.1 Test Purpose and Environment
4300A.9A.1.1.4.2 Test Requirements 4303A.9A.1.1.5 NR SL PRS-RSRP
measurement reporting delay test case in FR1 SA 4304A.9A.1.1.5.1 Test
Purpose and Environment 4304A.9A.1.1.5.2 Test Requirements
4304A.9A.1.1.6 NR SL PRS-RSRPP measurement reporting delay test case in
FR1 SA 4304A.9A.1.1.6.1 Test Purpose and Environment 4304A.9A.1.1.6.2
Test Requirements 4304A.9A.1.2 Measurement Accuracy Tests 4305A.9A.1.2.1
NR SL RSTD measurement accuracy test case in FR1 SA 4305A.9A.1.2.1.1
Test Purpose and Environment 4305A.9A.1.2.1.2 Test Requirements
4308A.9A.1.2.2 SL Rx-Tx measurement accuracy test case in FR1
4309A.9A.1.2.2.1 Test Purpose and Environment 4309A.9A.1.2.2.2 Test
Requirements 4312A.9A.1.2.3 NR SL PRS-RSRP measurement accuracy test
case in FR1 SA 4312A.9A.1.2.3.1 Test Purpose and Environment
4312A.9A.1.2.3.2 Test Requirements 4313A.9A.1.2.4 NR SL PRS-RSRPP
measurement accuracy test case in FR1 SA 4313A.9A.1.2.4.1 Test Purpose
and Environment 4313A.9A.1.2.4.2 Test Requirements 4313A.10 EN-DC Tests
with NR PSCell under CCA and Other NR Cells in FR1 4318A.10.1
RRC\_CONNECTED state mobility 4318A.10.1.1 RRC connection mobility
control 4318A.10.1.1.1 Random Access 4318A.10.1.1.1.1 4-step RA type
contention-based random access for NR PSCell with CCA 4318A.10.1.1.1.1.1
Test Purpose and Environment 4318A.10.1.1.1.1.2 Test Requirements
4319A.10.1.1.1.1.2.1 Random Access Preamble Transmission
4320A.10.1.1.1.1.2.2 Random Access Response Reception
4320A.10.1.1.1.1.2.3 No Random Access Response Reception
4320A.10.1.1.1.1.2.4 Receiving an UL grant for msg3 retransmission
4321A.10.1.1.1.1.2.5 Contention Resolution Timer expiry 4321A.10.1.1.1.2
4-step RA type non-contention based random access for NR PSCell with CCA
4321A.10.1.1.1.2.1 Test Purpose and Environment 4321A.10.1.1.1.2.2 Test
Requirements 4322A.10.1.1.1.2.2.1 SSB-based Random Access Preamble
Transmission 4323A.10.1.1.1.2.2.2 Random Access Response Reception
4323A.10.1.1.1.2.2.3 No Random Access Response Reception
4323A.10.1.1.1.3 2-step RA type contention-based random access for NR
PSCell with CCA 4324A.10.1.1.1.3.1 Test Purpose and Environment
4324A.10.1.1.1.3.2 Test Requirements 4325A.10.1.1.1.3.2.1 MsgA
Transmission 4326A.10.1.1.1.3.2.2 MsgB Reception 4326A.10.1.1.1.3.2.3 No
MsgB Reception 4326A.10.1.1.1.4 2-step RA type non-contention based
random access for NR PSCell with CCA 4327A.10.1.1.1.4.1 Test Purpose and
Environment 4327A.10.1.1.1.4.2 Test Requirements 4328A.10.1.1.1.4.2.1
MsgA Transmission 4329A.10.1.1.1.4.2.2 MsgB Reception
4329A.10.1.1.1.4.2.3 No MsgB Reception 4329**A.10.1.2** **Handover with
PSCell from EN-DC to EN-DC with known target PSCell using CCA**
4330A.10.1.2.1 Test Purpose and Environment 4330A.**10.1**.2.2 Test
Requirements 4334A.10.2 Timing 4335A.10.2.1 UE transmit timing
4335A.10.2.1.1 UE Transmit Timing Test with PSCell under DL CCA
4335A.10.2.1.1.1 Test Purpose and environment 4335A.10.2.1.1.2 Test
requirements 4337A.10.2.2 UE timing advance 4338A.10.2.2.1 UE Timing
Advance Adjustment Accuracy with PSCell under DL CCA 4338A.10.2.2.1.1
Test Purpose and Environment 4338A.10.2.2.1.2 Test Parameters
4338A.10.2.2.1.3 Test Requirements 4340A.10.3 Signalling characteristics
4340A.10.3.1 Radio link monitoring 4340A.10.3.1.1 Introduction
4340A.10.3.1.2 Radio link monitoring out-of-sync test for PSCell
configured with SSB-based RLM RS in non-DRX mode 4341A.10.3.1.2.1 Test
purpose and environment 4341A.10.3.1.2.2 Test requirements
4343A.10.3.1.3 Radio link monitoring in-sync test for PSCell configured
with SSB-based RLM RS in non-DRX mode 4344A.10.3.1.3.1 Test purpose and
environment 4344A.10.3.1.3.2 Test requirements 4346A.10.3.1.4 Void
4346A.10.3.1.4.1 Void 4346A.10.3.1.4.2 Void 4346A.10.3.1.5 Void
4347A.10.3.1.5.1 Void 4347A.10.3.1.5.2 Void 4347A.10.3.2 Void
4347A.10.3.3 SCell activation and deactivation delay 4347A.10.3.3.1
SCell Activation and Deactivation of known NR SCell with NR PSCell and
NR SCell under CCA, 160 ms SCell measurement cycle 4347A.10.3.3.1.1 Test
Purpose and Environment 4347A.10.3.3.1.2 Test Requirements
4350A.10.3.3.2 SCell Activation and Deactivation of known NR SCell with
NR PSCell and NR SCell under CCA, 640 ms SCell measurement cycle
4350A.10.3.3.2.1 Test Purpose and Environment 4350A.10.3.3.2.2 Test
Requirements 4351A.10.3.3.3 SCell Activation and Deactivation of unknown
NR SCell with NR PSCell and NR SCell under CCA 4351A.10.3.3.3.1 Test
Purpose and Environment 4351A.10.3.3.3.2 Test Requirements 4351A.10.3.4
Beam failure detection and link recovery procedures 4352A.10.3.4.1 EN-DC
Beam Failure Detection and Link Recovery Test for FR1 PSCell configured
with SSB-based BFD and LR in non-DRX mode 4352A.10.3.4.1.1 Test Purpose
and Environment 4352A.10.3.4.1.2 Test Requirements 4355A.10.3.4.2 EN-DC
Beam Failure Detection and Link Recovery Test for FR1 PSCell configured
with SSB-based BFD and LR in DRX mode 4355A.10.3.4.2.1 Test Purpose and
Environment 4355A.10.3.4.2.2 Test Requirements 4358A.10.3.5 Active BWP
switching 4359A.10.3.5.1 UL active BWP switch delay with consistent UL
LBT failure on PSCell subject to UL CCA in EN-DC 4359A.10.3.5.1.2 Test
Requirements 4361A.10.3.5.2 DCI-based and Timer-based Active BWP Switch
4362A.10.3.5.2.1 E-UTRAN -- NR PSCell FR1 DL active BWP switch in
non-DRX in synchronous EN-DC 4362A.10.3.5.2.2 E-UTRAN -- NR PSCell FR1
DL active BWP switch with FR1 SCell in non-DRX in synchronous EN-DC
4365A.10.3.5.3 RRC-based Active BWP Switch 4369A.10.3.5.3.1 E-UTRAN --
NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC
4369A.10.3.6 PSCell addition and release delay 4371A.10.3.6.1 Addition
and Release Delay of known NR PSCell on the carrier under CCA
4371A.10.3.6.1.1 Test purpose and environment 4371A.10.3.6.1.2 Test
Requirements 4374A.10.3.7 Void 4374A.10.4 Measurement procedure
4374A.10.4.1 Intra-frequency measurements 4375A.10.4.1.1 Event-triggered
reporting tests on PSCC without gaps under non-DRX 4375A.10.4.1.1.1 Test
purpose and environment 4375A.10.4.1.1.2 Test parameters
4375A.10.4.1.1.3 Test Requirements 4377A.10.4.1.2 Void 4377A.10.4.1.3
Void 4377A.10.4.1.4 Event-triggered reporting tests on PSCC with per-UE
gaps under DRX 4377A.10.4.1.4.1 Test purpose and environment
4377A.10.4.1.4.2 Test parameters 4377A.10.4.1.4.3 Test Requirements
4380A.10.4.1.5 Void 4380A.10.4.1.6 Void 4380A.10.4.1.7 Void
4380A.10.4.1.8 Void 4380A.10.4.1.9 Void 4380A.10.4.1.10 Void
4380A.10.4.1.11 Void 4380A.10.4.1.12 Void 4380A.10.4.2 Inter-frequency
measurements 4380A.10.4.2.1 Void 4380A.10.4.2.2 Void 4380A.10.4.2.3
EN-DC event triggered reporting tests for FR1 with CCA cell without SSB
time index detection when DRX is not used 4381A.10.4.2.3.1 Test Purpose
and Environment 4381A.10.4.2.3.2 Test Requirements 4383A.10.4.2.4 EN-DC
event triggered reporting tests for FR1 cell with CCA without SSB time
index detection when DRX is used 4383A.10.4.2.4.1 Test Purpose and
Environment 4383A.10.4.2.4.2 Test Requirements 4386A.10.4.2.5 EN-DC
event triggered reporting tests for FR1 cell with CCA with SSB time
index detection when DRX is not used 4387A.10.4.2.5.1 Test Purpose and
Environment 4387A.10.4.2.5.2 Test Requirements 4389A.10.4.2.6 EN-DC
event triggered reporting tests for FR1 cell with CCA with SSB time
index detection when DRX is used 4389A.10.4.2.6.1 Test Purpose and
Environment 4389A.10.4.2.6.2 Test Requirements 4392A.10.4.2.7 EN-DC
event triggered reporting tests for FR1 cell without SSB time index
detection when DRX is not used 4393A.10.4.2.7.1 Test Purpose and
Environment 4393A.10.4.2.7.2 Test Requirements 4396A.10.4.2.8 EN-DC
event triggered reporting tests for FR1 cell without SSB time index
detection when DRX is used 4396A.10.4.2.8.1 Test Purpose and Environment
4396A.10.4.2.8.2 Test Requirements 4400A.10.4.2.9 EN-DC event triggered
reporting tests for FR1 cell with SSB time index detection when DRX is
not used 4401A.10.4.2.9.1 Test Purpose and Environment 4401A.10.4.2.9.2
Test Requirements 4404A.10.4.2.10 EN-DC event triggered reporting tests
for FR1 cell with SSB time index detection when DRX is used
4404A.10.4.2.10.1 Test Purpose and Environment 4404A.10.4.2.10.2 Test
Requirements 4408A.10.4.3 L1-RSRP measurements for beam reporting
4409A.10.4.3.1 SSB based L1-RSRP measurement on PSCC when DRX is not
used 4409A.10.4.3.1.1 Test Purpose and Environment 4409A.10.4.3.1.2 Test
parameters 4409A.10.4.3.1.3 Test Requirements 4410A.10.4.3.2 SSB based
L1-RSRP measurement on PSCC when DRX is used 4411A.10.4.3.2.1 Test
Purpose and Environment 4411A.10.4.3.2.2 Test parameters
4411A.10.4.3.2.3 Test Requirements 4412A.10.4.3.3 SSB based L1-RSRP
measurement on SCC when DRX is not used 4413A.10.4.3.3.1 Test Purpose
and Environment 4413A.10.4.3.3.2 Test parameters 4413A.10.4.3.3.3 Test
Requirements 4414A.10.4.3.4 SSB based L1-RSRP measurement on SCC when
DRX is used 4415A.10.4.3.4.1 Test Purpose and Environment
4415A.10.4.3.4.2 Test parameters 4415A.10.4.3.4.3 Test Requirements
4416A.10.4.4 E-UTRAN−NR inter-RAT measurements on NR carrier frequency
under CCA 4417A.10.4.4.1 E-UTRA-NR inter-RAT event triggered reporting
tests for FR1 without SSB time index detection when DRX is not used
4417A.10.4.4.1.1 Test Purpose and Environment 4417A.10.4.4.1.2 Test
Requirements 4420A.10.4.4.2 E-UTRA-NR inter-RAT event triggered
reporting tests for FR1 without SSB time index detection when DRX is
used 4421A.10.4.4.2.1 Test Purpose and Environment 4421A.10.4.4.2.2 Test
Requirements 4424A.10.4.4.3 NR Inter-RAT event triggered reporting tests
for FR1 with SSB time index detection when DRX is not used
4425A.10.4.4.3.1 Test Purpose and Environment 4425A.10.4.4.3.2 Test
Requirements 4428A.10.4.4.4 NR Inter-RAT event triggered reporting tests
for FR1 with SSB time index detection when DRX is used 4428A.10.4.4.4.1
Test Purpose and Environment 4428A.10.4.4.4.2 Test Requirements
4432A.10.5 Measurement performance 4432A.10.5.1 SS-RSRP 4432A.10.5.1.1
Intra-frequency measurement accuracy on a CCA serving cell
4432A.10.5.1.1.1 Test Purpose and Environment 4432A.10.5.1.1.2 Test
parameters 4433A.10.5.1.1.3 Test Requirements 4434A.10.5.1.2
Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1
CCA target cell 4434A.10.5.1.2.1 Test Purpose and Environment
4434A.10.5.1.2.2 Test parameters 4435A.10.5.1.2.3 Test Requirements
4436A.10.5.2 SS-RSRQ 4436**A.10.5.2.1** **Intra-frequency measurement
accuracy with FR1 CCA serving cell and FR1 CCA target cell**
4436A.10.5.2.1.1 Test Purpose and Environment 4436A.10.5.2.1.2 Test
Parameters 4436A.10.5.2.1.3 Test Requirements 4438**A.10.5.2.2**
**Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1
CCA target cell** 4438A.10.5.2.2.1 Test Purpose and Environment
4438A.10.5.2.2.2 Test Parameters 4438A.10.5.2.2.3 Test Requirements
4439A.10.5.3 SS-SINR 4439A.10.5.3.1 Intra-frequency measurement accuracy
on PSCC 4439A.10.5.3.1.1 Test Purpose and Environment 4439A.10.5.3.1.2
Test Parameters 4439A.10.5.3.1.3 Test Requirements 4441A.10.5.3.2
Inter-frequency measurement accuracy on PSCC 4441A.10.5.3.2.1 Test
Purpose and Environment 4441A.10.5.3.2.2 Test Parameters
4441A.10.5.3.2.3 Test Requirements 4443A.10.5.3.3 Intra-frequency
measurement accuracy on SCC 4443A.10.5.3.3.1 Test Purpose and
Environment 4443A.10.5.3.3.2 Test Parameters 4443A.10.5.3.3.3 Test
Requirements 4445A.10.5.4 L1-RSRP measurement for beam reporting with
CCA serving cell 4445A.10.5.4.1 SSB based L1-RSRP measurement
4445A.10.5.4.1.1 Test Purpose and Environment 4445A.10.5.4.1.2 Test
parameters 4445A.10.5.4.1.3 Test Requirements 4447A.10.5.5 RSSI
4447A.10.5.5.1 RSSI measurement accuracy on PSCC with CCA
4447A.10.5.5.1.1 Test Purpose and Environment 4447A.10.5.5.1.2 Test
parameters 4447A.10.5.5.1.3 Test Requirements 4448A.10.5.5.2 RSSI
measurement accuracy on SCC with CCA 4449A.10.5.5.2.1 Test Purpose and
Environment 4449A.10.5.5.2.2 Test parameters 4449A.10.5.5.2.3 Test
Requirements 4450A.10.5.5.3 Inter-frequency RSSI measurement accuracy on
a carrier with CCA 4450A.10.5.5.3.1 Test Purpose and Environment
4450A.10.5.5.3.2 Test parameters 4451A.10.5.5.3.3 Test Requirements
4452A.10.5.6 Channel occupancy 4452A.10.5.6.1 Channel occupancy
measurement accuracy on PSCC with CCA 4452A.10.5.6.1.1 Test Purpose and
Environment 4452A.10.5.6.1.2 Test parameters 4452A.10.5.6.1.3 Test
Requirements 4454A.10.5.6.2 Channel occupancy measurement accuracy on
SCC with CCA 4454A.10.5.6.2.1 Test Purpose and Environment
4454A.10.5.6.2.2 Test parameters 4454A.10.5.6.2.3 Test Requirements
4456A.10.5.6.3 Inter-frequency channel occupancy measurement accuracy on
a carrier with CCA 4456A.10.5.6.3.1 Test Purpose and Environment
4456A.10.5.6.3.2 Test parameters 4456A.10.5.6.3.3 Test Requirements
4458A.11 NR Standalone Tests with NR PCell under CCA and Other NR Cells
in FR1 4460A.11.1 RRC\_IDLE state mobility 4460A.11.1.1 Cell
re-selection with both source and target NR carrier frequencies under
CCA 4460A.11.1.1.1 Cell reselection to FR1 intra-frequency NR cells when
subject to CCA on the serving and target cell 4460A.11.1.1.1.1 Test
Purpose and Environment 4460A.11.1.1.1.2 Test Parameters
4460A.11.1.1.1.3 Test Requirements 4462A.11.1.1.2 Cell reselection to
FR1 inter-frequency NR case when subject to CCA on the serving and
target cell 4463A.11.1.1.2.1 Test Purpose and Environment
4463A.11.1.1.2.2 Test Parameters 4463A.11.1.1.2.3 Test Requirements
4465A.11.1.2 Cell re-selection to NR with source NR carrier frequency
under CCA 4465A.11.1.2.1 Cell reselection to FR1 inter-frequency NR case
when serving cell is subject to CCA 4465A.11.1.2.1.1 Test Purpose and
Environment 4465A.11.1.2.1.2 Test Parameters 4466A.11.1.2.1.3 Test
Requirements 4468A.11.1.3 Cell re-selection from NR carrier with target
NR carrier frequency under CCA 4469A.11.1.3.1 Cell reselection to FR1
inter-frequency NR case when target cell is subject to CCA
4469A.11.1.3.1.1 Test Purpose and Environment 4469A.11.1.3.1.2 Test
Parameters 4469A.11.1.3.1.3 Test Requirements 4472A.11.1.4 Inter-RAT
cell re-selection to E-UTRAN with source NR carrier frequency under CCA
4473A.11.1.4.1 Cell reselection to higher priority E-UTRAN when serving
cell is subject to CCA 4473A.11.1.4.1.1 Test Purpose and Environment
4473A.11.1.4.1.2 Test Parameters 4473A.11.1.4.1.3 Test Requirements
4476A.11.1.4.2 Cell reselection to lower priority E-UTRAN when serving
cell is subject to CCA 4476A.11.1.4.2.1 Test Purpose and Environment
4476A.11.1.4.2.2 Test Requirements 4478A.11.2 RRC\_CONNECTED state
mobility 4479A.11.2.1 Handover 4479A.11.2.1.1 Intra-frequency handover
from FR1 carrier under CCA to FR1 carrier under CCA; known target cell
4479A.11.2.1.1.1 Test Purpose and Environment 4479A.11.2.1.1.2 Test
Parameters 4479A.11.2.1.1.3 Test Requirements 4481A.11.2.1.2
Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under
CCA; unknown target cell 4482A.11.2.1.2.1 Test Purpose and Environment
4482A.11.2.1.2.2 Test Parameters 4482A.11.2.1.2.3 Test Requirements
4484A.11.2.1.3 Inter-frequency handover from FR1 carrier under CCA to
FR1 carrier under CCA; unknown target cell 4484A.11.2.1.3.1 Test Purpose
and Environment 4484A.11.2.1.3.2 Test Parameters 4484A.11.2.1.3.3 Test
Requirements 4486A.11.2.1.4 Inter-frequency handover from FR1 carrier
under CCA to FR1; known target cell 4487A.11.2.1.4.1 Test Purpose and
Environment 4487A.11.2.1.4.2 Test Parameters 4487A.11.2.1.4.3 Test
Requirements 4490A.11.2.1.5 Inter-frequency handover from FR1 carrier
under CCA to FR1; unknown target cell 4490A.11.2.1.5.1 Test Purpose and
Environment 4490A.11.2.1.5.2 Test Parameters 4490A.11.2.1.5.3 Test
Requirements 4493A.11.2.1.6 Inter-frequency handover from FR1 to FR1
carrier under CCA; unknown target cell 4493A.11.2.1.6.1 Test Purpose and
Environment 4493A.11.2.1.6.2 Test Parameters 4493A.11.2.1.6.3 Test
Requirements 4496A.11.2.1.7 SA NR FR1 carrier under CCA - E-UTRAN
handover with known target cell 4496A.11.2.1.7.1 Test Purpose and
Environment 4496A.11.2.1.7.2 Test Requirements 4499A.11.2.1.8 SA NR FR1
carrier under CCA - E-UTRAN handover with unknown target cell
4500A.11.2.1.8.1 Test Purpose and Environment 4500A.11.2.1.8.2 Test
Requirements 4503A.11.2.1.9 Handover with PSCell from NR SA to EN-DC
with known target PSCell using CCA 4503A.11.2.1.9.1 Test Purpose and
Environment 4503A.11.2.1.9.2 Test Requirements 4509A.11.2.2 RRC
connection mobility control 4510A.11.2.2.1 RRC re-establishment
4510A.11.2.2.1.1 Intra-frequency RRC Re-establishment with CCA in FR1
4510A.11.2.2.1.2 Inter-frequency RRC Re-establishment with CCA in FR1
4513A.11.2.2.1.4 Inter-frequency RRC Re-establishment from NR FR1
carrier without CCA to NR FR1 carrier under CCA 4519A.11.2.2.2 Random
Access 4522A.11.2.2.2.1 4-step RA type contention-based random access
for NR PCell with CCA 4522A.11.2.2.2.1.1 Test Purpose and Environment
4522A.11.2.2.2.1.2 Test Requirements 4523A.11.2.2.2.1.2.1 Random Access
Preamble Transmission 4523A.11.2.2.2.1.2.2 Random Access Response
Reception 4524A.11.2.2.2.1.2.3 No Random Access Response Reception
4524A.11.2.2.2.1.2.4 Receiving an UL grant for msg3 retransmission
4524A.11.2.2.2.1.2.5 Reception of an Incorrect Message over Temporary
C-RNTI 4524A.11.2.2.2.1.2.6 Reception of a Correct Message over
Temporary C-RNTI 4525A.11.2.2.2.1.2.7 Contention Resolution Timer expiry
4525A.11.2.2.2.2 4-step RA type non-contention based random access for
NR PSCell with CCA 4525A.11.2.2.2.2.1 Test Purpose and Environment
4525A.11.2.2.2.2.2 Test Requirements 4526A.11.2.2.2.2.2.1 SSB-based
Random Access Preamble Transmission 4526A.11.2.2.2.2.2.2 Random Access
Response Reception 4527A.11.2.2.2.2.2.3 No Random Access Response
Reception 4527A.11.2.2.2.3 2-step RA type contention-based random access
for NR PCell with CCA 4528A.11.2.2.2.3.1 Test Purpose and Environment
4528A.11.2.2.2.3.2 Test Requirements 4529A.11.2.2.2.3.2.1 MsgA
Transmission 4529A.11.2.2.2.3.2.2 MsgB Reception 4530A.11.2.2.2.3.2.3 No
MsgB Reception 4530A.11.2.2.2.4 2-step RA type non-contention-based
random access for NR PCell with CCA 4531A.11.2.2.2.4.1 Test Purpose and
Environment 4531A.11.2.2.2.4.2 Test Requirements 4532A.11.2.2.2.4.2.1
MsgA Transmission 4532A.11.2.2.2.4.2.2 MsgB Reception
4533A.11.2.2.2.4.2.3 No MsgB Reception 4533A.11.2.2.3 RRC connection
release with redirection 4534A.11.2.2.3.1 Redirection from NR FR1
carrier under CCA to NR FR1 carrier under CCA 4534A.11.2.2.3.2
Redirection from NR FR1 carrier without CCA to NR FR1 carrier with CCA
4536A.11.3 Timing 4539A.11.3.1 UE transmit timing 4539A.11.3.1.1 UE
Transmit Timing Test with PCell under DL CCA 4539A.11.3.1.1.1 Test
Purpose and environment 4539A.11.3.1.1.2 Test requirements 4541A.11.3.2
UE timing advance 4542A.11.3.2.1 UE Timing Advance Adjustment Accuracy
with PCell under DL CCA 4542A.11.3.2.1.1 Test Purpose and Environment
4542A.11.3.2.1.2 Test Parameters 4542A.11.3.2.1.3 Test Requirements
4544A.11.4 Signalling characteristics 4544A.11.4.1 Radio link monitoring
4544A.11.4.1.1 Introduction 4544A.11.4.1.2 Radio link monitoring
out-of-sync test for PCell configured with SSB-based RLM RS in non-DRX
mode 4545A.11.4.1.2.1 Test purpose and environment 4545A.11.4.1.2.2 Test
requirements 4547A.11.4.1.3 Radio link monitoring in-sync test for PCell
configured with SSB-based RLM RS in non-DRX mode 4548A.11.4.1.3.1 Test
purpose and environment 4548A.11.4.1.3.2 Test requirements
4551A.11.4.1.4 Void 4551A.11.4.1.4.1 Void 4551A.11.4.1.4.2 Void
4551A.11.4.1.5 Void 4551A.11.4.1.5.1 Void 4551A.11.4.1.5.2 Void
4551A.11.4.2 Void 4551A.11.4.3 SCell activation and deactivation delay
4551A.11.4.3.1 SCell Activation and Deactivation of known SCell with
PCell and SCell under CCA, 160 ms SCell measurement cycle
4551A.11.4.3.1.1 Test Purpose and Environment 4551A.11.4.3.1.2 Test
Requirements 4554A.11.4.3.2 SCell Activation and Deactivation of known
SCell with PCell and SCell under CCA, 640 ms SCell measurement cycle
4554A.11.4.3.2.1 Test Purpose and Environment 4554A.11.4.3.2.2 Test
Requirements 4555A.11.4.3.3 SCell Activation and Deactivation of unknown
SCell with PCell and SCell under CCA 4555A.11.4.3.3.1 Test Purpose and
Environment 4555A.11.4.3.3.2 Test Requirements 4555A.11.4.4 Beam failure
detection and link recovery procedures 4556A.11.4.4.1 Beam Failure
Detection and Link Recovery Test for FR1 PCell configured with SSB-based
BFD and LR in non-DRX mode 4556A.11.4.4.1.1 Test Purpose and Environment
4556A.11.4.4.1.2 Test Requirements 4559A.11.4.4.2 Beam Failure Detection
and Link Recovery Test for FR1 PCell configured with SSB-based BFD and
LR in DRX mode 4560A.11.4.4.2.1 Test Purpose and Environment
4560A.11.4.4.2.2 Test Requirements 4563A.11.4.5 Active BWP switching
4563A.11.4.5.1 UL active BWP switch delay with consistent UL LBT failure
on PCell subject to UL CCA 4563A.11.4.5.1.1 Test Purpose and Environment
4563A.11.4.5.1.2 Test Requirements 4566A.11.4.5.2 DCI-based and
Timer-based Active BWP Switch 4566A.11.4.5.2.1 NR FR1- NR FR1 DL active
BWP switch of PCell with non-DRX in SA 4566A.11.4.5.2.2 NR FR1 DL active
BWP switch with non-DRX in SA 4569A.11.4.5.3 RRC-based Active BWP Switch
4572A.11.4.5.3.1 NR FR1 DL active BWP switch of Cell with non-DRX in SA
4572A.11.4.6 Void 4574A.11.5 Measurement procedure 4574A.11.5.1
Intra-frequency measurements 4574A.11.5.1.1 Event-triggered reporting
tests on PCC without gaps under non-DRX 4574A.11.5.1.1.1 Test purpose
and environment 4574A.11.5.1.1.2 Test parameters 4574A.11.5.1.1.3 Test
Requirements 4576A.11.5.1.2 Event-triggered reporting tests on PCC
without gaps under DRX 4576A.11.5.1.2.1 Test purpose and environment
4576A.11.5.1.2.2 Test parameters 4576A.11.5.1.2.3 Test Requirements
4578A.11.5.1.3 Void 4579A.11.5.1.4 Void 4579A.11.5.1.5 Void
4579A.11.5.1.6 Void 4579A.11.5.1.7 Void 4579A.11.5.1.8 Void
4579A.11.5.1.9 Void 4579A.11.5.1.10 Void 4579A.11.5.1.11 Void
4579A.11.5.1.12 Void 4579A.11.5.2 Inter-frequency measurements
4579A.11.5.2.1 Void 4579A.11.5.2.2 Void 4579A.11.5.2.3 Event triggered
reporting tests for FR1 with CCA without SSB time index detection when
DRX is not used 4579A.11.5.2.3.1 Test Purpose and Environment
4579A.11.5.2.3.2 Test Requirements 4582A.11.5.2.4 Event triggered
reporting tests for FR1 with CCA without SSB time index detection when
DRX is used 4582A.11.5.2.4.1 Test Purpose and Environment
4582A.11.5.2.4.2 Test Requirements 4585A.11.5.2.5 Event triggered
reporting tests for FR1 with CCA with SSB time index detection when DRX
is not used 4585A.11.5.2.5.1 Test Purpose and Environment
4585A.11.5.2.5.2 Test Requirements 4588A.11.5.2.6 Event triggered
reporting tests for FR1 with CCA with SSB time index detection when DRX
is used 4588A.11.5.2.6.1 Test Purpose and Environment 4588A.11.5.2.6.2
Test Requirements 4591A.11.5.2.7 Event triggered reporting tests for FR1
without SSB time index detection when DRX is not used 4592A.11.5.2.7.1
Test Purpose and Environment 4592A.11.5.2.7.2 Test Requirements
4594A.11.5.2.8 Event triggered reporting tests for FR1 without SSB time
index detection when DRX is used 4595A.11.5.2.8.1 Test Purpose and
Environment 4595A.11.5.2.8.2 Test Requirements 4598A.11.5.2.9 Event
triggered reporting tests for FR1 with SSB time index detection when DRX
is not used 4598A.11.5.2.9.1 Test Purpose and Environment
4598A.11.5.2.9.2 Test Requirements 4601A.11.5.2.10 Event triggered
reporting tests for FR1 with SSB time index detection when DRX is used
4601A.11.5.2.10.1 Test Purpose and Environment 4601A.11.5.2.10.2 Test
Requirements 4605A.11.5.3 Inter-RAT E-UTRAN measurements 4605A.11.5.3.1
SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1
4605A.11.5.3.1.1 Test Purpose and Environment 4605A.11.5.3.1.2 Test
Requirements 4608A.11.5.3.2 SA NR - E-UTRAN event-triggered reporting in
DRX in FR1 4608A.11.5.3.2.1 Test Purpose and Environment
4608A.11.5.3.2.2 Test Requirements 4612A.11.5.4 L1-RSRP measurements for
beam reporting 4612A.11.5.4.1 SSB based L1-RSRP measurement when DRX is
not used 4612A.11.5.4.1.1 Test Purpose and Environment 4612A.11.5.4.1.2
Test parameters 4612A.11.5.4.1.3 Test Requirements 4614A.11.5.4.2 SSB
based L1-RSRP measurement when DRX is used 4614A.11.5.4.2.1 Test Purpose
and Environment 4614A.11.5.4.2.2 Test parameters 4614A.11.5.4.2.3 Test
Requirements 4616A.11.5.4.3 SSB based L1-RSRP measurement on SCC when
DRX is not used 4616A.11.5.4.3.1 Test Purpose and Environment
4616A.11.5.4.3.2 Test parameters 4617A.11.5.4.3.3 Test Requirements
4618A.11.5.4.4 SSB based L1-RSRP measurement on SCC when DRX is used
4618A.11.5.4.4.1 Test Purpose and Environment 4618A.11.5.4.4.2 Test
parameters 4619A.11.5.4.4.3 Test Requirements 4620A.11.6 Measurement
performance 4620A.11.6.1 SS-RSRP 4620A.11.6.1.1 Intra-frequency
measurement accuracy on a carrier frequency with CCA 4620A.11.6.1.1.1
Test Purpose and Environment 4620A.11.6.1.1.2 Test parameters
4621A.11.6.1.1.3 Test Requirements 4622A.11.6.1.2 Intra-frequency
measurement accuracy on SCC on a carrier frequency with CCA
4622A.11.6.1.2.1 Test Purpose and Environment 4622A.11.6.1.2.2 Test
parameters 4622A.11.6.1.2.3 Test Requirements 4624A.11.6.2 SS-RSRQ
4624A.11.6.2.1 Intra-frequency measurement accuracy 4624A.11.6.2.1.1
Test Purpose and Environment 4624A.11.6.2.1.2 Test Parameters
4624A.11.6.2.1.3 Test Requirements 4626A.11.6.2.2 Inter-frequency
measurement accuracy 4626A.11.6.2.2.1 Test Purpose and Environment
4626A.11.6.2.2.2 Test Parameters 4626A.11.6.2.2.3 Test Requirements
4628A.11.6.2.3 Intra-frequency measurement accuracy on SCC
4628A.11.6.2.3.1 Test Purpose and Environment 4628A.11.6.2.3.2 Test
Parameters 4628A.11.6.2.3.3 Test Requirements 4630A.11.6.2.4
Inter-frequency measurement accuracy 4630A.11.6.2.4.1 Test Purpose and
Environment 4630A.11.6.2.4.2 Test Parameters 4630A.11.6.2.4.3 Test
Requirements 4635A.11.6.3 SS-SINR 4635A.11.6.3.1 Intra-frequency
measurement accuracy 4635A.11.6.3.1.1 Test Purpose and Environment
4635A.11.6.3.1.2 Test Parameters 4635A.11.6.3.1.3 Test Requirements
4636A.11.6.3.2 Inter-frequency measurement accuracy 4637A.11.6.3.2.1
Test Purpose and Environment 4637A.11.6.3.2.2 Test Parameters
4637A.11.6.3.2.3 Test Requirements 4638A.11.6.3.3 Intra-frequency
measurement accuracy on SCC 4638A.11.6.3.3.1 Test Purpose and
Environment 4638A.11.6.3.3.2 Test Parameters 4638A.11.6.3.3.3 Test
Requirements 4640A.11.6.3.4 Inter-frequency measurement accuracy
4640A.11.6.3.4.1 Test Purpose and Environment 4640A.11.6.3.4.2 Test
Parameters 4640A.11.6.3.4.3 Test Requirements 4644A.11.6.4 L1-RSRP
measurement for beam reporting with CCA serving cell 4645A.11.6.4.1 SSB
based L1-RSRP measurement 4645A.11.6.4.1.1 Test Purpose and Environment
4645A.11.6.4.1.2 Test parameters 4645A.11.6.4.1.3 Test Requirements
4646A.11.6.5 RSSI 4646A.11.6.5.1 Intra-frequency RSSI measurement
accuracy on PCC with CCA 4646A.11.6.5.1.1 Test Purpose and Environment
4646A.11.6.5.1.2 Test parameters 4646A.11.6.5.1.3 Test Requirements
4648A.11.6.5.2 Intra-frequency RSSI measurement accuracy on SCC with CCA
4648A.11.6.5.2.1 Test Purpose and Environment 4648A.11.6.5.2.2 Test
parameters 4648A.11.6.5.2.3 Test Requirements 4650A.11.6.5.3
Inter-frequency RSSI measurement accuracy on a carrier with CCA
4650A.11.6.5.3.1 Test Purpose and Environment 4650A.11.6.5.3.2 Test
parameters 4650A.11.6.5.3.3 Test Requirements 4651A.11.6.6 Channel
occupancy 4652A.11.6.6.1 Intra-frequency channel occupancy measurement
accuracy on PCC with CCA 4652A.11.6.6.1.1 Test Purpose and Environment
4652A.11.6.6.1.2 Test parameters 4652A.11.6.6.1.3 Test Requirements
4653A.11.6.6.2 Intra-frequency channel occupancy measurement accuracy on
SCC with CCA 4653A.11.6.6.2.1 Test Purpose and Environment
4653A.11.6.6.2.2 Test parameters 4653A.11.6.6.2.3 Test Requirements
4655A.11.6.6.3 Inter-frequency channel occupancy measurement accuracy on
a carrier with CCA 4655A.11.6.6.3.1 Test Purpose and Environment
4655A.11.6.6.3.2 Test parameters 4655A.11.6.6.3.3 Test Requirements
4657A.11.6.7 E-UTRAN RSRP 4657A.11.6.8 E-UTRAN RSRQ 4657A.11.6.9 E-UTRAN
SINR 4657A.12 E-UTRA Standalone Tests with at Least One NR Cell under
CCA 4657A.12.1 RRC\_IDLE state mobility 4657A.12.1.1 Inter-RAT cell
re-selection to NR on a carrier frequency with CCA 4657A.12.1.1.1 E-UTRA
Cell reselection to higher priority NR target Cell in FR1 when target
cell is subject to CCA 4657A.12.1.1.1.1 Test Purpose and Environment
4657A.12.1.1.1.2 Test Requirements 4660A.12.2 RRC\_CONNECTED state
mobility 4661A.12.2.1 Handover 4661A.12.2.1.1 E-UTRAN - NR with CCA
handover 4661A.12.2.1.1.1 Test Purpose and Environment 4661A.12.2.1.1.2
Test Requirements 4664A.12.3 Void 4665A.12.4 Measurement procedure
4665A.12.4.1 E-UTRAN−NR inter-RAT SFTD measurements 4665A.12.4.1.1
E-UTRA -- NR Inter-RAT SFTD Measurement Delay with NR under CCA in
non-DRX 4665A.12.4.1.1.1 Test Purpose and Environment 4665A.12.4.1.1.2
Test Requirements 4667A.12.4.2 E-UTRAN−NR inter-RAT measurements on NR
carrier frequency under CCA 4667A.12.4.2.1 E-UTRA-NR inter-RAT event
triggered reporting tests for FR1 without SSB time index detection when
DRX is not used 4667A.12.4.2.1.1 Test Purpose and Environment
4667A.12.4.2.1.2 Test Requirements 4671A.12.4.2.2 E-UTRA-NR inter-RAT
event triggered reporting tests for FR1 without SSB time index detection
when DRX is used 4671A.12.4.2.2.1 Test Purpose and Environment
4671A.12.4.2.2.2 Test Requirements 4674A.12.4.2.3 NR Inter-RAT event
triggered reporting tests for FR1 with SSB time index detection when DRX
is not used 4674A.12.4.2.3.1 Test Purpose and Environment
4674A.12.4.2.3.2 Test Requirements 4678A.12.4.2.4 NR Inter-RAT event
triggered reporting tests for FR1 with SSB time index detection when DRX
is used 4678A.12.4.2.4.1 Test Purpose and Environment 4678A.12.4.2.4.2
Test Requirements 4681A.12.4.2.5 Void 4682A.12.4.2.6 Void 4682A.12.5
Measurement performance 4682A.12.5.1 E-UTRAN−NR SFTD 4682A.12.5.1.1
Inter-RAT SFTD accuracy with NR target cell under CCA 4682A.12.5.1.1.1
Test Purpose 4682A.12.5.1.1.2 Test Environment 4682A.12.5.1.1.3 Test
Requirements 4684A.12.5.2 Void 4684A.12.5.3 Void 4684A.12.5.4 Void
4684A.12.5.5 Void 4685A.12.5.6 Void 4685A.13 NR Standalone Tests with NR
SCell under CCA and All Other NR Cells in FR1 4689A.13.1 Void
4689A.13.1.1 Void 4689A.13.1.2 Void 4689A.13.2 Signalling
characteristics 4689A.13.2.1 Void 4689A.13.2.2 SCell activation and
deactivation delay 4689A.13.2.2.1 SCell Activation and Deactivation of
known SCell under CCA, 160 ms SCell measurement cycle 4689A.13.2.2.1.1
Test Purpose and Environment 4689A.13.2.2.1.2 Test Requirements
4692A.13.2.2.2 SCell Activation and Deactivation of known SCell under
CCA, 640 ms SCell measurement cycle 4692A.13.2.2.2.1 Test Purpose and
Environment 4692A.13.2.2.2.2 Test Requirements 4693A.13.2.2.3 SCell
Activation and Deactivation of unknown SCell under CCA 4693A.13.2.2.3.1
Test Purpose and Environment 4693A.13.2.2.3.2 Test Requirements
4693A.13.2.3 Void 4694A.13.3 Measurement procedure 4694A.13.3.1
Intra-frequency measurements 4694A.13.3.1.1 Event-triggered reporting
tests on SCC without gaps under non-DRX 4694A.13.3.1.1.1 Test purpose
and environment 4694A.13.3.1.1.2 Test parameters 4694A.13.3.1.1.3 Test
Requirements 4697A.13.3.1.2 Event-triggered reporting tests on SCC
without gaps under DRX 4697A.13.3.1.2.1 Test purpose and environment
4697A.13.3.1.2.2 Test parameters 4697A.13.3.1.2.3 Test Requirements
4700A.13.3.1.3 Event-triggered reporting tests on SCC with per-UE gaps
under non-DRX 4700A.13.3.1.3.1 Test purpose and environment
4700A.13.3.1.3.2 Test parameters 4700A.13.3.1.3.3 Test Requirements
4703A.13.3.1.4 Event-triggered reporting tests on SCC with per-UE gaps
under DRX 4704A.13.3.1.4.1 Test purpose and environment 4704A.13.3.1.4.2
Test parameters 4704A.13.3.1.4.3 Test Requirements 4707A.13.3.1.5 Void
4707A.13.3.1.6 Void 4707A.13.3.2 Inter-frequency measurements
4707A.13.3.2.1 Void 4707A.13.3.2.2 Void 4707A.13.3.2.3 Event triggered
reporting tests for FR1 with CCA without SSB time index detection when
DRX is not used 4707A.13.3.2.3.1 Test Purpose and Environment
4707A.13.3.2.3.2 Test Requirements 4710A.13.3.2.4 Event triggered
reporting tests for FR1 with CCA without SSB time index detection when
DRX is used 4711A.13.3.2.4.1 Test Purpose and Environment
4711A.13.3.2.4.2 Test Requirements 4714A.13.3.2.5 Event triggered
reporting tests for FR1 with CCA with SSB time index detection when DRX
is not used 4714A.13.3.2.5.1 Test Purpose and Environment
4714A.13.3.2.5.2 Test Requirements 4717A.13.3.2.6 Event triggered
reporting tests for FR1 with CCA with SSB time index detection when DRX
is used 4717A.13.3.2.6.1 Test Purpose and Environment 4717A.13.3.2.6.2
Test Requirements 4721A.13.3.3 L1-RSRP measurements for beam reporting
4721A.13.3.3.1 SSB based L1-RSRP measurement when DRX is not used
4721A.13.3.3.1.1 Test Purpose and Environment 4721A.13.3.3.1.2 Test
parameters 4721A.13.3.3.1.3 Test Requirements 4723A.13.3.3.2 SSB based
L1-RSRP measurement when DRX is used 4724A.13.3.3.2.1 Test Purpose and
Environment 4724A.13.3.3.2.2 Test parameters 4724A.13.3.3.2.3 Test
Requirements 4726A.13.4 Measurement performance 4726A.13.4.1 SS-RSRP
4726A.13.4.1.1 Intra-frequency measurement accuracy on a carrier
frequency with CCA 4726A.13.4.1.1.1 Test Purpose and Environment
4726A.13.4.1.1.2 Test parameters 4726A.13.4.1.1.3 Test Requirements
4728A.13.4.2 SS-RSRQ 4728A.13.4.2.1 Intra-frequency measurement accuracy
on SCC 4728A.13.4.2.1.1 Test Purpose and Environment 4728A.13.4.2.1.2
Test Parameters 4728A.13.4.2.1.3 Test Requirements 4733A.13.4.3 SS-SINR
4733A.13.4.3.1 Intra-frequency measurement accuracy on SCC
4733A.13.4.3.1.1 Test Purpose and Environment 4733A.13.4.3.1.2 Test
Parameters 4733A.13.4.3.1.3 Test Requirements 4737A.13.4.4 L1-RSRP
measurement for beam reporting with CCA serving cell 4737A.13.4.4.1 SSB
based L1-RSRP measurement 4737A.13.4.4.1.1 Test Purpose and Environment
4737A.13.4.4.1.2 Test parameters 4738A.13.4.4.1.3 Test Requirements
4740A.13.4.5 RSSI 4740A.13.4.5.1 Intra-frequency RSSI measurement
accuracy on a carrier with CCA 4740A.13.4.5.1.1 Test Purpose and
Environment 4740A.13.4.5.1.2 Test parameters 4740A.13.4.5.1.3 Test
Requirements 4742A.13.4.5.2 Inter-frequency RSSI measurement accuracy on
a carrier with CCA 4742A.13.4.5.2.1 Test Purpose and Environment
4742A.13.4.5.2.2 Test parameters 4742A.13.4.5.2.3 Test Requirements
4744A.13.4.6 Channel occupancy 4744A.13.4.6.1 Intra-frequency channel
occupancy measurement accuracy on SCC with CCA 4744A.13.4.6.1.1 Test
Purpose and Environment 4744A.13.4.6.1.2 Test parameters
4744A.13.4.6.1.3 Test Requirements 4746A.13.4.6.2 Inter-frequency
channel occupancy measurement accuracy on a carrier with CCA
4746A.13.4.6.2.1 Test Purpose and Environment 4746A.13.4.6.2.2 Test
parameters 4746A.13.4.6.2.3 Test Requirements 4748A.14 NR standalone
tests for Satellite access 4748A.14.1 RRC\_IDLE state mobility
4748A.14.1.1 Cell reselection to FR1 intra-frequency NR case
4748A.14.1.1.1 Test Purpose and Environment 4748A.14.1.1.2 Test
Parameters 4748A.14.1.1.3 Test Requirements 4750A.14.1.2 Cell
reselection to FR1 intra-frequency NR cell for UE configured with the
feature for enhanced requirements 4750A.14.1.2.1 Test Purpose and
Environment 4750A.14.1.2.2 Test Parameters 4751A.14.1.2.3 Test
Requirements 4752A.14.1.3 Time-based measurement initiation to FR1
intra-frequency NR cell reselection 4753A.14.1.3.1 Test Purpose and
Environment 4753A.14.1.3.2 Test Parameters 4753A.14.1.3.3 Test
Requirements 4754A.14.1.4 Location-based measurement initiation to FR1
intra-frequency NR cell reselection 4754A.14.1.4.1 Test Purpose and
Environment 4755A.14.1.4.2 Test Parameters 4755A.14.1.4.3 Test
Requirements 4756A.14.1.5 Cell reselection to FR1 inter-frequency NR
case 4756A.14.1.5.1 Test Purpose and Environment 4756A.14.1.5.2 Test
Parameters 4757A.14.1.5.3 Test Requirements 4758A.14.1.6 Cell
re-selection to FR1 inter-frequency NR cell for UE configured with
feature for enhanced requirements 4759A.14.1.6.1 Test Purpose and
Environment 4759A.14.1.6.2 Test Parameters 4759A.14.1.6.3 Test
Requirements 4760A.14.1.7 Time-based measurement initiation to FR1
inter-frequency cell reselection 4761A.14.1.7.1 Test Purpose and
Environment 4761A.14.1.7.2 Test Parameters 4761A.14.1.7.3 Test
Requirements 4762A.14.1.8 Location-based measurement initiation to FR1
inter-frequency NR cell reselection 4763A.14.1.8.1 Test Purpose and
Environment 4763A.14.1.8.2 Test Parameters 4763A.14.1.8.3 Test
Requirements 4764A.14.1.9 Cell reselection to FR1 inter-frequency NR
case for UE fulfilling low mobility relaxed measurement criterion
4764A.14.1.9.1 Test Purpose and Environment 4764A.14.1.9.2 Test
Parameters 4765A.14.1.9.3 Test Requirements 4766A.14.1.10 Cell
reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell
edge relaxed measurement criterion 4767A.14.1.10.1 Test Purpose and
Environment 4767A.14.1.10.2 Test Parameters 4767A.14.1.10.3 Test
Requirements 4769A.14.1.11 Cell reselection to FR1 inter-RAT for NR NTN
carrier 4769**A.14.1.11.1** Test purpose and Environment
4769**A.14.1.11.2** Test parameters 4769**A.14.1.11.3** Test
requirements 4771A.14.1.12 Cell re-selection to FR1 inter-frequency NR
case with TN carrier 4772**A.14.1.12.1** Test purpose and Environment
4772**A.14.1.12.2** Test parameters 4772**A.14.1.12.3** Test
requirements 4773A.14.2 RRC\_CONNECTED state mobility 4774A.14.2.1
Handover 4774A.14.2.1.1 Intra-frequency SAN Handover from FR1 to FR1
4774A.14.2.1.1.1 Test Purpose and Environment 4774A.14.2.1.1.2 Test
Parameters 4774A.14.2.1.1.3 Test Requirements 4776A.14.2.1.2
Inter-frequency SAN Handover from FR1 to FR1 4776A.14.2.1.2.1 Test
Purpose and Environment 4776A.14.2.1.2.2 Test Parameters
4776A.14.2.1.2.3 Test Requirements 4778A.14.2.1.3 Intra-frequency SAN
time-based conditional Handover from FR1 to FR1 4778A.14.2.1.3.1 Test
Purpose and Environment 4778A.14.2.1.3.2 Test Parameters
4778A.14.2.1.3.3 Test Requirements 4780A.14.2.1.4 Inter-frequency SAN
time-based conditional Handover from FR1 to FR1 4780A.14.2.1.4.1 Test
Purpose and Environment 4780A.14.2.1.4.2 Test Parameters
4780A.14.2.1.4.3 Test Requirements 4782A.14.2.1.5 Intra-frequency SAN
distance-based conditional Handover from FR1 to FR1 4782A.14.2.1.5.1
Test Purpose and Environment 4782A.14.2.1.5.2 Test Parameters
4783A.14.2.1.5.3 Test Requirements 4784A.14.2.1.6 Inter-frequency SAN
distance-based conditional Handover from FR1 to FR1 4785A.14.2.1.6.1
Test Purpose and Environment 4785A.14.2.1.6.2 Test Parameters
4785A.14.2.1.6.3 Test Requirements 4787A.14.2.1.7 Intra-frequency
intra-satellite Handover from FR2-NTN to FR2-NTN 4787A.14.2.1.7.1 Test
Purpose and Environment 4787A.14.2.1.7.2 Test Parameters
4787A.14.2.1.7.3 Test Requirements 4789A.14.2.1.8 Intra-frequency SAN
Handover from FR1 to FR1 4789A.14.2.1.8.1 Test Purpose and Environment
4789A.14.2.1.8.2 Test Parameters 4790A.14.2.1.8.3 Test Requirements
4791A.14.2.1.9 Intra-frequency inter-satellite handover from FR2-NTN to
FR2-NTN 4792A.14.2.1.9.1 Test Purpose and Environment 4792A.14.2.1.9.2
Test Parameters 4792A.14.2.1.9.3 Test Requirements 4793A.14.2.2 RRC
Connection Mobility Control 4794A.14.2.2.1 SA: RRC Re-establishment for
SAN 4794A.14.2.2.1.1 Intra-frequency RRC Re-establishment in FR1
4794A.14.2.2.1.2 Inter-frequency RRC Re-establishment in FR1
4796A.14.2.2.2 Random Access 4798A.14.2.2.2.1 4-step RA type contention
based random access test in FR1 for NR standalone 4798A.14.2.2.2.1.1
Test Purpose and Environment 4798A.14.2.2.2.1.2 Test Requirements
4800A.14.2.2.2.2 4-step RA type non-contention based random access test
in FR1 for NR standalone 4801A.14.2.2.2.2.1 Test Purpose and Environment
4801A.14.2.2.2.2.2 Test Requirements 4803A.14.2.2.3 RRC Connection
Release with Redirection 4804A.14.2.2.3.1 Redirection from NR in FR1 to
NR in FR1 4804A.14.2.2.3.1.1 Test Purpose and Environment
4804A.14.2.2.3.1.2 Test Parameters 4804A.14.2.2.3.1.3 Test Requirements
4805A.14.2.2.4 RACH-based Hard Satellite switching with
re-synchronization from FR1 to FR1 4806A.14.2.2.4.1 Test Purpose and
Environment 4806A.14.2.2.4.2 Test Parameters 4806A.14.2.2.4.3 Test
Requirements 4808A.14.2.2.5 RACH-less Soft Satellite switching with
re-synchronization from FR1 to FR1 4808A.14.2.2.5.1 Test Purpose and
Environment 4808A.14.2.2.5.2 Test Parameters 4808A.14.2.2.5.3 Test
Requirements 4810A.14.2.3 Intra-frequency SAN time-based conditional
Handover without L3 measurement criteria from FR1 to FR1 4810A.14.2.3.1
Test Purpose and Environment 4810A.14.2.3.2 Test Parameters
4810A.14.2.3.3 Test Requirements 4812A.14.2.4 Inter-frequency SAN
time-based conditional Handover without L3 measurement criteria from FR1
to FR1 4812A.14.2.4.1 Test Purpose and Environment 4812A.14.2.4.2 Test
Parameters 4812A.14.2.4.3 Test Requirements 4814A.14.3 Timing for
Satellite Access 4814A.14.3.1 UE transmit timing for Satellite Access
4814A.14.3.1.1 NR UE Transmit Timing Test for FR1 4814A.14.3.1.1.1 Test
Purpose and environment 4814A.14.3.1.1.2 Test requirements
4816A.14.3.1.2 NR UE Transmit Timing Test for FR2-NTN 4817A.14.3.1.2.1
Test Purpose and environment 4817A.14.3.1.2.2 Test requirements
4819A.14.3.2 Timing advance for satellite access 4819A.14.3.2.1 SA FR1
timing advance adjustment accuracy 4819A.14.3.2.1.1 Test Purpose and
Environment 4819A.14.3.2.1.2 Test Parameters 4820A.14.3.2.1.3 Test
Requirements 4822A.14.3.2.3 SA FR2-NTN timing advance adjustment
accuracy 4822A.14.3.2.3.1 Test Purpose and Environment 4822A.14.3.2.3.2
Test Parameters 4822A.14.3.2.1.3 Test Requirements 4825A.14.4 Signalling
characteristics 4825A.14.4.1 Radio link Monitoring 4825A.14.4.1.1 Radio
Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with
SSB-based RLM RS in non-DRX mode 4825A.14.4.1.1.1 Test Purpose and
Environment 4825A.14.4.1.1.2 Test Requirements 4827A.14.4.1.2 Radio Link
Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM
RS in non-DRX mode 4828A.14.4.1.2.1 Test Purpose and Environment
4828A.14.4.1.2.2 Test Requirements 4830A.14.4.1.3 Radio Link Monitoring
Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in
DRX mode 4830A.14.4.1.3.1 Test Purpose and Environment 4830A.14.4.1.3.2
Test Requirements 4832A.14.4.1.4 Radio Link Monitoring In-sync Test for
FR1 SAN PCell configured with SSB-based RLM RS in DRX mode
4833A.14.4.1.4.1 Test Purpose and Environment 4833A.14.4.1.4.2 Test
Requirements 4835A.14.4.1.5 Radio Link Monitoring Out-of-sync Test for
FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode
4835A.14.4.1.5.1 Test Purpose and Environment 4835A.14.4.1.5.2 Test
Requirements 4838A.14.4.1.6 Radio Link Monitoring In-sync Test for FR1
SAN PCell configured with CSI-RS-based RLM in non-DRX mode
4838A.14.4.1.6.1 Test Purpose and Environment 4838A.14.4.1.6.2 Test
Requirements 4841A.14.4.1.7 Radio Link Monitoring Out-of-sync Test for
FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode
4841A.14.4.1.7.1 Test Purpose and Environment 4841A.14.4.1.7.2 Test
Requirements 4844A.14.4.1.8 Radio Link Monitoring In-sync Test for FR1
SAN PCell configured with CSI-RS-based RLM in DRX mode 4844A.14.4.1.8.1
Test Purpose and Environment 4844A.14.4.1.8.2 Test Requirements
4847A.14.4.1.9 Radio Link Monitoring Out-of-sync Test for FR2 SAN PCell
configured with SSB-based RLM RS in non-DRX mode 4847A.14.4.1.9.1 Test
Purpose and Environment 4847A.14.4.1.9.2 Test Requirements
4849A.14.4.1.10 Radio Link Monitoring In-sync Test for FR2 SAN PCell
configured with SSB-based RLM RS in non-DRX mode 4850A.14.4.1.10.1 Test
Purpose and Environment 4850A.14.4.1.10.2 Test Requirements 4852A.14.4.2
Beam Failure Detection and Link recovery procedures for satellite access
4853A.14.4.2.1 Beam Failure Detection and Link Recovery Test for FR1
PCell for satellite access configured with SSB-based BFD and LR in
non-DRX mode 4853A.14.4.2.1.1 Test Purpose and Environment
4853A.14.4.2.1.2 Test Requirements 4855A.14.4.2.2 Beam Failure Detection
and Link Recovery Test for FR1 PCell for satellite access configured
with SSB-based BFD and LR in DRX mode 4856A.14.4.2.2.1 Test Purpose and
Environment 4856A.14.4.2.2.2 Test Requirements 4858A.14.4.2.3 Beam
Failure Detection and Link Recovery Test for FR1 PCell for satellite
access configured with CSI-RS-based BFD and LR in non-DRX mode
4859A.14.4.2.3.1 Test Purpose and Environment 4859A.14.4.2.3.2 Test
Requirements 4861A.14.4.2.4 Beam Failure Detection and Link Recovery
Test for FR1 PCell for satellite access configured with CSI-RS-based BFD
and LR in DRX mode 4862A.14.4.2.4.1 Test Purpose and Environment
4862A.14.4.2.4.2 Test Requirements 4864A.14.4.2.5 Void 4865A.14.4.2.6
Void 4865A.14.4.3 Active BWP switch for satellite access 4865A.14.4.3.1
DCI-based and Timer-based Active BWP Switch 4865A.14.4.3.1.1 NR FR1 DL
active BWP switch with non-DRX in SA 4865A.14.4.3.1.1.1 Test Purpose and
Environment 4865A.14.4.3.1.1.2 Test Requirements 4867A.14.4.3.2
RRC-based Active BWP Switch 4867A.14.4.3.2.1 NR FR1 DL active BWP switch
of Cell with non-DRX in SA 4867A.14.4.3.2.1.1 Test Purpose and
Environment 4867A.14.4.3.2.1.2 Test Requirements 4869A.14.4.4 UE
specific CBW change for satellite access 4869A.14.4.4.1 UE specific CBW
change on PCell in FR1 in non-DRX 4869A.14.4.4.1.1 Test Purpose and
Environment 4869A.14.4.4.1.2 Test Requirements 4871A.14.4.5 Pathloss
reference signal switching delay 4872A.14.4.5.1 MAC-CE based pathloss
reference signal switch delay 4872A.14.4.5.1.1 Test Purpose and
Environment 4872A.14.4.5.1.2 Test Requirements 4874A.14.5 Measurement
procedure 4874A.14.5.1 Intra-frequency Measurements 4874A.14.5.1.1 SA
event triggered reporting tests without gap under non-DRX
4874A.14.5.1.1.1 Test purpose and Environment 4874A.14.5.1.1.2 Test
parameters 4874A.14.5.1.1.3 Test Requirements 4876A.14.5.1.2 SA event
triggered reporting tests without gap under DRX 4876A.14.5.1.2.1 Test
purpose and Environment 4876A.14.5.1.2.2 Test parameters
4876A.14.5.1.2.3 Test Requirements 4878A.14.5.1.3 SA event triggered
reporting tests without gap under non-DRX with SSB index reading
4878A.14.5.1.3.1 Test purpose and Environment 4878A.14.5.1.3.2 Test
parameters 4878A.14.5.1.3.3 Test Requirements 4880A.14.5.1.4 SA event
triggered reporting tests with single measurement gap under non-DRX for
satellite access 4880A.14.5.1.4.1 Test purpose and Environment
4880A.14.5.1.4.2 Test parameters 4880A.14.5.1.4.3 Test Requirements
4882A.14.5.1.5 SA event triggered reporting tests with FNO concurrent
gaps under DRX for satellite access 4882A.14.5.1.5.1 Test purpose and
Environment 4882A.14.5.1.5.2 Test parameters 4882A.15.5.1.5.3 Test
Requirements 4884A.14.5.1.6 SA event triggered reporting tests with PPO
concurrent gaps under non-DRX with SSB index reading for satellite
access 4884A.14.5.1.6.1 Test purpose and Environment 4884A.14.5.1.6.2
Test parameters 4884A.14.5.1.6.3 Test Requirements 4886A.14.5.1.7 SA
event triggered reporting test with SSB time index reading without gap
under non-DRX for FR2-NTN 4886A.14.5.1.7.1 Test purpose and Environment
4886A.14.5.1.7.2 Test parameters 4886A.14.5.1.7.3 Test Requirements
4888A.14.5.2 Inter-frequency Measurements 4888A.14.5.2.1 SA event
triggered reporting tests for FR1 without SSB time index detection when
DRX is not used with single gap for satellite access 4888A.14.5.2.1.1
Test Purpose and Environment 4888A.14.5.2.1.2 Test Requirements
4890A.14.5.2.2 SA event triggered reporting tests for FR1 without SSB
time index detection when DRX is used with single gap for satellite
access 4890A.14.5.2.2.1 Test Purpose and Environment 4890A.14.5.2.2.2
Test Requirements 4893A.14.5.2.3 SA event triggered reporting tests for
FR1 with SSB time index detection when DRX is not used with single gap
for satellite access 4893A.14.5.2.3.1 Test Purpose and Environment
4893A.14.5.2.3.2 Test Requirements 4895A.14.5.2.4 SA event triggered
reporting tests for FR1 without SSB time index detection when DRX is not
used with two gaps in fully non-overlapped for satellite access
4895A.14.5.2.4.1 Test Purpose and Environment 4895A.14.5.2.4.2 Test
Requirements 4897A.14.5.2.5 void 4897A.14.5.2.5.1 void 4897A.14.5.2.5.2
void 4898A.14.5.2.6 SA event triggered reporting tests for FR1 without
SSB time index detection when DRX is not used with two gaps in partially
partial overalpping for satellite access 4898A.14.5.2.6.1 Test Purpose
and Environment 4898A.14.5.2.6.2 Test Requirements 4900A.14.5.2.7 Event
triggered reporting test without gap under non-DRX 4900A.14.5.2.7.1 Test
purpose and Environment 4900A.14.5.2.7.2 Test parameters
4900A.14.5.2.7.3 Test Requirements 4901A.14.5.2.8 Event triggered
reporting tests without gap under DRX 4902A.14.5.2.8.1 Test purpose and
Environment 4902A.14.5.2.8.2 Test parameters 4902A.14.5.2.8.3 Test
Requirements 4903A.14.5.3 L1-RSRP measurement for beam reporting for
satellite access 4903A.14.5.3.1 SSB based L1-RSRP measurement for
satellite access when DRX is not used 4903A.14.5.3.1.1 Test Purpose and
Environment 4904A.14.5.3.1.2 Test parameters 4904A.14.5.3.1.3 Test
Requirements 4905A.14.5.3.2 SSB based L1-RSRP measurement for satellite
access when DRX is used 4905A.14.5.3.2.1 Test Purpose and Environment
4905A.14.5.3.2.2 Test parameters 4906A.14.5.3.2.3 Test Requirements
4907A.14.5.3.3 CSI-RS based L1-RSRP measurement for satellite access
when DRX is not used 4907A.14.5.3.3.1 Test Purpose and Environment
4907A.14.5.3.3.2 Test parameters 4908A.14.5.3.3.3 Test Requirements
4909A.14.5.3.4 CSI-RS based L1-RSRP measurement for satellite access
when DRX is used 4909A.14.5.3.4.1 Test Purpose and Environment
4909A.14.5.3.4.2 Test parameters 4909A.14.5.3.4.3 Test Requirements
4911A.14.5.3.5 SSB based L1-RSRP measurement when DRX is not used in
FR2-NTN 4911A.14.5.3.5.1 Test Purpose and Environment 4911A.14.5.3.5.2
Test parameters 4911A.14.5.3.5.3 Test Requirements 4913A.14.6
Measurement Performance requirements 4913A.14.6.1 SS-RSRP for SAN
4913A.14.6.1.1 SA: intra-frequency case measurement accuracy with FR1
serving cell and FR1 target cell 4913A.14.6.1.1.1 Test Purpose and
Environment 4913A.14.6.1.1.2 Test parameters 4913A.14.6.1.1.3 Test
Requirements 4915A.14.6.1.2 SA inter-frequency case measurement accuracy
with FR1 serving cell and FR1 target cell 4915A.14.6.1.2.1 Test Purpose
and Environment 4915A.14.6.1.2.2 Test parameters 4915A.14.6.1.2.3 Test
Requirements 4916A.14.6.1.3 SA intra-frequency case measurement accuracy
with FR2 serving cell and FR2 target cell 4916A.14.6.1.3.1 Test Purpose
and Environment 4916A.14.6.1.3.2 Test parameters 4917A.14.6.1.3.3 Test
Requirements 4918A.14.6.2 SS-RSRQ 4919A.14.6.2.1 SA: Intra-frequency
measurement accuracy with FR1 serving cell and FR1 target cell for
satellite access 4919A.14.6.2.1.1 Test Purpose and Environment
4919A.14.6.2.1.2 Test Parameters 4919A.14.6.2.1.3 Test Requirements
4920A.14.6.2.2 SA Inter-frequency measurement accuracy with FR1 serving
cell and FR1 target cell for satellite access 4920A.14.6.2.2.1 Test
Purpose and Environment 4920A.14.6.2.2.2 Test Parameters
4920A.14.6.2.2.3 Test Requirements 4922A.14.6.3 SS-SINR 4922A.14.6.3.1
SA intra-frequency measurement accuracy with FR1 serving cell and FR1
target cell 4922A.14.6.3.1.1 Test Purpose and Environment
4922A.14.6.3.1.2 Test Parameters 4922A.14.6.3.1.3 Test Requirements
4923A.14.6.3.2 SA Inter-frequency measurement accuracy with FR1 serving
cell and FR1 target cell 4923A.14.6.3.2.1 Test Purpose and Environment
4923A.14.6.3.2.2 Test Parameters 4923A.14.6.3.2.3 Test Requirements
4924A.14.6.4 L1-RSRP measurement for beam reporting 4925A.14.6.4.1 SSB
based L1-RSRP measurement 4925A.14.6.4.1.1 Test Purpose and Environment
4925A.14.6.4.1.2 Test parameters 4925A.14.6.4.1.3 Test Requirements
4926A.14.6.4.2 CSI-RS based L1-RSRP measurement on resource set with
repetition off 4926A.14.6.4.2.1 Test Purpose and Environment
4926A.14.6.4.2.2 Test parameters 4926A.14.6.4.2.3 Test Requirements
4927A.14.6.4.3 SSB based L1-RSRP measurement for VSAT UE in FR2-NTN when
DRX is not used 4928A.14.6.4.3.1 Test Purpose and Environment
4928A.14.6.4.3.2 Test parameters 4928A.14.6.4.3.3 Test Requirements
4929A.15 NR standalone tests with one or more NR cells in FR2-2
4941A.15.1 SA: RRC\_IDLE state mobility 4941A.15.1.1 Cell re-selection
to NR 4941A.15.1.1.1 Cell re-selection to FR2-2 intra-frequency NR case
4941A.15.1.1.1.1 Test Purpose and Environment 4941A.15.1.1.1.2 Test
Parameters 4941A.15.1.1.1.3 Test Requirements 4943A.15.1.2 Cell
re-selection to FR2-2 inter-frequency NR case 4943A.15.1.2.1 Test
Purpose and Environment 4943A.15.1.2.2 Test Parameters 4944A.15.1.2.3
Test Requirements 4946A.15.1.3 Cell re-selection to FR2-2
intra-frequency NR case for UE fulfilling low mobility relaxed
measurement criterion 4946A.15.1.3.1 Test Purpose and Environment
4946A.15.1.3.2 Test Parameters 4946A.15.1.3.3 Test Requirements
4948A.15.1.4 Cell re-selection to FR2-2 intra-frequency NR case for UE
fulfilling not-at-cell edge relaxed measurement criterion 4949A.15.1.4.1
Test Purpose and Environment 4949A.15.1.4.2 Test Parameters
4949A.15.1.4.3 Test Requirements 4951A.15.1.5 Cell re-selection to FR2-2
inter-frequency NR case for UE fulfilling low mobility relaxed
measurement criterion 4951A.15.1.5.1 Test Purpose and Environment
4951A.15.1.5.2 Test Parameters 4951A.15.1.5.3 Test Requirements
4953A.15.1.6 Cell re-selection to FR2-2 inter-frequency NR case for UE
fulfilling not-at-cell edge relaxed measurement criterion 4954A.15.1.6.1
Test Purpose and Environment 4954A.15.1.6.2 Test Parameters
4954A.15.1.6.3 Test Requirements 4956A.15.2 Signaling characteristics
4956A.15.2.1 SCell Activation and Deactivation Delay 4956A.15.2.1.1
SCell Activation and deactivation for SCell in FR2-2 intra-band in
non-DRX 4956A.15.2.1.1.1 Test Purpose and Environment 4956A.15.2.1.1.2
Test Requirements 4958A.15.2.1.2 SCell Activation and deactivation for
FR1+FR2-2 inter-band with target SCell in FR2-2 4958A.15.2.1.2.1 Test
Purpose and Environment 4958A.15.2.1.2.2 Test Requirements
4961A.15.2.1.3 SCell Activation and deactivation for SCell in FR2-2
inter-band in non-DRX 4961A.15.2.1.3.1 Test Purpose and Environment
4962A.15.2.1.3.2 Test Requirements 4964A.15.2.1.4 Direct SCell
activation at SCell addition of known SCell in FR2-2 4965A.15.2.1.4.1
Test Purpose and Environment 4965A.15.2.1.4.2 Test Requirements
4967A.15.2.1.5 Direct SCell activation at handover with known SCell in
FR2-2 4968A.15.2.1.5.1 Test Purpose and Environment 4968A.15.2.1.5.2
Test Requirements 4970A.15.3 RRC\_CONNECTED state mobility 4971A.15.3.1
Handover 4971A.15.3.1.1 Intra-frequency handover from FR2-2 carrier with
CCA to FR2-2 carrier with CCA; unknown target cell 4971A.15.3.1.1.1 Test
Purpose and Environment 4971A.15.3.1.1.2 Test Parameters
4971A.15.3.1.1.3 Test Requirements 4973A.15.3.1.2 Inter-frequency
handover from FR1 to FR2-2 carrier with CCA; unknown target cell
4974A.15.3.1.2.1 Test Purpose and Environment 4974A.15.3.1.2.2 Test
Parameters 4974A.15.3.1.2.3 Test Requirements 4976A.15.4 Measurement
procedure 4976A.15.4.1 Intra-frequency Measurements 4976A.15.4.1.1 SA
event triggered reporting test without gap under non-DRX for FR2-2 with
CCA 4976A.15.4.1.1.1 Test purpose and Environment 4976A.15.4.1.1.2 Test
Requirements 4979A.15.4.2 Inter-frequency Measurements 4980A.15.4.2.1 SA
event triggered reporting tests for FR2-2 with CCA without SSB time
index detection when DRX is not used (PCell in FR2-2) 4980A.15.4.2.1.1
Test Purpose and Environment 4980A.15.4.2.1.2 Test Requirements 4982A.16
NR standalone tests with all NR cells in FR1 for RedCap 4983A.16.1 SA:
RRC\_IDLE state mobility for RedCap 4983A.16.1.1 Cell re-selection to NR
4983A.16.1.1.1 Cell re-selection to FR1 intra-frequency NR case for 1 Rx
UE 4983A.16.1.1.1.1 Test Purpose and Environment 4983A.16.1.1.1.2 Test
Parameters 4983A.16.1.1.1.3 Test Requirements 4985A.16.1.1.2 Cell
re-selection to FR1 intra-frequency NR case for 2 Rx UE 4986A.16.1.1.2.1
Test Purpose and Environment 4986A.16.1.1.2.2 Test Parameters
4986A.16.1.1.2.3 Test Requirements 4988A.16.1.1.3 Cell re-selection to
FR1 inter-frequency NR case for 1 Rx UE 4988A.16.1.1.3.1 Test Purpose
and Environment 4988A.16.1.1.3.2 Test Parameters 4988A.16.1.1.3.3 Test
Requirements 4991A.16.1.1.4 Cell re-selection to FR1 inter-frequency NR
case for 2 Rx UE 4991A.16.1.1.4.1 Test Purpose and Environment
4991A.16.1.1.4.2 Test Parameters 4991A.16.1.1.4.3 Test Requirements
4994A.16.1.1.5 Cell re-selection to FR1 intra-frequency NR case for UE
fulfilling stationary relaxed measurement criterion for 1 Rx UE
4994A.16.1.1.5.1 Test Purpose and Environment 4994A.16.1.1.5.2 Test
Parameters 4994A.16.1.1.5.3 Test Requirements 4997A.16.1.1.6 Cell
re-selection to FR1 intra-frequency NR case for UE fulfilling stationary
relaxed measurement criterion for 2 Rx UE 4997A.16.1.1.6.1 Test Purpose
and Environment 4997A.16.1.1.6.2 Test Parameters 4997A.16.1.1.6.3 Test
Requirements 4999A.16.1.1.7 Cell re-selection to FR1 inter-frequency NR
case for UE fulfilling stationary relaxed measurement criterion for 1 Rx
UE 5000A.16.1.1.7.1 Test Purpose and Environment 5000A.16.1.1.7.2 Test
Parameters 5000A.16.1.1.7.3 Test Requirements 5002A.16.1.1.8 Cell
re-selection to FR1 inter-frequency NR case for UE fulfilling stationary
relaxed measurement criterion for 2 Rx UE 5003A.16.1.1.8.1 Test Purpose
and Environment 5003A.16.1.1.8.2 Test Parameters 5003A.16.1.1.8.3 Test
Requirements 5005A.16.1.2 Inter-RAT E-UTRAN cell re-selection for RedCap
5006A.16.1.2.1 Cell re-selection to higher priority E-UTRAN for 1 RX
5006A.16.1.2.1.1 Test Purpose and Environment 5006A.16.1.2.1.2 Test
Parameters 5006A.16.1.2.1.3 Test Requirements 5009A.16.1.2.2 Cell
re-selection to higher priority E-UTRAN for 2 RX 5009A.16.1.2.2.1 Test
Purpose and Environment 5009A.16.1.2.2.2 Test Parameters
5009A.16.1.2.2.3 Test Requirements 5012A.16.1.2.3.1 Test Purpose and
Environment 5012A. 16.1.2.3.2 Test Parameters 5012A.16.1.2.3.3 Test
Requirements 5015A.16.1.2.4.1 Test Purpose and Environment
5015A.16.1.2.4.2 Test Parameters 5015A.16.1.3.1.3 Test Requirements
5018A.16.1.2.5 Cell re-selection to lower priority E-UTRAN for UE
fulfilling stationary relaxed measurement criterion for 1 Rx UE
5018A.16.1.2.5.1 Test Purpose and Environment 5018A.16.1.2.5.2 Test
Parameters 5018A.16.1.2.5.3 Test Requirements 5021A.16.1.2.6 Cell
re-selection to lower priority E-UTRAN for UE fulfilling stationary
relaxed measurement criterion for 2 Rx UE 5021A.16.1.2.6.1 Test Purpose
and Environment 5021A.16.1.2.6.2 Test Parameters 5022A.16.1.2.6.3 Test
Requirements 5024A.16.2 SA: RRC\_INACTIVE state mobility for RedCap
5025A.16.2.1 Configured Grant based Small Data Transmissions (CG-SDT)
for RedCap 5025A.16.2.1.1 NR UE CG-SDT Test in FR1 for 1 Rx RedCap UE
5025A.16.2.1.1.1 Test purpose and Environment 5025A.16.2.1.1.2 Test
Parameters 5026A.16.2.1.1.3 Test requirements 5028A.16.2.1.2 NR UE
CG-SDT Test in FR1 for 2 Rx RedCap UE 5028A.16.2.1.2.1 Test purpose and
Environment 5028A.16.2.1.2.2 Test Parameters 5030A.16.2.1.2.3 Test
requirements 5031A.16.2.2 Cell Reselection for Positioning
5032A.16.2.2.1 Cell re-selection to FR1 intra-frequency NR case with
RRC\_INACTIVE eDRX and positioning SRS 5032A.16.2.2.1.1 Test Purpose and
Environment 5032A.16.2.2.1.2 Test Parameters 5032A.16.2.2.1.3 Test
Requirements 5035A.16.3 RRC\_CONNECTED state mobility for RedCap
5035A.16.3.1 Handover 5035A.16.3.1.1 Intra-frequency handover from FR1
to FR1; known target cell for 1 Rx UE 5035A.16.3.1.1.1 Test Purpose and
Environment 5035A.16.3.1.1.2 Test Parameters 5035A.16.3.1.1.3 Test
Requirements 5037A.16.3.1.2 Intra-frequency handover from FR1 to FR1;
known target cell for 2 Rx UE 5037A.16.3.1.2.1 Test Purpose and
Environment 5037A.16.3.1.2.2 Test Parameters 5037A.16.3.1.2.3 Test
Requirements 5039A.16.3.1.3 Intra-frequency handover from FR1 to FR1;
unknown target cell for 1 Rx UE 5039A.16.3.1.3.1 Test Purpose and
Environment 5039A.16.3.1.3.2 Test Parameters 5040A.16.3.1.3.3 Test
Requirements 5042A.16.3.1.4 Intra-frequency handover from FR1 to FR1;
unknown target cell for 2 Rx UE 5042A.16.3.1.4.1 Test Purpose and
Environment 5042A.16.3.1.4.2 Test Parameters 5042A.16.3.1.5
Inter-frequency handover from FR1 to FR1; unknown target cell for 1 Rx
UE 5044A.16.3.1.5.1 Test Purpose and Environment 5044A.16.3.1.5.2 Test
Parameters 5044A.16.3.1.5.3 Test Requirements 5046A.16.3.1.6
Inter-frequency handover from FR1 to FR1; unknown target cell for 2 Rx
UE 5047A.16.3.1.6.1 Test Purpose and Environment 5047A.16.3.1.6.2 Test
Parameters 5047A.16.3.1.6.3 Test Requirements 5049A.16.3.1.7 SA NR -
E-UTRAN handover for 1 Rx UE 5049A.16.3.1.7.1 Test Purpose and
Environment 5049A.16.3.1.7.2 Test Requirements 5053A.16.3.1.8 SA NR -
E-UTRAN handover for 2 Rx UE 5053A.16.3.1.8.1 Test Purpose and
Environment 5053A.16.3.1.8.2 Test Requirements 5056A.16.3.1.9 SA NR -
E-UTRAN handover with unknown target cell for 1 Rx UE 5056A.16.3.1.9.1
Test Purpose and Environment 5056A.16.3.1.9.2 Test Requirements
5059A.16.3.1.10 SA NR - E-UTRAN handover with unknown target cell for 2
Rx UE 5059A.16.3.1.10.1 Test Purpose and Environment 5059A.16.3.1.10.2
Test Requirements 5063A.16.3.2 RRC Connection Mobility Control
5063A.16.3.2.1 SA: RRC Re-establishment 5063A.16.3.2.1.1 Intra-frequency
RRC Re-establishment in FR1 for 1 Rx UE 5063A.16.3.2.1.2 Intra-frequency
RRC Re-establishment in FR1 for 2 Rx UE 5066A.16.3.2.1.3 Inter-frequency
RRC Re-establishment in FR1 for 1 Rx UE 5068A.16.3.2.1.4 Inter-frequency
RRC Re-establishment in FR1 for 2 Rx UE 5071A.16.3.2.1.5 Intra-frequency
RRC Re-establishment in FR1 for 1 Rx UE without serving cell timing
5074A.16.3.2.1.6 Intra-frequency RRC Re-establishment in FR1 for 2 Rx UE
without serving cell timing 5077A.16.3.2.2 Random Access
5080A.16.3.2.2.1 4-step RA type contention based random access test in
FR1 for NR standalone for 1 Rx UE 5080A.16.3.2.2.2 4-step RA type
contention based random access test in FR1 for NR standalone for 2 Rx UE
5083A.16.3.2.2.3 4-step RA type non-contention based random access test
in FR1 for NR standalone for 1 Rx UE 5086A.16.3.2.2.4 4-step RA type
non-contention based random access test in FR1 for NR standalone for 2
Rx UE 5089A.16.3.2.2.5 2-step RA type contention based random access
test in FR1 for NR standalone for 1 Rx UE 5093A.16.3.2.2.6 2-step RA
type contention based random access test in FR1 for NR standalone for 2
Rx UE 5096A.16.3.2.2.7 2-step RA type non-contention based test in FR1
for NR standalone for 1 RX UE 5098A.16.3.2.2.8 2-step RA type
non-contention based test in FR1 for NR standalone for 2 RX UE
5101A.16.3.2.3 SA: RRC Connection Release with Redirection
5104A.16.3.2.3.1 Redirection from NR in FR1 to NR in FR1 for 1 Rx UE
5104A.16.3.2.3.2 Redirection from NR in FR1 to NR in FR1 for 2 Rx UE
5106A.16.3.2.3.3 Redirection from NR in FR1 to E-UTRAN for 1 Rx UE
5109A.16.3.2.3.4 Redirection from NR in FR1 to E-UTRAN for 2 Rx UE
5112A.16.4 Timing for RedCap 5116A.16.4.1 UE transmit timing
5116A.16.4.1.1 NR UE Transmit Timing Test for FR1 for 1 Rx RedCap UE
5116A.16.4.1.1.1 Test Purpose and environment 5116A.16.4.1.1.2 Test
requirements 5118A.16.4.1.2 NR UE Transmit Timing Test for FR1 for 2 Rx
RedCap UE 5118A.16.4.1.2.1 Test Purpose and environment 5118A.16.4.1.2.2
Test requirements 5120A.16.4.2 Void 5120A.16.4.3 Timing advance
5120A.16.4.3.1 SA FR1 timing advance adjustment accuracy for 1 Rx UE
5120A.16.4.3.1.1 Test Purpose and Environment 5120A.16.4.3.1.2 Test
Parameters 5120A.16.4.3.1.3 Test Requirements 5122A.16.4.3.2 SA FR1
timing advance adjustment accuracy for 2 Rx UE 5123A.16.4.3.2.1 Test
Purpose and Environment 5123A.16.4.3.2.2 Test Parameters
5123A.16.4.3.2.3 Test Requirements 5125A.16.5 Signalling characteristics
for RedCap 5125A.16.5.1 Radio link Monitoring 5125A.16.5.1.1 Radio Link
Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM
RS in non-DRX mode for 1 Rx UE 5125A.16.5.1.1.1 Test Purpose and
Environment 5125A.16.5.1.1.2 Test Requirements 5128A.16.5.1.2 Radio Link
Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM
RS in non-DRX mode for 2 Rx UE 5128A.16.5.1.2.1 Test Purpose and
Environment 5128A.16.5.1.2.2 Test Requirements 5131A.16.5.1.3 Radio Link
Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS
in non-DRX mode for 1 Rx UE 5131A.16.5.1.3.1 Test Purpose and
Environment 5131A.16.5.1.3.2 Test Requirements 5134A.16.5.1.4 Radio Link
Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS
in non-DRX mode for 2 Rx UE 5134A.16.5.1.4.1 Test Purpose and
Environment 5134A.16.5.1.4.2 Test Requirements 5137A.16.5.1.5 Radio Link
Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM
RS in DRX mode for 1 Rx UE 5137A.16.5.1.5.1 Test Purpose and Environment
5137A.16.5.1.5.2 Test Requirements 5140A.16.5.1.6 Radio Link Monitoring
Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX
mode for 2 Rx UE 5140A.16.5.1.6.1 Test Purpose and Environment
5140A.16.5.1.6.2 Test Requirements 5143A.16.5.1.7 Radio Link Monitoring
In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode
for 1 Rx UE 5143A.16.5.1.7.1 Test Purpose and Environment
5143A.16.5.1.7.2 Test Requirements 5146A.16.5.1.8 Radio Link Monitoring
In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode
for 2 Rx UE 5146A.16.5.1.8.1 Test Purpose and Environment
5146A.16.5.1.8.2 Test Requirements 5149A.16.5.1.9 Radio Link Monitoring
Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in
non-DRX mode for 1 Rx UE 5149A.16.5.1.9.1 Test Purpose and Environment
5149A.16.5.1.9.2 Test Requirements 5152A.16.5.1.10 Radio Link Monitoring
Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in
non-DRX mode for 2 Rx UE 5152A.16.5.1.10.1 Test Purpose and Environment
5152A.16.5.1.10.2 Test Requirements 5155A.16.5.1.11 Radio Link
Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM
in non-DRX mode for 1 Rx UE 5155A.16.5.1.11.1 Test Purpose and
Environment 5155A.16.5.1.11.2 Test Requirements 5158A.16.5.1.12 Radio
Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based
RLM in non-DRX mode for 2 Rx UE 5158A.16.5.1.12.1 Test Purpose and
Environment 5158A.16.5.1.12.2 Test Requirements 5161A.16.5.1.13 Radio
Link Monitoring Out-of-sync Test for FR1 PCell configured with
CSI-RS-based RLM in DRX mode for 1 Rx UE 5162A.16.5.1.13.1 Test Purpose
and Environment 5162A.16.5.1.13.2 Test Requirements 5164A.16.5.1.14
Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with
CSI-RS-based RLM in DRX mode for 2 Rx UE 5165A.16.5.1.14.1 Test Purpose
and Environment 5165A.16.5.1.14.2 Test Requirements 5167A.16.5.1.15
Radio Link Monitoring In-sync Test for FR1 PCell configured with
CSI-RS-based RLM in DRX mode for 1 Rx UE 5168A.16.5.1.15.1 Test Purpose
and Environment 5168A.16.5.1.15.2 Test Requirements 5171A.16.5.1.16
Radio Link Monitoring In-sync Test for FR1 PCell configured with
CSI-RS-based RLM in DRX mode for 2 Rx UE 5171A.16.5.1.16.1 Test Purpose
and Environment 5171A.16.5.1.16.2 Test Requirements 5174A.16.5.2 Beam
Failure Detection and Link recovery procedures 5174A.16.5.2.1 Beam
Failure Detection and Link Recovery Test for FR1 PCell configured with
SSB-based BFD and LR in non-DRX mode for 1 Rx UE 5174A.16.5.2.1.1 Test
Purpose and Environment 5174A.16.5.2.1.2 Test Requirements
5177A.16.5.2.2 Beam Failure Detection and Link Recovery Test for FR1
PCell configured with SSB-based BFD and LR in non-DRX mode for 2 Rx UE
5178A.16.5.2.2.1 Test Purpose and Environment 5178A.16.5.2.2.2 Test
Requirements 5181A.16.5.2.3 Beam Failure Detection and Link Recovery
Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode for
1 Rx UE 5181A.16.5.2.3.1 Test Purpose and Environment 5181A.16.5.2.3.2
Test Requirements 5184A.16.5.2.4 Beam Failure Detection and Link
Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX
mode for 2 Rx UE 5185A.16.5.2.4.1 Test Purpose and Environment
5185A.16.5.2.4.2 Test Requirements 5188A.16.5.2.5 Beam Failure Detection
and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD
and LR in non-DRX mode for 1 Rx UE 5188A.16.5.2.5.1 Test Purpose and
Environment 5188A.16.5.2.5.2 Test Requirements 5191A.16.5.2.6 Beam
Failure Detection and Link Recovery Test for FR1 PCell configured with
CSI-RS-based BFD and LR in non-DRX mode for 2 Rx UE 5192A.16.5.2.6.1
Test Purpose and Environment 5192A.16.5.2.6.2 Test Requirements
5195A.16.5.2.7 Beam Failure Detection and Link Recovery Test for FR1
PCell configured with CSI-RS-based BFD and LR in DRX mode for 1 Rx UE
5195A.16.5.2.7.1 Test Purpose and Environment 5195A.16.5.2.7.2 Test
Requirements 5198A.16.5.2.8 Beam Failure Detection and Link Recovery
Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode
for 2 Rx UE 5199A.16.5.2.8.1 Test Purpose and Environment
5199A.16.5.2.8.2 Test Requirements 5202A.16.5.3 Active BWP switch
5202A.16.5.3.1 DCI-based and Timer-based Active BWP Switch
5202A.16.5.3.1.1 NR FR1 DL active BWP switch with non-DRX in SA for 1 Rx
UE 5202A.16.5.3.1.1.1 Test Purpose and Environment
5202A.1**6.5.3.1.1.**2 Test Requirements 5205A.16.5.3.1.2 NR FR1 DL
active BWP switch with non-DRX in SA for 2 Rx UE 5205A.16.5.3.1.2.1 Test
Purpose and Environment 5205A.1**6.5.3.1.2.**2 Test Requirements
5207A.16.5.3.2 RRC-based Active BWP Switch 5208A.16.5.3.2.1 NR FR1 DL
active BWP switch of Cell with non-DRX in SA for 1 Rx UE
5208A.16.5.3.2.1.1 Test Purpose and Environment 5208A.16.5.3.2.1.2 Test
Requirements 5210A.16.5.3.2.2 NR FR1 DL active BWP switch of Cell with
non-DRX in SA for 2 Rx UE 5210A.16.5.3.2.2.1 Test Purpose and
Environment 5210A.16.5.3.2.2.2 Test Requirements 5212A.16.5.4 UE
specific CBW change 5213A.16.5.4.1 UE specific CBW change on PCell in
FR1 in non-DRX for 1 Rx UE 5213A.16.5.4.1.1 Test Purpose and Environment
5213A.16.5.4.1.2 Test Requirements 5215A.16.5.4.2 UE specific CBW change
on PCell in FR1 in non-DRX for 2 Rx UE 5215A.16.5.4.2.1 Test Purpose and
Environment 5215A.16.5.4.2.2 Test Requirements 5218A.16.6 Measurement
procedure for RedCap 5218A.16.6.1 Intra-frequency Measurements
5218A.16.6.1.1 SA event triggered reporting tests without gap under
non-DRX for 1 Rx UE 5218A.16.6.1.1.1 Test purpose and Environment
5218A.16.6.1.1.2 Test parameters 5218A.16.6.1.1.3 Test Requirements
5220A.16.6.1.2 SA event triggered reporting tests without gap under
non-DRX for 2 Rx UE 5220A.16.6.1.2.1 Test purpose and Environment
5220A.16.6.1.2.2 Test parameters 5220A.16.6.1.2.3 Test Requirements
5222A.16.6.1.3 SA event triggered reporting tests without gap under DRX
for 1 Rx UE 5222A.16.6.1.3.1 Test purpose and Environment
5222A.16.6.1.3.2 Test parameters 5222A.16.6.1.3.3 Test Requirements
5224A.16.6.1.4 SA event triggered reporting tests without gap under DRX
for 2 Rx UE 5225A.16.6.1.4.1 Test purpose and Environment
5225A.16.6.1.4.2 Test parameters 5225A.16.6.1.4.3 Test Requirements
5227A.16.6.1.5 SA event triggered reporting tests with per-UE gaps under
non-DRX for 1 Rx UE 5227A.16.6.1.5.1 Test purpose and Environment
5227A.16.6.1.5.2 Test parameters 5227A.16.6.1.5.3 Test Requirements
5229A.16.6.1.6 SA event triggered reporting tests with per-UE gaps under
non-DRX for 2 Rx UE 5229A.16.6.1.6.1 Test purpose and Environment
5229A.16.6.1.6.2 Test parameters 5229A.16.6.1.6.3 Test Requirements
5231A.16.6.1.7 SA event triggered reporting tests with per-UE gaps under
DRX for 1 Rx UE 5232A.16.6.1.7.1 Test purpose and Environment
5232A.16.6.1.7.2 Test parameters 5232A.16.6.1.7.3 Test Requirements
5234A.16.6.1.8 SA event triggered reporting tests with per-UE gaps under
DRX for 2 Rx UE 5234A.16.6.1.8.1 Test purpose and Environment
5234A.16.6.1.8.2 Test parameters 5234A.16.6.1.8.3 Test Requirements
5236A.16.6.1.9 SA event triggered reporting tests without gap under
non-DRX with SSB index reading for 1 Rx UE 5236A.16.6.1.9.1 Test purpose
and Environment 5236A.16.6.1.9.2 Test parameters 5237A.16.6.1.9.3 Test
Requirements 5238A.16.6.1.10 SA event triggered reporting tests without
gap under non-DRX with SSB index reading for 2 Rx UE 5238A.16.6.1.10.1
Test purpose and Environment 5238A.16.6.1.10.2 Test parameters
5238A.16.6.1.10.3 Test Requirements 5240A.16.6.1.11 SA event triggered
reporting tests with per-UE gaps under non-DRX with SSB index reading
for 1 Rx UE 5240A.16.6.1.11.1 Test purpose and Environment
5240A.16.6.1.11.2 Test parameters 5240A.16.6.1.11.3 Test Requirements
5242A.16.6.1.12 SA event triggered reporting tests with per-UE gaps
under non-DRX with SSB index reading for 2 Rx UE 5242A.16.6.1.12.1 Test
purpose and Environment 5242A.16.6.1.12.2 Test parameters
5242A.16.6.1.12.3 Test Requirements 5243A.16.6.2 Inter-frequency
Measurements 5244A.16.6.2.1 SA event triggered reporting tests for FR1
without SSB time index detection when DRX is used for 1 Rx UE
5244A.16.6.2.1.1 Test Purpose and Environment 5244A.16.6.2.1.2 Test
Requirements 5246A.16.6.2.2 SA event triggered reporting tests for FR1
without SSB time index detection when DRX is used for 2 Rx UE
5247A.16.6.2.2.1 Test Purpose and Environment 5247A.16.6.2.2.2 Test
Requirements 5249A.16.6.2.3 SA event triggered reporting tests for FR1
without SSB time index detection when DRX is not used for 1 Rx UE
5249A.16.6.2.3.1 Test Purpose and Environment 5250A.16.6.2.3.2 Test
Requirements 5252A.16.6.2.4 SA event triggered reporting tests for FR1
without SSB time index detection when DRX is not used for 2 Rx UE
5252A.16.6.2.4.1 Test Purpose and Environment 5252A.16.6.2.4.2 Test
Requirements 5254A.16.6.2.5 SA event triggered reporting tests for FR1
with SSB time index detection when DRX is not used for 1 Rx UE
5254A.16.6.2.5.1 Test Purpose and Environment 5254A.16.6.2.5.2 Test
Requirements 5257A.16.6.2.6 SA event triggered reporting tests for FR1
with SSB time index detection when DRX is not used for 2 Rx UE
5257A.16.6.2.6.1 Test Purpose and Environment 5257A.16.6.2.6.2 Test
Requirements 5259A.16.6.2.7 SA event triggered reporting tests for FR1
with SSB time index detection when DRX is used for 1 Rx UE
5259A.16.6.2.7.1 Test Purpose and Environment 5259A.16.6.2.7.2 Test
Requirements 5262A.16.6.2.8 SA event triggered reporting tests for FR1
with SSB time index detection when DRX is used for 2 Rx UE
5262A.16.6.2.8.1 Test Purpose and Environment 5262A.16.6.2.8.2 Test
Requirements 5264A.16.6.2.9 SA event triggered reporting tests with
additional mandatory gap pattern for 1 Rx UE 5265A.16.6.2.9.1 Test
Purpose and Environment 5265A.16.6.2.9.2 Test Requirements
5267A.16.6.2.10 SA event triggered reporting tests with additional
mandatory gap pattern for 2 Rx UE 5267A.16.6.2.10.1 Test Purpose and
Environment 5267A.16.6.2.10.2 Test Requirements 5269A.16.6.2.11 SA event
triggered reporting tests for FR1 when DRX is used for 1 Rx UE
5270A.16.6.2.11.1 Test Purpose and Environment 5270A.16.6.2.11.2 Test
Requirements 5272A.16.6.2.12 SA event triggered reporting tests for FR1
when DRX is used for 2 Rx UE 5272A.16.6.2.12.1 Test Purpose and
Environment 5272A.16.6.2.12.2 Test Requirements 5275A.16.6.3 Inter-RAT
Measurements 5275A.16.6.3.1 SA NR - E-UTRAN event-triggered reporting in
non-DRX in FR1 for 1 Rx UE 5275A.16.6.3.1.1 Test purpose and Environment
5275A.16.6.3.1.2 Test Requirements 5278A.16.6.3.2 SA NR - E-UTRAN
event-triggered reporting in non-DRX in FR1 for 2 Rx UE 5279A.16.6.3.2.1
Test purpose and Environment 5279A.16.6.3.2.2 Test Requirements
5282A.16.6.3.3 SA NR - E-UTRAN event-triggered reporting in DRX in FR1
for 1 Rx UE 5282A.16.6.3.3.1 Test purpose and Environment
5282A.16.6.3.3.2 Test Requirements 5286A.16.6.3.4 SA NR - E-UTRAN
event-triggered reporting in DRX in FR1 for 2 Rx UE 5286A.16.6.3.4.1
Test purpose and Environment 5286A.16.6.3.4.2 Test Requirements
5289A.16.6.4 L1-RSRP measurement for beam reporting 5290A.16.6.4.1 SSB
based L1-RSRP measurement when DRX is not used for 1 Rx UE
5290A.16.6.4.1.1 Test Purpose and Environment 5290A.16.6.4.1.2 Test
parameters 5290A.16.6.4.1.3 Test Requirements 5291A.16.6.4.2 SSB based
L1-RSRP measurement when DRX is not used for 2 Rx UE 5292A.16.6.4.2.1
Test Purpose and Environment 5292A.16.6.4.2.2 Test parameters
5292A.16.6.4.2.3 Test Requirements 5293A.16.6.4.3 SSB based L1-RSRP
measurement when DRX is used for 1 Rx UE 5293A.16.6.4.3.1 Test Purpose
and Environment 5293A.16.6.4.3.2 Test parameters 5294A.16.6.4.3.3 Test
Requirements 5295A.16.6.4.4 SSB based L1-RSRP measurement when DRX is
used for 2 Rx UE 5295A.16.6.4.4.1 Test Purpose and Environment
5295A.16.6.4.4.2 Test parameters 5296A.16.6.4.4.3 Test Requirements
5297A.16.6.4.5 CSI-RS based L1-RSRP measurement when DRX is not used for
1 Rx UE 5297A.16.6.4.5.1 Test Purpose and Environment 5297A.16.6.4.5.2
Test parameters 5298A.16.6.4.5.3 Test Requirements 5299A.16.6.4.6 CSI-RS
based L1-RSRP measurement when DRX is not used for 2 Rx UE
5299A.16.6.4.6.1 Test Purpose and Environment 5299A.16.6.4.6.2 Test
parameters 5300A.16.6.4.6.3 Test Requirements 5301A.16.6.4.7 CSI-RS
based L1-RSRP measurement when DRX is used for 1 Rx UE 5301A.16.6.4.7.1
Test Purpose and Environment 5301A.16.6.4.7.2 Test parameters
5302A.16.6.4.7.3 Test Requirements 5303A.16.6.4.8 CSI-RS based L1-RSRP
measurement when DRX is used for 2 Rx UE 5303A.16.6.4.8.1 Test Purpose
and Environment 5303A.16.6.4.8.2 Test parameters 5304A.16.6.4.8.3 Test
Requirements 5305A.16.6.5 NR measurements with autonomous gaps
5306A.16.6.5.1 SA intra-frequency CGI identification of NR neighbor cell
in FR1 for 1 Rx UE 5306A.16.6.5.1.1 Test Purpose and Environment
5306A.16.6.5.1.2 Test Parameters 5306A.16.6.5.1.3 Test Requirements
5308A.16.6.5.2 SA intra-frequency CGI identification of NR neighbor cell
in FR1 for 2 Rx UE 5308A.16.6.5.2.1 Test Purpose and Environment
5308A.16.6.5.2.2 Test Parameters 5308A.16.6.5.2.3 Test Requirements
5310A.16.6.5.3 Identification of a new CGI of inter-RAT E-UTRA cell
using autonomous gaps in NR SA for 1 Rx UE 5310A.16.6.5.3.1 Test Purpose
and Environment 5310A.16.6.5.3.2 Test Requirements 5313A.16.6.5.4
Identification of a new CGI of inter-RAT E-UTRA cell using autonomous
gaps in NR SA for 2 Rx UE 5313A.16.6.5.4.1 Test Purpose and Environment
5313A.16.6.5.4.2 Test Requirements 5316A.16.6.6 RSTD Measurements
5316A.16.6.6.1 NR RSTD measurement reporting delay test case for RedCap
UE without FH in FR1 SA 5316A.16.6.6.1.1 Test Purpose and Environment
5316A.16.6.6.1.2 Test Requirements 5321A.16.6.6.2 NR RSTD measurement
reporting delay test case with PRS frequency hopping 5321A.16.6.6.2.1
Test Purpose and Environment 5321A.16.6.6.2.2 Test Requirements
5325A.16.6.7 UE Rx-Tx Measurements 5326A.16.6.7.1 UE Rx-Tx measurement
reporting delay test case for single positioning frequency layer in FR1
SA for RedCap UE without RX FH in RRC\_CONNECTED mode 5326A.16.6.7.1.1
Test purpose and environment 5326A.16.6.7.1.2 Test requirements
5330A.16.6.7.2 UE Rx-Tx time difference measurement with Rx FH for
single positioning frequency layer in FR1 SA in RRC\_CONNECTED state
5330A.16.6.7.2.1 Test purpose and environment 5330A.16.6.7.2.2 Test
requirements 5334A.16.6.8 PRS-RSRP measurements 5334A.16.6.8.1 PRS-RSRP
measurement delay test case for single positioning frequency layer
5334A.16.6.8.1.1 Test purpose and Environment 5334A.16.6.8.1.2 Test
Requirements 5338A.16.6.8.2 PRS-RSRP measurement delay with FH in
RRC\_CONNECTED state in FR1 5338A.16.6.8.2.1 Test purpose and
Environment 5338A.16.6.8.2.2 Test Requirements 5342A.16.6.9 PRS-RSRPP
Measurements 5342A.16.6.9.1 PRS-RSRPP measurement delay without FH in
RRC\_CONNECTED state in FR1 5342A.16.6.9.1.1 Test purpose and
Environment 5342A.16.6.9.1.2 Test Requirements 5344A.16.6.9.2 PRS-RSRPP
measurement with Rx FH reporting delay test case for single positioning
frequency layer in FR1 SA in RRC\_CONNECTED state 5345A.16.6.9.2.1 Test
purpose and Environment 5345A.16.6.9.2.2 Test Requirements 5347A.16.7
Measurement Performance requirements for RedCap 5347A.16.7.1 SS-RSRP
5347A.16.7.1.1 SA: intra-frequency case measurement accuracy with FR1
serving cell and FR1 target cell for 1 Rx UE 5347A.16.7.1.1.1 Test
Purpose and Environment 5347A.16.7.1.1.2 Test parameters
5347A.16.7.1.1.3 Test Requirements 5351A.16.7.1.2 SA: intra-frequency
case measurement accuracy with FR1 serving cell and FR1 target cell for
2 RX UE 5351A.16.7.1.2.1 Test Purpose and Environment 5351A.16.7.1.2.2
Test parameters 5351A.16.7.1.2.3 Test Requirements 5355A.16.7.1.3 SA
inter-frequency case measurement accuracy with FR1 serving cell and FR1
target cell for 1 Rx UE 5355A.16.7.1.3.1 Test Purpose and Environment
5355A.16.7.1.3.2 Test parameters 5355A.16.7.1.3.3 Test Requirements
5358A.16.7.1.4 SA inter-frequency case measurement accuracy with FR1
serving cell and FR1 target cell for 2 Rx UE 5358A.16.7.1.4.1 Test
Purpose and Environment 5358A.16.7.1.4.2 Test parameters
5358A.16.7.1.4.3 Test Requirements 5361A.16.7.2 SS-RSRQ 5361A.16.7.2.1
SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1
target cell for 1 Rx UE 5361A.16.7.2.1.1 Test Purpose and Environment
5361A.16.7.2.1.2 Test Parameters 5361A.16.7.2.1.3 Test Requirements
5365A.16.7.2.2 SA: Intra-frequency measurement accuracy with FR1 serving
cell and FR1 target cell for 2 Rx UE 5365A.16.7.2.2.1 Test Purpose and
Environment 5365A.16.7.2.2.2 Test Parameters 5365A.16.7.2.2.3 Test
Requirements 5368A.16.7.2.3 SA Inter-frequency measurement accuracy with
FR1 serving cell and FR1 target cell for 1 Rx UE 5368A.16.7.2.3.1 Test
Purpose and Environment 5368A.16.7.2.3.2 Test parameters
5369A.16.7.2.3.3 Test Requirements 5372A.16.7.2.4 SA Inter-frequency
measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx
UE 5372A.16.7.2.4.1 Test Purpose and Environment 5372A.16.7.2.4.2 Test
parameters 5372A.16.7.2.4.3 Test Requirements 5376A.16.7.3 SS-SINR
5376A.16.7.3.1 SA intra-frequency measurement accuracy with FR1 serving
cell and FR1 target cell for 1 Rx UE 5376A.16.7.3.1.1 Test Purpose and
Environment 5376A.16.7.3.1.2 Test parameters 5376A.16.7.3.1.3 Test
Requirements 5379A.16.7.3.2 SA intra-frequency measurement accuracy with
FR1 serving cell and FR1 target cell for 2 Rx UE 5379A.16.7.3.2.1 Test
Purpose and Environment 5379A.16.7.3.2.2 Test parameters 5379A.16.7.3.3
SA Inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell for 1 Rx UE 5382A.16.7.3.3.1 Test Purpose and Environment
5382A.16.7.3.3.2 Test parameters 5382A.16.7.3.3.3 Test Requirements
5385A.16.7.3.4 SA Inter-frequency measurement accuracy with FR1 serving
cell and FR1 target cell for 2 Rx UE 5385A.16.7.3.4.1 Test Purpose and
Environment 5385A.16.7.3.4.2 Test parameters 5385A.16.7.3.4.3 Test
Requirements 5388A.16.7.4 L1-RSRP measurement for beam reporting
5389A.16.7.4.1 SSB based L1-RSRP measurement for 1 Rx UE
5389A.16.7.4.1.1 Test Purpose and Environment 5389A.16.7.4.1.2 Test
parameters 5389A.16.7.4.1.3 Test Requirements 5391A.16.7.4.2 SSB based
L1-RSRP measurement for 2 Rx UE 5391A.16.7.4.2.1 Test Purpose and
Environment 5391A.16.7.4.2.2 Test parameters 5392A.16.7.4.2.3 Test
Requirements 5392A.16.7.4.3 CSI-RS based L1-RSRP measurement on resource
set with repetition off for 1 Rx UE 5392A.16.7.4.3.1 Test Purpose and
Environment 5392A.16.7.4.3.2 Test parameters 5392A.16.7.4.3.3 Test
Requirements 5395A.16.7.4.4 CSI-RS based L1-RSRP measurement on resource
set with repetition off for 2 Rx UE 5395A.16.7.4.4.1 Test Purpose and
Environment 5395A.16.7.4.4.2 Test parameters 5395A.16.7.4.4.3 Test
Requirements 5395A.16.7.5 E-UTRAN RSRP 5395A.16.7.5.1 SA: inter-RAT
measurement accuracy with FR1 serving cell for 1 Rx UE 5395A.16.7.5.1.1
Test Purpose and Environment 5395A.16.7.5.1.2 Test parameters
5395A.16.7.5.1.3 Test Requirements 5399A.16.7.5.2 SA: inter-RAT
measurement accuracy with FR1 serving cell for 2 Rx UE 5399A.16.7.5.2.1
Test Purpose and Environment 5399A.16.7.5.2.2 Test parameters
5399A.16.7.5.2.3 Test Requirements 5402A.16.7.6 E-UTRAN RSRQ
5402A.16.7.6.1 SA: inter-RAT measurement accuracy with FR1 serving cell
for 1 Rx UE 5402A.16.7.6.1.1 Test Purpose and Environment
5402A.16.7.6.1.2 Test parameters 5402A.16.7.6.1.3 Test Requirements
5406A.16.7.6.2 SA: inter-RAT measurement accuracy with FR1 serving cell
for 2 Rx UE 5406A.16.7.6.2.1 Test Purpose and Environment
5406A.16.7.6.2.2 Test parameters 5406A.16.7.6.2.3 Test Requirements
5409A.16.7.7 RSTD measurements 5409A.16.7.7.1 RSTD measurement accuracy
test case for RedCap UE without FH 5409A.16.7.7.1.1 Test purpose and
Environment 5409A.16.7.7.1.2 Test Requirements 5411A.16.7.8 UE Rx-Tx
measurements 5415A.16.7.8.1 UE Rx-Tx time difference measurement
accuracy for single positioning frequency layer in FR1 SA for RedCap UE
without RX FH in RRC\_CONNECTED mode 5415A.16.7.8.1.1 Test purpose and
environment 5415A.16.7.8.1.2 Test parameters 5416A.16.7.8.1.3 Test
requirements 5419A.16.7.8.2 SA: UE Rx-Tx time difference measurement
accuracy with Rx FH in RRC\_CONNECTED state in FR1 5419A.16.7.8.2.1 Test
purpose and Environment 5419A.16.7.8.2.2 Test parameters
5420A.16.7.8.2.3 Test requirements 5423A.16.7.9 PRS-RSRP Measurements
5423A.16.7.9.1 PRS-RSRP measurement accuracy without FH in
RRC\_CONNECTED state in FR1 5423A.16.7.9.1.1 Test Purpose and
Environment 5423A.16.7.9.1.2 Test parameters 5423A.16.7.9.1.3 Test
Requirements 5427A.16.7.9.2 PRS-RSRP measurement accuracy with FH in
RRC\_CONNECTED state in FR1 5428A.16.7.9.2.1 Test Purpose and
Environment 5428A.16.7.9.2.2 Test parameters 5428A.16.7.9.2.3 Test
Requirements 5431A.16.7.10 PRS-RSRPP measurements 5432A.16.7.10.1
PRS-RSRPP measurement accuracy without FH in RRC\_CONNECTED state in FR1
5432A.16.7.10.1.1 Test Purpose and Environment 5432A.16.7.10.1.2 Test
parameters 5432A.16.7.10.1.3 Test Requirements 5435A.16.7.10.2 SA:
PRS-RSRPP measurement accuracy with Rx FH in RRC\_CONNECTED state in FR1
5435**A.16.7.10.2.1** Test purpose and Environment 5435**A.16.7.10.2.2**
Test parameters 5435**A.16.7.10.2.3** Test requirements 5439A.16.8
Measurement Procedure for RedCap in RRC\_INACTIVE 5439A.16.8.1 RSTD
Measurements 5439A.16.8.1.1 NR RSTD measurement reporting delay test
case for for RedCap UE without FH in FR1 SA in RRC\_INACTIVE state
5439A.16.8.1.1.1 Test Purpose and Environment 5439A.16.8.1.1.2 Test
Requirements 5443A.16.8.1.2 NR RSTD measurement reporting delay test
case with PRS frequency hopping 5443A.16.8.1.2.1 Test Purpose and
Environment 5443A.16.8.1.2.2 Test Requirements 5447A.16.8.1.3 NR RSTD
measurement reporting delay test case for single positioning frequency
layer in FR1 SA in RRC\_INACTIVE state when eDRX cycle \> 10.24s for
RedCap UE 5447A.16.8.1.3.1 Test Purpose and Environment 5447A.16.8.1.3.2
Test Requirements 5451A.16.8.2 UE Rx-Tx Measurements 5451A.16.8.2.1 UE
Rx-Tx measurement reporting delay test case for single positioning
frequency layer in FR1 SA for RedCap UE without RX FH in RRC\_INACTIVE
mode 5451A.16.8.2.1.1 Test purpose and environment 5451A.16.8.2.1.2 Test
requirements 5455A.16.8.2.2 UE Rx-Tx time difference measurement with Rx
FH for single positioning frequency layer in FR1 SA in RRC\_INACTIVE
state 5455A.16.8.2.2.1 Test purpose and environment 5455A.16.8.2.2.2
Test requirements 5459A.16.8.2.3. UE Rx-Tx time difference measurement
for single positioning frequency layer with eDRX \> 10.24s in FR1 SA
5459A.16.8.2.3.1 Test purpose and environment 5459A.16.8.2.3.2 Test
requirements 5463A.16.8.3 PRS-RSRP Measurements 5463A.16.8.3.1 PRS-RSRP
reporting delay test case for single positioning frequency layer in
RRC\_INACTIVE 5463A.16.8.3.1.1 Test purpose and Environment
5463A.16.8.3.1.2 Test Requirements 5465A.16.8.3.3 PRS-RSRP reporting
delay test case in RRC\_INACTIVE state in FR1 when eDRX cycle \> 10.24s
5466A.16.8.3.3.1 Test purpose and Environment 5466A.16.8.3.3.2 Test
Requirements 5468A.16.8.4 PRS-RSRPP Measurements 5469A.16.8.4.1
PRS-RSRPP measurement delay without FH in RRC\_INACTIVE state in FR1
5469A.16.8.4.1.1 Test purpose and Environment 5469A.16.8.4.2 PRS-RSRPP
measurement with Rx FH reporting delay test case for single positioning
frequency layer in FR1 SA in RRC\_INACTIVE state 5472A.16.8.4.2.1 Test
purpose and Environment 5472A.16.8.4.2.2 Test Requirements 5474A.16.9
Measurement Performance Requirements for RedCap in RRC\_INACTIVE
5477A.16.9.1 RSTD Measurements 5477A.16.9.1.1 RSTD measurement accuracy
test case for RedCap UE without FH in FR1 in RRC\_INACTIVE state
5477A.16.9.1.1.1 Test purpose and Environment 5477A.16.9.1.1.2 Test
Requirements 5479A.16.9.1.2 RSTD measurement accuracy test case for
RedCap UE with FH in FR1 in RRC\_INACTIVE state 5479A.16.9.1.2.1 Test
purpose and Environment 5479A.16.9.1.2.2 Test Requirements 5481A.16.9.2
UE Rx-Tx measurements 5481A.16.9.2.1 UE Rx-Tx time difference
measurement accuracy for single positioning frequency layer in FR1 SA
for RedCap UE without RX FH in RRC\_INACTIVE mode 5481A.16.9.2.1.1 Test
purpose and environment 5481A.16.9.2.1.2 Test parameters
5482A.16.9.2.1.3 Test requirements 5483A.16.9.2.2 SA: UE Rx-Tx time
difference measurement accuracy with Rx FH in RRC\_INACTIVE state in FR1
5484A.16.9.2.2.1 Test purpose and Environment 5484A.16.9.2.2.2 Test
parameters 5484A.16.9.2.2.3 Test requirements 5487A.16.9.3 PRS-RSRP
Measurements 5487A.16.9.3.1 PRS-RSRP measurement accuracy without FH in
RRC\_INACTIVE state in FR1 5487A.16.9.3.1.1 Test Purpose and Environment
5487A.16.9.3.1.2 Test parameters 5487A.16.9.3.1.3 Test Requirements
5490A.16.9.3.2 PRS-RSRP measurement accuracy with FH in RRC\_INACTIVE
state in FR1 5490A.16.9.3.2.1 Test Purpose and Environment
5490A.16.9.3.2.2 Test parameters 5490A.16.9.3.2.3 Test Requirements
5493A.16.9.4 PRS-RSRPP measurements 5493A.16.9.4.1 PRS-RSRPP measurement
accuracy without Rx FH in RRC\_INACTIVE state in FR1
5493**A.16.9.4.1.1** Test purpose and Environment 5493**A.16.9.4.1.2**
Test parameters 5493**A.16.9.4.1.3** Test requirements 5497A.16.9.4.2
SA: PRS-RSRPP measurement accuracy with Rx FH in RRC\_INACTIVE state in
FR1 5497**A.16.9.4.2.1** Test purpose and Environment 5497A.16.9.4.2.2
Test parameters 5497**A.16.9.4.2.3** Test requirements 5500A.16.10
Measurement procedure for RedCap in RRC\_IDLE 5500A.16.10.1 RSTD
measurements 5500A.16.10.1.1 NR RSTD measurement reporting delay test
case for RedCap UE without FH in FR1 SA in RRC\_IDLE state without eDRX
5500A.16.10.1.1.1 Test Purpose and Environment 5500A.16.10.1.1.2 Test
Requirements 5504A.16.10.1.2 NR RSTD measurement reporting delay test
case for RedCap UE without RX FH in FR1 SA in RRC\_IDLE state when eDRX
\> 10.24s 5504A.16.10.1.2.1 Test Purpose and Environment
5504A.16.10.1.2.2 Test Requirements 5508A.16.10.2 PRS-RSRP Measurements
5508A.16.10.2.1 PRS-RSRP reporting delay test case for single
positioning frequency layer in RRC\_IDLE 5508A.16.10.2.1.1 Test purpose
and Environment 5508A.16.10.2.1.2 Test Requirements 5510A.16.10.2.2
PRS-RSRP measurement without Rx FH reporting delay test case for single
positioning frequency layer in FR1 SA in RRC\_IDLE state with eDRX cycle
\> 10.24s 5511A.16.10.2.2.1 Test purpose and Environment
5511A.16.10.2.2.2 Test Requirements 5513A.16.11 Measurement Performance
Requirements for RedCap in RRC\_IDLE 5513A.16.11.1 RSTD Measurements
5513A.16.11.1.1 RSTD measurement accuracy test case for RedCap UE
without FH in FR1 in RRC\_IDLE state without eDRX 5513A.16.11.1.1.1 Test
purpose and Environment 5513A.16.11.1.1.2 Test Requirements
5515A.16.11.1.2 RSTD measurement accuracy test case for RedCap UE
without FH in FR1 in RRC\_IDLE state with eDRX \> 10.24s
5516A.16.11.1.2.1 Test purpose and Environment 5516A.16.11.1.2.2 Test
Requirements 5518A.16.11.2 PRS-RSRP Measurements 5518A.16.11.2.1
PRS-RSRP measurement accuracy test case for RedCap UE in FR1 in
RRC\_IDLE state 5518A.16.11.2.1.1 Test Purpose and Environment
5518A.16.11.2.1.2 Test parameters 5518A.16.11.2.1.3 Test Requirements
5520A.16.11.2.2 PRS-RSRP measurement without Rx FH accuracy test case
for single positioning frequency layer in FR1 SA in RRC\_IDLE state with
eDRX cycle \> 10.24s 5520A.16.11.2.2.1 Test purpose and Environment
5520A.16.11.2.2.2 Test Requirements 5522A.17 NR standalone tests with
one or more NR cells in FR2 for RedCap 5524A.17.1 SA: RRC\_IDLE state
mobility for RedCap 5524A.17.1.1 Cell re-selection to NR 5524A.17.1.1.1
Cell reselection to FR2 intra-frequency NR case for 2 Rx
5524A.17.1.1.1.1 Test Purpose and Environment 5524A.17.1.1.1.2 Test
Parameters 5524A.17.1.1.1.3 Test Requirements 5526A.17.1.1.2 Cell
reselection to FR2 inter-frequency NR case 5526A.17.1.1.2.1 Test Purpose
and Environment 5526A.17.1.1.2.2 Test Parameters 5526A.17.1.1.2.3 Test
Requirements 5528A.17.1.1.3 Cell reselection to FR2 intra-frequency NR
case for UE fulfilling stationary relaxed measurement criterion for 2 Rx
UE 5529A.17.1.1.3.1 Test Purpose and Environment 5529A.17.1.1.3.2 Test
Parameters 5529A.17.1.1.3.3 Test Requirements 5531A.17.1.1.4 Cell
reselection to FR2 inter-frequency NR case for UE fulfilling stationary
mobility relaxed measurement criterion for 2 Rx UE 5531A.17.1.1.4.1 Test
Purpose and Environment 5531A.17.1.1.4.2 Test Parameters
5531A.17.1.1.4.3 Test Requirements 5533A.17.2 SA: RRC\_INACTIVE state
mobility for RedCap 5534A.17.2.1 Configured Grant based Small Data
Transmissions (CG-SDT) for RedCap 5534A.17.2.1.1 TA validation for
CG-SDT in FR2 for RedCap 5534A.17.2.1.1.1 Test Purpose and Environment
5534A.17.2.1.1.2 Test Requirements 5537A.17.2.2 Cell Reselection for
Positioning 5537A.17.2.2.1 Cell reselection to FR2 intra-frequency NR
case with RRC\_INACTIVE eDRX and positioning SRS 5537A.17.2.2.1.1 Test
Purpose and Environment 5537A.17.2.2.1.2 Test Parameters
5537A.17.2.2.1.3 Test Requirements 5537A.17.3 RRC\_CONNECTED state
mobility for RedCap 5537A.17.3.1 Handover for RedCap 5537A.17.3.1.1
Intra-frequency handover from FR2 to FR2; unknown target cell for 2 Rx
5537A.17.3.1.1.1 Test Purpose and Environment 5537A.17.3.1.1.2 Test
Parameters 5537A.17.3.1.1.3 Test Requirements 5539A.17.3.1.2
Inter-frequency handover from FR2 to FR2; unknown target cell for 2 Rx
5539A.17.3.1.2.1 Test Purpose and Environment 5539A.17.3.1.2.2 Test
Parameters 5539A.17.3.1.2.3 Test Requirements 5541A.17.3.2 RRC
Connection Mobility Control for RedCap 5541A.17.3.2.1 SA: RRC
Re-establishment 5541A.17.3.2.1.1 Intra-frequency RRC Re-establishment
in FR2 5541A.17.3.2.1.1.1 Test Purpose and Environment 5541A.17.3.2.1.2
Inter-frequency RRC Re-establishment in FR2 5543A.17.3.2.1.2.1 Test
Purpose and Environment 5543A.17.3.2.1.3 Intra-frequency RRC
Re-establishment in FR2 without serving cell timing 5545A.17.3.2.1.3.1
Test Purpose and Environment 5545A.17.3.2.1.3.2 Test Requirements
5547A.17.3.2.2 Random Access 5547A.17.3.2.2.1 4-step RA type contention
based random access test in FR2 for NR Standalone 5547A.17.3.2.2.1.1
Test Purpose and Environment 5547A.17.3.2.2.1.2 Test Requirements
5549A.17.3.2.2.2 4-step RA type non-contention based random access test
in FR2 for NR Standalone 5551A.17.3.2.2.2.1 Test Purpose and Environment
5551A.17.3.2.2.2.2 Test Requirements 5552A.17.3.2.2.3 2-step RA type
contention based random access test in FR2 for NR Standalone
5554A.17.3.2.2.3.1 Test Purpose and Environment 5554A.17.3.2.2.3.2 Test
Requirements 5555A.17.3.2.2.4 2-step RA type non-contention based random
access test in FR2 for NR Standalone 5556A.17.3.2.2.4.1 Test Purpose and
Environment 5556A.17.3.2.2.4.2 Test Requirements 5558A.17.3.2.3 SA: RRC
Connection Release with Redirection 5559A.17.3.2.3.1 Redirection from NR
in FR2 to NR in FR2 5559A.17.3.2.3.1.1 Test Purpose and Environment
5559A.17.3.2.3.1.2 Test Parameters 5559A.17.3.2.3.1.3 Test Requirements
5561A.17.4 Timing 5561A.17.4.1 UE transmit timing 5561A.17.4.1.1 NR UE
Transmit Timing Test for FR2 5561A.17.4.1.1.1 Test Purpose and
environment 5561A.17.4.1.1.2 Test requirements 5563A.17.4.2 UE timer
accuracy 5564A.17.4.3 Timing advance 5564A.17.4.3.1 SA FR2 timing
advance adjustment accuracy 5564A.17.4.3.1.1 Test Purpose and
Environment 5564A.17.4.3.1.2 Test Parameters 5564A.17.4.3.1.3 Test
Requirements 5567A.17.5 Signaling characteristics for RedCap
5567A.17.5.1 Radio link Monitoring for RedCap 5567A.17.5.1.1 Radio Link
Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM
RS in non-DRX mode 5567A.17.5.1.1.1 Test Purpose and Environment
5567A.17.5.1.1.2 Test Requirements 5570A.17.5.1.2 Radio Link Monitoring
In-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX
mode 5570A.17.5.1.2.1 Test Purpose and Environment 5570A.17.5.1.2.2 Test
Requirements 5573A.17.5.1.3 Radio Link Monitoring Out-of-sync Test for
FR2 PCell configured with SSB-based RLM RS in DRX mode 5573A.17.5.1.3.1
Test Purpose and Environment 5573A.17.5.1.3.2 Test Requirements
5576A.17.5.1.4 Radio Link Monitoring In-sync Test for FR2 PCell
configured with SSB-based RLM RS in DRX mode 5576A.17.5.1.4.1 Test
Purpose and Environment 5576A.17.5.1.4.2 Test Requirements
5578A.17.5.1.5 Radio Link Monitoring Out-of-sync Test for FR2 PCell
configured with CSI-RS-based RLM in non-DRX mode 5579A.17.5.1.5.1 Test
Purpose and Environment 5579A.17.5.1.5.2 Test Requirements
5581A.17.5.1.6 Radio Link Monitoring In-sync Test for FR2 PCell
configured with CSI-RS-based RLM in non-DRX mode 5582A.17.5.1.6.1 Test
Purpose and Environment 5582A.17.5.1.6.2 Test Requirements
5584A.17.5.1.7 Radio Link Monitoring Out-of-sync Test for FR2 PCell
configured with CSI-RS-based RLM in DRX mode 5585A.17.5.1.7.1 Test
Purpose and Environment 5585A.17.5.1.7.2 Test Requirements
5587A.17.5.1.8 Radio Link Monitoring In-sync Test for FR2 PCell
configured with CSI-RS-based RLM in DRX mode 5587A.17.5.1.8.1 Test
Purpose and Environment 5587A.17.5.1.8.2 Test Requirements
5590A.17.5.1.9 UE Radio Link Monitoring Scheduling Restrictions on FR2
5591A.17.5.1.9.1 Test Purpose and Environment 5591A.17.5.1.9.2 Test
Requirements 5592A.17.5.2 Beam Failure Detection and Link recovery
procedures 5593A.17.5.2.1 Beam Failure Detection and Link Recovery Test
for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode
5593A.17.5.2.1.1 Test Purpose and Environment 5593A.17.5.2.1.2 Test
Requirements 5595A.17.5.2.2 Beam Failure Detection and Link Recovery
Test for FR2 PCell configured with SSB-based BFD and LR in DRX mode
5596A.17.5.2.2.1 Test Purpose and Environment 5596A.17.5.2.2.2 Test
Requirements 5599A.17.5.2.3 Beam Failure Detection and Link Recovery
Test for FR2 PCell configured with CSI-RS-based BFD and LR in non-DRX
mode 5599A.17.5.2.3.1 Test Purpose and Environment 5599A.17.5.2.3.2 Test
Requirements 5602A.17.5.2.4 Beam Failure Detection and Link Recovery
Test for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode
5602A.17.5.2.4.1 Test Purpose and Environment 5602A.17.5.2.4.2 Test
Requirements 5605A.17.5.2.5 Scheduling availability restriction during
Beam Failure Detection and Link Recovery for FR2 PCell configured with
SSB-based BFD and LR in non-DRX mode for 2 Rx UE 5605A.17.5.2.5.1 Test
Purpose and Environment 5605A.17.5.2.5.2 Test Requirements 5608A.17.5.3
Active BWP switch for RedCap 5609A.17.5.3.1 DCI-based and Timer-based
Active BWP Switch 5609A.17.5.3.1.1 NR FR2 DL active BWP switch with
non-DRX in SA 5609A.17.5.3.1.1.1 Test Purpose and Environment
5609A.17.5.3.1.1.2 Test Requirements 5611A.17.5.3.2 RRC-based Active BWP
Switch 5611A.17.5.3.2.1 NR FR2 DL active BWP switch of PCell with
non-DRX in SA 5611A.17.5.3.2.1.1 Test Purpose and Environment
5611A.17.5.3.2.1.2 Test Requirements 5614A.17.5.4 Active TCI state
switch delay 5614A.17.5.4.1 MAC-CE based active TCI state switch
5614A.17.5.4.1.1 NR PCell FR2 active TCI state switch for a known TCI
state 5614A.17.5.4.1.1.1 Test Purpose and Environment 5614A.17.5.4.1.1.2
Test Requirements 5617A.17.5.4.2 RRC based active TCI state switch
5617A.17.5.4.2.1 NR PCell FR2 active TCI state switch for a known TCI
state 5617A.17.5.4.2.1.1 Test Purpose and Environment 5617A.17.5.4.2.1.2
Test Requirements 5620A.17.5.5 Uplink spatial relation switch delay
5620A.17.5.5.1 MAC-CE based Spatial Relation switch 5620A.17.5.5.1.1 NR
PCell FR2 spatial relation associated with known DL-RS
5620A.17.5.5.1.1.1 Test Purpose and Environment 5620A.17.5.5.1.1.2 Test
Requirements 5622A.17.5.5.2 RRC based spatial relation switch
5623A.17.5.5.2.1 NR PCell FR2 spatial relation switch associated with a
known DL-RS 5623A.17.5.5.2.1.2 Test Requirements 5625A.17.5.6 UE
specific CBW change 5625A.17.5.6.1 NR FR2 UE specific CBW change of
PCell with non-DRX in SA 5625A.17.5.6.1.1 Test Purpose and Environment
5625A.17.5.6.1.2 Test Requirements 5627A.17.6 Measurement procedure for
RedCap 5628A.17.6.1 Intra-frequency Measurements 5628A.17.6.1.1 SA event
triggered reporting test without gap under non-DRX 5628A.17.6.1.1.1 Test
purpose and Environment 5628A.17.6.1.1.2 Test Requirements
5630A.17.6.1.2 SA event triggered reporting test without gap under DRX
5630A.17.6.1.2.1 Test purpose and Environment 5630A.7.6.1.2.2 Test
Requirements 5631A.17.6.1.3 SA event triggered reporting test with
per-UE gaps under non-DRX 5631A.17.6.1.3.1 Test purpose and Environment
5631A.17.6.1.3.2 Test Requirements 5634A.17.6.1.4 SA event triggered
reporting test with per-UE gaps under DRX 5634A.17.6.1.4.1 Test purpose
and Environment 5634A.17.6.1.4.2 Test Requirements 5636A.17.6.2
Inter-frequency Measurements 5637A.17.6.2.1 SA event triggered reporting
tests For FR2 without SSB time index detection when DRX is not used
(PCell in FR2) 5637A.17.6.2.1.1 Test Purpose and Environment
5637A.17.6.2.1.2 Test Requirements 5639A.17.6.2.2 SA event triggered
reporting tests For FR2 without SSB time index detection when DRX is
used (PCell in FR2) 5639A.17.6.2.2.1 Test Purpose and Environment
5639A.17.6.2.2.2 Test Requirements 5641A.17.6.2.3 SA event triggered
reporting tests For FR2 with SSB time index detection when DRX is not
used (PCell in FR2) 5642A.17.6.2.3.1 Test Purpose and Environment
5642A.17.6.2.3.2 Test Requirements 5644A.17.6.2.4 SA event triggered
reporting tests For FR2 with SSB time index detection when DRX is used
(PCell in FR2) for 2 RX UE 5644A.17.6.2.4.1 Test Purpose and Environment
5644A.17.6.2.4.2 Test Requirements 5646A.17.6.3 L1-RSRP measurement for
beam reporting 5647A.17.6.3.1 SSB based L1-RSRP measurement when DRX is
not used 5647A.17.6.3.1.1 Test Purpose and Environment 5647A.17.6.3.1.2
Test parameters 5647A.17.6.3.1.3 Test Requirements 5647A.17.6.3.2 SSB
based L1-RSRP measurement when DRX is used 5647A.17.6.3.2.1 Test Purpose
and Environment 5647A.17.6.3.2.2 Test parameters 5648A.17.6.3.2.3 Test
Requirements 5649A.17.6.3.3 CSI-RS based L1-RSRP measurement when DRX is
not used 5649A.17.6.3.3.1 Test Purpose and Environment 5649A.17.6.3.3.2
Test parameters 5649A.17.6.3.3.3 Test Requirements 5651A.17.6.3.4 CSI-RS
based L1-RSRP measurement when DRX is used 5651A.17.6.3.4.1 Test Purpose
and Environment 5651A.17.6.3.4.2 Test parameters 5652A.7.6.3.3.3 Test
Requirements 5653A.17.6.4.1 SA interfrequency CGI reporting in
autonomous gaps test (PCell in FR2) for 2 RX UE 5653A.17.6.4.1.1 Test
Purpose and Environment 5653A.17.6.4.1.2 Test Requirements 5656A.17.6.5
RSTD measurements 5656A.17.6.5.1 NR RSTD measurement reporting delay
test case for RedCap UE without FH in FR2 SA 5656A.17.6.5.1.1 Test
Purpose and Environment 5656A.17.6.5.1.2 Test Requirements
5663A.17.6.5.2 NR RSTD measurement reporting delay test case with PRS
frequency hopping 5663A.17.6.5.2.1 Test Purpose and Environment
5663A.17.6.5.2.2 Test Requirements 5668A.17.6.6 UE Rx-Tx Measurements
5669A.17.6.6.1 UE Rx-Tx measurement reporting delay for single
positioning frequency layer in FR2 SA without RX FH in RRC\_CONNECTED
mode 5669A.17.6.6.1.1 Test purpose and environment 5669A.17.6.6.1.2 Test
requirements 5673A.17.6.6.2 UE Rx-Tx time difference measurement with Rx
FH for single positioning frequency layer in FR2 SA in RRC\_CONNECTED
state 5673A.17.6.6.2.1 Test purpose and environment 5673A.17.6.6.2.2
Test requirements 5677A.17.6.7 PRS-RSRP measurements 5677A.17.6.7.1
PRS-RSRP measurement delay test case for RedCap positioning without Rx
FH in RRC\_CONNECTED state in FR2 5677A.17.6.7.1.1 PRS-RSRP measurement
delay test case for single positioning frequency layer
5677A.17.6.7.1.1.1 Test Purpose and Environment 5677A.17.6.7.1.1.2 Test
Requirements 5681A.17.6.7.1.2 PRS-RSRP measurement delay test case for
dual positioning frequency layer 5681A.17.6.7.1.2.1 Test Purpose and
Environment 5681A.17.6.7.1.2.2 Test Requirements 5685A.17.6.7.2 PRS-RSRP
measurement delay with FH in RRC\_CONNECTED state in FR2
5685A.17.6.7.2.1 Test Purpose and Environment 5685A.17.6.7.2.2 Test
Requirements 5689A.17.6.8 PRS-RSRPP Measurements 5689A.17.6.8.1
PRS-RSRPP measurement delay without FH in RRC\_CONNECTED state in FR2
5689A.17.6.8.1.1 Test Purpose and Environment 5689A.17.6.8.1.2 Test
Requirements 5692A.17.6.8.2 PRS-RSRPP measurement with Rx FH reporting
delay test case for single positioning frequency layer in FR2 SA in
RRC\_CONNECTED state 5692A.17.6.8.2.1 Test Purpose and Environment
5692A.17.6.8.2.2 Test Requirements 5694A.17.7 Measurement Performance
requirements 5695A.17.7.1 SS-RSRP 5695A.17.7.1.1 SA intra-frequency case
measurement accuracy with FR2 serving cell and FR2 target cell
5695A.17.7.1.1.1 Test Purpose and Environment 5695A.17.7.1.1.2 Test
parameters 5695A.17.7.1.1.3 Test Requirements 5697A.17.7.1.2 SA
inter-frequency case measurement accuracy with FR2 serving cell and FR2
target cell 5697A.17.7.1.2.1 Test Purpose and Environment
5697A.17.7.1.2.2 Test parameters 5697A.17.7.1.2.3 Test Requirements
5699A.17.7.2 SS-RSRQ 5700A.17.7.2.1 SA intra-frequency measurement
accuracy with FR2 serving cell and FR2 target cell 5700A.17.7.2.1.1 Test
Purpose and Environment 5700A.17.7.2.1.2 Test Parameters
5700A.17.7.2.1.3 Test Requirements 5702A.17.7.2.2 SA Inter-frequency
measurement accuracy with FR2 serving cell and FR2 TDD target cell for 2
Rx UE 5702A.17.7.2.2.1 Test Purpose and Environment 5702A.17.7.2.2.2
Test parameters 5702A.17.7.2.2.3 Test Requirements 5704A.17.7.2.3 SA
Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 5704A.17.7.3 L1-RSRP measurement for beam reporting
5704A.17.7.3.1 SSB based L1-RSRP measurement 5704A.17.7.3.1.1 Test
Purpose and Environment 5704A.17.7.3.1.2 Test parameters
5704A.17.7.3.1.3 Test Requirements 5705A.17.7.3.2 CSI-RS based L1-RSRP
measurement on resource set with repetition off 5705A.17.7.3.2.1 Test
Purpose and Environment 5705A.17.7.3.2.2 Test parameters
5705A.17.7.3.2.3 Test Requirements 5705A.17.7.4 SS-SINR 5706A.17.7.4 SA
intra-frequency case measurement accuracy with FR2 serving cell and FR2
target cell for 2Rx UE 5706A.17.7.4.1.1 Test Purpose and Environment
5706A.17.7.4.1.2 Test parameters 5706A.17.7.4.1.3 Test Requirements
5708A.17.7.5 RSTD measurements 5708A.17.7.5.1 RSTD measurement accuracy
test case for RedCap UE without FH 5708A.17.7.5.1.1 Test purpose and
Environment 5708A.17.7.5.1.2 Test Requirements 5710A.17.7.6 UE Rx-Tx
Measurements 5712A.17.7.6.1 UE Rx-Tx measurement accuracy for single
positioning frequency layer in FR2 SA without RX FH in RRC\_CONNECTED
mode 5712A.17.7.6.1.1 Test purpose and environment 5712A.17.7.6.1.2 Test
parameters 5713A.17.7.6.1.3 Test requirements 5716A.17.7.6.2 SA: UE
Rx-Tx time difference measurement accuracy with Rx FH in RRC\_CONNECTED
state in FR2 5716A.17.7.6.2.1 Test purpose and Environment
5716A.17.7.6.2.2 Test parameters 5717A.17.7.6.2.3 Test requirements
5720A.17.7.7 PRS-RSRP Measurements 5720A.17.7.7.1 PRS-RSRP measurement
accuracy without FH in RRC\_CONNECTED state in FR2 5720A.17.7.7.1.1 Test
Purpose and Environment 5720A.17.7.7.1.2 Test parameters
5720A.17.7.7.1.3 Test Requirements 5723A.17.7.7.2 PRS-RSRP measurement
accuracy with FH in RRC\_CONNECTED state in FR2 5723A.17.7.7.2.1 Test
Purpose and Environment 5723A.17.7.7.2.2 Test parameters
5724A.17.7.7.2.3 Test Requirements 5726A.17.7.8 PRS-RSRPP Measurements
5726A.17.7.8.1 PRS-RSRPP measurement accuracy without FH in
RRC\_CONNECTED state in FR2 5726A.17.7.8.1.1 Test Purpose and
Environment 5726A.17.7.8.1.2 Test parameters 5727A.17.7.8.1.3 Test
Requirements 5729A.17.7.8.2 SA: PRS-RSRPP measurement accuracy with Rx
FH in RRC\_CONNECTED state in FR2 5729**A.17.7.8.2.1** Test purpose and
Environment 5729**A.17.7.8.2.2** Test parameters 5730A.17.7.8.2.3 Test
requirements 5732A.17.8 Measurement Procedure for RedCap in
RRC\_INACTIVE 5733A.17.8.1 RSTD Measurements 5733A.17.8.1.1 NR RSTD
measurement reporting delay test case for RedCap UE without FH in FR2 SA
in RRC\_INACTIVE state 5733A.17.8.1.1.1 Test Purpose and Environment
5733A.17.8.1.1.2 Test Requirements 5736A.17.8.1.2 NR RSTD measurement
reporting delay test case for single positioning frequency layer in FR2
SA in RRC\_INACTIVE state 5736A.17.8.1.2.1 Test Purpose and Environment
5736A.17.8.1.2.2 Test Requirements 5739A.17.8.1.3 NR RSTD measurement
reporting delay test case for single positioning frequency layer in FR2
SA in RRC\_INACTIVE state with eDRX \> 10.24s 5739A.17.8.1.3.1 Test
purpose and environment 5739A.17.8.1.3.2 Test requirements 5739A.17.8.2
UE Rx-Tx Measurements 5740A.17.8.2.1 UE Rx-Tx measurement reporting
delay for single positioning frequency layer in FR2 SA without RX FH in
RRC\_INACTIVE mode 5740A.17.8.2.1.1 Test purpose and environment
5740A.17.8.2.1.2 Test requirements 5743A.17.8.2.2 UE Rx-Tx time
difference measurement with Rx FH for single positioning frequency layer
in FR2 SA in RRC\_INACTIVE state 5743A.17.8.2.2.1 Test purpose and
environment 5743A.17.8.2.2.2 Test requirements 5747A.17.8.2.3 UE Rx-Tx
time difference measurements for single positioning frequency layer with
eDRX \> 10.24s in FR2 SA 5747A.17.8.2.3.1 Test purpose and environment
5747A.17.8.2.3.2 Test requirements 5747A.17.8.3 PRS-RSRP Measurements
5748A.17.8.3.1 PRS-RSRP reporting delay test case for single positioning
frequency layer in RRC\_INACTIVE 5748A.17.8.3.1.1 Test Purpose and
Environment 5748A.17.8.3.1.2 Test Requirements 5752A.17.8.3.2.2 Test
Requirements 5756A.17.8.3.3 PRS-RSRP reporting delay in RRC\_INACTIVE
with eDRX 5756A.17.8.3.3.1 Test Purpose and Environment 5756A.17.8.3.3.2
Test Requirements 5760A.17.8.4 PRS-RSRPP Measurements 5760A.17.8.4.1
PRS-RSRPP measurement delay without FH in RRC\_INACTIVE state in FR2
5760A.17.8.4.1.1 Test Purpose and Environment 5760A.17.8.4.2 PRS-RSRPP
measurement with Rx FH reporting delay test case for single positioning
frequency layer in FR2 SA in RRC\_INACTIVE state 5763A.17.8.4.2.1 Test
Purpose and Environment 5763A.17.8.4.2.2 Test Requirements
5765A.17.8.4.3 PRS-RSPP reporting delay in RRC\_INACTIVE state with eDRX
\> 10.24s 5765A.17.8.4.3.1 Test purpose and environment 5765A.17.8.4.3.2
Test requirements 5765A.17.9 Measurement Performance Requirements for
RedCap in RRC\_INACTIVE 5766A.17.9.1 RSTD Measurements 5766A.17.9.1.1
RSTD measurement accuracy test case for RedCap UE without FH in FR2 in
RRC\_INACTIVE state 5766A.17.9.1.1.1 Test purpose and Environment
5766A.17.9.1.1.2 Test Requirements 5768A.17.9.1.2 RSTD measurement
accuracy test case for RedCap UE with FH in FR2 in RRC\_INACTIVE state
5768A.17.9.1.2.1 Test purpose and Environment 5768A.17.9.1.2.2 Test
Requirements 5770A.17.9.2 UE Rx-Tx Measurements 5770A.17.9.2.1 UE Rx-Tx
measurement accuracy for single positioning frequency layer in FR2 SA
without RX FH in RRC\_INACTIVE mode 5770A.17.9.2.1.1 Test purpose and
environment 5770A.17.9.2.1.2 Test parameters 5771A.17.9.2.1.3 Test
requirements 5774A.17.9.2.2 SA: UE Rx-Tx time difference measurement
accuracy with Rx FH in RRC\_INACTIVE state in FR2 5774A.17.9.2.2.1 Test
purpose and Environment 5774A.17.9.2.2.2 Test parameters
5774A.17.9.2.2.3 Test requirements 5777A.17.9.3 PRS-RSRP Measurements
5777A.17.9.3.2 PRS-RSRP measurement accuracy with FH in RRC\_INACTIVE
state in FR2 5779A.17.9.3.2.1 Test Purpose and Environment
5779A.17.9.3.2.2 Test parameters 5780A.17.9.3.2.3 Test Requirements
5781A.17.9.4 PRS-RSRPP Measurements 5781A.17.9.4.1 SA: PRS-RSRPP
measurement accuracy with Rx FH in RRC\_INACTIVE state in FR2
5781A.17.9.4.1.1 Test Purpose and Environment 5781A.17.9.4.1.2 Test
parameters 5782A.17.9.4.1.3 Test Requirements 5784A.17.9.4.2 SA:
PRS-RSRPP measurement accuracy with Rx FH in RRC\_INACTIVE state in FR2
5784A.17.9.4.2.1 Test Purpose and Environment 5784A.17.9.4.2.2 Test
parameters 5785A.17.9.4.2.3 Test Requirements 5787A.17.10 Measurement
Procedure for RedCap in RRC\_IDLE 5788A.17.10.1 RSTD Measurements
5788A.17.10.1.1 NR RSTD measurement reporting delay test case for RedCap
UE without FH in FR2 SA in RRC\_IDLE state without eDRX
5788A.17.10.1.1.1 Test Purpose and Environment 5788A.17.10.1.1.2 Test
Requirements 5791A.17.10.1.2 NR RSTD without FH measurement reporting
delay test case for single positioning frequency layer in FR2 SA in
RRC\_IDLE state with eDRX \> 10.24s 5791A.17.10.1.2.1 Test purpose and
environment 5791A.17.10.1.2.2 Test requirements 5791A.17.10.2 PRS-RSRP
Measurements 5792A.17.10.2.1 PRS-RSRP measurement delay test case for
single positioning frequency layer in RRC\_IDLE 5792A.17.10.2.1.1 Test
Purpose and Environment 5792A.17.10.2.1.2 Test Requirements
5796A.17.10.2.2 PRS-RSRP reporting delay test case in RRC\_IDLE state in
FR2 when eDRX cycle \> 10.24s 5796A.17.10.2.2.1 Test Purpose and
Environment 5796A.17.10.2.2.2 Test Requirements 5796A.17.11 Measurement
Performance Requirements for RedCap in RRC\_IDLE 5797A.17.11.1 RSTD
Measurements 5797A.17.11.1.1 RSTD measurement accuracy test case for
RedCap UE without FH in FR2 in RRC\_IDLE state without eDRX
5797A.17.11.1.1.1 Test purpose and Environment 579711.1.1.2 Test
Requirements 5799A.17.11.1.2 RSTD without FH measurement accuracy test
case for single positioning frequency layer in FR2 SA in RRC\_IDLE state
with eDRX \> 10.24s 5799A.17.11.1.2.1 Test purpose and environment
5799A.17.11.1.2.2 Test requirements 5801A.17.11.2 PRS-RSRP Measurements
5801A.17.11.2.1 PRS-RSRP measurement accuracy test case for RedCap UE in
FR2 in RRC\_IDLE state 5801A.17.11.2.1.1 Test Purpose and Environment
5801A.17.11.2.1.2 Test parameters 5801A.17.11.2.2 PRS-RSRP measurement
accuracy test case in RRC\_IDLE state in FR2 when eDRX cycle \> 10.24s
5803A.17.11.2.2.1 Test purpose and Environment 5803A.17.11.2.2.1 Test
parameters 5804A.17.11.2.2.2 Test Requirements 5804A.18 E-UTRA
standalone tests for NR RRM for RedCap 5804A.18.1 RRC\_IDLE state
mobility 5804A.18.1.1 Inter-RAT NR Cell re-selection 5804A.18.1.1.1
E-UTRA Cell reselection to higher priority NR target Cell in FR1
5804A.18.1.1.1.1 Test Purpose and Environment 5804A.18.1.1.1.2 Test
Requirements 5807A.18.2 RRC\_CONNECTED state mobility 5807A.18.2.1
Handover 5807A.18.2.1.1 E-UTRAN - NR handover in FR1 5807A.18.2.1.1.1
Test Purpose and Environment 5807A.18.2.1.1.2 Test Requirements
5811A.18.2.2 RRC connection release with redirection 5811A.18.2.2.1
Redirection from E-UTRA to NR FR1 for redcap UE 5811A.18.2.2.1.1 Test
Purpose and Environment 5811A.18.2.2.1.2 Test Parameters
5811A.18.2.2.1.3 Test Requirements 5814A.18.3 Measurement procedure
5815A.18.3.1 E-UTRA -- NR Inter-RAT Measurements 5815A.18.3.1.1 NR
Inter-RAT event triggered reporting tests for FR1 without SSB time index
detection when DRX is not used 5815A.18.3.1.1.1 Test Purpose and
Environment 5815A.18.3.1.1.2 Test Requirements 5818A.18.3.1.2 NR
Inter-RAT event triggered reporting tests for FR1 without SSB time index
detection when DRX is used 5818A.18.3.1.2.1 Test Purpose and Environment
5818A.18.3.1.2.2 Test Requirements 5822A.18.3.1.3 NR Inter-RAT event
triggered reporting tests for FR1 with SSB time index detection when DRX
is not used 5822A.18.3.1.3.1 Test Purpose and Environment
5822A.18.3.1.3.2 Test Requirements 5826A.18.3.1.4 NR Inter-RAT event
triggered reporting tests for FR1 with SSB time index detection when DRX
is used 5826A.18.3.1.4.1 Test Purpose and Environment 5826A.18.3.1.4.2
Test Requirements 5830A.18.3.1.5 NR Inter-RAT event triggered reporting
tests for FR2 without SSB time index detection when DRX is not used
5830A.18.3.1.5.1 Test Purpose and Environment 5830A.18.3.1.5.2 Test
Requirements 5832A.18.3.1.6 NR Inter-RAT event triggered reporting tests
for FR2 without SSB time index detection when DRX is used
5832A.18.3.1.6.1 Test Purpose and Environment 5832A.18.3.1.6.2 Test
Requirements 5834A.18.3.1.7 NR Inter-RAT event triggered reporting tests
for FR2 with SSB time index detection when DRX is not used
5835A.18.3.1.7.1 Test Purpose and Environment 5835A.18.3.1.7.2 Test
Requirements 5837A.18.3.1.8 NR Inter-RAT event triggered reporting tests
for FR2 with SSB time index detection when DRX is used 5837A.18.3.1.8.1
Test Purpose and Environment 5837A.18.3.1.8.2 Test Requirements 5839A.19
NR standalone tests for ATG 5840A.19.1 RRC\_IDLE state mobility
5840A.19.1.1 Cell reselection to FR1 intra-frequency NR case
5840A.19.1.1.1 Test Purpose and Environment 5840A.19.1.1.2 Test
Parameters 5840A.19.1.1.3 Test Requirements 5841A.19.1.2 Cell
reselection to FR1 inter-frequency NR case 5841A.19.1.2.1 Test Purpose
and Environment 5841A.19.1.2.2 Test Parameters 5841A.19.1.2.3 Test
Requirements 5843A.19.1.3 Cell reselection to FR1 inter-frequency NR
case for UE configured with *hs-ATG-cellReselectionSet-r18*
5844A.19.1.3.1 Test Purpose and Environment 5844A.19.1.3.2 Test
Parameters 5844A.19.1.3.3 Test Requirements 5846A.19.2 RRC\_CONNECTED
state mobility 5847A.19.2.1 Handover 5847A.19.2.1.1 Intra-frequency
handover from FR1 to FR1; known target cell 5847A19.2.1.1.1 Test Purpose
and Environment 5847A.19.2.1.1.2 Test Parameters 5847A.19.2.1.2.3 Test
Requirements 5847A.19.2.1.2 Inter-frequency handover from FR1 to FR1;
unknown target cell 5848A.19.2.1.2.1 Test Purpose and Environment
5848A.19.2.1.2.2 Test Parameters 5848A.19.2.1.2.3 Test Requirements
5849A.19.2.2 Conditional Handover 5849A.19.2.2.1 Intra-frequency
distance-based conditional Handover from FR1 to FR1 5849A.19.2.2.1.1
Test Purpose and Environment 5849A.19.2.2.1.2 Test Parameters
5849A.19.2.2.1.3 Test Requirements 5851A.19.2.2.2 Inter-frequency
distance-based conditional Handover from FR1 to FR1 5852A.19.2.2.2.1
Test Purpose and Environment 5852A.19.2.2.2.2 Test Parameters
5852A.19.2.2.2.3 Test Requirements 5854A.19.2.3 RRC Connection Mobility
Control 5854A.19.2.3.1 SA: RRC Re-establishment 5854A.19.2.3.1.1
Intra-frequency RRC Re-establishment in FR1 for ATG 5854A.19.2.3.1.1.1
Test Purpose and Environment 5855A.19.2.3.1.1.2 Test Requirements
5855A.19.2.3.1.2 Inter-frequency RRC Re-establishment in FR1 with
unknown target cell without serving cell timing for ATG
5855A.19.2.3.1.2.1 Test Purpose and Environment 5855A.19.2.3.1.2.2 Test
Requirements 5857A.19.2.3.2 Random Access for ATG UE 5858A.19.2.3.2.1.1
Test Purpose and Environment 5858A.19.2.3.2.1.2 Test Requirements
5859A.19.2.3.2.2.1 Test Purpose and Environment 5859A.19.2.3.2.2.2 Test
Requirements 5859A.19.2.3.2.3 2-step RA type contention based random
access test in FR1 for NR standalone 5859A.19.2.3.2.3.1 Test Purpose and
Environment 5859A.19.2.3.2.3.2 Test Requirements 5860A.19.2.3.2.4 2-step
RA type non-contention based test in FR1 for NR standalone
5860A.19.2.3.2.4.1 Test Purpose and Environment 5860A.19.2.3.2.4.2 Test
Requirements 5861A.19.2.3.3.1.1 Test Purpose and Environment
5861A.19.2.3.3.1.2 Test Parameters 5861A.19.2.3.3.1.3 Test Requirements
5862A.19.3 Timing 5862A.19.3.1 UE transmit timing 5862A.19.3.1.1 ATG UE
Transmit Timing Test for FR1 5862A.19.3.1.1.1 Test Purpose and
environment 5862A.19.3.1.1.2 Test requirements 5864A.19.3.2 UE timer
accuracy 5864A.19.3.3 Timing advance 5864A.19.3.3.1 SA FR1 timing
advance adjustment accuracy 5864A.19.3.3.1.1 Test Purpose and
Environment 5864A.19.3.3.1.2 Test Parameters 5864A.19.3.3.1.3 Test
Requirements 5865A.19.4 Signalling characteristics 5865A.19.4.1 Radio
link Monitoring 5865A.19.4.1.1 Radio Link Monitoring Out-of-sync Test
for FR1 PCell configured with SSB-based RLM RS in non-DRX mode
5865A.19.4.1.1.1 Test Purpose and Environment 5866A.19.4.1.1.2 Test
Requirements 5868A.19.4.1.2 Radio Link Monitoring In-sync Test for FR1
PCell configured with SSB-based RLM RS in non-DRX mode 5868A.19.4.1.2.1
Test Purpose and Environment 5868A.19.4.1.2.2 Test Requirements
5871A.19.4.1.3 Radio Link Monitoring Out-of-sync Test for FR1 PCell
configured with CSI-RS-based RLM in non-DRX mode 5871A.19.4.1.3.1 Test
Purpose and Environment 5871A.19.4.1.3.2 Test Requirements
5874A.19.4.1.4 Radio Link Monitoring In-sync Test for FR1 PCell
configured with CSI-RS-based RLM in non-DRX mode 5875A.19.4.1.4.1 Test
Purpose and Environment 5875A.19.4.1.4.2 Test Requirements 5878A.19.4.2
Beam Failure Detection and Link recovery procedures 5878A.19.4.2.1 Beam
Failure Detection and Link Recovery Test for FR1 PCell configured with
SSB-based BFD and LR in non-DRX mode 5878A.19.4.2.1.1 Test Purpose and
Environment 5878A.19.4.2.1.2 Test Requirements 5882A.19.4.2.2 Beam
Failure Detection and Link Recovery Test for FR1 PCell configured with
CSI-RS-based BFD and LR in non-DRX mode 5882A.19.4.2.2.1 Test Purpose
and Environment 5882A.19.4.2.2.2 Test Requirements 5886A.19.4.3 Active
BWP switch 5886A.19.4.3.1 DCI-based and Timer-based Active BWP Switch
5886A.19.4.3.1.1 NR FR1 DL active BWP switch with non-DRX in SA
5886A.19.4.3.2 RRC-based Active BWP Switch 5889A.19.4.3.2.1 NR FR1 DL
active BWP switch of Cell with non-DRX in SA 5889A.19.4.4 UE specific
CBW change 5891A19.4.4.1 UE specific CBW change on PCell in FR1 in
non-DRX 5891A19.4.4.1.1 Test Purpose and Environment 5891A.19.4.4.1.2
Test Requirements 5894A.19.4.5 Pathloss reference signal switching delay
5894A.19.4.5.1 MAC-CE based pathloss reference signal switch delay
5894A.19.4.5.1.1 Test Purpose and Environment 5894A.19.4.5.1.2 Test
Requirements 5896A.19.5 Measurement procedure 5897A.19.5.1
Intra-frequency Measurements 5897A.19.5.1.1 SA event triggered reporting
tests without gap without SSB index reading under non-DRX
5897A.19.5.1.1.1 Test purpose and Environment 5897A.19.5.1.1.2 Test
parameters 5897A.19.5.1.1.3 Test Requirements 5897A.19.5.1.2 SA event
triggered reporting tests with per-UE gaps under non-DRX
5898A.19.5.1.2.1 Test purpose and Environment 5898A.19.5.1.2.2 Test
parameters 5898A.19.5.1.2.3 Test Requirements 5898A.19.5.1.3 SA event
triggered reporting tests without gap under non-DRX with SSB index
reading 5898A.19.5.1.3.1 Test purpose and Environment 5898A.19.5.1.3.2
Test parameters 5898A.19.5.1.3.3 Test Requirements 5899A.19.5.1.4 SA
event triggered reporting tests with per-UE gaps under non-DRX with SSB
index reading 5899A.19.5.1.4.1 Test purpose and Environment
5899A.19.5.1.4.2 Test parameters 5899A.19.5.1.4.3 Test Requirements
5900A.19.5.2 Inter-frequency Measurements 5900A.19.5.2.1.2 Test
parameters 5900A.19.5.2.1.3 Test Requirements 5901A.19.5.2.2.2 Test
parameters 5902A.19.5.2.3.2 Test parameters 5902A.19.5.2.3.3 Test
Requirements 5903A.19.5.3 L1-RSRP measurement for beam reporting for ATG
5903A.19.5.3.1 SSB based L1-RSRP measurement when DRX is not used
5903A.19.5.3.1.1 Test Purpose and Environment 5903A.19.5.3.1.2 Test
parameters 5903A.19.5.3.1.3 Test Requirements 5904A.19.5.3.2 CSI-RS
based L1-RSRP measurement when DRX is not used 5904A.19.5.3.2.1 Test
Purpose and Environment 5904A.19.5.3.2.2 Test parameters
5904A.19.5.3.2.3 Test Requirements 5904A.19.5.4 L1-SINR measurement for
beam reporting for ATG 5904A.19.5.4.1 L1-SINR measurement with CSI-RS
based CMR and no dedicated IMR configured when DRX is not used
5904A.19.5.4.1.3 Test Requirements 5905A.19.5.4.2 L1-SINR measurement
with SSB based CMR and dedicated IMR when DRX is not used
5905A.19.5.4.2.1 Test Purpose and Environment 5905A.19.5.4.2.2 Test
parameters 5905A.19.5.4.2.3 Test Requirements 5906A.19.5.4.3 L1-SINR
measurement with CSI-RS based CMR and dedicated IMR configured when DRX
is not used 5906A.19.5.4.3.1 Test Purpose and Environment
5906A.19.5.4.3.2 Test parameters 5906A.19.5.4.3.3 Test Requirements
5906A.19.5.5 NR measurements with autonomous gaps for ATG 5907A.19.5.5.1
SA intra-frequency CGI identification of NR neighbor cell in FR1
5907A.19.5.5.1.1 Test Purpose and Environment 5907A.19.5.5.1.2 Test
Parameters 5907A.19.5.5.1.3 Test Requirements 5907A.19.6 Measurement
Performance requirements 5907A.19.6.1 SS-RSRP for ATG UE 5908A.19.6.1.1
SA: intra-frequency case measurement accuracy with FR1 serving cell and
FR1 target cell 5908A.19.6.1.1.1 Test Purpose and Environment
5908A.19.6.1.1.2 Test parameters 5908A.19.6.1.1.3 Test Requirements
5908A.19.6.1.2 SA inter-frequency case measurement accuracy with FR1
serving cell and FR1 target cell 5908A.19.6.1.2.1 Test Purpose and
Environment 5908A.19.6.1.2.2 Test parameters 5909A.19.6.1.2.3 Test
Requirements 5909A.19.6.2 SS-RSRQ for ATG UE 5909A.19.6.2.1 SA:
Intra-frequency measurement accuracy with FR1 serving cell and FR1
target cell 5909A.19.6.2.1.1 Test Purpose and Environment
5909A.19.6.2.1.2 Test Parameters 5909A.19.6.2.1.3 Test Requirements
5910A.19.6.2.2 SA Inter-frequency measurement accuracy with FR1 serving
cell and FR1 target cell 5910A.19.6.2.2.1 Test Purpose and Environment
5910A.19.6.2.2.2 Test Parameters 5910A.19.6.2.2.3 Test Requirements
5910A.19.6.3 SS-SINR for ATG UE 5911A.19.6.3.1 SA intra-frequency
measurement accuracy with FR1 serving cell and FR1 target cell
5911A.19.6.3.1.1 Test Purpose and Environment 5911A.19.6.3.1.2 Test
Parameters 5911A.19.6.3.1.3 Test Requirements 5911A.19.6.3.2 SA
Inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell 5911A.19.6.3.2.1 Test Purpose and Environment
5911A.19.6.3.2.2 Test Parameters 5911A.19.6.3.2.3 Test Requirements
5912A.19.6.4 L1-RSRP measurement for beam reporting for ATG UE
5912A.19.6.4.1 SSB based L1-RSRP measurement 5912A.19.6.4.1.1 Test
Purpose and Environment 5912A.19.6.4.1.2 Test parameters
5912A.19.6.4.1.3 Test Requirements 5913A.19.6.4.2 CSI-RS based L1-RSRP
measurement on resource set with repetition off 5913A.19.6.4.2.1 Test
Purpose and Environment 5913A.19.6.4.2.2 Test parameters
5913A.19.6.4.2.3 Test Requirements 5913A.19.6.5 L1-SINR measurement for
beam reporting based CMR for ATG UE 5914A.19.6.5.1 L1-SINR measurement
with CSI-RS based CMR and no dedicated IMR configured and CSI-RS
resource set with repetition off 5914A.19.6.5.1.1 Test Purpose and
Environment 5914A.19.6.5.1.2 Test parameters 5914A.19.6.5.1.3 Test
Requirements 5914A.19.6.5.2 L1-SINR measurement with SSB based CMR and
dedicated IMR 5914A.19.6.5.2.1 Test Purpose and Environment
5914A.19.6.5.2.2 Test parameters 5915A.19.6.5.2.3 Test Requirements
5915A.19.6.5.3 L1-SINR measurement with CSI-RS based CMR and dedicated
IMR 5915A.19.6.5.3.1 Test Purpose and Environment 5915A.19.6.5.3.2 Test
parameters 5915A.19.6.5.3.3 Test Requirements 5916A.19.6.6 CSI-RSRP for
ATG UE 5916A.19.6.6.1 SA: intra-frequency case measurement accuracy with
FR1 serving cell and FR1 target cell 5916A.19.6.6.1.1 Test Purpose and
Environment 5916A.19.6.6.1.2 Test parameters 5916A.19.6.6.1.3 Test
Requirements 5916A.19.6.6.2 SA inter-frequency case measurement accuracy
with FR1 serving cell and FR1 target cell 5917A.19.6.6.2.1 Test Purpose
and Environment 5917A.19.6.6.2.2 Test parameters 5917A.19.6.6.2.3 Test
Requirements 5917A.19.6.7 CSI-RSRQ for ATG UE 5917A.19.6.7.1 SA:
Intra-frequency measurement accuracy with FR1 serving cell and FR1
target cell 5917A.19.6.7.1.1 Test Purpose and Environment
5917A.19.6.7.1.2 Test Parameters 5917A.19.6.7.1.3 Test Requirements
5918A.19.6.7.2 SA Inter-frequency measurement accuracy with FR1 serving
cell and FR1 target cell 5918A.19.6.7.2.1 Test Purpose and Environment
5918A.19.6.7.2.2 Test Parameters 5918A.19.6.7.2.3 Test Requirements
5919A.19.6.8 CSI-SINR for ATG UE 5919A.19.6.8.1 SA intra-frequency
measurement accuracy with FR1 serving cell and FR1 target cell
5919A.19.6.8.1.1 Test Purpose and Environment 5919A.19.6.8.1.2 Test
Parameters 5919A.19.6.8.1.3 Test Requirements 5919A.19.6.8.2 SA
Inter-frequency measurement accuracy with FR1 serving cell and FR1
target cell 5920A.19.6.8.2.1 Test Purpose and Environment
5920A.19.6.8.2.2 Test Parameters 5920A.19.6.8.2.3 Test Requirements
5920Annex B (normative): Conditions for RRM requirements applicability
for operating bands 5922B.1 Conditions for NR RRC\_IDLE state mobility
5922B.1.1 Introduction 5922B.1.2 Conditions for measurements on NR
intra-frequency cells for cell re-selection 5922B.1.2A Conditions for
measurements on NR intra-frequency cells under CCA for cell re-selection
5924B.1.3 Conditions for measurements on NR inter-frequency cells for
cell re-selection 5925B.1.3A Conditions for measurements on NR
inter-frequency cells under CCA for cell re-selection 5925B.1.4
Conditions for measurements on NR intra-frequency cells for cell
re-selection for RedCap 5925B.1.5 Conditions for measurements on NR
inter-frequency cells for cell re-selection for RedCap 5928B.1.6
Conditions for measurements on NR intra-frequency cells for cell
re-selection for satellite access 5928B.1.7 Conditions for measurements
on NR inter-frequency cells for cell re-selection for satellite access
5928B.2 Conditions for UE measurements procedures and performance
requirements in RRC\_CONNECTED state 5928B.2.1 Introduction 5928B.2.1.1
General 5928B.2.1.2 Derivation of Minimum SSB\_RP values for FR1
5929B.2.1.3 Derivation of Minimum SSB\_RP values for FR2 5929B.2.1.3.1
Minimum SSB\_RP values for Rx Beam Peak angle of arrival 5929B.2.1.3.2
Minimum SSB\_RP values for angle of arrival within Spherical coverage
5930B.2.1.4 Gain to SS-RSRP and CSI-RSRP measurement point for FR1
5930B.2.1.5 Gain to SS-RSRP and CSI-RSRP measurement point for FR2
5930B.2.1.5.1 Gain to SS-RSRP and CSI-RSRP measurement point for Rx Beam
Peak angle of arrival 5930B.2.1.5.2 Gain to SS-RSRP measurement point
for different frequency 5931B.2.1.5.3 Alignment of Rough beam to Rx beam
Peak 5931B.2.1.6 Gain to PRS-RSRP measurement point for FR2
5932B.2.1.6.1 Gain to PRS-RSRP measurement point for Rx Beam Peak angle
of arrival 5932B.2.1.7 Derivation of Minimum SSB\_RP values for FR2-NTN
for satellite access 5932B.2.1.7.1 Minimum SSB\_RP values for Rx Beam
5932B.2.1.8 Gain to SS-RSRP for FR2-NTN for satellite access 5933B.2.2
Conditions for NR intra-frequency measurements 5934B.2.3 Conditions for
NR inter-frequency measurements 5936B.2.4 Conditions for NR L1-RSRP
reporting 5938B.2.4.1 Conditions for SSB based L1-RSRP reporting
5938B.2.4.2 Conditions for CSI-RS based L1-RSRP reporting 5940B.2.5
Conditions for RRC connection release with redirection to NR 5942B.2.6
Void 5944B.2.6.1 Void 5944B.2.6.2 Void 5944B.2.7 Conditions for SRS-RSRP
measurements 5944B.2.8 Conditions for NR L1-SINR reporting 5945B.2.8.1
Conditions for L1-SINR reporting with CSI-RS based CMR and no dedicated
IMR configured 5945B.2.8.2 Conditions for L1-SINR reporting with SSB
based CMR and dedicated IMR configured 5947B.2.8.2.1 L1-SINR reporting
with SSB based CMR and dedicated ZP-IMR configured 5947B.2.8.2.2 L1-SINR
reporting with SSB based CMR and dedicated NZP-IMR configured
5949B.2.8.3 Conditions for L1-SINR reporting with CSI-RS based CMR and
dedicated IMR configured 5951B.2.8.3.1 L1-SINR reporting with CSI-RS
based CMR and dedicated ZP-IMR configured 5951B.2.8.3.2 L1-SINR
reporting with CSI-RS based CMR and dedicated NZP-IMR configured
5953B.2.9 Conditions for NR intra-frequency measurements under CCA
5955B.2.10 Conditions for NR inter-frequency measurements under CCA
5955B.2.11 Conditions for NR L1-RSRP reporting under CCA 5955B.2.11.1
Conditions for SSB based L1-RSRP reporting 5955B.2.12 Conditions for NR
CSI-RS based intra-frequency measurements 5956B.2.13 Conditions for NR
CSI-RS based inter-frequency measurements 5957B.2.14 Conditions for NR
PRS-based measurements 5958B.2.15 Conditions for NR intra-frequency
measurements for RedCap 5960B.2.16 Conditions for NR inter-frequency
measurements for RedCap 5961B.2.17 Conditions for NR intra-frequency
measurements for satellite access 5963B.2.18 Conditions for NR
inter-frequency measurements for satellite access 5963B.2.19 Conditions
for NR L1-RSRP reporting for satellite access 5963B.2.19.1 Conditions
for SSB based L1-RSRP reporting for satellite access 5964B.2.19.2
Conditions for CSI-RS based L1-RSRP reporting for satellite access
5964B.2.20 Conditions for RRC connection release with redirection to NR
for satellite access 5964B.3 RRM Requirements Exceptions 5964B.3.1
Introduction 5964B.3.2 Receiver sensitivity relaxation for CA
5965B.3.2.1 Receiver sensitivity relaxation for UE supporting CA in FR1
5965B.3.2.2 Receiver sensitivity relaxation for UE configured with CA in
FR1 5965B.3.2.2.1 Inter-band carrier aggregation 5965B.3.2.2.2 Reference
sensitivity exceptions due to UL harmonic interference for CA
5965B.3.2.2.3 Reference sensitivity exceptions due to intermodulation
interference due to 2UL CA 5965B.3.2.3 Receiver sensitivity relaxation
for UE supporting CA in FR2 5965B.3.2.4 Receiver sensitivity relaxation
for UE configured with CA in FR2 5966B.3.2.4.1 Intra-band contiguous
carrier aggregation 5966B.3.2.4.2 Intra-band non-contiguous carrier
aggregation 5966B.3.3 Receiver sensitivity relaxation for DC 5966B.3.3.1
Receiver sensitivity relaxation for EN-DC 5966B.3.3.2 Receiver
sensitivity relaxation for NE-DC 5966B.3.4 Receiver sensitivity
relaxation for SUL 5966B.3.4.1 Receiver sensitivity relaxation for UE
supporting SUL in FR1 5966B.3.4.2 Receiver sensitivity relaxation for UE
configured with SUL in FR1 5966B.3.4.2.1 Reference sensitivity
exceptions due to UL harmonic interference for SUL 5966B.4 Conditions
for V2X 5967B.4.1 Test parameters for GNSS signals 5967B.4.2 Conditions
for PSBCH-RSRP Accuracy Requirements 5967B.4.3 Conditions for
Selection/Reselection to Intra-frequency SyncRef UE 5967B.4.4 Conditions
for L1 SL-RSRP Accuracy Requirements 5968B.4.5 Conditions for PSBCH-RSRP
Accuracy Requirements under CCA 5968B.4.6 Conditions for
Selection/Reselection to Intra-frequency SyncRef UE under CCA 5968B.4.7
Conditions for L1 SL-RSRP Accuracy Requirements under CCA 5969B.4A
Conditions for NR Sidelink Positioning Measurement Procedures and
Performance Requirements 5969B.4A.1 Conditions for NR SL-PRS based
measurements 5969B.5 High level test procedure for SAN RRM tests
5969Annex C (informative): Change history 5971
