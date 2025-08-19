| 3GPP TS 38.133 V16.24.0 (2025-06)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 3GPP TS 38.133 V16.24.0 (2025-06)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Technical Specification                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Technical Specification                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 3rd Generation Partnership Project; Technical Specification Group Radio Access Network; NR; Requirements for support of radio resource management (Release 16)                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 3rd Generation Partnership Project; Technical Specification Group Radio Access Network; NR; Requirements for support of radio resource management (Release 16)                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP. The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification. Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices. | The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP. The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification. Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices. |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3GPP Postal address  3GPP support office address 650 Route des Lucioles - Sophia Antipolis Valbonne - FRANCE Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16 Internet http://www.3gpp.org                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Copyright Notification No part may be reproduced except as authorized by written permission. The copyright and the foregoing restriction extend to reproduction in all media.  © 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC). All rights reserved.  UMTS™ is a Trade Mark of ETSI registered for the benefit of its members 3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners GSM® and the GSM logo are registered and owned by the GSM Association |

## Contents

Foreword	69

1	Scope	71

2	References	71

3	Definitions, symbols and abbreviations	72

3.1	Definitions	72

3.2	Symbols	73

3.3	Abbreviations	74

3.4	Test tolerances	77

3.5	Frequency bands grouping	77

3.5.1	Introduction	77

3.5.2	NR operating bands in FR1	77

3.5.3	NR operating bands in FR2	78

3.6	Applicability of requirements in this specification version	78

3.6.1	RRC connected state requirements in DRX	79

3.6.2	Number of serving carriers	79

3.6.2.1	Number of serving carriers for SA	79

3.6.2.2	Number of serving carriers for EN-DC	79

3.6.2.3	Number of serving carriers for NE-DC	79

3.6.2.4	Number of serving carriers for NR-DC	80

3.6.3	Applicability for intra-band FR2	80

3.6.4	Applicability for FR2 UE power classes	80

3.6.5	Applicability for SDL bands	80

3.6.6	Applicability of requirements for NGEN-DC operation	80

3.6.7	Applicability of QCL	80

3.6.9	Applicability of requirements for scheduling availability	81

3.6.10	Applicability of requirements for measurement restrictions	81

4	SA: RRC\_IDLE state mobility	81

4.1	Cell Selection	81

4.2	Cell Re-selection	81

4.2.1	Introduction	81

4.2.2	Requirements	82

4.2.2.1	UE measurement capability	82

4.2.2.2	Measurement and evaluation of serving cell	82

4.2.2.3	Measurements of intra-frequency NR cells	83

4.2.2.4	Measurements of inter-frequency NR cells	84

4.2.2.5	Measurements of inter-RAT E-UTRAN cells	86

4.2.2.6	Maximum interruption in paging reception	88

4.2.2.7	General requirements	88

4.2.2.8	Minimum requirement at transitions	88

4.2.2.9	Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion	89

4.2.2.9.1	Introduction	89

4.2.2.9.2	Measurements for UE fulfilling low mobility criterion	89

4.2.2.9.3	Measurements for UE fulfilling not-at-cell edge criterion	90

4.2.2.9.4	Measurements for UE fulfilling low mobility and not-at-cell edge criteria	91

4.2.2.10	Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion	91

4.2.2.10.1	Introduction	91

4.2.2.10.2	Measurements for UE fulfilling low mobility criterion	91

4.2.2.10.3	Measurements for UE fulfilling not-at-cell edge criterion	92

4.2.2.10.4	Measurements for UE fulfilling low mobility and not-at-cell edge criterion	93

4.2.2.11	Measurements of inter-RAT E-UTRAN cells for UE configured with relaxed measurement criterion	94

4.2.2.11.1	Introduction	94

4.2.2.11.2	Measurements for UE fulfilling low mobility criterion	94

4.2.2.11.3	Measurements for UE fulfilling with not-at-cell edge criterion	95

4.2.2.11.4	Measurements for UE fulfilling low mobility and not-at-cell edge criterion	96

4.2A	Cell Re-selection when subject to CCA	96

4.2A.1	Introduction	96

4.2A.2	Requirements	97

4.2A.2.1	UE measurement capability	97

4.2A.2.2	Measurement and evaluation when subject to CCA on the serving cell	97

4.2A.2.3	Measurements of intra-frequency NR cells when subject to CCA on the serving cell and target cell	98

4.2A.2.4	Measurements of inter-frequency NR cells when subject to CCA on the target cell	99

4.2A.2.5	Measurements of inter-RAT E-UTRAN cells when subject to CCA on the serving cell	101

4.2A.2.6	Maximum interruption in paging reception when subject to CCA on the target cell	101

4.2A.2.7	General requirements	101

4.3	Minimization of Drive Tests (MDT)	102

4.3.1	Introduction	102

4.3.2	Measurement Requirements	102

4.3.3	Requirements for Relative Time Stamp Accuracy	102

4.3.4	Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting	103

4.3.5	Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting	103

4.4	Idle Mode CA/DC Measurements	103

4.4.1	Introduction	103

4.4.2	Measurement Requirements	103

4.4.2.1	Detected cell requirement during state transition and Idle mode	103

4.4.2.2	Measurements of inter-frequency CA/DC candidate cells	104

4.4.2.3	Measurements on serving cell	105

4.4.2.4	Measurements of E-UTRAN inter-RAT DC candidate cells	105

5	SA: RRC\_INACTIVE state mobility	107

5.1	Cell Re-selection	107

5.1.1	Introduction	107

5.1.2	Requirements	107

5.1.2.1	UE measurement capability	107

5.1.2.2	Measurement and evaluation of serving cell	107

5.1.2.3	Measurements of intra-frequency NR cells	107

5.1.2.4	Measurements of inter-frequency NR cells	107

5.1.2.5	Measurements of inter-RAT E-UTRAN cells	107

5.1.2.6	Maximum interruption in paging reception	107

5.1.2.7	General requirements	107

5.1A	Cell Re-selection with CCA	107

5.1A.1	Introduction	107

5.1A.2	Requirements	108

5.1A.2.1	UE measurement capability	108

5.1A.2.2	Measurement and evaluation when CCA is used on the serving cell	108

5.1A.2.3	Measurements of intra-frequency NR cells when CCA is used on the serving cell and target cell	108

5.1A.2.4	Measurements of inter-frequency NR cells when CCA is used on the target cell	108

5.1A.2.5	Measurements of inter-RAT E-UTRAN cells when CCA is used on the serving cell	108

5.1A.2.6	Maximum interruption in paging reception when CCA is used on the target cell	108

5.1A.2.7	General requirements	108

5.2	Void	108

5.3	Minimization of Drive Tests (MDT)	108

5.3.1	Introduction	108

5.3.2	Measurement Requirements	109

5.3.3	Requirements for Relative Time Stamp Accuracy	109

5.3.4	Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting	109

5.3.5	Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting	109

5.3.6	Requirements for Relative Time Stamp Accuracy for RRC Resume Failure Log Reporting	109

5.4	Inactive Mode CA/DC Measurements	109

5.4.1	Introduction	109

5.4.2	Measurement Requirements	109

5.4.2.1	Detected cell requirement during state transition and inactive mode	110

5.4.2.2	Measurements of inter-frequency CA/DC candidate cells	110

5.4.2.3	Measurements on serving cell	110

5.4.2.4	Measurements on E-UTRAN inter-RAT DC candidate cells	110

6	RRC\_CONNECTED state mobility	110

6.1	Handover	110

6.1.1	NR Handover	110

6.1.1.1	Introduction	110

6.1.1.2	NR FR1 - NR FR1 Handover	110

6.1.1.2.1	Handover delay	110

6.1.1.2.2	Interruption time	110

6.1.1.3	NR FR2- NR FR1 Handover	111

6.1.1.3.1	Handover delay	111

6.1.1.3.2	Interruption time	111

6.1.1.4	NR FR2- NR FR2 Handover	112

6.1.1.4.1	Handover delay	112

6.1.1.4.2	Interruption time	112

6.1.1.5	NR FR1- NR FR2 Handover	113

6.1.1.5.1	Handover delay	113

6.1.1.5.2	Interruption time	113

6.1.2	NR Handover to other RATs	114

6.1.2.1	NR – E-UTRAN Handover	114

6.1.2.1.1	Introduction	114

6.1.2.1.2	Handover delay	114

6.1.2.1.3	Interruption time	114

6.1.2.2	NR – UTRAN Handover	115

6.1.2.2.1	Introduction	115

6.1.2.2.2	Handover delay	115

6.1.2.2.3	Interruption time	115

6.1.3	NR DAPS Handover	116

6.1.3.1	Introduction	116

6.1.3.2	NR FR1 - NR FR1 DAPS Handover	116

6.1.3.2.1	DAPS handover delay	116

6.1.3.2.2	Interruption time	117

6.1.3.3	NR FR2- NR FR1 DAPS Handover	119

6.1.3.3.1	DAPS handover delay	119

6.1.3.3.2	Interruption time	119

6.1.3.4	NR FR1- NR FR2 DAPS Handover	120

6.1.3.4.1	DAPS handover delay	120

6.1.3.4.2	Interruption time	120

6.1.4	NR Conditional Handover	121

6.1.4.1	Introduction	121

6.1.4.2	NR FR1 – NR FR1 conditional handover	121

6.1.4.3	NR FR2 – NR FR1 conditional handover	122

6.1.4.4	NR FR2 – NR FR2 conditional handover	123

6.1.4.4.1	Handover delay	123

6.1.4.4.2	Measurement time	123

6.1.4.4.3	Preparation time	123

6.1.4.4.4	Interruption time	123

6.1.4.5	NR FR1 – NR FR2 conditional handover	124

6.1A	Void	124

6.1A.1	Void	124

6.1A.1.1	Void	124

6.1A.1.2	Void	124

6.1A.1.2.1	Void	124

6.1A.1.2.2	Void	124

6.1B	Handover to target cell using CCA	124

6.1B.1	NR Handover	124

6.1B.1.1	Introduction	124

6.1B.1.2	NR FR1 - NR FR1 Handover	125

6.1B.1.2.1	Handover delay	125

6.1B.1.2.2	Interruption time	125

6.2	RRC Connection Mobility Control	126

6.2.1	SA: RRC Re-establishment	126

6.2.1.1	Introduction	126

6.2.1.2	Requirements	126

6.2.1.2.1	UE Re-establishment delay requirement	126

6.2.1A	RRC Re-establishment with CCA	127

6.2.1A.1	Introduction	127

6.2.1A.2	Requirements	128

6.2.1A.2.1	UE Re-establishment with CCA delay requirement	128

6.2.2	Random access	130

6.2.2.1	Introduction	130

6.2.2.2	Requirements for 4-step RA type	130

6.2.2.2.1	Contention based random access	130

6.2.2.2.2	Non-Contention based random access	131

6.2.2.2.3	UE behaviour when configured with supplementary UL	132

6.2.2.3	Requirements for 2-step RA type	132

6.2.2.3.1	Contention based random access	132

6.2.2.3.2	Non-Contention based random access	133

6.2.2.3.3	UE behaviour when configured with supplementary UL	134

6.2.2A	Random access when CCA is used on target frequency	134

6.2.2A.1	Introduction	134

6.2.2A.2	Requirements for 4-step RA type	134

6.2.2A.2.1	Contention based random access	134

6.2.2A.2.2	Non-Contention based random access	135

6.2.2A.3	Requirements for 2-step RA type	136

6.2.2A.3.1	Contention based random access	137

6.2.2A.3.2	Non-Contention based random access	138

6.2.3	SA: RRC Connection Release with Redirection	139

6.2.3.1	Introduction	139

6.2.3.2	Requirements	139

6.2.3.2.1	RRC connection release with redirection to NR	139

6.2.3.2.2	RRC connection release with redirection to E-UTRAN	140

6.2.3.2.3	RRC connection release with redirection to NR carrier subject to CCA	140

7	Timing	141

7.1	UE transmit timing	141

7.1.1	Introduction	141

7.1.2	Requirements	142

7.1.2.1	Gradual timing adjustment	143

7.1.2.2	Void	143

7.2	UE timer accuracy	143

7.2.1	Introduction	143

7.2.2	Requirements	144

7.3	Timing advance	144

7.3.1	Introduction	144

7.3.2	Requirements	144

7.3.2.1	Timing Advance adjustment delay	144

7.3.2.2	Timing Advance adjustment accuracy	144

7.4	Cell phase synchronization accuracy	144

7.4.1	Definition	144

7.4.2	Minimum requirements	144

7.5	Maximum Transmission Timing Difference	145

7.5.1	Introduction	145

7.5.2	Minimum Requirements for inter-band EN-DC	145

7.5.2.1	Minimum Requirements for inter-band synchronous EN-DC	145

7.5.3	Minimum Requirements for intra-band EN-DC	146

7.5.4	Minimum Requirements for NR Carrier Aggregation	146

7.5.5	Minimum Requirements for inter-band NE-DC	147

7.5.5.1	Minimum Requirements for inter-band synchronous NE-DC	147

7.5.6	Minimum Requirements for inter-band NR DC	148

7.6	Maximum Receive Timing Difference	148

7.6.1	Introduction	148

7.6.2	Minimum Requirements for inter-band EN-DC	149

7.6.2.1	Minimum Requirements for inter-band synchronous EN-DC	149

7.6.3	Minimum Requirements for intra-band EN-DC	149

7.6.4	Minimum Requirements for NR Carrier Aggregation	150

7.6.5	Minimum Requirements for inter-band NE-DC	151

7.6.5.1	Minimum Requirements for inter-band synchronous NE-DC	151

7.6.6	Minimum Requirements for inter-band NR DC	151

7.7 *deriveSSB-IndexFromCell* tolerance	152

7.7.1	Minimum requirements	152

7.8	Void	152

8	Signalling characteristics	152

8.1	Radio Link Monitoring	152

8.1.1	Introduction	152

8.1.2	Requirements for SSB based radio link monitoring	153

8.1.2.1	Introduction	153

8.1.2.2	Minimum requirement	154

8.1.2.3	Measurement restrictions for SSB based RLM	156

8.1.3	Requirements for CSI-RS based radio link monitoring	156

8.1.3.1	Introduction	156

8.1.3.2	Minimum requirement	157

8.1.3.3	Measurement restrictions for CSI-RS based RLM	159

8.1.4	Minimum requirement at transitions	160

8.1.5	Minimum requirement for UE turning off the transmitter	160

8.1.6	Minimum requirement for L1 indication	160

8.1.7	Scheduling availability of UE during radio link monitoring	161

8.1.7.1	Scheduling availability of UE performing radio link monitoring with a same subcarrier spacing as PDSCH/PDCCH on FR1	161

8.1.7.2	Scheduling availability of UE performing radio link monitoring with a different subcarrier spacing than PDSCH/PDCCH on FR1	161

8.1.7.3	Scheduling availability of UE performing radio link monitoring on FR2	161

8.1.7.4	Scheduling availability of UE performing radio link monitoring on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC	162

8.1A	Radio Link Monitoring with CCA on Target Frequency	162

8.1A.1	Introduction	162

8.1A.2	Requirements for SSB Based Radio Link Monitoring	163

8.1A.2.1	Introduction	163

8.1A.2.2	Minimum Requirement	164

8.1A.3	Minimum requirement at transitions	165

8.1A.4	Minimum requirement for UE turning off the transmitter	166

8.1A.5	Minimum requirement for L1 indication	166

8.1A.6	Scheduling availability of UE during radio link monitoring	166

8.1A.6.1	Scheduling availability of UE performing radio link monitoring with the same subcarrier spacing as PDSCH/PDCCH	166

8.1A.6.2	Scheduling availability of UE performing radio link monitoring with a different subcarrier spacing than PDSCH/PDCCH	166

8.2	Interruption	167

8.2.1	EN-DC Interruption	167

8.2.1.1	Introduction	167

8.2.1.2	Requirements	167

8.2.1.2.1	Interruptions at transitions between active and non-active during DRX	167

8.2.1.2.2	Interruptions at transitions from non-DRX to DRX	168

8.2.1.2.3	Interruptions at SCell addition/release	168

8.2.1.2.4	Interruptions at SCell activation/deactivation	169

8.2.1.2.5	Interruptions during measurements on SCC	170

8.2.1.2.6	Interruptions at UL carrier RRC reconfiguration	172

8.2.1.2.7	Interruptions due to Active BWP switching Requirement	172

8.2.1.2.8	Interruptions at direct SCell activation and hibernation	173

8.2.1.2.9	Interruptions at SCell hibernation	174

8.2.1.2.10	Interruptions at SCell activation/deactivation with multiple downlink SCells	174

8.2.1.2.11	Interruptions due to UE-specific CBW change	174

8.2.1.2.12	 Interruptions at NR SRS carrier based switching	175

8.2.1.2.13	 Interruptions at E-UTRA SRS carrier based switching	176

8.2.1.2.14	DL Interruptions at switching between two uplink carriers	177

8.2.1.2.15	Interruptions due to SCell dormancy	177

8.2.1.2.16	Interruptions when identifying CGI of an NR cell with autonomous gaps	178

8.2.1.2.17	 Interruptions when identifying CGI of an E-UTRA cell with autonomous gaps	178

8.2.2	SA: Interruptions with Standalone NR Carrier Aggregation	179

8.2.2.1	Introduction	179

8.2.2.2	Requirements	180

8.2.2.2.1	Interruptions at SCell addition/release	180

8.2.2.2.2	Interruptions at SCell activation/deactivation	181

8.2.2.2.3	Interruptions during measurements on deactivated SCC	182

8.2.2.2.4	Interruptions at UL carrier RRC reconfiguration	182

8.2.2.2.5	Interruptions due to Active BWP switching Requirement	183

8.2.2.2.6	Interruptions at inter-frequency SFTD measurement	184

8.2.2.2.7	Interruptions at SCell activation/deactivation with multiple downlink SCells	185

8.2.2.2.8	Interruptions due to UE-specific CBW change	185

8.2.2.2.9	 Interruptions at NR SRS carrier based switching	185

8.2.2.2.10	DL Interruptions at UE switching between two uplink carriers	187

8.2.2.2.11	Interruptions at direct SCell activation	187

8.2.2.2.12	Interruptions due to SCell dormancy	188

8.2.2.2.13	Interruptions at transitions between active and non-active during DRX	188

8.2.2.2.14	Interruptions when identifying CGI of an NR cell with autonomous gaps	188

8.2.2.2.15	 Interruptions when identifying CGI of an E-UTRA cell with autonomous gaps	189

8.2.3	NE-DC Interruptions	189

8.2.3.1	Introduction	189

8.2.3.2	Requirements	190

8.2.3.2.1	Interruptions at transitions between active and non-active during DRX	190

8.2.3.2.2	Interruptions at transitions from non-DRX to DRX	190

8.2.3.2.3	Interruptions at PSCell/SCell addition/release	190

8.2.3.2.4	Interruptions at SCell activation/deactivation	192

8.2.3.2.5	Interruptions during measurements on SCC	193

8.2.3.2.6	Interruptions at UL carrier RRC reconfiguration	194

8.2.3.2.7	Interruptions due to Active BWP switching Requirement	194

8.2.3.2.8	Interruptions at direct SCell activation and hibernation	195

8.2.3.2.9	Interruptions at SCell hibernation	195

8.2.3.2.10	Interruptions at SCell activation/deactivation with multiple downlink SCells	195

8.2.3.2.11	 Interruptions at NR SRS carrier based switching	195

8.2.3.2.12	 Interruptions at E-UTRA SRS carrier based switching	197

8.2.3.2.13	Interruptions due to SCell dormancy	198

8.2.3.2.14	Interruptions when identifying CGI of an NR cell with autonomous gaps	198

8.2.3.2.15	 Interruptions when identifying CGI of an E-UTRA cell with autonomous gaps	199

8.2.3.2.16	Interruptions due to UE-specific CBW change	199

8.2.4	NR-DC: Interruptions	200

8.2.4.1	Introduction	200

8.2.4.2	Requirements	200

8.2.4.2.1	Interruptions at PSCell/SCell addition/release	200

8.2.4.2.3	Interruptions during measurements on SCC	202

8.2.4.2.4	Interruptions at UL carrier RRC reconfiguration	202

8.2.4.2.5	Interruptions due to Active BWP switching Requirement	203

8.2.4.2.6	Interruptions at transitions between active and non-active during DRX	203

8.2.4.2.7	Interruptions at transitions from non-DRX to DRX	203

8.2.4.2.8	Interruptions at SCell activation/deactivation with multiple downlink SCells	203

8.2.4.2.9	Interruptions at NR SRS carrier based switching	204

8.2.4.2.10	Interruptions at direct SCell activation	205

8.2.4.2.11	Interruptions when identifying CGI of an NR cell with autonomous gaps	205

8.2.4.2.12	 Interruptions when identifying CGI of an E-UTRA cell with autonomous gaps	206

8.2.4.2.13	 Interruptions due to SCell dormancy	207

8.2.4.2.14	Interruptions due to UE-specific CBW change	207

8.2.4.2A	Void	207

8.2.4.2A.1	Void	207

8.2.4.2A.2	Void	207

8.2.4.2A.3	Void	207

8.3	SCell Activation and Deactivation Delay	207

8.3.1	Introduction	207

8.3.2	SCell Activation Delay Requirement for Deactivated SCell	208

8.3.3	SCell Deactivation Delay Requirement for Activated SCell	212

8.3.4	Direct SCell Activation at SCell addition	212

8.3.5	Direct SCell Activation at Handover	214

8.3.7	SCell Activation Delay Requirement for Deactivated SCell with Multiple Downlink SCells	216

8.3.8	SCell Deactivation Delay Requirement for Activated SCell with Multiple Downlink SCells	219

8.3.9	Direct SCell Activation of Multiple Downlink SCells at SCell addition	220

8.3.10	Direct SCell Activation of Multiple Downlink SCells at Handover	221

8.3A	SCell Activation and Deactivation Delay in Carriers with CCA	222

8.3A.1	Introduction	222

8.3A.2	SCell Activation Delay Requirement for Deactivated SCell	223

8.3A.3	SCell Deactivation Delay Requirement for Activated SCell	225

8.4	UE UL carrier RRC reconfiguration delay	226

8.4.1	Introduction	226

8.4.2	UE UL carrier configuration delay requirement	226

8.4.3	UE UL carrier deconfiguration delay requirement	226

8.5	Link Recovery Procedures	226

8.5.1	Introduction	226

8.5.2	Requirements for SSB based beam failure detection	227

8.5.2.1	Introduction	227

8.5.2.2	Minimum requirement	228

8.5.2.3	Measurement restriction for SSB based beam failure detection	229

8.5.3	Requirements for CSI-RS based beam failure detection	230

8.5.3.1	Introduction	230

8.5.3.2	Minimum requirement	230

8.5.3.3	Measurement restrictions for CSI-RS beam failure detection	232

8.5.4	Minimum requirement for L1 indication	233

8.5.5	Requirements for SSB based candidate beam detection	234

8.5.5.1	Introduction	234

8.5.5.2	Minimum requirement	234

8.5.5.3	Measurement restriction for SSB based candidate beam detection	236

8.5.6	Requirements for CSI-RS based candidate beam detection	236

8.5.6.1	Introduction	236

8.5.6.2	Minimum requirement	236

8.5.6.3	Measurement restriction for CSI-RS based candidate beam detection	239

8.5.7	Scheduling availability of UE during beam failure detection	239

8.5.7.1	Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1	239

8.5.7.2	Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH on FR1	239

8.5.7.3	Scheduling availability of UE performing beam failure detection on FR2	240

8.5.7.4	Scheduling availability of UE performing beam failure detection on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR DC	240

8.5.8	Scheduling availability of UE during candidate beam detection	240

8.5.8.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	240

8.5.8.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	241

8.5.8.3	Scheduling availability of UE performing L1-RSRP measurement on FR2	241

8.5.8.4	Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC	241

8.5.9	Requirements for Beam Failure Recovery in SCell	242

8.5.9.1	Introduction	242

8.5.9.2	Requirement	242

8.5.10	Minimum requirement at transitions for beam failure detection	242

8.5A	Link Recovery Procedures when CCA is used on target frequency	243

8.5A.1	Introduction	243

8.5A.2	Requirements for SSB based beam failure detection	243

8.5A.2.1	Introduction	243

8.5A.2.2	Minimum requirement	244

8.5A.2.3	Measurement restriction for SSB based beam failure detection	244

8.5A.4	Minimum requirement for L1 indication	245

8.5A.5	Requirements for SSB based candidate beam detection	245

8.5A.5.1	Introduction	245

8.5A.5.2	Minimum requirement	245

8.5A.5.3	Measurement restriction for SSB based candidate beam detection	246

8.5A.7	Scheduling availability of UE during beam failure detection	246

8.5A.7.1	Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH	246

8.5A.7.2	Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH	246

8.5A.8	Scheduling availability of UE during candidate beam detection	246

8.5A.8.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH	247

8.5A.8.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH	247

8.6	Active BWP switch delay	247

8.6.1	Introduction	247

8.6.2	DCI and timer based BWP switch delay on a single CC	247

8.6.2A	DCI based BWP switch delay on multiple CCs	248

8.6.2A.1	Simultaneous DCI based BWP switch delay on multiple CCs	248

8.6.2A.2	Non-simultaneous DCI based BWP switch delay on multiple CCs	250

8.6.2B	Timer based BWP switch delay on multiple CCs	250

8.6.2B.1	Simultaneous timer based BWP switch delay on multiple CCs	250

8.6.2B.2	Non-simultaneous timer based BWP switch delay on multiple CCs	251

8.6.3	RRC based BWP switch delay on a single CC	251

8.6.3A	RRC based BWP switch delay on multiple CCs	252

8.6.3A.1	Simultaneous RRC based BWP switch delay on multiple CCs	252

8.6.3A.2	Non-simultaneous RRC based BWP switch delay on multiple CCs	252

8.6.4	BWP switch delay on Consistent UL CCA recovery	253

8.7	Void	253

8.8	NE-DC: E-UTRAN PSCell Addition and Release Delay	253

8.8.1	Introduction	253

8.8.2	E-UTRAN PSCell Addition Delay Requirement	253

8.8.3	E-UTRAN PSCell Release Delay Requirement	254

8.9	NR-DC: PSCell Addition and Release Delay	254

8.9.1	Introduction	254

8.9.2	PSCell Addition Delay Requirement	254

8.9.3	PSCell Release Delay Requirement	255

8.10	Active TCI state switching delay	255

8.10.4	DCI based TCI state switch delay	257

8.10.5	RRC based TCI state switch delay	257

8.10.6	Active TCI state list update delay	257

8.10A	Active TCI state switching delay with CCA	258

8.10A.1	Introduction	258

8.10A.2	Known conditions for TCI state	258

8.10A.3	MAC-CE based TCI state switch delay	258

8.10A.4	DCI based TCI state switch delay	259

8.10A.5	RRC based TCI state switch delay	259

8.10A.6	Active TCI state list update delay	260

8.11	PSCell Change	260

8.11A	void	261

8.11B	Conditional PSCell Change	261

8.11B.1	Introduction	261

8.11B.2	Conditoinal PSCell Change delay	261

8.11B.2.1	Measurement time	261

8.12	Uplink spatial relation switch delay	262

8.12.1	Introduction	262

8.12.2	Known conditions for spatial relation when associated with DL-RS	262

8.12.3	MAC-CE based spatial relation switch delay	262

8.12.4	DCI based spatial relation switch delay	263

8.12.5	RRC based spatial relation switch delay	263

8.13	UE-specific CBW change	264

8.13.1	Introduction	264

8.13.2	UE-specific CBW change delay	264

8.14	Pathloss reference signal switching delay	264

8.14.1	Introduction	264

8.14.2	Known conditions for pathloss reference signal	264

8.14.3	MAC-CE based pathloss reference signal switch delay	265

9	Measurement Procedure	266

9.1	General measurement requirement	266

9.1.1	Introduction	266

9.1.2	Measurement gap	266

9.1.2.1	EN-DC: Measurement Gap Sharing	277

9.1.2.1a	SA: Measurement Gap Sharing	277

9.1.2.1b	NE-DC: Measurement Gap Sharing	278

9.1.2.1c	NR-DC: Measurement Gap Sharing	279

9.1.3	UE Measurement capability	280

9.1.3.1	EN-DC: Monitoring of multiple layers using gaps	280

9.1.3.1a	SA: Monitoring of multiple layers using gaps	280

9.1.3.1b	NE-DC: Monitoring of multiple layers using gaps	281

9.1.3.1c	NR-DC: Monitoring of multiple layers using gaps	281

9.1.3.2	EN-DC: Maximum allowed layers for multiple monitoring	282

9.1.3.2a	SA: Maximum allowed layers for multiple monitoring	283

9.1.3.2b	NE-DC: Maximum allowed layers for multiple monitoring	283

9.1.3.2c	NR-DC: Maximum allowed layers for multiple monitoring	284

9.1A.3.2	Void	285

9.1.3A	UE Measurement capability under operation mode with CCA	285

9.1.3A.1	EN-DC: Monitoring of multiple layers using gaps under CCA	285

