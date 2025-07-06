+----------------------------------+----------------------------------+
| 3GPP TR 38.858 V18.1.0 (2024-03) |                                  |
+==================================+==================================+
| Technical Report                 |                                  |
+----------------------------------+----------------------------------+
| 3rd Generation Partnership       |                                  |
| Project;                         |                                  |
|                                  |                                  |
| Technical Specification Group    |                                  |
| Radio Access Network;            |                                  |
|                                  |                                  |
| *Study on Evolution of NR Duplex |                                  |
| Operation*                       |                                  |
|                                  |                                  |
| (Release 18)                     |                                  |
+----------------------------------+----------------------------------+
|                                  |                                  |
+----------------------------------+----------------------------------+
| ![](./media/image1.p             | ![](./media/image2.p             |
| ng){width="1.4152777777777779in" | ng){width="1.7673611111111112in" |
| height="0.8631944444444445in"}   | height="1.0409722222222222in"}   |
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
| © 2024, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, |
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

######### Annex \<C\>: System level simulation calibration

C.1 SLS calibration methodology
===============================

**[Calibration scenarios]{.underline}**

The SLS calibration focuses on the following scenarios of SBFD
Deployment Case 1:

\- FR1

\- Urban Macro

\- Indoor office

\- FR2-1

\- Dense Urban Macro layer

\- Indoor office

**[Calibration metrics]{.underline}**

*The following metrics are considered for **SLS calibration:***

\- CDF of gNB-UE coupling loss

\- CDF of Inter-gNB coupling loss

\- CDF of Inter-UE coupling loss

\- Optional: CDF of DL SINR for legacy TDD/ DL SINR in DL-only slots for
SBFD

\- Optional: CDF of DL SINR in SBFD slots

\- Optional: CDF of UL SINR for legacy TDD/ UL SINR in UL-only slots for
SBFD

\- Optional: CDF of UL SINR in SBFD slots

Table C.1-1: Statistic method for SLS calibration

