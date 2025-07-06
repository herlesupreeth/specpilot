3GPP TS 38.133 V15.30.0 (2025-06)

Technical Specification

3rd Generation Partnership Project;

Technical Specification Group Radio Access Network;

NR;

Requirements for support of radio resource management

(Release 15)

![5G-logo\_175px](./media/image1.jpeg){width="1.3229166666666667in"
height="0.9166666666666666in"}
![3GPP-logo\_web](./media/image2.png){width="1.78125in"
height="1.0416666666666667in"}

The present document has been developed within the 3rd Generation
Partnership Project (3GPP ^TM^) and may be further elaborated for the
purposes of 3GPP..\
The present document has not been subject to any approval process by the
3GPP Organizational Partners and shall not be implemented.\
This Specification is provided for future development work within 3GPP
only. The Organizational Partners accept no liability for any use of
this Specification.\
Specifications and Reports for implementation of the 3GPP ^TM^ system
should be obtained via the 3GPP Organizational Partners\' Publications
Offices.

> ***3GPP***
>
> Postal address
>
> 3GPP support office address
>
> 650 Route des Lucioles - Sophia Antipolis
>
> Valbonne - FRANCE
>
> Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16
>
> Internet
>
> http://www.3gpp.org

***Copyright Notification***

No part may be reproduced except as authorized by written permission.\
The copyright and the foregoing restriction extend to reproduction in
all media.

© 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI,
TTA, TTC).

All rights reserved.

UMTS™ is a Trade Mark of ETSI registered for the benefit of its members

3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members
and of the 3GPP Organizational Partners\
LTE™ is a Trade Mark of ETSI registered for the benefit of its Members
and of the 3GPP Organizational Partners