9.1.3A.1A	SA: Monitoring of multiple layers using gaps under CCA	285

9.1.3A.2	EN-DC: Maximum allowed layers for multiple monitoring under CCA	285

9.1A.3.2a	Void	286

9.1.3A.2A	SA: Maximum allowed layers for multiple monitoring under CCA	286

9.1.4	Capabilities for Support of Event Triggering and Reporting Criteria	286

9.1.4.1	Introduction	286

9.1.4.2	Requirements	286

9.1.5	Carrier-specific scaling factor	290

9.1.5.1	Monitoring of multiple layers outside gaps	290

9.1.5.1.1	EN-DC mode: carrier-specific scaling factor for SSB-based, CSI-RS based L3 measurements and RSSI and channel occupancy measurements performed outside gaps	292

9.1.5.1.2	SA mode: carrier-specific scaling factor for SSB-based, CSI-RS based L3 measurements and RSSI and channel occupancy measurements performed outside gaps	293

9.1.5.1.3	NR-DC mode: carrier-specific scaling factor for SSB-based and CSI-RS based L3 measurements performed outside gaps	294

9.1.5.1.4	NE-DC mode: carrier-specific scaling factor for SSB-based and CSI-RS based measurements performed outside gaps	295

9.1.5.2	Monitoring of multiple layers within gaps	296

9.1.5.2.1	EN-DC mode: carrier-specific scaling factor for SSB, CSI-RS-based L3 measurements and RSSI and channel occupancy measurements performed within gaps	297

9.1.5.2.2	SA mode: carrier-specific scaling factor for SSB, CSI-RS-based L3 measurements and RSSI and channel occupancy measurements performed within gaps	299

9.1.5.2.3	NE-DC: carrier-specific scaling factor for SSB-based and CSI-RS based L3 measurements performed within gaps	301

9.1.5.2.4	NR-DC: carrier-specific scaling factor for SSB-based and CSI-RS-based L3 measurements performed within gaps	303

9.1.5.2.5	SA mode: carrier-specific scaling factor for PRS-based measurements performed within gaps	304

9.1.5.2.6	NE-DC: carrier-specific scaling factor for PRS-based measurements performed within gaps	305

9.1.5.2.7	NR-DC: carrier-specific scaling factor for PRS-based measurements performed within gaps	305

9.1.6	Minimum requirement at transitions	305

9.2	NR intra-frequency measurements	305

9.2.1	Introduction	305

9.2.2	Requirements applicability	306

9.2.3	Number of cells and number of SSB	306

9.2.3.1	Requirements for FR1	306

9.2.3.2	Requirements for FR2	306

9.2.4	Measurement Reporting Requirements	307

9.2.4.1	Periodic Reporting	307

9.2.4.2	Event-triggered Periodic Reporting	307

9.2.4.3	Event Triggered Reporting	307

9.2.5	Intrafrequency measurements without measurement gaps	308

9.2.5.1	Intrafrequency cell identification	308

9.2.5.2	Measurement period	310

9.2.5.3	Scheduling availability of UE during intra-frequency measurements	312

9.2.5.3.1	Scheduling availability of UE performing measurements in TDD bands on FR1	312

9.2.5.3.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	312

9.2.5.3.3	Scheduling availability of UE performing measurements on FR2	313

9.2.5.3.4	Scheduling availability of UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA	314

9.2.5.4	SFTD Measurements between PCell and PSCell	314

9.2.5.4.1	Introduction	314

9.2.5.4.2	SFTD Measurement delay	314

9.2.5.4.3	SFTD Measurement Reporting Delay	315

9.2.6	Intra-frequency measurements with measurement gaps	315

9.2.6.1	Void	315

9.2.6.2	Intra-frequency cell identification	315

9.2.6.3	Intrafrequency Measurement Period	317

9.2A	NR intra-frequency measurements with CCA	318

9.2A.1	Introduction	318

9.2A.2	Requirements applicability	318

9.2A.3	Number of cells and number of SSB	319

9.2A.4	Measurement Reporting Requirements	319

9.2A.5	Intra-frequency measurements without measurement gaps	319

9.2A.5.2	Measurement period	322

9.2A.5.3	Scheduling availability of UE during intra-frequency measurements	323

9.2A.5.3.1	Scheduling availability of UE performing measurements in TDD bands	323

9.2A.5.3.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH	323

9.2A.6	Intra-frequency measurements with measurement gaps	324

9.2A.6.1	Intra-frequency cell identification	324

9.2A.6.2	Intra-frequency Measurement Period	325

9.2A.7	Intra-frequency RSSI and Channel occupancy measurements	326

9.2A.7.1	Intra-frequency RSSI measurements	326

9.2A.7.2	Intra-frequency Channel occupancy measurements	327

9.2A.7.3	Scheduling restriction during RSSI and Channel Occupancy measurements	327

9.3	NR inter-frequency measurements	328

9.3.1	Introduction	328

9.3.2	Requirements applicability	328

9.3.2.1	Void	329

9.3.2.2	Void	329

9.3.3	Number of cells and number of SSB	329

9.3.3.1	Requirements for FR1	329

9.3.3.2	Requirements for FR2	329

9.3.4	Inter-frequency measurement with measurement gaps	329

9.3.4.1	Void	330

9.3.4.2	Void	330

9.3.5	Inter-frequency measurements	330

9.3.5.1	Void	331

9.3.5.2	Void	331

9.3.5.3	Void	331

9.3.6	Inter-frequency measurements reporting requirements	331

9.3.6.1	Periodic Reporting	331

9.3.6.2	Event-triggered Periodic Reporting	331

9.3.6.3	Event-triggered Reporting	331

9.3.7	Void	332

9.3.8	Inter-frequency SFTD measurement requirements	332

9.3.8.1	Introduction	332

9.3.8.2	SFTD Measurement delay	332

9.3.8.3	SFTD Measurement reporting delay	333

9.3.9	Inter frequency measurements without measurement gaps	333

9.3.9.1	Inter frequency Cell identification	333

9.3.9.2	Measurement period	335

9.3.9.3	Scheduling availability of UE during inter-frequency measurements	336

9.3.9.3.1	Scheduling availability of UE performing measurements in TDD bands on FR1	336

9.3.9.3.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	336

9.3.9.3.3	Scheduling availability of UE performing measurements on FR2	337

9.3.9.3.4	Scheduling availability of UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA	337

9.3A	NR inter-frequency measurements in carrier frequencies with CCA	337

9.3A.1	Introduction	337

9.3A.2	Requirements applicability	338

9.3A.3	Number of cells and number of SSB	338

9.3A.3.1	Requirements	338

9.3A.4	Inter-frequency cell identification	338

9.3A.5	Inter-frequency measurements	340

9.3A.6	NR Inter-frequency measurements reporting requirements	340

9.3A.6.1	Periodic Reporting	340

9.3A.6.2	Event-triggered Periodic Reporting	340

9.3A.6.3	Event-triggered Reporting	340

9.3A.8	Inter-frequency RSSI measurements	341

9.3A.9	Inter-frequency channel occupancy measurements	341

9.4	Inter-RAT measurements	342

9.4.1	Introduction	342

9.4.2	NR − E-UTRAN FDD measurements	343

9.4.2.1	Introduction	343

9.4.2.2	Requirements when no DRX is used	344

9.4.2.3	Requirements when DRX is used	344

9.4.2.4	Measurement reporting requirements	345

9.4.2.4.1	Periodic Reporting	345

9.4.2.4.2	Event-Triggered Periodic Reporting	346

9.4.2.4.3	Event-Triggered Reporting	346

9.4.3	NR − E-UTRAN TDD measurements	346

9.4.3.1	Introduction	346

9.4.3.2	Requirements when no DRX is used	346

9.4.3.3	Requirements when DRX is used	347

9.4.3.4	Measurement reporting requirements	349

9.4.3.4.1	Periodic Reporting	349

9.4.3.4.2	Event-Triggered Periodic Reporting	349

9.4.3.4.3	Event-Triggered Reporting	349

9.4.4	Inter-RAT RSTD measurements	349

9.4.4.1	NR − E-UTRAN FDD RSTD measurements	349

9.4.4.1.1	Introduction	349

9.4.4.1.2	Requirements	350

9.4.4.2	NR − E-UTRAN TDD RSTD measurements	353

9.4.4.2.1	Introduction	353

9.4.4.2.2	Requirements	354

9.4.5	Inter-RAT E-CID measurements	357

9.4.5.1	NR−E-UTRAN FDD E-CID RSRP and RSRQ measurements	357

9.4.5.1.1	Introduction	357

9.4.5.1.2	Requirements	357

9.4.5.1.3	Measurement Reporting Delay	357

9.4.5.2	NR−E-UTRAN TDD E-CID RSRP and RSRQ measurements	357

9.4.5.2.1	Introduction	357

9.4.5.2.2	Requirements	357

9.4.5.2.3	Measurement Reporting Delay	358

9.4.6	NR − UTRAN FDD measurements	358

9.4.6.1	Introduction	358

9.4.6.2	Requirements when no DRX is used	358

9.4.6.3	Requirements when DRX is used	359

9.4.7	NR – E-UTRAN measurements with autonomous gaps	361

9.4.7.1	CGI identification of an E-UTRA cell with autonomous gaps	361

9.4.7.2	CGI reporting delay	361

9.5	L1-RSRP measurements for Reporting	362

9.5.1	Introduction	362

9.5.2	Requirements applicability	362

9.5.3	Measurement Reporting Requirements	362

9.5.3.1	Periodic Reporting	363

9.5.3.2	Semi-Persistent Reporting	363

9.5.3.3	Aperiodic Reporting	363

9.5.4	L1-RSRP measurement requirements	363

9.5.4.1	SSB based L1-RSRP Reporting	363

9.5.4.2	CSI-RS based L1-RSRP Reporting	365

9.5.4A	Void	368

9.5.4A.1	Void	368

9.5.5	Measurement restriction for CSI-RS and SSB for L1-RSRP measurement	368

9.5.5.1	Measurement restriction for SSB based L1-RSRP	368

9.5.5.2	Measurement restriction for CSI-RS based L1-RSRP	368

9.5.6	Scheduling availability of UE during L1-RSRP measurement	369

9.5.6.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	369

9.5.6.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	369

9.5.6.3	Scheduling availability of UE performing L1-RSRP measurement on FR2	370

9.5.6.4	Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA	370

9.5A	L1-RSRP measurements for Reporting under CCA	371

9.5A.1	Introduction	371

9.5A.2	Requirements applicability	371

9.5A.3	Measurement Reporting Requirements	371

9.5A.3.1	Periodic Reporting	371

9.5A.3.2	Semi-Persistent Reporting	372

9.5A.3.3	Aperiodic Reporting	372

9.5A.4	L1-RSRP measurement requirements	372

9.5A.4.1	SSB based L1-RSRP Reporting	372

9.5A.5	Measurement restriction for L1-RSRP measurement	373

9.5A.5.1	Measurement restriction for SSB based L1-RSRP	373

9.5A.6	Scheduling availability of UE during L1-RSRP measurement	373

9.5A.6.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH	373

9.5A.6.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH	374

9.5A.6.3	Scheduling availability of UE performing L1-RSRP measurement in case of FR1-FR2 inter-band CA	374

9.6	NE-DC: Measurements	374

9.6.1	Introduction	374

9.6.2	SFTD Measurements	374

9.6.2.1	Introduction	374

9.6.2.2	SFTD Measurement requirements	374

9.7	Cross Link Interference measurements	375

9.7.1	Introduction	375

9.7.2	SRS-RSRP measurements	375

9.7.2.1	Introduction	375

9.7.2.2	Requirements applicability	375

9.7.2.3	Measurement Reporting Requirements	376

9.7.2.3.1	Periodic Reporting	376

9.7.2.3.2	Event-triggered Periodic Reporting	376

9.7.2.3.3	Event Triggered Reporting	376

9.7.2.4	Measurement capability	376

9.7.2.5	SRS-RSRP measurement period	376

9.7.3	CLI-RSSI measurements	377

9.7.3.1	Introduction	377

9.7.3.2	Requirements applicability	377

9.7.3.3	Measurement Reporting Requirements	377

9.7.3.3.1	Periodic Reporting	377

9.7.3.3.2	Event-triggered Periodic Reporting	377

9.7.3.3.3	Event Triggered Reporting	377

9.7.3.4	Measurement capability	378

9.7.3.5	CLI-RSSI measurement period	378

9.7.4	Scheduling availability of UE during CLI measurements	378

9.7.4.1	Scheduling availability of UE performing measurement on FR1	378

9.7.4.2	Scheduling availability of UE performing measurement on FR2	378

9.8	L1-SINR measurements for Reporting	379

9.8.1	Introduction	379

9.8.2	Requirements applicability	379

9.8.3	Measurement Reporting Requirements	380

9.8.3.1	Periodic Reporting	380

9.8.3.2	Semi-Persistent Reporting	380

9.8.3.3	Aperiodic Reporting	381

9.8.4	L1-SINR measurement requirements	381

9.8.4.1	L1-SINR reporting with CSI-RS based CMR and no dedicated IMR configured	381

9.8.4.3	L1-SINR reporting with CSI-RS based CMR and dedicated IMR configured	384

9.8.5	Measurement restriction for L1-SINR measurement	386

9.8.5.1	Measurement restriction if SSB configured for L1-SINR Measurement	386

9.8.5.2	Measurement restriction if CSI-RS configured for L1-SINR measurement	387

9.8.5.3	Measurement restriction if CSI-IM configured for L1-SINR measurement	387

9.8.6	Scheduling availability of UE during L1-SINR measurement	388

9.8.6.1	Scheduling availability of UE performing L1-SINR measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	388

9.8.6.2	Scheduling availability of UE performing L1-SINR measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	388

9.8.6.4	Scheduling availability of UE performing L1-SINR measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA	389

9.9	 NR measurements for positioning	389

9.9.1	Introduction	389

9.9.2	RSTD measurements	390

9.9.2.1	Introduction	390

9.9.2.2	Requirements Applicability	390

9.9.2.3	Measurement Capability	390

9.9.2.4	Measurement Reporting Requirements	390

9.9.2.4.1	Void	390

9.9.2.4.2	Void	390

9.9.2.4.3	Void	390

9.9.2.5	Measurements Period Requirements	390

9.9.2.6	Void	392

9.9.3	PRS-RSRP measurements	392

9.9.3.1	Introduction	392

9.9.3.2	Requirements applicability	392

9.9.3.3	Measurement Capability	393

9.9.3.4	Measurement Reporting Requirements	393

9.9.3.5	Measurement Period Requirements	393

9.9.4	UE Rx-Tx time difference measurements	395

9.9.4.1 Introduction	395

9.9.4.2 Requirements Applicability	395

9.9.4.3 Measurement Capability	395

9.9.4.4 Measurement Reporting Requirements	395

9.9.4.5	Measurement Period Requirements	395

9.9.5	NR E-CID measurements	398

9.9.5.1	Introduction	398

9.9.5.2	Measurement Requirements	398

9.9.5.2.1	Intra-frequency Measurement Requirements	398

9.9.5.2.2	Inter-frequency Measurement Requirements	398

9.9.5.2.3	Measurement Reporting Delay	399

9.10	CSI-RS based L3 measurements	399

9.10.1	Introduction	399

9.10.2	CSI-RS based intra-frequency measurements	399

9.10.2.1	Introduction	399

9.10.2.2	Requirements applicability	400

9.10.2.3	Number of cells and number of CSI-RS	401

9.10.2.3.1	Requirements for FR1	401

9.10.2.3.2	Requirements for FR2	401

9.10.2.4	Measurement Reporting Requirements	401

9.10.2.4.1	Periodic Reporting	402

9.10.2.4.2	Event-triggered Periodic Reporting	402

9.10.2.4.3	Event Triggered Reporting	402

9.10.2.5	Intra-frequency measurements without measurement gaps	402

9.10.2.6	Scheduling availability of UE during CSI-RS based intra-frequency measurements	403

9.10.2.6.1	Scheduling availability of UE performing CSI-RS based measurements in TDD bands	403

9.10.2.6.2	Scheduling availability of UE performing CSI-RS based measurements in FR2	404

9.10.3	CSI-RS based Inter-frequency measurements	404

9.10.3.1	Introduction	404

9.10.3.2	Requirements applicability	404

9.10.3.3	Number of cells and number of CSI-RS resources	405

9.10.3.3.1	Requirements for FR1	405

9.10.3.3.2	Requirements for FR2	405

9.10.3.4	Measurements reporting requirements	405

9.10.3.4.1	Periodic Reporting	405

9.10.3.4.2	Event-triggered Periodic Reporting	405

9.10.3.4.3	Event-triggered Reporting	406

9.10.3.5	Inter frequency measurements with measurement gaps	406

9.11	NR measurements with autonomous gaps	407

9.11.1	Introduction	407

9.11.2	CGI identification of an NR cell with autonomous gaps	407

9.11.3	CGI reporting delay	408

10	Measurement Performance requirements	408

10.1	NR measurements	408

10.1.1	Introduction	408

10.1.2	Intra-frequency RSRP accuracy requirements for FR1	409

10.1.2.1	Intra-frequency SS-RSRP accuracy requirements	409

10.1.2.1.1	Absolute SS-RSRP Accuracy	409

10.1.2.1.2	Relative SS-RSRP Accuracy	410

10.1.2.2	Void	411

10.1.2.3	Intra-frequency CSI-RSRP accuracy requirements	411

10.1.2.3.1	Absolute CSI-RSRP Accuracy	411

10.1.2.3.2	Relative CSI-RSRP Accuracy	412

10.1.2B	Intra-frequency RSRP accuracy requirements for FR1 for CA/DC Idle Mode Measurements	413

10.1.2B.1	Intra-frequency SS-RSRP accuracy requirements	413

10.1.2B.1.1	Absolute SS-RSRP Accuracy	413

10.1.3	Intra-frequency RSRP accuracy requirements for FR2	414

10.1.3.1	Intra-frequency SS-RSRP accuracy requirements	414

10.1.3.1.1	Absolute SS-RSRP Accuracy	414

10.1.3.1.2	Relative SS-RSRP Accuracy	415

10.1.3.2	Void	416

10.1.3.3	Intra-frequency CSI-RSRP accuracy requirements	416

10.1.3.3.1	Absolute CSI-RSRP Accuracy	416

10.1.3.3.2	Relative CSI-RSRP Accuracy	416

10.1.3B	Intra-frequency RSRP accuracy requirements for FR2 for CA/DC Idle Mode Measurements	417

10.1.3B.1	Intra-frequency SS-RSRP accuracy requirements	417

10.1.3B.1.1	Absolute SS-RSRP Accuracy	418

10.1.4	Inter-frequency RSRP accuracy requirements for FR1	418

10.1.4.1	Inter-frequency SS-RSRP accuracy requirements	418

10.1.4.1.1	Absolute Accuracy of SS-RSRP in FR1	418

10.1.4.1.2	Relative Accuracy of SS-RSRP in FR1	419

10.1.4.2	Void	420

10.1.4.3	Inter-frequency CSI-RSRP accuracy requirements	420

10.1.4.3.1	Absolute Accuracy of CSI-RSRP in FR1	420

10.1.4.3.2	Relative Accuracy of CS-RSRP in FR1	421

10.1.4B	Inter-frequency RSRP accuracy requirements for FR1 for CA/DC Idle Mode Measurements	422

10.1.4B.1	Inter-frequency SS-RSRP accuracy requirements	422

10.1.4B.1.1	Absolute Accuracy of SS-RSRP in FR1	422

10.1.5	Inter-frequency RSRP accuracy requirements for FR2	423

10.1.5.1	Inter-frequency SS-RSRP accuracy requirements	423

10.1.5.1.1	Absolute SS-RSRP Accuracy	423

10.1.5.1.2	Relative SS-RSRP Accuracy	424

10.1.5.2	Void	425

10.1.5.3	Inter-frequency CSI-RSRP accuracy requirements	425

10.1.5.3.1	Absolute CSI-RSRP Accuracy	425

10.1.5.3.2	Relative CSI-RSRP Accuracy	425

10.1.5B	Inter-frequency RSRP accuracy requirements for FR2 for CA/DC Idle Mode Measurements	426

10.1.6	RSRP Measurement Report Mapping	427

10.1.7	Intra-frequency RSRQ accuracy requirements for FR1	429

10.1.7.1	Intra-frequency SS-RSRQ accuracy requirements in FR1	429

10.1.7.1.1	Absolute SS-RSRQ Accuracy in FR1	429

10.1.7.2	Intra-frequency CSI-RSRQ accuracy requirements	430

10.1.7.2.1	Absolute CSI-RSRQ Accuracy	430

10.1.7B	Intra-frequency RSRQ accuracy requirements for FR1 for CA/DC Idle Mode Measurements	431

10.1.7B.1	Intra-frequency SS-RSRQ accuracy requirements in FR1	431

10.1.7B.1.1	Absolute SS-RSRQ Accuracy in FR1	431

10.1.8	Intra-frequency RSRQ accuracy requirements for FR2	432

10.1.8.1	Intra-frequency SS-RSRQ accuracy requirements in FR2	432

10.1.8.1.1	Absolute SS-RSRQ Accuracy in FR2	432

10.1.8.2	Intra-frequency CSI-RSRQ accuracy requirements	433

10.1.8.2.1	Absolute CSI-RSRQ Accuracy	433

10.1.8B	Intra-frequency RSRQ accuracy requirements for FR2 for CA/DC Idle Mode Measurements	434

10.1.8B.1	Intra-frequency SS-RSRQ accuracy requirements in FR2	434

10.1.8B.1.1	Absolute SS-RSRQ Accuracy in FR2	434

10.1.9	Inter-frequency RSRQ accuracy requirements for FR1	435

10.1.9.1	Inter-frequency SS-RSRQ accuracy requirements in FR1	435

10.1.9.1.1	Absolute Accuracy of SS-RSRQ in FR1	435

10.1.9.1.2	Relative Accuracy of SS-RSRQ in FR1	436

10.1.9.2	Inter-frequency CSI-RSRQ accuracy requirements	437

10.1.9.2.1	Absolute CSI-RSRQ Accuracy	437

10.1.9.2.2	Relative CSI-RSRQ Accuracy	438

10.1.9B	Inter-frequency RSRQ accuracy requirements for FR1 for CA/DC Idle Mode Measurements	439

10.1.9B.1	Inter-frequency SS-RSRQ accuracy requirements in FR1	439

10.1.9B.1.1	Absolute Accuracy of SS-RSRQ in FR1	439

10.1.10	Inter-frequency RSRQ accuracy requirements for FR2	440

10.1.10.2	Inter-frequency CSI-RSRQ accuracy requirements	442

10.1.10.2.1	Absolute CSI-RSRQ Accuracy	442

10.1.10.2.2	Relative CSI-RSRQ Accuracy	442

10.1.10B	Inter-frequency RSRQ accuracy requirements for FR2 for CA/DC Idle Mode Measurements	443

10.1.10B.1	Inter-frequency SS-RSRQ accuracy requirements in FR2	443

10.1.10B.1.1	Absolute Accuracy of SS-RSRQ in FR2	443

10.1.11	RSRQ report mapping	444

10.1.12	Intra-frequency SINR accuracy requirements for FR1	445

10.1.12.2	Intra-frequency CSI-SINR accuracy requirements in FR1	445

10.1.12.2.1	Absolute CSI-SINR Accuracy in FR1	445

10.1.13	Intra-frequency SINR accuracy requirements for FR2	446

10.1.13.2	Intra-frequency CSI-SINR accuracy requirements in FR2	447

10.1.13.2.1	Absolute CSI-SINR Accuracy in FR2	447

10.1.14	Inter-frequency SINR accuracy requirements for FR1	448

10.1.14.2	Inter-frequency CSI-SINR accuracy requirements in FR1	450

10.1.14.2.1	Aboslute Accuracy of CSI-SINR in FR1	450

10.1.15	Inter-frequency SINR accuracy requirements for FR2	452

10.1.15.2	Inter-frequency CSI-SINR accuracy requirements in FR2	454

10.1.15.2.1	Aboslute Accuracy of CSI-SINR in FR2	454

10.1.15.2.2	Relative Accuracy of CSI-SINR in FR2	454

10.1.16	SINR report mapping	455

10.1.17	Power Headroom	456

10.1.18	PCMAX,c,f	457

10.1.19	L1-RSRP accuracy requirements for FR1	457

10.1.20	L1-RSRP accuracy requirements for FR2	461

10.1.21	SFTD accuracy requirements	464

10.1.22	CLI measurement accuracy requirements	468

10.1.24.3.1	Absolute PRS-RSRP Measurement Report Mapping	472

10.1.24.3.2	Differential Report Mapping for PRS-RSRP Measurement	472

10.1.23	RSTD Measurements	474

10.1.23.1	Introduction	474

10.1.23.2	Measurement Accuracy Requirements	475

10.1.23.3	Report mapping	481

10.1.23.3.1	 Absolute DL RSTD Measurement Reporting	481

10.1.23.3.2	 Differential Reporting for DL RSTD Measurement	483

10.1.23.3.3	Additional Path Report Mapping for DL RSTD	485

10.1.24	PRS-RSRP Measurements	487

10.1.24.1	Introduction	487

10.1.24.2	Measurement Accuracy Requirements	487

10.1.24.2.1 Absolute PRS RSRP accuracy	487

10.1.24.3	Report mapping	491

10.1.24.3.1	Absolute PRS-RSRP Measurement Report Mapping	491

10.1.24.3.2	Differential Report Mapping for PRS-RSRP Measurement	492

10.1.25	UE Rx-Tx Time Difference Measurements	494

10.1.25.1	Introduction	494

10.1.25.2	Measurement Accuracy Requirements	495

10.1.25.3	Report mapping	501

10.1.25.3.1	 Absolute UE Rx-Tx Measurement Report Mapping	501

10.1.25.3.2	 Differential UE Rx-Tx Measurement Report Mapping	503

10.1.25.3.3	 Additional Path Report Mapping for UE Rx-Tx Time Difference	504

10.1.26	FR2 P-MPR report	506

10.1.26.1	Report mapping	506

10.1.27	L1-SINR accuracy requirements for FR1	506

10.1.27.1	L1-SINR accuracy requirements with CSI-RS based CMR and no dedicated IMR configured	506

10.1.27.1.1	Absolute Accuracy	506

10.1.27.1.2	Relative Accuracy	507

10.1.27.2	L1-SINR accuracy requirements with SSB based CMR and dedicated IMR configured	508

10.1.27.2.1	Absolute Accuracy	508

10.1.27.2.2	Relative Accuracy	509

10.1.27.3	L1-SINR accuracy requirements with CSI-RS based CMR and dedicated IMR configured	511

10.1.27.3.1	Absolute Accuracy	511

10.1.27.3.2	Relative Accuracy	513

10.1.28	L1-SINR accuracy requirements for FR2	514

10.1.28.1	L1-SINR accuracy requirements with CSI-RS based CMR and no dedicated IMR configured	514

10.1.28.1.1	Absolute Accuracy	514

10.1.28.1.2	Relative Accuracy	515

10.1.28.2	L1-SINR accuracy requirements with SSB based CMR and dedicated IMR configured	516

10.1.28.2.1	Absolute Accuracy	516

10.1.28.2.2	Relative Accuracy	517

10.1.28.3	L1-SINR accuracy requirements with CSI-RS based CMR and dedicated IMR configured	518

10.1.28.3.1	Absolute Accuracy	518

10.1.28.3.2	Relative Accuracy	519

10.1.29	Intra-frequency RSRQ accuracy requirements under CCA	521

10.1.29.1	Intra-frequency SS-RSRQ accuracy requirements in FR1	521

10.1.29.1.1	Absolute SS-RSRQ Accuracy	521

10.1.30	Inter-frequency RSRQ accuracy requirements under CCA	522

10.1.30.1	Inter-frequency SS-RSRQ accuracy requirements in FR1	522

10.1.30.1.1	Aboslute Accuracy of SS-RSRQ	522

10.1.30.1.2	Relative Accuracy of SS-RSRQ	522

10.1.31	Intra-frequency SINR accuracy requirements under CCA	523

10.1.32	Inter-frequency SINR accuracy requirements under CCA	524

10.1.33	L1-RSRP accuracy requirements under CCA	525

10.1.34	RSSI measurements under CCA	526

10.1.34.1	Intra-frequency absolute RSSI measurement accuracy requirements in FR1	526

10.1.34.2	Inter-frequency absolute RSSI measurement accuracy requirements in FR1	527

10.1.34.3	RSSI measurement report mapping	527

10.1.35	Channel occupancy measurements under CCA	527

10.1.35.1	Intra-frequency channel occupancy measurement accuracy requirements in FR1	527

10.1.35.2	Inter-frequency channel occupancy measurement accuracy requirements in FR1	528

10.1.36	Intra-frequency RSRP accuracy requirements under CCA	528

10.1.36.1	Intra-frequency SS-RSRP accuracy requirements in FR1	528

10.1.36.1.1	Absolute SS-RSRP Accuracy	528

10.1.36.1.2	Relative SS-RSRP Accuracy	529

