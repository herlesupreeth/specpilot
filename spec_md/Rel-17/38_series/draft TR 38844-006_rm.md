+----------------------------------+----------------------------------+
| 3GPP TR 38.844 V0.0.5 (2021-11)  |                                  |
+==================================+==================================+
| Technical Report                 |                                  |
+----------------------------------+----------------------------------+
| 3rd Generation Partnership       |                                  |
| Project;                         |                                  |
|                                  |                                  |
| Technical Specification Group    |                                  |
| Radio Access Network;            |                                  |
|                                  |                                  |
| NR;                              |                                  |
|                                  |                                  |
| Study on Efficient utilization   |                                  |
| of licensed spectrum that is not |                                  |
| aligned with existing NR channel |                                  |
| bandwidths                       |                                  |
|                                  |                                  |
| (Release 17)                     |                                  |
+----------------------------------+----------------------------------+
|                                  |                                  |
+----------------------------------+----------------------------------+
| ![](./media/image1.jp            | ![](./media/image2.p             |
| eg){width="1.3229166666666667in" | ng){width="1.7708333333333333in" |
| height="0.9166666666666666in"}   | height="1.0416666666666667in"}   |
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
| © 2021, 3GPP Organizational Partners (ARIB, ATIS, CCSA, ETSI, TSDSI, |
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

Foreword 5

Introduction 6

1 Scope 7

2 References 7

3 Definitions of terms, symbols and abbreviations 7

3.1 Terms 7

3.2 Symbols 7

3.3 Abbreviations 8

4 Examples for Styles 8

4.1 Heading Styles 8

4.2 Other common styles 8

\"TSG \<Name\>\" on the front page 9

Page setup parameters 9

Proforma copyright release text block 11

X.1 The right to copy 11

Abstract Test Suite (ATS) text block 12

Y Abstract Test Suite (ATS) 12

Y.1 Introduction 12

Y.2 The TTCN Graphical form (TTCN.GR) 12

Y.3 The TTCN Machine Processable form (TTCN.MP) 12

Annex \<A\> (normative): \<Normative annex for a Technical
Specification\> 13

Annex \<B\> (informative): \<Informative annex for a Technical
Specification\> 14

B.1 Heading levels in an annex 14

Annex \<B\>: \<Informative annex title for a Technical Report\> 15

Annex \<C\> (informative): Bibliography 16

Annex \<D\> (informative): Index 17

Annex \<X\> (informative): Change history 18

Foreword
========

This Technical Report has been produced by the 3rd Generation
Partnership Project (3GPP).

The contents of the present document are subject to continuing work
within the TSG and may change following formal TSG approval. Should the
TSG modify the contents of the present document, it will be re-released
by the TSG with an identifying change of release date and an increase in
version number as follows:

Version x.y.z

where:

x the first digit:

1 presented to TSG for information;

2 presented to TSG for approval;

3 or greater indicates TSG approved document under change control.

y the second digit is incremented for all changes of substance, i.e.
technical enhancements, corrections, updates, etc.

z the third digit is incremented when editorial only changes have been
incorporated in the document.

In the present document, modal verbs have the following meanings:

**shall** indicates a mandatory requirement to do something

**shall not** indicates an interdiction (prohibition) to do something

The constructions \"shall\" and \"shall not\" are confined to the
context of normative provisions, and do not appear in Technical Reports.

The constructions \"must\" and \"must not\" are not used as substitutes
for \"shall\" and \"shall not\". Their use is avoided insofar as
possible, and they are not used in a normative context except in a
direct citation from an external, referenced, non-3GPP document, or so
as to maintain continuity of style when extending or modifying the
provisions of such a referenced document.

**should** indicates a recommendation to do something

**should not** indicates a recommendation not to do something

**may** indicates permission to do something

**need not** indicates permission not to do something

The construction \"may not\" is ambiguous and is not used in normative
elements. The unambiguous constructions \"might not\" or \"shall not\"
are used instead, depending upon the meaning intended.

**can** indicates that something is possible

**cannot** indicates that something is impossible

The constructions \"can\" and \"cannot\" are not substitutes for \"may\"
and \"need not\".

**will** indicates that something is certain or expected to happen as a
result of action taken by an agency the behaviour of which is outside
the scope of the present document

**will not** indicates that something is certain or expected not to
happen as a result of action taken by an agency the behaviour of which
is outside the scope of the present document

**might** indicates a likelihood that something will happen as a result
of action taken by some agency the behaviour of which is outside the
scope of the present document

**might not** indicates a likelihood that something will not happen as a
result of action taken by some agency the behaviour of which is outside
the scope of the present document

In addition:

**is** (or any other verb in the indicative mood) indicates a statement
of fact

**is not** (or any other negative verb in the indicative mood) indicates
a statement of fact

The constructions \"is\" and \"is not\" do not indicate requirements.

Introduction
============

One of the aims of 5G is providing bandwidth flexibility. Although this
is achieved in general, but for some spectrum allocations the ability to
achieve such flexibility needs further study.

 1 Scope
=======

The present document is the Technical Report of the Study Item on
Efficient utilization of licensed spectrum that is not aligned with
existing NR channel bandwidths, approved at TSG RAN \#89-e \[2\]. The
purpose of this document is to capture and document the outcome of the
objectives stated in the SID.

2 References
============

The following documents contain provisions which, through reference in
this text, constitute provisions of the present document.

\- References are either specific (identified by date of publication,
edition number, version number, etc.) or non‑specific.

\- For a specific reference, subsequent revisions do not apply.

\- For a non-specific reference, the latest version applies. In the case
of a reference to a 3GPP document (including a GSM document), a
non-specific reference implicitly refers to the latest version of that
document *in the same Release as the present document*.

\[1\] 3GPP TR 21.905: \"Vocabulary for 3GPP Specifications\".

\[2\] RP-202103: SID "Study on Efficient utilization of licensed
spectrum that is not aligned with existing NR channel bandwidths"

3 Definitions of terms, symbols and abbreviations
=================================================

3.1 Terms
---------

For the purposes of the present document, the terms given in 3GPP
TR 21.905 \[1\] and the following apply. A term defined in the present
document takes precedence over the definition of the same term, if any,
in 3GPP TR 21.905 \[1\].

**Existing immediately lower regular channel bandwidth:** the closest NR
channel bandwidth defined in Rel-17 which is smaller/less than the
irregular bandwidth

**Existing immediately wider regular channel bandwidth:** the closest NR
channel bandwidth defined in Rel-17 which is larger/wider than the
irregular bandwidth

**Irregular bandwidth**: an NR bandwidth that is not defined in Rel-17

**Overlapping UE channel BW from network perspective:** network supports
the irregular bandwidth (either by a single carrier or by two
overlapping carriers) while each UE operates in an existing lower
regular NR channel bandwidth

**Overlapping UE channel BW from UE perspective:** network supports the
irregular bandwidth while some new UEs support two overlapping (RF)
carriers

**Overlapping CA:** the irregular bandwidth is handled by two
overlapping component carriers (CCs) with NR channel bandwidth defined
in Rel-17. It is network responsibility to prevent collisions between
the different component carriers.

**Single BB carrier:** means that from baseband (RAN1) perspective,
there is a single cell with a waveform according to a single carrier

3.2 Symbols
-----------

For the purposes of the present document, the following symbols apply:

\<symbol\> \<Explanation\>

3.3 Abbreviations
-----------------

For the purposes of the present document, the abbreviations given in
3GPP TR 21.905 \[1\] and the following apply. An abbreviation defined in
the present document takes precedence over the definition of the same
abbreviation, if any, in 3GPP TR 21.905 \[1\].

ACLR Adjacent Channel Leakage Ratio

ACS Adjacent Channel Selectivity

BS Base Station

BW Bandwidth

CBW Channel Bandwidth

SCBW Smaller Channel Bandwidth (Existing immediate lower channel
bandwidth)

FR1 Frequency Range 1

RF Radio Frequency

WCBW Wider Channel Bandwidth (Existing immediate wider channel
bandwidth)

UE User Equipment

4 Background
============

One of the aims of 5G is providing bandwidth flexibility. Although this
is achieved in general, but for some spectrum allocations the ability to
achieve such flexibility needs further study.

Solutions for the following spectrum allocations have been requested so
far:

Table 4-1: Summary of operators' input for irregular channel bandwidth

  Band (s)   Channel Bandwidth(s)
  ---------- ----------------------
  n5         7, 11 MHz
  n12, n85   6, 12 MHz
  n26        7 MHz
  n28        13 MHz
  n29        6, 11 MHz

Some techniques have been suggested for re-using existing channel
bandwidths which can include but not limited to overlapping UE channel
bandwidths, and/or using larger bandwidths than operator licensed
bandwidth. This Study Item is needed to evaluate where existing
techniques can be used to efficiently utilize operator spectrum
allocations, and whether and how new channel bandwidths should be
created. The Study shall also analyse if a proprietary solution(s) is
sufficient.

4.1 Objectives
--------------

The following objectives are listed in the SID \[2\]

1\) Identify operator licensed channel bandwidths in FR1 that do not
align with existing NR channel bandwidths.

