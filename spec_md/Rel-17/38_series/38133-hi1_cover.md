| 3GPP TS 38.133 V17.18.1 (2025-06)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 3GPP TS 38.133 V17.18.1 (2025-06)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Technical Specification                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Technical Specification                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 3rd Generation Partnership Project; Technical Specification Group Radio Access Network; NR; Requirements for support of radio resource management (Release 17)                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 3rd Generation Partnership Project; Technical Specification Group Radio Access Network; NR; Requirements for support of radio resource management (Release 17)                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP. The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification. Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices. | The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP. The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification. Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices. |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3GPP Postal address  3GPP support office address 650 Route des Lucioles - Sophia Antipolis Valbonne - FRANCE Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16 Internet http://www.3gpp.org                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Copyright Notification No part may be reproduced except as authorized by written permission. The copyright and the foregoing restriction extend to reproduction in all media.  © 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC). All rights reserved.  UMTS™ is a Trade Mark of ETSI registered for the benefit of its members 3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners GSM® and the GSM logo are registered and owned by the GSM Association |

## Contents

Foreword	120

1	Scope	122

2	References	122

3	Definitions, symbols and abbreviations	123

3.1	Definitions	123

3.2	Symbols	125

3.3	Abbreviations	126

3.4	Test tolerances	128

3.5	Frequency bands grouping	128

3.5.1	Introduction	128

3.5.2	NR operating bands in FR1	129

3.5.2A	NR operating bands for satellite access in FR1	129

3.5.3	NR operating bands in FR2	130

3.6	Applicability of requirements in this specification version	130

3.6.1	RRC connected state requirements in DRX	131

3.6.2	Number of serving carriers	131

3.6.2.1	Number of serving carriers for SA	131

3.6.2.2	Number of serving carriers for EN-DC	131

3.6.2.3	Number of serving carriers for NE-DC	131

3.6.2.4	Number of serving carriers for NR-DC	132

3.6.3	Applicability for intra-band FR2	132

3.6.4	Applicability for FR2 UE power classes	132

3.6.5	Applicability for SDL bands	132

3.6.6	Applicability of requirements for NGEN-DC operation	132

3.6.7	Applicability of QCL	132

3.6.9	Applicability of requirements for scheduling availability	133

3.6.10	Applicability of requirements for measurement restrictions	133

3.6.11	Applicability of requirements for Redcap UEs	133

3.6.11.1	RRC connected state requirements in DRX	133

3.6.11.2	Applicability for FR2 Redcap UE power classes	133

3.6.11.3	Applicability of QCL	133

3.6.12	Applicability of requirements for Satellite Access	134

3.6.13	Applicability of requirements for FR2	134

3.6.14	Applicability of requirements for FR2 Power Class 6	134

3.6.15	Applicability of requirements for per-FR gap	134

4	SA: RRC\_IDLE state mobility	134

4.1	Cell Selection	134

4.2	Cell Re-selection	135

4.2.1	Introduction	135

4.2.2	Requirements	135

4.2.2.1	UE measurement capability	135

4.2.2.2	Measurement and evaluation of serving cell	135

4.2.2.3	Measurements of intra-frequency NR cells	138

4.2.2.4	Measurements of inter-frequency NR cells	141

4.2.2.5	Measurements of inter-RAT E-UTRAN cells	146

4.2.2.6	Maximum interruption in paging reception	149

4.2.2.7	General requirements	150

4.2.2.8	Minimum requirement at transitions	150

4.2.2.9	Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion	150

4.2.2.9.1	Introduction	150

4.2.2.9.2	Measurements for UE fulfilling low mobility criterion	151

4.2.2.9.3	Measurements for UE fulfilling not-at-cell edge criterion	153

4.2.2.9.4	Measurements for UE fulfilling low mobility and not-at-cell edge criteria	155

4.2.2.10	Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion	156

4.2.2.10.1	Introduction	156

4.2.2.10.2	Measurements for UE fulfilling low mobility criterion	156

4.2.2.10.3	Measurements for UE fulfilling not-at-cell edge criterion	159

4.2.2.10.4	Measurements for UE fulfilling low mobility and not-at-cell edge criterion	162

4.2.2.11	Measurements of inter-RAT E-UTRAN cells for UE configured with relaxed measurement criterion	162

4.2.2.11.1	Introduction	162

4.2.2.11.2	Measurements for UE fulfilling low mobility criterion	163

4.2.2.11.3	Measurements for UE fulfilling with not-at-cell edge criterion	165

4.2.2.11.4	Measurements for UE fulfilling low mobility and not-at-cell edge criterion	166

4.2A	Cell Re-selection when subject to CCA	167

4.2A.1	Introduction	167

4.2A.2	Requirements	167

4.2A.2.1	UE measurement capability	167

4.2A.2.2	Measurement and evaluation when subject to CCA on the serving cell	168

4.2A.2.3	Measurements of intra-frequency NR cells when subject to CCA on the serving cell and target cell	168

4.2A.2.4	Measurements of inter-frequency NR cells when subject to CCA on the target cell	170

4.2A.2.5	Measurements of inter-RAT E-UTRAN cells when subject to CCA on the serving cell	172

4.2A.2.6	Maximum interruption in paging reception when subject to CCA on the target cell	172

4.2A.2.7	General requirements	172

4.2B	Cell Re-selection for RedCap	173

4.2B.1	Introduction	173

4.2B.2	Requirements	173

4.2B.2.1	UE measurement capability for RedCap	173

4.2B.2.1.1	UE measurement capability for 1 Rx RedCap	173

4.2B.2.1.2	UE measurement capability for 2 Rx RedCap	173

4.2B.2.2	Measurement and evaluation of serving cell for RedCap UE	173

4.2B.2.3	Measurements of intra-frequency NR cells for RedCap UE	175

4.2B.2.4	Measurements of inter-frequency NR cells for RedCap UE	178

4.2B.2.5	Measurements of inter-RAT E-UTRAN cells for RedCap UE	181

4.2B.2.6	Maximum interruption in paging reception for RedCap	183

4.2B.2.7	General requirements for RedCap	183

4.2B.2.8	Minimum requirement at transitions	183

4.2B.2.9	Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion for RedCap	184

4.2B.2.9.1	Introduction	184

4.2B.2.9.2	Measurements for UE fulfilling stationary criterion	185

4.2B.2.9.3	Measurements for a UE fulfilling not-at-cell edge while stationary criterion	188

4.2B.2.9.3A	Measurements for a UE fulfilling stationary and not-at-cell-edge criteria	188

4.2B.2.9.4	Measurements for a UE fulfilling low mobility and stationary criteria	188

4.2B.2.9.5	Measurements for a UE fulfilling low mobility and not-at-cell-edge while stationary criteria	189

4.2B.2.9.6	Measurements for a UE fulfilling not-at-cell edge and not-at-cell edge while stationary criteria	189

4.2B.2.9.7	Measurements for a UE fulfilling low mobility and not-at-cell edge criteria and not-at-cell-edge while stationary criteria	189

4.2B.2.9.8	Measurements for a UE fulfilling low mobility, not-at-cell edge and stationary criterion	189

4.2B.2.9.9	Measurements for UE fulfilling low mobility criterion	190

4.2B.2.9.10	Measurements for UE fulfilling not-at-cell edge criterion	193

4.2B.2.9.11	Measurements for UE fulfilling low mobility and not-at-cell edge criteria	195

4.2B.2.10	Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion	195

4.2B.2.10.1	Introduction	195

4.2B.2.10.2	Measurements for UE fulfilling stationary criterion	196

4.2B.2.10.3	Measurements for a UE fulfilling not-at-cell edge while stationary criterion	198

4.2B.2.10.3A	Measurements for a UE fulfilling stationary and not-at-cell-edge-criterion	199

4.2B.2.10.4	Measurements for a UE fulfilling low mobility and stationary criteria	199

4.2B.2.10.5	Measurements for a UE fulfilling low mobility and not-at-cell-edge while stationary criteria	200

4.2B.2.10.6	Measurements for a UE fulfilling not-at-cell edge and not-at-cell edge while stationary criteria	200

4.2B.2.10.7	Measurements for a UE fulfilling low mobility and not-at-cell edge criteria and not-at-cell-edge while stationary criteria	200

4.2B.2.10.8	Measurements for a UE fulfilling low mobility, not-at-cell edge and stationary criteria	200

4.2B.2.10.9	Measurements for UE fulfilling low mobility criterion	201

4.2B.2.10.10	Measurements for UE fulfilling not-at-cell edge criterion	203

4.2B.2.10.11	Measurements for UE fulfilling low mobility and not-at-cell edge criterion	206

4.2B.2.11	Measurements of inter-RAT E-UTRAN cells for UE configured with relaxed measurement criterion	206

4.2B.2.11.1	Introduction	206

4.2B.2.11.2	Measurements for UE fulfilling stationary criterion	207

4.2B.2.11.3	Measurements for a UE not-at-cell edge while stationary criterion	208

4.2B.2.11.3A	Measurements for a UE fulfilling stationary and not-at-cell-edge criterion	208

4.2B.2.11.4	Measurements for a UE fulfilling low mobility and stationary criteria	209

4.2B.2.11.5	Measurements for a UE fulfilling low mobility and stationary not-at-cell-edge while stationary criteria	209

4.2B.2.11.6	Measurements for a UE fulfilling not-at-cell edge and not-at-cell edge while stationary criteria	209

4.2B.2.11.7	Measurements for a UE fulfilling low mobility and not-at-cell edge criteria and not-at-cell-edge while stationary criteria	210

4.2B.2.11.8	Measurements for a UE fulfilling low mobility, not-at-cell edge and stationary criteria	210

4.2B.2.11.9	Measurements for UE fulfilling low mobility criterion	210

4.2B.2.11.10	Measurements for UE fulfilling with not-at-cell edge criterion	212

4.2B.2.11.11	Measurements for UE fulfilling low mobility and not-at-cell edge criterion	213

4.2C	Cell Re-selection for NR UE for Satellite Access	213

4.2C.1	Introduction	213

4.2C.2	Requirements	214

4.2C.2.1	UE measurement capability	214

4.2C.2.2	Measurement and evaluation of serving cell	214

4.2C.2.3	Measurements of intra-frequency NR cells	215

4.2C.2.4	Measurements of inter-frequency NR cells	217

4.2C.2.5	Maximum interruption in paging reception	220

4.2C.2.6	Minimum requirement at transitions	221

4.2C.2.7	Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion	221

4.2C.2.8	Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion	221

4.2C.2.9	General requirements	221

4.3	Minimization of Drive Tests (MDT)	221

4.3.1	Introduction	221

4.3.2	Measurement Requirements	222

4.3.3	Requirements for Relative Time Stamp Accuracy	222

4.3.4	Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting	222

4.3.5	Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting	223

4.3C	Minimization of Drive Tests (MDT) for Satellite Access	223

4.3C.1	Introduction	223

4.3C.2	Measurement Requirements	223

4.3C.3	Requirements for Relative Time Stamp Accuracy	224

4.3C.4	Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting	224

4.3C.5	Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting	224

4.4	Idle Mode CA/DC Measurements	225

4.4.1	Introduction	225

4.4.2	Measurement Requirements	225

4.4.2.1	Detected cell requirement during state transition and Idle mode	225

4.4.2.2	Measurements of inter-frequency CA/DC candidate cells	225

4.4.2.3	Measurements on serving cell	227

4.4.2.4	Measurements of E-UTRAN inter-RAT DC candidate cells	227

5	SA: RRC\_INACTIVE state mobility	228

5.1	Cell Re-selection	228

5.1.1	Introduction	228

5.1.2	Requirements	228

5.1.2.1	UE measurement capability	228

5.1.2.2	Measurement and evaluation of serving cell	228

5.1.2.3	Measurements of intra-frequency NR cells	229

5.1.2.4	Measurements of inter-frequency NR cells	230

5.1.2.5	Measurements of inter-RAT E-UTRAN cells	231

5.1.2.6	Maximum interruption in paging reception	232

5.1.2.7	General requirements	232

5.1.2.8	Minimum requirement at transitions	232

5.1.2.9	Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion	232

5.1.2.10	Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion	233

5.1.2.11	Measurements of inter-RAT E-UTRAN cells for UE configured with relaxed measurement criterion	234

5.1A	Cell Re-selection with CCA	235

5.1A.1	Introduction	235

5.1A.2	Requirements	235

5.1A.2.1	UE measurement capability	235

5.1A.2.2	Measurement and evaluation when CCA is used on the serving cell	235

5.1A.2.3	Measurements of intra-frequency NR cells when CCA is used on the serving cell and target cell	235

5.1A.2.4	Measurements of inter-frequency NR cells when CCA is used on the target cell	235

5.1A.2.5	Measurements of inter-RAT E-UTRAN cells when CCA is used on the serving cell	235

5.1A.2.6	Maximum interruption in paging reception when CCA is used on the target cell	235

5.1A.2.7	General requirements	235

5.1B	Cell Re-selection for RedCap	235

5.1B.1	Introduction	235

5.1B.2	Requirements	236

5.1B.2.1	UE measurement capability	236

5.1B.2.2	Measurement and evaluation of serving cell	236

5.1B.2.3	Measurements of intra-frequency NR cells	237

5.1B.2.4	Measurements of inter-frequency NR cells	238

5.1B.2.5	Measurements of inter-RAT E-UTRAN cells	238

5.1B.2.6	Maximum interruption in paging reception	239

5.1B.2.7	General requirements	239

5.1B.2.8	Minimum requirement at transitions	239

5.1B.2.9	Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion	239

5.1B.2.10	Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion	240

5.1B.2.11	Measurements of inter-RAT E-UTRAN cells for UE configured with relaxed measurement criterion	241

5.1C	Cell Re-selection	242

5.1C.1	Introduction	242

5.1C.2	Requirements	242

5.1C.2.1	UE measurement capability	242

5.1C.2.2	Measurement and evaluation of serving cell	242

5.1C.2.3	Measurements of intra-frequency NR cells	242

5.1C.2.4	Measurements of inter-frequency NR cells	243

5.1C.2.5	Maximum interruption in paging reception	243

5.1C.2.6	General requirements	243

5.2	Void	243

5.2B	Configured Grant based Small Data Transmissions (CG-SDT) for RedCap	243

5.2B.1	Introduction	243

5.2B.2	Requirements on UE synchronization for small data transmissions for RedCap	243

5.2B.2.1	Void	243

5.2B.3	TA validation requirements for RedCap	243

5.2B.3.1	Void	244

5.2B.3.2	Void	244

5.2B.4	Scheduling restriction	244

5.2B.5	Applicability conditions for CG-SDT for RedCap	245

5.3	Minimization of Drive Tests (MDT)	245

5.3.1	Introduction	245

5.3.2	Measurement Requirements	245

5.3.3	Requirements for Relative Time Stamp Accuracy	245

5.3.4	Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting	245

5.3.5	Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting	245

5.3.6	Requirements for Relative Time Stamp Accuracy for RRC Resume Failure Log Reporting	246

5.3C	Minimization of Drive Tests (MDT) for Satellite Access	246

5.3C.1	Introduction	246

5.3C.2	Measurement Requirements	246

5.3C.3	Requirements for Relative Time Stamp Accuracy	246

5.3C.4	Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting	246

5.3C.5	Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting	246

5.3C.6	Requirements for Relative Time Stamp Accuracy for RRC Resume Failure Log Reporting	247

5.4	Inactive Mode CA/DC Measurements	247

5.4.1	Introduction	247

5.4.2	Measurement Requirements	247

5.4.2.1	Detected cell requirement during state transition and inactive mode	247

5.4.2.2	Measurements of inter-frequency CA/DC candidate cells	247

5.4.2.3	Measurements on serving cell	247

5.4.2.4	Measurements on E-UTRAN inter-RAT DC candidate cells	247

5.5	Configured Grant based Small Data Transmissions (CG-SDT)	247

5.5.1	Introduction	247

5.5.2	Requirements on UE synchronization for small data transmissions	247

5.5.3	TA validation requirements	248

5.5.4	Scheduling restriction	249

5.5.4.1	Scheduling availability of UE performing measurements in TDD bands on FR1	249

5.5.4.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	249

5.5.4.3	Scheduling availability of UE performing measurements on FR2	249

5.5.5	Applicability conditions for SDT	250

5.6	NR measurements for positioning	250

5.6.1	Introduction	250

5.6.2	RSTD measurements	251

5.6.2.1	Introduction	251

5.6.2.2	Requirements Applicability	251

5.6.2.3	Measurement Capability	251

5.6.2.5	Measurements Period Requirements	252

5.6.3	PRS-RSRP measurements	254

5.6.3.1	Introduction	254

5.6.3.2	Requirements applicability	254

5.6.3.3	Measurement Capability	255

5.6.3.4	Measurement Reporting Requirements	255

5.6.3.5	Measurement Period Requirements	255

5.6.4	UE Rx-Tx time difference measurements	257

5.6.4.1	Introduction	257

5.6.4.2	Requirements Applicability	257

5.6.4.3	Measurement Capability	258

5.6.4.4	Measurement Reporting Requirements	258

5.6.4.5	Measurement Period Requirements	258

5.6.5	PRS-RSRPP measurements	261

5.6.5.1	Introduction	261

5.6.5.2	Requirements Applicability	261

5.6.5.3	Measurement Capability	261

5.6.5.4	Measurement Reporting Requirements	261

5.6.5.5	Measurement Period Requirements	262

5.7	Random access based Small Data Transmissions (RA-SDT)	263

5.7.1	Introduction	263

5.7.2	Requirements for small data transmissions based on 2-step RA	263

5.7.3	Requirements for small data transmissions based on 4-step RA	263

5.7.4	Applicability conditions for SDT	263

5.7B	Random access based Small Data Transmissions (RA-SDT) for RedCap	263

5.7B.1	Introduction	263

5.7B.2	Requirements for small data transmissions based on 2-step RA	263

5.7B.3	Requirements for small data transmissions based on 4-step RA	264

5.7B.4	Applicability conditions for RA-SDT for RedCap	264

6	RRC\_CONNECTED state mobility	264

6.1	Handover	264

6.1.1	NR Handover	264

6.1.1.1	Introduction	264

6.1.1.2	NR FR1 - NR FR1 Handover	264

6.1.1.2.1	Handover delay	264

6.1.1.2.2	Interruption time	264

6.1.1.3	NR FR2- NR FR1 Handover	265

6.1.1.3.1	Handover delay	265

6.1.1.3.2	Interruption time	265

6.1.1.4	NR FR2- NR FR2 Handover	266

6.1.1.4.1	Handover delay	266

6.1.1.4.2	Interruption time	266

6.1.1.5	NR FR1- NR FR2 Handover	267

6.1.1.5.1	Handover delay	267

6.1.1.5.2	Interruption time	267

6.1.2	NR Handover to other RATs	268

6.1.2.1	NR – E-UTRAN Handover	268

6.1.2.1.1	Introduction	268

6.1.2.1.2	Handover delay	268

6.1.2.1.3	Interruption time	268

6.1.2.2	NR – UTRAN Handover	269

6.1.2.2.1	Introduction	269

6.1.2.2.2	Handover delay	269

6.1.2.2.3	Interruption time	269

6.1.3	NR DAPS Handover	270

6.1.3.1	Introduction	270

6.1.3.2	NR FR1 - NR FR1 DAPS Handover	270

6.1.3.2.1	DAPS handover delay	271

6.1.3.2.2	Interruption time	271

6.1.3.3	NR FR2- NR FR1 DAPS Handover	273

6.1.3.3.1	DAPS handover delay	273

6.1.3.3.2	Interruption time	274

6.1.3.4	NR FR1- NR FR2 DAPS Handover	274

6.1.3.4.1	DAPS handover delay	274

6.1.3.4.2	Interruption time	275

6.1.4	NR Conditional Handover	275

6.1.4.1	Introduction	275

6.1.4.2	NR FR1 – NR FR1 conditional handover	275

6.1.4.3	NR FR2 – NR FR1 conditional handover	277

6.1.4.4	NR FR2 – NR FR2 conditional handover	277

6.1.4.4.1	Handover delay	277

6.1.4.4.2	Measurement time	277

6.1.4.4.3	Preparation time	278

6.1.4.4.4	Interruption time	278

6.1.4.5	NR FR1 – NR FR2 conditional handover	278

6.1.5	NR Handover with PSCell	278

6.1.5.1	Introduction	278

6.1.5.2	Handover with PSCell from NR SA to EN-DC	279

6.1.5.2.1	Interruption time for inter-RAT HO from NR to E-UTRAN	279

6.1.5.2.2	PSCell addition in HO with PSCell for NR SA to EN-DC	279

6.1.5.3	HO with PSCell from NE-DC to NE-DC	280

6.1.5.3.1	Handover delay	280

6.1.5.3.2	HO with PSCell - PCell Interruption time	280

6.1.5.3.3	PSCell addition/change in NE-DC to NE-DC HO with PSCell	280

6.1.5.4	HO with PSCell from NR-DC to NR-DC	281

6.1.5.5	Handover with PSCell from NR SA to EN-DC with PSCell using CCA	282

6.1.5.5.1	Introduction	282

6.1.5.5.2	NR SA to EN-DC HO with PSCell- NR to E-UTRA HO Interruption time	282

6.1.5.5.3	NR SA to EN-DC HO with PSCell - NR PSCell Addition Delay requirements	283

6.1A	Void	284

6.1A.1	Void	284

6.1A.1.1	Void	284

6.1A.1.2	Void	284

6.1A.1.2.1	Void	284

6.1A.1.2.2	Void	284

6.1B	Handover to target cell using CCA	284

6.1B.1	NR Handover	284

6.1B.1.1	Introduction	284

6.1B.1.2	NR FR1 - NR FR1 Handover	284

6.1B.1.2.1	Handover delay	284

6.1B.1.2.2	Interruption time	284

6.1B.1.3	NR FR2-2 NR FR2-2 Handover	285

6.1B.1.3.1	Handover delay	285

6.1B.1.3.2	Interruption time	285

6.1B.1.4	NR FR1- NR FR2-2 Handover	286

6.1B.1.4.1	Handover delay	286

6.1B.1.4.2	Interruption time	287

6.1C	Handover for SAN	288

6.1C.1	NR SAN Handover	288

6.1C.1.1	Introduction	288

6.1C.1.2	NR SAN FR1 – NR SAN FR1 Handover	288

6.1C.1.2.1	Handover delay	288

6.1C.1.2.2	Interruption time	288

6.1C.2	NR SAN Conditional Handover	289

6.1C.2.1	Introduction	289

6.1C.2.2	NR SAN FR1 – NR SAN FR1 conditional handover	289

6.1C.2.2.1	Handover delay	289

6.1C.2.2.2	Measurement time	289

6.1C.2.2.3	Preparation time	291

6.1C.2.2.4	Interruption time	291

6.1D	Handover for RedCap	291

6.1D.1	NR Handover	291

6.1D.1.1	Introduction	291

6.1D.1.2	NR FR1 - NR FR1 Handover	292

6.1D.1.2.1	Handover delay	292

6.1D.1.2.2	Interruption time	292

6.1D.1.3	NR FR2- NR FR2 Handover	293

6.1D.1.3.1	Handover delay	293

6.1D.1.3.2	Interruption time	293

6.1D.2	NR Handover to other RATs	295

6.1D.2.1	NR – E-UTRAN Handover	295

6.2	RRC Connection Mobility Control	295

6.2.1	SA: RRC Re-establishment	295

6.2.1.1	Introduction	295

6.2.1.2	Requirements	295

6.2.1.2.1	UE Re-establishment delay requirement	295

6.2.1A	RRC Re-establishment with CCA	297

6.2.1A.1	Introduction	297

6.2.1A.2	Requirements	297

6.2.1A.2.1	UE Re-establishment with CCA delay requirement	298

6.2.1B	SA: RRC Re-establishment for RedCap	299

6.2.1B.1	Introduction	299

6.2.1B.2	Requirements	300

6.2.2	Random access	300

6.2.2.1	Introduction	300

6.2.2.2	Requirements for 4-step RA type	300

6.2.2.2.1	Contention based random access	301

6.2.2.2.1.1	Correct behaviour when transmitting Random Access Preamble	301

6.2.2.2.1.2	Correct behaviour when receiving Random Access Response	301

6.2.2.2.1.3	Correct behaviour when not receiving Random Access Response	301

6.2.2.2.1.4	Correct behaviour when receiving an UL grant for msg3 retransmission	301

6.2.2.2.1.5	SA: Correct behaviour when receiving a message over Temporary C-RNTI	301

6.2.2.2.1.6	Correct behaviour when contention Resolution timer expires	301

6.2.2.2.2	Non-Contention based random access	301

6.2.2.2.2.1	Correct behaviour when transmitting Random Access Preamble	301

6.2.2.2.2.2	Correct behaviour when receiving Random Access Response	302

6.2.2.2.2.3	Correct behaviour when not receiving Random Access Response	302

6.2.2.2.3	UE behaviour when configured with supplementary UL	302

6.2.2.3	Requirements for 2-step RA type	302

6.2.2.3.1	Contention based random access	303

6.2.2.3.1.1	Correct behaviour when transmitting MsgA	303

6.2.2.3.1.2	Correct behaviour when receiving MsgB	303

6.2.2.3.1.3	Correct behaviour when not receiving MsgB	303

6.2.2.3.2	Non-Contention based random access	304

6.2.2.3.2.1	Correct behaviour when transmitting MsgA	304

6.2.2.3.2.2	Correct behaviour when receiving MsgB	304

6.2.2.3.2.3	Correct behaviour when not receiving MsgB	304

6.2.2.3.3	UE behaviour when configured with supplementary UL	304

6.2.2A	Random access when CCA is used on target frequency	304

6.2.2A.1	Introduction	304

6.2.2A.2	Requirements for 4-step RA type	305

6.2.2A.2.1	Contention based random access	305

6.2.2A.2.1.1	Correct behaviour when transmitting Random Access Preamble	305

6.2.2A.2.1.2	Correct behaviour when receiving Random Access Response	305

6.2.2A.2.1.3	Correct behaviour when not receiving Random Access Response	305

6.2.2A.2.1.4	Correct behaviour when receiving an UL grant for msg3 retransmission	306

6.2.2A.2.1.6	Correct behaviour when contention Resolution timer expires	306

6.2.2A.2.2	Non-Contention based random access	306

6.2.2A.2.2.1	Correct behaviour when transmitting Random Access Preamble	306

6.2.2A.2.2.2	Correct behaviour when receiving Random Access Response	306

6.2.2A.2.2.3	Correct behaviour when not receiving Random Access Response	307

6.2.2A.3	Requirements for 2-step RA type	307

6.2.2A.3.1	Contention based random access	307

6.2.2A.3.1.1	Correct behaviour when transmitting MsgA	307

6.2.2A.3.1.2	Correct behaviour when receiving MsgB	308

6.2.2A.3.1.3	Correct behaviour when not receiving MsgB	308

6.2.2A.3.2	Non-Contention based random access	308

6.2.2A.3.2.1	Correct behaviour when transmitting MsgA	308

6.2.2A.3.2.2	Correct behaviour when receiving MsgB	309

6.2.2A.3.2.3	Correct behaviour when not receiving MsgB	309

6.2.2B	Random access for RedCap	309

6.2.2B.1	Introduction	309

6.2.2B.2	Requirements	310

6.2.3	SA: RRC Connection Release with Redirection	310

6.2.3.1	Introduction	310

6.2.3.2	Requirements	310

6.2.3.2.1	RRC connection release with redirection to NR	310

6.2.3.2.2	RRC connection release with redirection to E-UTRAN	311

6.2.3.2.3	RRC connection release with redirection to NR carrier subject to CCA	312

6.2.3A	SA: RRC Connection Release with Redirection for RedCap	313

6.2.3A.1	Introduction	313

6.2.3A.2	Requirements	313

6.2.3A.2.1	RRC connection release with redirection to NR	313

6.2.3A.2.2	RRC connection release with redirection to E-UTRAN	313

6.2C	RRC Connection Mobility Control for Satellite Access	313

6.2C.1	SA: RRC Re-establishment for Satellite Access	313

6.2C.1.1	Introduction	313

6.2C.1.2	Requirements	314

6.2C.1.2.1	UE Re-establishment delay requirement	314

6.2C.2	Random access for satellite access	315

6.2C.2.1	Introduction	315

6.2C.2.2	Requirements for 4-step RA type	315

6.2C.2.2.1	Contention based random access	316

6.2C.2.2.1.1	Correct behaviour when transmitting Random Access Preamble	316

6.2C.2.2.1.2	Correct behaviour when receiving Random Access Response	316

6.2C.2.2.1.3	Correct behaviour when not receiving Random Access Response	316

6.2C.2.2.1.4	Correct behaviour when receiving an UL grant for msg3 retransmission	316

6.2C.2.2.1.5	SA: Correct behaviour when receiving a message over Temporary C-RNTI	316

6.2C.2.2.1.6	Correct behaviour when contention Resolution timer expires	316

6.2C.2.2.2	Non-Contention based random access	316

6.2C.2.2.2.1	Correct behaviour when transmitting Random Access Preamble	316

6.2C.2.2.2.2	Correct behaviour when receiving Random Access Response	317

6.2C.2.2.2.3	Correct behaviour when not receiving Random Access Response	317

6.2C.2.3	Requirements for 2-step RA type	317

6.2C.2.3.1	Contention based random access	318

6.2C.2.3.1.1	Correct behaviour when transmitting MsgA	318

6.2C.2.3.1.2	Correct behaviour when receiving MsgB	318

6.2C.2.3.1.3	Correct behaviour when not receiving MsgB	318

6.2C.2.3.2	Non-Contention based random access	318

6.2C.2.3.2.1	Correct behaviour when transmitting MsgA	318

6.2C.2.3.2.2	Correct behaviour when receiving MsgB	319

6.2C.2.3.2.3	Correct behaviour when not receiving MsgB	319

6.2C.3	SA: RRC Connection Release with Redirection for Satellite Access	319

6.2C.3.1	Introduction	319

6.2C.3.2	Requirements	319

6.2C.3.2.1	RRC connection release with redirection to NR	319

7	Timing	320

7.1	UE transmit timing	320

7.1.1	Introduction	320

7.1.2	Requirements	320

7.1.2.1	Gradual timing adjustment	322

7.1.2.2	Void	323

7.1.2.3	One shot large UL timing adjustment for FR2 Power Class 6 UE	323

7.1A	UE transmit timing for RedCap	323

7.1A.1	Introduction	323

7.1A.2	Requirements	324

7.1A.2.1	Gradual timing adjustment	325

7.1C	UE transmit timing for Satellite Access	325

7.1C.1	Introduction	325

7.1C.2	Requirements	325

7.1C.2.1	Gradual timing adjustment	326

7.2	UE timer accuracy	327

7.2.1	Introduction	327

7.2.2	Requirements	327

7.2A	UE timer accuracy for RedCap	327

7.2A.1	Introduction	327

7.2A.2	Requirements	327

7.2C	UE timer accuracy for satellite access	327

7.2C.1	Introduction	327

7.2C.2	Requirements	328

7.3	Timing advance	328

7.3.1	Introduction	328

7.3.2	Requirements	328

7.3.2.1	Timing Advance adjustment delay	328

7.3.2.2	Timing Advance adjustment accuracy	328

7.3A	Timing Advance for RedCap	328

7.3A.1	Introduction	328

7.3A.2	Requirements	329

7.3A.2.1	Timing Advance adjustment delay	329

7.3A.2.2	Timing Advance adjustment accuracy	329

7.3C	Timing advance for satellite access	329

7.3C.1	Introduction	329

7.3C.2	Requirements	329

7.3C.2.1	Timing Advance adjustment delay	329

7.3C.2.2	Timing Advance adjustment accuracy	329

7.4	Cell phase synchronization accuracy	330

7.4.1	Definition	330

7.4.2	Minimum requirements	330

7.5	Maximum Transmission Timing Difference	330

7.5.1	Introduction	330

7.5.2	Minimum Requirements for inter-band EN-DC	330

7.5.2.1	Minimum Requirements for inter-band synchronous EN-DC	331

7.5.3	Minimum Requirements for intra-band EN-DC	331

7.5.4	Minimum Requirements for NR Carrier Aggregation	332

7.5.5	Minimum Requirements for inter-band NE-DC	332

7.5.5.1	Minimum Requirements for inter-band synchronous NE-DC	333

7.5.6	Minimum Requirements for inter-band NR DC	333

7.6	Maximum Receive Timing Difference	334

7.6.1	Introduction	334

7.6.2	Minimum Requirements for inter-band EN-DC	334

7.6.2.1	Minimum Requirements for inter-band synchronous EN-DC	335

7.6.3	Minimum Requirements for intra-band EN-DC	335

7.6.4	Minimum Requirements for NR Carrier Aggregation	336

7.6.5	Minimum Requirements for inter-band NE-DC	337

7.6.5.1	Minimum Requirements for inter-band synchronous NE-DC	337

7.6.6	Minimum Requirements for inter-band NR DC	337

7.7 *deriveSSB-IndexFromCell* tolerance	338

7.7.1	Minimum requirements	338

7.7A	deriveSSB-IndexFromCell tolerance for RedCap	339

7.7A.1	Minimum requirements	339

7.8	Void	339

7.9 *deriveSSB-IndexFromCellInter-r17* tolerance	339

7.9.1	Minimum requirements	339

8	Signalling characteristics	340

8.1	Radio Link Monitoring	340

8.1.1	Introduction	340

8.1.1.1	Introduction of Requirement on Radio Link Monitoring for UE Configured with Relaxed Measurement Criteria	341

8.1.2	Requirements for SSB based radio link monitoring	341

8.1.2.1	Introduction	342

8.1.2.2	Minimum requirement	342

8.1.2.3	Measurement restrictions for SSB based RLM	346

8.1.2.4	Minimum requirement of SSB based radio link monitoring for UE fulfilling relaxed measurement criteria	346

8.1.3	Requirements for CSI-RS based radio link monitoring	347

8.1.3.1	Introduction	347

8.1.3.2	Minimum requirement	348

8.1.3.3	Measurement restrictions for CSI-RS based RLM	351

8.1.3.4	Minimum requirement of CSI-RS based radio link monitoring for UE fulfilling relaxed measurement criteria	352

8.1.4	Minimum requirement at transitions	353

8.1.5	Minimum requirement for UE turning off the transmitter	353

8.1.6	Minimum requirement for L1 indication	353

8.1.7	Scheduling availability of UE during radio link monitoring	354

8.1.7.1	Scheduling availability of UE performing radio link monitoring with a same subcarrier spacing as PDSCH/PDCCH on FR1	354

8.1.7.2	Scheduling availability of UE performing radio link monitoring with a different subcarrier spacing than PDSCH/PDCCH on FR1	354

8.1.7.3	Scheduling availability of UE performing radio link monitoring on FR2	354

8.1.7.4	Scheduling availability of UE performing radio link monitoring on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC	355

8.1A	Radio Link Monitoring with CCA on Target Frequency	355

8.1A.1	Introduction	355

8.1A.2	Requirements for SSB Based Radio Link Monitoring	356

8.1A.2.1	Introduction	356

8.1A.2.2	Minimum Requirement	357

8.1A.3	Minimum requirement at transitions	360

8.1A.4	Minimum requirement for UE turning off the transmitter	361

8.1A.5	Minimum requirement for L1 indication	361

8.1A.6	Scheduling availability of UE during radio link monitoring	361

8.1A.6.3	Scheduling availability of UE performing radio link monitoring on FR2-2	361

8.1A.6.4	Scheduling availability of UE performing radio link monitoring on FR1 or FR2-2 in case of FR1-FR2-2 inter-band CA and NR-DC	362

8.1B	Radio Link Monitoring for RedCap	362

8.1B.1	Introduction	362

8.1B.2	Requirements for SSB based radio link monitoring	363

8.1B.2.1	Introduction	363

8.1B.2.2	Minimum requirement	364

8.1B.2.3	Measurement restrictions for SSB based RLM	366

8.1B.3	Requirements for CSI-RS based radio link monitoring	367

8.1B.3.1	Introduction	367

8.1B.3.2	Minimum requirement	367

8.1B.3.3	Measurement restrictions for CSI-RS based RLM	370

8.1B.4	Minimum requirement at transitions	371

8.1B.5	Minimum requirement for UE turning off the transmitter	371

8.1B.6	Minimum requirement for L1 indication	371

8.1B.7	Scheduling availability of UE during radio link monitoring	371

8.1B.7.1	Scheduling availability of UE performing radio link monitoring with a same subcarrier spacing as PDSCH/PDCCH on FR1	372

8.1B.7.2	Scheduling availability of UE performing radio link monitoring with a different subcarrier spacing than PDSCH/PDCCH on FR1	372

8.1B.7.3	Scheduling availability of UE performing radio link monitoring on FR2	372

8.1C	Radio Link Monitoring for Satellite Access	372

8.1C.1	Introduction	372

8.1C.2	Requirements for SSB based radio link monitoring	373

8.1C.2.1	Introduction	373

8.1C.2.2	Minimum requirement	374

8.1C.2.3	Measurement restrictions for SSB based RLM	375

8.1C.3	Requirements for CSI-RS based radio link monitoring	375

8.1C.3.1	Introduction	375

8.1C.3.2	Minimum requirement	376

8.1C.3.3	Measurement restrictions for CSI-RS based RLM	377

8.1C.4	Minimum requirement at transitions	378

8.1C.5	Minimum requirement for UE turning off the transmitter	378

8.1C.6	Minimum requirement for L1 indication	378

8.1C.7	Scheduling availability of UE during radio link monitoring	378

8.1C.7.1	Scheduling availability of UE performing radio link monitoring with a same subcarrier spacing as PDSCH/PDCCH on FR1	379

8.1C.7.2	Scheduling availability of UE performing radio link monitoring with a different subcarrier spacing than PDSCH/PDCCH on FR1	379

8.2	Interruption	379

8.2.1	EN-DC Interruption	379

8.2.1.1	Introduction	379

8.2.1.2	Requirements	380

8.2.1.2.1	Interruptions at transitions between active and non-active during DRX	380

8.2.1.2.2	Interruptions at transitions from non-DRX to DRX	380

8.2.1.2.3	Interruptions at SCell addition/release	380

8.2.1.2.4	Interruptions at SCell activation/deactivation	381

8.2.1.2.5	Interruptions during measurements on SCC	383

8.2.1.2.5.1	Interruptions during measurements on deactivated NR SCC	383

8.2.1.2.5.2	Interruptions during measurements on deactivated E-UTRAN SCC	383

8.2.1.2.5.3	Interruptions during CQI measurements on dormant E-UTRAN SCell	383

8.2.1.2.5.4	Interruptions during RRM measurements on dormant E-UTRAN SCC	384

8.2.1.2.6	Interruptions at UL carrier RRC reconfiguration	384

8.2.1.2.7	Interruptions due to Active BWP switching Requirement	385

8.2.1.2.8	Interruptions at direct SCell activation and hibernation	386

8.2.1.2.8.1	Interruptions during direct SCell activation and hibernation of E-UTRA SCell	386

8.2.1.2.8.2	Interruptions during direct SCell activation	386

8.2.1.2.9	Interruptions at SCell hibernation	386

8.2.1.2.10	Interruptions at SCell activation/deactivation with multiple downlink SCells	387

8.2.1.2.11	Interruptions due to UE-specific CBW change	387

8.2.1.2.12	Interruptions at NR SRS carrier based switching	387

8.2.1.2.13	Interruptions at E-UTRA SRS carrier based switching	389

8.2.1.2.14	DL Interruptions at switching between two uplink carriers	390

8.2.1.2.15	Interruptions due to SCell dormancy	390

8.2.1.2.15.1	Interruptions due to SCell dormancy switch	390

8.2.1.2.15.2	Interruptions due to CQI measurements during SCell dormancy	390

8.2.1.2.15.3	Interruptions due to RRM measurements during SCell dormancy	391

8.2.1.2.16	Interruptions when identifying CGI of an NR cell with autonomous gaps	391

8.2.1.2.17	Interruptions when identifying CGI of an E-UTRA cell with autonomous gaps	391

8.2.1.2.18	Interruptions at NR SRS antenna port switching	392

8.2.1.2.19	Interruptions at fast SCell activation	393

8.2.1.2.20	Interruptions due to PUCCH SCell activation/deactivation	394

8.2.2	SA: Interruptions with Standalone NR Carrier Aggregation	394

8.2.2.1	Introduction	394

8.2.2.2	Requirements	395

8.2.2.2.1	Interruptions at SCell addition/release	395

8.2.2.2.2	Interruptions at SCell activation/deactivation	396

8.2.2.2.3	Interruptions during measurements on deactivated SCC	397

8.2.2.2.4	Interruptions at UL carrier RRC reconfiguration	398

8.2.2.2.5	Interruptions due to Active BWP switching Requirement	398

8.2.2.2.6	Interruptions at inter-frequency SFTD measurement	399

8.2.2.2.7	Interruptions at SCell activation/deactivation with multiple downlink SCells	401

8.2.2.2.8	Interruptions due to UE-specific CBW change	401

8.2.2.2.9	Interruptions at NR SRS carrier based switching	401

8.2.2.2.10	DL Interruptions at UE switching between two uplink carriers	403

8.2.2.2.10A	DL Interruptions at UE switching between two uplink carriers with two transmit antenna connectors	403

8.2.2.2.10B	DL Interruptions at UE switching between one uplink band with one transmit antenna connector and one uplink band with two transmit antenna connectors	404

8.2.2.2.10C	DL Interruptions at UE switching between two uplink bands with two transmit antenna connectors	404

8.2.2.2.11	Interruptions at direct SCell activation	404

8.2.2.2.12	Interruptions due to SCell dormancy	405

8.2.2.2.12.1	Interruptions due to SCell dormancy switch	405

8.2.2.2.12.2	Interruptions due to CQI measurements during SCell dormancy	405

8.2.2.2.12.3	Interruptions due to RRM measurements during SCell dormancy	405

8.2.2.2.13	Interruptions at transitions between active and non-active during DRX	405

8.2.2.2.14	Interruptions when identifying CGI of an NR cell with autonomous gaps	405

8.2.2.2.15	Interruptions when identifying CGI of an E-UTRA cell with autonomous gaps	406

8.2.2.2.16	Interruptions at NR SRS antenna port switching	406

8.2.2.2.17	Interruptions at fast SCell activation	407

8.2.2.2.18	Interruptions due to PUCCH SCell activation/deactivation	408

8.2.3	NE-DC Interruptions	408

8.2.3.1	Introduction	408

8.2.3.2	Requirements	409

8.2.3.2.1	Interruptions at transitions between active and non-active during DRX	409

8.2.3.2.2	Interruptions at transitions from non-DRX to DRX	409

8.2.3.2.3	Interruptions at PSCell/SCell addition/release	409

8.2.3.2.4	Interruptions at SCell activation/deactivation	410

8.2.3.2.5	Interruptions during measurements on SCC	412

8.2.3.2.5.1	Interruptions during measurements on deactivated NR SCC	412

8.2.3.2.5.2	Interruptions during measurements on deactivated E-UTRAN SCC	412

8.2.3.2.5.3	Interruptions during CQI measurements on dormant E-UTRAN SCC	412

8.2.3.2.5.4	Interruptions during RRM measurements on dormant E-UTRAN SCC	412

8.2.3.2.6	Interruptions at UL carrier RRC reconfiguration	413

8.2.3.2.7	Interruptions due to Active BWP switching Requirement	413

8.2.3.2.8	Interruptions at direct SCell activation and hibernation	413

8.2.3.2.9	Interruptions at SCell hibernation	414

8.2.3.2.10	Interruptions at SCell activation/deactivation with multiple downlink SCells	414

8.2.3.2.11	 Interruptions at NR SRS carrier based switching	414

8.2.3.2.12	 Interruptions at E-UTRA SRS carrier based switching	416

8.2.3.2.13	Interruptions due to SCell dormancy	416

8.2.3.2.14	Interruptions when identifying CGI of an NR cell with autonomous gaps	417

8.2.3.2.15	 Interruptions when identifying CGI of an E-UTRA cell with autonomous gaps	417

8.2.3.2.17	Interruptions at fast SCell activation	419

8.2.3.2.18	Interruptions due to UE-specific CBW change	420

8.2.3.2.19	Interruptions due to PUCCH SCell activation/deactivation	420

8.2.4	NR-DC: Interruptions	420

8.2.4.1	Introduction	420

8.2.4.2	Requirements	421

8.2.4.2.1	Interruptions at PSCell/SCell addition/release	421

8.2.4.2.2	Interruptions at SCell activation/deactivation	422

8.2.4.2.3	Interruptions during measurements on SCC	423

8.2.4.2.4	Interruptions at UL carrier RRC reconfiguration	423

8.2.4.2.5	Interruptions due to Active BWP switching Requirement	424

8.2.4.2.6	Interruptions at transitions between active and non-active during DRX	424

8.2.4.2.7	Interruptions at transitions from non-DRX to DRX	424

8.2.4.2.8	Interruptions at SCell activation/deactivation with multiple downlink SCells	425

8.2.4.2.9	Interruptions at NR SRS carrier based switching	425

8.2.4.2.10	Interruptions at direct SCell activation	426

8.2.4.2.11	Interruptions when identifying CGI of an NR cell with autonomous gaps	427

8.2.4.2.12	Interruptions when identifying CGI of an E-UTRA cell with autonomous gaps	427

8.2.4.2.13	 Interruptions due to SCell dormancy	428

8.2.4.2.14	Interruptions at NR SRS antenna port switching	428

8.2.4.2.15	Interruptions at fast SCell activation	429

8.2.4.2.16	Interruptions at SCG activation/deactivation	430

8.2.4.2.17	Interruptions due to RRM measurements on deactivated SCG	430

8.2.4.2.18 Interruptions during RLM/BFD measurements on deactivated PSCell	431

8.2.4.2.19	Interruptions due to UE-specific CBW change	431

8.2.4.2A	Void	431

8.2.4.2A.1	Void	431

8.2.4.2A.2	Void	431

8.2.4.2A.3	Void	431

8.3	SCell Activation and Deactivation Delay	431

8.3.1	Introduction	431

8.3.2	SCell Activation Delay Requirement for Deactivated SCell	431

8.3.3	SCell Deactivation Delay Requirement for Activated SCell	436

8.3.4	Direct SCell Activation at SCell addition	436

8.3.5	Direct SCell Activation at Handover	438

8.3.7	SCell Activation Delay Requirement for Deactivated SCell with Multiple Downlink SCells	440

8.3.8	SCell Deactivation Delay Requirement for Activated SCell with Multiple Downlink SCells	444

8.3.9	Direct SCell Activation of Multiple Downlink SCells at SCell addition	444

8.3.10	Direct SCell Activation of Multiple Downlink SCells at Handover	445

8.3.12	SCell Activation Delay Requirement for Deactivated PUCCH SCell	447

8.3.13	SCell activation delay Requirement for Deactivated PUCCH SCell with Multiple SCells	449

8.3.14	SCell Deactivation Delay Requirement for Activated PUCCH SCell	451

8.3.15	SCell Deactivation Delay Requirement for Activated PUCCH SCell with Multiple Downlink SCells	452

8.3.16	Fast SCell Activation Delay Requirement for Deactivated SCell	452

8.3A	SCell Activation and Deactivation Delay in Carriers with CCA	455

8.3A.1	Introduction	455

8.3A.2	SCell Activation Delay Requirement for Deactivated SCell	455

8.3A.3	SCell Deactivation Delay Requirement for Activated SCell	460

8.4	UE UL carrier RRC reconfiguration delay	460

8.4.1	Introduction	460

8.4.2	UE UL carrier configuration delay requirement	460

8.4.3	UE UL carrier deconfiguration delay requirement	460

8.5	Link Recovery Procedures	461

8.5.1	Introduction	461

8.5.1.1	Introduction of Requirement on Link Recovery Procedures for UE configured with relaxed measurement criteria	462

8.5.2	Requirements for SSB based beam failure detection	463

8.5.2.1	Introduction	463

8.5.2.2	Minimum requirement	463

8.5.2.3	Measurement restriction for SSB based beam failure detection	466

8.5.2.4	Minimum requirement of SSB based beam failure detection for UE fulfilling relaxed measurement criteria	467

8.5.3	Requirements for CSI-RS based beam failure detection	468

8.5.3.1	Introduction	468

8.5.3.2	Minimum requirement	468

8.5.3.3	Measurement restrictions for CSI-RS beam failure detection	471

8.5.3.4	Minimum requirement of CSI-RS based beam failure detection for UE fulfilling relaxed measurement criteria	472

8.5.4	Minimum requirement for L1 indication	473

8.5.5	Requirements for SSB based candidate beam detection	474

8.5.5.1	Introduction	474

8.5.5.2	Minimum requirement	474

8.5.5.3	Measurement restriction for SSB based candidate beam detection	477

8.5.6	Requirements for CSI-RS based candidate beam detection	477

8.5.6.1	Introduction	477

8.5.6.2	Minimum requirement	477

8.5.6.3	Measurement restriction for CSI-RS based candidate beam detection	480

8.5.7	Scheduling availability of UE during beam failure detection	481

8.5.7.1	Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1	481

8.5.7.2	Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH on FR1	481

8.5.7.3	Scheduling availability of UE performing beam failure detection on FR2	482

8.5.7.4	Scheduling availability of UE performing beam failure detection on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR DC	482

8.5.8	Scheduling availability of UE during candidate beam detection	482

8.5.8.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	483

8.5.8.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	483

8.5.8.3	Scheduling availability of UE performing L1-RSRP measurement on FR2	483

8.5.8.4	Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC	484

8.5.9	Requirements for Beam Failure Recovery in SCell	484

8.5.9.1	Introduction	484

8.5.9.2	Requirement	484

8.5.10	Minimum requirement at transitions for beam failure detection	484

8.5A	Link Recovery Procedures when CCA is used on target frequency	485

8.5A.1	Introduction	485

8.5A.2	Requirements for SSB based beam failure detection	485

8.5A.2.1	Introduction	485

8.5A.2.2	Minimum requirement	486

8.5A.2.3	Measurement restriction for SSB based beam failure detection	488

8.5A.3	Void	488

8.5A.4	Minimum requirement for L1 indication	488

8.5A.5	Requirements for SSB based candidate beam detection	489

8.5A.5.1	Introduction	489

8.5A.5.2	Minimum requirement	489

8.5A.5.3	Measurement restriction for SSB based candidate beam detection	491

8.5A.6	Void	492

8.5A.7	Scheduling availability of UE during beam failure detection	492

8.5A.7.1	Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH	492

8.5A.7.2	Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH	492

8.5A.7.3	Scheduling availability of UE performing beam failure detection on FR2-2	492

8.5A.7.4	Scheduling availability of UE performing beam failure detection on FR1 or FR2-2 in case of FR1-FR2-2 inter-band CA and NR DC	492

8.5A.8	Scheduling availability of UE during candidate beam detection	492

8.5A.8.3	Scheduling availability of UE performing L1-RSRP measurement on FR2-2	492

8.5A.8.4	Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2-2 in case of FR1-FR2-2 inter-band CA and NR-DC	492

8.5B	Link Recovery Procedures for Redcap	493

8.5B.1	Introduction	493

8.5B.2	Requirements for SSB based beam failure detection for Redcap	493

8.5B.2.1	Introduction	493

8.5B.2.2	Minimum requirement	494

8.5B.2.3	Measurement restriction for SSB based beam failure detection	495

8.5B.3	Requirements for CSI-RS based beam failure detection for Redcap	496

8.5B.3.1	Introduction	496

8.5B.3.2	Minimum requirement	496

8.5B.3.3	Measurement restrictions for CSI-RS beam failure detection	498

8.5B.4	Minimum requirement for L1 indication for Redcap	499

8.5B.5	Requirements for SSB based candidate beam detection for Redcap	500

8.5B.5.1	Introduction	500

8.5B.5.2	Minimum requirement	500

8.5B.5.3	Measurement restriction for SSB based candidate beam detection	502

8.5B.6	Requirements for CSI-RS based candidate beam detection for Redcap	502

8.5B.6.1	Introduction	502

8.5B.6.2	Minimum requirement	502

8.5B.6.3	Measurement restriction for CSI-RS based candidate beam detection	504

8.5B.7	Scheduling availability of UE during beam failure detection for Redcap	505

8.5B.7.1	Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1	505

8.5B.7.2	Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH on FR1	505

8.5B.7.3	Scheduling availability of UE performing beam failure detection on FR2	505

8.5B.8	Scheduling availability of UE during candidate beam detection for Redcap	506

8.5B.8.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	506

8.5B.8.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	506

8.5B.8.3	Scheduling availability of UE performing L1-RSRP measurement on FR2	506

8.5B.9	Minimum requirement at transitions for beam failure detection for Redcap	506

8.5C	Link Recovery Procedures for Satellite Access	507

8.5C.1	Introduction	507

8.5C.2	Requirements for SSB based beam failure detection	507

8.5C.2.1	Introduction	507

8.5C.2.2	Minimum requirement	508

8.5C.2.3	Measurement restriction for SSB based beam failure detection	508

8.5C.3	Requirements for CSI-RS based beam failure detection	509

8.5C.3.1	Introduction	509

8.5C.3.2	Minimum requirement	509

8.5C.3.3	Measurement restrictions for CSI-RS beam failure detection	510

8.5C.4	Minimum requirement for L1 indication	511

8.5C.5	Requirements for SSB based candidate beam detection	511

8.5C.5.1	Introduction	511

8.5C.5.2	Minimum requirement	511

8.5C.5.3	Measurement restriction for SSB based candidate beam detection	512

8.5C.6	Requirements for CSI-RS based candidate beam detection	513

8.5C.6.1	Introduction	513

8.5C.6.2	Minimum requirement	513

8.5C.6.3	Measurement restriction for CSI-RS based candidate beam detection	514

8.5C.7	Scheduling availability of UE during beam failure detection	514

8.5C.7.1	Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1	514

8.5C.7.2	Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH on FR1	514

8.5C.8	Scheduling availability of UE during candidate beam detection	515

8.5C.8.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	515

8.5C.8.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	515

8.5C.9	Minimum requirement at transitions for beam failure detection	515

8.6	Active BWP switch delay	515

8.6.1	Introduction	515

8.6.2	DCI and timer based BWP switch delay on a single CC	516

8.6.2A	DCI based BWP switch delay on multiple CCs	517

8.6.2A.1	Simultaneous DCI based BWP switch delay on multiple CCs	517

8.6.2A.2	Non-simultaneous DCI based BWP switch delay on multiple CCs	519

8.6.2B	Timer based BWP switch delay on multiple CCs	519

8.6.2B.1	Simultaneous timer based BWP switch delay on multiple CCs	519

8.6.2B.2	Non-simultaneous timer based BWP switch delay on multiple CCs	519

8.6.3	RRC based BWP switch delay on a single CC	520

8.6.3A	RRC based BWP switch delay on multiple CCs	521

8.6.3A.1	Simultaneous RRC based BWP switch delay on multiple CCs	521

8.6.3A.2	Non-simultaneous RRC based BWP switch delay on multiple CCs	521

8.6.4	BWP switch delay on Consistent UL CCA recovery	522

8.6A	Active BWP switch delay for RedCap	522

8.6A.1	Introduction	522

8.6A.2	DCI and timer based BWP switch delay on a single CC	522

8.6A.3	RRC based BWP switch delay on a single CC	524

8.6C	Active BWP switch delay for satellite access	524

8.6C.1	Introduction	524

8.6C.2	DCI and timer based BWP switch delay on a single CC	524

8.6C.3	RRC based BWP switch delay on a single CC	526

8.7	Void	526

8.8	NE-DC: E-UTRAN PSCell Addition and Release Delay	526

8.8.1	Introduction	526

8.8.2	E-UTRAN PSCell Addition Delay Requirement	526

8.8.3	E-UTRAN PSCell Release Delay Requirement	527

8.9	NR-DC: PSCell Addition and Release Delay	527

8.9.1	Introduction	527

8.9.2	PSCell Addition Delay Requirement	527

8.9.3	PSCell Release Delay Requirement	528

8.9A	Conditional PSCell Addition Delay	528

8.9A.1	Introduction	528

8.9A.2	Conditional PSCell Addition Delay Requirement	528

8.9A.2.1	Measurement time	529

8.9B	NR-DC: PSCell Addition and Release Delay in Carriers with CCA	529

8.9B.1	Introduction	529

8.9B.2	PSCell Addition Delay Requirement	530

8.9B.3	PSCell Release Delay Requirement	530

8.10	Active TCI state switching delay	531

8.10.3A	MAC-CE based TCI state switch delay in HST FR2 scenarios	532

8.10.4	DCI based TCI state switch delay	532

8.10.5	RRC based TCI state switch delay	533

8.10.6	Active TCI state list update delay	533

8.10A	Active TCI state switching delay with CCA	533

8.10A.1	Introduction	533

8.10A.2	Known conditions for TCI state	534

8.10A.3	MAC-CE based TCI state switch delay	534

8.10A.4	DCI based TCI state switch delay	535

8.10A.5	RRC based TCI state switch delay	535

8.10A.6	Active TCI state list update delay	536

8.10B	Active TCI state switching delay for RedCap	536

8.10B.1	Introduction	536

8.10B.2	Known conditions for TCI state	536

8.10B.3	MAC-CE based TCI state switch delay	537

8.10B.4	DCI based TCI state switch delay	538

8.10B.5	RRC based TCI state switch delay	538

8.10B.6	Active TCI state list update delay	538

8.10C	Active TCI state switching delay for satellite access	539

8.10C.1	Introduction	539

8.10C.2	MAC-CE based TCI state switch delay	539

8.10C.4	DCI based TCI state switch delay	539

8.10C.5	RRC based TCI state switch delay	539

8.10C.6	Active TCI state list update delay	539

8.11	PSCell Change	540

8.11A	PSCell Change in Carriers with CCA	540

8.11B	Conditional PSCell Change	540

8.11B.1	Introduction	540

8.11B.2	Conditoinal PSCell Change delay	541

8.11B.2.1	Measurement time	541

8.11D	Conditional PSCell Change in Carriers with CCA	542

8.11D.1	Introduction	542

8.11D.2	Conditional PSCell Change delay	542

8.11D.2.1	Measurement time	543

8.12	Uplink spatial relation switch delay	543

8.12.1	Introduction	543

8.12.2	Known conditions for spatial relation when associated with DL-RS	543

8.12.3	MAC-CE based spatial relation switch delay	544

8.12.4	DCI based spatial relation switch delay	544

8.12.5	RRC based spatial relation switch delay	545

8.12A	Uplink spatial relation switch delay for RedCap	545

8.12A.1	Introduction	545

8.12A.2	Known conditions for spatial relation when associated with DL-RS	545

8.12A.3	MAC-CE based spatial relation switch delay	546

8.12A.4	DCI based spatial relation switch delay	546

8.12A.5	RRC based spatial relation switch delay	547

8.12C	Uplink spatial relation switch delay for satellite access	547

8.12C.1	Void	548

8.12C.2	Void	548

8.12C.3	Void	548

8.12C.4	Void	548

8.12C.5	Void	548

8.13	UE-specific CBW change	548

8.13.1	Introduction	548

8.13.2	UE-specific CBW change delay	548

8.13A	UE-specific CBW change for RedCap	548

8.13A.1	Introduction	548

8.13A.2	UE-specific CBW change delay	548

8.13C	UE-specific CBW change for satellite access	549

8.13C.1	Introduction	549

8.13C.2	UE-specific CBW change delay	549

8.14	Pathloss reference signal switching delay	549

8.14.1	Introduction	549

8.14.2	Known conditions for pathloss reference signal	550

8.14.3	MAC-CE based pathloss reference signal switch delay	550

8.14C	Pathloss reference signal switching delay for satellite access	551

8.14C.1	Introduction	551

8.14C.2	Known conditions for pathloss reference signal	551

8.14C.3	MAC-CE based pathloss reference signal switch delay	551

8.15	Active downlink TCI state switching delay for unified TCI	552

8.15.1	Introduction	552

8.15.4	DCI based downlink TCI state switch delay	554

8.15.5	Active Downlink TCI state list update delay	554

8.16	Active uplink TCI state switching delay for unified TCI	555

8.16.1	Introduction	555

8.16.4	DCI based uplink TCI state switch delay	557

8.16.5	Active Uplink TCI state list update delay	558

8.17	SCG Activation and Deactivation Delay	559

8.17.1	Introduction	559

8.17.2	SCG Activation Delay Requirement	559

8.17.3	SCG Deactivation Delay Requirement	560

8.18	TRP specific Link Recovery Procedures	561

8.18.1	Introduction	561

8.18.2	Requirements for TRP specific SSB based beam failure detection	561

8.18.2.1	Introduction	561

8.18.2.2	Minimum requirement	562

8.18.2.3	Measurement restriction for SSB based beam failure detection	564

8.18.3	Requirements for CSI-RS based beam failure detection	564

8.18.3.1	Introduction	564

8.18.3.2	Minimum requirement	565

8.18.3.3	Measurement restrictions for CSI-RS beam failure detection	567

8.18.4	Minimum requirement for L1 indication	568

8.18.5	Requirements for SSB based candidate beam detection	568

8.18.5.1	Introduction	568

8.18.5.2	Minimum requirement	568

8.18.5.3	Measurement restriction for SSB based candidate beam detection	570

8.18.6	Requirements for CSI-RS based candidate beam detection	571

8.18.6.1	Introduction	571

8.18.6.2	Minimum requirement	571

8.18.6.3	Measurement restriction for CSI-RS based candidate beam detection	573

8.18.7	Requirements for TRP specific Beam Failure Recovery	574

8.18.7.1	Introduction	574

8.18.7.2	Requirement	574

8.18.8	Scheduling availability of UE during TRP specific beam failure detection	574

8.18.8.1	Scheduling availability of UE performing TRP specific beam failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1	574

8.18.8.2	Scheduling availability of UE performing TRP specific beam failure detection with a different subcarrier spacing than PDSCH/PDCCH on FR1	575

8.18.8.3	Scheduling availability of UE performing TRP specific beam failure detection on FR2	575

8.18.8.4	Scheduling availability of UE performing TRP specific beam failure detection on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR DC	575

8.18.9	Scheduling availability of UE during TRP specific candidate beam detection	576

8.18.9.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	576

8.18.9.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	576

8.18.9.3	Scheduling availability of UE performing L1-RSRP measurement on FR2	576

8.18.9.4	Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC	577

8.19	Pre-configured measurement gap activation/deactivation delay	577

8.19.1	Introduction	577

8.19.2	Pre-configured measurement gap activation/deactivation upon DCI/timer-based BWP switch	577

8.19.2.1	Activation/deactivation upon DCI/timer-based BWP switch delay on a single CC	577

8.19.3	Pre-configured measurement gap activation/deactivation upon SCell activation/deactivation	577

8.19.4	Pre-configured measurement gap activation/deactivation upon RRC reconfiguration	578

9	Measurement Procedure	579

9.1	General measurement requirement	579

9.1.1	Introduction	579

9.1.2	Measurement gap	579

9.1.2.1	EN-DC: Measurement Gap Sharing	591

9.1.2.1a	SA: Measurement Gap Sharing	592

9.1.2.1b	NE-DC: Measurement Gap Sharing	593

9.1.2.1c	NR-DC: Measurement Gap Sharing	594

9.1.3	UE Measurement capability	595

9.1.3.1	EN-DC: Monitoring of multiple layers using gaps	595

9.1.3.1a	SA: Monitoring of multiple layers using gaps	595

9.1.3.1b	NE-DC: Monitoring of multiple layers using gaps	596

9.1.3.1c	NR-DC: Monitoring of multiple layers using gaps	596

9.1.3.2	EN-DC: Maximum allowed layers for multiple monitoring	597

9.1.3.2a	SA: Maximum allowed layers for multiple monitoring	598

9.1.3.2b	NE-DC: Maximum allowed layers for multiple monitoring	598

9.1.3.2c	NR-DC: Maximum allowed layers for multiple monitoring	599

9.1A.3.2	Void	600

9.1.3A	UE Measurement capability under operation mode with CCA	600

9.1.3A.1	EN-DC: Monitoring of multiple layers using gaps under CCA	600

9.1.3A.1a	SA: Monitoring of multiple layers using gaps under CCA	600

9.1.3A.2	EN-DC: Maximum allowed layers for multiple monitoring under CCA	600

9.1.3A.2a	SA: Maximum allowed layers for multiple monitoring under CCA	601

9.1.3C	UE Measurement capability under operation mode with satellite access	601

9.1.3C.1a	SA: Monitoring of multiple layers using gaps under satellite access	601

9.1.3C.2a	SA: Maximum allowed layers for multiple monitoring for SAN	602

9.1.4	Capabilities for Support of Event Triggering and Reporting Criteria	602

9.1.4.1	Introduction	602

9.1.4.2	Requirements	602

9.1.5	Carrier-specific scaling factor	606

9.1.5.1	Monitoring of multiple layers outside gaps	607

9.1.5.1.1	EN-DC mode: carrier-specific scaling factor for SSB-based, CSI-RS based L3 measurements and RSSI and channel occupancy measurements performed outside gaps	609

9.1.5.1.2	SA mode: carrier-specific scaling factor for SSB-based, CSI-RS based L3 measurements and RSSI and channel occupancy measurements performed outside gaps	610

9.1.5.1.3	NR-DC mode: carrier-specific scaling factor for SSB-based and CSI-RS based L3 measurements performed outside gaps	611

9.1.5.1.4	NE-DC mode: carrier-specific scaling factor for SSB-based and CSI-RS based measurements performed outside gaps	611

9.1.5.2	Monitoring of multiple layers within gaps	612

9.1.5.2.1	EN-DC mode: carrier-specific scaling factor for SSB, CSI-RS-based L3 measurements and RSSI and channel occupancy measurements performed within gaps	614

9.1.5.2.2	SA mode: carrier-specific scaling factor for SSB, CSI-RS-based L3 measurements and RSSI and channel occupancy measurements performed within gaps	616

9.1.5.2.3	NE-DC: carrier-specific scaling factor for SSB-based and CSI-RS based L3 measurements performed within gaps	618

9.1.5.2.4	NR-DC: carrier-specific scaling factor for SSB-based and CSI-RS-based L3 measurements performed within gaps	620

9.1.5.2.5	SA mode: carrier-specific scaling factor for PRS-based measurements performed within gaps	621

9.1.5.2.6	NE-DC: carrier-specific scaling factor for PRS-based measurements performed within gaps	622

9.1.5.2.7	NR-DC: carrier-specific scaling factor for PRS-based measurements performed within gaps	622

9.1.5.3	Monitoring of multiple layers within NCSG	622

9.1.5.3.1	SA mode: carrier-specific scaling factor for measurements performed within NCSG	623

9.1.6	Minimum requirement at transitions	623

9.1.7	Pre-configured measurement gap	624

9.1.7.1	Introduction	624

9.1.7.2	Requirements applicability	624

9.1.7.3	Requirements	625

9.1.7.3.1	Requirements for autonomous activation/deactivation mechanism	625

9.1.7.3.2	Requirements for network-controlled activation/deactivation mechanism	626

9.1.7.3.3	Requirements for reception/transmission during activation/deactivation	626

9.1.8	Concurrent measurement gaps	626

9.1.8.1	Introduction	626

9.1.8.2	Requirements	626

9.1.8.3	Collision between concurrent measurement gaps	628

9.1.8.4	Measurement gap related requirements of concurrent measurement gaps	628

9.1.9	Network controlled small gap	628

9.1.9.1	Introduction	628

9.1.9.2	Requirements applicability	629

9.1.10	MUSIM gaps	632

9.1.11	UL gap for Tx power management	633

9.1A	General measurement requirement for RedCap	634

9.1A.1	Introduction	634

9.1A.2	Measurement gap	634

9.1A.2.1	SA: Measurement Gap Sharing	638

9.1A.3	UE Measurement capability	639

9.1A.3.1	SA: Monitoring of multiple layers using gaps	639

9.1A.3.2	SA: Maximum allowed layers for multiple monitoring	639

9.1A.4	Capabilities for Support of Event Triggering and Reporting Criteria	639

9.1A.4.1	Introduction	639

9.1A.4.2	Requirements	640

9.1A.5	Carrier-specific scaling factor	640

9.1A.5.1	Monitoring of multiple layers outside gaps	640

9.1A.5.1.1	SA mode: carrier-specific scaling factor for SSB-based measurements performed outside gaps	641

9.1A.5.2	Monitoring of multiple layers within gaps	641

9.1A.5.2.1	SA mode: carrier-specific scaling factor for SSB measurements performed within gaps	641

9.1A.6	Minimum requirement at transitions	642

9.1C	General measurement requirement for SAN	643

9.1C.1	Introduction	643

9.1C.2	Measurement gap	643

9.1C.8	Concurrent measurement gaps for SAN	645

9.1C.8.1	Introduction	645

9.1C.8.2	Requirements	645

9.1C.8.3	Collision between concurrent measurement gaps	645

9.1C.8.4	Measurement gap related requirements of concurrent measurement gaps	646

9.1C.9	Collision between SMTC and measurement gap for SAN	646

9.1C.9.1	Introduction	646

9.1C.9.2	Collision between SMTCs and measurement gap	646

9.1C.9.3	Collision between multiple SMTCs on a SAN carrier	646

9.2	NR intra-frequency measurements	647

9.2.1	Introduction	647

9.2.2	Requirements applicability	649

9.2.3	Number of cells and number of SSB	649

9.2.3.1	Requirements for FR1	649

9.2.3.2	Requirements for FR2	649

9.2.4	Measurement Reporting Requirements	649

9.2.4.1	Periodic Reporting	649

9.2.4.2	Event-triggered Periodic Reporting	650

9.2.4.3	Event Triggered Reporting	650

9.2.5	Intrafrequency measurements without measurement gaps	650

9.2.5.1	Intrafrequency cell identification	650

9.2.5.2	Measurement period	655

9.2.5.3	Scheduling availability of UE during intra-frequency measurements	658

9.2.5.3.1	Scheduling availability of UE performing measurements in TDD bands on FR1	658

9.2.5.3.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	658

9.2.5.3.3	Scheduling availability of UE performing measurements on FR2	659

9.2.5.3.4	Scheduling availability of UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA	660

9.2.5.4	SFTD Measurements between PCell and PSCell	661

9.2.5.4.1	Introduction	661

9.2.5.4.2	SFTD Measurement delay	661

9.2.5.4.3	SFTD Measurement Reporting Delay	661

9.2.6	Intra-frequency measurements with measurement gaps	662

9.2.6.1	Void	662

9.2.6.2	Intra-frequency cell identification	662

9.2.6.3	Intrafrequency Measurement Period	664

9.2.7	Intra-frequency measurements with NCSG	666

9.2.7.1	Intra-frequency cell identification	666

9.2.7.2	Measurement period	668

9.2.7.3	Scheduling availability during intra-frequency measurement with NCSG	669

9.2A	NR intra-frequency measurements with CCA	669

9.2A.1	Introduction	669

9.2A.2	Requirements applicability	670

9.2A.3	Number of cells and number of SSB	670

9.2A.3.1	Requirements for FR1	670

9.2A.3.2	Requirements for FR2-2	671

9.2A.4	Measurement Reporting Requirements	671

9.2A.5	Intra-frequency measurements without measurement gaps	672

9.2A.5.2	Measurement period	676

9.2A.5.3	Scheduling availability of UE during intra-frequency measurements	678

9.2A.5.3.1	Scheduling availability of UE performing measurements in TDD bands on FR1	679

9.2A.5.3.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	679

9.2A.5.3.3	Scheduling availability of UE performing measurements in TDD bands on FR2-2	679

9.2A.6	Intra-frequency measurements with measurement gaps	679

9.2A.6.1	Intra-frequency cell identification	679

9.2A.6.2	Intra-frequency Measurement Period	682

9.2A.7	Intra-frequency RSSI and Channel occupancy measurements	683

9.2A.7.1	Intra-frequency RSSI measurements	683

9.2A.7.2	Intra-frequency Channel occupancy measurements	685

9.2A.7.3	Scheduling restriction during RSSI and Channel Occupancy measurements in FR1	686

9.2A.7.4	Scheduling restriction during RSSI measurements in FR2-2	686

9.2B	NR intra-frequency measurements for RedCap	687

9.2B.1	Introduction	687

9.2B.2	Requirements applicability	687

9.2B.3	Number of cells and number of SSB	688

9.2B.3.1	Requirements for FR1	688

9.2B.3.2	Requirements for FR2	688

9.2B.4	Measurement Reporting Requirements	688

9.2B.4.1	Periodic Reporting	688

9.2B.4.2	Event-triggered Periodic Reporting	688

9.2B.4.3	Event Triggered Reporting	688

9.2B.5	Intra-frequency measurements without measurement gaps	689

9.2B.5.1	Intra-frequency cell identification	689

9.2B.5.2	Measurement period	691

9.2B.5.3	Scheduling availability of UE during intra-frequency measurements	692

9.2B.5.3.1	Scheduling availability of UE performing measurements in TDD bands on FR1	692

9.2B.5.3.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	692

9.2B.5.3.3	Scheduling availability of UE performing measurements on FR2	693

9.2B.5.3.4	Scheduling availability of HD-FDD UE performing measurements on FR1	693

9.2B.6	Intra-frequency measurements with measurement gaps	694

9.2B.6.1	Intra-frequency cell identification	694

9.2B.6.2	Intra-frequency Measurement Period	695

9.2C	NR intra-frequency measurements for SAN	696

9.2C.1	Introduction	696

9.2C.2	Requirements applicability	697

9.2C.3	Number of cells and number of SSB	698

9.2C.3.1	Requirements for FR1	698

9.2C.4	Measurement Reporting Requirements	698

9.2C.4.1	Periodic Reporting	698

9.2C.4.2	Event-triggered Periodic Reporting	698

9.2C.4.3	Event Triggered Reporting	698

9.2C.5	Intra frequency measurements without measurement gaps	699

9.2C.5.1	Intra frequency cell identification	699

9.2C.5.2	Measurement period	701

9.2C.5.3	Scheduling availability of UE during intra-frequency measurements	701

9.2C.5.3.1	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	701

9.2C.5.3.2	Scheduling availability of UE performing measurements on a neighbor cell served by a different satellite in LEO	702

9.2C.6	Intra-frequency measurements with measurement gaps	702

9.2C.6.1	Intra-frequency cell identification	702

9.2C.6.3	Intrafrequency Measurement Period	704

9.3	NR inter-frequency measurements	704

9.3.1	Introduction	704

9.3.2	Requirements applicability	706

9.3.2.1	Void	706

9.3.2.2	Void	706

9.3.3	Number of cells and number of SSB	706

9.3.3.1	Requirements for FR1	706

9.3.3.2	Requirements for FR2	706

9.3.4	Inter-frequency measurement with measurement gaps	706

9.3.4.1	Void	710

9.3.4.2	Void	710

9.3.5	Inter-frequency measurements	710

9.3.5.1	Void	711

9.3.5.2	Void	711

9.3.5.3	Void	711

9.3.6	Inter-frequency measurements reporting requirements	711

9.3.6.1	Periodic Reporting	711

9.3.6.2	Event-triggered Periodic Reporting	711

9.3.6.3	Event-triggered Reporting	711

9.3.7	Void	712

9.3.8	Inter-frequency SFTD measurement requirements	712

9.3.8.1	Introduction	712

9.3.8.2	SFTD Measurement delay	712

9.3.8.3	SFTD Measurement reporting delay	713

9.3.9	Inter frequency measurements without measurement gaps	713

9.3.9.1	Inter frequency Cell identification	713

9.3.9.2	Measurement period	716

9.3.9.3	Scheduling availability of UE during inter-frequency measurements when the SSB is completely contained in the active BWP of the UE	718

9.3.9.3.1	Scheduling availability of UE performing measurements in TDD bands on FR1	718

9.3.9.3.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	718

9.3.9.3.3	Scheduling availability of UE performing measurements on FR2	719

9.3.9.3.4	Scheduling availability of UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA	719

9.3.9.4	Scheduling availability of UE during inter-frequency measurements when the SSB is not completely contained in the active BWP of the UE	719

9.3.9.4.1	Scheduling availability of UE performing measurements in TDD bands on FR1	720

9.3.9.4.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	720

9.3.9.4.3	Scheduling availability of UE performing measurements on FR2	721

9.3.9.4.4	Scheduling availability of UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA	722

9.3.10	Inter-frequency measurement with NCSG	723

9.3.10.1	Inter-frequency cell identification	723

9.3.10.2	Measurement period	724

9.3.10.3	Scheduling availability during inter-frequency measurement with NCSG	724

9.3.10.3.1	Scheduling availability of UE performing measurements in TDD bands on FR1	725

9.3.10.3.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	725

9.3.10.3.3	Scheduling availability of UE performing measurements on FR2	726

9.3.10.3.4	Scheduling availability of UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA	727

9.3A	NR inter-frequency measurements in carrier frequencies with CCA	728

9.3A.1	Introduction	728

9.3A.2	Requirements applicability	728

9.3A.3	Number of cells and number of SSB	729

9.3A.3.1	Requirements for FR1	729

9.3A.3.2	Requirements for FR2-2	729

9.3A.4	Inter-frequency cell identification	729

9.3A.5	Inter-frequency measurements	731

9.3A.6	NR Inter-frequency measurements reporting requirements	733

9.3A.6.1	Periodic Reporting	733

9.3A.6.2	Event-triggered Periodic Reporting	733

9.3A.6.3	Event-triggered Reporting	733

9.3A.8	Inter-frequency RSSI measurements	733

9.3A.9	Inter-frequency channel occupancy measurements	734

9.3B	NR inter-frequency measurements for RedCap	735

9.3B.1	Introduction	735

9.3B.2	Requirements applicability	735

9.3B.3	Number of cells and number of SSB	736

9.3B.3.1	Requirements for FR1	736

9.3B.3.2	Requirements for FR2	736

9.3B.4	Inter-frequency measurement with measurement gaps	736

9.3B.5	Inter-frequency measurements	737

9.3B.6	Inter-frequency measurements reporting requirements	738

9.3B.6.1	Periodic Reporting	738

9.3B.6.2	Event-triggered Periodic Reporting	738

9.3B.6.3	Event-triggered Reporting	738

9.3B.7	Inter frequency measurements without measurement gaps	739

9.3B.7.1	Inter frequency Cell identification	739

9.3B.7.2	Measurement period	741

9.3B.7.3	Scheduling availability of UE during inter-frequency measurements	742

9.3B.7.3.1	Scheduling availability of UE performing measurements in TDD bands on FR1	742

9.3B.7.3.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	743

9.3B.7.3.3	Scheduling availability of UE performing measurements on FR2	743

9.3B.7.3.4	Scheduling availability of HD-FDD UE performing measurements on FR1	743

9.3C	NR inter-frequency measurements for SAN	744

9.3C.1	Introduction	744

9.3C.2	Requirements applicability	745

9.3C.3	Number of cells and number of SSB	745

9.3C.3.1	Requirements for FR1	745

9.3C.4	Inter-frequency measurement with measurement gaps	745

9.3C.5	Inter-frequency measurements	747

9.3C.6	Inter-frequency measurements reporting requirements	747

9.3C.6.1	Periodic Reporting	747

9.3C.6.2	Event-triggered Periodic Reporting	747

9.3C.6.3	Event-triggered Reporting	747

9.3C.7	Inter frequency measurements without measurement gaps	748

9.3C.7.1	Inter frequency Cell identification	748

9.3C.7.2	Measurement period	749

9.3C.7.3	Scheduling availability of UE during inter-frequency measurements	749

9.3C.7.3.1	Void	750

9.3C.7.3.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	750

9.4	Inter-RAT measurements	750

9.4.1	Introduction	750

9.4.2	NR − E-UTRAN FDD measurements	752

9.4.2.1	Introduction	752

9.4.2.2	Requirements when no DRX is used	752

9.4.2.3	Requirements when DRX is used	753

9.4.2.4	Measurement reporting requirements	755

9.4.2.4.1	Periodic Reporting	755

9.4.2.4.2	Event-Triggered Periodic Reporting	755

9.4.2.4.3	Event-Triggered Reporting	756

9.4.2.5	Scheduling Availability During NR − E-UTRAN FDD measurements with NCSG	756

9.4.3	NR − E-UTRAN TDD measurements	756

9.4.3.1	Introduction	756

9.4.3.2	Requirements when no DRX is used	756

9.4.3.3	Requirements when DRX is used	758

9.4.3.4	Measurement reporting requirements	759

9.4.3.4.1	Periodic Reporting	759

9.4.3.4.2	Event-Triggered Periodic Reporting	760

9.4.3.4.3	Event-Triggered Reporting	760

9.4.3.5	Scheduling Availability During NR − E-UTRAN TDD measurements with NCSG	760

9.4.4	Inter-RAT RSTD measurements	760

9.4.4.1	NR − E-UTRAN FDD RSTD measurements	760

9.4.4.1.1	Introduction	760

9.4.4.1.2	Requirements	761

9.4.4.2	NR − E-UTRAN TDD RSTD measurements	764

9.4.4.2.1	Introduction	764

9.4.4.2.2	Requirements	765

9.4.5	Inter-RAT E-CID measurements	768

9.4.5.1	NR−E-UTRAN FDD E-CID RSRP and RSRQ measurements	768

9.4.5.1.1	Introduction	768

9.4.5.1.2	Requirements	768

9.4.5.1.3	Measurement Reporting Delay	768

9.4.5.2	NR−E-UTRAN TDD E-CID RSRP and RSRQ measurements	769

9.4.5.2.1	Introduction	769

9.4.5.2.2	Requirements	769

9.4.5.2.3	Measurement Reporting Delay	769

9.4.6	NR − UTRAN FDD measurements	769

9.4.6.1	Introduction	769

9.4.6.2	Requirements when no DRX is used	769

9.4.6.3	Requirements when DRX is used	770

9.4.7	NR – E-UTRAN measurements with autonomous gaps	772

9.4.7.1	CGI identification of an E-UTRA cell with autonomous gaps	772

9.4.7.2	CGI reporting delay	772

9.4A	Inter-RAT measurements for RedCap	773

9.4A.1	Introduction	773

9.4A.2	NR − E-UTRAN FDD measurements	774

9.4A.2.1	Introduction	774

9.4A.2.2	Requirements when no DRX is used	774

9.4A.2.3	Requirements when DRX is used	775

9.4A.2.4	Measurement reporting requirements	776

9.4A.2.4.1	Periodic Reporting	776

9.4A.2.4.2	Event-Triggered Periodic Reporting	776

9.4A.2.4.3	Event-Triggered Reporting	776

9.4A.3	NR − E-UTRAN TDD measurements	777

9.4A.3.1	Introduction	777

9.4A.3.2	Requirements when no DRX is used	777

9.4A.3.3	Requirements when DRX is used	779

9.4A.3.4	Measurement reporting requirements	780

9.4A.3.4.1	Periodic Reporting	780

9.4A.3.4.2	Event-Triggered Periodic Reporting	780

9.4A.3.4.3	Event-Triggered Reporting	780

9.4A.4	NR – E-UTRAN measurements with autonomous gaps	781

9.4A.4.1	CGI identification of an E-UTRA cell with autonomous gaps	781

9.4A.4.2	CGI reporting delay	781

9.4A.4.3	CGI reporting scheduling restriction	781

9.5	L1-RSRP measurements for Reporting	782

9.5.1	Introduction	782

9.5.2	Requirements applicability	782

9.5.3	Measurement Reporting Requirements	783

9.5.3.1	Periodic Reporting	783

9.5.3.2	Semi-Persistent Reporting	783

9.5.3.3	Aperiodic Reporting	783

9.5.4	L1-RSRP measurement requirements	784

9.5.4.1	SSB based L1-RSRP Reporting	784

9.5.4.2	CSI-RS based L1-RSRP Reporting	787

9.5.4A	Void	790

9.5.4A.1	Void	790

9.5.5	Measurement restriction for CSI-RS and SSB for L1-RSRP measurement	790

9.5.5.1	Measurement restriction for SSB based L1-RSRP	790

9.5.5.2	Measurement restriction for CSI-RS based L1-RSRP	791

9.5.6	Scheduling availability of UE during L1-RSRP measurement	792

9.5.6.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	792

9.5.6.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	792

9.5.6.3	Scheduling availability of UE performing L1-RSRP measurement on FR2	792

9.5.6.4	Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA	794

9.5A	L1-RSRP measurements for Reporting under CCA	794

9.5A.1	Introduction	794

9.5A.2	Requirements applicability	794

9.5A.3	Measurement Reporting Requirements	794

9.5A.3.1	Periodic Reporting	795

9.5A.3.2	Semi-Persistent Reporting	795

9.5A.3.3	Aperiodic Reporting	795

9.5A.4	L1-RSRP measurement requirements	795

9.5A.4.1	SSB based L1-RSRP Reporting	795

9.5A.5	Measurement restriction for L1-RSRP measurement	798

9.5A.5.1	Measurement restriction for SSB based L1-RSRP	798

9.5A.6	Scheduling availability of UE during L1-RSRP measurement	798

9.5A.6.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	798

9.5A.6.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	799

9.5A.6.3	(Void)	799

9.5A.6.3A	Scheduling availability of UE performing L1-RSRP measurement in case of FR1-FR2 inter-band CA	799

9.5A.6.3B	Scheduling availability of UE performing L1-RSRP measurement on FR2-2	799

9.5A.6.4	Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA	800

9.5B	L1-RSRP measurements for Reporting for RedCap	800

9.5B.1	Introduction	800

9.5B.2	Requirements applicability	800

9.5B.3	Measurement Reporting Requirements	801

9.5B.3.1	Periodic Reporting	801

9.5B.3.2	Semi-Persistent Reporting	801

9.5B.3.3	Aperiodic Reporting	801

9.5B.4	L1-RSRP measurement requirements	802

9.5B.4.1	SSB based L1-RSRP Reporting	802

9.5B.4.2	CSI-RS based L1-RSRP Reporting	803

9.5B.5	Measurement restriction for CSI-RS and SSB for L1-RSRP measurement	806

9.5B.5.1	Measurement restriction for SSB based L1-RSRP	806

9.5B.5.2	Measurement restriction for CSI-RS based L1-RSRP	807

9.5B.6	Scheduling availability of UE during L1-RSRP measurement	807

9.5B.6.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	807

9.5B.6.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	807

9.5B.6.3	Scheduling availability of UE performing L1-RSRP measurement on FR2	808

9.5C	L1-RSRP measurements for Reporting for satellite access	808

9.5C.1	Introduction	808

9.5C.3	Measurement Reporting Requirements	809

9.5C.3.1	Periodic Reporting	809

9.5C.3.2	Semi-Persistent Reporting	809

9.5C.3.3	Aperiodic Reporting	810

9.5C.4	L1-RSRP measurement requirements	810

9.5C.4.1	SSB based L1-RSRP Reporting	810

9.5C.5	Measurement restriction for L1-RSRP measurement	812

9.5C.5.1	Measurement restriction for SSB based L1-RSRP	812

9.5C.5.2	Measurement restriction for CSI-RS based L1-RSRP	812

9.5C.6	Scheduling availability of UE during L1-RSRP measurement	813

9.5C.6.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	813

9.5C.6.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	813

9.6	NE-DC: Measurements	813

9.6.1	Introduction	813

9.6.2	SFTD Measurements	813

9.6.2.1	Introduction	813

9.6.2.2	SFTD Measurement requirements	813

9.7	Cross Link Interference measurements	814

9.7.1	Introduction	814

9.7.2	SRS-RSRP measurements	814

9.7.2.1	Introduction	814

9.7.2.2	Requirements applicability	815

9.7.2.3	Measurement Reporting Requirements	815

9.7.2.3.1	Periodic Reporting	815

9.7.2.3.2	Event-triggered Periodic Reporting	815

9.7.2.3.3	Event Triggered Reporting	815

9.7.2.4	Measurement capability	815

9.7.2.5	SRS-RSRP measurement period	816

9.7.3	CLI-RSSI measurements	816

9.7.3.1	Introduction	816

9.7.3.2	Requirements applicability	816

9.7.3.3	Measurement Reporting Requirements	816

9.7.3.3.1	Periodic Reporting	816

9.7.3.3.2	Event-triggered Periodic Reporting	816

9.7.3.3.3	Event Triggered Reporting	817

9.7.3.4	Measurement capability	817

9.7.3.5	CLI-RSSI measurement period	817

9.7.4	Scheduling availability of UE during CLI measurements	817

9.7.4.1	Scheduling availability of UE performing measurement on FR1	817

9.7.4.2	Scheduling availability of UE performing measurement on FR2	818

9.8	L1-SINR measurements for Reporting	818

9.8.1	Introduction	818

9.8.2	Requirements applicability	819

9.8.3	Measurement Reporting Requirements	819

9.8.3.1	Periodic Reporting	819

9.8.3.2	Semi-Persistent Reporting	820

9.8.4	L1-SINR measurement requirements	820

9.8.4.1	L1-SINR reporting with CSI-RS based CMR and no dedicated IMR configured	820

9.8.4.3	L1-SINR reporting with CSI-RS based CMR and dedicated IMR configured	825

9.8.5	Measurement restriction for L1-SINR measurement	826

9.8.5.1	Measurement restriction if SSB configured for L1-SINR Measurement	827

9.8.5.2	Measurement restriction if CSI-RS configured for L1-SINR measurement	827

9.8.5.3	Measurement restriction if CSI-IM configured for L1-SINR measurement	828

9.8.6	Scheduling availability of UE during L1-SINR measurement	828

9.8.6.1	Scheduling availability of UE performing L1-SINR measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	828

9.8.6.2	Scheduling availability of UE performing L1-SINR measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	828

9.8.6.4	Scheduling availability of UE performing L1-SINR measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA	829

9.9	 NR measurements for positioning	830

9.9.1	Introduction	830

9.9.1.1	General Aspects of Gap-based Measurement	830

9.9.1.2	General Aspects of Gapless Measurement	830

9.9.1.3	Scheduling Availability of UE during PRS Measurement without Measurement Gaps	831

9.9.2	RSTD measurements	832

9.9.2.1	Introduction	832

9.9.2.2	Requirements Applicability	832

9.9.2.3	Measurement Capability	833

9.9.2.4	Measurement Reporting Requirements	833

9.9.2.4.1	Void	833

9.9.2.4.2	Void	833

9.9.2.4.3	Void	833

9.9.2.5	Measurements Period Requirements	833

9.9.2.6	Void	836

9.9.2.7	Measurements Period Requirements without Measurement Gaps	836

9.9.2.8	Void	839

9.9.2.9	Measurements Period Requirements with both MG and PPW	839

9.9.3	PRS-RSRP measurements	840

9.9.3.1	Introduction	840

9.9.3.2	Requirements applicability	840

9.9.3.3	Measurement Capability	840

9.9.3.4	Measurement Reporting Requirements	840

9.9.3.5	Measurement Period Requirements	840

9.9.3.6	Measurement Period Requirements without Measurement Gaps	843

9.9.3.7	Void	845

9.9.3.8	Measurements Period Requirements with both MG and PPW	845

9.9.4	UE Rx-Tx time difference measurements	846

9.9.4.1	Introduction	846

9.9.4.2	Requirements Applicability	846

9.9.4.3	Measurement Capability	846

9.9.4.4	Measurement Reporting Requirements	846

9.9.4.5	Measurement Period Requirements	846

9.9.4.6	Measurement Period Requirements without Measurement Gaps	850

9.9.4.7	Void	853

9.9.4.8	Measurements Period Requirements with both MG and PPW	853

9.9.5	E-CID measurements	854

9.9.5.1	Introduction	854

9.9.5.2	Measurement Requirements	854

9.9.5.2.1	Intra-frequency Measurement Requirements	854

9.9.5.2.2	Inter-frequency Measurement Requirements	854

9.9.5.2.3	Measurement Reporting Delay	855

9.9.6	PRS-RSRPP measurements	855

9.9.6.1	Introduction	855

9.9.6.2	Requirements applicability	855

9.9.6.3	Measurement capability	855

9.9.6.4	Measurement reporting requirements	855

9.9.6.5	Measurement period requirements	856

9.9.6.6	Measurement Period Requirements without Measurement Gaps	856

9.9.6.7	Void	856

9.9.6.8	Measurements Period Requirements with both MG and PPW	856

9.10	CSI-RS based L3 measurements	856

9.10.1	Introduction	856

9.10.2	CSI-RS based intra-frequency measurements	856

9.10.2.1	Introduction	856

9.10.2.2	Requirements applicability	857

9.10.2.3	Number of cells and number of CSI-RS	858

9.10.2.3.1	Requirements for FR1	858

9.10.2.3.2	Requirements for FR2	858

9.10.2.4	Measurement Reporting Requirements	858

9.10.2.4.1	Periodic Reporting	859

9.10.2.4.2	Event-triggered Periodic Reporting	859

9.10.2.4.3	Event Triggered Reporting	859

9.10.2.5	Intra-frequency measurements without measurement gaps	859

9.10.2.6	Scheduling availability of UE during CSI-RS based intra-frequency measurements	861

9.10.2.6.1	Scheduling availability of UE performing CSI-RS based measurements in TDD bands	861

9.10.2.6.2	Scheduling availability of UE performing CSI-RS based measurements in FR2	861

9.10.3	CSI-RS based Inter-frequency measurements	861

9.10.3.1	Introduction	861

9.10.3.2	Requirements applicability	862

9.10.3.3	Number of cells and number of CSI-RS resources	862

9.10.3.3.1	Requirements for FR1	862

9.10.3.3.2	Requirements for FR2	863

9.10.3.4	Measurements reporting requirements	863

9.10.3.4.1	Periodic Reporting	863

9.10.3.4.2	Event-triggered Periodic Reporting	863

9.10.3.4.3	Event-triggered Reporting	863

9.10.3.5	Inter frequency measurements with measurement gaps	863

9.11	NR measurements with autonomous gaps	865

9.11.1	Introduction	865

9.11.2	CGI identification of an NR cell with autonomous gaps	865

9.11.3	CGI reporting delay	866

9.11A	NR measurements with autonomous gaps for RedCap	866

9.11A.1	Introduction	866

9.11A.2	CGI identification of an NR cell with autonomous gaps	867

9.11A.3	CGI reporting delay	868

9.11A.4	CGI reporting scheduling restriction	868

9.12	Measurement for Propagation Delay Compensation	868

9.12.1	Introduction	868

9.12.2	Requirements Applicability	868

9.12.3	Measurement Capability	869

9.12.4	Measurement period requirements	869

9.12.4.1	PRS Measurement Period	869

9.12.4.2	TRS Measurement Period	870

9.12.5	Measurement Reporting Requirements	871

9.12.6	Scheduling availability during measurement for Propagation Delay Compensation	871

9.12.7	Measurement restriction for measurement for Propagation Delay Compensation	871

9.13	L1-RSRP measurements for a cell with different PCI from serving cell	871

9.13.1	Introduction	871

9.13.2	Requirements Applicability	872

9.13.3	Measurement Reporting Requirements	872

9.13.3.1	Periodic Reporting	873

9.13.3.2	Semi-Persistent Reporting	873

9.13.3.3	Aperiodic Reporting	873

9.13.4	L1-RSRP measurement requirements	873

9.13.4.1	Inter-cell SSB based L1-RSRP Reporting	873

9.13.5	Measurement restriction for L1-RSRP measurement	875

9.13.5.1	Measurement restriction for SSB based L1-RSRP	876

9.13.6	Scheduling availability of UE during L1-RSRP measurement	876

9.13.6.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	877

9.13.6.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	877

9.13.6.3	Scheduling availability of UE performing L1-RSRP measurement on FR2	877

9.13.6.4	Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA	877

9.13.6.5	Scheduling availability of UE performing L1-RSRP measurement in TDD bands on FR1	878

10	Measurement Performance requirements	879

10.1	NR measurements	879

10.1.1	Introduction	879

10.1.2	Intra-frequency RSRP accuracy requirements for FR1	879

10.1.2.1	Intra-frequency SS-RSRP accuracy requirements	879

10.1.2.1.1	Absolute SS-RSRP Accuracy	879

10.1.2.1.2	Relative SS-RSRP Accuracy	880

10.1.2.2	Void	881

10.1.2.3	Intra-frequency CSI-RSRP accuracy requirements	881

10.1.2.3.1	Absolute CSI-RSRP Accuracy	881

10.1.2.3.2	Relative CSI-RSRP Accuracy	882

10.1.2B	Intra-frequency RSRP accuracy requirements for FR1 for CA/DC Idle Mode Measurements	883

10.1.2B.1	Intra-frequency SS-RSRP accuracy requirements	883

10.1.2B.1.1	Absolute SS-RSRP Accuracy	883

10.1.2C	Intra-frequency RSRP accuracy requirements for FR1 SAN	884

10.1.2C.1	Intra-frequency SS-RSRP accuracy requirements	884

10.1.2C.1.1	Absolute SS-RSRP Accuracy	884

10.1.2C.1.2	Relative SS-RSRP Accuracy	885

10.1.3	Intra-frequency RSRP accuracy requirements for FR2	885

10.1.3.1	Intra-frequency SS-RSRP accuracy requirements	885

10.1.3.1.1	Absolute SS-RSRP Accuracy	885

10.1.3.1.2	Relative SS-RSRP Accuracy	886

10.1.3.2	Void	887

10.1.3.3	Intra-frequency CSI-RSRP accuracy requirements	887

10.1.3.3.1	Absolute CSI-RSRP Accuracy	887

10.1.3.3.2	Relative CSI-RSRP Accuracy	888

10.1.3B	Intra-frequency RSRP accuracy requirements for FR2 for CA/DC Idle Mode Measurements	889

10.1.3B.1	Intra-frequency SS-RSRP accuracy requirements	889

10.1.3B.1.1	Absolute SS-RSRP Accuracy	889

10.1.4	Inter-frequency RSRP accuracy requirements for FR1	890

10.1.4.1	Inter-frequency SS-RSRP accuracy requirements	890

10.1.4.1.1	Absolute Accuracy of SS-RSRP in FR1	890

10.1.4.1.2	Relative Accuracy of SS-RSRP in FR1	891

10.1.4.2	Void	892

10.1.4.3	Inter-frequency CSI-RSRP accuracy requirements	892

10.1.4.3.1	Absolute Accuracy of CSI-RSRP in FR1	892

10.1.4.3.2	Relative Accuracy of CS-RSRP in FR1	893

10.1.4B	Inter-frequency RSRP accuracy requirements for FR1 for CA/DC Idle Mode Measurements	894

10.1.4B.1	Inter-frequency SS-RSRP accuracy requirements	894

10.1.4B.1.1	Absolute Accuracy of SS-RSRP in FR1	894

10.1.4C	Inter-frequency RSRP accuracy requirements for FR1 SAN	895

10.1.4C.1	Inter-frequency SS-RSRP accuracy requirements	895

10.1.4C.1.1	Absolute Accuracy of SS-RSRP in FR1	895

10.1.4C.1.2	Relative Accuracy of SS-RSRP in FR1	896

10.1.5	Inter-frequency RSRP accuracy requirements for FR2	897

10.1.5.1	Inter-frequency SS-RSRP accuracy requirements	897

10.1.5.1.1	Absolute SS-RSRP Accuracy	897

10.1.5.1.2	Relative SS-RSRP Accuracy	897

10.1.5.2	Void	898

10.1.5.3	Inter-frequency CSI-RSRP accuracy requirements	898

10.1.5.3.1	Absolute CSI-RSRP Accuracy	898

10.1.5.3.2	Relative CSI-RSRP Accuracy	899

10.1.5B	Inter-frequency RSRP accuracy requirements for FR2 for CA/DC Idle Mode Measurements	900

10.1.5B.1	Inter-frequency SS-RSRP accuracy requirements	900

10.1.5B.1.1	Absolute SS-RSRP Accuracy	900

10.1.6	RSRP Measurement Report Mapping	901

10.1.7	Intra-frequency RSRQ accuracy requirements for FR1	903

10.1.7.1	Intra-frequency SS-RSRQ accuracy requirements in FR1	903

10.1.7.1.1	Absolute SS-RSRQ Accuracy in FR1	903

10.1.7.2	Intra-frequency CSI-RSRQ accuracy requirements	904

10.1.7.2.1	Absolute CSI-RSRQ Accuracy	904

10.1.7B	Intra-frequency RSRQ accuracy requirements for FR1 for CA/DC Idle Mode Measurements	905

10.1.7B.1	Intra-frequency SS-RSRQ accuracy requirements in FR1	905

10.1.7B.1.1	Absolute SS-RSRQ Accuracy in FR1	905

10.1.7C	Intra-frequency RSRQ accuracy requirements for FR1 SAN	906

10.1.7C.1	Intra-frequency SS-RSRQ accuracy requirements in FR1	906

10.1.7C.1.1	Absolute SS-RSRQ Accuracy in FR1	906

10.1.8	Intra-frequency RSRQ accuracy requirements for FR2	907

10.1.8.1	Intra-frequency SS-RSRQ accuracy requirements in FR2	907

10.1.8.1.1	Absolute SS-RSRQ Accuracy in FR2	907

10.1.8.2	Intra-frequency CSI-RSRQ accuracy requirements	908

10.1.8.2.1	Absolute CSI-RSRQ Accuracy	908

10.1.8B	Intra-frequency RSRQ accuracy requirements for FR2 for CA/DC Idle Mode Measurements	908

10.1.8B.1	Intra-frequency SS-RSRQ accuracy requirements in FR2	908

10.1.8B.1.1	Absolute SS-RSRQ Accuracy in FR2	909

10.1.9	Inter-frequency RSRQ accuracy requirements for FR1	909

10.1.9.1	Inter-frequency SS-RSRQ accuracy requirements in FR1	909

10.1.9.1.1	Absolute Accuracy of SS-RSRQ in FR1	909

10.1.9.1.2	Relative Accuracy of SS-RSRQ in FR1	910

10.1.9.2	Inter-frequency CSI-RSRQ accuracy requirements	911

10.1.9.2.1	Absolute CSI-RSRQ Accuracy	911

10.1.9.2.2	Relative CSI-RSRQ Accuracy	912

10.1.9B	Inter-frequency RSRQ accuracy requirements for FR1 for CA/DC Idle Mode Measurements	913

10.1.9B.1	Inter-frequency SS-RSRQ accuracy requirements in FR1	913

10.1.9B.1.1	Absolute Accuracy of SS-RSRQ in FR1	913

10.1.9C	Inter-frequency RSRQ accuracy requirements for FR1 SAN	914

10.1.9C.1	Inter-frequency SS-RSRQ accuracy requirements in FR1	914

10.1.9C.1.1	Absolute Accuracy of SS-RSRQ in FR1	914

10.1.9C.1.2	Relative Accuracy of SS-RSRQ in FR1	915

10.1.10	Inter-frequency RSRQ accuracy requirements for FR2	916

10.1.10.1	Inter-frequency SS-RSRQ accuracy requirements in FR2	916

10.1.10.1.1	Absolute Accuracy of SS-RSRQ in FR2	916

10.1.10.1.2	Relative Accuracy of SS-RSRQ in FR2	916

10.1.10.2	Inter-frequency CSI-RSRQ accuracy requirements	917

10.1.10.2.1	Absolute CSI-RSRQ Accuracy	917

10.1.10.2.2	Relative CSI-RSRQ Accuracy	918

10.1.10B	 Inter-frequency RSRQ accuracy requirements for FR2 for CA/DC Idle Mode Measurements	919

10.1.10B.1	Inter-frequency SS-RSRQ accuracy requirements in FR2	919

10.1.10B.1.1	Absolute Accuracy of SS-RSRQ in FR2	919

10.1.11	RSRQ report mapping	920

10.1.12	Intra-frequency SINR accuracy requirements for FR1	920

10.1.12.1	Intra-frequency SS-SINR accuracy requirements in FR1	920

10.1.12.1.1	Absolute SS-SINR Accuracy in FR1	920

10.1.12.2	Intra-frequency CSI-SINR accuracy requirements in FR1	921

10.1.12.2.1	Absolute CSI-SINR Accuracy in FR1	921

10.1.12C	Intra-frequency SINR accuracy requirements for FR1 SAN	922

10.1.12C.1	Intra-frequency SS-SINR accuracy requirements in FR1	922

10.1.12C.1.1	Absolute SS-SINR Accuracy in FR1	922

10.1.13	Intra-frequency SINR accuracy requirements for FR2	923

10.1.13.1	Intra-frequency SS-SINR accuracy requirements in FR2	923

10.1.13.1.1	Absolute SS-SINR Accuracy in FR2	923

10.1.13.2	Intra-frequency CSI-SINR accuracy requirements in FR2	924

10.1.13.2.1	Absolute CSI-SINR Accuracy in FR2	924

10.1.14	Inter-frequency SINR accuracy requirements for FR1	924

10.1.14.1	Inter-frequency SS-SINR accuracy requirements in FR1	924

10.1.14.1.1	Aboslute Accuracy of SS-SINR in FR1	924

10.1.14.1.2	Relative Accuracy of SS-SINR in FR1	925

10.1.14.2	Inter-frequency CSI-SINR accuracy requirements in FR1	926

10.1.14.2.1	Aboslute Accuracy of CSI-SINR in FR1	926

10.1.14.2.2	Relative Accuracy of CSI-SINR in FR1	927

10.1.14C	Inter-frequency SINR accuracy requirements for FR1 SAN	928

10.1.14C.1	Inter-frequency SS-SINR accuracy requirements in FR1	928

10.1.14C.1.1	Aboslute Accuracy of SS-SINR in FR1	928

10.1.14C.1.2	Relative Accuracy of SS-SINR in FR1	929

10.1.15	Inter-frequency SINR accuracy requirements for FR2	930

10.1.15.1	Inter-frequency SS-SINR accuracy requirements in FR2	930

10.1.15.1.1	Aboslute Accuracy of SS-SINR in FR2	930

10.1.15.1.2	Relative Accuracy of SS-SINR in FR2	930

10.1.15.2	Inter-frequency CSI-SINR accuracy requirements in FR2	931

10.1.15.2.1	Aboslute Accuracy of CSI-SINR in FR2	931

10.1.15.2.2	Relative Accuracy of CSI-SINR in FR2	932

10.1.16	SINR report mapping	933

10.1.16.1	SS-SINR and CSI-SINR measurement report mapping	933

10.1.17	Power Headroom	934

10.1.17.1	Power Headroom Report	934

10.1.17.1.1	Power Headroom Report Mapping	934

10.1.18	PCMAX,c,f	935

10.1.18.1	Report Mapping	935

10.1.19	L1-RSRP accuracy requirements for FR1	935

10.1.19.1	SSB based L1-RSRP accuracy requirements	935

10.1.19.1.1	Absolute Accuracy	935

10.1.19.1.2	Relative Accuracy	936

10.1.19.2	CSI-RS based L1-RSRP accuracy requirements	937

10.1.19.2.1	Absolute Accuracy	937

10.1.19.2.2	Relative Accuracy	938

10.1.19C	L1-RSRP accuracy requirements for FR1 SAN	939

10.1.19C.1	SSB based L1-RSRP accuracy requirements	939

10.1.19C.1.1	Absolute Accuracy	939

10.1.19C.1.2	Relative Accuracy	940

10.1.19C.2	CSI-RS based L1-RSRP accuracy requirements	940

10.1.19C.2.1	Absolute Accuracy	940

10.1.19C.2.2	Relative Accuracy	941

10.1.20	L1-RSRP accuracy requirements for FR2	942

10.1.20.1	SSB based L1-RSRP accuracy requirements	942

10.1.20.1.1	Absolute Accuracy	942

10.1.20.1.2	Relative Accuracy	942

10.1.20.2	CSI-RS based L1-RSRP accuracy requirements	943

10.1.20.2.1	Absolute Accuracy	943

10.1.20.2.2	Relative Accuracy	944

10.1.21	SFTD accuracy requirements	945

10.1.21.1	SFTD acuracy requirements for NE-DC	945

10.1.21.2	SFTD acuracy requirements for NR-DC	947

10.1.21.3	Inter frequency SFTD acuracy requirements	948

10.1.22	CLI measurement accuracy requirements	949

10.1.22.1	SRS-RSRP	949

10.1.22.1.1	SRS-RSRP Accuracy	949

10.1.22.1.2	SRS-RSRP report mapping	951

10.1.22.2	CLI-RSSI	951

10.1.22.2.1	CLI-RSSI Accuracy	951

10.1.22.2.2	CLI-RSSI report mapping	952

10.1.23	RSTD Measurements	953

10.1.23.1	Introduction	953

10.1.23.2	Measurement Accuracy Requirements	953

10.1.23.3	Report mapping	963

10.1.23.3.1	Absolute DL RSTD Measurement Reporting	963

10.1.23.3.2	Differential Reporting for DL RSTD Measurement	965

10.1.23.3.3	Additional Path Report Mapping for DL RSTD	967

10.1.24	PRS-RSRP Measurements	969

10.1.24.1	Introduction	969

10.1.24.2	Measurement Accuracy Requirements	969

10.1.24.2.1	Absolute PRS RSRP accuracy	969

10.1.24.2.2	Relative PRS RSRP accuracy	973

10.1.24.3	Report mapping	977

10.1.24.3.1	Absolute PRS-RSRP Measurement Report Mapping	977

10.1.24.3.2	Differential Report Mapping for PRS-RSRP Measurement	978

10.1.25	UE Rx-Tx Time Difference Measurements	980

10.1.25.1	Introduction	980

10.1.25.2	Measurement Accuracy Requirements	980

10.1.25.3	Report mapping	993

10.1.25.3.1	Absolute UE Rx-Tx Measurement Report Mapping	993

10.1.25.3.2	Differential UE Rx-Tx Measurement Report Mapping	995

10.1.25.3.3	Additional Path Report Mapping for UE Rx-Tx Time Difference	996

10.1.26	FR2 P-MPR report	998

10.1.26.1	Report mapping	998

10.1.27	L1-SINR accuracy requirements for FR1	998

10.1.27.1	L1-SINR accuracy requirements with CSI-RS based CMR and no dedicated IMR configured	998

10.1.27.1.1	Absolute Accuracy	998

10.1.27.1.2	Relative Accuracy	999

10.1.27.2	L1-SINR accuracy requirements with SSB based CMR and dedicated IMR configured	1000

10.1.27.2.1	Absolute Accuracy	1000

10.1.27.2.2	Relative Accuracy	1002

10.1.27.3	L1-SINR accuracy requirements with CSI-RS based CMR and dedicated IMR configured	1004

10.1.27.3.1	Absolute Accuracy	1004

10.1.27.3.2	Relative Accuracy	1006

10.1.28	L1-SINR accuracy requirements for FR2	1008

10.1.29	Intra-frequency RSRQ accuracy requirements under CCA	1015

10.1.29.1	Intra-frequency SS-RSRQ accuracy requirements in FR1	1015

10.1.29.1.1	Absolute SS-RSRQ Accuracy	1015

10.1.30	Inter-frequency RSRQ accuracy requirements under CCA	1015

10.1.30.1	Inter-frequency SS-RSRQ accuracy requirements in FR1	1015

10.1.30.1.1	Aboslute Accuracy of SS-RSRQ	1015

10.1.30.1.2	Relative Accuracy of SS-RSRQ	1016

10.1.31	Intra-frequency SINR accuracy requirements under CCA	1017

10.1.31.1	Intra-frequency SS-SINR accuracy requirements in FR1	1017

10.1.31.1.1	Absolute SS-SINR Accuracy	1017

10.1.32	Inter-frequency SINR accuracy requirements under CCA	1017

10.1.32.1	Inter-frequency SS-SINR accuracy requirements in FR1	1017

10.1.32.1.1	Aboslute Accuracy of SS-SINR	1017

10.1.32.1.2	Relative Accuracy of SS-SINR	1018

10.1.33	L1-RSRP accuracy requirements under CCA	1019

10.1.33.1	SSB based L1-RSRP accuracy requirements in FR1	1019

10.1.33.1.1	Absolute Accuracy	1019

10.1.33.1.2	Relative Accuracy	1019

10.1.34	RSSI measurements under CCA	1020

10.1.34.1	Intra-frequency absolute RSSI measurement accuracy requirements in FR1	1020

10.1.34.2	Inter-frequency absolute RSSI measurement accuracy requirements in FR1	1020

10.1.34.3	RSSI measurement report mapping	1020

10.1.35	Channel occupancy measurements under CCA	1021

10.1.35.1	Intra-frequency channel occupancy measurement accuracy requirements in FR1	1021

10.1.35.2	Inter-frequency channel occupancy measurement accuracy requirements in FR1	1021

10.1.36	Intra-frequency RSRP accuracy requirements under CCA	1021

10.1.36.1	Intra-frequency SS-RSRP accuracy requirements in FR1	1021

10.1.36.1.1	Absolute SS-RSRP Accuracy	1021

10.1.36.1.2	Relative SS-RSRP Accuracy	1022

10.1.37	Inter-frequency RSRP accuracy requirements under CCA	1023

10.1.37.1	Inter-frequency SS-RSRP accuracy requirements in FR1	1023

10.1.37.1.1	Absolute Accuracy of SS-RSRP	1023

10.1.37.1.2	Relative Accuracy of SS-RSRP	1023

10.1.38	PRS-RSRPP Measurements	1024

10.1.38.1	Introduction	1024

10.1.38.2	Measurement Accuracy Requirements	1024

10.1.38.2.1	Absolute PRS RSRPP accuracy	1024

10.1.38.3	Report mapping	1029

10.1.38.3.1	Absolute PRS-RSRPP Measurement Report Mapping	1029

10.1.38.3.2	Differential Report Mapping for PRS-RSRPP Measurement	1030

*10.1.39* UE Rx-Tx time difference measurements for RTT-based PDC	1031

10.1.39.1 *Void* 1031

10.1.39.2	 Measurement Accuracy Requirements for PRS	1031

10.1.39.3	 Measurement Accuracy Requirements for TRS	1036

10.1.40	Void	1040

10.1A	NR measurements for RedCap	1040

10.1A.1	Introduction	1040

10.1A.2	Intra-frequency RSRP accuracy requirements for FR1	1040

10.1A.2.1	Intra-frequency SS-RSRP accuracy requirements	1040

10.1A.2.1.1	Absolute SS-RSRP Accuracy	1040

10.1A.2.1.2	Relative SS-RSRP Accuracy	1041

10.1A.3	Intra-frequency RSRP accuracy requirements for FR2	1042

10.1A.3.1	Intra-frequency SS-RSRP accuracy requirements	1042

10.1A.3.1.1	Absolute SS-RSRP Accuracy	1042

10.1A.3.1.2	Relative SS-RSRP Accuracy	1042

10.1A.4	Inter-frequency RSRP accuracy requirements for FR1	1042

10.1A.4.1	Inter-frequency SS-RSRP accuracy requirements	1042

10.1A.4.1.1	Absolute Accuracy of SS-RSRP in FR1	1042

10.1A.4.1.2	Relative Accuracy of SS-RSRP in FR1	1043

10.1A.5	Inter-frequency RSRP accuracy requirements for FR2	1044

10.1A.5.1	Inter-frequency SS-RSRP accuracy requirements	1044

10.1A.5.1.1	Absolute SS-RSRP Accuracy	1044

10.1A.5.1.2	Relative SS-RSRP Accuracy	1044

10.1A.6	Intra-frequency RSRQ accuracy requirements for FR1	1044

10.1A.6.1	Intra-frequency SS-RSRQ accuracy requirements in FR1	1044

10.1A.6.1.1	Absolute SS-RSRQ Accuracy in FR1	1044

10.1A.7	Intra-frequency RSRQ accuracy requirements for FR2	1045

10.1A.7.1	Intra-frequency SS-RSRQ accuracy requirements in FR2	1045

10.1A.7.1.1	Absolute SS-RSRQ Accuracy in FR2	1045

10.1A.8	Inter-frequency RSRQ accuracy requirements for FR1	1045

10.1A.8.1	Inter-frequency SS-RSRQ accuracy requirements in FR1	1045

10.1A.8.1.1	Absolute Accuracy of SS-RSRQ in FR1	1045

10.1A.8.1.2	Relative Accuracy of SS-RSRQ in FR1	1046

10.1A.9	Inter-frequency RSRQ accuracy requirements for FR2	1047

10.1A.9.1	Inter-frequency SS-RSRQ accuracy requirements in FR2	1047

10.1A.9.1.1	Absolute Accuracy of SS-RSRQ in FR2	1047

10.1A.9.1.2	Relative Accuracy of SS-RSRQ in FR2	1047

10.1A.10	 Intra-frequency SINR accuracy requirements for FR1	1047

10.1A.10.1	Intra-frequency SS-SINR accuracy requirements in FR1	1047

10.1A.10.1.1	Absolute SS-SINR Accuracy in FR1	1047

10.1A.11	Intra-frequency SINR accuracy requirements for FR2	1048

10.1A.11.1	Intra-frequency SS-SINR accuracy requirements in FR2	1048

10.1A.11.1.1	Absolute SS-SINR Accuracy in FR2	1048

10.1A.12 	Inter-frequency SINR accuracy requirements for FR1	1048

10.1A.12.1	Inter-frequency SS-SINR accuracy requirements in FR1	1048

10.1A.12.1.1	Aboslute Accuracy of SS-SINR in FR1	1048

10.1A.12.1.2	Relative Accuracy of SS-SINR in FR1	1049

10.1A.13	Inter-frequency SINR accuracy requirements for FR2	1050

10.1A.13.1	Inter-frequency SS-SINR accuracy requirements in FR2	1050

10.1A.13.1.1	Aboslute Accuracy of SS-SINR in FR2	1050

10.1A.13.1.2	Relative Accuracy of SS-SINR in FR2	1050

10.1A.14	L1-RSRP accuracy requirements for FR1	1050

10.1A.14.1	SSB based L1-RSRP accuracy requirements	1050

10.1A.14.1.1	Absolute Accuracy	1050

10.1A.14.1.2	Relative Accuracy	1051

10.1A.14.2	CSI-RS based L1-RSRP accuracy requirements	1052

10.1A.14.2.1	Absolute Accuracy	1052

10.1A.14.2.2	Relative Accuracy	1053

10.1A.15	 L1-RSRP accuracy requirements for FR2	1054

10.1A.15.1	SSB based L1-RSRP accuracy requirements	1054

10.1A.15.1.1	Absolute Accuracy	1054

10.1A.15.1.2	Relative Accuracy	1054

10.1A.15.2	CSI-RS based L1-RSRP accuracy requirements	1054

10.1A.15.2.1	Absolute Accuracy	1054

10.1A.15.2.2	Relative Accuracy	1054

10.2	E-UTRAN measurements	1055

10.2.1	Introduction	1055

10.2.2	E-UTRAN RSRP measurements	1055

10.2.3	E-UTRAN RSRQ measurements	1055

10.2.4	E-UTRAN RSTD measurements	1055

10.2.5	E-UTRAN RS-SINR measurements	1056

10.2.6	E-UTRAN RSRP measurements for CA/DC Idle Mode Measurements	1056

10.2.7	E-UTRAN RSRQ measurements for CA/DC Idle Mode Measurements	1056

10.2A	E-UTRAN measurements for RedCap	1057

10.2A.1	Introduction	1057

10.2A.2	E-UTRAN RSRP measurements	1057

10.2A.3	E-UTRAN RSRQ measurements	1057

10.2A.4	E-UTRAN RS-SINR measurements	1058

10.3	UTRAN FDD Measurements	1058

10.3.1	UTRAN FDD CPICH RSCP	1058

10.3.2	UTRAN FDD CPICH Ec/No	1059

10.4	V2X measurements	1059

10.4.1	Introduction	1059

10.4.2	Intra-frequency PSBCH-RSRP accuracy requirements for FR1	1059

10.4.2.1	PSBCH-RSRP Absolute Accuracy	1059

10.4.2.2	PSBCH-RSRP Relative Accuracy	1060

10.4.3	Intra-Frequency SL-RSSI Measurement Accuracy Requirements for FR1	1061

10.4.3.1	Absolute SL-RSSI Accuracy	1061

10.4.4	Intra-Frequency L1 SL-RSRP Measurement Accuracy Requirements for FR1	1061

10.4.4.1	Absolute L1 SL-RSRP Accuracy	1061

10.4.5	Intra-Frequency Discovery Signal Measurement Accuracy Requirements	1062

10.4.5.1	Absolute Discovery Signal Measurement Accuracy	1062

11	Void	1063

12	V2X Requirements	1059

12.1	Introduction	1059

12.2	UE Transmit Timing	1059

12.2.1	Introduction	1059

12.2.2	GNSS as synchronization reference source	1059

12.2.3	NR Cell as synchronization reference source	1060

12.2.4	E-URTAN Cell as synchronization reference source	1060

12.2.5	SyncRef UE as synchronization reference source	1061

12.3	Initiation/Cease of SLSS Transmissions	1061

12.3.1	Introduction	1061

12.3.1.1	Initiation/Cease of SLSS transmissions with NR cell as synchronization reference source	1061

12.3.1.2	Initiation/Cease of SLSS transmissions with EUTRAN cell as synchronization reference source	1062

12.3.1.3	Initiation/Cease of SLSS transmissions with GNSS as synchronization reference source	1063

12.3.1.4	Initiation/Cease of SLSS transmissions with SyncRef UE as synchronization reference source	1063

12.4	Selection / Reselection of V2X Synchronization Reference Source	1064

12.5	L1 SL-RSRP measurements	1065

12.5.1	Introduction	1065

12.5.2	SL-RSRP measurements	1066

12.6	Congestion Control measurements	1066

12.7	Interruption	1066

12.7.1	Interruptions to WAN due to V2X Sidelink Communication	1066

12.7.2	V2X Sidelink Communication Dropping due to synchronization source change	1067

12.7.3	Interruptions to WAN due to switching between E-UTRA V2X Sidelink and NR V2X Sidelink	1068

12.7.4	Interruptions to WAN at transitions between active and non-active during SL-DRX	1069

12.7.5	Interruptions to V2X sidelink at transitions between active and non-active during DRX	1069

12.7.6	Interruptions to V2X sidelink due to Active BWP switching Requirement	1070

12.7.7	Interruptions to WAN due to SyncRef UE detection and/or Sensing during SL DRX off duration	1070

12.7.8	Interruptions at NR sidelink discovery configuration	1070

12.8	Reliability of GNSS signal	1071

12.9	Scheduling availability	1071

12.9.1	Scheduling availability of UE switching between E-UTRA sidelink and NR sidelink	1071

12.9.2	Scheduling availability of UE switching between Uu uplink  and V2X sidelink	1071

12.10	Selection / Reselection of relay UE	1072

12.10.1	Introduction	1072

12.10.2	Selection / Reselection of relay UE	1072

13	Measurement Performance Requirements for NR gNB	1072

13.1	UL-RTOA	1072

13.1.1	Report mapping	1072

13.1.1A	Additional Path Report Mapping for UL-RTOA	1074

13.2	gNB Rx-Tx time difference	1076

13.2.1	Report mapping	1076

13.2.1A	 Additional Path Report Mapping for gNB Rx-Tx	1078

13.2.2	Measurement Accuracy Requirements	1080

13.2.2.1	Introduction	1080

13.3	UL SRS RSRP measurement	1081

13.3.1	Report mapping	1081

13.3.2	Measurement accuracy requirements	1082

13.3.2.1	Introduction	1082

13.3.2.2	Requirements	1082

13.4	AoA/ZoA	1083

13.4.1	Report mapping	1083

13.5	Timing advance (TADV)	1084

13.5.1	Report mapping	1084

13.6	UL SRS RSRPP measurement	1085

13.6.1	Report mapping	1085

13.7	gNB Rx-Tx time difference measurements for RTT-based PDC	1087

13.7.1	Report mapping	1087

13.7.2	Measurement Accuracy Requirements	1087

13.7.2.1	Introduction	1087

13.7.2.2	Requirements	1087

Annex A (normative): Test Cases	1089

A.1	Purpose of annex	1089

A.2	Requirement classification for statistical testing	1089

A.2.1	Types of requirements in TS 38.133	1089

A.2.1.1	Time and delay requirements on UE higher layer actions	1089

A.2.1.2	Measurements of power levels, relative powers and time	1089

A.2.1.3	Implementation requirements	1090

A.2.1.4	Physical layer timing requirements	1090

A.2.1.5	Requirements under CCA	1090

A.3	RRM test configurations	1091

A.3.1	Reference measurement channels	1091

A.3.1.1	PDSCH	1091

A.3.1.1.1	FDD	1091

A.3.1.1.2	TDD	1092

A.3.1.2	CORESET for RMSI scheduling	1095

A.3.1.2.1	FDD	1095

A.3.1.2.2	TDD	1096

A.3.1.3	CORESET for RMC scheduling	1099

A.3.1.3.1	FDD	1099

A.3.1.3.2	TDD	1101

A.3.1.4	TDD UL/DL configuration	1106

A.3.1A	Reference measurement channels under CCA	1108

A.3.1A.1	PDSCH	1108

A.3.1A.1.1	TDD	1108

A.3.1A.2	CORESET for RMSI scheduling	1109

A.3.1A.2.1	TDD	1109

A.3.1A.3	CORESET for RMC scheduling	1110

A.3.1A.3.1	TDD	1110

A.3.1A.4	TDD UL/DL configuration	1111

A.3.1A.5	RMC burst transmission model	1111

A.3.2	OFDMA channel noise generator (OCNG)	1111

A.3.2.1	Generic OFDMA Channel Noise Generator (OCNG)	1111

A.3.2.1.1	OCNG pattern 1: Generic OCNG pattern for all unused REs	1112

A.3.2.1.2	OCNG pattern 2: Generic OCNG pattern for all unused REs for 2AoA setup	1112

A.3.2.1.3	OCNG pattern 3: Generic OCNG pattern for unused REs in the same bandwidth as CORESET	1113

A.3.2.1.4	OCNG pattern 4: Generic OCNG pattern for all unused REs outside SSB slot(s)	1113

A.3.2.2	Void	1114

A.3.3	Reference DRX configurations	1114

A.3.3.1	DRX Configuration 1: DRX cycle = 40 ms and TAT = 500 ms	1114

A.3.3.2	DRX Configuration 2: DRX cycle = 640 ms and TAT = 500 ms	1115

A.3.3.3	DRX Configuration 3: DRX cycle = 40 ms and TAT = Infinity	1115

A.3.3.4	DRX Configuration 4: DRX cycle = 160 ms and TAT = Infinity	1115

A.3.3.5	DRX Configuration 5: DRX cycle = 320 ms and TAT = Infinity	1116

A.3.3.6	DRX Configuration 6: DRX cycle = 320 ms and TAT = 500 ms	1116

A.3.3.7	DRX Configuration 7: DRX cycle = 640 ms and TAT = Infinity	1116

A.3.3.8	DRX Configuration 8: DRX cycle = 320 ms and TAT = Infinity	1117

A.3.3.9	DRX Configuration 9: DRX cycle = 40 ms and TAT = 500 ms	1117

A.3.3.10	DRX Configuration 10: DRX cycle = 640 ms and TAT = 500 ms	1117

A.3.3.11	DRX Configuration 11: DRX cycle = 20 ms and TAT = Infinity	1118

A.3.3.12	DRX Configuration 12: DRX cycle = 640 ms and TAT = Infinity	1118

A.3.3.13	DRX Configuration X1: DRX cycle = 80 ms and TAT = Infinity	1118

A.3.3.14	DRX Configuration 14: DRX cycle = 160 ms and TAT = Infinity	1119

A.3.4	Test Cases with Different Channel Bandwidths	1119

A.3.4.1	Test Cases with Different E-UTRA Channel Bandwidths	1119

A.3.4.1.1	Introduction	1119

A.3.4.1.2	Principle of testing	1119

A.3.5	Test Cases for Synchronous and Asynchronous DC Operations	1119

A.3.5.1	EN-DC Test Cases for Synchronous and Asynchronous EN-DC Operations	1119

A.3.5.1.1	Introduction	1119

A.3.5.1.2	Principle of Testing	1119

A.3.6	Antenna configurations	1120

A.3.6.1	Antenna configurations for FR1	1120

A.3.6.1.1	Antenna connection for 4 Rx capable UEs	1120

A.3.6.1.1.1	Introduction	1120

A.3.6.1.1.2	Principle of testing	1120

A.3.6.2	Antenna configurations for FR2	1123

A.3.6A	Antenna configurations with unlicensed bands	1123

A.3.6A.1	Antenna configurations for FR1	1123

A.3.6A.1.1	Antenna connection for 4 Rx capable UEs	1123

A.3.6A.1.1.1	Introduction	1123

A.3.6A.1.1.2	Principle of testing	1123

A.3.7	EN-DC test setup	1125

A.3.7.1	Introduction	1125

A.3.7.2	E-UTRAN Serving Cell Parameters	1125

A.3.7.2.1	E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR1	1125

A.3.7.2.2	E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR2	1126

A.3.7A	NR FR1-FR2 test setup	1127

A.3.7B	EN-DC test setup with unlicensed bands	1128

A.3.7B.1	Introduction	1128

A.3.7B.2	E-UTRAN Serving Cell Parameters	1128

A.3.7B.2.1	E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) under CCA in FR1	1128

A.3.7C	LTE-FR1/FR2 test setup	1129

A.3.7D	NE-DC test setup	1129

A.3.7D.1	Introduction	1129

A.3.7D.2	E-UTRAN Serving Cell Parameters	1129

A.3.7D.2.1	E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR1	1129

A.3.7D.2.2	E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR2	1129

A.3.8	PRACH configurations	1129

A.3.8.1	Introduction	1129

A.3.8.2	PRACH configurations in FR1	1130

A.3.8.2.1	FR1 PRACH configuration 1	1130

A.3.8.2.2	FR1 PRACH configuration 2	1130

A.3.8.2.3	FR1 PRACH configuration 3	1131

A.3.8.2.4	FR1 PRACH configuration 4	1132

A.3.8.3	PRACH configurations in FR2	1133

A.3.8.3.1	FR2 PRACH configuration 1	1133

A.3.8.3.2	FR2 PRACH configuration 2	1134

A.3.8.3.3	FR2 PRACH configuration 3	1135

A.3.8.3.4	FR2 PRACH configuration 4	1136

A.3.8A	PRACH configurations under CCA	1137

A.3.8A.1	Introduction	1137

A.3.8A.2	PRACH configurations in FR1	1137

A.3.8A.2.1	FR1 PRACH configuration 1 under CCA	1137

A.3.8A.2.2	FR1 PRACH configuration 2 under CCA	1138

A.3.9	BWP configurations	1139

A.3.9.1	Introduction	1139

A.3.9.2	Downlink BWP configurations	1140

A.3.9.2.1	Initial BWP	1140

A.3.9.2.2	Dedicated BWP	1140

A.3.9.3	Uplink BWP configurations	1141

A.3.9.3.1	Initial BWP	1141

A.3.9.3.2	Dedicated BWP	1141

A.3.9A	BWP configurations for RedCap	1141

A.3.9A.1	Introduction	1141

A.3.9A.2	Downlink BWP configurations	1142

A.3.9A.2.1	Dedicated BWP	1142

A.3.9A.3	Uplink BWP configurations	1142

A.3.9A.3.1	Dedicated BWP	1142

A.3.10	SSB Configurations	1143

A.3.10.1	SSB Configurations for FR1	1143

A.3.10.1.1	SSB pattern 1 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz	1143

A.3.10.1.2	SSB pattern 2 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz	1143

A.3.10.1.3	SSB pattern 3 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz	1144

A.3.10.1.4	SSB pattern 4 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz	1144

A.3.10.1.5	SSB pattern 5 in FR1: SSB allocation for SSB SCS=15 kHz starting from odd SFN in 10 MHz	1145

A.3.10.1.6	SSB pattern 6 in FR1: SSB allocation for SSB SCS=30 kHz starting from odd SFN in 40 MHz	1145

A.3.10.1.7	SSB pattern 7 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz	1146

A.3.10.1.8	SSB pattern 8 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz	1146

A.3.10.2	SSB Configurations for FR2	1147

A.3.10.2.1	SSB pattern 1 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1147

A.3.10.2.2	SSB pattern 2 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz	1147

A.3.10.2.3	SSB pattern 3 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1148

A.3.10.2.4	SSB pattern 4 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz	1148

A.3.10.2.5	SSB pattern 5 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1149

A.3.10.2.6	SSB pattern 6 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz	1149

A.3.10.2.7	SSB pattern 7 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1150

A.3.10.2.8	SSB pattern 8 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz	1150

A.3.10.2.9	SSB pattern 9 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1151

A.3.10.2.10	SSB pattern 10 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz	1151

A.3.10.2.11	SSB pattern 11 in FR2: SSB allocation for SSB SCS=480 kHz in 400 MHz	1152

A.3.10.2.12	SSB pattern 12 in FR2: SSB allocation for SSB SCS=960 kHz in 400 MHz	1152

A.3.10.2.13	SSB pattern 13 in FR2: SSB allocation for SSB SCS=480 kHz in 400 MHz	1153

A.3.10.2.14	SSB pattern 14 in FR2: SSB allocation for SSB SCS=960 kHz in 400 MHz	1153

A.3.10.2.15	SSB pattern 15 in FR2: SSB allocation for SSB SCS=480 kHz in 400 MHz	1154

A.3.10.2.16	SSB pattern 16 in FR2: SSB allocation for SSB SCS=960 kHz in 400 MHz	1154

A.3.10.2.17	SSB pattern 17 in FR2: SSB allocation for SSB SCS=480 kHz in 400 MHz	1155

A.3.10.2.18	SSB pattern 18 in FR2: SSB allocation for SSB SCS=960 kHz in 400 MHz	1155

A.3.10A	SSB Configurations under CCA	1156

A.3.10A.1	SSB Configurations under CCA for FR1	1156

A.3.10A.1.1	SSB pattern 1 under CCA for semi-static channel access: SSB allocation for SSB SCS=30kHz in 40MHz	1156

A.3.10A.1.2	SSB pattern 2 under CCA for dynamic channel access: SSB allocation for SSB SCS=30kHz in 40MHz	1156

A.3.10A.1.3	SSB pattern 3 under CCA for semi-static channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz	1157

A.3.10A.1.4	SSB pattern 4 under CCA for dynamic channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz	1157

A.3.10B	SSB Configurations for RedCap	1158

A.3.10B.1	SSB Configurations for FR1	1158

A.3.10B.1.1	SSB pattern 1 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz	1158

A.3.10B.1.2	SSB pattern 2 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz	1158

A.3.10B.1.3	SSB pattern 3 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz starting from odd SFN in 20 MHz	1159

A.3.10B.1.4	SSB pattern 4 for RedCap in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz	1159

A.3.10B.1.5	SSB pattern 5 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz	1160

A.3.10B.1.6	SSB pattern 6 for RedCap in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz	1160

A.3.10B.1.7	SSB pattern 7 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz	1161

A.3.10B.2	SSB Configurations for FR2	1161

A.3.10B.2.1	SSB pattern 1 for RedCap in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1161

A.3.10B.2.2	SSB pattern 2 for RedCap in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1162

A.3.10B.2.3	SSB pattern 3 for RedCap in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1162

A.3.10B.2.4	SSB pattern 4 for RedCap in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz	1163

A.3.10B.2.5	SSB pattern 5 for RedCap in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz	1163

A.3.11	SMTC Configurations	1164

A.3.11.1	SMTC pattern 1: SMTC period = 20 ms with SMTC duration = 1 ms	1164

A.3.11.2	SMTC pattern 2: SMTC period = 20 ms with SMTC duration = 5 ms	1164

A.3.11.3	SMTC pattern 3: SMTC period = 160 ms with SMTC duration = 1 ms	1164

A.3.11.4	SMTC pattern 4: SMTC period = 20 ms with SMTC duration = 1 ms	1164

A.3.11.5	SMTC pattern 5: SMTC period = 20 ms with SMTC duration = 5 ms	1165

A.3.11.6	SMTC pattern 6: SMTC period = 20 ms with SMTC duration = 5 ms	1165

A.3.11.7	SMTC pattern 7: SMTC period = 20 ms with SMTC duration = 5 ms	1165

A.3.11.8	SMTC pattern 8: SMTC period = 10 ms with SMTC duration = 1 ms	1165

A.3.11.9	SMTC pattern 9: SMTC period = 20 ms with SMTC duration = 1 ms	1165

A.3.11A	SMTC Configurations for RedCap	1166

A.3.11A.1	SMTC pattern 1 for RedCap: SMTC period = 40 ms with SMTC duration = 1 ms	1166

A.3.11A.2	SMTC pattern 2 for RedCap: SMTC period = 80 ms with SMTC duration = 1 ms	1166

A.3.11A.3	SMTC pattern 3 for RedCap: SMTC period = 40 ms with SMTC duration = 1 ms	1166

A.3.11A.4	SMTC pattern 4 for RedCap: SMTC period = 80 ms with SMTC duration = 5 ms	1166

A.3.11.12	SMTC pattern 12: SMTC period = 20 ms with SMTC duration = 5 ms	1166

A.3.12	Test Cases with Different CC Configurations	1167

A.3.12.1 EN-DC Test Cases with Different EN-DC Configurations	1167

A.3.12.1.1	Introduction	1167

A.3.12.1.2	Principle of testing	1167

A.3.12.2	Carrier Aggregation Test Cases with Different CA Configurations	1167

A.3.12.2.1	Introduction	1167

A.3.12.2.2	Principle of testing	1167

A.3.13	Test Cases in SA and EN-DC Operations	1167

A.3.13.1	Introduction	1167

A.3.13.2	Principle of Testing	1168

A.3.13A	Test Cases involving E-UTRA/FR1 and FR2 carriers	1168

A.3.13A.1	Introduction	1168

A.3.13A.2	Principle of Testing in EN-DC	1168

A.3.13A.3	Principle of Testing in SA	1169

A.3.13A.4	Principle of Testing in E-UTRA	1170

A.3.13B	Test Cases for EN-DC and NE-DC Operations	1171

A.3.13B.1	Active BWP switch Test Cases for EN-DC and NE-DC Operations	1171

A.3.13B.1.1	Introduction	1171

A.3.13B.1.2	Principle of Testing	1171

A.3.13B.2	SFTD accuracy Test Cases for EN-DC and NE-DC Operations	1171

A.3.13B.2.1	Introduction	1171

A.3.13B.2.2	Principle of Testing	1171

A.3.14	CSI-RS configurations	1172

A.3.14.1	FDD	1172

A.3.14.2	TDD	1174

A.3.15	Angle of Arrival (AoA) for FR2 RRM test cases	1180

A.3.15.1	Setup 1: Single AoA in Rx beam peak direction	1180

A.3.15.2	Setup 2: Single AoA in non Rx beam peak direction	1180

A.3.15.2.1	Setup 2a: Single AoA in non Rx beam peak direction without change in direction	1180

A.3.15.2.2	Setup 2b: Single AoA in non Rx beam peak direction with change in direction	1181

A.3.15.3	Setup 3: 2 AoAs	1181

A.3.15.4	Setup 4: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak	1181

A.3.15.4.1	Setup 4a: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak without change in direction	1181

A.3.15.4.2	Setup 4b: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak with change in direction	1181

A.3.16	TCI State Configuration	1182

A.3.16.1	Introduction	1182

A.3.16.2	TCI states	1182

A.3.16A	Unified TCI State Configuration	1182

A.3.16A.1	Introduction	1182

A.3.16A.2	DLorJoint TCI states	1183

A.3.16A.3	UL TCI states	1183

A.3.17	Configurations of CSI-RS for tracking	1184

A.3.17.1	Configuration of CSI-RS for tracking for FR1	1184

A.3.17.1.1	FDD	1184

A.3.17.1.2	TDD	1186

A.3.17.2	Configuration of CSI-RS for tracking for FR2	1188

A.3.17.2.1	TDD	1188

A.3.18	Additional definitions related to OTA testing for FR2 RRM test cases	1189

A.3.18.1	Introduction	1189

A.3.18.2	PRACH Power Measurement	1189

A.3.19	Test applicability for DAPS handover	1189

A.3.19.1	Introduction	1189

A.3.19.2	Principle of testing	1189

A.3.20	MsgA configurations	1190

A.3.20.1	Introduction	1190

A.3.20.2	MsgA configurations in FR1	1190

A.3.20.2.1	FR1 MsgA configuration 1	1190

A.3.20.2.2	FR1 MsgA configuration 2	1191

A.3.20.3	MsgA configurations in FR2	1193

A.3.20.3.1	FR2 MsgA configuration 1	1193

A.3.20.3.2	FR2 MsgA configuration 2	1194

A.3.20A	MsgA configurations under CCA	1196

A.3.20A.1	Introduction	1196

A.3.20A.2	MsgA configurations in FR1	1196

A.3.20A.2.1	FR1 MsgA configuration 1 under CCA	1196

A.3.20A.2.2	FR1 MsgA configuration 2 under CCA	1197

A.3.21	V2X sidelink communication	1200

A.3.21.1	Introduction	1200

A.3.21.2	Reference resource pool configurations for V2X Sidelink Communication	1200

A.3.21.3	Reference measurement channels for V2X Sidelink Communication	1204

A.3.21.4	Reference SL-DRX configurations	1205

A.3.21.4.1	SL-DRX Configuration 1: SL-DRX cycle = 40 ms	1205

A.3.21.4.2	SL-DRX Configuration 2: SL-DRX cycle = 320 ms	1205

A.3.21.4.3	SL-DRX Configuration 3: SL-DRX cycle = 640 ms	1205

A.3.22	CSI-IM configurations	1205

A.3.22.1	FDD	1205

A.3.22.2	TDD	1206

A.3.23	Spatial Relation Configuration	1207

A.3.23.1	Introduction	1207

A.3.23.2	Spatial Relation	1208

A.3.24	SRS configuration	1209

A.3.25	Channel bandwidth (CBW) configurations	1211

A.3.25.1	DL UE specific CBW	1211

A.3.25.2	UL UE specific CBW	1212

A.3.26	CCA model	1212

A.3.26.1	Introduction	1212

A.3.26.2	CCA model for operation on a carrier frequency with CCA in FR1	1212

A.3.26.2.1	DL CCA model	1212

A.3.26.2.2	UL CCA model	1214

A.3.26.3	CCA model for operation on a carrier frequency with CCA in FR2-2	1214

A.3.26.3.1	DL CCA model	1214

A.3.26.3.2	UL CCA model	1215

A.3.27	Test Cases with at Least One Cell on a Carrier Frequency with CCA	1215

A.3.27.1	Introduction	1215

A.3.27.2	 NR Standalone Tests with NR SCell under CCA and All Other NR Cells in FR1	1215

A.3.27.3	EN-DC Tests with NR PSCell under CCA and Other NR Cells in FR1	1216

A.3.27.4	NR Standalone Tests with NR PCell under CCA and Other NR Cells in FR1	1216

A.3.27.5	E-UTRA Standalone Tests with at Least One NR Cell under CCA	1216

A.3.28	Discovery Burst Transmission Window configuration under CCA	1216

A.3.28.1	DBT Window pattern 1: DBT Window period = 20 ms with DBT Window duration = 1 ms	1216

A.3.29	Testing principles for UE capable of only NR bands with shared spectrum access	1216

A.3.29.1	Introduction	1216

A.3.29.2	Principle of testing for UE capable of EN-DC with only NR bands with shared spectrum access	1216

A.3.29.3	Principle of testing for UE capable of SA operation with only NR bands with shared spectrum access	1217

A.3.30	CSI-RS configurations for RRM	1218

A.3.30.1	FDD	1218

A.3.30.2	TDD	1219

A.3.31	PRS Configurations	1221

A.3.31.1.	PRS Configurations for FR1	1221

A.3.31.1.1.	PRS pattern 1 in FR1: SCS=15 KHz	1221

A.3.31.1.2.	PRS pattern 2 in FR1: SCS=30 KHz	1222

A.3.31.2.	PRS Configurations for FR2	1222

A.3.31.2.1.	PRS pattern 1 in FR2: SCS=120 KHz	1222

A.3.32	NR sidelink discovery	1222

A.3.32.1	Introduction	1222

A.3.32.2	Reference resource pool configurations for NR Sidelink Discovery	1222

A.3.32.3	Principle of Testing	1223

A.3.33	PRS Processing Window (PPW) configurations	1223

A.3.34	Testing principles for test cases related to PRS measurements	1223

A.3.34.1	Introduction	1223

A.3.34.2	Test cases in RRC\_INACTIVE state	1224

A.3.34.3	Test cases for PRS measurements with gaps in RRC\_CONNECTED state	1224

A.3.34.4	Test cases for PRS measurements without gaps in RRC\_CONNECTED state	1224

A.3.35	Testing principle for RedCap UE	1225

A.3.35.1	Introduction	1225

A.3.35.2	Principle of testing for FR1	1225

A.3.35.3	Principle of testing for FR2	1225

A.3.36	Testing related to Satellite access	1225

A.3.36.1	Introduction	1225

A.3.36.2	Principle of testing GSO and NGSO scenarios	1225

A.3.36.2	Principle of testing different RRM requirements	1226

A.3.36.3	Principle of testing different ephemeris formats	1226

A.3.36.4	General setup for SIB19	1228

A.3.36.5	Satellite specific parameters configuration	1229

A.3.36.5.1	Satellite specific configuration for serving cell	1229

A.3.36.5.2	Satellite specific configuration for neighbour cell	1230

A.4	EN-DC tests with all NR cells in FR1	1227

A.4.1	Void	1227

A.4.2	Void	1227

A.4.3	RRC\_CONNECTED state mobility	1227

A.4.3.1	Void	1227

A.4.3.2	RRC Connection Mobility Control	1227

A.4.3.2.1	Void	1227

A.4.3.2.2	Random Access	1227

A.4.3.2.2.1	4-step RA type contention based random access test in FR1 for PSCell in EN-DC	1227

A.4.3.2.2.2	4-step RA type n on-contention based random access test in FR1 for PSCell in EN-DC	1231

A.4.3.2.2.3	2-step RA type contention based random access test in FR1 for PSCell in EN-DC	1235

A.4.3.2.2.4	2-step RA type n on-contention based random access test in FR1 for PSCell in EN-DC	1239

A.4.3.2.3	Void	1243

A.4.3.3	Handover with PSCell from EN-DC to EN-DC with known target PSCell in FR1	1243

A.4.3.3.1	Test Purpose and Environment	1243

A.4.3.3.2	Test Requirements	1249

A.4.4	Timing	1250

A.4.4.1	UE transmit timing	1250

A.4.4.1.1	NR UE Transmit Timing Test for FR1	1250

A.4.4.1.1.1	Test Purpose and environment	1250

A.4.4.1.1.2	Test requirements	1254

A.4.4.2	UE timer accuracy	1254

A.4.4.3	Timing advance	1254

A.4.4.3.1	EN-DC FR1 timing advance adjustment accuracy	1254

A.4.4.3.1.1	Test Purpose and Environment	1254

A.4.4.3.1.2	Test Parameters	1254

A.4.4.3.1.3	Test Requirements	1258

A.4.5	Signaling characteristics	1258

A.4.5.1	Radio link Monitoring	1258

A.4.5.1.1	Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in non-DRX mode	1259

A.4.5.1.1.1	Test Purpose and Environment	1259

A.4.5.1.1.2	Test Requirements	1263

A.4.5.1.2	Radio Link Monitoring In-sync Test for FR1 PSCell configured with SSB-based RLM RS in non-DRX mode	1263

A.4.5.1.2.1	Test Purpose and Environment	1263

A.4.5.1.2.2	Test Requirements	1269

A.4.5.1.3	Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in DRX mode	1269

A.4.5.1.3.1	Test Purpose and Environment	1269

A.4.5.1.3.2	Test Requirements	1274

A.4.5.1.4	Radio Link Monitoring In-sync Test for FR1 PSCell configured with SSB-based RLM RS in DRX mode	1274

A.4.5.1.4.1	Test Purpose and Environment	1274

A.4.5.1.4.2	Test Requirements	1280

A.4.5.1.5	EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode	1280

A.4.5.1.5.1	Test Purpose and Environment	1280

A.4.5.1.5.2	Test Requirements	1285

A.4.5.1.6	EN-DC Radio Link Monitoring In-sync Test for FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode	1285

A.4.5.1.6.1	Test Purpose and Environment	1285

A.4.5.1.6.2	Test Requirements	1291

A.4.5.1.7	EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with CSI-RS-based RLM in DRX mode	1291

A.4.5.1.7.1	Test Purpose and Environment	1291

A.4.5.1.7.2	Test Requirements	1296

A.4.5.1.8	EN-DC Radio Link Monitoring In-sync Test for FR1 PSCell configured with CSI-RS-based RLM in DRX mode	1297

A.4.5.1.8.1	Test Purpose and Environment	1297

A.4.5.1.8.2	Test Requirements	1302

A.4.5.1.9	Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS for UE fulfilling relaxed measurement criterion	1302

A.4.5.1.9.1	Test Purpose and Environment	1302

A.4.5.2	Interruption	1308

A.4.5.2.1	E-UTRAN – NR FR1 interruptions at transitions between active and non-active during DRX in synchronous EN-DC	1308

A.4.5.2.1.1	Test Purpose and Environment	1308

A.4.5.2.1.2	Test Requirements	1312

A.4.5.2.2	E-UTRAN – NR FR1 interruptions at transitions between active and non-active during DRX in asynchronous EN-DC	1312

A.4.5.2.2.1	Test Purpose and Environment	1312

A.4.5.2.2.2	Test Requirements	1316

A.4.5.2.3	E-UTRAN – NR FR1 interruptions during measurements on deactivated NR SCC in synchronous EN-DC	1316

A.4.5.2.3.1	Test Purpose and Environment	1316

A.4.5.2.3.2	Test Requirements	1323

A.4.5.2.4	E-UTRAN – NR FR1 interruptions during measurements on deactivated NR SCC in asynchronous EN-DC	1324

A.4.5.2.4.1	Test Purpose and Environment	1324

A.4.5.2.4.2	Test Requirements	1328

A.4.5.2.5	E-UTRAN – NR FR1 interruptions during measurements on deactivated E-UTRAN SCC in synchronous EN-DC	1329

A.4.5.2.5.1	Test Purpose and Environment	1329

A.4.5.2.5.2	Test Requirements	1332

A.4.5.2.6	E-UTRAN – NR FR1 interruptions during measurements on deactivated E-UTRAN SCC in asynchronous EN-DC	1332

A.4.5.2.6.1	Test Purpose and Environment	1332

A.4.5.2.6.2	Test Requirements	1336

A.4.5.2.7	Void	1336

A.4.5.2.8	E-UTRAN - NR FR1 interruptions at NR SRS carrier based switching in asynchronous EN-DC	1336

A.4.5.2.8.1	Test Purpose and Environment	1336

A.4.5.2.8.2	Test Requirements	1339

A.4.5.2.9	E-UTRAN – NR interruptions at E-UTRA SRS carrier based switching	1340

A.4.5.2.9.1	Test Purpose and Environment	1340

A.4.5.2.9.2	Test Requirements	1343

A.4.5.2.10	E-UTRAN – NR FR1 interruptions due to RRM and RLM/BFD measurements on deactivated NR PSCell	1344

A.4.5.2.10.1	Test Purpose and Environment	1344

A.4.5.2.10.2	Test Requirements	1347

A.4.5.2.11	E-UTRAN - NR FR1 interruptions at NR SRS antenna port switching with 1 SRS symbol in a slot in synchronous EN-DC	1347

A.4.5.2.11.1	Test Purpose and Environment	1347

A.4.5.2.11.2	Test Requirements	1352

A.4.5.2.12	E-UTRAN - NR FR1 interruptions at NR SRS antenna port switching in asynchronous EN-DC	1353

A.4.5.2.12.1	Test Purpose and Environment	1353

A.4.5.3	SCell Activation and Deactivation Delay	1361

A.4.5.3.1	SCell Activation and deactivation of known SCell in FR1 for 160ms SCell measurement cycle	1361

A.4.5.3.1.1	Test Purpose and Environment	1361

A.4.5.3.1.2	Test Requirements	1367

A.4.5.3.2	SCell Activation and deactivation of known SCell in FR1 for 640ms SCell measurement cycle	1368

A.4.5.3.2.1	Test Purpose and Environment	1368

A.4.5.3.2.2	Test Requirements	1368

A.4.5.3.3	SCell Activation and deactivation of unknown SCell in FR1	1368

A.4.5.3.3.1	Test Purpose and Environment	1368

A.4.5.3.3.2	Test Requirements	1369

A.4.5.3.4	SCell Activation and deactivation of multiple unknown SCells in FR1 with single activation/deactivation command	1370

A.4.5.3.4.1	Test Purpose and Environment	1370

A.4.5.3.4.2	Test Requirements	1372

A.4.5.3.5	Direct SCell activation at SCell addition of known SCell in FR1	1373

A.4.5.3.5.1	Test Purpose and Environment	1373

A.4.5.3.5.2	Test Requirements	1380

A.4.5.3.6	Fast SCell Activation of known SCell in FR1 for 160ms SCell measurement cycle	1381

A.4.5.3.6.1	Test Purpose and Environment	1381

A.4.5.3.6.2	Test Requirements	1385

A.4.5.3.7	Fast SCell Activation of known SCell in FR1 for 640 ms SCell measurement cycle	1386

A.4.5.3.7.1	Test Purpose and Environment	1386

A.4.5.3.7.2	Test Requirements	1386

A.4.5.4	UE UL carrier RRC reconfiguration Delay	1387

A.4.5.4.1	UE UL carrier RRC reconfiguration Delay	1387

A.4.5.4.1.1	Test Purpose and Environment	1387

A.4.5.4.1.2	Test Requirements	1395

A.4.5.5	Beam Failure Detection and Link recovery procedures	1395

A.4.5.5.1	EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in non-DRX mode	1395

A.4.5.5.1.1	Test Purpose and Environment	1395

A.4.5.5.1.2	Test Requirements	1401

A.4.5.5.2	EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in DRX mode	1402

A.4.5.5.2.1	Test Purpose and Environment	1402

A.4.5.5.2.2	Test Requirements	1407

A.4.5.5.3	EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with CSI-RS-based BFD and LR in non-DRX mode	1408

A.4.5.5.3.1	Test Purpose and Environment	1408

A.4.5.5.3.2	Test Requirements	1413

A.4.5.5.4	EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with CSI-RS-based BFD and LR in DRX mode	1414

A.4.5.5.4.1	Test Purpose and Environment	1414

A.4.5.5.4.2	Test Requirements	1419

A.4.5.5.5	EN-DC Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in non-DRX mode	1420

A.4.5.5.5.1	Test Purpose and Environment	1420

A.4.5.5.5.2	Test Requirements	1425

A.4.5.5.6	EN-DC Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in DRX mode	1426

A.4.5.5.6.1	Test Purpose and Environment	1426

A.4.5.5.6.2	Test Requirements	1432

A.4.5.5.7	EN-DC TRP specific Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in non-DRX mode	1433

A.4.5.5.7.1	Test Purpose and Environment	1433

A.4.5.5.7.2	Test Requirements	1438

A.4.5.5.8	EN-DC TRP specific Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in non-DRX mode	1439

A.4.5.5.8.1	Test Purpose and Environment	1439

A.4.5.5.8.2	Test Requirements	1445

A.4.5.6	Active BWP switch	1446

A.4.5.6.1	DCI-based and Timer-based Active BWP Switch	1446

A.4.5.6.1.1	E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC	1446

A.4.5.6.1.2	E-UTRAN – NR PSCell FR1 DL active BWP switch with FR1 SCell in non-DRX in synchronous EN-DC	1451

A.4.5.6.2	RRC-based Active BWP Switch	1457

A.4.5.6.3	Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs	1461

A.4.5.6.3.1	Simultaneous E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in EN-DC on multiple CCs	1461

A.4.5.6.3.1.1	Test Purpose and Environment	1461

A.4.5.6.4	Simultaneous RRC-based Active BWP Switch on multiple CCs	1467

A.4.5.6.4.1	E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC on multiple CCs	1467

A.4.5.6.4.1.1	Test Purpose and Environment	1467

A.4.5.6.4.1.2	Test Requirements	1474

A.4.5.6.4.2	E-UTRAN – NR FR1 PSCell SCell dormancy switch of two FR1 SCells inside active time	1474

A.4.5.6.4.2.1	Test Purpose and Environment	1474

A.4.5.6.4.2.2	Test Requirements	1484

A.4.5.6.5	SCell dormancy switch	1485

A.4.5.6.5.1	E-UTRAN – NR FR1 PSCell SCell dormancy switch of single FR1 SCell outside active time	1485

A.4.5.6.5.2	E-UTRAN – NR FR1 PSCell SCell dormancy switch of two FR1 SCells inside active time	1490

A.4.5.6.5.2.1	Test Purpose and Environment	1490

A.4.5.6.5.2.2	Test Requirements	1496

A.4.5.7	PSCell addition and release delay	1496

A.4.5.7.1	Addition and Release Delay of known NR PSCell	1496

A.4.5.7.1.1	Test purpose and environment	1496

A.4.5.7.1.2	Test Requirements	1501

A.4.5.8	DL Interruptions at switching between two uplink carriers	1502

A.4.5.8.1	Test Purpose and Environment	1502

A.4.5.8.2	Test Requirements	1505

A.4.5.9	UE specific CBW change	1506

A.4.5.9.1	UE specific CBW change on FR1 NR PSCell with non-DRX in synchronous EN- DC	1506

A.4.5.9.1.1	Test Purpose and Environment	1506

A.4.5.9.1.2	Test Requirements	1510

A.4.5.10	PSCell activation and deactivation delay	1510

A.4.5.10.1	PSCell activation and deactivation delay	1510

A.4.5.10.1.1	Test purpose and environment	1510

A.4.5.10.1.2	Test Requirements	1514

A.4.5.11	Conditional PSCell addition and release delay (FR1 EN-DC)	1515

A.4.5.11.1	Conditional PSCell Addition and Release Delay	1515

A.4.5.11.1.1	Test purpose and environment	1515

A.4.5.11.1.2	Test Parameters	1515

A.4.5.11.1.3	Test Requirements	1519

A.4.6	Measurement procedure	1519

A.4.6.1	Intra-frequency Measurements	1519

A.4.6.1.1	EN-DC event triggered reporting tests without gap under non-DRX	1519

A.4.6.1.1.1	Test purpose and Environment	1519

A.4.6.1.1.2	Test parameters	1519

A.4.6.1.1.3	Test Requirements	1523

A.4.6.1.2	EN-DC event triggered reporting tests without gap under DRX	1523

A.4.6.1.2.1	Test purpose and Environment	1523

A.4.6.1.2.2	Test parameters	1523

A.4.6.1.2.2	Test Requirements	1527

A.4.6.1.3	EN-DC event triggered reporting tests with per-UE gaps under non-DRX	1527

A.4.6.1.3.1	Test purpose and Environment	1527

A.4.6.1.3.2	Test parameters	1527

A.4.6.1.3.3	Test Requirements	1531

A.4.6.1.4	EN-DC event triggered reporting tests with per-UE gaps under DRX	1531

A.4.6.1.4.1	Test purpose and Environment	1531

A.4.6.1.4.2	Test parameters	1531

A.4.6.1.4.3	Test Requirements	1535

A.4.6.1.5	EN-DC event triggered reporting tests without gap under non-DRX with SSB index reading	1535

A.4.6.1.5.1	Test purpose and Environment	1535

A.4.6.1.5.2	Test parameters	1535

A.4.6.1.5.3	Test Requirements	1537

A.4.6.1.6	EN-DC event triggered reporting tests with SSB index reading with per-UE gaps	1538

A.4.6.1.6.1	Test purpose and Environment	1538

A.4.6.1.6.2	Test parameters	1538

A.4.6.1.6.3	Test Requirements	1540

A.4.6.1.7	EN-DC event triggered reporting tests under DRX for UE configured with highSpeedMeasFlag-r16	1541

A.4.6.1.7.1	Test purpose and Environment	1541

A.4.6.1.7.2	Test parameters	1541

A.4.6.1.7.3	Test Requirements	1545

A.4.6.1.8	EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used for UE configured with *highSpeedMeasCA-Scell-r17* 1545

A.4.6.1.8.1	Test Purpose and Environment	1545

A.4.6.1.8.2	Test Requirements	1550

A.4.6.2	Inter-frequency Measurements	1551

A.4.6.2.1	EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is not used	1551

A.4.6.2.1.1	Test Purpose and Environment	1551

A.4.6.2.1.2	Test Requirements	1555

A.4.6.2.2	EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used	1555

A.4.6.2.2.1	Test Purpose and Environment	1555

A.4.6.2.2.2	Test Requirements	1559

A.4.6.2.3	Void	1559

A.4.6.2.4	Void	1559

A.4.6.2.5	EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is not used	1559

A.4.6.2.5.1	Test Purpose and Environment	1559

A.4.6.2.5.2	Test Requirements	1564

A.4.6.2.6	EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is used	1564

A.4.6.2.6.1	Test Purpose and Environment	1564

A.4.6.2.6.2	Test Requirements	1569

A.4.6.2.7	Void	1569

A.4.6.2.8	Void	1569

A.4.6.2.9	EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used for UE configured with highSpeedMeasInterFreq-r17	1570

A.4.6.2.9.1	Test Purpose and Environment	1570

A.4.6.2.9.2	Test Requirements	1573

A.4.6.3	Void	1573

A.4.6.4	L1-RSRP measurement for beam reporting	1573

A.4.6.4.1	SSB based L1-RSRP measurement when DRX is not used	1573

A.4.6.4.1.1	Test Purpose and Environment	1573

A.4.6.4.1.2	Test parameters	1574

A.4.6.4.1.3	Test Requirements	1577

A.4.6.4.2	SSB based L1-RSRP measurement when DRX is used	1577

A.4.6.4.2.1	Test Purpose and Environment	1577

A.4.6.4.2.2	Test parameters	1578

A.4.6.4.2.3	Test Requirements	1581

A.4.6.4.3	CSI-RS based L1-RSRP measurement when DRX is not used	1581

A.4.6.4.3.1	Test Purpose and Environment	1581

A.4.6.4.3.2	Test parameters	1582

A.4.6.4.3.3	Test Requirements	1585

A.4.6.4.4	CSI-RS based L1-RSRP measurement when DRX is used	1585

A.4.6.4.4.1	Test Purpose and Environment	1585

A.4.6.4.4.2	Test parameters	1586

A.4.6.4.4.3	Test Requirements	1588

A.4.6.4.5	SSB based L1-RSRP measurement when DRX is used for UE configured with *highSpeedMeasFlag-r16* 1588

A.4.6.4.5.1	Test Purpose and Environment	1588

A.4.6.4.5.2	Test parameters	1589

A.4.6.4.5.3	Test Requirements	1592

A.4.6.5	CLI measurements	1592

A.4.6.5.1	SRS-RSRP measurement with non-DRX	1592

A.4.6.5.1.1	Test Purpose and Environment	1592

A.4.6.5.1.2	Test Parameters	1593

A.4.6.5.1.3	Test Requirements	1596

A.4.6.5.2	CLI-RSSI measurement with non-DRX	1596

A.4.6.5.2.1	Test Purpose and Environment	1596

A.4.6.5.2.2	Test Parameters	1597

A.4.6.5.2.3	Test Requirements	1598

A.4.6.6.1.2	Test Requirements	1603

A.4.6.7	L1-SINR measurement for beam reporting	1604

A.4.6.7.2	L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is used	1606

A.4.6.7.2.1	Test Purpose and Environment	1606

A.4.6.7.2.2	Test parameters	1607

A.4.6.7.2.3	Test Requirements	1609

A.4.6.7.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is used	1609

A.4.6.7.3.1	Test Purpose and Environment	1609

A.4.6.7.3.2	Test parameters	1609

A.4.6.7.3.3	Test Requirements	1611

A.4.6.8	CSI-RS based intra-frequency Measurement	1612

A.4.6.8.1	EN-DC event triggered reporting tests without gap under DRX	1612

A.4.6.8.1.1	Test purpose and Environment	1612

A.4.6.8.1.2	Test Requirements	1616

A.4.6.9	CSI-RS based inter-frequency Measurement	1616

A.4.6.9.1	EN-DC event triggered reporting tests for FR1 cell when non-DRX is used	1616

A.4.6.9.1.1	Test Purpose and Environment	1616

A.4.6.9.1.2	Test Requirements	1620

A.4.7	Measurement Performance requirements	1621

A.4.7.1	SS-RSRP	1621

A.4.7.1.1	EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1621

A.4.7.1.1.1	Test Purpose and Environment	1621

A.4.7.1.1.2	Test parameters	1621

A.4.7.1.1.3	Test Requirements	1625

A.4.7.1.2	EN-DC inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1625

A.4.7.1.2.1	Test Purpose and Environment	1625

A.4.7.1.2.2	Test parameters	1626

A.4.7.1.2.3	Test Requirements	1630

A.4.7.1.3	Void	1630

A.4.7.2	SS-RSRQ	1630

A.4.7.2.1	EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1630

A.4.7.2.1.1	Test Purpose and Environment	1630

A.4.7.2.1.2	Test Parameters	1631

A.4.7.2.1.3	Test Requirements	1635

A.4.7.2.2	EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1635

A.4.7.2.2.1	Test Purpose and Environment	1635

A.4.7.2.2.2	Test Parameters	1635

A.4.7.2.2.3	Test Requirements	1640

A.4.7.3	SS-SINR	1640

A.4.7.3.1	EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1640

A.4.7.3.1.1	Test Purpose and Environment	1640

A.4.7.3.1.2	Test Parameters	1640

A.4.7.3.1.3	Test Requirements	1643

A.4.7.3.2	EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1643

A.4.7.3.2.1	Test Purpose and Environment	1643

A.4.7.3.2.2	Test Parameters	1643

A.4.7.3.2.3	Test Requirements	1648

A.4.7.4	L1-RSRP measurement for beam reporting	1648

A.4.7.4.1	SSB based L1-RSRP measurement	1648

A.4.7.4.1.1	Test Purpose and Environment	1648

A.4.7.4.1.2	Test parameters	1649

A.4.7.4.1.3	Test Requirements	1652

A.4.7.4.2	CSI-RS based L1-RSRP measurement on resource set with repetition off	1652

A.4.7.4.2.1	Test Purpose and Environment	1652

A.4.7.4.2.2	Test parameters	1653

A.4.7.4.2.3	Test Requirements	1656

A.4.7.5	SFTD accuracy	1656

A.4.7.5.1	SFTD accuracy	1656

A.4.7.5.1.1	Test Purpose and Environment	1656

A.4.7.5.1.2	Test Parameters	1656

A.4.7.5.1.3	Test Requirements	1661

A.4.7.5.2	Void	1661

A.4.7.5.3	Void	1661

A.4.7.6	CLI measurements	1661

A.4.7.6.1	EN-DC SRS-RSRP measurement accuracy with FR1 serving cell	1661

A.4.7.6.1.1	Test Purpose and Environment	1661

A.4.7.6.1.2	Test parameters	1662

A.4.7.6.1.3	Test Requirements	1667

A.4.7.6.2	EN-DC CLI-RSSI measurement accuracy with FR1 serving cell	1667

A.4.7.6.2.1	Test Purpose and Environment	1667

A.4.7.6.2.2	Test parameters	1668

A.4.7.6.2.3	Test Requirements	1671

A.4.7.7	L1-SINR measurement for beam reporting	1671

A.4.7.7.2	L1-SINR measurement with SSB based CMR and dedicated IMR	1675

A.4.7.7.2.1	Test Purpose and Environment	1675

A.4.7.7.2.2	Test parameters	1675

A.4.7.7.2.3	Test Requirements	1679

A.4.7.7.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR	1679

A.4.7.7.3.1	Test Purpose and Environment	1679

A.4.7.7.3.2	Test parameters	1679

A.4.7.7.3.3	Test Requirements	1682

A.4.7.8	CSI-RSRP	1682

A.4.7.8.1	EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1682

A.4.7.8.1.1	Test Purpose and Environment	1682

A.4.7.8.1.2	Test parameters	1683

A.4.7.8.1.3	Test Requirements	1688

A.4.7.8.2	EN-DC inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1688

A.4.7.8.2.1	Test Purpose and Environment	1688

A.4.7.8.2.2	Test parameters	1688

A.4.7.8.2.3	Test Requirements	1693

A.4.7.9	CSI-RSRQ	1693

A.4.7.9.1	EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1693

A.4.7.9.1.1	Test Purpose and Environment	1693

A.4.7.9.1.2	Test Parameters	1693

A.4.7.9.1.3	Test Requirements	1698

A.4.7.9.2	EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1698

A.4.7.9.2.1	Test Purpose and Environment	1698

A.4.7.9.2.2	Test Parameters	1698

A.4.7.9.2.3	Test Requirements	1703

A.4.7.10	CSI-SINR	1703

A.4.7.10.1	EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1703

A.4.7.10.1.1	Test Purpose and Environment	1703

A.4.7.10.1.2	Test Parameters	1704

A.4.7.10.1.3	Test Requirements	1708

A.4.7.10.2	EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1709

A.4.7.10.2.1	Test Purpose and Environment	1709

A.4.7.10.2.2	Test Parameters	1709

A.4.7.10.2.3	Test Requirements	1713

A.4.8	Void	1714

A.4A	NE-DC test with all NR cells in FR1	1714

A.4A.1	Signaling characteristics	1714

A.4A.1.1	E-UTRAN PSCell addition	1714

A.4A.1.1.1	Test purpose and environment	1714

A.4A.1.1.2	Test Requirements	1718

A.4A.1.2	Active BWP switch	1719

A.4A.1.2.1	E-UTRAN PSCell – NR PCell FR1 DCI-based and Timer-based DL active BWP switch in non-DRX in synchronous NE-DC	1719

A.4A.1.2.1.1	Test Purpose and Environment	1719

A.4A.1.2.1.2	Test Requirements	1723

A.4A.1.3	Intra-frequency handover with E-UTRAN PSCell	1724

A.4A.1.3.1	Test purpose and environment	1724

A.4A.1.3.2	Test Requirements	1728

A.4A.1.4	Handover with PSCell from NE-DC to NE-DC with unknown target PSCell	1729

A.4A.1.4.1	Test Purpose and Environment	1729

A.4A.1.4.2	Test Parameters	1729

A.4A.1.4.3	Test Requirements	1734

A.4A.1.4.3.1	Test Requirements for NR HO	1734

A.4A.1.4.3.2	Test Requirements for LTE PSCell Change	1734

A.4A.2	Measurement performance	1735

A.4A.2.1	SFTD accuracy	1735

A.4A.2.1.1	SFTD accuracy	1735

A.4A.2.1.1.1	Test Purpose	1735

A.4A.2.1.1.2	Test Environment	1735

A.4A.2.1.1.3	Test Requirements	1739

A.5	EN-DC tests with one or more NR cells in FR2	1740

A.5.1	Void	1740

A.5.2	Void	1740

A.5.3	RRC\_CONNECTED state mobility	1740

A.5.3.1	Void	1740

A.5.3.2	RRC Connection Mobility Control	1740

A.5.3.2.1	Void	1740

A.5.3.2.2	Random Access	1740

A.5.3.2.2.1	4-step RA type c ontention based random access test in FR2 for PSCell/SCell in EN-DC	1740

A.5.3.2.2.2	4-step RA type non-contention based random access test in FR2 for PSCell/SCell in EN-DC	1743

A.5.3.2.2.3	2-step RA type contention based random access test in FR2 for PSCell/SCell in EN-DC	1749

A.5.3.2.2.4	2-step RA type non-contention based random access test in FR2 for PSCell/SCell in EN-DC	1752

A.5.3.2.3	Void	1756

A.5.3.3	Handover with PSCell with known FR2 target PSCell	1756

A.5.3.3.1	Test purpose and environment	1756

A.5.3.3.2	Test Requirements	1761

A.5.5.3.3	void	1762

A.5.5.3.4	void	1762

A.5.5.3.5	void	1762

A.5.5.3.6	void	1762

A.5.4	Timing	1762

A.5.4.1	UE transmit timing	1762

A.5.4.1.1	NR UE Transmit Timing Test for FR2	1762

A.5.4.1.1.1	Test Purpose and environment	1762

A.5.4.1.1.2	Test requirements	1765

A.5.4.2	UE timer accuracy	1766

A.5.4.3	Timing advance	1766

A.5.4.3.1 EN-DC FR2 timing advance adjustment accuracy	1766

A.5.4.3.1.1 Test Purpose and Environment	1766

A.5.4.3.1.2 Test Parameters	1766

A.5.4.3.1.3	Test Requirements	1770

A.5.5	Signaling characteristics	1770

A.5.5.1	Radio link Monitoring	1770

A.5.5.1.1	Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode	1770

A.5.5.1.1.1	Test Purpose and Environment	1770

A.5.5.1.1.2	Test Requirements	1774

A.5.5.1.2	Radio Link Monitoring In-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode	1775

A.5.5.1.2.1	Test Purpose and Environment	1775

A.5.5.1.2.2	Test Requirements	1778

A.5.5.1.3	Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in DRX mode	1779

A.5.5.1.3.1	Test Purpose and Environment	1779

A.5.5.1.3.2	Test Requirements	1783

A.5.5.1.4	Radio Link Monitoring In-sync Test for FR2 PSCell configured with SSB-based RLM RS in DRX mode	1783

A.5.5.1.4.1	Test Purpose and Environment	1783

A.5.5.1.4.2	Test Requirements	1787

A.5.5.1.5	EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with CSI-RS-based RLM in non-DRX mode	1787

A.5.5.1.6	EN-DC Radio Link Monitoring In-sync Test for FR2 PSCell configured with CSI-RS-based RLM in non-DRX mode	1791

A.5.5.1.7	EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with CSI-RS-based RLM in DRX mode	1795

A.5.5.1.8	EN-DC Radio Link Monitoring In-sync Test for FR2 PSCell configured with CSI-RS-based RLM in DRX mode	1800

A.5.5.1.8.2	Test Requirements	1804

A.5.5.1.9	EN-DC Radio Link Monitoring UE Scheduling Restrictions on FR2	1805

A.5.5.1.9.1	Test Purpose and Environment	1805

A.5.5.1.9.2	Test Requirements	1807

A.5.5.1.10	Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS for UE fulfilling relaxed measurement criterion	1807

A.5.5.1.10.1	Test Purpose and Environment	1807

A.5.5.1.10.2	Test Requirements	1810

A.5.5.2	Interruption	1810

A.5.5.2.1	E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in synchronous EN-DC	1810

A.5.5.2.1.1	Test Purpose and Environment	1810

A.5.5.2.1.2	Test Requirements	1813

A.5.5.2.2	E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in asynchronous EN-DC	1813

A.5.5.2.2.1	Test Purpose and Environment	1813

A.5.5.2.2.2	Test Requirements	1816

A.5.5.2.3	E-UTRAN – NR FR2 interruptions during measurements on deactivated NR SCC in synchronous EN-DC	1816

A.5.5.2.3.1	Test Purpose and Environment	1816

A.5.5.2.3.2	Test Requirements	1820

A.5.5.2.4	E-UTRAN – NR FR2 interruptions during measurements on deactivated NR SCC in asynchronous EN-DC	1820

A.5.5.2.4.1	Test Purpose and Environment	1820

A.5.5.2.4.2	Test Requirements	1823

A.5.5.2.5	E-UTRAN – NR FR2 interruptions during measurements on deactivated E-UTRAN SCC in synchronous EN-DC	1824

A.5.5.2.5.1	Test Purpose and Environment	1824

A.5.5.2.5.2	Test Requirements	1827

A.5.5.2.6	E-UTRAN – NR FR2 interruptions during measurements on deactivated E-UTRAN SCC in asynchronous EN-DC	1827

A.5.5.2.6.1	Test Purpose and Environment	1827

A.5.5.2.6.2	Test Requirements	1830

A.5.5.2.7	E-UTRAN – NR FR2 interruptions at E-UTRA SRS carrier based switching	1830

A.5.5.2.7.1	Test Purpose and Environment	1830

A.5.5.2.7.2	Test Requirements	1834

A.5.5.2.8 E-UTRAN – NR FR2 interruptions at NR SRS carrier based switching	1834

A.5.5.2.8.1 Test Purpose and Environment	1834

A.5.5.2.8.3	Test Requirements	1836

A.5.5.3	SCell Activation and Deactivation Delay	1836

A.5.5.3.1	SCell Activation and deactivation of SCell in FR2 intra-band	1836

A.5.5.3.1.1	Test Purpose and Environment	1836

A.5.5.3.1.2	Test Requirements	1838

A.5.5.3.2	SCell Activation and deactivation of known SCell in FR1 for 160ms SCell measurement cycle	1838

A.5.5.3.2.1	Test Purpose and Environment	1838

A.5.5.3.2.2	Test Requirements	1842

A.5.5.3.3	Void	1842

A.5.5.3.4	Void	1842

A.5.5.3.5	SCell Activation and deactivation of SCell in FR2	1842

A.5.5.3.5.1	Test Purpose and Environment	1842

A.5.5.3.5.2	Test Requirements	1845

A.5.5.3.6	Multiple SCell Activation and deactivation of one unknown SCell and one known SCell in FR2	1846

A.5.5.3.6.1	Test Purpose and Environment	1846

A.5.5.3.6.2	Test Requirements	1850

A.5.5.3.7	Direct SCell activation at SCell addition of known SCell in FR2	1851

A.5.5.3.7.1	Test Purpose and Environment	1851

A.5.5.3.7.2	Test Requirements	1854

A.5.5.3.8	Fast SCell Activation of SCell in FR2 intra-band	1854

A.5.5.3.8.1	Test Purpose and Environment	1854

A.5.5.3.8.2	Test Requirements	1858

A.5.5.3.9	PUCCH SCell Activation and deactivation of known SCell in FR2	1859

A.5.5.3.9.1	Test Purpose and Environment	1859

A.5.5.3.9.2	Test Requirements	1862

A.5.5.3.10	PUCCH SCell Activation and deactivation of unknown SCell in FR2	1863

A.5.5.3.10.1	Test Purpose and Environment	1863

A.5.5.3.10.2	Test Requirements	1866

A.5.5.3.11	Multiple SCell activation and deactivation of one known PUCCH SCell and one unknown SCell in FR2	1867

A.5.5.3.11.1	Test Purpose and Environment	1867

A.5.5.3.11.2	Test Requirements	1870

A.5.5.3.12	SCell Activation and deactivation of unknown PUCCH SCell and unknown DL SCell in FR2 in non-DRX	1871

A.5.5.3.12.1	Test Purpose and Environment	1871

A.5.5.3.12.2	Test Requirements	1874

A.5.5.4	Void	1875

A.5.5.5	Beam Failure Detection and Link recovery procedures	1875

A.5.5.5.1	EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with SSB-based BFD and LR in non-DRX mode	1875

A.5.5.5.1.1	Test Purpose and Environment	1875

A.5.5.5.1.2	Test Requirements	1879

A.5.5.5.2	EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with SSB-based BFD and LR in DRX mode	1880

A.5.5.5.2.1	Test Purpose and Environment	1880

A.5.5.5.2.2	Test Requirements	1884

A.5.5.5.3	EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with CSI-RS-based BFD and LR in non-DRX mode	1885

A.5.5.5.3.1	Test Purpose and Environment	1885

A.5.5.5.3.2	Test Requirements	1889

A.5.5.5.4	EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with CSI-RS-based BFD and LR in DRX mode	1890

A.5.5.5.4.1	Test Purpose and Environment	1890

A.5.5.5.4.2	Test Requirements	1894

A.5.5.5.5	EN-DC scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2 PSCell configured with SSB-based BFD and LR in non-DRX mode	1895

A.5.5.5.5.1	Test Purpose and Environment	1895

A.5.5.5.5.2	Test Requirements	1899

A.5.5.5.6	EN-DC Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in non-DRX mode	1900

A.5.5.5.6.1	Test Purpose and Environment	1900

A.5.5.5.6.2	Test Requirements	1904

A.5.5.5.7	EN-DC Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in DRX mode	1905

A.5.5.5.7.1	Test Purpose and Environment	1905

A.5.5.5.7.2	Test Requirements	1909

A.5.5.5.8	EN-DC TRP specific Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with CSI-RS-based BFD and LR in DRX mode	1910

A.5.5.5.8.1	Test Purpose and Environment	1910

A.5.5.5.8.2	Test Requirements	1915

A.5.5.5.9	Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with SSB-based BFD and LR in DRX mode for UE fulfilling relaxed measurement criterion	1915

A.5.5.5.9.1	Test Purpose and Environment	1915

A.5.5.5.9.2	Test Requirements	1919

A.5.5.6	Active BWP switch	1919

A.5.5.6.1	DCI-based and Timer-based Active BWP Switch	1919

A.5.5.6.1.1	E-UTRAN – NR PSCell FR2 DL active BWP switch with non-DRX in synchronous EN-DC	1919

A.5.5.6.1.1.1	Test Purpose and Environment	1919

A.5.5.6.1.1.2	Test Requirements	1923

A.5.5.6.1.2	E-UTRAN – NR PSCell FR2 with FR2 SCell DL active BWP switch in non-DRX in synchronous EN-DC	1923

A.5.5.6.2	RRC-based Active BWP Switch	1928

A.5.5.6.2.1	E-UTRAN – NR PSCell FR2 DL active BWP switch with non-DRX in synchronous EN-DC	1928

A.5.5.6.3 Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs	1932

A.5.5.6.3.1	E-UTRAN – NR PSCell FR2 and NR SCell FR2 DL active BWP switch on multiple CCs in synchronous EN-DC	1932

A.5.5.6.4	SCell dormancy switch	1936

A.5.5.6.4.1	E-UTRAN – NR FR2 PSCell SCell dormancy switch of single FR2 SCell inside active time	1936

A.5.5.6.4.1.1	Test Purpose and Environment	1936

A.5.5.6.4.1.2	Test Requirements	1940

A.5.5.6.4.2	E-UTRAN – NR FR1 PSCell SCell dormancy switch of two FR2 SCells outside active time	1940

A.5.5.6.4.2.1	Test Purpose and Environment	1940

A.5.5.6.4.2.2	Test Requirements	1947

A.5.5.6.5	Simultaneous RRC-based Active BWP Switch on multiple CCs	1947

A.5.5.6.5.1	E-UTRAN – NR PSCell FR2  and NR SCell FR2 DL active BWP switch on multiple CCs with non-DRX in synchronous EN-DC	1947

A.5.5.7	PSCell addition and release delay	1950

A.5.5.7.1	Addition and Release Delay of NR PSCell	1950

A.5.5.7.1.1	Test purpose and environment	1950

A.5.5.7.1.2	Test Requirements	1953

A.5.5.8	Active TCI state switch delay	1954

A.5.5.8.1	MAC-CE based active TCI state switch	1954

A.5.5.8.1.1	E-UTRAN – NR PSCell FR2 active TCI state switch for a known TCI state	1954

A.5.5.8.1.1.1	Test Purpose and Environment	1954

A.5.5.8.1.1.2	Test Requirements	1958

A.5.5.8.2	RRC based active TCI state switch	1958

A.5.5.8.2.1	E-UTRAN – NR PSCell FR2 active TCI state switch for a known TCI state	1958

A.5.5.8.2.1.1	Test Purpose and Environment	1958

A.5.5.8.2.1.2	Test Requirements	1962

A.5.5.9	Uplink spatial relation switch delay	1962

A.5.5.9.1	MAC-CE based uplink spatial relation switch	1962

A.5.5.9.1.1	E-UTRAN – NR PSCell FR2 uplink spatial relation switch for a known spatial relation	1962

A.5.5.9.1.1.1	Test Purpose and Environment	1962

A.5.5.9.1.1.2	Test Requirements	1965

A.5.5.9.2	RRC based spatial relation switch	1965

A.5.5.9.2.1	E-UTRAN – NR PSCell FR2 spatial relation switch associated with a known DL-RS	1965

A.5.5.9.2.1.1	Test Purpose and Environment	1965

A.5.5.9.2.1.2	Test Requirements	1968

A.5.5.10	UE specific CBW change	1968

A.5.5.10.1	UE specific CBW change on FR2 NR PSCell	1968

A.5.5.10.1.1	Test Purpose and Environment	1968

A.5.5.10.1.2	Test Requirements	1971

A.5.5.11	Unified TCI state switch delay	1972

A.5.5.11.1	MAC-CE based active joint TCI state switch	1972

A.5.5.11.1.1	E-UTRAN – NR PSCell FR2 active joint TCI state switch for a known TCI state	1972

A.5.5.11.1.1.1	Test Purpose and Environment	1972

A.5.5.11.1.1.2	Test parameters	1972

A.5.5.11.1.1.3	Test Requirements	1975

A.5.5.11.2	MAC-CE based active uplink TCI state switch	1975

A.5.5.11.2.1	E-UTRAN – NR PSCell FR2 active uplink TCI state switch for a known TCI state	1975

A.5.5.11.2.1.1	Test Purpose and Environment	1975

A.5.5.11.2.1.2	Test parameters	1976

A.5.5.11.2.1.3	Test Requirements	1978

A.5.5.11.3	MAC-CE based active downlink TCI state switch	1978

A.5.5.11.3.1	E-UTRAN – NR PSCell FR2 downlink TCI state switch to cell with additional PCI for a known TCI state	1978

A.5.5.11.3.1.1	Test Purpose and Environment	1978

A.5.5.11.3.1.2	Test Parameters	1979

A.5.5.11.3.1.3	Test Requirements	1983

A.5.5.12	PSCell activation and deactivation delay	1983

A.5.5.12.1	PSCell activation and deactivation delay	1983

A.5.5.12.1.1	Test purpose and environment	1983

A.5.5.12.1.2	Test Requirements	1986

A.5.5.13	Conditional PSCell addition and release delay	1987

A.5.5.13.1	Addition and Release Delay of NR PSCell	1987

A.5.5.13.1.1	Test purpose and environment	1987

A.5.5.13.1.2	Test Requirements	1990

A.5.5.13.2	E-UTRAN – NR FR2 interruptions during measurements on deactivated NR PSCell	1991

A.5.5.13.2.1	Test Purpose and Environment	1991

A.5.5.13.2.2	Test Requirements	1994

A.5.6	Measurement procedure	1994

A.5.6.1	Intra-frequency Measurements	1994

A.5.6.1.1	EN-DC event triggered reporting test without gap under non-DRX	1994

A.5.6.1.1.1	Test purpose and Environment	1994

A.5.6.1.1.2	Test Requirements	1998

A.5.6.1.2	EN-DC event triggered reporting test without gap under DRX	1998

A.5.6.1.2.1	Test purpose and Environment	1998

A.5.6.1.2.2	Test Requirements	2000

A.5.6.1.3	EN-DC event triggered reporting test with per-UE gaps under non-DRX	2001

A.5.6.1.3.1	Test purpose and Environment	2001

A.5.6.1.3.2	Test Requirements	2005

A.5.6.1.4	EN-DC event triggered reporting test with per-UE gaps under DRX	2005

A.5.6.1.4.1	Test purpose and Environment	2005

A.5.6.1.4.2	Test Requirements	2008

A.5.6.2	Inter-frequency Measurements	2009

A.5.6.2.1 	EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is not used	2009

A.5.6.2.1.1	Test Purpose and Environment	2009

A.5.6.2.1.2	Test Requirements	2012

A.5.6.2.2 	EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is used	2012

A.5.6.2.2.1	Test Purpose and Environment	2012

A.5.6.2.2.2	Test Requirements	2016

A.5.6.2.3 	EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is not used	2016

A.5.6.2.3.1	Test Purpose and Environment	2016

A.5.6.2.3.2	Test Requirements	2020

A.5.6.2.4	EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is used	2020

A.5.6.2.4.1	Test Purpose and Environment	2020

A.5.6.2.4.2	Test Requirements	2024

A.5.6.2.5	EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is not used	2024

A.5.6.2.5.1	Test Purpose and Environment	2024

A.5.6.2.5.2	Test Requirements	2029

A.5.6.2.6	EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is used	2029

A.5.6.2.6.1	Test Purpose and Environment	2029

A.5.6.2.6.2	Test Requirements	2033

A.5.6.2.7	EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is not used	2033

A.5.6.2.7.1	Test Purpose and Environment	2033

A.5.6.2.7.2	Test Requirements	2038

A.5.6.2.8	EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is used	2038

A.5.6.2.8.1	Test Purpose and Environment	2038

A.5.6.2.8.2	Test Requirements	2043

A.5.6.3	L1-RSRP measurement for beam reporting	2044

A.5.6.3.1	SSB based L1-RSRP measurement when DRX is not used	2044

A.5.6.3.1.1	Test Purpose and Environment	2044

A.5.6.3.1.2	Test parameters	2044

A.5.6.3.1.3	Test Requirements	2046

A.5.6.3.2	SSB based L1-RSRP measurement when DRX is used	2046

A.5.6.3.2.1	Test Purpose and Environment	2046

A.5.6.3.2.2	Test parameters	2047

A.5.6.3.2.3	Test Requirements	2049

A.5.6.3.3	CSI-RS based L1-RSRP measurement when DRX is not used	2049

A.5.6.3.3.1	Test Purpose and Environment	2049

A.5.6.3.3.2	Test parameters	2050

A.5.6.3.3.3	Test Requirements	2052

A.5.6.3.4	CSI-RS based L1-RSRP measurement when DRX is used	2052

A.5.6.3.4.1	Test Purpose and Environment	2052

A.5.6.3.4.2	Test parameters	2053

A.5.6.3.4.3	Test Requirements	2055

A.5.6.4	CLI measurements	2056

A.5.6.4.1	SRS-RSRP measurement with DRX	2056

A.5.6.4.1.1	Test Purpose and Environment	2056

A.5.6.4.1.2	Test Parameters	2056

A.5.6.4.1.3	Test Requirements	2058

A.5.6.4.2	CLI-RSSI measurement with DRX	2058

A.5.6.4.2.1	Test Purpose and Environment	2058

A.5.6.4.2.2	Test Parameters	2059

A.5.6.4.2.3	Test Requirements	2061

A.5.6.5	Measurements with autonomous gaps	2061

A.5.6.5.1 	EN-DC inter-frequency CGI identification of NR neighbor cell in FR2	2061

A.5.6.5.1.1	Test Purpose and Environment	2061

A.5.6.5.1.2	Test Requirements	2064

A.5.6.6	L1-SINR measurement for beam reporting	2065

A.5.6.6.2	L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is not used	2067

A.5.6.6.2.1	Test Purpose and Environment	2067

A.5.6.6.2.2	Test parameters	2068

A.5.6.6.2.3	Test Requirements	2071

A.5.6.6.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is not used	2071

A.5.6.6.3.1	Test Purpose and Environment	2071

A.5.6.6.3.2	Test parameters	2072

A.5.6.6.3.3	Test Requirements	2074

A.5.6.7	CSI-RS based Intra-frequency Measurements	2074

A.5.6.7.1	EN-DC event triggered reporting test without gap under non-DRX	2074

A.5.6.7.1.1	Test purpose and Environment	2074

A.5.6.7.1.2	Test Requirements	2077

A.5.6.8	CSI-RS based Inter-frequency Measurements	2078

A.5.6.8.1	EN-DC event triggered reporting tests for NR FR2 cell when DRX is used	2078

A.5.6.8.1.1	Test Purpose and Environment	2078

A.5.6.8.1.2	Test Requirements	2082

A.5.7	Measurement Performance requirements	2082

A.5.7.1	SS-RSRP	2082

A.5.7.1.1	EN-DC intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	2082

A.5.7.1.1.1	Test Purpose and Environment	2082

A.5.7.1.1.2	Test parameters	2083

A.5.7.1.1.3	Test Requirements	2085

A.5.7.1.2	EN-DC inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	2086

A.5.7.1.2.1	Test Purpose and Environment	2086

A.5.7.1.2.2	Test parameters	2086

A.5.7.1.2.3	Test Requirements	2090

A.5.7.1.3	EN-DC inter-frequency measurement accuracy with FR1 serving cell and FR2 target cell	2091

A.5.7.1.3.1	Test Purpose and Environment	2091

A.5.7.1.3.2	Test parameters	2091

A.5.7.1.3.3	Test Requirements	2094

A.5.7.2	SS-RSRQ	2095

A.5.7.2.1	EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	2095

A.5.7.2.1.1	Test Purpose and Environment	2095

A.5.7.2.1.2	Test Parameters	2095

A.5.7.2.1.3	Test Requirements	2098

A.5.7.2.2	EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	2098

A.5.7.2.2.1	Test Purpose and Environment	2098

A.5.7.2.2.2	Test Parameters	2098

A.5.7.2.2.3	Test Requirements	2100

A.5.7.3	SS-SINR	2101

A.5.7.3.1	EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	2101

A.5.7.3.1.1	Test Purpose and Environment	2101

A.5.7.3.1.2	Test Parameters	2101

A.5.7.3.1.3	Test Requirements	2104

A.5.7.3.2	EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	2104

A.5.7.3.2.1	Test Purpose and Environment	2104

A.5.7.3.2.2	Test Parameters	2104

A.5.7.3.2.3	Test Requirements	2106

A.5.7.4	L1-RSRP measurement for beam reporting	2106

A.5.7.4.1	SSB based L1-RSRP measurement	2106

A.5.7.4.1.1	Test Purpose and Environment	2106

A.5.7.4.1.2	Test parameters	2107

A.5.7.4.1.3	Test Requirements	2109

A.5.7.4.2	CSI-RS based L1-RSRP measurement on resource set with repetition off	2110

A.5.7.4.2.1	Test Purpose and Environment	2110

A.5.7.4.2.2	Test parameters	2110

A.5.7.4.2.3	Test Requirements	2112

A.5.7.5	CLI measurements	2113

A.5.7.5.1	EN-DC SRS-RSRP measurement accuracy with FR2 serving cell	2113

A.5.7.5.1.1	Test Purpose and Environment	2113

A.5.7.5.1.2	Test parameters	2113

A.5.7.5.1.3	Test Requirements	2116

A.5.7.5.2	EN-DC CLI-RSSI measurement accuracy with FR2 serving cell	2117

A.5.7.5.2.1	Test Purpose and Environment	2117

A.5.7.5.2.2	Test parameters	2117

A.5.7.5.2.3	Test Requirements	2119

A.5.7.6	L1-SINR measurement for beam reporting	2120

A.5.7.6.2	L1-SINR measurement with SSB based CMR and dedicated IMR	2123

A.5.7.6.2.1	Test Purpose and Environment	2123

A.5.7.6.2.2	Test parameters	2123

A.5.7.6.2.3	Test Requirements	2125

A.5.7.6.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR	2126

A.5.7.6.3.1	Test Purpose and Environment	2126

A.5.7.6.3.2	Test parameters	2126

A.5.7.6.3.3	Test Requirements	2128

A.5.7.7	CSI-RSRP	2129

A.5.7.7.1	EN-DC intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	2129

A.5.7.7.1.1	Test Purpose and Environment	2129

A.5.7.7.1.2	Test parameters	2129

A.5.7.7.1.3	Test Requirements	2133

A.5.7.7.2	EN-DC inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	2134

A.5.7.7.2.1	Test Purpose and Environment	2134

A.5.7.7.2.2	Test parameters	2134

A.5.7.7.2.3	Test Requirements	2138

A.5.7.8	CSI-RSRQ	2139

A.5.7.8.1	EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell	2139

A.5.7.8.1.1	Test Purpose and Environment	2139

A.5.7.8.1.2	Test Parameters	2139

A.5.7.8.1.3	Test Requirements	2141

A.5.7.8.2	EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	2141

A.5.7.8.2.1	Test Purpose and Environment	2141

A.5.7.8.2.2	Test Parameters	2141

A.5.7.8.2.3	Test Requirements	2143

A.5.7.9	CSI-SINR	2143

A.5.7.9.1	EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	2143

A.5.7.9.1.1	Test Purpose and Environment	2143

A.5.7.9.1.2	Test Parameters	2144

A.5.7.9.1.3	Test Requirements	2146

A.5.7.9.2	EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	2146

A.5.7.9.2.1	Test Purpose and Environment	2146

A.5.7.9.2.2	Test Parameters	2147

A.5.7.9.2.3	Test Requirements	2149

A.5.8	Void	2149

A.6	NR standalone tests with all NR cells in FR1	2151

A.6.1	SA: RRC\_IDLE state mobility	2151

A.6.1.1	Cell re-selection to NR	2151

A.6.1.1.1	Cell reselection to FR1 intra-frequency NR case	2151

A.6.1.1.1.1	Test Purpose and Environment	2151

A.6.1.1.1.2	Test Parameters	2151

A.6.1.1.1.3	Test Requirements	2155

A.6.1.1.2	Cell reselection to FR1 inter-frequency NR case	2155

A.6.1.1.2.1	Test Purpose and Environment	2155

A.6.1.1.2.2	Test Parameters	2155

A.6.1.1.2.3	Test Requirements	2159

A.6.1.1.3	Cell reselection to FR1 intra-frequency NR case for UE fulfilling low mobility relaxed measurement criterion	2159

A.6.1.1.3.1	Test Purpose and Environment	2159

A.6.1.1.3.2	Test Parameters	2159

A.6.1.1.3.3	Test Requirements	2164

A.6.1.1.4	Cell reselection to FR1 intra-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion	2164

A.6.1.1.4.1	Test Purpose and Environment	2164

A.6.1.1.4.2	Test Parameters	2164

A.6.1.1.4.3	Test Requirements	2167

A.6.1.1.5	Cell reselection to FR1 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion	2167

A.6.1.1.5.1	Test Purpose and Environment	2167

A.6.1.1.5.2	Test Parameters	2167

A.6.1.1.5.3	Test Requirements	2172

A.6.1.1.6	Cell reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion	2173

A.6.1.1.6.1	Test Purpose and Environment	2173

A.6.1.1.6.2	Test Parameters	2173

A.6.1.1.6.3	Test Requirements	2177

A.6.1.1.7	Cell reselection to FR1 intra-frequency NR case for UE configured with *highSpeedMeasFlag-r16* 2178

A.6.1.1.7.1	Test Purpose and Environment	2178

A.6.1.1.7.2	Test Parameters	2178

A.6.1.1.7.3	Test Requirements	2181

A.6.1.1.8	Cell reselection to FR1 inter-frequency NR case for UE configured with *highSpeedMeasInterFreq-r17* 2181

A.6.1.1.8.1	Test Purpose and Environment	2181

A.6.1.1.8.2	Test Parameters	2181

A.6.1.1.8.3	Test Requirements	2185

A.6.1.2	Inter-RAT E-UTRAN cell re-selection	2185

A.6.1.2.1	Cell reselection to higher priority E-UTRAN	2185

A.6.1.2.1.1	Test Purpose and Environment	2185

A.6.1.2.1.2	Test Parameters	2185

A.6.1.2.1.3	Test Requirements	2188

A.6.1.2.2	Cell reselection to lower priority E-UTRAN	2189

A.6.1.2.2.1	Test Purpose and Environment	2189

A.6.1.2.2.2	Test Parameters	2189

A.6.1.2.2.3	Test Requirements	2192

A.6.1.2.3	Cell reselection to lower priority E-UTRAN for UE fulfilling low mobility relaxed measurement criterion	2193

A.6.1.2.3.1	Test Purpose and Environment	2193

A.6.1.2.3.2	Test Parameters	2193

A.6.1.2.3.3	Test Requirements	2196

A.6.1.2.4	Cell reselection to lower priority E-UTRAN for UE fulfilling not-at-cell edge relaxed measurement criterion	2197

A.6.1.2.4.1	Test Purpose and Environment	2197

A.6.1.2.4.2	Test Parameters	2197

A.6.1.2.4.3	Test Requirements	2200

A.6.1.2.5	Cell reselection to lower priority E-UTRAN cell for UE configured with highSpeedMeasFlag-r16	2201

A.6.1.2.5.1	Test Purpose and Environment	2201

A.6.1.2.5.2	Test Parameters	2201

A.6.1.2.5.3	Test Requirements	2205

A.6.1.1.7	Void	2206

A.6.2	SA: RRC\_INACTIVE state mobility	2206

A.6.2.1	Configured Grant based Small Data Transmissions (CG-SDT)	2206

A.6.2.1.1	Test purpose and Environment	2206

A.6.2.1.2	Test Parameters	2208

A.6.2.1.3	Test requirements	2210

A.6.3	RRC\_CONNECTED state mobility	2210

A.6.3.1	Handover	2210

A.6.3.1.1	Intra-frequency handover from FR1 to FR1; known target cell	2210

A.6.3.1.1.1	Test Purpose and Environment	2210

A.6.3.1.1.2	Test Parameters	2210

A.6.3.1.1.3 Test Requirements	2214

A.6.3.1.2	Intra-frequency handover from FR1 to FR1; unknown target cell	2214

A.6.3.1.2.1	Test Purpose and Environment	2214

A.6.3.1.2.2	Test Parameters	2214

A.6.3.1.2.3	Test Requirements	2218

A.6.3.1.3	Inter-frequency handover from FR1 to FR1; unknown target cell	2218

A.6.3.1.3.1	Test Purpose and Environment	2218

A.6.3.1.3.2	Test Parameters	2218

A.6.3.1.3.3	Test Requirements	2222

A.6.3.1.4	SA NR - E-UTRAN handover	2222

A.6.3.1.4.1	Test Purpose and Environment	2222

A.6.3.1.4.2	Test Requirements	2228

A.6.3.1.5	SA NR - E-UTRAN handover with unknown target cell	2228

A.6.3.1.5.1	Test Purpose and Environment	2228

A.6.3.1.5.2	Test Requirements	2234

A.6.3.1.6	 SA NR - UTRAN FDD handover	2234

A.6.3.1.6.1	Test Purpose and Environment	2234

A.6.3.1.6.2	Test Requirements	2238

A.6.3.1.7	Intra-frequency synchronous DAPS handover in FR1	2238

A.6.3.1.7.1	Test Purpose and Environment	2238

A.6.3.1.7.2	Test Parameters	2238

A.6.3.1.7.3	Test Requirements	2242

A.6.3.1.8	Intra-frequency asynchronous DAPS handover in FR1	2243

A.6.3.1.8.1	Test Purpose and Environment	2243

A.6.3.1.8.2	Test Parameters	2243

A.6.3.1.8.3	Test Requirements	2247

A.6.3.1.9	Intra-band inter-frequency synchronous DAPS handover test in SA for FR1	2248

A.6.3.1.9.1	Test Purpose and Environment	2248

A.6.3.1.9.2	Test Parameters	2248

A.6.3.1.9.3	Test Requirements	2252

A.6.3.1.10	Intra-band inter-frequency asynchronous DAPS handover test in SA for FR1	2252

A.6.3.1.10.1	Test Purpose and Environment	2252

A.6.3.1.10.2	Test Parameters	2252

A.6.3.1.10.3	Test Requirements	2255

A.6.3.1.11	Inter-band inter-frequency synchronous DAPS handover from FR1 to FR1	2255

A.6.3.1.11.1	Test Purpose and Environment	2255

A.6.3.1.11.2	Test Parameters	2255

A.6.3.1.11.3 Test Requirements	2262

A.6.3.1.12	Inter-band inter-frequency asynchronous DAPS handover from FR1 to FR1	2262

A.6.3.1.12.1	Test Purpose and Environment	2262

A.6.3.1.12.2	Test Parameters	2262

A.6.3.1.12.3 Test Requirements	2270

A.6.3.1.13	SA NR - E-UTRAN with NR PSCell addition in FR1	2270

A.6.3.1.13.1	Test Purpose and Environment	2270

A.6.3.1.13.2	Test Requirements	2279

A.6.3.1.14	SA NR - E-UTRAN handover with NR FR1 PScell addition	2279

A.6.3.1.14.1	Test Purpose and Environment	2279

A.6.3.1.14.2	Test Requirements	2288

A.6.3.2	RRC Connection Mobility Control	2289

A.6.3.2.1	SA: RRC Re-establishment	2289

A.6.3.2.1.1	Intra-frequency RRC Re-establishment in FR1	2289

A.6.3.2.1.2	Inter-frequency RRC Re-establishment in FR1	2293

A.6.3.2.1.3	Intra-frequency RRC Re-establishment in FR1 without serving cell timing	2297

A.6.3.2.2	Random Access	2300

A.6.3.2.2.1	4-step RA type contention based random access test in FR1 for NR standalone	2300

A.6.3.2.2.2	4-step RA type non-contention based random access test in FR1 for NR standalone	2304

A.6.3.2.2.3	2-step RA type contention based random access test in FR1 for NR standalone	2309

A.6.3.2.2.4	2-step RA type non-contention based test in FR1 for NR standalone	2314

A.6.3.2.3	SA: RRC Connection Release with Redirection	2318

A.6.3.2.3.1	Redirection from NR in FR1 to NR in FR1	2318

A.6.3.2.3.2	Redirection from NR in FR1 to E-UTRAN	2322

A.6.3.3 Conditional handover	2329

A.6.3.3.1	Intra-frequency conditional handover from FR1 to FR1	2329

A.6.3.3.1.1	Test Purpose and Environment	2329

A.6.3.3.1.2	Test Parameters	2329

A.6.3.3.1.3 Test Requirements	2333

A.6.3.3.2	Inter-frequency conditional handover from FR1 to FR1	2333

A.6.3.3.2.1	Test Purpose and Environment	2333

A.6.3.3.2.2	Test Parameters	2333

A.6.3.3.2.3 Test Requirements	2337

A.6.4	Timing	2337

A.6.4.1	UE transmit timing	2337

A.6.4.1.1	NR UE Transmit Timing Test for FR1	2337

A.6.4.1.1.1	Test Purpose and environment	2337

A.6.4.1.1.2	Test requirements	2341

A.6.4.2	UE timer accuracy	2341

A.6.4.3	Timing advance	2341

A.6.4.3.1	SA FR1 timing advance adjustment accuracy	2341

A.6.4.3.1.1	Test Purpose and Environment	2341

A.6.4.3.1.2	Test Parameters	2341

A.6.4.3.1.3	Test Requirements	2345

A.6.5	Signalling characteristics	2345

A.6.5.1	Radio link Monitoring	2345

A.6.5.1.1	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode	2346

A.6.5.1.1.1	Test Purpose and Environment	2346

A.6.5.1.1.2	Test Requirements	2351

A.6.5.1.2	Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode	2351

A.6.5.1.2.1	Test Purpose and Environment	2351

A.6.5.1.2.2	Test Requirements	2357

A.6.5.1.3	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode	2357

A.6.5.1.3.1	Test Purpose and Environment	2357

A.6.5.1.3.2	Test Requirements	2363

A.6.5.1.4	Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode	2363

A.6.5.1.4.1	Test Purpose and Environment	2363

A.6.5.1.4.2	Test Requirements	2369

A.6.5.1.5	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode	2369

A.6.5.1.5.1	Test Purpose and Environment	2369

A.6.5.1.5.2	Test Requirements	2375

A.6.5.1.6	Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode	2375

A.6.5.1.6.1	Test Purpose and Environment	2375

A.6.5.1.6.2	Test Requirements	2380

A.6.5.1.7	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode	2380

A.6.5.1.7.1	Test Purpose and Environment	2380

A.6.5.1.7.2	Test Requirements	2384

A.6.5.1.8	Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode	2384

A.6.5.1.8.1	Test Purpose and Environment	2384

A.6.5.1.8.2	Test Requirements	2390

A.6.5.1.9	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM for UE fulfilling relaxed measurement criterion	2390

A.6.5.1.9.1	Test Purpose and Environment	2390

A.6.5.1.9.2	Test Requirements	2396

A.6.5.2	Interruption	2396

A.6.5.2.1	Interruptions during measurements on deactivated NR SCC in FR1	2396

A.6.5.2.1.2	Test Requirements	2400

A.6.5.2.2	SA interruptions at NR SRS carrier based switching	2401

A.6.5.2.2.1	Test Purpose and Environment	2401

A.6.5.2.2.2	Test Parameters	2401

A.6.5.2.2.3	Test Requirements	2403

A.6.5.2.3	SA interruptions at NR SRS antenna port switching with 1 SRS symbol in a slot in NR-CA	2404

A.6.5.2.3.1	Test Purpose and Environment	2404

A.6.5.2.3.2	Test Parameters	2404

A.6.5.2.3.3	Test Requirements	2406

A.6.5.2.4	SA interruptions at NR SRS antenna port switching	2407

A.6.5.2.4.1	Test Purpose and Environment	2407

A.6.5.2.4.2	Test Parameters	2407

A.6.5.2.4.3	Test Requirements	2409

A.6.5.3	SCell Activation and Deactivation Delay	2410

A.6.5.3.1	SCell Activation and deactivation of known SCell in FR1 in non-DRX for 160ms SCell measurement cycle	2410

A.6.5.3.1.1	Test Purpose and Environment	2410

A.6.5.3.1.2	Test Requirements	2415

A.6.5.3.2	SCell Activation and deactivation of known SCell in FR1 in non-DRX for 640 ms SCell measurement cycle	2416

A.6.5.3.2.1	Test Purpose and Environment	2416

A.6.5.3.2.2	Test Requirements	2416

A.6.5.3.3	SCell Activation and deactivation of unknown SCell in FR1 in non-DRX	2416

A.6.5.3.3.1	Test Purpose and Environment	2416

A.6.5.3.3.2	Test Requirements	2417

A.6.5.3.4	Direct SCell activation at SCell addition of known SCell in FR1	2417

A.6.5.3.4.1	Test Purpose and Environment	2417

A.6.5.3.4.2	Test Requirements	2424

A.6.5.3.5	Direct SCell activation at handover with known SCell in FR1	2424

A.6.5.3.5.1	Test Purpose and Environment	2424

A.6.5.3.5.2	Test Requirements	2429

A.6.5.3.6	PUCCH SCell Activation and deactivation of known SCell in FR1	2429

A.6.5.3.6.1	Test Purpose and Environment	2429

A.6.5.3.6.2	Test Requirements	2433

A.6.5.3.7	SCell Activation and deactivation of unknown SCell in FR1 in non-DRX	2434

A.6.5.3.7.1	Test Purpose and Environment	2434

A.6.5.3.7.2	Test Requirements	2438

A.6.5.3.8	SCell Activation and Deactivation of one FR1 known PUCCH SCell and one FR1 unknown SCell with single activation/deactivation command	2439

A.6.5.3.8.1	Test Purpose and Environment	2439

A.6.5.3.8.2	Test Requirements	2443

A.6.5.3.9	SCell Activation and deactivation of unknown PUCCH SCell and unknown DL SCell in FR1 in non-DRX	2444

A.6.5.3.9.1	Test Purpose and Environment	2444

A.6.5.3.9.2	Test Requirements	2448

A.6.5.3.10	Fast SCell Activation of known SCell in FR1 in non-DRX for 160ms SCell measurement cycle	2449

A.6.5.3.10.1	Test Purpose and Environment	2449

A.6.5.3.10.2	Test Requirements	2452

A.6.5.3.11	SCell Activation of known SCell in FR1 in non-DRX for 640 ms SCell measurement cycle	2452

A.6.5.3.11.1	Test Purpose and Environment	2452

A.6.5.3.11.2	Test Requirements	2453

A.6.5.4	UE UL carrier RRC reconfiguration Delay	2453

A.6.5.4.1	UE UL carrier RRC reconfiguration Delay	2453

A.6.5.4.1.1	Test Purpose and Environment	2453

A.6.5.4.1.2	Test Requirements	2462

A.6.5.4.2	Void	2463

A.6.5.5	Beam Failure Detection and Link recovery procedures	2463

A.6.5.5.1	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode	2463

A.6.5.5.1.1	Test Purpose and Environment	2463

A.6.5.5.2	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode	2469

A.6.5.5.2.1	Test Purpose and Environment	2469

A.6.5.5.2.2	Test Requirements	2475

A.6.5.5.3	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode	2476

A.6.5.5.3.1	Test Purpose and Environment	2476

A.6.5.5.3.2	Test Requirements	2481

A.6.5.5.4	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode	2482

A.6.5.5.4.1	Test Purpose and Environment	2482

A.6.5.5.4.2	Test Requirements	2487

A.6.5.5.5	Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in non-DRX mode	2488

A.6.5.5.5.1	Test Purpose and Environment	2488

A.6.5.5.5.2	Test Requirements	2492

A.6.5.5.6	Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in DRX mode	2492

A.6.5.5.6.1	Test Purpose and Environment	2492

A.6.5.5.6.2	Test Requirements	2497

A.6.5.5.7	TRP Specific Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode	2497

A.6.5.5.7.1	Test Purpose and Environment	2497

A.6.5.5.7.2	Test Requirements	2503

A.6.5.6	Active BWP switch	2504

A.6.5.6.1	DCI-based and Timer-based Active BWP Switch	2504

A.6.5.6.1.1	NR FR1- NR FR1 DL active BWP switch of SCell with non-DRX in SA	2504

A.6.5.6.1.2	NR FR1 DL active BWP switch with non-DRX in SA	2510

A.6.5.6.2	RRC-based Active BWP Switch	2515

A.6.5.6.2.1	NR FR1 DL active BWP switch of Cell with non-DRX in SA	2515

A.6.5.6.3 Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs	2519

A.6.5.6.3.1	NR FR1- NR FR1 DL active BWP switch on multiple CCs with non-DRX in SA	2519

A.6.5.6.4	SCell dormancy switch	2526

A.6.5.6.4.1	NR FR1 PCell SCell dormancy switch of single FR1 SCell outside active time	2526

A.6.5.6.4.1.1	Test Purpose and Environment	2526

A.6.5.6.4.1.2	Test Requirements	2532

A.6.5.6.4.2	NR FR1 PCell SCell dormancy switch of two FR1 SCells inside active time	2532

A.6.5.6.4.2.1	 Test Purpose and Environment	2532

A.6.5.6.4.2.2	Test Requirements	2539

A.6.5.6.5	Simultaneous RRC-based Active BWP Switch on multiple CCs	2539

A.6.5.6.5.1	NR FR1- NR FR1 DL active BWP switch on multiple CCs with non-DRX in SA	2539

A.6.5.7	DL interruptions at switching between two uplink carriers	2544

A.6.5.7.1	DL interruptions at switching between two uplink carriers in FDD-TDD CA	2544

A.6.5.7.1.1	Test Purpose and Environment	2544

A.6.5.7.1.2	Test Requirements	2548

A.6.5.7.2	DL interruptions at switching between two uplink carriers in TDD-TDD CA	2548

A.6.5.7.2.1	Test Purpose and Environment	2548

A.6.5.7.2.2	Test Requirements	2552

A.6.5.7A	DL interruptions at switching between two uplink carriers with two transmit antenna connectors	2552

A.6.5.7A.1	DL interruptions at switching between two uplink carriers in FDD-TDD CA	2552

A.6.5.7A.1.1	Test Purpose and Environment	2552

A.6.5.7A.1.2	Test Requirements	2556

A.6.5.7A.2	DL interruptions at switching between two uplink carriers in TDD-TDD CA	2556

A.6.5.7A.2.1	Test Purpose and Environment	2556

A.6.5.7A.2.2	Test Requirements	2560

A.6.5.7B	DL interruptions at switching between one uplink band with one transmit antenna connector and one uplink band with two transmit antenna connectors	2560

A.6.5.7B.1	DL interruptions at switching between two uplink bands in FDD-TDD CA	2560

A.6.5.7B.1.1	Test Purpose and Environment	2560

A.6.5.7B.1.2	Test Requirements	2564

A.6.5.7B.2	DL interruptions at switching between two uplink bands in TDD-TDD CA	2564

A.6.5.7B.2.1	Test Purpose and Environment	2564

A.6.5.7B.2.2	Test Requirements	2568

A.6.5.7C	DL interruptions at switching between two uplink bands with two transmit antenna connectors	2568

A.6.5.7C.1	DL interruptions at switching between two uplink bands with two transmit antenna connectors in FDD-TDD CA	2568

A.6.5.7C.1.1	Test Purpose and Environment	2568

A.6.5.7C.1.2	Test Requirements	2572

A.6.5.7C.2	DL interruptions at switching between two uplink bands with two transmit antenna connectors in TDD-TDD CA	2573

A.6.5.7C.2.1	Test Purpose and Environment	2573

A.6.5.7C.2.2	Test Requirements	2577

A.6.5.8	UE specific CBW change	2578

A.6.5.8.1	UE specific CBW change on PCell in FR1 in non-DRX	2578

A.6.5.8.1.1	Test Purpose and Environment	2578

A.6.5.8.1.2	Test Requirements	2582

A.6.5.9	Pathloss reference signal switching delay	2582

A.6.5.9.1	MAC-CE based pathloss reference signal switch delay	2582

A.6.5.9.1.1	Test Purpose and Environment	2582

A.6.5.9.1.2	Test Requirements	2585

A.6.6	Measurement procedure	2586

A.6.6.1	Intra-frequency Measurements	2586

A.6.6.1.1	SA event triggered reporting tests without gap under non-DRX	2586

A.6.6.1.1.1	Test purpose and Environment	2586

A.6.6.1.1.2	Test parameters	2586

A.6.6.1.1.3	Test Requirements	2590

A.6.6.1.2	SA event triggered reporting tests without gap under DRX	2590

A.6.6.1.2.1	Test purpose and Environment	2590

A.6.6.1.2.2	Test parameters	2590

A.6.6.1.2.3	Test Requirements	2594

A.6.6.1.3	SA event triggered reporting tests with per-UE gaps under non-DRX	2594

A.6.6.1.3.1	Test purpose and Environment	2594

A.6.6.1.3.2	Test parameters	2594

A.6.6.1.3.3	Test Requirements	2598

A.6.6.1.4	SA event triggered reporting tests with per-UE gaps under DRX	2598

A.6.6.1.4.1	Test purpose and Environment	2598

A.6.6.1.4.2	Test parameters	2598

A.6.6.1.4.3	Test Requirements	2602

A.6.6.1.5	SA event triggered reporting tests without gap under non-DRX with SSB index reading	2602

A.6.6.1.5.1	Test purpose and Environment	2602

A.6.6.1.5.2	Test parameters	2602

A.6.6.1.5.3	Test Requirements	2604

A.6.6.1.6	SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading	2605

A.6.6.1.6.1	Test purpose and Environment	2605

A.6.6.1.6.2	Test parameters	2605

A.6.6.1.6.3	Test Requirements	2606

A.6.6.1.7	SA event triggered reporting tests under DRX for UE configured with highSpeedMeasFlag-r16	2607

A.6.6.1.7.1	Test purpose and Environment	2607

A.6.6.1.7.2	Test parameters	2607

A.6.6.1.7.3	Test Requirements	2611

A.6.6.1.8	SA event triggered reporting tests without gap under DRX for UE configured with highSpeedMeasCA-Scell-r17	2611

A.6.6.1.8.1	Test purpose and Environment	2611

A.6.6.1.8.2	Test parameters	2611

A.6.6.1.8.3	Test Requirements	2616

A.6.6.2	Inter-frequency Measurements	2616

A.6.6.2.1	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used	2616

A.6.6.2.1.1	Test Purpose and Environment	2616

A.6.6.2.1.2	Test Requirements	2620

A.6.6.2.2	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used	2620

A.6.6.2.2.1	Test Purpose and Environment	2620

A.6.6.2.2.2	Test Requirements	2624

A.6.6.2.3	Void	2625

A.6.6.2.4	Void	2625

A.6.6.2.5	SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used	2625

A.6.6.2.5.1	Test Purpose and Environment	2625

A.6.6.2.5.2	Test Requirements	2629

A.6.6.2.6	SA event triggered reporting tests for FR1 with SSB time index detection when DRX is used	2629

A.6.6.2.6.1	Test Purpose and Environment	2629

A.6.6.2.6.2	Test Requirements	2633

A.6.6.2.7	Void	2633

A.6.6.2.8	Void	2633

A.6.6.2.9	SA event triggered reporting tests with additional mandatory gap pattern	2633

A.6.6.2.9.1	Test Purpose and Environment	2633

A.6.6.2.9.2	Test Requirements	2637

A.6.6.2.10	SA event triggered reporting tests for FR1 when DRX is used	2637

A.6.6.2.10.1	Test Purpose and Environment	2637

A.6.6.2.10.2	Test Requirements	2641

A.6.6.2.12	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used for UE configured with highSpeedMeasInterFreq-r17	2645

A.6.6.2.12.1	Test Purpose and Environment	2645

A.6.6.2.12.2	Test Requirements	2649

A.6.6.3	Inter-RAT Measurements	2649

A.6.6.3.1	SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1	2649

A.6.6.3.1.1	Test Purpose and Environment	2649

A.6.6.3.1.2	Test Requirements	2655

A.6.6.3.2	SA NR - E-UTRAN event-triggered reporting in DRX in FR1	2655

A.6.6.3.2.1	Test Purpose and Environment	2655

A.6.6.3.2.2	Test Requirements	2662

A.6.6.3.3	SA NR - E-UTRAN event-triggered reporting in DRX in FR1 for UE configured with highSpeedMeasFlag-r16	2662

A.6.6.3.3.1	Test Purpose and Environment	2662

A.6.6.3.3.2	Test Requirements	2669

A.6.6.4	L1-RSRP measurement for beam reporting	2669

A.6.6.4.1	SSB based L1-RSRP measurement when DRX is not used	2669

A.6.6.4.1.1	Test Purpose and Environment	2669

A.6.6.4.1.2	Test parameters	2669

A.6.6.4.1.3	Test Requirements	2672

A.6.6.4.2	SSB based L1-RSRP measurement when DRX is used	2672

A.6.6.4.2.1	Test Purpose and Environment	2672

A.6.6.4.2.2	Test parameters	2673

A.6.6.4.2.3	Test Requirements	2676

A.6.6.4.3	CSI-RS based L1-RSRP measurement when DRX is not used	2676

A.6.6.4.3.1	Test Purpose and Environment	2676

A.6.6.4.3.2	Test parameters	2677

A.6.6.4.3.3	Test Requirements	2680

A.6.6.4.4	CSI-RS based L1-RSRP measurement when DRX is used	2680

A.6.6.4.4.1	Test Purpose and Environment	2680

A.6.6.4.4.2	Test parameters	2681

A.6.6.4.4.3	Test Requirements	2684

A.6.6.4.5	SSB based L1-RSRP measurement when DRX is used for UE configured with *highSpeedMeasFlag-r16* 2684

A.6.6.4.5.1	Test Purpose and Environment	2684

A.6.6.4.5.2	Test parameters	2685

A.6.6.4.5.3	Test Requirements	2688

A.6.6.4.6	Inter-cell SSB based L1-RSRP measurements on FR1 PCell when DRX is used	2688

A.6.6.4.6.1	Test Purpose and Environment	2688

A.6.6.4.6.2	Test parameters	2689

A.6.6.4.6.3	Test Requirements	2692

A.6.6.5	Inter-RAT UTRAN FDD measurements	2693

A.6.6.5.1	SA NR - UTRAN FDD event-triggered reporting in non-DRX in FR1	2693

A.6.6.5.1.1	Test Purpose and Environment	2693

A.6.6.5.1.2	Test Requirements	2696

A.6.6.6	CLI measurements	2696

A.6.6.6.1	SRS-RSRP measurement with DRX	2696

A.6.6.6.1.1	Test Purpose and Environment	2696

A.6.6.6.1.2	Test Parameters	2697

A.6.6.6.1.3	Test Requirements	2700

A.6.6.6.2	CLI-RSSI measurement with DRX	2700

A.6.6.6.2.1	Test Purpose and Environment	2700

A.6.6.6.2.2	Test Parameters	2701

A.6.6.6.2.3	Test Requirements	2703

A.6.6.7	NR measurements with autonomous gaps	2703

A.6.6.7.1	SA intra-frequency CGI identification of NR neighbor cell in FR1	2703

A.6.6.7.1.1	Test Purpose and Environment	2703

A.6.6.7.1.2	Test Parameters	2703

A.6.6.7.1.3	Test Requirements	2707

A.6.6.7.2	Identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR SA	2707

A.6.6.7.2.1	Test Purpose and Environment	2707

A.6.6.7.2.2	Test Requirements	2710

A.6.6.8	L1-SINR measurement for beam reporting	2711

A.6.6.8.2	L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is not used	2713

A.6.6.8.2.1	Test Purpose and Environment	2713

A.6.6.8.2.2	Test parameters	2714

A.6.6.8.2.3	Test Requirements	2718

A.6.6.8.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is not used	2718

A.6.6.8.3.1	Test Purpose and Environment	2718

A.6.6.8.3.2	Test parameters	2719

A.6.6.8.3.3	Test Requirements	2721

A.6.6.9	Idle Mode CA/DC Measurements	2721

A.6.6.9.1	SA Idle mode CA/DC measurement for FR1	2721

A.6.6.9.1.1	Test Purpose and Environment	2721

A.6.6.9.1.2	Test Requirements	2728

A.6.6.10	CSI-RS based intra-frequency Measurements	2728

A.6.6.10.1	SA event triggered reporting tests without gap under non-DRX	2728

A.6.6.10.1.1	Test purpose and Environment	2728

A.6.6.10.1.2	Test Requirements	2732

A.6.6.11	CSI-RS based inter-frequency Measurements	2732

A.6.6.11.1	 SA event triggered reporting tests with gap under DRX	2732

A.6.6.11.1.1	Test Purpose and Environment	2732

A.6.6.11.1.2	Test Requirements	2736

A.6.6.12	RSTD measurements	2736

A.6.6.12.1	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA	2736

A.6.6.12.1.1	Test Purpose and Environment	2736

A.6.6.12.1.2	Test Requirements	2743

A.6.6.12.2	NR RSTD measurement reporting delay test case for dual positioning frequency layers in FR1 SA	2744

A.6.6.12.2.1	Test Purpose and Environment	2744

A.6.6.12.2.2	Test Requirements	2750

A.6.6.12.3	NR RSTD measurement reporting delay test case for single positioning frequency layer with reduced number of samples in FR1 SA	2750

A.6.6.12.3.1	Test Purpose and Environment	2750

A.6.6.12.3.2	Test Requirements	2756

A.6.6.12.4	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA without measurement gap	2757

A.6.6.12.4.1	Test Purpose and Environment	2757

A.6.6.12.4.2	Test Requirements	2760

A.6.6.12.5	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC\_CONNECTED state with Rx TEG	2761

A.6.6.12.5.1	Test Purpose and Environment	2761

A.6.6.12.5.2	Test Requirements	2765

A.6.6.13 PRS-RSRP measurements	2765

A.6.6.13.1	PRS-RSRP reporting delay test case for single positioning frequency layer	2765

A.6.6.13.1.1	Test purpose and Environment	2765

A.6.6.13.1.2	Test Requirements	2769

A.6.6.13.2	PRS-RSRP reporting delay test case for dual positioning frequency layer	2769

A.6.6.13.2.1	Test purpose and Environment	2769

A.6.6.13.2.2	Test Requirements	2773

A.6.6.13.3	PRS-RSRP reporting delay test case for reduced number of samples	2773

A.6.6.13.3.1	Test purpose and Environment	2773

A.6.6.13.3.2	Test Requirements	2776

A.6.6.13.4	PRS-RSRP reporting delay test case for single positioning frequency layer outside MG	2776

A.6.6.13.4.1	Test purpose and Environment	2776

A.6.6.14	UE Rx-Tx time difference measurements	2781

A.6.6.14.1	UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA	2781

A.6.6.14.1.1	Test purpose and environment	2781

A.6.6.14.1.2	Test requirements	2785

A.6.6.14.2	UE Rx-Tx time difference measurement for dual positioning frequency layers in FR1 SA	2785

A.6.6.14.2.1	Test purpose and environment	2785

A.6.6.14.2.2	Test requirements	2790

A.6.6.14.3	UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA with reduced sample number	2790

A.6.6.14.3.1	Test purpose and environment	2790

A.6.6.14.3.2	Test requirements	2793

A.6.6.14.4	UE Rx-Tx time difference measurement without gaps in FR1 SA	2794

A.6.6.14.4.1	Test purpose and environment	2794

A.6.6.14.4.2	Test requirements	2796

A.6.6.14.5	UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA with multiple RxTx TEGs	2797

A.6.6.14.4.1	Test purpose and environment	2797

A.6.6.14.4.2	Test requirements	2801

A.6.6.15	Idle Mode measurements of inter-RAT DC candidate cells for early reporting	2801

A.6.6.15.1	Test Purpose and Environment	2801

A.6.6.15.2	Test Requirements	2808

A.6.6.16	PRS-RSRPP measurements	2809

A.6.6.16.1	PRS-RSRPP reporting delay test case for single positioning frequency layer in FR1 in RRC\_CONNECTED state	2809

A.6.6.16.1.1	Test purpose and Environment	2809

A.6.6.16.1.2	Test Requirements	2811

A.6.6.16.2	PRS-RSRPP reporting delay test case with reduced number of samples for single positioning frequency layer in FR1 in RRC\_CONNECTED state	2811

A.6.6.16.2.1	Test purpose and Environment	2811

A.6.6.16.2.2	Test Requirements	2814

A.6.6.16.3	PRS-RSRPP reporting delay test case for single positioning frequency layer in FR1 in RRC\_CONNECTED state without measurement gap	2814

A.6.6.16.3.1	Test purpose and Environment	2814

A.6.6.16.3.2	Test Requirements	2817

A.6.6.17	SA event triggered reporting tests with Pre-MG	2817

A.6.6.17.1	SA event triggered reporting tests with autonomous activation/deactivation Pre-MG	2817

A.6.6.17.1.1	Test purpose and Environment	2817

A.6.6.17.1.2	Test parameters	2817

A.6.6.17.1.3	Test Requirements	2821

A.6.6.17.2	SA event triggered reporting tests with pre-configured measurement gaps and network-controlled activation/deactivation	2821

A.6.6.17.2.1	Test purpose and Environment	2821

A.6.6.17.2.2	Test parameters	2821

A.6.6.17.2.3	Test Requirements	2826

A.6.6.17.3	Void	2826

A.6.6.17.3.1	Void	2826

A.6.6.17.3.2	Void	2826

A.6.6.17.3.3	Void	2826

A.6.6.18	SA event triggered reporting tests with concurrent gaps	2826

A.6.6.18.1	SA event triggered reporting tests for FR1 concurrent gaps with non-overalpping scenario for SSB-based measurements in both inter-frequency layers	2826

A.6.6.18.1.1	Test Purpose and Environment	2826

A.6.6.18.1.2	Test Requirements	2830

A.6.6.18.2	SA event triggered reporting tests for FR1 concurrent gap with partially partial overalpping scenario for SSB-based measurements in both inter-frequency layers	2830

A.6.6.18.2.1	Test Purpose and Environment	2830

A.6.6.18.2.2	Test Requirements	2834

A.6.6.18.3	SA NR - E-UTRAN and NR FR1 concurrent event-triggered reporting in non-DRX in FR1	2834

A.6.6.18.3.1	Test Purpose and Environment	2834

A.6.6.18.3.2	Test Requirements	2841

A.6.6.18.4	SA event triggered reporting tests for PRS and SSB measurement in FR1 without SSB time index detection when DRX is not used	2841

A.6.6.18.4.1	Test Purpose and Environment	2841

A.6.6.18.4.2	Test Requirements	2845

A.6.6.19	SA event triggered reporting tests with NCSG	2846

A.6.6.19.1	SA event triggered reporting tests with NCSG under non-DRX in FR1	2846

A.6.6.19.1.1	Test purpose and Environment	2846

A.6.6.19.1.2	Test parameters	2846

A.6.6.19.1.3	Test Requirements	2850

A.6.6.19.2	SA event triggered reporting tests for FR1 with NCSG for inter-frequency measurement	2850

A.6.6.19.2.1	Test Purpose and Environment	2850

A.6.6.19.2.2	Test parameters	2850

A.6.6.19.2.3	Test Requirements	2854

A.6.6.19.3	SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 with NCSG	2854

A.6.6.19.3.1	Test Purpose and Environment	2854

A.6.6.19.3.2	Test parameters	2855

A.6.6.19.3.3	Test Requirements	2860

A.6.6.19.4	Event triggered reporting on SCC with deactivated SCell test with per-UE NCSG under non-DRX	2860

A.6.6.19.4.1	Test purpose and Environment	2860

A.6.6.19.4.2	Test parameters	2860

A.6.6.19.4.3	Test Requirements	2863

A.6.6.20	UE Rx-Tx time difference measurement for propagation delay compensation	2863

A.6.6.20.1	Test purpose and environment	2863

A.6.6.20.2	Test requirements	2867

A.6.6.21	UE Rx-Tx time difference measurement with TRS for RTT-based PDC in FR1 SA	2867

A.6.6.21.1	Test purpose and environment	2867

A.6.6.21.2	Test requirements	2869

A.6.7	Measurement Performance requirements	2870

A.6.7.1	SS-RSRP	2870

A.6.7.1.1	SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell	2870

A.6.7.1.1.1	Test Purpose and Environment	2870

A.6.7.1.1.2	Test parameters	2870

A.6.7.1.1.3	Test Requirements	2875

A.6.7.1.2	SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell	2875

A.6.7.1.2.1	Test Purpose and Environment	2875

A.6.7.1.2.2	Test parameters	2875

A.6.7.1.2.3	Test Requirements	2879

A.6.7.1.3	Void	2879

A.6.7.2	SS-RSRQ	2879

A.6.7.2.1	SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2879

A.6.7.2.1.1	Test Purpose and Environment	2879

A.6.7.2.1.2	Test Parameters	2880

A.6.7.2.1.3	Test Requirements	2884

A.6.7.2.2	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2884

A.6.7.2.2.1	Test Purpose and Environment	2884

A.6.7.2.2.2	Test Parameters	2884

A.6.7.2.2.3	Test Requirements	2889

A.6.7.3	SS-SINR	2889

A.6.7.3.1	SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2889

A.6.7.3.1.1	Test Purpose and Environment	2889

A.6.7.3.1.2	Test Parameters	2890

A.6.7.3.1.3	Test Requirements	2894

A.6.7.3.2	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2895

A.6.7.3.2.1	Test Purpose and Environment	2895

A.6.7.3.2.2	Test Parameters	2895

A.6.7.3.2.3	Test Requirements	2899

A.6.7.4	L1-RSRP measurement for beam reporting	2900

A.6.7.4.1	SSB based L1-RSRP measurement	2900

A.6.7.4.1.1	Test Purpose and Environment	2900

A.6.7.4.1.2	Test parameters	2900

A.6.7.4.1.3	Test Requirements	2904

A.6.7.4.2	CSI-RS based L1-RSRP measurement on resource set with repetition off	2904

A.6.7.4.2.1	Test Purpose and Environment	2904

A.6.7.4.2.2	Test parameters	2905

A.6.7.4.2.3	Test Requirements	2909

A.6.7.5	E-UTRAN RSRP	2909

A.6.7.5.1	SA: inter-RAT measurement accuracy with FR1 serving cell	2909

A.6.7.5.1.1	Test Purpose and Environment	2909

A.6.7.5.1.2	Test parameters	2910

A.6.7.5.1.3	Test Requirements	2916

A.6.7.6	E-UTRAN RSRQ	2917

A.6.7.6.1	SA: inter-RAT measurement accuracy with FR1 serving cell	2917

A.6.7.6.1.1	Test Purpose and Environment	2917

A.6.7.6.1.2	Test parameters	2917

A.6.7.6.1.3	Test Requirements	2922

A.6.7.7	E-UTRAN RS-SINR	2923

A.6.7.7.1	SA: inter-RAT measurement accuracy with FR1 serving cell	2923

A.6.7.7.1.1	Test Purpose and Environment	2923

A.6.7.7.1.2	Test parameters	2923

A.6.7.7.1.3	Test Requirements	2929

A.6.7.8	CLI measurements	2930

A.6.7.8.1	SA SRS-RSRP measurement accuracy with FR1 serving cell	2930

A.6.7.8.1.1	Test Purpose and Environment	2930

A.6.7.8.1.2	Test parameters	2930

A.6.7.8.1.3	Test Requirements	2936

A.6.7.8.2	SA CLI-RSSI measurement accuracy with FR1 serving cell	2936

A.6.7.8.2.1	Test Purpose and Environment	2936

A.6.7.8.2.2	Test parameters	2937

A.6.7.8.2.3	Test Requirements	2940

A.6.7.9	L1-SINR measurement for beam reporting	2941

A.6.7.9.2	L1-SINR measurement with SSB based CMR and dedicated IMR	2945

A.6.7.9.2.1	Test Purpose and Environment	2945

A.6.7.9.2.2	Test parameters	2946

A.6.7.9.2.3	Test Requirements	2951

A.6.7.9.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR	2951

A.6.7.9.3.1	Test Purpose and Environment	2951

A.6.7.9.3.2	Test parameters	2951

A.6.7.9.3.3	Test Requirements	2956

A.6.7.10	CSI-RSRP	2956

A.6.7.10.1	SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell	2956

A.6.7.9.10.1	Test Purpose and Environment	2956

A.6.7.9.10.2	Test parameters	2957

A.6.7.10.1.3	Test Requirements	2962

A.6.7.10.2	SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell	2962

A.6.7.9.10.1	Test Purpose and Environment	2962

A.6.7.10.2.2	Test parameters	2962

A.6.7.10.2.3	Test Requirements	2968

A.6.7.11	CSI-RSRQ	2968

A.6.7.11.1	SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2968

A.6.7.11.1.1	Test Purpose and Environment	2968

A.6.7.11.1.2	Test Parameters	2968

A.6.7.11.1.3	Test Requirements	2973

A.6.7.11.2	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2973

A.6.7.11.2.1	Test Purpose and Environment	2973

A.6.7.11.2.2	Test Parameters	2973

A.6.7.11.2.3	Test Requirements	2980

A.6.7.12	CSI-SINR	2980

A.6.7.12.1	SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2980

A.6.7.12.1.1	Test Purpose and Environment	2980

A.6.7.12.1.2	Test Parameters	2980

A.6.7.12.1.3	Test Requirements	2985

A.6.7.12.2	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2985

A.6.7.12.2.1	Test Purpose and Environment	2985

A.6.7.12.2.2	Test Parameters	2985

A.6.7.12.2.3	Test Requirements	2991

A.6.7.13	RSTD measurements	2991

A.6.7.13.1	RSTD measurement accuracy test case for single positioning frequency layer	2991

A.6.7.13.1.1	Test purpose and Environment	2991

A.6.7.13.1.2	Test Requirements	2994

A.6.7.13.2	RSTD measurement accuracy test case for dual positioning frequency layer	2994

A.6.7.13.2.1	Test purpose and Environment	2994

A.6.7.13.2.2	Test Requirements	2998

A.6.7.13.3	RSTD measurement accuracy test case with reduced number of samples for single positioning frequency layer in FR1 in RRC\_CONNECTED state	2998

A.6.7.13.3.1	Test purpose and Environment	2998

A.6.7.13.3.2	Test Requirements	3000

A.6.7.13.4	RSTD measurement accuracy test case with Rx TEG	3001

A.6.7.14	PRS-RSRP measurements	3003

A.6.7.14.1	SA: measurement accuracy with PRS in FR1	3003

A.6.7.14.1.1	Test Purpose and Environment	3003

A.6.7.14.1.2	Test parameters	3003

A.6.7.14.1.3	Test Requirements	3007

A.6.7.14.2	SA: measurement accuracy with PRS in FR1 with reduced sample number	3007

A.6.7.14.2.1	Test Purpose and Environment	3007

A.6.7.14.2.2	Test parameters	3007

A.6.7.14.2.3	Test Requirements	3010

A.6.7.14.3	Void	3010

A.6.7.14.3.1	Void	3010

A.6.7.14.3.2	Void	3010

A.6.7.14.3.3	Void	3010

A.6.7.15	UE Rx-Tx time difference measurements	3010

A.6.7.15.1	UE Rx-Tx time difference measurement accuracy for single positioning frequency layer in FR1 SA	3010

A.6.7.15.1.1	Test purpose and environment	3010

A.6.7.15.1.2	Test parameters	3011

A.6.7.15.1.3	Test requirements	3014

A.6.7.15.2	UE Rx-Tx time difference measurement accuracy with reduced number of samples in FR1 SA	3015

A.6.7.15.2.1	Test purpose and environment	3015

A.6.7.15.2.2	Test parameters	3015

A.6.7.15.2.3	Test requirements	3017

A.6.7.15.3	UE Rx-Tx time difference measurement accuracy with RxTx TEG	3017

A.6.7.15.3.1	Test purpose and environment	3017

A.6.7.15.3.2	Test parameters	3018

A.6.7.15.3.3	Test requirements	3021

A.6.7.16	PRS-RSRPP measurements	3021

A.6.7.16.1	SA: measurement accuracy with PRS in FR1	3021

A.6.7.16.1.1	Test Purpose and Environment	3021

A.6.7.16.1.2	Test parameters	3022

A.6.7.16.1.3	Test Requirements	3026

A.6.7.16.2	SA: measurement accuracy with reduced PRS samples in FR1	3026

A.6.7.16.2.1	Test Purpose and Environment	3026

A.6.7.16.2.2	Test parameters	3026

A.6.8	Measurement procedure in RRC\_INACTIVE	3030

A.6.8.1	RSTD measurements	3030

A.6.8.1.1	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC\_INACTIVE state	3030

A.6.8.1.1.1	Test Purpose and Environment	3030

A.6.8.1.1.2	Test Requirements	3033

A.6.8.1.2	 NR RSTD measurement reporting delay test case with reduced number of samples in RRC\_INACTIVE, FR1 SA	3033

A.6.8.1.2.1	Test Purpose and Environment	3033

A.6.8.1.2.2	Test Requirements	3038

A.6.8.2	PRS-RSRP measurements	3038

A.6.8.2.1	PRS-RSRP reporting delay test case for single positioning frequency layer in RRC\_INACTIVE	3038

A.6.8.2.1.1	Test purpose and Environment	3038

A.6.8.2.1.2	Test Requirements	3040

A.6.8.2.2	PRS-RSRP reporting delay test case with reduced number of samples in RRC\_INACTIVE	3041

A.6.8.2.2.1	Test purpose and Environment	3041

A.6.8.2.2.2	Test Requirements	3045

A.6.8.3	UE Rx-Tx time difference measurements	3045

A.6.8.3.1	UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA	3045

A.6.8.3.1.1	Test purpose and environment	3045

A.6.8.3.1.2	Test requirements	3049

A.6.8.3.2	UE Rx-Tx time difference measurement with reduced number of samples in RRC\_INACTIVE, FR1 SA	3049

A.6.8.3.2.1	Test purpose and environment	3049

A.6.8.3.2.2	Test requirements	3052

A.6.8.4	PRS-RSRPP measurements	3052

A.6.8.4.1	PRS-RSRPP reporting delay test case for single positioning frequency layer in FR1 in RRC\_INACTIVE state	3052

A.6.8.4.1.1	Test purpose and Environment	3052

A.6.8.4.1.2	Test Requirements	3055

A.6.8.4.2	PRS-RSRPP reporting delay test case for single positioning frequency layer in FR1 in RRC\_INACTIVE state for reduced number of samples	3055

A.6.8.4.2.1	Test purpose and Environment	3055

A.6.8.4.2.2	Test Requirements	3057

A.6.9	Measurement performance requirements in RRC\_INACTIVE	3058

A.6.9.1	RSTD measurements	3058

A.6.9.1.1	RSTD measurement accuracy test case for single positioning frequency layer in FR1 in RRC\_INACTIVE state	3058

A.6.9.1.1.1	Test purpose and Environment	3058

A.6.9.1.1.2	Test Requirements	3060

A.6.9.1.2	RSTD measurement accuracy test case with reduced number of samples for single positioning frequency layer in FR1 in RRC\_INACTIVE state	3060

A.6.9.1.2.1	Test purpose and Environment	3060

A.6.9.1.2.2	Test Requirements	3062

A.6.9.2	PRS-RSRP measurements	3062

A.6.9.2.1	SA: measurement accuracy with PRS in FR1 in RRC\_INACTIVE	3062

A.6.9.2.1.1	Test Purpose and Environment	3062

A.6.9.2.1.2	Test parameters	3062

A.6.9.2.1.3	Test Requirements	3066

A.6.9.2.2	SA: measurement accuracy with PRS in FR1 with reduced number of samples in RRC\_INACTIVE state	3066

A.6.9.2.2.1	Test Purpose and Environment	3066

A.6.9.2.2.2	Test parameters	3066

A.6.9.2.2.3	Test Requirements	3068

A.6.9.3	UE Rx-Tx time difference measurements	3069

A.6.9.3.1.1	UE Rx-Tx time difference measurement accuracy in FR1 SA	3069

A.6.9.3.1.1.1	Test purpose and environment	3069

A.6.9.3.1.1.2 Test parameters	3069

A.6.9.3.1.1.3	Test requirements	3071

A.6.9.3.2	UE Rx-Tx time difference measurement accuracy with reduced number of samples	3071

A.6.9.3.2.1	Test purpose and environment	3071

A.6.9.3.2.2	Test parameters	3071

A.6.9.3.2.3	Test requirements	3074

A.6.9.4	PRS-RSRPP measurements	3074

A.6.9.4.1	SA: PRS-RSRPP measurement accuracy in FR1 in RRC INACTIVE	3074

A.6.9.4.1.1	Test Purpose and Environment	3074

A.6.9.4.1.2	Test parameters	3074

A.6.9.4.1.3	Test Requirements	3078

A.6.9.4.2	SA: measurement accuracy with reduced PRS samples in FR1 in RRC INACTIVE	3078

A.6.9.4.2.1	Test Purpose and Environment	3078

A.6.9.4.2.2	Test parameters	3078

A.6.9.4.2.3	Test Requirements	3080

A.7	NR standalone tests with one or more NR cells in FR2	3076

A.7.1	SA: RRC\_IDLE state mobility	3076

A.7.1.1	Cell re-selection to NR	3076

A.7.1.1.1	Cell reselection to FR2 intra-frequency NR case	3076

A.7.1.1.1.1	Test Purpose and Environment	3076

A.7.1.1.1.2	Test Parameters	3076

A.7.1.1.1.3	Test Requirements	3079

A.7.1.1.2	Cell reselection to FR2 inter-frequency NR case	3080

A.7.1.1.2.1	Test Purpose and Environment	3080

A.7.1.1.2.2	Test Parameters	3080

A.7.1.1.2.3	Test Requirements	3082

A.7.1.1.3	Cell reselection to FR2 intra-frequency NR case for UE fulfilling low mobility relaxed measurement criterion	3083

A.7.1.1.3.1	Test Purpose and Environment	3083

A.7.1.1.3.2	Test Parameters	3083

A.7.1.1.3.3	Test Requirements	3086

A.7.1.1.4	Cell reselection to FR2 intra-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion	3086

A.7.1.1.4.1	Test Purpose and Environment	3086

A.7.1.1.4.2	Test Parameters	3086

A.7.1.1.4.3	Test Requirements	3089

A.7.1.1.5	Cell reselection to FR2 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion	3089

A.7.1.1.5.1	Test Purpose and Environment	3089

A.7.1.1.5.2	Test Parameters	3089

A.7.1.1.5.3	Test Requirements	3092

A.7.1.1.6	Cell reselection to FR2 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion	3093

A.7.1.1.6.1	Test Purpose and Environment	3093

A.7.1.1.6.2	Test Parameters	3093

A.7.1.1.6.3	Test Requirements	3096

A.7.1.1.7	Cell reselection to FR2 intra-frequency NR case for FR2 power class 6 UE configured with *highSpeedMeasFlagFR2-r17* 3097

A.7.1.1.7.1	Test Purpose and Environment	3097

A.7.1.1.7.2	Test Parameters	3097

A.7.1.1.7.3	Test Requirements	3101

A.7.2	SA: RRC\_INACTIVE state mobility	3101

A.7.2.1	Small Data Transmission	3101

A.7.2.1.1	TA validation for CG-SDT in FR2	3101

A.7.2.1.1.1	Test Purpose and Environment	3101

A.7.2.1.1.2	Test Requirements	3105

A.7.3	RRC\_CONNECTED state mobility	3105

A.7.3.1	Handover	3105

A.7.3.1.1	Inter-frequency handover from FR1 to FR2; unknown target cell	3105

A.7.3.1.1.1	Test Purpose and Environment	3105

A.7.3.1.1.2	Test Parameters	3105

A.7.3.1.1.3	Test Requirements	3109

A.7.3.1.2	Intra-frequency handover from FR2 to FR2; unknown target cell	3109

A.7.3.1.2.1	Test Purpose and Environment	3109

A.7.3.1.2.2	Test Parameters	3109

A.7.3.1.2.3	Test Requirements	3112

A.7.3.1.3	Inter-frequency handover from FR2 to FR2; unknown target cell	3112

A.7.3.1.3.1	Test Purpose and Environment	3112

A.7.3.1.3.2	Test Parameters	3112

A.7.3.1.3.3	Test Requirements	3113

A.7.3.1.4	Inter-band inter-frequency synchronous DAPS handover from FR1 to FR2	3114

A.7.3.1.4.1	Test Purpose and Environment	3114

A.7.3.1.4.2	Test Parameters	3114

A.7.3.1.4.3 Test Requirements	3121

A.7.3.1.5	Inter-band inter-frequency asynchronous DAPS handover from FR1 to FR2	3121

A.7.3.1.5.1	Test Purpose and Environment	3121

A.7.3.1.5.2	Test Parameters	3121

A.7.3.1.5.3 Test Requirements	3128

A.7.3.1.6	Handover with PSCell from SA to EN-DC with; unknown FR2 target PScell	3128

A.7.3.1.6.1	Test Purpose and Environment	3128

A.7.3.1.6.2	Test Parameters	3128

A.7.3.1.6.3	Test Requirements	3137

A.7.3.1.7	HO with PSCell from FR1 NR-SA to EN-DC with known E-UTRA PCell and known FR2 PSCell	3138

A.7.3.1.7.1	Test purpose and environment	3138

A.7.3.1.7.2	Test Requirements	3143

A.7.3.1.8	NR PSCell change delay in HO with PSCell from NR-DC to NR-DC	3144

A.7.3.1.8.1	Test Purpose and Environment	3144

A.7.3.1.8.2	Test Requirements	3149

A.7.3.1.9	Intra-frequency handover from FR2-2 to FR2-2; unknown target cell	3149

A.7.3.1.9.1	Test Purpose and Environment	3149

A.7.3.1.9.2	Test Parameters	3149

A.7.3.1.9.3	Test Requirements	3152

A.7.3.1.10	Inter-frequency handover from FR2-2 to FR2-2; unknown target cell	3152

A.7.3.1.10.1	Test Purpose and Environment	3152

A.7.3.1.10.2	Test Parameters	3152

A.7.3.1.10.3	Test Requirements	3156

A.7.3.1.11	Inter-frequency handover from FR1 to FR2-2; unknown target cell	3156

A.7.3.1.11.1	Test Purpose and Environment	3156

A.7.3.1.11.2	Test Parameters	3156

A.7.3.1.11.3	Test Requirements	3160

A.7.3.2	RRC Connection Mobility Control	3160

A.7.3.2.1	SA: RRC Re-establishment	3160

A.7.3.2.1.1	Intra-frequency RRC Re-establishment in FR2	3160

A.7.3.2.1.2	Inter-frequency RRC Re-establishment in FR2	3163

A.7.3.2.1.3	Intra-frequency RRC Re-establishment in FR2 without serving cell timing	3166

A.7.3.2.1.3.1	Test Purpose and Environment	3166

A.7.3.2.1.3.2	Test Requirements	3168

A.7.3.2.1.4	Intra-frequency RRC Re-establishment in FR2-2	3169

A.7.3.2.1.4.1	Test Purpose and Environment	3169

A.7.3.2.1.4.2	Test Requirements	3171

A.7.3.2.1.5	Inter-frequency RRC Re-establishment in FR2-2	3172

A.7.3.2.1.5.1	Test Purpose and Environment	3172

A.7.3.2.1.5.2	Test Requirements	3175

A.7.3.2.1.6	Intra-frequency RRC Re-establishment in FR2-2 without serving cell timing	3175

A.7.3.2.1.6.1	Test Purpose and Environment	3175

A.7.3.2.1.6.2	Test Requirements	3177

A.7.3.2.2	Random Access	3178

A.7.3.2.2.1	4-step RA type c ontention based random access test in FR2 for NR Standalone	3178

A.7.3.2.2.2	4-step RA type n on-contention based random access test in FR2 for NR Standalone	3182

A.7.3.2.2.3	2-step RA type contention based random access test in FR2 for NR Standalone	3186

A.7.3.2.2.4	2-step RA type n on-contention based random access test in FR2 for NR Standalone	3189

A.7.3.2.3	SA: RRC Connection Release with Redirection	3192

A.7.3.2.3.1	Redirection from NR in FR2 to NR in FR2	3192

A.7.3.3 Conditional Handover	3196

A.7.3.3.1	Intra-frequency conditional handover from FR2 to FR2	3196

A.7.3.3.1.1	Test Purpose and Environment	3196

A.7.3.3.1.2	Test Parameters	3196

A.7.3.3.1.2.3	Test Requirements	3199

A.7.3.3.2	Inter-frequency conditional handover from FR2 to FR2; unknown target cell	3199

A.7.3.3.2.1	Test Purpose and Environment	3199

A.7.3.3.2.2	Test Parameters	3199

A.7.3.3.2.3 Test Requirements	3201

A.7.4	Timing	3201

A.7.4.1	UE transmit timing	3201

A.7.4.1.1	NR UE Transmit Timing Test for FR2	3201

A.7.4.1.1.1	Test Purpose and environment	3201

A.7.4.1.1.2	Test requirements	3204

A.7.4.1.2	NR UE Transmit Timing Test for FR2-2	3204

A.7.4.1.2.1	Test Purpose and environment	3204

A.7.4.1.2.2	Test requirements	3209

A.7.4.2	UE timer accuracy	3210

A.7.4.3	Timing advance	3210

A.7.4.3.1	SA FR2 timing advance adjustment accuracy	3210

A.7.4.3.1.1	Test Purpose and Environment	3210

A.7.4.3.1.2	Test Parameters	3210

A.7.4.3.1.3 Test Requirements	3213

A.7.4.3.2	SA FR2-2 timing advance adjustment accuracy	3214

A.7.4.3.2.1	Test Purpose and Environment	3214

A.7.4.3.2.2	Test Parameters	3214

A.7.4.3.2.3	Test Requirements	3218

A.7.5	Signaling characteristics	3218

A.7.5.1	Radio link Monitoring	3218

A.7.5.1.1	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode	3218

A.7.5.1.1.1	Test Purpose and Environment	3218

A.7.5.1.1.2	Test Requirements	3221

A.7.5.1.2	Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode	3222

A.7.5.1.2.1	Test Purpose and Environment	3222

A.7.5.1.2.2	Test Requirements	3226

A.7.5.1.3	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode	3227

A.7.5.1.3.1	Test Purpose and Environment	3227

A.7.5.1.3.2	Test Requirements	3231

A.7.5.1.4	Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode	3231

A.7.5.1.4.1	Test Purpose and Environment	3231

A.7.5.1.4.2	Test Requirements	3236

A.7.5.1.5	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode	3236

A.7.5.1.5.1	Test Purpose and Environment	3236

A.7.5.1.5.2	Test Requirements	3241

A.7.5.1.6	Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode	3241

A.7.5.1.6.1	Test Purpose and Environment	3241

A.7.5.1.6.2	Test Requirements	3245

A.7.5.1.7	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode	3245

A.7.5.1.7.1	Test Purpose and Environment	3245

A.7.5.1.7.2	Test Requirements	3249

A.7.5.1.8	Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode	3249

A.7.5.1.8.1	Test Purpose and Environment	3249

A.7.5.1.8.2	Test Requirements	3254

A.7.5.1.9	UE Radio Link Monitoring Scheduling Restrictions on FR2	3254

A.7.5.1.9.1	Test Purpose and Environment	3254

A.7.5.1.9.2	Test Requirements	3257

A.7.5.2	Interruption	3257

A.7.5.2.1	Interruptions during measurements on deactivated NR SCC in FR2	3257

A.7.5.2.1.1	Test Purpose and Environment	3257

A.7.5.2.1.2	Test Requirements	3260

A.7.5.2.2	SA interruptions at NR SRS carrier-based switching	3261

A.7.5.2.2.1	Test Purpose and Environment	3261

A.7.5.2.2.2	Test Parameters	3261

A.7.5.2.2.3	Test Requirements	3263

A.7.5.3	SCell Activation and Deactivation Delay	3263

A.7.5.3.1	SCell Activation and deactivation for SCell in FR2 intra-band in non-DRX	3263

A.7.5.3.1.1	Test Purpose and Environment	3263

A.7.5.3.1.2	Test Requirements	3265

A.7.5.3.2	SCell Activation and deactivation for FR1+FR2 inter-band with target SCell in FR2	3265

A.7.5.3.2.1	Test Purpose and Environment	3265

A.7.5.3.2.2	Test Requirements	3269

A.7.5.3.3	SCell Activation and deactivation for SCell in FR2 inter-band in non-DRX	3270

A.7.5.3.3.1	Test Purpose and Environment	3270

A.7.5.3.3.2	Test Requirements	3273

A.7.5.3.4	Direct SCell activation at SCell addition of known SCell in FR2	3274

A.7.5.3.4.1	Test Purpose and Environment	3274

A.7.5.3.4.2	Test Requirements	3277

A.7.5.3.5	Direct SCell activation at handover with known SCell in FR2	3278

A.7.5.3.5.1	Test Purpose and Environment	3278

A.7.5.3.5.2	Test Requirements	3281

A.7.5.3.6	PUCCH SCell activation and deactivation for FR1+FR2 inter-band with target SCell in FR2 and known	3282

A.7.5.3.6.1	Test Purpose and Environment	3282

A.7.5.3.6.2	Test Requirements	3286

A.7.5.3.7	PUCCH SCell activation and deactivation delay requirements of FR2 unknown cell with FR1 PCell	3287

A.7.5.3.7.1	Test Purpose and Environment	3287

A.7.5.3.7.2	Test Requirements	3291

A.7.5.3.8	SCell Activation and deactivation for known PUCCH SCell in FR2 inter-band in non-DRX	3292

A.7.5.3.8.1	Test Purpose and Environment	3292

A.7.5.3.8.2	Test Requirements	3296

A.7.5.3.9	PUCCH SCell Activation and deactivation of unknown SCell in FR2	3297

A.7.5.3.9.1	Test Purpose and Environment	3297

A.7.5.3.9.2	Test Requirements	3300

A.7.5.3.10	SCell Activation and deactivation of FR2 known PUCCH SCell and one FR2 unknown SCell with FR2 PCell	3301

A.7.5.3.10.1	Test Purpose and Environment	3301

A.7.5.3.10.2	Test Requirements	3305

A.7.5.3.11	PUCCH SCell activation and deactivation delay requirements of FR2 unknown cell with FR2 PCell	3306

A.7.5.3.11.1	PUCCH SCell activation with non-PUCCH SCell in a secondary PUCCH Group	3306

A.7.5.3.11.1.1	Test Purpose and Environment	3306

A.7.5.3.11.1.2	Test Requirements	3310

A.7.5.3.11.2	PUCCH SCell activation with non-PUCCH SCell in a primary PUCCH Group	3311

A.7.5.3.11.2.1	Test Purpose and Environment	3311

A.7.5.3.11.2.2	Test Requirements	3315

A.7.5.3.12	Void	3316

A.7.5.3.13	SCell Activation for SCell in FR2 intra-band in non-DRX	3316

A.7.5.3.13.1	Test Purpose and Environment	3316

A.7.5.3.13.2	Test Requirements	3318

A.7.5.3.14	SCell Activation for known SCell in FR2 inter-band	3319

A.7.5.3.14.1	Test Purpose and Environment	3319

A.7.5.3.14.2	Test Requirements	3322

A.7.5.15	Void	3323

A.7.5.4	Void	3323

A.7.5.5	Beam Failure Detection and Link recovery procedures	3323

A.7.5.5.1	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode	3323

A.7.5.5.1.1	Test Purpose and Environment	3323

A.7.5.5.1.2	Test Requirements	3327

A.7.5.5.2	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in DRX mode	3328

A.7.5.5.2.1	Test Purpose and Environment	3328

A.7.5.5.2.2	Test Requirements	3331

A.7.5.5.3	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode	3332

A.7.5.5.3.1	Test Purpose and Environment	3332

A.7.5.5.3.2	Test Requirements	3336

A.7.5.5.4	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode	3337

A.7.5.5.4.1	Test Purpose and Environment	3337

A.7.5.5.4.2	Test Requirements	3341

A.7.5.5.5	Scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode	3342

A.7.5.5.5.1	Test Purpose and Environment	3342

A.7.5.5.5.2	Test Requirements	3345

A.7.5.5.6	Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in non-DRX mode	3346

A.7.5.5.6.1	Test Purpose and Environment	3346

A.7.5.5.6.2	Test Requirements	3350

A.7.5.5.7	Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in DRX mode	3351

A.7.5.5.7.1	Test Purpose and Environment	3351

A.7.5.5.7.2	Test Requirements	3355

A.7.5.5.8	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode for UE fulfilling relaxed measurement criterion	3356

A.7.5.5.8.1	Test Purpose and Environment	3356

A.7.5.5.8.2	Test Requirements	3360

A.7.5.5.9	TRP specific Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in DRX mode	3360

A.7.5.5.9.1	Test Purpose and Environment	3360

A.7.5.5.9.2	Test Requirements	3366

A.7.5.5.10	TRP specific Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode	3366

A.7.5.5.10.1	Test Purpose and Environment	3366

A.7.5.5.10.2	Test Requirements	3372

A.7.5.5.11	Beam Failure Detection and Link Recovery Test for FR2-2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode	3372

A.7.5.5.11.1	Test Purpose and Environment	3372

A.7.5.5.11.2	Test Requirements	3377

A.7.5.5.12	Beam Failure Detection and Link Recovery Test for FR2-2 PCell configured with CSI-RS-based BFD and LR in DRX mode	3377

A.7.5.5.12.1	Test Purpose and Environment	3377

A.7.5.5.12.2	Test Requirements	3382

A.7.5.5.13	Scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2-2 PCell configured with SSB-based BFD and LR in non-DRX mode	3382

A.7.5.5.13.1	Test Purpose and Environment	3382

A.7.5.5.13.2	Test Requirements	3386

A.7.5.6	Active BWP switch	3386

A.7.5.6.1	DCI-based and Timer-based Active BWP Switch	3386

A.7.5.6.1.1	NR FR2- NR FR2 DL active BWP switch of SCell with non-DRX in SA	3386

A.7.5.6.1.2	NR FR1- NR FR2 DL active BWP switch of SCell with non-DRX in SA	3391

A.7.5.6.1.3	NR FR2 DL active BWP switch with non-DRX in SA	3396

A.7.5.6.1.3.1	Test Purpose and Environment	3396

A.7.5.6.1.3.2	Test Requirements	3399

A.7.5.6.1.4	NR FR2-2- NR FR2-2 DL active BWP switch of SCell with non-DRX in SA	3399

A.7.5.6.1.4.1	Test Purpose and Environment	3399

A.7.5.6.1.4.2	Test Requirements	3404

A.7.5.6.2	RRC-based Active BWP Switch	3405

A.7.5.6.2.1.1	Test Purpose and Environment	3405

A.7.5.6.2.1.2	Test Requirements	3408

A.7.5.6.2.2	NR FR2-2 DL active BWP switch of PCell with non-DRX in SA	3409

A.7.5.6.2.2.1	Test Purpose and Environment	3409

A.7.5.6.2.2.2	Test Requirements	3413

A.7.5.6.3 Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs	3414

A.7.5.6.3.1.1	Test Purpose and Environment	3414

A.7.5.6.3.1.2	Test Requirements	3417

A.7.5.6.4	SCell dormancy switch	3417

A.7.5.6.4.1	NR FR2 PCell SCell dormancy switch of single FR2 SCell inside active time	3417

A.7.5.6.4.1.1	Test Purpose and Environment	3417

A.7.5.6.4.1.2	Test Requirements	3422

A.7.5.6.4.2	NR FR1 PCell SCell dormancy switch of two FR2 SCells outside active time	3422

A.7.5.6.4.2.1	 Test Purpose and Environment	3422

A.7.5.6.4.2.2	 Test Requirements	3427

A.7.5.6.5	Simultaneous RRC-based Active BWP Switch on multiple CCs	3427

A.7.5.6.5.1	Active BWP switch on multiple SCells with non-DRX in SA	3427

A.7.5.6.5.2	NR FR2-2 Active BWP switch on multiple SCells with non-DRX in SA	3430

A.7.5.6.5.2.1	Test Purpose and Environment	3430

A.7.5.6.5.2.2	Test Requirements	3434

A.7.5.7	PSCell addition and release delay	3435

A.7.5.7.1	Addition and Release Delay of known NR PSCell	3435

A.7.5.7.1.1	Test Purpose and Environment	3435

A.7.5.7.1.2	Test Requirements	3438

A.7.5.7.2	Addition and Release Delay of unknown NR PSCell in	3438

A.7.5.7.2.1	Test Purpose and Environment	3438

A.7.5.7.2.2	Test Requirements	3441

A.7.5.7.3	Addition and Release Delay of known NR PSCell in FR2-2	3441

A.7.5.7.3.1	Test Purpose and Environment	3441

A.7.5.7.3.2	Test Requirements	3444

A.7.5.7.4	Addition and Release Delay of unknown NR PSCell in FR2-2	3444

A.7.5.7.4.1	Test Purpose and Environment	3444

A.7.5.7.4.2	Test Requirements	3447

A.7.5.8	Active TCI state switch delay	3447

A.7.5.8.1	MAC-CE based active TCI state switch	3447

A.7.5.8.2	RRC based active TCI state switch	3451

A.7.5.8.3	MAC-CE based active TCI state switch for HST FR2 scenario	3455

A.7.5.8.3.1	NR PCell FR2 HST active TCI state switch for a known TCI state	3455

A.7.5.8.3.1.1	Test Purpose and Environment	3455

A.7.5.8.3.1.2	Test Requirements	3459

A.7.5.9	Uplink spatial relation switch delay	3460

A.7.5.9.1.1.1	Test Purpose and Environment	3460

A.7.5.9.1.1.2	Test Requirements	3463

A.7.5.9.2	RRC based spatial relation switch	3463

A.7.5.9.2.1	NR PCell FR2 spatial relation switch associated with a known DL-RS	3463

A.7.5.9.2.1.1	Test Purpose and Environment	3463

A.7.5.9.2.1.2	Test Requirements	3466

A.7.5.10	UE specific CBW change	3466

A.7.5.10.1	NR FR2 UE specific CBW change of PCell with non-DRX in SA	3466

A.7.5.10.1.1	Test Purpose and Environment	3466

A.7.5.10.1.2	Test Requirements	3469

A.7.5.11	UE UL carrier RRC reconfiguration Delay	3470

A.7.5.11.1	UE UL carrier RRC reconfiguration Delay	3470

A.7.5.11.1.1	Test Purpose and Environment	3470

A.7.5.11.1.2	Test Requirements	3473

A.7.5.12	Conditional PSCell addition and release delay (FR2 SA)	3473

A.7.5.12.1	Addition and Release Delay of PSCell	3473

A.7.5.12.1.1	Test purpose and environment	3473

A.7.5.12.1.2	Test Parameters	3473

A.7.5.12.1.3	Test Requirements	3476

A.7.5.13	 Unified TCI state switching delay	3476

A.7.5.13.1	MAC-CE based active joint TCI state switching	3476

A.7.5.13.1.1	NR PCell FR2 active joint TCI state switch for a known TCI state	3476

A.7.5.13.1.1.1	Test Purpose and Environment	3476

A.7.5.13.1.1.2	Test parameters	3477

A.7.5.13.1.1.3	Test Requirements	3479

A.7.5.13.2	 MAC-CE based active uplink TCI state switch	3479

A.7.5.13.2.1	 NR FR2 PCell uplink TCI state switch for a known TCI state	3479

A.7.5.13.2.1.1	Test Purpose and Environment	3479

A.7.5.13.2.1.2	Test parameters	3480

A.7.5.13.2.1.3	Test Requirements	3482

A.7.5.13.3	MAC-CE based active downlink TCI state switch	3482

A.7.5.13.3.1	NR PCell FR2 active downlink TCI state switch to cell with additional PCI for a known TCI state	3482

A.7.5.13.3.1.1	Test Purpose and Environment	3482

A.7.5.13.3.1.2	Test Parameters	3483

A.7.5.13.3.1.3	Test Requirements	3486

A.7.5.14	PSCell RACH-less based Activation and deactivation for FR1+FR2 inter-band with target PSCell in FR2	3486

A.7.5.14.1	Test Purpose and Environment	3486

A.7.5.14.2	Test Requirements	3489

A.7.6	Measurement procedure	3490

A.7.6.1	Intra-frequency Measurements	3490

A.7.6.1.1	SA event triggered reporting test without gap under non-DRX	3490

A.7.6.1.1.1	Test purpose and Environment	3490

A.7.6.1.1.2	Test Requirements	3493

A.7.6.1.2	SA event triggered reporting test without gap under DRX	3493

A.7.6.1.2.1	Test purpose and Environment	3493

A.7.6.1.2.2	Test Requirements	3496

A.7.6.1.3	SA event triggered reporting test with per-UE gaps under non-DRX	3497

A.7.6.1.3.1	Test purpose and Environment	3497

A.7.6.1.3.2	Test Requirements	3500

A.7.6.1.4	SA event triggered reporting test with per-UE gaps under DRX	3500

A.7.6.1.4.1	Test purpose and Environment	3500

A.7.6.1.4.2	Test Requirements	3503

A.7.6.1.5	SA event triggered reporting test without gap under non-DRX for UE configured with *highSpeedMeasFlagFR2-r17* 3504

A.7.6.1.5.1	Test purpose and Environment	3504

A.7.6.1.5.2	Test Requirements	3507

A.7.6.1.6	SA event triggered reporting test without gap under non-DRX for FR2-2	3507

A.7.6.1.6.1	Test purpose and Environment	3507

A.7.6.1.6.2	Test Requirements	3510

A.7.6.1.7	SA event triggered reporting test without gap under DRX for FR2-2	3511

A.7.6.1.7.1	Test purpose and Environment	3511

A.7.6.1.7.2	Test Requirements	3513

A.7.6.1.8	SA event triggered reporting test with per-UE gaps under non-DRX for FR2-2	3514

A.7.6.1.8.1	Test purpose and Environment	3514

A.7.6.1.8.2	Test Requirements	3517

A.7.6.1.9	SA event triggered reporting test with per-UE gaps under DRX for FR2-2	3518

A.7.6.1.9.1	Test purpose and Environment	3518

A.7.6.1.9.2	Test Requirements	3520

A.7.6.1.10	SA event triggered reporting test with SSB time index detection without gap under non-DRX for FR2-2	3521

A.7.6.1.10.1	Test purpose and Environment	3521

A.7.6.1.10.2	Test Requirements	3525

A.7.6.1.11	SA event triggered reporting test with SSB time index detection with per-UE gaps under non-DRX for FR2-2	3525

A.7.6.1.11.1	Test purpose and Environment	3525

A.7.6.1.11.2	Test Requirements	3528

A.7.6.2	Inter-frequency Measurements	3528

A.7.6.2.1	SA event triggered reporting tests for FR2 without SSB time index detection when DRX is not used (PCell in FR2)	3528

A.7.6.2.1.1	Test Purpose and Environment	3528

A.7.6.2.1.2	Test Requirements	3532

A.7.6.2.2	SA event triggered reporting tests for FR2 without SSB time index detection when DRX is used (Pcell in FR2)	3532

A.7.6.2.2.1	Test Purpose and Environment	3532

A.7.6.2.2.2	Test Requirements	3536

A.7.6.2.3	SA event triggered reporting tests for FR2 with SSB time index detection when DRX is not used (PCell in FR2)	3536

A.7.6.2.3.1	Test Purpose and Environment	3536

A.7.6.2.3.2	Test Requirements	3540

A.7.6.2.4	SA event triggered reporting tests for FR2 with SSB time index detection when DRX is used (Pcell in FR2)	3540

A.7.6.2.4.1	Test Purpose and Environment	3540

A.7.6.2.4.2	Test Requirements	3544

A.7.6.2.5	SA event triggered reporting tests for FR2 without SSB time index detection when DRX is not used (PCell in FR1)	3544

A.7.6.2.5.1	Test Purpose and Environment	3544

A.7.6.2.5.2	Test Requirements	3548

A.7.6.2.6	SA event triggered reporting tests for FR2 without SSB time index detection when DRX is used (Pcell in FR1)	3549

A.7.6.2.6.1	Test Purpose and Environment	3549

A.7.6.2.6.2	Test Requirements	3553

A.7.6.2.7	SA event triggered reporting tests for FR2 with SSB time index detection when DRX is not used (PCell in FR1)	3554

A.7.6.2.7.1	Test Purpose and Environment	3554

A.7.6.2.7.2	Test Requirements	3558

A.7.6.2.8	SA event triggered reporting tests for FR2 with SSB time index detection when DRX is used (PCell in FR1)	3559

A.7.6.2.8.1	Test Purpose and Environment	3559

A.7.6.2.8.2	Test Requirements	3563

A.7.6.2.9	SA event triggered reporting tests For FR2 without SSB time index detection when DRX is not used (PCell in FR2) (rel16 additional mandatory gap pattern 17)	3564

A.7.6.2.9.1	Test Purpose and Environment	3564

A.7.6.2.9.2	Test Requirements	3568

A.7.6.2.10	SA event triggered reporting test without gap under non-DRX	3568

A.7.6.2.10.1	Test Purpose and Environment	3568

A.7.6.2.10.2	Test Requirements	3570

A.7.6.2.11	SA event triggered reporting test without gap under DRX	3571

A.7.6.2.11.1	Test Purpose and Environment	3571

A.7.6.2.11.2	Test Requirements	3573

A.7.6.2.12	SA event triggered reporting tests for FR2-2 without SSB time index detection when DRX is not used (PCell in FR2-2)	3574

A.7.6.2.12.1	Test Purpose and Environment	3574

A.7.6.2.12.2	Test Requirements	3577

A.7.6.2.13	SA event triggered reporting tests for FR2-2 without SSB time index detection when DRX is used (PCell in FR2-2)	3578

A.7.6.2.13.1	Test Purpose and Environment	3578

A.7.6.2.13.2	Test Requirements	3582

A.7.6.2.14	SA event triggered reporting tests for FR2-2 with SSB time index detection when DRX is not used (PCell in FR2-2)	3583

A.7.6.2.14.1	Test Purpose and Environment	3583

A.7.6.2.14.2	Test Requirements	3587

A.7.6.2.15	SA event triggered reporting tests for FR2-2 with SSB time index detection when DRX is used (PCell in FR2-2)	3588

A.7.6.2.15.1	Test Purpose and Environment	3588

A.7.6.2.15.2	Test Requirements	3592

A.7.6.2.16	SA event triggered reporting tests for FR2-2 without SSB time index detection when DRX is not used (PCell in FR1)	3593

A.7.6.2.16.1	Test Purpose and Environment	3593

A.7.6.2.16.2	Test Requirements	3599

A.7.6.2.17	SA event triggered reporting tests for FR2-2 without SSB time index detection when DRX is used (PCell in FR1)	3599

A.7.6.2.17.1	Test Purpose and Environment	3599

A.7.6.2.17.2	Test Requirements	3606

A.7.6.2.18	SA event triggered reporting tests for FR2-2 with SSB time index detection when DRX is not used (PCell in FR1)	3607

A.7.6.2.18.1	Test Purpose and Environment	3607

A.7.6.2.18.2	Test Requirements	3613

A.7.6.2.19	SA event triggered reporting tests for FR2-2 with SSB time index detection when DRX is used (PCell in FR1)	3613

A.7.6.2.19.1	Test Purpose and Environment	3613

A.7.6.2.19.2	Test Requirements	3621

A.7.6.3	L1-RSRP measurement for beam reporting	3622

A.7.6.3.1	SSB based L1-RSRP measurement when DRX is not used	3622

A.7.6.3.1.1	Test Purpose and Environment	3622

A.7.6.3.1.2	Test parameters	3622

A.7.6.3.1.3	Test Requirements	3624

A.7.6.3.2	SSB based L1-RSRP measurement when DRX is used	3624

A.7.6.3.2.1	Test Purpose and Environment	3624

A.7.6.3.2.2	Test parameters	3625

A.7.6.3.2.3	Test Requirements	3627

A.7.6.3.3	CSI-RS based L1-RSRP measurement when DRX is not used	3627

A.7.6.3.3.1	Test Purpose and Environment	3627

A.7.6.3.3.2	Test parameters	3628

A.7.6.3.3.3	Test Requirements	3630

A.7.6.3.4	CSI-RS based L1-RSRP measurement when DRX is used	3631

A.7.6.3.4.1	Test Purpose and Environment	3631

A.7.6.3.4.2	Test parameters	3631

A.7.6.3.3.3	Test Requirements	3633

A.7.6.3.5	SSB based L1-RSRP measurement when DRX is used for power class 6 UE configured with *highSpeedMeasFlagFR2-r17* 3634

A.7.6.3.5.1	Test Purpose and Environment	3634

A.7.6.3.5.2	Test parameters	3634

A.7.6.3.5.3	Test Requirements	3636

A.7.6.3.6	Inter-cell SSB based L1-RSRP measurements on FR2 SCell when DRX is not used	3636

A.7.6.3.6.1	Test Purpose and Environment	3636

A.7.6.3.6.2	Test parameters	3637

A.7.6.3.6.3	Test Requirements	3640

A.7.6.3.7	SSB based L1-RSRP measurement for FR2-2 when DRX is used	3640

A.7.6.3.7.1	Test Purpose and Environment	3640

A.7.6.3.7.2	Test parameters	3641

A.7.6.3.7.3	Test Requirements	3644

A.7.6.4	CLI measurements	3645

A.7.6.4.1	SRS-RSRP measurement with non-DRX	3645

A.7.6.4.1.1	Test Purpose and Environment	3645

A.7.6.4.1.2	Test Parameters	3645

A.7.6.4.1.3	Test Requirements	3647

A.7.6.4.2	CLI-RSSI measurement with non-DRX	3647

A.7.6.4.2.1	Test Purpose and Environment	3647

A.7.6.4.2.2	Test Parameters	3648

A.7.6.4.2.3	Test Requirements	3649

A.7.6.5.1   SA interfrequency CGI reporting in autonomous gaps test (PCell in FR2)	3650

A.7.6.5.1.1	Test Purpose and Environment	3650

A.7.6.5.1.2	Test Requirements	3653

A.7.6.6	L1-SINR measurement for beam reporting	3653

A.7.6.6.2	L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is used	3655

A.7.6.6.2.1	Test Purpose and Environment	3655

A.7.6.6.2.2	Test parameters	3656

A.7.6.6.2.3	Test Requirements	3658

A.7.6.6.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is used	3658

A.7.6.6.3.1	Test Purpose and Environment	3658

A.7.6.6.3.2	Test parameters	3659

A.7.6.6.3.3	Test Requirements	3661

A.7.6.7	CSI-RS based intra-frequency Measurements	3661

A.7.6.7.1	SA event triggered reporting test without gap under DRX for CSI-RS based intra-frequency measurement	3661

A.7.6.7.1.1	Test purpose and Environment	3661

A.7.6.7.1.2	Test Requirements	3664

A.7.6.8	CSI-RS based inter-frequency Measurements	3665

A.7.6.8.1	SA event triggered reporting tests for FR2 CSI-RS based measurement when non-DRX is used (PCell in FR2)	3665

A.7.6.8.1.1	Test Purpose and Environment	3665

A.7.6.8.1.2	Test Requirements	3668

A.7.6.9	RSTD measurements	3668

A.7.6.9.1	 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA	3668

A.7.6.9.1.1	Test Purpose and Environment	3668

A.7.6.9.1.2	Test Requirements	3676

A.7.6.9.2	 NR RSTD measurement reporting delay test case for dual positioning frequency layers in FR2 SA	3676

A.7.6.9.2.1	Test Purpose and Environment	3676

A.7.6.9.2.2	Test Requirements	3684

A.7.6.9.3	NR RSTD measurement reporting delay test case for single positioning frequency layer with reduced number of samples in FR2 SA	3684

A.7.6.9.3.1	Test Purpose and Environment	3684

A.7.6.9.3.2	Test Requirements	3690

A.7.6.9.4	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA without measurement gap	3691

A.7.6.9.4.1	Test Purpose and Environment	3691

A.7.6.9.4.2	Test Requirements	3694

A.7.6.9.5	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC\_CONNECTED state with Rx TEG	3695

A.7.6.9.5.1	Test Purpose and Environment	3695

A.7.6.9.5.2	Test Requirements	3698

A.7.6.10 PRS-RSRP measurements	3699

A.7.6.10.1 PRS-RSRP reporting delay test case for single positioning frequency layer	3699

A.7.6.10.1.1	Test Purpose and Environment	3699

A.7.6.10.1.2	Test Requirements	3703

A.7.6.10.2	PRS-RSRP reporting delay test case for dual positioning frequency layer	3703

A.7.6.10.2.1	Test Purpose and Environment	3703

A.7.6.10.2.2	Test Requirements	3707

A.7.6.10.3	PRS-RSRP reporting delay test case for reduced number of samples	3707

A.7.6.10.3.1	Test Purpose and Environment	3707

A.7.6.10.3.2	Test Requirements	3712

A.7.6.10.4	PRS-RSRP reporting delay test case for single positioning frequency layer outside MG	3712

A.7.6.10.4.1	Test Purpose and Environment	3712

A.7.6.10.4.2	Test Requirements	3717

A.7.6.11	UE Rx-Tx time difference measurements	3717

A.7.6.11.1	UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA	3717

A.7.6.11.1.1	Test purpose and environment	3717

A.7.6.11.1.2	Test requirements	3721

A.7.6.11.2	UE Rx-Tx time difference measurement period for dual positioning frequency layers in FR2 SA	3721

A.7.6.11.2.1	Test purpose and environment	3721

A.7.6.11.2.2	Test requirements	3725

A.7.6.11.3	UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA with reduced sample number	3725

A.7.6.11.3.1	Test purpose and environment	3725

A.7.6.11.3.2	Test requirements	3727

A.7.6.11.4	UE Rx-Tx time difference measurements without gaps in FR2 SA	3728

A.7.6.11.4.1	Test purpose and environment	3728

A.7.6.11.4.2	Test requirements	3730

A.7.6.11.5	UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA with RxTx TEG	3731

A.7.6.11.5.1	Test purpose and environment	3731

A.7.6.11.5.2	Test requirements	3733

A.7.6.12	PRS-RSRPP measurements	3734

A.7.6.12.1 PRS-RSRPP reporting delay test case for single positioning frequency layer in FR2 in RRC\_CONNECTED state	3734

A.7.6.12.1.1	Test Purpose and Environment	3734

A.7.6.12.1.2	Test Requirements	3737

A.7.6.12.2	PRS-RSRPP reporting delay test case for reduced number of samples for single positioning frequency layer in FR2 in RRC\_CONNECTED state	3737

A.7.6.12.2.1	Test Purpose and Environment	3737

A.7.6.12.2.2	Test Requirements	3740

A.7.6.12.3	PRS-RSRPP reporting delay test case for gapless measurement in FR2	3740

A.7.6.12.3.1	Test Purpose and Environment	3740

A.7.6.12.3.2	Test Requirements	3743

A.7.6.13	UE Rx-Tx time difference measurements for PDC	3744

A.7.6.13.1	UE Rx-Tx time difference measurement for propagation delay compensation using PRS in FR2	3744

A.7.6.13.1.1	Test purpose and environment	3744

A.7.6.13.1.2	Test requirements	3745

A.7.6.13.2	UE Rx-Tx time difference measurement for propagation delay compensation using TRS in FR2	3746

A.7.6.13.2.1	Test purpose and environment	3746

A.7.6.13.2.2	Test requirements	3747

A.7.6.14	SA event triggered reporting tests with Pre-MG	3748

A.7.6.14.1	Intra-frequency measurement test with SA event triggered reporting tests: with autonomous activation/deactivation of Pre-MG in FR2	3748

A.7.6.14.1.1	Test purpose and Environment	3748

A.7.6.14.1.2	Test parameters	3748

A.7.6.14.1.3	Test Requirements	3751

A.7.6.14.2	Intra-frequency measurement test with SA event triggered reporting tests: with network-controlled activation/deactivation of Pre-MG in FR2	3751

A.7.6.14.2.1	Test purpose and Environment	3751

A.7.6.14.2.2	Test parameters	3751

A.7.6.14.2.3	Test Requirements	3754

A.7.6.15	SA event triggered reporting tests with concurrent gaps	3754

A.7.6.15.1	SA event triggered reporting tests For FR2 with fully non-overlapping concurrent MGs for SSB-based inter-frequency measurements	3754

A.7.6.15.1.1	Test Purpose and Environment	3754

A.7.6.15.1.2	Test Requirements	3757

A.7.6.15.2	SA event triggered reporting tests For FR2 with concurrent measurement gaps without SSB time index detection when DRX is not used (PCell in FR2)	3757

A.7.6.15.2.1	Test Purpose and Environment	3757

A.7.6.15.2.2	Test Requirements	3760

A.7.6.15.3	SA event triggered reporting tests for FR2 concurrent gap with partially partial overlapping scenario for SSB-based measurements and PRS-based measurement	3760

A.7.6.15.3.1	Test Purpose and Environment	3760

A.7.6.15.3.2	Test Requirements	3764

A.7.6.16	SA event triggered reporting tests with NCSG	3764

A.7.6.16.1	SA event triggered reporting test with per-UE NCSG under non-DRX	3764

A.7.6.16.1.1	Test purpose and Environment	3764

A.7.6.16.1.2	Test Requirements	3768

A.7.6.16.2	SA event triggered reporting tests on inter-frequency measurement with NCSG for FR2 when DRX is not used (PCell in FR2)	3768

A.7.6.16.2.1	Test Purpose and Environment	3768

A.7.6.16.2.2	Test Requirements	3771

A.7.6.16.3	Event triggered reporting test on deactivated Scell measurement via NCSG in FR2 in non-DRX	3771

A.7.6.16.3.1	Test Purpose and Environment	3771

A.7.6.16.3.2	Test Requirements	3774

A.7.7	Measurement Performance requirements	3774

A.7.7.1	SS-RSRP	3775

A.7.7.1.1	SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	3775

A.7.7.1.1.1	Test Purpose and Environment	3775

A.7.7.1.1.2	Test parameters	3775

A.7.7.1.1.3	Test Requirements	3779

A.7.7.1.2	SA inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	3780

A.7.7.1.2.1	Test Purpose and Environment	3780

A.7.7.1.2.2	Test parameters	3780

A.7.7.1.2.3	Test Requirements	3784

A.7.7.1.3	SA inter-frequency measurement accuracy with FR1 serving cell and FR2 target cell	3785

A.7.7.1.3.1	Test Purpose and Environment	3785

A.7.7.1.3.2	Test parameters	3785

A.7.7.1.3.3	Test Requirements	3789

A.7.7.2	SS-RSRQ	3789

A.7.7.2.1	SA intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell	3789

A.7.7.2.1.1	Test Purpose and Environment	3789

A.7.7.2.1.2	Test Parameters	3789

A.7.7.2.1.3	Test Requirements	3791

A.7.7.2.2	SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	3791

A.7.7.2.2.1	Test Purpose and Environment	3791

A.7.7.2.2.2	Test Parameters	3791

A.7.7.2.2.3	Test Requirements	3793

A.7.7.3	SS-SINR	3793

A.7.7.3.1	SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	3793

A.7.7.3.1.1	Test Purpose and Environment	3793

A.7.7.3.1.2	Test Parameters	3793

A.7.7.3.1.3	Test Requirements	3795

A.7.7.3.2	SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	3795

A.7.7.3.2.1	Test Purpose and Environment	3795

A.7.7.3.2.2	Test Parameters	3795

A.7.7.3.2.3	Test Requirements	3797

A.7.7.4	L1-RSRP measurement for beam reporting	3797

A.7.7.4.1	SSB based L1-RSRP measurement	3797

A.7.7.4.1.1	Test Purpose and Environment	3797

A.7.7.4.1.2	Test parameters	3798

A.7.7.4.1.3	Test Requirements	3800

A.7.7.4.2	CSI-RS based L1-RSRP measurement on resource set with repetition off	3801

A.7.7.4.2.1	Test Purpose and Environment	3801

A.7.7.4.2.2	Test parameters	3801

A.7.7.4.2.3	Test Requirements	3803

A.7.7.5	CLI measurements	3804

A.7.7.5.1	SA SRS-RSRP measurement accuracy with FR2 serving cell	3804

A.7.7.5.1.1	Test Purpose and Environment	3804

A.7.7.5.1.2	Test parameters	3804

A.7.7.5.1.3	Test Requirements	3807

A.7.7.5.2	SA CLI-RSSI measurement accuracy with FR2 serving cell	3808

A.7.7.5.2.1	Test Purpose and Environment	3808

A.7.7.5.2.2	Test parameters	3808

A.7.7.5.2.3	Test Requirements	3810

A.7.7.6	L1-SINR measurement for beam reporting	3811

A.7.7.6.1.1	Test Purpose and Environment	3811

A.7.7.6.1.2	Test parameters	3811

A.7.7.6.1.3	Test Requirements	3813

A.7.7.6.2	L1-SINR measurement with SSB based CMR and dedicated IMR	3814

A.7.7.6.2.1	Test Purpose and Environment	3814

A.7.7.6.2.2	Test parameters	3814

A.7.7.6.2.3	Test Requirements	3816

A.7.7.6.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR	3817

A.7.7.6.3.1	Test Purpose and Environment	3817

A.7.7.6.3.2	Test parameters	3817

A.7.7.6.3.3	Test Requirements	3819

A.7.7.7	CSI-RSRP	3820

A.7.7.7.1	SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	3820

A.7.7.7.1.1	Test Purpose and Environment	3820

A.7.7.7.1.2	Test parameters	3820

A.7.7.7.1.3	Test Requirements	3825

A.7.7.7.2	SA inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	3825

A.7.7.7.2.1	Test Purpose and Environment	3825

A.7.7.7.2.2	Test parameters	3826

A.7.7.7.2.3	Test Requirements	3830

A.7.7.8	CSI-RSRQ	3831

A.7.7.8.1	SA intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell	3831

A.7.7.8.1.1	Test Purpose and Environment	3831

A.7.7.8.1.2	Test Parameters	3831

A.7.7.8.1.3	Test Requirements	3833

A.7.7.8.2	SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	3833

A.7.7.8.2.1	Test Purpose and Environment	3833

A.7.7.8.2.2	Test Parameters	3834

A.7.7.8.2.3	Test Requirements	3835

A.7.7.9	CSI-SINR	3835

A.7.7.9.1	SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	3835

A.7.7.9.1.1	Test Purpose and Environment	3835

A.7.7.9.1.2	Test Parameters	3836

A.7.7.9.1.3	Test Requirements	3838

A.7.7.9.2	SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	3839

A.7.7.9.2.1	Test Purpose and Environment	3839

A.7.7.9.2.2	Test Parameters	3839

A.7.7.9.2.3	Test Requirements	3841

A.7.7.10	RSTD measurements	3842

A.7.7.10.1	RSTD measurement accuracy test case for single positioning frequency layer	3842

A.7.7.10.1.1	Test purpose and Environment	3842

A.7.7.10.1.2	Test Requirements	3844

A.7.7.10.2	RSTD measurement accuracy test case for dual positioning frequency layer	3844

A.7.7.10.2.1	Test purpose and Environment	3844

A.7.7.10.2.2	Test Requirements	3848

A.7.7.10.3	RSTD measurement accuracy test case with reduced number of samples for single positioning frequency layer in FR2 in RRC\_CONNECTED state	3849

A.7.7.10.3.1	Test purpose and Environment	3849

A.7.7.10.3.2	Test Requirements	3850

A.7.7.10.4	RSTD measurement accuracy test case with Rx TEG	3851

A.7.7.10.4.1	Test purpose and Environment	3851

A.7.7.10.4.2	Test Requirements	3853

A.7.7.11	PRS-RSRP measurements	3853

A.7.7.11.1	SA measurement accuracy with PRS in FR2	3853

A.7.7.11.1.1	Test Purpose and Environment	3853

A.7.7.11.1.2	Test parameters	3853

A.7.7.11.1.3	Test Requirements	3857

A.7.7.11.2	SA measurement accuracy with PRS in FR2 with reduced sample number	3858

A.7.7.11.2.1	Test Purpose and Environment	3858

A.7.7.11.2.2	Test parameters	3858

A.7.7.11.2.3	Test Requirements	3860

A.7.7.12	UE Rx-Tx time difference measurements	3861

A.7.7.12.1	UE Rx-Tx time difference measurement accuracy for single positioning frequency layer in FR2 SA	3861

A.7.7.12.1.1	Test purpose and environment	3861

A.7.7.12.1.2	Test parameters	3861

A.7.7.12.1.3	Test requirements	3864

A.7.7.12.2	UE Rx-Tx time difference measurement accuracy with reduced number of samples in FR2 SA	3865

A.7.7.12.2.1	Test purpose and environment	3865

A.7.7.12.2.2	Test parameters	3865

A.7.7.12.2.3	Test requirements	3868

A.7.7.12.3	UE Rx-Tx time difference measurement accuracy with RxTx TEG	3868

A.7.7.12.3.1	Test purpose and environment	3868

A.7.7.12.3.2	Test parameters	3868

A.7.7.12.3.3	Test requirements	3871

A.7.7.13	PRS-RSRPP measurements	3871

A.7.7.13.1	SA measurement accuracy with PRS in FR2	3871

A.7.7.13.1.1	Test Purpose and Environment	3871

A.7.7.13.1.2	Test parameters	3872

A.7.7.13.1.3	Test Requirements	3874

A.7.7.13.2	SA measurement accuracy with reduced PRS samples in FR2	3875

A.7.7.13.2.1	Test Purpose and Environment	3875

A.7.7.13.2.2	Test parameters	3875

A.7.7.13.2.3	Test Requirements	3877

A.7.8	Measurement procedure in RRC\_INACTIVE	3878

A.7.8.1	RSTD measurements	3878

A.7.8.1.1	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC\_INACTIVE state	3878

A.7.8.1.1.1	Test Purpose and Environment	3878

A.7.8.1.1.2	Test Requirements	3881

A.7.8.1.2	NR RSTD measurement reporting delay test case with reduced number of samples in RRC\_INACTIVE, FR1 SA	3881

A.7.8.1.2.1	Test Purpose and Environment	3881

A.7.8.1.2.2	Test Requirements	3887

A.7.8.2	PRS-RSRP measurements	3888

A.7.8.2.1	PRS-RSRP reporting delay test case for single positioning frequency layer in RRC\_INACTIVE	3888

A.7.8.2.1.1	Test Purpose and Environment	3888

A.7.8.2.1.2	Test Requirements	3892

A.7.8.2.2	PRS-RSRP reporting delay test case with reduced number of samples in RRC\_INACTIVE	3892

A.7.8.2.2.1	Test purpose and Environment	3892

A.7.8.2.2.2	Test Requirements	3896

A.7.8.3	UE Rx-Tx time difference measurements	3896

A.7.8.3.1	UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA	3896

A.7.8.3.1.1	Test purpose and environment	3896

A.7.8.3.1.2	Test requirements	3900

A.7.8.3.2	UE Rx-Tx time difference measurement with reduced number of samples in RRC\_INACTIVE, FR2 SA	3900

A.7.8.3.2.1	Test purpose and environment	3900

A.7.8.3.2.2	Test requirements	3902

A.7.8.4	PRS-RSRPP measurements	3903

A.7.8.4.1	PRS-RSRPP reporting delay test case for single positioning frequency layer in FR2 in RRC\_INACTIVE state	3903

A.7.8.4.1.1	Test Purpose and Environment	3903

A.7.8.4.1.2	Test Requirements	3905

A.7.8.4.2	PRS-RSRPP reporting delay test with reduced number of samples for single positioning frequency layer in FR2 in RRC\_INACTIVE state	3906

A.7.8.4.2.1	Test Purpose and Environment	3906

A.7.8.4.2.2	Test Requirements	3908

A.7.9	Measurement performance requirements in RRC\_INACTIVE	3909

A.7.9.1	RSTD measurements	3909

A.7.9.1.1	RSTD measurement accuracy test case for single positioning frequency layer in FR2 in RRC\_INACTIVE state	3909

A.7.9.1.1.1	Test purpose and Environment	3909

A.7.9.1.1.2	Test Requirements	3911

A.7.9.1.2	RSTD measurement accuracy test case with reduced number of samples for single positioning frequency layer in FR2 in RRC\_INACTIVE state	3911

A.7.9.1.2.1	Test purpose and Environment	3911

A.7.9.1.2.2	Test Requirements	3913

A.7.9.2	PRS-RSRP measurements	3913

A.7.9.2.1	SA measurement accuracy with PRS in FR2 in RRC\_INACTIVE	3913

A.7.9.2.1.1	Test Purpose and Environment	3913

A.7.9.2.1.2	Test parameters	3913

A.7.9.2.1.3	Test Requirements	3915

A.7.9.2.2	PRS-RSRP measurements with reduced number of sample in RRC\_INACTIVE	3916

A.7.9.2.2.1	Test Purpose and Environment	3916

A.7.9.2.2.2	Test parameters	3916

A.7.9.2.2.3	Test Requirements	3918

A.7.9.3	UE Rx-Tx time difference measurements	3919

A.7.9.3.1	UE Rx-Tx time difference measurements in RRC\_INACTIVE	3919

A.7.9.3.1.1	Test purpose and environment	3919

A.7.9.3.1.2	Test parameters	3919

A.7.9.3.1.3	Test requirements	3922

A.7.9.3.2	UE Rx-Tx time difference measurement accuracy with reduced number of samples in FR2 SA	3922

A.7.9.3.2.1	Test purpose and environment	3922

A.7.9.3.2.2	Test parameters	3922

A.7.9.3.2.3	Test requirements	3925

A.7.9.4	PRS-RSRPP measurements	3925

A.7.9.4.1	SA measurement accuracy in FR2 in RRC INACTIVE	3925

A.7.9.4.1.1	Test Purpose and Environment	3925

A.7.9.4.1.2	Test parameters	3925

A.7.9.4.1.3	Test Requirements	3927

A.7.9.4.2	SA measurement accuracy with reduced PRS samples in FR2 in RRC INACTIVE	3928

A.7.9.4.2.1	Test Purpose and Environment	3928

A.7.9.4.2.2	Test parameters	3928

A.7.9.4.2.3	Test Requirements	3930

A.8	E-UTRA standalone tests for NR RRM	3928

A.8.1	Void	3928

A.8.2	RRC\_IDLE state mobility	3928

A.8.2.1	Inter-RAT NR Cell re-selection	3928

A.8.2.1.1	E-UTRA Cell reselection to higher priority NR target Cell in FR1	3928

A.8.2.1.1.1	Test Purpose and Environment	3928

A.8.2.1.1.2	Test Requirements	3933

A.8.2.1.2	E-UTRA Cell reselection to lower priority NR target Cell in FR1 for UE configured with highSpeedInterRAT-NR-r16	3934

A.8.2.1.2.1	Test Purpose and Environment	3934

A.8.2.1.2.2	Test Requirements	3938

A.8.2.2	E-UTRA – NR Inter-RAT Early Measruement Reporting	3939

A.8.2.2.1	E-UTRA – NR Early Measurement Reporting for NR in FR1	3939

A.8.2.2.1.1	Test Purpose and Environment	3939

A.8.2.2.1.2	Test Requirements	3943

A.8.2.2.2	E-UTRA – NR Early Measurement Reporting for NR in FR2	3943

A.8.2.2.2.1	Test Purpose and Environment	3943

A.8.2.2.2.2	Test Requirements	3946

A.8.3	RRC\_CONNECTED state mobility	3947

A.8.3.1	Handover	3947

A.8.3.1.1	E-UTRAN - NR handover in FR1	3947

A.8.3.1.1.1	Test Purpose and Environment	3947

A.8.3.1.1.2	Test Requirements	3952

A.8.4	Measurement procedure	3952

A.8.4.1	E-UTRA – NR Inter-RAT SFTD Measurement Delay	3952

A.8.4.1.1	E-UTRA – NR Inter-RAT SFTD Measurement Delay in non-DRX	3952

A.8.4.1.1.1	Test Purpose and Environment	3952

A.8.4.1.1.2	Test Requirements	3954

A.8.4.1.2	E-UTRA – NR Inter-RAT SFTD Measurement Delay in DRX	3955

A.8.4.1.2.1	Test Purpose and Environment	3955

A.8.4.1.2.2	Test Requirements	3956

A.8.4.2	E-UTRA – NR Inter-RAT Measurements	3956

A.8.4.2.1	NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used	3956

A.8.4.2.1.1	Test Purpose and Environment	3956

A.8.4.2.1.2	Test Requirements	3961

A.8.4.2.2	NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used	3961

A.8.4.2.2.1	Test Purpose and Environment	3961

A.8.4.2.2.2	Test Requirements	3965

A.8.4.2.3	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used	3965

A.8.4.2.3.1	Test Purpose and Environment	3965

A.8.4.2.3.2	Test Requirements	3969

A.8.4.2.4	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used	3969

A.8.4.2.4.1	Test Purpose and Environment	3969

A.8.4.2.4.2	Test Requirements	3973

A.8.4.2.5	NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is not used	3973

A.8.4.2.5.1	Test Purpose and Environment	3973

A.8.4.2.5.2	Test Requirements	3975

A.8.4.2.6	NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is used	3976

A.8.4.2.6.1	Test Purpose and Environment	3976

A.8.4.2.6.2	Test Requirements	3978

A.8.4.2.7	NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is not used	3979

A.8.4.2.7.1	Test Purpose and Environment	3979

A.8.4.2.7.2	Test Requirements	3981

A.8.4.2.8	NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is used	3982

A.8.4.2.8.1	Test Purpose and Environment	3982

A.8.4.2.8.2	Test Requirements	3984

A.8.4.2.9	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection in DRX for UE configured with highSpeedInterRAT-NR-r16	3985

A.8.4.2.9.1	Test Purpose and Environment	3985

A.8.4.2.9.2	Test Requirements	3990

A.8.5	Measurement performance	3990

A.8.5.1	SFTD accuracy	3990

A.8.5.1.1	SFTD accuracy	3990

A.8.5.1.1.1	Test Purpose	3990

A.8.5.1.1.2	Test Environment	3990

A.8.5.1.1.3	Test Requirements	3996

A.8.5.2	E-UTRA – NR Inter-RAT Measurement Performance requirements	3996

A.8.5.2.1.1	E-UTRAN – NR inter-RAT measurements with FR1 target cell	3996

A.8.5.2.1.2	E-UTRAN – NR inter-RAT measurements with FR2 target cell	4001

A.8.5.2.1.2.1	Test Purpose and Environment	4001

A.8.5.2.1.2.2	Test Parameters	4001

A.8.5.2.1.2.3	Test Requirements	4003

A.8.5.2.2	SS-RSRQ	4003

A.8.5.2.2.1	E-UTRAN – NR inter-RAT measurements with FR1 target cell	4003

A.8.5.2.2.2	E-UTRAN – NR inter-RAT measurements with FR2 target cell	4008

A.8.5.2.2.2.1	Test Purpose and Environment	4008

A.8.5.2.2.2.2	Test Parameters	4008

A.8.5.2.2.2.3	Test Requirements	4010

A.8.5.2.3	SS-SINR	4010

A.8.5.2.3.1	E-UTRAN – NR inter-RAT measurements with FR1 target cell	4010

A.8.5.2.3.2	E-UTRAN – NR inter-RAT measurements with FR2 target cell	4014

A.8.5.2.3.2.1	Test Purpose and Environment	4014

A.8.5.2.3.2.2	Test Parameters	4014

A.8.5.2.3.2.3	Test Requirements	4016

A.9	V2X Tests	4017

A.9.1	V2X Tests in FR1	4017

A.9.1.1	Test for V2X UE Transmit Timing	4017

A.9.1.1.1 Test for GNSS as Synchronization Reference Source	4017

A.9.1.1.1.1	Test Purpose and Environment	4017

A.9.1.1.1.2	Test requirements	4017

A.9.1.1.2	Test for SyncRef UE as Synchronization Reference Source	4017

A.9.1.1.2.1	Test Purpose and Environment	4017

A.9.1.1.2.2	Test requirements	4018

A.9.1.1.3	Test for FR1 NR Cell as Synchronization Reference Source	4018

A.9.1.1.3.1	Test Purpose and Environment	4018

A.9.1.1.3.2	Test requirements	4021

A.9.1.2	Test for Initiation/Cease of S-SSB Transmission with V2X Sidelink Communication	4021

A.9.1.2.1	Test for FR1 NR Cell as synchronization reference source without gap under non-DRX	4021

A.9.1.2.1.1	Test Purpose and Environment	4021

A.9.1.2.1.2	Test Requirements	4024

A.9.1.2.2	Test for SyncRef UE as synchronization reference source	4024

A.9.1.2.2.1	Test Purpose and Environment	4024

A.9.1.2.2.2	Test Requirements	4026

A.9.1.2.3	Test for SyncRef UE as synchronization reference source when SL-DRX is used	4026

A.9.1.2.3.1	Test Purpose and Environment	4026

A.9.1.2.3.2	Test Requirements	4028

A.9.1.3	 Test for V2X Synchronization Reference Selection/Reselection	4028

A.9.1.3.1	 Test for GNSS configured as the highest priority	4028

A.9.1.3.1.1	Test Purpose and Environment	4028

A.9.1.3.1.2	Test Requirements	4030

A.9.1.3.2	 Test for FR1 NR Cell configured as the highest priority	4031

A.9.1.3.2.1	Test Purpose and Environment	4031

A.9.1.3.2.2	Test Requirements	4033

A.9.1.3.3	Test for GNSS configured as the highest priority under SL-DRX	4034

A.9.1.3.3.1	Test Purpose and Environment	4034

A.9.1.3.3.2	Test Requirements	4036

A.9.1.3.4	Test for FR1 NR Cell configured as the highest priority under SL-DRX	4037

A.9.1.3.4.1	Test Purpose and Environment	4037

A.9.1.3.4.2	Test Requirements	4039

A.9.1.4	Test for L1 SL-RSRP Measurement	4040

A.9.1.4.1	Test for V2X UE Autonomous Resource Selection/Reselection	4040

A.9.1.4.1.1	Test Purpose and Environment	4040

A.9.1.4.1.2	Test Requirements	4043

A.9.1.4.2	Test for V2X UE Resource Pre-emption	4043

A.9.1.4.2.1	Test Purpose and Environment	4043

A.9.1.4.2.2	Test Requirements	4047

A.9.1.4.3	 Test for V2X UE Resource Re-evaluation	4047

A.9.1.4.3.1	Test Purpose and Environment	4047

A.9.1.4.3.2	Test Requirements	4054

A.9.1.4.4	Test for V2X UE Autonomous Resource Selection/Reselection with Periodic Sensing	4054

A.9.1.4.4.1	Test Purpose and Environment	4054

A.9.1.4.4.2	Test Requirements	4058

A.9.1.4.5	Test for V2X UE Autonomous Resource Selection/Reselection with Contiguous Sensing	4058

A.9.1.4.5.1	Test Purpose and Environment	4058

A.9.1.4.5.2	Test Requirements	4061

A.9.1.4.6	Test for V2X UE Autonomous Resource Selection/Reselection in SL-DRX	4061

A.9.1.4.6.1	Test Purpose and Environment	4061

A.9.1.4.6.2	Test Requirements	4065

A.9.1.5	Test for Congestion Control Measurement	4065

A.9.1.5.1	Test Purpose and Environment	4065

A.9.1.5.2	Test Requirements	4071

A.9.1.6	Test for Interruption	4071

A.9.1.6.1	Test for Interruption to WAN due to V2X Sidelink Communication	4071

A.9.1.6.1.1	Test Purpose and Environment	4071

A.9.1.6.1.2	Test Requirements	4074

A.9.1.6.2	Test for interruption to WAN at transitions between active and non-active during SL-DRX in asynchronous case	4074

A.9.1.6.2.1	Test Purpose and Environment	4074

A.9.1.6.2.2	Test Requirements	4078

A.9.1.6.3	Test for Interruption at NR Sidelink Diccovery Configuration	4078

A.9.1.6.3.1	Test Purpose and Environment	4078

A.9.1.6.3.2	Test Requirements	4081

A.9.1.7	Selection / Reselection of relay UE	4081

A.9.1.7.1	Test Purpose and Environment	4081

A.9.1.7.2	Test Requirements	4087

A.10	EN-DC Tests with NR PSCell under CCA and Other NR Cells in FR1	4089

A.10.1	RRC\_CONNECTED state mobility	4089

A.10.1.1	RRC connection mobility control	4089

A.10.1.1.1	Random Access	4089

A.10.1.1.1.1	4-step RA type contention-based random access for NR PSCell with CCA	4089

A.10.1.1.1.1.1	Test Purpose and Environment	4089

A.10.1.1.1.1.2	Test Requirements	4092

A.10.1.1.1.1.2.1	Random Access Preamble Transmission	4092

A.10.1.1.1.1.2.2	Random Access Response Reception	4092

A.10.1.1.1.1.2.3	No Random Access Response Reception	4093

A.10.1.1.1.1.2.4	Receiving an UL grant for msg3 retransmission	4093

A.10.1.1.1.1.2.5	 Contention Resolution Timer expiry	4093

A.10.1.1.1.2	4-step RA type non-contention based random access for NR PSCell with CCA	4094

A.10.1.1.1.2.1	Test Purpose and Environment	4094

A.10.1.1.1.2.2	Test Requirements	4097

A.10.1.1.1.2.2.1	SSB-based Random Access Preamble Transmission	4097

A.10.1.1.1.2.2.2	Random Access Response Reception	4098

A.10.1.1.1.2.2.3	No Random Access Response Reception	4098

A.10.1.1.1.3	2-step RA type contention-based random access for NR PSCell with CCA	4098

A.10.1.1.1.3.1	Test Purpose and Environment	4098

A.10.1.1.1.3.2	Test Requirements	4102

A.10.1.1.1.3.2.1	MsgA Transmission	4102

A.10.1.1.1.3.2.2	MsgB Reception	4102

A.10.1.1.1.3.2.3	No MsgB Reception	4103

A.10.1.1.1.4	2-step RA type non-contention based random access for NR PSCell with CCA	4103

A.10.1.1.1.4.1	Test Purpose and Environment	4103

A.10.1.1.1.4.2	Test Requirements	4107

A.10.1.1.1.4.2.1	MsgA Transmission	4107

A.10.1.1.1.4.2.2	MsgB Reception	4108

A.10.1.1.1.4.2.3	No MsgB Reception	4108

A.10.1.2	Handover with PSCell from EN-DC to EN-DC with known target PSCell using CCA	4108

A.10.1.2.1	Test Purpose and Environment	4108

A.10.1.2.2	Test Requirements	4115

A.10.2	Timing	4116

A.10.2.1	UE transmit timing	4116

A.10.2.1.1	UE Transmit Timing Test with PSCell under DL CCA	4116

A.10.2.1.1.1	Test Purpose and environment	4116

A.10.2.1.1.2	Test requirements	4119

A.10.2.2	UE timing advance	4120

A.10.2.2.1	UE Timing Advance Adjustment Accuracy with PSCell under DL CCA	4120

A.10.2.2.1.1	Test Purpose and Environment	4120

A.10.2.2.1.2	Test Parameters	4120

A.10.2.2.1.3	Test Requirements	4124

A.10.3	Signalling characteristics	4124

A.10.3.1	Radio link monitoring	4124

A.10.3.1.1	Introduction	4124

A.10.3.1.2	Radio link monitoring out-of-sync test for PSCell configured with SSB-based RLM RS in non-DRX mode	4125

A.10.3.1.2.1	Test purpose and environment	4125

A.10.3.1.2.2	Test requirements	4129

A.10.3.1.3	Radio link monitoring in-sync test for PSCell configured with SSB-based RLM RS in non-DRX mode	4130

A.10.3.1.3.1	Test purpose and environment	4130

A.10.3.1.3.2	Test requirements	4135

A.10.3.1.4	Void	4135

A.10.3.1.4.1	Void	4135

A.10.3.1.4.2	Void	4135

A.10.3.1.5	Void	4135

A.10.3.1.5.1	Void	4135

A.10.3.1.5.2	Void	4135

A.10.3.2	Void	4135

A.10.3.3	SCell activation and deactivation delay	4135

A.10.3.3.1	SCell Activation and Deactivation of known NR SCell with NR PSCell and NR SCell under CCA, 160 ms SCell measurement cycle	4135

A.10.3.3.1.1	Test Purpose and Environment	4135

A.10.3.3.1.2	Test Requirements	4140

A.10.3.3.2	SCell Activation and Deactivation of known NR SCell with NR PSCell and NR SCell under CCA, 640 ms SCell measurement cycle	4140

A.10.3.3.2.1	Test Purpose and Environment	4140

A.10.3.3.2.2	Test Requirements	4141

A.10.3.3.3	SCell Activation and Deactivation of unknown NR SCell with NR PSCell and NR SCell under CCA	4141

A.10.3.3.3.1	Test Purpose and Environment	4141

A.10.3.3.3.2	Test Requirements	4142

A.10.3.4	Beam failure detection and link recovery procedures	4142

A.10.3.4.1	EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in non-DRX mode	4142

A.10.3.4.1.1	Test Purpose and Environment	4142

A.10.3.4.1.2	Test Requirements	4147

A.10.3.4.2	EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in DRX mode	4147

A.10.3.4.2.1	Test Purpose and Environment	4147

A.10.3.4.2.2	Test Requirements	4153

A.10.3.5	Active BWP switching	4153

A.10.3.5.1	UL active BWP switch delay with consistent UL LBT failure on PSCell subject to UL CCA in EN-DC	4153

A.10.3.5.1.2	Test Requirements	4158

A.10.3.5.2	DCI-based and Timer-based Active BWP Switch	4159

A.10.3.5.2.1	E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC	4159

A.10.3.5.2.2	E-UTRAN – NR PSCell FR1 DL active BWP switch with FR1 SCell in non-DRX in synchronous EN-DC	4162

A.10.3.5.3	RRC-based Active BWP Switch	4166

A.10.3.5.3.1	E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC	4166

A.10.3.6	PSCell addition and release delay	4170

A.10.3.6.1	Addition and Release Delay of known NR PSCell on the carrier under CCA	4170

A.10.3.6.1.1	Test purpose and environment	4170

A.10.3.6.1.2	Test Requirements	4175

A.10.3.7	Void	4176

A.10.4	Measurement procedure	4176

A.10.4.1	Intra-frequency measurements	4176

A.10.4.1.1	Event-triggered reporting tests on PSCC without gaps under non-DRX	4176

A.10.4.1.1.1	Test purpose and environment	4176

A.10.4.1.1.2	Test parameters	4176

A.10.4.1.1.3	Test Requirements	4179

A.10.4.1.2	Void	4179

A.10.4.1.3	Void	4179

A.10.4.1.4	Event-triggered reporting tests on PSCC with per-UE gaps under DRX	4179

A.10.4.1.4.1	Test purpose and environment	4179

A.10.4.1.4.2	Test parameters	4180

A.10.4.1.4.3	Test Requirements	4184

A.10.4.1.5	Void	4185

A.10.4.1.6	Void	4185

A.10.4.1.7	Void	4185

A.10.4.1.8	Void	4185

A.10.4.1.9	Void	4185

A.10.4.1.10	Void	4185

A.10.4.1.11	Void	4185

A.10.4.1.12	Void	4185

A.10.4.2	Inter-frequency measurements	4185

A.10.4.2.1	Void	4185

A.10.4.2.2	Void	4185

A.10.4.2.3	EN-DC event triggered reporting tests for FR1 with CCA cell without SSB time index detection when DRX is not used	4185

A.10.4.2.3.1	Test Purpose and Environment	4185

A.10.4.2.3.2	Test Requirements	4189

A.10.4.2.4	EN-DC event triggered reporting tests for FR1 cell with CCA without SSB time index detection when DRX is used	4190

A.10.4.2.4.1	Test Purpose and Environment	4190

A.10.4.2.4.2	Test Requirements	4195

A.10.4.2.5	EN-DC event triggered reporting tests for FR1 cell with CCA with SSB time index detection when DRX is not used	4195

A.10.4.2.5.1	Test Purpose and Environment	4195

A.10.4.2.5.2	Test Requirements	4199

A.10.4.2.6	EN-DC event triggered reporting tests for FR1 cell with CCA with SSB time index detection when DRX is used	4200

A.10.4.2.6.1	Test Purpose and Environment	4200

A.10.4.2.6.2	Test Requirements	4205

A.10.4.2.7	EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is not used	4205

A.10.4.2.7.1	Test Purpose and Environment	4205

A.10.4.2.7.2	Test Requirements	4211

A.10.4.2.8	EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used	4211

A.10.4.2.8.1	Test Purpose and Environment	4211

A.10.4.2.8.2	Test Requirements	4217

A.10.4.2.9	EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is not used	4217

A.10.4.2.9.1	Test Purpose and Environment	4217

A.10.4.2.9.2	Test Requirements	4223

A.10.4.2.10	EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is used	4223

A.10.4.2.10.1	Test Purpose and Environment	4223

A.10.4.2.10.2	Test Requirements	4229

A.10.4.3	L1-RSRP measurements for beam reporting	4230

A.10.4.3.1	SSB based L1-RSRP measurement on PSCC when DRX is not used	4230

A.10.4.3.1.1	Test Purpose and Environment	4230

A.10.4.3.1.2	Test parameters	4230

A.10.4.3.1.3	Test Requirements	4232

A.10.4.3.2	SSB based L1-RSRP measurement on PSCC when DRX is used	4233

A.10.4.3.2.1	Test Purpose and Environment	4233

A.10.4.3.2.2	Test parameters	4233

A.10.4.3.2.3	Test Requirements	4235

A.10.4.3.3	SSB based L1-RSRP measurement on SCC when DRX is not used	4236

A.10.4.3.3.1	Test Purpose and Environment	4236

A.10.4.3.3.2	Test parameters	4236

A.10.4.3.3.3	Test Requirements	4239

A.10.4.3.4	SSB based L1-RSRP measurement on SCC when DRX is used	4240

A.10.4.3.4.1	Test Purpose and Environment	4240

A.10.4.3.4.2	Test parameters	4240

A.10.4.3.4.3	Test Requirements	4243

A.10.4.4	E-UTRANNR inter-RAT measurements on NR carrier frequency under CCA	4244

A.10.4.4.1	E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used	4244

A.10.4.4.1.1	Test Purpose and Environment	4244

A.10.4.4.1.2	Test Requirements	4251

A.10.4.4.2	E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used	4251

A.10.4.4.2.1	Test Purpose and Environment	4251

A.10.4.4.2.2	Test Requirements	4258

A.10.4.4.3	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used	4258

A.10.4.4.3.1	Test Purpose and Environment	4258

A.10.4.4.3.2	Test Requirements	4266

A.10.4.4.4	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used	4266

A.10.4.4.4.1	Test Purpose and Environment	4266

A.10.4.4.4.2	Test Requirements	4274

A.10.5	Measurement performance	4274

A.10.5.1	SS-RSRP	4274

A.10.5.1.1	Intra-frequency measurement accuracy on a CCA serving cell	4274

A.10.5.1.1.1	Test Purpose and Environment	4274

A.10.5.1.1.2	Test parameters	4274

A.10.5.1.1.3	Test Requirements	4277

A.10.5.1.2	Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell	4277

A.10.5.1.2.1	Test Purpose and Environment	4277

A.10.5.1.2.2	Test parameters	4277

A.10.5.1.2.3	Test Requirements	4280

A.10.5.2	SS-RSRQ	4280

A.10.5.2.1	Intra-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell	4280

A.10.5.2.1.1	Test Purpose and Environment	4280

A.10.5.2.1.2	Test Parameters	4280

A.10.5.2.1.3	Test Requirements	4283

A.10.5.2.2	Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell	4283

A.10.5.2.2.1	Test Purpose and Environment	4283

A.10.5.2.2.2	Test Parameters	4283

A.10.5.2.2.3	Test Requirements	4286

A.10.5.3	SS-SINR	4286

A.10.5.3.1	Intra-frequency measurement accuracy on PSCC	4286

A.10.5.3.1.1	Test Purpose and Environment	4286

A.10.5.3.1.2	Test Parameters	4286

A.10.5.3.1.3	Test Requirements	4289

A.10.5.3.2	Inter-frequency measurement accuracy on PSCC	4289

A.10.5.3.2.1	Test Purpose and Environment	4289

A.10.5.3.2.2	Test Parameters	4289

A.10.5.3.2.3	Test Requirements	4292

A.10.5.3.3	Intra-frequency measurement accuracy on SCC	4292

A.10.5.3.3.1	Test Purpose and Environment	4292

A.10.5.3.3.2	Test Parameters	4292

A.10.5.3.3.3	Test Requirements	4295

A.10.5.4	L1-RSRP measurement for beam reporting with CCA serving cell	4295

A.10.5.4.1	SSB based L1-RSRP measurement	4295

A.10.5.4.1.1	Test Purpose and Environment	4295

A.10.5.4.1.2	Test parameters	4296

A.10.5.4.1.3	Test Requirements	4298

A.10.5.5	RSSI	4298

A.10.5.5.1 	RSSI measurement accuracy on PSCC with CCA	4298

A.10.5.5.1.1	Test Purpose and Environment	4298

A.10.5.5.1.2	Test parameters	4298

A.10.5.5.1.3	Test Requirements	4301

A.10.5.5.2 	RSSI measurement accuracy on SCC with CCA	4301

A.10.5.5.2.1	Test Purpose and Environment	4301

A.10.5.5.2.2	Test parameters	4301

A.10.5.5.2.3	Test Requirements	4304

A.10.5.5.3 	Inter-frequency RSSI measurement accuracy on a carrier with CCA	4304

A.10.5.5.3.1	Test Purpose and Environment	4304

A.10.5.5.3.2	Test parameters	4304

A.10.5.5.3.3	Test Requirements	4308

A.10.5.6	Channel occupancy	4308

A.10.5.6.1 	Channel occupancy measurement accuracy on PSCC with CCA	4308

A.10.5.6.1.1	Test Purpose and Environment	4308

A.10.5.6.1.2	Test parameters	4308

A.10.5.6.1.3	Test Requirements	4312

A.10.5.6.2 	Channel occupancy measurement accuracy on SCC with CCA	4312

A.10.5.6.2.1	Test Purpose and Environment	4312

A.10.5.6.2.2	Test parameters	4312

A.10.5.6.2.3	Test Requirements	4315

A.10.5.6.3 	Inter-frequency channel occupancy measurement accuracy on a carrier with CCA	4315

A.10.5.6.3.1	Test Purpose and Environment	4315

A.10.5.6.3.2	Test parameters	4315

A.10.5.6.3.3	Test Requirements	4319

A.11	NR Standalone Tests with NR PCell under CCA and Other NR Cells in FR1	4317

A.11.1	RRC\_IDLE state mobility	4317

A.11.1.1	Cell re-selection with both source and target NR carrier frequencies under CCA	4317

A.11.1.1.1	Cell reselection to FR1 intra-frequency NR cells when subject to CCA on the serving and target cell	4317

A.11.1.1.1.1	Test Purpose and Environment	4317

A.11.1.1.1.2	Test Parameters	4317

A.11.1.1.1.3	Test Requirements	4320

A.11.1.1.2	Cell reselection to FR1 inter-frequency NR case when subject to CCA on the serving and target cell	4320

A.11.1.1.2.1	Test Purpose and Environment	4320

A.11.1.1.2.2	Test Parameters	4320

A.11.1.1.2.3	Test Requirements	4324

A.11.1.2	Cell re-selection to NR with source NR carrier frequency under CCA	4324

A.11.1.2.1	Cell reselection to FR1 inter-frequency NR case when serving cell is subject to CCA	4324

A.11.1.2.1.1	Test Purpose and Environment	4324

A.11.1.2.1.2	Test Parameters	4325

A.11.1.2.1.3	Test Requirements	4330

A.11.1.3	Cell re-selection from NR carrier with target NR carrier frequency under CCA	4331

A.11.1.3.1	Cell reselection to FR1 inter-frequency NR case when target cell is subject to CCA	4331

A.11.1.3.1.1	Test Purpose and Environment	4331

A.11.1.3.1.2	Test Parameters	4331

A.11.1.3.1.3	Test Requirements	4337

A.11.1.4	Inter-RAT cell re-selection to E-UTRAN with source NR carrier frequency under CCA	4338

A.11.1.4.1	Cell reselection to higher priority E-UTRAN when serving cell is subject to CCA	4338

A.11.1.4.1.1	Test Purpose and Environment	4338

A.11.1.4.1.2	Test Parameters	4338

A.11.1.4.1.3	Test Requirements	4341

A.11.1.4.2	Cell reselection to lower priority E-UTRAN when serving cell is subject to CCA	4342

A.11.1.4.2.1	Test Purpose and Environment	4342

A.11.1.4.2.2	Test Requirements	4345

A.11.2	RRC\_CONNECTED state mobility	4346

A.11.2.1	Handover	4346

A.11.2.1.1	Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; known target cell	4346

A.11.2.1.1.1	Test Purpose and Environment	4346

A.11.2.1.1.2	Test Parameters	4346

A.11.2.1.1.3 Test Requirements	4349

A.11.2.1.2	Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; unknown target cell	4349

A.11.2.1.2.1	Test Purpose and Environment	4349

A.11.2.1.2.2	Test Parameters	4349

A.11.2.1.2.3	Test Requirements	4352

A.11.2.1.3	Inter-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; unknown target cell	4352

A.11.2.1.3.1	Test Purpose and Environment	4352

A.11.2.1.3.2	Test Parameters	4352

A.11.2.1.3.3 Test Requirements	4355

A.11.2.1.4	Inter-frequency handover from FR1 carrier under CCA to FR1; known target cell	4355

A.11.2.1.4.1	Test Purpose and Environment	4355

A.11.2.1.4.2	Test Parameters	4355

A.11.2.1.4.3 Test Requirements	4359

A.11.2.1.5	Inter-frequency handover from FR1 carrier under CCA to FR1; unknown target cell	4360

A.11.2.1.5.1	Test Purpose and Environment	4360

A.11.2.1.5.2	Test Parameters	4360

A.11.2.1.5.3 Test Requirements	4363

A.11.2.1.6	Inter-frequency handover from FR1 to FR1 carrier under CCA; unknown target cell	4364

A.11.2.1.6.1	Test Purpose and Environment	4364

A.11.2.1.6.2	Test Parameters	4364

A.11.2.1.6.3	Test Requirements	4368

A.11.2.1.7	 SA NR FR1 carrier under CCA - E-UTRAN handover with known target cell	4369

A.11.2.1.7.1	Test Purpose and Environment	4369

A.11.2.1.7.2	Test Requirements	4375

A.11.2.1.8	SA NR FR1 carrier under CCA - E-UTRAN handover with unknown target cell	4375

A.11.2.1.8.1	Test Purpose and Environment	4375

A.11.2.1.8.2	Test Requirements	4380

A.11.2.1.9	Handover with PSCell from NR SA to EN-DC with known target PSCell using CCA	4380

A.11.2.1.9.1	Test Purpose and Environment	4380

A.11.2.1.9.2	Test Requirements	4389

A.11.2.2	RRC connection mobility control	4390

A.11.2.2.1	RRC re-establishment	4390

A.11.2.2.1.1	Intra-frequency RRC Re-establishment with CCA in FR1	4390

A.11.2.2.1.2	Inter-frequency RRC Re-establishment with CCA in FR1	4393

A.11.2.2.1.4	Inter-frequency RRC Re-establishment from NR FR1 carrier without CCA to NR FR1 carrier under CCA	4400

A.11.2.2.2	Random Access	4406

A.11.2.2.2.1	4-step RA type contention-based random access for NR PCell with CCA	4406

A.11.2.2.2.1.1	Test Purpose and Environment	4406

A.11.2.2.2.1.2	Test Requirements	4409

A.11.2.2.2.1.2.1	Random Access Preamble Transmission	4409

A.11.2.2.2.1.2.2	Random Access Response Reception	4409

A.11.2.2.2.1.2.3	No Random Access Response Reception	4410

A.11.2.2.2.1.2.4	Receiving an UL grant for msg3 retransmission	4410

A.11.2.2.2.1.2.5	Reception of an Incorrect Message over Temporary C-RNTI	4410

A.11.2.2.2.1.2.6	Reception of a Correct Message over Temporary C-RNTI	4411

A.11.2.2.2.1.2.7	Contention Resolution Timer expiry	4411

A.11.2.2.2.2	4-step RA type non-contention based random access for NR PSCell with CCA	4411

A.11.2.2.2.2.1	Test Purpose and Environment	4411

A.11.2.2.2.2.2	Test Requirements	4414

A.11.2.2.2.2.2.1	SSB-based Random Access Preamble Transmission	4414

A.11.2.2.2.2.2.2	Random Access Response Reception	4415

A.11.2.2.2.2.2.3	No Random Access Response Reception	4415

A.11.2.2.2.3	2-step RA type contention-based random access for NR PCell with CCA	4415

A.11.2.2.2.3.1	Test Purpose and Environment	4415

A.11.2.2.2.3.2	Test Requirements	4419

A.11.2.2.2.3.2.1	MsgA Transmission	4419

A.11.2.2.2.3.2.2	MsgB Reception	4419

A.11.2.2.2.3.2.3	No MsgB Reception	4420

A.11.2.2.2.4	2-step RA type non-contention-based random access for NR PCell with CCA	4420

A.11.2.2.2.4.1	Test Purpose and Environment	4420

A.11.2.2.2.4.2	Test Requirements	4424

A.11.2.2.2.4.2.1	MsgA Transmission	4424

A.11.2.2.2.4.2.2	MsgB Reception	4425

A.11.2.2.2.4.2.3	No MsgB Reception	4425

A.11.2.2.3	RRC connection release with redirection	4426

A.11.2.2.3.1	Redirection from NR FR1 carrier under CCA to NR FR1 carrier under CCA	4426

A.11.2.2.3.2	Redirection from NR FR1 carrier without CCA to NR FR1 carrier with CCA	4430

A.11.3	Timing	4435

A.11.3.1	UE transmit timing	4435

A.11.3.1.1	UE Transmit Timing Test with PCell under DL CCA	4435

A.11.3.1.1.1	Test Purpose and environment	4435

A.11.3.1.1.2	Test requirements	4438

A.11.3.2	UE timing advance	4439

A.11.3.2.1	UE Timing Advance Adjustment Accuracy with PCell under DL CCA	4439

A.11.3.2.1.1	Test Purpose and Environment	4439

A.11.3.2.1.2	Test Parameters	4439

A.11.3.2.1.3	Test Requirements	4443

A.11.4	Signalling characteristics	4443

A.11.4.1	Radio link monitoring	4443

A.11.4.1.1	Introduction	4443

A.11.4.1.2	Radio link monitoring out-of-sync test for PCell configured with SSB-based RLM RS in non-DRX mode	4444

A.11.4.1.2.1	Test purpose and environment	4444

A.11.4.1.2.2	Test requirements	4448

A.11.4.1.3	Radio link monitoring in-sync test for PCell configured with SSB-based RLM RS in non-DRX mode	4448

A.11.4.1.3.1	Test purpose and environment	4448

A.11.4.1.3.2	Test requirements	4454

A.11.4.1.4	Void	4455

A.11.4.1.4.1	Void	4455

A.11.4.1.4.2	Void	4455

A.11.4.1.5	Void	4455

A.11.4.1.5.1	Void	4455

A.11.4.1.5.2	Void	4455

A.11.4.2	Void	4455

A.11.4.3	SCell activation and deactivation delay	4455

A.11.4.3.1	SCell Activation and Deactivation of known SCell with PCell and SCell under CCA, 160 ms SCell measurement cycle	4455

A.11.4.3.1.1	Test Purpose and Environment	4455

A.11.4.3.1.2	Test Requirements	4459

A.11.4.3.2	SCell Activation and Deactivation of known SCell with PCell and SCell under CCA, 640 ms SCell measurement cycle	4459

A.11.4.3.2.1	Test Purpose and Environment	4459

A.11.4.3.2.2	Test Requirements	4460

A.11.4.3.3	SCell Activation and Deactivation of unknown SCell with PCell and SCell under CCA	4460

A.11.4.3.3.1	Test Purpose and Environment	4460

A.11.4.3.3.2	Test Requirements	4461

A.11.4.4	Beam failure detection and link recovery procedures	4461

A.11.4.4.1	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode	4461

A.11.4.4.1.1	Test Purpose and Environment	4461

A.11.4.4.1.2	Test Requirements	4466

A.11.4.4.2	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode	4466

A.11.4.4.2.1	Test Purpose and Environment	4466

A.11.4.4.2.2	Test Requirements	4472

A.11.4.5	Active BWP switching	4472

A.11.4.5.1	UL active BWP switch delay with consistent UL LBT failure on PCell subject to UL CCA	4472

A.11.4.5.1.1	Test Purpose and Environment	4472

A.11.4.5.1.2	Test Requirements	4476

A.11.4.5.2	DCI-based and Timer-based Active BWP Switch	4477

A.11.4.5.2.1	NR FR1- NR FR1 DL active BWP switch of PCell with non-DRX in SA	4477

A.11.4.5.2.2	NR FR1 DL active BWP switch with non-DRX in SA	4480

A.11.4.5.3	RRC-based Active BWP Switch	4483

A.11.4.5.3.1	NR FR1 DL active BWP switch of Cell with non-DRX in SA	4483

A.11.4.6	Void	4486

A.11.5	Measurement procedure	4486

A.11.5.1	Intra-frequency measurements	4486

A.11.5.1.1	Event-triggered reporting tests on PCC without gaps under non-DRX	4486

A.11.5.1.1.1	Test purpose and environment	4486

A.11.5.1.1.2	Test parameters	4486

A.11.5.1.1.3	Test Requirements	4490

A.11.5.1.2	Event-triggered reporting tests on PCC without gaps under DRX	4490

A.11.5.1.2.1	Test purpose and environment	4490

A.11.5.1.2.2	Test parameters	4490

A.11.5.1.2.3	Test Requirements	4493

A.11.5.1.3	Void	4494

A.11.5.1.4	Void	4494

A.11.5.1.5	Void	4494

A.11.5.1.6	Void	4494

A.11.5.1.7	Void	4494

A.11.5.1.8	Void	4494

A.11.5.1.9	Void	4494

A.11.5.1.10	Void	4494

A.11.5.1.11	Void	4494

A.11.5.1.12	Void	4494

A.11.5.2	Inter-frequency measurements	4494

A.11.5.2.1	Void	4494

A.11.5.2.2	Void	4494

A.11.5.2.3	Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is not used	4494

A.11.5.2.3.1	Test Purpose and Environment	4494

A.11.5.2.3.2	Test Requirements	4498

A.11.5.2.4	Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is used	4499

A.11.5.2.4.1	Test Purpose and Environment	4499

A.11.5.2.4.2	Test Requirements	4504

A.11.5.2.5	Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is not used	4504

A.11.5.2.5.1	Test Purpose and Environment	4504

A.11.5.2.5.2	Test Requirements	4508

A.11.5.2.6	Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is used	4509

A.11.5.2.6.1	Test Purpose and Environment	4509

A.11.5.2.6.2	Test Requirements	4514

A.11.5.2.7	Event triggered reporting tests for FR1 without SSB time index detection when DRX is not used	4514

A.11.5.2.7.1	Test Purpose and Environment	4514

A.11.5.2.7.2	Test Requirements	4518

A.11.5.2.8	Event triggered reporting tests for FR1 without SSB time index detection when DRX is used	4519

A.11.5.2.8.1	Test Purpose and Environment	4519

A.11.5.2.8.2	Test Requirements	4524

A.11.5.2.9	Event triggered reporting tests for FR1 with SSB time index detection when DRX is not used	4524

A.11.5.2.9.1	Test Purpose and Environment	4524

A.11.5.2.9.2	Test Requirements	4528

A.11.5.2.10	Event triggered reporting tests for FR1 with SSB time index detection when DRX is used	4529

A.11.5.2.10.1	Test Purpose and Environment	4529

A.11.5.2.10.2	Test Requirements	4534

A.11.5.3	Inter-RAT E-UTRAN measurements	4534

A.11.5.3.1	SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1	4534

A.11.5.3.1.1	Test Purpose and Environment	4534

A.11.5.3.1.2	Test Requirements	4540

A.11.5.3.2	SA NR - E-UTRAN event-triggered reporting in DRX in FR1	4540

A.11.5.3.2.1	Test Purpose and Environment	4540

A.11.5.3.2.2	Test Requirements	4546

A.11.5.4	L1-RSRP measurements for beam reporting	4546

A.11.5.4.1	SSB based L1-RSRP measurement when DRX is not used	4546

A.11.5.4.1.1	Test Purpose and Environment	4546

A.11.5.4.1.2	Test parameters	4546

A.11.5.4.1.3	Test Requirements	4548

A.11.5.4.2	SSB based L1-RSRP measurement when DRX is used	4548

A.11.5.4.2.1	Test Purpose and Environment	4548

A.11.5.4.2.2	Test parameters	4549

A.11.5.4.2.3	Test Requirements	4551

A.11.5.4.3	SSB based L1-RSRP measurement on SCC when DRX is not used	4551

A.11.5.4.3.1	Test Purpose and Environment	4551

A.11.5.4.3.2	Test parameters	4552

A.11.5.4.3.3	Test Requirements	4555

A.11.5.4.4	SSB based L1-RSRP measurement on SCC when DRX is used	4556

A.11.5.4.4.1	Test Purpose and Environment	4556

A.11.5.4.4.2	Test parameters	4556

A.11.5.4.4.3	Test Requirements	4559

A.11.6	Measurement performance	4560

A.11.6.1	SS-RSRP	4560

A.11.6.1.1	Intra-frequency measurement accuracy on a carrier frequency with CCA	4560

A.11.6.1.1.1	Test Purpose and Environment	4560

A.11.6.1.1.2	Test parameters	4560

A.11.6.1.1.3	Test Requirements	4562

A.11.6.1.2	Intra-frequency measurement accuracy on SCC on a carrier frequency with CCA	4562

A.11.6.1.2.1	Test Purpose and Environment	4562

A.11.6.1.2.2	Test parameters	4562

A.11.6.1.2.3	Test Requirements	4565

A.11.6.2	SS-RSRQ	4565

A.11.6.2.1	Intra-frequency measurement accuracy	4565

A.11.6.2.1.1	Test Purpose and Environment	4565

A.11.6.2.1.2	Test Parameters	4565

A.11.6.2.1.3	Test Requirements	4568

A.11.6.2.2	Inter-frequency measurement accuracy	4568

A.11.6.2.2.1	Test Purpose and Environment	4568

A.11.6.2.2.2	Test Parameters	4568

A.11.6.2.2.3	Test Requirements	4571

A.11.6.2.3	Intra-frequency measurement accuracy on SCC	4571

A.11.6.2.3.1	Test Purpose and Environment	4571

A.11.6.2.3.2	Test Parameters	4571

A.11.6.2.3.3	Test Requirements	4574

A.11.6.2.4	Inter-frequency measurement accuracy	4574

A.11.6.2.4.1	Test Purpose and Environment	4574

A.11.6.2.4.2	Test Parameters	4574

A.11.6.2.4.3	Test Requirements	4581

A.11.6.3	SS-SINR	4581

A.11.6.3.1	Intra-frequency measurement accuracy	4581

A.11.6.3.1.1	Test Purpose and Environment	4581

A.11.6.3.1.2	Test Parameters	4581

A.11.6.3.1.3	Test Requirements	4584

A.11.6.3.2	Inter-frequency measurement accuracy	4584

A.11.6.3.2.1	Test Purpose and Environment	4584

A.11.6.3.2.2	Test Parameters	4584

A.11.6.3.2.3	Test Requirements	4587

A.11.6.3.3	Intra-frequency measurement accuracy on SCC	4587

A.11.6.3.3.1	Test Purpose and Environment	4587

A.11.6.3.3.2	Test Parameters	4587

A.11.6.3.3.3	Test Requirements	4590

A.11.6.3.4	Inter-frequency measurement accuracy	4590

A.11.6.3.4.1	Test Purpose and Environment	4590

A.11.6.3.4.2	Test Parameters	4590

A.11.6.3.4.3	Test Requirements	4598

A.11.6.4	L1-RSRP measurement for beam reporting with CCA serving cell	4598

A.11.6.4.1	SSB based L1-RSRP measurement	4598

A.11.6.4.1.1	Test Purpose and Environment	4598

A.11.6.4.1.2	Test parameters	4599

A.11.6.4.1.3	Test Requirements	4602

A.11.6.5	RSSI	4602

A.11.6.5.1 	Intra-frequency RSSI measurement accuracy on PCC with CCA	4602

A.11.6.5.1.1	Test Purpose and Environment	4602

A.11.6.5.1.2	Test parameters	4602

A.11.6.5.1.3	Test Requirements	4605

A.11.6.5.2 	Intra-frequency RSSI measurement accuracy on SCC with CCA	4605

A.11.6.5.2.1	Test Purpose and Environment	4605

A.11.6.5.2.2	Test parameters	4605

A.11.6.5.2.3	Test Requirements	4608

A.11.6.5.3	Inter-frequency RSSI measurement accuracy on a carrier with CCA	4608

A.11.6.5.3.1	Test Purpose and Environment	4608

A.11.6.5.3.2	Test parameters	4608

A.11.6.5.3.3	Test Requirements	4612

A.11.6.6	Channel occupancy	4612

A.11.6.6.1	Intra-frequency channel occupancy measurement accuracy on PCC with CCA	4612

A.11.6.6.1.1	Test Purpose and Environment	4612

A.11.6.6.1.2	Test parameters	4612

A.11.6.6.1.3	Test Requirements	4616

A.11.6.6.2	Intra-frequency channel occupancy measurement accuracy on SCC with CCA	4616

A.11.6.6.2.1	Test Purpose and Environment	4616

A.11.6.6.2.2	Test parameters	4616

A.11.6.6.2.3	Test Requirements	4619

A.11.6.6.3	Inter-frequency channel occupancy measurement accuracy on a carrier with CCA	4619

A.11.6.6.3.1	Test Purpose and Environment	4619

A.11.6.6.3.2	Test parameters	4619

A.11.6.6.3.3	Test Requirements	4623

A.11.6.7	E-UTRAN RSRP	4624

A.11.6.8	E-UTRAN RSRQ	4624

A.11.6.9	E-UTRAN SINR	4624

A.12	E-UTRA Standalone Tests with at Least One NR Cell under CCA	4624

A.12.1	RRC\_IDLE state mobility	4624

A.12.1.1	Inter-RAT cell re-selection to NR on a carrier frequency with CCA	4624

A.12.1.1.1	E-UTRA Cell reselection to higher priority NR target Cell in FR1 when target cell is subject to CCA	4624

A.12.1.1.1.1	Test Purpose and Environment	4624

A.12.1.1.1.2	Test Requirements	4629

A.12.2	RRC\_CONNECTED state mobility	4630

A.12.2.1	Handover	4630

A.12.2.1.1	E-UTRAN - NR with CCA handover	4630

A.12.2.1.1.1	Test Purpose and Environment	4630

A.12.2.1.1.2	Test Requirements	4635

A.12.3	Void	4636

A.12.4	Measurement procedure	4636

A.12.4.1	E-UTRANNR inter-RAT SFTD measurements	4636

A.12.4.1.1	E-UTRA – NR Inter-RAT SFTD Measurement Delay with NR under CCA in non-DRX	4636

A.12.4.1.1.1	Test Purpose and Environment	4636

A.12.4.1.1.2	Test Requirements	4640

A.12.4.2	E-UTRANNR inter-RAT measurements on NR carrier frequency under CCA	4640

A.12.4.2.1	E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used	4640

A.12.4.2.1.1	Test Purpose and Environment	4640

A.12.4.2.1.2	Test Requirements	4646

A.12.4.2.2	E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used	4646

A.12.4.2.2.1	Test Purpose and Environment	4646

A.12.4.2.2.2	Test Requirements	4652

A.12.4.2.3	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used	4652

A.12.4.2.3.1	Test Purpose and Environment	4652

A.12.4.2.3.2	Test Requirements	4657

A.12.4.2.4	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used	4657

A.12.4.2.4.1	Test Purpose and Environment	4657

A.12.4.2.4.2	Test Requirements	4662

A.12.4.2.5	Void	4662

A.12.4.2.6	Void	4662

A.12.5	Measurement performance	4662

A.12.5.1	E-UTRANNR SFTD	4662

A.12.5.1.1	Inter-RAT SFTD accuracy with NR target cell under CCA	4662

A.12.5.1.1.1	Test Purpose	4662

A.12.5.1.1.2	Test Environment	4662

A.12.5.1.1.3	Test Requirements	4667

A.12.5.2	Void	4667

A.12.5.3	Void	4667

A.12.5.4	Void	4667

A.12.5.5	Void	4667

A.12.5.6	Void	4667

A.13	NR Standalone Tests with NR SCell under CCA and All Other NR Cells in FR1	4671

A.13.1	Void	4671

A.13.2	Signalling characteristics	4671

A.13.2.1	Void	4671

A.13.2.2	SCell activation and deactivation delay	4671

A.13.2.2.1	SCell Activation and Deactivation of known SCell under CCA, 160 ms SCell measurement cycle	4671

A.13.2.2.1.1	Test Purpose and Environment	4671

A.13.2.2.1.2	Test Requirements	4675

A.13.2.2.2 SCell Activation and Deactivation of known SCell under CCA, 640 ms SCell measurement cycle	4675

A.13.2.2.2.1	Test Purpose and Environment	4675

A.13.2.2.2.2	Test Requirements	4676

A.13.2.2.3	SCell Activation and Deactivation of unknown SCell under CCA	4676

A.13.2.2.3.1	Test Purpose and Environment	4676

A.13.2.2.3.2	Test Requirements	4677

A.13.2.3	Void	4677

A.13.3	Measurement procedure	4677

A.13.3.1	Intra-frequency measurements	4677

A.13.3.1.1	Event-triggered reporting tests on SCC without gaps under non-DRX	4677

A.13.3.1.1.1	Test purpose and environment	4677

A.13.3.1.1.2	Test parameters	4677

A.13.3.1.1.3	Test Requirements	4682

A.13.3.1.2	Event-triggered reporting tests on SCC without gaps under DRX	4682

A.13.3.1.2.1	Test purpose and environment	4682

A.13.3.1.2.2	Test parameters	4682

A.13.3.1.2.3	Test Requirements	4687

A.13.3.1.3	Event-triggered reporting tests on SCC with per-UE gaps under non-DRX	4687

A.13.3.1.3.1	Test purpose and environment	4687

A.13.3.1.3.2	Test parameters	4687

A.13.3.1.3.3	Test Requirements	4692

A.13.3.1.4	Event-triggered reporting tests on SCC with per-UE gaps under DRX	4692

A.13.3.1.4.1	Test purpose and environment	4692

A.13.3.1.4.2	Test parameters	4692

A.13.3.1.4.3	Test Requirements	4698

A.13.3.1.5	Void	4698

A.13.3.1.6	Void	4698

A.13.3.2	Inter-frequency measurements	4698

A.13.3.2.1	Void	4698

A.13.3.2.2	Void	4698

A.13.3.2.3	Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is not used	4698

A.13.3.2.3.1	Test Purpose and Environment	4698

A.13.3.2.3.2	Test Requirements	4703

A.13.3.2.4	Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is used	4703

A.13.3.2.4.1	Test Purpose and Environment	4703

A.13.3.2.4.2	Test Requirements	4708

A.13.3.2.5	Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is not used	4709

A.13.3.2.5.1	Test Purpose and Environment	4709

A.13.3.2.5.2	Test Requirements	4714

A.13.3.2.6	Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is used	4714

A.13.3.2.6.1	Test Purpose and Environment	4714

A.13.3.2.6.2	Test Requirements	4719

A.13.3.3	L1-RSRP measurements for beam reporting	4720

A.13.3.3.1	SSB based L1-RSRP measurement when DRX is not used	4720

A.13.3.3.1.1	Test Purpose and Environment	4720

A.13.3.3.1.2	Test parameters	4720

A.13.3.3.1.3	Test Requirements	4724

A.13.3.3.2	SSB based L1-RSRP measurement when DRX is used	4724

A.13.3.3.2.1	Test Purpose and Environment	4724

A.13.3.3.2.2	Test parameters	4724

A.13.3.3.2.3	Test Requirements	4728

A.13.4	Measurement performance	4728

A.13.4.1	SS-RSRP	4728

A.13.4.1.1	Intra-frequency measurement accuracy on a carrier frequency with CCA	4728

A.13.4.1.1.1	Test Purpose and Environment	4728

A.13.4.1.1.2	Test parameters	4728

A.13.4.1.1.3	Test Requirements	4731

A.13.4.2	SS-RSRQ	4731

A.13.4.2.1	Intra-frequency measurement accuracy on SCC	4731

A.13.4.2.1.1	Test Purpose and Environment	4731

A.13.4.2.1.2	Test Parameters	4731

A.13.4.2.1.3	Test Requirements	4738

A.13.4.3	SS-SINR	4738

A.13.4.3.1	Intra-frequency measurement accuracy on SCC	4738

A.13.4.3.1.1	Test Purpose and Environment	4738

A.13.4.3.1.2	Test Parameters	4738

A.13.4.3.1.3	Test Requirements	4746

A.13.4.4	L1-RSRP measurement for beam reporting with CCA serving cell	4746

A.13.4.4.1	SSB based L1-RSRP measurement	4746

A.13.4.4.1.1	Test Purpose and Environment	4746

A.13.4.4.1.2	Test parameters	4746

A.13.4.4.1.3	Test Requirements	4750

A.13.4.5	RSSI	4750

A.13.4.5.1 	Intra-frequency RSSI measurement accuracy on a carrier with CCA	4750

A.13.4.5.1.1	Test Purpose and Environment	4750

A.13.4.5.1.2	Test parameters	4750

A.13.4.5.1.3	Test Requirements	4754

A.13.4.5.2	Inter-frequency RSSI measurement accuracy on a carrier with CCA	4754

A.13.4.5.2.1	Test Purpose and Environment	4754

A.13.4.5.2.2	Test parameters	4754

A.13.4.5.2.3	Test Requirements	4758

A.13.4.6	Channel occupancy	4758

A.13.4.6.1	Intra-frequency channel occupancy measurement accuracy on SCC with CCA	4758

A.13.4.6.1.1	Test Purpose and Environment	4758

A.13.4.6.1.2	Test parameters	4758

A.13.4.6.1.3	Test Requirements	4762

A.13.4.6.2	Inter-frequency channel occupancy measurement accuracy on a carrier with CCA	4762

A.13.4.6.2.1	Test Purpose and Environment	4762

A.13.4.6.2.2	Test parameters	4762

A.13.4.6.2.3	Test Requirements	4766

A.14	NR standalone tests for Satellite access	4766

A.14.1	RRC\_IDLE state mobility	4766

A.14.1.1	Cell reselection to FR1 intra-frequency NR case	4766

A.14.1.1.1	Test Purpose and Environment	4766

A.14.1.1.2	Test Parameters	4766

A.14.1.1.3	Test Requirements	4768

A.14.1.2	Cell reselection to FR1 intra-frequency NR cell for UE configured with the feature for enhanced requirements	4769

A.14.1.2.1	Test Purpose and Environment	4769

A.14.1.2.2	Test Parameters	4769

A.14.1.2.3	Test Requirements	4771

A.14.1.3	Time-based measurement initiation to FR1 intra-frequency NR cell reselection	4772

A.14.1.3.1	Test Purpose and Environment	4772

A.14.1.3.2	Test Parameters	4772

A.14.1.3.3	Test Requirements	4774

A.14.1.4	Location-based cell measurement initiation to FR1 intra-frequency NR cell reselection	4775

A.14.1.4.1	Test Purpose and Environment	4775

A.14.1.4.2	Test Parameters	4775

A.14.1.4.3	Test Requirements	4777

A.14.1.5	Cell reselection to FR1 inter-frequency NR case	4778

A.14.1.5.1	Test Purpose and Environment	4778

A.14.1.5.2	Test Parameters	4778

A.14.1.5.3	Test Requirements	4780

A.14.1.6	Cell reselection to FR1 inter-frequency NR cell for UE configured with feature for enhanced requirements	4781

A.14.1.6.1	Test Purpose and Environment	4781

A.14.1.6.2	Test Parameters	4781

A.14.1.6.3	Test Requirements	4783

A.14.1.7	Time-based Cell measurement initiation to FR1 inter-frequency cell reselection	4784

A.14.1.7.1	Test Purpose and Environment	4784

A.14.1.7.2	Test Parameters	4784

A.14.1.7.3	Test Requirements	4786

A.14.1.8	Location-based measurement initiation to FR1 inter-frequency NR cell reselection	4787

A.14.1.8.1	Test Purpose and Environment	4787

A.14.1.8.2	Test Parameters	4787

A.14.1.8.3	Test Requirements	4789

A.14.1.9	Cell reselection to FR1 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion	4790

A.14.1.9.1	Test Purpose and Environment	4790

A.14.1.9.2	Test Parameters	4790

A.14.1.9.3	Test Requirements	4793

A.14.1.10	Cell reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion	4793

A.14.1.10.1	Test Purpose and Environment	4793

A.14.1.10.2	Test Parameters	4793

A.14.1.10.3	Test Requirements	4795

A.14.2	RRC\_CONNECTED state mobility	4796

A.14.2.1	Handover	4796

A.14.2.1.1	Intra-frequency SAN Handover from FR1 to FR1	4796

A.14.2.1.1.1	Test Purpose and Environment	4796

A.14.2.1.1.2	Test Parameters	4796

A.14.2.1.1.3	Test Requirements	4798

A.14.2.1.2	Inter-frequency SAN Handover from FR1 to FR1	4799

A.14.2.1.2.1	Test Purpose and Environment	4799

A.14.2.1.2.2	Test Parameters	4799

A.14.2.1.2.3	Test Requirements	4801

A.14.2.1.3	Intra-frequency SAN time-based conditional Handover from FR1 to FR1	4801

A.14.2.1.3.1	Test Purpose and Environment	4801

A.14.2.1.3.2	Test Parameters	4801

A.14.2.1.3.3	Test Requirements	4805

A.14.2.1.4	Inter-frequency SAN time-based conditional Handover from FR1 to FR1	4805

A.14.2.1.4.1	Test Purpose and Environment	4805

A.14.2.1.4.2	Test Parameters	4805

A.14.2.1.4.3	Test Requirements	4807

A.14.2.1.5	Intra-frequency SAN distance-based conditional Handover from FR1 to FR1	4807

A.14.2.1.5.1	Test Purpose and Environment	4807

A.14.2.1.5.2	Test Parameters	4808

A.14.2.1.5.3	Test Requirements	4811

A.14.2.1.6	Inter-frequency SAN distance-based conditional Handover from FR1 to FR1	4811

A.14.2.1.6.1	Test Purpose and Environment	4811

A.14.2.1.6.2	Test Parameters	4811

A.14.2.1.6.3	Test Requirements	4815

A.14.2.2	RRC Connection Mobility Control	4815

A.14.2.2.1	SA: RRC Re-establishment for SAN	4815

A.14.2.2.1.1	Intra-frequency RRC Re-establishment in FR1	4815

A.14.2.2.1.2	Inter-frequency RRC Re-establishment in FR1	4818

A.14.2.2.2	Random Access	4821

A.14.2.2.2.1	4-step RA type contention based random access test in FR1 for NR standalone	4821

A.14.2.2.2.1.1	Test Purpose and Environment	4821

A.14.2.2.2.1.2	Test Requirements	4824

A.14.2.2.2.2	4-step RA type non-contention based random access test in FR1 for NR standalone	4825

A.14.2.2.2.2.1	Test Purpose and Environment	4825

A.14.2.2.2.2.2	Test Requirements	4829

A.14.2.2.3	RRC Connection Release with Redirection	4830

A.14.2.2.3.1	Redirection from NR in FR1 to NR in FR1	4830

A.14.2.2.3.1.1	Test Purpose and Environment	4830

A.14.2.2.3.1.2	Test Parameters	4830

A.14.2.2.3.1.3	Test Requirements	4834

A.14.3	Timing for Satellite Access	4834

A.14.3.1	UE transmit timing for Satellite Access	4834

A.14.3.1.1	NR UE Transmit Timing Test for FR1	4834

A.14.3.1.1.1	Test Purpose and environment	4834

A.14.3.1.1.2	Test requirements	4836

A.14.3.2	Timing advance for satellite access	4837

A.14.3.2.1	SA FR1 timing advance adjustment accuracy	4837

A.14.3.2.1.1	Test Purpose and Environment	4837

A.14.3.2.1.2	Test Parameters	4837

A.14.3.2.1.3	Test Requirements	4840

A.14.4	Signalling characteristics	4840

A.14.4.1	Radio link Monitoring	4840

A.14.4.1.1	Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode	4840

A.14.4.1.1.1	Test Purpose and Environment	4840

A.14.4.1.1.2	Test Requirements	4845

A.14.4.1.2	Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode	4845

A.14.4.1.2.1	Test Purpose and Environment	4845

A.14.4.1.2.2	Test Requirements	4851

A.14.4.1.3	Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode	4851

A.14.4.1.3.1	Test Purpose and Environment	4851

A.14.4.1.3.2	Test Requirements	4855

A.14.4.1.4	Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode	4855

A.14.4.1.4.1	Test Purpose and Environment	4855

A.14.4.1.4.2	Test Requirements	4860

A.14.4.1.5	Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode	4860

A.14.4.1.5.1	Test Purpose and Environment	4860

A.14.4.1.5.2	Test Requirements	4865

A.14.4.1.6	Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode	4865

A.14.4.1.6.1	Test Purpose and Environment	4865

A.14.4.1.6.2	Test Requirements	4869

A.14.4.1.7	Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode	4869

A.14.4.1.7.1	Test Purpose and Environment	4869

A.14.4.1.7.2	Test Requirements	4874

A.14.4.1.8	Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode	4874

A.14.4.1.8.1	Test Purpose and Environment	4874

A.14.4.1.8.2	Test Requirements	4879

A.14.4.2	Beam Failure Detection and Link recovery procedures for satellite access	4879

A.14.4.2.1	Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in non-DRX mode	4879

A.14.4.2.1.1	Test Purpose and Environment	4879

A.14.4.2.1.2	Test Requirements	4885

A.14.4.2.2	Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in DRX mode	4885

A.14.4.2.2.1	Test Purpose and Environment	4885

A.14.4.2.2.2	Test Requirements	4890

A.14.4.2.3	Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in non-DRX mode	4890

A.14.4.2.3.1	Test Purpose and Environment	4890

A.14.4.2.3.2	Test Requirements	4895

A.14.4.2.4	Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in DRX mode	4896

A.14.4.2.4.1	Test Purpose and Environment	4896

A.14.4.2.4.2	Test Requirements	4901

A.14.4.2.5	Void	4901

A.14.4.2.6	Void	4901

A.14.4.3	Active BWP switch for satellite access	4901

A.14.4.3.1	DCI-based and Timer-based Active BWP Switch	4901

A.14.4.3.1.1	NR FR1 DL active BWP switch with non-DRX in SA	4901

A.14.4.3.1.1.1	Test Purpose and Environment	4901

A.14.4.3.1.1.2	Test Requirements	4906

A.14.4.3.2	RRC-based Active BWP Switch	4906

A.14.4.3.2.1	NR FR1 DL active BWP switch of Cell with non-DRX in SA	4906

A.14.4.3.2.1.1	Test Purpose and Environment	4906

A.14.4.3.2.1.2	Test Requirements	4910

A.14.4.4	UE specific CBW change for satellite access	4910

A.14.4.4.1	UE specific CBW change on PCell in FR1 in non-DRX	4910

A.14.4.4.1.1	Test Purpose and Environment	4910

A.14.4.4.1.2	Test Requirements	4914

A.14.4.5	Pathloss reference signal switching delay	4914

A.14.4.5.1	MAC-CE based pathloss reference signal switch delay	4914

A.14.4.5.1.1	Test Purpose and Environment	4914

A.14.4.5.1.2	Test Requirements	4917

A.14.5	Measurement procedure	4918

A.14.5.1	Intra-frequency Measurements	4918

A.14.5.1.1	SA event triggered reporting tests without gap under non-DRX	4918

A.14.5.1.1.1	Test purpose and Environment	4918

A.14.5.1.1.2	Test parameters	4918

A.14.5.1.1.3	Test Requirements	4920

A.14.5.1.2	SA event triggered reporting tests without gap under DRX	4921

A.14.5.1.2.1	Test purpose and Environment	4921

A.14.5.1.2.2	Test parameters	4921

A.14.5.1.2.3	Test Requirements	4922

A.14.5.1.3	SA event triggered reporting tests without gap under non-DRX with SSB index reading	4923

A.14.5.1.3.1	Test purpose and Environment	4923

A.14.5.1.3.2	Test parameters	4923

A.14.5.1.3.3	Test Requirements	4925

A.14.5.1.4	SA event triggered reporting tests with single measurement gap under non-DRX for satellite access	4926

A.14.5.1.4.1	Test purpose and Environment	4926

A.14.5.1.4.2	Test parameters	4926

A.14.5.1.4.3	Test Requirements	4928

A.14.5.1.5	SA event triggered reporting tests with FNO concurrent gaps under DRX for satellite access	4929

A.14.5.1.5.1	Test purpose and Environment	4929

A.14.5.1.5.2	Test parameters	4929

A.15.5.1.5.3	Test Requirements	4932

A.14.5.1.6	SA event triggered reporting tests with PPO concurrent gaps under non-DRX with SSB index reading for satellite access	4932

A.14.5.1.6.1	Test purpose and Environment	4932

A.14.5.1.6.2	Test parameters	4932

A.14.5.1.6.3	Test Requirements	4934

A.14.5.2	Inter-frequency Measurements	4935

A.14.5.2.1	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with single gap for satellite access	4935

A.14.5.2.1.1	Test Purpose and Environment	4935

A.14.5.2.1.2	Test Requirements	4939

A.14.5.2.2	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used with single gap for satellite access	4939

A.14.5.2.2.1	Test Purpose and Environment	4939

A.14.5.2.2.2	Test Requirements	4943

A.14.5.2.3	SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used with single gap for satellite access	4943

A.14.5.2.3.1	Test Purpose and Environment	4943

A.14.5.2.3.2	Test Requirements	4947

A.14.5.2.4	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in fully non-overlapped for satellite access	4947

A.14.5.2.4.1	Test Purpose and Environment	4947

A.14.5.2.4.2	Test Requirements	4951

A.14.5.2.5	void	4951

A.14.5.2.5.1	void	4951

A.14.5.2.5.2	void	4951

A.14.5.2.6	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in partially partial overalpping for satellite access	4951

A.14.5.2.6.1	Test Purpose and Environment	4951

A.14.5.2.6.2	Test Requirements	4955

A.14.5.2.7	Event triggered reporting test without gap under non-DRX	4955

A.14.5.2.7.1	Test purpose and Environment	4955

A.14.5.2.7.2	Test parameters	4955

A.14.5.2.7.3	Test Requirements	4957

A.14.5.2.8	Event triggered reporting tests without gap under DRX	4958

A.14.5.2.8.1	Test purpose and Environment	4958

A.14.5.2.8.2	Test parameters	4958

A.14.5.2.8.3	Test Requirements	4960

A.14.5.3	L1-RSRP measurement for beam reporting for satellite access	4961

A.14.5.3.1	SSB based L1-RSRP measurement for satellite access when DRX is not used	4961

A.14.5.3.1.1	Test Purpose and Environment	4961

A.14.5.3.1.2	Test parameters	4961

A.14.5.3.1.3	Test Requirements	4964

A.14.5.3.2	SSB based L1-RSRP measurement for satellite access when DRX is used	4964

A.14.5.3.2.1	Test Purpose and Environment	4964

A.14.5.3.2.2	Test parameters	4964

A.14.5.3.2.3	Test Requirements	4968

A.14.5.3.3	CSI-RS based L1-RSRP measurement for satellite access when DRX is not used	4968

A.14.5.3.3.1	Test Purpose and Environment	4968

A.14.5.3.3.2	Test parameters	4968

A.14.5.3.3.3	Test Requirements	4970

A.14.5.3.4	CSI-RS based L1-RSRP measurement for satellite access when DRX is used	4970

A.14.5.3.4.1	Test Purpose and Environment	4970

A.14.5.3.4.2	Test parameters	4970

A.14.5.3.4.3	Test Requirements	4974

A.14.6	Measurement Performance requirements	4974

A.14.6.1	 SS-RSRP for SAN	4974

A.14.6.1.1	SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell	4974

A.14.6.1.1.1	Test Purpose and Environment	4974

A.14.6.1.1.2	Test parameters	4975

A.14.6.1.1.3	Test Requirements	4978

A.14.6.1.2	SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell	4978

A.14.6.1.2.1	Test Purpose and Environment	4978

A.14.6.1.2.2	Test parameters	4978

A.14.6.1.2.3	Test Requirements	4981

A.14.6.2	SS-RSRQ	4981

A.14.6.2.1	SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access	4981

A.14.6.2.1.1	Test Purpose and Environment	4981

A.14.6.2.1.2	Test Parameters	4981

A.14.6.2.1.3	Test Requirements	4984

A.14.6.2.2	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access	4984

A.14.6.2.2.1	Test Purpose and Environment	4984

A.14.6.2.2.2	Test Parameters	4984

A.14.6.2.2.3	Test Requirements	4987

A.14.6.3	SS-SINR	4987

A.14.6.3.1	SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	4987

A.14.6.3.1.1	Test Purpose and Environment	4987

A.14.6.3.1.2	Test Parameters	4987

A.14.6.3.1.3	Test Requirements	4990

A.14.6.3.2	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	4990

A.14.6.3.2.1	Test Purpose and Environment	4990

A.14.6.3.2.2	Test Parameters	4990

A.14.6.3.2.3	Test Requirements	4993

A.14.6.4	L1-RSRP measurement for beam reporting	4993

A.14.6.4.1	SSB based L1-RSRP measurement	4993

A.14.6.4.1.1	Test Purpose and Environment	4993

A.14.6.4.1.2	Test parameters	4993

A.14.6.4.1.3	Test Requirements	4996

A.14.6.4.2	CSI-RS based L1-RSRP measurement on resource set with repetition off	4996

A.14.6.4.2.1	Test Purpose and Environment	4996

A.14.6.4.2.2	Test parameters	4996

A.14.6.4.2.3	Test Requirements	4999

A.15	NR standalone tests with one or more NR cells in FR2-2	5012

A.15.1	SA: RRC\_IDLE state mobility	5012

A.15.1.1	Cell re-selection to NR	5012

A.15.1.1.1	Cell reselection to FR2-2 intra-frequency NR case	5012

A.15.1.1.1.1	Test Purpose and Environment	5012

A.15.1.1.1.2	Test Parameters	5012

A.15.1.1.1.3	Test Requirements	5016

A.15.1.2	Cell reselection to FR2-2 inter-frequency NR case	5016

A.15.1.2.1	Test Purpose and Environment	5016

A.15.1.2.2	Test Parameters	5016

A.15.1.2.3	Test Requirements	5020

A.15.1.3	Cell reselection to FR2-2 intra-frequency NR case for UE fulfilling low mobility relaxed measurement criterion	5020

A.15.1.3.1	Test Purpose and Environment	5020

A.15.1.3.2	Test Parameters	5020

A.15.1.3.3	Test Requirements	5023

A.15.1.4	Cell reselection to FR2-2 intra-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion	5023

A.15.1.4.1	Test Purpose and Environment	5023

A.15.1.4.2	Test Parameters	5023

A.15.1.4.3	Test Requirements	5026

A.15.1.5	Cell reselection to FR2-2 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion	5026

A.15.1.5.1	Test Purpose and Environment	5026

A.15.1.5.2	Test Parameters	5026

A.15.1.5.3	Test Requirements	5030

A.15.1.6	Cell reselection to FR2-2 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion	5030

A.15.1.6.1	Test Purpose and Environment	5030

A.15.1.6.2	Test Parameters	5030

A.15.1.6.3	Test Requirements	5033

A.15.2	Signaling characteristics	5033

A.15.2.1	SCell Activation and Deactivation Delay	5033

A.15.2.1.1	SCell Activation and deactivation for SCell in FR2-2 intra-band in non-DRX	5033

A.15.2.1.1.1	Test Purpose and Environment	5033

A.15.2.1.1.2	Test Requirements	5036

A.15.2.1.2	SCell Activation and deactivation for FR1+FR2-2 inter-band with target SCell in FR2-2	5036

A.15.2.1.2.1	Test Purpose and Environment	5036

A.15.2.1.2.2	Test Requirements	5041

A.15.2.1.3	SCell Activation and deactivation for SCell in FR2-2 inter-band in non-DRX	5042

A.15.2.1.3.1	Test Purpose and Environment	5042

A.15.2.1.3.2	Test Requirements	5045

A.15.2.1.4	Direct SCell activation at SCell addition of known SCell in FR2-2	5046

A.15.2.1.4.1	Test Purpose and Environment	5046

A.15.2.1.4.2	Test Requirements	5049

A.15.2.1.5	Direct SCell activation at handover with known SCell in FR2-2	5050

A.15.2.1.5.1	Test Purpose and Environment	5050

A.15.2.1.5.2	Test Requirements	5054

A.15.3	RRC\_CONNECTED state mobility	5055

A.15.3.1	Handover	5055

A.15.3.1.1	Intra-frequency handover from FR2-2 carrier with CCA to FR2-2 carrier with CCA; unknown target cell	5055

A.15.3.1.1.1	Test Purpose and Environment	5055

A.15.3.1.1.2	Test Parameters	5055

A.15.3.1.1.3	Test Requirements	5059

A.15.3.1.2	Inter-frequency handover from FR1 to FR2-2 carrier with CCA; unknown target cell	5059

A.15.3.1.2.1	Test Purpose and Environment	5059

A.15.3.1.2.2	Test Parameters	5059

A.15.3.1.2.3	Test Requirements	5063

A.15.4	Measurement procedure	5064

A.15.4.1	Intra-frequency Measurements	5064

A.15.4.1.1	SA event triggered reporting test without gap under non-DRX for FR2-2 with CCA	5064

A.15.4.1.1.1	Test purpose and Environment	5064

A.15.4.1.1.2	Test Requirements	5066

A.15.4.2	Inter-frequency Measurements	5067

A.15.4.2.1	SA event triggered reporting tests for FR2-2 with CCA without SSB time index detection when DRX is not used (PCell in FR2-2)	5067

A.15.4.2.1.1	Test Purpose and Environment	5067

A.15.4.2.1.2	Test Requirements	5070

A.16	NR standalone tests with all NR cells in FR1 for RedCap	5071

A.16.1	SA: RRC\_IDLE state mobility for RedCap	5071

A.16.1.1	Cell re-selection to NR	5071

A.16.1.1.1	Cell reselection to FR1 intra-frequency NR case for 1 Rx UE	5071

A.16.1.1.1.1	Test Purpose and Environment	5071

A.16.1.1.1.2	Test Parameters	5071

A.16.1.1.1.3	Test Requirements	5075

A.16.1.1.2	Cell reselection to FR1 intra-frequency NR case for 2 Rx UE	5075

A.16.1.1.2.1	Test Purpose and Environment	5075

A.16.1.1.2.2	Test Parameters	5075

A.16.1.1.2.3	Test Requirements	5079

A.16.1.1.3	Cell reselection to FR1 inter-frequency NR case for 1 Rx UE	5079

A.16.1.1.3.1	Test Purpose and Environment	5079

A.16.1.1.3.2	Test Parameters	5079

A.16.1.1.3.3	Test Requirements	5084

A.16.1.1.4	Cell reselection to FR1 inter-frequency NR case for 2 Rx UE	5084

A.16.1.1.4.1	Test Purpose and Environment	5084

A.16.1.1.4.2	Test Parameters	5084

A.16.1.1.4.3	Test Requirements	5089

A.16.1.1.5	Cell reselection to FR1 intra-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 1 Rx UE	5089

A.16.1.1.5.1	Test Purpose and Environment	5089

A.16.1.1.5.2	Test Parameters	5089

A.16.1.1.5.3	Test Requirements	5094

A.16.1.1.6	Cell reselection to FR1 intra-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE	5094

A.16.1.1.6.1	Test Purpose and Environment	5094

A.16.1.1.6.2	Test Parameters	5094

A.16.1.1.6.3	Test Requirements	5099

A.16.1.1.7	Cell reselection to FR1 inter-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 1 Rx UE	5099

A.16.1.1.7.1	Test Purpose and Environment	5099

A.16.1.1.7.2	Test Parameters	5099

A.16.1.1.7.3	Test Requirements	5104

A.16.1.1.8	Cell reselection to FR1 inter-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE	5105

A.16.1.1.8.1	Test Purpose and Environment	5105

A.16.1.1.8.2	Test Parameters	5105

A.16.1.1.8.3	Test Requirements	5109

A.16.1.2	Inter-RAT E-UTRAN cell re-selection for RedCap	5110

A.16.1.2.1	Cell reselection to higher priority E-UTRAN for 1RX	5110

A.16.1.2.1.1	Test Purpose and Environment	5110

A.16.1.2.1.2	Test Parameters	5110

A.16.1.2.1.3	Test Requirements	5113

A.16.1.2.2	Cell reselection to higher priority E-UTRAN for 2RX	5114

A.16.1.2.2.1	Test Purpose and Environment	5114

A.16.1.2.2.2	Test Parameters	5114

A.16.1.2.2.3	Test Requirements	5117

A.16.1.2.3.1	Test Purpose and Environment	5118

A. 16.1.2.3.2	Test Parameters	5118

A.16.1.2.3.3	Test Requirements	5121

A.16.1.2.4.1	Test Purpose and Environment	5122

A.16.1.2.4.2	Test Parameters	5122

A.16.1.3.1.3	Test Requirements	5125

A.16.1.2.5	Cell reselection to lower priority E-UTRAN for UE fulfilling stationary relaxed measurement criterion for 1 Rx UE	5126

A.16.1.2.5.1	Test Purpose and Environment	5126

A.16.1.2.5.2	Test Parameters	5126

A.16.1.2.5.3	Test Requirements	5129

A.16.1.2.6	Cell reselection to lower priority E-UTRAN for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE	5130

A.16.1.2.6.1	Test Purpose and Environment	5130

A.16.1.2.6.2	Test Parameters	5130

A.16.1.2.6.3	Test Requirements	5133

A.16.2	SA: RRC\_INACTIVE state mobility for RedCap	5134

A.16.2.1	Configured Grant based Small Data Transmissions (CG-SDT) for RedCap	5134

A.16.2.1.1	NR UE CG-SDT Test in FR1 for 1Rx RedCap UE	5134

A.16.2.1.1.1	Test purpose and Environment	5134

A.16.2.1.1.2	Test Parameters	5135

A.16.2.1.1.3	Test requirements	5139

A.16.2.1.2	NR UE CG-SDT Test in FR1 for 2Rx RedCap UE	5139

A.16.2.1.2.1	Test purpose and Environment	5139

A.16.2.1.2.2	Test Parameters	5141

A.16.2.1.2.3	Test requirements	5144

A.16.3	RRC\_CONNECTED state mobility for RedCap	5144

A.16.3.1	Handover	5144

A.16.3.1.1	Intra-frequency handover from FR1 to FR1; known target cell for 1 Rx UE	5144

A.16.3.1.1.1	Test Purpose and Environment	5144

A.16.3.1.1.2	Test Parameters	5145

A.16.3.1.1.3	Test Requirements	5148

A.16.3.1.2	Intra-frequency handover from FR1 to FR1; known target cell for 2 Rx UE	5148

A.16.3.1.2.1	Test Purpose and Environment	5148

A.16.3.1.2.2	Test Parameters	5148

A.16.3.1.2.3	Test Requirements	5152

A.16.3.1.3	Intra-frequency handover from FR1 to FR1; unknown target cell for 1 Rx UE	5152

A.16.3.1.3.1	Test Purpose and Environment	5152

A.16.3.1.3.2	Test Parameters	5152

A.16.3.1.3.3	Test Requirements	5156

A.16.3.1.4	Intra-frequency handover from FR1 to FR1; unknown target cell for 2 Rx UE	5156

A.16.3.1.4.1	Test Purpose and Environment	5156

A.16.3.1.4.2	Test Parameters	5156

A.16.3.1.5	Inter-frequency handover from FR1 to FR1; unknown target cell for 1 Rx UE	5160

A.16.3.1.5.1	Test Purpose and Environment	5160

A.16.3.1.5.2	Test Parameters	5160

A.16.3.1.5.3	Test Requirements	5164

A.16.3.1.6	Inter-frequency handover from FR1 to FR1; unknown target cell for 2 Rx UE	5164

A.16.3.1.6.1	Test Purpose and Environment	5164

A.16.3.1.6.2	Test Parameters	5164

A.16.3.1.6.3	Test Requirements	5168

A.16.3.1.7	SA NR - E-UTRAN handover for 1Rx UE	5168

A.16.3.1.7.1	Test Purpose and Environment	5168

A.16.3.1.7.2	Test Requirements	5174

A.16.3.1.8	 SA NR - E-UTRAN handover for 2Rx UE	5174

A.16.3.1.8.1	Test Purpose and Environment	5174

A.16.3.1.8.2	Test Requirements	5180

A.16.3.1.9	SA NR - E-UTRAN handover with unknown target cell for 1 Rx UE	5180

A.16.3.1.9.1	Test Purpose and Environment	5180

A.16.3.1.9.2	Test Requirements	5187

A.16.3.1.10	SA NR - E-UTRAN handover with unknown target cell for 2 Rx UE	5187

A.16.3.1.10.1	Test Purpose and Environment	5187

A.16.3.1.10.2	Test Requirements	5193

A.16.3.2	RRC Connection Mobility Control	5193

A.16.3.2.1	SA: RRC Re-establishment	5193

A.16.3.2.1.1	Intra-frequency RRC Re-establishment in FR1 for 1 Rx UE	5193

A.16.3.2.1.2	Intra-frequency RRC Re-establishment in FR1 for 2 Rx UE	5197

A.16.3.2.1.3	Inter-frequency RRC Re-establishment in FR1 for 1 Rx UE	5201

A.16.3.2.1.4	Inter-frequency RRC Re-establishment in FR1 for 2 Rx UE	5206

A.16.3.2.1.5	Intra-frequency RRC Re-establishment in FR1 for 1 Rx UE without serving cell timing	5211

A.16.3.2.1.6	Intra-frequency RRC Re-establishment in FR1 for 2 Rx UE without serving cell timing	5215

A.16.3.2.2	Random Access	5219

A.16.3.2.2.1	4-step RA type contention based random access test in FR1 for NR standalone for 1 Rx UE	5219

A.16.3.2.2.2	4-step RA type contention based random access test in FR1 for NR standalone for 2 Rx UE	5225

A.16.3.2.2.3	4-step RA type non-contention based random access test in FR1 for NR standalone for 1 Rx UE	5230

A.16.3.2.2.5	2-step RA type contention based random access test in FR1 for NR standalone for 1 Rx UE	5240

A.16.3.2.2.6	2-step RA type contention based random access test in FR1 for NR standalone for 2 Rx UE	5244

A.16.3.2.2.7	2-step RA type non-contention based test in FR1 for NR standalone for 1 RX UE	5248

A.16.3.2.2.8	2-step RA type non-contention based test in FR1 for NR standalone for 2 RX UE	5252

A.16.3.2.3	SA: RRC Connection Release with Redirection	5256

A.16.3.2.3.1	Redirection from NR in FR1 to NR in FR1 for 1 Rx UE	5256

A.16.3.2.3.2	Redirection from NR in FR1 to NR in FR1 for 2 Rx UE	5260

A.16.3.2.3.3	Redirection from NR in FR1 to E-UTRAN for 1 Rx UE	5264

A.16.3.2.3.4	Redirection from NR in FR1 to E-UTRAN for 2 Rx UE	5271

A.16.4	Timing for RedCap	5278

A.16.4.1	UE transmit timing	5278

A.16.4.1.1	NR UE Transmit Timing Test for FR1 for 1Rx RedCap UE	5278

A.16.4.1.1.1	Test Purpose and environment	5278

A.16.4.1.1.2	Test requirements	5283

A.16.4.1.2	NR UE Transmit Timing Test for FR1 for 2Rx RedCap UE	5283

A.16.4.1.2.1	Test Purpose and environment	5283

A.16.4.1.2.2	Test requirements	5286

A.16.4.2	UE timer accuracy	5286

A.16.4.3	Timing advance	5286

A.16.4.3.1	SA FR1 timing advance adjustment accuracy for 1 Rx UE	5286

A.16.4.3.1.1	Test Purpose and Environment	5286

A.16.4.3.1.2	Test Parameters	5286

A.16.4.3.1.3	Test Requirements	5290

A.16.4.3.2	SA FR1 timing advance adjustment accuracy for 2 Rx UE	5290

A.16.4.3.2.1	Test Purpose and Environment	5290

A.16.4.3.2.2	Test Parameters	5291

A.16.4.3.2.3	Test Requirements	5294

A.16.5	Signalling characteristics for RedCap	5295

A.16.5.1	Radio link Monitoring	5295

A.16.5.1.1	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for 1 Rx UE	5295

A.16.5.1.1.1	Test Purpose and Environment	5295

A.16.5.1.1.2	Test Requirements	5300

A.16.5.1.2	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for 2 Rx UE	5300

A.16.5.1.2.1	Test Purpose and Environment	5300

A.16.5.1.2.2	Test Requirements	5306

A.16.5.1.3	Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for 1 Rx UE	5306

A.16.5.1.3.1	Test Purpose and Environment	5306

A.16.5.1.3.2	Test Requirements	5312

A.16.5.1.4	Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for 2 Rx UE	5312

A.16.5.1.4.1	Test Purpose and Environment	5312

A.16.5.1.4.2	Test Requirements	5318

A.16.5.1.5	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for 1 Rx UE	5318

A.16.5.1.5.1	Test Purpose and Environment	5318

A.16.5.1.5.2	Test Requirements	5324

A.16.5.1.6	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for 2 Rx UE	5324

A.16.5.1.6.1	Test Purpose and Environment	5324

A.16.5.1.6.2	Test Requirements	5329

A.16.5.1.7	Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for 1 Rx UE	5329

A.16.5.1.7.1	Test Purpose and Environment	5329

A.16.5.1.7.2	Test Requirements	5334

A.16.5.1.8	Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for 2 Rx UE	5334

A.16.5.1.8.1	Test Purpose and Environment	5334

A.16.5.1.8.2	Test Requirements	5340

A.16.5.1.9	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode for 1 Rx UE	5340

A.16.5.1.9.1	Test Purpose and Environment	5340

A.16.5.1.9.2	Test Requirements	5346

A.16.5.1.10	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode for 2 Rx UE	5346

A.16.5.1.10.1	Test Purpose and Environment	5346

A.16.5.1.10.2	Test Requirements	5352

A.16.5.1.11	Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode for 1 Rx UE	5352

A.16.5.1.11.1	Test Purpose and Environment	5352

A.16.5.1.11.2	Test Requirements	5358

A.16.5.1.12	Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode for 2 Rx UE	5358

A.16.5.1.12.1	Test Purpose and Environment	5358

A.16.5.1.12.2	Test Requirements	5364

A.16.5.1.13	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for 1 Rx UE	5364

A.16.5.1.13.1	Test Purpose and Environment	5364

A.16.5.1.13.2	Test Requirements	5369

A.16.5.1.14	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for 2 Rx UE	5369

A.16.5.1.14.1	Test Purpose and Environment	5369

A.16.5.1.14.2	Test Requirements	5375

A.16.5.1.15	Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for 1 Rx UE	5375

A.16.5.1.15.1	Test Purpose and Environment	5375

A.16.5.1.15.2	Test Requirements	5381

A.16.5.1.16	Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for 2 Rx UE	5381

A.16.5.1.16.1	Test Purpose and Environment	5381

A.16.5.1.16.2	Test Requirements	5387

A.16.5.2	Beam Failure Detection and Link recovery procedures	5387

A.16.5.2.1	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode for 1 Rx UE	5387

A.16.5.2.1.1	Test Purpose and Environment	5387

A.16.5.2.1.2	Test Requirements	5393

A.16.5.2.2	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode for 2 Rx UE	5393

A.16.5.2.2.1	Test Purpose and Environment	5393

A.16.5.2.2.2	Test Requirements	5399

A.16.5.2.3	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode for 1 Rx UE	5399

A.16.5.2.3.1	Test Purpose and Environment	5399

A.16.5.2.3.2	Test Requirements	5406

A.16.5.2.4	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode for 2 Rx UE	5406

A.16.5.2.4.1	Test Purpose and Environment	5406

A.16.5.2.4.2	Test Requirements	5412

A.16.5.2.5	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode for 1 Rx UE	5412

A.16.5.2.5.1	Test Purpose and Environment	5412

A.16.5.2.5.2	Test Requirements	5418

A.16.5.2.6	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode for 2 Rx UE	5418

A.16.5.2.6.1	Test Purpose and Environment	5418

A.16.5.2.6.2	Test Requirements	5424

A.16.5.2.7	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode for 1 Rx UE	5424

A.16.5.2.7.1	Test Purpose and Environment	5424

A.16.5.2.7.2	Test Requirements	5430

A.16.5.2.8	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode for 2 Rx UE	5430

A.16.5.2.8.1	Test Purpose and Environment	5430

A.16.5.2.8.2	Test Requirements	5436

A.16.5.3	Active BWP switch	5436

A.16.5.3.1	DCI-based and Timer-based Active BWP Switch	5436

A.16.5.3.1.1	NR FR1 DL active BWP switch with non-DRX in SA for 1 Rx UE	5436

A.16.5.3.1.1.1	Test Purpose and Environment	5436

A.16.5.3.1.2.1	Test Requirements	5441

A.16.5.3.1.2	NR FR1 DL active BWP switch with non-DRX in SA for 2 Rx UE	5441

A.16.5.3.1.2.1	Test Purpose and Environment	5441

A.16.5.3.1.2.2	Test Requirements	5446

A.16.5.3.2	RRC-based Active BWP Switch	5446

A.16.5.3.2.1	NR FR1 DL active BWP switch of Cell with non-DRX in SA for 1 Rx UE	5446

A.16.5.3.2.1.1	Test Purpose and Environment	5446

A.16.5.3.2.1.2	Test Requirements	5450

A.16.5.3.2.2	NR FR1 DL active BWP switch of Cell with non-DRX in SA for 2 Rx UE	5450

A.16.5.3.2.2.1	Test Purpose and Environment	5450

A.16.5.3.2.2.2	Test Requirements	5454

A.16.5.4	UE specific CBW change	5454

A.16.5.4.1	UE specific CBW change on PCell in FR1 in non-DRX for 1 Rx UE	5454

A.16.5.4.1.1	Test Purpose and Environment	5454

A.16.5.4.1.2	Test Requirements	5458

A.16.5.4.2	UE specific CBW change on PCell in FR1 in non-DRX for 2 Rx UE	5458

A.16.5.4.2.1	Test Purpose and Environment	5458

A.16.5.4.2.2	Test Requirements	5462

A.16.6	Measurement procedure for RedCap	5462

A.16.6.1	Intra-frequency Measurements	5462

A.16.6.1.1	SA event triggered reporting tests without gap under non-DRX for 1 Rx UE	5462

A.16.6.1.1.1	Test purpose and Environment	5462

A.16.6.1.1.2	Test parameters	5462

A.16.6.1.1.3	Test Requirements	5466

A.16.6.1.2	SA event triggered reporting tests without gap under non-DRX for 2 Rx UE	5466

A.16.6.1.2.1	Test purpose and Environment	5466

A.16.6.1.2.2	Test parameters	5466

A.16.6.1.2.3	Test Requirements	5470

A.16.6.1.3	SA event triggered reporting tests without gap under DRX for 1 Rx UE	5470

A.16.6.1.3.1	Test purpose and Environment	5470

A.16.6.1.3.2	Test parameters	5470

A.16.6.1.3.3	Test Requirements	5474

A.16.6.1.4	SA event triggered reporting tests without gap under DRX for 2 Rx UE	5474

A.16.6.1.4.1	Test purpose and Environment	5474

A.16.6.1.4.2	Test parameters	5474

A.16.6.1.4.3	Test Requirements	5478

A.16.6.1.5	SA event triggered reporting tests with per-UE gaps under non-DRX for 1 Rx UE	5478

A.16.6.1.5.1	Test purpose and Environment	5478

A.16.6.1.5.2	Test parameters	5478

A.16.6.1.5.3	Test Requirements	5482

A.16.6.1.6	SA event triggered reporting tests with per-UE gaps under non-DRX for 2 Rx UE	5482

A.16.6.1.6.1	Test purpose and Environment	5482

A.16.6.1.6.2	Test parameters	5482

A.16.6.1.6.3	Test Requirements	5486

A.16.6.1.7	SA event triggered reporting tests with per-UE gaps under DRX for 1 Rx UE	5486

A.16.6.1.7.1	Test purpose and Environment	5486

A.16.6.1.7.2	Test parameters	5486

A.16.6.1.7.3	Test Requirements	5490

A.16.6.1.8	SA event triggered reporting tests with per-UE gaps under DRX for 2 Rx UE	5490

A.16.6.1.8.1	Test purpose and Environment	5490

A.16.6.1.8.2	Test parameters	5490

A.16.6.1.8.3	Test Requirements	5494

A.16.6.1.9	SA event triggered reporting tests without gap under non-DRX with SSB index reading for 1 Rx UE	5494

A.16.6.1.9.1	Test purpose and Environment	5494

A.16.6.1.9.2	Test parameters	5494

A.16.6.1.9.3	Test Requirements	5496

A.16.6.1.10	SA event triggered reporting tests without gap under non-DRX with SSB index reading for 2 Rx UE	5497

A.16.6.1.10.1	Test purpose and Environment	5497

A.16.6.1.10.2	Test parameters	5497

A.16.6.1.10.3	Test Requirements	5498

A.16.6.1.11	SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading for 1 Rx UE	5499

A.16.6.1.11.1	Test purpose and Environment	5499

A.16.6.1.11.2	Test parameters	5499

A.16.6.1.11.3	Test Requirements	5501

A.16.6.1.12	SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading for 2 Rx UE	5502

A.16.6.1.12.1	Test purpose and Environment	5502

A.16.6.1.12.2	Test parameters	5502

A.16.6.1.12.3	Test Requirements	5504

A.16.6.2	Inter-frequency Measurements	5505

A.16.6.2.1	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used for 1 Rx UE	5505

A.16.6.2.1.1	Test Purpose and Environment	5505

A.16.6.2.1.2	Test Requirements	5510

A.16.6.2.2	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used for 2 Rx UE	5510

A.16.6.2.2.1	Test Purpose and Environment	5510

A.16.6.2.2.2	Test Requirements	5515

A.16.6.2.3	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used for 1 Rx UE	5515

A.16.6.2.3.1	Test Purpose and Environment	5515

A.16.6.2.3.2	Test Requirements	5518

A.16.6.2.4	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used for 2 Rx UE	5519

A.16.6.2.4.1	Test Purpose and Environment	5519

A.16.6.2.4.2	Test Requirements	5522

A.16.6.2.5	SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used for 1 Rx UE	5523

A.16.6.2.5.1	Test Purpose and Environment	5523

A.16.6.2.5.2	Test Requirements	5526

A.16.6.2.6	SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used for 2 Rx UE	5527

A.16.6.2.6.1	Test Purpose and Environment	5527

A.16.6.2.6.2	Test Requirements	5530

A.16.6.2.7	SA event triggered reporting tests for FR1 with SSB time index detection when DRX is used for 1 Rx UE	5531

A.16.6.2.7.1	Test Purpose and Environment	5531

A.16.6.2.7.2	Test Requirements	5535

A.16.6.2.8	SA event triggered reporting tests for FR1 with SSB time index detection when DRX is used for 2 Rx UE	5536

A.16.6.2.8.1	Test Purpose and Environment	5536

A.16.6.2.8.2	Test Requirements	5539

A.16.6.2.9	SA event triggered reporting tests with additional mandatory gap pattern for 1 Rx UE	5540

A.16.6.2.9.1	Test Purpose and Environment	5540

A.16.6.2.9.2	Test Requirements	5543

A.16.6.2.10	SA event triggered reporting tests with additional mandatory gap pattern for 2 Rx UE	5543

A.16.6.2.10.1	Test Purpose and Environment	5543

A.16.6.2.10.2	Test Requirements	5546

A.16.6.2.11	SA event triggered reporting tests for FR1 when DRX is used for 1 Rx UE	5546

A.16.6.2.11.1	Test Purpose and Environment	5546

A.16.6.2.11.2	Test Requirements	5549

A.16.6.2.12	SA event triggered reporting tests for FR1 when DRX is used for 2 Rx UE	5549

A.16.6.2.12.1	Test Purpose and Environment	5549

A.16.6.2.12.2	Test Requirements	5553

A.16.6.3	Inter-RAT Measurements	5554

A.16.6.3.1	SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 for 1 Rx UE	5554

A.16.6.3.1.1	Test purpose and Environment	5554

A.16.6.3.1.2	Test Requirements	5559

A.16.6.3.2	SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 for 2 Rx UE	5559

A.16.6.3.2.1	Test purpose and Environment	5559

A.16.6.3.2.2	Test Requirements	5564

A.16.6.3.3	SA NR - E-UTRAN event-triggered reporting in DRX in FR1 for 1 Rx UE	5564

A.16.6.3.3.1	Test purpose and Environment	5564

A.16.6.3.3.2	Test Requirements	5569

A.16.6.3.4	SA NR - E-UTRAN event-triggered reporting in DRX in FR1 for 2 Rx UE	5569

A.16.6.3.4.1	Test purpose and Environment	5569

A.16.6.3.4.2	Test Requirements	5574

A.16.6.4	L1-RSRP measurement for beam reporting	5574

A.16.6.4.1	SSB based L1-RSRP measurement when DRX is not used for 1 Rx UE	5574

A.16.6.4.1.1	Test Purpose and Environment	5574

A.16.6.4.1.2	Test parameters	5574

A.16.6.4.1.3	Test Requirements	5578

A.16.6.4.2	SSB based L1-RSRP measurement when DRX is not used for 2 Rx UE	5578

A.16.6.4.2.1	Test Purpose and Environment	5578

A.16.6.4.2.2	Test parameters	5579

A.16.6.4.2.3	Test Requirements	5582

A.16.6.4.3	SSB based L1-RSRP measurement when DRX is used for 1 Rx UE	5582

A.16.6.4.3.1	Test Purpose and Environment	5582

A.16.6.4.3.2	Test parameters	5583

A.16.6.4.3.3	Test Requirements	5586

A.16.6.4.4	SSB based L1-RSRP measurement when DRX is used for 2 Rx UE	5586

A.16.6.4.4.1	Test Purpose and Environment	5586

A.16.6.4.4.2	Test parameters	5587

A.16.6.4.4.3	Test Requirements	5590

A.16.6.4.5	CSI-RS based L1-RSRP measurement when DRX is not used for 1 Rx UE	5590

A.16.6.4.5.1	Test Purpose and Environment	5590

A.16.6.4.5.2	Test parameters	5591

A.16.6.4.5.3	Test Requirements	5594

A.16.6.4.6	CSI-RS based L1-RSRP measurement when DRX is not used for 2 Rx UE	5594

A.16.6.4.6.1	Test Purpose and Environment	5594

A.16.6.4.6.2	Test parameters	5595

A.16.6.4.6.3	Test Requirements	5598

A.16.6.4.7	CSI-RS based L1-RSRP measurement when DRX is used for 1 Rx UE	5598

A.16.6.4.7.1	Test Purpose and Environment	5598

A.16.6.4.7.2	Test parameters	5599

A.16.6.4.7.3	Test Requirements	5602

A.16.6.4.8	CSI-RS based L1-RSRP measurement when DRX is used for 2 Rx UE	5602

A.16.6.4.8.1	Test Purpose and Environment	5602

A.16.6.4.8.2	Test parameters	5603

A.16.6.4.8.3	Test Requirements	5606

A.16.6.5	NR measurements with autonomous gaps	5606

A.16.6.5.1	SA intra-frequency CGI identification of NR neighbor cell in FR1 for 1 Rx UE	5606

A.16.6.5.1.1	Test Purpose and Environment	5606

A.16.6.5.1.2	Test Parameters	5606

A.16.6.5.1.3	Test Requirements	5609

A.16.6.5.2	SA intra-frequency CGI identification of NR neighbor cell in FR1 for 2 Rx UE	5609

A.16.6.5.2.1	Test Purpose and Environment	5609

A.16.6.5.2.2	Test Parameters	5609

A.16.6.5.2.3	Test Requirements	5612

A.16.6.5.3	Identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR SA for 1 Rx UE	5612

A.16.6.5.3.1	Test Purpose and Environment	5612

A.16.6.5.3.2	Test Requirements	5617

A.16.6.5.4	Identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR SA for 2 Rx UE	5618

A.16.6.5.4.1	Test Purpose and Environment	5618

A.16.6.5.4.2	Test Requirements	5623

A.16.7	Measurement Performance requirements for RedCap	5624

A.16.7.1	SS-RSRP	5624

A.16.7.1.1	SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE	5624

A.16.7.1.1.1	Test Purpose and Environment	5624

A.16.7.1.1.2	Test parameters	5624

A.16.7.1.1.3	Test Requirements	5629

A.16.7.1.2	SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 2Rx UE	5629

A.16.7.1.2.1	Test Purpose and Environment	5629

A.16.7.1.2.2	Test parameters	5629

A.16.7.1.2.3	Test Requirements	5634

A.16.7.1.3	SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE	5634

A.16.7.1.3.1	Test Purpose and Environment	5634

A.16.7.1.3.2	Test parameters	5634

A.16.7.1.3.3	Test Requirements	5638

A.16.7.1.4	SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE	5638

A.16.7.1.4.1	Test Purpose and Environment	5638

A.16.7.1.4.2	Test parameters	5639

A.16.7.1.4.3	Test Requirements	5643

A.16.7.2	SS-RSRQ	5643

A.16.7.2.1	SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE	5643

A.16.7.2.1.1	Test Purpose and Environment	5643

A.16.7.2.1.2	Test Parameters	5644

A.16.7.2.1.3	Test Requirements	5648

A.16.7.2.2	SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE	5648

A.16.7.2.2.1	Test Purpose and Environment	5648

A.16.7.2.2.2	Test Parameters	5648

A.16.7.2.2.3	Test Requirements	5652

A.16.7.2.3	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE	5652

A.16.7.2.3.1	Test Purpose and Environment	5652

A.16.7.2.3.2	Test parameters	5652

A.16.7.2.3.3	Test Requirements	5657

A.16.7.2.4	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE	5657

A.16.7.2.4.1	Test Purpose and Environment	5657

A.16.7.2.4.2	Test parameters	5657

A.16.7.2.4.3	Test Requirements	5663

A.16.7.3	SS-SINR	5663

A.16.7.3.1	SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE	5663

A.16.7.3.1.1	Test Purpose and Environment	5663

A.16.7.3.1.2	Test parameters	5664

A.16.7.3.1.3	Test Requirements	5668

A.16.7.3.2	SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE	5668

A.16.7.3.2.1	Test Purpose and Environment	5668

A.16.7.3.2.2	Test parameters	5669

A.16.7.3.3	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE	5673

A.16.7.3.3.1	Test Purpose and Environment	5673

A.16.7.3.3.2	Test parameters	5673

A.16.7.3.3.3	Test Requirements	5678

A.16.7.3.4	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE	5679

A.16.7.3.4.1	Test Purpose and Environment	5679

A.16.7.3.4.2	Test parameters	5679

A.16.7.3.4.3	Test Requirements	5683

A.16.7.4	L1-RSRP measurement for beam reporting	5684

A.16.7.4.1	SSB based L1-RSRP measurement for 1 Rx UE	5684

A.16.7.4.1.1	Test Purpose and Environment	5684

A.16.7.4.1.2	Test parameters	5684

A.16.7.4.1.3	Test Requirements	5688

A.16.7.4.2	SSB based L1-RSRP measurement for 2 Rx UE	5688

A.16.7.4.2.1	Test Purpose and Environment	5688

A.16.7.4.2.2	Test parameters	5688

A.16.7.4.2.3	Test Requirements	5689

A.16.7.4.3	CSI-RS based L1-RSRP measurement on resource set with repetition off for 1 Rx UE	5689

A.16.7.4.3.1	Test Purpose and Environment	5689

A.16.7.4.3.2	Test parameters	5689

A.16.7.4.3.3	Test Requirements	5693

A.16.7.4.4	CSI-RS based L1-RSRP measurement on resource set with repetition off for 2 Rx UE	5693

A.16.7.4.4.1	Test Purpose and Environment	5693

A.16.7.4.4.2	Test parameters	5694

A.16.7.4.4.3	Test Requirements	5694

A.16.7.5	E-UTRAN RSRP	5694

A.16.7.5.1	SA: inter-RAT measurement accuracy with FR1 serving cell for 1 Rx UE	5694

A.16.7.5.1.1	Test Purpose and Environment	5694

A.16.7.5.1.2	Test parameters	5694

A.16.7.5.1.3	Test Requirements	5700

A.16.7.5.2	SA: inter-RAT measurement accuracy with FR1 serving cell for 2 Rx UE	5701

A.16.7.5.2.1	Test Purpose and Environment	5701

A.16.7.5.2.2	Test parameters	5701

A.16.7.5.2.3	Test Requirements	5707

A.16.7.6	E-UTRAN RSRQ	5708

A.16.7.6.1	SA: inter-RAT measurement accuracy with FR1 serving cell for 1 Rx UE	5708

A.16.7.6.1.1	Test Purpose and Environment	5708

A.16.7.6.1.2	Test parameters	5708

A.16.7.6.1.3	Test Requirements	5714

A.16.7.6.2	SA: inter-RAT measurement accuracy with FR1 serving cell for 2 Rx UE	5715

A.16.7.6.2.1	Test Purpose and Environment	5715

A.16.7.6.2.2	Test parameters	5715

A.16.7.6.2.3	Test Requirements	5721

A.17	NR standalone tests with one or more NR cells in FR2 for RedCap	5722

A.17.1	SA: RRC\_IDLE state mobility for RedCap	5722

A.17.1.1	Cell re-selection to NR	5722

A.17.1.1.1	Cell reselection to FR2 intra-frequency NR case for 2 Rx	5722

A.17.1.1.1.1	Test Purpose and Environment	5722

A.17.1.1.1.2	Test Parameters	5722

A.17.1.1.1.3	Test Requirements	5726

A.17.1.1.2	Cell reselection to FR2 inter-frequency NR case	5726

A.17.1.1.2.1	Test Purpose and Environment	5726

A.17.1.1.2.2	Test Parameters	5726

A.17.1.1.2.3	Test Requirements	5730

A.17.1.1.3	Cell reselection to FR2 intra-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE	5730

A.17.1.1.3.1	Test Purpose and Environment	5730

A.17.1.1.3.2	Test Parameters	5730

A.17.1.1.3.3	Test Requirements	5733

A.17.1.1.4	Cell reselection to FR2 inter-frequency NR case for UE fulfilling stationary mobility relaxed measurement criterion for 2 Rx UE	5733

A.17.1.1.4.1	Test Purpose and Environment	5733

A.17.1.1.4.2	Test Parameters	5733

A.17.1.1.4.3	Test Requirements	5737

A.17.2	SA: RRC\_INACTIVE state mobility for RedCap	5737

A.17.2.1	Configured Grant based Small Data Transmissions (CG-SDT) for RedCap	5737

A.17.2.1.1	TA validation for CG-SDT in FR2 for RedCap	5737

A.17.2.1.1.1	Test Purpose and Environment	5737

A.17.2.1.1.2	Test Requirements	5741

A.17.3	RRC\_CONNECTED state mobility for RedCap	5742

A.17.3.1	Handover for RedCap	5742

A.17.3.1.1	Intra-frequency handover from FR2 to FR2; unknown target cell for 2 Rx	5742

A.17.3.1.1.1	Test Purpose and Environment	5742

A.17.3.1.1.2	Test Parameters	5742

A.17.3.1.1.3	Test Requirements	5744

A.17.3.1.2	Inter-frequency handover from FR2 to FR2; unknown target cell for 2 Rx	5744

A.17.3.1.2.1	Test Purpose and Environment	5744

A.17.3.1.2.2	Test Parameters	5744

A.17.3.1.2.3 Test Requirements	5747

A.17.3.2	RRC Connection Mobility Control for RedCap	5747

A.17.3.2.1	SA: RRC Re-establishment	5747

A.17.3.2.1.1	Intra-frequency RRC Re-establishment in FR2	5747

A.17.3.2.1.1.1	Test Purpose and Environment	5747

A.17.3.2.1.2	Inter-frequency RRC Re-establishment in FR2	5750

A.17.3.2.1.2.1	Test Purpose and Environment	5750

A.17.3.2.1.3	Intra-frequency RRC Re-establishment in FR2 without serving cell timing	5753

A.17.3.2.1.3.1	Test Purpose and Environment	5753

A.17.3.2.1.3.2	Test Requirements	5755

A.17.3.2.2	Random Access	5756

A.17.3.2.2.1	4-step RA type contention based random access test in FR2 for NR Standalone	5756

A.17.3.2.2.1.1	Test Purpose and Environment	5756

A.17.3.2.2.1.2	Test Requirements	5758

A.17.3.2.2.2	4-step RA type non-contention based random access test in FR2 for NR Standalone	5760

A.17.3.2.2.2.1	Test Purpose and Environment	5760

A.17.3.2.2.2.2	Test Requirements	5762

A.17.3.2.2.3	2-step RA type contention based random access test in FR2 for NR Standalone	5764

A.17.3.2.2.3.1	Test Purpose and Environment	5764

A.17.3.2.2.3.2	Test Requirements	5766

A.17.3.2.2.4	2-step RA type non-contention based random access test in FR2 for NR Standalone	5767

A.17.3.2.2.4.1	Test Purpose and Environment	5767

A.17.3.2.2.4.2	Test Requirements	5769

A.17.3.2.3	SA: RRC Connection Release with Redirection	5770

A.17.3.2.3.1	Redirection from NR in FR2 to NR in FR2	5770

A.17.3.2.3.1.1	Test Purpose and Environment	5770

A.17.3.2.3.1.2	Test Parameters	5770

A.17.3.2.3.1.3	Test Requirements	5774

A.17.4	Timing	5774

A.17.4.1	UE transmit timing	5774

A.17.4.1.1	NR UE Transmit Timing Test for FR2	5774

A.17.4.1.1.1	Test Purpose and environment	5774

A.17.4.1.1.2	Test requirements	5777

A.17.4.2	UE timer accuracy	5778

A.17.4.3	Timing advance	5778

A.17.4.3.1	SA FR2 timing advance adjustment accuracy	5778

A.17.4.3.1.1	Test Purpose and Environment	5778

A.17.4.3.1.2	Test Parameters	5778

A.17.4.3.1.3 Test Requirements	5781

A.17.5	Signaling characteristics for RedCap	5781

A.17.5.1	Radio link Monitoring for RedCap	5781

A.17.5.1.1	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode	5781

A.17.5.1.1.1	Test Purpose and Environment	5781

A.17.5.1.1.2	Test Requirements	5784

A.17.5.1.2	Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode	5785

A.17.5.1.2.1	Test Purpose and Environment	5785

A.17.5.1.2.2	Test Requirements	5789

A.17.5.1.3	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode	5790

A.17.5.1.3.1	Test Purpose and Environment	5790

A.17.5.1.3.2	Test Requirements	5794

A.17.5.1.4	Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode	5794

A.17.5.1.4.1	Test Purpose and Environment	5794

A.17.5.1.4.2	Test Requirements	5799

A.17.5.1.5	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode	5799

A.17.5.1.5.1	Test Purpose and Environment	5799

A.17.5.1.5.2	Test Requirements	5804

A.17.5.1.6	Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode	5804

A.17.5.1.6.1	Test Purpose and Environment	5804

A.17.5.1.6.2	Test Requirements	5808

A.17.5.1.7	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode	5808

A.17.5.1.7.1	Test Purpose and Environment	5808

A.17.5.1.7.2	Test Requirements	5812

A.17.5.1.8	Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode	5812

A.17.5.1.8.1	Test Purpose and Environment	5812

A.17.5.1.8.2	Test Requirements	5817

A.17.5.1.9	UE Radio Link Monitoring Scheduling Restrictions on FR2	5817

A.17.5.1.9.1	Test Purpose and Environment	5817

A.17.5.1.9.2	Test Requirements	5820

A.17.5.2	Beam Failure Detection and Link recovery procedures	5820

A.17.5.2.1	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode	5820

A.17.5.2.1.1	Test Purpose and Environment	5820

A.17.5.2.1.2	Test Requirements	5824

A.17.5.2.2	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in DRX mode	5824

A.17.5.2.2.1	Test Purpose and Environment	5824

A.17.5.2.2.2	Test Requirements	5828

A.17.5.2.3	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode	5828

A.17.5.2.3.1	Test Purpose and Environment	5828

A.17.5.2.3.2	Test Requirements	5832

A.17.5.2.4	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode	5832

A.17.5.2.4.1	Test Purpose and Environment	5832

A.17.5.2.4.2	Test Requirements	5836

A.17.5.2.5	Scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode for 2 Rx UE	5836

A.17.5.2.5.1	Test Purpose and Environment	5836

A.17.5.2.5.2	Test Requirements	5840

A.17.5.3	Active BWP switch for RedCap	5840

A.17.5.3.1	DCI-based and Timer-based Active BWP Switch	5840

A.17.5.3.1.1	NR FR2 DL active BWP switch with non-DRX in SA	5840

A.17.5.3.1.1.1	Test Purpose and Environment	5840

A.17.5.3.1.1.2	Test Requirements	5843

A.17.5.3.2	RRC-based Active BWP Switch	5843

A.17.5.3.2.1	NR FR2 DL active BWP switch of PCell with non-DRX in SA	5843

A.17.5.3.2.1.1	Test Purpose and Environment	5843

A.17.5.3.2.1.2	Test Requirements	5846

A.17.5.4	Active TCI state switch delay	5847

A.17.5.4.1	MAC-CE based active TCI state switch	5847

A.17.5.4.1.1	NR PCell FR2 active TCI state switch for a known TCI state	5847

A.17.5.4.1.1.1	Test Purpose and Environment	5847

A.17.5.4.1.1.2	Test Requirements	5850

A.17.5.4.2	RRC based active TCI state switch	5850

A.17.5.4.2.1	NR PCell FR2 active TCI state switch for a known TCI state	5850

A.17.5.4.2.1.1	Test Purpose and Environment	5850

A.17.5.4.2.1.2	Test Requirements	5854

A.17.5.5	Uplink spatial relation switch delay	5854

A.17.5.5.1	MAC-CE based Spatial Relation switch	5854

A.17.5.5.1.1	 NR PCell FR2 spatial relation associated with known DL-RS	5854

A.17.5.5.1.1.1	Test Purpose and Environment	5854

A.17.5.5.1.1.2	Test Requirements	5857

A.17.5.5.2	RRC based spatial relation switch	5857

A.17.5.5.2.1	NR PCell FR2 spatial relation switch associated with a known DL-RS	5857

A.17.5.5.2.1.2	Test Requirements	5860

A.17.5.6	UE specific CBW change	5860

A.17.5.6.1	NR FR2 UE specific CBW change of PCell with non-DRX in SA	5860

A.17.5.6.1.1	Test Purpose and Environment	5860

A.17.5.6.1.2	Test Requirements	5863

A.17.6	Measurement procedure for RedCap	5864

A.17.6.1	Intra-frequency Measurements	5864

A.17.6.1.1	SA event triggered reporting test without gap under non-DRX	5864

A.17.6.1.1.1	Test purpose and Environment	5864

A.17.6.1.1.2	Test Requirements	5867

A.17.6.1.2	SA event triggered reporting test without gap under DRX	5867

A.17.6.1.2.1	Test purpose and Environment	5867

A.7.6.1.2.2	Test Requirements	5867

A.17.6.1.3	SA event triggered reporting test with per-UE gaps under non-DRX	5868

A.17.6.1.3.1	Test purpose and Environment	5868

A.17.6.1.3.2	Test Requirements	5872

A.17.6.1.4	SA event triggered reporting test with per-UE gaps under DRX	5872

A.17.6.1.4.1	Test purpose and Environment	5872

A.17.6.1.4.2	Test Requirements	5875

A.17.6.2	Inter-frequency Measurements	5876

A.17.6.2.1	SA event triggered reporting tests For FR2 without SSB time index detection when DRX is not used (PCell in FR2)	5876

A.17.6.2.1.1	Test Purpose and Environment	5876

A.17.6.2.1.2	Test Requirements	5879

A.17.6.2.2	SA event triggered reporting tests For FR2 without SSB time index detection when DRX is used (PCell in FR2)	5879

A.17.6.2.2.1	Test Purpose and Environment	5879

A.17.6.2.2.2	Test Requirements	5883

A.17.6.2.3	SA event triggered reporting tests For FR2 with SSB time index detection when DRX is not used (PCell in FR2)	5883

A.17.6.2.3.1	Test Purpose and Environment	5883

A.17.6.2.3.2	Test Requirements	5887

A.17.6.2.4	SA event triggered reporting tests For FR2 with SSB time index detection when DRX is used (PCell in FR2) for 2 RX UE	5887

A.17.6.2.4.1	Test Purpose and Environment	5887

A.17.6.2.4.2	Test Requirements	5891

A.17.6.3	L1-RSRP measurement for beam reporting	5892

A.17.6.3.1	SSB based L1-RSRP measurement when DRX is not used	5892

A.17.6.3.1.1	Test Purpose and Environment	5892

A.17.6.3.1.2	Test parameters	5892

A.17.6.3.1.3	Test Requirements	5892

A.17.6.3.2	SSB based L1-RSRP measurement when DRX is used	5892

A.17.6.3.2.1	Test Purpose and Environment	5892

A.17.6.3.2.2	Test parameters	5892

A.17.6.3.2.3	Test Requirements	5894

A.17.6.3.3	CSI-RS based L1-RSRP measurement when DRX is not used	5894

A.17.6.3.3.1	Test Purpose and Environment	5894

A.17.6.3.3.2	Test parameters	5895

A.17.6.3.3.3	Test Requirements	5897

A.17.6.3.4	CSI-RS based L1-RSRP measurement when DRX is used	5898

A.17.6.3.4.1	Test Purpose and Environment	5898

A.17.6.3.4.2	Test parameters	5898

A.7.6.3.3.3	Test Requirements	5900

A.17.6.4	NR Measurements with autonomous gaps	5901

A.17.6.4.1	SA interfrequency CGI reporting in autonomous gaps test (PCell in FR2) for 2 RX UE	5901

A.17.6.4.1.1	Test Purpose and Environment	5901

A.17.6.4.1.2	Test Requirements	5904

A.17.7	Measurement Performance requirements	5904

A.17.7.1	SS-RSRP	5904

A.17.7.1.1	SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	5904

A.17.7.1.1.1	Test Purpose and Environment	5904

A.17.7.1.1.2	Test parameters	5904

A.17.7.1.1.3	Test Requirements	5908

A.17.7.1.2	SA inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	5909

A.17.7.1.2.1	Test Purpose and Environment	5909

A.17.7.1.2.2	Test parameters	5909

A.17.7.1.2.3	Test Requirements	5913

A.17.7.2	SS-RSRQ	5914

A.17.7.2.1	SA intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell	5914

A.17.7.2.1.1	Test Purpose and Environment	5914

A.17.7.2.1.2	Test Parameters	5914

A.17.7.2.1.3	Test Requirements	5916

A.17.7.2.2	SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell for 2 Rx UE	5916

A.17.7.2.2.1	Test Purpose and Environment	5916

A.17.7.2.2.2	Test parameters	5916

A.17.7.2.2.3	Test Requirements	5918

A.17.7.3	L1-RSRP measurement for beam reporting	5918

A.17.7.3.1	SSB based L1-RSRP measurement	5918

A.17.7.3.1.1	Test Purpose and Environment	5918

A.17.7.3.1.2	Test parameters	5919

A.17.7.3.1.3	Test Requirements	5919

A.17.7.3.2	CSI-RS based L1-RSRP measurement on resource set with repetition off	5919

A.17.7.3.2.1	Test Purpose and Environment	5919

A.17.7.3.2.2	Test parameters	5919

A.17.7.3.2.3	Test Requirements	5919

A.17.7.4	SS-SINR	5920

A.17.7.4.1	SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell for 2Rx UE	5920

A.17.7.4.1.1	Test Purpose and Environment	5920

A.17.7.4.1.2	Test parameters	5920

A.17.7.4.1.3	Test Requirements	5922

A.17.7.4.2	SA inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell for 2Rx UE	5922

A.17.7.4.2.1	Test Purpose and Environment	5922

A.17.7.4.2.2	Test Parameters	5922

A.17.7.4.2.3	Test Requirements	5924

A.18	E-UTRA standalone tests for NR RRM for RedCap	5924

A.18.1	RRC\_IDLE state mobility	5924

A.18.1.1	Inter-RAT NR Cell re-selection	5924

A.18.1.1.1	E-UTRA Cell reselection to higher priority NR target Cell in FR1	5924

A.18.1.1.1.1	Test Purpose and Environment	5924

A.18.1.1.1.2	Test Requirements	5929

A.18.2	RRC\_CONNECTED state mobility	5929

A.18.2.1	Handover	5929

A.18.2.1.1	E-UTRAN - NR handover in FR1	5929

A.18.2.1.1.1	Test Purpose and Environment	5929

A.18.2.1.1.2	Test Requirements	5934

A.18.2.2	RRC connection release with redirection	5934

A.18.2.2.1	Redirection from E-UTRA to NR FR1 for redcap UE	5934

A.18.2.2.1.1	Test Purpose and Environment	5934

A.18.2.2.1.2	Test Parameters	5934

A.18.2.2.1.3	Test Requirements	5941

A.18.3	Measurement procedure	5941

A.18.3.1	E-UTRA – NR Inter-RAT Measurements	5941

A.18.3.1.1	NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used	5941

A.18.3.1.1.1	Test Purpose and Environment	5941

A.18.3.1.1.2	Test Requirements	5946

A.18.3.1.2	NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used	5946

A.18.3.1.2.1	Test Purpose and Environment	5946

A.18.3.1.2.2	Test Requirements	5952

A.18.3.1.3	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used	5952

A.18.3.1.3.1	Test Purpose and Environment	5952

A.18.3.1.3.2	Test Requirements	5958

A.18.3.1.4	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used	5958

A.18.3.1.4.1	Test Purpose and Environment	5958

A.18.3.1.4.2	Test Requirements	5964

A.18.3.1.5	NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is not used	5964

A.18.3.1.5.1	Test Purpose and Environment	5964

A.18.3.1.5.2	Test Requirements	5966

A.18.3.1.6	NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is used	5967

A.18.3.1.6.1	Test Purpose and Environment	5967

A.18.3.1.6.2	Test Requirements	5969

A.18.3.1.7	NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is not used	5970

A.18.3.1.7.1	Test Purpose and Environment	5970

A.18.3.1.7.2	Test Requirements	5972

A.18.3.1.8	NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is used	5973

A.18.3.1.8.1	Test Purpose and Environment	5973

A.18.3.1.8.2	Test Requirements	5975

Annex B (normative): Conditions for RRM requirements applicability for operating bands	5976

B.1	Conditions for NR RRC\_IDLE state mobility	5976

B.1.1	Introduction	5976

B.1.2	Conditions for measurements on NR intra-frequency cells for cell re-selection	5976

B.1.2A	Conditions for measurements on NR intra-frequency cells under CCA for cell re-selection	5977

B.1.3	Conditions for measurements on NR inter-frequency cells for cell re-selection	5978

B.1.3A	Conditions for measurements on NR inter-frequency cells under CCA for cell re-selection	5978

B.1.4	Conditions for measurements on NR intra-frequency cells for cell re-selection for RedCap	5978

B.1.5	Conditions for measurements on NR inter-frequency cells for cell re-selection for RedCap	5979

B.1.6	Conditions for measurements on NR intra-frequency cells for cell re-selection for satellite access	5980

B.1.7	Conditions for measurements on NR inter-frequency cells for cell re-selection for satellite access	5980

B.2	Conditions for UE measurements procedures and performance requirements in RRC\_CONNECTED state	5980

B.2.1	Introduction	5980

B.2.1.1	General	5980

B.2.1.2	Derivation of Minimum SSB\_RP values for FR1	5980

B.2.1.3	Derivation of Minimum SSB\_RP values for FR2	5981

B.2.1.3.1	Minimum SSB\_RP values for Rx Beam Peak angle of arrival	5981

B.2.1.3.2	Minimum SSB\_RP values for angle of arrival within Spherical coverage	5981

B.2.1.4	Gain to SS-RSRP and CSI-RSRP measurement point for FR1	5982

B.2.1.5	Gain to SS-RSRP and CSI-RSRP measurement point for FR2	5982

B.2.1.5.1	Gain to SS-RSRP and CSI-RSRP measurement point for Rx Beam Peak angle of arrival	5982

B.2.1.5.2	Gain to SS-RSRP measurement point for different frequency	5983

B.2.1.5.3	Alignment of Rough beam to Rx beam Peak	5983

B.2.1.6	Gain to PRS-RSRP measurement point for FR2	5984

B.2.1.6.1	Gain to PRS-RSRP measurement point for Rx Beam Peak angle of arrival	5984

B.2.2	Conditions for NR intra-frequency measurements	5984

B.2.3	Conditions for NR inter-frequency measurements	5986

B.2.4	Conditions for NR L1-RSRP reporting	5987

B.2.4.1	Conditions for SSB based L1-RSRP reporting	5987

B.2.4.2	Conditions for CSI-RS based L1-RSRP reporting	5988

B.2.5	Conditions for RRC connection release with redirection to NR	5990

B.2.6	Void	5991

B.2.6.1	Void	5991

B.2.6.2	Void	5991

B.2.7	Conditions for SRS-RSRP measurements	5991

B.2.8	Conditions for NR L1-SINR reporting	5992

B.2.8.1	Conditions for L1-SINR reporting with CSI-RS based CMR and no dedicated IMR configured	5992

B.2.8.2	Conditions for L1-SINR reporting with SSB based CMR and dedicated IMR configured	5993

B.2.8.2.1	L1-SINR reporting with SSB based CMR and dedicated ZP-IMR configured	5993

B.2.8.2.2	L1-SINR reporting with SSB based CMR and dedicated NZP-IMR configured	5993

B.2.8.3	Conditions for L1-SINR reporting with CSI-RS based CMR and dedicated IMR configured	5995

B.2.8.3.1	L1-SINR reporting with CSI-RS based CMR and dedicated ZP-IMR configured	5995

B.2.8.3.2	L1-SINR reporting with CSI-RS based CMR and dedicated NZP-IMR configured	5996

B.2.9	Conditions for NR intra-frequency measurements under CCA	5997

B.2.10	Conditions for NR inter-frequency measurements under CCA	5997

B.2.11	Conditions for NR L1-RSRP reporting under CCA	5997

B.2.11.1	Conditions for SSB based L1-RSRP reporting	5997

B.2.12	Conditions for NR CSI-RS based intra-frequency measurements	5998

B.2.13	Conditions for NR CSI-RS based inter-frequency measurements	5999

B.2.14	Conditions for NR PRS-based measurements	6001

B.2.15	Conditions for NR intra-frequency measurements for RedCap	6003

B.2.16	Conditions for NR inter-frequency measurements for RedCap	6004

B.2.17	Conditions for NR intra-frequency measurements for satellite access	6006

B.2.18	Conditions for NR inter-frequency measurements for satellite access	6007

B.2.19	Conditions for NR L1-RSRP reporting for satellite access	6007

B.2.19.1	Conditions for SSB based L1-RSRP reporting for satellite access	6007

B.2.19.2	Conditions for CSI-RS based L1-RSRP reporting for satellite access	6007

B.2.20	Conditions for RRC connection release with redirection to NR for satellite access	6008

B.3	RRM Requirements Exceptions	6008

B.3.1	Introduction	6008

B.3.2	Receiver sensitivity relaxation for CA	6008

B.3.2.1	Receiver sensitivity relaxation for UE supporting CA in FR1	6008

B.3.2.2	Receiver sensitivity relaxation for UE configured with CA in FR1	6008

B.3.2.2.1	Inter-band carrier aggregation	6008

B.3.2.2.2	Reference sensitivity exceptions due to UL harmonic interference for CA	6008

B.3.2.2.3	Reference sensitivity exceptions due to intermodulation interference due to 2UL CA	6009

B.3.2.3	Receiver sensitivity relaxation for UE supporting CA in FR2	6009

B.3.2.4	Receiver sensitivity relaxation for UE configured with CA in FR2	6009

B.3.2.4.1	Intra-band contiguous carrier aggregation	6009

B.3.2.4.2	Intra-band non-contiguous carrier aggregation	6009

B.3.3	Receiver sensitivity relaxation for DC	6009

B.3.3.1	Receiver sensitivity relaxation for EN-DC	6009

B.3.3.2	Receiver sensitivity relaxation for NE-DC	6009

B.3.4	Receiver sensitivity relaxation for SUL	6009

B.3.4.1	Receiver sensitivity relaxation for UE supporting SUL in FR1	6009

B.3.4.2	Receiver sensitivity relaxation for UE configured with SUL in FR1	6010

B.3.4.2.1	Reference sensitivity exceptions due to UL harmonic interference for SUL	6010

B.4	Conditions for V2X	6010

B.4.1	Test parameters for GNSS signals	6010

B.4.2	Conditions for PSBCH-RSRP Accuracy Requirements	6010

B.4.3	Conditions for Selection/Reselection to Intra-frequency SyncRef UE	6011

B.4.4	Conditions for L1 SL-RSRP Accuracy Requirements	6011

B.5	High level test procedure for SAN RRM tests	6011

Annex C (informative): Change history	6013