10.1.37	Inter-frequency RSRP accuracy requirements under CCA	529

10.1.37.1	Inter-frequency SS-RSRP accuracy requirements in FR1	529

10.1.37.1.1	Absolute Accuracy of SS-RSRP	529

10.1.37.1.2	Relative Accuracy of SS-RSRP	530

10.2	E-UTRAN measurements	530

10.2.1	Introduction	530

10.2.2	E-UTRAN RSRP measurements	531

10.2.3	E-UTRAN RSRQ measurements	531

10.2.4	E-UTRAN RSTD measurements	531

10.2.5	E-UTRAN RS-SINR measurements	532

10.2.6	E-UTRAN RSRP measurements for CA/DC Idle Mode Measurements	532

10.2.7	E-UTRAN RSRQ measurements for CA/DC Idle Mode Measurements	532

10.3	UTRAN FDD Measurements	532

10.3.1	UTRAN FDD CPICH RSCP	533

10.3.2	UTRAN FDD CPICH Ec/No	533

10.4	V2X measurements	534

10.4.1	Introduction	534

10.4.2	Intra-frequency PSBCH-RSRP accuracy requirements for FR1	534

10.4.2.1	PSBCH-RSRP Absolute Accuracy	534

10.4.2.2	PSBCH-RSRP Relative Accuracy	534

10.4.3	Intra-Frequency SL-RSSI Measurement Accuracy Requirements for FR1	535

10.4.3.1	Absolute SL-RSSI Accuracy	535

10.4.4	Intra-Frequency L1 SL-RSRP Measurement Accuracy Requirements for FR1	536

10.4.4.1	Absolute L1 SL-RSRP Accuracy	536

11	Void	537

12	V2X Requirements	537

12.1	Introduction	537

12.2	UE Transmit Timing	537

12.2.1	Introduction	537

12.2.2	GNSS as synchronization reference source	537

12.2.3	NR Cell as synchronization reference source	538

12.2.4	E-URTAN Cell as synchronization reference source	538

12.2.5	SyncRef UE as synchronization reference source	538

12.3	Initiation/Cease of SLSS Transmissions	539

12.3.1	Introduction	539

12.3.1.1	Initiation/Cease of SLSS transmissions with NR cell as synchronization reference source	539

12.3.1.2	Initiation/Cease of SLSS transmissions with EUTRAN cell as synchronization reference source	540

12.3.1.3	Initiation/Cease of SLSS transmissions with GNSS as synchronization reference source	541

12.3.1.4	Initiation/Cease of SLSS transmissions with SyncRef UE as synchronization reference source	541

12.4	Selection / Reselection of V2X Synchronization Reference Source	541

12.5	L1 SL-RSRP measurements	542

12.5.1	Introduction	542

12.5.2	SL-RSRP measurements	542

12.6	Congestion Control measurements	543

12.7	Interruption	543

12.7.1	Interruptions to WAN due to V2X Sidelink Communication	543

12.7.2	V2X Sidelink Communication Dropping due to synchronization source change	543

12.7.3	Interruptions to WAN due to switching between E-UTRA V2X Sidelink and NR V2X Sidelink	545

12.8	Reliability of GNSS signal	545

12.9	Scheduling availability	546

12.9.1	Scheduling availability of UE switching between E-UTRA sidelink and NR sidelink	546

13	Measurement Performance Requirements for NR gNB	546

13.1	UL-RTOA	546

13.1.1	Report mapping	546

13.2	gNB Rx-Tx time difference	548

13.2.1	Report mapping	548

13.2.2	Measurement Accuracy Requirements	550

13.2.2.1	Introduction	550

13.2.2.2	Requirements	551

13.3	UL SRS RSRP measurement	552

13.3.1	Report mapping	552

13.3.2	Measurement accuracy requirements	552

13.3.2.1	Introduction	552

13.3.2.2	Requirements	553

13.4	AoA/ZoA	554

13.4.1	Report mapping	554

Annex A	(normative): Test Cases	555

A.1	Purpose of annex	555

A.2	Requirement classification for statistical testing	555

A.2.1	Types of requirements in TS 38.133	555

A.2.1.1	Time and delay requirements on UE higher layer actions	555

A.2.1.2	Measurements of power levels, relative powers and time	555

A.2.1.3	Implementation requirements	556

A.2.1.4	Physical layer timing requirements	556

A.2.1.5	Requirements under CCA	556

A.3	RRM test configurations	557

A.3.1	Reference measurement channels	557

A.3.1.1	PDSCH	557

A.3.1.1.1	FDD	557

A.3.1.1.2	TDD	558

A.3.1A	Reference measurement channels under CCA	561

A.3.1A.1	PDSCH	561

A.3.1A.1.1	TDD	561

A.3.1A.2	CORESET for RMSI scheduling	562

A.3.1A.2.1	TDD	562

A.3.1A.3	CORESET for RMC scheduling	563

A.3.1A.3.1	TDD	563

A.3.1A.4	TDD UL/DL configuration	564

A.3.1A.5	RMC burst transmission model	564

A.3.1.2	CORESET for RMSI scheduling	565

A.3.1.2.1	FDD	565

A.3.1.2.2	TDD	566

A.3.1.3	CORESET for RMC scheduling	569

A.3.1.3.1	FDD	569

A.3.1.3.2	TDD	570

A.3.1.4	TDD UL/DL configuration	573

A.3.2	OFDMA channel noise generator (OCNG)	574

A.3.2.1	Generic OFDMA Channel Noise Generator (OCNG)	574

A.3.2.1.1	OCNG pattern 1: Generic OCNG pattern for all unused REs	574

A.3.2.1.2	OCNG pattern 2: Generic OCNG pattern for all unused REs for 2AoA setup	575

A.3.2.1.3	OCNG pattern 3: Generic OCNG pattern for unused REs in the same bandwidth as CORESET	575

A.3.2.1.4	OCNG pattern 4: Generic OCNG pattern for all unused REs outside SSB slot(s)	576

A.3.2.2	Void	577

A.3.3	Reference DRX configurations	577

A.3.3.1	DRX Configuration 1: DRX cycle = 40 ms and TAT = 500 ms	577

A.3.3.2	DRX Configuration 2: DRX cycle = 640 ms and TAT = 500 ms	577

A.3.3.3	DRX Configuration 3: DRX cycle = 40 ms and TAT = Infinity	577

A.3.3.4	DRX Configuration 4: DRX cycle = 160 ms and TAT = Infinity	578

A.3.3.5	DRX Configuration 5: DRX cycle = 320 ms and TAT = Infinity	578

A.3.3.6	DRX Configuration 6: DRX cycle = 320 ms and TAT = 500 ms	578

A.3.3.7	DRX Configuration 7: DRX cycle = 640 ms and TAT = Infinity	579

A.3.3.8	DRX Configuration 8: DRX cycle = 320 ms and TAT = Infinity	579

A.3.3.9	DRX Configuration 9: DRX cycle = 40 ms and TAT = 500 ms	579

A.3.3.10	DRX Configuration 10: DRX cycle = 640 ms and TAT = 500 ms	580

A.3.3.11	DRX Configuration 11: DRX cycle = 20 ms and TAT = Infinity	580

A.3.3.12	DRX Configuration 12: DRX cycle = 640 ms and TAT = Infinity	580

A.3.4	Test Cases with Different Channel Bandwidths	580

A.3.4.1	Test Cases with Different E-UTRA Channel Bandwidths	580

A.3.4.1.1	Introduction	580

A.3.4.1.2	Principle of testing	581

A.3.5	Test Cases for Synchronous and Asynchronous DC Operations	581

A.3.5.1	EN-DC Test Cases for Synchronous and Asynchronous EN-DC Operations	581

A.3.5.1.1	Introduction	581

A.3.5.1.2	Principle of Testing	581

A.3.6	Antenna configurations	581

A.3.6.1	Antenna configurations for FR1	581

A.3.6.1.1	Antenna connection for 4 Rx capable UEs	581

A.3.6.1.1.1	Introduction	581

A.3.6.1.1.2	Principle of testing	581

A.3.6.2	Antenna configurations for FR2	584

A.3.6A	Antenna configurations with unlicensed bands	584

A.3.6A.1	Antenna configurations for FR1	584

A.3.6A.1.1	Antenna connection for 4 Rx capable UEs	584

A.3.6A.1.1.1	Introduction	584

A.3.6A.1.1.2	Principle of testing	584

A.3.7	EN-DC test setup	586

A.3.7.1	Introduction	586

A.3.7.2	E-UTRAN Serving Cell Parameters	586

A.3.7.2.1	E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR1	586

A.3.7.2.2	E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR2	587

A.3.7A	NR FR1-FR2 test setup	588

A.3.7B	EN-DC test setup with unlicensed bands	589

A.3.7B.1	Introduction	589

A.3.7B.2	E-UTRAN Serving Cell Parameters	589

A.3.7B.2.1	E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) under CCA in FR1	589

A.3.7C	LTE-FR1/FR2 test setup	590

A.3.7D	NE-DC test setup	590

A.3.7D.1	Introduction	590

A.3.7D.2	E-UTRAN Serving Cell Parameters	590

A.3.7D.2.1	E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR1	590

A.3.7D.2.2	E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR2	590

A.3.8	PRACH configurations	590

A.3.8.1	Introduction	590

A.3.8.2	PRACH configurations in FR1	591

A.3.8.2.1	FR1 PRACH configuration 1	591

A.3.8.2.2	FR1 PRACH configuration 2	591

A.3.8.2.3	FR1 PRACH configuration 3	592

A.3.8.2.4	FR1 PRACH configuration 4	593

A.3.8.3	PRACH configurations in FR2	594

A.3.8.3.1	FR2 PRACH configuration 1	594

A.3.8.3.2	FR2 PRACH configuration 2	595

A.3.8.3.3	FR2 PRACH configuration 3	596

A.3.8.3.4	FR2 PRACH configuration 4	597

A.3.8A	PRACH configurations under CCA	598

A.3.8A.1	Introduction	598

A.3.8A.2	PRACH configurations in FR1	598

A.3.8A.2.1	FR1 PRACH configuration 1 under CCA	598

A.3.8A.2.2	FR1 PRACH configuration 2 under CCA	599

A.3.9	BWP configurations	600

A.3.9.1	Introduction	600

A.3.9.2	Downlink BWP configurations	601

A.3.9.2.1	Initial BWP	601

A.3.9.2.2	Dedicated BWP	601

A.3.9.3	Uplink BWP configurations	602

A.3.9.3.1	Initial BWP	602

A.3.9.3.2	Dedicated BWP	602

A.3.10	SSB Configurations	603

A.3.10.1	SSB Configurations for FR1	603

A.3.10.1.1	SSB pattern 1 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz	603

A.3.10.1.5	SSB pattern 5 in FR1: SSB allocation for SSB SCS=15 kHz starting from odd SFN in 10 MHz	605

A.3.10A	SSB Configurations under CCA	610

A.3.10A.1	SSB Configurations under CCA for FR1	610

A.3.10A.1.1	SSB pattern 1 under CCA for semi-static channel access: SSB allocation for SSB SCS=30kHz in 40MHz	610

A.3.10A.1.2	SSB pattern 2 under CCA for dynamic channel access: SSB allocation for SSB SCS=30kHz in 40MHz	610

A.3.10A.1.3	SSB pattern 3 under CCA for semi-static channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz	611

A.3.10A.1.4	SSB pattern 4 under CCA for dynamic channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz	611

A.3.11	SMTC Configurations	612

A.3.11.1	SMTC pattern 1: SMTC period = 20 ms with SMTC duration = 1 ms	612

A.3.11.2	SMTC pattern 2: SMTC period = 20 ms with SMTC duration = 5 ms	612

A.3.11.3	SMTC pattern 3: SMTC period = 160 ms with SMTC duration = 1 ms	612

A.3.11.4	SMTC pattern 4: SMTC period = 20 ms with SMTC duration = 1 ms	612

A.3.11.5	SMTC pattern 5: SMTC period = 20 ms with SMTC duration = 5 ms	613

A.3.11.6	SMTC pattern 6: SMTC period = 20 ms with SMTC duration = 5 ms	613

A.3.11.7	Void	613

A.3.11.8	Void	613

A.3.11.9	SMTC pattern 9: SMTC period = 20 ms with SMTC duration = 1 ms	613

A.3.12	Test Cases with Different CC Configurations	613

A.3.12.1 EN-DC Test Cases with Different EN-DC Configurations	613

A.3.12.1.1	Introduction	613

A.3.12.1.2	Principle of testing	613

A.3.12.2	Carrier Aggregation Test Cases with Different CA Configurations	614

A.3.12.2.1	Introduction	614

A.3.12.2.2	Principle of testing	614

A.3.13	Test Cases in SA and EN-DC Operations	614

A.3.13.1	Introduction	614

A.3.13.2	Principle of Testing	614

A.3.13A Test Cases involving E-UTRA/FR1 and FR2 carriers	614

A.3.13A.1	Introduction	614

A.3.13A.2	Principle of Testing in EN-DC	615

A.3.13A.3	Principle of Testing in SA	615

A.3.13B	Test Cases for EN-DC and NE-DC Operations	616

A.3.13B.1	Active BWP switch Test Cases for EN-DC and NE-DC Operations	616

A.3.13B.1.1	Introduction	616

A.3.13B.1.2	Principle of Testing	617

A.3.13B.2	SFTD accuracy Test Cases for EN-DC and NE-DC Operations	617

A.3.13B.2.1	Introduction	617

A.3.13B.2.2	Principle of Testing	617

A.3.14	CSI-RS configurations	617

A.3.14.1	FDD	617

A.3.14.2	TDD	619

A.3.15	Angle of Arrival (AoA) for FR2 RRM test cases	624

A.3.15.1	Setup 1: Single AoA in Rx beam peak direction	624

A.3.15.2	Setup 2: Single AoA in non Rx beam peak direction	624

A.3.15.2.1	Setup 2a: Single AoA in non Rx beam peak direction without change in direction	624

A.3.15.2.2	Setup 2b: Single AoA in non Rx beam peak direction with change in direction	625

A.3.15.3	Setup 3: 2 AoAs	625

A.3.15.4	Setup 4: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak	625

A.3.15.4.1	Setup 4a: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak without change in direction	625

A.3.15.4.2	Setup 4b: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak with change in direction	625

A.3.16	TCI State Configuration	626

A.3.16.1	Introduction	626

A.3.16.2	TCI states	626

A.3.17	Configurations of CSI-RS for tracking	626

A.3.17.1	Configuration of CSI-RS for tracking for FR1	626

A.3.17.1.1	FDD	626

A.3.17.1.2	TDD	627

A.3.17.2	Configuration of CSI-RS for tracking for FR2	628

A.3.17.2.1	TDD	628

A.3.18	Additional definitions related to OTA testing for FR2 RRM test cases	629

A.3.18.1	Introduction	629

A.3.18.2	PRACH Power Measurement	629

A.3.19	Test applicability for DAPS handover	629

A.3.19.1	Introduction	629

A.3.19.2	Principle of testing	629

A.3.20	MsgA configurations	630

A.3.20.1	Introduction	630

A.3.20.2	MsgA configurations in FR1	630

A.3.20.2.1	FR1 MsgA configuration 1	630

A.3.20.2.2	FR1 MsgA configuration 2	631

A.3.20.3	MsgA configurations in FR2	633

A.3.20.3.1	FR2 MsgA configuration 1	633

A.3.20.3.2	FR2 MsgA configuration 2	634

A.3.20A	MsgA configurations under CCA	636

A.3.20A.1	Introduction	636

A.3.20A.2	MsgA configurations in FR1	636

A.3.20A.2.1	FR1 MsgA configuration 1 under CCA	636

A.3.20A.2.2	FR1 MsgA configuration 2 under CCA	637

A.3.21	V2X sidelink communication	640

A.3.21.1	Introduction	640

A.3.21.2	Reference resource pool configurations for V2X Sidelink Communication	640

A.3.21.3	Reference measurement channels for V2X Sidelink Communication	644

A.3.22	CSI-IM configurations	644

A.3.22.1	FDD	644

A.3.22.2	TDD	645

A.3.23	Spatial Relation Configuration	647

A.3.23.1	Introduction	647

A.3.23.2	Spatial Relation	647

A.3.24	SRS configuration	648

A.3.25	Channel bandwidth (CBW) configurations	650

A.3.25.1	DL UE specific CBW	651

A.3.26	CCA model	651

A.3.26.1	Introduction	651

A.3.26.2	CCA model for operation on a carrier frequency with CCA in FR1	651

A.3.26.2.1	DL CCA model	651

A.3.26.2.2	UL CCA model	653

A.3.27	Test Cases with at Least One Cell on a Carrier Frequency with CCA	653

A.3.27.1	Introduction	654

A.3.27.2	 NR Standalone Tests with NR SCell under CCA and All Other NR Cells in FR1	654

A.3.27.3	EN-DC Tests with NR PSCell under CCA and Other NR Cells in FR1	654

A.3.27.4	NR Standalone Tests with NR PCell under CCA and Other NR Cells in FR1	654

A.3.27.5	E-UTRA Standalone Tests with at Least One NR Cell under CCA	654

A.3.28	Discovery Burst Transmission Window configuration under CCA	654

A.3.28.1	DBT Window pattern 1: DBT Window period = 20 ms with DBT Window duration = 1 ms	654

A.3.29	Testing principles for UE capable of only NR bands with shared spectrum access	654

A.3.29.1	Introduction	654

A.3.29.2	Principle of testing for UE capable of EN-DC with only NR bands with shared spectrum access	655

A.3.29.3	Principle of testing for UE capable of SA operation with only NR bands with shared spectrum access	655

A.3.30	CSI-RS configurations for RRM	656

A.3.30.1	FDD	656

A.3.30.2	TDD	657

A.3.31	PRS Configurations	659

A.3.31.1.	PRS Configurations for FR1	659

A.3.31.1.1.	PRS pattern 1 in FR1: SCS=15 KHz	659

A.3.31.1.2.	PRS pattern 2 in FR1: SCS=30 KHz	660

A.3.31.2.	PRS Configurations for FR2	660

A.3.31.2.1.	PRS pattern 1 in FR2: SCS=120 KHz	660

A.4	EN-DC tests with all NR cells in FR1	661

A.4.1	Void	661

A.4.2	Void	661

A.4.3	RRC\_CONNECTED state mobility	661

A.4.3.1	Void	661

A.4.3.2	RRC Connection Mobility Control	661

A.4.3.2.1	Void	661

A.4.3.2.2	Random Access	661

A.4.3.2.2.1	4-step RA type contention based random access test in FR1 for PSCell in EN-DC	661

A.4.3.2.2.2	4-step RA type non-contention based random access test in FR1 for PSCell in EN-DC	665

A.4.3.2.2.3	2-step RA type contention based random access test in FR1 for PSCell in EN-DC	669

A.4.3.2.2.4	2-step RA type non-contention based random access test in FR1 for PSCell in EN-DC	673

A.4.3.2.3	Void	677

A.4.4	Timing	677

A.4.4.1	UE transmit timing	677

A.4.4.1.1	NR UE Transmit Timing Test for FR1	677

A.4.4.1.1.1	Test Purpose and environment	677

A.4.4.1.1.2	Test requirements	681

A.4.4.2	UE timer accuracy	681

A.4.4.3	Timing advance	681

A.4.4.3.1	EN-DC FR1 timing advance adjustment accuracy	681

A.4.4.3.1.1	Test Purpose and Environment	681

A.4.4.3.1.2	Test Parameters	682

A.4.4.3.1.3	Test Requirements	685

A.4.5	Signaling characteristics	685

A.4.5.1	Radio link Monitoring	685

A.4.5.1.1	Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in non-DRX mode	686

A.4.5.1.1.1	Test Purpose and Environment	686

A.4.5.1.1.2	Test Requirements	690

A.4.5.1.2	Radio Link Monitoring In-sync Test for FR1 PSCell configured with SSB-based RLM RS in non-DRX mode	690

A.4.5.1.2.1	Test Purpose and Environment	690

A.4.5.1.2.2	Test Requirements	696

A.4.5.1.3	Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in DRX mode	696

A.4.5.1.3.1	Test Purpose and Environment	696

A.4.5.1.3.2	Test Requirements	702

A.4.5.1.4	Radio Link Monitoring In-sync Test for FR1 PSCell configured with SSB-based RLM RS in DRX mode	702

A.4.5.1.4.1	Test Purpose and Environment	702

A.4.5.1.4.2	Test Requirements	708

A.4.5.1.5	EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode	708

A.4.5.1.5.1	Test Purpose and Environment	708

A.4.5.1.5.2	Test Requirements	714

A.4.5.1.6	EN-DC Radio Link Monitoring In-sync Test for FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode	714

A.4.5.1.6.1	Test Purpose and Environment	714

A.4.5.1.6.2	Test Requirements	720

A.4.5.1.7	EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with CSI-RS-based RLM in DRX mode	720

A.4.5.1.7.1	Test Purpose and Environment	720

A.4.5.1.7.2	Test Requirements	725

A.4.5.1.8	EN-DC Radio Link Monitoring In-sync Test for FR1 PSCell configured with CSI-RS-based RLM in DRX mode	726

A.4.5.1.8.1	Test Purpose and Environment	726

A.4.5.1.8.2	Test Requirements	731

A.4.5.2	Interruption	731

A.4.5.2.1	E-UTRAN – NR FR1 interruptions at transitions between active and non-active during DRX in synchronous EN-DC	731

A.4.5.2.1.1	Test Purpose and Environment	731

A.4.5.2.1.2	Test Requirements	735

A.4.5.2.2	E-UTRAN – NR FR1 interruptions at transitions between active and non-active during DRX in asynchronous EN-DC	735

A.4.5.2.2.1	Test Purpose and Environment	735

A.4.5.2.2.2	Test Requirements	739

A.4.5.2.3	E-UTRAN – NR FR1 interruptions during measurements on deactivated NR SCC in synchronous EN-DC	739

A.4.5.2.3.1	Test Purpose and Environment	739

A.4.5.2.3.2	Test Requirements	744

A.4.5.2.4	E-UTRAN – NR FR1 interruptions during measurements on deactivated NR SCC in asynchronous EN-DC	745

A.4.5.2.4.1	Test Purpose and Environment	745

A.4.5.2.4.2	Test Requirements	749

A.4.5.2.5	E-UTRAN – NR FR1 interruptions during measurements on deactivated E-UTRAN SCC in synchronous EN-DC	750

A.4.5.2.5.1	Test Purpose and Environment	750

A.4.5.2.5.2	Test Requirements	754

A.4.5.2.6	E-UTRAN – NR FR1 interruptions during measurements on deactivated E-UTRAN SCC in asynchronous EN-DC	754

A.4.5.2.6.1	Test Purpose and Environment	754

A.4.5.2.6.2	Test Requirements	758

A.4.5.2.7	Void	758

A.4.5.2.8	E-UTRAN - NR FR1 interruptions at NR SRS carrier based switching in asynchronous EN-DC	758

A.4.5.2.8.1	Test Purpose and Environment	758

A.4.5.2.8.2	Test Requirements	761

A.4.5.2.9	E-UTRAN – NR interruptions at E-UTRA SRS carrier based switching	762

A.4.5.2.9.1	Test Purpose and Environment	762

A.4.5.2.9.2	Test Requirements	766

A.4.5.3	SCell Activation and Deactivation Delay	767

A.4.5.3.1	SCell Activation and deactivation of known SCell in FR1 for 160ms SCell measurement cycle	767

A.4.5.3.1.1	Test Purpose and Environment	767

A.4.5.3.1.2	Test Requirements	773

A.4.5.3.2	SCell Activation and deactivation of known SCell in FR1 for 640ms SCell measurement cycle	774

A.4.5.3.2.1	Test Purpose and Environment	774

A.4.5.3.2.2	Test Requirements	774

A.4.5.3.3	SCell Activation and deactivation of unknown SCell in FR1	774

A.4.5.3.3.1	Test Purpose and Environment	774

A.4.5.3.3.2	Test Requirements	775

A.4.5.3.4	SCell Activation and deactivation of multiple unknown SCells in FR1 with single activation/deactivation command	776

A.4.5.3.4.1	Test Purpose and Environment	776

A.4.5.3.4.2	Test Requirements	780

A.4.5.3.5	Direct SCell activation at SCell addition of known SCell in FR1	780

A.4.5.3.5.1	Test Purpose and Environment	780

A.4.5.3.5.2	Test Requirements	788

A.4.5.4	UE UL carrier RRC reconfiguration Delay	789

A.4.5.4.1	UE UL carrier RRC reconfiguration Delay	789

A.4.5.4.1.1	Test Purpose and Environment	789

A.4.5.4.1.2	Test Requirements	796

A.4.5.5	Beam Failure Detection and Link recovery procedures	796

A.4.5.5.1	EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in non-DRX mode	796

A.4.5.5.1.1	Test Purpose and Environment	796

A.4.5.5.1.2	Test Requirements	802

A.4.5.5.2	EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in DRX mode	803

A.4.5.5.2.1	Test Purpose and Environment	803

A.4.5.5.2.2	Test Requirements	808

A.4.5.5.3	EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with CSI-RS-based BFD and LR in non-DRX mode	809

A.4.5.5.3.1	Test Purpose and Environment	809

A.4.5.5.3.2	Test Requirements	814

A.4.5.5.4	EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with CSI-RS-based BFD and LR in DRX mode	815

A.4.5.5.4.1	Test Purpose and Environment	815

A.4.5.5.4.2	Test Requirements	820

A.4.5.5.5	EN-DC Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in non-DRX mode	821

A.4.5.5.5.1	Test Purpose and Environment	821

A.4.5.5.5.2	Test Requirements	826

A.4.5.5.6	EN-DC Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in DRX mode	827

A.4.5.5.6.1	Test Purpose and Environment	827

A.4.5.5.6.2	Test Requirements	833

A.4.5.6	Active BWP switch	834

A.4.5.6.1	DCI-based and Timer-based Active BWP Switch	834

A.4.5.6.1.1	E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC	834

A.4.5.6.1.2	E-UTRAN – NR PSCell FR1 DL active BWP switch with FR1 SCell in non-DRX in synchronous EN-DC	839

A.4.5.6.2	RRC-based Active BWP Switch	845

A.4.5.6.3	Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs	849

A.4.5.6.3.1	Simultaneous E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in EN-DC on multiple CCs	849

A.4.5.6.3.1.2	Test Requirements	855

A.4.5.6.4	SCell dormancy switch	855

A.4.5.6.4.1	E-UTRAN – NR FR1 PSCell SCell dormancy switch of single FR1 SCell outside active time	855

A.4.5.6.4.1.1	Test Purpose and Environment	855

A.4.5.6.4.1.2	Test Requirements	863

A.4.5.6.4.2	E-UTRAN – NR FR1 PSCell SCell dormancy switch of two FR1 SCells inside active time	863

A.4.5.6.4.2.1	Test Purpose and Environment	863

A.4.5.6.4.2.2	Test Requirements	875

A.4.5.6.5	Simultaneous RRC-based Active BWP Switch on multiple CCs	876

A.4.5.6.5.1	E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC on multiple CCs	876

A.4.5.7	PSCell addition and release delay	880

A.4.5.7.1	Addition and Release Delay of known NR PSCell	880

A.4.5.7.1.1	Test purpose and environment	880

A.4.5.7.1.2	Test Requirements	884

A.4.5.8	DL Interruptions at switching between two uplink carriers	885

A.4.5.8.1	Test Purpose and Environment	885

A.4.5.8.2	Test Requirements	888

A.4.5.9	UE specific CBW change	889

A.4.5.9.1	UE specific CBW change on FR1 NR PSCell with non-DRX in synchronous EN- DC	889

A.4.5.9.1.1	Test Purpose and Environment	889

A.4.5.9.1.2	Test Requirements	893

A.4.6	Measurement procedure	893

A.4.6.1	Intra-frequency Measurements	893

A.4.6.1.1	EN-DC event triggered reporting tests without gap under non-DRX	893

A.4.6.1.1.1	Test purpose and Environment	893

A.4.6.1.1.2	Test parameters	893

A.4.6.1.1.3	Test Requirements	897

A.4.6.1.2	EN-DC event triggered reporting tests without gap under DRX	897

A.4.6.1.2.1	Test purpose and Environment	897

A.4.6.1.2.2	Test parameters	897

A.4.6.1.2.2	Test Requirements	901

A.4.6.1.3	EN-DC event triggered reporting tests with per-UE gaps under non-DRX	901

A.4.6.1.3.1	Test purpose and Environment	901

A.4.6.1.3.2	Test parameters	901

A.4.6.1.3.3	Test Requirements	905

A.4.6.1.4	EN-DC event triggered reporting tests with per-UE gaps under DRX	905

A.4.6.1.4.1	Test purpose and Environment	905

A.4.6.1.4.2	Test parameters	905

A.4.6.1.4.3	Test Requirements	909

A.4.6.1.5	EN-DC event triggered reporting tests without gap under non-DRX with SSB index reading	909

A.4.6.1.5.1	Test purpose and Environment	909

A.4.6.1.5.2	Test parameters	909