\- Only licensed spectrum wider than 5 MHz to be considered in this SID.

\- Spectrum block of 33MHz in n28 require further investigation since
there is dual duplexer assumption (2x30MHz) for this band.

2\) Evaluate the potential use of larger channel bandwidths than
operator licensed bandwidth, including the impacts on regulatory
emission requirements/UE output power implications and UE ACS/blocking
impacts depending on the guard band and the SCS.

3\) Study the use of overlapping UE channel bandwidths (from both UE and
network perspective) to cover operator's license spectrum for both UL
and DL, and if new gNB channel bandwidths are needed.

NOTE: For all considered solutions, new (dedicated) channel filters
(e.g. non-integer-multiples of 5MHz) are not considered for the UE and
not prioritized for the gNB.

4\) Identify operator licensed bandwidths that are not compatible with
the use of techniques like overlapping UE channel bandwidths. Every
proposed method shall be summarized with respect to whether all
considered spectrum scenarios are supported or whether there are
specific limitations. Some limitations for a specific method shall not
disqualify such method if there is a trade-off between flexibility and
implementation challenges.

5\) Study the complexity and efficiency of adding new channel bandwidths
vs. using other including testing aspects.

6\) Generic solution(s) should be intended as much as possible, with
priority should be given to approaches that avoid the introduction of
new channel BWs on the UE side. Proprietary solutions if proven relevant
should not be precluded. Spectrally efficient methods providing a fine
channel bandwidth granularity as well as low to moderate guard band
width and signalling overhead should be preferred

7\) Impact on RAN1 and RAN2 should be considered and minimized

8\) For any considered solution, UEs not supporting such solution (both
legacy and new UEs) should be able to use the next lower supported
channel bandwidth in the UL and DL without implications.

9\) Impact (if any) on RAN4 requirements should be identified for the
preferred solutions.

5 General
=========

5.1 UE channel bandwidth
------------------------

The following text is copied from TS38.101-1 for information:

The UE channel bandwidth supports a single NR RF carrier in the uplink
or downlink at the UE. From a BS perspective, different UE channel
bandwidths may be supported within the same spectrum for transmitting to
and receiving from UEs connected to the BS. Transmission of multiple
carriers to the same UE (CA) or multiple carriers to different UEs
within the BS channel bandwidth can be supported.

From a UE perspective, the UE is configured with one or more BWP /
carriers, each with its own UE channel bandwidth. The UE does not need
to be aware of the BS channel bandwidth or how the BS allocates
bandwidth to different UEs.

The placement of the UE channel bandwidth for each UE carrier is
flexible but can only be completely within the BS channel bandwidth.

6 Result, Analysis outcome
==========================

6.1 Study of larger Channel BW than licensed BW
-----------------------------------------------

### 6.1.1 General Aspects

This clause describes, in general terms, how to utilize an irregular
Channel Bandwidth by deploying the "larger channel Bandwidth" method.

The premise idea is that the system is configured with the larger
channel bandwidth, as indicated in the broadcast System Information, ,
but the actual number of scheduled RBs is restricted so that it matches
actual spectrum allocation ensuring sufficiently large guard bands.

![](./media/image3.emf){width="1.4305555555555556in"
height="0.7777777777777778in"}

**Figure 6.1.1-1: Using the next larger channel bandwidth (example for
7MHz).**

NOTE: It should be checked further whether it is possible to configure
the next larger channel so that it goes over the band edge and which
implications it has.

One of the first aspects for this approach is the size of guard bands
and the anticipated number of schedulable RBs. For the standard channel
bandwidths, both values are captured in the corresponding specification
to avoid any misinterpretation on how many RBs can be configured and
scheduled. Following the same principle for every irregular channel
bandwidth would be feasible, but would create the same amount of
technical specification work as if the corresponding irregular channel
bandwidth were explicitly added to the specifications. Thus, the number
of \"available\" RBs can be calculated based on certain assumptions.

The maximum number of \"available\" or \"schedulable\" RBs for a
particular irregular channel bandwidth can be calculated based on the
assumption of using larger guard bands from the next *larger* channel
bandwidth. As an example, while considering the 7MHz channel bandwidth,
the assumption is to consider next larger 10MHz channel guard bands at
both ends, from which number of available RBs can be calculated.

NOTE: Since a UE will be configured with the channel bandwidth, which is
larger than the actual allocation, and it is not expected to provide the
usual stop-band attenuation at the edges of the irregular channel
bandwidth, it is necessary to verify the level of potential degradation
of ACS/blocking. Sub-clause 6.1.3 provides further information on UE
filters and potential performance.

NOTE: Similarly, the gNB operating with wider channel filters cannot be
expected to provide stop-band attenuation at the edges of the irregular
channel bandwidth to guarantee the co-existence. Further information on
gNB transmit channel filters and ACS/blocking should be provided to
assess resulting performance degradation and the gap to the RF
performance requirements. The gNB Tx transmitter filter assumption is
FFS.

Table 6.1.1-1 below presents example maximum number of available RBs for
different irregular channel bandwidths considered in this study item.

NOTE: Number of available RBs and spectral utilisation are taken from
R4-2112365. The gNB transmitter filter assumption used to derive the RB
numbers is FFS.

Table 6.1.1-1: Exemplary number of RBs based on the next larger channel
guard bands (15kHz SCS).

+----------+----------+----------+----------+----------+----------+
| Channel  | Next     | Next     | Next     | Channel  | Uti      |
| (MHz)    | larger   | larger   | larger   | Nrb      | lisation |
|          | channel  | channel  | channel  |          | (%)      |
|          | (MHz)    | guard    |          |          |          |
|          |          | band     | Nrb      |          |          |
|          |          | (kHz)    |          |          |          |
+==========+==========+==========+==========+==========+==========+
| 6        | 10       | 312,5    | 52       | 29       | 87       |
+----------+----------+----------+----------+----------+----------+
| 7        | 10       | 312,5    | 52       | 35       | 90       |
+----------+----------+----------+----------+----------+----------+
| 11       | 15       | 382,5    | 79       | 56       | 91,6     |
+----------+----------+----------+----------+----------+----------+
| 12       | 15       | 382,5    | 79       | 62       | 93       |
+----------+----------+----------+----------+----------+----------+
| 13       | 15       | 382,5    | 79       | 67       | 92,8     |
+----------+----------+----------+----------+----------+----------+

Table 6.1.1-2 below presents similar calculations for 30kHz SCS, from
which one can see that combination of 30kHz SCS and the next larger
channel is not generally a good approach for small channel bandwidths.
The main reason is that 30kHz SCS has much larger guard bands, which
immediately impacts number of available RBs. As a small summary,
assuming using guard band from the next larger channel the resulting
spectrum Utilization would range from 87 to 92.8% for an SCS of 15kHz
and 72 to 88.6% for an SCS of 30kHz.

NOTE: Number of available RBs and spectral utilisation are taken from
R4-2112365. The gNB transmitter filter assumption used to derive the RB
numbers is FFS.

Table 6.1.1-2: Exemplary number of RBs based on the next larger channel
guard bands (30kHz SCS).

  Channel (MHz)   Next larger channel (MHz)   Next larger channel guard band (kHz)   Next larger channel Nrb   Channel Nrb   Utilisation (%)
  --------------- --------------------------- -------------------------------------- ------------------------- ------------- -----------------
  6               10                          665                                    24                        12            72
  7               10                          665                                    24                        15            77,1
  11              15                          645                                    38                        26            85,1
  12              15                          645                                    38                        29            87
  13              15                          645                                    38                        32            88,6

### 

### 6.1.2 Signalling and configuration aspects

In this section we provide further signaling details on how to support
irregular channels given the 7MHz allocation as an example.