GSM® and the GSM logo are registered and owned by the GSM Association

 Contents {#contents .TT}
========

Foreword 301 Scope 312 References 313 Definitions, symbols and
abbreviations 323.1 Definitions 323.2 Symbols 333.3 Abbreviations 343.4
Test tolerances 363.5 Frequency bands grouping 363.5.1 Introduction
363.5.2 NR operating bands in FR1 363.5.3 NR operating bands in FR2
363.6 Applicability of requirements in this specification version
373.6.1 RRC connected state requirements in DRX 373.6.2 Number of
serving carriers 383.6.2.1 Number of serving carriers for SA 383.6.2.2
Number of serving carriers for EN-DC 383.6.2.3 Number of serving
carriers for NE-DC 383.6.2.4 Number of serving carriers for NR-DC
383.6.3 Applicability for intra-band FR2 383.6.4 Applicability for FR2
UE power classes 393.6.5 Applicability for SDL bands 393.6.6
Applicability of requirements for NGEN-DC operation 393.6.7
Applicability of QCL 394 SA: RRC\_IDLE state mobility 394.1 Cell
Selection 394.2 Cell Re-selection 394.2.1 Introduction 394.2.2
Requirements 404.2.2.1 UE measurement capability 404.2.2.2 Measurement
and evaluation of serving cell 404.2.2.3 Measurements of intra-frequency
NR cells 404.2.2.4 Measurements of inter-frequency NR cells 414.2.2.5
Measurements of inter-RAT E-UTRAN cells 434.2.2.6 Maximum interruption
in paging reception 444.2.2.7 General requirements 445 SA: RRC\_INACTIVE
state mobility 455.1 Cell Re-selection 455.1.1 Introduction 455.1.2
Requirements 455.1.2.1 UE measurement capability 455.1.2.2 Measurement
and evaluation of serving cell 455.1.2.3 Measurements of intra-frequency
NR cells 455.1.2.4 Measurements of inter-frequency NR cells 455.1.2.5
Measurements of inter-RAT E-UTRAN cells 455.1.2.6 Maximum interruption
in paging reception 455.1.2.7 General requirements 455.2 Void 466
RRC\_CONNECTED state mobility 466.1 Handover 466.1.1 NR Handover
466.1.1.1 Introduction 466.1.1.2 NR FR1 - NR FR1 Handover 466.1.1.2.1
Handover delay 466.1.1.2.2 Interruption time 466.1.1.3 NR FR2- NR FR1
Handover 476.1.1.3.1 Handover delay 476.1.1.3.2 Interruption time
476.1.1.4 NR FR2- NR FR2 Handover 486.1.1.4.1 Handover delay 486.1.1.4.2
Interruption time 486.1.1.5 NR FR1- NR FR2 Handover 496.1.1.5.1 Handover
delay 496.1.1.5.2 Interruption time 496.1.2 NR Handover to other RATs
506.1.2.1 NR -- E-UTRAN Handover 506.1.2.1.1 Introduction 506.1.2.1.2
Handover delay 506.1.2.1.3 Interruption time 506.2 RRC Connection
Mobility Control 516.2.1 SA: RRC Re-establishment 516.2.1.1 Introduction
516.2.1.2 Requirements 516.2.1.2.1 UE Re-establishment delay requirement
516.2.2 Random access 526.2.2.1 Introduction 526.2.2.2 Requirements
526.2.2.2.1 Contention based random access 536.2.2.2.2 Non-Contention
based random access 546.2.2.2.3 UE behaviour when configured with
supplementary UL 556.2.3 SA: RRC Connection Release with Redirection
556.2.3.1 Introduction 556.2.3.2 Requirements 556.2.3.2.1 RRC connection
release with redirection to NR 556.2.3.2.2 RRC connection release with
redirection to E-UTRAN 567 Timing 567.1 UE transmit timing 567.1.1
Introduction 567.1.2 Requirements 567.1.2.1 Gradual timing adjustment
577.1.2.2 Void 587.2 UE timer accuracy 587.2.1 Introduction 587.2.2
Requirements 587.3 Timing advance 587.3.1 Introduction 587.3.2
Requirements 597.3.2.1 Timing Advance adjustment delay 597.3.2.2 Timing
Advance adjustment accuracy 597.4 Cell phase synchronization accuracy
597.4.1 Definition 597.4.2 Minimum requirements 597.5 Maximum
Transmission Timing Difference 597.5.1 Introduction 597.5.2 Minimum
Requirements for inter-band EN-DC 597.5.2.1 Minimum Requirements for
inter-band synchronous EN-DC 607.5.3 Minimum Requirements for intra-band
EN-DC 607.5.4 Minimum Requirements for NR Carrier Aggregation 617.5.5
Minimum Requirements for inter-band NE-DC 617.5.5.1 Minimum Requirements
for inter-band synchronous NE-DC 617.5.6 Minimum Requirements for
inter-band NR DC 627.6 Maximum Receive Timing Difference 627.6.1
Introduction 627.6.2 Minimum Requirements for inter-band EN-DC 627.6.2.1
Minimum Requirements for inter-band synchronous EN-DC 637.6.3 Minimum
Requirements for intra-band EN-DC 637.6.4 Minimum Requirements for NR
Carrier Aggregation 647.6.5 Minimum Requirements for inter-band NE-DC
647.6.5.1 Minimum Requirements for inter-band synchronous NE-DC 657.6.6
Minimum Requirements for inter-band NR DC 657.7
*deriveSSB-IndexFromCell* tolerance 657.7.1 Minimum requirements 657.8
Void 668 Signalling characteristics 668.1 Radio Link Monitoring 668.1.1
Introduction 668.1.2 Requirements for SSB based radio link monitoring
678.1.2.1 Introduction 678.1.2.2 Minimum requirement 688.1.2.3
Measurement restrictions for SSB based RLM 698.1.3 Requirements for
CSI-RS based radio link monitoring 708.1.3.1 Introduction 708.1.3.2
Minimum requirement 708.1.3.3 Measurement restrictions for CSI-RS based
RLM 728.1.4 Minimum requirement at transitions 738.1.5 Minimum
requirement for UE turning off the transmitter 738.1.6 Minimum
requirement for L1 indication 738.1.7 Scheduling availability of UE
during radio link monitoring 748.1.7.1 Scheduling availability of UE
performing radio link monitoring with a same subcarrier spacing as
PDSCH/PDCCH on FR1 748.1.7.2 Scheduling availability of UE performing
radio link monitoring with a different subcarrier spacing than
PDSCH/PDCCH on FR1 748.1.7.3 Scheduling availability of UE performing
radio link monitoring on FR2 748.1.7.4 Scheduling availability of UE
performing radio link monitoring on FR1 or FR2 in case of FR1-FR2
inter-band CA and NR-DC 758.2 Interruption 758.2.1 EN-DC Interruption
758.2.1.1 Introduction 758.2.1.2 Requirements 768.2.1.2.1 Interruptions
at transitions between active and non-active during DRX 768.2.1.2.2
Interruptions at transitions from non-DRX to DRX 768.2.1.2.3
Interruptions at SCell addition/release 768.2.1.2.4 Interruptions at
SCell activation/deactivation 778.2.1.2.5 Interruptions during
measurements on SCC 788.2.1.2.6 Interruptions at UL carrier RRC
reconfiguration 798.2.1.2.7 Interruptions due to Active BWP switching
Requirement 798.2.2 SA: Interruptions with Standalone NR Carrier
Aggregation 808.2.2.1 Introduction 808.2.2.2 Requirements 808.2.2.2.1
Interruptions at SCell addition/release 808.2.2.2.2 Interruptions at
SCell activation/deactivation 818.2.2.2.3 Interruptions during
measurements on deactivated SCC 828.2.2.2.4 Interruptions at UL carrier
RRC reconfiguration 828.2.2.2.5 Interruptions due to Active BWP
switching Requirement 838.2.2.2.6 Interruptions at inter-frequency SFTD
measurement 848.2.3 NE-DC Interruptions 858.2.3.1 Introduction 858.2.3.2
Requirements 858.2.3.2.1 Interruptions at transitions between active and
non-active during DRX 858.2.3.2.2 Interruptions at transitions from
non-DRX to DRX 868.2.3.2.3 Interruptions at PSCell/SCell
addition/release 868.2.3.2.4 Interruptions at SCell
activation/deactivation 878.2.3.2.5 Interruptions during measurements on
SCC 888.2.3.2.6 Interruptions at UL carrier RRC reconfiguration
898.2.3.2.7 Interruptions due to Active BWP switching Requirement
898.2.4 NR-DC: Interruptions 898.2.4.1 Introduction 898.2.4.2
Requirements 908.2.4.2.1 Interruptions at PSCell/SCell addition/release
908.2.4.2.2 Interruptions at SCell activation/deactivation 908.2.4.2.3
Interruptions during measurements on SCC 918.2.4.2.4 Interruptions at UL
carrier RRC reconfiguration 918.2.4.2.5 Interruptions due to Active BWP
switching Requirement 928.2.4.2.6 Interruptions at transitions between
active and non-active during DRX 928.2.4.2.7 Interruptions at
transitions from non-DRX to DRX 928.3 SCell Activation and Deactivation
Delay 928.3.1 Introduction 928.3.2 SCell Activation Delay Requirement
for Deactivated SCell 938.3.3 SCell Deactivation Delay Requirement for
Activated SCell 968.4 UE UL carrier RRC reconfiguration delay 978.4.1
Introduction 978.4.2 UE UL carrier configuration delay requirement
978.4.3 UE UL carrier deconfiguration delay requirement 978.5 Link
Recovery Procedures 978.5.1 Introduction 978.5.2 Requirements for SSB
based beam failure detection 988.5.2.1 Introduction 988.5.2.2 Minimum
requirement 988.5.2.3 Measurement restriction for SSB based beam failure
detection 1008.5.3 Requirements for CSI-RS based beam failure detection
1008.5.3.1 Introduction 1008.5.3.2 Minimum requirement 1018.5.3.3
Measurement restrictions for CSI-RS beam failure detection 1038.5.4
Minimum requirement for L1 indication 1038.5.5 Requirements for SSB
based candidate beam detection 1048.5.5.1 Introduction 1048.5.5.2
Minimum requirement 1048.5.5.3 Measurement restriction for SSB based
candidate beam detection 1068.5.6 Requirements for CSI-RS based
candidate beam detection 1068.5.6.1 Introduction 1068.5.6.2 Minimum
requirement 1068.5.6.3 Measurement restriction for CSI-RS based
candidate beam detection 1088.5.7 Scheduling availability of UE during
beam failure detection 1098.5.7.1 Scheduling availability of UE
performing beam failure detection with a same subcarrier spacing as
PDSCH/PDCCH on FR1 1098.5.7.2 Scheduling availability of UE performing
beam failure detection with a different subcarrier spacing than
PDSCH/PDCCH on FR1 1098.5.7.3 Scheduling availability of UE performing
beam failure detection on FR2 1098.5.7.4 Scheduling availability of UE
performing beam failure detection on FR1 or FR2 in case of FR1-FR2
inter-band CA and NR DC 1108.5.8 Scheduling availability of UE during
candidate beam detection 1108.5.8.1 Scheduling availability of UE
performing L1-RSRP measurement with a same subcarrier spacing as
PDSCH/PDCCH on FR1 1108.5.8.2 Scheduling availability of UE performing
L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH
on FR1 1108.5.8.3 Scheduling availability of UE performing L1-RSRP
measurement on FR2 1108.5.8.4 Scheduling availability of UE performing
L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA and
NR-DC 1118.5.9 Minimum requirement at transitions for beam failure
detection 1118.6 Active BWP switch delay 1118.6.1 Introduction 1118.6.2
DCI and timer based BWP switch delay 1118.6.3 RRC based BWP switch delay
1128.7 Void 1138.8 NE-DC: E-UTRAN PSCell Addition and Release Delay
1138.8.1 Introduction 1138.8.2 E-UTRAN PSCell Addition Delay Requirement
1138.8.3 E-UTRAN PSCell Release Delay Requirement 1148.9 NR-DC: PSCell
Addition and Release Delay 1148.9.1 Introduction 1148.9.2 PSCell
Addition Delay Requirement 1148.9.3 PSCell Release Delay Requirement
1158.10 Active TCI state switching delay 1158.10.6 Active TCI state list
update delay 1178.11 PSCell Change 1179 Measurement Procedure 1189.1
General measurement requirement 1189.1.1 Introduction 1189.1.2
Measurement gap 1189.1.2.1 EN-DC: Measurement Gap Sharing 1259.1.2.1a
SA: Measurement Gap Sharing 1269.1.2.1b NE-DC: Measurement Gap Sharing
1279.1.2.1c NR-DC: Measurement Gap Sharing 1279.1.3 UE Measurement
capability 1289.1.3.1 EN-DC: Monitoring of multiple layers using gaps
1289.1.3.1a SA: Monitoring of multiple layers using gaps 1299.1.3.1b
NE-DC: Monitoring of multiple layers using gaps 1299.1.3.1c NR-DC:
Monitoring of multiple layers using gaps 1309.1.3.2 EN-DC: Maximum
allowed layers for multiple monitoring 1309.1.3.2a SA: Maximum allowed
layers for multiple monitoring 1319.1.3.2b NE-DC: Maximum allowed layers
for multiple monitoring 1319.1.3.2c NR-DC: Maximum allowed layers for
multiple monitoring 1319.1.4 Capabilities for Support of Event
Triggering and Reporting Criteria 1329.1.4.1 Introduction 1329.1.4.2
Requirements 1329.1.5 Carrier-specific scaling factor 1349.1.5.1
Monitoring of multiple layers outside gaps 1349.1.5.1.1 EN-DC mode:
carrier-specific scaling factor for SSB-based measurements performed
outside gaps 1359.1.5.1.2 SA mode: carrier-specific scaling factor for
SSB-based measurements performed outside gaps 1359.1.5.1.3 NR-DC mode:
carrier-specific scaling factor for SSB-based measurements performed
outside gaps 1369.1.5.1.4 NE-DC mode: carrier-specific scaling factor
for SSB-based measurements performed outside gaps 1369.1.5.2 Monitoring
of multiple layers within gaps 1379.1.5.2.1 EN-DC mode: carrier-specific
scaling factor for SSB-based measurements performed within gaps
1389.1.5.2.2 SA mode: carrier-specific scaling factor for SSB-based
measurements performed within gaps 1399.1.5.2.3 NE-DC: carrier-specific
scaling factor for SSB-based measurements performed within gaps
1409.1.5.2.4 NR-DC: carrier-specific scaling factor for SSB-based
measurements performed within gaps 1419.1.6 Minimum requirement at
transitions 1439.2 NR intra-frequency measurements 1439.2.1 Introduction
1439.2.2 Requirements applicability 1439.2.3 Number of cells and number
of SSB 1449.2.3.1 Requirements for FR1 1449.2.3.2 Requirements for FR2
1449.2.4 Measurement Reporting Requirements 1449.2.4.1 Periodic
Reporting 1449.2.4.2 Event-triggered Periodic Reporting 1449.2.4.3 Event
Triggered Reporting 1459.2.5 Intrafrequency measurements without
measurement gaps 1459.2.5.1 Intrafrequency cell identification
1459.2.5.2 Measurement period 1489.2.5.3 Scheduling availability of UE
during intra-frequency measurements 1499.2.5.3.1 Scheduling availability
of UE performing measurements in TDD bands on FR1 1499.2.5.3.2
Scheduling availability of UE performing measurements with a different
subcarrier spacing than PDSCH/PDCCH on FR1 1499.2.5.3.3 Scheduling
availability of UE performing measurements on FR2 1509.2.5.3.4
Scheduling availability of UE performing measurements on FR1 or FR2 in
case of FR1-FR2 inter-band CA 1509.2.5.4 SFTD Measurements between PCell
and PSCell 1519.2.5.4.1 Introduction 1519.2.5.4.2 SFTD Measurement delay
1519.2.5.4.3 SFTD Measurement Reporting Delay 1519.2.6 Intra-frequency
measurements with measurement gaps 1529.2.6.1 Void 1529.2.6.2
Intra-frequency cell identification 1529.2.6.3 Intra-frequency
Measurement Period 1539.3 NR inter-frequency measurements 1539.3.1
Introduction 1539.3.2 Requirements applicability 1549.3.2.1 Void
1549.3.2.2 Void 1549.3.3 Number of cells and number of SSB 1549.3.3.1
Requirements for FR1 1549.3.3.2 Requirements for FR2 1549.3.4
Inter-frequency cell identification 1559.3.4.1 Void 1569.3.4.2 Void
1569.3.5 Inter-frequency measurements 1569.3.5.1 Void 1579.3.5.2 Void
1579.3.5.3 Void 1579.3.6 Inter-frequency measurements reporting
requirements 1579.3.6.1 Periodic Reporting 1579.3.6.2 Event-triggered
Periodic Reporting 1579.3.6.3 Event-triggered Reporting 1579.3.7 Void
1579.3.8 Inter-frequency SFTD measurement requirements 1579.3.8.1
Introduction 1579.3.8.2 SFTD Measurement delay 1589.3.8.3 SFTD
Measurement reporting delay 1599.4 Inter-RAT measurements 1599.4.1
Introduction 1599.4.2 NR − E-UTRAN FDD measurements 1609.4.2.1
Introduction 1609.4.2.2 Requirements when no DRX is used 1619.4.2.3
Requirements when DRX is used 1619.4.2.4 Measurement reporting
requirements 1629.4.2.4.1 Periodic Reporting 1629.4.2.4.2
Event-Triggered Periodic Reporting 1629.4.2.4.3 Event-Triggered
Reporting 1629.4.3 NR − E-UTRAN TDD measurements 1639.4.3.1 Introduction
1639.4.3.2 Requirements when no DRX is used 1639.4.3.3 Requirements when
DRX is used 1649.4.3.4 Measurement reporting requirements 1659.4.3.4.1
Periodic Reporting 1659.4.3.4.2 Event-Triggered Periodic Reporting
1659.4.3.4.3 Event-Triggered Reporting 1659.4.4 Inter-RAT RSTD
measurements 1659.4.4.1 NR − E-UTRAN FDD RSTD measurements 1659.4.4.1.1
Introduction 1659.4.4.1.2 Requirements 1669.4.4.2 NR − E-UTRAN TDD RSTD
measurements 1699.4.4.2.1 Introduction 1699.4.4.2.2 Requirements
1709.4.5 Inter-RAT E-CID measurements 1739.4.5.1 NR−E-UTRAN FDD E-CID
RSRP and RSRQ measurements 1739.4.5.1.1 Introduction 1739.4.5.1.2
Requirements 1739.4.5.1.3 Measurement Reporting Delay 1739.4.5.2
NR−E-UTRAN TDD E-CID RSRP and RSRQ measurements 1739.4.5.2.1
Introduction 1739.4.5.2.2 Requirements 1739.4.5.2.3 Measurement
Reporting Delay 1749.5 L1-RSRP measurements for Reporting 1749.5.1
Introduction 1749.5.2 Requirements applicability 1749.5.3 Measurement
Reporting Requirements 1749.5.3.1 Periodic Reporting 1759.5.3.2
Semi-Persistent Reporting 1759.5.3.3 Aperiodic Reporting 1759.5.4
L1-RSRP measurement requirements 1759.5.4.1 SSB based L1-RSRP Reporting
1759.5.4.2 CSI-RS based L1-RSRP Reporting 1779.5.5 Measurement
restriction for CSI-RS and SSB for L1-RSRP measurement 1799.5.5.1
Measurement restriction for SSB based L1-RSRP 1809.5.5.2 Measurement
restriction for CSI-RS based L1-RSRP 1809.5.6 Scheduling availability of
UE during L1-RSRP measurement 1819.5.6.1 Scheduling availability of UE
performing L1-RSRP measurement with a same subcarrier spacing as
PDSCH/PDCCH on FR1 1819.5.6.2 Scheduling availability of UE performing
L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH
on FR1 1819.5.6.3 Scheduling availability of UE performing L1-RSRP
measurement on FR2 1819.5.6.4 Scheduling availability of UE performing
L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA
1829.6 NE-DC: Measurements 1829.6.1 Introduction 1829.6.2 SFTD
Measurements 1829.6.2.1 Introduction 1829.6.2.2 SFTD Measurement
requirements 18210 Measurement Performance requirements 18310.1 NR
measurements 18310.1.1 Introduction 18310.1.2 Intra-frequency RSRP
accuracy requirements for FR1 18410.1.2.1 Intra-frequency SS-RSRP
accuracy requirements 18410.1.2.1.1 Absolute SS-RSRP Accuracy
18410.1.2.1.2 Relative SS-RSRP Accuracy 18410.1.2.2 Void 18510.1.3
Intra-frequency RSRP accuracy requirements for FR2 18510.1.3.1
Intra-frequency SS-RSRP accuracy requirements 18510.1.3.1.1 Absolute
SS-RSRP Accuracy 18510.1.3.1.2 Relative SS-RSRP Accuracy 18610.1.3.2
Void 18710.1.4 Inter-frequency RSRP accuracy requirements for FR1
18710.1.4.1 Inter-frequency SS-RSRP accuracy requirements 18710.1.4.1.1
Absolute Accuracy of SS-RSRP in FR1 18710.1.4.1.2 Relative Accuracy of
SS-RSRP in FR1 18710.1.4.2 Void 18810.1.5 Inter-frequency RSRP accuracy
requirements for FR2 18810.1.5.1 Inter-frequency SS-RSRP accuracy
requirements 18810.1.5.1.1 Absolute SS-RSRP Accuracy 18810.1.5.1.2
Relative SS-RSRP Accuracy 18910.1.5.2 Void 19010.1.6 RSRP Measurement
Report Mapping 19010.1.7 Intra-frequency RSRQ accuracy requirements for
FR1 19210.1.7.1 Intra-frequency SS-RSRQ accuracy requirements in FR1
19210.1.7.1.1 Absolute SS-RSRQ Accuracy in FR1 19210.1.8 Intra-frequency
RSRQ accuracy requirements for FR2 19310.1.8.1 Intra-frequency SS-RSRQ
accuracy requirements in FR2 19310.1.8.1.1 Absolute SS-RSRQ Accuracy in
FR2 19310.1.9 Inter-frequency RSRQ accuracy requirements for FR1
19410.1.9.1 Inter-frequency SS-RSRQ accuracy requirements in FR1
19410.1.9.1.1 Aboslute Accuracy of SS-RSRQ in FR1 19410.1.9.1.2 Relative
Accuracy of SS-RSRQ in FR1 19510.1.10 Inter-frequency RSRQ accuracy
requirements for FR2 19510.1.11 RSRQ report mapping 19710.1.12
Intra-frequency SINR accuracy requirements for FR1 19710.1.13
Intra-frequency SINR accuracy requirements for FR2 19810.1.14
Inter-frequency SINR accuracy requirements for FR1 19910.1.15
Inter-frequency SINR accuracy requirements for FR2 20010.1.16 SINR
report mapping 20210.1.17 Power Headroom 20210.1.18 P~CMAX,c,f~
20310.1.19 L1-RSRP accuracy requirements for FR1 20310.1.20 L1-RSRP
accuracy requirements for FR2 20710.1.21 SFTD accuracy requirements
21010.2 E-UTRAN measurements 21410.2.1 Introduction 21410.2.2 E-UTRAN
RSRP measurements 21410.2.3 E-UTRAN RSRQ measurements 21510.2.4 E-UTRAN
RSTD measurements 21510.2.5 E-UTRAN RS-SINR measurements 21511 Void
215Annex A (normative): Test Cases 212A.1 Purpose of annex 212A.2
Requirement classification for statistical testing 212A.2.1 Types of
requirements in TS 38.133 212A.2.1.1 Time and delay requirements on UE
higher layer actions 212A.2.1.2 Measurements of power levels, relative
powers and time 213A.2.1.3 Implementation requirements 213A.2.1.4
Physical layer timing requirements 213A.3 RRM test configurations
214A.3.1 Reference measurement channels 214A.3.1.1 PDSCH 214A.3.1.1.1
FDD 214A.3.1.1.2 TDD 215A.3.1.2 CORESET for RMSI scheduling 218A.3.1.2.1
FDD 218A.3.1.2.2 TDD 219A.3.1.3 CORESET for RMC scheduling 222A.3.1.3.1
FDD 222A.3.1.3.2 TDD 223A.3.1.4 TDD UL/DL configuration 226A.3.2 OFDMA
channel noise generator (OCNG) 227A.3.2.1 Generic OFDMA Channel Noise
Generator (OCNG) 227A.3.2.1.1 OCNG pattern 1: Generic OCNG pattern for
all unused REs 227A.3.2.1.2 OCNG pattern 2: Generic OCNG pattern for all
unused REs for 2AoA setup 228A.3.2.1.3 OCNG pattern 3: Generic OCNG
pattern for unused REs in the same bandwidth as CORESET 228A.3.2.1.4
OCNG pattern 4: Generic OCNG pattern for all unused REs outside SSB
slot(s) 229A.3.2.2 Void 230A.3.3 Reference DRX configurations 230A.3.3.1
DRX Configuration 1: DRX cycle = 40 ms and TAT = 500 ms 230A.3.3.2 DRX
Configuration 2: DRX cycle = 640 ms and TAT = 500 ms 230A.3.3.3 DRX
Configuration 3: DRX cycle = 40 ms and TAT = Infinity 231A.3.3.4 DRX
Configuration 4: DRX cycle = 160 ms and TAT = Infinity 231A.3.3.5 DRX
Configuration 5: DRX cycle = 320 ms and TAT = Infinity 231A.3.3.6 DRX
Configuration 6: DRX cycle = 320 ms and TAT = 500 ms 232A.3.3.7 DRX
Configuration 7: DRX cycle = 640 ms and TAT = Infinity 232A.3.3.8 DRX
Configuration 8: DRX cycle = 320 ms and TAT = Infinity 232A.3.3.9 DRX
Configuration 9: DRX cycle = 40 ms and TAT = 500 ms 233A.3.3.10 DRX
Configuration 10: DRX cycle = 640 ms and TAT = 500 ms 233A.3.3.11 DRX
Configuration 11: DRX cycle = 20 ms and TAT = Infinity 233A.3.3.12 DRX
Configuration 12: DRX cycle = 640 ms and TAT = Infinity 234A.3.4 Test
Cases with Different Channel Bandwidths 234A.3.4.1 Test Cases with
Different E-UTRA Channel Bandwidths 234A.3.4.1.1 Introduction
234A.3.4.1.2 Principle of testing 234A.3.5 Test Cases for Synchronous
and Asynchronous DC Operations 234A.3.5.1 EN-DC Test Cases for
Synchronous and Asynchronous EN-DC Operations 234A.3.5.1.1 Introduction
234A.3.5.1.2 Principle of Testing 235A.3.6 Antenna configurations
235A.3.6.1 Antenna configurations for FR1 235A.3.6.1.1 Antenna
connection for 4 Rx capable UEs 235A.3.6.1.1.1 Introduction
235A.3.6.1.1.2 Principle of testing 235A.3.6.2 Antenna configurations
for FR2 238A.3.7 EN-DC test setup 238A.3.7.1 Introduction 238A.3.7.2
E-UTRAN Serving Cell Parameters 238A.3.7.2.1 E-UTRAN Serving Cell
Parameters for Tests with NR Cell(s) in FR1 238A.3.7.2.2 E-UTRAN Serving
Cell Parameters for Tests with NR Cell(s) in FR2 239A.3.7A NR FR1-FR2
test setup 240A.3.7B Void 240A.3.7C LTE-FR1/FR2 test setup 241A.3.7D
NE-DC test setup 241A.3.7D.1 Introduction 241A.3.7D.2 E-UTRAN Serving
Cell Parameters 241A.3.7D.2.1 E-UTRAN Serving Cell Parameters for Tests
with NR Cell(s) in FR1 241A.3.7D.2.2 E-UTRAN Serving Cell Parameters for
Tests with NR Cell(s) in FR2 241A.3.8 PRACH configurations 241A.3.8.1
Introduction 241A.3.8.2 PRACH configurations in FR1 241A.3.8.2.1 FR1
PRACH configuration 1 241A.3.8.2.2 FR1 PRACH configuration 2
242A.3.8.2.3 FR1 PRACH configuration 3 243A.3.8.2.4 FR1 PRACH
configuration 4 244A.3.8.3 PRACH configurations in FR2 245A.3.8.3.1 FR2
PRACH configuration 1 245A.3.8.3.2 FR2 PRACH configuration 2
246A.3.8.3.3 FR2 PRACH configuration 3 247A.3.8.3.4 FR2 PRACH
configuration 4 248A.3.9 BWP configurations 249A.3.9.1 Introduction
249A.3.9.2 Downlink BWP configurations 250A.3.9.2.1 Initial BWP
250A.3.9.2.2 Dedicated BWP 250A.3.9.3 Uplink BWP configurations
251A.3.9.3.1 Initial BWP 251A.3.9.3.2 Dedicated BWP 251A.3.10 SSB
Configurations 252A.3.10.1 SSB Configurations for FR1 252A.3.10.1.1 SSB
pattern 1 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz
252A.3.10.1.2 SSB pattern 2 in FR1: SSB allocation for SSB SCS=30 kHz in
40 MHz 252A.3.10.1.3 SSB pattern 3 in FR1: SSB allocation for SSB SCS=15
kHz in 10 MHz 253A.3.10.1.4 SSB pattern 4 in FR1: SSB allocation for SSB
SCS=30 kHz in 40 MHz 253A.3.10.1.5 SSB pattern 5 in FR1: SSB allocation
for SSB SCS=15 kHz starting from odd SFN in 10 MHz 254A.3.10.1.6 SSB
pattern 6 in FR1: SSB allocation for SSB SCS=30 kHz starting from odd
SFN in 40 MHz 254A.3.10.2 SSB Configurations for FR2 255A.3.10.2.1 SSB
pattern 1 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz
255A.3.10.2.2 SSB pattern 2 in FR2: SSB allocation for SSB SCS=240 kHz
in 100 MHz 255A.3.10.2.3 SSB pattern 3 in FR2: SSB allocation for SSB
SCS=120 kHz in 100 MHz 256A.3.10.2.4 SSB pattern 4 in FR2: SSB
allocation for SSB SCS=240 kHz in 100 MHz 256A.3.10.2.5 SSB pattern 5 in
FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz 257A.3.10.2.6 SSB
pattern 6 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz
257A.3.10.2.7 SSB pattern 7 in FR2: SSB allocation for SSB SCS=120 kHz
in 100 MHz 258A.3.10.2.8 SSB pattern 8 in FR2: SSB allocation for SSB
SCS=240 kHz in 100 MHz 258A.3.11 SMTC Configurations 258A.3.11.1 SMTC
pattern 1: SMTC period = 20 ms with SMTC duration = 1 ms 258A.3.11.2
SMTC pattern 2: SMTC period = 20 ms with SMTC duration = 5 ms
259A.3.11.3 SMTC pattern 3: SMTC period = 160 ms with SMTC duration = 1
ms 259A.3.11.4 SMTC pattern 4: SMTC period = 20 ms with SMTC duration =
1 ms 259A.3.11.5 SMTC pattern 5: SMTC period = 20 ms with SMTC duration
= 5 ms 259A.3.11.6 SMTC pattern 6: SMTC period = 20 ms with SMTC
duration = 5 ms 260A.3.12 Test Cases with Different CC Configurations
260A.3.12.1 EN-DC Test Cases with Different EN-DC Configurations
260A.3.12.1.1 Introduction 260A.3.12.1.2 Principle of testing
260A.3.12.2 Carrier Aggregation Test Cases with Different CA
Configurations 260A.3.12.2.1 Introduction 260A.3.12.2.2 Principle of
testing 260A.3.13 Test Cases in SA and EN-DC Operations 261A.3.13.1
Introduction 261A.3.13.2 Principle of Testing 261A.3.13A Test Cases
involving E-UTRA/FR1 and FR2 carriers 261A.3.13A.1 Introduction
261A.3.13A.2 Principle of Testing in EN-DC 261A.3.13A.3 Principle of
Testing in SA 262A.3.13A.4 Principle of Testing in E-UTRA 262A.3.13B
Test Cases for EN-DC and NE-DC Operations 263A.3.13B.1 Active BWP switch
Test Cases for EN-DC and NE-DC Operations 263A.3.13B.1.1 Introduction
263A.3.13B.1.2 Principle of Testing 263A.3.13B.2 SFTD accuracy Test
Cases for EN-DC and NE-DC Operations 263A.3.13B.2.1 Introduction
263A.3.13B.2.2 Principle of Testing 263A.3.14 CSI-RS configurations
264A.3.14.1 FDD 264A.3.14.2 TDD 265A.3.15 Angle of Arrival (AoA) for FR2
RRM test cases 267A.3.15.1 Setup 1: Single AoA in Rx beam peak direction
267A.3.15.2 Setup 2: Single AoA in non Rx beam peak direction
267A.3.15.2.1 Setup 2a: Single AoA in non Rx beam peak direction without
change in direction 267A.3.15.2.2 Setup 2b: Single AoA in non Rx beam
peak direction with change in direction 268A.3.15.3 Setup 3: 2 AoAs
268A.3.15.4 Setup 4: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non
Rx beam peak 268A.3.15.4.1 Setup 4a: 2 AoAs, 1 AoA in Rx beam peak
direction, 1 in non Rx beam peak without change in direction
268A.3.15.4.2 Setup 4b: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in
non Rx beam peak with change in direction 268A.3.16 TCI State
Configuration 269A.3.16.1 Introduction 269A.3.16.2 TCI states 269A.3.17
Configurations of CSI-RS for tracking 270A.3.17.1 Configuration of
CSI-RS for tracking for FR1 270A.3.17.1.1 FDD 270A.3.17.1.2 TDD
271A.3.17.2 Configuration of CSI-RS for tracking for FR2 272A.3.17.2.1
TDD 272A.3.18 Additional definitions related to OTA testing for FR2 RRM
test cases 273A.3.18.1 Introduction 273A.3.18.2 PRACH Power Measurement
273A.4 EN-DC tests with all NR cells in FR1 273A.4.1 Void 273A.4.2 Void
273A.4.3 RRC\_CONNECTED state mobility 273A.4.3.1 Void 273A.4.3.2 RRC
Connection Mobility Control 273A.4.3.2.1 Void 273A.4.3.2.2 Random Access
273A.4.3.2.2.1 Contention based random access test in FR1 for PSCell in
EN-DC 273A.4.3.2.2.1.1 Test Purpose and Environment 273A.4.3.2.2.2
Non-contention based random access test in FR1 for PSCell in EN-DC
276A.4.3.2.3 Void 280A.4.4 Timing 280A.4.4.1 UE transmit timing
280A.4.4.1.1 NR UE Transmit Timing Test for FR1 280A.4.4.1.1.1 Test
Purpose and environment 280A.4.4.1.1.2 Test requirements 283A.4.4.2 UE
timer accuracy 284A.4.4.3 Timing advance 284A.4.4.3.1 EN-DC FR1 timing
advance adjustment accuracy 284A.4.4.3.1.1 Test Purpose and Environment
284A.4.4.3.1.2 Test Parameters 284A.4.4.3.1.3 Test Requirements 287A.4.5
Signaling characteristics 287A.4.5.1 Radio link Monitoring 287A.4.5.1.1
Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with
SSB-based RLM RS in non-DRX mode 288A.4.5.1.1.1 Test Purpose and
Environment 288A.4.5.1.1.2 Test Requirements 291A.4.5.1.2 Radio Link
Monitoring In-sync Test for FR1 PSCell configured with SSB-based RLM RS
in non-DRX mode 291A.4.5.1.2.2 Test Requirements 295A.4.5.1.3 Radio Link
Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM
RS in DRX mode 295A.4.5.1.3.1 Test Purpose and Environment
295A.4.5.1.3.2 Test Requirements 298A.4.5.1.4 Radio Link Monitoring
In-sync Test for FR1 PSCell configured with SSB-based RLM RS in DRX mode
299A.4.5.1.4.1 Test Purpose and Environment 299A.4.5.1.4.2 Test
Requirements 302A.4.5.1.5 EN-DC Radio Link Monitoring Out-of-sync Test
for FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode
303A.4.5.1.5.1 Test Purpose and Environment 303A.4.5.1.5.2 Test
Requirements 306A.4.5.1.6 EN-DC Radio Link Monitoring In-sync Test for
FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode
306A.4.5.1.6.1 Test Purpose and Environment 306A.4.5.1.6.2 Test
Requirements 310A.4.5.1.7 EN-DC Radio Link Monitoring Out-of-sync Test
for FR1 PSCell configured with CSI-RS-based RLM in DRX mode
310A.4.5.1.7.1 Test Purpose and Environment 310A.4.5.1.7.2 Test
Requirements 314A.4.5.1.8 EN-DC Radio Link Monitoring In-sync Test for
FR1 PSCell configured with CSI-RS-based RLM in DRX mode 314A.4.5.1.8.1
Test Purpose and Environment 314A.4.5.1.8.2 Test Requirements 318A.4.5.2
Interruption 318**A.4.5.2.1** E-UTRAN -- NR FR1 interruptions at
transitions between active and non-active during DRX in synchronous
EN-DC 318A.4.5.2.1.1 Test Purpose and Environment 318A.4.5.2.1.2 Test
Requirements 321**A.4.5.2.2** E-UTRAN -- NR FR1 interruptions at
transitions between active and non-active during DRX in asynchronous
EN-DC 321A.4.5.2.2.1 Test Purpose and Environment 321A.4.5.2.2.2 Test
Requirements 324**A.4.5.2.3** E-UTRAN -- NR FR1 interruptions during
measurements on deactivated NR SCC in synchronous EN-DC 324A.4.5.2.3.1
Test Purpose and Environment 324A.4.5.2.3.2 Test Requirements
329A.4.5.2.4 E-UTRAN -- NR FR1 interruptions during measurements on
deactivated NR SCC in asynchronous EN-DC 330A.4.5.2.4.1 Test Purpose and
Environment 330A.4.5.2.4.2 Test Requirements 334**A.4.5.2.5** E-UTRAN --
NR FR1 interruptions during measurements on deactivated E-UTRAN SCC in
synchronous EN-DC 335A.4.5.2.5.1 Test Purpose and Environment
335A.4.5.2.5.2 Test Requirements 338**A.4.5.2.6** E-UTRAN -- NR FR1
interruptions during measurements on deactivated E-UTRAN SCC in
asynchronous EN-DC 338A.4.5.2.6.1 Test Purpose and Environment
338A.4.5.2.6.2 Test Requirements 341A.4.5.2.7 Void 342A.4.5.3.1 SCell
Activation and deactivation of known SCell in FR1 for 160ms SCell
measurement cycle 342A.4.5.3.1.1 Test Purpose and Environment
342A.4.5.3.1.2 Test Requirements 348A.4.5.3.2 SCell Activation and
deactivation of known SCell in FR1 for 640ms SCell measurement cycle
349A.4.5.3.2.1 Test Purpose and Environment 349A.4.5.3.2.2 Test
Requirements 349A.4.5.3.3 SCell Activation and deactivation of unknown
SCell in FR1 349A.4.5.3.3.1 Test Purpose and Environment 349A.4.5.3.3.2
Test Requirements 350A.4.5.4 UE UL carrier RRC reconfiguration Delay
350A.4.5.4.1 UE UL carrier RRC reconfiguration Delay 350A.4.5.4.1.1 Test
Purpose and Environment 350A.4.5.4.1.2 Test Requirements 359A.4.5.5 Beam
Failure Detection and Link recovery procedures 360A.4.5.5.1 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 PSCell configured with
SSB-based BFD and LR in non-DRX mode 360A.4.5.5.1.1 Test Purpose and
Environment 360A.4.5.5.1.2 Test Requirements 365A.4.5.5.2 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 PSCell configured with
SSB-based BFD and LR in DRX mode 366A.4.5.5.2.1 Test Purpose and
Environment 366A.4.5.5.2.2 Test Requirements 372A.4.5.5.3 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 PSCell configured with
CSI-RS-based BFD and LR in non-DRX mode 373A.4.5.5.3.1 Test Purpose and
Environment 373A.4.5.5.3.2 Test Requirements 378A.4.5.5.4 EN-DC Beam
Failure Detection and Link Recovery Test for FR1 PSCell configured with
CSI-RS-based BFD and LR in DRX mode 379A.4.5.5.4.1 Test Purpose and
Environment 379A.4.5.5.4.2 Test Requirements 383A.4.5.6.1 DCI-based and
Timer-based Active BWP Switch 384A.4.5.6.1.1 E-UTRAN -- NR PSCell FR1 DL
active BWP switch in non-DRX in synchronous EN-DC 384A.4.5.6.1.1.1 Test
Purpose and Environment 384A.**4**.**5**.**6**.**1**.**1**.2 Test
Requirements 388A.4.5.6.1.2 E-UTRAN -- NR PSCell FR1 DL active BWP
switch with FR1 SCell in non-DRX in synchronous EN-DC 388A.4.5.6.1.2.1
Test Purpose and Environment 388A.4.5.6.1.2.2 Test Requirements
394A.4.5.6.2 RRC-based Active BWP Switch 395A.4.5.6.2.1.1 Test Purpose
and Environment 395A.4.5.6.2.1.2 Test Requirements 399A.4.5.7 PSCell
addition and release delay 400A.4.5.7.1 Addition and Release Delay of
known NR PSCell 400A.4.5.7.1.1 Test purpose and environment
400A.4.5.7.1.2 Test Requirements 403A.4.6 Measurement procedure
404A.4.6.1 Intra-frequency Measurements 404A.4.6.1.1 EN-DC event
triggered reporting tests without gap under non-DRX 404A.4.6.1.1.1 Test
purpose and Environment 404A.4.6.1.1.2 Test parameters 404A.4.6.1.1.3
Test Requirements 408A.4.6.1.2 EN-DC event triggered reporting tests
without gap under DRX 408A.4.6.1.2.1 Test purpose and Environment
408A.4.6.1.2.2 Test parameters 408A.4.6.1.2.2 Test Requirements
412A.4.6.1.3 EN-DC event triggered reporting tests with per-UE gaps
under non-DRX 412A.4.6.1.3.1 Test purpose and Environment 412A.4.6.1.3.2
Test parameters 412A.4.6.1.3.3 Test Requirements 416A.4.6.1.4 EN-DC
event triggered reporting tests with per-UE gaps under DRX
416A.4.6.1.4.1 Test purpose and Environment 416A.4.6.1.4.2 Test
parameters 416A.4.6.1.4.3 Test Requirements 420A.4.6.1.5 EN-DC event
triggered reporting tests without gap under non-DRX with SSB index
reading 420A.4.6.1.5.1 Test purpose and Environment 420A.4.6.1.5.2 Test
parameters 420A.4.6.1.5.3 Test Requirements 422A.4.6.1.6 EN-DC event
triggered reporting tests with SSB index reading with per-UE gaps
423A.4.6.1.6.1 Test purpose and Environment 423A.4.6.1.6.2 Test
parameters 423A.4.6.1.6.3 Test Requirements 425A.4.6.2 Inter-frequency
Measurements 426A.4.6.2.1 EN-DC event triggered reporting tests for FR1
cell without SSB time index detection when DRX is not used
426A.4.6.2.1.1 Test Purpose and Environment 426A.4.6.2.1.2 Test
Requirements 429A.4.6.2.2 EN-DC event triggered reporting tests for FR1
cell without SSB time index detection when DRX is used 429A.4.6.2.2.1
Test Purpose and Environment 429A.4.6.2.2.2 Test Requirements
432A.4.6.2.3 Void 433A.4.6.2.4 Void 433A.4.6.2.5 EN-DC event triggered
reporting tests for FR1 cell with SSB time index detection when DRX is
not used 433A.4.6.2.5.1 Test Purpose and Environment 433A.4.6.2.5.2 Test
Requirements 436A.4.6.2.6 EN-DC event triggered reporting tests for FR1
cell with SSB time index detection when DRX is used 436A.4.6.2.6.1 Test
Purpose and Environment 436A.4.6.2.6.2 Test Requirements 440A.4.6.2.7
Void 440A.4.6.2.8 Void 440A.4.6.3 Void 440A.4.6.4 L1-RSRP measurement
for beam reporting 440A.4.6.4.1 SSB based L1-RSRP measurement when DRX
is not used 440A.4.6.4.1.1 Test Purpose and Environment 440A.4.6.4.1.2
Test parameters 440A.4.6.4.1.3 Test Requirements 443A.4.6.4.2 SSB based
L1-RSRP measurement when DRX is used 443A.4.6.4.2.1 Test Purpose and
Environment 443A.4.6.4.2.2 Test parameters 443A.4.6.4.2.3 Test
Requirements 445A.4.6.4.3 CSI-RS based L1-RSRP measurement when DRX is
not used 445A.4.6.4.3.1 Test Purpose and Environment 445A.4.6.4.3.2 Test
parameters 446A.4.6.4.3.3 Test Requirements 448A.4.6.4.4 CSI-RS based
L1-RSRP measurement when DRX is used 448A.4.6.4.4.1 Test Purpose and
Environment 448A.4.6.4.4.2 Test parameters 448A.4.6.4.4.3 Test
Requirements 451A.4.7 Measurement Performance requirements 451A.4.7.1
SS-RSRP 452A.4.7.1.1 EN-DC Intra-frequency measurement accuracy with FR1
serving cell and FR1 target cell 452A.4.7.1.1.1 Test Purpose and
Environment 452A.4.7.1.1.2 Test parameters 452A.4.7.1.1.3 Test
Requirements 455A.4.7.1.2 EN-DC inter-frequency measurement accuracy
with FR1 serving cell and FR1 target cell 455A.4.7.1.2.1 Test Purpose
and Environment 455A.4.7.1.2.2 Test parameters 455A.4.7.1.2.3 Test
Requirements 458A.4.7.1.3 Void 458A.4.7.2 SS-RSRQ 458**A.4.7.2.1**
**EN-DC Intra-frequency measurement accuracy with FR1 serving cell and
FR1 target cell** 458A.4.7.2.1.1 Test Purpose and Environment
458A.4.7.2.1.2 Test Parameters 458A.4.7.2.1.3 Test Requirements
462A.4.7.2.2 EN-DC Inter-frequency measurement accuracy with FR1 serving
cell and FR1 target cell 462A.4.7.2.2.1 Test Purpose and Environment
462A.4.7.2.2.2 Test Parameters 462A.4.7.2.2.3 Test Requirements
465A.4.7.3 SS-SINR 465A.4.7.3.1 EN-DC Intra-frequency measurement
accuracy with FR1 serving cell and FR1 target cell 465A.4.7.3.1.1 Test
Purpose and Environment 465A.4.7.3.1.2 Test Parameters 466A.4.7.3.1.3
Test Requirements 468A.4.7.3.2 EN-DC Inter-frequency measurement
accuracy with FR1 serving cell and FR1 target cell 469A.4.7.3.2.1 Test
Purpose and Environment 469A.4.7.3.2.2 Test Parameters 469A.4.7.3.2.3
Test Requirements 473A.4.7.4 L1-RSRP measurement for beam reporting
474A.4.7.4.1 SSB based L1-RSRP measurement 474A.4.7.4.1.1 Test Purpose
and Environment 474A.4.7.4.1.2 Test parameters 474A.4.7.4.1.3 Test
Requirements 477A.4.7.4.2 CSI-RS based L1-RSRP measurement on resource
set with repetition off 477A.4.7.4.2.1 Test Purpose and Environment
477A.4.7.4.2.2 Test parameters 477A.4.7.4.2.3 Test Requirements
480A.4.7.5 SFTD accuracy 480A.4.7.5.1 SFTD accuracy 480A.4.7.5.1.1 Test
Purpose and Environment 480A.4.7.5.1.2 Test Parameters 480A.4.7.5.1.3
Test Requirements 483A.4.7.5.2 Void 483A.4.7.5.3 Void 483A.4.8 Void
483A.4A NE-DC test with all NR cells in FR1 484A.4A.1 Signaling
characteristics 484A.4A.1.1 E-UTRAN PSCell addition 484A.4A.1.1.1 Test
purpose and environment 484A.4A.1.1.2 Test Requirements 488A.4A.1.2
Active BWP switch 489A.4A.1.2.1 E-UTRAN PSCell -- NR PCell FR1 DCI-based
and Timer-based DL active BWP switch in non-DRX in synchronous NE-DC
489A.4A.1.2.1.1 Test Purpose and Environment 489A.4A.2 Measurement
performance 494A.4A.2.1 SFTD accuracy 494A.4A.2.1.1 SFTD accuracy
494A.4A.2.1.1.1 Test Purpose 494A.4A.2.1.1.2 Test Environment
494A.4A.2.1.1.3 Test Requirements 497A.5 EN-DC tests with one or more NR
cells in FR2 498A.5.1 Void 498A.5.2 Void 498A.5.3 RRC\_CONNECTED state
mobility 498A.5.3.1 Void 498A.5.3.2 RRC Connection Mobility Control
498A.5.3.2.1 Void 498A.5.3.2.2 Random Access 498A.5.3.2.2.1 Contention
based random access test in FR2 for PSCell/SCell in EN-DC 498A.5.3.2.2.2
Non-contention based random access test in FR2 for PSCell/SCell in EN-DC
502A.5.3.2.3 Void 507A.5.4 Timing 507A.5.4.1 UE transmit timing
507A.5.4.1.1 NR UE Transmit Timing Test for FR2 507A.5.4.1.1.1 Test
Purpose and environment 507A.5.4.1.1.2 Test requirements 510A.5.4.2 UE
timer accuracy 510A.5.4.3 Timing advance 510A.5.4.3.1 EN-DC FR2 timing
advance adjustment accuracy 510A.5.4.3.1.1 Test Purpose and Environment
510A.5.4.3.1.2 Test Parameters 511A.5.4.3.1.3 Test Requirements 514A.5.5
Signaling characteristics 514A.5.5.1 Radio link Monitoring 514A.5.5.1.1
Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with
SSB-based RLM RS in non-DRX mode 514A.5.5.1.1.1 Test Purpose and
Environment 514A.5.5.1.1.2 Test Requirements 518A.5.5.1.2 Radio Link
Monitoring In-sync Test for FR2 PSCell configured with SSB-based RLM RS
in non-DRX mode 519A.5.5.1.2.1 Test Purpose and Environment
519A.5.5.1.2.2 Test Requirements 522A.5.5.1.3 Radio Link Monitoring
Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in DRX
mode 522A.5.5.1.3.1 Test Purpose and Environment 522A.5.5.1.3.2 Test
Requirements 527A.5.5.1.4 Radio Link Monitoring In-sync Test for FR2
PSCell configured with SSB-based RLM RS in DRX mode 527A.5.5.1.4.1 Test
Purpose and Environment 527A.5.5.1.4.2 Test Requirements 531A.5.5.1.5
EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured
with CSI-RS-based RLM in non-DRX mode 531A.5.5.1.6 EN-DC Radio Link
Monitoring In-sync Test for FR2 PSCell configured with CSI-RS-based RLM
in non-DRX mode 535A.5.5.1.6.1 Test Purpose and Environment
535A.5.5.1.6.2 Test Requirements 539A.5.5.1.7 EN-DC Radio Link
Monitoring Out-of-sync Test for FR2 PSCell configured with CSI-RS-based
RLM in DRX mode 539A.5.5.1.7.1 Test Purpose and Environment
539A.5.5.1.7.2 Test Requirements 544A.5.5.1.8 EN-DC Radio Link
Monitoring In-sync Test for FR2 PSCell configured with CSI-RS-based RLM
in DRX mode 544A.5.5.1.8.1 Test Purpose and Environment 544A.5.5.1.8.2
Test Requirements 548A.5.5.1.9 EN-DC Radio Link Monitoring UE Scheduling
Restrictions on FR2 549A.5.5.1.9.1 Test Purpose and Environment
549A.5.5.1.9.2 Test Requirements 551A.5.5.2 Interruption 551A.5.5.2.1
E-UTRAN -- NR FR2 interruptions at transitions between active and
non-active during DRX in synchronous EN-DC 551A.5.5.2.1.1 Test Purpose
and Environment 551A.5.5.2.1.2 Test Requirements 554A.5.5.2.2 E-UTRAN --
NR FR2 interruptions at transitions between active and non-active during
DRX in asynchronous EN-DC 554A.5.5.2.2.1 Test Purpose and Environment
554A.5.5.2.2.2 Test Requirements 557**A.5.5.2.3** E-UTRAN -- NR FR2
interruptions during measurements on deactivated NR SCC in synchronous
EN-DC 557A.5.5.2.3.1 Test Purpose and Environment 557A.5.5.2.**3.2**
Test Requirements 560**A.5.5.2.4** E-UTRAN -- NR FR2 interruptions
during measurements on deactivated NR SCC in asynchronous EN-DC
561A.5.5.2.4.1 Test Purpose and Environment 561A.5.5.2.**4.2** Test
Requirements 564**A.5.5.2.5** E-UTRAN -- NR FR2 interruptions during
measurements on deactivated E-UTRAN SCC in synchronous EN-DC
565A.5.5.2.5.1 Test Purpose and Environment 565A.5.5.2.**5.2** Test
Requirements 568**A.5.5.2.6** E-UTRAN -- NR FR2 interruptions during
measurements on deactivated E-UTRAN SCC in asynchronous EN-DC
569A.5.5.2.6.1 Test Purpose and Environment 569A.5.5.2.**6.2** Test
Requirements 571A.5.5.3.1 SCell Activation and deactivation of SCell in
FR2 intra-band 572A.5.5.3.1.1 Test Purpose and Environment
572A.5.5.3.1.2 Test Requirements 574A.5.5.3.2 SCell Activation and
deactivation of known SCell in FR1 for 160ms SCell measurement cycle
574A.5.5.3.2.1 Test Purpose and Environment 574A.5.5.3.2.2 Test
Requirements 577A.5.5.3.3 Void 577A.5.5.3.4 Void 577A.5.5.3.5 SCell
Activation and deactivation of SCell in FR2 577A.5.5.3.5.1 Test Purpose
and Environment 577A.5.5.3.5.2 Test Requirements 580A.5.5.4 Void
581A.5.5.5 Beam Failure Detection and Link recovery procedures
581A.5.5.5.1 EN-DC Beam Failure Detection and Link Recovery Test for FR2
PSCell configured with SSB-based BFD and LR in non-DRX mode
581A.5.5.5.1.1 Test Purpose and Environment 581A.5.5.5.1.2 Test
Requirements 585A.5.5.5.2 EN-DC Beam Failure Detection and Link Recovery
Test for FR2 PSCell configured with SSB-based BFD and LR in DRX mode
586A.5.5.5.2.1 Test Purpose and Environment 586A.5.5.5.2.2 Test
Requirements 590A.5.5.5.3 EN-DC Beam Failure Detection and Link Recovery
Test for FR2 PSCell configured with CSI-RS-based BFD and LR in non-DRX
mode 591A.5.5.5.3.1 Test Purpose and Environment 591A.5.5.5.3.2 Test
Requirements 595A.5.5.5.4 EN-DC Beam Failure Detection and Link Recovery
Test for FR2 PSCell configured with CSI-RS-based BFD and LR in DRX mode
596A.5.5.5.4.1 Test Purpose and Environment 596A.5.5.5.4.2 Test
Requirements 600A.5.5.5.5 EN-DC scheduling availability restriction
during Beam Failure Detection and Link Recovery for FR2 PSCell
configured with SSB-based BFD and LR in non-DRX mode 600A.5.5.5.5.1 Test
Purpose and Environment 600A.5.5.5.5.2 Test Requirements 604A.5.5.6
Active BWP switch 605A.5.5.6.1 DCI-based and Timer-based Active BWP
Switch 605A.5.5.6.1.1 E-UTRAN -- NR PSCell FR2 DL active BWP switch with
non-DRX in synchronous EN-DC 605A.5.5.6.1.1.1 Test Purpose and
Environment 605A.**5.5.6.1.1**.2 Test Requirements 608A.5.5.6.1.2
E-UTRAN -- NR PSCell FR2 with FR2 SCell DL active BWP switch in non-DRX
in synchronous EN-DC 609A.5.5.6.1.2.1 Test Purpose and Environment
609A.**5.5.6.1.2**.2 Test Requirements 612A.5.5.6.2 RRC-based Active BWP
Switch 613A.5.5.6.2.1 E-UTRAN -- NR PSCell FR2 DL active BWP switch with
non-DRX in synchronous EN-DC 613A.5.5.6.2.1.1 Test Purpose and
Environment 613A.**5**.**5**.**6**.**2**.**1**.2 Test Requirements
616A.5.5.7 PSCell addition and release delay 617A.5.5.7.1 Addition and
Release Delay of NR PSCell 617A.5.5.7.1.1 Test purpose and environment
617A.5.5.7.1.2 Test Requirements 620A.5.5.8 Active TCI state switch
delay 621A.5.5.8.1 MAC-CE based active TCI state switch 621A.5.5.8.1.1
E-UTRAN -- NR PSCell FR2 active TCI state switch for a known TCI state
621A.5.5.8.1.1.1 Test Purpose and Environment 621A.5.5.8**.1.1**.2 Test
Requirements 625A.5.5.8.2 RRC based active TCI state switch
625A.5.5.8.2.1 E-UTRAN -- NR PSCell FR2 active TCI state switch for a
known TCI state 625A.5.5.8.2.1.1 Test Purpose and Environment
625A.5.5.8.2**.1**.2 Test Requirements 629A.5.6 Measurement procedure
629A.5.6.1 Intra-frequency Measurements 629A.5.6.1.1 EN-DC event
triggered reporting test without gap under non-DRX 629A.5.6.1.1.1 Test
purpose and Environment 629A.5.6.1.1.2 Test Requirements 633A.5.6.1.2
EN-DC event triggered reporting test without gap under DRX
633A.5.6.1.2.1 Test purpose and Environment 633A.5.6.1.2.2 Test
Requirements 635A.5.6.1.3 EN-DC event triggered reporting test with
per-UE gaps under non-DRX 636A.5.6.1.3.1 Test purpose and Environment
636A.5.6.1.3.2 Test Requirements 640A.5.6.1.4 EN-DC event triggered
reporting test with per-UE gaps under DRX 640A.5.6.1.4.1 Test purpose
and Environment 640A.5.6.1.4.2 Test Requirements 643A.5.6.2
Inter-frequency Measurements 644A.5.6.2.1 EN-DC event triggered
reporting tests for FR2 cell without SSB time index detection when DRX
is not used 644A.5.6.2.1.1 Test Purpose and Environment 644A.5.6.2.1.2
Test Requirements 647A.5.6.2.2 EN-DC event triggered reporting tests for
FR2 cell without SSB time index detection when DRX is used
647A.5.6.2.2.1 Test Purpose and Environment 647A.5.6.2.2.2 Test
Requirements 650A.5.6.2.3 EN-DC event triggered reporting tests for FR2
cell with SSB time index detection when DRX is not used 651A.5.6.2.3.1
Test Purpose and Environment 651A.5.6.2.3.2 Test Requirements
654A.5.6.2.4 EN-DC event triggered reporting tests for FR2 cell with SSB
time index detection when DRX is used 654A.5.6.2.4.1 Test Purpose and
Environment 654A.5.6.2.5 EN-DC event triggered reporting tests for FR2
cell without SSB time index detection when DRX is not used
658A.5.6.2.5.1 Test Purpose and Environment 658A.5.6.2.5.2 Test
Requirements 661A.5.6.2.6 EN-DC event triggered reporting tests for FR2
cell without SSB time index detection when DRX is used 662A.5.6.2.6.1
Test Purpose and Environment 662A.5.6.2.6.2 Test Requirements
666A.5.6.2.7 EN-DC event triggered reporting tests for FR2 cell with SSB
time index detection when DRX is not used 666A.5.6.2.7.1 Test Purpose
and Environment 666A.5.6.2.7.2 Test Requirements 670A.5.6.2.8 EN-DC
event triggered reporting tests for FR2 cell with SSB time index
detection when DRX is used 671A.5.6.2.8.1 Test Purpose and Environment
671A.5.6.2.8.2 Test Requirements 675A.5.6.3 L1-RSRP measurement for beam
reporting 676A.5.6.3.1 SSB based L1-RSRP measurement when DRX is not
used 676A.5.6.3.1.1 Test Purpose and Environment 676A.5.6.3.1.2 Test
parameters 676A.5.6.3.1.3 Test Requirements 678A.5.6.3.1.3 Test
Requirements 678A.5.6.3.2 SSB based L1-RSRP measurement when DRX is used
679A.5.6.3.2.1 Test Purpose and Environment 679A.5.6.3.2.2 Test
parameters 679A.5.6.3.2.3 Test Requirements 681A.5.6.3.3 CSI-RS based
L1-RSRP measurement when DRX is not used 681A.5.6.3.3.1 Test Purpose and
Environment 681A.5.6.3.3.2 Test parameters 682A.5.6.3.3.3 Test
Requirements 683A.5.6.3.4 CSI-RS based L1-RSRP measurement when DRX is
used 684A.5.6.3.4.1 Test Purpose and Environment 684A.5.6.3.4.2 Test
parameters 684A.5.6.3.4.3 Test Requirements 686A.5.7 Measurement
Performance requirements 687A.5.7.1 SS-RSRP 687A.5.7.1.1 EN-DC
intra-frequency case measurement accuracy with FR2 serving cell and FR2
target cell 687A.5.7.1.1.1 Test Purpose and Environment 687A.5.7.1.1.2
Test parameters 687A.5.7.1.1.3 Test Requirements 689A.5.7.1.2 EN-DC
inter-frequency case measurement accuracy with FR2 serving cell and FR2
target cell 690A.5.7.1.2.1 Test Purpose and Environment 690A.5.7.1.2.2
Test parameters 690A.5.7.1.2.3 Test Requirements 695A.5.7.1.3 EN-DC
inter-frequency measurement accuracy with FR1 serving cell and FR2
target cell 696A.5.7.1.3.1 Test Purpose and Environment 696A.5.7.1.3.2
Test parameters 696A.5.7.1.3.3 Test Requirements 699A.5.7.2 SS-RSRQ
699A.5.7.2.1 EN-DC Intra-frequency measurement accuracy with FR2 serving
cell and FR2 TDD target cell 699A.5.7.2.1.1 Test Purpose and Environment
699A.5.7.2.1.2 Test Parameters 699A.5.7.2.1.3 Test Requirements
701A.5.7.2.2 EN-DC Inter-frequency measurement accuracy with FR2 serving
cell and FR2 TDD target cell 701A.5.7.2.2.1 Test Purpose and Environment
701A.5.7.2.2.2 Test Parameters 702A.5.7.2.2.3 Test Requirements
704A.5.7.3 SS-SINR 704A.5.7.3.1 EN-DC Intra-frequency measurement
accuracy with FR2 serving cell and FR2 TDD target cell 704A.5.7.3.1.1
Test Purpose and Environment 704A.5.7.3.1.2 Test Parameters
704A.5.7.3.1.3 Test Requirements 707A.5.7.3.2 EN-DC Inter-frequency
measurement accuracy with FR2 serving cell and FR2 TDD target cell
708A.5.7.3.2.1 Test Purpose and Environment 708A.5.7.3.2.2 Test
Parameters 708A.5.7.3.2.3 Test Requirements 710A.5.7.4 L1-RSRP
measurement for beam reporting 710A.5.7.4.1 SSB based L1-RSRP
measurement 710A.5.7.4.1.1 Test Purpose and Environment 710A.5.7.4.1.2
Test parameters 711A.5.7.4.1.3 Test Requirements 713A.5.7.4.2 CSI-RS
based L1-RSRP measurement on resource set with repetition off
714A.5.7.4.2.1 Test Purpose and Environment 714A.5.7.4.2.2 Test
parameters 714A.5.7.4.2.3 Test Requirements 716A.5.8 Void 717A.6 NR
standalone tests with all NR cells in FR1 715A.6.1 SA: RRC\_IDLE state
mobility 715A.6.1.1 Cell re-selection to NR 715A.6.1.1.1 Cell
reselection to FR1 intra-frequency NR case 715A.6.1.1.1.1 Test Purpose
and Environment 715A.6.1.1.1.2 Test Parameters 715A.6.1.1.1.3 Test
Requirements 719A.6.1.1.2 Cell reselection to FR1 inter-frequency NR
case 719A.6.1.1.2.1 Test Purpose and Environment 719A.6.1.1.2.2 Test
Parameters 719A.6.1.1.2.3 Test Requirements 723A.6.1.2.1 Cell
reselection to higher priority E-UTRAN 723A.6.1.2.1.1 Test Purpose and
Environment 723A.6.1.2.1.2 Test Parameters 723A.6.1.2.1.3 Test
Requirements 726A.6.1.2.2 Cell reselection to lower priority E-UTRAN
727A.6.1.2.2.1 Test Purpose and Environment 727A.6.1.2.2.2 Test
Parameters 727A.6.1.2.2.3 Test Requirements 729A.6.2 SA: RRC\_INACTIVE
state mobility 730A.6.3 RRC\_CONNECTED state mobility 730A.6.3.1.1
Intra-frequency handover from FR1 to FR1; known target cell
730A.6.3.1.1.1 Test Purpose and Environment 730A.6.3.1.1.2 Test
Parameters 730A.6.3.1.1.3 Test Requirements 732A.6.3.1.2 Intra-frequency
handover from FR1 to FR1; unknown target cell 732A.6.3.1.2.1 Test
Purpose and Environment 732A.6.3.1.2.2 Test Parameters 732A.6.3.1.2.3
Test Requirements 734A.6.3.1.3 Inter-frequency handover from FR1 to FR1;
unknown target cell 734A.6.3.1.3.1 Test Purpose and Environment
734A.6.3.1.3.2 Test Parameters 734A.6.3.1.3.3 Test Requirements
736A.6.3.1.4 SA NR - E-UTRAN handover 736A.6.3.1.4.1 Test Purpose and
Environment 736A.6.3.1.4.2 Test Requirements 740A.6.3.1.5 SA NR -
E-UTRAN handover with unknown target cell 740A.6.3.1.5.1 Test Purpose
and Environment 740A.6.3.1.5.2 Test Requirements 743A.6.3.2.1 SA: RRC
Re-establishment 744A.6.3.2.1.1 Intra-frequency RRC Re-establishment in
FR1 744A.6.3.2.1.2 Inter-frequency RRC Re-establishment in FR1
747A.6.3.2.1.3 Intra-frequency RRC Re-establishment in FR1 without
serving cell timing 750A.6.3.2.2 Random Access 753A.6.3.2.2.1 Contention
based random access test in FR1 for NR standalone 753A.6.3.2.2.2
Non-Contention based random access test in FR1 for NR standalone
757A.6.3.2.3.1 Redirection from NR in FR1 to NR in FR1 760A.6.3.2.3.2
Redirection from NR in FR1 to E-UTRAN 763A.6.4 Timing 767A.6.4.1.1 NR UE
Transmit Timing Test for FR1 767A.6.4.1.1.1 Test Purpose and environment
767A.6.4.1.1.2 Test requirements 769A.6.4.3.1 SA FR1 timing advance
adjustment accuracy 770A.6.4.3.1.1 Test Purpose and Environment
770A.6.4.3.1.2 Test Parameters 770A.6.4.3.1.3 Test Requirements 773A.6.5
Signalling characteristics 773A.6.5.1.1 Radio Link Monitoring
Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in
non-DRX mode 774A.6.5.1.1.1 Test Purpose and Environment 774A.6.5.1.1.2
Test Requirements 777A.6.5.1.2 Radio Link Monitoring In-sync Test for
FR1 PCell configured with SSB-based RLM RS in non-DRX mode
777A.6.5.1.2.1 Test Purpose and Environment 777A.6.5.1.2.2 Test
Requirements 781A.6.5.1.3 Radio Link Monitoring Out-of-sync Test for FR1
PCell configured with SSB-based RLM RS in DRX mode 781A.6.5.1.3.1 Test
Purpose and Environment 781A.6.5.1.3.2 Test Requirements 785A.6.5.1.4
Radio Link Monitoring In-sync Test for FR1 PCell configured with
SSB-based RLM RS in DRX mode 785A.6.5.1.4.1 Test Purpose and Environment
785A.6.5.1.4.2 Test Requirements 789A.6.5.1.5 Radio Link Monitoring
Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in
non-DRX mode 789A.6.5.1.5.1 Test Purpose and Environment 789A.6.5.1.5.2
Test Requirements 794A.6.5.1.6 Radio Link Monitoring In-sync Test for
FR1 PCell configured with CSI-RS-based RLM in non-DRX mode
794A.6.5.1.6.1 Test Purpose and Environment 794A.6.5.1.6.2 Test
Requirements 798A.6.5.1.7 Radio Link Monitoring Out-of-sync Test for FR1
PCell configured with CSI-RS-based RLM in DRX mode 798A.6.5.1.7.1 Test
Purpose and Environment 798A.6.5.1.7.2 Test Requirements 802A.6.5.1.8
Radio Link Monitoring In-sync Test for FR1 PCell configured with
CSI-RS-based RLM in DRX mode 802A.6.5.1.8.1 Test Purpose and Environment
802A.6.5.1.8.2 Test Requirements 806**A.6.5.2.1** Interruptions during
measurements on deactivated NR SCC in FR1 806A.6.5.3.1 SCell Activation
and deactivation of known SCell in FR1 in non-DRX for 160ms SCell
measurement cycle 811A.6.5.3.1.1 Test Purpose and Environment
811A.6.5.3.1.2 Test Requirements 816A.6.5.3.2 SCell Activation and
deactivation of known SCell in FR1 in non-DRX for 640 ms SCell
measurement cycle 817A.6.5.3.2.1 Test Purpose and Environment
817A.6.5.3.2.2 Test Requirements 817A.6.5.3.3 SCell Activation and
deactivation of unknown SCell in FR1 in non-DRX 817A.6.5.3.3.1 Test
Purpose and Environment 817A.6.5.3.3.2 Test Requirements 818A.6.5.4.1 UE
UL carrier RRC reconfiguration Delay 818A.6.5.4.1.1 Test Purpose and
Environment 818A.6.5.4.1.2 Test Requirements 828A.6.5.4.2 Void
829A.6.5.5.1 Beam Failure Detection and Link Recovery Test for FR1 PCell
configured with SSB-based BFD and LR in non-DRX mode 829A.6.5.5.1.1 Test
Purpose and Environment 829A.6.5.5.1.2 Test Requirements 833A.6.5.5.2
Beam Failure Detection and Link Recovery Test for FR1 PCell configured
with SSB-based BFD and LR in DRX mode 834A.6.5.5.2.1 Test Purpose and
Environment 834A.6.5.5.2.2 Test Requirements 838A.6.5.5.3 Beam Failure
Detection and Link Recovery Test for FR1 PCell configured with
CSI-RS-based BFD and LR in non-DRX mode 839A.6.5.5.3.1 Test Purpose and
Environment 839A.6.5.5.3.2 Test Requirements 844A.6.5.5.4 Beam Failure
Detection and Link Recovery Test for FR1 PCell configured with
CSI-RS-based BFD and LR in DRX mode 845A.6.5.5.4.1 Test Purpose and
Environment 845A.6.5.5.4.2 Test Requirements 849A.6.5.6.1 DCI-based and
Timer-based Active BWP Switch 850A.6.5.6.1.1 NR FR1- NR FR1 DL active
BWP switch of SCell with non-DRX in SA 850A.6.5.6.1.2 NR FR1 DL active
BWP switch with non-DRX in SA 857A.6.5.6.2 RRC-based Active BWP Switch
861A.6.5.6.2.1 NR FR1 DL active BWP switch of Cell with non-DRX in SA
861A.6.6 Measurement procedure 864A.6.6.1.1 SA event triggered reporting
tests without gap under non-DRX 864A.6.6.1.1.1 Test purpose and
Environment 864A.6.6.1.1.2 Test parameters 864A.6.6.1.1.3 Test
Requirements 866A.6.6.1.2 SA event triggered reporting tests without gap
under DRX 866A.6.6.1.2.1 Test purpose and Environment 866A.6.6.1.2.2
Test parameters 867A.6.6.1.2.3 Test Requirements 868A.6.6.1.3 SA event
triggered reporting tests with per-UE gaps under non-DRX 869A.6.6.1.3.1
Test purpose and Environment 869A.6.6.1.3.2 Test parameters
869A.6.6.1.3.3 Test Requirements 873A.6.6.1.4 SA event triggered
reporting tests with per-UE gaps under DRX 873A.6.6.1.4.1 Test purpose
and Environment 873A.6.6.1.4.2 Test parameters 873A.6.6.1.4.3 Test
Requirements 876A.6.6.1.5 SA event triggered reporting tests without gap
under non-DRX with SSB index reading 876A.6.6.1.5.1 Test purpose and
Environment 876A.6.6.1.5.2 Test parameters 876A.6.6.1.5.3 Test
Requirements 878A.6.6.1.6 SA event triggered reporting tests with per-UE
gaps under non-DRX with SSB index reading 878A.6.6.1.6.1 Test purpose
and Environment 878A.6.6.1.6.2 Test parameters 878A.6.6.1.6.3 Test
Requirements 880A.6.6.2.1 SA event triggered reporting tests for FR1
without SSB time index detection when DRX is not used 880A.6.6.2.1.1
Test Purpose and Environment 880A.6.6.2.1.2 Test Requirements
883A.6.6.2.2 SA event triggered reporting tests for FR1 without SSB time
index detection when DRX is used 883A.6.6.2.2.1 Test Purpose and
Environment 883A.6.6.2.2.2 Test Requirements 886A.6.6.2.3 Void
887A.6.6.2.4 Void 887A.6.6.2.5 SA event triggered reporting tests for
FR1 with SSB time index detection when DRX is not used 887A.6.6.2.5.1
Test Purpose and Environment 887A.6.6.2.5.2 Test Requirements
891A.6.6.2.6 SA event triggered reporting tests for FR1 with SSB time
index detection when DRX is used 891A.6.6.2.6.1 Test Purpose and
Environment 891A.6.6.2.6.2 Test Requirements 894A.6.6.2.7 Void
894A.6.6.2.8 Void 894A.6.6.3 Inter-RAT Measurements 894A.6.6.3.1 SA NR -
E-UTRAN event-triggered reporting in non-DRX in FR1 894A.6.6.3.1.1 Test
Purpose and Environment 894A.6.6.3.1.2 Test Requirements 898A.6.6.3.2 SA
NR - E-UTRAN event-triggered reporting in DRX in FR1 898A.6.6.3.2.1 Test
Purpose and Environment 898A.6.6.3.2.2 Test Requirements 901A.6.6.4
L1-RSRP measurement for beam reporting 902A.6.6.4.1 SSB based L1-RSRP
measurement when DRX is not used 902A.6.6.4.1.1 Test Purpose and
Environment 902A.6.6.4.1.2 Test parameters 902A.6.6.4.1.3 Test
Requirements 904A.6.6.4.2 SSB based L1-RSRP measurement when DRX is used
904A.6.6.4.2.1 Test Purpose and Environment 904A.6.6.4.2.2 Test
parameters 904A.6.6.4.2.3 Test Requirements 907A.6.6.4.3 CSI-RS based
L1-RSRP measurement when DRX is not used 907A.6.6.4.3.1 Test Purpose and
Environment 907A.6.6.4.3.2 Test parameters 907A.6.6.4.3.3 Test
Requirements 909A.6.6.4.4 CSI-RS based L1-RSRP measurement when DRX is
used 909A.6.6.4.4.1 Test Purpose and Environment 909A.6.6.4.4.2 Test
parameters 909A.6.6.4.4.3 Test Requirements 911A.6.7 Measurement
Performance requirements 912A.6.7.1.1 SA: intra-frequency case
measurement accuracy with FR1 serving cell and FR1 target cell
912A.6.7.1.1.1 Test Purpose and Environment 912A.6.7.1.1.2 Test
parameters 912A.6.7.1.1.3 Test Requirements 917A.6.7.1.2 SA
inter-frequency case measurement accuracy with FR1 serving cell and FR1
target cell 917A.6.7.1.2.1 Test Purpose and Environment 917A.6.7.1.2.2
Test parameters 917A.6.7.1.2.3 Test Requirements 920A.6.7.1.3 Void
920A.6.7.2 SS-RSRQ 920A.6.7.2.1 SA: Intra-frequency measurement accuracy
with FR1 serving cell and FR1 target cell 920A.6.7.2.1.1 Test Purpose
and Environment 920A.6.7.2.1.2 Test Parameters 920A.6.7.2.1.3 Test
Requirements 924A.6.7.2.2 SA Inter-frequency measurement accuracy with
FR1 serving cell and FR1 target cell 924A.6.7.2.2.1 Test Purpose and
Environment 924A.6.7.2.2.2 Test Parameters 924A.6.7.2.2.3 Test
Requirements 928A.6.7.3.1 SA intra-frequency measurement accuracy with
FR1 serving cell and FR1 target cell 928A.6.7.3.1.1 Test Purpose and
Environment 928A.6.7.3.1.2 Test Parameters 928A.6.7.3.1.3 Test
Requirements 931A.6.7.3.2 SA Inter-frequency measurement accuracy with
FR1 serving cell and FR1 target cell 931A.6.7.3.2.1 Test Purpose and
Environment 931A.6.7.3.2.2 Test Parameters 931A.6.7.3.2.3 Test
Requirements 935A.6.7.4.1 SSB based L1-RSRP measurement 935A.6.7.4.1.1
Test Purpose and Environment 935A.6.7.4.1.2 Test parameters
935A.6.7.4.1.3 Test Requirements 938A.6.7.4.2 CSI-RS based L1-RSRP
measurement on resource set with repetition off 938A.6.7.4.2.1 Test
Purpose and Environment 938A.6.7.4.2.2 Test parameters 938A.6.7.4.2.3
Test Requirements 941A.6.7.5.1 SA: inter-RAT measurement accuracy with
FR1 serving cell 941A.6.7.5.1.1 Test Purpose and Environment
941A.6.7.5.1.2 Test parameters 941A.6.7.5.1.3 Test Requirements
946A.6.7.6.1 SA: inter-RAT measurement accuracy with FR1 serving cell
947A.6.7.6.1.1 Test Purpose and Environment 947A.6.7.6.1.2 Test
parameters 947A.6.7.6.1.3 Test Requirements 952A.6.7.7.1 SA: inter-RAT
measurement accuracy with FR1 serving cell 952A.6.7.7.1.1 Test Purpose
and Environment 952A.6.7.7.1.2 Test parameters 952A.6.7.7.1.3 Test
Requirements 957A.7 NR standalone tests with one or more NR cells in FR2
957A.7.1 SA: RRC\_IDLE state mobility 957A.7.1.1.1 Cell reselection to
FR2 intra-frequency NR case 957A.7.1.1.1.1 Test Purpose and Environment
957A.7.1.1.1.2 Test Parameters 957A.7.1.1.1.3 Test Requirements
960A.7.1.1.2 Cell reselection to FR2 inter-frequency NR case
961A.7.1.1.2.1 Test Purpose and Environment 961A.7.1.1.2.2 Test
Parameters 961A.7.1.1.2.3 Test Requirements 963A.7.2 SA: RRC\_INACTIVE
state mobility 964A.7.3 RRC\_CONNECTED state mobility 964A.7.3.1
Handover 964A.7.3.1.1 Inter-frequency handover from FR1 to FR2; unknown
target cell 964A.7.3.1.1.1 Test Purpose and Environment 964A.7.3.1.1.2
Test Parameters 964A.7.3.1.1.3 Test Requirements 967A.7.3.1.2
Intra-frequency handover from FR2 to FR2; unknown target cell
968A.7.3.1.2.1 Test Purpose and Environment 968A.7.3.1.2.2 Test
Parameters 968A.7.3.1.2.3 Test Requirements 970A.7.3.1.3 Inter-frequency
handover from FR2 to FR2; unknown target cell 970A.7.3.1.3.1 Test
Purpose and Environment 970A.7.3.1.3.2 Test Parameters 970A.7.3.1.3.3
Test Requirements 972A.7.3.2.1 SA: RRC Re-establishment 972A.7.3.2.1.1
Intra-frequency RRC Re-establishment in FR2 972A.7.3.2.1.2
Inter-frequency RRC Re-establishment in FR2 975A.7.3.2.1.3
Intra-frequency RRC Re-establishment in FR2 without serving cell timing
978A.7.3.2.1.3.1 Test Purpose and Environment 978A.7.3.2.1.3.2 Test
Requirements 980A.7.3.2.2 Random Access 981A.7.3.2.2.1 Contention based
random access test in FR2 for NR Standalone 981A.7.3.2.2.2
Non-contention based random access test in FR2 for NR Standalone
985A.7.3.2.3 SA: RRC Connection Release with Redirection 989A.7.3.2.3.1
Redirection from NR in FR2 to NR in FR2 989A.7.4 Timing 991A.7.4.1.1 NR
UE Transmit Timing Test for FR2 991A.7.4.1.1.1 Test Purpose and
environment 991A.7.4.1.1.2 Test requirements 994A.7.4.3.1 SA FR2 timing
advance adjustment accuracy 995A.7.4.3.1.1 Test Purpose and Environment
995A.7.4.3.1.2 Test Parameters 995A.7.4.3.1.3 Test Requirements 999A.7.5
Signaling characteristics 999A.7.5.1.1 Radio Link Monitoring Out-of-sync
Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode
999A.7.5.1.1.1 Test Purpose and Environment 999A.7.5.1.1.2 Test
Requirements 1002A.7.5.1.2 Radio Link Monitoring In-sync Test for FR2
PCell configured with SSB-based RLM RS in non-DRX mode 1003A.7.5.1.2.1
Test Purpose and Environment 1003A.7.5.1.2.2 Test Requirements
1007A.7.5.1.3 Radio Link Monitoring Out-of-sync Test for FR2 PCell
configured with SSB-based RLM RS in DRX mode 1008A.7.5.1.3.1 Test
Purpose and Environment 1008A.7.5.1.3.2 Test Requirements 1012A.7.5.1.4
Radio Link Monitoring In-sync Test for FR2 PCell configured with
SSB-based RLM RS in DRX mode 1012A.7.5.1.4.1 Test Purpose and
Environment 1012A.7.5.1.4.2 Test Requirements 1017A.7.5.1.5 Radio Link
Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based
RLM in non-DRX mode 1017A.7.5.1.5.1 Test Purpose and Environment
1017A.7.5.1.5.2 Test Requirements 1022A.7.5.1.6 Radio Link Monitoring
In-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX
mode 1022A.7.5.1.6.1 Test Purpose and Environment 1022A.7.5.1.6.2 Test
Requirements 1027A.7.5.1.7 Radio Link Monitoring Out-of-sync Test for
FR2 PCell configured with CSI-RS-based RLM in DRX mode 1027A.7.5.1.7.1
Test Purpose and Environment 1027A.7.5.1.7.2 Test Requirements
1031A.7.5.1.8 Radio Link Monitoring In-sync Test for FR2 PCell
configured with CSI-RS-based RLM in DRX mode 1031A.7.5.1.8.1 Test
Purpose and Environment 1031A.7.5.1.8.2 Test Requirements 1036A.7.5.1.9
UE Radio Link Monitoring Scheduling Restrictions on FR2 1036A.7.5.1.9.1
Test Purpose and Environment 1036A.7.5.1.9.2 Test Requirements
1039**A.7.5.2.1** Interruptions during measurements on deactivated NR
SCC in FR2 1039A.7.5.3.1 SCell Activation and deactivation for SCell in
FR2 intra-band in non-DRX 1043A.7.5.3.1.1 Test Purpose and Environment
1043A.7.5.3.1.2 Test Requirements 1045A.7.5.3.2 SCell Activation and
deactivation for FR1+FR2 inter-band with target SCell in FR2
1045A.7.5.3.2.1 Test Purpose and Environment 1045A.7.5.3.2.2 Test
Requirements 1049A.7.5.5.1 Beam Failure Detection and Link Recovery Test
for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode
1050A.7.5.5.1.1 Test Purpose and Environment 1050A.7.5.5.1.2 Test
Requirements 1054A.7.5.5.2 Beam Failure Detection and Link Recovery Test
for FR2 PCell configured with SSB-based BFD and LR in DRX mode
1055A.7.5.5.2.1 Test Purpose and Environment 1055A.7.5.5.2.2 Test
Requirements 1058A.7.5.5.3 Beam Failure Detection and Link Recovery Test
for FR2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode
1059A.7.5.5.3.1 Test Purpose and Environment 1059A.7.5.5.3.2 Test
Requirements 1063A.7.5.5.4 Beam Failure Detection and Link Recovery Test
for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode
1063A.7.5.5.4.1 Test Purpose and Environment 1063A.7.5.5.4.2 Test
Requirements 1067A.7.5.5.5 Scheduling availability restriction during
Beam Failure Detection and Link Recovery for FR2 PCell configured with
SSB-based BFD and LR in non-DRX mode 1067A.7.5.5.5.1 Test Purpose and
Environment 1067A.7.5.5.5.2 Test Requirements 1071A.7.5.6.1 DCI-based
and Timer-based Active BWP Switch 1072A.7.5.6.1.1 NR FR2- NR FR2 DL
active BWP switch of SCell with non-DRX in SA 1072A.7.5.6.1.2 NR FR1- NR
FR2 DL active BWP switch of SCell with non-DRX in SA 1076A.7.5.6.1.3 NR
FR2 DL active BWP switch with non-DRX in SA 1080A.7.5.6.1.3.1 Test
Purpose and Environment 1080A.7.5.6.1.3.2 Test Requirements
1083A.7.5.6.2 RRC-based Active BWP Switch 1083A.7.5.7.1 Addition and
Release Delay of known NR PSCell 1087A.7.5.7.1.1 Test Purpose and
Environment 1087A.7.5.7.2 Addition and Release Delay of unknown NR
PSCell 1090A.7.5.7.2.1 Test Purpose and Environment 1090A.7.5.8.1 MAC-CE
based active TCI state switch 1093A.7.5.8.2 RRC based active TCI state
switch 1097A.7.6 Measurement procedure 1101A.7.6.1.1 SA event triggered
reporting test without gap under non-DRX 1101A.7.6.1.1.1 Test purpose
and Environment 1101A.7.6.1.1.2 Test Requirements 1104A.7.6.1.2 SA event
triggered reporting test without gap under DRX 1105A.7.6.1.2.1 Test
purpose and Environment 1105A.7.6.1.2.2 Test Requirements 1108A.7.6.1.3
SA event triggered reporting test with per-UE gaps under non-DRX
1108A.7.6.1.3.1 Test purpose and Environment 1108A.7.6.1.3.2 Test
Requirements 1112A.7.6.1.4 SA event triggered reporting test with per-UE
gaps under DRX 1112A.7.6.1.4.1 Test purpose and Environment
1112A.7.6.1.4.2 Test Requirements 1115A.7.6.2.1 SA event triggered
reporting tests For FR2 without SSB time index detection when DRX is not
used (PCell in FR2) 1115A.7.6.2.1.1 Test Purpose and Environment
1115A.7.6.2.1.2 Test Requirements 1119A.7.6.2.2 SA event triggered
reporting tests For FR2 without SSB time index detection when DRX is
used (PCell in FR2) 1119A.7.6.2.2.1 Test Purpose and Environment
1119A.7.6.2.2.2 Test Requirements 1122A.7.6.2.3 SA event triggered
reporting tests For FR2 with SSB time index detection when DRX is not
used (PCell in FR2) 1122A.7.6.2.3.1 Test Purpose and Environment
1122A.7.6.2.3.2 Test Requirements 1126A.7.6.2.4 SA event triggered
reporting tests For FR2 with SSB time index detection when DRX is used
(PCell in FR2) 1126A.7.6.2.4.1 Test Purpose and Environment
1126A.7.6.2.4.2 Test Requirements 1129A.7.6.2.5 SA event triggered
reporting tests for FR2 without SSB time index detection when DRX is not
used (PCell in FR1) 1129A.7.6.2.5.1 Test Purpose and Environment
1129A.7.6.2.5.2 Test Requirements 1132A.7.6.2.6 SA event triggered
reporting tests for FR2 without SSB time index detection when DRX is
used (PCell in FR1) 1133A.7.6.2.6.1 Test Purpose and Environment
1133A.7.6.2.6.2 Test Requirements 1136A.7.6.2.7 SA event triggered
reporting tests for FR2 with SSB time index detection when DRX is not
used (PCell in FR1) 1137A.7.6.2.7.1 Test Purpose and Environment
1137A.7.6.2.7.2 Test Requirements 1140A.7.6.2.8 SA event triggered
reporting tests for FR2 with SSB time index detection when DRX is used
(PCell in FR1) 1141A.7.6.2.8.1 Test Purpose and Environment
1141A.7.6.2.8.2 Test Requirements 1144A.7.6.3 L1-RSRP measurement for
beam reporting 1145A.7.6.3.1 SSB based L1-RSRP measurement when DRX is
not used 1145A.7.6.3.1.1 Test Purpose and Environment 1145A.7.6.3.1.2
Test parameters 1145A.7.6.3.1.3 Test Requirements 1147A.7.6.3.2 SSB
based L1-RSRP measurement when DRX is used 1147A.7.6.3.2.1 Test Purpose
and Environment 1147A.7.6.3.2.2 Test parameters 1148A.7.6.3.2.3 Test
Requirements 1150A.7.6.3.3 CSI-RS based L1-RSRP measurement when DRX is
not used 1150A.7.6.3.3.1 Test Purpose and Environment 1150A.7.6.3.3.2
Test parameters 1151A.7.6.3.3.3 Test Requirements 1153A.7.6.3.4 CSI-RS
based L1-RSRP measurement when DRX is used 1154A.7.6.3.4.1 Test Purpose
and Environment 1154A.7.6.3.4.2 Test parameters 1154A.7.6.3.4.3 Test
Requirements 1156A.7.7 Measurement Performance requirements
1157A.7.7.1.1 SA intra-frequency case measurement accuracy with FR2
serving cell and FR2 target cell 1157A.7.7.1.1.1 Test Purpose and
Environment 1157A.7.7.1.1.2 Test parameters 1157A.7.7.1.1.3 Test
Requirements 1160A.7.7.1.2 SA inter-frequency case measurement accuracy
with FR2 serving cell and FR2 target cell 1160A.7.7.1.2.1 Test Purpose
and Environment 1160A.7.7.1.2.2 Test parameters 1161A.7.7.1.2.3 Test
Requirements 1165A.7.7.1.3 SA inter-frequency measurement accuracy with
FR1 serving cell and FR2 target cell 1166A.7.7.1.3.1 Test Purpose and
Environment 1166A.7.7.1.3.2 Test parameters 1166A.7.7.1.3.3 Test
Requirements 1168A.7.7.2 SS-RSRQ 1169A.7.7.2.1 SA intra-frequency
measurement accuracy with FR2 serving cell and FR2 target cell
1169A.7.7.2.1.1 Test Purpose and Environment 1169A.7.7.2.1.2 Test
Parameters 1169A.7.7.2.1.3 Test Requirements 1171A.7.7.2.2 SA
Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 1171A.7.7.2.2.1 Test Purpose and Environment 1171A.7.7.2.2.2
Test Parameters 1171A.7.7.2.2.3 Test Requirements 1173A.7.7.3.1 SA
intra-frequency case measurement accuracy with FR2 serving cell and FR2
target cell 1173A.7.7.3.1.1 Test Purpose and Environment 1173A.7.7.3.1.2
Test Parameters 1174A.7.7.3.1.3 Test Requirements 1175A.7.7.3.2 SA
Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD
target cell 1175A.7.7.3.2.1 Test Purpose and Environment 1175A.7.7.3.2.2
Test Parameters 1175A.7.7.3.2.3 Test Requirements 1177A.7.7.4.1 SSB
based L1-RSRP measurement 1177A.7.7.4.1.1 Test Purpose and Environment
1177A.7.7.4.1.2 Test parameters 1178A.7.7.4.1.3 Test Requirements
1180A.7.7.4.2 CSI-RS based L1-RSRP measurement on resource set with
repetition off 1181A.7.7.4.2.1 Test Purpose and Environment
1181A.7.7.4.2.2 Test parameters 1181A.7.7.4.2.3 Test Requirements
1183A.8 E-UTRA standalone tests for NR RRM 1184A.8.1 Void 1184A.8.2
RRC\_IDLE state mobility 1184A.8.2.1 Inter-RAT NR Cell re-selection
1184A.8.2.1.1 E-UTRA Cell reselection to higher priority NR target Cell
in FR1 1184A.8.2.1.1.1 Test Purpose and Environment 1184A.8.2.1.1.2 Test
Requirements 1187A.8.3 RRC\_CONNECTED state mobility 1188A.8.3.1
Handover 1188A.8.3.1.1 E-UTRAN - NR handover in FR1 1188A.8.3.1.1.1 Test
Purpose and Environment 1188A.8.3.1.1.2 Test Requirements 1193A.8.4
Measurement procedure 1193A.8.4.1.1 E-UTRA -- NR Inter-RAT SFTD
Measurement Delay in non-DRX 1193A.8.4.1.1.1 Test Purpose and
Environment 1193A.8.4.1.1.2 Test Requirements 1195A.8.4.1.2 E-UTRA -- NR
Inter-RAT SFTD Measurement Delay in DRX 1196A.8.4.1.2.1 Test Purpose and
Environment 1196A.8.4.1.2.2 Test Requirements 1197A.8.4.2 E-UTRA -- NR
Inter-RAT Measurements 1197A.8.4.2.1 NR Inter-RAT event triggered
reporting tests for FR1 without SSB time index detection when DRX is not
used 1197A.8.4.2.1.1 Test Purpose and Environment 1197A.8.4.2.1.2 Test
Requirements 1201A.8.4.2.2 NR Inter-RAT event triggered reporting tests
for FR1 without SSB time index detection when DRX is used
1202A.8.4.2.2.1 Test Purpose and Environment 1202A.8.4.2.2.2 Test
Requirements 1205A.8.4.2.3 NR Inter-RAT event triggered reporting tests
for FR1 with SSB time index detection when DRX is not used
1206A.8.4.2.3.1 Test Purpose and Environment 1206A.8.4.2.3.2 Test
Requirements 1210A.8.4.2.4 NR Inter-RAT event triggered reporting tests
for FR1 with SSB time index detection when DRX is used 1210A.8.4.2.4.1
Test Purpose and Environment 1210A.8.4.2.4.2 Test Requirements
1215A.8.4.2.5 NR Inter-RAT event triggered reporting tests for FR2
without SSB time index detection when DRX is not used 1216A.8.4.2.5.1
Test Purpose and Environment 1216A.8.4.2.5.2 Test Requirements
1218A.8.4.2.6 NR Inter-RAT event triggered reporting tests for FR2
without SSB time index detection when DRX is used 1219A.8.4.2.6.1 Test
Purpose and Environment 1219A.8.4.2.6.2 Test Requirements 1221A.8.4.2.7
NR Inter-RAT event triggered reporting tests for FR2 with SSB time index
detection when DRX is not used 1222A.8.4.2.7.1 Test Purpose and
Environment 1222A.8.4.2.7.2 Test Requirements 1224A.8.4.2.8 NR Inter-RAT
event triggered reporting tests for FR2 with SSB time index detection
when DRX is used 1225A.8.4.2.8.1 Test Purpose and Environment
1225A.8.4.2.8.2 Test Requirements 1227A.8.5 Measurement performance
1228A.8.5.1.1 SFTD accuracy 1228A.8.5.1.1.1 Test Purpose 1228A.8.5.1.1.2
Test Environment 1228A.8.5.1.1.3 Test Requirements 1232A.8.5.2 E-UTRA --
NR Inter-RAT Measurement Performance requirements 1232A.8.5.2.1 SS-RSRP
1232A.8.5.2.1.1 E-UTRAN -- NR inter-RAT measurements with FR1 target
cell 1232A.8.5.2.1.2 E-UTRAN -- NR inter-RAT measurements with FR2
target cell 1236A.8.5.2.1.2.1 Test Purpose and Environment
1236A.8.5.2.1.2.2 Test Parameters 1236A.8.5.2.1.2.3 Test Requirements
1238A.8.5.2.2 SS-RSRQ 1239A.8.5.2.2.1 E-UTRAN -- NR inter-RAT
measurements with FR1 target cell 1239A.8.5.2.2.2 E-UTRAN -- NR
inter-RAT measurements with FR2 target cell 1242A.8.5.2.2.2.1 Test
Purpose and Environment 1242A.8.5.2.2.2.2 Test Parameters
1242A.8.5.2.2.2.3 Test Requirements 1244A.8.5.2.3 SS-SINR
1245A.8.5.2.3.1 E-UTRAN -- NR inter-RAT measurements with FR1 target
cell 1245A.8.5.2.3.2 E-UTRAN -- NR inter-RAT measurements with FR2
target cell 1248A.8.5.2.3.2.1 Test Purpose and Environment
1248A.8.5.2.3.2.2 Test Parameters 1248A.8.5.2.3.2.3 Test Requirements
1249Annex B (normative): Conditions for RRM requirements applicability
for operating bands 1247B.1 Conditions for NR RRC\_IDLE state mobility
1247B.1.1 Introduction 1247B.1.2 Conditions for measurements on NR
intra-frequency cells for cell re-selection 1247B.1.3 Conditions for
measurements on NR inter-frequency cells for cell re-selection 1248B.2
Conditions for UE measurements procedures and performance requirements
in RRC\_CONNECTED state 1249B.2.1 Introduction 1249B.2.1.1 General
1249B.2.1.2 Derivation of Minimum SSB\_RP values for FR1 1249B.2.1.3
Derivation of Minimum SSB\_RP values for FR2 1249B.2.1.3.1 Minimum
SSB\_RP values for Rx Beam Peak angle of arrival 1249B.2.1.4 Gain to
SS-RSRP measurement point for FR1 1251B.2.1.5 Gain to SS-RSRP
measurement point for FR2 1251B.2.1.5.1 Gain to SS-RSRP measurement
point for Rx Beam Peak angle of arrival 1251B.2.1.5.2 Gain to SS-RSRP
measurement point for different frequency 1251B.2.1.5.3 Alignment of
Rough beam to Rx beam Peak 1252B.2.2 Conditions for NR intra-frequency
measurements 1252B.2.3 Conditions for NR inter-frequency measurements
1253B.2.4 Conditions for NR L1-RSRP reporting 1254B.2.4.1 Conditions for
SSB based L1-RSRP reporting 1254B.2.4.2 Conditions for CSI-RS based
L1-RSRP reporting 1255B.2.5 Conditions for RRC connection release with
redirection to NR 1257B.2.6 Void 1258B.2.6.1 Void 1258B.2.6.2 Void
1258B.3 RRM Requirements Exceptions 1258B.3.1 Introduction 1258B.3.2
Receiver sensitivity relaxation for CA 1258B.3.2.1 Receiver sensitivity
relaxation for UE supporting CA in FR1 1258B.3.2.2 Receiver sensitivity
relaxation for UE configured with CA in FR1 1258B.3.2.2.1 Inter-band
carrier aggregation 1258B.3.2.2.2 Reference sensitivity exceptions due
to UL harmonic interference for CA 1258B.3.2.2.3 Reference sensitivity
exceptions due to intermodulation interference due to 2UL CA 1259B.3.2.3
Receiver sensitivity relaxation for UE supporting CA in FR2 1259B.3.2.4
Receiver sensitivity relaxation for UE configured with CA in FR2
1259B.3.2.4.1 Intra-band contiguous carrier aggregation 1259B.3.2.4.2
Intra-band non-contiguous carrier aggregation 1259B.3.3 Receiver
sensitivity relaxation for DC 1259B.3.3.1 Receiver sensitivity
relaxation for EN-DC 1259B.3.3.2 Receiver sensitivity relaxation for
NE-DC 1259B.3.4 Receiver sensitivity relaxation for SUL 1259B.3.4.1
Receiver sensitivity relaxation for UE supporting SUL in FR1 1259B.3.4.2
Receiver sensitivity relaxation for UE configured with SUL in FR1
1259B.3.4.2.1 Reference sensitivity exceptions due to UL harmonic
interference for SUL 1259Annex C (informative): Change history 1261