A.4.6.1.5.3	Test Requirements	911

A.4.6.1.6	EN-DC event triggered reporting tests with SSB index reading with per-UE gaps	912

A.4.6.1.6.1	Test purpose and Environment	912

A.4.6.1.6.2	Test parameters	912

A.4.6.1.6.3	Test Requirements	914

A.4.6.1.7	EN-DC event triggered reporting tests under DRX for UE configured with highSpeedMeasFlag-r16	915

A.4.6.1.7.1	Test purpose and Environment	915

A.4.6.1.7.2	Test parameters	915

A.4.6.1.7.3	Test Requirements	919

A.4.6.2	Inter-frequency Measurements	919

A.4.6.2.1	EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is not used	919

A.4.6.2.1.1	Test Purpose and Environment	919

A.4.6.2.1.2	Test Requirements	923

A.4.6.2.2	EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used	923

A.4.6.2.2.1	Test Purpose and Environment	923

A.4.6.2.2.2	Test Requirements	927

A.4.6.2.3	Void	927

A.4.6.2.4	Void	927

A.4.6.2.5	EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is not used	927

A.4.6.2.5.1	Test Purpose and Environment	927

A.4.6.2.5.2	Test Requirements	932

A.4.6.2.6	EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is used	932

A.4.6.2.6.1	Test Purpose and Environment	932

A.4.6.2.6.2	Test Requirements	937

A.4.6.2.7	Void	938

A.4.6.2.8	Void	938

A.4.6.3	Void	938

A.4.6.4	L1-RSRP measurement for beam reporting	938

A.4.6.4.1	SSB based L1-RSRP measurement when DRX is not used	938

A.4.6.4.1.1	Test Purpose and Environment	938

A.4.6.4.1.2	Test parameters	938

A.4.6.4.1.3	Test Requirements	941

A.4.6.4.2	SSB based L1-RSRP measurement when DRX is used	941

A.4.6.4.2.1	Test Purpose and Environment	941

A.4.6.4.2.2	Test parameters	942

A.4.6.4.2.3	Test Requirements	945

A.4.6.4.3	CSI-RS based L1-RSRP measurement when DRX is not used	945

A.4.6.4.3.1	Test Purpose and Environment	945

A.4.6.4.3.2	Test parameters	946

A.4.6.4.3.3	Test Requirements	949

A.4.6.4.4	CSI-RS based L1-RSRP measurement when DRX is used	949

A.4.6.4.4.1	Test Purpose and Environment	949

A.4.6.4.4.2	Test parameters	950

A.4.6.4.4.3	Test Requirements	952

A.4.6.4.5	SSB based L1-RSRP measurement when DRX is used for UE configured with *highSpeedMeasFlag-r16* 952

A.4.6.4.5.1	Test Purpose and Environment	952

A.4.6.4.5.2	Test parameters	953

A.4.6.4.5.3	Test Requirements	956

A.4.6.5	CLI measurements	956

A.4.6.5.1	SRS-RSRP measurement with non-DRX	956

A.4.6.5.1.1	Test Purpose and Environment	956

A.4.6.5.1.2	Test Parameters	957

A.4.6.5.1.3	Test Requirements	960

A.4.6.5.2	CLI-RSSI measurement with non-DRX	960

A.4.6.5.2.1	Test Purpose and Environment	960

A.4.6.5.2.2	Test Parameters	961

A.4.6.5.2.3	Test Requirements	962

A.4.6.6	Measurements with autonomous gaps	963

A.4.6.6.1	EN-DC intra-frequency CGI identification of NR FR1 cell with autonomous gaps in synchronous EN-DC	963

A.4.6.6.1.1	Test Purpose and Environment	963

A.4.6.6.1.2	Test Requirements	967

A.4.6.7	L1-SINR measurement for beam reporting	967

A.4.6.7.1	L1-SINR measurement with CSI-RS based CMR and no dedicated IMR when DRX is not used	967

A.4.6.7.1.1	Test Purpose and Environment	967

A.4.6.7.1.2	Test parameters	968

A.4.6.7.1.3	Test Requirements	971

A.4.6.7.2	L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is used	971

A.4.6.7.2.1	Test Purpose and Environment	971

A.4.6.7.2.2	Test parameters	972

A.4.6.7.2.3	Test Requirements	975

A.4.6.7.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is used	975

A.4.6.7.3.1	Test Purpose and Environment	975

A.4.6.7.3.2	Test parameters	976

A.4.6.7.3.3	Test Requirements	979

A.4.6.8	CSI-RS based intra-frequency Measurement	979

A.4.6.8.1	EN-DC event triggered reporting tests without gap under DRX	979

A.4.6.8.1.1	Test purpose and Environment	979

A.4.6.8.1.2	Test Requirements	983

A.4.6.9	CSI-RS based inter-frequency Measurement	984

A.4.6.9.1	EN-DC event triggered reporting tests for FR1 cell when non-DRX is used	984

A.4.6.9.1.1	Test Purpose and Environment	984

A.4.6.9.1.2	Test Requirements	988

A.4.7	Measurement Performance requirements	989

A.4.7.1	SS-RSRP	989

A.4.7.1.1	EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	989

A.4.7.1.1.1	Test Purpose and Environment	989

A.4.7.1.1.2	Test parameters	989

A.4.7.1.1.3	Test Requirements	993

A.4.7.1.2	EN-DC inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	993

A.4.7.1.2.1	Test Purpose and Environment	993

A.4.7.1.2.2	Test parameters	994

A.4.7.1.2.3	Test Requirements	998

A.4.7.1.3	Void	998

A.4.7.2	SS-RSRQ	998

A.4.7.2.1	EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	998

A.4.7.2.1.1	Test Purpose and Environment	998

A.4.7.2.1.2	Test Parameters	999

A.4.7.2.1.3	Test Requirements	1004

A.4.7.2.2	EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1004

A.4.7.2.2.1	Test Purpose and Environment	1004

A.4.7.2.2.2	Test Parameters	1004

A.4.7.2.2.3	Test Requirements	1009

A.4.7.3	SS-SINR	1009

A.4.7.3.1	EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1009

A.4.7.3.1.1	Test Purpose and Environment	1009

A.4.7.3.1.2	Test Parameters	1009

A.4.7.3.1.3	Test Requirements	1013

A.4.7.3.2	EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1013

A.4.7.3.2.1	Test Purpose and Environment	1013

A.4.7.3.2.2	Test Parameters	1013

A.4.7.3.2.3	Test Requirements	1018

A.4.7.4	L1-RSRP measurement for beam reporting	1018

A.4.7.4.1	SSB based L1-RSRP measurement	1018

A.4.7.4.1.1	Test Purpose and Environment	1018

A.4.7.4.1.2	Test parameters	1019

A.4.7.4.1.3	Test Requirements	1022

A.4.7.4.2	CSI-RS based L1-RSRP measurement on resource set with repetition off	1022

A.4.7.4.2.1	Test Purpose and Environment	1022

A.4.7.4.2.2	Test parameters	1023

A.4.7.4.2.3	Test Requirements	1026

A.4.7.5	SFTD accuracy	1026

A.4.7.5.1	SFTD accuracy	1026

A.4.7.5.1.1	Test Purpose and Environment	1026

A.4.7.5.1.2	Test Parameters	1026

A.4.7.5.1.3	Test Requirements	1031

A.4.7.5.2	Void	1031

A.4.7.5.3	Void	1031

A.4.7.6	CLI measurements	1031

A.4.7.6.1	EN-DC SRS-RSRP measurement accuracy with FR1 serving cell	1031

A.4.7.6.1.1	Test Purpose and Environment	1031

A.4.7.6.1.2	Test parameters	1032

A.4.7.6.1.3	Test Requirements	1037

A.4.7.6.2	EN-DC CLI-RSSI measurement accuracy with FR1 serving cell	1037

A.4.7.6.2.1	Test Purpose and Environment	1037

A.4.7.6.2.2	Test parameters	1038

A.4.7.6.2.3	Test Requirements	1041

A.4.7.7	L1-SINR measurement for beam reporting	1041

A.4.7.7.1	L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured and CSI-RS resource set with repetition off	1041

A.4.7.7.1.1	Test Purpose and Environment	1041

A.4.7.7.1.2	Test parameters	1042

A.4.7.7.1.3	Test Requirements	1046

A.4.7.7.2	L1-SINR measurement with SSB based CMR and dedicated IMR	1046

A.4.7.7.2.1	Test Purpose and Environment	1046

A.4.7.7.2.2	Test parameters	1047

A.4.7.7.2.3	Test Requirements	1051

A.4.7.7.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR	1051

A.4.7.7.3.1	Test Purpose and Environment	1051

A.4.7.7.3.2	Test parameters	1052

A.4.7.7.3.3	Test Requirements	1055

A.4.7.8	CSI-RSRP	1055

A.4.7.8.1	EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1055

A.4.7.8.1.1	Test Purpose and Environment	1055

A.4.7.8.1.2	Test parameters	1056

A.4.7.8.1.3	Test Requirements	1059

A.4.7.8.2	EN-DC inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1060

A.4.7.8.2.1	Test Purpose and Environment	1060

A.4.7.8.2.2	Test parameters	1060

A.4.7.8.2.3	Test Requirements	1064

A.4.7.9	CSI-RSRQ	1064

A.4.7.9.1	EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1064

A.4.7.9.1.1	Test Purpose and Environment	1064

A.4.7.9.1.2	Test Parameters	1064

A.4.7.9.1.3	Test Requirements	1069

A.4.7.9.2	EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1069

A.4.7.9.2.1	Test Purpose and Environment	1069

A.4.7.9.2.2	Test Parameters	1069

A.4.7.2.2.3	Test Requirements	1074

A.4.7.10	CSI-SINR	1074

A.4.7.10.1	EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1074

A.4.7.10.1.1	Test Purpose and Environment	1074

A.4.7.10.1.2	Test Parameters	1075

A.4.7.10.1.3	Test Requirements	1079

A.4.7.10.2	EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1079

A.4.7.10.2.1	Test Purpose and Environment	1079

A.4.7.10.2.2	Test Parameters	1080

A.4.7.10.2.3	Test Requirements	1084

A.4.8	Void	1085

A.4A	NE-DC test with all NR cells in FR1	1085

A.4A.1	Signaling characteristics	1085

A.4A.1.1	E-UTRAN PSCell addition	1085

A.4A.1.1.1	Test purpose and environment	1085

A.4A.1.1.2	Test Requirements	1089

A.4A.1.2	Active BWP switch	1090

A.4A.1.2.1	E-UTRAN PSCell – NR PCell FR1 DCI-based and Timer-based DL active BWP switch in non-DRX in synchronous NE-DC	1090

A.4A.1.2.1.1	Test Purpose and Environment	1090

A.4A.1.2.1.2	Test Requirements	1094

A.4A.2	Measurement performance	1095

A.4A.2.1	SFTD accuracy	1095

A.4A.2.1.1	SFTD accuracy	1095

A.4A.2.1.1.1	Test Purpose	1095

A.4A.2.1.1.2	Test Environment	1095

A.4A.2.1.1.3	Test Requirements	1099

A.5	EN-DC tests with one or more NR cells in FR2	1100

A.5.1	Void	1100

A.5.2	Void	1100

A.5.3	RRC\_CONNECTED state mobility	1100

A.5.3.1	Void	1100

A.5.3.2	RRC Connection Mobility Control	1100

A.5.3.2.1	Void	1100

A.5.3.2.2	Random Access	1100

A.5.3.2.2.1	4-step RA type contention based random access test in FR2 for PSCell/SCell in EN-DC	1100

A.5.3.2.2.2	4-step RA type non-contention based random access test in FR2 for PSCell/SCell in EN-DC	1103

A.5.3.2.2.3	2-step RA type contention based random access test in FR2 for PSCell/SCell in EN-DC	1109

A.5.3.2.2.4	2-step RA type non-contention based random access test in FR2 for PSCell/SCell in EN-DC	1112

A.5.3.2.3	Void	1116

A.5.4	Timing	1116

A.5.4.1	UE transmit timing	1116

A.5.4.1.1	NR UE Transmit Timing Test for FR2	1116

A.5.4.1.1.1	Test Purpose and environment	1116

A.5.4.1.1.2	Test requirements	1119

A.5.4.2	UE timer accuracy	1120

A.5.4.3	Timing advance	1120

A.5.4.3.1 EN-DC FR2 timing advance adjustment accuracy	1120

A.5.4.3.1.1 Test Purpose and Environment	1120

A.5.4.3.1.2 Test Parameters	1120

A.5.4.3.1.3	Test Requirements	1124

A.5.5	Signaling characteristics	1124

A.5.5.1	Radio link Monitoring	1124

A.5.5.1.1	Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode	1124

A.5.5.1.1.1	Test Purpose and Environment	1124

A.5.5.1.1.2	Test Requirements	1128

A.5.5.1.2	Radio Link Monitoring In-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode	1129

A.5.5.1.2.1	Test Purpose and Environment	1129

A.5.5.1.2.2	Test Requirements	1132

A.5.5.1.3	Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in DRX mode	1133

A.5.5.1.3.1	Test Purpose and Environment	1133

A.5.5.1.3.2	Test Requirements	1137

A.5.5.1.4	Radio Link Monitoring In-sync Test for FR2 PSCell configured with SSB-based RLM RS in DRX mode	1137

A.5.5.1.4.1	Test Purpose and Environment	1137

A.5.5.1.4.2	Test Requirements	1141

A.5.5.1.5	EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with CSI-RS-based RLM in non-DRX mode	1141

A.5.5.1.6	EN-DC Radio Link Monitoring In-sync Test for FR2 PSCell configured with CSI-RS-based RLM in non-DRX mode	1145

A.5.5.1.7	EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with CSI-RS-based RLM in DRX mode	1149

A.5.5.1.8	EN-DC Radio Link Monitoring In-sync Test for FR2 PSCell configured with CSI-RS-based RLM in DRX mode	1154

A.5.5.1.8.2	Test Requirements	1158

A.5.5.1.9	EN-DC Radio Link Monitoring UE Scheduling Restrictions on FR2	1159

A.5.5.1.9.1	Test Purpose and Environment	1159

A.5.5.1.9.2	Test Requirements	1161

A.5.5.2	Interruption	1161

A.5.5.2.1	E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in synchronous EN-DC	1161

A.5.5.2.1.1	Test Purpose and Environment	1161

A.5.5.2.1.2	Test Requirements	1164

A.5.5.2.2	E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in asynchronous EN-DC	1164

A.5.5.2.2.1	Test Purpose and Environment	1164

A.5.5.2.2.2	Test Requirements	1167

A.5.5.2.3	E-UTRAN – NR FR2 interruptions during measurements on deactivated NR SCC in synchronous EN-DC	1167

A.5.5.2.3.1	Test Purpose and Environment	1167

A.5.5.2.3.2	Test Requirements	1171

A.5.5.2.4	E-UTRAN – NR FR2 interruptions during measurements on deactivated NR SCC in asynchronous EN-DC	1171

A.5.5.2.4.1	Test Purpose and Environment	1171

A.5.5.2.4.2	Test Requirements	1174

A.5.5.2.5	E-UTRAN – NR FR2 interruptions during measurements on deactivated E-UTRAN SCC in synchronous EN-DC	1175

A.5.5.2.5.1	Test Purpose and Environment	1175

A.5.5.2.5.2	Test Requirements	1178

A.5.5.2.6	E-UTRAN – NR FR2 interruptions during measurements on deactivated E-UTRAN SCC in asynchronous EN-DC	1179

A.5.5.2.6.1	Test Purpose and Environment	1179

A.5.5.2.6.2	Test Requirements	1181

A.5.5.2.7	E-UTRAN – NR FR2 interruptions at E-UTRA SRS carrier based switching	1182

A.5.5.2.7.1	Test Purpose and Environment	1182

A.5.5.2.7.2	Test Requirements	1185

A.5.5.2.8 E-UTRAN – NR FR2 interruptions at NR SRS carrier based switching	1185

A.5.5.2.8.1 Test Purpose and Environment	1185

A.5.5.2.8.3	Test Requirements	1188

A.5.5.3	SCell Activation and Deactivation Delay	1188

A.5.5.3.1	SCell Activation and deactivation of SCell in FR2 intra-band	1188

A.5.5.3.1.1	Test Purpose and Environment	1188

A.5.5.3.1.2	Test Requirements	1191

A.5.5.3.2	SCell Activation and deactivation of known SCell in FR1 for 160ms SCell measurement cycle	1191

A.5.5.3.2.1	Test Purpose and Environment	1191

A.5.5.3.2.2	Test Requirements	1195

A.5.5.3.3	Void	1195

A.5.5.3.4	Void	1195

A.5.5.3.5	SCell Activation and deactivation of SCell in FR2	1195

A.5.5.3.5.1	Test Purpose and Environment	1195

A.5.5.3.5.2	Test Requirements	1199

A.5.5.3.6	Multiple SCell Activation and deactivation of one unknown SCell and one known SCell in FR2	1200

A.5.5.3.6.1	Test Purpose and Environment	1200

A.5.5.3.6.2	Test Requirements	1203

A.5.5.3.7	Direct SCell activation at SCell addition of known SCell in FR2	1204

A.5.5.3.7.1	Test Purpose and Environment	1204

A.5.5.3.7.2	Test Requirements	1207

A.5.5.4	Void	1207

A.5.5.5	Beam Failure Detection and Link recovery procedures	1207

A.5.5.5.1	EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with SSB-based BFD and LR in non-DRX mode	1207

A.5.5.5.1.1	Test Purpose and Environment	1207

A.5.5.5.1.2	Test Requirements	1211

A.5.5.5.2	EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with SSB-based BFD and LR in DRX mode	1212

A.5.5.5.2.1	Test Purpose and Environment	1212

A.5.5.5.2.2	Test Requirements	1216

A.5.5.5.3	EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with CSI-RS-based BFD and LR in non-DRX mode	1217

A.5.5.5.3.1	Test Purpose and Environment	1217

A.5.5.5.3.2	Test Requirements	1221

A.5.5.5.4	EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with CSI-RS-based BFD and LR in DRX mode	1222

A.5.5.5.4.1	Test Purpose and Environment	1222

A.5.5.5.4.2	Test Requirements	1226

A.5.5.5.5	EN-DC scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2 PSCell configured with SSB-based BFD and LR in non-DRX mode	1227

A.5.5.5.5.1	Test Purpose and Environment	1227

A.5.5.5.5.2	Test Requirements	1231

A.5.5.5.6	EN-DC Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in non-DRX mode	1231

A.5.5.5.6.1	Test Purpose and Environment	1231

A.5.5.5.6.2	Test Requirements	1236

A.5.5.5.7	EN-DC Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in DRX mode	1237

A.5.5.5.7.1	Test Purpose and Environment	1237

A.5.5.5.7.2	Test Requirements	1241

A.5.5.6	Active BWP switch	1242

A.5.5.6.1	DCI-based and Timer-based Active BWP Switch	1242

A.5.5.6.1.1	E-UTRAN – NR PSCell FR2 DL active BWP switch with non-DRX in synchronous EN-DC	1242

A.5.5.6.1.1.1	Test Purpose and Environment	1242

A.5.5.6.1.1.2	Test Requirements	1245

A.5.5.6.1.2	E-UTRAN – NR PSCell FR2 with FR2 SCell DL active BWP switch in non-DRX in synchronous EN-DC	1245

A.5.5.6.2	RRC-based Active BWP Switch	1250

A.5.5.6.3 Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs	1254

A.5.5.6.3.1	E-UTRAN – NR PSCell FR2 and NR SCell FR2 DL active BWP switch on multiple CCs in synchronous EN-DC	1254

A.5.5.6.3.1.1	Test Purpose and Environment	1254

A.5.5.6.4	SCell dormancy switch	1258

A.5.5.6.4.1	E-UTRAN – NR FR2 PSCell SCell dormancy switch of single FR2 SCell inside active time	1258

A.5.5.6.4.1.1	Test Purpose and Environment	1258

A.5.5.6.4.1.2	Test Requirements	1262

A.5.5.6.4.2	E-UTRAN – NR FR1 PSCell SCell dormancy switch of two FR2 SCells outside active time	1262

A.5.5.6.4.2.1	Test Purpose and Environment	1262

A.5.5.6.4.2.2	Test Requirements	1269

A.5.5.6.5	Simultaneous RRC-based Active BWP Switch on multiple CCs	1269

A.5.5.7	PSCell addition and release delay	1272

A.5.5.7.1	Addition and Release Delay of NR PSCell	1272

A.5.5.7.1.1	Test purpose and environment	1272

A.5.5.7.1.2	Test Requirements	1276

A.5.5.8	Active TCI state switch delay	1277

A.5.5.8.1	MAC-CE based active TCI state switch	1277

A.5.5.8.1.1	E-UTRAN – NR PSCell FR2 active TCI state switch for a known TCI state	1277

A.5.5.8.1.1.1	Test Purpose and Environment	1277

A.5.5.8.1.1.2	Test Requirements	1281

A.5.5.8.2	RRC based active TCI state switch	1281

A.5.5.8.2.1	E-UTRAN – NR PSCell FR2 active TCI state switch for a known TCI state	1281

A.5.5.8.2.1.1	Test Purpose and Environment	1281

A.5.5.8.2.1.2	Test Requirements	1285

A.5.5.9	Uplink spatial relation switch delay	1285

A.5.5.9.1	MAC-CE based uplink spatial relation switch	1285

A.5.5.9.1.1	E-UTRAN – NR PSCell FR2 uplink spatial relation switch for a known spatial relation	1285

A.5.5.9.1.1.1	Test Purpose and Environment	1285

A.5.5.9.1.1.2	Test Requirements	1288

A.5.5.9.2	RRC based spatial relation switch	1288

A.5.5.9.2.1	E-UTRAN – NR PSCell FR2 spatial relation switch associated with a known DL-RS	1288

A.5.5.9.2.1.1	Test Purpose and Environment	1288

A.5.5.9.2.1.2	Test Requirements	1291

A.5.5.10	UE specific CBW change	1291

A.5.5.10.1	UE specific CBW change on FR2 NR PSCell	1291

A.5.5.10.1.1	Test Purpose and Environment	1291

A.5.5.10.1.2	Test Requirements	1294

A.5.6	Measurement procedure	1295

A.5.6.1	Intra-frequency Measurements	1295

A.5.6.1.1	EN-DC event triggered reporting test without gap under non-DRX	1295

A.5.6.1.1.1	Test purpose and Environment	1295

A.5.6.1.1.2	Test Requirements	1298

A.5.6.1.2	EN-DC event triggered reporting test without gap under DRX	1298

A.5.6.1.2.1	Test purpose and Environment	1298

A.5.6.1.2.2	Test Requirements	1300

A.5.6.1.3	EN-DC event triggered reporting test with per-UE gaps under non-DRX	1301

A.5.6.1.3.1	Test purpose and Environment	1301

A.5.6.1.3.2	Test Requirements	1305

A.5.6.1.4	EN-DC event triggered reporting test with per-UE gaps under DRX	1305

A.5.6.1.4.1	Test purpose and Environment	1305

A.5.6.1.4.2	Test Requirements	1308

A.5.6.2	Inter-frequency Measurements	1309

A.5.6.2.1 	EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is not used	1309

A.5.6.2.1.1	Test Purpose and Environment	1309

A.5.6.2.1.2	Test Requirements	1312

A.5.6.2.2 	EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is used	1312

A.5.6.2.2.1	Test Purpose and Environment	1312

A.5.6.2.2.2	Test Requirements	1316

A.5.6.2.3 	EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is not used	1316

A.5.6.2.3.1	Test Purpose and Environment	1316

A.5.6.2.3.2	Test Requirements	1320

A.5.6.2.4	EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is used	1320

A.5.6.2.4.1	Test Purpose and Environment	1320

A.5.6.2.4.2	Test Requirements	1324

A.5.6.2.5	EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is not used	1324

A.5.6.2.5.1	Test Purpose and Environment	1324

A.5.6.2.5.2	Test Requirements	1329

A.5.6.2.6	EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is used	1330

A.5.6.2.6.1	Test Purpose and Environment	1330

A.5.6.2.6.2	Test Requirements	1333

A.5.6.2.7	EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is not used	1334

A.5.6.2.7.1	Test Purpose and Environment	1334

A.5.6.2.7.2	Test Requirements	1338

A.5.6.2.8	EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is used	1338

A.5.6.2.8.1	Test Purpose and Environment	1338

A.5.6.2.8.2	Test Requirements	1343

A.5.6.3	L1-RSRP measurement for beam reporting	1343

A.5.6.3.1	SSB based L1-RSRP measurement when DRX is not used	1343

A.5.6.3.1.1	Test Purpose and Environment	1343

A.5.6.3.1.2	Test parameters	1343

A.5.6.3.1.3	Test Requirements	1345

A.5.6.3.2	SSB based L1-RSRP measurement when DRX is used	1345

A.5.6.3.2.1	Test Purpose and Environment	1345

A.5.6.3.2.2	Test parameters	1346

A.5.6.3.2.3	Test Requirements	1348

A.5.6.3.3	CSI-RS based L1-RSRP measurement when DRX is not used	1348

A.5.6.3.3.1	Test Purpose and Environment	1348

A.5.6.3.3.2	Test parameters	1349

A.5.6.3.3.3	Test Requirements	1351

A.5.6.3.4	CSI-RS based L1-RSRP measurement when DRX is used	1352

A.5.6.3.4.1	Test Purpose and Environment	1352

A.5.6.3.4.2	Test parameters	1352

A.5.6.3.4.3	Test Requirements	1354

A.5.6.4	CLI measurements	1355

A.5.6.4.1	SRS-RSRP measurement with DRX	1355

A.5.6.4.1.1	Test Purpose and Environment	1355

A.5.6.4.1.2	Test Parameters	1355

A.5.6.4.1.3	Test Requirements	1357

A.5.6.4.2	CLI-RSSI measurement with DRX	1357

A.5.6.4.2.1	Test Purpose and Environment	1357

A.5.6.4.2.2	Test Parameters	1358

A.5.6.4.2.3	Test Requirements	1360

A.5.6.5	Measurements with autonomous gaps	1360

A.5.6.5.1 	EN-DC inter-frequency CGI identification of NR neighbor cell in FR2	1360

A.5.6.5.1.1	Test Purpose and Environment	1360

A.5.6.5.1.2	Test Requirements	1363

A.5.6.6	L1-SINR measurement for beam reporting	1364

A.5.6.6.1	L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured when DRX is used	1364

A.5.6.6.1.1	Test Purpose and Environment	1364

A.5.6.6.1.2	Test parameters	1364

A.5.6.6.1.3	Test Requirements	1366

A.5.6.6.2	L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is not used	1366

A.5.6.6.2.1	Test Purpose and Environment	1366

A.5.6.6.2.2	Test parameters	1367

A.5.6.6.2.3	Test Requirements	1370

A.5.6.6.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is not used	1370

A.5.6.6.3.1	Test Purpose and Environment	1370

A.5.6.6.3.2	Test parameters	1371

A.5.6.6.3.3	Test Requirements	1373

A.5.6.7	CSI-RS based Intra-frequency Measurements	1373

A.5.6.7.1	EN-DC event triggered reporting test without gap under non-DRX	1373

A.5.6.7.1.1	Test purpose and Environment	1373

A.5.6.7.1.2	Test Requirements	1376

A.5.6.8	CSI-RS based Inter-frequency Measurements	1377

A.5.6.8.1 	EN-DC event triggered reporting tests for NR FR2 cell when DRX is used	1377

A.5.6.8.1.1	Test Purpose and Environment	1377

A.5.6.8.1.2	Test Requirements	1380

A.5.7	Measurement Performance requirements	1380

A.5.7.1	SS-RSRP	1381

A.5.7.1.1	EN-DC intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	1381

A.5.7.1.1.1	Test Purpose and Environment	1381

A.5.7.1.1.2	Test parameters	1381

A.5.7.1.1.3	Test Requirements	1383

A.5.7.1.2	EN-DC inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	1384

A.5.7.1.2.1	Test Purpose and Environment	1384

A.5.7.1.2.2	Test parameters	1384

A.5.7.1.2.3	Test Requirements	1389

A.5.7.1.3	EN-DC inter-frequency measurement accuracy with FR1 serving cell and FR2 target cell	1390

A.5.7.1.3.1	Test Purpose and Environment	1390

A.5.7.1.3.2	Test parameters	1390

A.5.7.1.3.3	Test Requirements	1393

A.5.7.2	SS-RSRQ	1394

A.5.7.2.1	EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	1394

A.5.7.2.1.1	Test Purpose and Environment	1394

A.5.7.2.1.2	Test Parameters	1394

A.5.7.2.1.3	Test Requirements	1396

A.5.7.2.2	EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	1397

A.5.7.2.2.1	Test Purpose and Environment	1397

A.5.7.2.2.2	Test Parameters	1397

A.5.7.2.2.3	Test Requirements	1399

A.5.7.3	SS-SINR	1399

A.5.7.3.1	EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	1399

A.5.7.3.1.1	Test Purpose and Environment	1399

A.5.7.3.1.2	Test Parameters	1399

