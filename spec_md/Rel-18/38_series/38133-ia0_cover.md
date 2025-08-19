| 3GPP TS 38.133 V18.10.0 (2025-06)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | 3GPP TS 38.133 V18.10.0 (2025-06)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Technical Specification                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Technical Specification                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 3rd Generation Partnership Project; Technical Specification Group Radio Access Network; NR; Requirements for support of radio resource management (Release 18)                                                                                                                                                                                                                                                                                                                                                                                                                                                 | 3rd Generation Partnership Project; Technical Specification Group Radio Access Network; NR; Requirements for support of radio resource management (Release 18)                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP. The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification. Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices. | The present document has been developed within the 3rd Generation Partnership Project (3GPP TM) and may be further elaborated for the purposes of 3GPP. The present document has not been subject to any approval process by the 3GPP Organizational Partners and shall not be implemented. This Specification is provided for future development work within 3GPP only. The Organizational Partners accept no liability for any use of this Specification. Specifications and Reports for implementation of the 3GPP TM system should be obtained via the 3GPP Organizational Partners' Publications Offices. |

|                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 3GPP Postal address  3GPP support office address 650 Route des Lucioles - Sophia Antipolis Valbonne - FRANCE Tel.: +33 4 92 94 42 00 Fax: +33 4 93 65 47 16 Internet http://www.3gpp.org                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Copyright Notification No part may be reproduced except as authorized by written permission. The copyright and the foregoing restriction extend to reproduction in all media.  © 2025, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, TTA, TTC). All rights reserved.  UMTS™ is a Trade Mark of ETSI registered for the benefit of its members 3GPP™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners LTE™ is a Trade Mark of ETSI registered for the benefit of its Members and of the 3GPP Organizational Partners GSM® and the GSM logo are registered and owned by the GSM Association |

## Contents

Foreword	149

1	Scope	151

2	References	151

3	Definitions, symbols and abbreviations	153

3.1	Definitions	153

3.2	Symbols	154

3.3	Abbreviations	155

3.4	Test tolerances	158

3.5	Frequency bands grouping	158

3.5.1	Introduction	158

3.5.2	NR operating bands in FR1	159

3.5.2A	NR operating bands for satellite access in FR1	148

3.5.3	NR operating bands in FR2	148

3.6	Applicability of requirements in this specification version	149

3.6.1	RRC connected state requirements in DRX	149

3.6.2	Number of serving carriers	150

3.6.2.1	Number of serving carriers for SA	150

3.6.2.2	Number of serving carriers for EN-DC	150

3.6.2.3	Number of serving carriers for NE-DC	150

3.6.2.4	Number of serving carriers for NR-DC	150

3.6.3	Applicability for intra-band FR2	150

3.6.4	Applicability for FR2 UE power classes	150

3.6.5	Applicability for SDL bands	151

3.6.6	Applicability of requirements for NGEN-DC operation	151

3.6.7	Applicability of QCL	151

3.6.9	Applicability of requirements for scheduling availability	152

3.6.10	Applicability of requirements for measurement restrictions	152

3.6.11	Applicability of requirements for Redcap UEs	152

3.6.11.1	RRC connected state requirements in DRX	152

3.6.11.2	Applicability for FR2 Redcap UE power classes	152

3.6.11.3	Applicability of QCL	152

3.6.12	Applicability of requirements for Satellite Access	152

3.6.13	Applicability of requirements for FR2	152

3.6.14	Applicability of requirements for FR2 Power Class 6	153

3.6.15	Applicability of requirements for per-FR gap	153

3.6.16	Applicability of requirements for ATG	153

3.6.17	Applicability of requirements for MUSIM gaps	153

3.6.18	Applicability of requirements for a UE operating on a cell with less than 5 MHz BW	153

3.6.19	Applicability of requirements for multi-Rx operation in FR2-1	153

4	SA: RRC\_IDLE state mobility	153

4.1	Cell Selection	153

4.2	Cell Re-selection	154

4.2.1	Introduction	154

4.2.2	Requirements	154

4.2.2.1	UE measurement capability	154

4.2.2.2	Measurement and evaluation of serving cell	154

4.2.2.3	Measurements of intra-frequency NR cells	156

4.2.2.4	Measurements of inter-frequency NR cells	160

4.2.2.5	Measurements of inter-RAT E-UTRAN cells	165

4.2.2.6	Maximum interruption in paging reception	167

4.2.2.7	General requirements	168

4.2.2.8	Minimum requirement at transitions	168

4.2.2.9	Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion	169

4.2.2.9.1	Introduction	169

4.2.2.9.2	Measurements for UE fulfilling low mobility criterion	169

4.2.2.9.3	Measurements for UE fulfilling not-at-cell edge criterion	171

4.2.2.9.4	Measurements for UE fulfilling low mobility and not-at-cell edge criteria	173

4.2.2.10	Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion	174

4.2.2.10.1	Introduction	174

4.2.2.10.2	Measurements for UE fulfilling low mobility criterion	174

4.2.2.10.3	Measurements for UE fulfilling not-at-cell edge criterion	176

4.2.2.10.4	Measurements for UE fulfilling low mobility and not-at-cell edge criterion	179

4.2.2.11	Measurements of inter-RAT E-UTRAN cells for UE configured with relaxed measurement criterion	179

4.2.2.11.1	Introduction	179

4.2.2.11.2	Measurements for UE fulfilling low mobility criterion	180

4.2.2.11.3	Measurements for UE fulfilling with not-at-cell edge criterion	181

4.2.2.11.4	Measurements for UE fulfilling low mobility and not-at-cell edge criterion	183

4.2.2.12	 Measurements of inter-frequency NR cells with NTN carrier	183

4.2A	Cell Re-selection when subject to CCA	186

4.2A.1	Introduction	186

4.2A.2	Requirements	187

4.2A.2.1	UE measurement capability	187

4.2A.2.2	Measurement and evaluation when subject to CCA on the serving cell	187

4.2A.2.3	Measurements of intra-frequency NR cells when subject to CCA on the serving cell and target cell	188

4.2A.2.4	Measurements of inter-frequency NR cells when subject to CCA on the target cell	189

4.2A.2.5	Measurements of inter-RAT E-UTRAN cells when subject to CCA on the serving cell	191

4.2A.2.6	Maximum interruption in paging reception when subject to CCA on the target cell	191

4.2A.2.7	General requirements	192

4.2B	Cell Re-selection for RedCap	192

4.2B.1	Introduction	192

4.2B.2	Requirements	192

4.2B.2.1	UE measurement capability for RedCap	192

4.2B.2.1.1	UE measurement capability for 1 Rx RedCap	192

4.2B.2.1.2	UE measurement capability for 2 Rx RedCap	192

4.2B.2.2	Measurement and evaluation of serving cell for RedCap UE	192

4.2B.2.3	Measurements of intra-frequency NR cells for RedCap UE	194

4.2B.2.4	Measurements of inter-frequency NR cells for RedCap UE	196

4.2B.2.5	Measurements of inter-RAT E-UTRAN cells for RedCap UE	199

4.2B.2.6	Maximum interruption in paging reception for RedCap	201

4.2B.2.7	General requirements for RedCap	201

4.2B.2.8	Minimum requirement at transitions	201

4.2B.2.9	Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion for RedCap	202

4.2B.2.9.1	Introduction	202

4.2B.2.9.2	Measurements for UE fulfilling stationary criterion	203

4.2B.2.9.3	Measurements for a UE fulfilling not-at-cell edge while stationary criterion	205

4.2B.2.9.3A	Measurements for a UE fulfilling stationary and not-at-cell-edge criteria	206

4.2B.2.9.4	Measurements for a UE fulfilling low mobility and stationary criteria	206

4.2B.2.9.5	Measurements for a UE fulfilling low mobility and not-at-cell-edge while stationary criteria	206

4.2B.2.9.6	Measurements for a UE fulfilling not-at-cell edge and not-at-cell edge while stationary criteria	207

4.2B.2.9.7	Measurements for a UE fulfilling low mobility and not-at-cell edge criteria and not-at-cell-edge while stationary criteria	207

4.2B.2.9.8	Measurements for a UE fulfilling low mobility, not-at-cell edge and stationary criterion	207

4.2B.2.9.9	Measurements for UE fulfilling low mobility criterion	207

4.2B.2.9.10	Measurements for UE fulfilling not-at-cell edge criterion	210

4.2B.2.9.11	Measurements for UE fulfilling low mobility and not-at-cell edge criteria	212

4.2B.2.10	Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion	213

4.2B.2.10.1	Introduction	213

4.2B.2.10.2	Measurements for UE fulfilling stationary criterion	213

4.2B.2.10.3	Measurements for a UE fulfilling not-at-cell edge while stationary  criterion	215

4.2B.2.10.3A	Measurements for a UE fulfilling stationary and not-at-cell-edge criterion	216

4.2B.2.10.4	Measurements for a UE fulfilling low mobility and stationary criteria	216

4.2B.2.10.5	Measurements for a UE fulfilling low mobility and not-at-cell-edge while stationary criteria	216

4.2B.2.10.6	Measurements for a UE fulfilling not-at-cell edge and not-at-cell edge while stationary criteria	217

4.2B.2.10.7	Measurements for a UE fulfilling low mobility and not-at-cell edge criteria and not-at-cell-edge while stationary criteria	217

4.2B.2.10.8	Measurements for a UE fulfilling low mobility, not-at-cell edge and stationary  criteria	217

4.2B.2.10.9	Measurements for UE fulfilling low mobility criterion	217

4.2B.2.10.10	Measurements for UE fulfilling not-at-cell edge criterion	220

4.2B.2.10.11	Measurements for UE fulfilling low mobility and not-at-cell edge criterion	222

4.2B.2.11	Measurements of inter-RAT E-UTRAN cells for UE configured with relaxed measurement criterion	222

4.2B.2.11.1	Introduction	222

4.2B.2.11.2	Measurements for UE fulfilling stationary criterion	223

4.2B.2.11.3	Measurements for a UE fulfilling not-at-cell edge while stationary criterion	224

4.2B.2.11.3A	Measurements for a UE fulfilling stationary and not-at-cell-edge criterion	224

4.2B.2.11.4	Measurements for a UE fulfilling low mobility and stationary criteria	225

4.2B.2.11.5	Measurements for a UE fulfilling low mobility and not-at-cell-edge while stationary  criteria	225

4.2B.2.11.6	Measurements for a UE fulfilling not-at-cell edge and not-at-cell edge while stationary criteria	225

4.2B.2.11.7	Measurements for a UE fulfilling low mobility and not-at-cell edge criteria and not-at-cell-edge while stationary criteria	225

4.2B.2.11.8	Measurements for a UE fulfilling low mobility, not-at-cell edge and stationary  criteria	226

4.2B.2.11.9	Measurements for UE fulfilling low mobility criterion	226

4.2B.2.11.10	Measurements for UE fulfilling with not-at-cell edge criterion	227

4.2B.2.11.11	Measurements for UE fulfilling low mobility and not-at-cell edge criterion	228

4.2C	Cell Re-selection for NR UE for Satellite Access	229

4.2C.1	Introduction	229

4.2C.2	Requirements	229

4.2C.2.1	UE measurement capability	229

4.2C.2.2	Measurement and evaluation of serving cell	229

4.2C.2.3	Measurements of intra-frequency NR cells	230

4.2C.2.4	Measurements of inter-frequency NR cells	233

4.2C.2.5	Maximum interruption in paging reception	236

4.2C.2.6	Minimum requirement at transitions	237

4.2C.2.7	Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion	237

4.2C.2.8	Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion	237

4.2C.2.9	General requirements	237

4.2C.2.10	Measurements of inter-frequency NR cells with TN carrier	237

4.2C.2.11	Measurements of inter-RAT E-UTRAN cells with TN carrier	240

4.2C.3	Void	241

4.2C.4	Void	241

4.2D	Cell Re-selection for ATG	241

4.2D.1	Introduction	241

4.2D.2	Requirements	242

4.2D.2.1	UE measurement capability	242

4.2D.2.2	Measurement and evaluation of serving cell	242

4.2D.2.3	Measurements of intra-frequency NR cells	242

4.2D.2.4	Measurements of inter-frequency NR cells	243

4.2D.2.5	Maximum interruption in paging reception	245

4.2D.2.6	General requirements	245

4.3	Minimization of Drive Tests (MDT)	246

4.3.1	Introduction	246

4.3.2	Measurement Requirements	246

4.3.3	Requirements for Relative Time Stamp Accuracy	246

4.3.4	Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting	247

4.3.5	Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting	247

4.3C	Minimization of Drive Tests (MDT) for Satellite Access	247

4.3C.1	Introduction	247

4.3C.2	Measurement Requirements	248

4.3C.3	Requirements for Relative Time Stamp Accuracy	248

4.3C.4	Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting	248

4.3C.5	Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting	248

4.4	Idle Mode CA/DC Measurements	249

4.4.1	Introduction	249

4.4.2	Measurement Requirements	249

4.4.2.1	Detected cell requirement during state transition and Idle mode	249

4.4.2.2	Measurements of inter-frequency CA/DC candidate cells	250

4.4.2.3	Measurements on serving cell	251

4.4.2.4	Measurements of E-UTRAN inter-RAT DC candidate cells	251

4.5	NR measurements for positioning	251

4.5.1	Introduction	251

4.5.2	RSTD measurements	252

4.5.2.1	Introduction	252

4.5.2.2	Requirements Applicability	252

4.5.2.3	Measurement Capability	252

4.5.2.4	Measurement Reporting Requirements	252

4.5.2.5	Measurements Period Requirements	252

4.5.2.6	Measurements Period Requirements with Bandwidth Aggregation	256

4.5.3	PRS-RSRP measurements	259

4.5.3.1	Introduction	259

4.5.3.2	Requirements applicability	259

4.5.3.3	Measurement Capability	259

4.5.3.4	Measurement Reporting Requirements	259

4.5.3.5	Measurement Period Requirements	260

4.5.4	PRS-RSRPP measurements	262

4.5.4.1	Introduction	262

4.5.4.2	Requirements Applicability	262

4.5.4.3	Measurement Capability	262

4.5.4.4	Measurement Reporting Requirements	263

4.5.4.5	Measurement Period Requirements	263

4.5.5	Measurement requirements for DL RSCPD reported with RSTD	263

4.5.5.1	Introduction	263

4.5.5.2	Requirements Applicability	263

4.5.5.3	Measurement Capability	263

4.5.5.4	Measurement Reporting Requirements	263

4.5.5.5	Measurements Period Requirements	264

4.6	NR measurements for positioning for RedCap	268

4.6.1	Introduction	268

4.6.2	RSTD measurements for RedCap	268

4.6.2.1	Introduction	268

4.6.2.2	Requirements Applicability	269

4.6.2.3	Measurement Capability	269

4.6.2.4	Measurement Reporting Requirements	269

4.6.2.5	Measurements Period Requirements without RX FH	269

4.6.2.6	Measurement Period Requirements with RX FH	270

4.6.3	PRS-RSRP measurements for RedCap	272

4.6.3.1	Introduction	272

4.6.3.2	Requirements applicability	272

4.6.3.3	Measurement Capability	272

4.6.3.4	Measurement Reporting Requirements	272

4.6.3.5	Measurement Period Requirements without RX FH	273

4.6.3.6	Measurement Period Requirements with RX FH	275

4.6.4	PRS-RSRPP measurements for RedCap	277

4.6.4.1	Introduction	277

4.6.4.2	Requirements Applicability	277

4.6.4.3	Measurement Capability	277

4.6.4.4	Measurement Reporting Requirements	277

4.6.4.5	Measurement Period Requirements without RX FH	278

4.6.4.6	Measurement Period Requirements with RX FH	278

4.7	Measurement report for fast CA/DC setup	278

4.7.1	Introduction	278

4.7.2	Void	278

4.7.3	Measurement Report Requirements	278

5	SA: RRC\_INACTIVE state mobility	279

5.1	Cell Re-selection	279

5.1.1	Introduction	279

5.1.2	Requirements	279

5.1.2.1	UE measurement capability	279

5.1.2.2	Measurement and evaluation of serving cell	279

5.1.2.3	Measurements of intra-frequency NR cells	281

5.1.2.4	Measurements of inter-frequency NR cells	283

5.1.2.5	Measurements of inter-RAT E-UTRAN cells	285

5.1.2.6	Maximum interruption in paging reception	286

5.1.2.7	General requirements	286

5.1.2.8	Measurement of inter-frequency NR cells with NTN carrier	287

5.1.2.9	Minimum requirement at transitions	287

5.1.2.10	Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion	287

5.1.2.11	Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion	288

5.1.2.12	Measurements of inter-RAT E-UTRAN cells for UE configured with relaxed measurement criterion	289

5.1A	Cell Re-selection with CCA	289

5.1A.1	Introduction	289

5.1A.2	Requirements	290

5.1A.2.1	UE measurement capability	290

5.1A.2.2	Measurement and evaluation when CCA is used on the serving cell	290

5.1A.2.3	Measurements of intra-frequency NR cells when CCA is used on the serving cell and target cell	290

5.1A.2.4	Measurements of inter-frequency NR cells when CCA is used on the target cell	290

5.1A.2.5	Measurements of inter-RAT E-UTRAN cells when CCA is used on the serving cell	290

5.1A.2.6	Maximum interruption in paging reception when CCA is used on the target cell	290

5.1A.2.7	General requirements	290

5.1B	Cell Re-selection for RedCap	290

5.1B.1	Introduction	290

5.1B.2	Requirements	290

5.1B.2.1	UE measurement capability	290

5.1B.2.2	Measurement and evaluation of serving cell	290

5.1B.2.3	Measurements of intra-frequency NR cells	293

5.1B.2.4	Measurements of inter-frequency NR cells	295

5.1B.2.5	Measurements of inter-RAT E-UTRAN cells	297

5.1B.2.6	Maximum interruption in paging reception	298

5.1B.2.7	General requirements	298

5.1B.2.8	Minimum requirement at transitions	298

5.1B.2.9	Measurements of intra-frequency NR cells for UE configured with relaxed measurement criterion	298

5.1B.2.10	Measurements of inter-frequency NR cells for UE configured with relaxed measurement criterion	300

5.1B.2.11	Measurements of inter-RAT E-UTRAN cells for UE configured with relaxed measurement criterion	303

5.1C	Cell Re-selection for Satellite Access	304

5.1C.1	Introduction	304

5.1C.2	Requirements	304

5.1C.2.1	UE measurement capability	304

5.1C.2.2	Measurement and evaluation of serving cell	304

5.1C.2.3	Measurements of intra-frequency NR cells	304

5.1C.2.4	Measurements of inter-frequency NR cells	305

5.1C.2.5	Maximum interruption in paging reception	305

5.1C.2.6	General requirements	305

5.1C.2.7	Measurements of inter-frequency NR cells with TN carrier	305

5.1C.2.8	Measurements of inter-RAT E-UTRAN cells with TN carrier	305

5.1C.3	Void	305

5.1C.4	Void	305

5.1D	Cell Re-selection for ATG	305

5.1D.1	Introduction	305

5.1D.2	Requirements	305

5.1D.2.1	UE measurement capability	305

5.1D.2.2	Measurement and evaluation of serving cell	305

5.1D.2.3	Measurements of intra-frequency NR cells	305

5.1D.2.4	Measurements of inter-frequency NR cells	305

5.1D.2.5	Maximum interruption in paging reception	306

5.1D.2.6	General requirements	306

5.2	Void	306

5.2B	Configured Grant based Small Data Transmissions (CG-SDT) for RedCap	306

5.2B.1	Introduction	306

5.2B.2	Requirements on UE synchronization for small data transmissions for RedCap	306

5.2B.2.1	Void	306

5.2B.3	TA validation requirements for RedCap	306

5.2B.3.1	Void	307

5.2B.3.2	Void	307

5.2B.4	Scheduling restriction	307

5.2B.5	Applicability conditions for CG-SDT for RedCap	308

5.3	Minimization of Drive Tests (MDT)	308

5.3.1	Introduction	308

5.3.2	Measurement Requirements	308

5.3.3	Requirements for Relative Time Stamp Accuracy	308

5.3.4	Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting	308

5.3.5	Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting	308

5.3.6	Requirements for Relative Time Stamp Accuracy for RRC Resume Failure Log Reporting	308

5.3C	Minimization of Drive Tests (MDT) for Satellite Access	309

5.3C.1	Introduction	309

5.3C.2	Measurement Requirements	309

5.3C.3	Requirements for Relative Time Stamp Accuracy	309

5.3C.4	Requirements for Relative Time Stamp Accuracy for RRC Connection Establishment Failure Log Reporting	309

5.3C.5	Requirements for Relative Time Stamp Accuracy for Radio Link Failure and Handover Failure Log Reporting	309

5.3C.6	Requirements for Relative Time Stamp Accuracy for RRC Resume Failure Log Reporting	309

5.4	Inactive Mode CA/DC Measurements	310

5.4.1	Introduction	310

5.4.2	Measurement Requirements	310

5.4.2.1	Detected cell requirement during state transition and inactive mode	310

5.4.2.2	Measurements of inter-frequency CA/DC candidate cells	310

5.4.2.3	Measurements on serving cell	310

5.4.2.4	Measurements on E-UTRAN inter-RAT DC candidate cells	310

5.5	Configured Grant based Small Data Transmissions (CG-SDT)	310

5.5.1	Introduction	310

5.5.2	Requirements on UE synchronization for small data transmissions	310

5.5.3	TA validation requirements	310

5.5.4	Scheduling restriction	312

5.5.4.1	Scheduling availability of UE performing measurements in TDD bands on FR1	312

5.5.4.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	312

5.5.4.3	Scheduling availability of UE performing measurements on FR2	312

5.5.5	Applicability conditions for SDT	313

5.5D	Configured Grant based Small Data Transmissions (CG-SDT) for ATG	313

5.6	NR measurements for positioning	313

5.6.1	Introduction	313

5.6.1A	Cell re-selection for positioning	314

5.6.1A.1	Measurement and evaluation of serving cell	314

5.6.1A.2	Measurements of intra-frequency NR cells	315

5.6.2	RSTD measurements	316

5.6.2.1	Introduction	316

5.6.2.2	Requirements Applicability	316

5.6.2.3	Measurement Capability	316

5.6.2.5	Measurements Period Requirements	317

5.6.2.6	Measurements Period Requirements with Bandwidth Aggregation	320

5.6.3	PRS-RSRP measurements	323

5.6.3.1	Introduction	323

5.6.3.2	Requirements applicability	323

5.6.3.3	Measurement Capability	323

5.6.3.4	Measurement Reporting Requirements	323

5.6.3.5	Measurement Period Requirements	324

5.6.4	UE Rx-Tx time difference measurements	327

5.6.4.1	Introduction	327

5.6.4.2	Requirements Applicability	327

5.6.4.3	Measurement Capability	327

5.6.4.4	Measurement Reporting Requirements	327

5.6.4.5	Measurement Period Requirements	327

5.6.4.6	Measurement Period Requirements with Bandwidth Aggregation	331

5.6.5	PRS-RSRPP measurements	334

5.6.5.1	Introduction	334

5.6.5.2	Requirements Applicability	334

5.6.5.3	Measurement Capability	334

5.6.5.4	Measurement Reporting Requirements	334

5.6.5.5	Measurement Period Requirements	335

5.6.6	TA validation requirements for positioning	335

5.6.6.1	Introduction	335

5.6.6.2	TA validation requirements	335

5.6.6.3	TA validation requirements when configured with validity area	336

5.6.7	Measurement requirements for DL RSCPD reported with RSTD	337

5.6.7.1	Introduction	337

5.6.7.2	Requirements Applicability	337

5.6.7.3	Measurement Capability	337

5.6.7.4	Measurement Reporting Requirements	337

5.6.7.5	Measurements Period Requirements	337

5.6.8	Measurement requirements for DL RSCP reported with UE Rx-Tx time difference	340

5.6.8.1	Introduction	340

5.6.8.2	Requirements Applicability	340

5.6.8.3	Measurement Capability	340

5.6.8.4	Measurement Reporting Requirements	340

5.6.8.5	Measurement Period Requirements	341

5.6A	NR measurements for positioning for RedCap	343

5.6A.1	Introduction	343

5.6A.2	Cell re-selection for positioning	344

5.6A.2.1	Measurement and evaluation of serving cell	344

5.6A.2.2	Measurements of intra-frequency NR cells	345

5.6A.3	TA validation requirements for positioning SRS	346

5.6A.3.1	Introduction	346

5.6A.3.2	TA validation requirements	346

5.6A.3.3	TA validation requirements when configured with validity area	346

5.6A.4	RSTD measurements for RedCap	346

5.6A.4.1	 Introduction	346

5.6A.4.2	Requirements applicability	346

5.6A.4.3	Measurement Capability	347

5.6A.4.4	Measurement Reporting Requirements	347

5.6A.4.5	Measurement Period Requirement without RX FH	347

5.6A.4.6	Measurement Period Requirement with RX FH	351

5.6A.5	PRS-RSRP measurements for RedCap	352

5.6A.5.1	Introduction	352

5.6A.5.2	Requirements applicability	353

5.6A.5.3	Measurement Capability	353

5.6A.5.4	Measurement Reporting Requirements	353

5.6A.5.5	Measurement Period Requirements without RX FH	354

5.6A.5.6	Measurement Period Requirement with RX FH	356

5.6A.6	UE Rx-Tx time difference measurements for RedCap	358

5.6A.6.1	Introduction	358

5.6A.6.2	Requirements Applicability	358

5.6A.6.3	Measurement Capability	359

5.6A.6.4	Measurement Reporting Requirements	359

5.6A.6.5	Measurement Period Requirements without RX FH	359

5.6A.6.6	Measurement Period Requirements with RX FH	360

5.6A.7	PRS-RSRPP measurements for RedCap	362

5.6A.7.1	 Introduction	362

5.6A.7.2	Requirements applicability	362

5.6A.7.3	Measurement Capability	362

5.6A.7.4	Measurement Reporting Requirements	362

5.6A.7.5	Measurement Period Requirements without FH	363

5.6A.7.6	Measurement period requirement with FH	363

5.7	Random access based Small Data Transmissions (RA-SDT)	363

5.7.1	Introduction	363

5.7.2	Requirements for small data transmissions based on 2-step RA	363

5.7.3	Requirements for small data transmissions based on 4-step RA	363

5.7.4	Applicability conditions for SDT	363

5.7B	Random access based Small Data Transmissions (RA-SDT) for RedCap	364

5.7B.1	Introduction	364

5.7B.2	Requirements for small data transmissions based on 2-step RA	364

5.7B.3	Requirements for small data transmissions based on 4-step RA	364

5.7B.4	Applicability conditions for RA-SDT for RedCap	364

5.7D	Random access based Small Data Transmissions (RA-SDT) for ATG	364

5.8	Measurement report for fast CA/DC setup	364

5.8.1	Introduction	364

5.8.2	Void	365

5.8.3	Measurement Report Requirements	365

6	RRC\_CONNECTED state mobility	365

6.1	Handover	365

6.1.1	NR Handover	365

6.1.1.1	Introduction	365

6.1.1.2	NR FR1 - NR FR1 Handover	365

6.1.1.2.1	Handover delay	365

6.1.1.2.2	Interruption time	365

6.1.1.3	NR FR2- NR FR1 Handover	367

6.1.1.3.1	Handover delay	367

6.1.1.3.2	Interruption time	367

6.1.1.4	NR FR2- NR FR2 Handover	368

6.1.1.4.1	Handover delay	368

6.1.1.4.2	Interruption time	368

6.1.1.5	NR FR1- NR FR2 Handover	369

6.1.1.5.1	Handover delay	369

6.1.1.5.2	Interruption time	369

6.1.2	NR Handover to other RATs	371

6.1.2.1	NR – E-UTRAN Handover	371

6.1.2.1.1	Introduction	371

6.1.2.1.2	Handover delay	371

6.1.2.1.3	Interruption time	371

6.1.2.2	NR – UTRAN Handover	371

6.1.2.2.1	Introduction	371

6.1.2.2.2	Handover delay	372

6.1.2.2.3	Interruption time	372

6.1.3	NR DAPS Handover	372

6.1.3.1	Introduction	372

6.1.3.2	NR FR1 - NR FR1 DAPS Handover	373

6.1.3.2.1	DAPS handover delay	373

6.1.3.2.2	Interruption time	374

6.1.3.3	NR FR2- NR FR1 DAPS Handover	375

6.1.3.3.1	DAPS handover delay	376

6.1.3.3.2	Interruption time	376

6.1.3.4	NR FR1- NR FR2 DAPS Handover	376

6.1.3.4.1	DAPS handover delay	377

6.1.3.4.2	Interruption time	377

6.1.4	NR Conditional Handover	378

6.1.4.1	Introduction	378

6.1.4.2	NR FR1 – NR FR1 conditional handover	378

6.1.4.2.2	Measurement time	378

6.1.4.3	NR FR2 – NR FR1 conditional handover	380

6.1.4.4	NR FR2 – NR FR2 conditional handover	380

6.1.4.4.1	Handover delay	380

6.1.4.4.2	Measurement time	381

6.1.4.4.3	Preparation time	382

6.1.4.4.4	Interruption time	382

6.1.4.5	NR FR1 – NR FR2 conditional handover	382

6.1.5	NR Handover with PSCell	382

6.1.5.1	Introduction	382

6.1.5.2	Handover with PSCell from NR SA to EN-DC	383

6.1.5.2.1	Interruption time for inter-RAT HO from NR to E-UTRAN	383

6.1.5.2.2	PSCell addition in HO with PSCell for NR SA to EN-DC	383

6.1.5.3	HO with PSCell from NE-DC to NE-DC	384

6.1.5.3.1	Handover delay	384

6.1.5.3.2	HO with PSCell - PCell Interruption time	384

6.1.5.3.3	PSCell addition/change in NE-DC to NE-DC HO with PSCell	384

6.1.5.4	HO with PSCell from NR-DC to NR-DC	385

6.1.5.5	Handover with PSCell from NR SA to EN-DC with PSCell using CCA	386

6.1.5.5.1	Introduction	386

6.1.5.5.2	NR SA to EN-DC HO with PSCell- NR to E-UTRA HO Interruption time	386

6.1.5.5.3	NR SA to EN-DC HO with PSCell - NR PSCell Addition Delay requirements	387

6.1.6.1	Conditional handover including target MCG in FR1 and target SCG in FR1 in NR-DC	388

6.1.6.1.1	CHO with PSCell – PCell Interruption time	388

6.1.6.1.2	CHO with PSCell – PSCell change delay	389

6.1.6.2	Conditional handover including target MCG in FR1 and target SCG in FR2 in NR-DC	389

6.1.6.2.2	CHO with PSCell – PSCell change delay	390

6.1.7.1.2	PSCell conditional change delay	393

6.1.7.2	Conditional handover including target MCG in FR1 and Candidate SCG for CPC in FR2 in NR-DC	394

6.1.7.2.1	PCell handover delay	394

6.1.7.2.1.1	Measurement time	395

6.1.7.2.2	PSCell conditional change delay	395

6.1A	Void	397

6.1A.1	Void	397

6.1A.1.1	Void	397

6.1A.1.2	Void	397

6.1A.1.2.1	Void	397

6.1A.1.2.2	Void	397

6.1B	Handover to target cell using CCA	397

6.1B.1	NR Handover	397

6.1B.1.1	Introduction	397

6.1B.1.2	NR FR1 - NR FR1 Handover	397

6.1B.1.2.1	Handover delay	397

6.1B.1.2.2	Interruption time	397

6.1B.1.3	NR FR2-2 NR FR2-2 Handover	398

6.1B.1.3.1	Handover delay	398

6.1B.1.3.2	Interruption time	398

6.1B.1.4	NR FR1- NR FR2-2 Handover	399

6.1B.1.4.1	Handover delay	399

6.1B.1.4.2	Interruption time	400

6.1C	Handover for SAN	401

6.1C.1	NR SAN Handover	401

6.1C.1.1	Introduction	401

6.1C.1.2	NR SAN FR1 – NR SAN FR1 Handover	401

6.1C.1.2.1	Handover delay	401

6.1C.1.2.2	Interruption time	401

6.1C.1.3	NR SAN FR2-NTN – NR SAN FR2-NTN Handover	402

6.1C.1.3.1	Handover delay	402

6.1C.1.3.2	Interruption time	403

6.1C.2	NR SAN Conditional Handover	403

6.1C.2.1	Introduction	403

6.1C.2.2	NR SAN FR1 – NR SAN FR1 conditional handover	403

6.1C.2.2.1	Handover delay	404

6.1C.2.2.2	Measurement time	404

6.1C.2.2.3	Preparation time	405

6.1C.2.2.4	Interruption time	405

6.1C.2.3	NR SAN FR1 – NR SAN FR1 conditional handover without L3 measurement criteria	406

6.1C.2.3.1	Handover delay	406

6.1C.2.3.2	Preparation time	407

6.1C.2.3.3	Interruption time	407

6.1C.2.4	NR SAN FR2-NTN – NR SAN FR2-NTN conditional handover	407

6.1C.3	NR SAN Satellite switching with re-synchronization	408

6.1C.3.1	Introduction	408

6.1C.3.2	NR SAN FR1 – NR SAN FR1 Satellite switching with re-synchronization	408

6.1C.3.2.1	Satellite switching delay	408

6.1C.3.2.2	Interruption time for hard satellite switch with re-sync	408

6.1D	Handover for RedCap	409

6.1D.1	NR Handover	409

6.1D.1.1	Introduction	409

6.1D.1.2	NR FR1 - NR FR1 Handover	410

6.1D.1.2.1	Handover delay	410

6.1D.1.2.2	Interruption time	410

6.1D.1.3	NR FR2- NR FR2 Handover	411

6.1D.1.3.1	Handover delay	411

6.1D.1.3.2	Interruption time	412

6.1D.2	NR Handover to other RATs	413

6.1D.2.1	NR – E-UTRAN Handover	413

6.1E	Handover for ATG	413

6.1E.1	NR Handover	413

6.1E.1.1	Introduction	413

6.1E.1.2	NR FR1 - NR FR1 Handover	413

6.1E.1.2.1	Handover delay	413

6.1E.1.2.2	Interruption time	413

6.1E.2	NR Conditional Handover	414

6.1E.2.1	Introduction	414

6.1E.2.2	NR FR1 – NR FR1 conditional handover	414

6.1E.2.2.1	Handover delay	414

6.1E.2.2.2	Measurement time	415

6.1E.2.2.3	Preparation time	415

6.1E.2.2.4	Interruption time	416

6.2	RRC Connection Mobility Control	416

6.2.1	SA: RRC Re-establishment	416

6.2.1.1	Introduction	416

6.2.1.2	Requirements	416

6.2.1.2.1	UE Re-establishment delay requirement	416

6.2.1A	RRC Re-establishment with CCA	418

6.2.1A.1	Introduction	418

6.2.1A.2	Requirements	418

6.2.1A.2.1	UE Re-establishment with CCA delay requirement	418

6.2.1B	SA: RRC Re-establishment for RedCap	420

6.2.1B.1	Introduction	420

6.2.1B.2	Requirements	420

6.2.2	Random access	421

6.2.2.1	Introduction	421

6.2.2.2	Requirements for 4-step RA type	421

6.2.2.2.1	Contention based random access	421

6.2.2.2.1.1	Correct behaviour when transmitting Random Access Preamble	421

6.2.2.2.1.2	Correct behaviour when receiving Random Access Response	422

6.2.2.2.1.3	Correct behaviour when not receiving Random Access Response	422

6.2.2.2.1.4	Correct behaviour when receiving an UL grant for msg3 retransmission	422

6.2.2.2.1.5	SA: Correct behaviour when receiving a message over Temporary C-RNTI	422

6.2.2.2.1.6	Correct behaviour when contention Resolution timer expires	422

6.2.2.2.2	Non-Contention based random access	422

6.2.2.2.2.1	Correct behaviour when transmitting Random Access Preamble	422

6.2.2.2.2.2	Correct behaviour when receiving Random Access Response	423

6.2.2.2.2.3	Correct behaviour when not receiving Random Access Response	423

6.2.2.2.3	UE behaviour when configured with supplementary UL	423

6.2.2.3	Requirements for 2-step RA type	423

6.2.2.3.1	Contention based random access	424

6.2.2.3.1.1	Correct behaviour when transmitting MsgA	424

6.2.2.3.1.2	Correct behaviour when receiving MsgB	424

6.2.2.3.1.3	Correct behaviour when not receiving MsgB	424

6.2.2.3.2	Non-Contention based random access	424

6.2.2.3.2.1	Correct behaviour when transmitting MsgA	424

6.2.2.3.2.2	Correct behaviour when receiving MsgB	425

6.2.2.3.2.3	Correct behaviour when not receiving MsgB	425

6.2.2.3.3	UE behaviour when configured with supplementary UL	425

6.2.2A	Random access when CCA is used on target frequency	425

6.2.2A.1	Introduction	425

6.2.2A.2	Requirements for 4-step RA type	425

6.2.2A.2.1	Contention based random access	426

6.2.2A.2.1.1	Correct behaviour when transmitting Random Access Preamble	426

6.2.2A.2.1.2	Correct behaviour when receiving Random Access Response	426

6.2.2A.2.1.3	Correct behaviour when not receiving Random Access Response	426

6.2.2A.2.1.4	Correct behaviour when receiving an UL grant for msg3 retransmission	426

6.2.2A.2.1.6	Correct behaviour when contention Resolution timer expires	427

6.2.2A.2.2	Non-Contention based random access	427

6.2.2A.2.2.1	Correct behaviour when transmitting Random Access Preamble	427

6.2.2A.2.2.2	Correct behaviour when receiving Random Access Response	427

6.2.2A.2.2.3	Correct behaviour when not receiving Random Access Response	428

6.2.2A.3	Requirements for 2-step RA type	428

6.2.2A.3.1	Contention based random access	428

6.2.2A.3.1.1	Correct behaviour when transmitting MsgA	428

6.2.2A.3.1.2	Correct behaviour when receiving MsgB	429

6.2.2A.3.1.3	Correct behaviour when not receiving MsgB	429

6.2.2A.3.2	Non-Contention based random access	429

6.2.2A.3.2.1	Correct behaviour when transmitting MsgA	429

6.2.2A.3.2.2	Correct behaviour when receiving MsgB	430

6.2.2A.3.2.3	Correct behaviour when not receiving MsgB	430

6.2.2B	Random access for RedCap	430

6.2.2B.1	Introduction	430

6.2.2B.2	Requirements	430

6.2.2C	PDCCH ordered Random Access for LTM	431

6.2.2C.1	Introduction	431

6.2.2C.2	PDCCH ordered Random Access delay	431

6.2.3	SA: RRC Connection Release with Redirection	432

6.2.3.1	Introduction	432

6.2.3.2	Requirements	432

6.2.3.2.1	RRC connection release with redirection to NR	432

6.2.3.2.2	RRC connection release with redirection to E-UTRAN	433

6.2.3.2.3	RRC connection release with redirection to NR carrier subject to CCA	433

6.2.3A	SA: RRC Connection Release with Redirection for RedCap	434

6.2.3A.1	Introduction	434

6.2.3A.2	Requirements	435

6.2.3A.2.1	RRC connection release with redirection to NR	435

6.2.3A.2.2	RRC connection release with redirection to E-UTRAN	435

6.2C	RRC Connection Mobility Control for Satellite Access	435

6.2C.1	SA: RRC Re-establishment for Satellite Access	435

6.2C.1.1	Introduction	435

6.2C.1.2	Requirements	435

6.2C.1.2.1	UE Re-establishment delay requirement	436

6.2C.1.2.2	UE Re-establishment delay requirement for VSAT	437

6.2C.2	Random access for satellite access	437

6.2C.2.1	Introduction	437

6.2C.2.2	Requirements for 4-step RA type	437

6.2C.2.2.1	Contention based random access	438

6.2C.2.2.1.1	Correct behaviour when transmitting Random Access Preamble	438

6.2C.2.2.1.2	Correct behaviour when receiving Random Access Response	438

6.2C.2.2.1.3	Correct behaviour when not receiving Random Access Response	438

6.2C.2.2.1.4	Correct behaviour when receiving an UL grant for msg3 retransmission	438

6.2C.2.2.1.5	SA: Correct behaviour when receiving a message over Temporary C-RNTI	438

6.2C.2.2.1.6	Correct behaviour when Contention Resolution Timer expires	438

6.2C.2.2.2	Non-Contention based random access	439

6.2C.2.2.2.1	Correct behaviour when transmitting Random Access Preamble	439

6.2C.2.2.2.2	Correct behaviour when receiving Random Access Response	439

6.2C.2.2.2.3	Correct behaviour when not receiving Random Access Response	439

6.2C.2.3	Requirements for 2-step RA type	440

6.2C.2.3.1	Contention based random access	440

6.2C.2.3.1.1	Correct behaviour when transmitting MsgA	440

6.2C.2.3.1.2	Correct behaviour when receiving MsgB	440

6.2C.2.3.1.3	Correct behaviour when not receiving MsgB	441

6.2C.2.3.2	Non-Contention based random access	441

6.2C.2.3.2.1	Correct behaviour when transmitting MsgA	441

6.2C.2.3.2.2	Correct behaviour when receiving MsgB	441

6.2C.2.3.2.3	Correct behaviour when not receiving MsgB	441

6.2C.3	SA: RRC Connection Release with Redirection for Satellite Access	441

6.2C.3.1	Introduction	441

6.2C.3.2	Requirements	441

6.2C.3.2.1	RRC connection release with redirection to NR	441

6.2D	RRC Connection Mobility Control for ATG	442

6.2D.1	SA: RRC Re-establishment	442

6.2D.1.1	Introduction	442

6.2D.1.2	Requirements	443

6.2D.1.2.1	UE Re-establishment delay requirement	443

6.2D.2	Random access	444

6.2D.2.1	Introduction	444

6.2D.2.2	Requirements for 4-step RA type	444

6.2D.2.3	Requirements for 2-step RA type	444

6.2D.3	SA: RRC Connection Release with Redirection	444

6.2D.3.1	Introduction	444

6.2D.3.2	Requirements	445

6.2D.3.2.1	RRC connection release with redirection to NR	445

6.3	L1/L2-Triggered Mobility	445

6.3.1	LTM PCell Cell Switch	445

6.3.1.1	Introduction	445

6.3.1.2	LTM Cell Switch delay	447

6.3.1.3	Interruption time	447

7	Timing	449

7.1	UE transmit timing	449

7.1.1	Introduction	449

7.1.2	Requirements	450

7.1.2.1	Gradual timing adjustment	452

7.1.2.2	Void	452

7.1.2.3	One shot large UL timing adjustment for FR2 Power Class 6 UE	452

7.1.2.4	UE transmit timing for positioning measurements	453

7.1A	UE transmit timing for RedCap	453

7.1A.1	Introduction	453

7.1A.2	Requirements	454

7.1A.2.1	Gradual timing adjustment	455

7.1A.2.2	UE transmit timing for positioning measurements	455

7.1C	UE transmit timing for Satellite Access	455

7.1C.1	Introduction	455

7.1C.2	Requirements	455

7.1C.2.1	Gradual timing adjustment	457

7.1D	UE transmit timing for ATG	457

7.1D.1	Introduction	457

7.1D.2	Requirements	457

7.1D.2.1	Gradual timing adjustment	458

7.2	UE timer accuracy	459

7.2.1	Introduction	459

7.2.2	Requirements	459

7.2A	UE timer accuracy for RedCap	459

7.2A.1	Introduction	459

7.2A.2	Requirements	459

7.2C	UE timer accuracy for satellite access	459

7.2C.1	Introduction	459

7.2C.2	Requirements	460

7.2D	UE timer accuracy for ATG	460

7.2D.1	Introduction	460

7.2D.2	Requirements	460

7.3	Timing advance	460

7.3.1	Introduction	460

7.3.2	Requirements	461

7.3.2.1	Timing Advance adjustment delay	461

7.3.2.2	Timing Advance adjustment accuracy	461

7.3A	Timing Advance for RedCap	461

7.3A.1	Introduction	461

7.3A.2	Requirements	461

7.3A.2.1	Timing Advance adjustment delay	461

7.3A.2.2	Timing Advance adjustment accuracy	461

7.3C	Timing advance for satellite access	461

7.3C.1	Introduction	461

7.3C.2	Requirements	462

7.3C.2.1	Timing Advance adjustment delay	462

7.3C.2.2	Timing Advance adjustment accuracy	462

7.3D	Timing advance for ATG	462

7.3D.1	Introduction	462

7.3D.2	Requirements	462

7.3D.2.1	Timing Advance adjustment delay	462

7.3D.2.2	Timing Advance adjustment accuracy	462

7.4	Cell phase synchronization accuracy	463

7.4.1	Definition	463

7.4.2	Minimum requirements	463

7.5	Maximum Transmission Timing Difference	463

7.5.1	Introduction	463

7.5.2	Minimum requirements for inter-band EN-DC	463

7.5.2.1	Minimum requirements for inter-band synchronous EN-DC	464

7.5.3	Minimum requirements for intra-band EN-DC	464

7.5.4	Minimum requirements for NR Carrier Aggregation	465

7.5.5	Minimum requirements for inter-band NE-DC	465

7.5.5.1	Minimum requirements for inter-band synchronous NE-DC	466

7.5.6	Minimum requirements for inter-band NR-DC	466

7.5.7	Minimum requirements for multi-TRP	467

7.6	Maximum Receive Timing Difference	467

7.6.1	Introduction	467

7.6.2	Minimum requirements for inter-band EN-DC	468

7.6.2.1	Minimum requirements for inter-band synchronous EN-DC	468

7.6.3	Minimum requirements for intra-band EN-DC	469

7.6.4	Minimum requirements for NR Carrier Aggregation	469

7.6.5	Minimum requirements for inter-band NE-DC	470

7.6.5.1	Minimum requirements for inter-band synchronous NE-DC	470

7.6.6	Minimum requirements for inter-band NR-DC	471

7.6.7	Minimum requirements for PC6 UE in FR2	472

7.6.8	Minimum requirements for Multi-TRPs	472

7.7 *deriveSSB-IndexFromCell* tolerance	473

7.7.1	Minimum requirements	473

7.7A	deriveSSB-IndexFromCell tolerance for RedCap	473

7.7A.1	Minimum requirements	473

7.7D	DeriveSSB-IndexFromCell tolerance for ATG	473

7.7D.1	Minimum requirements	473

7.8	Void	474

7.9 *deriveSSB-IndexFromCellInter-r17* tolerance	474

7.9.1	Minimum requirements	474

7.9D *DeriveSSB-IndexFromCellInter-r17* tolerance for ATG	474

7.9D.1	Minimum requirements	474

8	Signalling characteristics	476

8.1	Radio Link Monitoring	476

8.1.1	Introduction	476

8.1.1.1	Introduction of Requirement on Radio Link Monitoring for UE Configured with Relaxed Measurement Criteria	477

8.1.2	Requirements for SSB based radio link monitoring	478

8.1.2.1	Introduction	478

8.1.2.2	Minimum requirement	479

8.1.2.3	Measurement restrictions for SSB based RLM	483

8.1.2.4	Minimum requirement of SSB based radio link monitoring for UE fulfilling relaxed measurement criteria	484

8.1.3	Requirements for CSI-RS based radio link monitoring	485

8.1.3.1	Introduction	485

8.1.3.2	Minimum requirement	485

8.1.3.3	Measurement restrictions for CSI-RS based RLM	489

8.1.3.4	Minimum requirement of CSI-RS based radio link monitoring for UE fulfilling relaxed measurement criteria	490

8.1.4	Minimum requirement at transitions	491

8.1.5	Minimum requirement for UE turning off the transmitter	492

8.1.6	Minimum requirement for L1 indication	492

8.1.7	Scheduling availability of UE during radio link monitoring	492

8.1.7.1	Scheduling availability of UE performing radio link monitoring with a same subcarrier spacing as PDSCH/PDCCH on FR1	492

8.1.7.2	Scheduling availability of UE performing radio link monitoring with a different subcarrier spacing than PDSCH/PDCCH on FR1	492

8.1.7.3	Scheduling availability of UE performing radio link monitoring on FR2	493

8.1.7.4	Scheduling availability of UE performing radio link monitoring on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC	494

8.1.8	Minimum requirement under IDC Interference	494

8.1A	Radio Link Monitoring with CCA on Target Frequency	494

8.1A.1	Introduction	494

8.1A.2	Requirements for SSB Based Radio Link Monitoring	495

8.1A.2.1	Introduction	495

8.1A.2.2	Minimum Requirement	496

8.1A.3	Minimum requirement at transitions	499

8.1A.4	Minimum requirement for UE turning off the transmitter	499

8.1A.5	Minimum requirement for L1 indication	499

8.1A.6	Scheduling availability of UE during radio link monitoring	500

8.1A.6.3	Scheduling availability of UE performing radio link monitoring on FR2-2	500

8.1A.6.4	Scheduling availability of UE performing radio link monitoring on FR1 or FR2-2 in case of FR1-FR2-2 inter-band CA and NR-DC	501

8.1B	Radio Link Monitoring for RedCap	501

8.1B.1	Introduction	501

8.1B.2	Requirements for SSB based radio link monitoring	502

8.1B.2.1	Introduction	502

8.1B.2.2	Minimum requirement	502

8.1B.2.3	Measurement restrictions for SSB based RLM	504

8.1B.3	Requirements for CSI-RS based radio link monitoring	505

8.1B.3.1	Introduction	505

8.1B.3.2	Minimum requirement	505

8.1B.3.3	Measurement restrictions for CSI-RS based RLM	508

8.1B.4	Minimum requirement at transitions	508

8.1B.5	Minimum requirement for UE turning off the transmitter	509

8.1B.6	Minimum requirement for L1 indication	509

8.1B.7	Scheduling availability of UE during radio link monitoring	509

8.1B.7.1	Scheduling availability of UE performing radio link monitoring with a same subcarrier spacing as PDSCH/PDCCH on FR1	509

8.1B.7.2	Scheduling availability of UE performing radio link monitoring with a different subcarrier spacing than PDSCH/PDCCH on FR1	509

8.1B.7.3	Scheduling availability of UE performing radio link monitoring on FR2	510

8.1C	Radio Link Monitoring for Satellite Access	510

8.1C.1	Introduction	510

8.1C.2	Requirements for SSB based radio link monitoring	511

8.1C.2.1	Introduction	511

8.1C.2.2	Minimum requirement	512

8.1C.2.3	Measurement restrictions for SSB based RLM	513

8.1C.3	Requirements for CSI-RS based radio link monitoring	513

8.1C.3.1	Introduction	513

8.1C.3.2	Minimum requirement	514

8.1C.3.3	Measurement restrictions for CSI-RS based RLM	515

8.1C.4	Minimum requirement at transitions	516

8.1C.5	Minimum requirement for UE turning off the transmitter	516

8.1C.6	Minimum requirement for L1 indication	516

8.1C.7	Scheduling availability of UE during radio link monitoring	517

8.1C.7.1	Scheduling availability of UE performing radio link monitoring with a same subcarrier spacing as PDSCH/PDCCH on FR1 and FR2-NTN	517

8.1C.7.2	Scheduling availability of UE performing radio link monitoring with a different subcarrier spacing than PDSCH/PDCCH on FR1 and FR2-NTN	517

8.1D	Radio Link Monitoring for ATG	517

8.1D.1	Introduction	517

8.1D.2	Requirements for SSB based radio link monitoring	518

8.1D.2.1	Introduction	518

8.1D.2.2	Minimum requirement	518

8.1D.2.3	Measurement restrictions for SSB based RLM	519

8.1D.3	Requirements for CSI-RS based radio link monitoring	520

8.1D.3.1	Introduction	520

8.1D.3.2	Minimum requirement	520

8.1D.3.3	Measurement restrictions for CSI-RS based RLM	521

8.1D.4	Minimum requirement at transitions	521

8.1D.5	Minimum requirement for UE turning off the transmitter	521

8.1D.6	Minimum requirement for L1 indication	521

8.1D.7	Scheduling availability of UE during radio link monitoring	522

8.1D.7.1	Scheduling availability of UE performing radio link monitoring with a same subcarrier spacing as PDSCH/PDCCH on FR1	522

8.1D.7.2	Scheduling availability of UE performing radio link monitoring with a different subcarrier spacing than PDSCH/PDCCH on FR1	522

8.2	Interruption	522

8.2.1	EN-DC Interruption	522

8.2.1.1	Introduction	522

8.2.1.2	Requirements	523

8.2.1.2.1	Interruptions at transitions between active and non-active during DRX	523

8.2.1.2.2	Interruptions at transitions from non-DRX to DRX	523

8.2.1.2.3	Interruptions at SCell addition/release	523

8.2.1.2.4	Interruptions at SCell activation/deactivation	525

8.2.1.2.5	Interruptions during measurements on SCC	527

8.2.1.2.5.1	Interruptions during measurements on deactivated NR SCC	527

8.2.1.2.5.2	Interruptions during measurements on deactivated E-UTRAN SCC	527

8.2.1.2.5.3	Interruptions during CQI measurements on dormant E-UTRAN SCell	527

8.2.1.2.5.4	Interruptions during RRM measurements on dormant E-UTRAN SCC	528

8.2.1.2.6	Interruptions at UL carrier RRC reconfiguration	528

8.2.1.2.7	Interruptions due to Active BWP switching Requirement	529

8.2.1.2.8	Interruptions at direct SCell activation and hibernation	530

8.2.1.2.8.1	Interruptions during direct SCell activation and hibernation of E-UTRA SCell	530

8.2.1.2.8.2	Interruptions during direct SCell activation	530

8.2.1.2.9	Interruptions at SCell hibernation	530

8.2.1.2.10	Interruptions at SCell activation/deactivation with multiple downlink SCells	531

8.2.1.2.11	Interruptions due to UE-specific CBW change	531

8.2.1.2.12	Interruptions at NR SRS carrier based switching	531

8.2.1.2.13	Interruptions at E-UTRA SRS carrier based switching	533

8.2.1.2.14	DL Interruptions at switching between two uplink carriers	534

8.2.1.2.15	Interruptions due to SCell dormancy	534

8.2.1.2.15.1	Interruptions due to SCell dormancy switch	534

8.2.1.2.15.2	Interruptions due to CQI measurements during SCell dormancy	534

8.2.1.2.15.3	Interruptions due to RRM measurements during SCell dormancy	535

8.2.1.2.16	Interruptions when identifying CGI of an NR cell with autonomous gaps	535

8.2.1.2.17	Interruptions when identifying CGI of an E-UTRA cell with autonomous gaps	535

8.2.1.2.18	Interruptions at NR SRS antenna port switching	536

8.2.1.2.19	Interruptions at fast SCell activation	537

8.2.1.2.20	Interruptions due to PUCCH SCell activation/deactivation	537

8.2.2	SA: Interruptions with Standalone NR Carrier Aggregation	538

8.2.2.1	Introduction	538

8.2.2.2	Requirements	539

8.2.2.2.1	Interruptions at SCell addition/release	539

8.2.2.2.2	Interruptions at SCell activation/deactivation	540

8.2.2.2.3	Interruptions during measurements on deactivated SCC	541

8.2.2.2.4	Interruptions at UL carrier RRC reconfiguration	542

8.2.2.2.5	Interruptions due to Active BWP switching Requirement	542

8.2.2.2.6	Interruptions at inter-frequency SFTD measurement	543

8.2.2.2.7	Interruptions at SCell activation/deactivation with multiple downlink SCells	544

8.2.2.2.8	Interruptions due to UE-specific CBW change	545

8.2.2.2.9	Interruptions at NR SRS carrier based switching	545

8.2.2.2.10	DL Interruptions at UE switching between two uplink carriers	546

8.2.2.2.10A	DL Interruptions at UE switching between two uplink carriers with two transmit antenna connectors	547

8.2.2.2.10B	DL Interruptions at UE switching between one uplink band with one transmit antenna connector and one uplink band with two transmit antenna connectors	547

8.2.2.2.10C	DL Interruptions at UE switching between two uplink bands with two transmit antenna connectors	548

8.2.2.2.10D	DL Interruptions at UE switching across three or four uplink bands	548

8.2.2.2.11	Interruptions at direct SCell activation	549

8.2.2.2.12	Interruptions due to SCell dormancy	549

8.2.2.2.12.1	Interruptions due to SCell dormancy switch	549

8.2.2.2.12.2	Interruptions due to CQI measurements during SCell dormancy	549

8.2.2.2.12.3	Interruptions due to RRM measurements during SCell dormancy	550

8.2.2.2.13	Interruptions at transitions between active and non-active during DRX	550

8.2.2.2.14	Interruptions when identifying CGI of an NR cell with autonomous gaps	550

8.2.2.2.15	Interruptions when identifying CGI of an E-UTRA cell with autonomous gaps	550

8.2.2.2.16	Interruptions at NR SRS antenna port switching	551

8.2.2.2.17	Interruptions at fast SCell activation	552

8.2.2.2.18	Interruptions due to PUCCH SCell activation/deactivation	552

8.2.2.2.19	Interruptions due to measurements without gap carried out by UE supporting *NeedForInterruptionInfoNR* 553

8.2.2.2.20	Interruptions due to PDCCH ordered RACH on target LTM cell	554

8.2.2.2.21	Interruptions at NR SRS bandwidth aggregation for positioning	554

8.2.3	NE-DC Interruptions	556

8.2.3.1	Introduction	556

8.2.3.2	Requirements	557

8.2.3.2.1	Interruptions at transitions between active and non-active during DRX	557

8.2.3.2.2	Interruptions at transitions from non-DRX to DRX	557

8.2.3.2.3	Interruptions at PSCell/SCell addition/release	557

8.2.3.2.4	Interruptions at SCell activation/deactivation	558

8.2.3.2.5	Interruptions during measurements on SCC	559

8.2.3.2.5.1	Interruptions during measurements on deactivated NR SCC	559

8.2.3.2.5.2	Interruptions during measurements on deactivated E-UTRAN SCC	559

8.2.3.2.5.3	Interruptions during CQI measurements on dormant E-UTRAN SCC	560

8.2.3.2.5.4	Interruptions during RRM measurements on dormant E-UTRAN SCC	560

8.2.3.2.6	Interruptions at UL carrier RRC reconfiguration	560

8.2.3.2.7	Interruptions due to Active BWP switching Requirement	561

8.2.3.2.8	Interruptions at direct SCell activation and hibernation	561

8.2.3.2.9	Interruptions at SCell hibernation	561

8.2.3.2.10	Interruptions at SCell activation/deactivation with multiple downlink SCells	562

8.2.3.2.11	Interruptions at NR SRS carrier based switching	562

8.2.3.2.12	Interruptions at E-UTRA SRS carrier based switching	563

8.2.3.2.13	Interruptions due to SCell dormancy	564

8.2.3.2.14	Interruptions when identifying CGI of an NR cell with autonomous gaps	564

8.2.3.2.15	 Interruptions when identifying CGI of an E-UTRA cell with autonomous gaps	565

8.2.3.2.17	Interruptions at fast SCell activation	567

8.2.3.2.18	Interruptions due to UE-specific CBW change	567

8.2.3.2.19	Interruptions due to PUCCH SCell activation/deactivation	567

8.2.4	NR-DC: Interruptions	568

8.2.4.1	Introduction	568

8.2.4.2	Requirements	568

8.2.4.2.1	Interruptions at PSCell/SCell addition/release	568

8.2.4.2.2	Interruptions at SCell activation/deactivation	569

8.2.4.2.3	Interruptions during measurements on SCC	570

8.2.4.2.4	Interruptions at UL carrier RRC reconfiguration	570

8.2.4.2.5	Interruptions due to Active BWP switching Requirement	571

8.2.4.2.6	Interruptions at transitions between active and non-active during DRX	571

8.2.4.2.7	Interruptions at transitions from non-DRX to DRX	571

8.2.4.2.8	Interruptions at SCell activation/deactivation with multiple downlink SCells	572

8.2.4.2.9	Interruptions at NR SRS carrier based switching	572

8.2.4.2.10	Interruptions at direct SCell activation	573

8.2.4.2.11	Interruptions when identifying CGI of an NR cell with autonomous gaps	574

8.2.4.2.12	Interruptions when identifying CGI of an E-UTRA cell with autonomous gaps	574

8.2.4.2.13	 Interruptions due to SCell dormancy	575

8.2.4.2.14	Interruptions at NR SRS antenna port switching	575

8.2.4.2.15	Interruptions at fast SCell activation	576

8.2.4.2.16	Interruptions at SCG activation/deactivation	577

8.2.4.2.17	Interruptions due to RRM measurements on deactivated SCG	577

8.2.4.2.18	Interruptions during RLM/BFD measurements on deactivated PSCell	577

8.2.4.2.19	Interruptions due to UE-specific CBW change	577

8.2.4.2.20	Interruptions due to PDCCH ordered RACH on target LTM cell	578

8.2.4.2.21	Interruptions at PSCell Cell switch	578

8.2.4.2A	Void	579

8.2.4.2A.1	Void	579

8.2.4.2A.2	Void	579

8.2.4.2A.3	Void	579

8.3	SCell Activation and Deactivation Delay	579

8.3.1	Introduction	579

8.3.2	SCell Activation Delay Requirement for Deactivated SCell	579

8.3.3	SCell Deactivation Delay Requirement for Activated SCell	586

8.3.4	Direct SCell Activation at SCell addition	586

8.3.5	Direct SCell Activation at Handover	588

8.3.7	SCell Activation Delay Requirement for Deactivated SCell with Multiple Downlink SCells	590

8.3.8	SCell Deactivation Delay Requirement for Activated SCell with Multiple Downlink SCells	594

8.3.9	Direct SCell Activation of Multiple Downlink SCells at SCell addition	594

8.3.10	Direct SCell Activation of Multiple Downlink SCells at Handover	596

8.3.12	SCell Activation Delay Requirement for Deactivated PUCCH SCell	597

8.3.13	SCell activation delay Requirement for Deactivated PUCCH SCell with Multiple SCells	600

8.3.14	SCell Deactivation Delay Requirement for Activated PUCCH SCell	603

8.3.15	SCell Deactivation Delay Requirement for Activated PUCCH SCell with Multiple Downlink SCells	603

8.3.16	Fast SCell Activation Delay Requirement for Deactivated SCell	603

8.3.17	SCell Activation Delay Requirement for Deactivated SCell with the L3 reporting during activation	606

8.3.18	SCell Activation Delay Requirement for Deactivated SCell with Multiple Downlink SCells with L3 reporting	609

8.3A	SCell Activation and Deactivation Delay in Carriers with CCA	612

8.3A.1	Introduction	612

8.3A.2	SCell Activation Delay Requirement for Deactivated SCell	612

8.3A.3	SCell Deactivation Delay Requirement for Activated SCell	617

8.4	UE UL carrier RRC reconfiguration delay	617

8.4.1	Introduction	617

8.4.2	UE UL carrier configuration delay requirement	617

8.4.3	UE UL carrier deconfiguration delay requirement	618

8.5	Link Recovery Procedures	618

8.5.1	Introduction	618

8.5.1.1	Introduction of Requirement on Link Recovery Procedures for UE configured with relaxed measurement criteria	619

8.5.2	Requirements for SSB based beam failure detection	620

8.5.2.1	Introduction	620

8.5.2.2	Minimum requirement	621

8.5.2.3	Measurement restriction for SSB based beam failure detection	624

8.5.2.4	Minimum requirement of SSB based beam failure detection for UE fulfilling relaxed measurement criteria	625

8.5.3	Requirements for CSI-RS based beam failure detection	626

8.5.3.1	Introduction	626

8.5.3.2	Minimum requirement	626

8.5.3.3	Measurement restrictions for CSI-RS beam failure detection	630

8.5.3.4	Minimum requirement of CSI-RS based beam failure detection for UE fulfilling relaxed measurement criteria	632

8.5.4	Minimum requirement for L1 indication	632

8.5.5	Requirements for SSB based candidate beam detection	633

8.5.5.1	Introduction	633

8.5.5.2	Minimum requirement	633

8.5.5.3	Measurement restriction for SSB based candidate beam detection	636

8.5.6	Requirements for CSI-RS based candidate beam detection	637

8.5.6.1	Introduction	637

8.5.6.2	Minimum requirement	637

8.5.6.3	Measurement restriction for CSI-RS based candidate beam detection	641

8.5.7	Scheduling availability of UE during beam failure detection	642

8.5.7.1	Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1	642

8.5.7.2	Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH on FR1	642

8.5.7.3	Scheduling availability of UE performing beam failure detection on FR2	642

8.5.7.4	Scheduling availability of UE performing beam failure detection on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC	643

8.5.8	Scheduling availability of UE during candidate beam detection	643

8.5.8.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	643

8.5.8.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	644

8.5.8.3	Scheduling availability of UE performing L1-RSRP measurement on FR2	644

8.5.8.4	Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC	645

8.5.9	Requirements for Beam Failure Recovery in SCell	645

8.5.9.1	Introduction	645

8.5.9.2	Requirement	645

8.5.10	Minimum requirement at transitions for beam failure detection	645

8.5.11	Minimum requirement under IDC Interference	646

8.5A	Link Recovery Procedures when CCA is used on target frequency	646

8.5A.1	Introduction	646

8.5A.2	Requirements for SSB based beam failure detection	647

8.5A.2.1	Introduction	647

8.5A.2.2	Minimum requirement	647

8.5A.2.3	Measurement restriction for SSB based beam failure detection	649

8.5A.3	Void	650

8.5A.4	Minimum requirement for L1 indication	650

8.5A.5	Requirements for SSB based candidate beam detection	650

8.5A.5.1	Introduction	650

8.5A.5.2	Minimum requirement	650

8.5A.5.3	Measurement restriction for SSB based candidate beam detection	652

8.5A.6	Void	653

8.5A.7	Scheduling availability of UE during beam failure detection	653

8.5A.7.1	Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH	653

8.5A.7.2	Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH	653

8.5A.7.3	Scheduling availability of UE performing beam failure detection on FR2-2	653

8.5A.7.4	Scheduling availability of UE performing beam failure detection on FR1 or FR2-2 in case of FR1-FR2-2 inter-band CA and NR-DC	653

8.5A.8	Scheduling availability of UE during candidate beam detection	653

8.5A.8.3	Scheduling availability of UE performing L1-RSRP measurement on FR2-2	654

8.5.8A.4	Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2-2 in case of FR1-FR2-2 inter-band CA and NR-DC	654

8.5B	Link Recovery Procedures for Redcap	654

8.5B.1	Introduction	654

8.5B.2	Requirements for SSB based beam failure detection for Redcap	654

8.5B.2.1	Introduction	654

8.5B.2.2	Minimum requirement	655

8.5B.2.3	Measurement restriction for SSB based beam failure detection	656

8.5B.3	Requirements for CSI-RS based beam failure detection for Redcap	657

8.5B.3.1	Introduction	657

8.5B.3.2	Minimum requirement	657

8.5B.3.3	Measurement restrictions for CSI-RS beam failure detection	659

8.5B.4	Minimum requirement for L1 indication for Redcap	660

8.5B.5	Requirements for SSB based candidate beam detection for Redcap	660

8.5B.5.1	Introduction	660

8.5B.5.2	Minimum requirement	660

8.5B.5.3	Measurement restriction for SSB based candidate beam detection	662

8.5B.6	Requirements for CSI-RS based candidate beam detection for Redcap	662

8.5B.6.1	Introduction	662

8.5B.6.2	Minimum requirement	663

8.5B.6.3	Measurement restriction for CSI-RS based candidate beam detection	665

8.5B.7	Scheduling availability of UE during beam failure detection for Redcap	665

8.5B.7.1	Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1	665

8.5B.7.2	Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH on FR1	665

8.5B.7.3	Scheduling availability of UE performing beam failure detection on FR2	665

8.5B.8	Scheduling availability of UE during candidate beam detection for Redcap	666

8.5B.8.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	666

8.5B.8.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	666

8.5B.8.3	Scheduling availability of UE performing L1-RSRP measurement on FR2	666

8.5B.9	Minimum requirement at transitions for beam failure detection for Redcap	667

8.5C	Link Recovery Procedures for Satellite Access	667

8.5C.1	Introduction	667

8.5C.2	Requirements for SSB based beam failure detection	667

8.5C.2.1	Introduction	667

8.5C.2.2	Minimum requirement	668

8.5C.2.3	Measurement restriction for SSB based beam failure detection	669

8.5C.3	Requirements for CSI-RS based beam failure detection	669

8.5C.3.1	Introduction	669

8.5C.3.2	Minimum requirement	669

8.5C.3.3	Measurement restrictions for CSI-RS beam failure detection	670

8.5C.4	Minimum requirement for L1 indication	671

8.5C.5	Requirements for SSB based candidate beam detection	671

8.5C.5.1	Introduction	671

8.5C.5.2	Minimum requirement	671

8.5C.5.3	Measurement restriction for SSB based candidate beam detection	672

8.5C.6	Requirements for CSI-RS based candidate beam detection	673

8.5C.6.1	Introduction	673

8.5C.6.2	Minimum requirement	673

8.5C.6.3	Measurement restriction for CSI-RS based candidate beam detection	674

8.5C.7	Scheduling availability of UE during beam failure detection	674

8.5C.7.1	Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1	674

8.5C.7.2	Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH on FR1	674

8.5C.8	Scheduling availability of UE during candidate beam detection	674

8.5C.8.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	675

8.5C.8.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	675

8.5C.9	Minimum requirement at transitions for beam failure detection	675

8.5D	Link Recovery Procedures for ATG	675

8.5D.1	Introduction	675

8.5D.2	Requirements for SSB based beam failure detection	676

8.5D.2.1	Introduction	676

8.5D.2.2	Minimum requirement	676

8.5D.2.3	Measurement restriction for SSB based beam failure detection	677

8.5D.3	Requirements for CSI-RS based beam failure detection	677

8.5D.3.1	Introduction	677

8.5D.3.2	Minimum requirement	677

8.5D.3.3	Measurement restrictions for CSI-RS beam failure detection	678

8.5D.4	Minimum requirement for L1 indication	679

8.5D.5	Requirements for SSB based candidate beam detection	679

8.5D.5.1	Introduction	679

8.5D.5.2	Minimum requirement	679

8.5D.5.3	Measurement restriction for SSB based candidate beam detection	680

8.5D.6	Requirements for CSI-RS based candidate beam detection	680

8.5D.6.1	Introduction	680

8.5D.6.2	Minimum requirement	680

8.5D.6.3	Measurement restriction for CSI-RS based candidate beam detection	681

8.5D.7	Scheduling availability of UE during beam failure detection	681

8.5D.7.1	Scheduling availability of UE performing beam failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1	682

8.5D.7.2	Scheduling availability of UE performing beam failure detection with a different subcarrier spacing than PDSCH/PDCCH on FR1	682

8.5D.8	Scheduling availability of UE during candidate beam detection	682

8.5D.8.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	682

8.5D.8.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	682

8.5D.9	Minimum requirement at transitions for beam failure detection	682

8.6	Active BWP switch delay	682

8.6.1	Introduction	682

8.6.2	DCI and timer based BWP switch delay on a single CC	683

8.6.2A	DCI based BWP switch delay on multiple CCs	684

8.6.2A.1	Simultaneous DCI based BWP switch delay on multiple CCs	684

8.6.2A.2	Non-simultaneous DCI based BWP switch delay on multiple CCs	686

8.6.2B	Timer based BWP switch delay on multiple CCs	686

8.6.2B.1	Simultaneous timer based BWP switch delay on multiple CCs	686

8.6.2B.2	Non-simultaneous timer based BWP switch delay on multiple CCs	686

8.6.3	RRC based BWP switch delay on a single CC	687

8.6.3A	RRC based BWP switch delay on multiple CCs	688

8.6.3A.1	Simultaneous RRC based BWP switch delay on multiple CCs	688

8.6.3A.2	Non-simultaneous RRC based BWP switch delay on multiple CCs	688

8.6.4	BWP switch delay on Consistent UL CCA recovery	689

8.6A	Active BWP switch delay for RedCap	689

8.6A.1	Introduction	689

8.6A.2	DCI and timer based BWP switch delay on a single CC	689

8.6A.3	RRC based BWP switch delay on a single CC	691

8.6C	Active BWP switch delay for satellite access	691

8.6C.1	Introduction	691

8.6C.2	DCI and timer based BWP switch delay on a single CC	691

8.6C.3	RRC based BWP switch delay on a single CC	693

8.6D	Active BWP switch delay for ATG	693

8.6D.1	Introduction	693

8.6D.2	DCI and timer based BWP switch delay	693

8.6D.3	RRC based BWP switch delay on a single CC	694

8.7	Void	695

8.8	NE-DC: E-UTRAN PSCell Addition and Release Delay	695

8.8.1	Introduction	695

8.8.2	E-UTRAN PSCell Addition Delay Requirement	695

8.8.3	E-UTRAN PSCell Release Delay Requirement	695

8.9	NR-DC: PSCell Addition and Release Delay	696

8.9.1	Introduction	696

8.9.2	PSCell Addition Delay Requirement	696

8.9.3	PSCell Release Delay Requirement	697

8.9A	Conditional PSCell Addition Delay	697

8.9A.1	Introduction	697

8.9A.2	Conditional PSCell Addition Delay Requirement	697

8.9A.2.1	Measurement time	698

8.9B	NR-DC: PSCell Addition and Release Delay in Carriers with CCA	698

8.9B.1	Introduction	698

8.9B.2	PSCell Addition Delay Requirement	698

8.9B.3	PSCell Release Delay Requirement	699

8.9C	Subsequent Conditional PSCell Addition Delay	699

8.9C.1	Introduction	699

8.9C.2	Subsequent Conditional PSCell Addition Delay Requirement	699

8.9C.2.1	Measurement time	700

8.10	Active TCI state switching delay	700

8.10.3A	MAC-CE based TCI state switch delay in HST FR2 scenarios	701

8.10.4	DCI based TCI state switch delay	702

8.10.5	RRC based TCI state switch delay	702

8.10.6	Active TCI state list update delay	703

8.10A	Active TCI state switching delay with CCA	703

8.10A.1	Introduction	703

8.10A.2	Known conditions for TCI state	703

8.10A.3	MAC-CE based TCI state switch delay	703

8.10A.4	DCI based TCI state switch delay	704

8.10A.5	RRC based TCI state switch delay	705

8.10A.6	Active TCI state list update delay	705

8.10B	Active TCI state switching delay for RedCap	706

8.10B.1	Introduction	706

8.10B.2	Known conditions for TCI state	706

8.10B.3	MAC-CE based TCI state switch delay	706

8.10B.4	DCI based TCI state switch delay	707

8.10B.5	RRC based TCI state switch delay	707

8.10B.6	Active TCI state list update delay	708

8.10C	Active TCI state switching delay for satellite access	708

8.10C.1	Introduction	708

8.10C.2	MAC-CE based TCI state switch delay	708

8.10C.4	DCI based TCI state switch delay	708

8.10C.5	RRC based TCI state switch delay	709

8.10C.6	Active TCI state list update delay	709

8.10D	Active TCI state switching delay for ATG	709

8.10D.2	Void	709

8.10D.6	Active TCI state list update delay	710

8.10E	Active TCI state switching delay for UE operating in FR2-1 and configured with groupBasedBeamReporting-r17	710

8.10E.1	Introduction	710

8.10E.2	Known conditions for TCI state	710

8.10E.3	MAC-CE based dual DL TCI state switch delay	711

8.10E.3.1	MAC-CE based dual DL TCI state switching delay for sDCI	711

8.10E.3.2	MAC-CE based dual DL TCI state switching delay for mDCI	711

8.10E.4	DCI based dual DL TCI state switch delay for sDCI and mDCI	711

8.10E.4.1	DCI based dual DL TCI state switching delay for sDCI	711

8.10E.4.2	DCI based dual DL TCI state switching delay for mDCI	712

8.10E.5	RRC based dual DL TCI state switch delay	712

8.10E.6	Active DL TCI state list update delay	712

8.10E.6.1	Active DL TCI state list update delay for sDCI	712

8.10E.6.2	Active DL TCI state list update delay for mDCI	712

8.11	PSCell Change	712

8.11A	PSCell Change in Carriers with CCA	713

8.11B	Conditional PSCell Change	713

8.11B.1	Introduction	713

8.11B.2	Conditional PSCell Change delay	713

8.11B.2.1	Measurement time	714

8.11D	Conditional PSCell Change in Carriers with CCA	714

8.11D.1	Introduction	714

8.11D.2	Conditional PSCell Change delay	715

8.11D.2.1	Measurement time	715

8.11E	Subsequent Conditional PSCell Change	716

8.11E.1	Introduction	716

8.11E.2	Subsequent Conditional PSCell Change delay	716

8.11E.2.1	Measurement time	717

8.12	Uplink spatial relation switch delay	717

8.12.1	Introduction	717

8.12.2	Known conditions for spatial relation when associated with DL-RS	717

8.12.3	MAC-CE based spatial relation switch delay	717

8.12.4	DCI based spatial relation switch delay	718

8.12.5	RRC based spatial relation switch delay	718

8.12A	Uplink spatial relation switch delay for RedCap	719

8.12A.1	Introduction	719

8.12A.2	Known conditions for spatial relation when associated with DL-RS	719

8.12A.3	MAC-CE based spatial relation switch delay	719

8.12A.4	DCI based spatial relation switch delay	720

8.12A.5	RRC based spatial relation switch delay	720

8.12C	Uplink spatial relation switch delay for satellite access	721

8.12C.1	Void	721

8.12C.2	Void	721

8.12C.3	Void	721

8.12C.4	Void	721

8.12C.5	Void	721

8.13	UE-specific CBW change	721

8.13.1	Introduction	721

8.13.2	UE-specific CBW change delay	721

8.13A	UE-specific CBW change for RedCap	722

8.13A.1	Introduction	722

8.13A.2	UE-specific CBW change delay	722

8.13C	UE-specific CBW change for satellite access	722

8.13C.1	Introduction	722

8.13C.2	UE-specific CBW change delay	722

8.13D	UE-specific CBW change for ATG	723

8.13D.1	Introduction	723

8.13D.2	UE-specific CBW change delay	723

8.14	Pathloss reference signal switching delay	723

8.14.1	Introduction	723

8.14.2	Known conditions for pathloss reference signal	723

8.14.3	MAC-CE based pathloss reference signal switch delay	724

8.14C	Pathloss reference signal switching delay for satellite access	724

8.14C.1	Introduction	724

8.14C.2	Known conditions for pathloss reference signal	724

8.14C.3	MAC-CE based pathloss reference signal switch delay	725

8.14D	Pathloss reference signal switching delay for ATG	725

8.14D.1	Introduction	725

8.14D.2	Known conditions for pathloss reference signal	725

8.14D.3	MAC-CE based pathloss reference signal switch delay	725

8.15	Active downlink TCI state switching delay for unified TCI	726

8.15.1	Introduction	726

8.15.4	DCI based downlink TCI state switch delay	727

8.15.5	Active Downlink TCI state list update delay	728

8.15D	Active downlink TCI state switching delay for unified TCI for ATG	729

8.15D.1	Introduction	729

8.15D.2	Void	729

8.15D.4	DCI based downlink TCI state switch delay	729

8.15D.5	Active Downlink TCI state list update delay	729

8.16	Active uplink TCI state switching delay for unified TCI	730

8.16.1	Introduction	730

8.16.4	DCI based uplink TCI state switch delay	732

8.16.5	Active Uplink TCI state list update delay	732

8.16D	Active uplink TCI state switching delay for unified TCI for ATG	734

8.16D.1	Introduction	734

8.16D.2	Void	734

8.16D.3	MAC-CE based uplink TCI state switch delay	734

8.16D.4	DCI based uplink TCI state switch delay	735

8.16D.5	Active Uplink TCI state list update delay	735

8.17	SCG Activation and Deactivation Delay	736

8.17.1	Introduction	736

8.17.2	SCG Activation Delay Requirement	736

8.17.3	SCG Deactivation Delay Requirement	737

8.18	TRP specific Link Recovery Procedures	737

8.18.1	Introduction	737

8.18.2	Requirements for TRP specific SSB based beam failure detection	738

8.18.2.1	Introduction	738

8.18.2.2	Minimum requirement	738

8.18.2.3	Measurement restriction for SSB based beam failure detection	740

8.18.3	Requirements for CSI-RS based beam failure detection	741

8.18.3.1	Introduction	741

8.18.3.2	Minimum requirement	741

8.18.3.3	Measurement restrictions for CSI-RS beam failure detection	745

8.18.4	Minimum requirement for L1 indication	746

8.18.5	Requirements for SSB based candidate beam detection	746

8.18.5.1	Introduction	746

8.18.5.2	Minimum requirement	746

8.18.5.3	Measurement restriction for SSB based candidate beam detection	749

8.18.6	Requirements for CSI-RS based candidate beam detection	750

8.18.6.1	Introduction	750

8.18.6.2	Minimum requirement	750

8.18.6.3	Measurement restriction for CSI-RS based candidate beam detection	752

8.18.7	Requirements for TRP specific Beam Failure Recovery	753

8.18.7.1	Introduction	753

8.18.7.2	Requirement	754

8.18.8	Scheduling availability of UE during TRP specific beam failure detection	754

8.18.8.1	Scheduling availability of UE performing TRP specific beam failure detection with a same subcarrier spacing as PDSCH/PDCCH on FR1	754

8.18.8.2	Scheduling availability of UE performing TRP specific beam failure detection with a different subcarrier spacing than PDSCH/PDCCH on FR1	754

8.18.8.3	Scheduling availability of UE performing TRP specific beam failure detection on FR2	754

8.18.8.4	Scheduling availability of UE performing TRP specific beam failure detection on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC	755

8.18.9	Scheduling availability of UE during TRP specific candidate beam detection	755

8.18.9.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	755

8.18.9.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	756

8.18.9.3	Scheduling availability of UE performing L1-RSRP measurement on FR2	756

8.18.9.4	Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA and NR-DC	756

8.19	Pre-configured measurement gap activation/deactivation delay	757

8.19.1	Introduction	757

8.19.2	Pre-configured measurement gap activation/deactivation upon DCI/timer-based BWP switch	757

8.19.2.1	Activation/deactivation upon DCI/timer-based BWP switch delay on a single CC	757

8.19.3	Pre-configured measurement gap activation/deactivation upon SCell activation/deactivation	757

8.19.4	Pre-configured measurement gap activation/deactivation upon RRC reconfiguration	757

8.19.5	Activation/deactivation delay requirements for concurrent measurement gaps with Pre-MG	757

8.19.5.1	Activation/deactivation delay requirements for non-overlapped activation/deactivation of concurrent measurement gaps with Pre- MG	758

8.19.5.2	Activation/deactivation delay requirements for fully overlapped activation/deactivation of concurrent measurement gaps with Pre- MG	758

8.19.5.3	Pre-MG activation/deactivation delay when colliding with a concurrent measurement gap	758

8.19D	Pre-configured measurement gap activation/deactivation delay for ATG	758

8.19D.1	Introduction	758

8.19D.2	Pre-configured measurement gap activation/deactivation upon DCI/timer-based BWP switch	758

8.19D.2.1	Activation/deactivation upon DCI/timer-based BWP switch delay on a single CC	758

8.19D.3	Pre-configured measurement gap activation/deactivation upon RRC reconfiguration	759

8.20	LTM PSCell Cell Switch	759

8.20.1	Introduction	759

8.20.2	LTM Cell Switch delay	760

8.20.3	Void	760

8.21	Active downlink TCI state switching delay for unified TCI for single-DCI mTRP	760

8.21.1	Introduction	760

8.21.2	Known conditions for downlink TCI state	760

8.21.3	MAC-CE based downlink TCI state switch delay	761

8.21.4	DCI based downlink TCI state switch delay	762

8.21.5	Active Downlink TCI state list update delay	762

8.22	Active downlink TCI state switching delay for unified TCI for multi-DCI mTRP	763

8.22.1	Introduction	763

8.22.2	Known conditions for downlink TCI state	763

8.22.3	MAC-CE based downlink TCI state switch delay	763

8.22.4	DCI based downlink TCI state switch delay	765

8.22.5	Active Downlink TCI state list update delay	765

8.23	Active uplink TCI state switching delay for unified TCI for single-DCI mTRP	766

8.23.1	Introduction	766

8.23.2	Known conditions for uplink TCI state	766

8.23.3	MAC-CE based uplink TCI state switch delay	766

8.23.4	DCI based uplink TCI state switch delay	768

8.23.5	Active uplink TCI state list update delay	768

8.24	Active uplink TCI state switching delay for unified TCI for multi-DCI mTRP	769

8.24.1	Introduction	769

8.24.2	Known conditions for uplink TCI state	769

8.24.3	MAC-CE based uplink TCI state switch delay	770

8.24.4	DCI based uplink TCI state switch delay	771

8.24.5	Active Uplink TCI state list update delay	771

8.25	TCI state activation for LTM candidate cell	772

8.25.1	Introduction	772

8.25.2	Known TCI state conditions	772

8.25.3	SSB based TCI state activation delay	773

9	Measurement Procedure	774

9.1	General measurement requirement	774

9.1.1	Introduction	774

9.1.2	Measurement gap	774

9.1.2.1	EN-DC: Measurement Gap Sharing	784

9.1.2.1a	SA: Measurement Gap Sharing	784

9.1.2.1b	NE-DC: Measurement Gap Sharing	785

9.1.2.1c	NR-DC: Measurement Gap Sharing	786

9.1.3	UE Measurement capability	787

9.1.3.1	EN-DC: Monitoring of multiple layers using gaps	787

9.1.3.1a	SA: Monitoring of multiple layers using gaps	788

9.1.3.1b	NE-DC: Monitoring of multiple layers using gaps	788

9.1.3.1c	NR-DC: Monitoring of multiple layers using gaps	789

9.1.3.2	EN-DC: Maximum allowed layers for multiple monitoring	789

9.1.3.2a	SA: Maximum allowed layers for multiple monitoring	790

9.1.3.2b	NE-DC: Maximum allowed layers for multiple monitoring	791

9.1.3.2c	NR-DC: Maximum allowed layers for multiple monitoring	791

9.1A.3.2	Void	792

9.1.3A	UE Measurement capability under operation mode with CCA	792

9.1.3A.1	EN-DC: Monitoring of multiple layers using gaps under CCA	792

9.1.3A.1a	SA: Monitoring of multiple layers using gaps under CCA	792

9.1.3A.2	EN-DC: Maximum allowed layers for multiple monitoring under CCA	792

9.1.3A.2a	SA: Maximum allowed layers for multiple monitoring under CCA	793

9.1.3C	UE Measurement capability under operation mode with satellite access	793

9.1.3C.1a	SA: Monitoring of multiple layers using gaps under satellite access	793

9.1.3C.2a	SA: Maximum allowed layers for multiple monitoring for SAN	794

9.1.4	Capabilities for Support of Event Triggering and Reporting Criteria	794

9.1.4.1	Introduction	794

9.1.4.2	Requirements	794

9.1.5	Carrier-specific scaling factor	797

9.1.5.1	Monitoring of multiple layers outside gaps	797

9.1.5.1.1	EN-DC mode: carrier-specific scaling factor for SSB-based, CSI-RS based L3 measurements and RSSI and channel occupancy measurements performed outside gaps	800

9.1.5.1.2	SA mode: carrier-specific scaling factor for SSB-based, CSI-RS based L3 measurements and RSSI and channel occupancy measurements performed outside gaps	802

9.1.5.1.3	NR-DC mode: carrier-specific scaling factor for SSB-based and CSI-RS based L3 measurements performed outside gaps	803

9.1.5.1.4	NE-DC mode: carrier-specific scaling factor for SSB-based and CSI-RS based measurements performed outside gaps	803

9.1.5.2	Monitoring of multiple layers within gaps	805

9.1.5.2.1	EN-DC mode: carrier-specific scaling factor for SSB, CSI-RS-based L3 measurements and RSSI and channel occupancy measurements performed within gaps	807

9.1.5.2.2	SA mode: carrier-specific scaling factor for SSB, CSI-RS-based L3 measurements and RSSI and channel occupancy measurements performed within gaps	809

9.1.5.2.3	NE-DC: carrier-specific scaling factor for SSB-based and CSI-RS based L3 measurements performed within gaps	811

9.1.5.2.4	NR-DC: carrier-specific scaling factor for SSB-based and CSI-RS-based L3 measurements performed within gaps	813

9.1.5.2.5	SA mode: carrier-specific scaling factor for PRS-based measurements performed within gaps	815

9.1.5.2.6	NE-DC: carrier-specific scaling factor for PRS-based measurements performed within gaps	815

9.1.5.2.7	NR-DC: carrier-specific scaling factor for PRS-based measurements performed within gaps	815

9.1.5.3	Monitoring of multiple layers within NCSG	816

9.1.5.3.1	SA mode: carrier-specific scaling factor for measurements performed within NCSG	817

9.1.5.4	L1-RSRP measurements within measurement gap	818

9.1.5.4.1	SA mode: carrier-specific scaling factor for L1-RSRP measurements performed within measurement gap	819

9.1.5.4.2	NR-DC: carrier-specific scaling factor for L1-RSRP measurements performed within measurement gap	820

9.1.6	Minimum requirement at transitions	822

9.1.7	Pre-configured measurement gap	823

9.1.7.1	Introduction	823

9.1.7.2	Requirements applicability	823

9.1.7.3	Requirements	823

9.1.7.3.1	Requirements for autonomous activation/deactivation mechanism	823

9.1.7.3.2	Requirements for network-controlled activation/deactivation mechanism	824

9.1.7.3.3	Requirements for reception/transmission during activation/deactivation	825

9.1.8	Concurrent measurement gaps	825

9.1.8.1	Introduction	825

9.1.8.2	Requirements	825

9.1.8.3	Collision between concurrent measurement gaps	826

9.1.8.4	Measurement gap related requirements of concurrent measurement gaps	827

9.1.9	Network controlled small gap	827

9.1.9.1	Introduction	827

9.1.9.2	Requirements applicability	828

9.1.10	MUSIM gaps	830

9.1.10.1	Introduction	831

9.1.10.2	Priorities for MUSIM gaps	831

9.1.10.3	Keep solution for MUSIM gaps	832

9.1.10.4	Collisions between different MUSIM gaps	832

9.1.10.5	Collisions between MUSIM gaps and measurement gaps	832

9.1.10.6	MUSIM gap related requirements	833

9.1.11	UL gap for Tx power management	833

9.1.12	Concurrent measurement gaps with Pre-MG	833

9.1.12.1	Introduction	833

9.1.12.2	Requirements	833

9.1.12.3	Collisions involving Pre-MG(s)	834

9.1.12.4	Collision between Pre-MG activation/deactivation and measurement gap	835

9.1.12.5	Pre-MG related requirements	835

9.1.13	Concurrent measurement gaps with NCSG	835

9.1.13.1	Introduction	835

9.1.13.2	Requirements	835

9.1.13.3	Collision involving NCSGs	837

9.1A	General measurement requirement for RedCap	837

9.1A.1	Introduction	837

9.1A.2	Measurement gap	837

9.1A.2.1	SA: Measurement Gap Sharing	841

9.1A.3	UE Measurement capability	842

9.1A.3.1	SA: Monitoring of multiple layers using gaps	842

9.1A.3.2	SA: Maximum allowed layers for multiple monitoring	842

9.1A.4	Capabilities for Support of Event Triggering and Reporting Criteria	842

9.1A.4.1	Introduction	842

9.1A.4.2	Requirements	843

9.1A.5	Carrier-specific scaling factor	843

9.1A.5.1	Monitoring of multiple layers outside gaps	843

9.1A.5.1.1	SA mode: carrier-specific scaling factor for SSB-based measurements performed outside gaps	844

9.1A.5.2	Monitoring of multiple layers within gaps	844

9.1A.5.2.1	SA mode: carrier-specific scaling factor for SSB measurements performed within gaps	844

9.1A.6	Minimum requirement at transitions	846

9.1C	General measurement requirement for SAN	846

9.1C.1	Introduction	846

9.1C.2	Measurement gap	847

9.1C.8	Concurrent measurement gaps for SAN	849

9.1C.8.1	Introduction	849

9.1C.8.2	Requirements	849

9.1C.8.3	Collision between concurrent measurement gaps	850

9.1C.8.4	Measurement gap related requirements of concurrent measurement gaps	850

9.1C.9	Collision between SMTC and measurement gap for SAN	850

9.1C.9.1	Introduction	850

9.1C.9.2	Collision between SMTCs and measurement gap	850

9.1C.9.3	Collision between multiple SMTCs on a SAN carrier	851

9.1D	General measurement requirement for ATG	851

9.1D.1	Introduction	851

9.1D.2	Measurement gap	851

9.1D.2.1a	SA: Measurement Gap Sharing	853

9.1D.3	UE Measurement capability	854

9.1D.3.1	SA: Monitoring of multiple layers using gaps	854

9.1D.3.2	SA: Maximum allowed layers for multiple monitoring	854

9.1D.4	Void	854

9.1D.5	Carrier-specific scaling factor	854

9.1D.5.1	Monitoring of multiple layers outside gaps	854

9.1D.5.1.1	Void	855

9.1D.5.1.2	SA mode: carrier-specific scaling factor for SSB-based, CSI-RS based L3 measurements performed outside gaps	855

9.1D.5.2	Monitoring of multiple layers within gaps	855

9.1D.5.2.1	Void	856

9.1D.5.2.2	SA mode: carrier-specific scaling factor for SSB, CSI-RS-based L3 measurements performed within gaps	856

9.1D.6	Void	857

9.1D.7	Pre-configured measurement gap	857

9.1D.7.1	Introduction	857

9.1D.7.2	Requirements applicability	857

9.1D.7.3	Requirements	857

9.1D.7.3.1	Requirements for autonomous activation/deactivation mechanism	858

9.1D.7.3.2	Requirements for network-controlled activation/deactivation mechanism	858

9.1D.7.3.3	Requirements for reception/transmission during activation/deactivation	858

9.1D.8	Capabilities for Support of Event Triggering and Reporting Criteria	859

9.1D.8.1	Introduction	859

9.1D.8.2	Requirements	859

9.1D.9	Minimum requirement at transitions	859

9.2	NR intra-frequency measurements	860

9.2.1	Introduction	860

9.2.2	Requirements applicability	863

9.2.3	Number of cells and number of SSB	863

9.2.3.1	Requirements for FR1	863

9.2.3.2	Requirements for FR2	864

9.2.4	Measurement Reporting Requirements	864

9.2.4.1	Periodic Reporting	864

9.2.4.2	Event-triggered Periodic Reporting	864

9.2.4.3	Event Triggered Reporting	864

9.2.4.4	SCell activation Triggered Reporting	865

9.2.5	Intrafrequency measurements without measurement gaps	865

9.2.5.1	Intrafrequency cell identification	865

9.2.5.2	Measurement period	872

9.2.5.3	Scheduling availability of UE during intra-frequency measurements	876

9.2.5.3.1	Scheduling availability of UE performing measurements in TDD bands on FR1	876

9.2.5.3.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	877

9.2.5.3.3	Scheduling availability of UE performing measurements on FR2	877

9.2.5.3.4	Scheduling availability of UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA	879

9.2.5.4	SFTD Measurements between PCell and PSCell	879

9.2.5.4.1	Introduction	879

9.2.5.4.2	SFTD Measurement delay	879

9.2.5.4.3	SFTD Measurement Reporting Delay	880

9.2.6	Intra-frequency measurements with measurement gaps	880

9.2.6.1	Void	880

9.2.6.2	Intra-frequency cell identification	880

9.2.6.3	Intra-frequency Measurement Period	883

9.2.7	Intra-frequency measurements with NCSG	884

9.2.7.1	Intra-frequency cell identification	884

9.2.7.2	Measurement period	886

9.2.7.3	Scheduling availability during intra-frequency measurement with NCSG	887

9.2A	NR intra-frequency measurements with CCA	887

9.2A.1	Introduction	887

9.2A.2	Requirements applicability	888

9.2A.3	Number of cells and number of SSB	889

9.2A.3.1	Requirements for FR1	889

9.2A.3.2	Requirements for FR2-2	889

9.2A.4	Measurement Reporting Requirements	889

9.2A.5	Intra-frequency measurements without measurement gaps	890

9.2A.5.2	Measurement period	894

9.2A.5.3	Scheduling availability of UE during intra-frequency measurements	896

9.2A.5.3.1	Scheduling availability of UE performing measurements in TDD bands on FR1	897

9.2A.5.3.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	897

9.2A.5.3.3	Scheduling availability of UE performing measurements in TDD bands on FR2-2	897

9.2A.6	Intra-frequency measurements with measurement gaps	898

9.2A.6.1	Intra-frequency cell identification	898

9.2A.6.2	Intra-frequency Measurement Period	900

9.2A.7	Intra-frequency RSSI and Channel occupancy measurements	901

9.2A.7.1	Intra-frequency RSSI measurements	901

9.2A.7.2	Intra-frequency Channel occupancy measurements	903

9.2A.7.3	Scheduling restriction during RSSI and Channel Occupancy measurements in FR1	905

9.2A.7.4	Scheduling restriction during RSSI measurements in FR2-2	905

9.2B	NR intra-frequency measurements for RedCap	905

9.2B.1	Introduction	905

9.2B.2	Requirements applicability	906

9.2B.3	Number of cells and number of SSB	906

9.2B.3.1	Requirements for FR1	906

9.2B.3.2	Requirements for FR2	906

9.2B.4	Measurement Reporting Requirements	907

9.2B.4.1	Periodic Reporting	907

9.2B.4.2	Event-triggered Periodic Reporting	907

9.2B.4.3	Event Triggered Reporting	907

9.2B.5	Intra-frequency measurements without measurement gaps	908

9.2B.5.1	Intra-frequency cell identification	908

9.2B.5.2	Measurement period	910

9.2B.5.3	Scheduling availability of UE during intra-frequency measurements	911

9.2B.5.3.1	Scheduling availability of UE performing measurements in TDD bands on FR1	911

9.2B.5.3.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	911

9.2B.5.3.3	Scheduling availability of UE performing measurements on FR2	912

9.2B.5.3.4	Scheduling availability of HD-FDD UE performing measurements on FR1	912

9.2B.6	Intra-frequency measurements with measurement gaps	913

9.2B.6.1	Intra-frequency cell identification	913

9.2B.6.2	Intra-frequency Measurement Period	914

9.2C	NR intra-frequency measurements for SAN	915

9.2C.1	Introduction	915

9.2C.2	Requirements applicability	916

9.2C.3	Number of cells and number of SSB	916

9.2C.3.1	Requirements for FR1	916

9.2C.4	Measurement Reporting Requirements	917

9.2C.4.1	Periodic Reporting	917

9.2C.4.2	Event-triggered Periodic Reporting	917

9.2C.4.3	Event Triggered Reporting	917

9.2C.5	Intra-frequency measurements without measurement gaps	917

9.2C.5.1	Intra-frequency cell identification	917

9.2C.5.2	Measurement period	919

9.2C.5.3	Scheduling availability of UE during intra-frequency measurements	920

9.2C.5.3.1	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	920

9.2C.5.3.2	Scheduling availability of UE performing measurements on a neighbor cell served by a different satellite in LEO	920

9.2C.6	Intra-frequency measurements with measurement gaps	921

9.2C.6.1	Intra-frequency cell identification	921

9.2C.6.3	Intrafrequency Measurement Period	922

9.2C.7	Intra-frequency measurements without measurement gaps for NTN band above 10 GHz	922

9.2C.7.1	Intra-frequency cell identification	922

9.2C.7.2	Measurement period	924

9.2C.7.3	Scheduling availability of UE during intra-frequency measurements	924

9.2C.7.3.1	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on NTN bands above 10 GHz	924

9.2C.8	Intra-frequency measurements with measurement gaps for NTN band above 10 GHz	925

9.2C.8.1	Intra-frequency cell identification	925

9.2C.8.3	Intra-frequency Measurement Period	926

9.2D	NR intra-frequency measurements for ATG	926

9.2D.1	Introduction	926

9.2D.2	Requirements applicability	926

9.2D.3	Number of cells and number of SSB	927

9.2D.3.1	Requirements for FR1	927

9.2D.4	Measurement Reporting Requirements	927

9.2D.4.1	Periodic Reporting	927

9.2D.4.2	Event-triggered Periodic Reporting	927

9.2D.4.3	Event Triggered Reporting	927

9.2D.5	Intra-frequency measurements without measurement gaps	928

9.2D.5.1	Intra-frequency cell identification	928

9.2D.5.2	Measurement period	929

9.2D.5.3	Scheduling availability of UE during intra-frequency measurements	930

9.2D.5.3.1	Scheduling availability of UE performing measurements on FR1	930

9.2D.5.3.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	931

9.2D.6	Intra-frequency measurements with measurement gaps	931

9.2D.6.1	Void	931

9.2D.6.2	Intra-frequency cell identification	931

9.2D.6.3	Intra-frequency Measurement Period	933

9.3	NR inter-frequency measurements	933

9.3.1	Introduction	933

9.3.2	Requirements applicability	936

9.3.2.1	Void	937

9.3.2.2	Void	937

9.3.3	Number of cells and number of SSB	937

9.3.3.1	Requirements for FR1	937

9.3.3.2	Requirements for FR2	937

9.3.4	Inter-frequency measurement with measurement gaps	937

9.3.4.1	Void	942

9.3.4.2	Void	942

9.3.5	Inter-frequency measurements	942

9.3.5.1	Void	943

9.3.5.2	Void	943

9.3.5.3	Void	943

9.3.6	Inter-frequency measurements reporting requirements	943

9.3.6.1	Periodic Reporting	943

9.3.6.2	Event-triggered Periodic Reporting	943

9.3.6.3	Event-triggered Reporting	943

9.3.7	Void	944

9.3.8	Inter-frequency SFTD measurement requirements	944

9.3.8.1	Introduction	944

9.3.8.2	SFTD Measurement delay	944

9.3.8.3	SFTD Measurement reporting delay	945

9.3.9	Inter-frequency measurements without measurement gaps	946

9.3.9.1	Inter-frequency Cell identification	946

9.3.9.2	Measurement period	951

9.3.9.3	Scheduling availability of UE during inter-frequency measurements when the SSB is completely contained in the active BWP of the UE	953

9.3.9.3.1	Scheduling availability of UE performing measurements in TDD bands on FR1	953

9.3.9.3.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	954

9.3.9.3.3	Scheduling availability of UE performing measurements on FR2	954

9.3.9.3.4	Scheduling availability of UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA	955

9.3.9.4	Scheduling availability of UE during inter-frequency measurements when the SSB is not completely contained in the active BWP of the UE	955

9.3.9.4.1	Scheduling availability of UE performing measurements in TDD bands on FR1	955

9.3.9.4.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	956

9.3.9.4.3	Scheduling availability of UE performing measurements on FR2	956

9.3.9.4.4	Scheduling availability of UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA	958

9.3.10	Inter-frequency measurement with NCSG	958

9.3.10.1	Inter-frequency cell identification	958

9.3.10.2	Measurement period	960

9.3.10.3	Scheduling availability during inter-frequency measurement with NCSG	960

9.3.10.3.1	Scheduling availability of UE performing measurements in TDD bands on FR1	961

9.3.10.3.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	961

9.3.10.3.3	Scheduling availability of UE performing measurements on FR2	962

9.3.10.3.4	Scheduling availability of UE performing measurements on FR1 or FR2 in case of FR1-FR2 inter-band CA	963

9.3A	NR inter-frequency measurements in carrier frequencies with CCA	964

9.3A.1	Introduction	964

9.3A.2	Requirements applicability	964

9.3A.3	Number of cells and number of SSB	965

9.3A.3.1	Requirements for FR1	965

9.3A.3.2	Requirements for FR2-2	965

9.3A.4	Inter-frequency cell identification	965

9.3A.5	Inter-frequency measurements	967

9.3A.6	Inter-frequency measurements reporting requirements	969

9.3A.6.1	Periodic Reporting	969

9.3A.6.2	Event-triggered Periodic Reporting	969

9.3A.6.3	Event-triggered Reporting	969

9.3A.8	Inter-frequency RSSI measurements	969

9.3A.9	Inter-frequency channel occupancy measurements	970

9.3B	NR inter-frequency measurements for RedCap	971

9.3B.1	Introduction	971

9.3B.2	Requirements applicability	971

9.3B.3	Number of cells and number of SSB	972

9.3B.3.1	Requirements for FR1	972

9.3B.3.2	Requirements for FR2	972

9.3B.4	Inter-frequency measurement with measurement gaps	972

9.3B.5	Inter-frequency measurements	974

9.3B.6	Inter-frequency measurements reporting requirements	974

9.3B.6.1	Periodic Reporting	974

9.3B.6.2	Event-triggered Periodic Reporting	974

9.3B.6.3	Event-triggered Reporting	975

9.3B.7	Inter-frequency measurements without measurement gaps	975

9.3B.7.1	Inter-frequency Cell identification	975

9.3B.7.2	Measurement period	977

9.3B.7.3	Scheduling availability of UE during inter-frequency measurements	978

9.3B.7.3.1	Scheduling availability of UE performing measurements in TDD bands on FR1	978

9.3B.7.3.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	978

9.3B.7.3.3	Scheduling availability of UE performing measurements on FR2	979

9.3B.7.3.4	Scheduling availability of HD-FDD UE performing measurements on FR1	979

9.3C	NR inter-frequency measurements for SAN	979

9.3C.1	Introduction	979

9.3C.2	Requirements applicability	980

9.3C.3	Number of cells and number of SSB	981

9.3C.3.1	Requirements for FR1	981

9.3C.4	Inter-frequency measurement with measurement gaps	981

9.3C.5	Inter-frequency measurements	982

9.3C.6	Inter-frequency measurements reporting requirements	983

9.3C.6.1	Periodic Reporting	983

9.3C.6.2	Event-triggered Periodic Reporting	983

9.3C.6.3	Event-triggered Reporting	983

9.3C.7	Inter-frequency measurements without measurement gaps	984

9.3C.7.1	Inter-frequency Cell identification	984

9.3C.7.2	Measurement period	985

9.3C.7.3	Scheduling availability of UE during inter-frequency measurements	985

9.3C.7.3.1	Void	985

9.3C.7.3.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	985

9.3C.8	Inter-frequency measurement with measurement gaps for NTN band above 10 GHz	986

9.3C.9	Inter-frequency measurements for NTN band above 10 GHz	987

9.3C.10	Inter-frequency measurements without measurement gaps for NTN band above 10 GHz	987

9.3C.10.1	Inter-frequency Cell identification	987

9.3C.10.2	Measurement period	988

9.3C.10.3	Scheduling availability of UE during inter-frequency measurements	988

9.3C.10.3.1	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on NTN bands above 10 GHz	989

9.3D	NR inter-frequency measurements for ATG	989

9.3D.1	Introduction	989

9.3D.2	Requirements applicability	989

9.3D.3	Number of cells and number of SSB	990

9.3D.3.1	Requirements for FR1	990

9.3D.4	Inter-frequency measurement with measurement gaps	990

9.3D.5	Inter-frequency measurements	991

9.3D.6	Inter-frequency measurements reporting requirements	991

9.3D.6.1	Periodic Reporting	991

9.3D.6.2	Event-triggered Periodic Reporting	992

9.3D.6.3	Event-triggered Reporting	992

9.3D.7	Void	992

9.3D.8	Void	992

9.3D.9	Inter-frequency measurements without measurement gaps	992

9.3D.9.1	Inter-frequency Cell identification	992

9.3D.9.2	Measurement period	994

9.3D.9.3	Scheduling availability of UE during inter-frequency measurements	995

9.3D.9.3.1	Scheduling availability of UE performing measurements in TDD bands on FR1	995

9.3D.9.3.2	Scheduling availability of UE performing measurements with a different subcarrier spacing than PDSCH/PDCCH on FR1	995

9.4	Inter-RAT measurements	996

9.4.1	Introduction	996

9.4.2	NR − E-UTRAN FDD measurements	998

9.4.2.1	Introduction	998

9.4.2.2	Requirements when no DRX is used	999

9.4.2.3	Requirements when DRX is used	1000

9.4.2.4	Measurement reporting requirements	1001

9.4.2.4.1	Periodic Reporting	1001

9.4.2.4.2	Event-Triggered Periodic Reporting	1001

9.4.2.4.3	Event-Triggered Reporting	1002

9.4.2.5	Scheduling Availability During NR − E-UTRAN FDD measurements with NCSG	1002

9.4.3	NR − E-UTRAN TDD measurements	1002

9.4.3.1	Introduction	1002

9.4.3.2	Requirements when no DRX is used	1002

9.4.3.3	Requirements when DRX is used	1004

9.4.3.4	Measurement reporting requirements	1005

9.4.3.4.1	Periodic Reporting	1005

9.4.3.4.2	Event-Triggered Periodic Reporting	1005

9.4.3.4.3	Event-Triggered Reporting	1006

9.4.3.5	Scheduling Availability During NR − E-UTRAN TDD measurements with NCSG	1006

9.4.4	Inter-RAT RSTD measurements	1006

9.4.4.1	NR − E-UTRAN FDD RSTD measurements	1006

9.4.4.1.1	Introduction	1006

9.4.4.1.2	Requirements	1007

9.4.4.2	NR − E-UTRAN TDD RSTD measurements	1009

9.4.4.2.1	Introduction	1009

9.4.4.2.2	Requirements	1010

9.4.5	Inter-RAT E-CID measurements	1013

9.4.5.1	NR−E-UTRAN FDD E-CID RSRP and RSRQ measurements	1013

9.4.5.1.1	Introduction	1013

9.4.5.1.2	Requirements	1013

9.4.5.1.3	Measurement Reporting Delay	1013

9.4.5.2	NR−E-UTRAN TDD E-CID RSRP and RSRQ measurements	1014

9.4.5.2.1	Introduction	1014

9.4.5.2.2	Requirements	1014

9.4.5.2.3	Measurement Reporting Delay	1014

9.4.6	NR − UTRAN FDD measurements	1014

9.4.6.1	Introduction	1014

9.4.6.2	Requirements when no DRX is used	1014

9.4.6.3	Requirements when DRX is used	1015

9.4.7	NR – E-UTRAN measurements with autonomous gaps	1017

9.4.7.1	CGI identification of an E-UTRA cell with autonomous gaps	1017

9.4.7.2	CGI reporting delay	1017

9.4.8	NR – E-UTRAN measurements without measurement gaps	1018

9.4.8.1	Introduction	1018

9.4.8.2	General requirements	1018

9.4.8.3	NR − E-UTRAN FDD measurements	1019

9.4.8.3.1	Introduction	1019

9.4.8.3.2	Requirements when no DRX is used	1019

9.4.8.3.3	Requirements when DRX is used	1020

9.4.8.3.4	Measurement reporting requirements	1020

9.4.8.3.5	Scheduling availability during NR − E-UTRAN FDD measurements	1021

9.4.8.4	NR − E-UTRAN TDD measurements	1021

9.4.8.4.1	Introduction	1021

9.4.8.4.2	Requirements when no DRX is used	1022

9.4.8.4.3	Requirements when DRX is used	1023

9.4.8.4.4	Measurement reporting requirements	1024

9.4.8.4.5	Scheduling availability during NR − E-UTRAN TDD measurements	1024

9.4A	Inter-RAT measurements for RedCap	1025

9.4A.1	Introduction	1025

9.4A.2	NR − E-UTRAN FDD measurements	1026

9.4A.2.1	Introduction	1026

9.4A.2.2	Requirements when no DRX is used	1026

9.4A.2.3	Requirements when DRX is used	1027

9.4A.2.4	Measurement reporting requirements	1028

9.4A.2.4.1	Periodic Reporting	1028

9.4A.2.4.2	Event-Triggered Periodic Reporting	1028

9.4A.2.4.3	Event-Triggered Reporting	1028

9.4A.3	NR − E-UTRAN TDD measurements	1029

9.4A.3.1	Introduction	1029

9.4A.3.2	Requirements when no DRX is used	1029

9.4A.3.3	Requirements when DRX is used	1031

9.4A.3.4	Measurement reporting requirements	1032

9.4A.3.4.1	Periodic Reporting	1032

9.4A.3.4.2	Event-Triggered Periodic Reporting	1032

9.4A.3.4.3	Event-Triggered Reporting	1032

9.4A.4	NR – E-UTRAN measurements with autonomous gaps	1033

9.4A.4.1	CGI identification of an E-UTRA cell with autonomous gaps	1033

9.4A.4.2	CGI reporting delay	1033

9.4A.4.3	CGI reporting scheduling restriction	1033

9.5	L1-RSRP measurements for Reporting	1034

9.5.1	Introduction	1034

9.5.2	Requirements applicability	1034

9.5.3	Measurement Reporting Requirements	1035

9.5.3.1	Periodic Reporting	1035

9.5.3.2	Semi-Persistent Reporting	1036

9.5.3.3	Aperiodic Reporting	1036

9.5.4	L1-RSRP measurement requirements	1036

9.5.4.1	SSB based L1-RSRP Reporting	1036

9.5.4.2	CSI-RS based L1-RSRP Reporting	1042

9.5.4A	Void	1046

9.5.4A.1	Void	1046

9.5.5	Measurement restriction for CSI-RS and SSB for L1-RSRP measurement	1046

9.5.5.1	Measurement restriction for SSB based L1-RSRP	1046

9.5.5.2	Measurement restriction for CSI-RS based L1-RSRP	1047

9.5.6	Scheduling availability of UE during L1-RSRP measurement	1048

9.5.6.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	1048

9.5.6.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	1048

9.5.6.3	Scheduling availability of UE performing L1-RSRP measurement on FR2	1049

9.5.6.4	Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA	1051

9.5.7	Minimum requirement at transitions	1051

9.5A	L1-RSRP measurements for Reporting under CCA	1051

9.5A.1	Introduction	1051

9.5A.2	Requirements applicability	1051

9.5A.3	Measurement Reporting Requirements	1052

9.5A.3.1	Periodic Reporting	1052

9.5A.3.2	Semi-Persistent Reporting	1052

9.5A.3.3	Aperiodic Reporting	1052

9.5A.4	L1-RSRP measurement requirements	1053

9.5A.4.1	SSB based L1-RSRP Reporting	1053

9.5A.5	Measurement restriction for L1-RSRP measurement	1055

9.5A.5.1	Measurement restriction for SSB based L1-RSRP	1055

9.5A.6	Scheduling availability of UE during L1-RSRP measurement	1056

9.5A.6.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	1056

9.5A.6.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	1056

9.5A.6.3	Void	1056

9.5A.6.3A	Scheduling availability of UE performing L1-RSRP measurement in case of FR1-FR2 inter-band CA	1056

9.5A.6.3B	Scheduling availability of UE performing L1-RSRP measurement on FR2-2	1056

9.5A.6.4	Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA	1057

9.5B	L1-RSRP measurements for Reporting for RedCap	1057

9.5B.1	Introduction	1057

9.5B.2	Requirements applicability	1057

9.5B.3	Measurement Reporting Requirements	1058

9.5B.3.1	Periodic Reporting	1058

9.5B.3.2	Semi-Persistent Reporting	1058

9.5B.3.3	Aperiodic Reporting	1059

9.5B.4	L1-RSRP measurement requirements	1059

9.5B.4.1	SSB based L1-RSRP Reporting	1059

9.5B.4.2	CSI-RS based L1-RSRP Reporting	1061

9.5B.5	Measurement restriction for CSI-RS and SSB for L1-RSRP measurement	1064

9.5B.5.1	Measurement restriction for SSB based L1-RSRP	1064

9.5B.5.2	Measurement restriction for CSI-RS based L1-RSRP	1064

9.5B.6	Scheduling availability of UE during L1-RSRP measurement	1064

9.5B.6.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	1065

9.5B.6.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	1065

9.5B.6.3	Scheduling availability of UE performing L1-RSRP measurement on FR2	1065

9.5C	L1-RSRP measurements for Reporting for satellite access	1066

9.5C.1	Introduction	1066

9.5C.3	Measurement Reporting Requirements	1066

9.5C.3.1	Periodic Reporting	1067

9.5C.3.2	Semi-Persistent Reporting	1067

9.5C.3.3	Aperiodic Reporting	1067

9.5C.4	L1-RSRP measurement requirements	1067

9.5C.4.1	SSB based L1-RSRP Reporting	1067

9.5C.5	Measurement restriction for L1-RSRP measurement	1069

9.5C.5.1	Measurement restriction for SSB based L1-RSRP	1069

9.5C.5.2	Measurement restriction for CSI-RS based L1-RSRP	1069

9.5C.6	Scheduling availability of UE during L1-RSRP measurement	1070

9.5C.6.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	1070

9.5C.6.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	1070

9.5C.7	L1-RSRP measurement requirements for NTN band above 10 GHz	1070

9.5C.7.1	SSB based L1-RSRP Reporting	1070

9.5C.7.2	CSI-RS based L1-RSRP Reporting	1071

9.5C.8	Measurement restriction for L1-RSRP measurement for NTN band above 10 GHz	1072

9.5C.8.1	Measurement restriction for SSB based L1-RSRP	1072

9.5C.8.2	Measurement restriction for CSI-RS based L1-RSRP	1072

9.5C.9	Scheduling availability of UE during L1-RSRP measurement for NTN band above 10 GHz	1073

9.5C.9.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on NTN bands above 10 GHz	1073

9.5C.9.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on NTN bands above 10 GHz	1073

9.5D	L1-RSRP measurements for Reporting for ATG	1073

9.5D.1	Introduction	1073

9.5D.2	Requirements applicability	1073

9.5D.3	Measurement Reporting Requirements	1074

9.5D.3.1	Periodic Reporting	1074

9.5D.3.2	Semi-Persistent Reporting	1074

9.5D.3.3	Aperiodic Reporting	1074

9.5D.4	L1-RSRP measurement requirements	1074

9.5D.4.1	SSB based L1-RSRP Reporting	1074

9.5D.4.2	CSI-RS based L1-RSRP Reporting	1076

9.5D.5	Measurement restriction for CSI-RS and SSB for L1-RSRP measurement	1077

9.5D.5.1	Measurement restriction for SSB based L1-RSRP	1077

9.5D.5.2	Measurement restriction for CSI-RS based L1-RSRP	1077

9.5D.6	Scheduling availability of UE during L1-RSRP measurement	1078

9.5D.6.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	1078

9.5D.6.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	1078

9.6	NE-DC: Measurements	1078

9.6.1	Introduction	1078

9.6.2	SFTD Measurements	1078

9.6.2.1	Introduction	1078

9.6.2.2	SFTD Measurement requirements	1079

9.7	Cross Link Interference measurements	1079

9.7.1	Introduction	1079

9.7.2	SRS-RSRP measurements	1080

9.7.2.1	Introduction	1080

9.7.2.2	Requirements applicability	1080

9.7.2.3	Measurement Reporting Requirements	1080

9.7.2.3.1	Periodic Reporting	1080

9.7.2.3.2	Event-triggered Periodic Reporting	1080

9.7.2.3.3	Event Triggered Reporting	1080

9.7.2.4	Measurement capability	1081

9.7.2.5	SRS-RSRP measurement period	1081

9.7.3	CLI-RSSI measurements	1081

9.7.3.1	Introduction	1081

9.7.3.2	Requirements applicability	1081

9.7.3.3	Measurement Reporting Requirements	1081

9.7.3.3.1	Periodic Reporting	1081

9.7.3.3.2	Event-triggered Periodic Reporting	1082

9.7.3.3.3	Event Triggered Reporting	1082

9.7.3.4	Measurement capability	1082

9.7.3.5	CLI-RSSI measurement period	1082

9.7.4	Scheduling availability of UE during CLI measurements	1082

9.7.4.1	Scheduling availability of UE performing measurement on FR1	1082

9.7.4.2	Scheduling availability of UE performing measurement on FR2	1083

9.8	L1-SINR measurements for Reporting	1084

9.8.1	Introduction	1084

9.8.2	Requirements applicability	1084

9.8.3	Measurement Reporting Requirements	1085

9.8.3.1	Periodic Reporting	1085

9.8.3.2	Semi-Persistent Reporting	1085

9.8.4	L1-SINR measurement requirements	1086

9.8.4.1	L1-SINR reporting with CSI-RS based CMR and no dedicated IMR configured	1086

9.8.4.3	L1-SINR reporting with CSI-RS based CMR and dedicated IMR configured	1091

9.8.5	Measurement restriction for L1-SINR measurement	1092

9.8.5.1	Measurement restriction if SSB configured for L1-SINR Measurement	1093

9.8.5.2	Measurement restriction if CSI-RS configured for L1-SINR measurement	1093

9.8.5.3	Measurement restriction if CSI-IM configured for L1-SINR measurement	1095

9.8.6	Scheduling availability of UE during L1-SINR measurement	1095

9.8.6.1	Scheduling availability of UE performing L1-SINR measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	1095

9.8.6.2	Scheduling availability of UE performing L1-SINR measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	1096

9.8.6.4	Scheduling availability of UE performing L1-SINR measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA	1097

9.8.7	Minimum requirement at transitions	1097

9.8D	L1-SINR measurements for Reporting for ATG	1097

9.8D.1	Introduction	1097

9.8D.2	Requirements applicability	1098

9.8D.3	Measurement Reporting Requirements	1098

9.8D.3.1	Periodic Reporting	1098

9.8D.3.2	Semi-Persistent Reporting	1098

9.8D.3.3	Aperiodic Reporting	1099

9.8D.4	L1-SINR measurement requirements	1099

9.8D.4.1	L1-SINR reporting with CSI-RS based CMR and no dedicated IMR configured	1099

9.8D.4.2	L1-SINR reporting with SSB based CMR and dedicated IMR configured	1100

9.8D.4.3	L1-SINR reporting with CSI-RS based CMR and dedicated IMR configured	1101

9.8D.5	Measurement restriction for L1-SINR measurement	1102

9.8D.5.1	Measurement restriction if SSB configured for L1-SINR Measurement	1102

9.8D.5.2	Measurement restriction if CSI-RS configured for L1-SINR measurement	1103

9.8D.5.3	Measurement restriction if CSI-IM configured for L1-SINR measurement	1103

9.8D.6	Scheduling availability of UE during L1-SINR measurement	1103

9.8D.6.1	Scheduling availability of UE performing L1-SINR measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	1103

9.8D.6.2	Scheduling availability of UE performing L1-SINR measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	1103

9.9	NR measurements for positioning	1104

9.9.1	Introduction	1104

9.9.1.1	General Aspects of Gap-based Measurement	1104

9.9.1.2	General Aspects of Gapless Measurement	1105

9.9.1.3	Scheduling Availability of UE during PRS Measurement without Measurement Gaps	1106

9.9.2	RSTD measurements	1107

9.9.2.1	Introduction	1107

9.9.2.2	Requirements Applicability	1107

9.9.2.3	Measurement Capability	1107

9.9.2.4	Measurement Reporting Requirements	1107

9.9.2.4.1	Void	1107

9.9.2.4.2	Void	1107

9.9.2.4.3	Void	1107

9.9.2.5	Measurements Period Requirements	1107

9.9.2.6	Void	1110

9.9.2.7	Measurements Period Requirements without Measurement Gaps	1110

9.9.2.8	Void	1113

9.9.2.9	Measurements Period Requirements with both MG and PPW	1113

9.9.2.10	Measurements Period Requirements with Bandwidth Aggregation	1114

9.9.3	PRS-RSRP measurements	1117

9.9.3.1	Introduction	1117

9.9.3.2	Requirements applicability	1118

9.9.3.3	Measurement Capability	1118

9.9.3.4	Measurement Reporting Requirements	1118

9.9.3.5	Measurement Period Requirements	1118

9.9.3.6	Measurement Period Requirements without Measurement Gaps	1121

9.9.3.7	Void	1123

9.9.3.8	Measurements Period Requirements with both MG and PPW	1123

9.9.4	UE Rx-Tx time difference measurements	1124

9.9.4.1	Introduction	1124

9.9.4.2	Requirements Applicability	1124

9.9.4.3	Measurement Capability	1124

9.9.4.4	Measurement Reporting Requirements	1124

9.9.4.5	Measurement Period Requirements	1124

9.9.4.6	Measurement Period Requirements without Measurement Gaps	1128

9.9.4.7	Void	1131

9.9.4.8	Measurements Period Requirements with both MG and PPW	1131

9.9.4.9	Measurements Period Requirements with Bandwidth Aggregation	1132

9.9.5	E-CID measurements	1136

9.9.5.1	Introduction	1136

9.9.5.2	Measurement Requirements	1136

9.9.5.2.1	Intra-frequency Measurement Requirements	1136

9.9.5.2.2	Inter-frequency Measurement Requirements	1136

9.9.5.2.3	Measurement Reporting Delay	1137

9.9.6	PRS-RSRPP measurements	1137

9.9.6.1	Introduction	1137

9.9.6.2	Requirements applicability	1137

9.9.6.3	Measurement capability	1137

9.9.6.4	Measurement reporting requirements	1137

9.9.6.5	Measurement period requirements	1137

9.9.6.6	Measurement Period Requirements without Measurement Gaps	1138

9.9.6.7	Void	1138

9.9.6.8	Measurements Period Requirements with both MG and PPW	1138

9.9.7	Measurement requirements for DL RSCPD reported with RSTD	1138

9.9.7.1	Introduction	1138

9.9.7.2	Requirements Applicability	1138

9.9.7.3	Measurement Capability	1138

9.9.7.4	Measurement Reporting Requirements	1138

9.9.7.5	Measurements Period Requirements for DL RSCPD reported with RSTD	1139

9.9.8	Measurement requirements for DL RSCP reported with UE Rx-Tx time difference	1141

9.9.8.1	Introduction	1141

9.9.8.2	Requirements Applicability	1142

9.9.8.3	Measurement Capability	1142

9.9.8.4	Measurement Reporting Requirements	1142

9.9.8.5	Measurement Period Requirements for DL RSCP and UE Rx-Tx time difference	1142

9.9A	NR measurements for positioning for RedCap	1146

9.9A.1	Introduction	1146

9.9A.1.1	General Aspects of Gap-based Measurement	1146

9.9A.1.2	General Aspects of Gapless Measurement for RedCap positioning without FH	1147

9.9A.1.3	Scheduling Availability of UE during PRS Measurement without Measurement Gaps for RedCap positioning without FH	1148

9.9A.2	RSTD measurements for RedCap	1149

9.9A.2.1	Introduction	1149

9.9A.2.2	Requirements Applicability	1149

9.9A.2.3	Measurement Capability	1149

9.9A.2.4	Measurement Reporting Requirements	1149

9.9A.2.5	Measurements Period Requirements without FH	1149

9.9A.2.5.1	Measurements Period Requirements without FH with MG	1149

9.9A.2.5.2	Measurements Period Requirements without FH without MG	1152

9.9A.2.5.3	Measurements Period Requirements without FH with both MG and PPW	1155

9.9A.2.6	Measurements Period Requirements with FH	1156

9.9A.2.6.1	Measurements Period Requirements with FH with MG	1156

9.9A.3	PRS-RSRP measurements for RedCap	1158

9.9A.3.1	Introduction	1158

9.9A.3.2	Requirements applicability	1158

9.9A.3.3	Measurement Capability	1158

9.9A.3.4	Measurement Reporting Requirements	1158

9.9A.3.5	Measurements Period Requirements without FH	1158

9.9A.3.5.1	Measurement Period Requirements without FH with MG	1158

9.9A.3.5.2	Measurement Period Requirements without FH without MG	1161

9.9A.3.5.3	Measurements Period Requirements without FH with both MG and PPW	1163

9.9A.3.6	Measurements Period Requirements with FH	1164

9.9A.3.6.1	Measurements Period Requirements with FH with MG	1164

9.9A.4	UE Rx-Tx time difference measurements for RedCap	1166

9.9A.4.1	Introduction	1166

9.9A.4.2	Requirements Applicability	1166

9.9A.4.3	Measurement Capability	1166

9.9A.4.4	Measurement Reporting Requirements	1166

9.9A.4.5	Measurement Period Requirements without FH with MG	1166

9.9A.4.6	Measurement Period Requirements without FH without MG	1166

9.9A.4.7	Measurements Period Requirements without FH with both MG and PPW	1166

9.9A.4.8	Measurements Period Requirements with FH	1166

9.9A.5	PRS-RSRPP measurements for RedCap	1168

9.9A.5.1	Introduction	1168

9.9A.5.2	Requirements Applicability	1168

9.9A.5.3	Measurement Capability	1168

9.9A.5.4	Measurement Reporting Requirements	1169

9.9A.5.5	Measurement Period Requirements without FH with MG	1169

9.9A.5.6	Measurement Period Requirements without FH without MG	1169

9.9A.5.7	Measurements Period Requirements without FH with both MG and PPW	1169

9.9A.5.8	Measurements Period Requirements with FH	1169

9.9C	NR measurements for positioning in Satellite Access	1169

9.9C.1	Introduction	1169

9.9C.1.1	General Aspects of Gap-based Measurement	1169

9.9C.1.2	General Aspects of Gapless Measurement	1170

9.9C.1.3	Scheduling Availability of UE during PRS Measurement without Measurement Gaps	1171

9.9C.2	Void	1171

9.9C.3	Void	1171

9.9C.4	UE Rx-Tx time difference measurements	1171

9.9C.4.1 Introduction	1171

9.9C.4.2 Requirements Applicability	1171

9.9C.4.3	Measurement Capability	1171

9.9C.4.4	Measurement Reporting Requirements	1171

9.9C.4.5	Measurement Period Requirements	1172

9.9C.4.6	Measurement Period Requirements without Measurement Gaps	1174

9.10	CSI-RS based L3 measurements	1176

9.10.1	Introduction	1176

9.10.2	CSI-RS based intra-frequency measurements	1176

9.10.2.1	Introduction	1176

9.10.2.2	Requirements applicability	1177

9.10.2.3	Number of cells and number of CSI-RS	1178

9.10.2.3.1	Requirements for FR1	1178

9.10.2.3.2	Requirements for FR2	1178

9.10.2.4	Measurement Reporting Requirements	1178

9.10.2.4.1	Periodic Reporting	1179

9.10.2.4.2	Event-triggered Periodic Reporting	1179

9.10.2.4.3	Event Triggered Reporting	1179

9.10.2.5	Intra-frequency measurements without measurement gaps	1179

9.10.2.6	Scheduling availability of UE during CSI-RS based intra-frequency measurements	1181

9.10.2.6.1	Scheduling availability of UE performing CSI-RS based measurements in TDD bands	1181

9.10.2.6.2	Scheduling availability of UE performing CSI-RS based measurements in FR2	1181

9.10.3	CSI-RS based Inter-frequency measurements	1182

9.10.3.1	Introduction	1182

9.10.3.2	Requirements applicability	1182

9.10.3.3	Number of cells and number of CSI-RS resources	1183

9.10.3.3.1	Requirements for FR1	1183

9.10.3.3.2	Requirements for FR2	1183

9.10.3.4	Measurements reporting requirements	1183

9.10.3.4.1	Periodic Reporting	1183

9.10.3.4.2	Event-triggered Periodic Reporting	1183

9.10.3.4.3	Event-triggered Reporting	1183

9.10.3.5	Inter-frequency measurements with measurement gaps	1184

9.10D	CSI-RS based L3 measurements for ATG	1185

9.10D.1	Introduction	1185

9.10D.2	CSI-RS based intra-frequency measurements	1186

9.10D.2.1	Introduction	1186

9.10D.2.2	Requirements applicability	1186

9.10D.2.3	Number of cells and number of CSI-RS	1187

9.10D.2.3.1	Requirements for FR1	1187

9.10D.2.4	Measurement Reporting Requirements	1187

9.10D.2.4.1	Periodic Reporting	1187

9.10D.2.4.2	Event-triggered Periodic Reporting	1187

9.10D.2.4.3	Event Triggered Reporting	1188

9.10D.2.5	Intra-frequency measurements without measurement gaps	1188

9.10D.2.6	Scheduling availability of UE during CSI-RS based intra-frequency measurements	1189

9.10D.2.6.1	Scheduling availability of UE performing CSI-RS based measurements in TDD bands	1190

9.10D.3	CSI-RS based Inter-frequency measurements	1190

9.10D.3.1	Introduction	1190

9.10D.3.2	Requirements applicability	1190

9.10D.3.3	Number of cells and number of CSI-RS resources	1191

9.10D.3.3.1	Requirements for FR1	1191

9.10D.3.4	Measurements reporting requirements	1191

9.10D.3.4.1	Periodic Reporting	1191

9.10D.3.4.2	Event-triggered Periodic Reporting	1191

9.10D.3.4.3	Event-triggered Reporting	1191

9.10D.3.5	Inter-frequency measurements with measurement gaps	1191

9.11	NR measurements with autonomous gaps	1193

9.11.1	Introduction	1193

9.11.2	CGI identification of an NR cell with autonomous gaps	1193

9.11.3	CGI reporting delay	1194

9.11A	NR measurements with autonomous gaps for RedCap	1195

9.11A.1	Introduction	1195

9.11A.2	CGI identification of an NR cell with autonomous gaps	1195

9.11A.3	CGI reporting delay	1196

9.11A.4	CGI reporting scheduling restriction	1196

9.11D	NR measurements with autonomous gaps for ATG	1196

9.11D.1	Introduction	1197

9.11D.2	CGI identification of an NR cell with autonomous gaps	1197

9.11D.3	CGI reporting delay	1198

9.12	Measurement for Propagation Delay Compensation	1198

9.12.1	Introduction	1198

9.12.2	Requirements Applicability	1198

9.12.3	Measurement Capability	1198

9.12.4	Measurement period requirements	1198

9.12.4.1	PRS Measurement Period	1198

9.12.4.2	TRS Measurement Period	1199

9.12.5	Measurement Reporting Requirements	1200

9.12.6	Scheduling availability during measurement for Propagation Delay Compensation	1200

9.12.7	Measurement restriction for measurement for Propagation Delay Compensation	1201

9.12.8	Measurement requirement for Propagation Delay Compensation with MUSIM gaps	1201

9.13	L1-RSRP measurements for a cell with different PCI from serving cell	1201

9.13.1	Introduction	1201

9.13.2	Requirements Applicability	1201

9.13.3	Measurement Reporting Requirements	1202

9.13.3.1	Periodic Reporting	1202

9.13.3.2	Semi-Persistent Reporting	1202

9.13.3.3	Aperiodic Reporting	1203

9.13.4	L1-RSRP measurement requirements	1203

9.13.4.1	Inter-cell SSB based L1-RSRP Reporting	1203

9.13.5	Measurement restriction for L1-RSRP measurement	1206

9.13.5.1	Measurement restriction for SSB based L1-RSRP	1206

9.13.6	Scheduling availability of UE during L1-RSRP measurement	1207

9.13.6.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	1207

9.13.6.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	1207

9.13.6.3	Scheduling availability of UE performing L1-RSRP measurement on FR2	1208

9.13.6.4	Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA	1208

9.13.6.5	Scheduling availability of UE performing L1-RSRP measurement in TDD bands on FR1	1208

9.14	NR intra-frequency L1-RSRP measurements for neighbor cell	1209

9.14.1	Introduction	1209

9.14.2	Requirements Applicability	1209

9.14.3	Measurement Reporting Requirements	1209

9.14.3.1	Periodic Reporting	1210

9.14.3.2	Semi-Persistent Reporting	1210

9.14.3.3	Aperiodic Reporting	1210

9.14.4	Number of SSB frequency layers, number of cells and number of SSBs	1210

9.14.5	L1-RSRP intra-frequency measurement requirements without measurement gaps	1210

9.14.5.1	Intra-frequency SSB based L1-RSRP reporting	1210

9.14.6	Measurement restriction for L1-RSRP measurement	1213

9.14.6.1	Measurement restriction for SSB based L1-RSRP	1213

9.14.7	Scheduling availability of UE during L1-RSRP measurement	1214

9.14.7.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	1214

9.14.7.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	1214

9.14.7.3	Scheduling availability of UE performing L1-RSRP measurement on FR2	1215

9.14.7.4	Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA	1215

9.14.7.5	Scheduling availability of UE performing L1-RSRP measurement in TDD bands on FR1	1215

9.15	NR inter-frequency L1-RSRP measurements for neighbor cell	1216

9.15.1	Introduction	1216

9.15.2	Requirements Applicability	1216

9.15.3	Measurement Reporting Requirements	1216

9.15.3.1	Periodic Reporting	1217

9.15.3.2	Semi-Persistent Reporting	1217

9.15.3.3	Aperiodic Reporting	1217

9.15.4	Number of SSB frequency layers, number of cells and number of SSBs	1217

9.15.5	L1-RSRP inter-frequency measurement requirements with measurement gaps	1217

9.15.5.1	Inter-frequency SSB based L1-RSRP reporting	1217

9.15.6	L1-RSRP inter-frequency L1-RSRP measurement requirements without measurement gaps	1219

9.15.6.1	Inter-frequency L1-RSRP measurement requirements	1219

9.15.6.1.1	Inter-frequency SSB based L1-RSRP measurement	1219

9.15.6.2	Measurement restriction for inter-frequency L1-RSRP measurement	1222

9.15.6.2.1	Measurement restriction for SSB based L1-RSRP	1222

9.15.6.3	Scheduling availability of UE during inter-frequency L1-RSRP measurements	1222

9.15.6.3.1	Scheduling availability of UE performing L1-RSRP measurement with a same subcarrier spacing as PDSCH/PDCCH on FR1	1222

9.15.6.3.2	Scheduling availability of UE performing L1-RSRP measurement with a different subcarrier spacing than PDSCH/PDCCH on FR1	1223

9.15.6.3.3	Scheduling availability of UE performing L1-RSRP measurement on FR2	1223

9.15.6.3.4	Scheduling availability of UE performing L1-RSRP measurement on FR1 or FR2 in case of FR1-FR2 inter-band CA	1223

9.15.6.3.5	Scheduling availability of UE performing L1-RSRP measurement in TDD bands on FR1	1224

10	Measurement Performance requirements	1223

10.1	NR measurements	1223

10.1.1	Introduction	1223

10.1.2	Intra-frequency RSRP accuracy requirements for FR1	1223

10.1.2.1	Intra-frequency SS-RSRP accuracy requirements	1223

10.1.2.1.1	Absolute SS-RSRP Accuracy	1223

10.1.2.1.2	Relative SS-RSRP Accuracy	1224

10.1.2.2	Void	1225

10.1.2.3	Intra-frequency CSI-RSRP accuracy requirements	1225

10.1.2.3.1	Absolute CSI-RSRP Accuracy	1225

10.1.2.3.2	Relative CSI-RSRP Accuracy	1226

10.1.2B	Intra-frequency RSRP accuracy requirements for FR1 for CA/DC Idle Mode Measurements	1227

10.1.2B.1	Intra-frequency SS-RSRP accuracy requirements	1227

10.1.2B.1.1	Absolute SS-RSRP Accuracy	1227

10.1.2C	Intra-frequency RSRP accuracy requirements for FR1 SAN	1228

10.1.2C.1	Intra-frequency SS-RSRP accuracy requirements	1228

10.1.2C.1.1	Absolute SS-RSRP Accuracy	1228

10.1.2C.1.2	Relative SS-RSRP Accuracy	1229

10.1.3	Intra-frequency RSRP accuracy requirements for FR2	1230

10.1.3.1	Intra-frequency SS-RSRP accuracy requirements	1230

10.1.3.1.1	Absolute SS-RSRP Accuracy	1230

10.1.3.1.2	Relative SS-RSRP Accuracy	1230

10.1.3.2	Void	1231

10.1.3.3	Intra-frequency CSI-RSRP accuracy requirements	1231

10.1.3.3.1	Absolute CSI-RSRP Accuracy	1231

10.1.3.3.2	Relative CSI-RSRP Accuracy	1232

10.1.3B	Intra-frequency RSRP accuracy requirements for FR2 for CA/DC Idle Mode Measurements	1233

10.1.3B.1	Intra-frequency SS-RSRP accuracy requirements	1233

10.1.3B.1.1	Absolute SS-RSRP Accuracy	1233

10.1.3C	Intra-frequency RSRP accuracy requirements for FR2-NTN	1233

10.1.3C.1	Intra-frequency SS-RSRP accuracy requirements	1233

10.1.3C.1.1	Absolute SS-RSRP Accuracy	1233

10.1.3C.1.2	Relative SS-RSRP Accuracy	1234

10.1.4	Inter-frequency RSRP accuracy requirements for FR1	1235

10.1.4.1	Inter-frequency SS-RSRP accuracy requirements	1235

10.1.4.1.1	Absolute SS-RSRP Accuracy in FR1	1235

10.1.4.1.2	Relative SS-RSRP Accuracy in FR1	1236

10.1.4.2	Void	1237

10.1.4.3	Inter-frequency CSI-RSRP accuracy requirements	1237

10.1.4.3.1	Absolute CSI-RSRP Accuracy in FR1	1237

10.1.4.3.2	Relative CSI-RSRP Accuracy in FR1	1238

10.1.4B	Inter-frequency RSRP accuracy requirements for FR1 for CA/DC Idle Mode Measurements	1239

10.1.4B.1	Inter-frequency SS-RSRP accuracy requirements	1239

10.1.4B.1.1	Absolute SS-RSRP Accuracy in FR1	1240

10.1.4C	Inter-frequency RSRP accuracy requirements for FR1 SAN	1241

10.1.4C.1	Inter-frequency SS-RSRP accuracy requirements	1241

10.1.4C.1.1	Absolute SS-RSRP Accuracy in FR1	1241

10.1.4C.1.2	Relative SS-RSRP Accuracy in FR1	1241

10.1.5	Inter-frequency RSRP accuracy requirements for FR2	1242

10.1.5.1	Inter-frequency SS-RSRP accuracy requirements	1242

10.1.5.1.1	Absolute SS-RSRP Accuracy	1242

10.1.5.1.2	Relative SS-RSRP Accuracy	1242

10.1.5.2	Void	1243

10.1.5.3	Inter-frequency CSI-RSRP accuracy requirements	1243

10.1.5.3.1	Absolute CSI-RSRP Accuracy	1243

10.1.5.3.2	Relative CSI-RSRP Accuracy	1244

10.1.5B	Inter-frequency RSRP accuracy requirements for FR2 for CA/DC Idle Mode Measurements	1245

10.1.5B.1	Inter-frequency SS-RSRP accuracy requirements	1245

10.1.5B.1.1	Absolute SS-RSRP Accuracy	1245

10.1.5C	Inter-frequency RSRP accuracy requirements for FR2-NTN	1246

10.1.5C.1	Inter-frequency SS-RSRP accuracy requirements	1246

10.1.5C.1.1	Absolute SS-RSRP Accuracy	1246

10.1.5C.1.2	Relative SS-RSRP Accuracy	1246

10.1.6	RSRP Measurement Report Mapping	1247

10.1.7	Intra-frequency RSRQ accuracy requirements for FR1	1249

10.1.7.1	Intra-frequency SS-RSRQ accuracy requirements in FR1	1249

10.1.7.1.1	Absolute SS-RSRQ Accuracy in FR1	1249

10.1.7.2	Intra-frequency CSI-RSRQ accuracy requirements	1250

10.1.7.2.1	Absolute CSI-RSRQ Accuracy	1250

10.1.7B	Intra-frequency RSRQ accuracy requirements for FR1 for CA/DC Idle Mode Measurements	1251

10.1.7B.1	Intra-frequency SS-RSRQ accuracy requirements in FR1	1251

10.1.7B.1.1	Absolute SS-RSRQ Accuracy in FR1	1251

10.1.7C	Intra-frequency RSRQ accuracy requirements for FR1 SAN	1252

10.1.7C.1	Intra-frequency SS-RSRQ accuracy requirements in FR1	1252

10.1.7C.1.1	Absolute SS-RSRQ Accuracy in FR1	1252

10.1.8	Intra-frequency RSRQ accuracy requirements for FR2	1253

10.1.8.1	Intra-frequency SS-RSRQ accuracy requirements in FR2	1253

10.1.8.1.1	Absolute SS-RSRQ Accuracy in FR2	1253

10.1.8.2	Intra-frequency CSI-RSRQ accuracy requirements	1253

10.1.8.2.1	Absolute CSI-RSRQ Accuracy	1253

10.1.8B	Intra-frequency RSRQ accuracy requirements for FR2 for CA/DC Idle Mode Measurements	1254

10.1.8B.1	Intra-frequency SS-RSRQ accuracy requirements in FR2	1254

10.1.8B.1.1	Absolute SS-RSRQ Accuracy in FR2	1254

10.1.8C	Intra-frequency RSRQ accuracy requirements for FR2-NTN	1255

10.1.8C.1	Intra-frequency SS-RSRQ accuracy requirements in FR2-NTN	1255

10.1.8C.1.1	Absolute SS-RSRQ Accuracy in FR2-NTN	1255

10.1.9	Inter-frequency RSRQ accuracy requirements for FR1	1256

10.1.9.1	Inter-frequency SS-RSRQ accuracy requirements in FR1	1256

10.1.9.1.1	Absolute SS-RSRQ Accuracy in FR1	1256

10.1.9.1.2	Relative SS-RSRQ Accuracy in FR1	1256

10.1.9.2	Inter-frequency CSI-RSRQ accuracy requirements	1257

10.1.9.2.1	Absolute CSI-RSRQ Accuracy	1257

10.1.9.2.2	Relative CSI-RSRQ Accuracy	1258

10.1.9B	Inter-frequency RSRQ accuracy requirements for FR1 for CA/DC Idle Mode Measurements	1259

10.1.9B.1	Inter-frequency SS-RSRQ accuracy requirements in FR1	1259

10.1.9B.1.1	Absolute SS-RSRQ Accuracy in FR1	1259

10.1.9C	Inter-frequency RSRQ accuracy requirements for FR1 SAN	1260

10.1.9C.1	Inter-frequency SS-RSRQ accuracy requirements in FR1	1260

10.1.9C.1.1	Absolute SS-RSRQ Accuracy in FR1	1260

10.1.9C.1.2	Relative SS-RSRQ Accuracy in FR1	1261

10.1.10	Inter-frequency RSRQ accuracy requirements for FR2	1261

10.1.10.1	Inter-frequency SS-RSRQ accuracy requirements in FR2	1261

10.1.10.1.1	Absolute SS-RSRQ Accuracy in FR2	1261

10.1.10.1.2	Relative SS-RSRQ Accuracy in FR2	1262

10.1.10.2	Inter-frequency CSI-RSRQ accuracy requirements	1263

10.1.10.2.1	Absolute CSI-RSRQ Accuracy	1263

10.1.10.2.2	Relative CSI-RSRQ Accuracy	1264

10.1.10B	 Inter-frequency RSRQ accuracy requirements for FR2 for CA/DC Idle Mode Measurements	1265

10.1.10B.1	Inter-frequency SS-RSRQ accuracy requirements in FR2	1265

10.1.10B.1.1	Absolute SS-RSRQ Accuracy in FR2	1265

10.1.10C	Inter-frequency RSRQ accuracy requirements for FR2-NTN	1266

10.1.10C.1	Inter-frequency SS-RSRQ accuracy requirements in FR2-NTN	1266

10.1.10C.1.1	Absolute SS-RSRQ Accuracy in FR2-NTN	1266

10.1.10C.1.2	Relative SS-RSRQ Accuracy in FR2-NTN	1266

10.1.11	RSRQ report mapping	1267

10.1.12	Intra-frequency SINR accuracy requirements for FR1	1268

10.1.12.1	Intra-frequency SS-SINR accuracy requirements in FR1	1268

10.1.12.1.1	Absolute SS-SINR Accuracy in FR1	1268

10.1.12.2	Intra-frequency CSI-SINR accuracy requirements in FR1	1268

10.1.12.2.1	Absolute CSI-SINR Accuracy in FR1	1268

10.1.12C	 Intra-frequency SINR accuracy requirements for FR1 SAN	1269

10.1.12C.1	Intra-frequency SS-SINR accuracy requirements in FR1	1269

10.1.12C.1.1	Absolute SS-SINR Accuracy in FR1	1269

10.1.13	Intra-frequency SINR accuracy requirements for FR2	1270

10.1.13.1	Intra-frequency SS-SINR accuracy requirements in FR2	1270

10.1.13.1.1	Absolute SS-SINR Accuracy in FR2	1270

10.1.13.2	Intra-frequency CSI-SINR accuracy requirements in FR2	1271

10.1.13.2.1	Absolute CSI-SINR Accuracy in FR2	1271

10.1.13C	Intra-frequency SINR accuracy requirements for FR2-NTN	1271

10.1.13C.1	Intra-frequency SS-SINR accuracy requirements in FR2-NTN	1271

10.1.13C.1.1	Absolute SS-SINR Accuracy in FR2-NTN	1271

10.1.14	Inter-frequency SINR accuracy requirements for FR1	1272

10.1.14.1	Inter-frequency SS-SINR accuracy requirements in FR1	1272

10.1.14.1.1	Absolute SS-SINR Accuracy in FR1	1272

10.1.14.1.2	Relative SS-SINR Accuracy in FR1	1273

10.1.14.2	Inter-frequency CSI-SINR accuracy requirements in FR1	1274

10.1.14.2.1	Absolute CSI-SINR Accuracy in FR1	1274

10.1.14.2.2	Relative CSI-SINR Accuracy in FR1	1275

10.1.14C	 Inter-frequency SINR accuracy requirements for FR1 SAN	1276

10.1.14C.1	Inter-frequency SS-SINR accuracy requirements in FR1	1276

10.1.14C.1.1	Absolute SS-SINR Accuracy in FR1	1276

10.1.14C.1.2	Relative SS-SINR Accuracy in FR1	1277

10.1.15	Inter-frequency SINR accuracy requirements for FR2	1278

10.1.15.1	Inter-frequency SS-SINR accuracy requirements in FR2	1278

10.1.15.1.1	Absolute SS-SINR Accuracy in FR2	1278

10.1.15.1.2	Relative SS-SINR Accuracy in FR2	1278

10.1.15.2	Inter-frequency CSI-SINR accuracy requirements in FR2	1279

10.1.15.2.1	Absolute CSI-SINR Accuracy in FR2	1279

10.1.15.2.2	Relative CSI-SINR Accuracy in FR2	1280

10.1.15C	Inter-frequency SINR accuracy requirements for FR2-NTN	1281

10.1.15C.1	Inter-frequency SS-SINR accuracy requirements in FR2-NTN	1281

10.1.15C.1.1	Absolute SS-SINR Accuracy in FR2-NTN	1281

10.1.15C.1.2	Relative SS-SINR Accuracy in FR2-NTN	1281

10.1.16	SINR report mapping	1282

10.1.16.1	SS-SINR and CSI-SINR measurement report mapping	1282

10.1.17	Power Headroom	1283

10.1.17.1	Power Headroom Report	1283

10.1.17.1.1	Power Headroom Report Mapping	1283

10.1.18	PCMAX,c,f	1283

10.1.18.1	Report Mapping	1283

10.1.19	L1-RSRP accuracy requirements for FR1	1284

10.1.19.1	SSB based L1-RSRP accuracy requirements	1284

10.1.19.1.1	Absolute Accuracy	1284

10.1.19.1.2	Relative Accuracy	1285

10.1.19.2	CSI-RS based L1-RSRP accuracy requirements	1286

10.1.19.2.1	Absolute Accuracy	1286

10.1.19.2.2	Relative Accuracy	1287

10.1.19C	L1-RSRP accuracy requirements for FR1 SAN	1288

10.1.19C.1	SSB based L1-RSRP accuracy requirements	1288

10.1.19C.1.1	Absolute Accuracy	1288

10.1.19C.1.2	Relative Accuracy	1289

10.1.19C.2	CSI-RS based L1-RSRP accuracy requirements	1289

10.1.19C.2.1	Absolute Accuracy	1289

10.1.19C.2.2	Relative Accuracy	1290

10.1.19D	LTM Intra-frequency L1-RSRP accuracy requirements for FR1	1291

10.1.19D.1	SSB based intra-frequency L1-RSRP accuracy requirements	1291

10.1.19D.1.1	Absolute Accuracy	1291

10.1.19D.1.2	Relative Accuracy	1292

10.1.19E	  LTM Inter-frequency L1-RSRP accuracy requirements for FR1	1292

10.1.19E.1	SSB based Inter-frequency L1-RSRP accuracy requirements	1292

10.1.19E.1.1	Absolute Accuracy	1292

10.1.19E.1.2	Relative Accuracy	1293

10.1.20	L1-RSRP accuracy requirements for FR2	1294

10.1.20.1	SSB based L1-RSRP accuracy requirements	1294

10.1.20.1.1	Absolute Accuracy	1294

10.1.20.1.2	Relative Accuracy	1295

10.1.20.2	CSI-RS based L1-RSRP accuracy requirements	1296

10.1.20.2.1	Absolute Accuracy	1296

10.1.20.2.2	Relative Accuracy	1296

10.1.20A	  LTM Intra-frequency L1-RSRP accuracy requirements for FR2	1297

10.1.20A.1	SSB based intra-frequency L1-RSRP accuracy requirements	1297

10.1.20A.1.1	Absolute Accuracy	1297

10.1.20A.1.2	Relative Accuracy	1298

10.1.20B	  LTM Inter-frequency L1-RSRP accuracy requirements for FR2	1299

10.1.20B.1	SSB based inter-frequency L1-RSRP accuracy requirements	1299

10.1.20B.1.1	Absolute Accuracy	1299

10.1.20B.1.2	Relative Accuracy	1299

10.1.20C	L1-RSRP accuracy requirements for FR2-NTN	1300

10.1.20C.1	SSB based L1-RSRP accuracy requirements	1300

10.1.20C.1.1	Absolute Accuracy	1300

10.1.20C.1.2	Relative Accuracy	1301

10.1.20C.2	CSI-RS based L1-RSRP accuracy requirements	1301

10.1.20C.2.1	Absolute Accuracy	1301

10.1.20C.2.2	Relative Accuracy	1302

10.1.21	SFTD accuracy requirements	1303

10.1.21.1	SFTD acuracy requirements for NE-DC	1303

10.1.21.2	SFTD acuracy requirements for NR-DC	1304

10.1.21.3	Inter-frequency SFTD acuracy requirements	1305

10.1.22	CLI measurement accuracy requirements	1307

10.1.22.1	SRS-RSRP	1307

10.1.22.1.1	SRS-RSRP Accuracy	1307

10.1.22.1.2	SRS-RSRP report mapping	1308

10.1.22.2	CLI-RSSI	1309

10.1.22.2.1	CLI-RSSI Accuracy	1309

10.1.22.2.2	CLI-RSSI report mapping	1310

10.1.23	RSTD Measurements	1310

10.1.23.1	Introduction	1310

10.1.23.2	Measurement Accuracy Requirements	1310

10.1.23.3	Report mapping	1318

10.1.23.3.1	Absolute DL RSTD Measurement Reporting	1318

10.1.23.3.2	Differential Reporting for DL RSTD Measurement	1321

10.1.23.3.3	Additional Path Report Mapping for DL RSTD	1324

10.1.23A	RSTD Measurements Based on PRS Aggregation	1328

10.1.23A.1	Introduction	1328

10.1.23A.3	Report Mapping	1335

10.1.23A.3.1	Absolute DL RSTD Measurement Reporting	1335

10.1.23A.3.2	Differential Reporting for DL RSTD Measurement	1335

10.1.23A.3.3	Additional Path Report Mapping for DL RSTD	1335

10.1.24	PRS-RSRP Measurements	1335

10.1.24.1	Introduction	1335

10.1.24.2	Measurement Accuracy Requirements	1336

10.1.24.2.1	Absolute PRS-RSRP accuracy	1336

10.1.24.2.2	Relative PRS RSRP accuracy	1340

10.1.24.3	Report mapping	1344

10.1.24.3.1	Absolute PRS-RSRP Measurement Report Mapping	1344

10.1.24.3.2	Differential Report Mapping for PRS-RSRP Measurement	1345

10.1.24A	PRS-RSRP Measurements Based on PRS Aggregation	1347

10.1.24A.1	Introduction	1347

10.1.24A.2	Measurement Accuracy Requirements	1348

10.1.24A.2.1	Absolute PRS RSRP Accuracy Requirement	1348

10.1.24A.2.2	Relative PRS RSRP Accuracy Requirement	1348

10.1.24A.3	Report Mapping	1348

10.1.24A.3.1	Absolute PRS-RSRP Measurement Report Mapping	1348

10.1.24A.3.2	Differential Report Mapping for PRS-RSRP Measurement	1348

10.1.25	UE Rx-Tx Time Difference Measurements	1348

10.1.25.1	Introduction	1348

10.1.25.2	Measurement Accuracy Requirements	1348

10.1.25.3	Report mapping	1360

10.1.25.3.1	Absolute UE Rx-Tx Measurement Report Mapping	1360

10.1.25.3.2	Differential UE Rx-Tx Measurement Report Mapping	1363

10.1.25.3.3	Additional Path Report Mapping for UE Rx-Tx Time Difference	1366

10.1.25A	UE Rx-Tx Time Difference Measurement Based on PRS Aggregation	1369

10.1.25A.1	Introduction	1369

10.1.25A.2	Measurement Accuracy Requirements	1370

10.1.25A.3	Report mapping	1386

10.1.25C	UE Rx-Tx Time Difference Measurements in Satellite Accesss	1386

10.1.25C.1	Introduction	1386

10.1.25C.2	Measurement Accuracy Requirements	1386

10.1.25C.3	Report mapping	1387

10.1.26	FR2 P-MPR report	1387

10.1.26.1	Report mapping	1387

10.1.27	L1-SINR accuracy requirements for FR1	1388

10.1.27.1	L1-SINR accuracy requirements with CSI-RS based CMR and no dedicated IMR configured	1388

10.1.27.1.1	Absolute Accuracy	1388

10.1.27.1.2	Relative Accuracy	1389

10.1.27.2	L1-SINR accuracy requirements with SSB based CMR and dedicated IMR configured	1390

10.1.27.2.1	Absolute Accuracy	1390

10.1.27.2.2	Relative Accuracy	1392

10.1.27.3	L1-SINR accuracy requirements with CSI-RS based CMR and dedicated IMR configured	1394

10.1.27.3.1	Absolute Accuracy	1394

10.1.27.3.2	Relative Accuracy	1396

10.1.28	L1-SINR accuracy requirements for FR2	1398

10.1.29	Intra-frequency RSRQ accuracy requirements under CCA	1405

10.1.29.1	Intra-frequency SS-RSRQ accuracy requirements in FR1	1405

10.1.29.1.1	Absolute SS-RSRQ Accuracy	1405

10.1.30	Inter-frequency RSRQ accuracy requirements under CCA	1405

10.1.30.1	Inter-frequency SS-RSRQ accuracy requirements in FR1	1405

10.1.30.1.1	Absolute SS-RSRQ Accuracy	1405

10.1.30.1.2	Relative SS-RSRQ Accuracy	1406

10.1.31	Intra-frequency SINR accuracy requirements under CCA	1407

10.1.31.1	Intra-frequency SS-SINR accuracy requirements in FR1	1407

10.1.31.1.1	Absolute SS-SINR Accuracy	1407

10.1.32	Inter-frequency SINR accuracy requirements under CCA	1407

10.1.32.1	Inter-frequency SS-SINR accuracy requirements in FR1	1407

10.1.32.1.1	Absolute SS-SINR Accuracy	1407

10.1.32.1.2	Relative SS-SINR Accuracy	1408

10.1.33	L1-RSRP accuracy requirements under CCA	1409

10.1.33.1	SSB based L1-RSRP accuracy requirements in FR1	1409

10.1.33.1.1	Absolute Accuracy	1409

10.1.33.1.2	Relative Accuracy	1409

10.1.34	RSSI measurements under CCA	1410

10.1.34.1	Intra-frequency absolute RSSI measurement accuracy requirements in FR1	1410

10.1.34.2	Inter-frequency absolute RSSI measurement accuracy requirements in FR1	1410

10.1.34.3	RSSI measurement report mapping	1410

10.1.35	Channel occupancy measurements under CCA	1411

10.1.35.1	Intra-frequency channel occupancy measurement accuracy requirements in FR1	1411

10.1.35.2	Inter-frequency channel occupancy measurement accuracy requirements in FR1	1411

10.1.36	Intra-frequency RSRP accuracy requirements under CCA	1411

10.1.36.1	Intra-frequency SS-RSRP accuracy requirements in FR1	1411

10.1.36.1.1	Absolute SS-RSRP Accuracy	1411

10.1.36.1.2	Relative SS-RSRP Accuracy	1412

10.1.37	Inter-frequency RSRP accuracy requirements under CCA	1412

10.1.37.1	Inter-frequency SS-RSRP accuracy requirements in FR1	1412

10.1.37.1.1	Absolute SS-RSRP	1412

10.1.37.1.2	Relative SS-RSRP Accuracy	1413

10.1.38	PRS-RSRPP Measurements	1414

10.1.38.1	Introduction	1414

10.1.38.2	Measurement Accuracy Requirements	1414

10.1.38.2.1	Absolute PRS RSRPP accuracy	1414

10.1.38.3	Report mapping	1418

10.1.38.3.1	Absolute PRS-RSRPP Measurement Report Mapping	1418

10.1.38.3.2	Differential Report Mapping for PRS-RSRPP Measurement	1419

10.1.38A	PRS-RSRPP Measurements Based on PRS Aggregation	1420

10.1. 38A.1	Introduction	1420

10.1.38A.2	Measurement Accuracy Requirements	1421

10.1.38A.2.1	Absolute PRS RSRPP accuracy	1421

10.1.38A.3	Report mapping	1421

10.1.38A.3.1	Absolute PRS-RSRPP Measurement Report Mapping	1421

10.1.38A.3.2	Differential Report Mapping for PRS-RSRPP Measurement	1421

10.1.39	UE Rx-Tx time difference measurements for RTT-based PDC	1421

10.1.39.1 *Void* 1421

10.1.39.2	 Measurement Accuracy Requirements for PRS	1421

10.1.39.3	 Measurement Accuracy Requirements for TRS	1424

10.1.40	Void	1428

10.1.41	FR1 DPC report	1428

10.1.41.1	Report mapping	1428

10.1.42	TDCP Measurement Report Mapping	1428

10.1.43	DL-RSCPD Measurements	1430

10.1.43.1	Introduction	1430

10.1.43.2.1	Measurement Accuracy Requirements	1430

10.1.43.3	Report Mapping	1437

10.1.43.3.1	Absolute DL RSCPD Measurement Reporting	1437

10.1.44	DL-RSCP Measurements	1438

10.1.44.1	Introduction	1438

10.1.44.2	Measurement Accuracy Requirements	1438

10.1.44.3	Report Mapping	1446

10.1.44.3.1	Relative DL RSCP Measurement Reporting	1446

10.1A	NR measurements for RedCap	1447

10.1A.1	Introduction	1447

10.1A.2	Intra-frequency RSRP accuracy requirements for FR1	1447

10.1A.2.1	Intra-frequency SS-RSRP accuracy requirements	1447

10.1A.2.1.1	Absolute SS-RSRP Accuracy	1447

10.1A.2.1.2	Relative SS-RSRP Accuracy	1448

10.1A.3	Intra-frequency RSRP accuracy requirements for FR2	1449

10.1A.3.1	Intra-frequency SS-RSRP accuracy requirements	1449

10.1A.3.1.1	Absolute SS-RSRP Accuracy	1449

10.1A.3.1.2	Relative SS-RSRP Accuracy	1449

10.1A.4	Inter-frequency RSRP accuracy requirements for FR1	1449

10.1A.4.1	Inter-frequency SS-RSRP accuracy requirements	1449

10.1A.4.1.1	Absolute SS-RSRP Accuracy in FR1	1449

10.1A.4.1.2	Relative SS-RSRP Accuracy in FR1	1450

10.1A.5	Inter-frequency RSRP accuracy requirements for FR2	1451

10.1A.5.1	Inter-frequency SS-RSRP accuracy requirements	1451

10.1A.5.1.1	Absolute SS-RSRP Accuracy	1451

10.1A.5.1.2	Relative SS-RSRP Accuracy	1451

10.1A.6	Intra-frequency RSRQ accuracy requirements for FR1	1451

10.1A.6.1	Intra-frequency SS-RSRQ accuracy requirements in FR1	1451

10.1A.6.1.1	Absolute SS-RSRQ Accuracy in FR1	1451

10.1A.7	Intra-frequency RSRQ accuracy requirements for FR2	1452

10.1A.7.1	Intra-frequency SS-RSRQ accuracy requirements in FR2	1452

10.1A.7.1.1	Absolute SS-RSRQ Accuracy in FR2	1452

10.1A.8	Inter-frequency RSRQ accuracy requirements for FR1	1452

10.1A.8.1	Inter-frequency SS-RSRQ accuracy requirements in FR1	1452

10.1A.8.1.1	Absolute SS-RSRQ in FR1	1452

10.1A.8.1.2	Relative SS-RSRQ Accuracy in FR1	1453

10.1A.9	Inter-frequency RSRQ accuracy requirements for FR2	1454

10.1A.9.1	Inter-frequency SS-RSRQ accuracy requirements in FR2	1454

10.1A.9.1.1	Absolute SS-RSRQ Accuracy in FR2	1454

10.1A.9.1.2	Relative SS-RSRQ Accuracy in FR2	1454

10.1A.10	 Intra-frequency SINR accuracy requirements for FR1	1454

10.1A.10.1	Intra-frequency SS-SINR accuracy requirements in FR1	1454

10.1A.10.1.1	Absolute SS-SINR Accuracy in FR1	1454

10.1A.11	Intra-frequency SINR accuracy requirements for FR2	1455

10.1A.11.1	Intra-frequency SS-SINR accuracy requirements in FR2	1455

10.1A.11.1.1	Absolute SS-SINR Accuracy in FR2	1455

10.1A.12 	Inter-frequency SINR accuracy requirements for FR1	1455

10.1A.12.1	Inter-frequency SS-SINR accuracy requirements in FR1	1455

10.1A.12.1.1	Absolute SS-SINR Accuracy in FR1	1455

10.1A.12.1.2	Relative SS-SINR Accuracy in FR1	1456

10.1A.13	 Inter-frequency SINR accuracy requirements for FR2	1457

10.1A.13.1	Inter-frequency SS-SINR accuracy requirements in FR2	1457

10.1A.13.1.1	Absolute SS-SINR Accuracy in FR2	1457

10.1A.13.1.2	Relative SS-SINR Accuracy in FR2	1457

10.1A.14	L1-RSRP accuracy requirements for FR1	1457

10.1A.14.1	SSB based L1-RSRP accuracy requirements	1457

10.1A.14.1.1	Absolute Accuracy	1457

10.1A.14.1.2	Relative Accuracy	1458

10.1A.14.2	CSI-RS based L1-RSRP accuracy requirements	1459

10.1A.14.2.1	Absolute Accuracy	1459

10.1A.14.2.2	Relative Accuracy	1460

10.1A.15	 L1-RSRP accuracy requirements for FR2	1461

10.1A.15.1	SSB based L1-RSRP accuracy requirements	1461

10.1A.15.1.1	Absolute Accuracy	1461

10.1A.15.1.2	Relative Accuracy	1461

10.1A.15.2	CSI-RS based L1-RSRP accuracy requirements	1461

10.1A.15.2.1	Absolute Accuracy	1461

10.1A.15.2.2	Relative Accuracy	1461

10.1A.16	RSTD Measurements for RedCap Positioning	1462

10.1A.16.1	Introduction	1462

10.1A.16.2	Measurement Accuracy Requirements	1462

10.1A.16.2.1	Accuracy requirement for RSTD measurement without RX FH	1462

10.1A.16.2.2	Accuracy requirement for RSTD measurement with RX FH	1469

10.1A.16.3	Report Mapping	1480

10.1A.16.3.1	Absolute DL RSTD Measurement Reporting	1480

10.1A.16.3.2	Differential Reporting for DL RSTD Measurement	1480

10.1A.16.3.3	Additional Path Report Mapping for DL RSTD	1480

10.1A.17	PRS-RSRP Measurements for RedCap positioning	1480

10.1A.17.1	Introduction	1480

10.1A.17.2	Measurement Accuracy Requirements	1480

10.1A.17.2.1	Absolute PRS RSRP Accuracy Requirement	1480

10.1A.17.2.2	Relative PRS RSRP Accuracy Requirement	1483

10.1A.17.3	Report Mapping	1483

10.1A.17.3.1	Absolute PRS-RSRP Measurement Report Mapping	1483

10.1A.17.3.2	Differential Report Mapping for PRS-RSRP Measurement	1483

10.1A.18	  UE Rx-Tx Time Difference Measurements for RedCap Positioning	1484

10.1A.18.1	Introduction	1484

10.1A.18.2	Measurement Accuracy Requirements	1484

10.1A.18.2.1	UE Rx-Tx Accuracy Requirement for 2RX RedCap UE without FH	1484

10.1A.18.2.2	UE Rx-Tx Accuracy Requirement for 1RX RedCap UE without FH	1485

10.1A.18.2.3	UE Rx-Tx Accuracy Requirement for 2RX RedCap UE with FH	1490

10.1A.18.3	Report mapping	1500

10.1A.18.3.1	Absolute UE Rx-Tx Measurement Report Mapping	1500

10.1A.18.3.2	Differential UE Rx-Tx Measurement Report Mapping	1500

10.1A.18.3.3	Additional Path Report Mapping for UE Rx-Tx Time Difference	1500

10.1A.19	PRS-RSRPP Measurements for RedCap Positioning	1500

10.1A.19.1	Introduction	1500

10.1A.19.2	Measurement Accuracy Requirements	1501

10.1A.19.2.1	Absolute PRS RSRPP accuracy	1501

10.1A.19.3	Report mapping	1503

10.1A.19.3.1	Absolute PRS-RSRPP Measurement Report Mapping	1503

10.1A.19.3.2	Differential Report Mapping for PRS-RSRPP Measurement	1504

10.2	E-UTRAN measurements	1504

10.2.1	Introduction	1504

10.2.2	E-UTRAN RSRP measurements	1504

10.2.3	E-UTRAN RSRQ measurements	1504

10.2.4	E-UTRAN RSTD measurements	1504

10.2.5	E-UTRAN RS-SINR measurements	1505

10.2.6	E-UTRAN RSRP measurements for CA/DC Idle Mode Measurements	1505

10.2.7	E-UTRAN RSRQ measurements for CA/DC Idle Mode Measurements	1505

10.2A	E-UTRAN measurements for RedCap	1506

10.2A.1	Introduction	1506

10.2A.2	E-UTRAN RSRP measurements	1506

10.2A.3	E-UTRAN RSRQ measurements	1506

10.2A.4	E-UTRAN RS-SINR measurements	1507

10.3	UTRAN FDD Measurements	1507

10.3.1	UTRAN FDD CPICH RSCP	1507

10.3.2	UTRAN FDD CPICH Ec/No	1508

10.4	V2X measurements	1508

10.4.1	Introduction	1508

10.4.2	Intra-frequency PSBCH-RSRP accuracy requirements for FR1	1508

10.4.2.1	PSBCH-RSRP Absolute Accuracy	1508

10.4.2.2	PSBCH-RSRP Relative Accuracy	1509

10.4.2A	Intra-frequency PSBCH-RSRP accuracy requirements for FR1 under CCA	1510

10.4.2A.1	PSBCH-RSRP Absolute Accuracy	1510

10.4.2A.2	PSBCH-RSRP Relative Accuracy	1510

10.4.3	Intra-Frequency SL-RSSI Measurement Accuracy Requirements for FR1	1511

10.4.3.1	Absolute SL-RSSI Accuracy	1511

10.4.3A	Intra-Frequency SL-RSSI Measurement Accuracy Requirements for FR1 under CCA	1511

10.4.3A.1	Absolute SL-RSSI Accuracy	1511

10.4.4	Intra-Frequency L1 SL-RSRP Measurement Accuracy Requirements for FR1	1512

10.4.4.1	Absolute L1 SL-RSRP Accuracy	1512

10.4.4A	Intra-Frequency L1 SL-RSRP Measurement Accuracy Requirements for FR1 under CCA	1512

10.4.4A.1	Absolute L1 SL-RSRP Accuracy	1512

10.4.5	Intra-Frequency Discovery Signal Measurement Accuracy Requirements	1513

10.4.5.1	Absolute Discovery Signal Measurement Accuracy	1513

10.4A	NR Sidelink Measurements for Positioning	1514

10.4A.1	Introduction	1514

10.4A.2	SL RSTD measurements	1514

10.4A.2.1	Measurement Report Mapping	1514

10.4A.2.1.1	Absolute SL RSTD Measurement Reporting	1514

10.4A.2.2	Measurement Accuracy Requirements	1515

10.4A.3	SL PRS-RSRP measurements	1517

10.4A.3.1	Measurement Report Mapping	1517

10.4A.3.1.1	Absolute SL PRS-RSRP Measurement Report Mapping	1517

10.4A.3.2	Measurement Accuracy Requirements	1518

10.4A.3.2.1	Absolute SL PRS-RSRP accuracy	1518

10.4A.4	SL Rx-Tx measurements	1519

10.4A.4.1	Measurement Report Mapping	1519

10.4A.4.1.1	Absolute SL Rx-Tx Measurement Report Mapping	1519

10.4A.4.2	Measurement Accuracy	1521

10.4A.5	SL PRS-RSRPP measurements	1522

10.4A.5.1	Measurement Report Mapping	1522

10.4A.5.1.1	Absolute SL PRS-RSRPP Measurement Report Mapping	1522

10.4A.5.2	Measurement Accuracy	1523

10.4A.5.2.1	Introduction	1523

10.4A.5.2.2	Measurement Accuracy Requirements	1524

10.4A.5.2.2.2	Absolute SL PRS-RSRPP accuracy	1524

10.4A.6	SL AoA measurements	1525

10.4A.6.1	Measurement Report Mapping	1525

10.4A.6.1.1	Absolute SL AoA Measurement Report Mapping	1525

10.4A.7	SL RTOA measurements	1526

10.4A.7.1	Measurement Report Mapping	1526

10.4A.7.1.1	Absolute SL RTOA Measurement Report Mapping	1526

11	Void	1528

12	V2X Requirements	1516

12.1	Introduction	1516

12.2	UE Transmit Timing	1516

12.2.1	Introduction	1516

12.2.2	GNSS as synchronization reference source	1517

12.2.3	NR Cell as synchronization reference source	1517

12.2.4	E-URTAN Cell as synchronization reference source	1517

12.2.5	SyncRef UE as synchronization reference source	1518

12.3	Initiation/Cease of SLSS Transmissions	1518

12.3.1	Introduction	1518

12.3.1.1	Initiation/Cease of SLSS transmissions with NR cell as synchronization reference source	1518

12.3.1.2	Initiation/Cease of SLSS transmissions with EUTRAN cell as synchronization reference source	1519

12.3.1.3	Initiation/Cease of SLSS transmissions with GNSS as synchronization reference source	1520

12.3.1.4	Initiation/Cease of SLSS transmissions with SyncRef UE as synchronization reference source	1520

12.3A	Initiation/Cease of SLSS Transmissions with CCA	1521

12.3A.1	Introduction	1521

12.3A.1.1	Initiation/Cease of SLSS transmissions with NR cell as synchronization reference source	1521

12.3A.1.2	Initiation/Cease of SLSS transmissions with EUTRAN cell as synchronization reference source	1521

12.3A.1.3	Initiation/Cease of SLSS transmissions with GNSS as synchronization reference source	1521

12.3A.1.4	Initiation/Cease of SLSS transmissions with SyncRef UE as synchronization reference source	1522

12.4	Selection / Reselection of V2X Synchronization Reference Source	1522

12.4A	Selection / Reselection of Sidelink Synchronization Reference Source with CCA	1524

12.5	L1 SL-RSRP measurements	1526

12.5.1	Introduction	1526

12.5.2	SL-RSRP measurements	1526

12.6	Congestion Control measurements	1527

12.7	Interruption	1527

12.7.1	Interruptions to WAN due to V2X Sidelink Communication	1527

12.7.2	V2X Sidelink Communication Dropping due to synchronization source change	1527

12.7.3	Interruptions to WAN due to switching between E-UTRA V2X Sidelink and NR V2X Sidelink	1529

12.7.4	Interruptions to WAN at transitions between active and non-active during SL-DRX	1529

12.7.5	Interruptions to V2X sidelink at transitions between active and non-active during DRX	1530

12.7.6	Interruptions to V2X sidelink due to Active BWP switching Requirement	1530

12.7.7	Interruptions to WAN due to SyncRef UE detection and/or Sensing during SL DRX off duration	1531

12.7.8	Interruptions at NR sidelink discovery configuration	1531

12.7.9	Interruptions to WAN due to sidelink carrier addition/release	1531

12.8	Reliability of GNSS signal	1532

12.9	Scheduling availability	1532

12.9.1	Scheduling availability of UE switching between E-UTRA sidelink and NR sidelink	1532

12.9.2	Scheduling availability of UE switching between Uu uplink  and V2X sidelink	1532

12.10	Selection / Reselection of relay UE	1533

12.10.1	Introduction	1533

12.10.2	Selection / Reselection of relay UE	1533

12.11	Component Carrier Addition and Release Delay for Sidelink Carrier Aggregation	1533

12.12	Selection / Reselection of Synchronization Reference Source for NR SL Carrier Aggregation	1534

12A	NR Sidelink Measurements for Positioning	1535

12A.1	Introduction	1535

12A.2	SL RSTD measurements	1536

12A.2.1	Introduction	1536

12A.2.3	Measurement Capability	1536

12A.2.4	Measurement Reporting Requirements	1536

12A.2.5	Measurements Period Requirements	1536

12A.3	SL PRS-RSRP measurements	1537

12A.3.1	Introduction	1537

12A.3.2	Requirements Applicability	1538

12A.3.4	Measurement Reporting Requirements	1538

12A.3.5	Measurements Period Requirements	1538

12A.4	SL Rx-Tx measurements	1539

12A.4.1	Introduction	1539

12A.4.2	Requirements Applicability	1539

12A.4.3	Measurement Capability	1539

12A.4.4	Measurement Reporting Requirements	1539

12A.4.5	Measurement Period Requirements	1540

12A.5	SL PRS-RSRPP measurements	1541

12A.5.1	Introduction	1541

12A.5.2	Requirements Applicability	1541

12A.5.3	Measurement Capability	1541

12A.5.4	Measurement Reporting Requirements	1541

12A.5.5	Measurement Period Requirements	1541

12A.6	SL AoA measurements	1542

12A.6.1	Introduction	1542

12A.6.2	Requirements Applicability	1542

12A.6.3	Measurement Capability	1542

12A.6.4	Measurement Reporting Requirements	1542

12A.6.5	Measurement Period Requirements	1543

12A.7	SL RTOA measurements	1543

12A.7.1	Introduction	1543

12A.7.2	Requirements Applicability	1544

12A.7.3	Measurement Capability	1544

12A.7.4	Measurement Reporting Requirements	1544

12A.7.5	Measurement Period Requirements	1544

13	Measurement Performance Requirements for NR gNB	1545

13.1	UL-RTOA	1545

13.1.1	Report mapping	1545

13.1.1A	Additional Path Report Mapping for UL-RTOA	1549

13.2	gNB Rx-Tx time difference	1552

13.2.1	Report mapping	1552

13.2.1A	Additional Path Report Mapping for gNB Rx-Tx	1556

13.2.2	Measurement Accuracy Requirements	1559

13.2.2.1	Introduction	1559

13.3	UL SRS RSRP measurement	1561

13.3.1	Report mapping	1561

13.3.2	Measurement accuracy requirements	1561

13.3.2.1	Introduction	1561

13.3.2.2	Requirements	1562

13.4	AoA/ZoA	1562

13.4.1	Report mapping	1562

13.5	Timing advance (TADV)	1563

13.5.1	Report mapping	1563

13.6	UL SRS RSRPP measurement	1564

13.6.1	Report mapping	1564

13.7	gNB Rx-Tx time difference measurements for RTT-based PDC	1564

13.7.1	Report mapping	1564

13.7.2	Measurement Accuracy Requirements	1565

13.7.2.1	Introduction	1565

13.7.2.2	Requirements	1565

13.8	UL-RSCP measurement	1566

13.8.1	Report mapping	1566

Annex A (normative): Test Cases	1567

A.1	Purpose of annex	1567

A.2	Requirement classification for statistical testing	1567

A.2.1	Types of requirements in TS 38.133	1567

A.2.1.1	Time and delay requirements on UE higher layer actions	1567

A.2.1.2	Measurements of power levels, relative powers and time	1568

A.2.1.3	Implementation requirements	1568

A.2.1.4	Physical layer timing requirements	1568

A.2.1.5	Requirements under CCA	1568

A.3	RRM test configurations	1569

A.3.1	Reference measurement channels	1569

A.3.1.1	PDSCH	1569

A.3.1.1.1	FDD	1569

A.3.1.1.2	TDD	1570

A.3.1.2	CORESET for RMSI scheduling	1573

A.3.1.2.1	FDD	1573

A.3.1.2.2	TDD	1574

A.3.1.3	CORESET for RMC scheduling	1576

A.3.1.3.1	FDD	1576

A.3.1.3.2	TDD	1578

A.3.1.4	TDD UL/DL configuration	1582

A.3.1A	Reference measurement channels under CCA	1584

A.3.1A.1	PDSCH	1584

A.3.1A.1.1	TDD	1584

A.3.1A.2	CORESET for RMSI scheduling	1585

A.3.1A.2.1	TDD	1585

A.3.1A.3	CORESET for RMC scheduling	1586

A.3.1A.3.1	TDD	1586

A.3.1A.4	TDD UL/DL configuration	1586

A.3.1A.5	RMC burst transmission model	1587

A.3.2.1	Generic OFDMA Channel Noise Generator (OCNG)	1587

A.3.2.1.1	OCNG pattern 1: Generic OCNG pattern for all unused REs	1587

A.3.2.1.2	OCNG pattern 2: Generic OCNG pattern for all unused REs for 2AoA setup	1588

A.3.2.1.3	OCNG pattern 3: Generic OCNG pattern for unused REs in the same bandwidth as CORESET	1588

A.3.2.1.4	OCNG pattern 4: Generic OCNG pattern for all unused REs outside SSB slot(s)	1589

A.3.2.2	Void	1590

A.3.3	Reference DRX configurations	1590

A.3.3.1	DRX Configuration 1: DRX cycle = 40 ms and TAT = 500 ms	1590

A.3.3.2	DRX Configuration 2: DRX cycle = 640 ms and TAT = 500 ms	1590

A.3.3.3	DRX Configuration 3: DRX cycle = 40 ms and TAT = Infinity	1590

A.3.3.4	DRX Configuration 4: DRX cycle = 160 ms and TAT = Infinity	1591

A.3.3.5	DRX Configuration 5: DRX cycle = 320 ms and TAT = Infinity	1591

A.3.3.6	DRX Configuration 6: DRX cycle = 320 ms and TAT = 500 ms	1591

A.3.3.7	DRX Configuration 7: DRX cycle = 640 ms and TAT = Infinity	1591

A.3.3.8	DRX Configuration 8: DRX cycle = 320 ms and TAT = Infinity	1592

A.3.3.9	DRX Configuration 9: DRX cycle = 40 ms and TAT = 500 ms	1592

A.3.3.10	DRX Configuration 10: DRX cycle = 640 ms and TAT = 500 ms	1592

A.3.3.11	DRX Configuration 11: DRX cycle = 20 ms and TAT = Infinity	1592

A.3.3.12	DRX Configuration 12: DRX cycle = 640 ms and TAT = Infinity	1593

A.3.3.13	DRX Configuration X1: DRX cycle = 80 ms and TAT = Infinity	1593

A.3.3.14	DRX Configuration 14: DRX cycle = 160 ms and TAT = Infinity	1593

A.3.4	Test Cases with Different Channel Bandwidths	1593

A.3.4.1	Test Cases with Different E-UTRA Channel Bandwidths	1593

A.3.4.1.1	Introduction	1593

A.3.4.1.2	Principle of testing	1594

A.3.5	Test Cases for Synchronous and Asynchronous DC Operations	1594

A.3.5.1	EN-DC Test Cases for Synchronous and Asynchronous EN-DC Operations	1594

A.3.5.1.1	Introduction	1594

A.3.5.1.2	Principle of Testing	1594

A.3.6	Antenna configurations	1594

A.3.6.1	Antenna configurations for FR1	1594

A.3.6.1.1	Antenna connection for 4 Rx capable UEs	1594

A.3.6.1.1.1	Introduction	1594

A.3.6.1.1.2	Principle of testing	1594

A.3.6.1.2	Antenna connection for 8 Rx capable UEs	1597

A.3.6.1.2.1	Introduction	1597

A.3.6.1.2.2	Principle of testing	1597

A.3.6.2	Antenna configurations for FR2	1599

A.3.6A	Antenna configurations with unlicensed bands	1599

A.3.6A.1	Antenna configurations for FR1	1599

A.3.6A.1.1	Antenna connection for 4 Rx capable UEs	1599

A.3.6A.1.1.1	Introduction	1599

A.3.6A.1.1.2	Principle of testing	1599

A.3.7	EN-DC test setup	1601

A.3.7.1	Introduction	1601

A.3.7.2	E-UTRAN Serving Cell Parameters	1601

A.3.7.2.1	E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR1	1601

A.3.7.2.2	E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR2	1602

A.3.7A	NR FR1-FR2 test setup	1603

A.3.7B	EN-DC test setup with unlicensed bands	1603

A.3.7B.1	Introduction	1603

A.3.7B.2	E-UTRAN Serving Cell Parameters	1603

A.3.7B.2.1	E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) under CCA in FR1	1603

A.3.7C	LTE-FR1/FR2 test setup	1604

A.3.7D	NE-DC test setup	1604

A.3.7D.1	Introduction	1604

A.3.7D.2	E-UTRAN Serving Cell Parameters	1604

A.3.7D.2.1	E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR1	1604

A.3.7D.2.2	E-UTRAN Serving Cell Parameters for Tests with NR Cell(s) in FR2	1604

A.3.8	PRACH configurations	1605

A.3.8.1	Introduction	1605

A.3.8.2	PRACH configurations in FR1	1605

A.3.8.2.1	FR1 PRACH configuration 1	1605

A.3.8.2.2	FR1 PRACH configuration 2	1605

A.3.8.2.3	FR1 PRACH configuration 3	1606

A.3.8.2.4	FR1 PRACH configuration 4	1607

A.3.8.2.5	FR1 PRACH configuration 5	1607

A.3.8.2.6	FR1 PRACH configuration 6	1608

A.3.8.3	PRACH configurations in FR2	1608

A.3.8.3.1	FR2 PRACH configuration 1	1608

A.3.8.3.2	FR2 PRACH configuration 2	1609

A.3.8.3.3	FR2 PRACH configuration 3	1610

A.3.8.3.4	FR2 PRACH configuration 4	1610

A.3.8.3.5	FR2 PRACH configuration 5	1611

A.3.8.3.6	FR2 PRACH configuration 6	1611

A.3.8A	PRACH configurations under CCA	1612

A.3.8A.1	Introduction	1612

A.3.8A.2	PRACH configurations in FR1	1612

A.3.8A.2.1	FR1 PRACH configuration 1 under CCA	1612

A.3.8A.2.2	FR1 PRACH configuration 2 under CCA	1613

A.3.9	BWP configurations	1614

A.3.9.1	Introduction	1614

A.3.9.2	Downlink BWP configurations	1614

A.3.9.2.1	Initial BWP	1614

A.3.9.2.2	Dedicated BWP	1615

A.3.9.3	Uplink BWP configurations	1615

A.3.9.3.1	Initial BWP	1615

A.3.9.3.2	Dedicated BWP	1616

A.3.9A	BWP configurations for RedCap	1616

A.3.9A.1	Introduction	1616

A.3.9A.2	Downlink BWP configurations	1616

A.3.9A.2.1	Dedicated BWP	1616

A.3.9A.3	Uplink BWP configurations	1617

A.3.9A.3.1	Dedicated BWP	1617

A.3.10	SSB Configurations	1617

A.3.10.1	SSB Configurations for FR1	1617

A.3.10.1.1	SSB pattern 1 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz	1617

A.3.10.1.5	SSB pattern 5 in FR1: SSB allocation for SSB SCS=15 kHz starting from odd SFN in 10 MHz	1619

A.3.10.1.6	SSB pattern 6 in FR1: SSB allocation for SSB SCS=30 kHz starting from odd SFN in 40 MHz	1619

A.3.10.1.7	SSB pattern 7 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz	1619

A.3.10.1.8	SSB pattern 8 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz	1620

A.3.10.1.9	SSB pattern 9 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz	1620

A.3.10.1.10	SSB pattern 10 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz	1620

A.3.10.1.11	SSB pattern 11 in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz	1621

A.3.10.1.12	SSB pattern 12 in FR1: SSB allocation for SSB SCS=30 kHz in 40 MHz	1621

A.3.10.1.13	SSB pattern 13 in FR1: SSB allocation for SSB SCS=15 kHz in 3 MHz	1621

A.3.10.2	SSB Configurations for FR2	1622

A.3.10.2.1	SSB pattern 1 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1622

A.3.10.2.2	SSB pattern 2 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz	1622

A.3.10.2.3	SSB pattern 3 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1623

A.3.10.2.4	SSB pattern 4 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz	1623

A.3.10.2.5	SSB pattern 5 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1623

A.3.10.2.6	SSB pattern 6 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz	1624

A.3.10.2.7	SSB pattern 7 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1624

A.3.10.2.8	SSB pattern 8 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz	1624

A.3.10.2.9	SSB pattern 9 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1625

A.3.10.2.10	SSB pattern 10 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz	1625

A.3.10.2.19	SSB pattern 19 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1629

A.3.10.2.20	SSB pattern 20 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz	1630

A.3.10.2.21	SSB pattern 21 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1630

A.3.10.2.22	SSB pattern 22 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz	1631

A.3.10.2.23	SSB pattern 23 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1631

A.3.10.2.24	SSB pattern 24 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz	1631

A.3.10.2.25	SSB pattern 25 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1632

A.3.10.2.26	SSB pattern 26 in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1632

A.3.10.2.27	SSB pattern 27 in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz	1633

A.3.10A	SSB Configurations under CCA	1633

A.3.10A.1	SSB Configurations under CCA for FR1	1633

A.3.10A.1.1	SSB pattern 1 under CCA for semi-static channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz	1633

A.3.10A.1.2	SSB pattern 2 under CCA for dynamic channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz	1634

A.3.10A.1.3	SSB pattern 3 under CCA for semi-static channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz	1634

A.3.10A.1.4	SSB pattern 4 under CCA for dynamic channel access: SSB allocation for SSB SCS=30 kHz in 40 MHz	1635

A.3.10B	SSB Configurations for RedCap	1635

A.3.10B.1	SSB Configurations for FR1	1635

A.3.10B.1.1	SSB pattern 1 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz	1635

A.3.10B.1.2	SSB pattern 2 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz	1636

A.3.10B.1.3	SSB pattern 3 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz starting from odd SFN in 20 MHz	1636

A.3.10B.1.4	SSB pattern 4 for RedCap in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz	1637

A.3.10B.1.5	SSB pattern 5 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz	1637

A.3.10B.1.6	SSB pattern 6 for RedCap in FR1: SSB allocation for SSB SCS=15 kHz in 10 MHz	1638

A.3.10B.1.7	SSB pattern 7 for RedCap in FR1: SSB allocation for SSB SCS=30 kHz in 20 MHz	1638

A.3.10B.2	SSB Configurations for FR2	1639

A.3.10B.2.1	SSB pattern 1 for RedCap in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1639

A.3.10B.2.2	SSB pattern 2 for RedCap in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1639

A.3.10B.2.3	SSB pattern 3 for RedCap in FR2: SSB allocation for SSB SCS=120 kHz in 100 MHz	1640

A.3.10B.2.4	SSB pattern 4 for RedCap in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz	1640

A.3.10B.2.5	SSB pattern 5 for RedCap in FR2: SSB allocation for SSB SCS=240 kHz in 100 MHz	1641

A.3.11	SMTC Configurations	1641

A.3.11.1	SMTC pattern 1: SMTC period = 20 ms with SMTC duration = 1 ms	1641

A.3.11.2	SMTC pattern 2: SMTC period = 20 ms with SMTC duration = 5 ms	1641

A.3.11.3	SMTC pattern 3: SMTC period = 160 ms with SMTC duration = 1 ms	1641

A.3.11.4	SMTC pattern 4: SMTC period = 20 ms with SMTC duration = 1 ms	1642

A.3.11.5	SMTC pattern 5: SMTC period = 20 ms with SMTC duration = 5 ms	1642

A.3.11.6	SMTC pattern 6: SMTC period = 20 ms with SMTC duration = 5 ms	1642

A.3.11.7	SMTC pattern 7: SMTC period = 20 ms with SMTC duration = 5 ms	1642

A.3.11.8	SMTC pattern 8: SMTC period = 10 ms with SMTC duration = 1 ms	1642

A.3.11.9	SMTC pattern 9: SMTC period = 20 ms with SMTC duration = 1 ms	1642

A.3.11.10	SMTC pattern 10: SMTC period = 80 ms with SMTC duration = 1 ms	1643

A.3.11.11	SMTC pattern 11: SMTC period = 80 ms with SMTC duration = 5 ms	1643

A.3.11.12	SMTC pattern 12: SMTC period = 20 ms with SMTC duration = 5 ms	1643

A.3.11A	SMTC Configurations for RedCap	1643

A.3.11A.0	Introduction	1643

A.3.11A.1	SMTC pattern 1 for RedCap: SMTC period = 40 ms with SMTC duration = 1 ms	1644

A.3.11A.2	SMTC pattern 2 for RedCap: SMTC period = 80 ms with SMTC duration = 1 ms	1644

A.3.11A.3	SMTC pattern 3 for RedCap: SMTC period = 40 ms with SMTC duration = 1 ms	1644

A.3.11A.4	SMTC pattern 4 for RedCap: SMTC period = 80 ms with SMTC duration = 5 ms	1644

A.3.12	Test Cases with Different CC Configurations	1644

A.3.12.1 EN-DC Test Cases with Different EN-DC Configurations	1644

A.3.12.1.1	Introduction	1644

A.3.12.1.2	Principle of testing	1644

A.3.12.2	Carrier Aggregation Test Cases with Different CA Configurations	1645

A.3.12.2.1	Introduction	1645

A.3.12.2.2	Principle of testing	1645

A.3.13	Test Cases in SA and EN-DC Operations	1645

A.3.13.1	Introduction	1645

A.3.13.2	Principle of Testing	1645

A.3.13A	Test Cases involving E-UTRA/FR1 and FR2 carriers	1645

A.3.13A.1	Introduction	1645

A.3.13A.2	Principle of Testing in EN-DC	1646

A.3.13A.3	Principle of Testing in SA	1646

A.3.13A.4	Principle of Testing in E-UTRA	1646

A.3.13A.5	Principle of Testing in NR-DC	1647

A.3.13B	 Test Cases for EN-DC and NE-DC Operations	1647

A.3.13B.1	Active BWP switch Test Cases for EN-DC and NE-DC Operations	1647

A.3.13B.1.1	Introduction	1647

A.3.13B.1.2	Principle of Testing	1647

A.3.13B.2	SFTD accuracy Test Cases for EN-DC and NE-DC Operations	1647

A.3.13B.2.1	Introduction	1647

A.3.13B.2.2	Principle of Testing	1647

A.3.14	CSI-RS configurations	1648

A.3.14.1	FDD	1648

A.3.14.2	TDD	1650

A.3.15	Angle of Arrival (AoA) for FR2 RRM test cases	1655

A.3.15.1	Setup 1: Single AoA in Rx beam peak direction	1655

A.3.15.2	Setup 2: Single AoA in non Rx beam peak direction	1655

A.3.15.2.1	Setup 2a: Single AoA in non Rx beam peak direction without change in direction	1655

A.3.15.2.2	Setup 2b: Single AoA in non Rx beam peak direction with change in direction	1656

A.3.15.3	Setup 3: 2 AoAs	1656

A.3.15.4	Setup 4: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak	1656

A.3.15.4.1	Setup 4a: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak without change in direction	1656

A.3.15.4.2	Setup 4b: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak with change in direction	1656

A.3.15.4.3	Setup 4c: 2 AoAs, 1 AoA in Rx beam peak direction, 1 in non Rx beam peak for power class 6 UE supporting simultaneous reception from multiple directions	1656

A.3.15.5	Setup 5: 2 AoAs for simultaneous reception with QCL Type-D	1657

A.3.15.6	Setup 6: 3 AoAs for simultaneous reception with different QCL Type-D	1657

A.3.15.7	Setup 7: 3 AoAs	1657

A.3.15C	Angle of Arrival (AoA) for FR2-NTN RRM test cases	1657

A.3.15C.1	Setup 1: Single AoA	1657

A.3.15C.2	Setup 2: 2 AoAs	1658

A.3.16	TCI State Configuration	1658

A.3.16.1	Introduction	1658

A.3.16.2	TCI states	1658

A.3.16A	Unified TCI State Configuration	1658

A.3.16A.1	Introduction	1658

A.3.16A.2	DLorJoint TCI states	1659

A.3.16A.3	UL TCI states	1660

A.3.16B	 LTM Candidate TCI State Configuration	1660

A.3.16B.1	Introduction	1660

A.3.16B.2	LTM candidate DLorJoint TCI states	1661

A.3.16B.3	LTM candidate UL TCI states	1661

A.3.17	Configurations of CSI-RS for tracking	1662

A.3.17.1	Configuration of CSI-RS for tracking for FR1	1662

A.3.17.1.1	FDD	1662

A.3.17.1.2	TDD	1665

A.3.17.2	Configuration of CSI-RS for tracking for FR2	1669

A.3.17.2.1	TDD	1669

A.3.17.2.2	FDD	1672

A.3.18	Additional definitions related to OTA testing for FR2 RRM test cases	1672

A.3.18.1	Introduction	1672

A.3.18.2	PRACH Power Measurement	1672

A.3.19	Test applicability for DAPS handover	1672

A.3.19.1	Introduction	1672

A.3.19.2	Principle of testing	1672

A.3.20	MsgA configurations	1673

A.3.20.1	Introduction	1673

A.3.20.2	MsgA configurations in FR1	1673

A.3.20.2.1	FR1 MsgA configuration 1	1673

A.3.20.2.2	FR1 MsgA configuration 2	1674

A.3.20.3	MsgA configurations in FR2	1675

A.3.20.3.1	FR2 MsgA configuration 1	1675

A.3.20.3.2	FR2 MsgA configuration 2	1676

A.3.20A	MsgA configurations under CCA	1677

A.3.20A.1	Introduction	1677

A.3.20A.2	MsgA configurations in FR1	1677

A.3.20A.2.1	FR1 MsgA configuration 1 under CCA	1677

A.3.20A.2.2	FR1 MsgA configuration 2 under CCA	1678

A.3.21	V2X sidelink communication	1679

A.3.21.1	Introduction	1679

A.3.21.2	Reference resource pool configurations for V2X Sidelink Communication	1679

A.3.21.3	Reference measurement channels for V2X Sidelink Communication	1682

A.3.21.4	Reference SL-DRX configurations	1683

A.3.21.4.1	SL-DRX Configuration 1: SL-DRX cycle = 40 ms	1683

A.3.21.4.2	SL-DRX Configuration 2: SL-DRX cycle = 320 ms	1683

A.3.21.4.3	SL-DRX Configuration 3: SL-DRX cycle = 640 ms	1683

A.3.21A	NR Sidelink Measurements for Positioning	1683

A.3.21A.1	Introduction	1683

A.3.21A.2	NR SL-PRS configurations	1684

A.3.21A.2.1	NR SL-PRS configurations for FR1	1684

A.3.22	CSI-IM configurations	1684

A.3.22.1	FDD	1684

A.3.22.2	TDD	1684

A.3.23	Spatial Relation Configuration	1685

A.3.23.1	Introduction	1685

A.3.23.2	Spatial Relation	1686

A.3.24	SRS configuration	1686

A.3.25	Channel bandwidth (CBW) configurations	1688

A.3.25.1	DL UE specific CBW	1688

A.3.25.2	UL UE specific CBW	1689

A.3.26	CCA model	1689

A.3.26.1	Introduction	1689

A.3.26.2	CCA model for operation on a carrier frequency with CCA in FR1	1689

A.3.26.2.1	DL CCA model	1689

A.3.26.2.2	UL CCA model	1690

A.3.26.3	CCA model for operation on a carrier frequency with CCA in FR2-2	1691

A.3.26.3.1	DL CCA model	1691

A.3.26.3.2	UL CCA model	1691

A.3.26.4	CCA model for operation on a sidelink carrier frequency with CCA	1692

A.3.26.4.1	CCA model for SyncRef UE	1692

A.3.27	Void	1693

A.3.27.1	Void	1693

A.3.27.2	 Void	1693

A.3.27.3	Void	1693

A.3.27.4	Void	1693

A.3.27.5	Void	1693

A.3.28	Discovery Burst Transmission Window configuration under CCA	1693

A.3.28.1	DBT Window pattern 1: DBT Window period = 20 ms with DBT Window duration = 1 ms	1693

A.3.29	Testing principles for UE capable of only NR bands with shared spectrum access	1693

A.3.29.1	Introduction	1693

A.3.29.2	Principle of testing for UE capable of EN-DC with only NR bands with shared spectrum access	1694

A.3.29.3	Principle of testing for UE capable of SA operation with only NR bands with shared spectrum access	1694

A.3.30	CSI-RS configurations for RRM	1695

A.3.30.1	FDD	1695

A.3.30.2	TDD	1695

A.3.31	PRS Configurations	1697

A.3.31.1	PRS Configurations for FR1	1697

A.3.31.1.1	PRS pattern 1 in FR1: SCS=15 kHz	1697

A.3.31.1.2	PRS pattern 2 in FR1: SCS=30 kHz	1698

A.3.31.2	PRS Configurations for FR2	1699

A.3.31.2.1	PRS pattern 1 in FR2: SCS=120 kHz	1699

A.3.32	NR sidelink discovery	1699

A.3.32.1	Introduction	1699

A.3.32.2	Reference resource pool configurations for NR Sidelink Discovery	1699

A.3.32.3	Principle of Testing	1700

A.3.33	PRS Processing Window (PPW) configurations	1700

A.3.34	Testing principles for test cases related to PRS measurements	1700

A.3.34.1	Introduction	1700

A.3.34.2	Test cases in RRC\_INACTIVE state	1700

A.3.34.3	Test cases for PRS measurements with gaps in RRC\_CONNECTED state	1701

A.3.34.4	Test cases for PRS measurements without gaps in RRC\_CONNECTED state	1701

A.3.34.5	Testing principles for positioning measurements by aggregating PRS resources from multiple PFLs	1701

A.3.34.6	Testing principles for carrier phase measurement for positioning	1702

A.3.34.7	Test cases in RRC\_IDLE state	1702

A.3.35	Testing principle for RedCap UE	1702

A.3.35.1	Introduction	1702

A.3.35.2	Principle of testing for FR1	1702

A.3.35.3	Principle of testing for FR2	1702

A.3.35.4	Principle of testing for PRS measurement	1702

A.3.36	Testing related to Satellite access	1703

A.3.36.1	Introduction	1703

A.3.36.1	Introduction	1703

A.3.36.2	Principle of testing GSO and NGSO scenarios	1703

A.3.36.2	Principle of testing different RRM requirements	1703

A.3.36.3	Principle of testing different ephemeris formats	1704

A.3.36.4	General setup for SIB19	1706

A.3.36.5	Satellite specific parameters configuration	1707

A.3.36.5.1	Satellite specific configuration for serving cell	1707

A.3.36.5.2	Satellite specific configuration for neighbour cell	1707

A.3.37	Reference Cell DTX configurations	1708

A.3.37.1	Cell DTX Configuration 1: Cell DTX cycle = 160 ms and TAT = Infinity	1708

A.3.38	DL-PRS Measurement Time Window configurations	1708

A.4	EN-DC tests with all NR cells in FR1	1709

A.4.1	Void	1709

A.4.2	Void	1709

A.4.3	RRC\_CONNECTED state mobility	1709

A.4.3.1	Void	1709

A.4.3.2	RRC Connection Mobility Control	1709

A.4.3.2.1	Void	1709

A.4.3.2.2	Random Access	1709

A.4.3.2.2.1	4-step RA type contention based random access test in FR1 for PSCell in EN-DC	1709

A.4.3.2.2.2	4-step RA type n on-contention based random access test in FR1 for PSCell in EN-DC	1712

A.4.3.2.2.3	2-step RA type contention based random access test in FR1 for PSCell in EN-DC	1714

A.4.3.2.2.4	2-step RA type non-contention based random access test in FR1 for PSCell in EN-DC	1717

A.4.3.2.3	Void	1719

A.4.3.3	Handover with PSCell from EN-DC to EN-DC with known target PSCell in FR1	1719

A.4.3.3.1	Test Purpose and Environment	1719

A.4.3.3.2	Test Requirements	1722

A.4.4	Timing	1723

A.4.4.1	UE transmit timing	1723

A.4.4.1.1	NR UE Transmit Timing Test for FR1	1723

A.4.4.1.1.1	Test Purpose and environment	1723

A.4.4.1.1.2	Test requirements	1725

A.4.4.1.2	NR UE Transmit Timing Test for two TRPs in FR1	1726

A.4.4.1.2.1	Test Purpose and environment	1726

A.4.4.1.2.2	Test requirements	1729

A.4.4.2	UE timer accuracy	1730

A.4.4.3	Timing advance	1730

A.4.4.3.1	EN-DC FR1 timing advance adjustment accuracy	1730

A.4.4.3.1.1	Test Purpose and Environment	1730

A.4.4.3.1.2	Test Parameters	1730

A.4.4.3.1.3	Test Requirements	1733

A.4.5	Signaling characteristics	1733

A.4.5.1	Radio link Monitoring	1733

A.4.5.1.1	Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in non-DRX mode	1733

A.4.5.1.1.1	Test Purpose and Environment	1733

A.4.5.1.1.2	Test Requirements	1737

A.4.5.1.2	Radio Link Monitoring In-sync Test for FR1 PSCell configured with SSB-based RLM RS in non-DRX mode	1737

A.4.5.1.2.1	Test Purpose and Environment	1737

A.4.5.1.2.2	Test Requirements	1740

A.4.5.1.3	Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in DRX mode	1740

A.4.5.1.3.1	Test Purpose and Environment	1740

A.4.5.1.3.2	Test Requirements	1743

A.4.5.1.4	Radio Link Monitoring In-sync Test for FR1 PSCell configured with SSB-based RLM RS in DRX mode	1743

A.4.5.1.4.1	Test Purpose and Environment	1743

A.4.5.1.4.2	Test Requirements	1746

A.4.5.1.5	EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode	1746

A.4.5.1.5.1	Test Purpose and Environment	1746

A.4.5.1.5.2	Test Requirements	1749

A.4.5.1.6	EN-DC Radio Link Monitoring In-sync Test for FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode	1750

A.4.5.1.6.1	Test Purpose and Environment	1750

A.4.5.1.6.2	Test Requirements	1752

A.4.5.1.7	EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with CSI-RS-based RLM in DRX mode	1753

A.4.5.1.7.1	Test Purpose and Environment	1753

A.4.5.1.7.2	Test Requirements	1755

A.4.5.1.8	EN-DC Radio Link Monitoring In-sync Test for FR1 PSCell configured with CSI-RS-based RLM in DRX mode	1756

A.4.5.1.8.1	Test Purpose and Environment	1756

A.4.5.1.8.2	Test Requirements	1759

A.4.5.1.9	Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS for UE fulfilling relaxed measurement criterion	1759

A.4.5.1.9.1	Test Purpose and Environment	1759

A.4.5.1.10	EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with CSI-RS-based RLM in non-DRX mode when CD-SSB is outside active BWP	1762

A.4.5.1.10.1	Test Purpose and Environment	1762

A.4.5.1.11	Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in non-DRX mode when CD-SSB is outside active BWP	1762

A.4.5.1.11.1	Test Purpose and Environment	1762

A.4.5.1.11.2	Test Requirements	1763

A.4.5.1.12	EN-DC Radio Link Monitoring Out-of-sync Test for FR1 PSCell configured with SSB-based RLM RS in non-DRX mode for UE supporting NCD-SSB based measurement outside active BWP	1763

A.4.5.1.12.1	Test Purpose and Environment	1763

A.4.5.1.12.2	Test Requirements	1766

A.4.5.2	Interruption	1766

A.4.5.2.1	E-UTRAN – NR FR1 interruptions at transitions between active and non-active during DRX in synchronous EN-DC	1766

A.4.5.2.1.1	Test Purpose and Environment	1766

A.4.5.2.1.2	Test Requirements	1768

A.4.5.2.2	E-UTRAN – NR FR1 interruptions at transitions between active and non-active during DRX in asynchronous EN-DC	1768

A.4.5.2.2.1	Test Purpose and Environment	1768

A.4.5.2.2.2	Test Requirements	1770

A.4.5.2.3	E-UTRAN – NR FR1 interruptions during measurements on deactivated NR SCC in synchronous EN-DC	1770

A.4.5.2.3.1	Test Purpose and Environment	1770

A.4.5.2.3.2	Test Requirements	1774

A.4.5.2.4	E-UTRAN – NR FR1 interruptions during measurements on deactivated NR SCC in asynchronous EN-DC	1775

A.4.5.2.4.1	Test Purpose and Environment	1775

A.4.5.2.4.2	Test Requirements	1779

A.4.5.2.5	E-UTRAN – NR FR1 interruptions during measurements on deactivated E-UTRAN SCC in synchronous EN-DC	1779

A.4.5.2.5.1	Test Purpose and Environment	1779

A.4.5.2.5.2	Test Requirements	1781

A.4.5.2.6	E-UTRAN – NR FR1 interruptions during measurements on deactivated E-UTRAN SCC in asynchronous EN-DC	1782

A.4.5.2.6.1	Test Purpose and Environment	1782

A.4.5.2.6.2	Test Requirements	1784

A.4.5.2.7	Void	1784

A.4.5.2.8	E-UTRAN - NR FR1 interruptions at NR SRS carrier based switching in asynchronous EN-DC	1784

A.4.5.2.8.1	Test Purpose and Environment	1784

A.4.5.2.8.2	Test Requirements	1787

A.4.5.2.9	E-UTRAN – NR interruptions at E-UTRA SRS carrier based switching	1787

A.4.5.2.9.1	Test Purpose and Environment	1787

A.4.5.2.9.2	Test Requirements	1790

A.4.5.2.10	E-UTRAN – NR FR1 interruptions due to RRM and RLM/BFD measurements on deactivated NR PSCell	1790

A.4.5.2.10.1	Test Purpose and Environment	1790

A.4.5.2.10.2	Test Requirements	1792

A.4.5.2.11	E-UTRAN - NR FR1 interruptions at NR SRS antenna port switching with 1 SRS symbol in a slot in synchronous EN-DC	1792

A.4.5.2.11.1	Test Purpose and Environment	1792

A.4.5.2.11.2	Test Requirements	1795

A.4.5.2.12	E-UTRAN - NR FR1 interruptions at NR SRS antenna port switching in asynchronous EN-DC	1795

A.4.5.2.12.1	Test Purpose and Environment	1795

A.4.5.3	SCell Activation and Deactivation Delay	1799

A.4.5.3.1	SCell Activation and deactivation of known SCell in FR1 for 160 ms SCell measurement cycle	1799

A.4.5.3.1.1	Test Purpose and Environment	1799

A.4.5.3.1.2	Test Requirements	1805

A.4.5.3.2	SCell Activation and deactivation of known SCell in FR1 for 640 ms SCell measurement cycle	1805

A.4.5.3.2.1	Test Purpose and Environment	1805

A.4.5.3.2.2	Test Requirements	1805

A.4.5.3.3	SCell Activation and deactivation of unknown SCell in FR1	1806

A.4.5.3.3.1	Test Purpose and Environment	1806

A.4.5.3.3.2	Test Requirements	1806

A.4.5.3.4	SCell Activation and deactivation of multiple unknown SCells in FR1 with single activation/deactivation command	1806

A.4.5.3.4.1	Test Purpose and Environment	1807

A.4.5.3.4.2	Test Requirements	1809

A.4.5.3.5	Direct SCell activation at SCell addition of known SCell in FR1	1809

A.4.5.3.5.1	Test Purpose and Environment	1809

A.4.5.3.5.2	Test Requirements	1814

A.4.5.3.6	Fast SCell Activation of known SCell in FR1 for 160 ms SCell measurement cycle	1814

A.4.5.3.6.1	Test Purpose and Environment	1814

A.4.5.3.6.2	Test Requirements	1817

A.4.5.3.7	Fast SCell Activation of known SCell in FR1 for 640 ms SCell measurement cycle	1818

A.4.5.3.7.1	Test Purpose and Environment	1818

A.4.5.3.7.2	Test Requirements	1818

A.4.5.3.8	SCell Activation and deactivation of unknown SCell in FR1 for UE capable of short measurement interval	1818

A.4.5.3.8.1	Test Purpose and Environment	1818

A.4.5.3.8.2	Test Requirements	1819

A.4.5.3.9	SCell Activation of unknown SCell with valid L3 measurement results in FR1 for 160 ms SCell measurement cycle	1820

A.4.5.3.9.1	Test Purpose and Environment	1820

A.4.5.3.9.2	Test Requirements	1825

A.4.5.3.10	SCell Activation of multiple unknown SCells in FR1 with L3 reporting with single activation/deactivation command in non-DRX	1826

A.4.5.3.10.1	Test Purpose and Environment	1826

A.4.5.3.10.2	Test Requirements	1828

A.4.5.3.11	TRS-based SCell Activation of SSB-less SCell in FR1 collocated inter-band	1829

A.4.5.3.11.1	Test Purpose and Environment	1829

A.4.5.3.11.2	Test Requirements	1832

A.4.5.3.12	Inter-band SSB-less Scell activation using A-TRS	1833

A.4.5.3.12.1	Test Purpose and Environment	1833

A.4.5.3.12.2	Test Requirements	1836

A.4.5.4	UE UL carrier RRC reconfiguration Delay	1836

A.4.5.4.1	UE UL carrier RRC reconfiguration Delay	1836

A.4.5.4.1.1 Test Purpose and Environment	1836

A.4.5.4.1.2	Test Requirements	1841

A.4.5.5	Beam Failure Detection and Link recovery procedures	1841

A.4.5.5.1	EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in non-DRX mode	1841

A.4.5.5.1.1	Test Purpose and Environment	1841

A.4.5.5.1.2	Test Requirements	1845

A.4.5.5.2	EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in DRX mode	1845

A.4.5.5.2.1	Test Purpose and Environment	1845

A.4.5.5.2.2	Test Requirements	1848

A.4.5.5.3	EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with CSI-RS-based BFD and LR in non-DRX mode	1849

A.4.5.5.3.1	Test Purpose and Environment	1849

A.4.5.5.3.2	Test Requirements	1852

A.4.5.5.4	EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with CSI-RS-based BFD and LR in DRX mode	1853

A.4.5.5.4.1	Test Purpose and Environment	1853

A.4.5.5.4.2	Test Requirements	1856

A.4.5.5.5	EN-DC Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in non-DRX mode	1857

A.4.5.5.5.1	Test Purpose and Environment	1857

A.4.5.5.5.2	Test Requirements	1860

A.4.5.5.6	EN-DC Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in DRX mode	1861

A.4.5.5.6.1	Test Purpose and Environment	1861

A.4.5.5.6.2	Test Requirements	1864

A.4.5.5.7	EN-DC TRP specific Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in non-DRX mode	1865

A.4.5.5.7.1	Test Purpose and Environment	1865

A.4.5.5.7.2	Test Requirements	1868

A.4.5.5.8	EN-DC TRP specific Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in non-DRX mode	1869

A.4.5.5.8.1	Test Purpose and Environment	1869

A.4.5.5.8.2	Test Requirements	1873

A.4.5.6	Active BWP switch	1873

A.4.5.6.1	DCI-based and Timer-based Active BWP Switch	1873

A.4.5.6.1.1	E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC	1873

A.4.5.6.1.2	E-UTRAN – NR PSCell FR1 DL active BWP switch with FR1 SCell in non-DRX in synchronous EN-DC	1877

A.4.5.6.2	RRC-based Active BWP Switch	1882

A.4.5.6.3	Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs	1885

A.4.5.6.3.1	Simultaneous E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in EN-DC on multiple CCs	1885

A.4.5.6.4	Simultaneous RRC-based Active BWP Switch on multiple CCs	1890

A.4.5.6.4.1	E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC on multiple CCs	1890

A.4.5.6.4.1.1	Test Purpose and Environment	1890

A.4.5.6.4.1.2	Test Requirements	1894

A.4.5.6.4.2	E-UTRAN – NR FR1 PSCell SCell dormancy switch of two FR1 SCells inside active time	1894

A.4.5.6.4.2.1	Test Purpose and Environment	1894

A.4.5.6.4.2.2	Test Requirements	1900

A.4.5.6.5	SCell dormancy switch	1900

A.4.5.6.5.1	E-UTRAN – NR FR1 PSCell SCell dormancy switch of single FR1 SCell outside active time	1900

A.4.5.6.5.2	E-UTRAN – NR FR1 PSCell SCell dormancy switch of two FR1 SCells inside active time	1905

A.4.5.6.5.2.1	Test Purpose and Environment	1905

A.4.5.6.5.2.2	Test Requirements	1909

A.4.5.7	PSCell addition and release delay	1909

A.4.5.7.1	Addition and Release Delay of known NR PSCell	1909

A.4.5.7.1.1	Test purpose and environment	1909

A.4.5.7.1.2	Test Requirements	1912

A.4.5.8	DL Interruptions at switching between two uplink carriers	1912

A.4.5.8.1	Test Purpose and Environment	1912

A.4.5.8.2	Test Requirements	1915

A.4.5.9	UE specific CBW change	1915

A.4.5.9.1	UE specific CBW change on FR1 NR PSCell with non-DRX in synchronous EN- DC	1915

A.4.5.9.1.1	Test Purpose and Environment	1915

A.4.5.9.1.2	Test Requirements	1917

A.4.5.10	PSCell activation and deactivation delay	1917

A.4.5.10.1	PSCell activation and deactivation delay	1917

A.4.5.10.1.1	Test purpose and environment	1917

A.4.5.10.1.2	Test Requirements	1920

A.4.5.11	Conditional PSCell addition and release delay (FR1 EN-DC)	1920

A.4.5.11.1	Conditional PSCell Addition and Release Delay	1920

A.4.5.11.1.1	Test purpose and environment	1920

A.4.5.11.1.2	Test Parameters	1920

A.4.5.11.1.3	Test Requirements	1923

A.4.6	Measurement procedure	1923

A.4.6.1	Intra-frequency Measurements	1923

A.4.6.1.1	EN-DC event triggered reporting tests without gap under non-DRX	1923

A.4.6.1.1.1	Test purpose and Environment	1923

A.4.6.1.1.2	Test parameters	1923

A.4.6.1.1.3	Test Requirements	1925

A.4.6.1.2	EN-DC event triggered reporting tests without gap under DRX	1925

A.4.6.1.2.1	Test purpose and Environment	1925

A.4.6.1.2.2	Test parameters	1925

A.4.6.1.2.2	Test Requirements	1927

A.4.6.1.3	EN-DC event triggered reporting tests with per-UE gaps under non-DRX	1927

A.4.6.1.3.1	Test purpose and Environment	1927

A.4.6.1.3.2	Test parameters	1928

A.4.6.1.3.3	Test Requirements	1930

A.4.6.1.4	EN-DC event triggered reporting tests with per-UE gaps under DRX	1930

A.4.6.1.4.1	Test purpose and Environment	1930

A.4.6.1.4.2	Test parameters	1930

A.4.6.1.4.3	Test Requirements	1932

A.4.6.1.5	EN-DC event triggered reporting tests without gap under non-DRX with SSB index reading	1932

A.4.6.1.5.1	Test purpose and Environment	1932

A.4.6.1.5.2	Test parameters	1932

A.4.6.1.5.3	Test Requirements	1934

A.4.6.1.6	EN-DC event triggered reporting tests with SSB index reading with per-UE gaps	1934

A.4.6.1.6.1	Test purpose and Environment	1934

A.4.6.1.6.2	Test parameters	1934

A.4.6.1.6.3	Test Requirements	1935

A.4.6.1.7	EN-DC event triggered reporting tests under DRX for UE configured with highSpeedMeasFlag-r16	1936

A.4.6.1.7.1	Test purpose and Environment	1936

A.4.6.1.7.2	Test parameters	1936

A.4.6.1.7.3	Test Requirements	1938

A.4.6.1.8	EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used for UE configured with *highSpeedMeasCA-Scell-r17* 1938

A.4.6.1.8.1	Test Purpose and Environment	1938

A.4.6.1.8.2	Test Requirements	1941

A.4.6.1.9	EN-DC event triggered reporting tests without gap under non-DRX with NCD-SSB	1941

A.4.6.1.9.1	Test purpose and Environment	1941

A.4.6.1.9.2	Test parameters	1942

A.4.6.1.9.3	Test Requirements	1943

A.4.6.1.10	EN-DC event triggered reporting tests without gap under non-DRX when CD-SSB is outside active BWP	1944

A.4.6.110.1	Test purpose and Environment	1944

A.4.6.1.10.2	Test Requirements	1944

A.4.6.2	Inter-frequency Measurements	1944

A.4.6.2.1	EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is not used	1944

A.4.6.2.1.1	Test Purpose and Environment	1944

A.4.6.2.1.2	Test Requirements	1947

A.4.6.2.2	EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used	1947

A.4.6.2.2.1	Test Purpose and Environment	1947

A.4.6.2.2.2	Test Requirements	1949

A.4.6.2.3	Void	1950

A.4.6.2.4	Void	1950

A.4.6.2.5	EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is not used	1950

A.4.6.2.5.1	Test Purpose and Environment	1950

A.4.6.2.5.2	Test Requirements	1952

A.4.6.2.6	EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is used	1952

A.4.6.2.6.1	Test Purpose and Environment	1952

A.4.6.2.6.2	Test Requirements	1955

A.4.6.2.7	Void	1955

A.4.6.2.8	Void	1955

A.4.6.2.9	EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used for UE configured with highSpeedMeasInterFreq-r17	1955

A.4.6.2.9.1	Test Purpose and Environment	1955

A.4.6.2.9.2	Test Requirements	1958

A.4.6.3	Void	1958

A.4.6.4	L1-RSRP measurement for beam reporting	1958

A.4.6.4.1	SSB based L1-RSRP measurement when DRX is not used	1958

A.4.6.4.1.1	Test Purpose and Environment	1958

A.4.6.4.1.2	Test parameters	1959

A.4.6.4.1.3	Test Requirements	1960

A.4.6.4.2	SSB based L1-RSRP measurement when DRX is used	1960

A.4.6.4.2.1	Test Purpose and Environment	1960

A.4.6.4.2.2	Test parameters	1961

A.4.6.4.2.3	Test Requirements	1962

A.4.6.4.3	CSI-RS based L1-RSRP measurement when DRX is not used	1962

A.4.6.4.3.1	Test Purpose and Environment	1962

A.4.6.4.3.2	Test parameters	1963

A.4.6.4.3.3	Test Requirements	1964

A.4.6.4.4	CSI-RS based L1-RSRP measurement when DRX is used	1964

A.4.6.4.4.1	Test Purpose and Environment	1964

A.4.6.4.4.2	Test parameters	1965

A.4.6.4.4.3	Test Requirements	1966

A.4.6.4.5	SSB based L1-RSRP measurement when DRX is used for UE configured with *highSpeedMeasFlag-r16* 1966

A.4.6.4.5.1	Test Purpose and Environment	1966

A.4.6.4.5.2	Test parameters	1967

A.4.6.4.5.3	Test Requirements	1968

A.4.6.4.6	CSI-RS based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP	1968

A.4.6.4.6.1	Test Purpose and Environment	1968

A.4.6.4.7	SSB based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP	1969

A.4.6.4.7.1	Test Purpose and Environment	1969

A.4.6.4.7.2	Test Requirements	1969

A.4.6.4.8	SSB based L1-RSRP measurement for UE supporting NCD-SSB based L1 measurement outside active BWP when DRX is not used	1969

A.4.6.4.8.1	Test Purpose and Environment	1969

A.4.6.4.8.2	Test parameters	1969

A.4.6.4.8.3	Test Requirements	1971

A.4.6.5	CLI measurements	1971

A.4.6.5.1	SRS-RSRP measurement with non-DRX	1971

A.4.6.5.1.1	Test Purpose and Environment	1971

A.4.6.5.1.2	Test Parameters	1971

A.4.6.5.1.3	Test Requirements	1974

A.4.6.5.2	CLI-RSSI measurement with non-DRX	1974

A.4.6.5.2.1	Test Purpose and Environment	1974

A.4.6.5.2.2	Test Parameters	1974

A.4.6.5.2.3	Test Requirements	1975

A.4.6.6.1.2	Test Requirements	1979

A.4.6.7	L1-SINR measurement for beam reporting	1979

A.4.6.7.2	L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is used	1981

A.4.6.7.2.1	Test Purpose and Environment	1981

A.4.6.7.2.2	Test parameters	1982

A.4.6.7.2.3	Test Requirements	1983

A.4.6.7.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is used	1983

A.4.6.7.3.1	Test Purpose and Environment	1984

A.4.6.7.3.2	Test parameters	1984

A.4.6.7.3.3	Test Requirements	1985

A.4.6.8	CSI-RS based intra-frequency Measurement	1986

A.4.6.8.1	EN-DC event triggered reporting tests without gap under DRX	1986

A.4.6.8.1.1	Test purpose and Environment	1986

A.4.6.8.1.2	Test Requirements	1988

A.4.6.9	CSI-RS based inter-frequency Measurement	1988

A.4.6.9.1	EN-DC event triggered reporting tests for FR1 cell when non-DRX is used	1988

A.4.6.9.1.1	Test Purpose and Environment	1988

A.4.6.9.1.2	Test Requirements	1990

A.4.7	Measurement Performance requirements	1992

A.4.7.1	SS-RSRP	1992

A.4.7.1.1	EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1992

A.4.7.1.1.1	Test Purpose and Environment	1992

A.4.7.1.1.2	Test parameters	1992

A.4.7.1.1.3	Test Requirements	1996

A.4.7.1.2	EN-DC inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	1997

A.4.7.1.2.1	Test Purpose and Environment	1997

A.4.7.1.2.2	Test parameters	1997

A.4.7.1.2.3	Test Requirements	1999

A.4.7.1.3	Void	1999

A.4.7.2	SS-RSRQ	2000

A.4.7.2.1	EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2000

A.4.7.2.1.1	Test Purpose and Environment	2000

A.4.7.2.1.2	Test Parameters	2000

A.4.7.2.1.3	Test Requirements	2003

A.4.7.2.2	EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2003

A.4.7.2.2.1	Test Purpose and Environment	2003

A.4.7.2.2.2	Test Parameters	2003

A.4.7.2.2.3	Test Requirements	2007

A.4.7.3	SS-SINR	2007

A.4.7.3.1	EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2007

A.4.7.3.1.1	Test Purpose and Environment	2007

A.4.7.3.1.2	Test Parameters	2007

A.4.7.3.1.3	Test Requirements	2010

A.4.7.3.2	EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2010

A.4.7.3.2.1	Test Purpose and Environment	2010

A.4.7.3.2.2	Test Parameters	2010

A.4.7.3.2.3	Test Requirements	2013

A.4.7.4	L1-RSRP measurement for beam reporting	2013

A.4.7.4.1	SSB based L1-RSRP measurement	2013

A.4.7.4.1.1	Test Purpose and Environment	2013

A.4.7.4.1.2	Test parameters	2014

A.4.7.4.1.3	Test Requirements	2016

A.4.7.4.2	CSI-RS based L1-RSRP measurement on resource set with repetition off	2016

A.4.7.4.2.1	Test Purpose and Environment	2016

A.4.7.4.2.2	Test parameters	2017

A.4.7.4.2.3	Test Requirements	2019

A.4.7.5	SFTD accuracy	2020

A.4.7.5.1	SFTD accuracy	2020

A.4.7.5.1.1	Test Purpose and Environment	2020

A.4.7.5.1.2	Test Parameters	2020

A.4.7.5.1.3	Test Requirements	2022

A.4.7.5.2	Void	2022

A.4.7.5.3	Void	2023

A.4.7.6	CLI measurements	2023

A.4.7.6.1	EN-DC SRS-RSRP measurement accuracy with FR1 serving cell	2023

A.4.7.6.1.1	Test Purpose and Environment	2023

A.4.7.6.1.2	Test parameters	2023

A.4.7.6.1.3	Test Requirements	2026

A.4.7.6.2	EN-DC CLI-RSSI measurement accuracy with FR1 serving cell	2026

A.4.7.6.2.1	Test Purpose and Environment	2026

A.4.7.6.2.2	Test parameters	2026

A.4.7.6.2.3	Test Requirements	2028

A.4.7.7	L1-SINR measurement for beam reporting	2028

A.4.7.7.2	L1-SINR measurement with SSB based CMR and dedicated IMR	2031

A.4.7.7.2.1	Test Purpose and Environment	2031

A.4.7.7.2.2	Test parameters	2032

A.4.7.7.2.3	Test Requirements	2034

A.4.7.7.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR	2034

A.4.7.7.3.1	Test Purpose and Environment	2034

A.4.7.7.3.2	Test parameters	2035

A.4.7.7.3.3	Test Requirements	2037

A.4.7.8	CSI-RSRP	2038

A.4.7.8.1	EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2038

A.4.7.8.1.1	Test Purpose and Environment	2038

A.4.7.8.1.2	Test parameters	2038

A.4.7.8.1.3	Test Requirements	2042

A.4.7.8.2	EN-DC inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2042

A.4.7.8.2.1	Test Purpose and Environment	2042

A.4.7.8.2.2	Test parameters	2042

A.4.7.8.2.3	Test Requirements	2045

A.4.7.9	CSI-RSRQ	2045

A.4.7.9.1	EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2045

A.4.7.9.1.1	Test Purpose and Environment	2045

A.4.7.9.1.2	Test Parameters	2045

A.4.7.9.1.3	Test Requirements	2049

A.4.7.9.2	EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2049

A.4.7.9.2.1	Test Purpose and Environment	2049

A.4.7.9.2.2	Test Parameters	2049

A.4.7.9.2.3	Test Requirements	2052

A.4.7.10	CSI-SINR	2052

A.4.7.10.1	EN-DC Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2052

A.4.7.10.1.1	Test Purpose and Environment	2053

A.4.7.10.1.2	Test Parameters	2053

A.4.7.10.1.3	Test Requirements	2056

A.4.7.10.2	EN-DC Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	2056

A.4.7.10.2.1	Test Purpose and Environment	2056

A.4.7.10.2.2	Test Parameters	2056

A.4.7.10.2.3	Test Requirements	2059

A.4.7.11	TDCP amplitude measurement accuracy	2059

A.4.7.11.1	TDCP amplitude measurement accuracy in EN-DC	2059

A.4.7.11.1.1	Test Purpose and Environment	2059

A.4.7.11.1.2	Test parameters	2059

A.4.7.11.1.3	Test Requirements	2061

A.4.8	Void	2061

A.4A	NE-DC test with all NR cells in FR1	2061

A.4A.1	Signaling characteristics	2061

A.4A.1.1	E-UTRAN PSCell addition	2061

A.4A.1.1.1	Test purpose and environment	2061

A.4A.1.1.2	Test Requirements	2064

A.4A.1.2	Active BWP switch	2065

A.4A.1.2.1	E-UTRAN PSCell – NR PCell FR1 DCI-based and Timer-based DL active BWP switch in non-DRX in synchronous NE-DC	2065

A.4A.1.2.1.1	Test Purpose and Environment	2065

A.4A.1.2.1.2	Test Requirements	2068

A.4A.1.3	Intra-frequency handover with E-UTRAN PSCell	2068

A.4A.1.3.1	Test purpose and environment	2068

A.4A.1.3.2	Test Requirements	2072

A.4A.1.4	Handover with PSCell from NE-DC to NE-DC with unknown target PSCell	2072

A.4A.1.4.1	Test Purpose and Environment	2072

A.4A.1.4.2	Test Parameters	2072

A.4A.1.4.3	Test Requirements	2076

A.4A.1.4.3.1	Test Requirements for NR HO	2076

A.4A.1.4.3.2	Test Requirements for LTE PSCell Change	2077

A.4A.2	Measurement performance	2077

A.4A.2.1	SFTD accuracy	2077

A.4A.2.1.1	SFTD accuracy	2077

A.4A.2.1.1.1	Test Purpose	2077

A.4A.2.1.1.2	Test Environment	2077

A.4A.2.1.1.3	Test Requirements	2080

A.5	EN-DC tests with one or more NR cells in FR2	2080

A.5.1	Void	2080

A.5.2	Void	2081

A.5.3	RRC\_CONNECTED state mobility	2081

A.5.3.1	Void	2081

A.5.3.2	RRC Connection Mobility Control	2081

A.5.3.2.1	Void	2081

A.5.3.2.2	Random Access	2081

A.5.3.2.2.1	4-step RA type c ontention based random access test in FR2 for PSCell/SCell in EN-DC	2081

A.5.3.2.2.2	4-step RA type non-contention based random access test in FR2 for PSCell/SCell in EN-DC	2084

A.5.3.2.2.3	2-step RA type contention based random access test in FR2 for PSCell/SCell in EN-DC	2087

A.5.3.2.2.4	2-step RA type non-contention based random access test in FR2 for PSCell/SCell in EN-DC	2090

A.5.3.2.3	Void	2092

A.5.3.3	Handover with PSCell with known FR2 target PSCell	2092

A.5.3.3.1	Test purpose and environment	2092

A.5.3.3.2	Test Requirements	2095

A.5.3.3.3	Void	2095

A.5.3.3.4	Void	2095

A.5.3.3.5	Void	2095

A.5.3.3.6	Void	2096

A.5.4	Timing	2096

A.5.4.1	UE transmit timing	2096

A.5.4.1.1	NR UE Transmit Timing Test for FR2	2096

A.5.4.1.1.1	Test Purpose and environment	2096

A.5.4.1.1.2	Test requirements	2098

A.5.4.1.2	NR UE Transmit Timing Test with 2-TA for FR2 UE supporting *multiDCI-IntraCellMultiTRP-TwoTA-r18* 2098

A.5.4.1.2.1	Test Purpose and environment	2098

A.5.4.1.2.2	Test requirements	2103

A.5.4.2	UE timer accuracy	2103

A.5.4.3	Timing advance	2103

A.5.4.3.1 EN-DC FR2 timing advance adjustment accuracy	2103

A.5.4.3.1.1 Test Purpose and Environment	2103

A.5.4.3.1.2 Test Parameters	2103

A.5.4.3.1.3	Test Requirements	2106

A.5.5	Signaling characteristics	2106

A.5.5.1	Radio link Monitoring	2106

A.5.5.1.1	Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode	2106

A.5.5.1.1.1	Test Purpose and Environment	2106

A.5.5.1.1.2	Test Requirements	2109

A.5.5.1.2	Radio Link Monitoring In-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode	2109

A.5.5.1.2.1	Test Purpose and Environment	2109

A.5.5.1.2.2	Test Requirements	2112

A.5.5.1.3	Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in DRX mode	2113

A.5.5.1.3.1	Test Purpose and Environment	2113

A.5.5.1.3.2	Test Requirements	2115

A.5.5.1.4	Radio Link Monitoring In-sync Test for FR2 PSCell configured with SSB-based RLM RS in DRX mode	2115

A.5.5.1.4.1	Test Purpose and Environment	2115

A.5.5.1.4.2	Test Requirements	2118

A.5.5.1.5	EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with CSI-RS-based RLM in non-DRX mode	2118

A.5.5.1.6	EN-DC Radio Link Monitoring In-sync Test for FR2 PSCell configured with CSI-RS-based RLM in non-DRX mode	2121

A.5.5.1.7	EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with CSI-RS-based RLM in DRX mode	2124

A.5.5.1.8	EN-DC Radio Link Monitoring In-sync Test for FR2 PSCell configured with CSI-RS-based RLM in DRX mode	2127

A.5.5.1.8.2	Test Requirements	2131

A.5.5.1.9	EN-DC Radio Link Monitoring UE Scheduling Restrictions on FR2	2131

A.5.5.1.9.1	Test Purpose and Environment	2131

A.5.5.1.9.2	Test Requirements	2132

A.5.5.1.10	Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS for UE fulfilling relaxed measurement criterion	2133

A.5.5.1.10.1	Test Purpose and Environment	2133

A.5.5.1.10.2	Test Requirements	2135

A.5.5.1.11	Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode for UE supporting fast beam sweeping in multi-Rx	2135

A.5.5.1.11.1	Test Purpose and Environment	2135

A.5.5.1.11.2	Test Requirements	2138

A.5.5.1.12	EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with CSI-RS-based RLM in non-DRX mode when CD-SSB is outside active BWP	2139

A.5.5.1.12.1	Test Purpose and Environment	2139

A.5.5.1.13	Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode when CD-SSB is outside active BWP	2139

A.5.5.1.13.1	Test Purpose and Environment	2139

A.5.5.1.13.2	Test Requirements	2139

A.5.5.1.14	EN-DC Radio Link Monitoring Out-of-sync Test for FR2 PSCell configured with SSB-based RLM RS in non-DRX mode for UE supporting NCD-SSB based measurement outside active BWP	2139

A.5.5.1.14.1	Test Purpose and Environment	2139

A.5.5.1.14.2	Test Requirements	2142

A.5.5.2	Interruption	2143

A.5.5.2.1	E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in synchronous EN-DC	2143

A.5.5.2.1.1	Test Purpose and Environment	2143

A.5.5.2.1.2	Test Requirements	2145

A.5.5.2.2	E-UTRAN – NR FR2 interruptions at transitions between active and non-active during DRX in asynchronous EN-DC	2145

A.5.5.2.2.1	Test Purpose and Environment	2145

A.5.5.2.2.2	Test Requirements	2147

A.5.5.2.3	E-UTRAN – NR FR2 interruptions during measurements on deactivated NR SCC in synchronous EN-DC	2147

A.5.5.2.3.1	Test Purpose and Environment	2147

A.5.5.2.3.2	Test Requirements	2149

A.5.5.2.4	E-UTRAN – NR FR2 interruptions during measurements on deactivated NR SCC in asynchronous EN-DC	2150

A.5.5.2.4.1	Test Purpose and Environment	2150

A.5.5.2.4.2	Test Requirements	2152

A.5.5.2.5	E-UTRAN – NR FR2 interruptions during measurements on deactivated E-UTRAN SCC in synchronous EN-DC	2153

A.5.5.2.5.1	Test Purpose and Environment	2153

A.5.5.2.5.2	Test Requirements	2155

A.5.5.2.6	E-UTRAN – NR FR2 interruptions during measurements on deactivated E-UTRAN SCC in asynchronous EN-DC	2155

A.5.5.2.6.1	Test Purpose and Environment	2155

A.5.5.2.6.2	Test Requirements	2157

A.5.5.2.7	E-UTRAN – NR FR2 interruptions at E-UTRA SRS carrier based switching	2158

A.5.5.2.7.1	Test Purpose and Environment	2158

A.5.5.2.7.2	Test Requirements	2160

A.5.5.2.8 E-UTRAN – NR FR2 interruptions at NR SRS carrier based switching	2160

A.5.5.2.8.1 Test Purpose and Environment	2160

A.5.5.2.8.3	Test Requirements	2162

A.5.5.2.9	E-UTRAN – NR FR2 interruptions during measurements on deactivated NR PSCell	2162

A.5.5.2.9.1	Test Purpose and Environment	2162

A.5.5.2.9.2	Test Requirements	2165

A.5.5.3	SCell Activation and Deactivation Delay	2165

A.5.5.3.1	SCell Activation and deactivation of SCell in FR2 intra-band	2165

A.5.5.3.1.1	Test Purpose and Environment	2165

A.5.5.3.1.2	Test Requirements	2166

A.5.5.3.2	SCell Activation and deactivation of known SCell in FR1 for 160 ms SCell measurement cycle	2167

A.5.5.3.2.1	Test Purpose and Environment	2167

A.5.5.3.2.2	Test Requirements	2169

A.5.5.3.3	Void	2169

A.5.5.3.4	Void	2169

A.5.5.3.5	SCell Activation and deactivation of SCell in FR2	2169

A.5.5.3.5.1	Test Purpose and Environment	2169

A.5.5.3.5.2	Test Requirements	2172

A.5.5.3.6	Multiple SCell Activation and deactivation of one unknown SCell and one known SCell in FR2	2172

A.5.5.3.6.1	Test Purpose and Environment	2172

A.5.5.3.6.2	Test Requirements	2175

A.5.5.3.7	Direct SCell activation at SCell addition of known SCell in FR2	2175

A.5.5.3.7.1	Test Purpose and Environment	2175

A.5.5.3.7.2	Test Requirements	2178

A.5.5.3.8	Fast SCell Activation of SCell in FR2 intra-band	2178

A.5.5.3.8.1	Test Purpose and Environment	2178

A.5.5.3.8.2	Test Requirements	2181

A.5.5.3.9	PUCCH SCell Activation and deactivation of known SCell in FR2	2181

A.5.5.3.9.1	Test Purpose and Environment	2181

A.5.5.3.9.2	Test Requirements	2184

A.5.5.3.10	PUCCH SCell Activation and deactivation of unknown SCell in FR2	2184

A.5.5.3.10.1	Test Purpose and Environment	2184

A.5.5.3.10.2	Test Requirements	2187

A.5.5.3.11	Multiple SCell activation and deactivation of one known PUCCH SCell and one unknown SCell in FR2	2187

A.5.5.3.11.1	Test Purpose and Environment	2187

A.5.5.3.11.2	Test Requirements	2190

A.5.5.3.12	SCell Activation and deactivation of unknown PUCCH SCell and unknown DL SCell in FR2 in non-DRX	2191

A.5.5.3.12.1	Test Purpose and Environment	2191

A.5.5.3.12.2	Test Requirements	2193

A.5.5.3.13	SCell Activation and deactivation of unknown SCell in FR2 for UE in DRX, capable of small beam sweeping factors and/or short measurement interval	2194

A.5.5.3.13.1	Test Purpose and Environment	2194

A.5.5.3.13.2	Test Requirements	2197

A.5.5.3.14	PUCCH SCell activation and deactivation with FR1 PSCell based on L3 reporting after SCell activation command	2199

A.5.5.3.14.1	Test Purpose and Environment	2199

A.5.5.3.14.2	Test Requirements	2203

A.5.5.3.15	SCell Activation of unknown SCell in FR2 in non-DRX for 160 ms SCell measurement cycle with the L3 reporting during activation	2203

A.5.5.3.15.1	Test Purpose and Environment	2203

A.5.5.3.15.2	Test Requirements	2207

A.5.5.4	Void	2208

A.5.5.5	Beam Failure Detection and Link recovery procedures	2208

A.5.5.5.1	EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with SSB-based BFD and LR in non-DRX mode	2208

A.5.5.5.1.1	Test Purpose and Environment	2208

A.5.5.5.1.2	Test Requirements	2211

A.5.5.5.2	EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with SSB-based BFD and LR in DRX mode	2211

A.5.5.5.2.1	Test Purpose and Environment	2211

A.5.5.5.2.2	Test Requirements	2215

A.5.5.5.3	EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with CSI-RS-based BFD and LR in non-DRX mode	2215

A.5.5.5.3.1	Test Purpose and Environment	2215

A.5.5.5.3.2	Test Requirements	2218

A.5.5.5.4	EN-DC Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with CSI-RS-based BFD and LR in DRX mode	2219

A.5.5.5.4.1	Test Purpose and Environment	2219

A.5.5.5.4.2	Test Requirements	2222

A.5.5.5.5	EN-DC scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2 PSCell configured with SSB-based BFD and LR in non-DRX mode	2222

A.5.5.5.5.1	Test Purpose and Environment	2222

A.5.5.5.5.2	Test Requirements	2225

A.5.5.5.6	EN-DC Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in non-DRX mode	2225

A.5.5.5.6.1	Test Purpose and Environment	2225

A.5.5.5.6.2	Test Requirements	2229

A.5.5.5.7	EN-DC Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in DRX mode	2229

A.5.5.5.7.1	Test Purpose and Environment	2229

A.5.5.5.7.2	Test Requirements	2232

A.5.5.5.8	EN-DC TRP specific Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with CSI-RS-based BFD and LR in DRX mode	2233

A.5.5.5.8.1	Test Purpose and Environment	2233

A.5.5.5.8.2	Test Requirements	2236

A.5.5.5.9	Beam Failure Detection and Link Recovery Test for FR2 PSCell configured with SSB-based BFD and LR in DRX mode for UE fulfilling relaxed measurement criterion	2236

A.5.5.5.9.1	Test Purpose and Environment	2236

A.5.5.5.9.2	Test Requirements	2239

A.5.5.6	Active BWP switch	2240

A.5.5.6.1	DCI-based and Timer-based Active BWP Switch	2240

A.5.5.6.1.1	E-UTRAN – NR PSCell FR2 DL active BWP switch with non-DRX in synchronous EN-DC	2240

A.5.5.6.1.1.1	Test Purpose and Environment	2240

A.5.5.6.1.1.2	Test Requirements	2242

A.5.5.6.1.2	E-UTRAN – NR PSCell FR2 with FR2 SCell DL active BWP switch in non-DRX in synchronous EN-DC	2243

A.5.5.6.2	RRC-based Active BWP Switch	2246

A.5.5.6.2.1	E-UTRAN – NR PSCell FR2 DL active BWP switch with non-DRX in synchronous EN-DC	2246

A.5.5.6.3 Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs	2249

A.5.5.6.3.1	E-UTRAN – NR PSCell FR2 and NR SCell FR2 DL active BWP switch on multiple CCs in synchronous EN-DC	2249

A.5.5.6.4	SCell dormancy switch	2252

A.5.5.6.4.1	E-UTRAN – NR FR2 PSCell SCell dormancy switch of single FR2 SCell inside active time	2252

A.5.5.6.4.1.1	Test Purpose and Environment	2252

A.5.5.6.4.1.2	Test Requirements	2255

A.5.5.6.4.2	E-UTRAN – NR FR1 PSCell SCell dormancy switch of two FR2 SCells outside active time	2256

A.5.5.6.4.2.1	Test Purpose and Environment	2256

A.5.5.6.4.2.2	Test Requirements	2260

A.5.5.6.5	Simultaneous RRC-based Active BWP Switch on multiple CCs	2260

A.5.5.6.5.1	E-UTRAN – NR PSCell FR2  and NR SCell FR2 DL active BWP switch on multiple CCs with non-DRX in synchronous EN-DC	2260

A.5.5.7	PSCell addition and release delay	2263

A.5.5.7.1	Addition and Release Delay of NR PSCell	2263

A.5.5.7.1.1	Test purpose and environment	2263

A.5.5.7.1.2	Test Requirements	2265

A.5.5.8	Active TCI state switch delay	2265

A.5.5.8.1	MAC-CE based active TCI state switch	2266

A.5.5.8.1.1	E-UTRAN – NR PSCell FR2 active TCI state switch for a known TCI state	2266

A.5.5.8.1.1.1	Test Purpose and Environment	2266

A.5.5.8.1.1.2	Test Requirements	2268

A.5.5.8.2	RRC based active TCI state switch	2269

A.5.5.8.2.1	E-UTRAN – NR PSCell FR2 active TCI state switch for a known TCI state	2269

A.5.5.8.2.1.1	Test Purpose and Environment	2269

A.5.5.8.2.1.2	Test Requirements	2272

A.5.5.9	Uplink spatial relation switch delay	2272

A.5.5.9.1	MAC-CE based uplink spatial relation switch	2272

A.5.5.9.1.1	E-UTRAN – NR PSCell FR2 uplink spatial relation switch for a known spatial relation	2272

A.5.5.9.1.1.1	Test Purpose and Environment	2272

A.5.5.9.1.1.2	Test Requirements	2274

A.5.5.9.2	RRC based spatial relation switch	2274

A.5.5.9.2.1	E-UTRAN – NR PSCell FR2 spatial relation switch associated with a known DL-RS	2274

A.5.5.9.2.1.1	Test Purpose and Environment	2275

A.5.5.9.2.1.2	Test Requirements	2276

A.5.5.10	UE specific CBW change	2277

A.5.5.10.1	UE specific CBW change on FR2 NR PSCell	2277

A.5.5.10.1.1	Test Purpose and Environment	2277

A.5.5.10.1.2	Test Requirements	2279

A.5.5.11	Unified TCI state switch delay	2280

A.5.5.11.1	MAC-CE based active joint TCI state switch	2280

A.5.5.11.1.1	E-UTRAN – NR PSCell FR2 active joint TCI state switch for a known TCI state	2280

A.5.5.11.1.1.1	Test Purpose and Environment	2280

A.5.5.11.1.1.2	Test parameters	2280

A.5.5.11.1.1.3	Test Requirements	2282

A.5.5.11.2	MAC-CE based active uplink TCI state switch	2282

A.5.5.11.2.1	E-UTRAN – NR PSCell FR2 active uplink TCI state switch for a known TCI state	2282

A.5.5.11.2.1.1	Test Purpose and Environment	2282

A.5.5.11.2.1.2	Test parameters	2283

A.5.5.11.2.1.3	Test Requirements	2284

A.5.5.11.3	MAC-CE based active downlink TCI state switch	2285

A.5.5.11.3.1	E-UTRAN – NR PSCell FR2 downlink TCI state switch to cell with additional PCI for a known TCI state	2285

A.5.5.11.3.1.1	Test Purpose and Environment	2285

A.5.5.11.3.1.2	Test Parameters	2285

A.5.5.11.3.1.3	Test Requirements	2288

A.5.5.12	PSCell activation and deactivation delay	2288

A.5.5.12.1	PSCell activation and deactivation delay	2288

A.5.5.12.1.1	Test purpose and environment	2288

A.5.5.12.1.2	Test Requirements	2290

A.5.5.13	Conditional PSCell addition and release delay	2291

A.5.5.13.1	Addition and Release Delay of NR PSCell	2291

A.5.5.13.1.1	Test purpose and environment	2291

A.5.5.13.1.2	Test Requirements	2293

A.5.6	Measurement procedure	2293

A.5.6.1	Intra-frequency Measurements	2293

A.5.6.1.1	EN-DC event triggered reporting test without gap under non-DRX	2293

A.5.6.1.1.1	Test purpose and Environment	2293

A.5.6.1.1.2	Test Requirements	2296

A.5.6.1.2	EN-DC event triggered reporting test without gap under DRX	2296

A.5.6.1.2.1	Test purpose and Environment	2296

A.5.6.1.2.2	Test Requirements	2298

A.5.6.1.3	EN-DC event triggered reporting test with per-UE gaps under non-DRX	2299

A.5.6.1.3.1	Test purpose and Environment	2299

A.5.6.1.3.2	Test Requirements	2301

A.5.6.1.4	EN-DC event triggered reporting test with per-UE gaps under DRX	2301

A.5.6.1.4.1	Test purpose and Environment	2301

A.5.6.1.4.2	Test Requirements	2304

A.5.6.1.5	EN-DC event triggered reporting test without gap under non-DRX when CD-SSB is outside active BWP	2304

A.5.6.1.5.1	Test purpose and Environment	2304

A.5.6.1.5.2	Test Requirements	2304

A.5.6.1.6	EN-DC event triggered reporting test without gap under non-DRX	2304

A.5.6.1.6.1	Test purpose and Environment	2304

A.5.6.1.6.2	Test Requirements	2307

A.5.6.2	Inter-frequency Measurements	2307

A.5.6.2.1 	EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is not used	2307

A.5.6.2.1.1	Test Purpose and Environment	2307

A.5.6.2.1.2	Test Requirements	2310

A.5.6.2.2 	EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is used	2310

A.5.6.2.2.1	Test Purpose and Environment	2310

A.5.6.2.2.2	Test Requirements	2312

A.5.6.2.3 	EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is not used	2313

A.5.6.2.3.1	Test Purpose and Environment	2313

A.5.6.2.3.2	Test Requirements	2315

A.5.6.2.4	EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is used	2315

A.5.6.2.4.1	Test Purpose and Environment	2315

A.5.6.2.4.2	Test Requirements	2318

A.5.6.2.5	EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is not used	2318

A.5.6.2.5.1	Test Purpose and Environment	2318

A.5.6.2.5.2	Test Requirements	2321

A.5.6.2.6	EN-DC event triggered reporting tests for FR2 cell without SSB time index detection when DRX is used	2321

A.5.6.2.6.1	Test Purpose and Environment	2321

A.5.6.2.6.2	Test Requirements	2324

A.5.6.2.7	EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is not used	2325

A.5.6.2.7.1	Test Purpose and Environment	2325

A.5.6.2.7.2	Test Requirements	2327

A.5.6.2.8	EN-DC event triggered reporting tests for FR2 cell with SSB time index detection when DRX is used	2328

A.5.6.2.8.1	Test Purpose and Environment	2328

A.5.6.2.8.2	Test Requirements	2331

A.5.6.3	L1-RSRP measurement for beam reporting	2331

A.5.6.3.1	SSB based L1-RSRP measurement when DRX is not used	2331

A.5.6.3.1.1	Test Purpose and Environment	2331

A.5.6.3.1.2	Test parameters	2332

A.5.6.3.1.3	Test Requirements	2333

A.5.6.3.2	SSB based L1-RSRP measurement when DRX is used	2333

A.5.6.3.2.1	Test Purpose and Environment	2333

A.5.6.3.2.2	Test parameters	2334

A.5.6.3.2.3	Test Requirements	2335

A.5.6.3.3	CSI-RS based L1-RSRP measurement when DRX is not used	2335

A.5.6.3.3.1	Test Purpose and Environment	2335

A.5.6.3.3.2	Test parameters	2335

A.5.6.3.3.3	Test Requirements	2337

A.5.6.3.4	CSI-RS based L1-RSRP measurement when DRX is used	2337

A.5.6.3.4.1	Test Purpose and Environment	2337

A.5.6.3.4.2	Test parameters	2338

A.5.6.3.4.3	Test Requirements	2339

A.5.6.3.5	CSI-RS based L1-RSRP measurement when DRX is not used and when CD-SSB is outside active BWP	2339

A.5.6.3.5.1	Test Purpose and Environment	2339

A.5.6.3.6	SSB based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP	2340

A.5.6.3.6.1	Test Purpose and Environment	2340

A.5.6.3.6.2	Test Requirements	2340

A.5.6.3.7	SSB based L1-RSRP measurement for UE supporting NCD-SSB based L1 measurement outside active BWP when DRX is not used	2340

A.5.6.3.7.1	Test Purpose and Environment	2340

A.5.6.3.7.2	Test parameters	2340

A.5.6.3.7.3	Test Requirements	2342

A.5.6.4	CLI measurements	2342

A.5.6.4.1	SRS-RSRP measurement with DRX	2342

A.5.6.4.1.1	Test Purpose and Environment	2342

A.5.6.4.1.2	Test Parameters	2342

A.5.6.4.1.3	Test Requirements	2344

A.5.6.4.2	CLI-RSSI measurement with DRX	2345

A.5.6.4.2.1	Test Purpose and Environment	2345

A.5.6.4.2.2	Test Parameters	2345

A.5.6.4.2.3	Test Requirements	2346

A.5.6.5	Measurements with autonomous gaps	2346

A.5.6.5.1 	EN-DC inter-frequency CGI identification of NR neighbor cell in FR2	2346

A.5.6.5.1.1	Test Purpose and Environment	2346

A.5.6.5.1.2	Test Requirements	2349

A.5.6.6	L1-SINR measurement for beam reporting	2349

A.5.6.6.2	L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is not used	2351

A.5.6.6.2.1	Test Purpose and Environment	2351

A.5.6.6.2.2	Test parameters	2351

A.5.6.6.2.3	Test Requirements	2353

A.5.6.6.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is not used	2353

A.5.6.6.3.1	Test Purpose and Environment	2353

A.5.6.6.3.2	Test parameters	2354

A.5.6.6.3.3	Test Requirements	2355

A.5.6.7	CSI-RS based Intra-frequency Measurements	2355

A.5.6.7.1	EN-DC event triggered reporting test without gap under non-DRX	2355

A.5.6.7.1.1	Test purpose and Environment	2355

A.5.6.7.1.2	Test Requirements	2357

A.5.6.8	CSI-RS based Inter-frequency Measurements	2357

A.5.6.8.1 	EN-DC event triggered reporting tests for NR FR2 cell when DRX is used	2357

A.5.6.8.1.1	Test Purpose and Environment	2357

A.5.6.8.1.2	Test Requirements	2359

A.5.7	Measurement Performance requirements	2360

A.5.7.1	SS-RSRP	2360

A.5.7.1.1	EN-DC intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	2360

A.5.7.1.1.1	Test Purpose and Environment	2360

A.5.7.1.1.2	Test parameters	2360

A.5.7.1.1.3	Test Requirements	2362

A.5.7.1.2	EN-DC inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	2362

A.5.7.1.2.1	Test Purpose and Environment	2362

A.5.7.1.2.2	Test parameters	2363

A.5.7.1.2.3	Test Requirements	2365

A.5.7.1.3	EN-DC inter-frequency measurement accuracy with FR1 serving cell and FR2 target cell	2366

A.5.7.1.3.1	Test Purpose and Environment	2366

A.5.7.1.3.2	Test parameters	2366

A.5.7.1.3.3	Test Requirements	2368

A.5.7.2	SS-RSRQ	2368

A.5.7.2.1	EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	2368

A.5.7.2.1.1	Test Purpose and Environment	2368

A.5.7.2.1.2	Test Parameters	2369

A.5.7.2.1.3	Test Requirements	2370

A.5.7.2.2	EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	2370

A.5.7.2.2.1	Test Purpose and Environment	2370

A.5.7.2.2.2	Test Parameters	2370

A.5.7.2.2.3	Test Requirements	2372

A.5.7.3	SS-SINR	2372

A.5.7.3.1	EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	2372

A.5.7.3.1.1	Test Purpose and Environment	2372

A.5.7.3.1.2	Test Parameters	2372

A.5.7.3.1.3	Test Requirements	2374

A.5.7.3.2	EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	2374

A.5.7.3.2.1	Test Purpose and Environment	2374

A.5.7.3.2.2	Test Parameters	2374

A.5.7.3.2.3	Test Requirements	2375

A.5.7.4	L1-RSRP measurement for beam reporting	2375

A.5.7.4.1	SSB based L1-RSRP measurement	2376

A.5.7.4.1.1	Test Purpose and Environment	2376

A.5.7.4.1.2	Test parameters	2376

A.5.7.4.1.3	Test Requirements	2377

A.5.7.4.2	CSI-RS based L1-RSRP measurement on resource set with repetition off	2378

A.5.7.4.2.1	Test Purpose and Environment	2378

A.5.7.4.2.2	Test parameters	2378

A.5.7.4.2.3	Test Requirements	2379

A.5.7.5	CLI measurements	2380

A.5.7.5.1	EN-DC SRS-RSRP measurement accuracy with FR2 serving cell	2380

A.5.7.5.1.1	Test Purpose and Environment	2380

A.5.7.5.1.2	Test parameters	2380

A.5.7.5.1.3	Test Requirements	2382

A.5.7.5.2	EN-DC CLI-RSSI measurement accuracy with FR2 serving cell	2382

A.5.7.5.2.1	Test Purpose and Environment	2382

A.5.7.5.2.2	Test parameters	2382

A.5.7.5.2.3	Test Requirements	2384

A.5.7.6	L1-SINR measurement for beam reporting	2384

A.5.7.6.2	L1-SINR measurement with SSB based CMR and dedicated IMR	2386

A.5.7.6.2.1	Test Purpose and Environment	2387

A.5.7.6.2.2	Test parameters	2387

A.5.7.6.2.3	Test Requirements	2388

A.5.7.6.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR	2389

A.5.7.6.3.1	Test Purpose and Environment	2389

A.5.7.6.3.2	Test parameters	2389

A.5.7.6.3.3	Test Requirements	2391

A.5.7.7	CSI-RSRP	2391

A.5.7.7.1	EN-DC intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	2391

A.5.7.7.1.1	Test Purpose and Environment	2391

A.5.7.7.1.2	Test parameters	2391

A.5.7.7.1.3	Test Requirements	2393

A.5.7.7.2	EN-DC inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	2394

A.5.7.7.2.1	Test Purpose and Environment	2394

A.5.7.7.2.2	Test parameters	2394

A.5.7.7.2.3	Test Requirements	2396

A.5.7.8	CSI-RSRQ	2397

A.5.7.8.1	EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell	2397

A.5.7.8.1.1	Test Purpose and Environment	2397

A.5.7.8.1.2	Test Parameters	2397

A.5.7.8.1.3	Test Requirements	2399

A.5.7.8.2	EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	2399

A.5.7.8.2.1	Test Purpose and Environment	2399

A.5.7.8.2.2	Test Parameters	2399

A.5.7.8.2.3	Test Requirements	2401

A.5.7.9	CSI-SINR	2401

A.5.7.9.1	EN-DC Intra-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	2401

A.5.7.9.1.1	Test Purpose and Environment	2401

A.5.7.9.1.2	Test Parameters	2401

A.5.7.9.1.3	Test Requirements	2403

A.5.7.9.2	EN-DC Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	2403

A.5.7.9.2.1	Test Purpose and Environment	2403

A.5.7.9.2.2	Test Parameters	2403

A.5.7.9.2.3	Test Requirements	2405

A.5.8	Void	2405

A.6	NR standalone tests with all NR cells in FR1	2407

A.6.1	SA: RRC\_IDLE state mobility	2407

A.6.1.1	Cell re-selection to NR	2407

A.6.1.1.1	Cell reselection to FR1 intra-frequency NR case	2407

A.6.1.1.1.1	Test Purpose and Environment	2407

A.6.1.1.1.2	Test Parameters	2407

A.6.1.1.1.3	Test Requirements	2409

A.6.1.1.2	Cell reselection to FR1 inter-frequency NR case	2409

A.6.1.1.2.1	Test Purpose and Environment	2409

A.6.1.1.2.2	Test Parameters	2410

A.6.1.1.2.3	Test Requirements	2412

A.6.1.1.3	Cell reselection to FR1 intra-frequency NR case for UE fulfilling low mobility relaxed measurement criterion	2412

A.6.1.1.3.1	Test Purpose and Environment	2412

A.6.1.1.3.2	Test Parameters	2412

A.6.1.1.3.3	Test Requirements	2415

A.6.1.1.4	Cell reselection to FR1 intra-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion	2415

A.6.1.1.4.1	Test Purpose and Environment	2415

A.6.1.1.4.2	Test Parameters	2415

A.6.1.1.4.3	Test Requirements	2417

A.6.1.1.5	Cell reselection to FR1 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion	2418

A.6.1.1.5.1	Test Purpose and Environment	2418

A.6.1.1.5.2	Test Parameters	2418

A.6.1.1.5.3	Test Requirements	2420

A.6.1.1.6	Cell reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion	2421

A.6.1.1.6.1	Test Purpose and Environment	2421

A.6.1.1.6.2	Test Parameters	2421

A.6.1.1.6.3	Test Requirements	2423

A.6.1.1.7	Cell reselection to FR1 intra-frequency NR case for UE configured with *highSpeedMeasFlag-r16* 2424

A.6.1.1.7.1	Test Purpose and Environment	2424

A.6.1.1.7.2	Test Parameters	2424

A.6.1.1.7.3	Test Requirements	2427

A.6.1.1.8	Cell reselection to FR1 inter-frequency NR case for UE configured with *highSpeedMeasInterFreq-r17* 2427

A.6.1.1.8.1	Test Purpose and Environment	2427

A.6.1.1.8.2	Test Parameters	2427

A.6.1.1.8.3	Test Requirements	2430

A.6.1.1.9	Cell reselection to FR1 intra-frequency NR case for UE operating on a cell with less than 5 MHz BW	2430

A.6.1.1.9.1	Test Purpose and Environment	2430

A.6.1.1.9.3	Test Requirements	2431

A.6.1.2	Inter-RAT E-UTRAN cell re-selection	2431

A.6.1.2.1	Cell reselection to higher priority E-UTRAN	2431

A.6.1.2.1.1	Test Purpose and Environment	2431

A.6.1.2.1.2	Test Parameters	2432

A.6.1.2.1.3	Test Requirements	2434

A.6.1.2.2	Cell reselection to lower priority E-UTRAN	2434

A.6.1.2.2.1	Test Purpose and Environment	2434

A.6.1.2.2.2	Test Parameters	2434

A.6.1.2.2.3	Test Requirements	2437

A.6.1.2.3	Cell reselection to lower priority E-UTRAN for UE fulfilling low mobility relaxed measurement criterion	2437

A.6.1.2.3.1	Test Purpose and Environment	2437

A.6.1.2.3.2	Test Parameters	2437

A.6.1.2.3.3	Test Requirements	2440

A.6.1.2.4	Cell reselection to lower priority E-UTRAN for UE fulfilling not-at-cell edge relaxed measurement criterion	2440

A.6.1.2.4.1	Test Purpose and Environment	2440

A.6.1.2.4.2	Test Parameters	2441

A.6.1.2.4.3	Test Requirements	2443

A.6.1.2.5	Cell reselection to lower priority E-UTRAN cell for UE configured with highSpeedMeasFlag-r16	2443

A.6.1.2.5.1	Test Purpose and Environment	2444

A.6.1.2.5.2	Test Parameters	2444

A.6.1.2.5.3	Test Requirements	2446

A.6.1.1.7	Void	2446

A.6.2	SA: RRC\_INACTIVE state mobility	2447

A.6.2.1	Configured Grant based Small Data Transmissions (CG-SDT)	2447

A.6.2.1.1	Test purpose and Environment	2447

A.6.2.1.2	Test Parameters	2448

A.6.2.1.3	Test requirements	2449

A.6.2.2	Cell reselection for positioning	2450

A.6.2.2.1	Cell reselection to FR1 intra-frequency NR case with RRC\_ INACTIVE eDRX and positioning SRS	2450

A.6.2.2.1.1	Test Purpose and Environment	2450

A.6.2.2.1.2	Test Parameters	2450

A.6.2.2.1.3	Test Requirements	2454

A.6.3	RRC\_CONNECTED state mobility	2454

A.6.3.1	Handover	2454

A.6.3.1.1	Intra-frequency handover from FR1 to FR1; known target cell	2454

A.6.3.1.1.1	Test Purpose and Environment	2454

A.6.3.1.1.2	Test Parameters	2454

A.6.3.1.1.3 Test Requirements	2456

A.6.3.1.2	Intra-frequency handover from FR1 to FR1; unknown target cell	2456

A.6.3.1.2.1	Test Purpose and Environment	2456

A.6.3.1.2.2	Test Parameters	2456

A.6.3.1.2.3	Test Requirements	2458

A.6.3.1.3	Inter-frequency handover from FR1 to FR1; unknown target cell	2458

A.6.3.1.3.1	Test Purpose and Environment	2458

A.6.3.1.3.2	Test Parameters	2458

A.6.3.1.3.3	Test Requirements	2460

A.6.3.1.4	SA NR - E-UTRAN handover	2460

A.6.3.1.4.1	Test Purpose and Environment	2460

A.6.3.1.4.2	Test Requirements	2463

A.6.3.1.5	SA NR - E-UTRAN handover with unknown target cell	2464

A.6.3.1.5.1	Test Purpose and Environment	2464

A.6.3.1.5.2	Test Requirements	2467

A.6.3.1.6	 SA NR - UTRAN FDD handover	2467

A.6.3.1.6.1	Test Purpose and Environment	2467

A.6.3.1.6.2	Test Requirements	2469

A.6.3.1.7	Intra-frequency synchronous DAPS handover in FR1	2469

A.6.3.1.7.1	Test Purpose and Environment	2469

A.6.3.1.7.2	Test Parameters	2469

A.6.3.1.7.3	Test Requirements	2472

A.6.3.1.8	Intra-frequency asynchronous DAPS handover in FR1	2472

A.6.3.1.8.1	Test Purpose and Environment	2472

A.6.3.1.8.2	Test Parameters	2473

A.6.3.1.8.3	Test Requirements	2475

A.6.3.1.9	Intra-band inter-frequency synchronous DAPS handover test in SA for FR1	2475

A.6.3.1.9.1	Test Purpose and Environment	2475

A.6.3.1.9.2	Test Parameters	2476

A.6.3.1.9.3	Test Requirements	2478

A.6.3.1.10	Intra-band inter-frequency asynchronous DAPS handover test in SA for FR1	2478

A.6.3.1.10.1	Test Purpose and Environment	2478

A.6.3.1.10.2	Test Parameters	2478

A.6.3.1.10.3	Test Requirements	2480

A.6.3.1.11	Inter-band inter-frequency synchronous DAPS handover from FR1 to FR1	2480

A.6.3.1.11.1	Test Purpose and Environment	2480

A.6.3.1.11.2	Test Parameters	2480

A.6.3.1.11.3 Test Requirements	2484

A.6.3.1.12	Inter-band inter-frequency asynchronous DAPS handover from FR1 to FR1	2485

A.6.3.1.12.1	Test Purpose and Environment	2485

A.6.3.1.12.2	Test Parameters	2485

A.6.3.1.12.3	Test Requirements	2489

A.6.3.1.13	SA NR - E-UTRAN with NR PSCell addition in FR1	2489

A.6.3.1.13.1	Test Purpose and Environment	2489

A.6.3.1.13.2	Test Requirements	2494

A.6.3.1.14	SA NR - E-UTRAN handover with NR FR1 PSCell addition	2494

A.6.3.1.14.1	Test Purpose and Environment	2494

A.6.3.1.14.2	Test Requirements	2499

A.6.3.1.15	Intra-frequency handover from FR1 to FR1; known target cell configured with NCD-SSB	2500

A.6.3.1.15.1	Test Purpose and Environment	2500

A.6.3.1.15.2	Test Parameters	2500

A.6.3.1.15.3	Test Requirements	2503

A.6.3.1.16	Inter-frequency handover from FR1 to FR1; known target cell configured with NCD-SSB	2503

A.6.3.1.16.1	Test Purpose and Environment	2503

A.6.3.1.16.2	Test Parameters	2503

A.6.3.1.16.3 Test Requirements	2505

A.6.3.1.17	Handover with PSCell change delay from NR-DC (FR1-FR1) to NR-DC (FR1-FR1)	2505

A.6.3.1.17.1	Test Purpose and Environment	2505

A.6.3.1.17.2	Test Requirements	2509

A.6.3.1.18	Intra-frequency handover from FR1 to FR1; unknown target cell operating with 12 PRB SSB bandwidth	2509

A.6.3.1.18.2	Test Parameters	2509

A.6.3.1.18.3	Test Requirements	2510

A.6.3.2	RRC Connection Mobility Control	2511

A.6.3.2.1	SA: RRC Re-establishment	2511

A.6.3.2.1.1	Intra-frequency RRC Re-establishment in FR1	2511

A.6.3.2.1.2	Inter-frequency RRC Re-establishment in FR1	2513

A.6.3.2.1.3	Intra-frequency RRC Re-establishment in FR1 without serving cell timing	2516

A.6.3.2.2	Random Access	2518

A.6.3.2.2.1	4-step RA type contention based random access test in FR1 for NR standalone	2518

A.6.3.2.2.2	4-step RA type non-contention based random access test in FR1 for NR standalone	2521

A.6.3.2.2.3	2-step RA type contention based random access test in FR1 for NR standalone	2524

A.6.3.2.2.4	2-step RA type non-contention based test in FR1 for NR standalone	2527

A.6.3.2.3	SA: RRC Connection Release with Redirection	2529

A.6.3.2.3.1	Redirection from NR in FR1 to NR in FR1	2529

A.6.3.2.3.2	Redirection from NR in FR1 to E-UTRAN	2531

A.6.3.2.4	LTM PDCCH-order Random Access	2534

A.6.3.2.4.1	PDCCH-order RACH on neighbor cell in FR1 when RACH BW is within active UL BWP	2534

A.6.3.2.4.2	PDCCH-ordered RACH to an inter-frequency candidate cell in FR1 for LTM	2538

A.6.3.2.4.3	PDCCH-order RACH on neighbor cell without L1-RSRP measurement in FR1 when RACH BW is within active UL BWP	2542

A.6.3.3	Conditional handover	2545

A.6.3.3.1	Intra-frequency conditional handover from FR1 to FR1	2545

A.6.3.3.1.1	Test Purpose and Environment	2545

A.6.3.3.1.2	Test Parameters	2545

A.6.3.3.1.3	Test Requirements	2547

A.6.3.3.2	Inter-frequency conditional handover from FR1 to FR1	2547

A.6.3.3.2.1	Test Purpose and Environment	2547

A.6.3.3.2.2	Test Parameters	2547

A.6.3.3.2.3	Test Requirements	2549

A.6.3.3.3	NR conditional handover including target MCG and target SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC	2549

A.6.3.3.3.1	Test Purpose and Environment	2549

A.6.3.3.3.2	Test Requirements	2553

A.6.3.3.4	NR conditional handover including target MCG and candidate SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC	2553

A.6.3.3.4.1	Test Purpose and Environment	2553

A.6.3.3.4.2	Test Parameters	2553

A.6.3.3.4.3	Test Requirements	2557

A.6.3.3.5	NR conditional handover including target MCG and candidate SCG from FR1-FR1 NR-DC to FR1-FR1 NR-DC with complementary conditional handover configuration	2557

A.6.3.3.5.1	Test Purpose and Environment	2557

A.6.3.3.5.2	Test Parameters	2558

A.6.3.3.5.3	Test Requirements	2561

A.6.3.3.6	NES triggering intra-frequency conditional handover from FR1 to FR1	2561

A.6.3.3.6.1	Test Purpose and Environment	2561

A.6.3.3.6.2	Test Parameters	2561

A.6.3.3.6.3	Test Requirements	2563

A.6.3.3.7	NES-based Inter-frequency conditional handover from FR1 to FR1	2563

A.6.3.3.7.1	Test Purpose and Environment	2563

A.6.3.3.7.2	Test Parameters	2563

A.6.3.3.7.3	Test Requirements	2565

A.6.3.4	LTM PCell Switch	2565

A.6.3.4.1	RACH-based Intra-frequency PCell switch from FR1 to FR1	2566

A.6.3.4.1.1	Test Purpose and Environment	2566

A.6.3.4.1.2	Test Parameters	2566

A.6.3.4.1.3	Test Requirements	2568

A.6.3.4.2	RACH based Inter-frequency LTM PCell switch from FR1 to FR1	2569

A.6.3.4.2.1	Test Purpose and Environment	2569

A.6.3.4.2.2	Test Parameters	2569

A.6.3.4.2.3	Test Requirements	2572

A.6.3.4.3	RACH-less Intra-frequency PCell switch from FR1 to FR1	2573

A.6.3.4.3.1	Test Purpose and Environment	2573

A.6.3.4.3.2	Test Parameters	2573

A.6.3.4.3.3	Test Requirements	2577

A.6.3.4.4	RACH-less Intra-frequency PCell switch from FR1 to FR1 without L1-RSRP measurement	2577

A.6.3.4.4.1	Test Purpose and Environment	2577

A.6.3.4.4.2	Test Parameters	2577

A.6.3.4.4.3	Test Requirements	2581

A.6.3.5	LTM PSCell Switch	2581

A.6.3.5.1 RACH-based intra-frequency LTM PSCell switch from FR1 to FR1	2581

A.6.3.5.1.1	Test Purpose and Environment	2581

A.6.3.5.1.2	Test Parameters	2581

A.6.3.5.1.3	Test Requirements	2586

A.6.4	Timing	2586

A.6.4.1	UE transmit timing	2586

A.6.4.1.1	NR UE Transmit Timing Test for FR1	2586

A.6.4.1.1.1	Test Purpose and environment	2586

A.6.4.1.1.2	Test requirements	2588

A.6.4.1.2	NR UE Transmit Timing Test for two TRPs in FR1	2589

A.6.4.1.2.1	Test Purpose and environment	2589

A.6.4.1.2.2	Test requirements	2591

A.6.4.2	UE timer accuracy	2592

A.6.4.3	Timing advance	2592

A.6.4.3.1	SA FR1 timing advance adjustment accuracy	2592

A.6.4.3.1.1	Test Purpose and Environment	2592

A.6.4.3.1.2	Test Parameters	2592

A.6.4.3.1.3	Test Requirements	2595

A.6.5	Signalling characteristics	2595

A.6.5.1	Radio link Monitoring	2595

A.6.5.1.1	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode	2595

A.6.5.1.1.1	Test Purpose and Environment	2595

A.6.5.1.1.2	Test Requirements	2598

A.6.5.1.2	Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode	2598

A.6.5.1.2.1	Test Purpose and Environment	2598

A.6.5.1.2.2	Test Requirements	2601

A.6.5.1.3	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode	2601

A.6.5.1.3.1	Test Purpose and Environment	2601

A.6.5.1.3.2	Test Requirements	2604

A.6.5.1.4	Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode	2604

A.6.5.1.4.1	Test Purpose and Environment	2604

A.6.5.1.4.2	Test Requirements	2607

A.6.5.1.5	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode	2607

A.6.5.1.5.1	Test Purpose and Environment	2607

A.6.5.1.5.2	Test Requirements	2610

A.6.5.1.6	Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode	2610

A.6.5.1.6.1	Test Purpose and Environment	2610

A.6.5.1.6.2	Test Requirements	2613

A.6.5.1.7	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode	2613

A.6.5.1.7.1	Test Purpose and Environment	2613

A.6.5.1.7.2	Test Requirements	2616

A.6.5.1.8	Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode	2617

A.6.5.1.8.1	Test Purpose and Environment	2617

A.6.5.1.8.2	Test Requirements	2620

A.6.5.1.9	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM for UE fulfilling relaxed measurement criterion	2620

A.6.5.1.9.1	Test Purpose and Environment	2620

A.6.5.1.9.2	Test Requirements	2623

A.6.5.1.10	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode when CD-SSB is outside active BWP	2623

A.6.5.1.10.1	Test Purpose and Environment	2623

A.6.5.1.11	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode when CD-SSB is outside active BWP	2624

A.6.5.1.11.1	Test Purpose and Environment	2624

A.6.5.1.11.2	Test Requirements	2624

A.6.5.1.12	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for UE supporting NCD-SSB based measurement outside active BWP	2624

A.6.5.1.12.1	Test Purpose and Environment	2624

A.6.5.1.12.2	Test Requirements	2627

A.6.5.1.13	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for UE operating on a cell with less than 5 MHz BW	2627

A.6.5.1.13.1	Test Purpose and Environment	2627

A.6.5.1.13.2	Test Requirements	2628

A.6.5.1.14	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for UE operating on a cell with less than 5 MHz BW	2628

A.6.5.1.14.1	Test Purpose and Environment	2628

A.6.5.1.14.2	Test Requirements	2629

A.6.5.1.15	Radio Link Monitoring In-sync Test for FR1 PCell with 3 MHz Channel Bandwidth configured with SSB-based RLM RS in non-DRX mode	2629

A.6.5.1.15.1	Test Purpose and Environment	2629

A.6.5.1.15.2	Test Requirements	2630

A.6.5.1.16	Radio Link Monitoring In-sync Test for FR1 PCell with 3MHz Channel Bandwidth configured with SSB-based RLM RS in DRX mode	2630

A.6.5.1.16.1	Test Purpose and Environment	2630

A.6.5.1.16.2	Test Requirements	2631

A.6.5.2	Interruption	2632

A.6.5.2.1	Interruptions during measurements on deactivated NR SCC in FR1	2632

A.6.5.2.1.2	Test Requirements	2635

A.6.5.2.2	SA interruptions at NR SRS carrier based switching	2636

A.6.5.2.2.1	Test Purpose and Environment	2636

A.6.5.2.2.2	Test Parameters	2636

A.6.5.2.2.3	Test Requirements	2638

A.6.5.2.3	SA interruptions at NR SRS antenna port switching with 1 SRS symbol in a slot in NR-CA	2638

A.6.5.2.3.1	Test Purpose and Environment	2638

A.6.5.2.3.2	Test Parameters	2638

A.6.5.2.3.3	Test Requirements	2640

A.6.5.2.4	SA interruptions at NR SRS antenna port switching	2640

A.6.5.2.4.1	Test Purpose and Environment	2640

A.6.5.2.4.2	Test Parameters	2640

A.6.5.2.4.3	Test Requirements	2642

A.6.5.3	SCell Activation and Deactivation Delay	2642

A.6.5.3.1	SCell Activation and deactivation of known SCell in FR1 in non-DRX for 160 ms SCell measurement cycle	2642

A.6.5.3.1.1	Test Purpose and Environment	2642

A.6.5.3.1.2	Test Requirements	2647

A.6.5.3.2	SCell Activation and deactivation of known SCell in FR1 in non-DRX for 640 ms SCell measurement cycle	2647

A.6.5.3.2.1	Test Purpose and Environment	2647

A.6.5.3.2.2	Test Requirements	2648

A.6.5.3.3	SCell Activation and deactivation of unknown SCell in FR1 in non-DRX	2648

A.6.5.3.3.1	Test Purpose and Environment	2648

A.6.5.3.3.2	Test Requirements	2649

A.6.5.3.4	Direct SCell activation at SCell addition of known SCell in FR1	2649

A.6.5.3.4.1	Test Purpose and Environment	2649

A.6.5.3.4.2	Test Requirements	2652

A.6.5.3.5	Direct SCell activation at handover with known SCell in FR1	2653

A.6.5.3.5.1	Test Purpose and Environment	2653

A.6.5.3.5.2	Test Requirements	2657

A.6.5.3.6	PUCCH SCell Activation and deactivation of known SCell in FR1	2658

A.6.5.3.6.1	Test Purpose and Environment	2658

A.6.5.3.6.2	Test Requirements	2661

A.6.5.3.7	SCell Activation and deactivation of unknown SCell in FR1 in non-DRX	2661

A.6.5.3.7.1	Test Purpose and Environment	2661

A.6.5.3.7.2	Test Requirements	2664

A.6.5.3.8	SCell Activation and Deactivation of one FR1 known PUCCH SCell and one FR1 unknown SCell with single activation/deactivation command	2665

A.6.5.3.8.1	Test Purpose and Environment	2665

A.6.5.3.8.2	Test Requirements	2668

A.6.5.3.9	SCell Activation and deactivation of unknown PUCCH SCell and unknown DL SCell in FR1 in non-DRX	2669

A.6.5.3.9.1	Test Purpose and Environment	2669

A.6.5.3.9.2	Test Requirements	2672

A.6.5.3.10	Fast SCell Activation of known SCell in FR1 in non-DRX for 160 ms SCell measurement cycle	2672

A.6.5.3.10.1	Test Purpose and Environment	2672

A.6.5.3.10.2	Test Requirements	2675

A.6.5.3.11	SCell Activation of known SCell in FR1 in non-DRX for 640 ms SCell measurement cycle	2676

A.6.5.3.11.1	Test Purpose and Environment	2676

A.6.5.3.11.2	Test Requirements	2676

A.6.5.3.12	SCell Activation and deactivation of unknown SCell in FR1 in DRX for UE capable of short measurement interval	2676

A.6.5.3.12.1	Test Purpose and Environment	2676

A.6.5.3.12.2	Test Requirements	2679

A.6.5.3.13	SCell Activation of multiple unknown SCells in FR1 with L3 reporting with single activation/deactivation commandin non-DRX	2679

A.6.5.3.13.1	Test Purpose and Environment	2679

A.6.5.3.13.2	Test Requirements	2684

A.6.5.3.14	SCell Activation of unknown SCell with valid L3 measurement results in FR1 in non-DRX for 160 ms SCell measurement cycle	2684

A.6.5.3.14.1	Test Purpose and Environment	2684

A.6.5.3.14.2	Test Requirements	2689

A.6.5.3.15	TRS based SCell Activation of SSB-less SCell in FR1 inter-band CA in non-DRX	2690

A.6.5.3.15.1	Test Purpose and Environment	2690

A.6.5.3.15.2	Test Requirements	2694

A.6.5.3.16	Inter-band SSB-less SCell Activation based on A-TRS	2694

A.6.5.3.16.1	Test Purpose and Environment	2694

A.6.5.3.16.2	Test Requirements	2698

A.6.5.4	UE UL carrier RRC reconfiguration Delay	2699

A.6.5.4.1	UE UL carrier RRC reconfiguration Delay	2699

A.6.5.4.1.1	Test Purpose and Environment	2699

A.6.5.4.1.2	Test Requirements	2704

A.6.5.4.2	Void	2704

A.6.5.5	Beam Failure Detection and Link recovery procedures	2704

A.6.5.5.1	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode	2704

A.6.5.5.1.1	Test Purpose and Environment	2704

A.6.5.5.1.2	Test Requirements	2708

A.6.5.5.2	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode	2708

A.6.5.5.2.1	Test Purpose and Environment	2708

A.6.5.5.2.2	Test Requirements	2712

A.6.5.5.3	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode	2712

A.6.5.5.3.1	Test Purpose and Environment	2712

A.6.5.5.3.2	Test Requirements	2715

A.6.5.5.4	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode	2716

A.6.5.5.4.1	Test Purpose and Environment	2716

A.6.5.5.4.2	Test Requirements	2720

A.6.5.5.5	Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in non-DRX mode	2720

A.6.5.5.5.1	Test Purpose and Environment	2720

A.6.5.5.5.2	Test Requirements	2723

A.6.5.5.6	Beam Failure Detection and Link Recovery Test for FR1 SCell configured with CSI-RS-based BFD and SSB-based LR in DRX mode	2724

A.6.5.5.6.1	Test Purpose and Environment	2724

A.6.5.5.6.2	Test Requirements	2727

A.6.5.5.7	TRP Specific Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode	2728

A.6.5.5.7.1	Test Purpose and Environment	2728

A.6.5.5.7.2	Test Requirements	2731

A.6.5.5.8	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode for a UE operating on a cell with less than 5 MHz BW	2732

A.6.5.5.8.1	Test Purpose and Environment	2732

A.6.5.5.8.2	Test Requirements	2733

A.6.5.6	Active BWP switch	2733

A.6.5.6.1	DCI-based and Timer-based Active BWP Switch	2733

A.6.5.6.1.1	NR FR1- NR FR1 DL active BWP switch of SCell with non-DRX in SA	2733

A.6.5.6.1.2	NR FR1 DL active BWP switch with non-DRX in SA	2738

A.6.5.6.2	RRC-based Active BWP Switch	2741

A.6.5.6.2.1	NR FR1 DL active BWP switch of Cell with non-DRX in SA	2741

A.6.5.6.3 Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs	2743

A.6.5.6.3.1	NR FR1- NR FR1 DL active BWP switch on multiple CCs with non-DRX in SA	2743

A.6.5.6.4	SCell dormancy switch	2749

A.6.5.6.4.1	NR FR1 PCell SCell dormancy switch of single FR1 SCell outside active time	2749

A.6.5.6.4.1.1	Test Purpose and Environment	2749

A.6.5.6.4.1.2	Test Requirements	2753

A.6.5.6.4.2	NR FR1 PCell SCell dormancy switch of two FR1 SCells inside active time	2754

A.6.5.6.4.2.1	 Test Purpose and Environment	2754

A.6.5.6.4.2.2	Test Requirements	2759

A.6.5.6.5	Simultaneous RRC-based Active BWP Switch on multiple CCs	2759

A.6.5.6.5.1	NR FR1- NR FR1 DL active BWP switch on multiple CCs with non-DRX in SA	2759

A.6.5.7	DL interruptions at switching between two uplink carriers	2763

A.6.5.7.1	DL interruptions at switching between two uplink carriers in FDD-TDD CA	2763

A.6.5.7.1.1	Test Purpose and Environment	2763

A.6.5.7.1.2	Test Requirements	2766

A.6.5.7.2	DL interruptions at switching between two uplink carriers in TDD-TDD CA	2766

A.6.5.7.2.1	Test Purpose and Environment	2766

A.6.5.7.2.2	Test Requirements	2768

A.6.5.7A	DL interruptions at switching between two uplink carriers with two transmit antenna connectors	2768

A.6.5.7A.1	DL interruptions at switching between two uplink carriers in FDD-TDD CA	2768

A.6.5.7A.1.1	Test Purpose and Environment	2768

A.6.5.7A.1.2	Test Requirements	2771

A.6.5.7A.2	DL interruptions at switching between two uplink carriers in TDD-TDD CA	2771

A.6.5.7A.2.1	Test Purpose and Environment	2771

A.6.5.7A.2.2	Test Requirements	2773

A.6.5.7B	DL interruptions at switching between one uplink band with one transmit antenna connector and one uplink band with two transmit antenna connectors	2773

A.6.5.7B.1	DL interruptions at switching between two uplink bands in FDD-TDD CA	2773

A.6.5.7B.1.1	Test Purpose and Environment	2773

A.6.5.7B.1.2	Test Requirements	2777

A.6.5.7B.2	DL interruptions at switching between two uplink bands in TDD-TDD CA	2777

A.6.5.7B.2.1	Test Purpose and Environment	2777

A.6.5.7B.2.2	Test Requirements	2781

A.6.5.7C	DL interruptions at switching between two uplink bands with two transmit antenna connectors	2781

A.6.5.7C.1	DL interruptions at switching between two uplink bands with two transmit antenna connectors in FDD-TDD CA	2781

A.6.5.7C.1.1	Test Purpose and Environment	2781

A.6.5.7C.1.2	Test Requirements	2785

A.6.5.7C.2	DL interruptions at switching between two uplink bands with two transmit antenna connectors in TDD-TDD CA	2785

A.6.5.7C.2.1	Test Purpose and Environment	2785

A.6.5.7C.2.2	Test Requirements	2789

A.6.5.7D	DL interruptions at UE switching across three or four uplink bands	2789

A.6.5.7D.1	DL interruptions at switching across three uplink bands in TDD-TDD CA for single TAG	2789

A.6.5.7D.1.1	Test Purpose and Environment	2789

A.6.5.7D.1.2	Test Requirements	2793

A.6.5.7D.2	DL interruptions at switching across four uplink bands in FDD-TDD CA for single TAG	2793

A.6.5.7D.2.1	Test Purpose and Environment	2793

A.6.5.7D.2.2	Test Requirements	2797

A.6.5.7D.3	DL interruptions at switching across three uplink bands in FDD-TDD CA for two TAGs	2797

A.6.5.7D.3.1	Test Purpose and Environment	2797

A.6.5.7D.3.2	Test Requirements	2801

A.6.5.7D.4	DL interruptions at switching across four uplink bands in TDD-TDD CA for two TAGs	2801

A.6.5.7D.4.1	Test Purpose and Environment	2801

A.6.5.7D.7.2	Test Requirements	2805

A.6.5.8	UE specific CBW change	2805

A.6.5.8.1	UE specific CBW change on PCell in FR1 in non-DRX	2805

A.6.5.8.1.1	Test Purpose and Environment	2805

A.6.5.8.1.2	Test Requirements	2807

A.6.5.9	Pathloss reference signal switching delay	2807

A.6.5.9.1	MAC-CE based pathloss reference signal switch delay	2807

A.6.5.9.1.1	Test Purpose and Environment	2807

A.6.5.9.1.2	Test Requirements	2810

A.6.5.10	Conditional PSCell addition and release delay (FR1 NR-DC)	2810

A.6.5.10.1	Conditional PSCell Addition and Release Delay	2810

A.6.5.10.1.1	Test purpose and environment	2810

A.6.5.10.1.2	Test Parameters	2810

A.6.5.10.1.3	Test Requirements	2813

A.6.5.11	PSCell addition and release delay	2813

A.6.5.11.1	Addition and Release Delay of unknown NR FR1 PSCell	2813

A.6.5.11.1.1	Test purpose and environment	2813

A.6.5.11.1.2	Test Requirements	2815

A.6.5.12	Subsequent conditional PSCell addition/change	2816

A.6.5.12.1	Intra-frequency subsequent CPC from FR1-FR1 NR-DC to FR1-FR1 NR-DC	2816

A.6.5.12.1.1	Test purpose and environment	2816

A.6.5.12.1.2	Test Parameters	2816

A.6.5.12.1.3	Test Requirements	2818

A.6.5.12.2	Inter-frequency subsequent CPA from FR1-FR1 NR-DC to FR1-FR1 NR-DC	2819

A.6.5.12.2.1	Test purpose and environment	2819

A.6.5.12.2.2	Test Parameters	2819

A.6.5.12.2.3	Test Requirements	2822

A.6.5.13	Active TCI state switch delay	2822

A.6.5.13.1	MAC-CE based joint TCI state switch for mDCI with two TA when RTD is larger than CP	2822

A.6.5.13.1.1	Test Purpose and Environment	2822

A.6.5.13.1.2	Test Requirements	2824

A.6.6	Measurement procedure	2827

A.6.6.1	Intra-frequency Measurements	2827

A.6.6.1.1	SA event triggered reporting tests without gap under non-DRX	2827

A.6.6.1.1.1	Test purpose and Environment	2827

A.6.6.1.1.2	Test parameters	2827

A.6.6.1.1.3	Test Requirements	2829

A.6.6.1.2	SA event triggered reporting tests without gap under DRX	2829

A.6.6.1.2.1	Test purpose and Environment	2829

A.6.6.1.2.2	Test parameters	2829

A.6.6.1.2.3	Test Requirements	2831

A.6.6.1.3	SA event triggered reporting tests with per-UE gaps under non-DRX	2831

A.6.6.1.3.1	Test purpose and Environment	2831

A.6.6.1.3.2	Test parameters	2831

A.6.6.1.3.3	Test Requirements	2833

A.6.6.1.4	SA event triggered reporting tests with per-UE gaps under DRX	2833

A.6.6.1.4.1	Test purpose and Environment	2833

A.6.6.1.4.2	Test parameters	2834

A.6.6.1.4.3	Test Requirements	2836

A.6.6.1.5	SA event triggered reporting tests without gap under non-DRX with SSB index reading	2836

A.6.6.1.5.1	Test purpose and Environment	2836

A.6.6.1.5.2	Test parameters	2836

A.6.6.1.5.3	Test Requirements	2837

A.6.6.1.6	SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading	2837

A.6.6.1.6.1	Test purpose and Environment	2837

A.6.6.1.6.2	Test parameters	2838

A.6.6.1.6.3	Test Requirements	2839

A.6.6.1.7	SA event triggered reporting tests under DRX for UE configured with highSpeedMeasFlag-r16	2839

A.6.6.1.7.1	Test purpose and Environment	2839

A.6.6.1.7.2	Test parameters	2839

A.6.6.1.7.3	Test Requirements	2841

A.6.6.1.8	SA event triggered reporting tests without gap under DRX for UE configured with highSpeedMeasCA-Scell-r17	2842

A.6.6.1.8.1	Test purpose and Environment	2842

A.6.6.1.8.2	Test parameters	2842

A.6.6.1.8.3	Test Requirements	2844

A.6.6.1.9	SA event triggered reporting tests with MUSIM gap configured	2844

A.6.6.1.9.1	Test purpose and Environment	2844

A.6.6.1.9.2	Test parameters	2844

A.6.6.1.9.3	Test requirements	2846

A.6.6.1.10	SA event triggered reporting tests without gap under non-DRX when CD-SSB is outside active BWP	2846

A.6.6.1.10.1	Test purpose and Environment	2846

A.6.6.1.10.2	Test Requirements	2847

A.6.6.1.11	SA event triggered reporting tests without gap under non-DRX with NCD-SSB	2847

A.6.6.1.11.1	Test purpose and Environment	2847

A.6.6.1.11.2	Test parameters	2847

A.6.6.1.11.3	Test Requirements	2848

A.6.6.1.12	SA event triggered reporting tests without gap under non-DRX with SSB index reading and 12 PRB SSB	2849

A.6.6.1.12.1	Test purpose and Environment	2849

A.6.6.1.12.2	Test parameters	2849

A.6.6.1.12.3	Test Requirements	2849

A.6.6.1.13	SA event triggered reporting tests without gap under Cell DTX	2849

A.6.6.1.13.1	Test purpose and Environment	2850

A.6.6.1.13.2	Test parameters	2850

A.6.6.1.13.3	Test Requirements	2851

A.6.6.2	Inter-frequency Measurements	2852

A.6.6.2.1	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used	2852

A.6.6.2.1.1	Test Purpose and Environment	2852

A.6.6.2.1.2	Test Requirements	2854

A.6.6.2.2	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used	2854

A.6.6.2.2.1	Test Purpose and Environment	2854

A.6.6.2.2.2	Test Requirements	2857

A.6.6.2.3	Void	2857

A.6.6.2.4	Void	2857

A.6.6.2.5	SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used	2857

A.6.6.2.5.1	Test Purpose and Environment	2857

A.6.6.2.5.2	Test Requirements	2860

A.6.6.2.6	SA event triggered reporting tests for FR1 with SSB time index detection when DRX is used	2860

A.6.6.2.6.1	Test Purpose and Environment	2860

A.6.6.2.6.2	Test Requirements	2862

A.6.6.2.7	Void	2863

A.6.6.2.8	Void	2863

A.6.6.2.9	SA event triggered reporting tests with additional mandatory gap pattern	2863

A.6.6.2.9.1	Test Purpose and Environment	2863

A.6.6.2.9.2	Test Requirements	2865

A.6.6.2.10	SA event triggered reporting tests for FR1 when DRX is used	2865

A.6.6.2.10.1	Test Purpose and Environment	2865

A.6.6.2.10.2	Test Requirements	2867

A.6.6.2.12	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used for UE configured with highSpeedMeasInterFreq-r17	2870

A.6.6.2.12.1	Test Purpose and Environment	2870

A.6.6.2.12.2	Test Requirements	2872

A.6.6.2.13	SA event triggered reporting tests for FR1 with measurement gap with priority and periodic MUSIM gap configured	2873

A.6.6.2.13.1	Test Purpose and Environment	2873

A.6.6.2.13.2	Test Requirements	2875

A.6.6.2.14	SA event triggered reporting tests for FR1 with measurement gap without priority and periodic MUSIM gapconfigured	2875

A.6.6.2.14.1	Test Purpose and Environment	2875

A.6.6.2.14.2	Test Requirements	2878

A.6.6.2.15	SA event triggered reporting tests for FR1 with 3 MHz Channel Bandwidth configured without SSB time index detection when DRX is used	2878

A.6.6.2.15.1	Test Purpose and Environment	2878

A.6.6.2.15.2	Test Requirements	2879

A.6.6.3	Inter-RAT Measurements	2879

A.6.6.3.1	SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1	2879

A.6.6.3.1.1	Test Purpose and Environment	2879

A.6.6.3.1.2	Test Requirements	2882

A.6.6.3.2	SA NR - E-UTRAN event-triggered reporting in DRX in FR1	2882

A.6.6.3.2.1	Test Purpose and Environment	2882

A.6.6.3.2.2	Test Requirements	2885

A.6.6.3.3	SA NR - E-UTRAN event-triggered reporting in DRX in FR1 for UE configured with highSpeedMeasFlag-r16	2886

A.6.6.3.3.1	Test Purpose and Environment	2886

A.6.6.3.3.2	Test Requirements	2889

A.6.6.4	L1-RSRP measurement for beam reporting	2889

A.6.6.4.1	SSB based L1-RSRP measurement when DRX is not used	2889

A.6.6.4.1.1	Test Purpose and Environment	2889

A.6.6.4.1.2	Test parameters	2889

A.6.6.4.1.3	Test Requirements	2891

A.6.6.4.2	SSB based L1-RSRP measurement when DRX is used	2891

A.6.6.4.2.1	Test Purpose and Environment	2891

A.6.6.4.2.2	Test parameters	2891

A.6.6.4.2.3	Test Requirements	2893

A.6.6.4.3	CSI-RS based L1-RSRP measurement when DRX is not used	2893

A.6.6.4.3.1	Test Purpose and Environment	2893

A.6.6.4.3.2	Test parameters	2893

A.6.6.4.3.3	Test Requirements	2895

A.6.6.4.4	CSI-RS based L1-RSRP measurement when DRX is used	2895

A.6.6.4.4.1	Test Purpose and Environment	2895

A.6.6.4.4.2	Test parameters	2895

A.6.6.4.4.3	Test Requirements	2896

A.6.6.4.5	SSB based L1-RSRP measurement when DRX is used for UE configured with *highSpeedMeasFlag-r16* 2897

A.6.6.4.5.1	Test Purpose and Environment	2897

A.6.6.4.5.2	Test parameters	2897

A.6.6.4.5.3	Test Requirements	2898

A.6.6.4.6	Inter-cell SSB based L1-RSRP measurements on FR1 PCell when DRX is used	2899

A.6.6.4.6.1	Test Purpose and Environment	2899

A.6.6.4.6.2	Test parameters	2899

A.6.6.4.6.3	Test Requirements	2900

A.6.6.4.7	SSB based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP	2901

A.6.6.4.7.1	Test Purpose and Environment	2901

A.6.6.4.7.2	Test Requirements	2901

A.6.6.4.8	CSI-RS based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP	2901

A.6.6.4.8.1	Test Purpose and Environment	2901

A.6.6.4.9	SSB based L1-RSRP measurement for UE supporting NCD-SSB based L1 measurement outside active BWP when DRX is not used	2901

A.6.6.4.9.1	Test Purpose and Environment	2901

A.6.6.4.9.2	Test parameters	2902

A.6.6.4.9.3	Test Requirements	2903

A.6.6.5	Inter-RAT UTRAN FDD measurements	2903

A.6.6.5.1	SA NR - UTRAN FDD event-triggered reporting in non-DRX in FR1	2903

A.6.6.5.1.1	Test Purpose and Environment	2903

A.6.6.5.1.2	Test Requirements	2906

A.6.6.6	CLI measurements	2906

A.6.6.6.1	SRS-RSRP measurement with DRX	2906

A.6.6.6.1.1	Test Purpose and Environment	2906

A.6.6.6.1.2	Test Parameters	2906

A.6.6.6.1.3	Test Requirements	2908

A.6.6.6.2	CLI-RSSI measurement with DRX	2908

A.6.6.6.2.1	Test Purpose and Environment	2908

A.6.6.6.2.2	Test Parameters	2909

A.6.6.6.2.3	Test Requirements	2910

A.6.6.7	NR measurements with autonomous gaps	2910

A.6.6.7.1	SA intra-frequency CGI identification of NR neighbor cell in FR1	2910

A.6.6.7.1.1	Test Purpose and Environment	2910

A.6.6.7.1.2	Test Parameters	2910

A.6.6.7.1.3	Test Requirements	2913

A.6.6.7.2	Identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR SA	2913

A.6.6.7.2.1	Test Purpose and Environment	2913

A.6.6.7.2.2	Test Requirements	2915

A.6.6.8	L1-SINR measurement for beam reporting	2916

A.6.6.8.1	L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured when DRX is used	2916

A.6.6.8.1.1	Test Purpose and Environment	2916

A.6.6.8.1.2	Test parameters	2916

A.6.6.8.1.3	Test Requirements	2918

A.6.6.8.2	L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is not used	2918

A.6.6.8.2.1	Test Purpose and Environment	2918

A.6.6.8.2.2	Test parameters	2918

A.6.6.8.2.3	Test Requirements	2920

A.6.6.8.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is not used	2920

A.6.6.8.3.1	Test Purpose and Environment	2920

A.6.6.8.3.2	Test parameters	2921

A.6.6.8.3.3	Test Requirements	2922

A.6.6.9	Idle Mode CA/DC Measurements	2922

A.6.6.9.1	SA Idle mode CA/DC measurement for FR1	2922

A.6.6.9.1.1	Test Purpose and Environment	2922

A.6.6.9.1.2	Test Requirements	2926

A.6.6.9.2	 Idle mode fast CA/DC eEMR measurement for FR1 without valid reporting	2926

A.6.6.9.2.1	Test Purpose and Environment	2926

A.6.6.9.2.2	Test Requirements	2929

A.6.6.9.3	Idle mode fast CA/DC cell reselection measurement for FR1 without valid reporting	2929

A.6.6.9.3.1	Test Purpose and Environment	2929

A.6.6.9.3.2	Test Requirements	2932

A.6.6.9.4	Idle mode fast CA/DC cell reselection measurement for FR1 with valid reporting	2932

A.6.6.9.4.1	Test Purpose and Environment	2932

A.6.6.9.4.2	Test Requirements	2935

A.6.6.10	CSI-RS based intra-frequency Measurements	2935

A.6.6.10.1	SA event triggered reporting tests without gap under non-DRX	2935

A.6.6.10.1.1	Test purpose and Environment	2935

A.6.6.10.1.2	Test Requirements	2937

A.6.6.11	CSI-RS based inter-frequency Measurements	2938

A.6.6.11.1	 SA event triggered reporting tests with gap under DRX	2938

A.6.6.11.1.1	Test Purpose and Environment	2938

A.6.6.11.1.2	Test Requirements	2940

A.6.6.12	RSTD measurements	2940

A.6.6.12.1	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA	2940

A.6.6.12.1.1	Test Purpose and Environment	2940

A.6.6.12.1.2	Test Requirements	2944

A.6.6.12.2	NR RSTD measurement reporting delay test case for dual positioning frequency layers in FR1 SA	2944

A.6.6.12.2.1	Test Purpose and Environment	2944

A.6.6.12.2.2	Test Requirements	2947

A.6.6.12.3	NR RSTD measurement reporting delay test case for single positioning frequency layer with reduced number of samples in FR1 SA	2948

A.6.6.12.3.1	Test Purpose and Environment	2948

A.6.6.12.3.2	Test Requirements	2951

A.6.6.12.4	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA without measurement gap	2951

A.6.6.12.4.1	Test Purpose and Environment	2951

A.6.6.12.4.2	Test Requirements	2954

A.6.6.12.5	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC\_CONNECTED state with Rx TEG	2954

A.6.6.12.5.1	Test Purpose and Environment	2954

A.6.6.12.5.2	Test Requirements	2958

A.6.6.12.6	NR RSTD measurement reporting delay test case for PRS aggregation in FR1 SA in RRC\_CONNECTED mode	2958

A.6.6.12.6.1	Test Purpose and Environment	2958

A.6.6.12.6.2	Test Requirements	2964

A.6.6.13 PRS-RSRP measurements	2964

A.6.6.13.1	PRS-RSRP reporting delay test case for single positioning frequency layer	2964

A.6.6.13.1.1	Test purpose and Environment	2964

A.6.6.13.1.2	Test Requirements	2966

A.6.6.13.2	PRS-RSRP reporting delay test case for dual positioning frequency layer	2966

A.6.6.13.2.1	Test purpose and Environment	2966

A.6.6.13.2.2	Test Requirements	2969

A.6.6.13.3	PRS-RSRP reporting delay test case for reduced number of samples	2969

A.6.6.13.3.1	Test purpose and Environment	2969

A.6.6.13.3.2	Test Requirements	2971

A.6.6.13.4	PRS-RSRP reporting delay test case for single positioning frequency layer outside MG	2971

A.6.6.13.4.1	Test purpose and Environment	2971

A.6.6.14	UE Rx-Tx time difference measurements	2974

A.6.6.14.1	UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA	2974

A.6.6.14.1.1	Test purpose and environment	2974

A.6.6.14.1.2	Test requirements	2976

A.6.6.14.2	UE Rx-Tx time difference measurement for dual positioning frequency layers in FR1 SA	2976

A.6.6.14.2.1	Test purpose and environment	2976

A.6.6.14.2.2	Test requirements	2978

A.6.6.14.3	UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA with reduced sample number	2979

A.6.6.14.3.1	Test purpose and environment	2979

A.6.6.14.3.2	Test requirements	2981

A.6.6.14.4	UE Rx-Tx time difference measurement without gaps in FR1 SA	2981

A.6.6.14.4.1	Test purpose and environment	2981

A.6.6.14.4.2	Test requirements	2983

A.6.6.14.5	UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA with multiple RxTx TEGs	2983

A.6.6.14.4.1	Test purpose and environment	2983

A.6.6.14.4.2	Test requirements	2985

A.6.6.14.6	UE Rx-Tx time difference measurements with PRS bandwidth aggregation in FR1 SA	2986

A.6.6.14.6.1	Test purpose and environment	2986

A.6.6.14.6.2	Test requirements	2989

A.6.6.15	Idle Mode measurements of inter-RAT DC candidate cells for early reporting	2989

A.6.6.15.1	Test Purpose and Environment	2989

A.6.6.15.2	Test Requirements	2993

A.6.6.16	PRS-RSRPP measurements	2994

A.6.6.16.1	PRS-RSRPP reporting delay test case for single positioning frequency layer in FR1 in RRC\_CONNECTED state	2994

A.6.6.16.1.1	Test purpose and Environment	2994

A.6.6.16.1.2	Test Requirements	2996

A.6.6.16.2	PRS-RSRPP reporting delay test case with reduced number of samples for single positioning frequency layer in FR1 in RRC\_CONNECTED state	2996

A.6.6.16.2.1	Test purpose and Environment	2996

A.6.6.16.2.2	Test Requirements	2998

A.6.6.16.3	PRS-RSRPP reporting delay test case for single positioning frequency layer in FR1 in RRC\_CONNECTED state without measurement gap	2998

A.6.6.16.3.1	Test purpose and Environment	2998

A.6.6.16.3.2	Test Requirements	3000

A.6.6.17	SA event triggered reporting tests with Pre-MG	3001

A.6.6.17.1	SA event triggered reporting tests with autonomous activation/deactivation Pre-MG	3001

A.6.6.17.1.1	Test purpose and Environment	3001

A.6.6.17.1.2	Test parameters	3001

A.6.6.17.1.3	Test Requirements	3003

A.6.6.17.2	SA event triggered reporting tests with pre-configured measurement gaps and network-controlled activation/deactivation	3004

A.6.6.17.2.1	Test purpose and Environment	3004

A.6.6.17.2.2	Test parameters	3004

A.6.6.17.2.3	Test Requirements	3006

A.6.6.17.3	Void	3007

A.6.6.17.3.1	Void	3007

A.6.6.17.3.2	Void	3007

A.6.6.17.3.3	Void	3007

A.6.6.18	SA event triggered reporting tests with concurrent gaps	3007

A.6.6.18.1	SA event triggered reporting tests for FR1 concurrent gaps with non-overalpping scenario for SSB-based measurements in both inter-frequency layers	3007

A.6.6.18.1.1	Test Purpose and Environment	3007

A.6.6.18.1.2	Test Requirements	3009

A.6.6.18.2	SA event triggered reporting tests for FR1 concurrent gap with partially partial overalpping scenario for SSB-based measurements in both inter-frequency layers	3009

A.6.6.18.2.1	Test Purpose and Environment	3009

A.6.6.18.2.2	Test Requirements	3012

A.6.6.18.3	SA NR - E-UTRAN and NR FR1 concurrent event-triggered reporting in non-DRX in FR1	3012

A.6.6.18.3.1	Test Purpose and Environment	3012

A.6.6.18.3.2	Test Requirements	3016

A.6.6.18.4	SA event triggered reporting tests for PRS and SSB measurement in FR1 without SSB time index detection when DRX is not used	3017

A.6.6.18.4.1	Test Purpose and Environment	3017

A.6.6.18.4.2	Test Requirements	3019

A.6.6.19	SA event triggered reporting tests with NCSG	3020

A.6.6.19.1	SA event triggered reporting tests with NCSG under non-DRX in FR1	3020

A.6.6.19.1.1	Test purpose and Environment	3020

A.6.6.19.1.2	Test parameters	3020

A.6.6.19.1.3	Test Requirements	3022

A.6.6.19.2	SA event triggered reporting tests for FR1 with NCSG for inter-frequency measurement	3022

A.6.6.19.2.1	Test Purpose and Environment	3022

A.6.6.19.2.2	Test parameters	3022

A.6.6.19.2.3	Test Requirements	3025

A.6.6.19.3	SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 with NCSG	3025

A.6.6.19.3.1	Test Purpose and Environment	3025

A.6.6.19.3.2	Test parameters	3025

A.6.6.19.3.3	Test Requirements	3028

A.6.6.19.4	Event triggered reporting on SCC with deactivated SCell test with per-UE NCSG under non-DRX	3029

A.6.6.19.4.1	Test purpose and Environment	3029

A.6.6.19.4.2	Test parameters	3029

A.6.6.19.4.3	Test Requirements	3031

A.6.6.20	UE Rx-Tx time difference measurement for propagation delay compensation	3031

A.6.6.20.1	Test purpose and environment	3031

A.6.6.20.2	Test requirements	3033

A.6.6.21	UE Rx-Tx time difference measurement with TRS for RTT-based PDC in FR1 SA	3033

A.6.6.21.1	Test purpose and environment	3033

A.6.6.21.2	Test requirements	3035

A.6.6.22	SA event triggered reporting tests for concurrent measurement gaps with Pre-MG	3035

A.6.6.22.1	SA event triggered reporting tests for FR1 concurrent gap with Pre-MG with partially partial overalpping scenario for SSB-based measurements in both intra-frequency and inter-frequency layers	3035

A.6.6.22.1.1	Test Purpose and Environment	3035

A.6.6.22.1.2	Test Requirements	3038

A.6.6.22.2	SA event triggered reporting tests for concurrent gap with pre-configured gaps and network-controlled activation/deactivation	3039

A.6.6.22.2.1	Test purpose and Environment	3039

A.6.6.22.2.2	Test parameters	3039

A.6.6.22.2.3	Test Requirements	3041

A.6.6.23	SA event triggered reporting tests for concurrent measurement gaps with NCSG	3042

A.6.6.23.1	SA event triggered reporting tests for FR1 concurrent gaps with NCSG for partially partial overalpping scenario for SSB-based measurements in both inter-frequency layers [one MG + one NCSG]	3042

A.6.6.23.1.1	Test Purpose and Environment	3042

A.6.6.23.1.2	Test Requirements	3044

A.6.6.23.2	SA event triggered reporting tests for FR1 concurrent gaps with NCSG for partially partial overalpping scenario for SSB-based measurements in both inter-frequency layers [two NCSG]	3045

A.6.6.23.2.1	Test Purpose and Environment	3045

A.6.6.23.2.2	Test Requirements	3047

A.6.6.23.3	Event triggered reporting on SCC with deactivated SCell test with per-UE Con-NCSG under non-DRX	3047

A.6.6.23.3.1	Test purpose and Environment	3047

A.6.6.23.3.2	Test parameters	3048

A.6.6.23.3.3	Test Requirements	3050

A.6.6.24	SA event triggered reporting tests with NeedForGap in FR1	3050

A.6.6.24.1	SA event triggered reporting tests without gaps, with interruptions, under non-DRX	3050

A.6.6.24.1.1	Test purpose and Environment	3050

A.6.6.24.1.2	Test parameters	3050

A.6.6.24.1.3	Test Requirements	3052

A.6.6.24.2	SA event triggered reporting tests for FR1 without gap with interruption for inter-frequency measurement with SSB time index detection when DRX is not used	3052

A.6.6.24.2.1	Test Purpose and Environment	3052

A.6.6.24.2.2	Test parameters	3052

A.6.6.24.2.3	Test Requirements	3055

A.6.6.24.3	SA event triggered reporting tests for FR1 with ‘no-gap-with-interruption’, without measurement gap or DRX	3055

A.6.6.24.3.1	Test Purpose and Environment	3055

A.6.6.24.3.2	Test Requirements	3057

A.6.6.24.4	SA event triggered reporting tests for FR1 NeedForGaps without gap without interruption when DRX is not used	3057

A.6.6.24.4.1	Test Purpose and Environment	3057

A.6.6.24.4.2	Test parameters	3058

A.6.6.24.4.3	Test Requirements	3060

A.6.6.24.5	SA event triggered reporting tests without gap under non-DRX for UE indicating *no-gap-no-interruption* 3060

A.6.6.24.5.1	Test purpose and Environment	3060

A.6.6.24.5.2	Test parameters	3060

A.6.6.24.5.3	Test Requirements	3062

A.6.6.25	SA NR - E-UTRAN event-triggered without measurement gaps	3062

A.6.6.25.1	SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1	3062

A.6.6.25.1.1	Test Purpose and Environment	3062

A.6.6.25.1.2	Test Requirements	3065

A.6.6.25.2	SA NR - E-UTRAN event-triggered reporting without gap under non-DRX in FR1	3066

A.6.6.25.2.1	Test Purpose and Environment	3066

A.6.6.25.2.2	Test parameters	3066

A.6.6.25.2.3	Test Requirements	3067

A.6.6.25.3	SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 for UE capable of inter-RAT EUTRAN measurement without gap when CRS is contained within UE’s active DL BWP	3067

A.6.6.25.3.1	Test Purpose and Environment	3067

A.6.6.25.3.2	Test Requirements	3070

A.6.6.26	LTM Intra-frequency L1-RSRP measurement	3070

A.6.6.26.1	Intra-frequency SSB based L1-RSRP measurement in FR1	3070

A.6.6.26.1.1	Test Purpose and Environment	3070

A.6.6.26.1.2	Test Parameters	3071

A.6.6.26.1.3	Test Requirements	3073

A.6.6.27	LTM Inter-frequency L1-RSRP measurement with measurement gap	3073

A.6.6.27.1	Inter-frequency SSB based L1-RSRP measurement with measurement gap	3073

A.6.6.27.1.1	Test Purpose and Environment	3073

A.6.6.27.1.2	Test parameters	3073

A.6.6.27.1.3	Test Requirements	3075

A.6.6.28	LTM Inter-frequency L1-RSRP measurement without measurement gap	3075

A.6.6.28.1	Inter-frequency SSB based L1-RSRP measurement without measurement gap	3075

A.6.6.28.1.1	Test Purpose and Environment	3075

A.6.6.28.1.2	Test parameters	3076

A.6.6.28.1.3	Test Requirements	3078

A.6.6.29	RSCPD Measurements	3078

A.6.6.29.1	NR RSCPD with RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC\_CONNECTED state	3078

A.6.6.29.1.1	Test Purpose and Environment	3078

A.6.6.29.1.2	Test Requirements	3086

A.6.6.30	RSCP Measurements	3086

A.6.6.30.1	DL RSCP with UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA	3086

A.6.6.30.1.1	Test purpose and environment	3086

A.6.6.30.1.2	Test requirements	3090

A.6.7	Measurement Performance requirements	3090

A.6.7.1	SS-RSRP	3090

A.6.7.1.1	SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell	3090

A.6.7.1.1.1	Test Purpose and Environment	3090

A.6.7.1.1.2	Test parameters	3090

A.6.7.1.1.3	Test Requirements	3094

A.6.7.1.2	SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell	3094

A.6.7.1.2.1	Test Purpose and Environment	3094

A.6.7.1.2.2	Test parameters	3094

A.6.7.1.2.3	Test Requirements	3097

A.6.7.1.3	Void	3097

A.6.7.2	SS-RSRQ	3097

A.6.7.2.1	SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	3097

A.6.7.2.1.1	Test Purpose and Environment	3097

A.6.7.2.1.2	Test Parameters	3097

A.6.7.2.1.3	Test Requirements	3100

A.6.7.2.2	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	3101

A.6.7.2.2.1	Test Purpose and Environment	3101

A.6.7.2.2.2	Test Parameters	3101

A.6.7.2.2.3	Test Requirements	3104

A.6.7.3	SS-SINR	3104

A.6.7.3.1	SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	3104

A.6.7.3.1.1	Test Purpose and Environment	3104

A.6.7.3.1.2	Test Parameters	3104

A.6.7.3.1.3	Test Requirements	3107

A.6.7.3.2	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	3107

A.6.7.3.2.1	Test Purpose and Environment	3107

A.6.7.3.2.2	Test Parameters	3108

A.6.7.3.2.3	Test Requirements	3111

A.6.7.4	L1-RSRP measurement for beam reporting	3111

A.6.7.4.1	SSB based L1-RSRP measurement	3111

A.6.7.4.1.1	Test Purpose and Environment	3111

A.6.7.4.1.2	Test parameters	3111

A.6.7.4.1.3	Test Requirements	3114

A.6.7.4.2	CSI-RS based L1-RSRP measurement on resource set with repetition off	3114

A.6.7.4.2.1	Test Purpose and Environment	3114

A.6.7.4.2.2	Test parameters	3114

A.6.7.4.2.3	Test Requirements	3117

A.6.7.5	E-UTRAN RSRP	3117

A.6.7.5.1	SA: inter-RAT measurement accuracy with FR1 serving cell	3117

A.6.7.5.1.1	Test Purpose and Environment	3117

A.6.7.5.1.2	Test parameters	3117

A.6.7.5.1.3	Test Requirements	3120

A.6.7.6	E-UTRAN RSRQ	3120

A.6.7.6.1	SA: inter-RAT measurement accuracy with FR1 serving cell	3120

A.6.7.6.1.1	Test Purpose and Environment	3120

A.6.7.6.1.2	Test parameters	3120

A.6.7.6.1.3	Test Requirements	3123

A.6.7.7	E-UTRAN RS-SINR	3124

A.6.7.7.1	SA: inter-RAT measurement accuracy with FR1 serving cell	3124

A.6.7.7.1.1	Test Purpose and Environment	3124

A.6.7.7.1.2	Test parameters	3124

A.6.7.7.1.3	Test Requirements	3127

A.6.7.8	CLI measurements	3127

A.6.7.8.1	SA SRS-RSRP measurement accuracy with FR1 serving cell	3127

A.6.7.8.1.1	Test Purpose and Environment	3127

A.6.7.8.1.2	Test parameters	3127

A.6.7.8.1.3	Test Requirements	3130

A.6.7.8.2	SA CLI-RSSI measurement accuracy with FR1 serving cell	3130

A.6.7.8.2.1	Test Purpose and Environment	3130

A.6.7.8.2.2	Test parameters	3131

A.6.7.8.2.3	Test Requirements	3132

A.6.7.9	L1-SINR measurement for beam reporting	3132

A.6.7.9.2	L1-SINR measurement with SSB based CMR and dedicated IMR	3135

A.6.7.9.2.1	Test Purpose and Environment	3135

A.6.7.9.2.2	Test parameters	3136

A.6.7.9.2.3	Test Requirements	3139

A.6.7.9.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR	3139

A.6.7.9.3.1	Test Purpose and Environment	3139

A.6.7.9.3.2	Test parameters	3139

A.6.7.9.3.3	Test Requirements	3142

A.6.7.10	CSI-RSRP	3142

A.6.7.10.1	SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell	3142

A.6.7.9.10.1	Test Purpose and Environment	3142

A.6.7.9.10.2	Test parameters	3142

A.6.7.10.1.3	Test Requirements	3145

A.6.7.10.2	SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell	3145

A.6.7.9.10.1	Test Purpose and Environment	3145

A.6.7.10.2.2	Test parameters	3146

A.6.7.10.2.3	Test Requirements	3148

A.6.7.11	CSI-RSRQ	3149

A.6.7.11.1	SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	3149

A.6.7.11.1.1	Test Purpose and Environment	3149

A.6.7.11.1.2	Test Parameters	3149

A.6.7.11.1.3	Test Requirements	3152

A.6.7.11.2	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	3152

A.6.7.11.2.1	Test Purpose and Environment	3152

A.6.7.11.2.2	Test Parameters	3152

A.6.7.11.2.3	Test Requirements	3156

A.6.7.12	CSI-SINR	3156

A.6.7.12.1	SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	3156

A.6.7.12.1.1	Test Purpose and Environment	3156

A.6.7.12.1.2	Test Parameters	3156

A.6.7.12.1.3	Test Requirements	3159

A.6.7.12.2	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	3159

A.6.7.12.2.1	Test Purpose and Environment	3159

A.6.7.12.2.2	Test Parameters	3159

A.6.7.12.2.3	Test Requirements	3162

A.6.7.13	RSTD measurements	3162

A.6.7.13.1	RSTD measurement accuracy test case for single positioning frequency layer	3162

A.6.7.13.1.1	Test purpose and Environment	3162

A.6.7.13.1.2	Test Requirements	3164

A.6.7.13.2	RSTD measurement accuracy test case for dual positioning frequency layer	3164

A.6.7.13.2.1	Test purpose and Environment	3164

A.6.7.13.2.2	Test Requirements	3166

A.6.7.13.3	RSTD measurement accuracy test case with reduced number of samples for single positioning frequency layer in FR1 in RRC\_CONNECTED state	3166

A.6.7.13.3.1	Test purpose and Environment	3166

A.6.7.13.3.2	Test Requirements	3168

A.6.7.13.4	RSTD measurement accuracy test case with Rx TEG	3168

A.6.7.13.5	NR RSTD measurement accuracy test case for PRS aggregation in FR1 SA in RRC\_CONNECTED mode	3170

A.6.7.13.5.1	Test purpose and Environment	3170

A.6.7.13.5.2	Test Requirements	3173

A.6.7.14	PRS-RSRP measurements	3173

A.6.7.14.1	SA: measurement accuracy with PRS in FR1	3173

A.6.7.14.1.1	Test Purpose and Environment	3173

A.6.7.14.1.2	Test parameters	3173

A.6.7.14.1.3	Test Requirements	3175

A.6.7.14.2	SA: measurement accuracy with PRS in FR1 with reduced sample number	3175

A.6.7.14.2.1	Test Purpose and Environment	3175

A.6.7.14.2.2	Test parameters	3175

A.6.7.14.2.3	Test Requirements	3177

A.6.7.14.3	Void	3177

A.6.7.14.3.1	Void	3177

A.6.7.14.3.2	Void	3177

A.6.7.14.3.3	Void	3177

A.6.7.15	UE Rx-Tx time difference measurements	3177

A.6.7.15.1	UE Rx-Tx time difference measurement accuracy for single positioning frequency layer in FR1 SA	3177

A.6.7.15.1.1	Test purpose and environment	3177

A.6.7.15.1.2	Test parameters	3178

A.6.7.15.1.3	Test requirements	3179

A.6.7.15.2	UE Rx-Tx time difference measurement accuracy with reduced number of samples in FR1 SA	3179

A.6.7.15.2.1	Test purpose and environment	3179

A.6.7.15.2.2	Test parameters	3180

A.6.7.15.2.3	Test requirements	3181

A.6.7.15.3	UE Rx-Tx time difference measurement accuracy with RxTx TEG	3181

A.6.7.15.3.1	Test purpose and environment	3181

A.6.7.15.3.2	Test parameters	3182

A.6.7.15.3.3	Test requirements	3184

A.6.7.15.4	UE Rx-Tx time difference measurement accuracy with PRS bandwidth aggregation in FR1 SA	3184

A.6.7.15.4.1	Test purpose and environment	3184

A.6.7.15.4.2	Test requirements	3187

A.6.7.16	PRS-RSRPP measurements	3187

A.6.7.16.1	SA: measurement accuracy with PRS in FR1	3187

A.6.7.16.1.1	Test Purpose and Environment	3187

A.6.7.16.1.2	Test parameters	3187

A.6.7.16.1.3	Test Requirements	3189

A.6.7.16.2	SA: measurement accuracy with reduced PRS samples in FR1	3189

A.6.7.16.2.1	Test Purpose and Environment	3189

A.6.7.16.2.2	Test parameters	3190

A.6.7.17	LTM L1-RSRP measurement	3191

A.6.7.17.1	Inter-frequency L1-RSRP accuracy requirements for neighbour cell in FR1	3191

A.6.7.17.1.1	Test Purpose and Environment	3191

A.6.7.17.1.2	Test parameters	3192

A.6.7.17.1.3	Test Requirements	3195

A.6.7.18	TDCP amplitude measurement accuracy	3195

A.6.7.18.1	TDCP amplitude measurement accuracy in FR1	3195

A.6.7.18.1.1	Test Purpose and Environment	3195

A.6.7.18.1.2	Test parameters	3195

A.6.7.18.1.3	Test Requirements	3196

A.6.7.19	RSCPD Measurements	3197

A.6.7.19.1	RSCPD with RSTD measurement accuracy in FR1 SA in RRC\_CONNECTED	3197

A.6.7.19.1.1	Test purpose and environment	3197

A.6.7.19.1.2	Test parameters	3197

A.6.7.19.1.3	Test requirements	3200

A.6.7.20	RSCP Measurements	3200

A.6.7.20.1	RSCP with UE Rx-Tx time difference measurement accuracy in FR1 SA	3200

A.6.7.20.1.1	Test purpose and environment	3200

A.6.7.20.1.2	Test parameters	3201

A.6.7.20.1.3	Test requirements	3204

A.6.8	Measurement procedure in RRC\_INACTIVE	3204

A.6.8.1	RSTD measurements	3204

A.6.8.1.1	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC\_INACTIVE state	3204

A.6.8.1.1.1	Test Purpose and Environment	3204

A.6.8.1.1.2	Test Requirements	3207

A.6.8.1.2	NR RSTD measurement reporting delay test case with reduced number of samples in RRC\_INACTIVE, FR1 SA	3207

A.6.8.1.2.1	Test Purpose and Environment	3207

A.6.8.1.2.1	Test Purpose and Environment	3207

A.6.8.1.2.2	Test Requirements	3210

A.6.8.1.3	NR RSTD measurement reporting delay test case for PRS aggregation in FR1 SA in RRC\_INACTIVE state	3211

A.6.8.1.3.1	Test purpose and environment	3211

A.6.8.1.3.2	Test requirements	3214

A.6.8.1.4	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC\_INACTIVE state when eDRX cycle &gt; 10.24s for non-RedCap UE	3215

A.6.8.1.4.1	Test Purpose and Environment	3215

A.6.8.1.4.2	Test Requirements	3218

A.6.8.2	PRS-RSRP measurements	3218

A.6.8.2.1	PRS-RSRP reporting delay test case for single positioning frequency layer in RRC\_INACTIVE	3218

A.6.8.2.1.1	Test purpose and Environment	3218

A.6.8.2.1.2	Test Requirements	3220

A.6.8.2.2	PRS-RSRP reporting delay test case with reduced number of samples in RRC\_INACTIVE	3220

A.6.8.2.2.1	Test purpose and Environment	3220

A.6.8.2.2.2	Test Requirements	3222

A.6.8.2.3	PRS-RSRP reporting delay test case in RRC\_INACTIVE state in FR1 with eDRX cycle &gt; 10.24s	3223

A.6.8.2.3.1	Test purpose and Environment	3223

A.6.8.2.3.2	Test Requirements	3225

A.6.8.3	UE Rx-Tx time difference measurements	3226

A.6.8.3.1	UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA	3226

A.6.8.3.1.1	Test purpose and environment	3226

A.6.8.3.1.2	Test requirements	3228

A.6.8.3.2	UE Rx-Tx time difference measurement with reduced number of samples in RRC\_INACTIVE, FR1 SA	3228

A.6.8.3.2.1	Test purpose and environment	3228

A.6.8.3.2.2	Test requirements	3230

A.6.8.3.3	UE Rx-Tx time difference measurement for single positioning frequency layer with eDRX &gt; 10.24s in FR1 SA	3231

A.6.8.3.3.1	Test purpose and environment	3231

A.6.8.3.3.2	Test requirements	3235

A.6.8.3.4	UE Rx-Tx time difference measurements with PRS bandwidth aggregation in FR1 SA	3235

A.6.8.3.4.1	Test purpose and environment	3235

A.6.8.3.4.2	Test requirements	3238

A.6.8.4	PRS-RSRPP measurements	3238

A.6.8.4.1	PRS-RSRPP reporting delay test case for single positioning frequency layer in FR1 in RRC\_INACTIVE state	3238

A.6.8.4.1.1	Test purpose and Environment	3239

A.6.8.4.1.2	Test Requirements	3240

A.6.8.4.2	PRS-RSRPP reporting delay test case for single positioning frequency layer in FR1 in RRC\_INACTIVE state for reduced number of samples	3241

A.6.8.4.2.1	Test purpose and Environment	3241

A.6.8.4.2.2	Test Requirements	3243

A.6.8.4.3	PRS-RSRPP reporting delay in RRC\_INACTIVE with eDRX	3243

A.6.8.4.3.1	Test purpose and Environment	3243

A.6.8.4.3.2	Test Requirements	3246

A.6.8.5	RSCPD Measurements	3246

A.6.8.5.1	DL RSCPD reported with RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC\_INACTIVE state	3246

A.6.8.5.1.1	Test Purpose and Environment	3246

A.6.8.5.1.2	Test Requirements	3246

A.6.8.6	RSCP Measurements	3247

A.6.8.6.1	DL RSCP with UE Rx-Tx time difference measurement for single positioning frequency layer in FR1 SA	3247

A.6.8.6.1.1	Test purpose and environment	3247

A.6.8.6.1.2	Test requirements	3251

A.6.9	Measurement performance requirements in RRC\_INACTIVE	3251

A.6.9.1	RSTD measurements	3251

A.6.9.1.1	RSTD measurement accuracy test case for single positioning frequency layer in FR1 in RRC\_INACTIVE state	3251

A.6.9.1.1.1	Test purpose and Environment	3251

A.6.9.1.1.2	Test Requirements	3253

A.6.9.1.2	RSTD measurement accuracy test case with reduced number of samples for single positioning frequency layer in FR1 in RRC\_INACTIVE state	3253

A.6.9.1.2.1	Test purpose and Environment	3253

A.6.9.1.2.2	Test Requirements	3255

A.6.9.1.3	RSTD measurement accuracy for PRS aggregation in FR1 in RRC\_INACTIVE state	3255

A.6.9.1.3.1	Test purpose and Environment	3255

A.6.9.1.3.2	Test Requirements	3258

A.6.9.2	PRS-RSRP measurements	3258

A.6.9.2.1	SA: measurement accuracy with PRS in FR1 in RRC\_INACTIVE	3258

A.6.9.2.1.1	Test Purpose and Environment	3258

A.6.9.2.1.2	Test parameters	3258

A.6.9.2.1.3	Test Requirements	3260

A.6.9.2.2	SA: measurement accuracy with PRS in FR1 with reduced number of samples in RRC\_INACTIVE state	3260

A.6.9.2.2.1	Test Purpose and Environment	3260

A.6.9.2.2.2	Test parameters	3260

A.6.9.2.2.3	Test Requirements	3262

A.6.9.3	UE Rx-Tx time difference measurements	3262

A.6.9.3.1.1	UE Rx-Tx time difference measurement accuracy in FR1 SA	3262

A.6.9.3.1.1.1	Test purpose and environment	3262

A.6.9.3.1.1.2 Test parameters	3263

A.6.9.3.1.1.3	Test requirements	3264

A.6.9.3.2	UE Rx-Tx time difference measurement accuracy with reduced number of samples	3264

A.6.9.3.2.1	Test purpose and environment	3264

A.6.9.3.2.2	Test parameters	3264

A.6.9.3.2.3	Test requirements	3266

A.6.9.3.3	UE Rx-Tx time difference measurement accuracy with PRS bandwidth aggregation in FR1 SA	3266

A.6.9.3.3.1	Test purpose and environment	3266

A.6.9.3.3.2	Test requirements	3269

A.6.9.4	PRS-RSRPP measurements	3269

A.6.9.4.1	SA: PRS-RSRPP measurement accuracy in FR1 in RRC INACTIVE	3269

A.6.9.4.1.1	Test Purpose and Environment	3269

A.6.9.4.1.2	Test parameters	3269

A.6.9.4.1.3	Test Requirements	3271

A.6.9.4.2	SA: measurement accuracy with reduced PRS samples in FR1 in RRC INACTIVE	3271

A.6.9.4.2.1	Test Purpose and Environment	3271

A.6.9.4.2.2	Test parameters	3272

A.6.9.4.2.3	Test Requirements	3273

A.6.9.5	RSCPD Measurements	3274

A.6.9.5.1	RSCPD with RSTD measurement accuracy in FR1 SA in RRC\_INACTIVE	3274

A.6.9.5.1.1	Test purpose and environment	3274

A.6.9.5.1.2	Test parameters	3274

A.6.9.5.1.3	Test requirements	3277

A.6.9.6	RSCP Measurements	3277

A.6.9.6.1	RSCP with UE Rx-Tx time difference measurement accuracy in FR1 SA	3277

A.6.9.6.1.1	Test purpose and environment	3277

A.6.9.6.1.2	Test parameters	3278

A.6.9.6.1.3	Test requirements	3281

A.6.10	Measurement Procedure in RRC\_IDLE	3281

A.6.10.1	RSTD Measurements	3281

A.6.10.1.1	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC\_IDLE state for non-RedCap UE	3281

A.6.10.1.1.1	Test purpose and environment	3281

A.6.10.1.1.2	Test requirements	3284

A.6.10.1.2	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC\_IDLE state with eDRX cycle &gt; 10.24s for non-RedCap UE	3285

A.6.10.1.2.1	Test Purpose and Environment	3285

A.6.10.1.2.2	Test Requirements	3288

A.6.10.1.3	NR RSTD measurement reporting delay test case for PRS aggregation in FR1 SA in RRC\_IDLE state	3288

A.6.10.1.3.1	Test purpose and environment	3288

A.6.10.1.3.2	Test requirements	3288

A.6.10.2	 PRS-RSRP Measurements	3289

A.6.10.2.1	PRS-RSRP reporting delay test case for single positioning frequency layer in RRC\_IDLE state for non-RedCap UE in FR1	3289

A.6.10.2.1.1	Test purpose and Environment	3289

A.6.10.2.1.2	Test Requirements	3291

A.6.10.2.2	PRS-RSRP reporting delay test case in RRC\_IDLE state in FR1 when eDRX cycle &gt; 10.24s	3292

A.6.10.2.2.1	Test purpose and Environment	3292

A.6.10.2.2.2	Test Requirements	3292

A.6.10.3	RSCPD Measurements	3292

A.6.10.3.1	DL RSCPD reported with RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC\_IDLE state	3292

A.6.10.3.1.1	Test Purpose and Environment	3292

A.6.10.3.1.2	Test Requirements	3293

A.6.11	Measurement Performance Requirements in RRC\_IDLE	3293

A.6.11.1	RSTD Measurements	3293

A.6.11.1.1	NR RSTD measurement accuracy test case for single positioning frequency layer in FR1 SA in RRC\_IDLE state for non-RedCap UE	3293

A.6.11.1.1.1	Test purpose and environment	3293

A.6.11.1.1.2	Test requirements	3295

A.6.11.1.2	RSTD measurement accuracy test case for single positioning frequency layer in FR1 in RRC\_IDLE state with eDRX&gt;10.24s for non-RedCap UE	3295

A.6.11.1.2.1	Test purpose and Environment	3295

A.6.11.1.2.2	Test Requirements	3297

A.6.11.1.3	NR RSTD measurement accuracy test case for PRS aggregation in FR1 SA in RRC\_IDLE state	3297

A.6.11.1.3.1	Test purpose and environment	3297

A.6.11.1.3.2	Test requirements	3297

A.6.11.2	PRS-RSRP measurements	3297

A.6.11.2.1	PRS-RSRP measurement accuracy test case for non-RedCap UE in FR1 in RRC\_IDLE state	3297

A.6.11.2.1.1	Test Purpose and Environment	3297

A.6.11.2.1.2	Test parameters	3298

A.6.11.2.1.3	Test Requirements	3300

A.6.11.2.2	PRS-RSRP measurement accuracy test case in RRC\_IDLE state in FR1 when eDRX cycle &gt; 10.24s	3300

A.6.11.2.2.1	Test purpose and Environment	3300

A.6.11.2.2.2	Test parameters	3300

A.6.11.2.2.3	Test Requirements	3301

A.6.11.3	RSCPD Measurements	3301

A.6.11.3.1	RSCPD with RSTD measurement accuracy in FR1 SA in RRC\_IDLE	3301

A.6.11.3.1.1	Test purpose and environment	3301

A.6.11.3.1.2	Test parameters	3301

A.6. 11.3.1.3	Test requirements	3304

A.7	NR standalone tests with one or more NR cells in FR2	3307

A.7.1	SA: RRC\_IDLE state mobility	3307

A.7.1.1	Cell re-selection to NR	3307

A.7.1.1.1	Cell reselection to FR2 intra-frequency NR case	3307

A.7.1.1.1.1	Test Purpose and Environment	3307

A.7.1.1.1.2	Test Parameters	3307

A.7.1.1.1.3	Test Requirements	3309

A.7.1.1.2	Cell reselection to FR2 inter-frequency NR case	3309

A.7.1.1.2.1	Test Purpose and Environment	3310

A.7.1.1.2.2	Test Parameters	3310

A.7.1.1.2.3	Test Requirements	3311

A.7.1.1.3	Cell reselection to FR2 intra-frequency NR case for UE fulfilling low mobility relaxed measurement criterion	3312

A.7.1.1.3.1	Test Purpose and Environment	3312

A.7.1.1.3.2	Test Parameters	3312

A.7.1.1.3.3	Test Requirements	3314

A.7.1.1.4	Cell reselection to FR2 intra-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion	3314

A.7.1.1.4.1	Test Purpose and Environment	3314

A.7.1.1.4.2	Test Parameters	3315

A.7.1.1.4.3	Test Requirements	3316

A.7.1.1.5	Cell reselection to FR2 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion	3317

A.7.1.1.5.1	Test Purpose and Environment	3317

A.7.1.1.5.2	Test Parameters	3317

A.7.1.1.5.3	Test Requirements	3319

A.7.1.1.6	Cell reselection to FR2 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion	3319

A.7.1.1.6.1	Test Purpose and Environment	3319

A.7.1.1.6.2	Test Parameters	3320

A.7.1.1.6.3	Test Requirements	3321

A.7.1.1.7	Cell reselection to FR2 intra-frequency NR case for FR2 power class 6 UE configured with *highSpeedMeasFlagFR2-r17* 3322

A.7.1.1.7.1	Test Purpose and Environment	3322

A.7.1.1.7.2	Test Parameters	3322

A.7.1.1.7.3	Test Requirements	3324

A.7.1.1.8	Cell reselection to FR2 inter-frequency NR case for UE configured with *highSpeedMeasFlagFR2-r17* 3325

A.7.1.1.8.1	Test Purpose and Environment	3325

A.7.1.1.8.2	Test Parameters	3325

A.7.1.1.8.3	Test Requirements	3327

A.7.2	SA: RRC\_INACTIVE state mobility	3327

A.7.2.1	Small Data Transmission	3327

A.7.2.1.1	TA validation for CG-SDT in FR2	3327

A.7.2.1.1.1	Test Purpose and Environment	3327

A.7.2.1.1.2	Test Requirements	3330

A.7.2.2	Cell reselection for positioning	3331

A.7.2.2.1	Cell reselection to FR2 intra-frequency NR case with RRC\_ INACTIVE eDRX and positioning SRS	3331

A.7.2.2.1.1	Test Purpose and Environment	3331

A.7.2.2.1.2	Test Parameters	3331

A.7.2.2.1.3	Test Requirements	3333

A.7.3	RRC\_CONNECTED state mobility	3333

A.7.3.1	Handover	3333

A.7.3.1.1	Inter-frequency handover from FR1 to FR2; unknown target cell	3333

A.7.3.1.1.1	Test Purpose and Environment	3333

A.7.3.1.1.2	Test Parameters	3333

A.7.3.1.1.3	Test Requirements	3335

A.7.3.1.2	Intra-frequency handover from FR2 to FR2; unknown target cell	3336

A.7.3.1.2.1	Test Purpose and Environment	3336

A.7.3.1.2.2	Test Parameters	3336

A.7.3.1.2.3	Test Requirements	3337

A.7.3.1.3	Inter-frequency handover from FR2 to FR2; unknown target cell	3337

A.7.3.1.3.1	Test Purpose and Environment	3337

A.7.3.1.3.2	Test Parameters	3337

A.7.3.1.3.3	Test Requirements	3339

A.7.3.1.4	Inter-band inter-frequency synchronous DAPS handover from FR1 to FR2	3339

A.7.3.1.4.1	Test Purpose and Environment	3339

A.7.3.1.4.2	Test Parameters	3339

A.7.3.1.4.3 Test Requirements	3342

A.7.3.1.5	Inter-band inter-frequency asynchronous DAPS handover from FR1 to FR2	3343

A.7.3.1.5.1	Test Purpose and Environment	3343

A.7.3.1.5.2	Test Parameters	3343

A.7.3.1.5.3 Test Requirements	3346

A.7.3.1.6	Handover with PSCell from SA to EN-DC with unknown FR2 target PScell	3347

A.7.3.1.6.1	Test Purpose and Environment	3347

A.7.3.1.6.2	Test Parameters	3347

A.7.3.1.6.3	Test Requirements	3352

A.7.3.1.7	HO with PSCell from FR1 NR-SA to EN-DC with known E-UTRA PCell and known FR2 PSCell	3352

A.7.3.1.7.1	Test purpose and environment	3352

A.7.3.1.7.2	Test Requirements	3356

A.7.3.1.8	NR PSCell change delay in HO with PSCell from NR-DC to NR-DC	3357

A.7.3.1.8.1	Test Purpose and Environment	3357

A.7.3.1.8.2	Test Requirements	3360

A.7.3.1.9	Intra-frequency handover from FR2-2 to FR2-2; unknown target cell	3360

A.7.3.1.9.1	Test Purpose and Environment	3360

A.7.3.1.9.2	Test Parameters	3360

A.7.3.1.9.3	Test Requirements	3362

A.7.3.1.10	Inter-frequency handover from FR2-2 to FR2-2; unknown target cell	3363

A.7.3.1.10.1	Test Purpose and Environment	3363

A.7.3.1.10.2	Test Parameters	3363

A.7.3.1.10.3	Test Requirements	3365

A.7.3.1.11	Inter-frequency handover from FR1 to FR2-2; unknown target cell	3365

A.7.3.1.11.1	Test Purpose and Environment	3365

A.7.3.1.11.2	Test Parameters	3365

A.7.3.1.11.3	Test Requirements	3367

A.7.3.1.12	Intra-frequency handover from FR2 to FR2; known target cell configured with NCD-SSB	3368

A.7.3.1.12.1	Test Purpose and Environment	3368

A.7.3.1.12.2	Test Parameters	3368

A.7.3.1.12.3	Test Requirements	3369

A.7.3.1.13	Inter-frequency handover from FR2 to FR2; known target cell configured with NCD-SSB	3370

A.7.3.1.13.1	Test Purpose and Environment	3370

A.7.3.1.13.2	Test Parameters	3370

A.7.3.1.13.3	Test Requirements	3372

A.7.3.1.14	Handover with PSCell from FR1-FR2 NR-DC to FR1-FR1 NR-DC with target PSCell in FR1	3372

A.7.3.1.14.1	Test Purpose and Environment	3372

A.7.3.1.14.2	Test Requirements	3376

A.7.3.1.15	HO with PSCell from FR1-FR1 NR-DC to FR1-FR2 NR-DC	3376

A.7.3.1.15.1	Test Purpose and Environment	3376

A.7.3.1.15.2	Test Requirements	3381

A.7.3.2	RRC Connection Mobility Control	3381

A.7.3.2.1	SA: RRC Re-establishment	3381

A.7.3.2.1.1	Intra-frequency RRC Re-establishment in FR2	3381

A.7.3.2.1.2	Inter-frequency RRC Re-establishment in FR2	3383

A.7.3.2.1.3	Intra-frequency RRC Re-establishment in FR2 without serving cell timing	3386

A.7.3.2.1.3.1	Test Purpose and Environment	3386

A.7.3.2.1.3.2	Test Requirements	3387

A.7.3.2.1.4	Intra-frequency RRC Re-establishment in FR2-2	3388

A.7.3.2.1.4.1	Test Purpose and Environment	3388

A.7.3.2.1.4.2	Test Requirements	3390

A.7.3.2.1.5	Inter-frequency RRC Re-establishment in FR2-2	3390

A.7.3.2.1.5.1	Test Purpose and Environment	3390

A.7.3.2.1.5.2	Test Requirements	3392

A.7.3.2.1.6	Intra-frequency RRC Re-establishment in FR2-2 without serving cell timing	3393

A.7.3.2.1.6.1	Test Purpose and Environment	3393

A.7.3.2.1.6.2	Test Requirements	3394

A.7.3.2.2	Random Access	3395

A.7.3.2.2.1	4-step RA type c ontention based random access test in FR2 for NR Standalone	3395

A.7.3.2.2.2	4-step RA type n on-contention based random access test in FR2 for NR Standalone	3398

A.7.3.2.2.3	2-step RA type contention based random access test in FR2 for NR Standalone	3401

A.7.3.2.2.4	2-step RA type n on-contention based random access test in FR2 for NR Standalone	3404

A.7.3.2.3	SA: RRC Connection Release with Redirection	3407

A.7.3.2.3.1	Redirection from NR in FR2 to NR in FR2	3407

A.7.3.2.4	LTM PDCCH-order Random Access	3409

A.7.3.2.4.1	PDCCH-order RACH on neighbor cell in FR2 when RACH BW is within active BWP	3409

A.7.3.2.4.2	PDCCH-order RACH on inter-frequency neighbor cell in FR2	3412

A.7.3.3	Conditional Handover	3415

A.7.3.3.1	Intra-frequency conditional handover from FR2 to FR2	3415

A.7.3.3.1.1	Test Purpose and Environment	3415

A.7.3.3.1.2	Test Parameters	3415

A.7.3.3.1.2.3	Test Requirements	3416

A.7.3.3.2	Inter-frequency conditional handover from FR2 to FR2; unknown target cell	3417

A.7.3.3.2.1	Test Purpose and Environment	3417

A.7.3.3.2.2	Test Parameters	3417

A.7.3.3.2.3Test Requirements	3418

A.7.3.3.3	NES triggering intra-frequency target CHO delay From FR2 to FR2	3418

A.7.3.3.3.1	Test Purpose and Environment	3418

A.7.3.3.3.2	Test Parameters	3419

A.7.3.3.3.2.3	Test Requirements	3420

A.7.3.3.4	NES triggering inter-frequency conditional handover from FR2 to FR1	3420

A.7.3.3.4.1	Test Purpose and Environment	3420

A.7.3.3.4.2	Test Parameters	3420

A.7.3.3.4.3	Test Requirements	3422

A.7.3.3.5	NR conditional handover including target MCG and target SCG from FR1-FR2 NR-DC to FR1-FR2 NR-DC	3423

A.7.3.3.5.1	Test Purpose and Environment	3423

A.7.3.3.5.2	Test Requirements	3426

A.7.3.3.5.2.1	Test Requirements for NR conditional handover	3426

A.7.3.3.5.2.2	Test Requirements for NR PSCell change	3426

A.7.3.3.6	NR conditional Handover including target MCG and candidate SCG from FR1-FR2 NR-DC to FR1-FR2 NR-DC	3426

A.7.3.3.6.1	Test Purpose and Environment	3426

A.7.3.3.6.2	Test Parameters	3426

A.7.3.3.6.3 Test Requirements	3430

A.7.3.4	LTM PCell Switch	3430

A.7.3.4.1	RACH based Intra-frequency PCell switch from FR2 to FR2	3430

A.7.3.4.1.1	Test Purpose and Environment	3430

A.7.3.4.1.2	Test Parameters	3430

A.7.3.4.1.3	Test Requirements	3433

A.7.3.4.2	RACH-less Intra-frequency PCell switch from FR2 to FR2	3434

A.7.3.4.2.1	Test Purpose and Environment	3434

A.7.3.4.2.2	Test Parameters	3434

A.7.3.4.2.3	Test Requirements	3438

A.7.3.4.3	RACH-based Inter-frequency LTM PCell switch from FR2 to FR2	3438

A.7.3.4.3.1	Test Purpose and Environment	3438

A.7.3.4.3.2	Test Parameters	3438

A.7.3.4.3.3	Test Requirements	3441

A.7.3.5	LTM PSCell Switch	3442

A.7.3.5.1	RACH-based Intra-frequency LTM PSCell switch from FR2 to FR2	3442

A.7.3.5.1.1	Test Purpose and Environment	3442

A.7.3.5.1.2	Test Parameters	3442

A.7.3.5.1.3	Test Requirements	3446

A.7.4	Timing	3447

A.7.4.1	UE transmit timing	3447

A.7.4.1.1	NR UE Transmit Timing Test for FR2	3447

A.7.4.1.1.1	Test Purpose and environment	3447

A.7.4.1.1.2	Test requirements	3449

A.7.4.1.2	NR UE Transmit Timing Test for FR2-2	3449

A.7.4.1.2.1	Test Purpose and environment	3450

A.7.4.1.2.2	Test requirements	3452

A.7.4.1.3	NR UE Transmit Timing Test with 2-TA for FR2 UE supporting *multiDCI-IntraCellMultiTRP-TwoTA-r18* 3452

A.7.4.1.3.1	Test Purpose and environment	3452

A.7.4.1.3.2	Test requirements	3456

A.7.4.2	UE timer accuracy	3456

A.7.4.3	Timing advance	3456

A.7.4.3.1	SA FR2 timing advance adjustment accuracy	3456

A.7.4.3.1.1	Test Purpose and Environment	3456

A.7.4.3.1.2	Test Parameters	3457

A.7.4.3.1.3 Test Requirements	3459

A.7.4.3.2	SA FR2-2 timing advance adjustment accuracy	3459

A.7.4.3.2.1	Test Purpose and Environment	3459

A.7.4.3.2.2	Test Parameters	3459

A.7.4.3.2.3	Test Requirements	3461

A.7.5	Signaling characteristics	3465

A.7.5.1	Radio link Monitoring	3465

A.7.5.1.1	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode	3465

A.7.5.1.1.1	Test Purpose and Environment	3465

A.7.5.1.1.2	Test Requirements	3468

A.7.5.1.2	Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode	3468

A.7.5.1.2.1	Test Purpose and Environment	3468

A.7.5.1.2.2	Test Requirements	3471

A.7.5.1.3	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode	3471

A.7.5.1.3.1	Test Purpose and Environment	3471

A.7.5.1.3.2	Test Requirements	3473

A.7.5.1.4	Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode	3474

A.7.5.1.4.1	Test Purpose and Environment	3474

A.7.5.1.4.2	Test Requirements	3476

A.7.5.1.5	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode	3476

A.7.5.1.5.1	Test Purpose and Environment	3476

A.7.5.1.5.2	Test Requirements	3479

A.7.5.1.6	Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode	3479

A.7.5.1.6.1	Test Purpose and Environment	3479

A.7.5.1.6.2	Test Requirements	3481

A.7.5.1.7	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode	3482

A.7.5.1.7.1	Test Purpose and Environment	3482

A.7.5.1.7.2	Test Requirements	3484

A.7.5.1.8	Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode	3484

A.7.5.1.8.1	Test Purpose and Environment	3484

A.7.5.1.8.2	Test Requirements	3487

A.7.5.1.9	UE Radio Link Monitoring Scheduling Restrictions on FR2	3488

A.7.5.1.9.1	Test Purpose and Environment	3488

A.7.5.1.9.2	Test Requirements	3489

A.7.5.1.10	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode for UE supporting fast beam sweeping in multi-Rx	3489

A.7.5.1.10.1	Test Purpose and Environment	3489

A.7.5.1.10.2	Test Requirements	3492

A.7.5.1.11	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode when CD-SSB is outside active BWP	3493

A.7.5.1.11.1	Test Purpose and Environment	3493

A.7.5.1.12	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode when CD-SSB is outside active BWP	3493

A.7.5.1.12.1	Test Purpose and Environment	3493

A.7.5.1.12.2	Test Requirements	3493

A.7.5.1.13	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode for UE supporting NCD-SSB based measurement outside active BWP	3493

A.7.5.1.13.1	Test Purpose and Environment	3493

A.7.5.1.13.2	Test Requirements	3496

A.7.5.2	Interruption	3496

A.7.5.2.1	Interruptions during measurements on deactivated NR SCC in FR2	3496

A.7.5.2.1.1	Test Purpose and Environment	3496

A.7.5.2.1.2	Test Requirements	3499

A.7.5.2.2	SA interruptions at NR SRS carrier-based switching	3499

A.7.5.2.2.1	Test Purpose and Environment	3499

A.7.5.2.2.2	Test Parameters	3499

A.7.5.2.2.3	Test Requirements	3501

A.7.5.3	SCell Activation and Deactivation Delay	3501

A.7.5.3.1	SCell Activation and deactivation for SCell in FR2 intra-band in non-DRX	3501

A.7.5.3.1.1	Test Purpose and Environment	3501

A.7.5.3.1.2	Test Requirements	3503

A.7.5.3.2	SCell Activation and deactivation for FR1+FR2 inter-band with target SCell in FR2	3503

A.7.5.3.2.1	Test Purpose and Environment	3503

A.7.5.3.2.2	Test Requirements	3505

A.7.5.3.3	SCell Activation and deactivation for SCell in FR2 inter-band in non-DRX	3506

A.7.5.3.3.1	Test Purpose and Environment	3506

A.7.5.3.3.2	Test Requirements	3508

A.7.5.3.4	Direct SCell activation at SCell addition of known SCell in FR2	3509

A.7.5.3.4.1	Test Purpose and Environment	3509

A.7.5.3.4.2	Test Requirements	3511

A.7.5.3.5	Direct SCell activation at handover with known SCell in FR2	3512

A.7.5.3.5.1	Test Purpose and Environment	3512

A.7.5.3.5.2	Test Requirements	3514

A.7.5.3.6	PUCCH SCell activation and deactivation for FR1+FR2 inter-band with target SCell in FR2 and known	3515

A.7.5.3.6.1	Test Purpose and Environment	3515

A.7.5.3.6.2	Test Requirements	3517

A.7.5.3.7	PUCCH SCell activation and deactivation delay requirements of FR2 unknown cell with FR1 PCell	3518

A.7.5.3.7.1	Test Purpose and Environment	3518

A.7.5.3.7.2	Test Requirements	3521

A.7.5.3.8	SCell Activation and deactivation for known PUCCH SCell in FR2 inter-band in non-DRX	3522

A.7.5.3.8.1	Test Purpose and Environment	3522

A.7.5.3.8.2	Test Requirements	3525

A.7.5.3.9	PUCCH SCell Activation and deactivation of unknown SCell in FR2	3526

A.7.5.3.9.1	Test Purpose and Environment	3526

A.7.5.3.9.2	Test Requirements	3528

A.7.5.3.10	SCell Activation and deactivation of FR2 known PUCCH SCell and one FR2 unknown SCell with FR2 PCell	3529

A.7.5.3.10.1	Test Purpose and Environment	3529

A.7.5.3.10.2	Test Requirements	3532

A.7.5.3.11	PUCCH SCell activation and deactivation delay requirements of FR2 unknown cell with FR2 PCell	3533

A.7.5.3.11.1	PUCCH SCell activation with non-PUCCH SCell in a secondary PUCCH Group	3533

A.7.5.3.11.1.1	Test Purpose and Environment	3533

A.7.5.3.11.1.2	Test Requirements	3536

A.7.5.3.11.2	PUCCH SCell activation with non-PUCCH SCell in a primary PUCCH Group	3537

A.7.5.3.11.2.1	Test Purpose and Environment	3537

A.7.5.3.11.2.2	Test Requirements	3540

A.7.5.3.12	Void	3541

A.7.5.3.13	SCell Activation for SCell in FR2 intra-band in non-DRX	3541

A.7.5.3.13.1	Test Purpose and Environment	3541

A.7.5.3.13.2	Test Requirements	3543

A.7.5.3.14	SCell Activation for known SCell in FR2 inter-band	3543

A.7.5.3.14.1	Test Purpose and Environment	3543

A.7.5.3.14.2	Test Requirements	3545

A.7.5.3.15	PUCCH SCell activation and deactivation with FR1 PCell based on L3 reporting after SCell activation command	3546

A.7.5.3.15.1	Test Purpose and Environment	3546

A.7.5.3.15.2	Test Requirements	3550

A.7.5.3.16	PUCCH SCell activation and deactivation with FR2 PCell based on L3 reporting after SCell activation command	3550

A.7.5.3.16.1	Test Purpose and Environment	3550

A.7.5.3.16.2	Test Requirements	3553

A.7.5.3.17	SCell Activation and deactivation for SCell in FR2 inter-band in DRX for UE capable of small beam sweeping factors and/or short measurement interval	3554

A.7.5.3.17.1	Test Purpose and Environment	3554

A.7.5.3.17.2	Test Requirements	3556

A.7.5.3.18	SCell Activation and deactivation for FR1+FR2 inter-band with target SCell in FR2, in DRX, for UE capable of small beam sweeping factors and/or short measurement interval	3558

A.7.5.3.18.1	Test Purpose and Environment	3558

A.7.5.3.18.2	Test Requirements	3561

A.7.5.3.19	SCell Activation and deactivation of FR2 unknown SCell with FR1 PCell in non-DRX with L3 reporting during activation	3563

A.7.5.3.19.1	Test Purpose and Environment	3563

A.7.5.3.19.2	Test Requirements	3566

A.7.5.3.20	SCell Activation and Deactivation of FR2 unkown SCell with FR2 PCell in non-DRX with L3 reporting during activation	3566

A.7.5.3.20.1	Test Purpose and Environment	3567

A.7.5.3.20.2	Test Requirements	3569

A.7.5.4	Void	3570

A.7.5.5	Beam Failure Detection and Link recovery procedures	3570

A.7.5.5.1	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode	3570

A.7.5.5.1.1	Test Purpose and Environment	3570

A.7.5.5.1.2	Test Requirements	3573

A.7.5.5.2	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in DRX mode	3574

A.7.5.5.2.1	Test Purpose and Environment	3574

A.7.5.5.2.2	Test Requirements	3577

A.7.5.5.3	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode	3577

A.7.5.5.3.1	Test Purpose and Environment	3577

A.7.5.5.3.2	Test Requirements	3580

A.7.5.5.4	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode	3580

A.7.5.5.4.1	Test Purpose and Environment	3580

A.7.5.5.4.2	Test Requirements	3583

A.7.5.5.5	Scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode	3584

A.7.5.5.5.1	Test Purpose and Environment	3584

A.7.5.5.5.2	Test Requirements	3587

A.7.5.5.6	Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in non-DRX mode	3587

A.7.5.5.6.1	Test Purpose and Environment	3587

A.7.5.5.6.2	Test Requirements	3590

A.7.5.5.7	Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in DRX mode	3590

A.7.5.5.7.1	Test Purpose and Environment	3590

A.7.5.5.7.2	Test Requirements	3593

A.7.5.5.8	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode for UE fulfilling relaxed measurement criterion	3594

A.7.5.5.8.1	Test Purpose and Environment	3594

A.7.5.5.8.2	Test Requirements	3597

A.7.5.5.9	TRP specific Beam Failure Detection and Link Recovery Test for FR2 SCell configured with CSI-RS-based BFD and LR in DRX mode	3597

A.7.5.5.9.1	Test Purpose and Environment	3597

A.7.5.5.9.2	Test Requirements	3600

A.7.5.5.10	TRP specific Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode	3601

A.7.5.5.10.1	Test Purpose and Environment	3601

A.7.5.5.10.2	Test Requirements	3604

A.7.5.5.11	Beam Failure Detection and Link Recovery Test for FR2-2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode	3604

A.7.5.5.11.1	Test Purpose and Environment	3604

A.7.5.5.11.2	Test Requirements	3607

A.7.5.5.12	Beam Failure Detection and Link Recovery Test for FR2-2 PCell configured with CSI-RS-based BFD and LR in DRX mode	3607

A.7.5.5.12.1	Test Purpose and Environment	3607

A.7.5.5.12.2	Test Requirements	3610

A.7.5.5.13	Scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2-2 PCell configured with SSB-based BFD and LR in non-DRX mode	3611

A.7.5.5.13.1	Test Purpose and Environment	3611

A.7.5.5.13.2	Test Requirements	3613

A.7.5.5.14	TRP specific Beam Failure Detection and Link Recovery for FR2 PCell configured with CSI-RS-based BFD and LR and multi-Rx operation in DRX mode	3613

A.7.5.5.14.1	Test Purpose and Environment	3613

A.7.5.5.14.2	Test Requirements	3617

A.7.5.6	Active BWP switch	3617

A.7.5.6.1	DCI-based and Timer-based Active BWP Switch	3617

A.7.5.6.1.1	NR FR2- NR FR2 DL active BWP switch of SCell with non-DRX in SA	3617

A.7.5.6.1.2	NR FR1- NR FR2 DL active BWP switch of SCell with non-DRX in SA	3621

A.7.5.6.1.3	NR FR2 DL active BWP switch with non-DRX in SA	3625

A.7.5.6.1.3.1	Test Purpose and Environment	3625

A.7.5.6.1.3.2	Test Requirements	3627

A.7.5.6.1.4	NR FR2-2- NR FR2-2 DL active BWP switch of SCell with non-DRX in SA	3627

A.7.5.6.1.4.1	Test Purpose and Environment	3627

A.7.5.6.1.4.2	Test Requirements	3630

A.7.5.6.2	RRC-based Active BWP Switch	3631

A.7.5.6.2.1.1	Test Purpose and Environment	3631

A.7.5.6.2.1.2	Test Requirements	3634

A.7.5.6.2.2	NR FR2-2 DL active BWP switch of PCell with non-DRX in SA	3634

A.7.5.6.2.2.1	Test Purpose and Environment	3634

A.7.5.6.2.2.2	Test Requirements	3636

A.7.5.6.3	Simultaneous DCI-based and Timer-based Active BWP Switch on multiple CCs	3637

A.7.5.6.3.1.1	Test Purpose and Environment	3637

A.7.5.6.3.1.2	Test Requirements	3639

A.7.5.6.4	SCell dormancy switch	3640

A.7.5.6.4.1	NR FR2 PCell SCell dormancy switch of single FR2 SCell inside active time	3640

A.7.5.6.4.1.1	Test Purpose and Environment	3640

A.7.5.6.4.1.2	Test Requirements	3642

A.7.5.6.4.2	NR FR1 PCell SCell dormancy switch of two FR2 SCells outside active time	3643

A.7.5.6.4.2.1	 Test Purpose and Environment	3643

A.7.5.6.4.2.2	 Test Requirements	3646

A.7.5.6.5	Simultaneous RRC-based Active BWP Switch on multiple CCs	3646

A.7.5.6.5.1	Active BWP switch on multiple SCells with non-DRX in SA	3646

A.7.5.6.5.2	NR FR2-2 Active BWP switch on multiple SCells with non-DRX in SA	3648

A.7.5.6.5.2.1	Test Purpose and Environment	3648

A.7.5.6.5.2.2	Test Requirements	3651

A.7.5.7	PSCell addition and release delay	3651

A.7.5.7.1	Addition and Release Delay of known NR PSCell	3651

A.7.5.7.1.1	Test Purpose and Environment	3651

A.7.5.7.1.2	Test Requirements	3654

A.7.5.7.2	Addition and Release Delay of unknown NR PSCell in	3654

A.7.5.7.2.1	Test Purpose and Environment	3654

A.7.5.7.2.2	Test Requirements	3656

A.7.5.7.3	Addition and Release Delay of known NR PSCell in FR2-2	3656

A.7.5.7.3.1	Test Purpose and Environment	3656

A.7.5.7.3.2	Test Requirements	3659

A.7.5.7.4	Addition and Release Delay of unknown NR PSCell in FR2-2	3659

A.7.5.7.4.1	Test Purpose and Environment	3659

A.7.5.7.4.2	Test Requirements	3661

A.7.5.8	Active TCI state switch delay	3662

A.7.5.8.1	MAC-CE based active TCI state switch	3662

A.7.5.8.2	RRC based active TCI state switch	3665

A.7.5.8.3	MAC-CE based active TCI state switch for HST FR2 scenario	3668

A.7.5.8.3.1	NR PCell FR2 HST active TCI state switch for a known TCI state	3668

A.7.5.8.3.1.1	Test Purpose and Environment	3668

A.7.5.8.3.1.2	Test Requirements	3671

A.7.5.8.3.2	NR PCell FR2 HST active TCI state switch for PC6 UE supporting *tci-StateSwitchInd-r18* for a known TCI state	3672

A.7.5.8.3.2.1	Test Purpose and Environment	3672

A.7.5.8.3.2.2	Test Requirements	3675

A.7.5.8.4	DCI based active TCI state switch with m-DCI for simultaneous reception	3675

A.7.5.8.4.1	Test Purpose and Environment	3675

A.7.5.8.4.2	Test Requirements	3678

A.7.5.8.5	Single-DCI FR2 DCI based active TCI state switch with known target TCI states for simultaneous reception	3678

A.7.5.8.5.1	Test Purpose and Environment	3678

A.7.5.8.5.1.2	Test Requirements	3680

A.7.5.9	Uplink spatial relation switch delay	3681

A.7.5.9.1.1.1	Test Purpose and Environment	3681

A.7.5.9.1.1.2	Test Requirements	3683

A.7.5.9.2	RRC based spatial relation switch	3683

A.7.5.9.2.1	NR PCell FR2 spatial relation switch associated with a known DL-RS	3683

A.7.5.9.2.1.1	Test Purpose and Environment	3683

A.7.5.9.2.1.2	Test Requirements	3685

A.7.5.10	UE specific CBW change	3685

A.7.5.10.1	NR FR2 UE specific CBW change of PCell with non-DRX in SA	3685

A.7.5.10.1.1	Test Purpose and Environment	3685

A.7.5.10.1.2	Test Requirements	3687

A.7.5.11	UE UL carrier RRC reconfiguration Delay	3688

A.7.5.11.1	UE UL carrier RRC reconfiguration Delay	3688

A.7.5.11.1.1	Test Purpose and Environment	3688

A.7.5.11.1.2	Test Requirements	3690

A.7.5.12	Conditional PSCell addition and release delay (FR2 SA)	3690

A.7.5.12.1	Addition and Release Delay of PSCell	3690

A.7.5.12.1.1	Test purpose and environment	3690

A.7.5.12.1.2	Test Parameters	3690

A.7.5.12.1.3	Test Requirements	3692

A.7.5.13	Unified TCI state switching delay	3692

A.7.5.13.1	MAC-CE based active joint TCI state switching	3692

A.7.5.13.1.1	NR PCell FR2 active joint TCI state switch for a known TCI state	3692

A.7.5.13.1.1.1	Test Purpose and Environment	3692

A.7.5.13.1.1.2	Test parameters	3693

A.7.5.13.1.1.3	Test Requirements	3694

A.7.5.13.2	 MAC-CE based active uplink TCI state switch	3695

A.7.5.13.2.1	 NR FR2 PCell uplink TCI state switch for a known TCI state	3695

A.7.5.13.2.1.1	Test Purpose and Environment	3695

A.7.5.13.2.1.2	Test parameters	3695

A.7.5.13.2.1.3	Test Requirements	3697

A.7.5.13.3	MAC-CE based active downlink TCI state switch	3697

A.7.5.13.3.1	NR PCell FR2 active downlink TCI state switch to cell with additional PCI for a known TCI state	3697

A.7.5.13.3.1.1	Test Purpose and Environment	3697

A.7.5.13.3.1.2	Test Parameters	3697

A.7.5.13.3.1.3	Test Requirements	3700

A.7.5.13.4	sDCI MAC-CE based joint TCI state switching	3701

A.7.5.13.4.1	NR PCell FR2 dual downlink and uplink TCI state switch in sDCI for known case	3701

A.7.5.13.4.1.1	Test Purpose and Environment	3701

A.7.5.13.4.1.2	Test parameters	3701

A.7.5.13.4.1.3	Test Requirements	3703

A.7.5.13.5	MAC-CE based dual downlink TCI state switching delay for unified TCI for single-DCI mTRP	3703

A.7.5.13.5.1	NR PCell FR2 dual downlink TCI state switch in sDCI for known case	3703

A.7.5.13.5.1.1	Test Purpose and Environment	3703

A.7.5.13.5.1.2	Test Parameters	3704

A.7.5.13.5.1.3	Test Requirements	3706

A.7.5.13.6	 MAC-CE based active uplink TCI state switch for single-DCI mTRP	3706

A.7.5.13.6.1	 NR FR2 PCell uplink TCI state switch for two known TCI states	3706

A.7.5.13.6.1.1	Test Purpose and Environment	3706

A.7.5.13.6.1.2	Test parameters	3707

A.7.5.13.6.1.3	Test Requirements	3708

A.7.5.14	PSCell RACH-less based Activation and deactivation for FR1+FR2 inter-band with target PSCell in FR2	3709

A.7.5.14.1	Test Purpose and Environment	3709

A.7.5.14.2	Test Requirements	3711

A.7.5.15	Void	3712

A.7.5.16	UE L1-RSRP Scheduling and Measurement Restrictions on FR2-1	3712

A.7.5.16.1	Test Purpose and Environment	3712

A.7.5.16.2	Test Requirements	3714

A.7.5.17	SCG Activation and deactivation for FR1+FR1 inter-band with target PSCell in FR1	3715

A.7.5.17.1	Test Purpose and Environment	3715

A.7.5.17.2	Test Requirements	3717

A.7.5.18	Subsequent conditional PSCell addition/change	3718

A.7.5.18.1	Intra-frequency subsequent CPC from FR1-FR2 NR-DC to FR1-FR2 NR-DC	3718

A.7.5.18.1.1	Test purpose and environment	3718

A.7.5.18.1.2	Test Requirements	3721

A.7.5.18.2	Inter-frequency subsequent CPA from FR1-FR2 NR-DC to FR1-FR2 NR-DC	3721

A.7.5.18.2.1	Test Purpose and Environment	3721

A.7.5.18.2.2	Test Requirements	3724

A.7.6	Measurement procedure	3727

A.7.6.1	Intra-frequency Measurements	3727

A.7.6.1.1	SA event triggered reporting test without gap under non-DRX	3727

A.7.6.1.1.1	Test purpose and Environment	3727

A.7.6.1.1.2	Test Requirements	3729

A.7.6.1.2	SA event triggered reporting test without gap under DRX	3729

A.7.6.1.2.1	Test purpose and Environment	3729

A.7.6.1.2.2	Test Requirements	3731

A.7.6.1.3	SA event triggered reporting test with per-UE gaps under non-DRX	3731

A.7.6.1.3.1	Test purpose and Environment	3731

A.7.6.1.3.2	Test Requirements	3734

A.7.6.1.4	SA event triggered reporting test with per-UE gaps under DRX	3734

A.7.6.1.4.1	Test purpose and Environment	3734

A.7.6.1.4.2	Test Requirements	3736

A.7.6.1.5	SA event triggered reporting test without gap under non-DRX for UE configured with *highSpeedMeasFlagFR2-r17* 3737

A.7.6.1.5.1	Test purpose and Environment	3737

A.7.6.1.5.2	Test Requirements	3739

A.7.6.1.6	SA event triggered reporting test without gap under non-DRX for FR2-2	3739

A.7.6.1.6.1	Test purpose and Environment	3739

A.7.6.1.6.2	Test Requirements	3741

A.7.6.1.7	SA event triggered reporting test without gap under DRX for FR2-2	3742

A.7.6.1.7.1	Test purpose and Environment	3742

A.7.6.1.7.2	Test Requirements	3744

A.7.6.1.8	SA event triggered reporting test with per-UE gaps under non-DRX for FR2-2	3745

A.7.6.1.8.1	Test purpose and Environment	3745

A.7.6.1.8.2	Test Requirements	3747

A.7.6.1.9	SA event triggered reporting test with per-UE gaps under DRX for FR2-2	3748

A.7.6.1.9.1	Test purpose and Environment	3748

A.7.6.1.9.2	Test Requirements	3750

A.7.6.1.10	SA event triggered reporting test with SSB time index detection without gap under non-DRX for FR2-2	3751

A.7.6.1.10.1	Test purpose and Environment	3751

A.7.6.1.10.2	Test Requirements	3753

A.7.6.1.11	SA event triggered reporting test with SSB time index detection with per-UE gaps under non-DRX for FR2-2	3753

A.7.6.1.11.1	Test purpose and Environment	3753

A.7.6.1.11.2	Test Requirements	3755

A.7.6.1.12	SA event triggered reporting test without gap under non-DRX when CD-SSB is outside active BWP	3756

A.7.6.1.12.1	Test purpose and Environment	3756

A.7.6.1.12.2	Test Requirements	3756

A.7.6.1.13	SA event triggered reporting test without gap under non-DRX with NCD-SSB	3756

A.7.6.1.13.1	Test purpose and Environment	3756

A.7.6.1.13.2	Test Requirements	3758

A.7.6.1.14	SA event triggered reporting test without gap under non-DRX for power class 6 UE supporting measEnhCAInterFreqFR2-r18	3759

A.7.6.1.14.1	Test Purpose and Environment	3759

A.7.6.1.14.2	Test Requirements	3760

A.7.6.2	Inter-frequency Measurements	3760

A.7.6.2.1	SA event triggered reporting tests for FR2 without SSB time index detection when DRX is not used (PCell in FR2)	3760

A.7.6.2.1.1	Test Purpose and Environment	3760

A.7.6.2.1.2	Test Requirements	3762

A.7.6.2.2	SA event triggered reporting tests for FR2 without SSB time index detection when DRX is used (PCell in FR2)	3763

A.7.6.2.2.1	Test Purpose and Environment	3763

A.7.6.2.2.2	Test Requirements	3765

A.7.6.2.3	SA event triggered reporting tests for FR2 with SSB time index detection when DRX is not used (PCell in FR2)	3765

A.7.6.2.3.1	Test Purpose and Environment	3765

A.7.6.2.3.2	Test Requirements	3767

A.7.6.2.4	SA event triggered reporting tests for FR2 with SSB time index detection when DRX is used (PCell in FR2)	3768

A.7.6.2.4.1	Test Purpose and Environment	3768

A.7.6.2.4.2	Test Requirements	3770

A.7.6.2.5	SA event triggered reporting tests for FR2 without SSB time index detection when DRX is not used (PCell in FR1)	3770

A.7.6.2.5.1	Test Purpose and Environment	3770

A.7.6.2.5.2	Test Requirements	3773

A.7.6.2.6	SA event triggered reporting tests for FR2 without SSB time index detection when DRX is used (PCell in FR1)	3773

A.7.6.2.6.1	Test Purpose and Environment	3773

A.7.6.2.6.2	Test Requirements	3776

A.7.6.2.7	SA event triggered reporting tests for FR2 with SSB time index detection when DRX is not used (PCell in FR1)	3776

A.7.6.2.7.1	Test Purpose and Environment	3776

A.7.6.2.7.2	Test Requirements	3779

A.7.6.2.8	SA event triggered reporting tests for FR2 with SSB time index detection when DRX is used (PCell in FR1)	3779

A.7.6.2.8.1	Test Purpose and Environment	3779

A.7.6.2.8.2	Test Requirements	3782

A.7.6.2.9	SA event triggered reporting tests For FR2 without SSB time index detection when DRX is not used (PCell in FR2) (rel16 additional mandatory gap pattern 17)	3782

A.7.6.2.9.1	Test Purpose and Environment	3782

A.7.6.2.9.2	Test Requirements	3784

A.7.6.2.10	SA event triggered reporting test without gap under non-DRX	3785

A.7.6.2.10.1	Test Purpose and Environment	3785

A.7.6.2.10.2	Test Requirements	3786

A.7.6.2.11	SA event triggered reporting test without gap under DRX	3786

A.7.6.2.11.1	Test Purpose and Environment	3787

A.7.6.2.11.2	Test Requirements	3788

A.7.6.2.12	SA event triggered reporting tests for FR2-2 without SSB time index detection when DRX is not used (PCell in FR2-2)	3789

A.7.6.2.12.1	Test Purpose and Environment	3789

A.7.6.2.12.2	Test Requirements	3791

A.7.6.2.13	SA event triggered reporting tests for FR2-2 without SSB time index detection when DRX is used (PCell in FR2-2)	3791

A.7.6.2.13.1	Test Purpose and Environment	3791

A.7.6.2.13.2	Test Requirements	3794

A.7.6.2.14	SA event triggered reporting tests for FR2-2 with SSB time index detection when DRX is not used (PCell in FR2-2)	3795

A.7.6.2.14.1	Test Purpose and Environment	3795

A.7.6.2.14.2	Test Requirements	3797

A.7.6.2.15	SA event triggered reporting tests for FR2-2 with SSB time index detection when DRX is used (PCell in FR2-2)	3798

A.7.6.2.15.1	Test Purpose and Environment	3798

A.7.6.2.15.2	Test Requirements	3800

A.7.6.2.16	SA event triggered reporting tests for FR2-2 without SSB time index detection when DRX is not used (PCell in FR1)	3801

A.7.6.2.16.1	Test Purpose and Environment	3801

A.7.6.2.16.2	Test Requirements	3805

A.7.6.2.17	SA event triggered reporting tests for FR2-2 without SSB time index detection when DRX is used (PCell in FR1)	3805

A.7.6.2.17.1	Test Purpose and Environment	3805

A.7.6.2.17.2	Test Requirements	3809

A.7.6.2.18	SA event triggered reporting tests for FR2-2 with SSB time index detection when DRX is not used (PCell in FR1)	3810

A.7.6.2.18.1	Test Purpose and Environment	3810

A.7.6.2.18.2	Test Requirements	3813

A.7.6.2.19	SA event triggered reporting tests for FR2-2 with SSB time index detection when DRX is used (PCell in FR1)	3814

A.7.6.2.19.1	Test Purpose and Environment	3814

A.7.6.2.19.2	Test Requirements	3818

A.7.6.2.20	SA event triggered reporting tests for FR2 with measurement gap with priority and two periodic MUSIM gaps configured	3819

A.7.6.2.20.1	Test Purpose and Environment	3819

A.7.6.2.20.2	Test Requirements	3821

A.7.6.2.21	SA event triggered reporting tests for FR2 with measurement gap without priority and periodic MUSIM gap configured	3821

A.7.6.2.21.1	Test Purpose and Environment	3821

A.7.6.2.21.2	Test Requirements	3823

A.7.6.2.22	SA event triggered reporting tests with SSB time index detection when DRX is not used (PCell in FR2) for FR2 power class 6 UE configured with *highSpeedMeasFlagFR2-r17* 3824

A.7.6.2.22.1	Test Purpose and Environment	3824

A.7.6.2.22.2	Test Requirements	3826

A.7.6.2.23	SA event triggered reporting tests without SSB time index detection when DRX is not used (PCell in FR2) for FR2 power class 6 UE configured with *highSpeedMeasFlagFR2-r17* 3826

A.7.6.2.23.1	Test Purpose and Environment	3826

A.7.6.2.23.2	Test Requirements	3828

A.7.6.3	L1-RSRP measurement for beam reporting	3828

A.7.6.3.1	SSB based L1-RSRP measurement when DRX is not used	3828

A.7.6.3.1.1	Test Purpose and Environment	3828

A.7.6.3.1.2	Test parameters	3828

A.7.6.3.1.3	Test Requirements	3830

A.7.6.3.2	SSB based L1-RSRP measurement when DRX is used	3830

A.7.6.3.2.1	Test Purpose and Environment	3830

A.7.6.3.2.2	Test parameters	3830

A.7.6.3.2.3	Test Requirements	3831

A.7.6.3.3	CSI-RS based L1-RSRP measurement when DRX is not used	3832

A.7.6.3.3.1	Test Purpose and Environment	3832

A.7.6.3.3.2	Test parameters	3832

A.7.6.3.3.3	Test Requirements	3833

A.7.6.3.4	CSI-RS based L1-RSRP measurement when DRX is used	3833

A.7.6.3.4.1	Test Purpose and Environment	3833

A.7.6.3.4.2	Test parameters	3834

A.7.6.3.3.3	Test Requirements	3835

A.7.6.3.5	SSB based L1-RSRP measurement when DRX is used for power class 6 UE configured with *highSpeedMeasFlagFR2-r17* 3835

A.7.6.3.5.1	Test Purpose and Environment	3835

A.7.6.3.5.2	Test parameters	3836

A.7.6.3.5.3	Test Requirements	3837

A.7.6.3.6	Inter-cell SSB based L1-RSRP measurements on FR2 SCell when DRX is not used	3837

A.7.6.3.6.1	Test Purpose and Environment	3837

A.7.6.3.6.2	Test parameters	3838

A.7.6.3.6.3	Test Requirements	3840

A.7.6.3.7	SSB based L1-RSRP measurement for FR2-2 when DRX is used	3840

A.7.6.3.7.1	Test Purpose and Environment	3840

A.7.6.3.7.2	Test parameters	3841

A.7.6.3.7.3	Test Requirements	3842

A.7.6.3.8	CSI-RS based L1-RSRP measurement when DRX is not used and when CD-SSB is outside active BWP	3842

A.7.6.3.8.1	Test Purpose and Environment	3842

A.7.6.3.9	SSB based L1-RSRP measurement when DRX is not used when CD-SSB is outside active BWP	3843

A.7.6.3.9.1	Test Purpose and Environment	3843

A.7.6.3.9.2	Test Requirements	3843

A.7.6.3.10	SSB based L1-RSRP measurement for UE supporting NCD-SSB based L1 measurement outside active BWP when DRX is not used	3843

A.7.6.3.10.1	Test Purpose and Environment	3843

A.7.6.3.10.2	Test parameters	3843

A.7.6.3.10.3	Test Requirements	3845

A.7.6.3.11	SSB based L1-RSRP measurement when DRX is used for power class 6 UE supporting simultaneousReceptionTwoQCL-r18	3845

A.7.6.3.11.1	Test Purpose and Environment	3845

A.7.6.3.11.2	Test parameters	3845

A.7.6.3.11.3	Test Requirements	3847

A.7.6.4	CLI measurements	3847

A.7.6.4.1	SRS-RSRP measurement with non-DRX	3847

A.7.6.4.1.1	Test Purpose and Environment	3847

A.7.6.4.1.2	Test Parameters	3847

A.7.6.4.1.3	Test Requirements	3849

A.7.6.4.2	CLI-RSSI measurement with non-DRX	3849

A.7.6.4.2.1	Test Purpose and Environment	3849

A.7.6.4.2.2	Test Parameters	3850

A.7.6.4.2.3	Test Requirements	3851

A.7.6.5.1	SA interfrequency CGI reporting in autonomous gaps test (PCell in FR2)	3851

A.7.6.5.1.1	Test Purpose and Environment	3851

A.7.6.5.1.2	Test Requirements	3854

A.7.6.6	L1-SINR measurement for beam reporting	3854

A.7.6.6.2	L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is used	3856

A.7.6.6.2.1	Test Purpose and Environment	3856

A.7.6.6.2.2	Test parameters	3856

A.7.6.6.2.3	Test Requirements	3857

A.7.6.6.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is used	3858

A.7.6.6.3.1	Test Purpose and Environment	3858

A.7.6.6.3.2	Test parameters	3858

A.7.6.6.3.3	Test Requirements	3859

A.7.6.7	CSI-RS based intra-frequency Measurements	3860

A.7.6.7.1	SA event triggered reporting test without gap under DRX for CSI-RS based intra-frequency measurement	3860

A.7.6.7.1.1	Test purpose and Environment	3860

A.7.6.7.1.2	Test Requirements	3861

A.7.6.8	CSI-RS based inter-frequency Measurements	3862

A.7.6.8.1	SA event triggered reporting tests for FR2 CSI-RS based measurement when non-DRX is used (PCell in FR2)	3862

A.7.6.8.1.1	Test Purpose and Environment	3862

A.7.6.8.1.2	Test Requirements	3864

A.7.6.9	RSTD measurements	3864

A.7.6.9.1	 NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA	3864

A.7.6.9.1.1	Test Purpose and Environment	3864

A.7.6.9.1.2	Test Requirements	3868

A.7.6.9.2	 NR RSTD measurement reporting delay test case for dual positioning frequency layers in FR2 SA	3868

A.7.6.9.2.1	Test Purpose and Environment	3868

A.7.6.9.2.2	Test Requirements	3871

A.7.6.9.3	NR RSTD measurement reporting delay test case for single positioning frequency layer with reduced number of samples in FR2 SA	3872

A.7.6.9.3.1	Test Purpose and Environment	3872

A.7.6.9.3.2	Test Requirements	3874

A.7.6.9.4	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA without measurement gap	3875

A.7.6.9.4.1	Test Purpose and Environment	3875

A.7.6.9.4.2	Test Requirements	3877

A.7.6.9.5	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC\_CONNECTED state with Rx TEG	3878

A.7.6.9.5.1	Test Purpose and Environment	3878

A.7.6.9.5.2	Test Requirements	3881

A.7.6.9.6	NR RSTD measurement reporting delay test case for PRS aggregation in FR2 SA in RRC\_CONNECTED mode	3881

A.7.6.9.6.1	Test Purpose and Environment	3881

A.7.6.9.6.2	Test Requirements	3889

A.7.6.10 PRS-RSRP measurements	3889

A.7.6.10.1 PRS-RSRP reporting delay test case for single positioning frequency layer	3889

A.7.6.10.1.1	Test Purpose and Environment	3889

A.7.6.10.1.2	Test Requirements	3891

A.7.6.10.2	PRS-RSRP reporting delay test case for dual positioning frequency layer	3892

A.7.6.10.2.1	Test Purpose and Environment	3892

A.7.6.10.2.2	Test Requirements	3894

A.7.6.10.3	PRS-RSRP reporting delay test case for reduced number of samples	3894

A.7.6.10.3.1	Test Purpose and Environment	3894

A.7.6.10.3.2	Test Requirements	3896

A.7.6.10.4	PRS-RSRP reporting delay test case for single positioning frequency layer outside MG	3897

A.7.6.10.4.1	Test Purpose and Environment	3897

A.7.6.10.4.2	Test Requirements	3899

A.7.6.11	UE Rx-Tx time difference measurements	3899

A.7.6.11.1	UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA	3899

A.7.6.11.1.1	Test purpose and environment	3899

A.7.6.11.1.2	Test requirements	3901

A.7.6.11.2	UE Rx-Tx time difference measurement period for dual positioning frequency layers in FR2 SA	3901

A.7.6.11.2.1	Test purpose and environment	3901

A.7.6.11.2.2	Test requirements	3903

A.7.6.11.3	UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA with reduced sample number	3904

A.7.6.11.3.1	Test purpose and environment	3904

A.7.6.11.3.2	Test requirements	3905

A.7.6.11.4	UE Rx-Tx time difference measurements without gaps in FR2 SA	3906

A.7.6.11.4.1	Test purpose and environment	3906

A.7.6.11.4.2	Test requirements	3907

A.7.6.11.5	UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA with RxTx TEG	3908

A.7.6.11.5.1	Test purpose and environment	3908

A.7.6.11.5.2	Test requirements	3909

A.7.6.11.6	UE Rx-Tx time difference measurements with PRS bandwidth aggregation in FR2 SA	3910

A.7.6.11.6.1	Test purpose and environment	3910

A.7.6.11.6.2	Test requirements	3913

A.7.6.12	PRS-RSRPP measurements	3913

A.7.6.12.1 PRS-RSRPP reporting delay test case for single positioning frequency layer in FR2 in RRC\_CONNECTED state	3913

A.7.6.12.1.1	Test Purpose and Environment	3913

A.7.6.12.1.2	Test Requirements	3916

A.7.6.12.2	PRS-RSRPP reporting delay test case for reduced number of samples for single positioning frequency layer in FR2 in RRC\_CONNECTED state	3916

A.7.6.12.2.1	Test Purpose and Environment	3916

A.7.6.12.2.2	Test Requirements	3918

A.7.6.12.3	PRS-RSRPP reporting delay test case for gapless measurement in FR2	3918

A.7.6.12.3.1	Test Purpose and Environment	3918

A.7.6.12.3.2	Test Requirements	3921

A.7.6.13	UE Rx-Tx time difference measurements for PDC	3921

A.7.6.13.1	UE Rx-Tx time difference measurement for propagation delay compensation using PRS in FR2	3921

A.7.6.13.1.1	Test purpose and environment	3921

A.7.6.13.1.2	Test requirements	3922

A.7.6.13.2	UE Rx-Tx time difference measurement for propagation delay compensation using TRS in FR2	3923

A.7.6.13.2.1	Test purpose and environment	3923

A.7.6.13.2.2	Test requirements	3924

A.7.6.14	SA event triggered reporting tests with Pre-MG	3924

A.7.6.14.1	Intra-frequency measurement test with SA event triggered reporting tests: with autonomous activation/deactivation of Pre-MG in FR2	3924

A.7.6.14.1.1	Test purpose and Environment	3924

A.7.6.14.1.2	Test parameters	3925

A.7.6.14.1.3	Test Requirements	3926

A.7.6.14.2	Intra-frequency measurement test with SA event triggered reporting tests: with network-controlled activation/deactivation of Pre-MG in FR2	3927

A.7.6.14.2.1	Test purpose and Environment	3927

A.7.6.14.2.2	Test parameters	3927

A.7.6.14.2.3	Test Requirements	3929

A.7.6.15	SA event triggered reporting tests with concurrent gaps	3929

A.7.6.15.1	SA event triggered reporting tests For FR2 with fully non-overlapping concurrent MGs for SSB-based inter-frequency measurements	3929

A.7.6.15.1.1	Test Purpose and Environment	3929

A.7.6.15.1.2	Test Requirements	3931

A.7.6.15.2	SA event triggered reporting tests For FR2 with concurrent measurement gaps without SSB time index detection when DRX is not used (PCell in FR2)	3932

A.7.6.15.2.1	Test Purpose and Environment	3932

A.7.6.15.2.2	Test Requirements	3934

A.7.6.15.3	SA event triggered reporting tests for FR2 concurrent gap with partially partial overlapping scenario for SSB-based measurements and PRS-based measurement	3934

A.7.6.15.3.1	Test Purpose and Environment	3934

A.7.6.15.3.2	Test Requirements	3937

A.7.6.16	SA event triggered reporting tests with NCSG	3937

A.7.6.16.1	SA event triggered reporting test with per-UE NCSG under non-DRX	3937

A.7.6.16.1.1	Test purpose and Environment	3937

A.7.6.16.1.2	Test Requirements	3940

A.7.6.16.2	SA event triggered reporting tests on inter-frequency measurement with NCSG for FR2 when DRX is not used (PCell in FR2)	3940

A.7.6.16.2.1	Test Purpose and Environment	3940

A.7.6.16.2.2	Test Requirements	3942

A.7.6.16.3	Event triggered reporting test on deactivated SCell measurement via NCSG in FR2 in non-DRX	3943

A.7.6.16.3.1	Test Purpose and Environment	3943

A.7.6.16.3.2	Test Requirements	3945

A.7.6.17	SA event triggered reporting tests for concurrent measurement gaps with Pre-MG in FR2	3945

A.7.6.17.1	SA event triggered reporting test for FR2 with one pre-configured gap and one measurement gap	3945

A.7.6.17.1.1	Test Purpose and Environment	3945

A.7.6.17.1.2	Test Requirements	3947

A.7.6.17.2	Inter-frequency measurement test with SA event triggered reporting tests: with autonomous activation/deactivation of Pre-MGs in FR2	3948

A.7.6.17.2.1	Test purpose and Environment	3948

A.7.6.17.2.2	Test parameters	3948

A.7.6.17.2.3	Test Requirements	3950

A.7.6.18	SA event triggered reporting tests with concurrent gaps and NCSG	3951

A.7.6.18.1	SA event triggered reporting tests For FR2 with concurrent measurement gaps and NCSG without SSB time index detection when DRX is not used (PCell in FR2)	3951

A.7.6.18.1.1	Test Purpose and Environment	3951

A.7.6.18.1.2	Test Requirements	3953

A.7.6.19	SA event triggered reporting tests with NeedForGap in FR2	3954

A.7.6.19.1	SA event triggered reporting test for UE indicating *NeedforInterruptionInfoNR* under non-DRX and no interruption outside configured measurement gaps	3954

A.7.6.19.1.1	Test purpose and Environment	3954

A.7.6.19.1.2	Test Requirements	3956

A.7.6.19.2	SA event triggered reporting test without gap under non-DRX	3956

A.7.6.19.2.1	Test purpose and Environment	3956

A.7.6.19.2.2	Test Requirements	3958

A.7.6.19.3	SA event triggered reporting test without gap without interruption under non-DRX	3959

A.7.6.19.3.1	Test Purpose and Environment	3959

A.7.6.19.3.2	Test Requirements	3961

A.7.6.20	LTM Intra-frequency L1-RSRP measurement	3961

A.7.6.20.1	Intra-frequency SSB based L1-RSRP measurement in FR2	3961

A.7.6.20.1.1	Test Purpose and Environment	3961

A.7.6.20.1.2	Test parameters	3962

A.7.6.20.1.3	Test Requirements	3964

A.7.6.21	LTM Inter-frequency L1-RSRP measurement with measurement gap	3964

A.7.6.21.1	Inter-frequency SSB-based L1-RSRP measurement with measurement gap for LTM in FR2	3964

A.7.6.21.1.1	Test Purpose and Environment	3964

A.7.6.21.1.2	Test parameters	3964

A.7.6.21.1.3	Test Requirements	3966

A.7.6.22	LTM Inter-frequency L1-RSRP measurement without measurement gap	3966

A.7.6.22.1	Inter-frequency SSB based L1-RSRP measurement without measurement gap in FR2	3966

A.7.6.22.1.1	Test Purpose and Environment	3966

A.7.6.22.1.2	Test parameters	3967

A.7.6.22.1.3	Test Requirements	3969

A.7.6.23	Idle Mode CA/DC Measurements	3969

A.7.6.23.1	Test case for Idle mode fast CA/DC eEMR measurement for FR2 without valid reporting	3969

A.7.6.23.1.1	Test Purpose and Environment	3969

A.7.6.23.1.2	Test Requirements	3972

A.7.6.23.2	Test case for Idle mode fast CA/DC cell reselection measurement for FR2 without valid reporting	3972

A.7.6.23.2.1	Test Purpose and Environment	3973

A.7.6.23.2.2	Test Requirements	3976

A.7.6.23.3 Test case for Idle mode fast CA/DC cell reselection measurement for FR2 with valid reporting	3976

A.7.6.23.3.1	Test Purpose and Environment	3976

A.7.6.23.3.2	Test Requirements	3979

A.7.6.24	RSCPD measurements	3980

A.7.6.24.1	NR RSCPD with RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC\_CONNECTED state	3980

A.7.6.24.1.1	Test Purpose and Environment	3980

A.7.6.24.1.2	Test Requirements	3987

A.7.6.25	RSCP measurements	3987

A.7.6.25.1	DL RSCP with UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA	3987

A.7.6.25.1.1	Test purpose and environment	3987

A.7.6.25.1.2	Test requirements	3991

A.7.7	Measurement Performance requirements	3991

A.7.7.1	SS-RSRP	3991

A.7.7.1.1	SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	3991

A.7.7.1.1.1	Test Purpose and Environment	3991

A.7.7.1.1.2	Test parameters	3991

A.7.7.1.1.3	Test Requirements	3993

A.7.7.1.2	SA inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	3994

A.7.7.1.2.1	Test Purpose and Environment	3994

A.7.7.1.2.2	Test parameters	3994

A.7.7.1.2.3	Test Requirements	3996

A.7.7.1.3	SA inter-frequency measurement accuracy with FR1 serving cell and FR2 target cell	3997

A.7.7.1.3.1	Test Purpose and Environment	3997

A.7.7.1.3.2	Test parameters	3997

A.7.7.1.3.3	Test Requirements	3999

A.7.7.2	SS-RSRQ	4000

A.7.7.2.1	SA intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell	4000

A.7.7.2.1.1	Test Purpose and Environment	4000

A.7.7.2.1.2	Test Parameters	4000

A.7.7.2.1.3	Test Requirements	4001

A.7.7.2.2	SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	4002

A.7.7.2.2.1	Test Purpose and Environment	4002

A.7.7.2.2.2	Test Parameters	4002

A.7.7.2.2.3	Test Requirements	4003

A.7.7.3	SS-SINR	4003

A.7.7.3.1	SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	4003

A.7.7.3.1.1	Test Purpose and Environment	4003

A.7.7.3.1.2	Test Parameters	4003

A.7.7.3.1.3	Test Requirements	4005

A.7.7.3.2	SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	4005

A.7.7.3.2.1	Test Purpose and Environment	4005

A.7.7.3.2.2	Test Parameters	4005

A.7.7.3.2.3	Test Requirements	4007

A.7.7.4	L1-RSRP measurement for beam reporting	4007

A.7.7.4.1	SSB based L1-RSRP measurement	4007

A.7.7.4.1.1	Test Purpose and Environment	4007

A.7.7.4.1.2	Test parameters	4007

A.7.7.4.1.3	Test Requirements	4008

A.7.7.4.2	CSI-RS based L1-RSRP measurement on resource set with repetition off	4009

A.7.7.4.2.1	Test Purpose and Environment	4009

A.7.7.4.2.2	Test parameters	4009

A.7.7.4.2.3	Test Requirements	4010

A.7.7.5	CLI measurements	4011

A.7.7.5.1	SA SRS-RSRP measurement accuracy with FR2 serving cell	4011

A.7.7.5.1.1	Test Purpose and Environment	4011

A.7.7.5.1.2	Test parameters	4011

A.7.7.5.1.3	Test Requirements	4013

A.7.7.5.2	SA CLI-RSSI measurement accuracy with FR2 serving cell	4013

A.7.7.5.2.1	Test Purpose and Environment	4013

A.7.7.5.2.2	Test parameters	4014

A.7.7.5.2.3	Test Requirements	4015

A.7.7.6	L1-SINR measurement for beam reporting	4016

A.7.7.6.1.1	Test Purpose and Environment	4016

A.7.7.6.1.2	Test parameters	4016

A.7.7.6.1.3	Test Requirements	4017

A.7.7.6.2	L1-SINR measurement with SSB based CMR and dedicated IMR	4018

A.7.7.6.2.1	Test Purpose and Environment	4018

A.7.7.6.2.2	Test parameters	4018

A.7.7.6.2.3	Test Requirements	4019

A.7.7.6.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR	4020

A.7.7.6.3.1	Test Purpose and Environment	4020

A.7.7.6.3.2	Test parameters	4020

A.7.7.6.3.3	Test Requirements	4021

A.7.7.7	CSI-RSRP	4022

A.7.7.7.1	SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	4022

A.7.7.7.1.1	Test Purpose and Environment	4022

A.7.7.7.1.2	Test parameters	4022

A.7.7.7.1.3	Test Requirements	4024

A.7.7.7.2	SA inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	4025

A.7.7.7.2.1	Test Purpose and Environment	4025

A.7.7.7.2.2	Test parameters	4025

A.7.7.7.2.3	Test Requirements	4026

A.7.7.8	CSI-RSRQ	4027

A.7.7.8.1	SA intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell	4027

A.7.7.8.1.1	Test Purpose and Environment	4027

A.7.7.8.1.2	Test Parameters	4027

A.7.7.8.1.3	Test Requirements	4029

A.7.7.8.2	SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	4029

A.7.7.8.2.1	Test Purpose and Environment	4029

A.7.7.8.2.2	Test Parameters	4029

A.7.7.8.2.3	Test Requirements	4031

A.7.7.9	CSI-SINR	4031

A.7.7.9.1	SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	4031

A.7.7.9.1.1	Test Purpose and Environment	4031

A.7.7.9.1.2	Test Parameters	4031

A.7.7.9.1.3	Test Requirements	4033

A.7.7.9.2	SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	4033

A.7.7.9.2.1	Test Purpose and Environment	4033

A.7.7.9.2.2	Test Parameters	4033

A.7.7.9.2.3	Test Requirements	4034

A.7.7.10	RSTD measurements	4035

A.7.7.10.1	RSTD measurement accuracy test case for single positioning frequency layer	4035

A.7.7.10.1.1	Test purpose and Environment	4035

A.7.7.10.1.2	Test Requirements	4036

A.7.7.10.2	RSTD measurement accuracy test case for dual positioning frequency layer	4036

A.7.7.10.2.1	Test purpose and Environment	4036

A.7.7.10.2.2	Test Requirements	4038

A.7.7.10.3	RSTD measurement accuracy test case with reduced number of samples for single positioning frequency layer in FR2 in RRC\_CONNECTED state	4038

A.7.7.10.3.1	Test purpose and Environment	4038

A.7.7.10.3.2	Test Requirements	4040

A.7.7.10.4	RSTD measurement accuracy test case with Rx TEG	4040

A.7.7.10.4.1	Test purpose and Environment	4040

A.7.7.10.4.2	Test Requirements	4041

A.7.7.10.5	NR RSTD measurement accuracy test case for PRS aggregation in FR2 SA in RRC\_CONNECTED mode	4041

A.7.7.10.5.1	Test purpose and Environment	4041

A.7.7.10.5.2	Test Requirements	4043

A.7.7.11	PRS-RSRP measurements	4043

A.7.7.11.1	SA measurement accuracy with PRS in FR2	4043

A.7.7.11.1.1	Test Purpose and Environment	4043

A.7.7.11.1.2	Test parameters	4043

A.7.7.11.1.3	Test Requirements	4045

A.7.7.11.2	SA measurement accuracy with PRS in FR2 with reduced sample number	4045

A.7.7.11.2.1	Test Purpose and Environment	4045

A.7.7.11.2.2	Test parameters	4045

A.7.7.11.2.3	Test Requirements	4047

A.7.7.12	UE Rx-Tx time difference measurements	4047

A.7.7.12.1	UE Rx-Tx time difference measurement accuracy for single positioning frequency layer in FR2 SA	4047

A.7.7.12.1.1	Test purpose and environment	4047

A.7.7.12.1.2	Test parameters	4048

A.7.7.12.1.3	Test requirements	4049

A.7.7.12.2	UE Rx-Tx time difference measurement accuracy with reduced number of samples in FR2 SA	4050

A.7.7.12.2.1	Test purpose and environment	4050

A.7.7.12.2.2	Test parameters	4050

A.7.7.12.2.3	Test requirements	4051

A.7.7.12.3	UE Rx-Tx time difference measurement accuracy with RxTx TEG	4051

A.7.7.12.3.1	Test purpose and environment	4051

A.7.7.12.3.2	Test parameters	4052

A.7.7.12.3.3	Test requirements	4053

A.7.7.12.4	UE Rx-Tx time difference measurement accuracy with PRS bandwidth aggregation in FR2 SA	4054

A.7.7.12.4.1	Test purpose and environment	4054

A.7.7.12.4.2	Test requirements	4058

A.7.7.13	PRS-RSRPP measurements	4058

A.7.7.13.1	SA measurement accuracy with PRS in FR2	4058

A.7.7.13.1.1	Test Purpose and Environment	4058

A.7.7.13.1.2	Test parameters	4058

A.7.7.13.1.3	Test Requirements	4060

A.7.7.13.2	SA measurement accuracy with reduced PRS samples in FR2	4060

A.7.7.13.2.1	Test Purpose and Environment	4060

A.7.7.13.2.2	Test parameters	4060

A.7.7.13.2.3	Test Requirements	4062

A.7.7.14	L1-RSRP measurement for group-based beam reporting	4062

A.7.7.14.1	SSB based L1-RSRP measurement	4062

A.7.7.14.1.1	Test Purpose and Environment	4062

A.7.7.14.1.2	Test parameters	4062

A.7.7.14.1.3	Test Requirements	4064

A.7.7.14.2	CSI-RS based L1-RSRP measurement on resource set with repetition off	4064

A.7.7.14.2.1	Test Purpose and Environment	4064

A.7.7.14.2.2	Test parameters	4064

A.7.7.14.2.3	Test Requirements	4066

A.7.7.15	LTM L1-RSRP measurement	4066

A.7.7.15.1	SSB based inter-frequency L1-RSRP measurement	4066

A.7.7.15.1.1	Test Purpose and Environment	4066

A.7.7.15.1.2	Test parameters	4067

A.7.7.15.1.3	Test Requirements	4068

A.7.7.16	RSCPD Measurements	4069

A.7.7.16.1	RSCPD with RSTD measurement accuracy in FR2 SA in RRC\_CONNECTED	4069

A.7.7.16.1.1	Test purpose and environment	4069

A.7.7.16.1.2	Test parameters	4069

A.7.7.16.1.3	Test requirements	4071

A.7.7.17	RSCP with UE Rx-Tx time difference measurements	4071

A.7.7.17.1	RSCP with UE Rx-Tx time difference measurement accuracy in FR2 SA	4071

A.7.7.17.1.1	Test purpose and environment	4071

A.7.7.17.1.2	Test parameters	4072

A.7.7.17.1.3	Test requirements	4075

A.7.8	Measurement procedure in RRC\_INACTIVE	4075

A.7.8.1	RSTD measurements	4075

A.7.8.1.1	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC\_INACTIVE state	4075

A.7.8.1.1.1	Test Purpose and Environment	4075

A.7.8.1.1.2	Test Requirements	4078

A.7.8.1.2	NR RSTD measurement reporting delay test case with reduced number of samples in RRC\_INACTIVE, FR1 SA	4078

A.7.8.1.2.1	Test Purpose and Environment	4078

A.7.8.1.2.2	Test Requirements	4081

A.7.8.1.3	NR RSTD measurement reporting delay test case for PRS aggregation in FR2 SA in RRC\_INACTIVE state	4081

A.7.8.1.3.1	Test purpose and environment	4081

A.7.8.1.3.2	Test requirements	4085

A.7.8.1.4	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC\_INACTIVE state with eDRX &gt; 10.24s	4085

A.7.8.1.4.1	Test purpose and environment	4085

A.7.8.1.4.2	Test requirements	4088

A.7.8.2	PRS-RSRP measurements	4088

A.7.8.2.1	PRS-RSRP reporting delay test case for single positioning frequency layer in RRC\_INACTIVE	4088

A.7.8.2.1.1	Test Purpose and Environment	4088

A.7.8.2.1.2	Test Requirements	4090

A.7.8.2.2	PRS-RSRP reporting delay test case with reduced number of samples in RRC\_INACTIVE	4091

A.7.8.2.2.1	Test purpose and Environment	4091

A.7.8.2.2.2	Test Requirements	4093

A.7.8.2.3	PRS-RSRP reporting delay in RRC\_INACTIVE with eDRX	4093

A.7.8.2.3.1	Test Purpose and Environment	4093

A.7.8.2.3.2	Test Requirements	4097

A.7.8.3	UE Rx-Tx time difference measurements	4097

A.7.8.3.1	UE Rx-Tx time difference measurements for single positioning frequency layer in FR2 SA	4097

A.7.8.3.1.1	Test purpose and environment	4097

A.7.8.3.1.2	Test requirements	4099

A.7.8.3.2	UE Rx-Tx time difference measurement with reduced number of samples in RRC\_INACTIVE, FR2 SA	4099

A.7.8.3.2.1	Test purpose and environment	4099

A.7.8.3.2.2	Test requirements	4101

A.7.8.3.3	UE Rx-Tx time difference measurements with PRS bandwidth aggregation in FR2 SA	4101

A.7.8.3.3.1	Test purpose and environment	4101

A.7.8.3.3.2	Test requirements	4104

A.7.8.3.4	UE Rx-Tx time difference measurements for single positioning frequency layer with eDRX &gt; 10.24s in FR2 SA	4104

A.7.8.3.4.1	Test purpose and environment	4104

A.7.8.3.4.2	Test requirements	4107

A.7.8.4	PRS-RSRPP measurements	4107

A.7.8.4.1	PRS-RSRPP reporting delay test case for single positioning frequency layer in FR2 in RRC\_INACTIVE state	4107

A.7.8.4.1.1	Test Purpose and Environment	4107

A.7.8.4.1.2	Test Requirements	4110

A.7.8.4.2	PRS-RSRPP reporting delay test with reduced number of samples for single positioning frequency layer in FR2 in RRC\_INACTIVE state	4110

A.7.8.4.2.1	Test Purpose and Environment	4110

A.7.8.4.2.2	Test Requirements	4112

A.7.8.4.3	PRS-RSPP reporting delay in RRC\_INACTIVE state with eDRX &gt; 10.24s in FR2	4113

A.7.8.4.3.1	Test purpose and environment	4113

A.7.8.4.3.2	Test requirements	4116

A.7.8.5	RSCPD Measurements	4116

A.7.8.5.1	DL RSCPD reported with RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC\_INACTIVE state	4116

A.7.8.5.1.1	Test Purpose and Environment	4116

A.7.8.5.1.2	Test Requirements	4117

A.7.8.6	RSCP Measurements	4117

A.7.8.6.1	DL RSCP with UE Rx-Tx time difference measurements in RRC\_INACTIVE for single positioning frequency layer in FR2 SA	4117

A.7.8.6.1.1	Test purpose and environment	4117

A.7.8.6.1.2	Test requirements	4121

A.7.9	Measurement performance requirements in RRC\_INACTIVE	4121

A.7.9.1	RSTD measurements	4121

A.7.9.1.1	RSTD measurement accuracy test case for single positioning frequency layer in FR2 in RRC\_INACTIVE state	4121

A.7.9.1.1.1	Test purpose and Environment	4121

A.7.9.1.1.2	Test Requirements	4123

A.7.9.1.2	RSTD measurement accuracy test case with reduced number of samples for single positioning frequency layer in FR2 in RRC\_INACTIVE state	4123

A.7.9.1.2.1	Test purpose and Environment	4123

A.7.9.1.2.2	Test Requirements	4125

A.7.9.2	PRS-RSRP measurements	4127

A.7.9.2.1	SA measurement accuracy with PRS in FR2 in RRC\_INACTIVE	4127

A.7.9.2.1.1	Test Purpose and Environment	4127

A.7.9.2.1.2	Test parameters	4127

A.7.9.2.1.3	Test Requirements	4128

A.7.9.2.2	PRS-RSRP measurements with reduced number of sample in RRC\_INACTIVE	4129

A.7.9.2.2.1	Test Purpose and Environment	4129

A.7.9.2.2.2	Test parameters	4129

A.7.9.2.2.3	Test Requirements	4130

A.7.9.3	UE Rx-Tx time difference measurements	4131

A.7.9.3.1	UE Rx-Tx time difference measurements in RRC\_INACTIVE	4131

A.7.9.3.1.1	Test purpose and environment	4131

A.7.9.3.1.2	Test parameters	4131

A.7.9.3.1.3	Test requirements	4132

A.7.9.3.2	UE Rx-Tx time difference measurement accuracy with reduced number of samples in FR2 SA	4132

A.7.9.3.2.1	Test purpose and environment	4132

A.7.9.3.2.2	Test parameters	4133

A.7.9.3.2.3	Test requirements	4134

A.7.9.3.3	UE Rx-Tx time difference measurement accuracy with PRS bandwidth aggregation in FR2 SA in RRC\_INACTIVE state	4134

A.7.9.3.3.1	Test purpose and environment	4134

A.7.9.3.3.2	Test requirements	4138

A.7.9.4	PRS-RSRPP measurements	4138

A.7.9.4.1	SA measurement accuracy in FR2 in RRC INACTIVE	4138

A.7.9.4.1.1	Test Purpose and Environment	4138

A.7.9.4.1.2	Test parameters	4138

A.7.9.4.1.3	Test Requirements	4140

A.7.9.4.2	SA measurement accuracy with reduced PRS samples in FR2 in RRC INACTIVE	4140

A.7.9.4.2.1	Test Purpose and Environment	4140

A.7.9.4.2.2	Test parameters	4140

A.7.9.4.2.3	Test Requirements	4142

A.7.9.5	RSCPD Measurements	4142

A.7.9.5.1	RSCPD with RSTD measurement accuracy in FR2 SA in RRC\_INACTIVE	4142

A.7.9.5.1.1	Test purpose and environment	4142

A.7.9.5.1.2	Test parameters	4142

A.7.9.5.1.3	Test requirements	4144

A.7.9.6	RSCP Measurements	4144

A.7.9.6.1	RSCP with UE Rx-Tx time difference measurement accuracy in FR2 SA	4144

A.7.9.6.1.1	Test purpose and environment	4144

A.7.9.6.1.2	Test parameters	4145

A.7.9.6.1.3	Test requirements	4146

A.7.10	Measurement Procedure in RRC\_IDLE	4146

A.7.10.1	RSTD Measurements	4146

A.7.10.1.1	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC\_IDLE state for non-RedCap UE	4146

A.7.10.1.1.1	Test purpose and environment	4146

A.7.10.1.1.2	Test requirements	4149

A.7.10.1.2	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC\_IDLE state with eDRX &gt; 10.24s	4149

A.7.10.1.2.1	Test purpose and environment	4149

A.7.10.1.2.2	Test requirements	4152

A.7.10.1.3	NR RSTD measurement reporting delay test case for PRS aggregation in FR2 SA in RRC\_IDLE state	4152

A.7.10.1.3.1	Test purpose and environment	4152

A.7.10.1.3.2	Test requirements	4153

A.7.10.2	PRS-RSRP Measurements	4153

A.7.10.2.1	PRS-RSRP reporting delay test case for single positioning frequency layer in RRC\_IDLE state for non-RedCap UE in FR2	4153

A.7.10.2.1.1	Test Purpose and Environment	4153

A.7.10.2.1.2	Test Requirements	4157

A.7.10.2.2	PRS-RSRP reporting delay test case in RRC\_IDLE state in FR2 when eDRX cycle &gt; 10.24s	4157

A.7.10.2.2.1	Test Purpose and Environment	4157

A.7.10.2.2.2	Test Requirements	4157

A.7.10.3	RSCPD Measurements	4158

A.7.10.3.1	DL RSCPD reported with RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC\_IDLE state	4158

A.7.10.3.1.1	Test Purpose and Environment	4158

A.7.10.3.1.2	Test Requirements	4158

A.7.11	Measurement Performance Requirements in RRC\_IDLE	4159

A.7.11.1	RSTD Measurements	4159

A.7.11.1.1	NR RSTD measurement accuracy test case for single positioning frequency layer in FR2 SA in RRC\_IDLE state for non-RedCap UE	4159

A.7.11.1.1.1	Test purpose and environment	4159

A.7.11.1.1.2	Test requirements	4160

A.7.11.1.2	RSTD measurement accuracy test case for single positioning frequency layer in FR2 SA in RRC\_IDLE state with eDRX &gt; 10.24s	4161

A.7.11.1.2.1	Test purpose and environment	4161

A.7.11.1.2.2	Test requirements	4162

A.7.11.1.3	NR RSTD measurement accuracy test case for PRS aggregation in FR2 SA in RRC\_IDLE state	4163

A.7.11.1.3.1	Test purpose and environment	4163

A.7.11.1.3.2	Test requirements	4163

A.7.11.2	PRS-RSRP measurements	4163

A.7.11.2.1	PRS-RSRP measurement accuracy test case for non-RedCap UE in FR2 in RRC\_IDLE state	4163

A.7.11.2.1.1	Test Purpose and Environment	4163

A.7.11.2.1.2	Test parameters	4163

A.7.11.2.1.3	Test Requirements	4165

A.7.11.2.2	PRS-RSRP measurement accuracy test case in RRC\_IDLE state in FR2 for case 2 when eDRX cycle &gt; 10.24s	4165

A.7.11.2.2.1	Test purpose and Environment	4165

A.7.11.2.2.1	Test parameters	4166

A.7.11.2.2.2	Test Requirements	4166

A.7.11.3	RSCPD measurements	4166

A.7.11.3.1	RSCPD with RSTD measurement accuracy in FR2 SA in RRC\_IDLE	4166

A.7.11.3.1.1	Test purpose and environment	4166

A.7.11.3.1.2	Test parameters	4166

A.7.11.3.1.3	Test requirements	4168

A.8	E-UTRA standalone tests for NR RRM	4170

A.8.1	Void	4170

A.8.2	RRC\_IDLE state mobility	4170

A.8.2.1	Inter-RAT NR Cell re-selection	4170

A.8.2.1.1	E-UTRA Cell reselection to higher priority NR target Cell in FR1	4170

A.8.2.1.1.1	Test Purpose and Environment	4170

A.8.2.1.1.2	Test Requirements	4173

A.8.2.1.2	E-UTRA Cell reselection to lower priority NR target Cell in FR1 for UE configured with highSpeedInterRAT-NR-r16	4173

A.8.2.1.2.1	Test Purpose and Environment	4173

A.8.2.1.2.2	Test Requirements	4176

A.8.2.2	E-UTRA – NR Inter-RAT Early Measruement Reporting	4177

A.8.2.2.1	E-UTRA – NR Early Measurement Reporting for NR in FR1	4177

A.8.2.2.1.1	Test Purpose and Environment	4177

A.8.2.2.1.2	Test Requirements	4179

A.8.2.2.2	E-UTRA – NR Early Measurement Reporting for NR in FR2	4180

A.8.2.2.2.1	Test Purpose and Environment	4180

A.8.2.2.2.2	Test Requirements	4182

A.8.3	RRC\_CONNECTED state mobility	4182

A.8.3.1	Handover	4182

A.8.3.1.1	E-UTRAN - NR handover in FR1	4182

A.8.3.1.1.1	Test Purpose and Environment	4182

A.8.3.1.1.2	Test Requirements	4186

A.8.4	Measurement procedure	4186

A.8.4.1	E-UTRA – NR Inter-RAT SFTD Measurement Delay	4186

A.8.4.1.1	E-UTRA – NR Inter-RAT SFTD Measurement Delay in non-DRX	4186

A.8.4.1.1.1	Test Purpose and Environment	4186

A.8.4.1.1.2	Test Requirements	4188

A.8.4.1.2	E-UTRA – NR Inter-RAT SFTD Measurement Delay in DRX	4188

A.8.4.1.2.1	Test Purpose and Environment	4188

A.8.4.1.2.2	Test Requirements	4189

A.8.4.2	E-UTRA – NR Inter-RAT Measurements	4189

A.8.4.2.1	NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used	4189

A.8.4.2.1.1	Test Purpose and Environment	4189

A.8.4.2.1.2	Test Requirements	4192

A.8.4.2.2	NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used	4192

A.8.4.2.2.1	Test Purpose and Environment	4192

A.8.4.2.2.2	Test Requirements	4195

A.8.4.2.3	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used	4196

A.8.4.2.3.1	Test Purpose and Environment	4196

A.8.4.2.3.2	Test Requirements	4199

A.8.4.2.4	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used	4199

A.8.4.2.4.1	Test Purpose and Environment	4199

A.8.4.2.4.2	Test Requirements	4202

A.8.4.2.5	NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is not used	4202

A.8.4.2.5.1	Test Purpose and Environment	4202

A.8.4.2.5.2	Test Requirements	4204

A.8.4.2.6	NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is used	4205

A.8.4.2.6.1	Test Purpose and Environment	4205

A.8.4.2.6.2	Test Requirements	4206

A.8.4.2.7	NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is not used	4207

A.8.4.2.7.1	Test Purpose and Environment	4207

A.8.4.2.7.2	Test Requirements	4209

A.8.4.2.8	NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is used	4209

A.8.4.2.8.1	Test Purpose and Environment	4209

A.8.4.2.8.2	Test Requirements	4211

A.8.4.2.9	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection in DRX for UE configured with highSpeedInterRAT-NR-r16	4211

A.8.4.2.9.1	Test Purpose and Environment	4211

A.8.4.2.9.2	Test Requirements	4214

A.8.4.3	E-UTRAN - NR Inter-RAT event-triggered without measurement gaps	4215

A.8.4.3.1	NR Inter-RAT event triggered reporting tests for FR2 without MG nor DRX	4215

A.8.4.3.1.1	Test Purpose and Environment	4215

A.8.4.3.1.2	Test Requirements	4216

A.8.4.3.2	NR Inter-RAT event triggered reporting tests for FR1 without gaps when DRX is not used	4217

A.8.4.3.2.1	Test Purpose and Environment	4217

A.8.4.3.2.2	Test Requirements	4220

A.8.5	Measurement performance	4220

A.8.5.1	SFTD accuracy	4220

A.8.5.1.1	SFTD accuracy	4220

A.8.5.1.1.1	Test Purpose	4220

A.8.5.1.1.2	Test Environment	4220

A.8.5.1.1.3	Test Requirements	4224

A.8.5.2	E-UTRA – NR Inter-RAT Measurement Performance requirements	4224

A.8.5.2.1.1	E-UTRAN – NR inter-RAT measurements with FR1 target cell	4224

A.8.5.2.1.2	E-UTRAN – NR inter-RAT measurements with FR2 target cell	4227

A.8.5.2.1.2.1	Test Purpose and Environment	4227

A.8.5.2.1.2.2	Test Parameters	4227

A.8.5.2.1.2.3	Test Requirements	4228

A.8.5.2.2	SS-RSRQ	4228

A.8.5.2.2.1	E-UTRAN – NR inter-RAT measurements with FR1 target cell	4228

A.8.5.2.2.2	E-UTRAN – NR inter-RAT measurements with FR2 target cell	4231

A.8.5.2.2.2.1	Test Purpose and Environment	4231

A.8.5.2.2.2.2	Test Parameters	4231

A.8.5.2.2.2.3	Test Requirements	4233

A.8.5.2.3	SS-SINR	4233

A.8.5.2.3.1	E-UTRAN – NR inter-RAT measurements with FR1 target cell	4233

A.8.5.2.3.2	E-UTRAN – NR inter-RAT measurements with FR2 target cell	4236

A.8.5.2.3.2.1	Test Purpose and Environment	4236

A.8.5.2.3.2.2	Test Parameters	4236

A.8.5.2.3.2.3	Test Requirements	4238

A.9	V2X Tests	4238

A.9.1	V2X Tests in FR1	4238

A.9.1.1	Test for V2X UE Transmit Timing	4238

A.9.1.1.1 Test for GNSS as Synchronization Reference Source	4238

A.9.1.1.1.1	Test Purpose and Environment	4238

A.9.1.1.1.2	Test requirements	4238

A.9.1.1.2	Test for SyncRef UE as Synchronization Reference Source	4238

A.9.1.1.2.1	Test Purpose and Environment	4238

A.9.1.1.2.2	Test requirements	4239

A.9.1.1.3	Test for FR1 NR Cell as Synchronization Reference Source	4239

A.9.1.1.3.1	Test Purpose and Environment	4239

A.9.1.1.3.2	Test requirements	4241

A.9.1.2	Test for Initiation/Cease of S-SSB Transmission with V2X Sidelink Communication	4241

A.9.1.2.1	Test for FR1 NR Cell as synchronization reference source without gap under non-DRX	4241

A.9.1.2.1.1	Test Purpose and Environment	4241

A.9.1.2.1.2	Test Requirements	4243

A.9.1.2.2	Test for SyncRef UE as synchronization reference source	4243

A.9.1.2.2.1	Test Purpose and Environment	4243

A.9.1.2.2.2	Test Requirements	4244

A.9.1.2.3	Test for SyncRef UE as synchronization reference source when SL-DRX is used	4245

A.9.1.2.3.1	Test Purpose and Environment	4245

A.9.1.2.3.2	Test Requirements	4246

A.9.1.2.4	Test for SyncRef UE as synchronization reference source with CCA	4246

A.9.1.2.4.1	Test Purpose and Environment	4247

A.9.1.2.4.2	Test Requirements	4248

A.9.1.3	 Test for V2X Synchronization Reference Selection/Reselection	4248

A.9.1.3.1	 Test for GNSS configured as the highest priority	4248

A.9.1.3.1.1	Test Purpose and Environment	4248

A.9.1.3.1.2	Test Requirements	4250

A.9.1.3.2	 Test for FR1 NR Cell configured as the highest priority	4251

A.9.1.3.2.1	Test Purpose and Environment	4251

A.9.1.3.2.2	Test Requirements	4252

A.9.1.3.3	Test for GNSS configured as the highest priority under SL-DRX	4253

A.9.1.3.3.1	Test Purpose and Environment	4253

A.9.1.3.3.2	Test Requirements	4254

A.9.1.3.4	Test for FR1 NR Cell configured as the highest priority under SL-DRX	4255

A.9.1.3.4.1	Test Purpose and Environment	4255

A.9.1.3.4.2	Test Requirements	4257

A.9.1.4	Test for L1 SL-RSRP Measurement	4257

A.9.1.4.1	Test for V2X UE Autonomous Resource Selection/Reselection	4257

A.9.1.4.1.1	Test Purpose and Environment	4257

A.9.1.4.1.2	Test Requirements	4259

A.9.1.4.2	Test for V2X UE Resource Pre-emption	4260

A.9.1.4.2.1	Test Purpose and Environment	4260

A.9.1.4.2.2	Test Requirements	4261

A.9.1.4.3	 Test for V2X UE Resource Re-evaluation	4262

A.9.1.4.3.1	Test Purpose and Environment	4262

A.9.1.4.3.2	Test Requirements	4265

A.9.1.4.4	Test for V2X UE Autonomous Resource Selection/Reselection with Periodic Sensing	4265

A.9.1.4.4.1	Test Purpose and Environment	4265

A.9.1.4.4.2	Test Requirements	4267

A.9.1.4.5	Test for V2X UE Autonomous Resource Selection/Reselection with Contiguous Sensing	4267

A.9.1.4.5.1	Test Purpose and Environment	4267

A.9.1.4.5.2	Test Requirements	4269

A.9.1.4.6	Test for V2X UE Autonomous Resource Selection/Reselection in SL-DRX	4270

A.9.1.4.6.1	Test Purpose and Environment	4270

A.9.1.4.6.2	Test Requirements	4272

A.9.1.5	Test for Congestion Control Measurement	4272

A.9.1.5.1	Test Purpose and Environment	4272

A.9.1.5.2	Test Requirements	4275

A.9.1.6	Test for Interruption	4275

A.9.1.6.1	Test for Interruption to WAN due to V2X Sidelink Communication	4275

A.9.1.6.1.1	Test Purpose and Environment	4275

A.9.1.6.1.2	Test Requirements	4278

A.9.1.6.2	Test for interruption to WAN at transitions between active and non-active during SL-DRX in asynchronous case	4278

A.9.1.6.2.1	Test Purpose and Environment	4278

A.9.1.6.2.2	Test Requirements	4279

A.9.1.6.3	Test for Interruption at NR Sidelink Diccovery Configuration	4280

A.9.1.6.3.1	Test Purpose and Environment	4280

A.9.1.6.3.2	Test Requirements	4282

A.9.1.7	Selection / Reselection of relay UE	4282

A.9.1.7.1	Test Purpose and Environment	4282

A.9.1.7.2	Test Requirements	4286

A.9A	Tests for NR Sidelink Measurements for Positioning	4287

A.9A.1	Tests for NR Sidelink Measurements for Positioning in FR1	4287

A.9A.1.1	Measurement delay tests	4287

A.9A.1.1.1	NR SL RSTD measurement reporting delay test case in FR1 SA	4287

A.9A.1.1.1.1	Test Purpose and Environment	4287

A.9A.1.1.1.2	Test Requirements	4292

A.9A.1.1.2	SL Rx-Tx measurement delay tests	4292

A.9A.1.1.2.1	Test Purpose and Environment	4292

A.9A.1.1.2.2	Test Requirements	4295

A.9A.1.1.3	NR SL AoA measurements reporting delay test in FR1 SA	4296

A.9A.1.1.3.1	Test Purpose and Environment	4296

A.9A.1.1.3.2	Test Requirements	4299

A.9A.1.1.4	NR SL RTOA measurements reporting delay test in FR1 SA	4300

A.9A.1.1.4.1	Test Purpose and Environment	4300

A.9A.1.1.4.2	Test Requirements	4303

A.9A.1.1.5	NR SL PRS-RSRP measurement reporting delay test case in FR1 SA	4304

A.9A.1.1.5.1	Test Purpose and Environment	4304

A.9A.1.1.5.2	Test Requirements	4304

A.9A.1.1.6	NR SL PRS-RSRPP measurement reporting delay test case in FR1 SA	4304

A.9A.1.1.6.1	Test Purpose and Environment	4304

A.9A.1.1.6.2	Test Requirements	4304

A.9A.1.2	Measurement Accuracy Tests	4305

A.9A.1.2.1	NR SL RSTD measurement accuracy test case in FR1 SA	4305

A.9A.1.2.1.1	Test Purpose and Environment	4305

A.9A.1.2.1.2	Test Requirements	4308

A.9A.1.2.2	SL Rx-Tx measurement accuracy test case in FR1	4309

A.9A.1.2.2.1	Test Purpose and Environment	4309

A.9A.1.2.2.2	Test Requirements	4312

A.9A.1.2.3	NR SL PRS-RSRP measurement accuracy test case in FR1 SA	4312

A.9A.1.2.3.1	Test Purpose and Environment	4312

A.9A.1.2.3.2	Test Requirements	4313

A.9A.1.2.4	NR SL PRS-RSRPP measurement accuracy test case in FR1 SA	4313

A.9A.1.2.4.1	Test Purpose and Environment	4313

A.9A.1.2.4.2	Test Requirements	4313

A.10	EN-DC Tests with NR PSCell under CCA and Other NR Cells in FR1	4318

A.10.1	RRC\_CONNECTED state mobility	4318

A.10.1.1	RRC connection mobility control	4318

A.10.1.1.1	Random Access	4318

A.10.1.1.1.1	4-step RA type contention-based random access for NR PSCell with CCA	4318

A.10.1.1.1.1.1	Test Purpose and Environment	4318

A.10.1.1.1.1.2	Test Requirements	4319

A.10.1.1.1.1.2.1	Random Access Preamble Transmission	4320

A.10.1.1.1.1.2.2	Random Access Response Reception	4320

A.10.1.1.1.1.2.3	No Random Access Response Reception	4320

A.10.1.1.1.1.2.4	Receiving an UL grant for msg3 retransmission	4321

A.10.1.1.1.1.2.5	 Contention Resolution Timer expiry	4321

A.10.1.1.1.2	4-step RA type non-contention based random access for NR PSCell with CCA	4321

A.10.1.1.1.2.1	Test Purpose and Environment	4321

A.10.1.1.1.2.2	Test Requirements	4322

A.10.1.1.1.2.2.1	SSB-based Random Access Preamble Transmission	4323

A.10.1.1.1.2.2.2	Random Access Response Reception	4323

A.10.1.1.1.2.2.3	No Random Access Response Reception	4323

A.10.1.1.1.3	2-step RA type contention-based random access for NR PSCell with CCA	4324

A.10.1.1.1.3.1	Test Purpose and Environment	4324

A.10.1.1.1.3.2	Test Requirements	4325

A.10.1.1.1.3.2.1	MsgA Transmission	4326

A.10.1.1.1.3.2.2	MsgB Reception	4326

A.10.1.1.1.3.2.3	No MsgB Reception	4326

A.10.1.1.1.4	2-step RA type non-contention based random access for NR PSCell with CCA	4327

A.10.1.1.1.4.1	Test Purpose and Environment	4327

A.10.1.1.1.4.2	Test Requirements	4328

A.10.1.1.1.4.2.1	MsgA Transmission	4329

A.10.1.1.1.4.2.2	MsgB Reception	4329

A.10.1.1.1.4.2.3	No MsgB Reception	4329

A.10.1.2	Handover with PSCell from EN-DC to EN-DC with known target PSCell using CCA	4330

A.10.1.2.1	Test Purpose and Environment	4330

A.10.1.2.2	Test Requirements	4334

A.10.2	Timing	4335

A.10.2.1	UE transmit timing	4335

A.10.2.1.1	UE Transmit Timing Test with PSCell under DL CCA	4335

A.10.2.1.1.1	Test Purpose and environment	4335

A.10.2.1.1.2	Test requirements	4337

A.10.2.2	UE timing advance	4338

A.10.2.2.1	UE Timing Advance Adjustment Accuracy with PSCell under DL CCA	4338

A.10.2.2.1.1	Test Purpose and Environment	4338

A.10.2.2.1.2	Test Parameters	4338

A.10.2.2.1.3	Test Requirements	4340

A.10.3	Signalling characteristics	4340

A.10.3.1	Radio link monitoring	4340

A.10.3.1.1	Introduction	4340

A.10.3.1.2	Radio link monitoring out-of-sync test for PSCell configured with SSB-based RLM RS in non-DRX mode	4341

A.10.3.1.2.1	Test purpose and environment	4341

A.10.3.1.2.2	Test requirements	4343

A.10.3.1.3	Radio link monitoring in-sync test for PSCell configured with SSB-based RLM RS in non-DRX mode	4344

A.10.3.1.3.1	Test purpose and environment	4344

A.10.3.1.3.2	Test requirements	4346

A.10.3.1.4	Void	4346

A.10.3.1.4.1	Void	4346

A.10.3.1.4.2	Void	4346

A.10.3.1.5	Void	4347

A.10.3.1.5.1	Void	4347

A.10.3.1.5.2	Void	4347

A.10.3.2	Void	4347

A.10.3.3	SCell activation and deactivation delay	4347

A.10.3.3.1	SCell Activation and Deactivation of known NR SCell with NR PSCell and NR SCell under CCA, 160 ms SCell measurement cycle	4347

A.10.3.3.1.1	Test Purpose and Environment	4347

A.10.3.3.1.2	Test Requirements	4350

A.10.3.3.2 SCell Activation and Deactivation of known NR SCell with NR PSCell and NR SCell under CCA, 640 ms SCell measurement cycle	4350

A.10.3.3.2.1	Test Purpose and Environment	4350

A.10.3.3.2.2	Test Requirements	4351

A.10.3.3.3	SCell Activation and Deactivation of unknown NR SCell with NR PSCell and NR SCell under CCA	4351

A.10.3.3.3.1	Test Purpose and Environment	4351

A.10.3.3.3.2	Test Requirements	4351

A.10.3.4	Beam failure detection and link recovery procedures	4352

A.10.3.4.1	EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in non-DRX mode	4352

A.10.3.4.1.1	Test Purpose and Environment	4352

A.10.3.4.1.2	Test Requirements	4355

A.10.3.4.2	EN-DC Beam Failure Detection and Link Recovery Test for FR1 PSCell configured with SSB-based BFD and LR in DRX mode	4355

A.10.3.4.2.1	Test Purpose and Environment	4355

A.10.3.4.2.2	Test Requirements	4358

A.10.3.5	Active BWP switching	4359

A.10.3.5.1	UL active BWP switch delay with consistent UL LBT failure on PSCell subject to UL CCA in EN-DC	4359

A.10.3.5.1.2	Test Requirements	4361

A.10.3.5.2	DCI-based and Timer-based Active BWP Switch	4362

A.10.3.5.2.1	E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC	4362

A.10.3.5.2.2	E-UTRAN – NR PSCell FR1 DL active BWP switch with FR1 SCell in non-DRX in synchronous EN-DC	4365

A.10.3.5.3	RRC-based Active BWP Switch	4369

A.10.3.5.3.1	E-UTRAN – NR PSCell FR1 DL active BWP switch in non-DRX in synchronous EN-DC	4369

A.10.3.6	PSCell addition and release delay	4371

A.10.3.6.1	Addition and Release Delay of known NR PSCell on the carrier under CCA	4371

A.10.3.6.1.1	Test purpose and environment	4371

A.10.3.6.1.2	Test Requirements	4374

A.10.3.7	Void	4374

A.10.4	Measurement procedure	4374

A.10.4.1	Intra-frequency measurements	4375

A.10.4.1.1	Event-triggered reporting tests on PSCC without gaps under non-DRX	4375

A.10.4.1.1.1	Test purpose and environment	4375

A.10.4.1.1.2	Test parameters	4375

A.10.4.1.1.3	Test Requirements	4377

A.10.4.1.2	Void	4377

A.10.4.1.3	Void	4377

A.10.4.1.4	Event-triggered reporting tests on PSCC with per-UE gaps under DRX	4377

A.10.4.1.4.1	Test purpose and environment	4377

A.10.4.1.4.2	Test parameters	4377

A.10.4.1.4.3	Test Requirements	4380

A.10.4.1.5	Void	4380

A.10.4.1.6	Void	4380

A.10.4.1.7	Void	4380

A.10.4.1.8	Void	4380

A.10.4.1.9	Void	4380

A.10.4.1.10	Void	4380

A.10.4.1.11	Void	4380

A.10.4.1.12	Void	4380

A.10.4.2	Inter-frequency measurements	4380

A.10.4.2.1	Void	4380

A.10.4.2.2	Void	4380

A.10.4.2.3	EN-DC event triggered reporting tests for FR1 with CCA cell without SSB time index detection when DRX is not used	4381

A.10.4.2.3.1	Test Purpose and Environment	4381

A.10.4.2.3.2	Test Requirements	4383

A.10.4.2.4	EN-DC event triggered reporting tests for FR1 cell with CCA without SSB time index detection when DRX is used	4383

A.10.4.2.4.1	Test Purpose and Environment	4383

A.10.4.2.4.2	Test Requirements	4386

A.10.4.2.5	EN-DC event triggered reporting tests for FR1 cell with CCA with SSB time index detection when DRX is not used	4387

A.10.4.2.5.1	Test Purpose and Environment	4387

A.10.4.2.5.2	Test Requirements	4389

A.10.4.2.6	EN-DC event triggered reporting tests for FR1 cell with CCA with SSB time index detection when DRX is used	4389

A.10.4.2.6.1	Test Purpose and Environment	4389

A.10.4.2.6.2	Test Requirements	4392

A.10.4.2.7	EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is not used	4393

A.10.4.2.7.1	Test Purpose and Environment	4393

A.10.4.2.7.2	Test Requirements	4396

A.10.4.2.8	EN-DC event triggered reporting tests for FR1 cell without SSB time index detection when DRX is used	4396

A.10.4.2.8.1	Test Purpose and Environment	4396

A.10.4.2.8.2	Test Requirements	4400

A.10.4.2.9	EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is not used	4401

A.10.4.2.9.1	Test Purpose and Environment	4401

A.10.4.2.9.2	Test Requirements	4404

A.10.4.2.10	EN-DC event triggered reporting tests for FR1 cell with SSB time index detection when DRX is used	4404

A.10.4.2.10.1	Test Purpose and Environment	4404

A.10.4.2.10.2	Test Requirements	4408

A.10.4.3	L1-RSRP measurements for beam reporting	4409

A.10.4.3.1	SSB based L1-RSRP measurement on PSCC when DRX is not used	4409

A.10.4.3.1.1	Test Purpose and Environment	4409

A.10.4.3.1.2	Test parameters	4409

A.10.4.3.1.3	Test Requirements	4410

A.10.4.3.2	SSB based L1-RSRP measurement on PSCC when DRX is used	4411

A.10.4.3.2.1	Test Purpose and Environment	4411

A.10.4.3.2.2	Test parameters	4411

A.10.4.3.2.3	Test Requirements	4412

A.10.4.3.3	SSB based L1-RSRP measurement on SCC when DRX is not used	4413

A.10.4.3.3.1	Test Purpose and Environment	4413

A.10.4.3.3.2	Test parameters	4413

A.10.4.3.3.3	Test Requirements	4414

A.10.4.3.4	SSB based L1-RSRP measurement on SCC when DRX is used	4415

A.10.4.3.4.1	Test Purpose and Environment	4415

A.10.4.3.4.2	Test parameters	4415

A.10.4.3.4.3	Test Requirements	4416

A.10.4.4	E-UTRANNR inter-RAT measurements on NR carrier frequency under CCA	4417

A.10.4.4.1	E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used	4417

A.10.4.4.1.1	Test Purpose and Environment	4417

A.10.4.4.1.2	Test Requirements	4420

A.10.4.4.2	E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used	4421

A.10.4.4.2.1	Test Purpose and Environment	4421

A.10.4.4.2.2	Test Requirements	4424

A.10.4.4.3	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used	4425

A.10.4.4.3.1	Test Purpose and Environment	4425

A.10.4.4.3.2	Test Requirements	4428

A.10.4.4.4	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used	4428

A.10.4.4.4.1	Test Purpose and Environment	4428

A.10.4.4.4.2	Test Requirements	4432

A.10.5	Measurement performance	4432

A.10.5.1	SS-RSRP	4432

A.10.5.1.1	Intra-frequency measurement accuracy on a CCA serving cell	4432

A.10.5.1.1.1	Test Purpose and Environment	4432

A.10.5.1.1.2	Test parameters	4433

A.10.5.1.1.3	Test Requirements	4434

A.10.5.1.2	Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell	4434

A.10.5.1.2.1	Test Purpose and Environment	4434

A.10.5.1.2.2	Test parameters	4435

A.10.5.1.2.3	Test Requirements	4436

A.10.5.2	SS-RSRQ	4436

A.10.5.2.1	Intra-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell	4436

A.10.5.2.1.1	Test Purpose and Environment	4436

A.10.5.2.1.2	Test Parameters	4436

A.10.5.2.1.3	Test Requirements	4438

A.10.5.2.2	Inter-frequency measurement accuracy with FR1 CCA serving cell and FR1 CCA target cell	4438

A.10.5.2.2.1	Test Purpose and Environment	4438

A.10.5.2.2.2	Test Parameters	4438

A.10.5.2.2.3	Test Requirements	4439

A.10.5.3	SS-SINR	4439

A.10.5.3.1	Intra-frequency measurement accuracy on PSCC	4439

A.10.5.3.1.1	Test Purpose and Environment	4439

A.10.5.3.1.2	Test Parameters	4439

A.10.5.3.1.3	Test Requirements	4441

A.10.5.3.2	Inter-frequency measurement accuracy on PSCC	4441

A.10.5.3.2.1	Test Purpose and Environment	4441

A.10.5.3.2.2	Test Parameters	4441

A.10.5.3.2.3	Test Requirements	4443

A.10.5.3.3	Intra-frequency measurement accuracy on SCC	4443

A.10.5.3.3.1	Test Purpose and Environment	4443

A.10.5.3.3.2	Test Parameters	4443

A.10.5.3.3.3	Test Requirements	4445

A.10.5.4	L1-RSRP measurement for beam reporting with CCA serving cell	4445

A.10.5.4.1	SSB based L1-RSRP measurement	4445

A.10.5.4.1.1	Test Purpose and Environment	4445

A.10.5.4.1.2	Test parameters	4445

A.10.5.4.1.3	Test Requirements	4447

A.10.5.5	RSSI	4447

A.10.5.5.1 	RSSI measurement accuracy on PSCC with CCA	4447

A.10.5.5.1.1	Test Purpose and Environment	4447

A.10.5.5.1.2	Test parameters	4447

A.10.5.5.1.3	Test Requirements	4448

A.10.5.5.2	RSSI measurement accuracy on SCC with CCA	4449

A.10.5.5.2.1	Test Purpose and Environment	4449

A.10.5.5.2.2	Test parameters	4449

A.10.5.5.2.3	Test Requirements	4450

A.10.5.5.3 	Inter-frequency RSSI measurement accuracy on a carrier with CCA	4450

A.10.5.5.3.1	Test Purpose and Environment	4450

A.10.5.5.3.2	Test parameters	4451

A.10.5.5.3.3	Test Requirements	4452

A.10.5.6	Channel occupancy	4452

A.10.5.6.1 	Channel occupancy measurement accuracy on PSCC with CCA	4452

A.10.5.6.1.1	Test Purpose and Environment	4452

A.10.5.6.1.2	Test parameters	4452

A.10.5.6.1.3	Test Requirements	4454

A.10.5.6.2 	Channel occupancy measurement accuracy on SCC with CCA	4454

A.10.5.6.2.1	Test Purpose and Environment	4454

A.10.5.6.2.2	Test parameters	4454

A.10.5.6.2.3	Test Requirements	4456

A.10.5.6.3 	Inter-frequency channel occupancy measurement accuracy on a carrier with CCA	4456

A.10.5.6.3.1	Test Purpose and Environment	4456

A.10.5.6.3.2	Test parameters	4456

A.10.5.6.3.3	Test Requirements	4458

A.11	NR Standalone Tests with NR PCell under CCA and Other NR Cells in FR1	4460

A.11.1	RRC\_IDLE state mobility	4460

A.11.1.1	Cell re-selection with both source and target NR carrier frequencies under CCA	4460

A.11.1.1.1	Cell reselection to FR1 intra-frequency NR cells when subject to CCA on the serving and target cell	4460

A.11.1.1.1.1	Test Purpose and Environment	4460

A.11.1.1.1.2	Test Parameters	4460

A.11.1.1.1.3	Test Requirements	4462

A.11.1.1.2	Cell reselection to FR1 inter-frequency NR case when subject to CCA on the serving and target cell	4463

A.11.1.1.2.1	Test Purpose and Environment	4463

A.11.1.1.2.2	Test Parameters	4463

A.11.1.1.2.3	Test Requirements	4465

A.11.1.2	Cell re-selection to NR with source NR carrier frequency under CCA	4465

A.11.1.2.1	Cell reselection to FR1 inter-frequency NR case when serving cell is subject to CCA	4465

A.11.1.2.1.1	Test Purpose and Environment	4465

A.11.1.2.1.2	Test Parameters	4466

A.11.1.2.1.3	Test Requirements	4468

A.11.1.3	Cell re-selection from NR carrier with target NR carrier frequency under CCA	4469

A.11.1.3.1	Cell reselection to FR1 inter-frequency NR case when target cell is subject to CCA	4469

A.11.1.3.1.1	Test Purpose and Environment	4469

A.11.1.3.1.2	Test Parameters	4469

A.11.1.3.1.3	Test Requirements	4472

A.11.1.4	Inter-RAT cell re-selection to E-UTRAN with source NR carrier frequency under CCA	4473

A.11.1.4.1	Cell reselection to higher priority E-UTRAN when serving cell is subject to CCA	4473

A.11.1.4.1.1	Test Purpose and Environment	4473

A.11.1.4.1.2	Test Parameters	4473

A.11.1.4.1.3	Test Requirements	4476

A.11.1.4.2	Cell reselection to lower priority E-UTRAN when serving cell is subject to CCA	4476

A.11.1.4.2.1	Test Purpose and Environment	4476

A.11.1.4.2.2	Test Requirements	4478

A.11.2	RRC\_CONNECTED state mobility	4479

A.11.2.1	Handover	4479

A.11.2.1.1	Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; known target cell	4479

A.11.2.1.1.1	Test Purpose and Environment	4479

A.11.2.1.1.2	Test Parameters	4479

A.11.2.1.1.3 Test Requirements	4481

A.11.2.1.2	Intra-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; unknown target cell	4482

A.11.2.1.2.1	Test Purpose and Environment	4482

A.11.2.1.2.2	Test Parameters	4482

A.11.2.1.2.3	Test Requirements	4484

A.11.2.1.3	Inter-frequency handover from FR1 carrier under CCA to FR1 carrier under CCA; unknown target cell	4484

A.11.2.1.3.1	Test Purpose and Environment	4484

A.11.2.1.3.2	Test Parameters	4484

A.11.2.1.3.3	Test Requirements	4486

A.11.2.1.4	Inter-frequency handover from FR1 carrier under CCA to FR1; known target cell	4487

A.11.2.1.4.1	Test Purpose and Environment	4487

A.11.2.1.4.2	Test Parameters	4487

A.11.2.1.4.3	Test Requirements	4490

A.11.2.1.5	Inter-frequency handover from FR1 carrier under CCA to FR1; unknown target cell	4490

A.11.2.1.5.1	Test Purpose and Environment	4490

A.11.2.1.5.2	Test Parameters	4490

A.11.2.1.5.3 Test Requirements	4493

A.11.2.1.6	Inter-frequency handover from FR1 to FR1 carrier under CCA; unknown target cell	4493

A.11.2.1.6.1	Test Purpose and Environment	4493

A.11.2.1.6.2	Test Parameters	4493

A.11.2.1.6.3	Test Requirements	4496

A.11.2.1.7	 SA NR FR1 carrier under CCA - E-UTRAN handover with known target cell	4496

A.11.2.1.7.1	Test Purpose and Environment	4496

A.11.2.1.7.2	Test Requirements	4499

A.11.2.1.8	SA NR FR1 carrier under CCA - E-UTRAN handover with unknown target cell	4500

A.11.2.1.8.1	Test Purpose and Environment	4500

A.11.2.1.8.2	Test Requirements	4503

A.11.2.1.9	Handover with PSCell from NR SA to EN-DC with known target PSCell using CCA	4503

A.11.2.1.9.1	Test Purpose and Environment	4503

A.11.2.1.9.2	Test Requirements	4509

A.11.2.2	RRC connection mobility control	4510

A.11.2.2.1	RRC re-establishment	4510

A.11.2.2.1.1	Intra-frequency RRC Re-establishment with CCA in FR1	4510

A.11.2.2.1.2	Inter-frequency RRC Re-establishment with CCA in FR1	4513

A.11.2.2.1.4	Inter-frequency RRC Re-establishment from NR FR1 carrier without CCA to NR FR1 carrier under CCA	4519

A.11.2.2.2	Random Access	4522

A.11.2.2.2.1	4-step RA type contention-based random access for NR PCell with CCA	4522

A.11.2.2.2.1.1	Test Purpose and Environment	4522

A.11.2.2.2.1.2	Test Requirements	4523

A.11.2.2.2.1.2.1	Random Access Preamble Transmission	4523

A.11.2.2.2.1.2.2	Random Access Response Reception	4524

A.11.2.2.2.1.2.3	No Random Access Response Reception	4524

A.11.2.2.2.1.2.4	Receiving an UL grant for msg3 retransmission	4524

A.11.2.2.2.1.2.5	Reception of an Incorrect Message over Temporary C-RNTI	4524

A.11.2.2.2.1.2.6	Reception of a Correct Message over Temporary C-RNTI	4525

A.11.2.2.2.1.2.7	Contention Resolution Timer expiry	4525

A.11.2.2.2.2	4-step RA type non-contention based random access for NR PSCell with CCA	4525

A.11.2.2.2.2.1	Test Purpose and Environment	4525

A.11.2.2.2.2.2	Test Requirements	4526

A.11.2.2.2.2.2.1	SSB-based Random Access Preamble Transmission	4526

A.11.2.2.2.2.2.2	Random Access Response Reception	4527

A.11.2.2.2.2.2.3	No Random Access Response Reception	4527

A.11.2.2.2.3	2-step RA type contention-based random access for NR PCell with CCA	4528

A.11.2.2.2.3.1	Test Purpose and Environment	4528

A.11.2.2.2.3.2	Test Requirements	4529

A.11.2.2.2.3.2.1	MsgA Transmission	4529

A.11.2.2.2.3.2.2	MsgB Reception	4530

A.11.2.2.2.3.2.3	No MsgB Reception	4530

A.11.2.2.2.4	2-step RA type non-contention-based random access for NR PCell with CCA	4531

A.11.2.2.2.4.1	Test Purpose and Environment	4531

A.11.2.2.2.4.2	Test Requirements	4532

A.11.2.2.2.4.2.1	MsgA Transmission	4532

A.11.2.2.2.4.2.2	MsgB Reception	4533

A.11.2.2.2.4.2.3	No MsgB Reception	4533

A.11.2.2.3	RRC connection release with redirection	4534

A.11.2.2.3.1	Redirection from NR FR1 carrier under CCA to NR FR1 carrier under CCA	4534

A.11.2.2.3.2	Redirection from NR FR1 carrier without CCA to NR FR1 carrier with CCA	4536

A.11.3	Timing	4539

A.11.3.1	UE transmit timing	4539

A.11.3.1.1	UE Transmit Timing Test with PCell under DL CCA	4539

A.11.3.1.1.1	Test Purpose and environment	4539

A.11.3.1.1.2	Test requirements	4541

A.11.3.2	UE timing advance	4542

A.11.3.2.1	UE Timing Advance Adjustment Accuracy with PCell under DL CCA	4542

A.11.3.2.1.1	Test Purpose and Environment	4542

A.11.3.2.1.2	Test Parameters	4542

A.11.3.2.1.3	Test Requirements	4544

A.11.4	Signalling characteristics	4544

A.11.4.1	Radio link monitoring	4544

A.11.4.1.1	Introduction	4544

A.11.4.1.2	Radio link monitoring out-of-sync test for PCell configured with SSB-based RLM RS in non-DRX mode	4545

A.11.4.1.2.1	Test purpose and environment	4545

A.11.4.1.2.2	Test requirements	4547

A.11.4.1.3	Radio link monitoring in-sync test for PCell configured with SSB-based RLM RS in non-DRX mode	4548

A.11.4.1.3.1	Test purpose and environment	4548

A.11.4.1.3.2	Test requirements	4551

A.11.4.1.4	Void	4551

A.11.4.1.4.1	Void	4551

A.11.4.1.4.2	Void	4551

A.11.4.1.5	Void	4551

A.11.4.1.5.1	Void	4551

A.11.4.1.5.2	Void	4551

A.11.4.2	Void	4551

A.11.4.3	SCell activation and deactivation delay	4551

A.11.4.3.1	SCell Activation and Deactivation of known SCell with PCell and SCell under CCA, 160 ms SCell measurement cycle	4551

A.11.4.3.1.1	Test Purpose and Environment	4551

A.11.4.3.1.2	Test Requirements	4554

A.11.4.3.2	SCell Activation and Deactivation of known SCell with PCell and SCell under CCA, 640 ms SCell measurement cycle	4554

A.11.4.3.2.1	Test Purpose and Environment	4554

A.11.4.3.2.2	Test Requirements	4555

A.11.4.3.3	SCell Activation and Deactivation of unknown SCell with PCell and SCell under CCA	4555

A.11.4.3.3.1	Test Purpose and Environment	4555

A.11.4.3.3.2	Test Requirements	4555

A.11.4.4	Beam failure detection and link recovery procedures	4556

A.11.4.4.1	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode	4556

A.11.4.4.1.1	Test Purpose and Environment	4556

A.11.4.4.1.2	Test Requirements	4559

A.11.4.4.2	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode	4560

A.11.4.4.2.1	Test Purpose and Environment	4560

A.11.4.4.2.2	Test Requirements	4563

A.11.4.5	Active BWP switching	4563

A.11.4.5.1	UL active BWP switch delay with consistent UL LBT failure on PCell subject to UL CCA	4563

A.11.4.5.1.1	Test Purpose and Environment	4563

A.11.4.5.1.2	Test Requirements	4566

A.11.4.5.2	DCI-based and Timer-based Active BWP Switch	4566

A.11.4.5.2.1	NR FR1- NR FR1 DL active BWP switch of PCell with non-DRX in SA	4566

A.11.4.5.2.2	NR FR1 DL active BWP switch with non-DRX in SA	4569

A.11.4.5.3	RRC-based Active BWP Switch	4572

A.11.4.5.3.1	NR FR1 DL active BWP switch of Cell with non-DRX in SA	4572

A.11.4.6	Void	4574

A.11.5	Measurement procedure	4574

A.11.5.1	Intra-frequency measurements	4574

A.11.5.1.1	Event-triggered reporting tests on PCC without gaps under non-DRX	4574

A.11.5.1.1.1	Test purpose and environment	4574

A.11.5.1.1.2	Test parameters	4574

A.11.5.1.1.3	Test Requirements	4576

A.11.5.1.2	Event-triggered reporting tests on PCC without gaps under DRX	4576

A.11.5.1.2.1	Test purpose and environment	4576

A.11.5.1.2.2	Test parameters	4576

A.11.5.1.2.3	Test Requirements	4578

A.11.5.1.3	Void	4579

A.11.5.1.4	Void	4579

A.11.5.1.5	Void	4579

A.11.5.1.6	Void	4579

A.11.5.1.7	Void	4579

A.11.5.1.8	Void	4579

A.11.5.1.9	Void	4579

A.11.5.1.10	Void	4579

A.11.5.1.11	Void	4579

A.11.5.1.12	Void	4579

A.11.5.2	Inter-frequency measurements	4579

A.11.5.2.1	Void	4579

A.11.5.2.2	Void	4579

A.11.5.2.3	Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is not used	4579

A.11.5.2.3.1	Test Purpose and Environment	4579

A.11.5.2.3.2	Test Requirements	4582

A.11.5.2.4	Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is used	4582

A.11.5.2.4.1	Test Purpose and Environment	4582

A.11.5.2.4.2	Test Requirements	4585

A.11.5.2.5	Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is not used	4585

A.11.5.2.5.1	Test Purpose and Environment	4585

A.11.5.2.5.2	Test Requirements	4588

A.11.5.2.6	Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is used	4588

A.11.5.2.6.1	Test Purpose and Environment	4588

A.11.5.2.6.2	Test Requirements	4591

A.11.5.2.7	Event triggered reporting tests for FR1 without SSB time index detection when DRX is not used	4592

A.11.5.2.7.1	Test Purpose and Environment	4592

A.11.5.2.7.2	Test Requirements	4594

A.11.5.2.8	Event triggered reporting tests for FR1 without SSB time index detection when DRX is used	4595

A.11.5.2.8.1	Test Purpose and Environment	4595

A.11.5.2.8.2	Test Requirements	4598

A.11.5.2.9	Event triggered reporting tests for FR1 with SSB time index detection when DRX is not used	4598

A.11.5.2.9.1	Test Purpose and Environment	4598

A.11.5.2.9.2	Test Requirements	4601

A.11.5.2.10	Event triggered reporting tests for FR1 with SSB time index detection when DRX is used	4601

A.11.5.2.10.1	Test Purpose and Environment	4601

A.11.5.2.10.2	Test Requirements	4605

A.11.5.3	Inter-RAT E-UTRAN measurements	4605

A.11.5.3.1	SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1	4605

A.11.5.3.1.1	Test Purpose and Environment	4605

A.11.5.3.1.2	Test Requirements	4608

A.11.5.3.2	SA NR - E-UTRAN event-triggered reporting in DRX in FR1	4608

A.11.5.3.2.1	Test Purpose and Environment	4608

A.11.5.3.2.2	Test Requirements	4612

A.11.5.4	L1-RSRP measurements for beam reporting	4612

A.11.5.4.1	SSB based L1-RSRP measurement when DRX is not used	4612

A.11.5.4.1.1	Test Purpose and Environment	4612

A.11.5.4.1.2	Test parameters	4612

A.11.5.4.1.3	Test Requirements	4614

A.11.5.4.2	SSB based L1-RSRP measurement when DRX is used	4614

A.11.5.4.2.1	Test Purpose and Environment	4614

A.11.5.4.2.2	Test parameters	4614

A.11.5.4.2.3	Test Requirements	4616

A.11.5.4.3	SSB based L1-RSRP measurement on SCC when DRX is not used	4616

A.11.5.4.3.1	Test Purpose and Environment	4616

A.11.5.4.3.2	Test parameters	4617

A.11.5.4.3.3	Test Requirements	4618

A.11.5.4.4	SSB based L1-RSRP measurement on SCC when DRX is used	4618

A.11.5.4.4.1	Test Purpose and Environment	4618

A.11.5.4.4.2	Test parameters	4619

A.11.5.4.4.3	Test Requirements	4620

A.11.6	Measurement performance	4620

A.11.6.1	SS-RSRP	4620

A.11.6.1.1	Intra-frequency measurement accuracy on a carrier frequency with CCA	4620

A.11.6.1.1.1	Test Purpose and Environment	4620

A.11.6.1.1.2	Test parameters	4621

A.11.6.1.1.3	Test Requirements	4622

A.11.6.1.2	Intra-frequency measurement accuracy on SCC on a carrier frequency with CCA	4622

A.11.6.1.2.1	Test Purpose and Environment	4622

A.11.6.1.2.2	Test parameters	4622

A.11.6.1.2.3	Test Requirements	4624

A.11.6.2	SS-RSRQ	4624

A.11.6.2.1	Intra-frequency measurement accuracy	4624

A.11.6.2.1.1	Test Purpose and Environment	4624

A.11.6.2.1.2	Test Parameters	4624

A.11.6.2.1.3	Test Requirements	4626

A.11.6.2.2	Inter-frequency measurement accuracy	4626

A.11.6.2.2.1	Test Purpose and Environment	4626

A.11.6.2.2.2	Test Parameters	4626

A.11.6.2.2.3	Test Requirements	4628

A.11.6.2.3	Intra-frequency measurement accuracy on SCC	4628

A.11.6.2.3.1	Test Purpose and Environment	4628

A.11.6.2.3.2	Test Parameters	4628

A.11.6.2.3.3	Test Requirements	4630

A.11.6.2.4	Inter-frequency measurement accuracy	4630

A.11.6.2.4.1	Test Purpose and Environment	4630

A.11.6.2.4.2	Test Parameters	4630

A.11.6.2.4.3	Test Requirements	4635

A.11.6.3	SS-SINR	4635

A.11.6.3.1	Intra-frequency measurement accuracy	4635

A.11.6.3.1.1	Test Purpose and Environment	4635

A.11.6.3.1.2	Test Parameters	4635

A.11.6.3.1.3	Test Requirements	4636

A.11.6.3.2	Inter-frequency measurement accuracy	4637

A.11.6.3.2.1	Test Purpose and Environment	4637

A.11.6.3.2.2	Test Parameters	4637

A.11.6.3.2.3	Test Requirements	4638

A.11.6.3.3	Intra-frequency measurement accuracy on SCC	4638

A.11.6.3.3.1	Test Purpose and Environment	4638

A.11.6.3.3.2	Test Parameters	4638

A.11.6.3.3.3	Test Requirements	4640

A.11.6.3.4	Inter-frequency measurement accuracy	4640

A.11.6.3.4.1	Test Purpose and Environment	4640

A.11.6.3.4.2	Test Parameters	4640

A.11.6.3.4.3	Test Requirements	4644

A.11.6.4	L1-RSRP measurement for beam reporting with CCA serving cell	4645

A.11.6.4.1	SSB based L1-RSRP measurement	4645

A.11.6.4.1.1	Test Purpose and Environment	4645

A.11.6.4.1.2	Test parameters	4645

A.11.6.4.1.3	Test Requirements	4646

A.11.6.5	RSSI	4646

A.11.6.5.1	Intra-frequency RSSI measurement accuracy on PCC with CCA	4646

A.11.6.5.1.1	Test Purpose and Environment	4646

A.11.6.5.1.2	Test parameters	4646

A.11.6.5.1.3	Test Requirements	4648

A.11.6.5.2	Intra-frequency RSSI measurement accuracy on SCC with CCA	4648

A.11.6.5.2.1	Test Purpose and Environment	4648

A.11.6.5.2.2	Test parameters	4648

A.11.6.5.2.3	Test Requirements	4650

A.11.6.5.3	Inter-frequency RSSI measurement accuracy on a carrier with CCA	4650

A.11.6.5.3.1	Test Purpose and Environment	4650

A.11.6.5.3.2	Test parameters	4650

A.11.6.5.3.3	Test Requirements	4651

A.11.6.6	Channel occupancy	4652

A.11.6.6.1	Intra-frequency channel occupancy measurement accuracy on PCC with CCA	4652

A.11.6.6.1.1	Test Purpose and Environment	4652

A.11.6.6.1.2	Test parameters	4652

A.11.6.6.1.3	Test Requirements	4653

A.11.6.6.2	Intra-frequency channel occupancy measurement accuracy on SCC with CCA	4653

A.11.6.6.2.1	Test Purpose and Environment	4653

A.11.6.6.2.2	Test parameters	4653

A.11.6.6.2.3	Test Requirements	4655

A.11.6.6.3	Inter-frequency channel occupancy measurement accuracy on a carrier with CCA	4655

A.11.6.6.3.1	Test Purpose and Environment	4655

A.11.6.6.3.2	Test parameters	4655

A.11.6.6.3.3	Test Requirements	4657

A.11.6.7	E-UTRAN RSRP	4657

A.11.6.8	E-UTRAN RSRQ	4657

A.11.6.9	E-UTRAN SINR	4657

A.12	E-UTRA Standalone Tests with at Least One NR Cell under CCA	4657

A.12.1	RRC\_IDLE state mobility	4657

A.12.1.1	Inter-RAT cell re-selection to NR on a carrier frequency with CCA	4657

A.12.1.1.1	E-UTRA Cell reselection to higher priority NR target Cell in FR1 when target cell is subject to CCA	4657

A.12.1.1.1.1	Test Purpose and Environment	4657

A.12.1.1.1.2	Test Requirements	4660

A.12.2	RRC\_CONNECTED state mobility	4661

A.12.2.1	Handover	4661

A.12.2.1.1	E-UTRAN - NR with CCA handover	4661

A.12.2.1.1.1	Test Purpose and Environment	4661

A.12.2.1.1.2	Test Requirements	4664

A.12.3	Void	4665

A.12.4	Measurement procedure	4665

A.12.4.1	E-UTRANNR inter-RAT SFTD measurements	4665

A.12.4.1.1	E-UTRA – NR Inter-RAT SFTD Measurement Delay with NR under CCA in non-DRX	4665

A.12.4.1.1.1	Test Purpose and Environment	4665

A.12.4.1.1.2	Test Requirements	4667

A.12.4.2	E-UTRANNR inter-RAT measurements on NR carrier frequency under CCA	4667

A.12.4.2.1	E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used	4667

A.12.4.2.1.1	Test Purpose and Environment	4667

A.12.4.2.1.2	Test Requirements	4671

A.12.4.2.2	E-UTRA-NR inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used	4671

A.12.4.2.2.1	Test Purpose and Environment	4671

A.12.4.2.2.2	Test Requirements	4674

A.12.4.2.3	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used	4674

A.12.4.2.3.1	Test Purpose and Environment	4674

A.12.4.2.3.2	Test Requirements	4678

A.12.4.2.4	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used	4678

A.12.4.2.4.1	Test Purpose and Environment	4678

A.12.4.2.4.2	Test Requirements	4681

A.12.4.2.5	Void	4682

A.12.4.2.6	Void	4682

A.12.5	Measurement performance	4682

A.12.5.1	E-UTRANNR SFTD	4682

A.12.5.1.1	Inter-RAT SFTD accuracy with NR target cell under CCA	4682

A.12.5.1.1.1	Test Purpose	4682

A.12.5.1.1.2	Test Environment	4682

A.12.5.1.1.3	Test Requirements	4684

A.12.5.2	Void	4684

A.12.5.3	Void	4684

A.12.5.4	Void	4684

A.12.5.5	Void	4685

A.12.5.6	Void	4685

A.13	NR Standalone Tests with NR SCell under CCA and All Other NR Cells in FR1	4689

A.13.1	Void	4689

A.13.1.1	Void	4689

A.13.1.2	Void	4689

A.13.2	Signalling characteristics	4689

A.13.2.1	Void	4689

A.13.2.2	SCell activation and deactivation delay	4689

A.13.2.2.1	SCell Activation and Deactivation of known SCell under CCA, 160 ms SCell measurement cycle	4689

A.13.2.2.1.1	Test Purpose and Environment	4689

A.13.2.2.1.2	Test Requirements	4692

A.13.2.2.2 SCell Activation and Deactivation of known SCell under CCA, 640 ms SCell measurement cycle	4692

A.13.2.2.2.1	Test Purpose and Environment	4692

A.13.2.2.2.2	Test Requirements	4693

A.13.2.2.3	SCell Activation and Deactivation of unknown SCell under CCA	4693

A.13.2.2.3.1	Test Purpose and Environment	4693

A.13.2.2.3.2	Test Requirements	4693

A.13.2.3	Void	4694

A.13.3	Measurement procedure	4694

A.13.3.1	Intra-frequency measurements	4694

A.13.3.1.1	Event-triggered reporting tests on SCC without gaps under non-DRX	4694

A.13.3.1.1.1	Test purpose and environment	4694

A.13.3.1.1.2	Test parameters	4694

A.13.3.1.1.3	Test Requirements	4697

A.13.3.1.2	Event-triggered reporting tests on SCC without gaps under DRX	4697

A.13.3.1.2.1	Test purpose and environment	4697

A.13.3.1.2.2	Test parameters	4697

A.13.3.1.2.3	Test Requirements	4700

A.13.3.1.3	Event-triggered reporting tests on SCC with per-UE gaps under non-DRX	4700

A.13.3.1.3.1	Test purpose and environment	4700

A.13.3.1.3.2	Test parameters	4700

A.13.3.1.3.3	Test Requirements	4703

A.13.3.1.4	Event-triggered reporting tests on SCC with per-UE gaps under DRX	4704

A.13.3.1.4.1	Test purpose and environment	4704

A.13.3.1.4.2	Test parameters	4704

A.13.3.1.4.3	Test Requirements	4707

A.13.3.1.5	Void	4707

A.13.3.1.6	Void	4707

A.13.3.2	Inter-frequency measurements	4707

A.13.3.2.1	Void	4707

A.13.3.2.2	Void	4707

A.13.3.2.3	Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is not used	4707

A.13.3.2.3.1	Test Purpose and Environment	4707

A.13.3.2.3.2	Test Requirements	4710

A.13.3.2.4	Event triggered reporting tests for FR1 with CCA without SSB time index detection when DRX is used	4711

A.13.3.2.4.1	Test Purpose and Environment	4711

A.13.3.2.4.2	Test Requirements	4714

A.13.3.2.5	Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is not used	4714

A.13.3.2.5.1	Test Purpose and Environment	4714

A.13.3.2.5.2	Test Requirements	4717

A.13.3.2.6	Event triggered reporting tests for FR1 with CCA with SSB time index detection when DRX is used	4717

A.13.3.2.6.1	Test Purpose and Environment	4717

A.13.3.2.6.2	Test Requirements	4721

A.13.3.3	L1-RSRP measurements for beam reporting	4721

A.13.3.3.1	SSB based L1-RSRP measurement when DRX is not used	4721

A.13.3.3.1.1	Test Purpose and Environment	4721

A.13.3.3.1.2	Test parameters	4721

A.13.3.3.1.3	Test Requirements	4723

A.13.3.3.2	SSB based L1-RSRP measurement when DRX is used	4724

A.13.3.3.2.1	Test Purpose and Environment	4724

A.13.3.3.2.2	Test parameters	4724

A.13.3.3.2.3	Test Requirements	4726

A.13.4	Measurement performance	4726

A.13.4.1	SS-RSRP	4726

A.13.4.1.1	Intra-frequency measurement accuracy on a carrier frequency with CCA	4726

A.13.4.1.1.1	Test Purpose and Environment	4726

A.13.4.1.1.2	Test parameters	4726

A.13.4.1.1.3	Test Requirements	4728

A.13.4.2	SS-RSRQ	4728

A.13.4.2.1	Intra-frequency measurement accuracy on SCC	4728

A.13.4.2.1.1	Test Purpose and Environment	4728

A.13.4.2.1.2	Test Parameters	4728

A.13.4.2.1.3	Test Requirements	4733

A.13.4.3	SS-SINR	4733

A.13.4.3.1	Intra-frequency measurement accuracy on SCC	4733

A.13.4.3.1.1	Test Purpose and Environment	4733

A.13.4.3.1.2	Test Parameters	4733

A.13.4.3.1.3	Test Requirements	4737

A.13.4.4	L1-RSRP measurement for beam reporting with CCA serving cell	4737

A.13.4.4.1	SSB based L1-RSRP measurement	4737

A.13.4.4.1.1	Test Purpose and Environment	4737

A.13.4.4.1.2	Test parameters	4738

A.13.4.4.1.3	Test Requirements	4740

A.13.4.5	RSSI	4740

A.13.4.5.1 	Intra-frequency RSSI measurement accuracy on a carrier with CCA	4740

A.13.4.5.1.1	Test Purpose and Environment	4740

A.13.4.5.1.2	Test parameters	4740

A.13.4.5.1.3	Test Requirements	4742

A.13.4.5.2	Inter-frequency RSSI measurement accuracy on a carrier with CCA	4742

A.13.4.5.2.1	Test Purpose and Environment	4742

A.13.4.5.2.2	Test parameters	4742

A.13.4.5.2.3	Test Requirements	4744

A.13.4.6	Channel occupancy	4744

A.13.4.6.1	Intra-frequency channel occupancy measurement accuracy on SCC with CCA	4744

A.13.4.6.1.1	Test Purpose and Environment	4744

A.13.4.6.1.2	Test parameters	4744

A.13.4.6.1.3	Test Requirements	4746

A.13.4.6.2	Inter-frequency channel occupancy measurement accuracy on a carrier with CCA	4746

A.13.4.6.2.1	Test Purpose and Environment	4746

A.13.4.6.2.2	Test parameters	4746

A.13.4.6.2.3	Test Requirements	4748

A.14	NR standalone tests for Satellite access	4748

A.14.1	RRC\_IDLE state mobility	4748

A.14.1.1	Cell reselection to FR1 intra-frequency NR case	4748

A.14.1.1.1	Test Purpose and Environment	4748

A.14.1.1.2	Test Parameters	4748

A.14.1.1.3	Test Requirements	4750

A.14.1.2	Cell reselection to FR1 intra-frequency NR cell for UE configured with the feature for enhanced requirements	4750

A.14.1.2.1	Test Purpose and Environment	4750

A.14.1.2.2	Test Parameters	4751

A.14.1.2.3	Test Requirements	4752

A.14.1.3	Time-based measurement initiation to FR1 intra-frequency NR cell reselection	4753

A.14.1.3.1	Test Purpose and Environment	4753

A.14.1.3.2	Test Parameters	4753

A.14.1.3.3	Test Requirements	4754

A.14.1.4	Location-based measurement initiation to FR1 intra-frequency NR cell reselection	4754

A.14.1.4.1	Test Purpose and Environment	4755

A.14.1.4.2	Test Parameters	4755

A.14.1.4.3	Test Requirements	4756

A.14.1.5	Cell reselection to FR1 inter-frequency NR case	4756

A.14.1.5.1	Test Purpose and Environment	4756

A.14.1.5.2	Test Parameters	4757

A.14.1.5.3	Test Requirements	4758

A.14.1.6	Cell re-selection to FR1 inter-frequency NR cell for UE configured with feature for enhanced requirements	4759

A.14.1.6.1	Test Purpose and Environment	4759

A.14.1.6.2	Test Parameters	4759

A.14.1.6.3	Test Requirements	4760

A.14.1.7	Time-based measurement initiation to FR1 inter-frequency cell reselection	4761

A.14.1.7.1	Test Purpose and Environment	4761

A.14.1.7.2	Test Parameters	4761

A.14.1.7.3	Test Requirements	4762

A.14.1.8	Location-based measurement initiation to FR1 inter-frequency NR cell reselection	4763

A.14.1.8.1	Test Purpose and Environment	4763

A.14.1.8.2	Test Parameters	4763

A.14.1.8.3	Test Requirements	4764

A.14.1.9	Cell reselection to FR1 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion	4764

A.14.1.9.1	Test Purpose and Environment	4764

A.14.1.9.2	Test Parameters	4765

A.14.1.9.3	Test Requirements	4766

A.14.1.10	Cell reselection to FR1 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion	4767

A.14.1.10.1	Test Purpose and Environment	4767

A.14.1.10.2	Test Parameters	4767

A.14.1.10.3	Test Requirements	4769

A.14.1.11	Cell reselection to FR1 inter-RAT for NR NTN carrier	4769

A.14.1.11.1	Test purpose and Environment	4769

A.14.1.11.2	Test parameters	4769

A.14.1.11.3	Test requirements	4771

A.14.1.12	Cell re-selection to FR1 inter-frequency NR case with TN carrier	4772

A.14.1.12.1	Test purpose and Environment	4772

A.14.1.12.2	Test parameters	4772

A.14.1.12.3	Test requirements	4773

A.14.2	RRC\_CONNECTED state mobility	4774

A.14.2.1	Handover	4774

A.14.2.1.1	Intra-frequency SAN Handover from FR1 to FR1	4774

A.14.2.1.1.1	Test Purpose and Environment	4774

A.14.2.1.1.2	Test Parameters	4774

A.14.2.1.1.3	Test Requirements	4776

A.14.2.1.2	Inter-frequency SAN Handover from FR1 to FR1	4776

A.14.2.1.2.1	Test Purpose and Environment	4776

A.14.2.1.2.2	Test Parameters	4776

A.14.2.1.2.3	Test Requirements	4778

A.14.2.1.3	Intra-frequency SAN time-based conditional Handover from FR1 to FR1	4778

A.14.2.1.3.1	Test Purpose and Environment	4778

A.14.2.1.3.2	Test Parameters	4778

A.14.2.1.3.3	Test Requirements	4780

A.14.2.1.4	Inter-frequency SAN time-based conditional Handover from FR1 to FR1	4780

A.14.2.1.4.1	Test Purpose and Environment	4780

A.14.2.1.4.2	Test Parameters	4780

A.14.2.1.4.3	Test Requirements	4782

A.14.2.1.5	Intra-frequency SAN distance-based conditional Handover from FR1 to FR1	4782

A.14.2.1.5.1	Test Purpose and Environment	4782

A.14.2.1.5.2	Test Parameters	4783

A.14.2.1.5.3	Test Requirements	4784

A.14.2.1.6	Inter-frequency SAN distance-based conditional Handover from FR1 to FR1	4785

A.14.2.1.6.1	Test Purpose and Environment	4785

A.14.2.1.6.2	Test Parameters	4785

A.14.2.1.6.3	Test Requirements	4787

A.14.2.1.7	Intra-frequency intra-satellite Handover from FR2-NTN to FR2-NTN	4787

A.14.2.1.7.1	Test Purpose and Environment	4787

A.14.2.1.7.2	Test Parameters	4787

A.14.2.1.7.3	Test Requirements	4789

A.14.2.1.8	Intra-frequency SAN Handover from FR1 to FR1	4789

A.14.2.1.8.1	Test Purpose and Environment	4789

A.14.2.1.8.2	Test Parameters	4790

A.14.2.1.8.3	Test Requirements	4791

A.14.2.1.9	Intra-frequency inter-satellite handover from FR2-NTN to FR2-NTN	4792

A.14.2.1.9.1	Test Purpose and Environment	4792

A.14.2.1.9.2	Test Parameters	4792

A.14.2.1.9.3	Test Requirements	4793

A.14.2.2	RRC Connection Mobility Control	4794

A.14.2.2.1	SA: RRC Re-establishment for SAN	4794

A.14.2.2.1.1	Intra-frequency RRC Re-establishment in FR1	4794

A.14.2.2.1.2	Inter-frequency RRC Re-establishment in FR1	4796

A.14.2.2.2	Random Access	4798

A.14.2.2.2.1	4-step RA type contention based random access test in FR1 for NR standalone	4798

A.14.2.2.2.1.1	Test Purpose and Environment	4798

A.14.2.2.2.1.2	Test Requirements	4800

A.14.2.2.2.2	4-step RA type non-contention based random access test in FR1 for NR standalone	4801

A.14.2.2.2.2.1	Test Purpose and Environment	4801

A.14.2.2.2.2.2	Test Requirements	4803

A.14.2.2.3	RRC Connection Release with Redirection	4804

A.14.2.2.3.1	Redirection from NR in FR1 to NR in FR1	4804

A.14.2.2.3.1.1	Test Purpose and Environment	4804

A.14.2.2.3.1.2	Test Parameters	4804

A.14.2.2.3.1.3	Test Requirements	4805

A.14.2.2.4	RACH-based Hard Satellite switching with re-synchronization from FR1 to FR1	4806

A.14.2.2.4.1	Test Purpose and Environment	4806

A.14.2.2.4.2	Test Parameters	4806

A.14.2.2.4.3	Test Requirements	4808

A.14.2.2.5	RACH-less Soft Satellite switching with re-synchronization from FR1 to FR1	4808

A.14.2.2.5.1	Test Purpose and Environment	4808

A.14.2.2.5.2	Test Parameters	4808

A.14.2.2.5.3	Test Requirements	4810

A.14.2.3	Intra-frequency SAN time-based conditional Handover without L3 measurement criteria from FR1 to FR1	4810

A.14.2.3.1	Test Purpose and Environment	4810

A.14.2.3.2	Test Parameters	4810

A.14.2.3.3	Test Requirements	4812

A.14.2.4	Inter-frequency SAN time-based conditional Handover without L3 measurement criteria from FR1 to FR1	4812

A.14.2.4.1	Test Purpose and Environment	4812

A.14.2.4.2	Test Parameters	4812

A.14.2.4.3	Test Requirements	4814

A.14.3	Timing for Satellite Access	4814

A.14.3.1	UE transmit timing for Satellite Access	4814

A.14.3.1.1	NR UE Transmit Timing Test for FR1	4814

A.14.3.1.1.1	Test Purpose and environment	4814

A.14.3.1.1.2	Test requirements	4816

A.14.3.1.2	NR UE Transmit Timing Test for FR2-NTN	4817

A.14.3.1.2.1	Test Purpose and environment	4817

A.14.3.1.2.2	Test requirements	4819

A.14.3.2	Timing advance for satellite access	4819

A.14.3.2.1	SA FR1 timing advance adjustment accuracy	4819

A.14.3.2.1.1	Test Purpose and Environment	4819

A.14.3.2.1.2	Test Parameters	4820

A.14.3.2.1.3	Test Requirements	4822

A.14.3.2.3	SA FR2-NTN timing advance adjustment accuracy	4822

A.14.3.2.3.1	Test Purpose and Environment	4822

A.14.3.2.3.2	Test Parameters	4822

A.14.3.2.1.3	Test Requirements	4825

A.14.4	Signalling characteristics	4825

A.14.4.1	Radio link Monitoring	4825

A.14.4.1.1	Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode	4825

A.14.4.1.1.1	Test Purpose and Environment	4825

A.14.4.1.1.2	Test Requirements	4827

A.14.4.1.2	Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in non-DRX mode	4828

A.14.4.1.2.1	Test Purpose and Environment	4828

A.14.4.1.2.2	Test Requirements	4830

A.14.4.1.3	Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode	4830

A.14.4.1.3.1	Test Purpose and Environment	4830

A.14.4.1.3.2	Test Requirements	4832

A.14.4.1.4	Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with SSB-based RLM RS in DRX mode	4833

A.14.4.1.4.1	Test Purpose and Environment	4833

A.14.4.1.4.2	Test Requirements	4835

A.14.4.1.5	Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode	4835

A.14.4.1.5.1	Test Purpose and Environment	4835

A.14.4.1.5.2	Test Requirements	4838

A.14.4.1.6	Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in non-DRX mode	4838

A.14.4.1.6.1	Test Purpose and Environment	4838

A.14.4.1.6.2	Test Requirements	4841

A.14.4.1.7	Radio Link Monitoring Out-of-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode	4841

A.14.4.1.7.1	Test Purpose and Environment	4841

A.14.4.1.7.2	Test Requirements	4844

A.14.4.1.8	Radio Link Monitoring In-sync Test for FR1 SAN PCell configured with CSI-RS-based RLM in DRX mode	4844

A.14.4.1.8.1	Test Purpose and Environment	4844

A.14.4.1.8.2	Test Requirements	4847

A.14.4.1.9	Radio Link Monitoring Out-of-sync Test for FR2 SAN PCell configured with SSB-based RLM RS in non-DRX mode	4847

A.14.4.1.9.1	Test Purpose and Environment	4847

A.14.4.1.9.2	Test Requirements	4849

A.14.4.1.10	Radio Link Monitoring In-sync Test for FR2 SAN PCell configured with SSB-based RLM RS in non-DRX mode	4850

A.14.4.1.10.1	Test Purpose and Environment	4850

A.14.4.1.10.2	Test Requirements	4852

A.14.4.2	Beam Failure Detection and Link recovery procedures for satellite access	4853

A.14.4.2.1	Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in non-DRX mode	4853

A.14.4.2.1.1	Test Purpose and Environment	4853

A.14.4.2.1.2	Test Requirements	4855

A.14.4.2.2	Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with SSB-based BFD and LR in DRX mode	4856

A.14.4.2.2.1	Test Purpose and Environment	4856

A.14.4.2.2.2	Test Requirements	4858

A.14.4.2.3	Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in non-DRX mode	4859

A.14.4.2.3.1	Test Purpose and Environment	4859

A.14.4.2.3.2	Test Requirements	4861

A.14.4.2.4	Beam Failure Detection and Link Recovery Test for FR1 PCell for satellite access configured with CSI-RS-based BFD and LR in DRX mode	4862

A.14.4.2.4.1	Test Purpose and Environment	4862

A.14.4.2.4.2	Test Requirements	4864

A.14.4.2.5	Void	4865

A.14.4.2.6	Void	4865

A.14.4.3	Active BWP switch for satellite access	4865

A.14.4.3.1	DCI-based and Timer-based Active BWP Switch	4865

A.14.4.3.1.1	NR FR1 DL active BWP switch with non-DRX in SA	4865

A.14.4.3.1.1.1	Test Purpose and Environment	4865

A.14.4.3.1.1.2	Test Requirements	4867

A.14.4.3.2	RRC-based Active BWP Switch	4867

A.14.4.3.2.1	NR FR1 DL active BWP switch of Cell with non-DRX in SA	4867

A.14.4.3.2.1.1	Test Purpose and Environment	4867

A.14.4.3.2.1.2	Test Requirements	4869

A.14.4.4	UE specific CBW change for satellite access	4869

A.14.4.4.1	UE specific CBW change on PCell in FR1 in non-DRX	4869

A.14.4.4.1.1	Test Purpose and Environment	4869

A.14.4.4.1.2	Test Requirements	4871

A.14.4.5	Pathloss reference signal switching delay	4872

A.14.4.5.1	MAC-CE based pathloss reference signal switch delay	4872

A.14.4.5.1.1	Test Purpose and Environment	4872

A.14.4.5.1.2	Test Requirements	4874

A.14.5	Measurement procedure	4874

A.14.5.1	Intra-frequency Measurements	4874

A.14.5.1.1	SA event triggered reporting tests without gap under non-DRX	4874

A.14.5.1.1.1	Test purpose and Environment	4874

A.14.5.1.1.2	Test parameters	4874

A.14.5.1.1.3	Test Requirements	4876

A.14.5.1.2	SA event triggered reporting tests without gap under DRX	4876

A.14.5.1.2.1	Test purpose and Environment	4876

A.14.5.1.2.2	Test parameters	4876

A.14.5.1.2.3	Test Requirements	4878

A.14.5.1.3	SA event triggered reporting tests without gap under non-DRX with SSB index reading	4878

A.14.5.1.3.1	Test purpose and Environment	4878

A.14.5.1.3.2	Test parameters	4878

A.14.5.1.3.3	Test Requirements	4880

A.14.5.1.4	SA event triggered reporting tests with single measurement gap under non-DRX for satellite access	4880

A.14.5.1.4.1	Test purpose and Environment	4880

A.14.5.1.4.2	Test parameters	4880

A.14.5.1.4.3	Test Requirements	4882

A.14.5.1.5	SA event triggered reporting tests with FNO concurrent gaps under DRX for satellite access	4882

A.14.5.1.5.1	Test purpose and Environment	4882

A.14.5.1.5.2	Test parameters	4882

A.15.5.1.5.3	Test Requirements	4884

A.14.5.1.6	SA event triggered reporting tests with PPO concurrent gaps under non-DRX with SSB index reading for satellite access	4884

A.14.5.1.6.1	Test purpose and Environment	4884

A.14.5.1.6.2	Test parameters	4884

A.14.5.1.6.3	Test Requirements	4886

A.14.5.1.7	SA event triggered reporting test with SSB time index reading without gap under non-DRX for FR2-NTN	4886

A.14.5.1.7.1	Test purpose and Environment	4886

A.14.5.1.7.2	Test parameters	4886

A.14.5.1.7.3	Test Requirements	4888

A.14.5.2	Inter-frequency Measurements	4888

A.14.5.2.1	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with single gap for satellite access	4888

A.14.5.2.1.1	Test Purpose and Environment	4888

A.14.5.2.1.2	Test Requirements	4890

A.14.5.2.2	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used with single gap for satellite access	4890

A.14.5.2.2.1	Test Purpose and Environment	4890

A.14.5.2.2.2	Test Requirements	4893

A.14.5.2.3	SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used with single gap for satellite access	4893

A.14.5.2.3.1	Test Purpose and Environment	4893

A.14.5.2.3.2	Test Requirements	4895

A.14.5.2.4	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in fully non-overlapped for satellite access	4895

A.14.5.2.4.1	Test Purpose and Environment	4895

A.14.5.2.4.2	Test Requirements	4897

A.14.5.2.5	void	4897

A.14.5.2.5.1	void	4897

A.14.5.2.5.2	void	4898

A.14.5.2.6	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used with two gaps in partially partial overalpping for satellite access	4898

A.14.5.2.6.1	Test Purpose and Environment	4898

A.14.5.2.6.2	Test Requirements	4900

A.14.5.2.7	Event triggered reporting test without gap under non-DRX	4900

A.14.5.2.7.1	Test purpose and Environment	4900

A.14.5.2.7.2	Test parameters	4900

A.14.5.2.7.3	Test Requirements	4901

A.14.5.2.8	Event triggered reporting tests without gap under DRX	4902

A.14.5.2.8.1	Test purpose and Environment	4902

A.14.5.2.8.2	Test parameters	4902

A.14.5.2.8.3	Test Requirements	4903

A.14.5.3	L1-RSRP measurement for beam reporting for satellite access	4903

A.14.5.3.1	SSB based L1-RSRP measurement for satellite access when DRX is not used	4903

A.14.5.3.1.1	Test Purpose and Environment	4904

A.14.5.3.1.2	Test parameters	4904

A.14.5.3.1.3	Test Requirements	4905

A.14.5.3.2	SSB based L1-RSRP measurement for satellite access when DRX is used	4905

A.14.5.3.2.1	Test Purpose and Environment	4905

A.14.5.3.2.2	Test parameters	4906

A.14.5.3.2.3	Test Requirements	4907

A.14.5.3.3	CSI-RS based L1-RSRP measurement for satellite access when DRX is not used	4907

A.14.5.3.3.1	Test Purpose and Environment	4907

A.14.5.3.3.2	Test parameters	4908

A.14.5.3.3.3	Test Requirements	4909

A.14.5.3.4	CSI-RS based L1-RSRP measurement for satellite access when DRX is used	4909

A.14.5.3.4.1	Test Purpose and Environment	4909

A.14.5.3.4.2	Test parameters	4909

A.14.5.3.4.3	Test Requirements	4911

A.14.5.3.5	SSB based L1-RSRP measurement when DRX is not used in FR2-NTN	4911

A.14.5.3.5.1	Test Purpose and Environment	4911

A.14.5.3.5.2	Test parameters	4911

A.14.5.3.5.3	Test Requirements	4913

A.14.6	Measurement Performance requirements	4913

A.14.6.1	SS-RSRP for SAN	4913

A.14.6.1.1	SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell	4913

A.14.6.1.1.1	Test Purpose and Environment	4913

A.14.6.1.1.2	Test parameters	4913

A.14.6.1.1.3	Test Requirements	4915

A.14.6.1.2	SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell	4915

A.14.6.1.2.1	Test Purpose and Environment	4915

A.14.6.1.2.2	Test parameters	4915

A.14.6.1.2.3	Test Requirements	4916

A.14.6.1.3	SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	4916

A.14.6.1.3.1	Test Purpose and Environment	4916

A.14.6.1.3.2	Test parameters	4917

A.14.6.1.3.3	Test Requirements	4918

A.14.6.2	SS-RSRQ	4919

A.14.6.2.1	SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access	4919

A.14.6.2.1.1	Test Purpose and Environment	4919

A.14.6.2.1.2	Test Parameters	4919

A.14.6.2.1.3	Test Requirements	4920

A.14.6.2.2	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for satellite access	4920

A.14.6.2.2.1	Test Purpose and Environment	4920

A.14.6.2.2.2	Test Parameters	4920

A.14.6.2.2.3	Test Requirements	4922

A.14.6.3	SS-SINR	4922

A.14.6.3.1	SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	4922

A.14.6.3.1.1	Test Purpose and Environment	4922

A.14.6.3.1.2	Test Parameters	4922

A.14.6.3.1.3	Test Requirements	4923

A.14.6.3.2	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	4923

A.14.6.3.2.1	Test Purpose and Environment	4923

A.14.6.3.2.2	Test Parameters	4923

A.14.6.3.2.3	Test Requirements	4924

A.14.6.4	L1-RSRP measurement for beam reporting	4925

A.14.6.4.1	SSB based L1-RSRP measurement	4925

A.14.6.4.1.1	Test Purpose and Environment	4925

A.14.6.4.1.2	Test parameters	4925

A.14.6.4.1.3	Test Requirements	4926

A.14.6.4.2	CSI-RS based L1-RSRP measurement on resource set with repetition off	4926

A.14.6.4.2.1	Test Purpose and Environment	4926

A.14.6.4.2.2	Test parameters	4926

A.14.6.4.2.3	Test Requirements	4927

A.14.6.4.3	SSB based L1-RSRP measurement for VSAT UE in FR2-NTN when DRX is not used	4928

A.14.6.4.3.1	Test Purpose and Environment	4928

A.14.6.4.3.2	Test parameters	4928

A.14.6.4.3.3	Test Requirements	4929

A.15	NR standalone tests with one or more NR cells in FR2-2	4941

A.15.1	SA: RRC\_IDLE state mobility	4941

A.15.1.1	Cell re-selection to NR	4941

A.15.1.1.1	Cell re-selection to FR2-2 intra-frequency NR case	4941

A.15.1.1.1.1	Test Purpose and Environment	4941

A.15.1.1.1.2	Test Parameters	4941

A.15.1.1.1.3	Test Requirements	4943

A.15.1.2	Cell re-selection to FR2-2 inter-frequency NR case	4943

A.15.1.2.1	Test Purpose and Environment	4943

A.15.1.2.2	Test Parameters	4944

A.15.1.2.3	Test Requirements	4946

A.15.1.3	Cell re-selection to FR2-2 intra-frequency NR case for UE fulfilling low mobility relaxed measurement criterion	4946

A.15.1.3.1	Test Purpose and Environment	4946

A.15.1.3.2	Test Parameters	4946

A.15.1.3.3	Test Requirements	4948

A.15.1.4	Cell re-selection to FR2-2 intra-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion	4949

A.15.1.4.1	Test Purpose and Environment	4949

A.15.1.4.2	Test Parameters	4949

A.15.1.4.3	Test Requirements	4951

A.15.1.5	Cell re-selection to FR2-2 inter-frequency NR case for UE fulfilling low mobility relaxed measurement criterion	4951

A.15.1.5.1	Test Purpose and Environment	4951

A.15.1.5.2	Test Parameters	4951

A.15.1.5.3	Test Requirements	4953

A.15.1.6	Cell re-selection to FR2-2 inter-frequency NR case for UE fulfilling not-at-cell edge relaxed measurement criterion	4954

A.15.1.6.1	Test Purpose and Environment	4954

A.15.1.6.2	Test Parameters	4954

A.15.1.6.3	Test Requirements	4956

A.15.2	Signaling characteristics	4956

A.15.2.1	SCell Activation and Deactivation Delay	4956

A.15.2.1.1	SCell Activation and deactivation for SCell in FR2-2 intra-band in non-DRX	4956

A.15.2.1.1.1	Test Purpose and Environment	4956

A.15.2.1.1.2	Test Requirements	4958

A.15.2.1.2	SCell Activation and deactivation for FR1+FR2-2 inter-band with target SCell in FR2-2	4958

A.15.2.1.2.1	Test Purpose and Environment	4958

A.15.2.1.2.2	Test Requirements	4961

A.15.2.1.3	SCell Activation and deactivation for SCell in FR2-2 inter-band in non-DRX	4961

A.15.2.1.3.1	Test Purpose and Environment	4962

A.15.2.1.3.2	Test Requirements	4964

A.15.2.1.4	Direct SCell activation at SCell addition of known SCell in FR2-2	4965

A.15.2.1.4.1	Test Purpose and Environment	4965

A.15.2.1.4.2	Test Requirements	4967

A.15.2.1.5	Direct SCell activation at handover with known SCell in FR2-2	4968

A.15.2.1.5.1	Test Purpose and Environment	4968

A.15.2.1.5.2	Test Requirements	4970

A.15.3	RRC\_CONNECTED state mobility	4971

A.15.3.1	Handover	4971

A.15.3.1.1	Intra-frequency handover from FR2-2 carrier with CCA to FR2-2 carrier with CCA; unknown target cell	4971

A.15.3.1.1.1	Test Purpose and Environment	4971

A.15.3.1.1.2	Test Parameters	4971

A.15.3.1.1.3	Test Requirements	4973

A.15.3.1.2	Inter-frequency handover from FR1 to FR2-2 carrier with CCA; unknown target cell	4974

A.15.3.1.2.1	Test Purpose and Environment	4974

A.15.3.1.2.2	Test Parameters	4974

A.15.3.1.2.3	Test Requirements	4976

A.15.4	Measurement procedure	4976

A.15.4.1	Intra-frequency Measurements	4976

A.15.4.1.1	SA event triggered reporting test without gap under non-DRX for FR2-2 with CCA	4976

A.15.4.1.1.1	Test purpose and Environment	4976

A.15.4.1.1.2	Test Requirements	4979

A.15.4.2	Inter-frequency Measurements	4980

A.15.4.2.1	SA event triggered reporting tests for FR2-2 with CCA without SSB time index detection when DRX is not used (PCell in FR2-2)	4980

A.15.4.2.1.1	Test Purpose and Environment	4980

A.15.4.2.1.2	Test Requirements	4982

A.16	NR standalone tests with all NR cells in FR1 for RedCap	4983

A.16.1	SA: RRC\_IDLE state mobility for RedCap	4983

A.16.1.1	Cell re-selection to NR	4983

A.16.1.1.1	Cell re-selection to FR1 intra-frequency NR case for 1 Rx UE	4983

A.16.1.1.1.1	Test Purpose and Environment	4983

A.16.1.1.1.2	Test Parameters	4983

A.16.1.1.1.3	Test Requirements	4985

A.16.1.1.2	Cell re-selection to FR1 intra-frequency NR case for 2 Rx UE	4986

A.16.1.1.2.1	Test Purpose and Environment	4986

A.16.1.1.2.2	Test Parameters	4986

A.16.1.1.2.3	Test Requirements	4988

A.16.1.1.3	Cell re-selection to FR1 inter-frequency NR case for 1 Rx UE	4988

A.16.1.1.3.1	Test Purpose and Environment	4988

A.16.1.1.3.2	Test Parameters	4988

A.16.1.1.3.3	Test Requirements	4991

A.16.1.1.4	Cell re-selection to FR1 inter-frequency NR case for 2 Rx UE	4991

A.16.1.1.4.1	Test Purpose and Environment	4991

A.16.1.1.4.2	Test Parameters	4991

A.16.1.1.4.3	Test Requirements	4994

A.16.1.1.5	Cell re-selection to FR1 intra-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 1 Rx UE	4994

A.16.1.1.5.1	Test Purpose and Environment	4994

A.16.1.1.5.2	Test Parameters	4994

A.16.1.1.5.3	Test Requirements	4997

A.16.1.1.6	Cell re-selection to FR1 intra-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE	4997

A.16.1.1.6.1	Test Purpose and Environment	4997

A.16.1.1.6.2	Test Parameters	4997

A.16.1.1.6.3	Test Requirements	4999

A.16.1.1.7	Cell re-selection to FR1 inter-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 1 Rx UE	5000

A.16.1.1.7.1	Test Purpose and Environment	5000

A.16.1.1.7.2	Test Parameters	5000

A.16.1.1.7.3	Test Requirements	5002

A.16.1.1.8	Cell re-selection to FR1 inter-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE	5003

A.16.1.1.8.1	Test Purpose and Environment	5003

A.16.1.1.8.2	Test Parameters	5003

A.16.1.1.8.3	Test Requirements	5005

A.16.1.2	Inter-RAT E-UTRAN cell re-selection for RedCap	5006

A.16.1.2.1	Cell re-selection to higher priority E-UTRAN for 1 RX	5006

A.16.1.2.1.1	Test Purpose and Environment	5006

A.16.1.2.1.2	Test Parameters	5006

A.16.1.2.1.3	Test Requirements	5009

A.16.1.2.2	Cell re-selection to higher priority E-UTRAN for 2 RX	5009

A.16.1.2.2.1	Test Purpose and Environment	5009

A.16.1.2.2.2	Test Parameters	5009

A.16.1.2.2.3	Test Requirements	5012

A.16.1.2.3.1	Test Purpose and Environment	5012

A. 16.1.2.3.2	Test Parameters	5012

A.16.1.2.3.3	Test Requirements	5015

A.16.1.2.4.1	Test Purpose and Environment	5015

A.16.1.2.4.2	Test Parameters	5015

A.16.1.3.1.3	Test Requirements	5018

A.16.1.2.5	Cell re-selection to lower priority E-UTRAN for UE fulfilling stationary relaxed measurement criterion for 1 Rx UE	5018

A.16.1.2.5.1	Test Purpose and Environment	5018

A.16.1.2.5.2	Test Parameters	5018

A.16.1.2.5.3	Test Requirements	5021

A.16.1.2.6	Cell re-selection to lower priority E-UTRAN for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE	5021

A.16.1.2.6.1	Test Purpose and Environment	5021

A.16.1.2.6.2	Test Parameters	5022

A.16.1.2.6.3	Test Requirements	5024

A.16.2	SA: RRC\_INACTIVE state mobility for RedCap	5025

A.16.2.1	Configured Grant based Small Data Transmissions (CG-SDT) for RedCap	5025

A.16.2.1.1	NR UE CG-SDT Test in FR1 for 1 Rx RedCap UE	5025

A.16.2.1.1.1	Test purpose and Environment	5025

A.16.2.1.1.2	Test Parameters	5026

A.16.2.1.1.3	Test requirements	5028

A.16.2.1.2	NR UE CG-SDT Test in FR1 for 2 Rx RedCap UE	5028

A.16.2.1.2.1	Test purpose and Environment	5028

A.16.2.1.2.2	Test Parameters	5030

A.16.2.1.2.3	Test requirements	5031

A.16.2.2	Cell Reselection for Positioning	5032

A.16.2.2.1	Cell re-selection to FR1 intra-frequency NR case with RRC\_INACTIVE eDRX and positioning SRS	5032

A.16.2.2.1.1	Test Purpose and Environment	5032

A.16.2.2.1.2	Test Parameters	5032

A.16.2.2.1.3	Test Requirements	5035

A.16.3	RRC\_CONNECTED state mobility for RedCap	5035

A.16.3.1	Handover	5035

A.16.3.1.1	Intra-frequency handover from FR1 to FR1; known target cell for 1 Rx UE	5035

A.16.3.1.1.1	Test Purpose and Environment	5035

A.16.3.1.1.2	Test Parameters	5035

A.16.3.1.1.3	Test Requirements	5037

A.16.3.1.2	Intra-frequency handover from FR1 to FR1; known target cell for 2 Rx UE	5037

A.16.3.1.2.1	Test Purpose and Environment	5037

A.16.3.1.2.2	Test Parameters	5037

A.16.3.1.2.3	Test Requirements	5039

A.16.3.1.3	Intra-frequency handover from FR1 to FR1; unknown target cell for 1 Rx UE	5039

A.16.3.1.3.1	Test Purpose and Environment	5039

A.16.3.1.3.2	Test Parameters	5040

A.16.3.1.3.3	Test Requirements	5042

A.16.3.1.4	Intra-frequency handover from FR1 to FR1; unknown target cell for 2 Rx UE	5042

A.16.3.1.4.1	Test Purpose and Environment	5042

A.16.3.1.4.2	Test Parameters	5042

A.16.3.1.5	Inter-frequency handover from FR1 to FR1; unknown target cell for 1 Rx UE	5044

A.16.3.1.5.1	Test Purpose and Environment	5044

A.16.3.1.5.2	Test Parameters	5044

A.16.3.1.5.3	Test Requirements	5046

A.16.3.1.6	Inter-frequency handover from FR1 to FR1; unknown target cell for 2 Rx UE	5047

A.16.3.1.6.1	Test Purpose and Environment	5047

A.16.3.1.6.2	Test Parameters	5047

A.16.3.1.6.3	Test Requirements	5049

A.16.3.1.7	SA NR - E-UTRAN handover for 1 Rx UE	5049

A.16.3.1.7.1	Test Purpose and Environment	5049

A.16.3.1.7.2	Test Requirements	5053

A.16.3.1.8	SA NR - E-UTRAN handover for 2 Rx UE	5053

A.16.3.1.8.1	Test Purpose and Environment	5053

A.16.3.1.8.2	Test Requirements	5056

A.16.3.1.9	SA NR - E-UTRAN handover with unknown target cell for 1 Rx UE	5056

A.16.3.1.9.1	Test Purpose and Environment	5056

A.16.3.1.9.2	Test Requirements	5059

A.16.3.1.10	SA NR - E-UTRAN handover with unknown target cell for 2 Rx UE	5059

A.16.3.1.10.1	Test Purpose and Environment	5059

A.16.3.1.10.2	Test Requirements	5063

A.16.3.2	RRC Connection Mobility Control	5063

A.16.3.2.1	SA: RRC Re-establishment	5063

A.16.3.2.1.1	Intra-frequency RRC Re-establishment in FR1 for 1 Rx UE	5063

A.16.3.2.1.2	Intra-frequency RRC Re-establishment in FR1 for 2 Rx UE	5066

A.16.3.2.1.3	Inter-frequency RRC Re-establishment in FR1 for 1 Rx UE	5068

A.16.3.2.1.4	Inter-frequency RRC Re-establishment in FR1 for 2 Rx UE	5071

A.16.3.2.1.5	Intra-frequency RRC Re-establishment in FR1 for 1 Rx UE without serving cell timing	5074

A.16.3.2.1.6	Intra-frequency RRC Re-establishment in FR1 for 2 Rx UE without serving cell timing	5077

A.16.3.2.2	Random Access	5080

A.16.3.2.2.1	4-step RA type contention based random access test in FR1 for NR standalone for 1 Rx UE	5080

A.16.3.2.2.2	4-step RA type contention based random access test in FR1 for NR standalone for 2 Rx UE	5083

A.16.3.2.2.3	4-step RA type non-contention based random access test in FR1 for NR standalone for 1 Rx UE	5086

A.16.3.2.2.4	4-step RA type non-contention based random access test in FR1 for NR standalone for 2 Rx UE	5089

A.16.3.2.2.5	2-step RA type contention based random access test in FR1 for NR standalone for 1 Rx UE	5093

A.16.3.2.2.6	2-step RA type contention based random access test in FR1 for NR standalone for 2 Rx UE	5096

A.16.3.2.2.7	2-step RA type non-contention based test in FR1 for NR standalone for 1 RX UE	5098

A.16.3.2.2.8	2-step RA type non-contention based test in FR1 for NR standalone for 2 RX UE	5101

A.16.3.2.3	SA: RRC Connection Release with Redirection	5104

A.16.3.2.3.1	Redirection from NR in FR1 to NR in FR1 for 1 Rx UE	5104

A.16.3.2.3.2	Redirection from NR in FR1 to NR in FR1 for 2 Rx UE	5106

A.16.3.2.3.3	Redirection from NR in FR1 to E-UTRAN for 1 Rx UE	5109

A.16.3.2.3.4	Redirection from NR in FR1 to E-UTRAN for 2 Rx UE	5112

A.16.4	Timing for RedCap	5116

A.16.4.1	UE transmit timing	5116

A.16.4.1.1	NR UE Transmit Timing Test for FR1 for 1 Rx RedCap UE	5116

A.16.4.1.1.1	Test Purpose and environment	5116

A.16.4.1.1.2	Test requirements	5118

A.16.4.1.2	NR UE Transmit Timing Test for FR1 for 2 Rx RedCap UE	5118

A.16.4.1.2.1	Test Purpose and environment	5118

A.16.4.1.2.2	Test requirements	5120

A.16.4.2	Void	5120

A.16.4.3	Timing advance	5120

A.16.4.3.1	SA FR1 timing advance adjustment accuracy for 1 Rx UE	5120

A.16.4.3.1.1	Test Purpose and Environment	5120

A.16.4.3.1.2	Test Parameters	5120

A.16.4.3.1.3	Test Requirements	5122

A.16.4.3.2	SA FR1 timing advance adjustment accuracy for 2 Rx UE	5123

A.16.4.3.2.1	Test Purpose and Environment	5123

A.16.4.3.2.2	Test Parameters	5123

A.16.4.3.2.3	Test Requirements	5125

A.16.5	Signalling characteristics for RedCap	5125

A.16.5.1	Radio link Monitoring	5125

A.16.5.1.1	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for 1 Rx UE	5125

A.16.5.1.1.1	Test Purpose and Environment	5125

A.16.5.1.1.2	Test Requirements	5128

A.16.5.1.2	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for 2 Rx UE	5128

A.16.5.1.2.1	Test Purpose and Environment	5128

A.16.5.1.2.2	Test Requirements	5131

A.16.5.1.3	Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for 1 Rx UE	5131

A.16.5.1.3.1	Test Purpose and Environment	5131

A.16.5.1.3.2	Test Requirements	5134

A.16.5.1.4	Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode for 2 Rx UE	5134

A.16.5.1.4.1	Test Purpose and Environment	5134

A.16.5.1.4.2	Test Requirements	5137

A.16.5.1.5	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for 1 Rx UE	5137

A.16.5.1.5.1	Test Purpose and Environment	5137

A.16.5.1.5.2	Test Requirements	5140

A.16.5.1.6	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for 2 Rx UE	5140

A.16.5.1.6.1	Test Purpose and Environment	5140

A.16.5.1.6.2	Test Requirements	5143

A.16.5.1.7	Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for 1 Rx UE	5143

A.16.5.1.7.1	Test Purpose and Environment	5143

A.16.5.1.7.2	Test Requirements	5146

A.16.5.1.8	Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in DRX mode for 2 Rx UE	5146

A.16.5.1.8.1	Test Purpose and Environment	5146

A.16.5.1.8.2	Test Requirements	5149

A.16.5.1.9	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode for 1 Rx UE	5149

A.16.5.1.9.1	Test Purpose and Environment	5149

A.16.5.1.9.2	Test Requirements	5152

A.16.5.1.10	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode for 2 Rx UE	5152

A.16.5.1.10.1	Test Purpose and Environment	5152

A.16.5.1.10.2	Test Requirements	5155

A.16.5.1.11	Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode for 1 Rx UE	5155

A.16.5.1.11.1	Test Purpose and Environment	5155

A.16.5.1.11.2	Test Requirements	5158

A.16.5.1.12	Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode for 2 Rx UE	5158

A.16.5.1.12.1	Test Purpose and Environment	5158

A.16.5.1.12.2	Test Requirements	5161

A.16.5.1.13	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for 1 Rx UE	5162

A.16.5.1.13.1	Test Purpose and Environment	5162

A.16.5.1.13.2	Test Requirements	5164

A.16.5.1.14	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for 2 Rx UE	5165

A.16.5.1.14.1	Test Purpose and Environment	5165

A.16.5.1.14.2	Test Requirements	5167

A.16.5.1.15	Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for 1 Rx UE	5168

A.16.5.1.15.1	Test Purpose and Environment	5168

A.16.5.1.15.2	Test Requirements	5171

A.16.5.1.16	Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in DRX mode for 2 Rx UE	5171

A.16.5.1.16.1	Test Purpose and Environment	5171

A.16.5.1.16.2	Test Requirements	5174

A.16.5.2	Beam Failure Detection and Link recovery procedures	5174

A.16.5.2.1	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode for 1 Rx UE	5174

A.16.5.2.1.1	Test Purpose and Environment	5174

A.16.5.2.1.2	Test Requirements	5177

A.16.5.2.2	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode for 2 Rx UE	5178

A.16.5.2.2.1	Test Purpose and Environment	5178

A.16.5.2.2.2	Test Requirements	5181

A.16.5.2.3	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode for 1 Rx UE	5181

A.16.5.2.3.1	Test Purpose and Environment	5181

A.16.5.2.3.2	Test Requirements	5184

A.16.5.2.4	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in DRX mode for 2 Rx UE	5185

A.16.5.2.4.1	Test Purpose and Environment	5185

A.16.5.2.4.2	Test Requirements	5188

A.16.5.2.5	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode for 1 Rx UE	5188

A.16.5.2.5.1	Test Purpose and Environment	5188

A.16.5.2.5.2	Test Requirements	5191

A.16.5.2.6	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode for 2 Rx UE	5192

A.16.5.2.6.1	Test Purpose and Environment	5192

A.16.5.2.6.2	Test Requirements	5195

A.16.5.2.7	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode for 1 Rx UE	5195

A.16.5.2.7.1	Test Purpose and Environment	5195

A.16.5.2.7.2	Test Requirements	5198

A.16.5.2.8	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in DRX mode for 2 Rx UE	5199

A.16.5.2.8.1	Test Purpose and Environment	5199

A.16.5.2.8.2	Test Requirements	5202

A.16.5.3	Active BWP switch	5202

A.16.5.3.1	DCI-based and Timer-based Active BWP Switch	5202

A.16.5.3.1.1	NR FR1 DL active BWP switch with non-DRX in SA for 1 Rx UE	5202

A.16.5.3.1.1.1	Test Purpose and Environment	5202

A.16.5.3.1.1.2	Test Requirements	5205

A.16.5.3.1.2	NR FR1 DL active BWP switch with non-DRX in SA for 2 Rx UE	5205

A.16.5.3.1.2.1	Test Purpose and Environment	5205

A.16.5.3.1.2.2	Test Requirements	5207

A.16.5.3.2	RRC-based Active BWP Switch	5208

A.16.5.3.2.1	NR FR1 DL active BWP switch of Cell with non-DRX in SA for 1 Rx UE	5208

A.16.5.3.2.1.1	Test Purpose and Environment	5208

A.16.5.3.2.1.2	Test Requirements	5210

A.16.5.3.2.2	NR FR1 DL active BWP switch of Cell with non-DRX in SA for 2 Rx UE	5210

A.16.5.3.2.2.1	Test Purpose and Environment	5210

A.16.5.3.2.2.2	Test Requirements	5212

A.16.5.4	UE specific CBW change	5213

A.16.5.4.1	UE specific CBW change on PCell in FR1 in non-DRX for 1 Rx UE	5213

A.16.5.4.1.1	Test Purpose and Environment	5213

A.16.5.4.1.2	Test Requirements	5215

A.16.5.4.2	UE specific CBW change on PCell in FR1 in non-DRX for 2 Rx UE	5215

A.16.5.4.2.1	Test Purpose and Environment	5215

A.16.5.4.2.2	Test Requirements	5218

A.16.6	Measurement procedure for RedCap	5218

A.16.6.1	Intra-frequency Measurements	5218

A.16.6.1.1	SA event triggered reporting tests without gap under non-DRX for 1 Rx UE	5218

A.16.6.1.1.1	Test purpose and Environment	5218

A.16.6.1.1.2	Test parameters	5218

A.16.6.1.1.3	Test Requirements	5220

A.16.6.1.2	SA event triggered reporting tests without gap under non-DRX for 2 Rx UE	5220

A.16.6.1.2.1	Test purpose and Environment	5220

A.16.6.1.2.2	Test parameters	5220

A.16.6.1.2.3	Test Requirements	5222

A.16.6.1.3	SA event triggered reporting tests without gap under DRX for 1 Rx UE	5222

A.16.6.1.3.1	Test purpose and Environment	5222

A.16.6.1.3.2	Test parameters	5222

A.16.6.1.3.3	Test Requirements	5224

A.16.6.1.4	SA event triggered reporting tests without gap under DRX for 2 Rx UE	5225

A.16.6.1.4.1	Test purpose and Environment	5225

A.16.6.1.4.2	Test parameters	5225

A.16.6.1.4.3	Test Requirements	5227

A.16.6.1.5	SA event triggered reporting tests with per-UE gaps under non-DRX for 1 Rx UE	5227

A.16.6.1.5.1	Test purpose and Environment	5227

A.16.6.1.5.2	Test parameters	5227

A.16.6.1.5.3	Test Requirements	5229

A.16.6.1.6	SA event triggered reporting tests with per-UE gaps under non-DRX for 2 Rx UE	5229

A.16.6.1.6.1	Test purpose and Environment	5229

A.16.6.1.6.2	Test parameters	5229

A.16.6.1.6.3	Test Requirements	5231

A.16.6.1.7	SA event triggered reporting tests with per-UE gaps under DRX for 1 Rx UE	5232

A.16.6.1.7.1	Test purpose and Environment	5232

A.16.6.1.7.2	Test parameters	5232

A.16.6.1.7.3	Test Requirements	5234

A.16.6.1.8	SA event triggered reporting tests with per-UE gaps under DRX for 2 Rx UE	5234

A.16.6.1.8.1	Test purpose and Environment	5234

A.16.6.1.8.2	Test parameters	5234

A.16.6.1.8.3	Test Requirements	5236

A.16.6.1.9	SA event triggered reporting tests without gap under non-DRX with SSB index reading for 1 Rx UE	5236

A.16.6.1.9.1	Test purpose and Environment	5236

A.16.6.1.9.2	Test parameters	5237

A.16.6.1.9.3	Test Requirements	5238

A.16.6.1.10	SA event triggered reporting tests without gap under non-DRX with SSB index reading for 2 Rx UE	5238

A.16.6.1.10.1	Test purpose and Environment	5238

A.16.6.1.10.2	Test parameters	5238

A.16.6.1.10.3	Test Requirements	5240

A.16.6.1.11	SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading for 1 Rx UE	5240

A.16.6.1.11.1	Test purpose and Environment	5240

A.16.6.1.11.2	Test parameters	5240

A.16.6.1.11.3	Test Requirements	5242

A.16.6.1.12	SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading for 2 Rx UE	5242

A.16.6.1.12.1	Test purpose and Environment	5242

A.16.6.1.12.2	Test parameters	5242

A.16.6.1.12.3	Test Requirements	5243

A.16.6.2	Inter-frequency Measurements	5244

A.16.6.2.1	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used for 1 Rx UE	5244

A.16.6.2.1.1	Test Purpose and Environment	5244

A.16.6.2.1.2	Test Requirements	5246

A.16.6.2.2	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is used for 2 Rx UE	5247

A.16.6.2.2.1	Test Purpose and Environment	5247

A.16.6.2.2.2	Test Requirements	5249

A.16.6.2.3	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used for 1 Rx UE	5249

A.16.6.2.3.1	Test Purpose and Environment	5250

A.16.6.2.3.2	Test Requirements	5252

A.16.6.2.4	SA event triggered reporting tests for FR1 without SSB time index detection when DRX is not used for 2 Rx UE	5252

A.16.6.2.4.1	Test Purpose and Environment	5252

A.16.6.2.4.2	Test Requirements	5254

A.16.6.2.5	SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used for 1 Rx UE	5254

A.16.6.2.5.1	Test Purpose and Environment	5254

A.16.6.2.5.2	Test Requirements	5257

A.16.6.2.6	SA event triggered reporting tests for FR1 with SSB time index detection when DRX is not used for 2 Rx UE	5257

A.16.6.2.6.1	Test Purpose and Environment	5257

A.16.6.2.6.2	Test Requirements	5259

A.16.6.2.7	SA event triggered reporting tests for FR1 with SSB time index detection when DRX is used for 1 Rx UE	5259

A.16.6.2.7.1	Test Purpose and Environment	5259

A.16.6.2.7.2	Test Requirements	5262

A.16.6.2.8	SA event triggered reporting tests for FR1 with SSB time index detection when DRX is used for 2 Rx UE	5262

A.16.6.2.8.1	Test Purpose and Environment	5262

A.16.6.2.8.2	Test Requirements	5264

A.16.6.2.9	SA event triggered reporting tests with additional mandatory gap pattern for 1 Rx UE	5265

A.16.6.2.9.1	Test Purpose and Environment	5265

A.16.6.2.9.2	Test Requirements	5267

A.16.6.2.10	SA event triggered reporting tests with additional mandatory gap pattern for 2 Rx UE	5267

A.16.6.2.10.1	Test Purpose and Environment	5267

A.16.6.2.10.2	Test Requirements	5269

A.16.6.2.11	SA event triggered reporting tests for FR1 when DRX is used for 1 Rx UE	5270

A.16.6.2.11.1	Test Purpose and Environment	5270

A.16.6.2.11.2	Test Requirements	5272

A.16.6.2.12	SA event triggered reporting tests for FR1 when DRX is used for 2 Rx UE	5272

A.16.6.2.12.1	Test Purpose and Environment	5272

A.16.6.2.12.2	Test Requirements	5275

A.16.6.3	Inter-RAT Measurements	5275

A.16.6.3.1	SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 for 1 Rx UE	5275

A.16.6.3.1.1	Test purpose and Environment	5275

A.16.6.3.1.2	Test Requirements	5278

A.16.6.3.2	SA NR - E-UTRAN event-triggered reporting in non-DRX in FR1 for 2 Rx UE	5279

A.16.6.3.2.1	Test purpose and Environment	5279

A.16.6.3.2.2	Test Requirements	5282

A.16.6.3.3	SA NR - E-UTRAN event-triggered reporting in DRX in FR1 for 1 Rx UE	5282

A.16.6.3.3.1	Test purpose and Environment	5282

A.16.6.3.3.2	Test Requirements	5286

A.16.6.3.4	SA NR - E-UTRAN event-triggered reporting in DRX in FR1 for 2 Rx UE	5286

A.16.6.3.4.1	Test purpose and Environment	5286

A.16.6.3.4.2	Test Requirements	5289

A.16.6.4	L1-RSRP measurement for beam reporting	5290

A.16.6.4.1	SSB based L1-RSRP measurement when DRX is not used for 1 Rx UE	5290

A.16.6.4.1.1	Test Purpose and Environment	5290

A.16.6.4.1.2	Test parameters	5290

A.16.6.4.1.3	Test Requirements	5291

A.16.6.4.2	SSB based L1-RSRP measurement when DRX is not used for 2 Rx UE	5292

A.16.6.4.2.1	Test Purpose and Environment	5292

A.16.6.4.2.2	Test parameters	5292

A.16.6.4.2.3	Test Requirements	5293

A.16.6.4.3	SSB based L1-RSRP measurement when DRX is used for 1 Rx UE	5293

A.16.6.4.3.1	Test Purpose and Environment	5293

A.16.6.4.3.2	Test parameters	5294

A.16.6.4.3.3	Test Requirements	5295

A.16.6.4.4	SSB based L1-RSRP measurement when DRX is used for 2 Rx UE	5295

A.16.6.4.4.1	Test Purpose and Environment	5295

A.16.6.4.4.2	Test parameters	5296

A.16.6.4.4.3	Test Requirements	5297

A.16.6.4.5	CSI-RS based L1-RSRP measurement when DRX is not used for 1 Rx UE	5297

A.16.6.4.5.1	Test Purpose and Environment	5297

A.16.6.4.5.2	Test parameters	5298

A.16.6.4.5.3	Test Requirements	5299

A.16.6.4.6	CSI-RS based L1-RSRP measurement when DRX is not used for 2 Rx UE	5299

A.16.6.4.6.1	Test Purpose and Environment	5299

A.16.6.4.6.2	Test parameters	5300

A.16.6.4.6.3	Test Requirements	5301

A.16.6.4.7	CSI-RS based L1-RSRP measurement when DRX is used for 1 Rx UE	5301

A.16.6.4.7.1	Test Purpose and Environment	5301

A.16.6.4.7.2	Test parameters	5302

A.16.6.4.7.3	Test Requirements	5303

A.16.6.4.8	CSI-RS based L1-RSRP measurement when DRX is used for 2 Rx UE	5303

A.16.6.4.8.1	Test Purpose and Environment	5303

A.16.6.4.8.2	Test parameters	5304

A.16.6.4.8.3	Test Requirements	5305

A.16.6.5	NR measurements with autonomous gaps	5306

A.16.6.5.1	SA intra-frequency CGI identification of NR neighbor cell in FR1 for 1 Rx UE	5306

A.16.6.5.1.1	Test Purpose and Environment	5306

A.16.6.5.1.2	Test Parameters	5306

A.16.6.5.1.3	Test Requirements	5308

A.16.6.5.2	SA intra-frequency CGI identification of NR neighbor cell in FR1 for 2 Rx UE	5308

A.16.6.5.2.1	Test Purpose and Environment	5308

A.16.6.5.2.2	Test Parameters	5308

A.16.6.5.2.3	Test Requirements	5310

A.16.6.5.3	Identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR SA for 1 Rx UE	5310

A.16.6.5.3.1	Test Purpose and Environment	5310

A.16.6.5.3.2	Test Requirements	5313

A.16.6.5.4	Identification of a new CGI of inter-RAT E-UTRA cell using autonomous gaps in NR SA for 2 Rx UE	5313

A.16.6.5.4.1	Test Purpose and Environment	5313

A.16.6.5.4.2	Test Requirements	5316

A.16.6.6	RSTD Measurements	5316

A.16.6.6.1	NR RSTD measurement reporting delay test case for RedCap UE without FH in FR1 SA	5316

A.16.6.6.1.1	Test Purpose and Environment	5316

A.16.6.6.1.2	Test Requirements	5321

A.16.6.6.2	NR RSTD measurement reporting delay test case with PRS frequency hopping	5321

A.16.6.6.2.1	Test Purpose and Environment	5321

A.16.6.6.2.2	Test Requirements	5325

A.16.6.7	UE Rx-Tx Measurements	5326

A.16.6.7.1	UE Rx-Tx measurement reporting delay test case for single positioning frequency layer in FR1 SA for RedCap UE without RX FH in RRC\_CONNECTED mode	5326

A.16.6.7.1.1	Test purpose and environment	5326

A.16.6.7.1.2	Test requirements	5330

A.16.6.7.2	UE Rx-Tx time difference measurement with Rx FH for single positioning frequency layer in FR1 SA in RRC\_CONNECTED state	5330

A.16.6.7.2.1	Test purpose and environment	5330

A.16.6.7.2.2	Test requirements	5334

A.16.6.8	PRS-RSRP measurements	5334

A.16.6.8.1	PRS-RSRP measurement delay test case for single positioning frequency layer	5334

A.16.6.8.1.1	Test purpose and Environment	5334

A.16.6.8.1.2	Test Requirements	5338

A.16.6.8.2	PRS-RSRP measurement delay with FH in RRC\_CONNECTED state in FR1	5338

A.16.6.8.2.1	Test purpose and Environment	5338

A.16.6.8.2.2	Test Requirements	5342

A.16.6.9	PRS-RSRPP Measurements	5342

A.16.6.9.1	PRS-RSRPP measurement delay without FH in RRC\_CONNECTED state in FR1	5342

A.16.6.9.1.1	Test purpose and Environment	5342

A.16.6.9.1.2	Test Requirements	5344

A.16.6.9.2	PRS-RSRPP measurement with Rx FH reporting delay test case for single positioning frequency layer in FR1 SA in RRC\_CONNECTED state	5345

A.16.6.9.2.1	Test purpose and Environment	5345

A.16.6.9.2.2	Test Requirements	5347

A.16.7	Measurement Performance requirements for RedCap	5347

A.16.7.1	SS-RSRP	5347

A.16.7.1.1	SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE	5347

A.16.7.1.1.1	Test Purpose and Environment	5347

A.16.7.1.1.2	Test parameters	5347

A.16.7.1.1.3	Test Requirements	5351

A.16.7.1.2	SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 2 RX UE	5351

A.16.7.1.2.1	Test Purpose and Environment	5351

A.16.7.1.2.2	Test parameters	5351

A.16.7.1.2.3	Test Requirements	5355

A.16.7.1.3	SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE	5355

A.16.7.1.3.1	Test Purpose and Environment	5355

A.16.7.1.3.2	Test parameters	5355

A.16.7.1.3.3	Test Requirements	5358

A.16.7.1.4	SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE	5358

A.16.7.1.4.1	Test Purpose and Environment	5358

A.16.7.1.4.2	Test parameters	5358

A.16.7.1.4.3	Test Requirements	5361

A.16.7.2	SS-RSRQ	5361

A.16.7.2.1	SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE	5361

A.16.7.2.1.1	Test Purpose and Environment	5361

A.16.7.2.1.2	Test Parameters	5361

A.16.7.2.1.3	Test Requirements	5365

A.16.7.2.2	SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE	5365

A.16.7.2.2.1	Test Purpose and Environment	5365

A.16.7.2.2.2	Test Parameters	5365

A.16.7.2.2.3	Test Requirements	5368

A.16.7.2.3	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE	5368

A.16.7.2.3.1	Test Purpose and Environment	5368

A.16.7.2.3.2	Test parameters	5369

A.16.7.2.3.3	Test Requirements	5372

A.16.7.2.4	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE	5372

A.16.7.2.4.1	Test Purpose and Environment	5372

A.16.7.2.4.2	Test parameters	5372

A.16.7.2.4.3	Test Requirements	5376

A.16.7.3	SS-SINR	5376

A.16.7.3.1	SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE	5376

A.16.7.3.1.1	Test Purpose and Environment	5376

A.16.7.3.1.2	Test parameters	5376

A.16.7.3.1.3	Test Requirements	5379

A.16.7.3.2	SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE	5379

A.16.7.3.2.1	Test Purpose and Environment	5379

A.16.7.3.2.2	Test parameters	5379

A.16.7.3.3	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 1 Rx UE	5382

A.16.7.3.3.1	Test Purpose and Environment	5382

A.16.7.3.3.2	Test parameters	5382

A.16.7.3.3.3	Test Requirements	5385

A.16.7.3.4	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell for 2 Rx UE	5385

A.16.7.3.4.1	Test Purpose and Environment	5385

A.16.7.3.4.2	Test parameters	5385

A.16.7.3.4.3	Test Requirements	5388

A.16.7.4	L1-RSRP measurement for beam reporting	5389

A.16.7.4.1	SSB based L1-RSRP measurement for 1 Rx UE	5389

A.16.7.4.1.1	Test Purpose and Environment	5389

A.16.7.4.1.2	Test parameters	5389

A.16.7.4.1.3	Test Requirements	5391

A.16.7.4.2	SSB based L1-RSRP measurement for 2 Rx UE	5391

A.16.7.4.2.1	Test Purpose and Environment	5391

A.16.7.4.2.2	Test parameters	5392

A.16.7.4.2.3	Test Requirements	5392

A.16.7.4.3	CSI-RS based L1-RSRP measurement on resource set with repetition off for 1 Rx UE	5392

A.16.7.4.3.1	Test Purpose and Environment	5392

A.16.7.4.3.2	Test parameters	5392

A.16.7.4.3.3	Test Requirements	5395

A.16.7.4.4	CSI-RS based L1-RSRP measurement on resource set with repetition off for 2 Rx UE	5395

A.16.7.4.4.1	Test Purpose and Environment	5395

A.16.7.4.4.2	Test parameters	5395

A.16.7.4.4.3	Test Requirements	5395

A.16.7.5	E-UTRAN RSRP	5395

A.16.7.5.1	SA: inter-RAT measurement accuracy with FR1 serving cell for 1 Rx UE	5395

A.16.7.5.1.1	Test Purpose and Environment	5395

A.16.7.5.1.2	Test parameters	5395

A.16.7.5.1.3	Test Requirements	5399

A.16.7.5.2	SA: inter-RAT measurement accuracy with FR1 serving cell for 2 Rx UE	5399

A.16.7.5.2.1	Test Purpose and Environment	5399

A.16.7.5.2.2	Test parameters	5399

A.16.7.5.2.3	Test Requirements	5402

A.16.7.6	E-UTRAN RSRQ	5402

A.16.7.6.1	SA: inter-RAT measurement accuracy with FR1 serving cell for 1 Rx UE	5402

A.16.7.6.1.1	Test Purpose and Environment	5402

A.16.7.6.1.2	Test parameters	5402

A.16.7.6.1.3	Test Requirements	5406

A.16.7.6.2	SA: inter-RAT measurement accuracy with FR1 serving cell for 2 Rx UE	5406

A.16.7.6.2.1	Test Purpose and Environment	5406

A.16.7.6.2.2	Test parameters	5406

A.16.7.6.2.3	Test Requirements	5409

A.16.7.7	RSTD measurements	5409

A.16.7.7.1	RSTD measurement accuracy test case for RedCap UE without FH	5409

A.16.7.7.1.1	Test purpose and Environment	5409

A.16.7.7.1.2	Test Requirements	5411

A.16.7.8	UE Rx-Tx measurements	5415

A.16.7.8.1	UE Rx-Tx time difference measurement accuracy for single positioning frequency layer in FR1 SA for RedCap UE without RX FH in RRC\_CONNECTED mode	5415

A.16.7.8.1.1	Test purpose and environment	5415

A.16.7.8.1.2	Test parameters	5416

A.16.7.8.1.3	Test requirements	5419

A.16.7.8.2	SA: UE Rx-Tx time difference measurement accuracy with Rx FH in RRC\_CONNECTED state in FR1	5419

A.16.7.8.2.1 	Test purpose and Environment	5419

A.16.7.8.2.2	Test parameters	5420

A.16.7.8.2.3	Test requirements	5423

A.16.7.9	PRS-RSRP Measurements	5423

A.16.7.9.1	PRS-RSRP measurement accuracy without FH in RRC\_CONNECTED state in FR1	5423

A.16.7.9.1.1	Test Purpose and Environment	5423

A.16.7.9.1.2	Test parameters	5423

A.16.7.9.1.3	Test Requirements	5427

A.16.7.9.2	PRS-RSRP measurement accuracy with FH in RRC\_CONNECTED state in FR1	5428

A.16.7.9.2.1	Test Purpose and Environment	5428

A.16.7.9.2.2	Test parameters	5428

A.16.7.9.2.3	Test Requirements	5431

A.16.7.10	PRS-RSRPP measurements	5432

A.16.7.10.1	PRS-RSRPP measurement accuracy without FH in RRC\_CONNECTED state in FR1	5432

A.16.7.10.1.1	Test Purpose and Environment	5432

A.16.7.10.1.2	Test parameters	5432

A.16.7.10.1.3	Test Requirements	5435

A.16.7.10.2	SA: PRS-RSRPP measurement accuracy with Rx FH in RRC\_CONNECTED state in FR1	5435

A.16.7.10.2.1	Test purpose and Environment	5435

A.16.7.10.2.2	Test parameters	5435

A.16.7.10.2.3	Test requirements	5439

A.16.8	Measurement Procedure for RedCap in RRC\_INACTIVE	5439

A.16.8.1	RSTD Measurements	5439

A.16.8.1.1	NR RSTD measurement reporting delay test case for for RedCap UE without FH in FR1 SA in RRC\_INACTIVE state	5439

A.16.8.1.1.1	Test Purpose and Environment	5439

A.16.8.1.1.2	Test Requirements	5443

A.16.8.1.2	NR RSTD measurement reporting delay test case with PRS frequency hopping	5443

A.16.8.1.2.1	Test Purpose and Environment	5443

A.16.8.1.2.2	Test Requirements	5447

A.16.8.1.3	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR1 SA in RRC\_INACTIVE state when eDRX cycle &gt; 10.24s for RedCap UE	5447

A.16.8.1.3.1	Test Purpose and Environment	5447

A.16.8.1.3.2	Test Requirements	5451

A.16.8.2	UE Rx-Tx Measurements	5451

A.16.8.2.1	UE Rx-Tx measurement reporting delay test case for single positioning frequency layer in FR1 SA for RedCap UE without RX FH in RRC\_INACTIVE mode	5451

A.16.8.2.1.1	Test purpose and environment	5451

A.16.8.2.1.2	Test requirements	5455

A.16.8.2.2	UE Rx-Tx time difference measurement with Rx FH for single positioning frequency layer in FR1 SA in RRC\_INACTIVE state	5455

A.16.8.2.2.1	Test purpose and environment	5455

A.16.8.2.2.2	Test requirements	5459

A.16.8.2.3.	UE Rx-Tx time difference measurement for single positioning frequency layer with eDRX &gt; 10.24s in FR1 SA	5459

A.16.8.2.3.1	Test purpose and environment	5459

A.16.8.2.3.2	Test requirements	5463

A.16.8.3	PRS-RSRP Measurements	5463

A.16.8.3.1	PRS-RSRP reporting delay test case for single positioning frequency layer in RRC\_INACTIVE	5463

A.16.8.3.1.1	Test purpose and Environment	5463

A.16.8.3.1.2	Test Requirements	5465

A.16.8.3.3	PRS-RSRP reporting delay test case in RRC\_INACTIVE state in FR1 when eDRX cycle &gt; 10.24s	5466

A.16.8.3.3.1	Test purpose and Environment	5466

A.16.8.3.3.2	Test Requirements	5468

A.16.8.4	PRS-RSRPP Measurements	5469

A.16.8.4.1	PRS-RSRPP measurement delay without FH in RRC\_INACTIVE state in FR1	5469

A.16.8.4.1.1	Test purpose and Environment	5469

A.16.8.4.2	PRS-RSRPP measurement with Rx FH reporting delay test case for single positioning frequency layer in FR1 SA in RRC\_INACTIVE state	5472

A.16.8.4.2.1	Test purpose and Environment	5472

A.16.8.4.2.2	Test Requirements	5474

A.16.9	Measurement Performance Requirements for RedCap in RRC\_INACTIVE	5477

A.16.9.1	 RSTD Measurements	5477

A.16.9.1.1	RSTD measurement accuracy test case for RedCap UE without FH in FR1 in RRC\_INACTIVE state	5477

A.16.9.1.1.1	Test purpose and Environment	5477

A.16.9.1.1.2	Test Requirements	5479

A.16.9.1.2	RSTD measurement accuracy test case for RedCap UE with FH in FR1 in RRC\_INACTIVE state	5479

A.16.9.1.2.1	Test purpose and Environment	5479

A.16.9.1.2.2	Test Requirements	5481

A.16.9.2	UE Rx-Tx measurements	5481

A.16.9.2.1	UE Rx-Tx time difference measurement accuracy for single positioning frequency layer in FR1 SA for RedCap UE without RX FH in RRC\_INACTIVE mode	5481

A.16.9.2.1.1	Test purpose and environment	5481

A.16.9.2.1.2	Test parameters	5482

A.16.9.2.1.3	Test requirements	5483

A.16.9.2.2	SA: UE Rx-Tx time difference measurement accuracy with Rx FH in RRC\_INACTIVE state in FR1	5484

A.16.9.2.2.1	Test purpose and Environment	5484

A.16.9.2.2.2	Test parameters	5484

A.16.9.2.2.3	Test requirements	5487

A.16.9.3	PRS-RSRP Measurements	5487

A.16.9.3.1	PRS-RSRP measurement accuracy without FH in RRC\_INACTIVE state in FR1	5487

A.16.9.3.1.1	Test Purpose and Environment	5487

A.16.9.3.1.2	Test parameters	5487

A.16.9.3.1.3	Test Requirements	5490

A.16.9.3.2	PRS-RSRP measurement accuracy with FH in RRC\_INACTIVE state in FR1	5490

A.16.9.3.2.1	Test Purpose and Environment	5490

A.16.9.3.2.2	Test parameters	5490

A.16.9.3.2.3	Test Requirements	5493

A.16.9.4	PRS-RSRPP measurements	5493

A.16.9.4.1	PRS-RSRPP measurement accuracy without Rx FH in RRC\_INACTIVE state in FR1	5493

A.16.9.4.1.1	Test purpose and Environment	5493

A.16.9.4.1.2	Test parameters	5493

A.16.9.4.1.3	Test requirements	5497

A.16.9.4.2	SA: PRS-RSRPP measurement accuracy with Rx FH in RRC\_INACTIVE state in FR1	5497

A.16.9.4.2.1	Test purpose and Environment	5497

A.16.9.4.2.2	Test parameters	5497

A.16.9.4.2.3	Test requirements	5500

A.16.10	 Measurement procedure for RedCap in RRC\_IDLE	5500

A.16.10.1	RSTD measurements	5500

A.16.10.1.1	NR RSTD measurement reporting delay test case for RedCap UE without FH in FR1 SA in RRC\_IDLE state without eDRX	5500

A.16.10.1.1.1	Test Purpose and Environment	5500

A.16.10.1.1.2	Test Requirements	5504

A.16.10.1.2	NR RSTD measurement reporting delay test case for RedCap UE without RX FH in FR1 SA in RRC\_IDLE state when eDRX &gt; 10.24s	5504

A.16.10.1.2.1	Test Purpose and Environment	5504

A.16.10.1.2.2	Test Requirements	5508

A.16.10.2	PRS-RSRP Measurements	5508

A.16.10.2.1	PRS-RSRP reporting delay test case for single positioning frequency layer in RRC\_IDLE	5508

A.16.10.2.1.1	Test purpose and Environment	5508

A.16.10.2.1.2	Test Requirements	5510

A.16.10.2.2	PRS-RSRP measurement without Rx FH reporting delay test case for single positioning frequency layer in FR1 SA in RRC\_IDLE state with eDRX cycle &gt; 10.24s	5511

A.16.10.2.2.1	Test purpose and Environment	5511

A.16.10.2.2.2	Test Requirements	5513

A.16.11	 Measurement Performance Requirements for RedCap in RRC\_IDLE	5513

A.16.11.1	RSTD Measurements	5513

A.16.11.1.1	RSTD measurement accuracy test case for RedCap UE without FH in FR1 in RRC\_IDLE state without eDRX	5513

A.16.11.1.1.1	Test purpose and Environment	5513

A.16.11.1.1.2	Test Requirements	5515

A.16.11.1.2	RSTD measurement accuracy test case for RedCap UE without FH in FR1 in RRC\_IDLE state with eDRX &gt; 10.24s	5516

A.16.11.1.2.1	Test purpose and Environment	5516

A.16.11.1.2.2	Test Requirements	5518

A.16.11.2	PRS-RSRP Measurements	5518

A.16.11.2.1	PRS-RSRP measurement accuracy test case for RedCap UE in FR1 in RRC\_IDLE state	5518

A.16.11.2.1.1	Test Purpose and Environment	5518

A.16.11.2.1.2	Test parameters	5518

A.16.11.2.1.3	Test Requirements	5520

A.16.11.2.2	PRS-RSRP measurement without Rx FH accuracy test case for single positioning frequency layer in FR1 SA in RRC\_IDLE state with eDRX cycle &gt; 10.24s	5520

A.16.11.2.2.1	Test purpose and Environment	5520

A.16.11.2.2.2	Test Requirements	5522

A.17	NR standalone tests with one or more NR cells in FR2 for RedCap	5524

A.17.1	SA: RRC\_IDLE state mobility for RedCap	5524

A.17.1.1	Cell re-selection to NR	5524

A.17.1.1.1	Cell reselection to FR2 intra-frequency NR case for 2 Rx	5524

A.17.1.1.1.1	Test Purpose and Environment	5524

A.17.1.1.1.2	Test Parameters	5524

A.17.1.1.1.3	Test Requirements	5526

A.17.1.1.2	Cell reselection to FR2 inter-frequency NR case	5526

A.17.1.1.2.1	Test Purpose and Environment	5526

A.17.1.1.2.2	Test Parameters	5526

A.17.1.1.2.3	Test Requirements	5528

A.17.1.1.3	Cell reselection to FR2 intra-frequency NR case for UE fulfilling stationary relaxed measurement criterion for 2 Rx UE	5529

A.17.1.1.3.1	Test Purpose and Environment	5529

A.17.1.1.3.2	Test Parameters	5529

A.17.1.1.3.3	Test Requirements	5531

A.17.1.1.4	Cell reselection to FR2 inter-frequency NR case for UE fulfilling stationary mobility relaxed measurement criterion for 2 Rx UE	5531

A.17.1.1.4.1	Test Purpose and Environment	5531

A.17.1.1.4.2	Test Parameters	5531

A.17.1.1.4.3	Test Requirements	5533

A.17.2	SA: RRC\_INACTIVE state mobility for RedCap	5534

A.17.2.1	Configured Grant based Small Data Transmissions (CG-SDT) for RedCap	5534

A.17.2.1.1	TA validation for CG-SDT in FR2 for RedCap	5534

A.17.2.1.1.1	Test Purpose and Environment	5534

A.17.2.1.1.2	Test Requirements	5537

A.17.2.2	Cell Reselection for Positioning	5537

A.17.2.2.1	Cell reselection to FR2 intra-frequency NR case with RRC\_INACTIVE eDRX and positioning SRS	5537

A.17.2.2.1.1	Test Purpose and Environment	5537

A.17.2.2.1.2	Test Parameters	5537

A.17.2.2.1.3	Test Requirements	5537

A.17.3	RRC\_CONNECTED state mobility for RedCap	5537

A.17.3.1	Handover for RedCap	5537

A.17.3.1.1	Intra-frequency handover from FR2 to FR2; unknown target cell for 2 Rx	5537

A.17.3.1.1.1	Test Purpose and Environment	5537

A.17.3.1.1.2	Test Parameters	5537

A.17.3.1.1.3	Test Requirements	5539

A.17.3.1.2	Inter-frequency handover from FR2 to FR2; unknown target cell for 2 Rx	5539

A.17.3.1.2.1	Test Purpose and Environment	5539

A.17.3.1.2.2	Test Parameters	5539

A.17.3.1.2.3 Test Requirements	5541

A.17.3.2	RRC Connection Mobility Control for RedCap	5541

A.17.3.2.1	SA: RRC Re-establishment	5541

A.17.3.2.1.1	Intra-frequency RRC Re-establishment in FR2	5541

A.17.3.2.1.1.1	Test Purpose and Environment	5541

A.17.3.2.1.2	Inter-frequency RRC Re-establishment in FR2	5543

A.17.3.2.1.2.1	Test Purpose and Environment	5543

A.17.3.2.1.3	Intra-frequency RRC Re-establishment in FR2 without serving cell timing	5545

A.17.3.2.1.3.1	Test Purpose and Environment	5545

A.17.3.2.1.3.2	Test Requirements	5547

A.17.3.2.2	Random Access	5547

A.17.3.2.2.1	4-step RA type contention based random access test in FR2 for NR Standalone	5547

A.17.3.2.2.1.1	Test Purpose and Environment	5547

A.17.3.2.2.1.2	Test Requirements	5549

A.17.3.2.2.2	4-step RA type non-contention based random access test in FR2 for NR Standalone	5551

A.17.3.2.2.2.1	Test Purpose and Environment	5551

A.17.3.2.2.2.2	Test Requirements	5552

A.17.3.2.2.3	2-step RA type contention based random access test in FR2 for NR Standalone	5554

A.17.3.2.2.3.1	Test Purpose and Environment	5554

A.17.3.2.2.3.2	Test Requirements	5555

A.17.3.2.2.4	2-step RA type non-contention based random access test in FR2 for NR Standalone	5556

A.17.3.2.2.4.1	Test Purpose and Environment	5556

A.17.3.2.2.4.2	Test Requirements	5558

A.17.3.2.3	SA: RRC Connection Release with Redirection	5559

A.17.3.2.3.1	Redirection from NR in FR2 to NR in FR2	5559

A.17.3.2.3.1.1	Test Purpose and Environment	5559

A.17.3.2.3.1.2	Test Parameters	5559

A.17.3.2.3.1.3	Test Requirements	5561

A.17.4	Timing	5561

A.17.4.1	UE transmit timing	5561

A.17.4.1.1	NR UE Transmit Timing Test for FR2	5561

A.17.4.1.1.1	Test Purpose and environment	5561

A.17.4.1.1.2	Test requirements	5563

A.17.4.2	UE timer accuracy	5564

A.17.4.3	Timing advance	5564

A.17.4.3.1	SA FR2 timing advance adjustment accuracy	5564

A.17.4.3.1.1	Test Purpose and Environment	5564

A.17.4.3.1.2	Test Parameters	5564

A.17.4.3.1.3	Test Requirements	5567

A.17.5	Signaling characteristics for RedCap	5567

A.17.5.1	Radio link Monitoring for RedCap	5567

A.17.5.1.1	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode	5567

A.17.5.1.1.1	Test Purpose and Environment	5567

A.17.5.1.1.2	Test Requirements	5570

A.17.5.1.2	Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in non-DRX mode	5570

A.17.5.1.2.1	Test Purpose and Environment	5570

A.17.5.1.2.2	Test Requirements	5573

A.17.5.1.3	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode	5573

A.17.5.1.3.1	Test Purpose and Environment	5573

A.17.5.1.3.2	Test Requirements	5576

A.17.5.1.4	Radio Link Monitoring In-sync Test for FR2 PCell configured with SSB-based RLM RS in DRX mode	5576

A.17.5.1.4.1	Test Purpose and Environment	5576

A.17.5.1.4.2	Test Requirements	5578

A.17.5.1.5	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode	5579

A.17.5.1.5.1	Test Purpose and Environment	5579

A.17.5.1.5.2	Test Requirements	5581

A.17.5.1.6	Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in non-DRX mode	5582

A.17.5.1.6.1	Test Purpose and Environment	5582

A.17.5.1.6.2	Test Requirements	5584

A.17.5.1.7	Radio Link Monitoring Out-of-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode	5585

A.17.5.1.7.1	Test Purpose and Environment	5585

A.17.5.1.7.2	Test Requirements	5587

A.17.5.1.8	Radio Link Monitoring In-sync Test for FR2 PCell configured with CSI-RS-based RLM in DRX mode	5587

A.17.5.1.8.1	Test Purpose and Environment	5587

A.17.5.1.8.2	Test Requirements	5590

A.17.5.1.9	UE Radio Link Monitoring Scheduling Restrictions on FR2	5591

A.17.5.1.9.1	Test Purpose and Environment	5591

A.17.5.1.9.2	Test Requirements	5592

A.17.5.2	Beam Failure Detection and Link recovery procedures	5593

A.17.5.2.1	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode	5593

A.17.5.2.1.1	Test Purpose and Environment	5593

A.17.5.2.1.2	Test Requirements	5595

A.17.5.2.2	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with SSB-based BFD and LR in DRX mode	5596

A.17.5.2.2.1	Test Purpose and Environment	5596

A.17.5.2.2.2	Test Requirements	5599

A.17.5.2.3	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in non-DRX mode	5599

A.17.5.2.3.1	Test Purpose and Environment	5599

A.17.5.2.3.2	Test Requirements	5602

A.17.5.2.4	Beam Failure Detection and Link Recovery Test for FR2 PCell configured with CSI-RS-based BFD and LR in DRX mode	5602

A.17.5.2.4.1	Test Purpose and Environment	5602

A.17.5.2.4.2	Test Requirements	5605

A.17.5.2.5	Scheduling availability restriction during Beam Failure Detection and Link Recovery for FR2 PCell configured with SSB-based BFD and LR in non-DRX mode for 2 Rx UE	5605

A.17.5.2.5.1	Test Purpose and Environment	5605

A.17.5.2.5.2	Test Requirements	5608

A.17.5.3	Active BWP switch for RedCap	5609

A.17.5.3.1	DCI-based and Timer-based Active BWP Switch	5609

A.17.5.3.1.1	NR FR2 DL active BWP switch with non-DRX in SA	5609

A.17.5.3.1.1.1	Test Purpose and Environment	5609

A.17.5.3.1.1.2	Test Requirements	5611

A.17.5.3.2	RRC-based Active BWP Switch	5611

A.17.5.3.2.1	NR FR2 DL active BWP switch of PCell with non-DRX in SA	5611

A.17.5.3.2.1.1	Test Purpose and Environment	5611

A.17.5.3.2.1.2	Test Requirements	5614

A.17.5.4	Active TCI state switch delay	5614

A.17.5.4.1	MAC-CE based active TCI state switch	5614

A.17.5.4.1.1	NR PCell FR2 active TCI state switch for a known TCI state	5614

A.17.5.4.1.1.1	Test Purpose and Environment	5614

A.17.5.4.1.1.2	Test Requirements	5617

A.17.5.4.2	RRC based active TCI state switch	5617

A.17.5.4.2.1	NR PCell FR2 active TCI state switch for a known TCI state	5617

A.17.5.4.2.1.1	Test Purpose and Environment	5617

A.17.5.4.2.1.2	Test Requirements	5620

A.17.5.5	Uplink spatial relation switch delay	5620

A.17.5.5.1	MAC-CE based Spatial Relation switch	5620

A.17.5.5.1.1	 NR PCell FR2 spatial relation associated with known DL-RS	5620

A.17.5.5.1.1.1	Test Purpose and Environment	5620

A.17.5.5.1.1.2	Test Requirements	5622

A.17.5.5.2	RRC based spatial relation switch	5623

A.17.5.5.2.1	NR PCell FR2 spatial relation switch associated with a known DL-RS	5623

A.17.5.5.2.1.2	Test Requirements	5625

A.17.5.6	UE specific CBW change	5625

A.17.5.6.1	NR FR2 UE specific CBW change of PCell with non-DRX in SA	5625

A.17.5.6.1.1	Test Purpose and Environment	5625

A.17.5.6.1.2	Test Requirements	5627

A.17.6	Measurement procedure for RedCap	5628

A.17.6.1	Intra-frequency Measurements	5628

A.17.6.1.1	SA event triggered reporting test without gap under non-DRX	5628

A.17.6.1.1.1	Test purpose and Environment	5628

A.17.6.1.1.2	Test Requirements	5630

A.17.6.1.2	SA event triggered reporting test without gap under DRX	5630

A.17.6.1.2.1	Test purpose and Environment	5630

A.7.6.1.2.2	Test Requirements	5631

A.17.6.1.3	SA event triggered reporting test with per-UE gaps under non-DRX	5631

A.17.6.1.3.1	Test purpose and Environment	5631

A.17.6.1.3.2	Test Requirements	5634

A.17.6.1.4	SA event triggered reporting test with per-UE gaps under DRX	5634

A.17.6.1.4.1	Test purpose and Environment	5634

A.17.6.1.4.2	Test Requirements	5636

A.17.6.2	Inter-frequency Measurements	5637

A.17.6.2.1	SA event triggered reporting tests For FR2 without SSB time index detection when DRX is not used (PCell in FR2)	5637

A.17.6.2.1.1	Test Purpose and Environment	5637

A.17.6.2.1.2	Test Requirements	5639

A.17.6.2.2	SA event triggered reporting tests For FR2 without SSB time index detection when DRX is used (PCell in FR2)	5639

A.17.6.2.2.1	Test Purpose and Environment	5639

A.17.6.2.2.2	Test Requirements	5641

A.17.6.2.3	SA event triggered reporting tests For FR2 with SSB time index detection when DRX is not used (PCell in FR2)	5642

A.17.6.2.3.1	Test Purpose and Environment	5642

A.17.6.2.3.2	Test Requirements	5644

A.17.6.2.4	SA event triggered reporting tests For FR2 with SSB time index detection when DRX is used (PCell in FR2) for 2 RX UE	5644

A.17.6.2.4.1	Test Purpose and Environment	5644

A.17.6.2.4.2	Test Requirements	5646

A.17.6.3	L1-RSRP measurement for beam reporting	5647

A.17.6.3.1	SSB based L1-RSRP measurement when DRX is not used	5647

A.17.6.3.1.1	Test Purpose and Environment	5647

A.17.6.3.1.2	Test parameters	5647

A.17.6.3.1.3	Test Requirements	5647

A.17.6.3.2	SSB based L1-RSRP measurement when DRX is used	5647

A.17.6.3.2.1	Test Purpose and Environment	5647

A.17.6.3.2.2	Test parameters	5648

A.17.6.3.2.3	Test Requirements	5649

A.17.6.3.3	CSI-RS based L1-RSRP measurement when DRX is not used	5649

A.17.6.3.3.1	Test Purpose and Environment	5649

A.17.6.3.3.2	Test parameters	5649

A.17.6.3.3.3	Test Requirements	5651

A.17.6.3.4	CSI-RS based L1-RSRP measurement when DRX is used	5651

A.17.6.3.4.1	Test Purpose and Environment	5651

A.17.6.3.4.2	Test parameters	5652

A.7.6.3.3.3	Test Requirements	5653

A.17.6.4.1	SA interfrequency CGI reporting in autonomous gaps test (PCell in FR2) for 2 RX UE	5653

A.17.6.4.1.1	Test Purpose and Environment	5653

A.17.6.4.1.2	Test Requirements	5656

A.17.6.5	RSTD measurements	5656

A.17.6.5.1	NR RSTD measurement reporting delay test case for RedCap UE without FH in FR2 SA	5656

A.17.6.5.1.1	Test Purpose and Environment	5656

A.17.6.5.1.2	Test Requirements	5663

A.17.6.5.2	NR RSTD measurement reporting delay test case with PRS frequency hopping	5663

A.17.6.5.2.1	Test Purpose and Environment	5663

A.17.6.5.2.2	Test Requirements	5668

A.17.6.6	UE Rx-Tx Measurements	5669

A.17.6.6.1	UE Rx-Tx measurement reporting delay for single positioning frequency layer in FR2 SA without RX FH in RRC\_CONNECTED mode	5669

A.17.6.6.1.1	Test purpose and environment	5669

A.17.6.6.1.2	Test requirements	5673

A.17.6.6.2	UE Rx-Tx time difference measurement with Rx FH for single positioning frequency layer in FR2 SA in RRC\_CONNECTED state	5673

A.17.6.6.2.1	Test purpose and environment	5673

A.17.6.6.2.2	Test requirements	5677

A.17.6.7	PRS-RSRP measurements	5677

A.17.6.7.1	PRS-RSRP measurement delay test case for RedCap positioning without Rx FH in RRC\_CONNECTED state in FR2	5677

A.17.6.7.1.1	PRS-RSRP measurement delay test case for single positioning frequency layer	5677

A.17.6.7.1.1.1	Test Purpose and Environment	5677

A.17.6.7.1.1.2	Test Requirements	5681

A.17.6.7.1.2	PRS-RSRP measurement delay test case for dual positioning frequency layer	5681

A.17.6.7.1.2.1	Test Purpose and Environment	5681

A.17.6.7.1.2.2	Test Requirements	5685

A.17.6.7.2	PRS-RSRP measurement delay with FH in RRC\_CONNECTED state in FR2	5685

A.17.6.7.2.1	Test Purpose and Environment	5685

A.17.6.7.2.2	Test Requirements	5689

A.17.6.8	PRS-RSRPP Measurements	5689

A.17.6.8.1	PRS-RSRPP measurement delay without FH in RRC\_CONNECTED state in FR2	5689

A.17.6.8.1.1	Test Purpose and Environment	5689

A.17.6.8.1.2	Test Requirements	5692

A.17.6.8.2	PRS-RSRPP measurement with Rx FH reporting delay test case for single positioning frequency layer in FR2 SA in RRC\_CONNECTED state	5692

A.17.6.8.2.1	Test Purpose and Environment	5692

A.17.6.8.2.2	Test Requirements	5694

A.17.7	Measurement Performance requirements	5695

A.17.7.1	SS-RSRP	5695

A.17.7.1.1	SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	5695

A.17.7.1.1.1	Test Purpose and Environment	5695

A.17.7.1.1.2	Test parameters	5695

A.17.7.1.1.3	Test Requirements	5697

A.17.7.1.2	SA inter-frequency case measurement accuracy with FR2 serving cell and FR2 target cell	5697

A.17.7.1.2.1	Test Purpose and Environment	5697

A.17.7.1.2.2	Test parameters	5697

A.17.7.1.2.3	Test Requirements	5699

A.17.7.2	SS-RSRQ	5700

A.17.7.2.1	SA intra-frequency measurement accuracy with FR2 serving cell and FR2 target cell	5700

A.17.7.2.1.1	Test Purpose and Environment	5700

A.17.7.2.1.2	Test Parameters	5700

A.17.7.2.1.3	Test Requirements	5702

A.17.7.2.2	SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell for 2 Rx UE	5702

A.17.7.2.2.1	Test Purpose and Environment	5702

A.17.7.2.2.2	Test parameters	5702

A.17.7.2.2.3	Test Requirements	5704

A.17.7.2.3	SA Inter-frequency measurement accuracy with FR2 serving cell and FR2 TDD target cell	5704

A.17.7.3	L1-RSRP measurement for beam reporting	5704

A.17.7.3.1	SSB based L1-RSRP measurement	5704

A.17.7.3.1.1	Test Purpose and Environment	5704

A.17.7.3.1.2	Test parameters	5704

A.17.7.3.1.3	Test Requirements	5705

A.17.7.3.2	CSI-RS based L1-RSRP measurement on resource set with repetition off	5705

A.17.7.3.2.1	Test Purpose and Environment	5705

A.17.7.3.2.2	Test parameters	5705

A.17.7.3.2.3	Test Requirements	5705

A.17.7.4	SS-SINR	5706

A.17.7.4	SA intra-frequency case measurement accuracy with FR2 serving cell and FR2 target cell for 2Rx UE	5706

A.17.7.4.1.1	Test Purpose and Environment	5706

A.17.7.4.1.2	Test parameters	5706

A.17.7.4.1.3	Test Requirements	5708

A.17.7.5	RSTD measurements	5708

A.17.7.5.1	RSTD measurement accuracy test case for RedCap UE without FH	5708

A.17.7.5.1.1	Test purpose and Environment	5708

A.17.7.5.1.2	Test Requirements	5710

A.17.7.6	UE Rx-Tx Measurements	5712

A.17.7.6.1	UE Rx-Tx measurement accuracy for single positioning frequency layer in FR2 SA without RX FH in RRC\_CONNECTED mode	5712

A.17.7.6.1.1	Test purpose and environment	5712

A.17.7.6.1.2	Test parameters	5713

A.17.7.6.1.3	Test requirements	5716

A.17.7.6.2	SA: UE Rx-Tx time difference measurement accuracy with Rx FH in RRC\_CONNECTED state in FR2	5716

A.17.7.6.2.1	Test purpose and Environment	5716

A.17.7.6.2.2	Test parameters	5717

A.17.7.6.2.3	Test requirements	5720

A.17.7.7	PRS-RSRP Measurements	5720

A.17.7.7.1	PRS-RSRP measurement accuracy without FH in RRC\_CONNECTED state in FR2	5720

A.17.7.7.1.1	Test Purpose and Environment	5720

A.17.7.7.1.2	Test parameters	5720

A.17.7.7.1.3	Test Requirements	5723

A.17.7.7.2	PRS-RSRP measurement accuracy with FH in RRC\_CONNECTED state in FR2	5723

A.17.7.7.2.1	Test Purpose and Environment	5723

A.17.7.7.2.2	Test parameters	5724

A.17.7.7.2.3	Test Requirements	5726

A.17.7.8	PRS-RSRPP Measurements	5726

A.17.7.8.1	PRS-RSRPP measurement accuracy without FH in RRC\_CONNECTED state in FR2	5726

A.17.7.8.1.1	Test Purpose and Environment	5726

A.17.7.8.1.2	Test parameters	5727

A.17.7.8.1.3	Test Requirements	5729

A.17.7.8.2	SA: PRS-RSRPP measurement accuracy with Rx FH in RRC\_CONNECTED state in FR2	5729

A.17.7.8.2.1	Test purpose and Environment	5729

A.17.7.8.2.2	Test parameters	5730

A.17.7.8.2.3	Test requirements	5732

A.17.8	Measurement Procedure for RedCap in RRC\_INACTIVE	5733

A.17.8.1	RSTD Measurements	5733

A.17.8.1.1	NR RSTD measurement reporting delay test case for RedCap UE without FH in FR2 SA in RRC\_INACTIVE state	5733

A.17.8.1.1.1	Test Purpose and Environment	5733

A.17.8.1.1.2	Test Requirements	5736

A.17.8.1.2	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC\_INACTIVE state	5736

A.17.8.1.2.1	Test Purpose and Environment	5736

A.17.8.1.2.2	Test Requirements	5739

A.17.8.1.3	NR RSTD measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC\_INACTIVE state with eDRX &gt; 10.24s	5739

A.17.8.1.3.1	Test purpose and environment	5739

A.17.8.1.3.2	Test requirements	5739

A.17.8.2	UE Rx-Tx Measurements	5740

A.17.8.2.1	UE Rx-Tx measurement reporting delay for single positioning frequency layer in FR2 SA without RX FH in RRC\_INACTIVE mode	5740

A.17.8.2.1.1	Test purpose and environment	5740

A.17.8.2.1.2	Test requirements	5743

A.17.8.2.2	UE Rx-Tx time difference measurement with Rx FH for single positioning frequency layer in FR2 SA in RRC\_INACTIVE state	5743

A.17.8.2.2.1	Test purpose and environment	5743

A.17.8.2.2.2	Test requirements	5747

A.17.8.2.3	UE Rx-Tx time difference measurements for single positioning frequency layer with eDRX &gt; 10.24s in FR2 SA	5747

A.17.8.2.3.1	Test purpose and environment	5747

A.17.8.2.3.2	Test requirements	5747

A.17.8.3	PRS-RSRP Measurements	5748

A.17.8.3.1	PRS-RSRP reporting delay test case for single positioning frequency layer in RRC\_INACTIVE	5748

A.17.8.3.1.1	Test Purpose and Environment	5748

A.17.8.3.1.2	Test Requirements	5752

A.17.8.3.2.2	Test Requirements	5756

A.17.8.3.3	PRS-RSRP reporting delay in RRC\_INACTIVE with eDRX	5756

A.17.8.3.3.1	Test Purpose and Environment	5756

A.17.8.3.3.2	Test Requirements	5760

A.17.8.4	PRS-RSRPP Measurements	5760

A.17.8.4.1	PRS-RSRPP measurement delay without FH in RRC\_INACTIVE state in FR2	5760

A.17.8.4.1.1	Test Purpose and Environment	5760

A.17.8.4.2	PRS-RSRPP measurement with Rx FH reporting delay test case for single positioning frequency layer in FR2 SA in RRC\_INACTIVE state	5763

A.17.8.4.2.1	Test Purpose and Environment	5763

A.17.8.4.2.2	Test Requirements	5765

A.17.8.4.3	PRS-RSPP reporting delay in RRC\_INACTIVE state with eDRX &gt; 10.24s	5765

A.17.8.4.3.1	Test purpose and environment	5765

A.17.8.4.3.2	Test requirements	5765

A.17.9	Measurement Performance Requirements for RedCap in RRC\_INACTIVE	5766

A.17.9.1	RSTD Measurements	5766

A.17.9.1.1	RSTD measurement accuracy test case for RedCap UE without FH in FR2 in RRC\_INACTIVE state	5766

A.17.9.1.1.1	Test purpose and Environment	5766

A.17.9.1.1.2	Test Requirements	5768

A.17.9.1.2	RSTD measurement accuracy test case for RedCap UE with FH in FR2 in RRC\_INACTIVE state	5768

A.17.9.1.2.1	Test purpose and Environment	5768

A.17.9.1.2.2	Test Requirements	5770

A.17.9.2	UE Rx-Tx Measurements	5770

A.17.9.2.1	UE Rx-Tx measurement accuracy for single positioning frequency layer in FR2 SA without RX FH in RRC\_INACTIVE mode	5770

A.17.9.2.1.1	Test purpose and environment	5770

A.17.9.2.1.2	Test parameters	5771

A.17.9.2.1.3	Test requirements	5774

A.17.9.2.2	SA: UE Rx-Tx time difference measurement accuracy with Rx FH in RRC\_INACTIVE state in FR2	5774

A.17.9.2.2.1	Test purpose and Environment	5774

A.17.9.2.2.2	Test parameters	5774

A.17.9.2.2.3	Test requirements	5777

A.17.9.3	PRS-RSRP Measurements	5777

A.17.9.3.2	PRS-RSRP measurement accuracy with FH in RRC\_INACTIVE state in FR2	5779

A.17.9.3.2.1	Test Purpose and Environment	5779

A.17.9.3.2.2	Test parameters	5780

A.17.9.3.2.3	Test Requirements	5781

A.17.9.4	PRS-RSRPP Measurements	5781

A.17.9.4.1	SA: PRS-RSRPP measurement accuracy with Rx FH in RRC\_INACTIVE state in FR2	5781

A.17.9.4.1.1	Test Purpose and Environment	5781

A.17.9.4.1.2	Test parameters	5782

A.17.9.4.1.3	Test Requirements	5784

A.17.9.4.2	SA: PRS-RSRPP measurement accuracy with Rx FH in RRC\_INACTIVE state in FR2	5784

A.17.9.4.2.1	Test Purpose and Environment	5784

A.17.9.4.2.2	Test parameters	5785

A.17.9.4.2.3	Test Requirements	5787

A.17.10	Measurement Procedure for RedCap in RRC\_IDLE	5788

A.17.10.1	RSTD Measurements	5788

A.17.10.1.1	NR RSTD measurement reporting delay test case for RedCap UE without FH in FR2 SA in RRC\_IDLE state without eDRX	5788

A.17.10.1.1.1	Test Purpose and Environment	5788

A.17.10.1.1.2	Test Requirements	5791

A.17.10.1.2	NR RSTD without FH measurement reporting delay test case for single positioning frequency layer in FR2 SA in RRC\_IDLE state with eDRX &gt; 10.24s	5791

A.17.10.1.2.1	Test purpose and environment	5791

A.17.10.1.2.2	Test requirements	5791

A.17.10.2	PRS-RSRP Measurements	5792

A.17.10.2.1	PRS-RSRP measurement delay test case for single positioning frequency layer in RRC\_IDLE	5792

A.17.10.2.1.1	Test Purpose and Environment	5792

A.17.10.2.1.2	Test Requirements	5796

A.17.10.2.2	PRS-RSRP reporting delay test case in RRC\_IDLE state in FR2 when eDRX cycle &gt; 10.24s	5796

A.17.10.2.2.1	Test Purpose and Environment	5796

A.17.10.2.2.2	Test Requirements	5796

A.17.11	 Measurement Performance Requirements for RedCap in RRC\_IDLE	5797

A.17.11.1	RSTD Measurements	5797

A.17.11.1.1	RSTD measurement accuracy test case for RedCap UE without FH in FR2 in RRC\_IDLE state without eDRX	5797

A.17.11.1.1.1	Test purpose and Environment	5797

11.1.1.2	Test Requirements	5799

A.17.11.1.2	RSTD without FH measurement accuracy test case for single positioning frequency layer in FR2 SA in RRC\_IDLE state with eDRX &gt; 10.24s	5799

A.17.11.1.2.1	Test purpose and environment	5799

A.17.11.1.2.2	Test requirements	5801

A.17.11.2	PRS-RSRP Measurements	5801

A.17.11.2.1	PRS-RSRP measurement accuracy test case for RedCap UE in FR2 in RRC\_IDLE state	5801

A.17.11.2.1.1	Test Purpose and Environment	5801

A.17.11.2.1.2	Test parameters	5801

A.17.11.2.2	PRS-RSRP measurement accuracy test case in RRC\_IDLE state in FR2 when eDRX cycle &gt; 10.24s	5803

A.17.11.2.2.1	Test purpose and Environment	5803

A.17.11.2.2.1	Test parameters	5804

A.17.11.2.2.2	Test Requirements	5804

A.18	E-UTRA standalone tests for NR RRM for RedCap	5804

A.18.1	RRC\_IDLE state mobility	5804

A.18.1.1	Inter-RAT NR Cell re-selection	5804

A.18.1.1.1	E-UTRA Cell reselection to higher priority NR target Cell in FR1	5804

A.18.1.1.1.1	Test Purpose and Environment	5804

A.18.1.1.1.2	Test Requirements	5807

A.18.2	RRC\_CONNECTED state mobility	5807

A.18.2.1	Handover	5807

A.18.2.1.1	E-UTRAN - NR handover in FR1	5807

A.18.2.1.1.1	Test Purpose and Environment	5807

A.18.2.1.1.2	Test Requirements	5811

A.18.2.2	RRC connection release with redirection	5811

A.18.2.2.1	Redirection from E-UTRA to NR FR1 for redcap UE	5811

A.18.2.2.1.1	Test Purpose and Environment	5811

A.18.2.2.1.2	Test Parameters	5811

A.18.2.2.1.3	Test Requirements	5814

A.18.3	Measurement procedure	5815

A.18.3.1	E-UTRA – NR Inter-RAT Measurements	5815

A.18.3.1.1	NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is not used	5815

A.18.3.1.1.1	Test Purpose and Environment	5815

A.18.3.1.1.2	Test Requirements	5818

A.18.3.1.2	NR Inter-RAT event triggered reporting tests for FR1 without SSB time index detection when DRX is used	5818

A.18.3.1.2.1	Test Purpose and Environment	5818

A.18.3.1.2.2	Test Requirements	5822

A.18.3.1.3	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is not used	5822

A.18.3.1.3.1	Test Purpose and Environment	5822

A.18.3.1.3.2	Test Requirements	5826

A.18.3.1.4	NR Inter-RAT event triggered reporting tests for FR1 with SSB time index detection when DRX is used	5826

A.18.3.1.4.1	Test Purpose and Environment	5826

A.18.3.1.4.2	Test Requirements	5830

A.18.3.1.5	NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is not used	5830

A.18.3.1.5.1	Test Purpose and Environment	5830

A.18.3.1.5.2	Test Requirements	5832

A.18.3.1.6	NR Inter-RAT event triggered reporting tests for FR2 without SSB time index detection when DRX is used	5832

A.18.3.1.6.1	Test Purpose and Environment	5832

A.18.3.1.6.2	Test Requirements	5834

A.18.3.1.7	NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is not used	5835

A.18.3.1.7.1	Test Purpose and Environment	5835

A.18.3.1.7.2	Test Requirements	5837

A.18.3.1.8	NR Inter-RAT event triggered reporting tests for FR2 with SSB time index detection when DRX is used	5837

A.18.3.1.8.1	Test Purpose and Environment	5837

A.18.3.1.8.2	Test Requirements	5839

A.19	NR standalone tests for ATG	5840

A.19.1	RRC\_IDLE state mobility	5840

A.19.1.1	Cell reselection to FR1 intra-frequency NR case	5840

A.19.1.1.1	Test Purpose and Environment	5840

A.19.1.1.2	Test Parameters	5840

A.19.1.1.3	Test Requirements	5841

A.19.1.2	Cell reselection to FR1 inter-frequency NR case	5841

A.19.1.2.1	Test Purpose and Environment	5841

A.19.1.2.2	Test Parameters	5841

A.19.1.2.3	Test Requirements	5843

A.19.1.3	Cell reselection to FR1 inter-frequency NR case for UE configured with *hs-ATG-cellReselectionSet-r18* 5844

A.19.1.3.1	Test Purpose and Environment	5844

A.19.1.3.2	Test Parameters	5844

A.19.1.3.3	Test Requirements	5846

A.19.2	RRC\_CONNECTED state mobility	5847

A.19.2.1	Handover	5847

A.19.2.1.1	Intra-frequency handover from FR1 to FR1; known target cell	5847

A19.2.1.1.1	Test Purpose and Environment	5847

A.19.2.1.1.2	Test Parameters	5847

A.19.2.1.2.3	Test Requirements	5847

A.19.2.1.2	Inter-frequency handover from FR1 to FR1; unknown target cell	5848

A.19.2.1.2.1	Test Purpose and Environment	5848

A.19.2.1.2.2	Test Parameters	5848

A.19.2.1.2.3	Test Requirements	5849

A.19.2.2	Conditional Handover	5849

A.19.2.2.1	Intra-frequency distance-based conditional Handover from FR1 to FR1	5849

A.19.2.2.1.1	Test Purpose and Environment	5849

A.19.2.2.1.2	Test Parameters	5849

A.19.2.2.1.3	Test Requirements	5851

A.19.2.2.2	Inter-frequency distance-based conditional Handover from FR1 to FR1	5852

A.19.2.2.2.1	Test Purpose and Environment	5852

A.19.2.2.2.2	Test Parameters	5852

A.19.2.2.2.3	Test Requirements	5854

A.19.2.3	RRC Connection Mobility Control	5854

A.19.2.3.1	SA: RRC Re-establishment	5854

A.19.2.3.1.1	Intra-frequency RRC Re-establishment in FR1 for ATG	5854

A.19.2.3.1.1.1	Test Purpose and Environment	5855

A.19.2.3.1.1.2 Test Requirements	5855

A.19.2.3.1.2	Inter-frequency RRC Re-establishment in FR1 with unknown target cell without serving cell timing for ATG	5855

A.19.2.3.1.2.1	Test Purpose and Environment	5855

A.19.2.3.1.2.2	Test Requirements	5857

A.19.2.3.2	Random Access for ATG UE	5858

A.19.2.3.2.1.1	Test Purpose and Environment	5858

A.19.2.3.2.1.2	Test Requirements	5859

A.19.2.3.2.2.1	Test Purpose and Environment	5859

A.19.2.3.2.2.2	Test Requirements	5859

A.19.2.3.2.3	2-step RA type contention based random access test in FR1 for NR standalone	5859

A.19.2.3.2.3.1	Test Purpose and Environment	5859

A.19.2.3.2.3.2	Test Requirements	5860

A.19.2.3.2.4	2-step RA type non-contention based test in FR1 for NR standalone	5860

A.19.2.3.2.4.1	Test Purpose and Environment	5860

A.19.2.3.2.4.2	Test Requirements	5861

A.19.2.3.3.1.1	Test Purpose and Environment	5861

A.19.2.3.3.1.2	Test Parameters	5861

A.19.2.3.3.1.3	Test Requirements	5862

A.19.3	Timing	5862

A.19.3.1	UE transmit timing	5862

A.19.3.1.1	ATG UE Transmit Timing Test for FR1	5862

A.19.3.1.1.1	Test Purpose and environment	5862

A.19.3.1.1.2	Test requirements	5864

A.19.3.2	UE timer accuracy	5864

A.19.3.3	Timing advance	5864

A.19.3.3.1	SA FR1 timing advance adjustment accuracy	5864

A.19.3.3.1.1	Test Purpose and Environment	5864

A.19.3.3.1.2	Test Parameters	5864

A.19.3.3.1.3	Test Requirements	5865

A.19.4	Signalling characteristics	5865

A.19.4.1	Radio link Monitoring	5865

A.19.4.1.1	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode	5865

A.19.4.1.1.1	Test Purpose and Environment	5866

A.19.4.1.1.2	Test Requirements	5868

A.19.4.1.2	Radio Link Monitoring In-sync Test for FR1 PCell configured with SSB-based RLM RS in non-DRX mode	5868

A.19.4.1.2.1	Test Purpose and Environment	5868

A.19.4.1.2.2	Test Requirements	5871

A.19.4.1.3	Radio Link Monitoring Out-of-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode	5871

A.19.4.1.3.1	Test Purpose and Environment	5871

A.19.4.1.3.2	Test Requirements	5874

A.19.4.1.4	Radio Link Monitoring In-sync Test for FR1 PCell configured with CSI-RS-based RLM in non-DRX mode	5875

A.19.4.1.4.1	Test Purpose and Environment	5875

A.19.4.1.4.2	Test Requirements	5878

A.19.4.2	Beam Failure Detection and Link recovery procedures	5878

A.19.4.2.1	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with SSB-based BFD and LR in non-DRX mode	5878

A.19.4.2.1.1	Test Purpose and Environment	5878

A.19.4.2.1.2	Test Requirements	5882

A.19.4.2.2	Beam Failure Detection and Link Recovery Test for FR1 PCell configured with CSI-RS-based BFD and LR in non-DRX mode	5882

A.19.4.2.2.1	Test Purpose and Environment	5882

A.19.4.2.2.2	Test Requirements	5886

A.19.4.3	Active BWP switch	5886

A.19.4.3.1	DCI-based and Timer-based Active BWP Switch	5886

A.19.4.3.1.1	NR FR1 DL active BWP switch with non-DRX in SA	5886

A.19.4.3.2	RRC-based Active BWP Switch	5889

A.19.4.3.2.1	NR FR1 DL active BWP switch of Cell with non-DRX in SA	5889

A.19.4.4	UE specific CBW change	5891

A19.4.4.1	UE specific CBW change on PCell in FR1 in non-DRX	5891

A19.4.4.1.1	Test Purpose and Environment	5891

A.19.4.4.1.2	Test Requirements	5894

A.19.4.5	Pathloss reference signal switching delay	5894

A.19.4.5.1	MAC-CE based pathloss reference signal switch delay	5894

A.19.4.5.1.1	Test Purpose and Environment	5894

A.19.4.5.1.2	Test Requirements	5896

A.19.5	Measurement procedure	5897

A.19.5.1	Intra-frequency Measurements	5897

A.19.5.1.1	SA event triggered reporting tests without gap without SSB index reading under non-DRX	5897

A.19.5.1.1.1	Test purpose and Environment	5897

A.19.5.1.1.2	Test parameters	5897

A.19.5.1.1.3	Test Requirements	5897

A.19.5.1.2	SA event triggered reporting tests with per-UE gaps under non-DRX	5898

A.19.5.1.2.1	Test purpose and Environment	5898

A.19.5.1.2.2	Test parameters	5898

A.19.5.1.2.3	Test Requirements	5898

A.19.5.1.3	SA event triggered reporting tests without gap under non-DRX with SSB index reading	5898

A.19.5.1.3.1	Test purpose and Environment	5898

A.19.5.1.3.2	Test parameters	5898

A.19.5.1.3.3	Test Requirements	5899

A.19.5.1.4	SA event triggered reporting tests with per-UE gaps under non-DRX with SSB index reading	5899

A.19.5.1.4.1	Test purpose and Environment	5899

A.19.5.1.4.2	Test parameters	5899

A.19.5.1.4.3	Test Requirements	5900

A.19.5.2	Inter-frequency Measurements	5900

A.19.5.2.1.2	Test parameters	5900

A.19.5.2.1.3	Test Requirements	5901

A.19.5.2.2.2	Test parameters	5902

A.19.5.2.3.2	Test parameters	5902

A.19.5.2.3.3	Test Requirements	5903

A.19.5.3	L1-RSRP measurement for beam reporting for ATG	5903

A.19.5.3.1	SSB based L1-RSRP measurement when DRX is not used	5903

A.19.5.3.1.1	Test Purpose and Environment	5903

A.19.5.3.1.2	Test parameters	5903

A.19.5.3.1.3	Test Requirements	5904

A.19.5.3.2	CSI-RS based L1-RSRP measurement when DRX is not used	5904

A.19.5.3.2.1	Test Purpose and Environment	5904

A.19.5.3.2.2	Test parameters	5904

A.19.5.3.2.3	Test Requirements	5904

A.19.5.4	L1-SINR measurement for beam reporting for ATG	5904

A.19.5.4.1	L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured when DRX is not used	5904

A.19.5.4.1.3	Test Requirements	5905

A.19.5.4.2	L1-SINR measurement with SSB based CMR and dedicated IMR when DRX is not used	5905

A.19.5.4.2.1	Test Purpose and Environment	5905

A.19.5.4.2.2	Test parameters	5905

A.19.5.4.2.3	Test Requirements	5906

A.19.5.4.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR configured when DRX is not used	5906

A.19.5.4.3.1	Test Purpose and Environment	5906

A.19.5.4.3.2	Test parameters	5906

A.19.5.4.3.3	Test Requirements	5906

A.19.5.5	NR measurements with autonomous gaps for ATG	5907

A.19.5.5.1	SA intra-frequency CGI identification of NR neighbor cell in FR1	5907

A.19.5.5.1.1	Test Purpose and Environment	5907

A.19.5.5.1.2	Test Parameters	5907

A.19.5.5.1.3	Test Requirements	5907

A.19.6	Measurement Performance requirements	5907

A.19.6.1	SS-RSRP for ATG UE	5908

A.19.6.1.1	SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell	5908

A.19.6.1.1.1	Test Purpose and Environment	5908

A.19.6.1.1.2	Test parameters	5908

A.19.6.1.1.3	Test Requirements	5908

A.19.6.1.2	SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell	5908

A.19.6.1.2.1	Test Purpose and Environment	5908

A.19.6.1.2.2	Test parameters	5909

A.19.6.1.2.3	Test Requirements	5909

A.19.6.2	SS-RSRQ for ATG UE	5909

A.19.6.2.1	SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	5909

A.19.6.2.1.1	Test Purpose and Environment	5909

A.19.6.2.1.2	Test Parameters	5909

A.19.6.2.1.3	Test Requirements	5910

A.19.6.2.2	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	5910

A.19.6.2.2.1	Test Purpose and Environment	5910

A.19.6.2.2.2	Test Parameters	5910

A.19.6.2.2.3	Test Requirements	5910

A.19.6.3	SS-SINR for ATG UE	5911

A.19.6.3.1	SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	5911

A.19.6.3.1.1	Test Purpose and Environment	5911

A.19.6.3.1.2	Test Parameters	5911

A.19.6.3.1.3	Test Requirements	5911

A.19.6.3.2	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	5911

A.19.6.3.2.1	Test Purpose and Environment	5911

A.19.6.3.2.2	Test Parameters	5911

A.19.6.3.2.3	Test Requirements	5912

A.19.6.4	L1-RSRP measurement for beam reporting for ATG UE	5912

A.19.6.4.1	SSB based L1-RSRP measurement	5912

A.19.6.4.1.1	Test Purpose and Environment	5912

A.19.6.4.1.2	Test parameters	5912

A.19.6.4.1.3	Test Requirements	5913

A.19.6.4.2	CSI-RS based L1-RSRP measurement on resource set with repetition off	5913

A.19.6.4.2.1	Test Purpose and Environment	5913

A.19.6.4.2.2	Test parameters	5913

A.19.6.4.2.3	Test Requirements	5913

A.19.6.5	L1-SINR measurement for beam reporting based CMR for ATG UE	5914

A.19.6.5.1	L1-SINR measurement with CSI-RS based CMR and no dedicated IMR configured and CSI-RS resource set with repetition off	5914

A.19.6.5.1.1	Test Purpose and Environment	5914

A.19.6.5.1.2	Test parameters	5914

A.19.6.5.1.3	Test Requirements	5914

A.19.6.5.2	L1-SINR measurement with SSB based CMR and dedicated IMR	5914

A.19.6.5.2.1	Test Purpose and Environment	5914

A.19.6.5.2.2	Test parameters	5915

A.19.6.5.2.3	Test Requirements	5915

A.19.6.5.3	L1-SINR measurement with CSI-RS based CMR and dedicated IMR	5915

A.19.6.5.3.1	Test Purpose and Environment	5915

A.19.6.5.3.2	Test parameters	5915

A.19.6.5.3.3	Test Requirements	5916

A.19.6.6	CSI-RSRP for ATG UE	5916

A.19.6.6.1	SA: intra-frequency case measurement accuracy with FR1 serving cell and FR1 target cell	5916

A.19.6.6.1.1	Test Purpose and Environment	5916

A.19.6.6.1.2	Test parameters	5916

A.19.6.6.1.3	Test Requirements	5916

A.19.6.6.2	SA inter-frequency case measurement accuracy with FR1 serving cell and FR1 target cell	5917

A.19.6.6.2.1	Test Purpose and Environment	5917

A.19.6.6.2.2	Test parameters	5917

A.19.6.6.2.3	Test Requirements	5917

A.19.6.7	CSI-RSRQ for ATG UE	5917

A.19.6.7.1	SA: Intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	5917

A.19.6.7.1.1	Test Purpose and Environment	5917

A.19.6.7.1.2	Test Parameters	5917

A.19.6.7.1.3	Test Requirements	5918

A.19.6.7.2	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	5918

A.19.6.7.2.1	Test Purpose and Environment	5918

A.19.6.7.2.2	Test Parameters	5918

A.19.6.7.2.3	Test Requirements	5919

A.19.6.8	CSI-SINR for ATG UE	5919

A.19.6.8.1	SA intra-frequency measurement accuracy with FR1 serving cell and FR1 target cell	5919

A.19.6.8.1.1	Test Purpose and Environment	5919

A.19.6.8.1.2	Test Parameters	5919

A.19.6.8.1.3	Test Requirements	5919

A.19.6.8.2	SA Inter-frequency measurement accuracy with FR1 serving cell and FR1 target cell	5920

A.19.6.8.2.1	Test Purpose and Environment	5920

A.19.6.8.2.2	Test Parameters	5920

A.19.6.8.2.3	Test Requirements	5920

Annex B (normative): Conditions for RRM requirements applicability for operating bands	5922

B.1	Conditions for NR RRC\_IDLE state mobility	5922

B.1.1	Introduction	5922

B.1.2	Conditions for measurements on NR intra-frequency cells for cell re-selection	5922

B.1.2A	Conditions for measurements on NR intra-frequency cells under CCA for cell re-selection	5924

B.1.3	Conditions for measurements on NR inter-frequency cells for cell re-selection	5925

B.1.3A	Conditions for measurements on NR inter-frequency cells under CCA for cell re-selection	5925

B.1.4	Conditions for measurements on NR intra-frequency cells for cell re-selection for RedCap	5925

B.1.5	Conditions for measurements on NR inter-frequency cells for cell re-selection for RedCap	5928

B.1.6	Conditions for measurements on NR intra-frequency cells for cell re-selection for satellite access	5928

B.1.7	Conditions for measurements on NR inter-frequency cells for cell re-selection for satellite access	5928

B.2	Conditions for UE measurements procedures and performance requirements in RRC\_CONNECTED state	5928

B.2.1	Introduction	5928

B.2.1.1	General	5928

B.2.1.2	Derivation of Minimum SSB\_RP values for FR1	5929

B.2.1.3	Derivation of Minimum SSB\_RP values for FR2	5929

B.2.1.3.1	Minimum SSB\_RP values for Rx Beam Peak angle of arrival	5929

B.2.1.3.2	Minimum SSB\_RP values for angle of arrival within Spherical coverage	5930

B.2.1.4	Gain to SS-RSRP and CSI-RSRP measurement point for FR1	5930

B.2.1.5	Gain to SS-RSRP and CSI-RSRP measurement point for FR2	5930

B.2.1.5.1	Gain to SS-RSRP and CSI-RSRP measurement point for Rx Beam Peak angle of arrival	5930

B.2.1.5.2	Gain to SS-RSRP measurement point for different frequency	5931

B.2.1.5.3	Alignment of Rough beam to Rx beam Peak	5931

B.2.1.6	Gain to PRS-RSRP measurement point for FR2	5932

B.2.1.6.1	Gain to PRS-RSRP measurement point for Rx Beam Peak angle of arrival	5932

B.2.1.7	Derivation of Minimum SSB\_RP values for FR2-NTN for satellite access	5932

B.2.1.7.1	Minimum SSB\_RP values for Rx Beam	5932

B.2.1.8	Gain to SS-RSRP for FR2-NTN for satellite access	5933

B.2.2	Conditions for NR intra-frequency measurements	5934

B.2.3	Conditions for NR inter-frequency measurements	5936

B.2.4	Conditions for NR L1-RSRP reporting	5938

B.2.4.1	Conditions for SSB based L1-RSRP reporting	5938

B.2.4.2	Conditions for CSI-RS based L1-RSRP reporting	5940

B.2.5	Conditions for RRC connection release with redirection to NR	5942

B.2.6	Void	5944

B.2.6.1	Void	5944

B.2.6.2	Void	5944

B.2.7	Conditions for SRS-RSRP measurements	5944

B.2.8	Conditions for NR L1-SINR reporting	5945

B.2.8.1	Conditions for L1-SINR reporting with CSI-RS based CMR and no dedicated IMR configured	5945

B.2.8.2	Conditions for L1-SINR reporting with SSB based CMR and dedicated IMR configured	5947

B.2.8.2.1	L1-SINR reporting with SSB based CMR and dedicated ZP-IMR configured	5947

B.2.8.2.2	L1-SINR reporting with SSB based CMR and dedicated NZP-IMR configured	5949

B.2.8.3	Conditions for L1-SINR reporting with CSI-RS based CMR and dedicated IMR configured	5951

B.2.8.3.1	L1-SINR reporting with CSI-RS based CMR and dedicated ZP-IMR configured	5951

B.2.8.3.2	L1-SINR reporting with CSI-RS based CMR and dedicated NZP-IMR configured	5953

B.2.9	Conditions for NR intra-frequency measurements under CCA	5955

B.2.10	Conditions for NR inter-frequency measurements under CCA	5955

B.2.11	Conditions for NR L1-RSRP reporting under CCA	5955

B.2.11.1	Conditions for SSB based L1-RSRP reporting	5955

B.2.12	Conditions for NR CSI-RS based intra-frequency measurements	5956

B.2.13	Conditions for NR CSI-RS based inter-frequency measurements	5957

B.2.14	Conditions for NR PRS-based measurements	5958

B.2.15	Conditions for NR intra-frequency measurements for RedCap	5960

B.2.16	Conditions for NR inter-frequency measurements for RedCap	5961

B.2.17	Conditions for NR intra-frequency measurements for satellite access	5963

B.2.18	Conditions for NR inter-frequency measurements for satellite access	5963

B.2.19	Conditions for NR L1-RSRP reporting for satellite access	5963

B.2.19.1	Conditions for SSB based L1-RSRP reporting for satellite access	5964

B.2.19.2	Conditions for CSI-RS based L1-RSRP reporting for satellite access	5964

B.2.20	Conditions for RRC connection release with redirection to NR for satellite access	5964

B.3	RRM Requirements Exceptions	5964

B.3.1	Introduction	5964

B.3.2	Receiver sensitivity relaxation for CA	5965

B.3.2.1	Receiver sensitivity relaxation for UE supporting CA in FR1	5965

B.3.2.2	Receiver sensitivity relaxation for UE configured with CA in FR1	5965

B.3.2.2.1	Inter-band carrier aggregation	5965

B.3.2.2.2	Reference sensitivity exceptions due to UL harmonic interference for CA	5965

B.3.2.2.3	Reference sensitivity exceptions due to intermodulation interference due to 2UL CA	5965

B.3.2.3	Receiver sensitivity relaxation for UE supporting CA in FR2	5965

B.3.2.4	Receiver sensitivity relaxation for UE configured with CA in FR2	5966

B.3.2.4.1	Intra-band contiguous carrier aggregation	5966

B.3.2.4.2	Intra-band non-contiguous carrier aggregation	5966

B.3.3	Receiver sensitivity relaxation for DC	5966

B.3.3.1	Receiver sensitivity relaxation for EN-DC	5966

B.3.3.2	Receiver sensitivity relaxation for NE-DC	5966

B.3.4	Receiver sensitivity relaxation for SUL	5966

B.3.4.1	Receiver sensitivity relaxation for UE supporting SUL in FR1	5966

B.3.4.2	Receiver sensitivity relaxation for UE configured with SUL in FR1	5966

B.3.4.2.1	Reference sensitivity exceptions due to UL harmonic interference for SUL	5966

B.4	Conditions for V2X	5967

B.4.1	Test parameters for GNSS signals	5967

B.4.2	Conditions for PSBCH-RSRP Accuracy Requirements	5967

B.4.3	Conditions for Selection/Reselection to Intra-frequency SyncRef UE	5967

B.4.4	Conditions for L1 SL-RSRP Accuracy Requirements	5968

B.4.5	Conditions for PSBCH-RSRP Accuracy Requirements under CCA	5968

B.4.6	Conditions for Selection/Reselection to Intra-frequency SyncRef UE under CCA	5968

B.4.7	Conditions for L1 SL-RSRP Accuracy Requirements under CCA	5969

B.4A	Conditions for NR Sidelink Positioning Measurement Procedures and Performance Requirements	5969

B.4A.1	Conditions for NR SL-PRS based measurements	5969

B.5	High level test procedure for SAN RRM tests	5969

Annex C (informative): Change history	5971