+----------------------------------+----------------------------------+
| **SLS calibration metrics**      | **Statistic method**             |
+==================================+==================================+
| **gNB-UE coupling loss**         | Only the coupling losses between |
|                                  | each UE and its serving cell are |
|                                  | collected for CDF statistic.     |
|                                  |                                  |
|                                  | -   $\mathbf{w}_{A}$ and         |
|                                  |     $\mathbf{g}_{B}$ are         |
|                                  |     determined by selecting the  |
|                                  |     best beam pair of the UE and |
|                                  |     its serving cell with the    |
|                                  |     criteria of maximizing       |
|                                  |     receive power of the UE.     |
+----------------------------------+----------------------------------+
| **Inter-gNB coupling loss**      | For one SLS drop, generate       |
|                                  | channels among gNBs, calculate   |
|                                  | and collect the coupling loss    |
|                                  | for each gNB pair                |
|                                  |                                  |
|                                  | -   The two gNBs in each gNB     |
|                                  |     pair should be from          |
|                                  |     different sites.             |
|                                  |                                  |
|                                  | -   Both $\mathbf{w}_{A}$ and    |
|                                  |     $\mathbf{g}_{B}$ are         |
|                                  |     randomly selected for        |
|                                  |     calculating the coupling     |
|                                  |     loss for each gNB pair.      |
|                                  |                                  |
|                                  | Companies to run enough SLS      |
|                                  | drops and report the number of   |
|                                  | SLS drops when plotting the CDF  |
|                                  | using the collected coupling     |
|                                  | losses.                          |
+----------------------------------+----------------------------------+
| **Inter-UE coupling loss**       | For one SLS drop, drop UEs in    |
|                                  | the network and generate         |
|                                  | channels among UEs, calculate    |
|                                  | and collect the coupling loss    |
|                                  | for each UE pair                 |
|                                  |                                  |
|                                  | -   For all of Urban Macro,      |
|                                  |     Dense Urban Macro Layer and  |
|                                  |     Indoor office scenarios, if  |
|                                  |     the 2D distance between two  |
|                                  |     UEs in a UE pair is larger   |
|                                  |     than 50m, the UE pair is not |
|                                  |     considered for statistic.    |
|                                  |                                  |
|                                  | -   For each UE,                 |
|                                  |     $\mathbf{w}_{A}$ and         |
|                                  |     $\mathbf{g}_{B}$ is          |
|                                  |     determined based on the best |
|                                  |     beam pair of the UE and its  |
|                                  |     serving cell.                |
|                                  |                                  |
|                                  | Companies to run enough SLS      |
|                                  | drops and report the number of   |
|                                  | SLS drops when plotting the CDF  |
|                                  | using the collected coupling     |
|                                  | losses.                          |
+----------------------------------+----------------------------------+
| NOTE 1: ***For calibration, only |                                  |
| large scale fading is            |                                  |
| modelled.*** Formula (A-16) in   |                                  |
| Annex A.8 for CL with averaging  |                                  |
| across all the Tx/Rx ports is    |                                  |
| used for coupling loss           |                                  |
| calculation above, i.e.,         |                                  |
|                                  |                                  |
| $$\text{CL                       |                                  |
| }^{A,B}\left( \mathbf{w}_{A},\ma |                                  |
| thbf{g}_{B} \right) = \frac{1}{S |                                  |
| }\sum_{p = 0}^{S - 1}\left( \fra |                                  |
| c{1}{U}\sum_{u = 0}^{U - 1}{\tex |                                  |
| t{CL}_{p,u}^{A,B}\left( \mathbf{ |                                  |
| w}_{A},\mathbf{g}_{B} \right)} \ |                                  |
| right) = \frac{1}{S}\sum_{p = 0} |                                  |
| ^{S - 1}\left( \text{PL} \bullet |                                  |
|  \text{SF} \bullet \frac{1}{U}\s |                                  |
| um_{u = 0}^{U - 1}\left| {\alpha |                                  |
| '}_{0,u,p} \right|^{2} \right)$$ |                                  |
|                                  |                                  |
| -   Not modelling fast fading    |                                  |
|     doesn't impact the           |                                  |
|     calculation of path loss     |                                  |
|     *PL* and shadowed fading     |                                  |
|     *SF*                         |                                  |
|                                  |                                  |
| -   The antenna pattern related  |                                  |
|     part                         |                                  |
|     (${\alpha^{'}}_{0,u,p}$) is  |                                  |
|     calculated based on the LOS  |                                  |
|     direction between the two    |                                  |
|     nodes*, i.e.*,               |                                  |
|     $                            |                                  |
| \theta_{LOS,ZOA}/\phi_{LOS,AOA}/ |                                  |
| \theta_{LOS,ZOD}/\phi_{LOS,AOD}$ |                                  |
|                                  |                                  |
| NOTE 2: The beams for above      |                                  |
| cases are selected based on a    |                                  |
| defined set of beams for FR1 and |                                  |
| FR2 in the table for calibration |                                  |
| assumptions.                     |                                  |
+----------------------------------+----------------------------------+

C.2 SLS calibration assumptions
===============================

Table C.2-1: SLS calibration assumptions

+-------------+-------------+-------------+-------------+-------------+
|             | **Urban     | **Dense     | **Indoor    | **Indoor    |
|             | Macro       | Urban Macro | office      | office      |
|             | (FR1)**     | Layer       | (FR1)**     | (FR2-1)**   |
|             |             | (FR2-1)**   |             |             |
+=============+=============+=============+=============+=============+
| **Carrier   | 4 GHz       | 30GHz       | 4 GHz       | 30GHz       |
| frequency** |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **System    | 100MHz      | 100MHz      | 100MHz      | 100MHz      |
| bandwidth** |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **N         | 14 OFDM     | 14 OFDM     | 14 OFDM     | 14 OFDM     |
| umerology** | symbol slot | symbol slot | symbol slot | symbol slot |
|             |             |             |             |             |
|             | SCS = 30kHz | SCS =       | SCS = 30kHz | SCS =       |
|             |             | 120kHz      |             | 120kHz      |
+-------------+-------------+-------------+-------------+-------------+
| **BS        | 53 dBm for  | 40 dBm for  | 24 dBm for  | 23 dBm for  |
| transmit    | 100MHz is   | 100MHz is   | 100MHz is   | 100MHz is   |
| power for   | assume for  | assume for  | assume for  | assume for  |
| SBFD**      | maximum BS  | maximum BS  | maximum BS  | maximum BS  |
|             | transmit    | transmit    | transmit    | transmit    |
|             | power for   | power for   | power for   | power for   |
|             | legacy TDD  | legacy TDD  | legacy TDD  | legacy TDD  |
+-------------+-------------+-------------+-------------+-------------+
|             | Assume the  |             |             |             |
|             | BS transmit |             |             |             |
|             | power       |             |             |             |
|             | spectrum    |             |             |             |
|             | density is  |             |             |             |
|             | kept the    |             |             |             |
|             | same for    |             |             |             |
|             | SBFD        |             |             |             |
|             | operation   |             |             |             |
|             | and legacy  |             |             |             |
|             | TDD         |             |             |             |
|             | operation.  |             |             |             |
|             | BS transmit |             |             |             |
|             | power is    |             |             |             |
|             | p           |             |             |             |
|             | roportional |             |             |             |
|             | to the RBs  |             |             |             |
|             | used for DL |             |             |             |
|             | tr          |             |             |             |
|             | ansmission. |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **UE Tx     | 23dBm       | 23 dBm.     | 23dBm       | 23 dBm.     |
| power**     |             | EIRP should |             | EIRP should |
|             |             | not exceed  |             | not exceed  |
|             |             | 43 dBm      |             | 43 dBm      |
+-------------+-------------+-------------+-------------+-------------+
| **Layout**  | Hexagonal   | 12 TRPs per |             |             |
|             | grid with 7 | 120m x 50m  |             |             |
|             | macro sites | x 3m        |             |             |
|             | and 3       |             |             |             |
|             | sectors per |             |             |             |
|             | site with   |             |             |             |
|             | wrap around |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **Inter-BS  | 500m        | 200m        | 20m         |             |
| (2D)        |             |             |             |             |
| distance**  |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **Minimum   | 35m         | 35m         | 0m          |             |
| BS-UE (2D)  |             |             |             |             |
| distance**  |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **Minimum   | 1m          | 1m          | 1m          |             |
| UE-UE (2D)  |             |             |             |             |
| distance**  |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **BS        | 25m         | 25m         | 3m          |             |
| antenna     |             |             |             |             |
| height**    |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **UE        | UE          | UE          | Uniform     |             |
| dis         | Clustering  | Clustering  |             |             |
| tribution** |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **UE number | 20          | 10          | 10          |             |
| per         |             |             |             |             |
| m           |             |             |             |             |
| acro/indoor |             |             |             |             |
| TRP (per    |             |             |             |             |
| direction)  |             |             |             |             |
| (M)**       |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **UE        | 2           | 1           | \-          |             |
| cluster     |             |             |             |             |
| number per  |             |             |             |             |
| macro cell  |             |             |             |             |
| (X)**       |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **UE number | 8           | 8           | \-          |             |
| per         |             |             |             |             |
| cluster**   |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **UE        | 20% outdoor | 100%        | 100% indoor |             |
| out         | in cars:    | outdoor     | in houses:  |             |
| door/indoor | 30km/h; 80% | without car | 3km/h       |             |
| p           | indoor in   | penetration |             |             |
| roportion** | houses:     | loss: 3km/h |             |             |
|             | 3km/h       |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **Indoor UE | 1.5m        | 1.5m        | 1.5m        |             |
| height      |             |             |             |             |
| (m)**       |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **Outdoor   | 1.5m        | 1.5m        | \-          |             |
| UE height   |             |             |             |             |
| (m)**       |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **Radius of | 25m         | 20m         | \-          |             |
| cluster     |             |             |             |             |
| (R)**       |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **Minimum   | 60m         | 55m         | \-          |             |
| distance    |             |             |             |             |
| between     |             |             |             |             |
| macro TRP   |             |             |             |             |
| to UE       |             |             |             |             |
| cluster     |             |             |             |             |
| center      |             |             |             |             |
| (           |             |             |             |             |
| D~macro-to- |             |             |             |             |
| cluster~)** |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **Minimum   | 50m         | \-          | \-          |             |
| distance    |             |             |             |             |
| between two |             |             |             |             |
| UE cluster  |             |             |             |             |
| centers     |             |             |             |             |
| (D~inter-   |             |             |             |             |
| cluster~)** |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **gNB-UE    | M           | TRP-to-UE:  |             |             |
| Channel     | acro-to-UE: | InH-Office  |             |             |
| model**     | UMa in TR   | in TR       |             |             |
|             | 38.901      | 38.901      |             |             |
|             |             |             |             |             |
|             | **For FR1,  | Penetration |             |             |
|             | gNB-UE O2I  | loss is not |             |             |
|             | penetration | modelled.   |             |             |
|             | loss: 8**0% |             |             |             |
|             | low-loss    |             |             |             |
|             | model, 20%  |             |             |             |
|             | high-loss   |             |             |             |
|             | model       |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **gNB-gNB   | Macr        | TRP-to-TRP: |             |             |
| Channel     | o-to-Macro: | InH-Office  |             |             |
| model       | UMa in TR   | in TR       |             |             |
| (lar        | 38.901      | 38.901      |             |             |
| ge-scale)** | (h~UE~      | (h~UE~ =3m) |             |             |
|             | =25m)       |             |             |             |
|             |             | Penetration |             |             |
|             | LOS         | loss is not |             |             |
|             | p           | modelled.   |             |             |
|             | robability: |             |             |             |
|             | If the 2D   |             |             |             |
|             | distance    |             |             |             |
|             | between two |             |             |             |
|             | Macro gNBs  |             |             |             |
|             | are less    |             |             |             |
|             | than or     |             |             |             |
|             | equal to    |             |             |             |
|             | the ISD,    |             |             |             |
|             | set the LOS |             |             |             |
|             | probability |             |             |             |
|             | to 0.75;    |             |             |             |
|             | Otherwise,  |             |             |             |
|             | reuse       |             |             |             |
|             | gNB-to-UE   |             |             |             |
|             | LOS         |             |             |             |
|             | probability |             |             |             |
|             | equation in |             |             |             |
|             | TR 38.901.  |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **UE-UE     | UE-to-UE:   | UE-to-UE:   |             |             |
| Channel     | UMi-Street  | InH-Office  |             |             |
| model       | canyon in   | in TR       |             |             |
| (lar        | TR 38.901   | 38.901      |             |             |
| ge-scale)** | (h~BS~      | (h~BS~      |             |             |
|             | =1.5m).     | =1.5m)      |             |             |
|             |             |             |             |             |
|             | For FR1,    |             |             |             |
|             | penetration |             |             |             |
|             | loss        |             |             |             |
|             | between UEs |             |             |             |
|             | follows     |             |             |             |
|             | Table       |             |             |             |
|             | A.2.1-12 in |             |             |             |
|             | TR38.802    |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **BS        | ***         | ***         | ***         | ***         |
| antenna     | (M,N,P,Mg,N | (M,N,P,Mg,N | (M,N,P,Mg,N | (M,N,P,Mg,N |
| array       | g;Mp,Np***) | g;Mp,Np***) | g;Mp,Np***) | g;Mp,Np***) |
| co          | =           | =           | =           | =(          |
| nfiguration | (8,8        | (           | (4,4,2,1,1; | 16,8,2,1,1; |
| for Legacy  | ,2,1,1;2,8) | 4,16,2,2,2; | 4,4)        | 1,1)        |
| TDD**       |             | 1,1)        |             |             |
|             | $\left      |             | $\left(     | $\left(     |
|             | ( d_{H},d_{ | $\left(     |  d_{H},d_{V |  d_{H},d_{V |
|             | V} \right)$ |  d_{H},d_{V | } \right)$= | } \right)$= |
|             | = (0.5,     | } \right)$= | (0.5,       | (0.5,       |
|             | 0.8)λ,      | (0.5,       | 0.5)λ,      | 0.5)λ,      |
|             | +45°/-45°   | 0.5)λ,      | +45°/-45°   | +45°/-45°   |
|             | p           | +45°/-45°   | p           | p           |
|             | olarization | p           | olarization | olarization |
|             |             | olarization |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **BS        | SBFD        | SBFD        | SBFD        | SBFD        |
| antenna     | antenna     | antenna     | antenna     | antenna     |
| array       | co          | co          | co          | co          |
| co          | nfiguration | nfiguration | nfiguration | nfiguration |
| nfiguration | **Option 2  | **Option 2  | **Option 2  | Option 2    |
| for SBFD**  | (Method     | (Method     | (Method     | (Method     |
|             | 2-1)**      | 2-1)**      | 2-1)**      | 2-1)        |
|             |             |             |             |             |
|             | -   Two     | -   Two     | -   Two     | -   Two     |
|             |     panel   |     panel   |     panel   |     panel   |
|             |     groups  |     groups  |     groups  |     groups  |
|             |             |             |             |             |
|             | -   For     | -   For     | -   For     | -   For     |
|             |     each    |     each    |     each    |     each    |
|             |     panel   |     panel   |     panel   |     panel   |
|             |     group:  |     group:  |     group:  |     group:  |
|             |             |             |             |             |
|             |    (***M,N, |    (***M,N, |    (***M,N, |    (***M,N, |
|             | P,Mg,Ng***) | P,Mg,Ng***) | P,Mg,Ng***) | P,Mg,Ng***) |
|             |     =       |     =       |     =       |     =       |
|             |     (       |     (4      |     (       |     (1      |
|             | 8,8,2,1,1). | ,16,2,2,2). | 4,4,2,1,1). | 6,8,2,1,1). |
|             |             |             |             |             |
|             | -   Number  | -   Number  | -   Number  | -   Number  |
|             |     of      |     of      |     of      |     of      |
|             |     TxRUs:  |     TxRUs:  |     TxRUs:  |     TxRUs:  |
|             |     same as |     same as |     same as |     same as |
|             |     legacy  |     legacy  |     legacy  |     legacy  |
|             |     TDD     |     TDD     |     TDD     |     TDD     |
|             |             |             |             |             |
|             | -   $\left  | -   $\left  | -   $\left( | -   $\left( |
|             | ( d_{H},d_{ | ( d_{H},d_{ |  d_{H},d_{V |  d_{H},d_{V |
|             | V} \right)$ | V} \right)$ | } \right)$= | } \right)$= |
|             |     = (0.5, |     = (0.5, |     (0.5,   |     (0.5,   |
|             |     0.8)λ,  |     0.5)λ,  |     0.5)λ,  |     0.5)λ,  |
|             |             |             |             |             |
|             |   +45°/-45° |   +45°/-45° |   +45°/-45° |   +45°/-45° |
|             |     po      |     po      |     po      |     po      |
|             | larization, | larization, | larization, | larization, |
|             |     (d~a    |     (d~a    |     (d~a    |             |
|             | ,H~,d~a,V~) | ,H~,d~a,V~) | ,H~,d~a,V~) | (da,H,da,V) |
|             |     = (0,   |     = (0,   |     = (0,   |     = (0,   |
|             |     4)λ     |     30)λ    |     4)λ     |     30)λ    |
+-------------+-------------+-------------+-------------+-------------+
| **BS        | ***reuse    | ***reuse    |             |             |
| antenna     | Table 9 in  | Table 10 in |             |             |
| radiation   | Report      | Report      |             |             |
| pattern**   | ITU-R       | ITU-R       |             |             |
|             | M.2412      | M.2412      |             |             |
|             | (same as    | (Table      |             |             |
|             | 3-sector BS | A.2.1-7 in  |             |             |
|             | antenna     | TR          |             |             |
|             | radiation   | 38.802)***  |             |             |
|             | model in    |             |             |             |
|             | Table       |             |             |             |
|             | A.2.1-6 in  |             |             |             |
|             | TR          |             |             |             |
|             | 38.802)***  |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **UE        | -   ***2Tx: | ***4Tx/Rx:  | -   ***2Tx: | 4Tx/Rx:     |
| antenna     |             | (M,N,P,M    |             | (M,N,P,M    |
| conf        |    (M,N,P,M | g,Ng;Mp,Np) |    (M,N,P,M | g,Ng;Mp,Np) |
| iguration** | g,Ng;Mp,Np) | =           | g,Ng;Mp,Np) | =           |
|             |     =       | (2,4,       |     =       | (2,4,       |
|             |     (1,1,   | 2,1,2;1,1); |     (1,1,   | 2,1,2;1,1); |
|             | 2,1,1;1,1), | (dH,dV) =   | 2,1,1;1,1), | (dH,dV) =   |
|             |     (dH,dV) | (0.5,0.5)λ, |     (dH,dV) | (0.5,0.5)λ, |
|             |     = (N/A, | (dg,V,dg,H) |     = (N/A, | (dg,V,dg,H) |
|             |     N/A)λ,  | = (0, 0)λ,  |     N/A)λ,  | = (0, 0)λ,  |
|             |     0°,90°  | 0°/90°      |     0°,90°  | 0°/90°      |
|             |     pola    | po          |     pola    | po          |
|             | rization*** | larization; | rization*** | larization; |
|             |             | Θmg,ng=90°; |             | Θmg,ng=90°; |
|             | -   ***4Rx: | Ω0,1=Ω      | -   ***4Rx: | Ω0,         |
|             |             | 0,0+180°*** |             | 1=Ω0,0+180° |
|             |    (M,N,P,M |             |    (M,N,P,M |             |
|             | g,Ng;Mp,Np) |             | g,Ng;Mp,Np) |             |
|             |     =       |             |     =       |             |
|             |     (1,2,   |             |     (1,2,   |             |
|             | 2,1,1;1,2), |             | 2,1,1;1,2), |             |
|             |     (dH,dV) |             |     (dH,dV) |             |
|             |     = (0.5, |             |     = (0.5, |             |
|             |     N/A)λ,  |             |     N/A)λ,  |             |
|             |     0°,90°  |             |     0°,90°  |             |
|             |     pola    |             |     pola    |             |
|             | rization*** |             | rization*** |             |
+-------------+-------------+-------------+-------------+-------------+
| **UE        | Omni-       | reuse Table | Omni-       | reuse Table |
| antenna     | directional | 11 in       | directional | 11 in       |
| radiation   | with 0 dBi  | Report      | with 0 dBi  | Report      |
| pattern**   | element     | ITU-R       | element     | ITU-R       |
|             | gain        | M.2412      | gain        | M.2412      |
|             |             | (same as UE |             | (same as UE |
|             |             | antenna     |             | antenna     |
|             |             | radiation   |             | radiation   |
|             |             | pattern     |             | pattern     |
|             |             | model 1 in  |             | model 1 in  |
|             |             | Table       |             | Table       |
|             |             | A.2.1-8 in  |             | A.2.1-8 in  |
|             |             | TR 38.802)  |             | TR 38.802)  |
+-------------+-------------+-------------+-------------+-------------+
| **BS        | 5dB         | 7 dB        | 5dB         | 7 dB        |
| receiver    |             |             |             |             |
| noise       |             |             |             |             |
| figure**    |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **UE        | 9 dB        | 13 dB       | 9 dB        | 13 dB       |
| receiver    |             |             |             |             |
| noise       |             |             |             |             |
| figure**    |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **Open loop | ***P0= -80  | ***P0= -86  | P0= -60     |             |
| power       | dBm, alpha  | dBm, alpha  | dBm, alpha  |             |
| control     | = 0.8***    | = 0.9***    | = 0.6       |             |
| p           |             |             |             |             |
| arameters** |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **Handover  | 3 dB        | 3 dB        | 3 dB        | 3 dB        |
| margin      |             |             |             |             |
| (dB)**      |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **UE        | Based on    | Based on    | Based on    | Based on    |
| a           | RSRP from   | RSRP from   | RSRP from   | RSRP from   |
| ttachment** | port 0      | port 0.     | port 0      | port 0.     |
|             |             |             |             |             |
|             |             | -   Out of  |             | -   Out of  |
|             |             |     the two |             |     the two |
|             |             |     UE      |             |     UE      |
|             |             |     panels, |             |     panels, |
|             |             |     the UE  |             |     the UE  |
|             |             |     panel   |             |     panel   |
|             |             |     with    |             |     with    |
|             |             |     the     |             |     the     |
|             |             |     best    |             |     best    |
|             |             |     receive |             |     receive |
|             |             |     SNR is  |             |     SNR is  |
|             |             |     chosen. |             |     chosen. |
|             |             |     i.e. no |             |     i.e. no |
|             |             |             |             |             |
|             |             |   combining |             |   combining |
|             |             |     is done |             |     is done |
|             |             |     between |             |     between |
|             |             |     panels. |             |     panels. |
|             |             |             |             |             |
|             |             | ```{=html}  |             | -   Single  |
|             |             | <!-- -->    |             |     gNB     |
|             |             | ```         |             |     panel   |
|             |             | -   Single  |             |     is used |
|             |             |     gNB     |             |     for UE  |
|             |             |     panel   |             |             |
|             |             |     is used |             |  attachment |
|             |             |     for UE  |             |             |
|             |             |             |             |             |
|             |             |  attachment |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **Polarized | Model-1 in  |             |             |             |
| antenna     | clause      |             |             |             |
| model**     | 7.3.2 in TR |             |             |             |
|             | 38.901      |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| **Mechanic  | 90° in GCS  | 90° in GCS  | 180° in GCS | 180° in GCS |
| tilt**      | (pointing   | (pointing   | (pointing   | (pointing   |
|             | to          | to          | to the      | to the      |
|             | horizontal  | horizontal  | ground)     | ground)     |
|             | direction)  | direction)  |             |             |
+-------------+-------------+-------------+-------------+-------------+
| *           | (According  | (According  | 90° in LCS  | (According  |
| *Electronic | to Zenith   | to Zenith   |             | to Zenith   |
| tilt**      | angle in    | angle in    |             | angle in    |
|             | \"Beam set  | \"Beam set  |             | \"Beam set  |
|             | at TRxP\")  | at TRxP\")  |             | at TRxP\")  |
+-------------+-------------+-------------+-------------+-------------+
| **Beam set  | For         | For         | \-          | For         |
| at TRxP**   | direction   | direction   |             | direction   |
|             | of TRxP     | of TRxP     |             | of TRxP     |
| **(         | analog beam | analog beam |             | analog beam |
| Constraints | steering    | steering    |             | steering    |
| for the     | (in LCS):   | (in LCS):   |             | (in LCS):   |
| range of    |             |             |             |             |
| selective   | Azimuth     | Azimuth     |             | Azimuth     |
| analog      | angle φi =  | angle φi =  |             | angle φi =  |
| beams per   | 0           | {-5\*pi/16, |             | {-5\*pi/16, |
| TRxP)**     |             | -3\*pi/16,  |             | -3\*pi/16,  |
|             | Zenith      | -pi/16,     |             | -pi/16,     |
|             | angle θj =  | pi/16,      |             | pi/16,      |
|             | pi\*102/180 | 3\*pi/16,   |             | 3\*pi/16,   |
|             |             | 5\*pi/16}   |             | 5\*pi/16}   |
|             | NOTE:       |             |             |             |
|             | (azimuth,   | Zenith      |             | Zenith      |
|             | zenith)=(0, | angle θj =  |             | angle θj =  |
|             | pi/2) is    | {5\*pi/8,   |             | {pi/4,      |
|             | the         | 7\*pi/8}    |             | 3\*pi/4}    |
|             | direction   |             |             |             |
|             | pe          | NOTE:       |             | NOTE:       |
|             | rpendicular | (azimuth,   |             | (azimuth,   |
|             | to the      | zenith)=(0, |             | zenith)=(0, |
|             | array.      | pi/2) is    |             | pi/2) is    |
|             |             | the         |             | the         |
|             | Precoder    | direction   |             | direction   |
|             | for beam at | pe          |             | pe          |
|             | (φi, θj) is | rpendicular |             | rpendicular |
|             | given by    | to the      |             | to the      |
|             | equation 1  | array.      |             | array.      |
|             | in Appendix |             |             |             |
|             | 1 (2D DFT   | Precoder    |             | Precoder    |
|             | beam) in    | for beam at |             | for beam at |
|             | RP-180524   | (φi, θj) is |             | (φi, θj) is |
|             |             | given by    |             | given by    |
|             |             | equation 1  |             | equation 1  |
|             |             | in Appendix |             | in Appendix |
|             |             | 1 (2D DFT   |             | 1 (2D DFT   |
|             |             | beam) in    |             | beam) in    |
|             |             | RP-180524   |             | RP-180524   |
+-------------+-------------+-------------+-------------+-------------+
| **Beam set  | \-          | For         | \-          | For         |
| at UE**     |             | direction   |             | direction   |
|             |             | of UE       |             | of UE       |
| **(         |             | analog beam |             | analog beam |
| Constraints |             | steering    |             | steering    |
| for the     |             | (in LCS):   |             | (in LCS):   |
| range of    |             |             |             |             |
| selective   |             | Azimuth     |             | Azimuth     |
| analog      |             | angle φi =  |             | angle φi =  |
| beams for   |             | {-3\*pi/8,  |             | {-3\*pi/8,  |
| UE)**       |             | -pi/8,      |             | -pi/8,      |
|             |             | pi/8,       |             | pi/8,       |
|             |             | 3\*pi/8};   |             | 3\*pi/8};   |
|             |             |             |             |             |
|             |             | Zenith      |             | Zenith      |
|             |             | angle θj =  |             | angle θj =  |
|             |             | {pi/4,      |             | {pi/4,      |
|             |             | 3\*pi/4};   |             | 3\*pi/4};   |
|             |             |             |             |             |
|             |             | NOTE:       |             | NOTE:       |
|             |             | (azimuth,   |             | (azimuth,   |
|             |             | zenith)=(0, |             | zenith)=(0, |
|             |             | pi/2) is    |             | pi/2) is    |
|             |             | the         |             | the         |
|             |             | direction   |             | direction   |
|             |             | pe          |             | pe          |
|             |             | rpendicular |             | rpendicular |
|             |             | to the      |             | to the      |
|             |             | array.      |             | array.      |
|             |             |             |             |             |
|             |             | Precoder    |             | Precoder    |
|             |             | for beam at |             | for beam at |
|             |             | (φi, θj) is |             | (φi, θj) is |
|             |             | given by    |             | given by    |
|             |             | equation 1  |             | equation 1  |
|             |             | in Appendix |             | in Appendix |
|             |             | 1 (2D DFT   |             | 1 (2D DFT   |
|             |             | beam) in    |             | beam) in    |
|             |             | RP-180524   |             | RP-180524   |
+-------------+-------------+-------------+-------------+-------------+

C.3 SLS calibration results

The SLS calibration results can be found in R1-2304212.

######### Annex \<D\>: Link level evaluation for coverage performance

D.1 Link level simulation assumptions
=====================================

This clause describes the link level simulation assumptions for FR1 and
FR2-1. Table D.1-1 shows the general parameters for FR1. Table D.1-2
shows PUSCH specific parameters for FR1. Table D.1-3 shows the general
parameters for FR2-1. Table D.1-4 shows PUSCH specific parameters for
FR2-1.

Table D.1-1: General parameters for FR1

+----------------------------------+----------------------------------+
| **Parameter**                    | **Value**                        |
+==================================+==================================+
| **Scenario and frequency**       | Urban Macro: 4GHz                |
+----------------------------------+----------------------------------+
| **Frame structure for TDD**      | TDD: DDDSU (S: 12D:2G:0U)        |
|                                  |                                  |
|                                  | SBFD: XXXXU, where X denotes     |
|                                  | SBFD slot.                       |
|                                  |                                  |
|                                  | -   For SBFD slot, {DUD} pattern |
|                                  |     is assumed.                  |
|                                  |                                  |
|                                  | -   100MHz channel bandwidth and |
|                                  |     30kHz SCS (273 PRB): \<      |
|                                  |     N~D~, N~U~, N~G~ \> = \<104, |
|                                  |     55, 5\>                      |
+----------------------------------+----------------------------------+
| **Target data rates for eMBB**   | UL 1Mbps                         |
+----------------------------------+----------------------------------+
| **Pathloss model (select from    | gNB-UE: NLOS                     |
| LoS or NLoS)**                   |                                  |
|                                  | gNB-gNB (if modelled in LLS):    |
|                                  | LOS: NLOS = 3:1                  |
+----------------------------------+----------------------------------+
| **BWP**                          | 100MHz                           |
+----------------------------------+----------------------------------+
| **Channel model for link-level   | gNB-UE: TDL-C, CDL-C             |
| simulation**                     |                                  |
|                                  | Note: Company can provide        |
|                                  | simulation results based on      |
|                                  | either TDL channel or CDL model  |
|                                  |                                  |
|                                  | Note: Companies can report       |
|                                  | gNB-gNB channel model if         |
|                                  | modelled in LLS.                 |
+----------------------------------+----------------------------------+
| **Delay spread**                 | 300ns                            |
|                                  |                                  |
|                                  | Note: Other values can be        |
|                                  | reported by companies.           |
+----------------------------------+----------------------------------+
| **UE velocity**                  | 3km/h for indoor                 |
+----------------------------------+----------------------------------+
| **Number of antenna elements for | SBFD antenna configuration       |
| BS**                             | option-2,                        |
|                                  |                                  |
|                                  | -   192 antenna elements         |
|                                  |                                  |
|                                  | -   (M,N,P,Mg,Ng) = (12,8,2,1,1) |
|                                  |                                  |
|                                  | -   (optional) 128 antenna       |
|                                  |     elements                     |
|                                  |                                  |
|                                  | -   (M,N,P,Mg,Ng) = (8,8,2,1,1)  |
|                                  |                                  |
|                                  | -   Note: it is the same for     |
|                                  |     both SBFD and non-SBFD slots |
|                                  |                                  |
|                                  | Note: Companies to report the    |
|                                  | details if other antenna         |
|                                  | configurations are used.         |
+----------------------------------+----------------------------------+
| **Number of TxRUs for BS**       | gNB architectures to study:      |
|                                  |                                  |
|                                  | SBFD antenna configuration       |
|                                  | option-2,                        |
|                                  |                                  |
|                                  | -   64 TxRUs                     |
|                                  |                                  |
|                                  | -   Note: it is the same for     |
|                                  |     both SBFD and non-SBFD slots |
|                                  |                                  |
|                                  | Note: Companies to report the    |
|                                  | details if other antenna         |
|                                  | configurations are used.         |
|                                  |                                  |
|                                  | gNB modelling in LLS for TDL:    |
|                                  |                                  |
|                                  | \- Option 1: 2 or 4 gNB RF       |
|                                  | chains in LLS.                   |
|                                  |                                  |
|                                  | \- Option 2 (Optional): Number   |
|                                  | of gNB RF chains = number of     |
|                                  | TXRUs in LLS.                    |
|                                  |                                  |
|                                  | \- Companies can report if and   |
|                                  | how correlation is modelled.     |
+----------------------------------+----------------------------------+

Table D.1-2: Channel-specific parameters for PUSCH for FR1

+----------------------------------+----------------------------------+
| **Parameter**                    | **Value**                        |
+==================================+==================================+
| **Frequency hopping**            | w/ or w/o frequency hopping      |
+----------------------------------+----------------------------------+
| **BLER**                         | For eMBB, w/ HARQ, 10% iBLER;    |
|                                  | w/o HARQ, 10% iBLER.             |
+----------------------------------+----------------------------------+
| **Number of UE transmit chains** | 1, 2 (optional)                  |
+----------------------------------+----------------------------------+
| **DMRS configuration**           | For 3km/h: Type I, 1 or 2 DMRS   |
|                                  | symbol, no multiplexing with     |
|                                  | data.                            |
|                                  |                                  |
|                                  | For frequency hopping: Type I, 1 |
|                                  | or 2 DMRS symbol for each hop,   |
|                                  | no multiplexing with data.       |
|                                  |                                  |
|                                  | PUSCH mapping Type, the number   |
|                                  | of DMRS symbols and DMRS         |
|                                  | position(s) are reported by      |
|                                  | companies.                       |
+----------------------------------+----------------------------------+
| **Waveform**                     | DFT-s-OFDM                       |
+----------------------------------+----------------------------------+
| **SCS**                          | 30kHz                            |
+----------------------------------+----------------------------------+
| **PUSCH duration**               | 14 OS                            |
+----------------------------------+----------------------------------+
| **HARQ configuration**           | For eMBB, whether HARQ is        |
|                                  | adopted is reported by           |
|                                  | companies.                       |
|                                  |                                  |
|                                  | The maximum number of HARQ       |
|                                  | transmission (limited by frame   |
|                                  | structure and latency            |
|                                  | requirements) can be reported by |
|                                  | companies.                       |
+----------------------------------+----------------------------------+
| **PRBs/TBS/MCS for eMBB**        | Any value of PRBs, and           |
|                                  | corresponding MCS index,         |
|                                  | reported by companies will be    |
|                                  | considered in the discussion.    |
|                                  | Companies are encouraged to use  |
|                                  | 30 PRBs for 1Mbps for PUSCH for  |
|                                  | legacy TDD and SBFD with PUSCH   |
|                                  | repetition type A. Companies are |
|                                  | encouraged to use 6 PRBs for     |
|                                  | SBFD with TBoMS PUSCH over 5     |
|                                  | slots with or w/o joint channel  |
|                                  | estimation.                      |
|                                  |                                  |
|                                  | TBS can be calculated based on   |
|                                  | e.g. the number of PRBs, target  |
|                                  | data rate, frame structure and   |
|                                  | overhead.                        |
+----------------------------------+----------------------------------+

Table D.1-3: General parameters for FR2-1

+----------------------------------+----------------------------------+
| **Parameter**                    | **Value**                        |
+==================================+==================================+
| **Scenario and frequency**       | Dense Urban Macro: 30GHz         |
+----------------------------------+----------------------------------+
| **Frame structure for TDD**      | TDD: DDDSU (S: 12D:2G:0U)        |
|                                  |                                  |
|                                  | SBFD: XXXXU where X denotes SBFD |
|                                  | slot.                            |
|                                  |                                  |
|                                  | -   For SBFD slot, {DUD} pattern |
|                                  |     is assumed,                  |
|                                  |                                  |
|                                  | -   200MHz channel bandwidth and |
|                                  |     120kHz SCS (132 PRB): \< ND, |
|                                  |     NU, NG \> = \<52, 26, 1\>    |
+----------------------------------+----------------------------------+
| **Target data rates for eMBB**   | UL: 5Mbps                        |
+----------------------------------+----------------------------------+
| **BWP**                          | 200MHz                           |
+----------------------------------+----------------------------------+
| **Pathloss model (select from    | gNB-UE: NLOS                     |
| LoS or NLoS)**                   |                                  |
|                                  | gNB-gNB (if modelled in LLS):    |
|                                  | LOS: NLOS = 3:1                  |
+----------------------------------+----------------------------------+
| **Channel model for link-level   | gNB-UE: CDL- A, TDL-A            |
| simulation**                     |                                  |
|                                  | Note: Company can provide        |
|                                  | simulation results based on      |
|                                  | either TDL channel or CDL model  |
|                                  |                                  |
|                                  | Note: Companies can report       |
|                                  | gNB-gNB channel model if         |
|                                  | modelled in LLS.                 |
+----------------------------------+----------------------------------+
| **Delay spread**                 | 100ns                            |
|                                  |                                  |
|                                  | Note: Other values can be        |
|                                  | reported by companies.           |
+----------------------------------+----------------------------------+
| **UE velocity**                  | 30 km/h for outdoor              |
+----------------------------------+----------------------------------+
| **Number of antenna elements for | [SBFD antenna configuration      |
| BS**                             | option-2,]{.underline}           |
|                                  |                                  |
|                                  | -   256 antenna elements         |
|                                  |                                  |
|                                  | -   (M,N,P,Mg,Ng) = (16,8,2,1,1) |
|                                  |                                  |
|                                  | -   Note: it is the same for     |
|                                  |     both SBFD and non-SBFD slots |
+----------------------------------+----------------------------------+
| **Number of TxRUs for BS**       | 2                                |
|                                  |                                  |
|                                  | Note: Analog beamforming is      |
|                                  | assumed.                         |
+----------------------------------+----------------------------------+
| **Number of UE antenna           | 8, one panel:(M, N, P) = (2,2,2) |
| elements**                       |                                  |
+----------------------------------+----------------------------------+

Table D.1-4: Channel-specific parameters for PUSCH for FR2-1

+-------------------------------+-------------------------------------+
| **Parameter**                 | **Value**                           |
+===============================+=====================================+
| **Frequency hopping**         | w/ or w/o frequency hopping         |
+-------------------------------+-------------------------------------+
| **BLER**                      | For eMBB,                           |
|                               |                                     |
|                               | w/ HARQ, 10% iBLER, Optional:       |
|                               | companies report iBLER.             |
|                               |                                     |
|                               | w/o HARQ, 10% iBLER.                |
+-------------------------------+-------------------------------------+
| **Number of UE Tx/Rx chains** | 1T2R, 2T2R                          |
+-------------------------------+-------------------------------------+
| **DMRS configuration**        | For 30km/h: Type I, 2 or 3 DMRS     |
|                               | symbol, no multiplexing with data.  |
|                               |                                     |
|                               | For frequency hopping for PUSCH:    |
|                               | Type I, 1 or 2 DMRS symbol for each |
|                               | hop, no multiplexing with data.     |
|                               |                                     |
|                               | PUSCH/PDSCH mapping Type, the       |
|                               | number of DMRS symbols and DMRS     |
|                               | position(s) are reported by         |
|                               | companies.                          |
+-------------------------------+-------------------------------------+
| **Waveform**                  | DFT-s-OFDM                          |
+-------------------------------+-------------------------------------+
| **SCS**                       | 120kHz.                             |
+-------------------------------+-------------------------------------+
| **PUSCH duration**            | 14 OS                               |
+-------------------------------+-------------------------------------+
| **HARQ configuration**        | For eMBB, whether HARQ is adopted   |
|                               | is reported by companies.           |
|                               |                                     |
|                               | The maximum number of HARQ          |
|                               | transmission (limited by frame      |
|                               | structure and latency requirements) |
|                               | can be reported by companies.       |
+-------------------------------+-------------------------------------+
| **PRBs/TBS/MCS for eMBB**     | Any value of PRBs, and              |
|                               | corresponding MCS index, reported   |
|                               | by companies will be considered in  |
|                               | the discussion. Companies are       |
|                               | encouraged to use 25 PRBs for 5Mbps |
|                               | for PUSCH for legacy TDD and SBFD   |
|                               | with PUSCH repetition type A.       |
|                               | Companies are encouraged to use 5   |
|                               | PRBs for SBFD with TBoMS PUSCH over |
|                               | 5 slots with or w/o joint channel   |
|                               | estimation.                         |
|                               |                                     |
|                               | TBS can be calculated based on e.g. |
|                               | the number of PRBs, target data     |
|                               | rate, frame structure and overhead. |
+-------------------------------+-------------------------------------+

D.2 Link budget template
========================

For coverage performance evaluation for SBFD, the link budget template
in Table A.3 in TR 38.830 is reused ***with the following
modifications.***

+----------------------------------+----------------------------------+
| **(10) Number of receive antenna | SBFD antenna configuration       |
| elements**                       | option-2,                        |
|                                  |                                  |
|                                  | FR1:                             |
|                                  |                                  |
|                                  | -   192 antenna elements         |
|                                  |                                  |
|                                  | -   (M,N,P,Mg,Ng) = (12,8,2,1,1) |
|                                  |                                  |
|                                  | -   (optional) 128 antenna       |
|                                  |     elements                     |
|                                  |                                  |
|                                  | -   (M,N,P,Mg,Ng) = (8,8,2,1,1)  |
|                                  |                                  |
|                                  | FR2:                             |
|                                  |                                  |
|                                  | -   256 antenna elements         |
|                                  |                                  |
|                                  | -   (M,N,P,Mg,Ng) = (16,8,2,1,1) |
|                                  |                                  |
|                                  | Note: Companies to report the    |
|                                  | details if other antenna         |
|                                  | configurations are used.         |
+==================================+==================================+
| **(10a) Number of receive        | SBFD antenna configuration       |
| TxRUs**                          | option-2,                        |
|                                  |                                  |
|                                  | FR1:                             |
|                                  |                                  |
|                                  | -   64 TxRUs                     |
|                                  |                                  |
|                                  | FR2:                             |
|                                  |                                  |
|                                  | -   2 TxRUs                      |
|                                  |                                  |
|                                  | Note: Companies to report the    |
|                                  | details if other antenna         |
|                                  | configurations are used.         |
+----------------------------------+----------------------------------+

D.3 Link level evaluation results
=================================

The detailed evaluation results for the coverage performance gain of
semi-static SBFD compared to legacy TDD can be found in the attached
document \"**D.3\_Coverage Evaluation.zip**\".