A.5.7.3.1.3	Test Requirements	1401

A.5.7.3.2	EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	1401

A.5.7.3.2.1	Test Purpose and Environment	1401

A.5.7.3.2.2	Test Parameters	1401

A.5.7.3.2.3	Test Requirements	1403

A.5.7.4	L1-RSRP measurement for beam reporting	1403

A.5.7.4.1	SSB based L1-RSRP measurement	1403

A.5.7.4.1.1	Test Purpose and Environment	1403

A.5.7.4.1.2	Test parameters	1404

A.5.7.4.1.3	Test Requirements	1406

A.5.7.4.2	CSI-RS based L1-RSRP measurement on resource set with repetition off	1407

A.5.7.4.2.1	Test Purpose and Environment	1407

A.5.7.4.2.2	Test parameters	1407

A.5.7.4.2.3	Test Requirements	1409

A.5.7.5	CLI measurements	1410

A.5.7.5.1	EN-DC SRS-RSRP measurement accuracy with FR2 serving cell	1410

A.5.7.5.1.1	Test Purpose and Environment	1410

A.5.7.5.1.2	Test parameters	1410

A.5.7.5.1.3	Test Requirements	1413

A.5.7.5.2	EN-DC CLI-RSSI measurement accuracy with FR2 serving cell	1414

A.5.7.5.2.1	Test Purpose and Environment	1414

A.5.7.5.2.2	Test parameters	1414

A.5.7.5.2.3	Test Requirements	1416

A.5.7.6	L1-SINR measurement for beam reporting	1417

A.5.7.6.1	L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured and CSI-RS resource set with repetition off	1417

A.5.7.6.1.1	Test Purpose and Environment	1417

A.5.7.6.1.2	Test parameters	1417

A.5.7.6.1.3	Test Requirements	1419

A.5.7.6.2	L1-SINR measurement with SSB based CMR and dedicated IMR	1420

A.5.7.6.2.1	Test Purpose and Environment	1420

A.5.7.6.2.2	Test parameters	1420

A.5.7.6.2.3	Test Requirements	1422

A.5.7.6.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR	1423

A.5.7.6.3.1	Test Purpose and Environment	1423

A.5.7.6.3.2	Test parameters	1423

A.5.7.6.3.3	Test Requirements	1425

A.5.7.7	CSI-RSRP	1426

A.5.7.7.1	EN-DC intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	1426

A.5.7.7.1.2	Test parameters	1426

A.5.7.7.1.3	Test Requirements	1430

A.5.7.7.2	EN-DC inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	1431

A.5.7.7.2.1	Test Purpose and Environment	1431

A.5.7.7.2.2	Test parameters	1431

A.5.7.7.2.3	Test Requirements	1435

A.5.7.8	CSI-RSRQ	1436

A.5.7.8.1	EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell	1436

A.5.7.8.1.1	Test Purpose and Environment	1436

A.5.7.8.1.2	Test Parameters	1436

A.5.7.8.1.3	Test Requirements	1438

A.5.7.8.2	EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	1438

A.5.7.8.2.1	Test Purpose and Environment	1438

A.5.7.8.2.2	Test Parameters	1438

A.5.7.9	CSI-SINR	1440

A.5.7.9.1	EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	1440

A.5.7.9.1.1	Test Purpose and Environment	1440

A.5.7.9.1.2	Test Parameters	1441

Table A.5.7.9.1.2-1: CSI-SINR Intra frequency CSI-SINR supported test configurations	1441

A.5.7.9.1.3	Test Requirements	1443

A.5.7.9.2	EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	1443

A.5.7.9.2.1	Test Purpose and Environment	1443

A.5.7.9.2.2	Test Parameters	1443

A.5.7.9.2.3	Test Requirements	1446

A.5.8	Void	1446

A.6	NR standalone tests with all NR cells in FR1	1446

A.6.1	SA: RRC\_IDLE state mobility	1446

A.6.1.1	Cell re-selection to NR	1446

A.6.1.1.1	Cell reselection to FR1 intra-frequency NR case	1446

A.6.1.1.1.1	Test Purpose and Environment	1446

A.6.1.1.1.2	Test Parameters	1446

A.6.1.1.1.3	Test Requirements	1450

A.6.1.1.2	Cell reselection to FR1 inter-frequency NR case	1450

A.6.1.1.2.1	Test Purpose and Environment	1450

A.6.1.1.2.2	Test Parameters	1450

A.6.1.1.2.3	Test Requirements	1454

A.6.1.1.3	Cell reselection to FR1 intra-frequency NR case for UE fulfilling low mobility relaxed measurement criterion	1454

A.6.1.1.3.1	Test Purpose and Environment	1454

A.6.1.1.3.2	Test Parameters	1454

A.6.1.1.3.3	Test Requirements	1459

A.6.1.1.4	Cell reselection to FR1 intra-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion	1459

A.6.1.1.4.1	Test Purpose and Environment	1459

A.6.1.1.4.2	Test Parameters	1459

A.6.1.1.4.3	Test Requirements	1463

A.6.1.1.5	Cell reselection to FR1 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion	1463

A.6.1.1.5.1	Test Purpose and Environment	1463

A.6.1.1.5.2	Test Parameters	1463

A.6.1.1.5.3	Test Requirements	1467

A.6.1.1.6	Cell reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion	1467

A.6.1.1.6.1	Test Purpose and Environment	1467

A.6.1.1.6.2	Test Parameters	1468

A.6.1.1.6.3	Test Requirements	1472

A.6.1.1.7	Cell reselection to FR1 intra-frequency NR case for UE configured with *highSpeedMeasFlag-r16* 1473

A.6.1.1.7.1	Test Purpose and Environment	1473

A.6.1.1.7.2	Test Parameters	1473

A.6.1.1.7.3	Test Requirements	1477

A.6.1.2	Inter-RAT E-UTRAN cell re-selection	1477

A.6.1.2.1	Cell reselection to higher priority E-UTRAN	1477

A.6.1.2.1.1	Test Purpose and Environment	1477

A.6.1.2.1.2	Test Parameters	1477

A.6.1.2.1.3	Test Requirements	1480

A.6.1.2.2	Cell reselection to lower priority E-UTRAN	1481

A.6.1.2.2.1	Test Purpose and Environment	1481

A.6.1.2.2.2	Test Parameters	1481

A.6.1.2.2.3	Test Requirements	1484

A.6.1.2.3	Cell reselection to lower priority E-UTRAN for UE fulfilling low mobility relaxed measurement criterion	1485

A.6.1.2.3.1	Test Purpose and Environment	1485

A.6.1.2.3.2	Test Parameters	1485

A.6.1.2.3.3	Test Requirements	1488

A.6.1.2.4	Cell reselection to lower priority E-UTRAN for UE fulfilling not-at-cell edge relaxed measurement criterion	1489

A.6.1.2.4.1	Test Purpose and Environment	1489

A.6.1.2.4.2	Test Parameters	1489

A.6.1.2.4.3	Test Requirements	1492

A.6.1.2.5.3	Test Requirements	1496

A.6.2	SA: RRC\_INACTIVE state mobility	1497

A.6.3	RRC\_CONNECTED state mobility	1497

A.6.3.1	Handover	1497

A.6.3.1.1	Intra-frequency handover from FR1 to FR1; known target cell	1497

A.6.3.1.1.1	Test Purpose and Environment	1497

A.6.3.1.1.2	Test Parameters	1497

A.6.3.1.1.3 Test Requirements	1501

A.6.3.1.2	Intra-frequency handover from FR1 to FR1; unknown target cell	1501

A.6.3.1.2.1	Test Purpose and Environment	1501

A.6.3.1.2.2	Test Parameters	1501

A.6.3.1.2.3	Test Requirements	1505

A.6.3.1.3	Inter-frequency handover from FR1 to FR1; unknown target cell	1505

A.6.3.1.3.1	Test Purpose and Environment	1505

A.6.3.1.3.2	Test Parameters	1505

A.6.3.1.3.3 Test Requirements	1509

A.6.3.1.4	 SA NR - E-UTRAN handover	1509

A.6.3.1.4.1	Test Purpose and Environment	1509

A.6.3.1.4.2	Test Requirements	1515

A.6.3.1.5	SA NR - E-UTRAN handover with unknown target cell	1515

A.6.3.1.5.1	Test Purpose and Environment	1515

A.6.3.1.5.2	Test Requirements	1521

A.6.3.1.6	 SA NR - UTRAN FDD handover	1521

A.6.3.1.6.1	Test Purpose and Environment	1521

A.6.3.1.6.2	Test Requirements	1525

A.6.3.1.7	Intra-frequency synchronous DAPS handover in FR1	1525

A.6.3.1.7.1	Test Purpose and Environment	1525

A.6.3.1.7.2	Test Parameters	1525

A.6.3.1.7.3 Test Requirements	1529

A.6.3.1.8	Intra-frequency asynchronous DAPS handover in FR1	1530

A.6.3.1.8.1	Test Purpose and Environment	1530

A.6.3.1.8.2	Test Parameters	1530

A.6.3.1.8.3 Test Requirements	1534

A.6.3.1.9	Intra-band inter-frequency synchronous DAPS handover test in SA for FR1	1535

A.6.3.1.9.1	Test Purpose and Environment	1535

A.6.3.1.9.2	Test Parameters	1535

A.6.3.1.9.3 Test Requirements	1539

A.6.3.1.10	Intra-band inter-frequency asynchronous DAPS handover test in SA for FR1	1539

A.6.3.1.10.1	Test Purpose and Environment	1539

A.6.3.1.10.2	Test Parameters	1539

A.6.3.1.10.3 Test Requirements	1542

A.6.3.1.11	Inter-band inter-frequency synchronous DAPS handover from FR1 to FR1	1542

A.6.3.1.11.1	Test Purpose and Environment	1542

A.6.3.1.11.2	Test Parameters	1542

A.6.3.1.11.3 Test Requirements	1549

A.6.3.1.12	Inter-band inter-frequency asynchronous DAPS handover from FR1 to FR1	1549

A.6.3.1.12.1	Test Purpose and Environment	1549

A.6.3.1.12.2	Test Parameters	1549

A.6.3.1.12.3 Test Requirements	1557

A.6.3.2	RRC Connection Mobility Control	1557

A.6.3.2.1	SA: RRC Re-establishment	1557

A.6.3.2.1.1	Intra-frequency RRC Re-establishment in FR1	1557

A.6.3.2.1.2	Inter-frequency RRC Re-establishment in FR1	1561

A.6.3.2.1.3	Intra-frequency RRC Re-establishment in FR1 without serving cell timing	1565

A.6.3.2.2	Random Access	1569

A.6.3.2.2.1	4-step RA type contention based random access test in FR1 for NR standalone	1569

A.6.3.2.2.2	4-step RA type non-contention based random access test in FR1 for NR standalone	1574

A.6.3.2.2.3	2-step RA type contention based random access test in FR1 for NR standalone	1578

A.6.3.2.2.4	2-step RA type non-contention based test in FR1 for NR standalone	1583

A.6.3.2.3	SA: RRC Connection Release with Redirection	1587

A.6.3.2.3.1	Redirection from NR in FR1 to NR in FR1	1587

A.6.3.2.3.2	Redirection from NR in FR1 to E-UTRAN	1591

A.6.3.3	Conditional handover	1598

A.6.3.3.1	Intra-frequency conditional handover from FR1 to FR1	1598

A.6.3.3.1.1	Test Purpose and Environment	1598

A.6.3.3.1.2	Test Parameters	1598

A.6.3.3.1.3 Test Requirements	1602

A.6.3.3.2	Inter-frequency conditional handover from FR1 to FR1	1602

A.6.3.3.2.1	Test Purpose and Environment	1602

A.6.3.3.2.2	Test Parameters	1602

A.6.3.3.2.3 Test Requirements	1606

A.6.4	Timing	1606

A.6.4.1	UE transmit timing	1606

A.6.4.1.1	NR UE Transmit Timing Test for FR1	1606

A.6.4.1.1.1	Test Purpose and environment	1606

A.6.4.1.1.2	Test requirements	1610

A.6.4.2	UE timer accuracy	1610

A.6.4.3	Timing advance	1610

A.6.4.3.1	SA FR1 timing advance adjustment accuracy	1610

A.6.4.3.1.1	Test Purpose and Environment	1610

A.6.4.3.1.2	Test Parameters	1610

A.6.4.3.1.3	Test Requirements	1614

A.6.5	Signalling characteristics	1614

A.6.5.1	Radio link Monitoring	1614

A.6.5.1.1	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode	1615

A.6.5.1.1.1	Test Purpose and Environment	1615

A.6.5.1.1.2	Test Requirements	1620

A.6.5.1.2	Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode	1620

A.6.5.1.2.1	Test Purpose and Environment	1620

A.6.5.1.2.2	Test Requirements	1626

A.6.5.1.3	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode	1626

A.6.5.1.3.1	Test Purpose and Environment	1626

A.6.5.1.3.2	Test Requirements	1632

A.6.5.1.4	Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode	1632

A.6.5.1.4.1	Test Purpose and Environment	1632

A.6.5.1.4.2	Test Requirements	1638

A.6.5.1.5	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode	1638

A.6.5.1.5.1	Test Purpose and Environment	1638

A.6.5.1.5.2	Test Requirements	1644

A.6.5.1.6	Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode	1644

A.6.5.1.6.1	Test Purpose and Environment	1644

A.6.5.1.6.2	Test Requirements	1649

A.6.5.1.7	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode	1649

A.6.5.1.7.1	Test Purpose and Environment	1649

A.6.5.1.7.2	Test Requirements	1653

A.6.5.1.8	Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode	1653

A.6.5.1.8.1	Test Purpose and Environment	1653

A.6.5.1.8.2	Test Requirements	1659

A.6.5.2	Interruption	1659

A.6.5.2.1	Interruptions during measurements on deactivated NR SCC in FR1	1659

A.6.5.2.1.2	Test Requirements	1663

A.6.5.2.2	SA interruptions at NR SRS carrier based switching	1664

A.6.5.2.2.1	Test Purpose and Environment	1664

A.6.5.2.2.2	Test Parameters	1664

A.6.5.2.2.3	Test Requirements	1666

A.6.5.3	SCell Activation and Deactivation Delay	1667

A.6.5.3.1	SCell Activation and deactivation of known SCell in FR1 in non-DRX for 160ms SCell measurement cycle	1667

A.6.5.3.1.1	Test Purpose and Environment	1667

A.6.5.3.1.2	Test Requirements	1672

A.6.5.3.2	SCell Activation and deactivation of known SCell in FR1 in non-DRX for 640 ms SCell measurement cycle	1673

A.6.5.3.2.1	Test Purpose and Environment	1673

A.6.5.3.2.2	Test Requirements	1673

A.6.5.3.3	SCell Activation and deactivation of unknown SCell in FR1 in non-DRX	1673

A.6.5.3.3.1	Test Purpose and Environment	1673

A.6.5.3.3.2	Test Requirements	1674

A.6.5.3.4	Direct SCell activation at SCell addition of known SCell in FR1	1674

A.6.5.3.4.1	 Test Purpose and Environment	1674

A.6.5.3.4.2	Test Requirements	1679

A.6.5.3.5	Direct SCell activation at handover with known SCell in FR1	1679

A.6.5.3.5.1	Test Purpose and Environment	1679

A.6.5.3.5.2	Test Requirements	1684

A.6.5.4	UE UL carrier RRC reconfiguration Delay	1685

A.6.5.4.1	UE UL carrier RRC reconfiguration Delay	1685

A.6.5.4.1.1	Test Purpose and Environment	1685

A.6.5.4.1.2	Test Requirements	1693

A.6.5.4.2	Void	1694

A.6.5.5	Beam Failure Detection and Link recovery procedures	1694

A.6.5.5.1	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode	1694

A.6.5.5.1.1	Test Purpose and Environment	1694

A.6.5.5.1.2	Test Requirements	1699

A.6.5.5.2	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode	1700

A.6.5.5.2.1	Test Purpose and Environment	1700

A.6.5.5.2.2	Test Requirements	1706

A.6.5.5.3	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode	1707

A.6.5.5.3.1	Test Purpose and Environment	1707

A.6.5.5.3.2	Test Requirements	1712

A.6.5.5.4	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode	1713

A.6.5.5.4.1	Test Purpose and Environment	1713

A.6.5.5.4.2	Test Requirements	1718

A.6.5.5.5	Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in non-DRX mode	1719

A.6.5.5.5.1	Test Purpose and Environment	1719

A.6.5.5.5.2	Test Requirements	1723

A.6.5.5.6	Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in DRX mode	1723

A.6.5.5.6.1	Test Purpose and Environment	1723

A.6.5.5.6.2	Test Requirements	1727

A.6.5.6	Active BWP switch	1728

A.6.5.6.1	DCI-based and Timer-based Active BWP Switch	1728

A.6.5.6.1.1	NR FR1- NR FR1 DL active BWP switch of SCell with non-DRX in SA	1728

A.6.5.6.1.2	NR FR1 DL active BWP switch with non-DRX in SA	1735

A.6.5.6.2	RRC-based Active BWP Switch	1739

A.6.5.6.2.1	NR FR1 DL active BWP switch of Cell with non-DRX in SA	1739

A.6.5.6.3	Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs	1743

A.6.5.6.3.1	NR FR1- NR FR1 DL active BWP switch on multiple CCs with non-DRX in SA	1743

A.6.5.6.4	SCell dormancy switch	1750

A.6.5.6.4.1	NR FR1 PCell SCell dormancy switch of single FR1 SCell outside active time	1750

A.6.5.6.4.2	NR FR1 PCell SCell dormancy switch of two FR1 SCells inside active time	1756

A.6.5.6.5	Simultaneous RRC-based Active BWP Switch on multiple CCs	1763

A.6.5.6.5.1	NR FR1- NR FR1 DL active BWP switch on multiple CCs with non-DRX in SA	1763

A.6.5.7	DL interruptions at switching between two uplink carriers	1768

A.6.5.7.1	DL interruptions at switching between two uplink carriers in FDD-TDD CA	1768

A.6.5.7.1.1	Test Purpose and Environment	1768

A.6.5.7.1.2	Test Requirements	1772

A.6.5.7.2	DL interruptions at switching between two uplink carriers in TDD-TDD CA	1772

A.6.5.7.2.1	Test Purpose and Environment	1772

A.6.5.7.2.2	Test Requirements	1776

A.6.5.8	UE specific CBW change	1776

A.6.5.8.1	UE specific CBW change on PCell in FR1 in non-DRX	1776

A.6.5.8.1.1	Test Purpose and Environment	1776

A.6.5.8.1.2	Test Requirements	1780

A.6.5.9	Pathloss reference signal switching delay	1780

A.6.5.9.1	MAC-CE based pathloss reference signal switch delay	1780

A.6.5.9.1.1	Test Purpose and Environment	1780

A.6.5.9.1.2	Test Requirements	1783

A.6.6	Measurement procedure	1784

A.6.6.1	Intra-frequency Measurements	1784

A.6.6.1.1	SA event triggered reporting tests without gap under non-DRX	1784

A.6.6.1.1.1	Test purpose and Environment	1784

A.6.6.1.1.2	Test parameters	1784

A.6.6.1.1.3	Test Requirements	1788

A.6.6.1.2	SA event triggered reporting tests without gap under DRX	1788

A.6.6.1.2.1	Test purpose and Environment	1788

A.6.6.1.2.2	Test parameters	1788

A.6.6.1.2.3	Test Requirements	1792

A.6.6.1.3	SA event triggered reporting tests with per-UE gaps under non-DRX	1792

A.6.6.1.3.1	Test purpose and Environment	1792

A.6.6.1.3.2	Test parameters	1792

A.6.6.1.3.3	Test Requirements	1796

A.6.6.1.4	SA event triggered reporting tests with per-UE gaps under DRX	1796

A.6.6.1.4.1	Test purpose and Environment	1796

A.6.6.1.4.2	Test parameters	1796

A.6.6.1.4.3	Test Requirements	1800

A.6.6.1.5	SA event triggered reporting tests without gap under non-DRX with SSB index reading	1800

A.6.6.1.5.1	Test purpose and Environment	1800

A.6.6.1.5.2	Test parameters	1800

A.6.6.1.5.3	Test Requirements	1802

A.6.6.1.6	SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading	1803

A.6.6.1.6.1	Test purpose and Environment	1803

A.6.6.1.6.2	Test parameters	1803

A.6.6.1.6.3	Test Requirements	1804

A.6.6.1.7	SA event triggered reporting tests under DRX for UE configured with highSpeedMeasFlag-r16	1805

A.6.6.1.7.1	Test purpose and Environment	1805

A.6.6.1.7.2	Test parameters	1805

A.6.6.1.7.3	Test Requirements	1809

A.6.6.2	Inter-frequency Measurements	1809

A.6.6.2.1	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used	1809

A.6.6.2.1.1	Test Purpose and Environment	1809

A.6.6.2.1.2	Test Requirements	1813

A.6.6.2.2	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used	1813

A.6.6.2.2.1	Test Purpose and Environment	1813

A.6.6.2.2.2	Test Requirements	1817

A.6.6.2.3	Void	1818

A.6.6.2.4	Void	1818

A.6.6.2.5	SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used	1818

A.6.6.2.5.1	Test Purpose and Environment	1818

A.6.6.2.5.2	Test Requirements	1822

A.6.6.2.6	SA event triggered reporting tests for FR1 with SSB time index detection when DRX is used	1822

A.6.6.2.6.1	Test Purpose and Environment	1822

A.6.6.2.6.2	Test Requirements	1826

A.6.6.2.7	Void	1827

A.6.6.2.8	Void	1827

A.6.6.2.9	SA event triggered reporting tests with additional mandatory gap pattern	1827

A.6.6.2.9.1	Test Purpose and Environment	1827

A.6.6.2.9.2	Test Requirements	1830

A.6.6.2.10	SA event triggered reporting tests for FR1 when DRX is used	1830

A.6.6.2.10.1	Test Purpose and Environment	1830

A.6.6.2.10.2	Test Requirements	1834

A.6.6.2.11	SA event triggered reporting tests for FR1 without gap when DRX is not used	1835

A.6.6.2.11.1	Test Purpose and Environment	1835

A.6.6.2.11.2	Test Requirements	1838

A.6.6.3	Inter-RAT Measurements	1838

A.6.6.3.1	SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1	1838

A.6.6.3.1.1	Test Purpose and Environment	1838

A.6.6.3.1.2	Test Requirements	1844

A.6.6.3.2	SA NR - E-UTRAN event-triggered reporting in DRX in FR1	1844

A.6.6.3.2.1	Test Purpose and Environment	1844

A.6.6.3.2.2	Test Requirements	1851

A.6.6.3.3	SA NR - E-UTRAN event-triggered reporting in DRX in FR1 for UE configured with highSpeedMeasFlag-r16	1851

A.6.6.3.3.1	Test Purpose and Environment	1851

A.6.6.3.3.2	Test Requirements	1858

A.6.6.4	L1-RSRP measurement for beam reporting	1858

A.6.6.4.1	SSB based L1-RSRP measurement when DRX is not used	1858

A.6.6.4.1.1	Test Purpose and Environment	1858

A.6.6.4.1.2	Test parameters	1858

A.6.6.4.1.3	Test Requirements	1861

A.6.6.4.2	SSB based L1-RSRP measurement when DRX is used	1861

A.6.6.4.2.1	Test Purpose and Environment	1861

A.6.6.4.2.2	Test parameters	1862

A.6.6.4.2.3	Test Requirements	1865

A.6.6.4.3	CSI-RS based L1-RSRP measurement when DRX is not used	1865

A.6.6.4.3.1	Test Purpose and Environment	1865

A.6.6.4.3.2	Test parameters	1866

A.6.6.4.3.3	Test Requirements	1869

A.6.6.4.4	CSI-RS based L1-RSRP measurement when DRX is used	1869

A.6.6.4.4.1	Test Purpose and Environment	1869

A.6.6.4.4.2	Test parameters	1870

A.6.6.4.4.3	Test Requirements	1873

A.6.6.4.5	SSB based L1-RSRP measurement when DRX is used for UE configured with *highSpeedMeasFlag-r16* 1873

A.6.6.4.5.1	Test Purpose and Environment	1873

A.6.6.4.5.2	Test parameters	1874

A.6.6.4.5.3	Test Requirements	1877

A.6.6.5	1877

A.6.6.5.1	SA NR - UTRAN FDD event-triggered reporting in non-DRX in FR1	1877

A.6.6.5.1.1	Test Purpose and Environment	1877

A.6.6.5.1.2	Test Requirements	1881

A.6.6.6	CLI measurements	1881

A.6.6.6.1	SRS-RSRP measurement with DRX	1881

A.6.6.6.1.1	Test Purpose and Environment	1881

A.6.6.6.1.2	Test Parameters	1882

A.6.6.6.1.3	Test Requirements	1885

A.6.6.6.2	CLI-RSSI measurement with DRX	1885

A.6.6.6.2.1	Test Purpose and Environment	1885

A.6.6.6.2.2	Test Parameters	1886

A.6.6.6.2.3	Test Requirements	1888

A.6.6.7	NR measurements with autonomous gaps	1888

A.6.6.7.1	SA intra-frequency CGI identification of NR neighbor cell in FR1	1888

A.6.6.7.1.1	Test Purpose and Environment	1888

A.6.6.7.1.2	Test Parameters	1888

A.6.6.7.1.3	Test Requirements	1891

A.6.6.7.2	Identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR SA	1891

A.6.6.7.2.1	Test Purpose and Environment	1891

A.6.6.7.2.2	Test Requirements	1894

A.6.6.8	L1-SINR measurement for beam reporting	1895

A.6.6.8.1	L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured when DRX is used	1895

A.6.6.8.1.1	Test Purpose and Environment	1895

A.6.6.8.2	L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is not used	1898

A.6.6.8.2.1	Test Purpose and Environment	1898

A.6.6.8.2.2	Test parameters	1899

A.6.6.8.2.3	Test Requirements	1903

A.6.6.8.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is not used	1903

A.6.6.8.3.1	Test Purpose and Environment	1903

A.6.6.8.3.2	Test parameters	1904

A.6.6.8.3.3	Test Requirements	1907

A.6.6.9	Idle Mode CA/DC Measurements	1907

A.6.6.9.1	SA Idle mode CA/DC measurement for FR1	1907

A.6.6.9.1.1	Test Purpose and Environment	1907

A.6.6.9.1.2	Test Requirements	1914

A.6.6.10	CSI-RS based intra-frequency Measurements	1914

A.6.6.10.1	SA event triggered reporting tests without gap under non-DRX	1914

A.6.6.10.1.1	Test purpose and Environment	1914

A.6.6.10.1.2	Test Requirements	1918

A.6.6.11	CSI-RS based inter-frequency Measurements	1918

A.6.6.11.1	 SA event triggered reporting tests with gap under DRX	1918

A.6.6.11.1.1	Test Purpose and Environment	1918

A.6.6.11.1.2	Test Requirements	1922

A.6.6.12	RSTD measurements	1922

A. 6.6.12.1	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA	1922

A. 6.6.12.1.1	Test Purpose and Environment	1922

A.6.6.12.1.2	Test Requirements	1930

A. 6.6.12.2	NR RSTD measurement reporting delay test case for dual positioning frequency layers in FR1 SA	1930

A. 6.6.12.2.1	Test Purpose and Environment	1930

A.6.6.12.2.2	Test Requirements	1937

A.6.6.13 PRS-RSRP measurements	1937

A.6.6.13.1	PRS-RSRP reporting delay test case for single positioning frequency layer	1937

A.6.6.13.1.1	Test purpose and Environment	1937

A.6.6.13.1.2	Test Requirements	1941

A.6.6.13.2	PRS-RSRP reporting delay test case for dual positioning frequency layer	1941

A.6.6.13.2.1	Test purpose and Environment	1941

A.6.6.13.2.2	Test Requirements	1945

A.6.6.14	UE Rx-Tx time difference measurements	1945

A.6.6.14.1 UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA	1945

A.6.6.14.1.1	Test purpose and environment	1945

A.6.6.14.1.2	Test requirements	1949

A.6.6.14.2 UE Rx-Tx time difference measurement for dual positioning frequency layers in FR1 SA	1949

A.6.6.14.2.1	Test purpose and environment	1949

A.6.6.14.2.2	Test requirements	1953

A.6.6.15	Idle Mode measurements of inter-RAT DC candidate cells for early reporting	1953

A.6.6.15.1	Test Purpose and Environment	1953

A.6.6.15.2	Test Requirements	1961

A.6.7	Measurement Performance requirements	1962

A.6.7.1	SS-RSRP	1962

A.6.7.1.1	SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell	1962

A.6.7.1.1.1	Test Purpose and Environment	1962

A.6.7.1.1.2	Test parameters	1962

A.6.7.1.1.3	Test Requirements	1967

A.6.7.1.2	SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell	1967

A.6.7.1.2.1	Test Purpose and Environment	1967

A.6.7.1.2.2	Test parameters	1967

A.6.7.1.2.3	Test Requirements	1971