The gNB broadcasts the DL carrier bandwidth and the bandwidth of the
initial BWP (BWP\#0) in SIB1. For the 7MHz allocation, SIB1 can indicate
DL next larger standard channel bandwidth, i.e. 10 MHz, and that the
initial DL BWP can be set to 5 MHz:

\- SIB1-\> servingCellConfigCommon-\> downlinkConfigCommon-\>
frequencyInfoDL-\> scs-SpecificCarrierList-\> carrierBandwidth = 52 PRBs
/ subcarrierSpacing = 15 kHz

\- SIB1-\> servingCellConfigCommon-\> downlinkConfigCommon-\>
initialDownlinkBWP-\> genericParameters-\> locationAndBandwidth = 25
PRBs

Once the UE established the RRC connection, the gNB can account for the
UE capabilities and re-configure the UE accordingly. At this point the
gNB may override the carrier bandwidth value that the UE obtained from
SIB1 and configure a dedicated BWP with a bandwidth that differs from
the bandwidth of BWP\#0. gNB may configure a larger bandwidth part that
will cover the whole 7MHz allocation.

\- ServingCellConfig-\> downlinkChannelBW-PerSCS-List-\>
carrierBandwidth = 52 PRBs, subcarrierSpacing = 15 kHz

\- ServingCellConfig-\> downlinkBWP-ToAddModList-\> bwp-Common-\>
genericParameters-\> locationAndBandwidth = TBD PRBs

### 6.1.3 UE channel filters

A typical UE architecture utilises a number of filters of two major
types -- analogue and digital -- and it is generally up to the UE
implementation how they are combined. Nevertheless, it is often the case
that a UE uses first the wideband analogue filter which typically covers
a whole band. In addition to that, a UE may use another NR channel
bandwidth specific analogue filter, premise function on which is to
filter our non-adjacent blockers. However, since even the NR channel
bandwidth specific analogue filter cannot ensure \"brick-wall\" like
filtering, a UE also applies digital filter after ADC to eliminate
adjacent blockers. Depending on the UE implementation, the digital
filter is a combination of the hardware and software components that
allow the UE to apply the corresponding filter coefficients to support a
wide range of standard channels, e.g. from 5MHz to 100MHz in case of
FR1.

Sub-clause 6.1.2 provides the example in which the carrier bandwidth is
10MHz / 52 RBs, but the actual allocation is limited to the smaller
bandwidth through the corresponding signalling of the bandwidth part.
Current specifications do not define how a UE configures its digital
filter. So, in the provided example a UE implementation may configure
the digital filter in accordance with the carrier bandwidth \"ignoring\"
the actual bandwidth part size. This is illustrated further in Figure
6.1.3-1 below the wanted signal is smaller than 10MHz, but the UE filter
is always set to 10MHz as signalled by the network. As can be seen, if
there an adjacent blocker, then it can \"leak\" into the wanted signal
region.

![](./media/image4.emf){width="1.9430413385826772in"
height="0.8554844706911636in"}
![](./media/image5.emf){width="1.928571741032371in"
height="0.9922364391951006in"}
![](./media/image6.emf){width="1.6862095363079614in"
height="0.9635487751531059in"}

Figure 6.1.3-1: Possible scenarios for the 10MHz channel filter.

6.2 Study of overlapping UE channel bandwidths
----------------------------------------------

### 6.2.1 Overlapping UE CBW 

#### 6.2.1.1 General

One way to utilise the whole chunk of irregular spectrum of a particular
size is to combine several overlapping channels of next lower standard
channel bandwidth. As an example, Figure X-1 shows a case when two
overlapping 10MHz carriers cover 13MHz channel bandwidth. From an
individual UE perspective, each UE is configured with existing
immediately lower channel bandwidth following legacy procedures and
signalling: one UE can use the first 10MHz carrier, while another UE can
use another carrier. In fact, both UEs can use overlapping part of the
spectrum provided that the BS takes care that the overlapping region is
allocated to one particular carrier at a time. It should be also noted
that from the UE perspective, an existing immediately lower channel
bandwidth will be always used, either for initial access (as the channel
bandwidth advertised by the network) or as a dedicated channel bandwidth
configured by RRC. From the network perspective, the BS will/can use the
whole irregular channel bandwidth.

![](./media/image7.emf){width="1.5833333333333333in"
height="1.1979166666666667in"}

**Figure 6.2.1.1-1: Using overlapping carriers (example for 13MHz).**

It is worth noting that overall capacity of the cell will be according
to the irregular channel bandwidth because the BS can use the full
bandwidth. However, since a particular UE will use only one carrier of a
smaller bandwidth within the irregular channel bandwidth, the maximum
throughput for a single UE will be less than the theoretically possible
within the spectrum in case there is only a single UE in the cell.
Nevertheless, since there will be multiple UEs in the cell the overall
system throughput will not decrease.

#### 6.2.1.2 Detailed description

One of the challenges associated with configuring overlapping carriers
for the same frequency allocation is that both carriers should have
aligned grid so that the BS can perform same FFT and schedule resources
in the overlapping region.

While aligning RB grids is not an issue for bands above 3GHz that have
the SCS based raster, it becomes more challenging for the sub-3GHz band
that have 100kHz raster. As a result, carriers can be configured on
raster points that correspond to the least common multiple of the
channel raster and the RB size. As an example, the least common multiple
will be 900kHz in case of the 15kHz SCS, which corresponds to 5RBs. It
effectively means that overlapping carriers will not be able to address
efficiently any irregular spectrum size and in some case maybe will not
be applicable at all. Of course one way to improve spectrum utilisation
is to allow shifting carriers in multiples of 1RB, but that will require
introduction of new raster points, which will not be supported by legacy
UEs.

Figure 6.2.1.2-2 presents an example for the 6MHz channel comprising two
5MHz channels. As can be seen from the figure, centre frequency distance
between carriers is 900kHz, which is a multiple of 100kHz channel raster
and 180kHz RB size. From an individual UE perspective, it is just a
normal 5MHz carrier comprising 25RBs and having the 5MHz channel guard
bands. From the BS perspective, it is a 6MHz channel with 30RBs. Figure
6.2.1.2-3 exemplifies how this approach can be used to support the 7MHz
irregular channel bandwidth, in which the distance between the carriers
is 1800kHz. Finally, Figure 6.2.1.2-4 shows the 11MHz channel that is
supported with two 10MHz channels.Referring to Figure 6.2.1.2-2,
6.2.1.2-3 and 6.2.1.2-4, it should be noted that guard bands will not
necessarily be symmetrical and the exact guard band size will depend on
a particular spectrum allocation, its size, and how the overlapping
channels are placed.

![](./media/image9.emf){width="3.6666666666666665in" height="0.59375in"}

**Figure 6.2.1.2-2: Detailed overview of overlapping carriers (6MHz
channel with 5MHz carriers).**

![](./media/image10.emf){width="4.1875in" height="0.59375in"}

**Figure 6.2.1.2-3: Detailed overview of overlapping carriers (7MHz
channel with 5MHz carriers).**

![](./media/image11.emf){width="6.697916666666667in"
height="0.6145833333333334in"}**Figure 6.2.1.2-4: Detailed overview of
overlapping carriers (11MHz channel with 10MHz carriers).**

Table 6.2.1.2-1 below summarises potential number of schedulable RBs for
a scenario when the next smaller overlapping channels are used. To
calculate them, it is assumed that distance between individual carriers
is a multiple of 900kHz and that the resulting guard bands must meet at
least next smaller channel requirements. So, \"Channel Nrb\", and
\"Utilisation\" represent the network view, while from the UE
perspective all the parameters are the same as for the next smaller
channel.

**Table 6.2.1.2-1: Exemplary number of RBs based on the next smaller
overlapping channel (15kHz SCS).**

  **Channel (MHz)**   **Next smaller channel (MHz)**   **Next smaller channel guard band (kHz)**   **Next smaller channel Nrb**   **Channel Nrb**   **Utilisation (%)**
  ------------------- -------------------------------- ------------------------------------------- ------------------------------ ----------------- ---------------------
  6                   5                                242,5                                       25                             30                90
  7                   5                                242,5                                       25                             35                90
  11                  10                               312,5                                       52                             57                93,3
  12                  10                               312,5                                       52                             62                93
  13                  10                               312,5                                       52                             67                92,8

Table 6.2.1.2-2 presents similar calculations for the number of
available RBs with overlapping carriers, but for the 30kHz SCS. As can
be seen from the table, a solution based on the 30kHz SCS overlapping
carriers does not provide a good spectral utilisation for certain
non-standard channel bandwidths due to the reason that the \"distance\"
between carriers raster points must be a multiple of 1800kHz. Because of
that, channel bandwidths such as 7 and 12MHz have more or less good
utilisation, whereas 6 and 11MHz do not provide any benefit at all.

**Table 6.2.1.2-2: Exemplary number of RBs based on the next smaller
overlapping channel (30kHz SCS).**

  **Channel (MHz)**   **Next smaller channel (MHz)**   **Next smaller channel guard band (kHz)**   **Next smaller channel Nrb**   **Channel Nrb**   **Utilisation (%)**
  ------------------- -------------------------------- ------------------------------------------- ------------------------------ ----------------- ---------------------
  6                   5                                505                                         11                             11                66
  7                   5                                505                                         11                             16                82,3
  11                  10                               665                                         24                             24                78,5
  12                  10                               665                                         24                             29                87
  13                  10                               665                                         24                             29                80,3

To suppport two overlapping carriers, the network can consider using one
or two SSBs. To be more precise, since the the SSB bandwidth is 3.6MHz
and the CORESET\#0 bandwidth is 4.32MHz, a single SSB/CORESET\#0 can be
placed into a common part between two overlapping channels. However,
this approach works only if the overlapping part is at least 4.32MHz,
e.g. it is not applicable to 7MHz irregular channels. So, some irregular
channel bandwidth will needed two SSB/CORESET\#0. In this case, at least
for irregular channel bandwidths \<10MHz the network broadcasts two
separate SSBs, one for each overlapping regular carrier. In case of
irregular channels of a small size, e.g. less than 10MHz, it may create
the challenge of aligning SSBs in the time and frequency domain so that
they do not overlap thus complicating the gNB scheduling. i.e. for this
approach complexity increases to coordinate the overlapping SSB for
different UEs. As an example, if a particular irregular channel
bandwidth does not allow for placing two SSBs in the same time slots,
then the network will have two ensure that they are \"multiplexed\"
accordingly in the time domain.

**Table 6.2.1.2-3: Summary of how many SSB/CORESET\#0 needed for
different channel bandwidths.**

  **Channel (MHz)**   **Number of SSB/CORESET\#0**   **Time multiplexing for 2 SSBs is needed**
  ------------------- ------------------------------ --------------------------------------------
  6                   2                              yes
  7                   2                              yes
  11                  1 or 2                         no
  12                  1 or 2                         no
  13                  1 or 2                         no

Figure 6.2.1.2-5 shows an example for the 13MHz irregular channel with a
single/common SSB configured in the overlapping part of two 10MHz
carriers.

![Graphical user interface, text, application, email Description
automatically
generated](./media/image8.png){width="3.3958333333333335in"
height="1.28125in"}

**Figure 6.2.1.2-1: Using overlapping carriers with single overlapping
SSB (example for 13MHz).**

6.2.1.3 Configuration and signalling aspects

Since from an individual UE perspective each overlapping carrier is just
a legacy carrier, the existing signalling applies. As an example, for
the 7MHz allocation the UE can be configured with the 5MHz channel
bandwidth, and the initial bandwidth part can be also 5MHz.

\- SIB1-\> servingCellConfigCommon-\> downlinkConfigCommon-\>
frequencyInfoDL-\> scs-SpecificCarrierList-\> carrierBandwidth = 25 PRBs
/ subcarrierSpacing = 15 kHz

\- SIB1-\> servingCellConfigCommon-\> downlinkConfigCommon-\>
initialDownlinkBWP-\> genericParameters-\> locationAndBandwidth = 25
PRBs

*Editor's note: Signalling aspects to be updated once LS from RAN1/2 is
received. The text above is current RAN4 understanding.*

6.2.1.4 Compatiblity with legacy devices

Overlapping channels from the network perspective works with all the
legacy UEs. As presented in previous sub-clauses, from an individual UE
perspective, this is just a standard Rel-15 channel and no special UE
side enhancements are needed. Thus an operator can use this solution
with the whole ecosystem of available devices.

### 6.2.2 Combined UE CBW (one cell)

#### 6.2.2.1 General Aspects

\- Studied spectrum blocks covered by "main RF carrier" and "additional
RF carrier"

\- The "main RF carrier" is Rel-15 compatible and contains the SSB as
well as all necessary broadcast information, legacy UEs and UEs which do
not support this solution are able to camp on it and be connected
without being aware of the "additional RF carrier"

\- The "additional RF carrier" , which is partially overlapping with the
"main RF carrier", is aligned to the "main RF carrier" PRB grid and
utilizes further PRBs that fit in relevant spectrum block. UEs which
support this solution would be reconfigured (once UE capabilities are
known) in RRC\_CONNECTED to use wider BWP than used for initial access.

\- The "main RF carrier" and the "additional RF carrier" treated as
single cell (one carrier from baseband perspective) to allow for a
single BWP to cover studied spectrum block in RRC\_CONNECTED

\- Both the "main RF carrier" and the "additional RF carrier" would
clearly define the size and position of the guard band which allows for
an unambiguous placement of the overlapping channel filters and thus
prevents problems with OBUE, ACS or in-band blocking

\- From UE perspective, supported in downlink only

6.2.2.2 Signalling and configuration aspects

In this section we provide further signaling details on how to support
irregular channels given the 7MHz allocation as an example.

The gNB broadcasts the DL carrier bandwidth and the bandwidth of the
initial BWP (BWP\#0) in SIB1. For the 7MHz allocation, SIB1 would
indicate DL standard channel bandwidth (i.e. 5 MHz), the initial DL BWP
would be set to 5 MHz to accommodate legacy and new UEs:

> \- SIB1-\> servingCellConfigCommon-\> downlinkConfigCommon-\>
> frequencyInfoDL-\> scs-SpecificCarrierList-\> carrierBandwidth = 25
> PRBs / subcarrierSpacing = 15 kHz

\- SIB1-\> servingCellConfigCommon-\> downlinkConfigCommon-\>
initialDownlinkBWP-\> genericParameters-\> locationAndBandwidth = 25
PRBs

Once the UE established the RRC connection, the gNB can account for the
UE capabilities and re-configure the UE accordingly. At this point the
gNB may override the carrier bandwidth value that the UE obtained from
SIB1 and configure a dedicated BWP with a bandwidth that differs from
the bandwidth of BWP\#0. gNB may configure a larger bandwidth part that
will cover the whole 7MHz allocation.

\- ServingCellConfig-\> downlinkChannelBW-PerSCS-List-\>
carrierBandwidth = 36 PRBs, subcarrierSpacing = 15 kHz

\- ServingCellConfig-\> downlinkBWP-ToAddModList-\> bwp-Common-\>
genericParameters-\> locationAndBandwidth = 36 PRBs

It should be noted that 36 PRBs do not correspond to any channel
bandwidth currently defined in TS 38.101-1.

*Editor's note: Signalling aspects to be updated once LS from RAN1/2 is
received. The text above is current RAN4 understanding.*

6.2.2.3 UE architecture aspects

With respect to the UE architecture, the following assumptions are made
(according to SID objectives):

-   New (dedicated) channel filters (e.g. non-integer-multiples of 5
    MHz) are not considered

-   UEs not supporting this solution (both legacy and new UEs) should be
    able to use the next lower supported channel bandwidth in the UL and
    DL without implications

Two different UE architecture scenarios are explained (legacy UEs using
next smaller bandwidth in Clause 6.6.2 and UEs supporting two receive
chains for reception described below:

This option is for new UEs that contain transceiver architectures and
configurations that have flexibility in local oscillator and receive
chain assignments. The flexibility in the configuration allows the UEs
to configure their receive paths (Antenna to FFT) similarly to
non-contiguous carrier aggregation, allowing the two LO and receive
chains to down-convert the spectrum of the irregular bandwidth as if it
consisted of two separate carriers on the UE side. Based on the channel
center of the main RF carrier and the configured irregular bandwidth the
UE would know where to place the center frequency of the additional RF
carrier that follows the PRB grid (which overlaps with the main RF
carrier and includes the remaining agreed PRBs for the irregular BW).
The UE down-converts two different sets of PRBs, with an overlapping
segment and may use for irregular bandwidth below 15MHz the next smaller
bandwidth channel filtering on both of the receive chains as shown in
Figure 6.2.2.3-1 ("DigRF" serves as an example only and corresponds to
the interface between RF and baseband chipset). This allows the UE to
benefit from channel filtering designed for the specific bandwidth.
Using the next smaller bandwidth channel filtering on both of the two
carrier parts, the baseband signal processing following the FFTs must be
modified such that the signals from these two carrier parts are combined
and processed as a single codeword instead of being process separately.
Since the LOs on the UE will operate at different frequencies, there
will be a phase difference of the two signals contained in the two
receive chains for the separate carriers.

In order to prevent problems in the channel estimation if there is an
averaging or interpolation across reference signals at different
subcarriers, the phases of the symbols in the frequency domain from both
RF receive chains caused by the UE's use of separate LOs should be
aligned. This can be achieved by a new function comparing the
overlapping symbols from both FFT outputs and phase shifting one FFT
output accordingly before the FFT outputs are merged.

![](./media/image12.png){width="8.868055555555555in"
height="4.021829615048119in"}

**Figure 6.2.2.3-1**: UE architecture for full BW support showing split
by the use of two LOs

Depending on the receiver architecture and the distribution of the
channel filtering between the analogue and the digital domain, it is
also possible to A/D convert a frequency range that accommodates the
entire irregular BW and to split the signal afterwards by means of NCOs
(instead of LOs) into the 2 RF carriers with their individual channel
filter positions as shown in Figure 6.2.2.3-2.

![](./media/image13.png){width="8.395833333333334in"
height="3.823015091863517in"}

**Figure 6.2.2.3-2**: UE architecture for full BW support showing split
by the use of NCOs

### 6.2.3 Overlapping CA (two cells)

#### 6.2.3.1 General Aspects

Using the Overlapping CA approach to support irregular spectrum is one
of the methods without the need of introduction of new dedicated channel
bandwidths for both UE and BS. Figure 6.2.3-1 shows overlapping CA from
network perspective, in which BS supports the intra-band overlapping CA,
while UEs only supports the single CC with the existing channel
bandwidth. And figure 6.2.3-2 shows overlapping CA from UE perspective,
in which both BS and UE support the intra-band overlapping CA to use all
RBs.

Even two CCs are overlapped in frequency domain, the network can
configure different CCs with non-overlapping BWP to avoid the conflict
of physical signals or channels.

**Figure 6.2.3-1**: Overlapping CA from network perspective

Figure 6.2.3-2: Overlapping CA from UE perspective

In summary,

\- No new gNB channel bandwidth is required

\- Legacy UE using existing lower regular NR channel bandwidth can
operate in either carrier

\- Overlapping CA approach needs to have PRB grid alignment between
overlapping CCs

\- UE perspective, overlapping CA is optional supported in DL only

\- Irregular bandwidth utilizing overlapping CA approach cannot be
combined with NR CA combinations

6.3 Complexity and efficiency study
-----------------------------------

#### 6.3.1 Combined UE CBW (one cell)

\- Does not require new channel filters for UE and gNB to be designed
and tested

\- Requires support of two RF carriers phase aligned on the Tx side to
ensure phase continuity on the Rx side

> \- Requires split of the irregular bandwidth into two sets of PRBs
> that may be filtered through the next smaller bandwidth after which
> the signal is combined at baseband as a single carrier. For such
> processing, UE may benefit from supporting intra-band non-contiguous
> CA.
>
> \- Requires UE architecture with capability to split LNA output signal
> to two separate LO paths for down-conversion. Also requires UE
> architecture with the ability to combine baseband signals.

\- For scenarios with less than 10 MHz, second SSB is not excluded but
not recommended due to significant additional overhead (duplicated SSB
transmission as well as other radio resources such as PDCCH, CSI-RS,
PDSCH (for SIB), CSI for Tracking, etc.). However, second SSB could
enable or improve the legacy UEs\' use of the further PRBs provided by
the additional RF carrier in spectrum scenarios with less than 10 MHz.

\- "Additional RF carrier" not to be on the channel raster to increase
spectrum utilization (up to 2 PRBs), it should be noted that the
complete "additional RF carrier" is used only by UEs which support this
solution "additional RF carrier" can be used partially (with up to 2
PRBs not available) by legacy UEs which are on the channel raster.

\- Proposed BWPs size of the irregular spectrum chunk may have an impact
on performance requirements and additional testing

\- High spectrum utilization:

> \- due to low internal guard band. The spectrum utilization values in
> the table below use guard band values according to the minimum guard
> bands defined for the smallest possible channel bandwidths that could
> be theoretically considered as part of each combined UE CBW. The
> actual minimum guard band requirements for combined UE CBW
> configurations would require further discussion in any follow-up WI.

\- as well as no additional CA overhead (duplicated common channels and
signals such as SSB, PDCCH and CSI-RS configured both in Pcell and
Scell, in addition of the MAC processes associated with CA) due to
single baseband carrier usage:

**Table 6.3.1-1: spectrum utilization**

+-------------+-------------+-------------+-------------+-------------+
| **Spectrum  | **Number of | **Spectrum  | **Number of | **Spectrum  |
| block       | PRBs**      | utilization | PRBs**      | utilization |
| \[MHz\]**   |             | for new     |             | for new     |
|             | **(15kHz    | UE**        | **(15kHz    | UE**        |
|             | SCS without | **(without  | SCS with    | **(with     |
|             | 100kHz      | 100kHz      | 100kHz      | 100kHz      |
|             | raster      | raster      | raster      | raster      |
|             | a           | alignment)  | a           | alignment)  |
|             | lignment)** | \[%\]**     | lignment)** | \[%\]**     |
+=============+=============+=============+=============+=============+
| 6           | 30          | 90          | 30          | 90          |
+-------------+-------------+-------------+-------------+-------------+
| 7           | 36          | 92.6        | 35          | 90          |
+-------------+-------------+-------------+-------------+-------------+
| 11          | 58          | 94.9        | 57          | 93.3        |
+-------------+-------------+-------------+-------------+-------------+
| 12          | 63          | 94.5        | 62          | 93          |
+-------------+-------------+-------------+-------------+-------------+
| 13          | 69          | 95.5        | 67          | 92.8        |
+-------------+-------------+-------------+-------------+-------------+

#### 6.3.2 Overlapping CA (two cells)

From network perspective:

For gNB, no new filter for RF channel is needed. The CA implementation
can be reused. The only update is to allow the configuration that the
two carriers can be partially overlapped by adjusting the channel
spacing. The network can prevent collisions between the two component
carriers.

For UE, there is no impact and fully backwards compatible.

From UE perspective:

For gNB, the two RF carriers aggregated by the UE would need to be
time-aligned by the gNB to at least \[the same level required for
existing intra-band contiguous CA (TS 38.104 Timing Adjustment Error)\]
to allow UE reception. It is FFS as to whether finer timing alignment
would be required.

For UE, it is optional support in DL only. For the UE supports DL
intra-band non-contiguous CA with corresponding channel bandwidth(s),
overlapping CA can be considered by support the configuration with
partially overlapping carriers. And in the case no new channel filter
for UE is needed.

For overlapping CA solution, the legacy channel bandwidth should be
supported, hence the minimum guardband should not be less than the
minimum guardband of lower UE channel bandwidth than operator licensed
bandwidth. To support legacy UEs, channel raster should be applied for
each UE channels. And in order to simplify the resource schedule and
make the use of single SSB for CA operation, RB alignment is required.
Table 6.3.x-1 show the channel spacing and spectrum utilization for the
example channel bandwidths assuming symmetric CA channel bandwidth.

**Table 6.3.2-1: channel spacing and spectrum utilization**

  Irregular Bandwidth(MHz)   SCS(kHz)   CA combos   Nominal channel spacing (MHz)   Transmission bandwidth configuration NRB   Spectrum utilization (%)
  -------------------------- ---------- ----------- ------------------------------- ------------------------------------------ --------------------------
  6                          15         5+5         0.9                             30                                         90
  7                          15         5+5         1.8                             35                                         90
  11                         15         10+10       0.9                             57                                         93.3
  12                         15         10+10       1.8                             62                                         93
  13                         15         10+10       2.7                             67                                         92.8

6.4 Generic solutions guidance
------------------------------

NOTE: The 6^th^ objective is not an analysis/study but a guidance on
solutions. A comparison of the proposed solutions with respect to the
criteria in the 6^th^ objective should be included in this clause.

6.4.1 Overlapping UE CBW

This approach can be also be applied to all irregular channel bandwidths
with only consideration of different spectral utilization
considerations. However the single CORESET\#0 and SSB is only applicable
for bandwidths greater than 10 MHz. All irregular channel bandwidths two
SSBs can be used (irregular channel bandwidths \< 10 MHz SSB can be
TDM). .

#### 6.4.2 Combined UE CBW (one cell)

\- Generic and future proof solution, the channel bandwidth can be
tailored with the resolution of 1PRB

\- Ensured co-existence with very limited specification impact since
both the "main RF carrier" and the "additional RF carrier" would conform
to existing 3GPP requirements

\- Does not require new channel filters for UE and gNB to be designed
and tested

6.5 RAN1 and RAN2 impact
------------------------

6.5.1 Overlapping CA (two cells)

CSI-RS measurement and reporting for the component carriers are
specified in TS 38.213 and to be performed independently per-carrier,
similarly for PDCCH. It is up to the gNB scheduler to avoid collisions
of different transmissions for the overlapping part with overlapping CA
cross-carrier scheduling.

UE capability signalling does not provide any possibility for UE to
indicate support of overlapped CA. New signalling would be required in
order for this approach to become feasible.

*Editor's note: An indication of the time required to setup two CSI-RS
measurements would be added later*

6.6 Legacy UE impact
--------------------

NOTE: The 8^th^ objective is not an analysis/study but a guidance on
solutions

6.6.1 Overlapping UE CBW

This approach works with all the legacy UEs and thus an operator can use
this solution with the whole ecosystem of available devices.

#### 

#### 6.6.2 Combined UE CBW (one cell)

\- No impact to legacy UEs. UEs which support this solution would be
reconfigured in RRC\_CONNECTED, there is no change to UE behaviour in
IDLE mode which could create potential issue with legacy UE
compatibility

This option is for UEs that have no support for using an irregular
bandwidth. Such a UE will apply the next smaller bandwidth referring to
the channel filtering. It will never receive more than the PRBs defined
for the next smaller bandwidth and it follows the conventional way of
aligning the center frequency of the channel in both DL and UL. These
UEs will camp on the same frequency part of the channel since the SIB1
only has one allocation. In CONNECTED mode, the network can configure UE
with the UE specific *ServingCellConfig* IE which configures the point A
reference that may shift the UE to operate either at the lower side or
the upper side of the irregular bandwidth. In most of the configurations
with an irregular BW below 10 MHz, legacy UEs can only use one side of
the irregular BW unless -- as in the case of overlapping CBWs from
network perspective -- a second, time-staggered SSB is spent.

![](./media/image7.emf){width="1.5833333333333333in"
height="1.1979166666666667in"}

> **Figure 6.6.2-1**: Legacy UE may be configured for either of the two
> carriers

6.7 RAN4 standard impact identification
---------------------------------------

#### 6.7.1 Combined UE CBW (one cell)

\- Very limited since both the "main RF carrier" and the "additional RF
carrier" would conform to existing 3GPP requirements, to guarantee
co-existence

#### 6.7.2 Overlapping CA (two cells)

The CA framework defines the transmitter emission and receiver blocking
at the edge of carriers. Limited impacted is expected to enable
coexistence with neighbouring channels for this scenario. Overlapping CA
channel spacing need to be updated to consider channel raster, minimum
guard band and RB alignment.

For 15 KHz SCS and 100 KHz channel raster,

$$\text{Channel}\mspace{6mu}\text{spacing} = \left\lfloor \frac{2*BW_{Ch\text{annel}} - (BW_{Ch\text{annel}\left( 1 \right)} + BW_{Ch\text{annel}\left( 2 \right)})}{1.8} \right\rfloor 0.9\mspace{6mu}(\text{MHz)}$$

For NR *operating bands* with 15 kHz channel raster,

$$\text{Channel}\mspace{6mu}\text{spacing} = \left\lfloor \frac{2*BW_{Ch\text{annel}} - (BW_{Ch\text{annel}\left( 1 \right)} + BW_{Ch\text{annel}\left( 2 \right)})}{0.18*2^{n + 1}} \right\rfloor 0.18*2^{n}\mspace{6mu}(\text{MHz)}$$

with

$n = \mu_{0}$

#### 6.7.y Overlapping UE CBW

If the irregular channel bandwidths are explicitly defined in the
specification, it will create huge technical specification work. For
each channel bandwidth, the guard band size and the transmission
bandwidth configuration need to be specified and used as a basis for
defining transmitter and receiver requirements. The identified impact to
BS core specification for a new channel BW is shown in following Table
6.7.y-1.

Table 6.7.y-1 Analysis on the impact to BS core specification for a new
channel BW

  **Subject**   **Clause in 36.104/38.104**   **Requirement**                                              **Assessment for new channel BW**
  ------------- ----------------------------- ------------------------------------------------------------ ----------------------------------------------------------------------------------------------------------------------
  General       5.3.2                         Transmission bandwidth configuration                         the Transmission bandwidth configuration NRB for the new CBW need to be defined
                5.3.3                         Minimum guardband and transmission bandwidth configuration   The minimum guardband for the new CBW need to be defined
                5.3.5                         BS channel bandwidth per operating band                      new CBW need defined per band
  Transmitter   6.3.3                         Total power dynamic range                                    it is a NRB related requirement
                6.6.2                         Occupied bandwidth                                           BS channel bandwidth should be defined
                6.6.3                         ACLR                                                         The filter are set using transmission bandwidth configuration (BWConfig). It need to be defined for testing
                6.7                           Transmitter intermodulation                                  the interfering is defined according to BS channel bandwidth
  Receiver      7.2                           Reference sensitivity level                                  for 15 KHz SCS, 25 RB and 106 RB FRC which can be reused
                7.3                           Dynamic range                                                interfering signal level is according to BS channel bandwidth
                7.4                           In-band selectivity and blocking                             the position of interfering signal is defined according to BS channel bandwidth/transmission bandwidth configuration
                7.7                           Receiver intermodulation                                     the position of interfering signal is defined according to BS channel bandwidth/transmission bandwidth configuration
                7.8                           In-channel selectivity                                       it is defined according to BS channel bandwidth

It is concluded that new dedicated BS channel bandwidths for irregular
channel bandwidths are not defined explicitly in the specification.

7 Conclusion 
============

TBD

Page setup parameters
=====================

This clause defines the margin parameters and the header to be used
(implemented in the macros).

Title page (= title section)

A4 portrait, Top: 4 cm, Bottom: 19 cm, Left: 1,5 cm, Right: 1,5 cm,
Gutter: 0 cm, Header: 0 cm, Footer: 0 cm.

Portrait sections

A4 portrait, Top: 2.5 cm, Bottom: 2 cm, Left: 2 cm, Right: 2 cm, Gutter:
0 cm, Header: 1,5 cm, Footer: 0,6 cm.

Landscape sections

A4 landscape, Top: 2 cm, Bottom: 2 cm, Left: 2 cm, Right: 2,5 cm,
Gutter: 0 cm, Header: 1,5 cm, Footer: 0,6 cm.

Headers and footers

Header

The following contains the master location for all headers (except for
the title section). These paragraphs contain framed fields which will
result in one header line and are bookmarked \"header\".

The left-most entry contains a possible additional document reference,
e.g. \" Release 17\", identified on the title page by the use of the
ZGSM character style.

Release \| 17 \| 16 \| 15

The centre entry is the page number.

11

The right-most entry repeats the title page information, identified by
the use of the ZA paragraph style.

3GPP TS ab.cde Vx.y.z (yyyy-mm)

> NOTE: For documents which are split into more than one file, the
> possible additional document reference and the title page information
> need to be hardcoded in all files except the one containing the title
> section.
>
> NOTE: It has been found that opening very long documents with MS Word
> 2016 onwards (including versions of Word packaged in MS Office 365)
> can take a very long time, as can navigating around the document. This
> applies both in draft view and in print layout view. To solve this
> problem, the page header **[for each section]{.underline}** of the
> document may be hard-coded, replicating the text which would otherwise
> have been automated via the use of ZGSM and ZA styles.

Footer

The footer contains always \"3GPP\" (except for the title page).

3GPP

########  Annex \<A\> (normative): \<Normative annex for a Technical Specification\>

########  Annex \<B\> (informative): \<Informative annex for a Technical Specification\>

########   

######## Annex \<X\> (informative): Change history

This is the last annex for TS/TSs which details the change history using
the following table.\
This table is to be used for recording progress during the WG drafting
process till TSG approval of this TS/TR.\
For TRs under change control, use one line per approved Change Request\
Date: use format YYYY-MM\
CR: four digits, leading zeros as necessary\
Rev: blank, or number (max two digits)\
Cat: use one of the letters A, B, C, D, F\
Subject/Comment: for TSs under change control, include full text of the
subject field of the Change Request cover\
New vers: use format \[n\]n.\[n\]n.\[n\]n

+-------+-------+-------+-------+-------+-------+-------+-------+
| **C   |       |       |       |       |       |       |       |
| hange |       |       |       |       |       |       |       |
| hist  |       |       |       |       |       |       |       |
| ory** |       |       |       |       |       |       |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| **D   | *     | **T   | *     | **    | **    | **Su  | **New |
| ate** | *Meet | Doc** | *CR** | Rev** | Cat** | bject | vers  |
|       | ing** |       |       |       |       | /Comm | ion** |
|       |       |       |       |       |       | ent** |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | RAN   | R4-20 |       |       |       | TR    | 0.0.1 |
| 20-11 | 4\#97 | 15722 |       |       |       | Ske   |       |
|       |       |       |       |       |       | leton |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | RAN   | R4-20 |       |       |       | TR    | 0.0.1 |
| 20-11 | 4\#97 | 16930 |       |       |       | Ske   |       |
|       |       |       |       |       |       | leton |       |
|       |       |       |       |       |       | (rev  |       |
|       |       |       |       |       |       | ised) |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | RAN   | R4-21 |       |       |       | Up    | 0.0.2 |
| 21-01 | 4\#98 | 01555 |       |       |       | dated |       |
|       |       |       |       |       |       | TR    |       |
|       |       |       |       |       |       | 3     |       |
|       |       |       |       |       |       | 8.844 |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | RAN   | R4-21 |       |       |       | Up    | 0.0.2 |
| 21-01 | 4\#98 | 03262 |       |       |       | dated |       |
|       |       |       |       |       |       | TR    |       |
|       |       |       |       |       |       | 3     |       |
|       |       |       |       |       |       | 8.844 |       |
|       |       |       |       |       |       | (rev  |       |
|       |       |       |       |       |       | ised) |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | TP to | 0.0.2 |
| 21-04 | AN4\# | 06690 |       |       |       | the   |       |
|       | 98bis |       |       |       |       | TR    |       |
|       |       |       |       |       |       | 38    |       |
|       |       |       |       |       |       | .844: |       |
|       |       |       |       |       |       | T     |       |
|       |       |       |       |       |       | ermin |       |
|       |       |       |       |       |       | ology |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | TP to | 0.0.2 |
| 21-04 | AN4\# | 05420 |       |       |       | the   |       |
|       | 98bis |       |       |       |       | TR    |       |
|       |       |       |       |       |       | 38    |       |
|       |       |       |       |       |       | .844: |       |
|       |       |       |       |       |       | T     |       |
|       |       |       |       |       |       | ermin |       |
|       |       |       |       |       |       | ology |       |
|       |       |       |       |       |       | (rev  |       |
|       |       |       |       |       |       | ised) |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | RAN4\ | R4-21 |       |       |       | U     | 0.0.3 |
| 21-05 | #99-e | 10487 |       |       |       | pdate |       |
|       |       |       |       |       |       | TR    |       |
|       |       |       |       |       |       | 3     |       |
|       |       |       |       |       |       | 8.844 |       |
|       |       |       |       |       |       | with  |       |
|       |       |       |       |       |       | TP    |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | RAN4\ | R4-21 |       |       |       | TP on | 0.0.3 |
| 21-05 | #99-e | 08021 |       |       |       | the   |       |
|       |       |       |       |       |       | use   |       |
|       |       |       |       |       |       | of    |       |
|       |       |       |       |       |       | o     |       |
|       |       |       |       |       |       | verla |       |
|       |       |       |       |       |       | pping |       |
|       |       |       |       |       |       | ch    |       |
|       |       |       |       |       |       | annel |       |
|       |       |       |       |       |       | bandw |       |
|       |       |       |       |       |       | idths |       |
|       |       |       |       |       |       | from  |       |
|       |       |       |       |       |       | UE    |       |
|       |       |       |       |       |       | p     |       |
|       |       |       |       |       |       | erspe |       |
|       |       |       |       |       |       | ctive |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | RAN4\ | R4-21 |       |       |       | TP to | 0.0.3 |
| 21-05 | #99-e | 07885 |       |       |       | TR3   |       |
|       |       |       |       |       |       | 8.844 |       |
|       |       |       |       |       |       | on    |       |
|       |       |       |       |       |       | wider |       |
|       |       |       |       |       |       | ch    |       |
|       |       |       |       |       |       | annel |       |
|       |       |       |       |       |       | BW    |       |
|       |       |       |       |       |       | m     |       |
|       |       |       |       |       |       | ethod |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | RAN4\ | R4-21 |       |       |       | TP to | 0.0.3 |
| 21-05 | #99-e | 08022 |       |       |       | TR3   |       |
|       |       |       |       |       |       | 8.844 |       |
|       |       |       |       |       |       | on    |       |
|       |       |       |       |       |       | wider |       |
|       |       |       |       |       |       | ch    |       |
|       |       |       |       |       |       | annel |       |
|       |       |       |       |       |       | BW    |       |
|       |       |       |       |       |       | m     |       |
|       |       |       |       |       |       | ethod |       |
|       |       |       |       |       |       | (rev  |       |
|       |       |       |       |       |       | ised) |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | RAN4\ | R4-21 |       |       |       | TP on | 0.0.3 |
| 21-05 | #99-e | 09436 |       |       |       | using |       |
|       |       |       |       |       |       | o     |       |
|       |       |       |       |       |       | verla |       |
|       |       |       |       |       |       | pping |       |
|       |       |       |       |       |       | cha   |       |
|       |       |       |       |       |       | nnels |       |
|       |       |       |       |       |       | from  |       |
|       |       |       |       |       |       | the   |       |
|       |       |       |       |       |       | ne    |       |
|       |       |       |       |       |       | twork |       |
|       |       |       |       |       |       | p     |       |
|       |       |       |       |       |       | erspe |       |
|       |       |       |       |       |       | ctive |       |
|       |       |       |       |       |       | sol   |       |
|       |       |       |       |       |       | ution |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | RAN4\ | R4-21 |       |       |       | TP on | 0.0.3 |
| 21-05 | #99-e | 07887 |       |       |       | using |       |
|       |       |       |       |       |       | o     |       |
|       |       |       |       |       |       | verla |       |
|       |       |       |       |       |       | pping |       |
|       |       |       |       |       |       | cha   |       |
|       |       |       |       |       |       | nnels |       |
|       |       |       |       |       |       | from  |       |
|       |       |       |       |       |       | the   |       |
|       |       |       |       |       |       | ne    |       |
|       |       |       |       |       |       | twork |       |
|       |       |       |       |       |       | p     |       |
|       |       |       |       |       |       | erspe |       |
|       |       |       |       |       |       | ctive |       |
|       |       |       |       |       |       | sol   |       |
|       |       |       |       |       |       | ution |       |
|       |       |       |       |       |       | (rev  |       |
|       |       |       |       |       |       | ised) |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | RAN4\ | R4-21 |       |       |       | TP on | 0.0.3 |
| 21-05 | #99-e | 08112 |       |       |       | using |       |
|       |       |       |       |       |       | o     |       |
|       |       |       |       |       |       | verla |       |
|       |       |       |       |       |       | pping |       |
|       |       |       |       |       |       | cha   |       |
|       |       |       |       |       |       | nnels |       |
|       |       |       |       |       |       | from  |       |
|       |       |       |       |       |       | the   |       |
|       |       |       |       |       |       | ne    |       |
|       |       |       |       |       |       | twork |       |
|       |       |       |       |       |       | p     |       |
|       |       |       |       |       |       | erspe |       |
|       |       |       |       |       |       | ctive |       |
|       |       |       |       |       |       | sol   |       |
|       |       |       |       |       |       | ution |       |
|       |       |       |       |       |       | (rev  |       |
|       |       |       |       |       |       | ised) |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | Up    | 0.0.4 |
| 21-08 | AN4\# | 13948 |       |       |       | dated |       |
|       | 100-e |       |       |       |       | TR    |       |
|       |       |       |       |       |       | 3     |       |
|       |       |       |       |       |       | 8.844 |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | TP    | 0.0.4 |
| 21-08 | AN4\# | 14239 |       |       |       | for   |       |
|       | 100-e |       |       |       |       | TR    |       |
|       |       |       |       |       |       | 38    |       |
|       |       |       |       |       |       | .844: |       |
|       |       |       |       |       |       | 6 MHz |       |
|       |       |       |       |       |       | for   |       |
|       |       |       |       |       |       | n85   |       |
|       |       |       |       |       |       | with  |       |
|       |       |       |       |       |       | o     |       |
|       |       |       |       |       |       | verla |       |
|       |       |       |       |       |       | pping |       |
|       |       |       |       |       |       | CHBW  |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | TP on | 0.0.4 |
| 21-08 | AN4\# | 12365 |       |       |       | using |       |
|       | 100-e |       |       |       |       | next  |       |
|       |       |       |       |       |       | l     |       |
|       |       |       |       |       |       | arger |       |
|       |       |       |       |       |       | ch    |       |
|       |       |       |       |       |       | annel |       |
|       |       |       |       |       |       | band  |       |
|       |       |       |       |       |       | width |       |
|       |       |       |       |       |       | sol   |       |
|       |       |       |       |       |       | ution |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | TP on | 0.0.4 |
| 21-08 | AN4\# | 14999 |       |       |       | using |       |
|       | 100-e |       |       |       |       | next  |       |
|       |       |       |       |       |       | l     |       |
|       |       |       |       |       |       | arger |       |
|       |       |       |       |       |       | ch    |       |
|       |       |       |       |       |       | annel |       |
|       |       |       |       |       |       | band  |       |
|       |       |       |       |       |       | width |       |
|       |       |       |       |       |       | sol   |       |
|       |       |       |       |       |       | ution |       |
|       |       |       |       |       |       | (rev  |       |
|       |       |       |       |       |       | ised) |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | TP on | 0.0.4 |
| 21-08 | AN4\# | 15114 |       |       |       | using |       |
|       | 100-e |       |       |       |       | next  |       |
|       |       |       |       |       |       | l     |       |
|       |       |       |       |       |       | arger |       |
|       |       |       |       |       |       | ch    |       |
|       |       |       |       |       |       | annel |       |
|       |       |       |       |       |       | band  |       |
|       |       |       |       |       |       | width |       |
|       |       |       |       |       |       | sol   |       |
|       |       |       |       |       |       | ution |       |
|       |       |       |       |       |       | (rev  |       |
|       |       |       |       |       |       | ised) |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | TP on | 0.0.4 |
| 21-08 | AN4\# | 13046 |       |       |       | o     |       |
|       | 100-e |       |       |       |       | verla |       |
|       |       |       |       |       |       | pping |       |
|       |       |       |       |       |       | UE    |       |
|       |       |       |       |       |       | ch    |       |
|       |       |       |       |       |       | annel |       |
|       |       |       |       |       |       | bandw |       |
|       |       |       |       |       |       | idths |       |
|       |       |       |       |       |       | (O    |       |
|       |       |       |       |       |       | verla |       |
|       |       |       |       |       |       | pping |       |
|       |       |       |       |       |       | CA)   |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | TP on | 0.0.4 |
| 21-08 | AN4\# | 15000 |       |       |       | o     |       |
|       | 100-e |       |       |       |       | verla |       |
|       |       |       |       |       |       | pping |       |
|       |       |       |       |       |       | UE    |       |
|       |       |       |       |       |       | ch    |       |
|       |       |       |       |       |       | annel |       |
|       |       |       |       |       |       | bandw |       |
|       |       |       |       |       |       | idths |       |
|       |       |       |       |       |       | (O    |       |
|       |       |       |       |       |       | verla |       |
|       |       |       |       |       |       | pping |       |
|       |       |       |       |       |       | CA)   |       |
|       |       |       |       |       |       | (rev  |       |
|       |       |       |       |       |       | ised) |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | TP to | 0.0.4 |
| 21-08 | AN4\# | 13949 |       |       |       | TR    |       |
|       | 100-e |       |       |       |       | 38    |       |
|       |       |       |       |       |       | .844: |       |
|       |       |       |       |       |       | Se    |       |
|       |       |       |       |       |       | ction |       |
|       |       |       |       |       |       | 6.2   |       |
|       |       |       |       |       |       | O     |       |
|       |       |       |       |       |       | verla |       |
|       |       |       |       |       |       | pping |       |
|       |       |       |       |       |       | UE    |       |
|       |       |       |       |       |       | Ch    |       |
|       |       |       |       |       |       | annel |       |
|       |       |       |       |       |       | BWs   |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | TP to | 0.0.4 |
| 21-08 | AN4\# | 15050 |       |       |       | TR    |       |
|       | 100-e |       |       |       |       | 38    |       |
|       |       |       |       |       |       | .844: |       |
|       |       |       |       |       |       | Se    |       |
|       |       |       |       |       |       | ction |       |
|       |       |       |       |       |       | 6.2   |       |
|       |       |       |       |       |       | O     |       |
|       |       |       |       |       |       | verla |       |
|       |       |       |       |       |       | pping |       |
|       |       |       |       |       |       | UE    |       |
|       |       |       |       |       |       | Ch    |       |
|       |       |       |       |       |       | annel |       |
|       |       |       |       |       |       | BWs   |       |
|       |       |       |       |       |       | (rev  |       |
|       |       |       |       |       |       | ised) |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | Up    | 0.0.5 |
| 21-11 | AN4\# | 18777 |       |       |       | dated |       |
|       | 101-e |       |       |       |       | TR    |       |
|       |       |       |       |       |       | 3     |       |
|       |       |       |       |       |       | 8.844 |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | TP to | 0.0.5 |
| 21-11 | AN4\# | 20012 |       |       |       | TR    |       |
|       | 101-e |       |       |       |       | 3     |       |
|       |       |       |       |       |       | 8.844 |       |
|       |       |       |       |       |       | Se    |       |
|       |       |       |       |       |       | ction |       |
|       |       |       |       |       |       | 6.3.2 |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | TP    | 0.0.5 |
| 21-11 | AN4\# | 17954 |       |       |       | with  |       |
|       | 101-e |       |       |       |       | fu    |       |
|       |       |       |       |       |       | rther |       |
|       |       |       |       |       |       | i     |       |
|       |       |       |       |       |       | nform |       |
|       |       |       |       |       |       | ation |       |
|       |       |       |       |       |       | on UE |       |
|       |       |       |       |       |       | ch    |       |
|       |       |       |       |       |       | annel |       |
|       |       |       |       |       |       | f     |       |
|       |       |       |       |       |       | ilter |       |
|       |       |       |       |       |       | a     |       |
|       |       |       |       |       |       | ssump |       |
|       |       |       |       |       |       | tions |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | TP    | 0.0.5 |
| 21-11 | AN4\# | 20013 |       |       |       | with  |       |
|       | 101-e |       |       |       |       | fu    |       |
|       |       |       |       |       |       | rther |       |
|       |       |       |       |       |       | i     |       |
|       |       |       |       |       |       | nform |       |
|       |       |       |       |       |       | ation |       |
|       |       |       |       |       |       | on UE |       |
|       |       |       |       |       |       | ch    |       |
|       |       |       |       |       |       | annel |       |
|       |       |       |       |       |       | f     |       |
|       |       |       |       |       |       | ilter |       |
|       |       |       |       |       |       | a     |       |
|       |       |       |       |       |       | ssump |       |
|       |       |       |       |       |       | tions |       |
|       |       |       |       |       |       | (rev  |       |
|       |       |       |       |       |       | ised) |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | TP    | 0.0.5 |
| 21-11 | AN4\# | 17955 |       |       |       | with  |       |
|       | 101-e |       |       |       |       | c     |       |
|       |       |       |       |       |       | orrec |       |
|       |       |       |       |       |       | tions |       |
|       |       |       |       |       |       | for   |       |
|       |       |       |       |       |       | o     |       |
|       |       |       |       |       |       | verla |       |
|       |       |       |       |       |       | pping |       |
|       |       |       |       |       |       | cha   |       |
|       |       |       |       |       |       | nnels |       |
|       |       |       |       |       |       | from  |       |
|       |       |       |       |       |       | the   |       |
|       |       |       |       |       |       | ne    |       |
|       |       |       |       |       |       | twork |       |
|       |       |       |       |       |       | p     |       |
|       |       |       |       |       |       | erspe |       |
|       |       |       |       |       |       | ctive |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | TP    | 0.0.5 |
| 21-11 | AN4\# | 20015 |       |       |       | with  |       |
|       | 101-e |       |       |       |       | c     |       |
|       |       |       |       |       |       | orrec |       |
|       |       |       |       |       |       | tions |       |
|       |       |       |       |       |       | for   |       |
|       |       |       |       |       |       | o     |       |
|       |       |       |       |       |       | verla |       |
|       |       |       |       |       |       | pping |       |
|       |       |       |       |       |       | cha   |       |
|       |       |       |       |       |       | nnels |       |
|       |       |       |       |       |       | from  |       |
|       |       |       |       |       |       | the   |       |
|       |       |       |       |       |       | ne    |       |
|       |       |       |       |       |       | twork |       |
|       |       |       |       |       |       | p     |       |
|       |       |       |       |       |       | erspe |       |
|       |       |       |       |       |       | ctive |       |
|       |       |       |       |       |       |       |       |
|       |       |       |       |       |       | (rev  |       |
|       |       |       |       |       |       | ised) |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | TP to | 0.0.5 |
| 21-11 | AN4\# | 19230 |       |       |       | TR    |       |
|       | 101-e |       |       |       |       | 38    |       |
|       |       |       |       |       |       | .844: |       |
|       |       |       |       |       |       | on    |       |
|       |       |       |       |       |       | the   |       |
|       |       |       |       |       |       | use   |       |
|       |       |       |       |       |       | of    |       |
|       |       |       |       |       |       | o     |       |
|       |       |       |       |       |       | verla |       |
|       |       |       |       |       |       | pping |       |
|       |       |       |       |       |       | ch    |       |
|       |       |       |       |       |       | annel |       |
|       |       |       |       |       |       | bandw |       |
|       |       |       |       |       |       | idths |       |
|       |       |       |       |       |       | from  |       |
|       |       |       |       |       |       | UE    |       |
|       |       |       |       |       |       | p     |       |
|       |       |       |       |       |       | erspe |       |
|       |       |       |       |       |       | ctive |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | TP to | 0.0.5 |
| 21-11 | AN4\# | 20016 |       |       |       | TR    |       |
|       | 101-e |       |       |       |       | 38    |       |
|       |       |       |       |       |       | .844: |       |
|       |       |       |       |       |       | on    |       |
|       |       |       |       |       |       | the   |       |
|       |       |       |       |       |       | use   |       |
|       |       |       |       |       |       | of    |       |
|       |       |       |       |       |       | o     |       |
|       |       |       |       |       |       | verla |       |
|       |       |       |       |       |       | pping |       |
|       |       |       |       |       |       | ch    |       |
|       |       |       |       |       |       | annel |       |
|       |       |       |       |       |       | bandw |       |
|       |       |       |       |       |       | idths |       |
|       |       |       |       |       |       | from  |       |
|       |       |       |       |       |       | UE    |       |
|       |       |       |       |       |       | p     |       |
|       |       |       |       |       |       | erspe |       |
|       |       |       |       |       |       | ctive |       |
|       |       |       |       |       |       | (rev  |       |
|       |       |       |       |       |       | ised) |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | TP to | 0.0.5 |
| 21-11 | AN4\# | 18778 |       |       |       | TR    |       |
|       | 101-e |       |       |       |       | 38    |       |
|       |       |       |       |       |       | .844: |       |
|       |       |       |       |       |       | O     |       |
|       |       |       |       |       |       | verla |       |
|       |       |       |       |       |       | pping |       |
|       |       |       |       |       |       | CBW   |       |
|       |       |       |       |       |       | from  |       |
|       |       |       |       |       |       | UE    |       |
|       |       |       |       |       |       | p     |       |
|       |       |       |       |       |       | erspe |       |
|       |       |       |       |       |       | ctive |       |
|       |       |       |       |       |       | util  |       |
|       |       |       |       |       |       | izing |       |
|       |       |       |       |       |       | intra |       |
|       |       |       |       |       |       | -band |       |
|       |       |       |       |       |       | CA    |       |
|       |       |       |       |       |       | app   |       |
|       |       |       |       |       |       | roach |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
| 20    | R     | R4-21 |       |       |       | TP to | 0.0.5 |
| 21-11 | AN4\# | 20017 |       |       |       | TR    |       |
|       | 101-e |       |       |       |       | 38    |       |
|       |       |       |       |       |       | .844: |       |
|       |       |       |       |       |       | O     |       |
|       |       |       |       |       |       | verla |       |
|       |       |       |       |       |       | pping |       |
|       |       |       |       |       |       | CBW   |       |
|       |       |       |       |       |       | from  |       |
|       |       |       |       |       |       | UE    |       |
|       |       |       |       |       |       | p     |       |
|       |       |       |       |       |       | erspe |       |
|       |       |       |       |       |       | ctive |       |
|       |       |       |       |       |       | util  |       |
|       |       |       |       |       |       | izing |       |
|       |       |       |       |       |       | intra |       |
|       |       |       |       |       |       | -band |       |
|       |       |       |       |       |       | CA    |       |
|       |       |       |       |       |       | app   |       |
|       |       |       |       |       |       | roach |       |
|       |       |       |       |       |       | (rev  |       |
|       |       |       |       |       |       | ised) |       |
+-------+-------+-------+-------+-------+-------+-------+-------+