A.6.7.1.3	Void	1971

A.6.7.2	SS-RSRQ	1971

A.6.7.2.1	SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1971

A.6.7.2.1.1	Test Purpose and Environment	1971

A.6.7.2.1.2	Test Parameters	1972

A.6.7.2.1.3	Test Requirements	1977

A.6.7.2.2	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1977

A.6.7.2.2.1	Test Purpose and Environment	1977

A.6.7.2.2.2	Test Parameters	1977

A.6.7.2.2.3	Test Requirements	1982

A.6.7.3	SS-SINR	1982

A.6.7.3.1	SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1982

A.6.7.3.1.1	Test Purpose and Environment	1982

A.6.7.3.1.2	Test Parameters	1982

A.6.7.3.1.3	Test Requirements	1986

A.6.7.3.2	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1986

A.6.7.3.2.1	Test Purpose and Environment	1986

A.6.7.3.2.2	Test Parameters	1987

A.6.7.3.2.3	Test Requirements	1991

A.6.7.4	L1-RSRP measurement for beam reporting	1992

A.6.7.4.1	SSB based L1-RSRP measurement	1992

A.6.7.4.1.1	Test Purpose and Environment	1992

A.6.7.4.1.2	Test parameters	1992

A.6.7.4.1.3	Test Requirements	1996

A.6.7.4.2	CSI-RS based L1-RSRP measurement on resource set with repetition off	1996

A.6.7.4.2.1	Test Purpose and Environment	1996

A.6.7.4.2.2	Test parameters	1997

A.6.7.4.2.3	Test Requirements	2001

A.6.7.5	E-UTRAN RSRP	2001

A.6.7.5.1	SA: inter-RAT measurement accuracy with FR1 serving cell	2001

A.6.7.5.1.1	Test Purpose and Environment	2001

A.6.7.5.1.2	Test parameters	2002

A.6.7.5.1.3	Test Requirements	2008

A.6.7.6	E-UTRAN RSRQ	2009

A.6.7.6.1	SA: inter-RAT measurement accuracy with FR1 serving cell	2009

A.6.7.6.1.1	Test Purpose and Environment	2009

A.6.7.6.1.2	Test parameters	2009

A.6.7.6.1.3	Test Requirements	2014

A.6.7.7	E-UTRAN RS-SINR	2015

A.6.7.7.1	SA: inter-RAT measurement accuracy with FR1 serving cell	2015

A.6.7.7.1.1	Test Purpose and Environment	2015

A.6.7.7.1.2	Test parameters	2015

A.6.7.7.1.3	Test Requirements	2021

A.6.7.8	CLI measurements	2022

A.6.7.8.1	SA SRS-RSRP measurement accuracy with FR1 serving cell	2022

A.6.7.8.1.1	Test Purpose and Environment	2022

A.6.7.8.1.2	Test parameters	2022

A.6.7.8.1.3	Test Requirements	2028

A.6.7.8.2	SA CLI-RSSI measurement accuracy with FR1 serving cell	2028

A.6.7.8.2.1	Test Purpose and Environment	2028

A.6.7.8.2.2	Test parameters	2029

A.6.7.8.2.3	Test Requirements	2032

A.6.7.9	L1-SINR measurement for beam reporting	2033

A.6.7.9.1	L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured and CSI-RS resource set with repetition off	2033

A.6.7.9.1.1	Test Purpose and Environment	2033

A.6.7.9.1.2	Test parameters	2033

A.6.7.9.1.3	Test Requirements	2037

A.6.7.9.2	L1-SINR measurement with SSB based CMR and dedicated IMR	2037

A.6.7.9.2.1	Test Purpose and Environment	2037

A.6.7.9.2.2	Test parameters	2038

A.6.7.9.2.3	Test Requirements	2043

A.6.7.9.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR	2043

A.6.7.9.3.1	Test Purpose and Environment	2043

A.6.7.9.3.2	Test parameters	2043

A.6.7.9.3.3	Test Requirements	2048

A.6.7.10	CSI-RSRP	2048

A.6.7.10.1	SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell	2048

A.6.7.10.1.1	Test Purpose and Environment	2048

A.6.7.10.1.2	Test parameters	2049

A.6.7.10.1.3	Test Requirements	2054

A.6.7.10.2	SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell	2054

A.6.7.10.2.1	Test Purpose and Environment	2054

A.6.7.10.2.2	Test parameters	2054

A.6.7.10.2.3	Test Requirements	2060

A.6.7.11	CSI-RSRQ	2060

A.6.7.11.1	SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2060

A.6.7.11.1.1	Test Purpose and Environment	2060

A.6.7.11.1.2	Test Parameters	2060

A.6.7.11.1.3	Test Requirements	2065

A.6.7.11.2	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2065

A.6.7.11.2.1	Test Purpose and Environment	2065

A.6.7.11.2.2	Test Parameters	2065

A.6.7.11.2.3	Test Requirements	2070

A.6.7.12	CSI-SINR	2070

A.6.7.12.1	SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2070

A.6.7.12.1.1	Test Purpose and Environment	2070

A.6.7.12.1.2	Test Parameters	2071

A.6.7.12.1.3	Test Requirements	2076

A.6.7.12.2	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2076

A.6.7.12.2.1	Test Purpose and Environment	2076

A.6.7.12.2.2	Test Parameters	2076

A.6.7.12.2.3	Test Requirements	2082

A.6.7.13	RSTD measurements	2082

A.6.7.13.1	RSTD measurement accuracy test case for single positioning frequency layer	2082

A.6.7.13.1.1	Test purpose and Environment	2082

A.6.7.13.1.2	Test Requirements	2085

A.6.7.13.2	RSTD measurement accuracy test case for dual positioning frequency layer	2085

A.6.7.13.2.1	Test purpose and Environment	2085

A.6.7.13.2.2	Test Requirements	2089

A.6.7.14	PRS-RSRP measurements	2089

A.6.7.14.1	SA: measurement accuracy with PRS in FR1	2089

A.6.7.14.1.1	Test Purpose and Environment	2089

A.6.7.14.1.2	Test parameters	2090

A.6.7.14.1.3	Test Requirements	2094

A.6.7.15	UE Rx-Tx time difference measurements	2094

A.6.7.15.1 UE Rx-Tx time difference measurement accuracy for single positioning frequency layer in FR1 SA	2094

A.6.7.15.1.1	Test purpose and environment	2094

A.6.7.15.1.2	Test parameters	2095

A.6.7.15.1.3	Test requirements	2098

A.7	NR standalone tests with one or more NR cells in FR2	2099

A.7.1	SA: RRC\_IDLE state mobility	2099

A.7.1.1	Cell re-selection to NR	2099

A.7.1.1.1	Cell reselection to FR2 intra-frequency NR case	2099

A.7.1.1.1.1	Test Purpose and Environment	2099

A.7.1.1.1.2	Test Parameters	2099

A.7.1.1.1.3	Test Requirements	2102

A.7.1.1.2	Cell reselection to FR2 inter-frequency NR case	2103

A.7.1.1.2.1	Test Purpose and Environment	2103

A.7.1.1.2.2	Test Parameters	2103

A.7.1.1.2.3	Test Requirements	2105

A.7.1.1.3	Cell reselection to FR2 intra-frequency NR case for UE fulfilling low mobility relaxed measurement criterion	2106

A.7.1.1.3.1	Test Purpose and Environment	2106

A.7.1.1.3.2	Test Parameters	2106

A.7.1.1.3.3	Test Requirements	2109

A.7.1.1.4	Cell reselection to FR2 intra-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion	2109

A.7.1.1.4.1	Test Purpose and Environment	2109

A.7.1.1.4.2	Test Parameters	2109

A.7.1.1.4.3	Test Requirements	2112

A.7.1.1.5	Cell reselection to FR2 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion	2112

A.7.1.1.5.1	Test Purpose and Environment	2112

A.7.1.1.5.2	Test Parameters	2112

A.7.1.1.5.3	Test Requirements	2115

A.7.1.1.6	Cell reselection to FR2 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion	2115

A.7.1.1.6.1	Test Purpose and Environment	2115

A.7.1.1.6.2	Test Parameters	2115

A.7.1.1.6.3	Test Requirements	2118

A.7.2	SA: RRC\_INACTIVE state mobility	2118

A.7.3	RRC\_CONNECTED state mobility	2118

A.7.3.1	Handover	2118

A.7.3.1.1	Inter-frequency handover from FR1 to FR2; unknown target cell	2118

A.7.3.1.1.1	Test Purpose and Environment	2118

A.7.3.1.1.2	Test Parameters	2118

A.7.3.1.1.3	Test Requirements	2122

A.7.3.1.2	Intra-frequency handover from FR2 to FR2; unknown target cell	2122

A.7.3.1.2.1	Test Purpose and Environment	2122

A.7.3.1.2.2	Test Parameters	2122

A.7.3.1.2.3	Test Requirements	2125

A.7.3.1.3	Inter-frequency handover from FR2 to FR2; unknown target cell	2125

A.7.3.1.3.1	Test Purpose and Environment	2125

A.7.3.1.3.2	Test Parameters	2125

A.7.3.1.3.3 Test Requirements	2126

A.7.3.1.4	Inter-band inter-frequency synchronous DAPS handover from FR1 to FR2	2127

A.7.3.1.4.1	Test Purpose and Environment	2127

A.7.3.1.4.2	Test Parameters	2127

A.7.3.1.4.3 Test Requirements	2134

A.7.3.1.5	Inter-band inter-frequency asynchronous DAPS handover from FR1 to FR2	2134

A.7.3.1.5.1	Test Purpose and Environment	2134

A.7.3.1.5.2	Test Parameters	2134

A.7.3.1.5.3 Test Requirements	2141

A.7.3.2	RRC Connection Mobility Control	2141

A.7.3.2.1	SA: RRC Re-establishment	2141

A.7.3.2.1.1	Intra-frequency RRC Re-establishment in FR2	2141

A.7.3.2.1.2	Inter-frequency RRC Re-establishment in FR2	2144

A.7.3.2.1.3	Intra-frequency RRC Re-establishment in FR2 without serving cell timing	2147

A.7.3.2.1.3.1	Test Purpose and Environment	2147

A.7.3.2.1.3.2	Test Requirements	2149

A.7.3.2.2	Random Access	2150

A.7.3.2.2.1	4-step RA type contention based random access test in FR2 for NR Standalone	2150

A.7.3.2.2.2	4-step RA type non-contention based random access test in FR2 for NR Standalone	2154

A.7.3.2.2.3	2-step RA type contention based random access test in FR2 for NR Standalone	2159

A.7.3.2.2.4	2-step RA type non-contention based random access test in FR2 for NR Standalone	2162

A.7.3.2.3	SA: RRC Connection Release with Redirection	2165

A.7.3.2.3.1	Redirection from NR in FR2 to NR in FR2	2165

A.7.3.3	Conditional Handover	2169

A.7.3.3.1	Intra-frequency conditional handover from FR2 to FR2	2169

A.7.3.3.1.1	Test Purpose and Environment	2169

A.7.3.3.1.2	Test Parameters	2169

A.7.3.3.1.2.3	Test Requirements	2172

A.7.3.3.2	Inter-frequency conditional handover from FR2 to FR2; unknown target cell	2172

A.7.3.3.2.1	Test Purpose and Environment	2172

A.7.3.3.2.2	Test Parameters	2172

A.7.3.3.2.3 Test Requirements	2175

A.7.4	Timing	2175

A.7.4.1	UE transmit timing	2175

A.7.4.1.1	NR UE Transmit Timing Test for FR2	2175

A.7.4.1.1.1	Test Purpose and environment	2175

A.7.4.1.1.2	Test requirements	2178

A.7.4.2	UE timer accuracy	2179

A.7.4.3	Timing advance	2179

A.7.4.3.1	SA FR2 timing advance adjustment accuracy	2179

A.7.4.3.1.1	Test Purpose and Environment	2179

A.7.4.3.1.2	Test Parameters	2179

A.7.4.3.1.3 Test Requirements	2182

A.7.5	Signaling characteristics	2183

A.7.5.1	Radio link Monitoring	2183

A.7.5.1.1	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode	2183

A.7.5.1.1.1	Test Purpose and Environment	2183

A.7.5.1.1.2	Test Requirements	2186

A.7.5.1.2	Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode	2187

A.7.5.1.2.1	Test Purpose and Environment	2187

A.7.5.1.2.2	Test Requirements	2191

A.7.5.1.3	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode	2192

A.7.5.1.3.1	Test Purpose and Environment	2192

A.7.5.1.3.2	Test Requirements	2196

A.7.5.1.4	Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode	2196

A.7.5.1.4.1	Test Purpose and Environment	2196

A.7.5.1.4.2	Test Requirements	2201

A.7.5.1.5	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode	2201

A.7.5.1.5.1	Test Purpose and Environment	2201

A.7.5.1.5.2	Test Requirements	2206

A.7.5.1.6	Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode	2206

A.7.5.1.6.1	Test Purpose and Environment	2206

A.7.5.1.6.2	Test Requirements	2210

A.7.5.1.7	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode	2210

A.7.5.1.7.1	Test Purpose and Environment	2210

A.7.5.1.7.2	Test Requirements	2214

A.7.5.1.8	Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode	2214

A.7.5.1.8.1	Test Purpose and Environment	2214

A.7.5.1.8.2	Test Requirements	2219

A.7.5.1.9	UE Radio Link Monitoring Scheduling Restrictions on FR2	2219

A.7.5.1.9.1	Test Purpose and Environment	2219

A.7.5.1.9.2	Test Requirements	2222

A.7.5.2	Interruption	2222

A.7.5.2.1	Interruptions during measurements on deactivated NR SCC in FR2	2222

A.7.5.2.2	SA interruptions at NR SRS carrier-based switching	2226

A.7.5.2.2.1	Test Purpose and Environment	2226

A.7.5.2.2.2	Test Parameters	2226

A.7.5.2.2.3	Test Requirements	2228

A.7.5.3	SCell Activation and Deactivation Delay	2228

A.7.5.3.1	SCell Activation and deactivation for SCell in FR2 intra-band in non-DRX	2228

A.7.5.3.1.1	Test Purpose and Environment	2228

A.7.5.3.1.2	Test Requirements	2230

A.7.5.3.2	SCell Activation and deactivation for FR1+FR2 inter-band with target SCell in FR2	2230

A.7.5.3.2.1	Test Purpose and Environment	2230

A.7.5.3.2.2	Test Requirements	2234

A.7.5.3.3	SCell Activation and deactivation for SCell in FR2 inter-band in non-DRX	2235

A.7.5.3.3.1	Test Purpose and Environment	2235

A.7.5.3.3.2	Test Requirements	2238

A.7.5.3.4	Direct SCell activation at SCell addition of known SCell in FR2	2239

A.7.5.3.4.1	Test Purpose and Environment	2239

A.7.5.3.4.2	Test Requirements	2242

A.7.5.3.5	Direct SCell activation at handover with known SCell in FR2	2243

A.7.5.3.5.1	Test Purpose and Environment	2243

A.7.5.3.5.2	Test Requirements	2246

A.7.5.4	Void	2247

A.7.5.5	Beam Failure Detection and Link recovery procedures	2247

A.7.5.5.1	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode	2247

A.7.5.5.1.1	Test Purpose and Environment	2247

A.7.5.5.1.2	Test Requirements	2251

A.7.5.5.2	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in DRX mode	2252

A.7.5.5.2.1	Test Purpose and Environment	2252

A.7.5.5.2.2	Test Requirements	2255

A.7.5.5.3	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode	2256

A.7.5.5.3.1	Test Purpose and Environment	2256

A.7.5.5.3.2	Test Requirements	2260

A.7.5.5.4	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode	2261

A.7.5.5.4.1	Test Purpose and Environment	2261

A.7.5.5.4.2	Test Requirements	2265

A.7.5.5.5	Scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode	2266

A.7.5.5.5.1	Test Purpose and Environment	2266

A.7.5.5.5.2	Test Requirements	2269

A.7.5.5.6	Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in non-DRX mode	2270

A.7.5.5.6.1	Test Purpose and Environment	2270

A.7.5.5.6.2	Test Requirements	2274

A.7.5.5.7	Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in DRX mode	2275

A.7.5.5.7.1	Test Purpose and Environment	2275

A.7.5.5.7.2	Test Requirements	2279

A.7.5.6	Active BWP switch	2280

A.7.5.6.1	DCI-based and Timer-based Active BWP Switch	2280

A.7.5.6.1.1	NR FR2- NR FR2 DL active BWP switch of SCell with non-DRX in SA	2280

A.7.5.6.1.2	NR FR1- NR FR2 DL active BWP switch of SCell with non-DRX in SA A.7.5.6.1.2.1 Test Purpose and Environment	2284

A.7.5.6.1.3	NR FR2 DL active BWP switch with non-DRX in SA	2289

A.7.5.6.1.3.1	Test Purpose and Environment	2289

A.7.5.6.1.3.2	Test Requirements	2292

A.7.5.6.2	RRC-based Active BWP Switch	2292

A.7.5.6.3	Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs	2296

A.7.5.6.3.1	Active BWP switch on multiple SCells with non-DRX in SA	2296

A.7.5.6.4	SCell dormancy switch	2299

A.7.5.6.4.1	NR FR2 PCell SCell dormancy switch of single FR2 SCell inside active time	2299

A.7.5.6.4.2	NR FR1 PCell SCell dormancy switch of two FR2 SCells outside active time	2304

A.7.5.6.4.2.2	 Test Requirements	2309

A.7.5.6.5	Simultaneous RRC-based Active BWP Switch on multiple CCs	2309

A.7.5.6.5.1	Active BWP switch on multiple SCells with non-DRX in SA	2309

A.7.5.7	PSCell addition and release delay	2312

A.7.5.7.1	Addition and Release Delay of known NR PSCell	2312

A.7.5.7.1.1	Test Purpose and Environment	2312

A.7.5.7.2	Addition and Release Delay of unknown NR PSCell	2316

A.7.5.7.2.1	Test Purpose and Environment	2316

A.7.5.7.2.2	Test Requirements	2319

A.7.5.8	Active TCI state switch delay	2319

A.7.5.8.1	MAC-CE based active TCI state switch	2319

A.7.5.8.2	RRC based active TCI state switch	2323

A.7.5.9	Uplink spatial relation switch delay	2327

A.7.5.9.1	MAC-CE based Spatial Relation switch	2327

A.7.5.9.1.1	 NR PCell FR2 spatial relation associated with known DL-RS	2327

A.7.5.9.1.1.2	Test Requirements	2330

A.7.5.9.2	RRC based spatial relation switch	2330

A.7.5.9.2.1	NR PCell FR2 spatial relation switch associated with a known DL-RS	2330

A.7.5.9.2.1.1	Test Purpose and Environment	2330

A.7.5.9.2.1.2	Test Requirements	2333

A.7.5.10	UE specific CBW change	2333

A.7.5.10.1	NR FR2 UE specific CBW change of PCell with non-DRX in SA	2333

A.7.5.10.1.1	Test Purpose and Environment	2333

A.7.5.10.1.2	Test Requirements	2336

A.7.6	Measurement procedure	2337

A.7.6.1	Intra-frequency Measurements	2337

A.7.6.1.1	SA event triggered reporting test without gap under non-DRX	2337

A.7.6.1.1.1	Test purpose and Environment	2337

A.7.6.1.1.2	Test Requirements	2339

A.7.6.1.2	SA event triggered reporting test without gap under DRX	2340

A.7.6.1.2.1	Test purpose and Environment	2340

A.7.6.1.2.2	Test Requirements	2342

A.7.6.1.3	SA event triggered reporting test with per-UE gaps under non-DRX	2343

A.7.6.1.3.1	Test purpose and Environment	2343

A.7.6.1.3.2	Test Requirements	2345

A.7.6.1.4	SA event triggered reporting test with per-UE gaps under DRX	2346

A.7.6.1.4.1	Test purpose and Environment	2346

A.7.6.1.4.2	Test Requirements	2349

A.7.6.2	Inter-frequency Measurements	2350

A.7.6.2.1	SA event triggered reporting tests For FR2 without SSB time index detection when DRX is not used (PCell in FR2)	2350

A.7.6.2.1.1	Test Purpose and Environment	2350

A.7.6.2.1.2	Test Requirements	2353

A.7.6.2.2	SA event triggered reporting tests For FR2 without SSB time index detection when DRX is used (PCell in FR2)	2353

A.7.6.2.2.1	Test Purpose and Environment	2353

A.7.6.2.2.2	Test Requirements	2357

A.7.6.2.3	SA event triggered reporting tests For FR2 with SSB time index detection when DRX is not used (PCell in FR2)	2357

A.7.6.2.3.1	Test Purpose and Environment	2357

A.7.6.2.3.2	Test Requirements	2361

A.7.6.2.4	SA event triggered reporting tests For FR2 with SSB time index detection when DRX is used (PCell in FR2)	2361

A.7.6.2.4.1	Test Purpose and Environment	2361

A.7.6.2.4.2	Test Requirements	2365

A.7.6.2.5	SA event triggered reporting tests for FR2 without SSB time index detection when DRX is not used (PCell in FR1)	2365

A.7.6.2.5.1	Test Purpose and Environment	2365

A.7.6.2.5.2	Test Requirements	2369

A.7.6.2.6	SA event triggered reporting tests for FR2 without SSB time index detection when DRX is used (PCell in FR1)	2370

A.7.6.2.6.1	Test Purpose and Environment	2370

A.7.6.2.6.2	Test Requirements	2374

A.7.6.2.7	SA event triggered reporting tests for FR2 with SSB time index detection when DRX is not used (PCell in FR1)	2375

A.7.6.2.7.1	Test Purpose and Environment	2375

A.7.6.2.7.2	Test Requirements	2379

A.7.6.2.8	SA event triggered reporting tests for FR2 with SSB time index detection when DRX is used (PCell in FR1)	2380

A.7.6.2.8.1	Test Purpose and Environment	2380

A.7.6.2.8.2	Test Requirements	2384

A.7.6.2.9	SA event triggered reporting tests For FR2 without SSB time index detection when DRX is not used (PCell in FR2) (rel16 additional mandatory gap pattern 17)	2385

A.7.6.2.9.1	Test Purpose and Environment	2385

A.7.6.2.9.2	Test Requirements	2388

A.7.6.2.10	SA event triggered reporting test without gap under non-DRX	2388

A.7.6.2.10.1	Test Purpose and Environment	2388

A.7.6.2.10.2	Test Requirements	2390

A.7.6.2.11	SA event triggered reporting test without gap under DRX	2390

A.7.6.2.11.1	Test Purpose and Environment	2390

A.7.6.2.11.2	Test Requirements	2393

A.7.6.3	L1-RSRP measurement for beam reporting	2394

A.7.6.3.1	SSB based L1-RSRP measurement when DRX is not used	2394

A.7.6.3.1	SSB based L1-RSRP measurement when DRX is not used	2394

A.7.6.3.1.1	Test Purpose and Environment	2394

A.7.6.3.1.2	Test parameters	2394

A.7.6.3.1.3	Test Requirements	2396

A.7.6.3.2	SSB based L1-RSRP measurement when DRX is used	2396

A.7.6.3.2.1	Test Purpose and Environment	2396

A.7.6.3.2.2	Test parameters	2397

A.7.6.3.2.3	Test Requirements	2399

A.7.6.3.3	CSI-RS based L1-RSRP measurement when DRX is not used	2399

A.7.6.3.3.1	Test Purpose and Environment	2399

A.7.6.3.3.2	Test parameters	2400

A.7.6.3.3.3	Test Requirements	2402

A.7.6.3.4	CSI-RS based L1-RSRP measurement when DRX is used	2403

A.7.6.3.4.1	Test Purpose and Environment	2403

A.7.6.3.4.2	Test parameters	2403

A.7.6.3.3.3	Test Requirements	2405

A.7.6.4	CLI measurements	2406

A.7.6.4.1	SRS-RSRP measurement with non-DRX	2406

A.7.6.4.1.1	Test Purpose and Environment	2406

A.7.6.4.1.2	Test Parameters	2406

A.7.6.4.1.3	Test Requirements	2408

A.7.6.4.2	CLI-RSSI measurement with non-DRX	2408

A.7.6.4.2.1	Test Purpose and Environment	2408

A.7.6.4.2.2	Test Parameters	2409

A.7.6.4.2.3	Test Requirements	2410

A.7.6.5	NR Measurements with autonomous gaps	2411

A.7.6.5.1	SA interfrequency CGI reporting in autonomous gaps test (PCell in FR2)	2411

A.7.6.5.1.1	Test Purpose and Environment	2411

A.7.6.5.1.2	Test Requirements	2414

A.7.6.6	L1-SINR measurement for beam reporting	2414

A.7.6.6.1	L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured when DRX is not used	2414

A.7.6.6.1.1	Test Purpose and Environment	2414

A.7.6.6.1.2	Test parameters	2414

A.7.6.6.1.3	Test Requirements	2416

A.7.6.6.2	L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is used	2416

A.7.6.6.2.1	Test Purpose and Environment	2416

A.7.6.6.2.2	Test parameters	2417

A.7.6.6.2.3	Test Requirements	2419

A.7.6.6.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is used	2419

A.7.6.6.3.1	Test Purpose and Environment	2419

A.7.6.6.3.2	Test parameters	2420

A.7.6.6.3.3	Test Requirements	2422

A.7.6.7	CSI-RS based intra-frequency Measurements	2422

A.7.6.7.1	SA event triggered reporting test without gap under DRX for CSI-RS based intra-frequency measurement	2422

A.7.6.7.1.1	Test purpose and Environment	2422

A.7.6.7.1.2	Test Requirements	2425

A.7.6.8	CSI-RS based inter-frequency Measurements	2426

A.7.6.8.1	SA event triggered reporting tests for FR2 CSI-RS based measurement when non-DRX is used (PCell in FR2)	2426

A.7.6.8.1.1	Test Purpose and Environment	2426

A.7.6.2.2.2	Test Requirements	2430

A.7.6.9	RSTD measurements	2430

A.7.6.9.1	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA	2430

A.7.6.9.1.1	Test Purpose and Environment	2430

A.7.6.9.1.2	Test Requirements	2436

A.7.6.9.2	 NR RSTD measurement reporting delay test case for dual positioning frequency layers in FR2 SA	2436

A.7.6.9.2.1	Test Purpose and Environment	2436

A.7.6.9.2.2	Test Requirements	2443

A.7.6.10 PRS-RSRP measurements	2443

A.7.6.10.1 PRS-RSRP reporting delay test case for single positioning frequency layer	2443

A.7.6.10.1.1	Test Purpose and Environment	2443

A.7.6.10.1.2	Test Requirements	2447

A.7.6.10.2 PRS-RSRP reporting delay test case for dual positioning frequency layer	2447

A.7.6.10.2.1	Test Purpose and Environment	2447

A.7.6.10.2.2	Test Requirements	2450

A.7.6.11	UE Rx-Tx time difference measurements	2450

A.7.6.11.1 UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA	2450

A.7.6.11.1.1	Test purpose and environment	2450

A.7.6.11.1.2	Test requirements	2454

A.7.6.11.2 UE Rx-Tx time difference measurement period for dual positioning frequency layers in FR2 SA	2454

A.7.6.11.2.1	Test purpose and environment	2454

A.7.6.11.2.2	Test requirements	2458

A.7.7	Measurement Performance requirements	2458

A.7.7.1	SS-RSRP	2459

A.7.7.1.1	SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	2459

A.7.7.1.1.1	Test Purpose and Environment	2459

A.7.7.1.1.2	Test parameters	2459

A.7.7.1.1.3	Test Requirements	2463

A.7.7.1.2	SA inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	2463

A.7.7.1.2.1	Test Purpose and Environment	2463

A.7.7.1.2.2	Test parameters	2464

A.7.7.1.2.3	Test Requirements	2468

A.7.7.1.3	SA inter-frequency measurement accuracy with FR1 serving cell and FR2 target cell	2469

A.7.7.1.3.1	Test Purpose and Environment	2469

A.7.7.1.3.2	Test parameters	2469

A.7.7.1.3.3	Test Requirements	2473

A.7.7.2	SS-RSRQ	2473

A.7.7.2.1	SA intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell	2473

A.7.7.2.1.1	Test Purpose and Environment	2473

A.7.7.2.1.2	Test Parameters	2473

A.7.7.2.1.3	Test Requirements	2475

A.7.7.2.2	SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	2475

A.7.7.2.2.1	Test Purpose and Environment	2475

A.7.7.2.2.2	Test Parameters	2475

A.7.7.2.2.3	Test Requirements	2477

A.7.7.3	SS-SINR	2477

A.7.7.3.1	SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	2477

A.7.7.3.1.1	Test Purpose and Environment	2477

A.7.7.3.1.2	Test Parameters	2477

A.7.7.3.1.3	Test Requirements	2480

A.7.7.3.2	SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	2480

A.7.7.3.2.1	Test Purpose and Environment	2480

A.7.7.3.2.2	Test Parameters	2480

A.7.7.3.2.3	Test Requirements	2482

A.7.7.4	L1-RSRP measurement for beam reporting	2482

A.7.7.4.1	SSB based L1-RSRP measurement	2482

A.7.7.4.1.1	Test Purpose and Environment	2482

A.7.7.4.1.2	Test parameters	2483

A.7.7.4.1.3	Test Requirements	2485

A.7.7.4.2	CSI-RS based L1-RSRP measurement on resource set with repetition off	2486

A.7.7.4.2.1	Test Purpose and Environment	2486

A.7.7.4.2.2	Test parameters	2486

A.7.7.4.2.3	Test Requirements	2488

A.7.7.5	CLI measurements	2489

A.7.7.5.1	SA SRS-RSRP measurement accuracy with FR2 serving cell	2489

A.7.7.5.1.1	Test Purpose and Environment	2489

A.7.7.5.1.2	Test parameters	2489

A.7.7.5.1.3	Test Requirements	2492

A.7.7.5.2	SA CLI-RSSI measurement accuracy with FR2 serving cell	2493

A.7.7.5.2.1	Test Purpose and Environment	2493

A.7.7.5.2.2	Test parameters	2493

A.7.7.5.2.3	Test Requirements	2495

A.7.7.6	L1-SINR measurement for beam reporting	2496

A.7.7.6.1	L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured and CSI-RS resource set with repetition off	2496

A.7.7.6.1.1	Test Purpose and Environment	2496

A.7.7.6.1.2	Test parameters	2496

A.7.7.6.1.3	Test Requirements	2498

A.7.7.6.2	L1-SINR measurement with SSB based CMR and dedicated IMR	2499

A.7.7.6.2.1	Test Purpose and Environment	2499

A.7.7.6.2.2	Test parameters	2499

A.7.7.6.2.3	Test Requirements	2501

A.7.7.6.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR	2502

A.7.7.6.3.1	Test Purpose and Environment	2502

A.7.7.6.3.2	Test parameters	2502

A.7.7.6.3.3	Test Requirements	2504

A.7.7.7	CSI-RSRP	2505

A.7.7.7.1	SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	2505

A.7.7.7.1.1	Test Purpose and Environment	2505

A.7.7.7.1.2	Test parameters	2505

A.7.7.7.1.3	Test Requirements	2510

A.7.7.7.2	SA inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	2510

A.7.7.7.2.1	Test Purpose and Environment	2510

A.7.7.7.2.2	Test parameters	2511

A.7.7.7.2.3	Test Requirements	2515

A.7.7.8	CSI-RSRQ	2516

A.7.7.8.1	SA intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell	2516

A.7.7.8.1.1	Test Purpose and Environment	2516

A.7.7.8.1.2	Test Parameters	2516

A.7.7.8.1.3	Test Requirements	2518

A.7.7.8.2	SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	2518

A.7.7.8.2.1	Test Purpose and Environment	2518

A.7.7.8.2.2	Test Parameters	2519

A.7.7.8.2.3	Test Requirements	2520

A.7.7.9	CSI-SINR	2520

A.7.7.9.1	SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	2520

A.7.7.9.1.1	Test Purpose and Environment	2520

A.7.7.9.1.2	Test Parameters	2521

A.7.7.9.1.3	Test Requirements	2523

A.7.7.9.2	SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	2523

A.7.7.9.2.2	Test Parameters	2524

A.7.7.9.2.3	Test Requirements	2525

A.7.7.10	RSTD measurements	2526

A.7.7.10.1	RSTD measurement accuracy test case for single positioning frequency layer	2526

A.7.7.10.1.1	Test purpose and Environment	2526

A.7.7.10.1.2	Test Requirements	2528

A.7.7.10.2	RSTD measurement accuracy test case for dual positioning frequency layer	2528

A.7.7.10.2.1	Test purpose and Environment	2528

A.7.7.10.2.2	Test Requirements	2531

A.7.7.11	PRS-RSRP measurements	2531

A.7.7.11.1	SA measurement accuracy with PRS in FR2	2531

A.7.7.11.1.1	Test Purpose and Environment	2531

A.7.7.11.1.2	Test parameters	2531

A.7.7.11.1.3	Test Requirements	2535

A.7.7.12	UE Rx-Tx time difference measurements	2536

A.7.7.12.1 UE Rx-Tx time difference measurement accuracy for single positioning frequency layer in FR2 SA	2536

A.7.7.12.1.1	Test purpose and environment	2536

A.7.7.12.1.2	Test parameters	2536

A.7.7.12.1.3	Test requirements	2539

A.8	E-UTRA standalone tests for NR RRM	2540

A.8.1	Void	2540

A.8.2	RRC\_IDLE state mobility	2540

A.8.2.1	Inter-RAT NR Cell re-selection	2540

A.8.2.1.1	E-UTRA Cell reselection to higher priority NR target Cell in FR1	2540

A.8.2.1.1.1	Test Purpose and Environment	2540

A.8.2.1.1.2	Test Requirements	2545

A.8.2.1.2	E-UTRA Cell reselection to lower priority NR target Cell in FR1 for UE configured with highSpeedInterRAT-NR-r16	2546

A.8.2.1.2.1	Test Purpose and Environment	2546

A.8.2.1.2.2	Test Requirements	2551

A.8.2.2	E-UTRA – NR Inter-RAT Early Measruement Reporting	2552

A.8.2.2.1	E-UTRA – NR Early Measurement Reporting for NR in FR1	2552

A.8.2.2.1.1	Test Purpose and Environment	2552

A.8.2.2.1.2	Test Requirements	2557

A.8.2.2.2	E-UTRA – NR Early Measurement Reporting for NR in FR2	2557

A.8.2.2.2.1	Test Purpose and Environment	2557

A.8.2.2.2.2	Test Requirements	2560

A.8.3	RRC\_CONNECTED state mobility	2561

A.8.3.1	Handover	2561

A.8.3.1.1	E-UTRAN - NR handover in FR1	2561

A.8.3.1.1.1	Test Purpose and Environment	2561

A.8.3.1.1.2	Test Requirements	2566

A.8.4	Measurement procedure	2566

A.8.4.1	E-UTRA – NR Inter-RAT SFTD Measurement Delay	2566

A.8.4.1.1	E-UTRA – NR Inter-RAT SFTD Measurement Delay in non-DRX	2566

A.8.4.1.1.1	Test Purpose and Environment	2566

A.8.4.1.1.2	Test Requirements	2568

A.8.4.1.2	E-UTRA – NR Inter-RAT SFTD Measurement Delay in DRX	2569

A.8.4.1.2.1	Test Purpose and Environment	2569

A.8.4.1.2.2	Test Requirements	2570

A.8.4.2	E-UTRA – NR Inter-RAT Measurements	2570

A.8.4.2.1	NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used	2570

A.8.4.2.1.1	Test Purpose and Environment	2570

A.8.4.2.1.2	Test Requirements	2575

A.8.4.2.2	NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used	2575

A.8.4.2.2.1	Test Purpose and Environment	2575

A.8.4.2.2.2	Test Requirements	2579

A.8.4.2.3	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used	2579

A.8.4.2.3.1	Test Purpose and Environment	2579

A.8.4.2.3.2	Test Requirements	2583

A.8.4.2.4	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used	2583

A.8.4.2.4.1	Test Purpose and Environment	2583

A.8.4.2.4.2	Test Requirements	2587

A.8.4.2.5	NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is not used	2587

A.8.4.2.5.1	Test Purpose and Environment	2587

A.8.4.2.5.2	Test Requirements	2589

A.8.4.2.6	NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is used	2590

A.8.4.2.6.1	Test Purpose and Environment	2590

A.8.4.2.6.2	Test Requirements	2592

A.8.4.2.7	NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is not used	2593

A.8.4.2.7.1	Test Purpose and Environment	2593

A.8.4.2.7.2	Test Requirements	2595

A.8.4.2.8	NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is used	2596

A.8.4.2.8.1	Test Purpose and Environment	2596

A.8.4.2.8.2	Test Requirements	2598

A.8.4.2.9	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection in DRX for UE configured with highSpeedInterRAT-NR-r16	2599

A.8.4.2.9.1	Test Purpose and Environment	2599

A.8.4.2.9.2	Test Requirements	2604

A.8.5	Measurement performance	2604

A.8.5.1	SFTD accuracy	2604

A.8.5.1.1	SFTD accuracy	2604

A.8.5.1.1.1	Test Purpose	2604

A.8.5.1.1.2	Test Environment	2604

A.8.5.1.1.3	Test Requirements	2610

A.8.5.2	E-UTRA – NR Inter-RAT Measurement Performance requirements	2610

A.8.5.2.1.1	E-UTRAN – NR inter-RAT measurements with FR1 target cell	2610

A.8.5.2.1.2	E-UTRAN – NR inter-RAT measurements with FR2 target cell	2615

A.8.5.2.1.2.1	Test Purpose and Environment	2615

A.8.5.2.1.2.2	Test Parameters	2615

A.8.5.2.1.2.3	Test Requirements	2617

A.8.5.2.2	SS-RSRQ	2617

A.8.5.2.2.1	E-UTRAN – NR inter-RAT measurements with FR1 target cell	2617

A.8.5.2.2.2	E-UTRAN – NR inter-RAT measurements with FR2 target cell	2622

A.8.5.2.2.2.1	Test Purpose and Environment	2622

A.8.5.2.2.2.2	Test Parameters	2622

A.8.5.2.2.2.3	Test Requirements	2624

A.8.5.2.3	SS-SINR	2624

A.8.5.2.3.1	E-UTRAN – NR inter-RAT measurements with FR1 target cell	2624

A.8.5.2.3.2	E-UTRAN – NR inter-RAT measurements with FR2 target cell	2628

A.8.5.2.3.2.1	Test Purpose and Environment	2628

A.8.5.2.3.2.2	Test Parameters	2628

A.8.5.2.3.2.3	Test Requirements	2630

A.9	V2X Tests	2631

A.9.1	V2X Tests in FR1	2631

A.9.1.1	Test for V2X UE Transmit Timing	2631

A.9.1.1.1	Test for GNSS as Synchronization Reference Source	2631

A.9.1.1.1.1	Test Purpose and Environment	2631

A.9.1.1.1.2	Test requirements	2631

A.9.1.1.2	Test for SyncRef UE as Synchronization Reference Source	2631

A.9.1.1.2.1	Test Purpose and Environment	2631

A.9.1.1.2.2	Test requirements	2632

A.9.1.1.3	Test for FR1 NR Cell as Synchronization Reference Source	2632

A.9.1.1.3.1	Test Purpose and Environment	2632

A.9.1.1.3.2	Test requirements	2635

A.9.1.2	Test for Initiation/Cease of S-SSB Transmission with V2X Sidelink Communication	2635

A.9.1.2.1	Test for FR1 NR Cell as synchronization reference source without gap under non-DRX	2635

A.9.1.2.1.1	Test Purpose and Environment	2635

A.9.1.2.1.2	Test Requirements	2639

A.9.1.2.2	Test for SyncRef UE as synchronization reference source	2639

A.9.1.2.2.1	Test Purpose and Environment	2639

A.9.1.2.2.2	Test Requirements	2640

A.9.1.3	Test for V2X Synchronization Reference Selection/Reselection	2641

A.9.1.3.1	Test for GNSS configured as the highest priority	2641

A.9.1.3.1.1	Test Purpose and Environment	2641

A.9.1.3.1.2	Test Requirements	2643

A.9.1.3.2	 Test for FR1 NR Cell configured as the highest priority	2645

A.9.1.3.2.1	Test Purpose and Environment	2645

A.9.1.3.2.2	Test Requirements	2647

A.9.1.4	Test for L1 SL-RSRP Measurement	2648

A.9.1.4.1	Test for V2X UE Autonomous Resource Selection/Reselection	2648

A.9.1.4.1.1	Test Purpose and Environment	2648

A.9.1.4.1.2	Test Requirements	2651

A.9.1.4.2	Test for V2X UE Resource Pre-emption	2652

A.9.1.4.2.1	Test Purpose and Environment	2652

A.9.1.4.2.2	Test Requirements	2655

A.9.1.4.3	Test for V2X UE Resource Re-evaluation	2655

A.9.1.4.3.1	Test Purpose and Environment	2655

A.9.1.4.3.2	Test Requirements	2662

A.9.1.5	Test for Congestion Control Measurement	2662

A.9.1.5.1	Test Purpose and Environment	2662

A.9.1.5.2	Test Requirements	2668

A.9.1.6	Test for Interruption	2668

A.9.1.6.1	Test for Interruption to WAN due to V2X Sidelink Communication	2668

A.9.1.6.1.1	Test Purpose and Environment	2668

A.9.1.6.1.2	Test Requirements	2671

A.10	EN-DC Tests with NR PSCell under CCA and Other NR Cells in FR1	2671

A.10.1	RRC\_CONNECTED state mobility	2671

A.10.1.1	RRC connection mobility control	2671

A.10.1.1.1	Random Access	2671

A.10.1.1.1.1	4-step RA type contention-based random access for NR PSCell with CCA	2671

A.10.1.1.1.1.1	Test Purpose and Environment	2671

A.10.1.1.1.1.2	Test Requirements	2674

A.10.1.1.1.1.2.1	Random Access Preamble Transmission	2674

A.10.1.1.1.1.2.2	Random Access Response Reception	2674

A.10.1.1.1.1.2.3	No Random Access Response Reception	2675

A.10.1.1.1.1.2.4	Receiving an UL grant for msg3 retransmission	2675

A.10.1.1.1.1.2.5	 Contention Resolution Timer expiry	2675

A.10.1.1.1.2	4-step RA type non-contention based random access for NR PSCell with CCA	2676

A.10.1.1.1.2.1	Test Purpose and Environment	2676

A.10.1.1.1.2.2	Test Requirements	2679

A.10.1.1.1.2.2.1	SSB-based Random Access Preamble Transmission	2679

A.10.1.1.1.2.2.2	Random Access Response Reception	2680

A.10.1.1.1.2.2.3	No Random Access Response Reception	2680

A.10.1.1.1.3	2-step RA type contention-based random access for NR PSCell with CCA	2680

A.10.1.1.1.3.1	Test Purpose and Environment	2680

A.10.1.1.1.3.2	Test Requirements	2684

A.10.1.1.1.3.2.1	MsgA Transmission	2684

A.10.1.1.1.3.2.2	MsgB Reception	2684

A.10.1.1.1.3.2.3	No MsgB Reception	2685

A.10.1.1.1.4	2-step RA type non-contention based random access for NR PSCell with CCA	2685

A.10.1.1.1.4.1	Test Purpose and Environment	2685

A.10.1.1.1.4.2	Test Requirements	2689

A.10.1.1.1.4.2.1	MsgA Transmission	2689

A.10.1.1.1.4.2.2	MsgB Reception	2690

A.10.1.1.1.4.2.3	No MsgB Reception	2690

A.10.2	Timing	2691

A.10.2.1	UE transmit timing	2691

A.10.2.2	UE timing advance	2695

A.10.3	Signalling characteristics	2698

A.10.3.1	Radio link monitoring	2698

A.10.3.1.1	Introduction	2698

A.10.3.1.2	Radio link monitoring out-of-sync test for PSCell configured with SSB-based RLM RS in non-DRX mode	2699

A.10.3.1.2.1	Test purpose and environment	2699

A.10.3.1.2.2	Test requirements	2704

A.10.3.1.3	Radio link monitoring in-sync test for PSCell configured with SSB-based RLM RS in non-DRX mode	2704

A.10.3.1.3.1	Test purpose and environment	2704

A.10.3.1.3.2	Test requirements	2710

A.10.3.1.4	Void	2710

A.10.3.1.4.1	Void	2710

A.10.3.1.4.2	Void	2710

A.10.3.1.5	Void	2710

A.10.3.1.5.1	Void	2710

A.10.3.1.5.2	Void	2710

A.10.3.2	Void	2711

A.10.3.3	SCell activation and deactivation delay	2711

A.10.3.3.2 SCell Activation and Deactivation of known NR SCell with NR PSCell and NR SCell under CCA, 640 ms SCell measurement cycle	2715

A.10.3.3.2.1	Test Purpose and Environment	2715

A.10.3.3.2.2	Test Requirements	2716

A.10.3.3.3 SCell Activation and Deactivation of unknown NR SCell with NR PSCell and NR SCell under CCA	2716

A.10.3.3.3.1	Test Purpose and Environment	2716

A.10.3.3.3.2	Test Requirements	2717

A.10.3.4	Beam failure detection and link recovery procedures	2717

A.10.3.4.1	EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in non-DRX mode	2717

A.10.3.4.1.1	Test Purpose and Environment	2717

A.10.3.4.1.2	Test Requirements	2722

A.10.3.4.2	EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in DRX mode	2722

A.10.3.4.2.1	Test Purpose and Environment	2722

A.10.3.4.2.2	Test Requirements	2728

A.10.3.5	Active BWP switching	2728

A.10.3.5.1	UL active BWP switch delay with consistent UL LBT failure on PSCell subject to UL CCA in EN-DC	2728

A.10.3.5.1.1	Test Purpose and Environment	2728

A.10.3.5.1.2	Test Requirements	2733

A.10.3.5.2	DCI-based and Timer-based Active BWP Switch	2734

A.10.3.5.2.1	E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC	2734

A.10.3.5.2.2	E-UTRAN – NR PSCell FR1 DL active BWP switch with FR1 SCell in non-DRX in synchronous EN-DC	2737

A.10.3.5.3	RRC-based Active BWP Switch	2741

A.10.3.6	PSCell addition and release delay	2745

A.10.3.6.1	Addition and Release Delay of known NR PSCell on the carrier under CCA	2745

A.10.3.6.1.1	Test purpose and environment	2745

A.10.3.6.1.2	Test Requirements	2750

A.10.3.7	Void	2751

A.10.4	Measurement procedure	2751

A.10.4.1	Intra-frequency measurements	2751

A.10.4.1.1	Event-triggered reporting tests on PSCC without gaps under non-DRX	2751

A.10.4.1.1.1	Test purpose and environment	2751

A.10.4.1.1.2	Test parameters	2751

A.10.4.1.1.3	Test Requirements	2755

A.10.4.1.2	Void	2755

A.10.4.1.3	Void	2755

A.10.4.1.4	Event-triggered reporting tests on PSCC with per-UE gaps under DRX	2755

A.10.4.1.4.1	Test purpose and environment	2755

A.10.4.1.4.2	Test parameters	2756

A.10.4.1.4.3	Test Requirements	2760

A.10.4.1.5	Void	2761

A.10.4.1.6	Void	2761

A.10.4.1.7	Void	2761

A.10.4.1.8	Void	2761

A.10.4.1.9	Void	2761

A.10.4.1.10	Void	2761

A.10.4.1.11	Void	2761

A.10.4.1.12	Void	2761

A.10.4.2	Inter-frequency measurements	2761

A.10.4.2.1	Void	2761

A.10.4.2.2	Void	2761

A.10.4.2.3	EN-DC event triggered reporting tests for FR1 with CCA cell without SSB time index detection when DRX is not used	2761

A.10.4.2.3.1	Test Purpose and Environment	2761

A.10.4.2.3.2	Test Requirements	2765

A.10.4.2.4	EN-DC event triggered reporting tests for FR1 cell with CCA without SSB time index detection when DRX is used	2766

A.10.4.2.4.1	Test Purpose and Environment	2766

A.10.4.2.4.2	Test Requirements	2770

A.10.4.2.5	EN-DC event triggered reporting tests for FR1 cell with CCA with SSB time index detection when DRX is not used	2771

A.10.4.2.5.1	Test Purpose and Environment	2771

A.10.4.2.5.2	Test Requirements	2775

A.10.4.2.6	EN-DC event triggered reporting tests for FR1 cell with CCA with SSB time index detection when DRX is used	2776

A.10.4.2.6.1	Test Purpose and Environment	2776

A.10.4.2.6.2	Test Requirements	2780

A.10.4.2.7	EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is not used	2781

A.10.4.2.7.1	Test Purpose and Environment	2781

A.10.4.2.7.2	Test Requirements	2787

A.10.4.2.8	EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used	2787

A.10.4.2.8.1	Test Purpose and Environment	2787

A.10.4.2.8.2	Test Requirements	2793

A.10.4.2.9	EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is not used	2794

A.10.4.2.9.1	Test Purpose and Environment	2794

A.10.4.2.9.2	Test Requirements	2799

A.10.4.2.10	EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is used	2799

A.10.4.2.10.1	Test Purpose and Environment	2799

A.10.4.2.10.2	Test Requirements	2805

A.10.4.3	L1-RSRP measurements for beam reporting	2806

A.10.4.3.1	SSB based L1-RSRP measurement on PSCC when DRX is not used	2806

A.10.4.3.1.1	Test Purpose and Environment	2806

A.10.4.3.1.2	Test parameters	2806

A.10.4.3.1.3	Test Requirements	2808

A.10.4.3.2	SSB based L1-RSRP measurement on PSCC when DRX is used	2809

A.10.4.3.2.1	Test Purpose and Environment	2809

A.10.4.3.2.2	Test parameters	2809

A.10.4.3.2.3	Test Requirements	2811

A.10.4.3.3	SSB based L1-RSRP measurement on SCC when DRX is not used	2812

A.10.4.3.3.1	Test Purpose and Environment	2812

A.10.4.3.3.2	Test parameters	2812

A.10.4.3.3.3	Test Requirements	2815

A.10.4.3.4	SSB based L1-RSRP measurement on SCC when DRX is used	2816

A.10.4.3.4.1	Test Purpose and Environment	2816

A.10.4.3.4.2	Test parameters	2816

A.10.4.3.4.3	Test Requirements	2819

A.10.4.4	E-UTRANNR inter-RAT measurements on NR carrier frequency under CCA	2820

A.10.4.4.1	E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used	2820

A.10.4.4.1.1	Test Purpose and Environment	2820

A.10.4.4.1.2	Test Requirements	2827

A.10.4.4.2	E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used	2827

A.10.4.4.2.1	Test Purpose and Environment	2827

A.10.4.4.2.2	Test Requirements	2834

A.10.4.4.3	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used	2834

A.10.4.4.3.1	Test Purpose and Environment	2834

A.10.4.4.3.2	Test Requirements	2841

A.10.4.4.4	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used	2841

A.10.4.4.4.1	Test Purpose and Environment	2841

A.10.4.4.4.2	Test Requirements	2849

A.10.5	Measurement performance	2849

A.10.5.1	SS-RSRP	2849

A.10.5.1.1	Intra-frequency measurement accuracy on a CCA serving cell	2849

A.10.5.1.1.1	Test Purpose and Environment	2849

A.10.5.1.1.2	Test parameters	2849

A.10.5.1.1.3	Test Requirements	2852

A.10.5.1.2	Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell	2852

A.10.5.1.2.1	Test Purpose and Environment	2852

A.10.5.1.2.2	Test parameters	2852

A.10.5.1.2.3	Test Requirements	2856

A.10.5.2	SS-RSRQ	2856

A.10.5.2.1	Intra-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell	2856

A.10.5.2.1.1	Test Purpose and Environment	2856

A.10.5.2.1.2	Test Parameters	2856

A.10.5.2.1.3	Test Requirements	2859

A.10.5.2.2	Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell	2859

A.10.5.2.2.1	Test Purpose and Environment	2859

A.10.5.2.2.2	Test Parameters	2859

A.10.5.2.2.3	Test Requirements	2862

A.10.5.3	SS-SINR	2862

A.10.5.3.1	Intra-frequency measurement accuracy on PSCC	2862

A.10.5.3.1.1	Test Purpose and Environment	2862

A.10.5.3.1.2	Test Parameters	2862

A.10.5.3.1.3	Test Requirements	2865

A.10.5.3.2	Inter-frequency measurement accuracy on PSCC	2865

A.10.5.3.2.1	Test Purpose and Environment	2865

A.10.5.3.2.2	Test Parameters	2865

A.10.5.3.2.3	Test Requirements	2869

A.10.5.3.3	Intra-frequency measurement accuracy on SCC	2869

A.10.5.3.3.1	Test Purpose and Environment	2869

A.10.5.3.3.2	Test Parameters	2869

A.10.5.3.3.3	Test Requirements	2872

A.10.5.4	L1-RSRP measurement for beam reporting with CCA serving cell	2872

A.10.5.4.1	SSB based L1-RSRP measurement	2872

A.10.5.4.1.1	Test Purpose and Environment	2872

A.10.5.4.1.2	Test parameters	2873

A.10.5.4.1.3	Test Requirements	2875

A.10.5.5	RSSI	2875

A.10.5.5.1 	RSSI measurement accuracy on PSCC with CCA	2875

A.10.5.5.1.1	Test Purpose and Environment	2875

A.10.5.5.1.2	Test parameters	2875

A.10.5.5.1.3	Test Requirements	2878

A.10.5.5.2 	RSSI measurement accuracy on SCC with CCA	2878

A.10.5.5.2.1	Test Purpose and Environment	2878

A.10.5.5.2.2	Test parameters	2878

A.10.5.5.2.3	Test Requirements	2881

A.10.5.5.3 	Inter-frequency RSSI measurement accuracy on a carrier with CCA	2881

A.10.5.5.3.1	Test Purpose and Environment	2881

A.10.5.5.3.2	Test parameters	2881

A.10.5.5.3.3	Test Requirements	2885

A.10.5.6	Channel occupancy	2885

A.10.5.6.1 	Channel occupancy measurement accuracy on PSCC with CCA	2885

A.10.5.6.1.1	Test Purpose and Environment	2885

A.10.5.6.1.2	Test parameters	2885

A.10.5.6.1.3	Test Requirements	2889

A.10.5.6.2 	Channel occupancy measurement accuracy on SCC with CCA	2889

A.10.5.6.2.1	Test Purpose and Environment	2889

A.10.5.6.2.2	Test parameters	2889

A.10.5.6.2.3	Test Requirements	2892

A.10.5.6.3 	Inter-frequency channel occupancy measurement accuracy on a carrier with CCA	2892

A.10.5.6.3.1	Test Purpose and Environment	2892

A.10.5.6.3.2	Test parameters	2892

A.10.5.6.3.3	Test Requirements	2896

A.11	NR Standalone Tests with NR PCell under CCA and Other NR Cells in FR1	2896

A.11.1	RRC\_IDLE state mobility	2897

A.11.1.1	Cell re-selection with both source and target NR carrier frequencies under CCA	2897

A.11.1.1.1	Cell reselection to FR1 intra-frequency NR cells when subject to CCA on the serving and target cell	2897

A.11.1.1.1.1	Test Purpose and Environment	2897

A.11.1.1.1.2	Test Parameters	2897

A.11.1.1.1.3	Test Requirements	2900

A.11.1.1.2	Cell reselection to FR1 inter-frequency NR case when subject to CCA on the serving and target cell	2900

A.11.1.1.2.1	Test Purpose and Environment	2900

A.11.1.1.2.2	Test Parameters	2900

A.11.1.1.2.3	Test Requirements	2904

A.11.1.2	Cell re-selection to NR with source NR carrier frequency under CCA	2904

A.11.1.2.1	Cell reselection to FR1 inter-frequency NR case when serving cell is subject to CCA	2904

A.11.1.2.1.1	Test Purpose and Environment	2904

A.11.1.2.1.2	Test Parameters	2905

A.11.1.2.1.3	Test Requirements	2911

A.11.1.3	Cell re-selection from NR carrier with target NR carrier frequency under CCA	2912

A.11.1.3.1	Cell reselection to FR1 inter-frequency NR case when target cell is subject to CCA	2912

A.11.1.3.1.1	Test Purpose and Environment	2912

A.11.1.3.1.2	Test Parameters	2912

A.11.1.3.1.3	Test Requirements	2917

A.11.1.4	Inter-RAT cell re-selection to E-UTRAN with source NR carrier frequency under CCA	2918

A.11.1.4.1	Cell reselection to higher priority E-UTRAN when serving cell is subject to CCA	2918

A.11.1.4.1.1	Test Purpose and Environment	2918

A.11.1.4.1.2	Test Parameters	2918

A.11.1.4.1.3	Test Requirements	2921

A.11.1.4.2	Cell reselection to lower priority E-UTRAN when serving cell is subject to CCA	2922

A.11.1.4.2.1	Test Purpose and Environment	2922

A.11.1.4.2.2	Test Requirements	2924

A.11.2	RRC\_CONNECTED state mobility	2925

A.11.2.1	Handover	2925

A.11.2.1.1	Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; known target cell	2925

A.11.2.1.1.1	Test Purpose and Environment	2925

A.11.2.1.1.2	Test Parameters	2925

A.11.2.1.1.3 Test Requirements	2928

A.11.2.1.2	Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; unknown target cell	2928

A.11.2.1.2.1	Test Purpose and Environment	2928

A.11.2.1.2.2	Test Parameters	2928

A.11.2.1.2.3	Test Requirements	2931

A.11.2.1.3	Inter-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; unknown target cell	2931

A.11.2.1.3.1	Test Purpose and Environment	2931

A.11.2.1.3.2	Test Parameters	2931

A.11.2.1.3.3	Test Requirements	2934

A.11.2.1.4	Inter-frequency handover from FR1 carrier under CCA to FR1; known target cell	2934

A.11.2.1.4.1	Test Purpose and Environment	2934

A.11.2.1.4.2	Test Parameters	2934

A.11.2.1.4.3 Test Requirements	2938

A.11.2.1.5	Inter-frequency handover from FR1 carrier under CCA to FR1; unknown target cell	2939

A.11.2.1.5.1	Test Purpose and Environment	2939

A.11.2.1.5.2	Test Parameters	2939

A.11.2.1.5.3 Test Requirements	2942

A.11.2.1.6	Inter-frequency handover from FR1 to FR1 carrier under CCA; unknown target cell	2943

A.11.2.1.6.1	Test Purpose and Environment	2943

A.11.2.1.6.2	Test Parameters	2943

A.11.2.1.6.3	Test Requirements	2948

A.11.2.1.7	 SA NR FR1 carrier under CCA - E-UTRAN handover with known target cell	2948

A.11.2.1.7.1	Test Purpose and Environment	2948

A.11.2.1.7.2	Test Requirements	2954

A.11.2.1.8	SA NR FR1 carrier under CCA - E-UTRAN handover with unknown target cell	2954

A.11.2.1.8.1	Test Purpose and Environment	2954

A.11.2.1.8.2	Test Requirements	2959

A.11.2.2	RRC connection mobility control	2959

A.11.2.2.1	RRC re-establishment	2959

A.11.2.2.1.1	Intra-frequency RRC Re-establishment with CCA in FR1	2959

A.11.2.2.1.2	Inter-frequency RRC Re-establishment with CCA in FR1	2962

A.11.2.2.1.3	Intra-frequency RRC Re-establishment with CCA in FR1 without serving cell timing	2968

A.11.2.2.1.4	Inter-frequency RRC Re-establishment from NR FR1 carrier without CCA to NR FR1 carrier under CCA	2972

A.11.2.2.2	Random Access	2977

A.11.2.2.2.1	4-step RA type contention-based random access for NR PCell with CCA	2977

A.11.2.2.2.1.1	Test Purpose and Environment	2977

A.11.2.2.2.1.2	Test Requirements	2980

A.11.2.2.2.1.2.1	Random Access Preamble Transmission	2980

A.11.2.2.2.1.2.2	Random Access Response Reception	2980

A.11.2.2.2.1.2.3	No Random Access Response Reception	2981

A.11.2.2.2.1.2.4	Receiving an UL grant for msg3 retransmission	2981

A.11.2.2.2.1.2.5	Reception of an Incorrect Message over Temporary C-RNTI	2981

A.11.2.2.2.1.2.6	Reception of a Correct Message over Temporary C-RNTI	2982

A.11.2.2.2.1.2.7	Contention Resolution Timer expiry	2982

A.11.2.2.2.2	4-step RA type non-contention based random access for NR PSCell with CCA	2982

A.11.2.2.2.2.1	Test Purpose and Environment	2982

A.11.2.2.2.2.2	Test Requirements	2985

A.11.2.2.2.2.2.1	SSB-based Random Access Preamble Transmission	2985

A.11.2.2.2.2.2.2	Random Access Response Reception	2986

A.11.2.2.2.2.2.3	No Random Access Response Reception	2986

A.11.2.2.2.3	2-step RA type contention-based random access for NR PCell with CCA	2986

A.11.2.2.2.3.1	Test Purpose and Environment	2986

A.11.2.2.2.3.2	Test Requirements	2990

A.11.2.2.2.3.2.1	MsgA Transmission	2990

A.11.2.2.2.3.2.2	MsgB Reception	2990

A.11.2.2.2.3.2.3	No MsgB Reception	2991

A.11.2.2.2.4	2-step RA type non-contention-based random access for NR PCell with CCA	2991

A.11.2.2.2.4.1	Test Purpose and Environment	2991

A.11.2.2.2.4.2	Test Requirements	2995

A.11.2.2.2.4.2.1	MsgA Transmission	2995

A.11.2.2.2.4.2.2	MsgB Reception	2996

A.11.2.2.2.4.2.3	No MsgB Reception	2996

A.11.2.2.3	RRC connection release with redirection	2997

A.11.2.2.3.1	Redirection from NR FR1 carrier under CCA to NR FR1 carrier under CCA	2997

A.11.3	Timing	3005

A.11.3.1	UE transmit timing	3005

A.11.3.2	UE timing advance	3009

A.11.3.2.1	UE Timing Advance Adjustment Accuracy with PCell under DL CCA	3009

A.11.3.2.1.1	Test Purpose and Environment	3009

A.11.3.2.1.2	Test Parameters	3009

A.11.3.2.1.3	Test Requirements	3013

A.11.4	Signalling characteristics	3013

A.11.4.1	Radio link monitoring	3013

A.11.4.1.1	Introduction	3013

A.11.4.1.2	Radio link monitoring out-of-sync test for PCell configured with SSB-based RLM RS in non-DRX mode	3014

A.11.4.1.2.1	Test purpose and environment	3014

A.11.4.1.2.2	Test requirements	3018

A.11.4.1.3	Radio link monitoring in-sync test for PCell configured with SSB-based RLM RS in non-DRX mode	3018

A.11.4.1.3.1	Test purpose and environment	3018

A.11.4.1.3.2	Test requirements	3024

A.11.4.1.4	Void	3024

A.11.4.1.4.1	Void	3024

A.11.4.1.4.2	Void	3024

A.11.4.1.5	Void	3024

A.11.4.1.5.1	Void	3024

A.11.4.1.5.2	Void	3024

A.11.4.2	Void	3025

A.11.4.3	SCell activation and deactivation delay	3025

A.11.4.3.2	SCell Activation and Deactivation of known SCell with PCell and SCell under CCA, 640 ms SCell measurement cycle	3029

A.11.4.3.2.1	Test Purpose and Environment	3029

A.11.4.3.2.2	Test Requirements	3030

A.11.4.4	Beam failure detection and link recovery procedures	3031

A.11.4.4.1	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode	3031

A.11.4.4.1.1	Test Purpose and Environment	3031

A.11.4.4.1.2	Test Requirements	3037

A.11.4.4.2	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode	3037

A.11.4.4.2.1	Test Purpose and Environment	3037

A.11.4.4.2.2	Test Requirements	3043

A.11.4.5	Active BWP switching	3043

A.11.4.5.1	UL active BWP switch delay with consistent UL LBT failure on PCell subject to UL CCA	3043

A.11.4.5.1.1	Test Purpose and Environment	3043

A.11.4.5.1.2	Test Requirements	3047

A.11.4.6	Void	3057

A.11.5	Measurement procedure	3057

A.11.5.1	Intra-frequency measurements	3057

A.11.5.1.1	Event-triggered reporting tests on PCC without gaps under non-DRX	3057

A.11.5.1.1.1	Test purpose and environment	3057

A.11.5.1.1.2	Test parameters	3057

A.11.5.1.1.3	Test Requirements	3061

A.11.5.1.2	Event-triggered reporting tests on PCC without gaps under DRX	3061

A.11.5.1.2.1	Test purpose and environment	3061

A.11.5.1.2.2	Test parameters	3061

A.11.5.1.2.3	Test Requirements	3065

A.11.5.1.3	Void	3065

A.11.5.1.4	Void	3065

A.11.5.1.5	Void	3065

A.11.5.1.6	Void	3065

A.11.5.1.7	Void	3065

A.11.5.1.8	Void	3065

A.11.5.1.9	Void	3065

A.11.5.1.10	Void	3065

A.11.5.1.11	Void	3065

A.11.5.1.12	Void	3065

A.11.5.2	Inter-frequency measurements	3066

A.11.5.2.1	Void	3066

A.11.5.2.2	Void	3066

A.11.5.2.3	Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is not used	3066

A.11.5.2.3.1	Test Purpose and Environment	3066

A.11.5.2.3.2	Test Requirements	3070

A.11.5.2.4	Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is used	3071

A.11.5.2.4.1	Test Purpose and Environment	3071

A.11.5.2.4.2	Test Requirements	3076

A.11.5.2.5	Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is not used	3076

A.11.5.2.5.1	Test Purpose and Environment	3076

A.11.5.2.5.2	Test Requirements	3080

A.11.5.2.6	Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is used	3081

A.11.5.2.6.1	Test Purpose and Environment	3081

A.11.5.2.6.2	Test Requirements	3086

A.11.5.2.7	Event triggered reporting tests for FR1 without SSB time index detection when DRX is not used	3086

A.11.5.2.7.1	Test Purpose and Environment	3086

A.11.5.2.7.2	Test Requirements	3090

A.11.5.2.8	Event triggered reporting tests for FR1 without SSB time index detection when DRX is used	3091

A.11.5.2.8.1	Test Purpose and Environment	3091

A.11.5.2.8.2	Test Requirements	3096

A.11.5.2.9	Event triggered reporting tests for FR1 with SSB time index detection when DRX is not used	3096

A.11.5.2.9.1	Test Purpose and Environment	3096

A.11.5.2.9.2	Test Requirements	3100

A.11.5.2.10	Event triggered reporting tests for FR1 with SSB time index detection when DRX is used	3101

A.11.5.2.10.1	Test Purpose and Environment	3101

A.11.5.2.10.2	Test Requirements	3106

A.11.5.3	Inter-RAT E-UTRAN measurements	3106

A.11.5.3.1	SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1	3106

A.11.5.3.1.1	Test Purpose and Environment	3106

A.11.5.3.1.2	Test Requirements	3112

A.11.5.3.2	SA NR - E-UTRAN event-triggered reporting in DRX in FR1	3112

A.11.5.3.2.1	Test Purpose and Environment	3112

A.11.5.3.2.2	Test Requirements	3118

A.11.5.4	L1-RSRP measurements for beam reporting	3118

A.11.5.4.1	SSB based L1-RSRP measurement when DRX is not used	3118

A.11.5.4.1.1	Test Purpose and Environment	3118

A.11.5.4.1.2	Test parameters	3118

A.11.5.4.1.3	Test Requirements	3120

A.11.5.4.2	SSB based L1-RSRP measurement when DRX is used	3120

A.11.5.4.2.1	Test Purpose and Environment	3120

A.11.5.4.2.2	Test parameters	3121

A.11.5.4.2.3	Test Requirements	3123

A.11.5.4.3	SSB based L1-RSRP measurement on SCC when DRX is not used	3123

A.11.5.4.3.1	Test Purpose and Environment	3123

A.11.5.4.3.2	Test parameters	3124

A.11.5.4.3.3	Test Requirements	3127

A.11.5.4.4	SSB based L1-RSRP measurement on SCC when DRX is used	3128

A.11.5.4.4.1	Test Purpose and Environment	3128

A.11.5.4.4.2	Test parameters	3128

A.11.5.4.4.3	Test Requirements	3131

A.11.6	Measurement performance	3132

A.11.6.1	SS-RSRP	3132

A.11.6.1.1	Intra-frequency measurement accuracy on a carrier frequency with CCA	3132

A.11.6.1.1.1	Test Purpose and Environment	3132

A.11.6.1.1.2	Test parameters	3132

A.11.6.1.1.3	Test Requirements	3134

A.11.6.1.2	Intra-frequency measurement accuracy on SCC on a carrier frequency with CCA	3134

A.11.6.1.2.1	Test Purpose and Environment	3134

A.11.6.1.2.2	Test parameters	3134

A.11.6.1.2.3	Test Requirements	3136

A.11.6.2	SS-RSRQ	3136

A.11.6.2.1	Intra-frequency measurement accuracy	3136

A.11.6.2.1.1	Test Purpose and Environment	3136

A.11.6.2.1.2	Test Parameters	3136

A.11.6.2.1.3	Test Requirements	3139

A.11.6.2.2	Inter-frequency measurement accuracy	3139

A.11.6.2.2.1	Test Purpose and Environment	3139

A.11.6.2.2.2	Test Parameters	3139

A.11.6.2.2.3	Test Requirements	3142

A.11.6.2.3	Intra-frequency measurement accuracy on SCC	3142

A.11.6.2.3.1	Test Purpose and Environment	3142

A.11.6.2.3.2	Test Parameters	3142

A.11.6.2.3.3	Test Requirements	3145

A.11.6.2.4	Inter-frequency measurement accuracy	3145

A.11.6.2.4.1	Test Purpose and Environment	3145

A.11.6.2.4.2	Test Parameters	3145

A.11.6.2.4.3	Test Requirements	3152

A.11.6.3	SS-SINR	3152

A.11.6.3.1	Intra-frequency measurement accuracy	3152

A.11.6.3.1.1	Test Purpose and Environment	3152

A.11.6.3.1.2	Test Parameters	3152

A.11.6.3.1.3	Test Requirements	3155

A.11.6.3.2	Inter-frequency measurement accuracy	3155

A.11.6.3.2.1	Test Purpose and Environment	3155

A.11.6.3.2.2	Test Parameters	3155

A.11.6.3.2.3	Test Requirements	3158

A.11.6.3.3	Intra-frequency measurement accuracy on SCC	3158

A.11.6.3.3.1	Test Purpose and Environment	3158

A.11.6.3.3.2	Test Parameters	3158

A.11.6.3.3.3	Test Requirements	3161

A.11.6.3.4	Inter-frequency measurement accuracy	3161

A.11.6.3.4.1	Test Purpose and Environment	3161

A.11.6.3.4.2	Test Parameters	3161

A.11.6.3.4.3	Test Requirements	3169

A.11.6.4	L1-RSRP measurement for beam reporting with CCA serving cell	3169

A.11.6.4.1	SSB based L1-RSRP measurement	3169

A.11.6.4.1.1	Test Purpose and Environment	3169

A.11.6.4.1.2	Test parameters	3170

A.11.6.4.1.3	Test Requirements	3173

A.11.6.5	RSSI	3173

A.11.6.5.1	Intra-frequency RSSI measurement accuracy on PCC with CCA	3173

A.11.6.5.1.1	Test Purpose and Environment	3173

A.11.6.5.1.2	Test parameters	3173

A.11.6.5.1.3	Test Requirements	3176

A.11.6.5.2 	Intra-frequency RSSI measurement accuracy on SCC with CCA	3176

A.11.6.5.2.1	Test Purpose and Environment	3176

A.11.6.5.2.2	Test parameters	3176

A.11.6.5.2.3	Test Requirements	3179

A.11.6.5.3 	Inter-frequency RSSI measurement accuracy on a carrier with CCA	3179

A.11.6.5.3.1	Test Purpose and Environment	3179

A.11.6.5.3.2	Test parameters	3179

A.11.6.5.3.3	Test Requirements	3183

A.11.6.6	Channel occupancy	3183

A.11.6.6.1 	Intra-frequency channel occupancy measurement accuracy on PCC with CCA	3183

A.11.6.6.1.1	Test Purpose and Environment	3183

A.11.6.6.1.2	Test parameters	3183

A.11.6.6.1.3	Test Requirements	3187

A.11.6.6.2 	Intra-frequency channel occupancy measurement accuracy on SCC with CCA	3187

A.11.6.6.2.1	Test Purpose and Environment	3187

A.11.6.6.2.2	Test parameters	3187

A.11.6.6.2.3	Test Requirements	3190

A.11.6.6.3 	Inter-frequency channel occupancy measurement accuracy on a carrier with CCA	3190

A.11.6.6.3.1	Test Purpose and Environment	3190

A.11.6.6.3.2	Test parameters	3190

A.11.6.6.3.3	Test Requirements	3194

A.11.6.7	E-UTRAN RSRP	3195

A.11.6.8	E-UTRAN RSRQ	3195

A.11.6.9	E-UTRAN SINR	3195

A.12	E-UTRA Standalone Tests with at Least One NR Cell under CCA	3195

A.12.1	RRC\_IDLE state mobility	3195

A.12.1.1	Inter-RAT cell re-selection to NR on a carrier frequency with CCA	3195

A.12.1.1.1	E-UTRA Cell reselection to higher priority NR target Cell in FR1 when target cell is subject to CCA	3195

A.12.1.1.1.1	Test Purpose and Environment	3195

A.12.1.1.1.2	Test Requirements	3200

A.12.2	RRC\_CONNECTED state mobility	3201

A.12.2.1	Handover	3201

A.12.2.1.1	E-UTRAN - NR with CCA handover	3201

A.12.2.1.1.1	Test Purpose and Environment	3201

A.12.2.1.1.2	Test Requirements	3206

A.12.3	Void	3207

A.12.4	Measurement procedure	3207

A.12.4.1	E-UTRANNR inter-RAT SFTD measurements	3207

A.12.4.1.1	E-UTRA – NR Inter-RAT SFTD Measurement Delay with NR under CCA in non-DRX	3207

A.12.4.1.1.1	Test Purpose and Environment	3207

A.12.4.1.1.2	Test Requirements	3211

A.12.4.2	E-UTRANNR inter-RAT measurements on NR carrier frequency under CCA	3211

A.12.4.2.1	E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used	3211

A.12.4.2.1.1	Test Purpose and Environment	3211

A.12.4.2.1.2	Test Requirements	3217

A.12.4.2.2	E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used	3217

A.12.4.2.2.1	Test Purpose and Environment	3217

A.12.4.2.2.2	Test Requirements	3222

A.12.4.2.3	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used	3222

A.12.4.2.3.1	Test Purpose and Environment	3222

A.12.4.2.3.2	Test Requirements	3227

A.12.4.2.4	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used	3227

A.12.4.2.4.1	Test Purpose and Environment	3227

A.12.4.2.4.2	Test Requirements	3232

A.12.4.2.5	Void	3232

A.12.4.2.6	Void	3232

A.12.5	Measurement performance	3232

A.12.5.1	E-UTRANNR SFTD	3232

A.12.5.2	Void	3239

A.12.5.3	Void	3239

A.12.5.4	Void	3239

A.12.5.5	Void	3239

A.12.5.6	Void	3239

A.13	 NR Standalone Tests with NR SCell under CCA and All Other NR Cells in FR1	3239

A.13.1	Void	3239

A.13.1.1	Void	3239

A.13.1.2	Void	3239

A.13.2	Signalling characteristics	3239

A.13.2.1	Void	3239

A.13.2.2	SCell activation and deactivation delay	3239

A.13.2.2.2	SCell Activation and Deactivation of known SCell under CCA, 640 ms SCell measurement cycle	3244

A.13.2.2.2.1	Test Purpose and Environment	3244

A.13.2.2.2.2	Test Requirements	3245

A.13.2.2.3	SCell Activation and Deactivation of unknown SCell under CCA	3245

A.13.2.2.3.1	Test Purpose and Environment	3245

A.13.2.2.3.2	Test Requirements	3246

A.13.2.3	Void	3246

A.13.3	Measurement procedure	3246

A.13.3.1	Intra-frequency measurements	3246

A.13.3.1.1	Event-triggered reporting tests on SCC without gaps under non-DRX	3246

A.13.3.1.1.1	Test purpose and environment	3246

A.13.3.1.1.2	Test parameters	3246

A.13.3.1.1.3	Test Requirements	3251

A.13.3.1.2	Event-triggered reporting tests on SCC without gaps under DRX	3251

A.13.3.1.2.1	Test purpose and environment	3251

A.13.3.1.2.2	Test parameters	3251

A.13.3.1.2.3	Test Requirements	3256

A.13.3.1.3	Event-triggered reporting tests on SCC with per-UE gaps under non-DRX	3256

A.13.3.1.3.1	Test purpose and environment	3256

A.13.3.1.3.2	Test parameters	3256

A.13.3.1.3.3	Test Requirements	3261

A.13.3.1.4	Event-triggered reporting tests on SCC with per-UE gaps under DRX	3261

A.13.3.1.4.1	Test purpose and environment	3261

A.13.3.1.4.2	Test parameters	3261

A.13.3.1.4.3	Test Requirements	3267

A.13.3.1.5	Void	3267

A.13.3.1.6	Void	3267

A.13.3.2	Inter-frequency measurements	3267

A.13.3.2.1	Void	3267

A.13.3.2.2	Void	3267

A.13.3.2.3	Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is not used	3267

A.13.3.2.3.1	Test Purpose and Environment	3267

A.13.3.2.3.2	Test Requirements	3272

A.13.3.2.4	Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is used	3272

A.13.3.2.4.1	Test Purpose and Environment	3272

A.13.3.2.4.2	Test Requirements	3277

A.13.3.2.5	Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is not used	3278

A.13.3.2.5.1	Test Purpose and Environment	3278

A.13.3.2.5.2	Test Requirements	3283

A.13.3.2.6	Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is used	3283

A.13.3.2.6.1	Test Purpose and Environment	3283

A.13.3.2.6.2	Test Requirements	3288

A.13.3.3	L1-RSRP measurements for beam reporting	3289

A.13.3.3.1	SSB based L1-RSRP measurement when DRX is not used	3289

A.13.3.3.1.1	Test Purpose and Environment	3289

A.13.3.3.1.2	Test parameters	3289

A.13.3.3.1.3	Test Requirements	3293

A.13.3.3.2	SSB based L1-RSRP measurement when DRX is used	3294

A.13.3.3.2.1	Test Purpose and Environment	3294

A.13.3.3.2.2	Test parameters	3294

A.13.3.3.2.3	Test Requirements	3298

A.13.4	Measurement performance	3299

A.13.4.1	SS-RSRP	3299

A.13.4.1.1	Intra-frequency measurement accuracy on a carrier frequency with CCA	3299

A.13.4.1.1.1	Test Purpose and Environment	3299

A.13.4.1.1.2	Test parameters	3299

A.13.4.1.1.3	Test Requirements	3301

A.13.4.2	SS-RSRQ	3301

A.13.4.2.1	Intra-frequency measurement accuracy on SCC	3301

A.13.4.2.1.1	Test Purpose and Environment	3301

A.13.4.2.1.2	Test Parameters	3301

A.13.4.2.1.3	Test Requirements	3308

A.13.4.3	SS-SINR	3308

A.13.4.3.1	Intra-frequency measurement accuracy on SCC	3308

A.13.4.3.1.1	Test Purpose and Environment	3308

A.13.4.3.1.2	Test Parameters	3308

A.13.4.3.1.3	Test Requirements	3315

A.13.4.4	L1-RSRP measurement for beam reporting with CCA serving cell	3315

A.13.4.4.1	SSB based L1-RSRP measurement	3315

A.13.4.4.1.1	Test Purpose and Environment	3315

A.13.4.4.1.2	Test parameters	3316

A.13.4.4.1.3	Test Requirements	3320

A.13.4.5	RSSI	3320

A.13.4.5.1 	Intra-frequency RSSI measurement accuracy on a carrier with CCA	3320

A.13.4.5.1.1	Test Purpose and Environment	3320

A.13.4.5.1.2	Test parameters	3320

A.13.4.5.1.3	Test Requirements	3324

A.13.4.5.2	  Inter-frequency RSSI measurement accuracy on a carrier with CCA	3324

A.13.4.5.2.1	Test Purpose and Environment	3324

A.13.4.5.2.2	Test parameters	3324

A.13.4.5.2.3	Test Requirements	3328

A.13.4.6	Channel occupancy	3328

A.13.4.6.1 	Intra-frequency channel occupancy measurement accuracy on SCC with CCA	3328

A.13.4.6.1.1	Test Purpose and Environment	3328

A.13.4.6.1.2	Test parameters	3328

A.13.4.6.1.3	Test Requirements	3332

A.13.4.6.2	  Inter-frequency channel occupancy measurement accuracy on a carrier with CCA	3332

A.13.4.6.2.1	Test Purpose and Environment	3332

A.13.4.6.2.2	Test parameters	3332

A.13.4.6.2.3	Test Requirements	3336

Annex B (normative): Conditions for RRM requirements applicability for operating bands	3328

B.1	Conditions for NR RRC\_IDLE state mobility	3328

B.1.1	Introduction	3328

B.1.2	Conditions for measurements on NR intra-frequency cells for cell re-selection	3328

B.1.2A	Conditions for measurements on NR intra-frequency cells under CCA for cell re-selection	3329

B.1.3	Conditions for measurements on NR inter-frequency cells for cell re-selection	3330

B.1.3A	Conditions for measurements on NR inter-frequency cells under CCA for cell re-selection	3330

B.2	Conditions for UE measurements procedures and performance requirements in RRC\_CONNECTED state	3330

B.2.1	Introduction	3330

B.2.1.1	General	3330

B.2.1.2	Derivation of Minimum SSB\_RP values for FR1	3330

B.2.1.3	Derivation of Minimum SSB\_RP values for FR2	3330

B.2.1.3.1	Minimum SSB\_RP values for Rx Beam Peak angle of arrival	3331

B.2.1.3.2	Minimum SSB\_RP values for angle of arrival within Spherical coverage	3331

B.2.1.4	Gain to SS-RSRP and CSI-RSRP measurement point for FR1	3332

B.2.1.5	Gain to SS-RSRP and CSI-RSRP measurement point for FR2	3332

B.2.1.5.1	Gain to SS-RSRP and CSI-RSRP measurement point for Rx Beam Peak angle of arrival	3332

B.2.1.5.2	Gain to SS-RSRP measurement point for different frequency	3333

B.2.1.5.3	Alignment of Rough beam to Rx beam Peak	3333

B.2.1.6	Gain to PRS-RSRP measurement point for FR2	3333

B.2.1.6.1	Gain to PRS-RSRP measurement point for Rx Beam Peak angle of arrival	3333

B.2.2	Conditions for NR intra-frequency measurements	3334

B.2.3	Conditions for NR inter-frequency measurements	3335

B.2.4	Conditions for NR L1-RSRP reporting	3337

B.2.4.1	Conditions for SSB based L1-RSRP reporting	3337

B.2.4.2	Conditions for CSI-RS based L1-RSRP reporting	3338

B.2.5	Conditions for RRC connection release with redirection to NR	3339

B.2.6	Void	3341

B.2.6.1	Void	3341

B.2.6.2	Void	3341

B.2.7	Conditions for SRS-RSRP measurements	3341

B.2.8	Conditions for NR L1-SINR reporting	3342

B.2.8.1	Conditions for L1-SINR reporting with CSI-RS based CMR and no dedicated IMR configured	3342

B.2.8.2	Conditions for L1-SINR reporting with SSB based CMR and dedicated IMR configured	3343

B.2.8.2.1	L1-SINR reporting with SSB based CMR and dedicated ZP-IMR configured	3343

B.2.8.2.2	L1-SINR reporting with SSB based CMR and dedicated NZP-IMR configured	3343

B.2.8.3	Conditions for L1-SINR reporting with CSI-RS based CMR and dedicated IMR configured	3345

B.2.8.3.1	L1-SINR reporting with CSI-RS based CMR and dedicated ZP-IMR configured	3345

B.2.8.3.2	L1-SINR reporting with CSI-RS based CMR and dedicated NZP-IMR configured	3346

B.2.9	Conditions for NR intra-frequency measurements under CCA	3347

B.2.10	Conditions for NR inter-frequency measurements under CCA	3347

B.2.11	Conditions for NR L1-RSRP reporting under CCA	3347

B.2.11.1	Conditions for SSB based L1-RSRP reporting	3347

B.2.12	Conditions for NR CSI-RS based intra-frequency measurements	3348

B.2.13	Conditions for NR CSI-RS based inter-frequency measurements	3349

B.2.14	Conditions for NR PRS-based measurements	3351

B.3	RRM Requirements Exceptions	3352

B.3.1	Introduction	3352

B.3.2	Receiver sensitivity relaxation for CA	3352

B.3.2.1	Receiver sensitivity relaxation for UE supporting CA in FR1	3352

B.3.2.2	Receiver sensitivity relaxation for UE configured with CA in FR1	3353

B.3.2.2.1	Inter-band carrier aggregation	3353

B.3.2.2.2	Reference sensitivity exceptions due to UL harmonic interference for CA	3353

B.3.2.2.3	Reference sensitivity exceptions due to intermodulation interference due to 2UL CA	3353

B.3.2.3	Receiver sensitivity relaxation for UE supporting CA in FR2	3353

B.3.2.4	Receiver sensitivity relaxation for UE configured with CA in FR2	3353

B.3.2.4.1	Intra-band contiguous carrier aggregation	3353

B.3.2.4.2	Intra-band non-contiguous carrier aggregation	3354

B.3.3	Receiver sensitivity relaxation for DC	3354

B.3.3.1	Receiver sensitivity relaxation for EN-DC	3354

B.3.3.2	Receiver sensitivity relaxation for NE-DC	3354

B.3.4	Receiver sensitivity relaxation for SUL	3354

B.3.4.1	Receiver sensitivity relaxation for UE supporting SUL in FR1	3354

B.3.4.2	Receiver sensitivity relaxation for UE configured with SUL in FR1	3354

B.3.4.2.1	Reference sensitivity exceptions due to UL harmonic interference for SUL	3354

B.4	Conditions for V2X	3354

B.4.1	Test parameters for GNSS signals	3354

B.4.2	Conditions for PSBCH-RSRP Accuracy Requirements	3355

B.4.3	Conditions for Selection/Reselection to Intra-frequency SyncRef UE	3355

B.4.4	Conditions for L1 SL-RSRP Accuracy Requirements	3355

Annex C (informative): Change history	3357