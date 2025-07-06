######## Annex A (informative): Connection Diagrams

A.1 Definition of Terms
=======================

**System Simulator or SS** -- A device or system, that is capable of
generating simulated Node B signalling and analysing UE signalling
responses on one or more RF channels, in order to create the required
test environment for the UE under test. It will also include the
following capabilities:

1\. Measurement and control of the UE Tx output power through TPC
commands

2\. Measurement of Throughput

3\. Measurement of signalling timing and delays

4\. Ability to simulate UTRAN and/or E-UTRAN and/or GERAN signalling

**Test System** -- A combination of devices brought together into a
system for the purpose of making one or more measurements on a UE in
accordance with the test case requirements. A test system may include
one or more System Simulators if additional signalling is required for
the test case. The following diagrams are all examples of Test Systems.

NOTE 1: The above terms are logical definitions to be used to describe
the test methods used in the documents TS 38.521-1, TS 38.521-2, TS
38.521-3, TS 38.523-1 and TS 38.533 in practice, real devices called
\'System Simulators\' may also include additional measurement
capabilities or may only support those features required for the test
cases they are designed to perform.

NOTE 2: Components in the connection diagrams:\
The components in the connection diagrams represent ideal components.
They are intended to display the wanted signal flow. They don't mandate
real implementations.

**Connection:** Each connection is displayed as a one or two sided
arrow, showing the intended signal flow. In some cases, for some tests,
some connections shown may not be necessary (for example UL RX
connection for a second cell).

**Circulator:** The signal, entering one port, is conducted to the
adjacent port, indicated by the arrow. The attenuation among the above
mentioned ports is ideally 0 and the isolation among the other ports is
ideally ∞.

**Splitter:** a splitter has one input and 2 or more outputs. The signal
at the input is equally divided to the outputs. The attenuation from
input to the outputs is ideally 0 and the isolation between the outputs
is ideally ∞.

**Combiner:** a combiner has one output and 2 or more inputs. The
signals at the inputs are conducted to the output, all with the same,
ideally 0 attenuation. The isolation between the inputs is ideally ∞.

**Switch:** contacts a sink (or source) alternatively to two or more
sources (or sinks).

**Fader:** The fader has one input and one output. The MIMO fading
channel is represented by several single faders (e.g. 8 in case of a
MIMO antenna configuration 4x2) The correlation among the faders is
described in TS 36.521-1 clause B.2.2. In some cases, for some tests,
diagrams with fader(s) are referenced when no fading is required; in
this case the fader(s) is omitted.

Attenuator: TBD

**Test Equipment Part (TE):** is the section of the connection diagram
focused including a combination of devices to perform one or several
measurements on a UE depending on the test requirements specified in
3GPP TS 38.101-1 \[7\], 3GPP TS 38.101-2 \[8\] and 3GPP TS 38.101-3
\[9\]. The basic TE is the system simulator to enable the connection
between the gNB (and the eNB, if NSA mode) and the DUT. The number of
cells, the number of streams per cell and how to combine them, channel
and propagations conditions, etc. are also part of the TE. Other
instruments as external spectrum analyser, interferer generators,
external faders or external AWGN generators can be also considered part
of the TE, as these instruments allow to measure a test requirement or
to set the UE under certain conditions.

**DUT Part (UE)**: for conducted measurement this section is focused on
the number of physical antenna connectors and how to combine in the DUT.
For radiated measurement this section shows the connections needed to
translate the UL/DL streams to the radiated part.

**GNSS System Simulator or GSS:** A device or system, that is capable of
generating simulated GNSS satellite transmissions in order to create the
required test environment for the UE under test. It will also include
the following capabilities:

1\. Control of the output power of individual satellites and the
simulation of atmospheric delays.

2\. Ability to synchronize with NR timing in the SS.

A.2 General Considerations on Connections Diagram
=================================================

In order to improve the maintainability and the readability of this
section and to make easy to identify the whole connection diagram to use
per each test case, several considerations have been used for this
section:

\- The whole connection diagram to use for a specific test has been
split in Test Equipment (TE) and User Equipment (UE) parts.

\- The same connection diagram will be used for SA and NSA, where the
LTE link is specified in each connection diagram (TE and UE) with a
dashed line (and this part will be only used for NSA).

\- To obtain the whole connection diagram required per each test case is
necessary to specify the TE part required for each measurement and the
UE part will depend on the UE antenna implementation.

A.3 Setup Diagrams
==================

A.3.1 Test Equipment Parts for Conducted Measurements
-----------------------------------------------------

### A.3.1.1 Basic Transmitter/Receiver tests

Figure A.3.1.1.1: Test Equipment connection for basic single cell, RX
and TX tests

Figure A.3.1.1.2: Test Equipment connection for single cell, RX and TX
tests for NR UL MIMO or NR Tx diversity

Figure A.3.1.1.3: Test Equipment connection for NR CA and NR-DC, basic
RX and TX tests

Figure A.3.1.1.4: Test Equipment connection for NR SUL, basic RX and TX
tests

![Table Description automatically
generated](./media/image5.jpeg){width="6.6930555555555555in"
height="4.080555555555556in"}

Figure A.3.1.1.5: Test Equipment connection for UL MIMO on SUL band,
basic RX and TX tests

Figure A.3.1.1.6: Test Equipment connection for NR intra-band UL
contiguous CA with UL MIMO

Figure A.3.1.1.7: Test Equipment connection for NR inter-band UL CA with
UL MIMO or Tx Diversity

![A black background with a black square Description automatically
generated with medium
confidence](./media/image8.png){width="6.692361111111111in"
height="4.571735564304462in"}

Figure A.3.1.1.8: Test Equipment connection for SUL configuration with
inter-band UL CA

### A.3.1.2 Transmitter tests using Spectrum Analyser

Figure A.3.1.2.1: Test Equipment connection for TX-tests with additional
Spectrum Analyzer

Figure A.3.1.2.2: Test Equipment connection for TX-tests for UL MIMO
with additional Spectrum Analyser

Figure A.3.1.2.3: Test Equipment connection for NR CA TX-tests with
additional Spectrum Analyser

Figure A.3.1.2.4: Test Equipment connection for NR SUL TX-tests with
additional Spectrum Analyzer

### A.3.1.3 Transmitter tests using Spectrum Analyser and Signal Generator

Figure A.3.1.3.1: Test Equipment connection for Transmitter tests with
CW Interference and spectrum analyser

Figure A.3.1.3.2: Test Equipment connection for Transmitter tests for UL
MIMO with CW Interference and spectrum analyser

Figure A.3.1.3.3: Test Equipment connection for NR CA Transmitter tests
with CW Interference and spectrum analyser

Figure A.3.1.3.4: Test Equipment connection for Transmitter tests for
SUL with CW Interference and spectrum analyzer

### A.3.1.4 Receiver tests using Signal Generator

Figure A.3.1.4.1: Test Equipment connection for Receiver tests with
Modulated Interference

Figure A.3.1.4.2: Test Equipment connection for Receiver tests with CW
Interference

Figure A.3.1.4.3: Test Equipment connection for Receiver tests both
Modulated and additional CW Interference signal

Figure A.3.1.4.4: Test Equipment connection for Receiver tests for UL
MIMO with Modulated Interference

Figure A.3.1.4.5: Test Equipment connection for Receiver tests for UL
MIMO with CW Interference

Figure A.3.1.4.6: Test Equipment connection for Receiver tests for UL
MIMO with both Modulated and additional CW Interference signal

Figure A.3.1.4.7: Test Equipment connection for NR CA Receiver tests
with additional Modulated Interference signal and/or CW Interference
signal

Figure A.3.1.4.8: Test Equipment connection for NR SUL Receiver tests
with Modulated Interference

Figure A.3.1.4.9: Test Equipment connection for NR SUL Receiver tests
with CW Interference

Figure A.3.1.4.10: Test Equipment connection for NR SUL with DL CA
Receiver tests with additional Modulated Interference and/or CW
Interference signal

### A.3.1.5 Receiver tests using Spectrum Analyser

Figure A.3.1.5.1: Test Equipment connection for RX-tests with additional
Spectrum Analyzer

Figure A.3.1.5.2: Test Equipment connection for NR CA RX-tests with
additional Spectrum Analyzer

### A.3.1.6 Receiver Performance tests

Figure A.3.1.6.1: Test Equipment connection for Receiver Performance
tests with antenna configuration 1x2

### A.3.1.7 Demodulation Performance and CSI reporting tests

Figure A.3.1.7.0: Test Equipment connection for Demodulation Performance
and CSI reporting tests with antenna configuration 2x1

Figure A.3.1.7.1: Test Equipment connection for Demodulation Performance
and CSI reporting tests with antenna configuration 2x2

Figure A.3.1.7.2: Test Equipment connection for Demodulation Performance
and CSI reporting tests with antenna configuration 1x2

Figure A.3.1.7.2A: Test Equipment connection for Demodulation
Performance and CSI reporting tests with antenna configuration 1x2 for
nDLCA

Figure A.3.1.7.3: Test Equipment connection for Demodulation Performance
and CSI reporting tests with antenna configuration 1x4

Note: LTE can be 2Rx or 4Rx and not dependent on NR \#Rx

Figure A.3.1.7.4: Test Equipment connection for Demodulation Performance
and CSI reporting tests with antenna configuration 2x4

Note 1: LTE can be 2Rx or 4Rx and not dependent on NR \#Rx

Note 2: NR may be 2Rx on some of the CCs, in that case TE NR TX3 and TE
NR TRX4 are not used

Figure A.3.1.7.5: Test Equipment connection for Demodulation Performance
and CSI reporting tests with antenna configuration 4x4

Note 1: LTE can be 2Rx or 4Rx and not dependent on NR \#Rx

Note: 2 NR may be 2Rx on some of the CCs, in that case TE NR TX3 and TE
NR TX4 are not used

Figure A.3.1.7.6: Test Equipment connection for Demodulation Performance
and CSI reporting tests with antenna configuration 2x4 for nDL CA and
multi-cell

Note 1: LTE can be 2Rx or 4Rx and not dependent on NR \#Rx

Note 2: NR may be 2Rx on some of the CCs, in that case TE NR TX3 and TE
NR TX4 are not used

Note 3: NR may be 1Tx on some of the cells, in that case TE NR TX2, TE
NR TX3 and TE NR TX4 are not used

Figure A.3.1.7.7: Test Equipment connection for Demodulation Performance
and CSI reporting tests with antenna configuration 4x4 for nDL CA

Note 1: LTE can be 2Rx or 4Rx and not dependent on NR \#Rx

Note 2: NR may be 2Rx on some of the CCs, in that case TE NR TX3 and TE
NR TX4 are not used

Figure A.3.1.7.8: Test Equipment connection for Demodulation Performance
and CSI reporting tests with antenna configuration 4x2

Note: LTE can be 2Rx or 4Rx and not dependent on NR \#Rx

Figure A.3.1.7.9: Test Equipment connection for Demodulation Performance
and CSI reporting tests with 2 carriers or 2 TRPs (2x2 or 2x4)

Note 1: LTE can be 2Rx or 4Rx and not dependent on NR \#Rx

Note 2: NR may be 2Rx on some of the CCs, in that case TE NR TX3 and TE
NR TX4 are not used

Figure A.3.1.7.10: Test Equipment connection for Demodulation
Performance and CSI reporting tests with antenna configuration Nx2 and
Nx4, N=16 or N=32

Note 1: LTE can be 2Rx or 4Rx and not dependent on NR \#Rx

Note 2: NR may be 2Rx on some of the CCs, in that case TE NR TX3 and TE
NR TX4 are not used

Figure A.3.1.7.11: Test Equipment connection for Demodulation
Performance and CSI reporting tests with antenna configuration 4x1

### A.3.1.8 RRM tests with more than one NR cell

The figures in this section represent connection diagrams for test cases
with more than one NR cell. The parameters in the connection diagram,
e.g. the number of cells *n* or the value of the phase rotator φ~i~
shall be defined by the test cases.

Figure A.3.1.8.1: Test Equipment connection for tests with more than one
NR cell and antenna configuration 1x1

Figure A.3.1.8.2: Test Equipment connection for tests with more than one
NR cell and antenna configuration 1x2

Figure A.3.1.8.2a: Test Equipment connection for tests with more than
one NR cell and antenna configuration 2x2

Figure A.3.1.8.3: Test Equipment connection for tests with more than one
NR cell and antenna configuration 1x2 and fading

Figure A.3.1.8.4: Test Equipment connection for tests with more than one
NR cell for 4Rx capable UEs with fading

Figure A.3.1.8.5: Test Equipment connection for tests with more than one
NR cell and antenna configuration 1x4

### A.3.1.9 Test Equipment supporting NR Sidelink

Figure A.3.1.9.1: Test Equipment connection for NR sidelink operation
non-concurrent with NR UL/DL transmission

Figure A.3.1.9.1a: Test Equipment connection for NR sidelink operation
non-concurrent Receiver tests with one Interference signal (Modulated or
CW)

Figure A.3.1.9.1b: Test Equipment connection for NR sidelink operation
non-concurrent Receiver tests with both Modulated and CW Interference
signals

Figure A.3.1.9.2: Test Equipment connection for NR sidelink operation
non-concurrent with NR UL/DL transmission SL-MIMO

Figure A.3.1.9.3: Test Equipment connection for inter-band con-current
NR V2X operation

Figure A.3.1.9.4: Test Equipment connection for con-current E-UTRA Uu
and NR Sidelink operation

Figure A.3.1.9.5: Test Equipment connection for con-current E-UTRA V2X
sidelink and NR Uu operation

A.3.2 User Equipment Parts for Conducted Measurements
-----------------------------------------------------

### A.3.2.1 General

The User Equipment part is focused on the number of physical antenna
connectors and how to combine in the DUT. Depending on the DUT
implementation only one of the following connection diagrams applies.
These connection diagrams are examples of User equipment parts.

### A.3.2.2 One Antenna Connector

Figure A.3.2.2.1: User Equipment connection for single basic cell

### A.3.2.3 Two Antenna Connectors

Figure A.3.2.3.1: User Equipment connection for single basic cell with
NR and LTE cells at different separated connectors

Figure A.3.2.3.2: User Equipment connection for single basic cell with
NR and LTE cells at the same connectors for both cells

Figure A.3.2.3.3: 2 Tx User Equipment connection for single basic cell
with NR and LTE cells at the same connectors for both cells and 2TX UL
MIMO or Tx diversity supported

Figure A.3.2.3.4: User Equipment connection for UEs with NR and LTE RxTx
and Rx antenna at same connectors

Figure A.3.2.3.5: User Equipment connection for single basic cell with
NR and LTE cells at different separated connectors with NR SUL and NR
NUL transmitted on separate antenna connectors

Figure A.3.2.3.6: User Equipment connection for single basic cell with
NR and LTE cells at different separated connectors with NR SUL and NR
NUL transmitted on the same antenna connector

Figure A.3.2.3.7: User Equipment connection for single basic cell with
NR and LTE cells at the same connectors for both cells with NR SUL and
NR NUL transmitted on separate antenna connectors

Figure A.3.2.3.8: User Equipment connection for single basic cell with
NR and LTE cells at the same connectors for both cells with NR SUL and
NR NUL transmitted on the same antenna connector

![Text Description automatically generated with low
confidence](./media/image64.png){width="6.6875in"
height="4.510416666666667in"}

Figure A.3.2.3.9: User Equipment connection for single basic cell with
NR and LTE cells at different separated connectors with UE supporting UL
MIMO on SUL band

![A picture containing text Description automatically
generated](./media/image65.png){width="6.59375in"
height="4.729166666666667in"}

Figure A.3.2.3.10: User Equipment connection for single basic cell with
NR and LTE cells at the same connectors for both cells with UE
supporting UL MIMO on SUL band

r

Figure A.3.2.3.11: 2 Tx User Equipment connection for NR intra-band UL
contiguous CA at the same connectors for both cells and 2TX UL MIMO
supported

### A.3.2.4 Three Antenna Connectors

Figure A.3.2.4.1: 2Tx User Equipment connection for single basic cell
with NR and LTE cells at different separated connectors and 2TX UL MIMO
supported

Figure A.3.2.4.2: 3Tx User Equipment connection for NR inter-band UL CA
at different separated connectors for both cells and 2TX UL MIMO or Tx
Diversity supported for PCell

### A.3.2.5 Four Antenna Connectors

Figure A.3.2.5.1: User Equipment connection for UEs with NR and LTE RxTx
and Rx antenna at different separated connectors

Figure A.3.2.5.2: User Equipment connection for 4Rx capable UEs without
any 2Rx RF bands (NR and LTE at same connectors)

Figure A.3.2.5.3: User Equipment connection for UEs with NR CA
(component carriers on common connector) and LTE

Figure A.3.2.5.4: User Equipment connection for UEs with NR SUL and DL
CA (component carriers on common connector) and LTE

![A black background with a black square Description automatically
generated with medium confidence](./media/image73.png){width="6.69375in"
height="3.889093394575678in"}

Figure A.3.2.5.5: User Equipment connection for SUL configuration with
inter-band UL CA

### A.3.2.6 Over Four Antenna Connectors

Figure A.3.2.6.1: User Equipment connection for UEs with NR CA
(component carriers on separated connectors) and LTE

Figure A.3.2.6.2: User Equipment connection for UEs with NR CA and NR
4Rx (component carriers on separated connectors) and LTE

Note: NR may be 2Rx on some of the CCs, in that case RX3 and RX4 are not
used

![A diagram of a computer system Description automatically
generated](./media/image76.png){width="6.69375in"
height="4.690277777777778in"}

Figure A.3.2.6.3: User Equipment connection for 8Rx capable UEs without
any 2Rx and 4Rx RF bands (NR and LTE at separate connectors)

![](./media/image77.png){width="6.69375in" height="7.490277777777778in"}

Figure A.3.2.6.4: User Equipment connection for UEs with NR CA and NR
8Rx (component carriers on separated connectors) and LTE

Note: NR may be 4Rx on some of the CCs, in that case RX5 to RX8 are not
used. And NR may be 2Rx on some of the CCs, in that case RX3 to RX8 are
not used.

### A.3.2.7 User Equipment supporting NR Sidelink

Figure A.3.2.7.1: User Equipment connection for NR sidelink operation
non-concurrent with NR UL/DL transmission

Figure A.3.2.7.2: User Equipment connection for NR sidelink operation
non-concurrent with NR UL/DL transmission with SL-MIMO

Figure A.3.2.7.3: User Equipment connection for inter-band con-current
NR V2X operation

Figure A.3.2.7.4: User Equipment connection for con-current E-UTRA Uu
and NR Sidelink operation

Figure A.3.2.7.5: User Equipment connection for con-current E-UTRA V2X
sidelink and NR Uu operation

A.3.3 Test Equipment Parts for Radiated Measurements
----------------------------------------------------

### A.3.3.1 Transmitter/Receiver tests

The Test Equipment part is focused on logical representation of TE
measurement and link antenna(s) and positioner controller. The Test
Equipment connection diagram below is applicable for NR radiated RX and
TX tests, including CA and UL MIMO tests.

Figure A.3.3.1.1: Basic TE diagram for radiated RX and TX tests

For NR radiated RX tests requiring to simulate a modulated interference,
connection diagram defined in figure A.3.3.1.2 will apply.

Figure A.3.3.1.2: TE diagram for radiated RX tests with Modulated
Interference

For NR radiated spurious emission test cases, connection diagram defined
in figure A.3.3.1.3 will apply.

Figure A.3.3.1.3: TE diagram for spurious emission tests

### A.3.3.2 Demodulation and CSI tests

Figure A.3.3.2.1: Demodulation and CSI tests

Figures A.3.3.2.1-1 and A.3.3.2.1-1 show the connection diagram inside
SS NR of Figure A.3.3.2.1 for downlink signal path.

Figure A.3.3.2.1-1: TE diagram for Demodulation and CSI tests (1x2)

Figure A.3.3.2.1-2: TE diagram for Demodulation and CSI tests (2x2)

### A.3.3.3 RRM tests

The Test Equipment part is focused on logical representation of TE
antenna(s) and positioner. The Test Equipment connection diagram below
is applicable for NR radiated RRM tests. SS NR uses several antennas to
cover all required AoA offsets. The actual number of antennas is not
determined and depends on the TE implementation. Positioner in the TE
part is optional.

Figure A.3.3.3.1: TE diagram for radiated RRM tests

Figure A.3.3.3.1-1 shows the connection diagram inside the SS NR of
Figure A.3.3.3.1 for downlink signal path (for single probe). 1x2
without fading in FR2 RRM test case represents the scenario with single
antenna transmission from TE side and 2 antenna receptions at UE side,
which is equivalent to 1x1 in conducted test case from test equipment
perspective.

Figure A.3.3.3.1-1: TE diagram for radiated 1AoA RRM tests (1x2 without
fading)

A.3.4 User Equipment Parts for Radiated Measurements
----------------------------------------------------

### A.3.4.1 Basic Transmitter/Receiver tests

The User Equipment part is focused on logical representation of UE
antenna(s), DUT positioner and positioner controller. The UE connection
diagram below is applicable for NR radiated RX and TX tests, including
CA and UL MIMO tests.

Figure A.3.4.1.1: UE diagram for radiated RX and TX tests

### A.3.4.2 Demodulation and CSI tests

Same as Figure A.3.4.1.1.

### A.3.4.3 RRM tests

Same as Figure A.3.4.1.1.

########  Annex B (normative): Permitted test methods For OTA Testing

B.1 General
===========

Editor\'s Note: The working assumption is that the DFF or IFF: CATR
based OTA test methodologies defined in Annexes B.2.2 and B.2.4
respectively should be used for Signalling test.

The applicability of the permitted test methods herein is defined by the
appropriate references within clauses 5, 6, and 7. A summary of the
applicability is shown in Table B.1-1.

Table B.1-1: Permitted Test Methods Applicability Summary

  Permitted Test Methods                                                                                                                              UE RF          Demodulation   RRM     
  --------------------------------------------------------------------------------------------------------------------------------------------------- -------------- -------------- ------- -------
                                                                                                                                                                                    1 AoA   2 AoA
  DFF                                                                                                                                                 yes            yes            yes     yes
  DFF Simplification                                                                                                                                  yes            yes            yes     N/A
  IFF                                                                                                                                                 yes            yes            yes     N/A
  NFTF                                                                                                                                                yes (Note 1)   N/A            N/A     N/A
  Enhanced IFF                                                                                                                                        yes            yes            yes     yes
  IFF+DFF                                                                                                                                             yes            yes            yes     yes
  Note 1: Not applicable for EIS, Frequency Error, EVM, Carrier Leakage, In-Band Emission, EVM SF, OBW as defined in Table J-1 of TS38.521-2 \[15\]                                         

B.2 Permitted Test Methods
==========================

B.2.1 General
-------------

The main objective of this annex is to specify basic parameters of
permitted OTA test methods suitable for RF Tx and Rx, Performance, and
RRM measurements and Signalling Conformance tests performed at high
frequency in the FR2 operating bands defined in clause 4.3.1.2. The
applicability of each OTA test method is summarized in Table B.1-1.

B.2.2 Direct far field (DFF)
----------------------------

### B.2.2.1 Description

The DFF measurement setup for FR2 is capable of centre and off-centre of
beam measurements and is shown in Figure B.2.2.1-1 below.

Figure B.2.2.1-1: DFF measurement setup

The key aspects of the DFF setup are:

\- Far-field measurement system in an anechoic chamber

\- The criterion for determining the far-field distance is described in
B.2.2.4.

\- A positioning system such that the angle between the dual-polarized
measurement antenna and the DUT has at least two axes of freedom and
maintains a polarization reference.

\- A positioning system such that the angle between the link antenna and
the DUT has at least two axes of freedom and maintains a polarization
reference; this positioning system for the link antenna is in addition
to the positioning system for the measurement antenna and provides for
an angular relationship independently controllable from the measurement
antenna.

\- For setups intended for measurements of UE RF characteristics in
non-standalone (NSA) mode with 1 UL configuration, an LTE link antenna
is used to provide the LTE link to the DUT. The LTE link antenna
provides a stable LTE signal without precise path loss or polarization
control.

\- For setups intended for measurements in NR CA mode with FR1 and FR2
inter-band NR CA, test setup provides NR FR1 link to the DUT. The NR FR1
link has a stable and noise-free signal without precise path loss or
polarization control.

The applicability criteria of the DFF setup are:

\- The DUT radiating aperture is D ≤ 5 cm

\- Either a single radiating aperture, multiple non-coherent apertures,
or multiple coherent apertures DUTs can be tested

\- If multiple antenna panels that are phase coherent are defined as a
single array, the criterion on DUT radiating aperture applies to this
single array

\- D is based on the MU assessment in Annex B.1.1.3 of TR 38.810 \[24\]

\- A measurement distance larger than the far-field criteria defined in
B.2.2.4 is not precluded

\- If the uncertainties can be further optimized, the MU may be reduced
or D may be increased

\- A manufacturer declaration on the following elements is needed unless
the entire DUT size is contained in a sphere of diameter of ≤ 5 cm:

\- Manufacturer declares antenna array size

For RRM testing, an example baseline system with two simultaneously
active AoA (NMAX\_AoAs = 2) as defined in Clause 7.1.3 using a DFF setup
is illustrated in Figure 2.2.1-2. Implementations of the RRM baseline
system with only a subset of the probes are possible as long as the
system can satisfy the relative angular relationships outlined in Clause
7.1.3.2.1.

![](./media/image92.emf){width="5.309027777777778in"
height="3.921527777777778in"}

Figure B.2.2.1-2: Example RRM baseline system with two simultaneously
active AoA using a DFF setup.

### B.2.2.2 Quiet zone dimension

In order to allow testing of DUTs of different sizes and to allow for
flexibility in test chamber implementations, there will be various
defined quiet zone dimensions. The smallest quiet zone shall have a
radius of 100mm to accommodate DUTs such as smartphones. The next larger
quiet zone shall have a radius of 150mm to accommodate larger DUTs such
as tablets. To test even larger devices, e.g., larger tablets and
laptops, quiet zones with 200mm and 275mm are defined The device types
are listed as examples and other device types are not precluded.

The radiating portions of the device have to be fully enclosed within
the quiet zone, but the non-radiating portions of the device can be
located/placed outside the quiet zone if a vendor declaration with
positioning reference points and the minimum QZ required to contain all
active antennas within the quiet zone (per band) is provided. This
grey-box testing approach where the declared reference point is aligned
with the centre of the QZ is further illustrated in Figure B.2.2.2-1.

Figure B.2.2.2-1: Grey-box test approach

In the absence of a vendor declaration, the geometric centre of the DUT
shall be aligned with the centre of the QZ and the DUT shall be fully
contained within the QZ. This black-box testing approach is further
illustrated in Figure B.2.2.2-2.

Figure B.2.2.2-2: Black-box test approach

### B.2.2.3 Quality of the quiet zone

The quality of the quiet zone shall be measured for the frequencies
defined in FFS. The measured quality of the quiet zone performance is
used in uncertainty calculations for the appropriate quality of the
quiet zone dimension utilized for the DUT.

### B.2.2.4 Measurement Distance

For far-field measurements, the distance *R* between the DUT and the
measurement antenna shall be calculated by the following equation.

where *λ* is the largest wavelength within the frequency band of
interest and *D* is the diameter of the smallest sphere that encloses
the radiating parts of the DUT.

For DFF, free space path loss is calculated by applying the Free Space
Loss formula with *R* equal to the far field distance: .

The minimum range length of a DFF system, i.e., the minimum distance
between the centre of the quiet zone and the measurement antenna, needs
to take into account the unknown offset of the antenna aperture from the
centre of quiet zone in order to guarantee far-field conditions for any
antenna array integrated inside the DUT. The distance between the centre
of the quiet zone to the measurement antenna is referenced as R~DFF~,
while the radius of the quiet zone is R~QZ~ as illustrated in Figure
B.2.2.4-1. The minimum distance between the antenna array integrated
anywhere within the DUT and the measurement antenna needs to meet the
far-field distance, R~FF~ = 2D^2^/λ.

Figure B.2.2.4-1: Illustration of DFF System for range length definition

The setup in Figure B.2.2.4-2 is used to derive the minimum range length
for NR FR2 DFF systems where the sphere enclosing the DUT matches the QZ
and the DUT antenna with radiating aperture diameter D located in the
corner of the DUT. With this setup, the minimum range length, R~DFF~,
can be determined as

R~DFF~ = R~QZ~ -- D/2 + R~FF~ = R~QZ~ -- D/2 + 2D^2^/λ

which is tabulated in Table B.2.2.4-1 for two different QZ sizes
assuming D=5cm.

Figure B.2.2.4-2: Illustration of DFF System for minimum range length
definition

Table B.2.2.4-1: Minimum Range Length of DFF System for *D* = 5cm

  --------------------------------------------------
  *f* \[GHz\]\   24.25   30     40     50     52.6
  QZ \[cm\]                                   
  -------------- ------- ------ ------ ------ ------
                                              

  20             0.48    0.58   0.74   0.91   0.95

  30             0.53    0.63   0.79   0.96   1.00
  --------------------------------------------------

The influence of measurement distance on measurement uncertainty is
discussed in Annex B.2.1 of TR 38.903 \[XX\].

B.2.3 Direct far field (DFF) setup simplification for centre of beam measurements
---------------------------------------------------------------------------------

### B.2.3.1 Description

The DFF setup in Annex B.2.2 can be simplified in the following way to
perform centre of the beam measurements:

\- The measurement and the link antenna can be combined so that the
single antenna is used to steer the beam and to perform UE measurements.

The measurement setup for FR2 capable of centre of beam measurements is
shown in Figure B.2.3.1-1 below.

Figure B.2.3.1-1: DFF simplification for centre of beam measurement
setup

The applicability criteria of the simplified DFF setup for centre of
beam measurements are defined in B.2.2.1.

### B.2.3.2 Quiet zone dimension

Same as Annex B.2.2.2.

### B.2.3.3 Quality of the quiet zone

Same as Annex B.2.2.3.

### B.2.3.4 Measurement Distance

Same as Annex B.2.2.4.

B.2.4 Indirect far field (IFF): Compact Antenna Test Range (CATR)
-----------------------------------------------------------------

### B.2.4.1 Description

The IFF method utilizing a compact antenna test range (CATR) creates the
far field environment using a transformation with a parabolic reflector.

The IFF CATR measurement setup for FR2 is capable of centre and
off-centre of beam measurements and an example setup is shown in Figure
B.2.4.1-1 below. The relative orientation of the coordinate system with
respect to the reflector and the axes of rotation apply to any CATR
measurement setup.

Figure B.2.4.1-1: Example of IFF: CATR measurement setup

The key aspects of this test method setup are:

\- Indirect Far Field using Compact Antenna Test Range as described in
TR 38.810 \[24\] with quiet zone diameter that meets the requirements of
B.2.4.2.

\- A positioning system such that the angle between the dual-polarized
measurement antenna and the DUT has at least two axes of freedom and
maintains a polarization reference.

\- Before performing the UE Beamlock Test Function as defined in clause
4.9.2, the measurement probe acts as a link antenna maintaining
polarization reference with respect to the DUT. Once the beam is locked
then the link is to be passed to the link antenna which maintains
reliable signal level with respect to the DUT.

\- For setups intended for measurements of UE RF characteristics in
non-standalone (NSA) mode with 1UL configuration, an LTE link antenna is
used to provide the LTE link to the DUT. The LTE link antenna provides a
stable LTE signal without precise path loss or polarization control.

\- For setups intended for measurements in NR CA mode with FR1 and FR2
inter-band NR CA, test setup provides NR FR1 link to the DUT. The NR FR1
link has a stable and noise-free signal without precise path loss or
polarization control.

The applicability criteria of this test method are:

\- The total test volume, i.e., the quiet zone is defined as a sphere
with radius R.

\- DUT must fit within the quiet zone for the entire duration of the
test.

\- Either a single radiating aperture, multiple non-coherent apertures
or multiple coherent apertures DUTs can be tested.

\- No manufacturer declaration of the antenna array size is needed.

### B.2.4.2 Quiet zone dimension

Same as Annex B.2.2.2.

### B.2.4.3 Quality of the quiet zone

Same as Annex B.2.2.3.

### B.2.4.4 Measurement Distance

The CATR system does not require a measurement distance of to achieve a
plane wave as in a standard far field range.

For the CATR system, the far-field distance is seen as the focal length.
The focal length is the distance between the feed and the reflector of
the CATR. Further information on the focal length of a CATR system can
be found in clause 5.2.3.2 of TR 38.810 \[24\].

The measurement distance for any CATR system implementation shall be
adequate to meet the quiet zone dimensions defined in B.2.4.2.

In a CATR, from the reflector to the quiet zone, there is a plane wave
with no free space path loss.

For CATR, free space path loss is calculated by applying the Free Space
Loss formula with *R* equal to the far field distance based on the focal
length: ![](./media/image101.emf){width="0.5in"
height="0.4166666666666667in"}.

A summary of the comparison of path losses which can be expected for the
CATR compared to a Fraunhofer limit distance () for different antenna
sizes and frequencies can be found in clause 5.2.3.2 of TR 38.810
\[24\].

The influence of measurement distance on measurement uncertainty can be
considered as zero as defined in Annex B.2.2 of TR 38.903 \[XX\].

B.2.5 Near field to far field transform (NFTF)
----------------------------------------------

### B.2.5.1 Description

The NFTF method computes the metrics defined in Far Field by using the
Near Field to Far Field transformation.

The NFTF measurement setup of UE RF characteristics for FR2 is capable
of centre and off centre of beam measurements and an example setup is
shown in Figure B.2.5.1-1:

Figure B.2.5.1-1: Example of NFTF measurement setup

The key aspects of the Near Field test range are:

\- Radiated Near Field UE beam pattern is measured and based on the NFTF
mathematical transform, the final metric such as EIRP is the same as the
metric for the baseline setup

\- A positioning system such as the angle between the dual-polarized
measurement/link antenna and the DUT has at least two axes of freedom
and maintains a polarization reference

\- For setups intended for measurements of UE RF characteristics in
non-standalone (NSA) mode with 1UL configuration, an LTE link antenna is
used to provide the LTE link to the DUT. The LTE link antenna provides a
stable LTE signal without precise path loss or polarization control.

\- For setups intended for measurements in NR CA mode with FR1 and FR2
inter-band NR CA, test setup provides NR FR1 link to the DUT. The NR FR1
link has a stable and noise-free signal without precise path loss or
polarization control.

The applicability criteria of the NFTF setup are:

\- The DUT radiating aperture is D ≤ 5 cm

\- Either a single radiating aperture, multiple non-coherent apertures
or multiple coherent apertures DUTs can be tested

\- If multiple antenna panels that are phase coherent are defined as a
single array, the criterion on DUT radiating aperture applies to this
single array

\- D is based on the MU assessment in Annex B.1.4.3 of TR 38.810 \[24\]

\- If the uncertainties can be further optimized, the MU may be reduced
or D may be increased

\- A manufacturer declaration on the following elements is needed unless
the entire DUT size is contained in a sphere of diameter of ≤ 5 cm:

\- Manufacturer declares antenna array size

\- EIRP, TRP, and spurious emissions metrics can be tested.

### B.2.5.2 Quiet zone dimension

Same as Annex B.2.2.2.

### B.2.5.3 Quality of the quiet zone

Same as Annex B.2.2.3.

### B.2.5.4 Measurement Distance

The NFTF system does not require a measurement distance of as in a
standard far field range due to the use of the Near Field to Far Field
transformation.

The measurement distance for any NFTF system implementation shall ensure
that the DUT is not measured in the reactive near-field region and is
adequate to meet the quiet zone dimensions defined in B.2.5.2.

B.2.6 Enhanced IFF
------------------

### B.2.6.1 Description

The Enhanced IFF method utilizing multiple compact antenna test ranges
(CATRs) creates the far field environment using a transformation with 2
or more parabolic reflectors for RRM testing with two simultaneously
active AoA (NMAX\_AoAs = 2) as defined in Clause 7.1.3.

An example RRM baseline system using an Enhanced IFF setup are shown in
Figure B.2.6.1-1. Implementations of the RRM baseline system with only a
subset of the reflectors/probes are possible as long as the system can
satisfy the relative angular relationships outlined in Clause 7.1.3.2.1.

![](./media/image103.emf){width="5.15625in"
height="3.8131944444444446in"}

Figure B.2.6.1-1: Example RRM baseline system with two simultaneously
active AoA using an Enhanced IFF setup

The key aspects of this test method setup are the same as the IFF setup,
outlined in Clause B.2.4.1.

### B.2.6.2 Quiet zone dimension

Same as Clause B.2.2.2.

### B.2.6.3 Quality of the quiet zone

Same as Clause B.2.2.3.

### B.2.6.4 Measurement Distance

Same as Clause B.2.4.4.

B.2.7 IFF+DFF
-------------

### B.2.7.1 Description

The IFF+DFF method is utilizing a combination of compact antenna test
ranges (CATRs) and DFF probes for RRM testing with two simultaneously
active AoA (NMAX\_AoAs = 2) as defined in Clause 7.1.3.

An example RRM baseline system using the IFF+DFF setup is shown in
Figure B.2.7.1-1. Implementations of the RRM baseline system with only a
subset of the probes are possible as long as the system can satisfy the
relative angular relationships outlined in Clause 7.1.3.2.1.

![](./media/image104.emf){width="5.530555555555556in"
height="3.921527777777778in"}

Figure B.2.7.1-1: Example RRM baseline system with two simultaneously
active AoA using an IFF+DFF setup

The key aspects of this test method setup are the same as the IFF setup
for the probes based on the IFF method, outlined in B.2.4.1 and the DFF
setup for the probes based on the DFF method, outlined in Clause
B.2.2.1.

### B.2.7.2 Quiet zone dimension

Same as Clause B.2.2.2.

### B.2.7.3 Quality of the quiet zone

Same as Clause B.2.2.3.

### B.2.7.4 Measurement Distance

Same as Clause B.2.4.4 for the IFF setup for the probes based on the IFF
method and Clause B.2.2.4 for the DFF setup for the probes based on the
DFF method.

########  Annex C (informative): Calculation of test frequencies

C.0 General
===========

Test frequencies are defined in clause 4.3.1 with extensions for
signalling test cases in clause 6.2.3. This annex gives a guideline to
determine these test frequencies and the associated signalling
parameters for a given NR band, NR CA or NR DC band combination.

Clause C.1 describes definitions and parameters used by the procedures
to determine test frequencies, SS/PBCH Block (SSB) and CORESET\#0
configuration parameters.

Clause C.2 describes how to calculate test frequencies for symmetric NR
bands, asymmetric NR bands, NR CA and NR DC configurations.

Clause C.3.2 describes how to determine the SSB, CORESET\#0 and
signalling parameters for FR1 carriers with SCS=15 kHz or SCS=30 kHz,
and for FR2 carriers with SCS=60 kHz or SCS=120 kHz. CORESET\#0 is
required for a carrier to be used as a Pcell.

Clause C.3.3 describes how to determine the SSB and signalling
parameters for a carriers without CORESET\#0.

Clause C.5 describes how to calculate test frequencies for NR V2X bands.

C.1 Definitions and Parameters
==============================

Figure C.1-1 shows SSB and CORESET\#0 and related parameters. CORESET\#0
is required for a carrier to be used as a PCell.

Figure C.1-1: location of SSB and CORESET\#0 within a channel

The parameters referenced in figure C.1-1 are defined in Table C.1-1.

Table C.1-1: Definition of parameters in Figure C.1-1 used in Annex C

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Parameter                     Description
  ----------------------------- -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  FPointA                       Reference Point A frequency.

  F~carrier~                    F~carrier~ is the centre frequency of a carrier corresponding to its NR-ARFCN value.

  F~carrierLow~                 F~carrierLow~ is the centre frequency of lowest subcarrier of the carrier.\
                                F~carrierLow~ = F~carrier~ - 12 \* SCS~Carrier~ \* (N~RB~ / 2) with N~RB~ according to Table 5.3.2-1 of TS 38.101-1 \[7\] and TS 38.101-2 \[8\] for the channel bandwidth of the carrier.

  ΔF~carrierBandwidth~          ΔF~carrierBandwidth~ is the carrier's channel bandwidth as provided in *carrierBandwidth* to the UE (*SCS-SpecificCarrier*).

  ΔF~offsetToCarrier~           ΔF~offsetToCarrier~ is the frequency offset between Point A and the centre frequency of lowest subcarrier of the carrier. ΔF~offsetToCarrier~ = *offsetToCarrier* \* PRB~size~, where PRB~size~ according to the subcarrier spacing of the carrier. *offsetToCarrier* is signalled to the UE (*SCS-SpecificCarrier*).

  F~SSref~                      Centre frequency of SSB. For a cell selectable as PCell the F~SSref~ corresponds to a valid GSCN value according to clause 5.4.3.1 of TS 38.101-1 \[7\] and TS 38.101-2 \[8\].

  ΔF~Offset(RBs)~               ΔF~Offset(RBs)~ = 12 \* Offset(RBs) \* *subCarrierSpacingCommon*, where Offset(RBs) is given in tables 13-1 to 13-10 of TS 38.213 \[22\].

  ΔF~kSSB~                      ΔF~KSSB~ = k~SSB~ \* {15 kHz for FR1, *subCarrierSpacingCommon* (MIB) for FR2} (TS 38.211 \[3\], clause 7.4.3.1)

  ΔF~OffsetSSB-CORESET0~        Frequency offset between the lowest subcarrier of the SSB and the lowest subcarrier of CORESET\#0. ΔF~OffsetSSB-CORESET0~ = ΔF~Offset(RBs)~ + ΔF~kSSB.~

  ΔF~OffsetCORESET-0-Carrier~   Frequency offset, F~OffsetCORESET\#0-Carrier~, between the lowest subcarrier of CORESET\#0 and the lowest subcarrier of the carrier.

  ΔF~OffsetSSB-Carrier~         Frequency offset between the lowest subcarrier of the SSB and the lowest subcarrier of the carrier.

  F~CORESET0Low~                Centre frequency of subcarrier 0 of CORESET\#0.

  F~OffsetToPointA~             Frequency of the lowest subcarrier of the lowest resource block, which has the subcarrier spacing provided by the higher-layer parameter subCarrierSpacingCommon and overlaps with the SS/PBCH block used by the UE for initial cell selection, expressed in units of resource blocks assuming 15 kHz subcarrier spacing for FR1 and 60 kHz subcarrier spacing for FR2 (TS 38.211 \[29\] clause 4.4.4.2).

  ΔF~OffsetToPointA~            Frequency offset between F~OffsetToPointA~ and point A. ΔF~OffsetToPointA~ = *offsetToPointA* \* {15 kHz for FR1; 60 kHz for FR2} (TS 38.211 \[29\] clause 4.4.4.2).
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Additional parameters used in this annex are defined in Table C.1-2.

Table C.1-2: Definition of additional parameters used in Annex C.

+-----------------------------+---------------------------------------+
| k~SSB~                      | As defined in TS 38.211 \[29\] clause |
|                             | 7.4.3.1                               |
+=============================+=======================================+
| SCS~Carrier~                | Subcarrier spacing for the carrier    |
|                             | (*SCS-SpecificCarrier*):\             |
|                             | FR1: 15kHz, 30kHz or 60kHz according  |
|                             | to TS 38.101-1 \[7\] Table 5.3.5-1    |
|                             |                                       |
|                             | FR2: 60kHz or 120kHz according to TS  |
|                             | 38.101-2 \[8\] Table 5.3.5-1          |
+-----------------------------+---------------------------------------+
| SCS~SSB~                    | SS/PBCH block subcarrier spacing      |
|                             |                                       |
|                             | FR1: 15kHz or 30kHz according to TS   |
|                             | 38.101-1 \[7\] Table 5.4.3.3-1        |
|                             |                                       |
|                             | FR2: 120kHz or 240kHz according to TS |
|                             | 38.101-2 \[8\] Table 5.4.3.3-1        |
|                             |                                       |
|                             | NOTE: According to the tables in      |
|                             | clause 13 of TS 38.213 \[22\] not all |
|                             | combinations of SCS~SSB~ and          |
|                             | SCS~Carrier~ are applicable.          |
+-----------------------------+---------------------------------------+
| SCS~common~                 | Subcarrier spacing for SIB1, Msg.2/4  |
|                             | for initial access, paging and        |
|                             | broadcast SI-messages. Provided to    |
|                             | the UE in the MIB in IE               |
|                             | *subCarrierSpacingCommon*.            |
+-----------------------------+---------------------------------------+
| PRB~size~                   | Physical Resource Block size of the   |
|                             | carrier = 12 \* SCS~Carrier~.         |
+-----------------------------+---------------------------------------+
| CRB~size~                   | Common Resource Block size = 12 \*    |
|                             | SCS~common~.                          |
+-----------------------------+---------------------------------------+
| F~DL\_Low,~ F~UL\_Low~      | Lowest frequency of the downlink and  |
|                             | uplink frequency range of the band as |
|                             | defined in clause 5.2 of TS 38.101-1  |
|                             | \[7\] and TS 38.101-2 \[8\].          |
+-----------------------------+---------------------------------------+
| F~DL\_High,~ F~UL\_High~    | Highest frequency of the downlink and |
|                             | uplink frequency range of the band as |
|                             | defined in clause 5.2 of TS 38.101-1  |
|                             | \[7\] and TS 38.101-2 \[8\].          |
+-----------------------------+---------------------------------------+
| ΔF~Raster~                  | Frequency raster of the band as       |
|                             | defined in clause 5.4.2.3 of TS       |
|                             | 38.101-1 \[7\] and TS 38.101-2 \[8\]. |
+-----------------------------+---------------------------------------+
| BW~DL~                      | Bandwidth of downlink frequency range |
|                             | of the band.                          |
+-----------------------------+---------------------------------------+
| BW~UL~                      | Bandwidth of uplink frequency range   |
|                             | of the band.                          |
+-----------------------------+---------------------------------------+
| CBW~DL~                     | Downlink channel bandwidth (MHz) of   |
|                             | the carrier according to Table        |
|                             | 5.3.2-1 of TS 38.101-1 \[7\] and TS   |
|                             | 38.101-2 \[8\].                       |
+-----------------------------+---------------------------------------+
| CBW~UL~                     | Uplink channel bandwidth (MHz) of the |
|                             | carrier according to Table 5.3.2-1 of |
|                             | TS 38.101-1 \[7\] and TS 38.101-2     |
|                             | \[8\].                                |
+-----------------------------+---------------------------------------+
| F~Tx-Rx\_separation~        | Default Tx -- Rx carrier centre       |
|                             | frequency separation of the band as   |
|                             | defined in clause 5.4.4 of TS         |
|                             | 38.101-1 \[7\]. For TDD bands         |
|                             | F~Tx-Rx\_separation~ = 0.             |
+-----------------------------+---------------------------------------+
| ΔF~Tx-Rx\_separation~       | ΔF~Tx-Rx\_separation~ = \| (BW~DL~ -- |
|                             | BW~UL~)/2 \| is the deviation to the  |
|                             | default Tx-Rx carrier centre          |
|                             | frequency separation                  |
|                             | (F~Tx-Rx\_separation~) for FDD FR1    |
|                             | bands supporting asymmetric channel   |
|                             | bandwidths as defined in clause 5.3.6 |
|                             | of TS 38.101-1 \[7\].                 |
+-----------------------------+---------------------------------------+
| BW~SSB~                     | **Bandwidth of the SSB.** BW~SSB~ =   |
|                             | 12 \* SCS~SSB~ \* 20.                 |
+-----------------------------+---------------------------------------+
| ΔGSCN, GSCN~MIN,~ GSCN~MAX~ | GSCN step size, GSCN minimum and GSCN |
|                             | maximum values for the NR band        |
|                             | according to table 5.4.3.3-1 of TS    |
|                             | 38.101-1 \[7\] and TS 38.101-2 \[8\]  |
+-----------------------------+---------------------------------------+
| Offset~RBs~                 | Offset (RBs) according to the         |
|                             | applicable table 13-1 to 13-10 in TS  |
|                             | 38.213 \[22\] for the given band and  |
|                             | {SCS~SSB~, SCS~Carrier~} combination  |
|                             | of the carrier.                       |
+-----------------------------+---------------------------------------+
| Offset~RBs,max~             | Maximum value for Offset (RBs)        |
|                             | according to the applicable table     |
|                             | 13-1 to 13-1o in TS 38.213 \[22\] for |
|                             | the given band and {SCS~SSB~,         |
|                             | SCS~Carrier~} combination of the      |
|                             | carrier limited to the table indexes  |
|                             | with number of RBs equal to the       |
|                             | maximum value of in the table.        |
+-----------------------------+---------------------------------------+
| Offset~RBs,min~             | Minimum value for Offset (RBs)        |
|                             | according to the applicable table     |
|                             | 13-1 to 13-1o in TS 38.213 \[22\] for |
|                             | the given band and {SCS~SSB~,         |
|                             | SCS~Carrier~} combination of the      |
|                             | carrier limited to the table indexes  |
|                             | with number of RBs equal to the       |
|                             | minimum value of in the table.        |
+-----------------------------+---------------------------------------+

C.2 Determination of test frequencies
=====================================

C.2.0 General
-------------

Test frequencies are determined as:

For symmetric NR bands (supporting same bandwidth in UL and DL):

\- test frequencies for the supported symmetric channel bandwidth
combinations are determined as described in clause C.2.1; and

\- the test frequencies for the supported asymmetric channel bandwidth
combinations are determined as described in clause C.2.3.

For asymmetric NR bands (supporting different bandwidth in UL and DL):

\- the test frequencies for the supported symmetric channel bandwidth
combinations are determined as described in clause C.2.2; and

\- the test frequencies for the supported asymmetric channel bandwidth
combinations are determined as described in clause C.2.3.

For NR CA and NR DC:

\- the test frequencies are determined as described in the relevant
subclause in C.2.4 depending to the type of configuration.

The carrier test frequencies are determined considering the channel
raster according to clause 5.4.2.3 in TS 38.101-1 \[7\] for FR1 and in
TS 38.101-2 \[8\] for FR2.

C.2.1 Determination of test frequencies for symmetric NR bands and symmetric uplink and downlink channel bandwidth combinations
-------------------------------------------------------------------------------------------------------------------------------

### C.2.1.1 Determination of test frequencies for Low-, Mid- and High-Range

Downlink:

  **F~DL\_LowRange~** = **Ceil**((F~DL\_Low~ + CBW~DL~/2) / ΔF~Raster~) \* ΔF~Raster~      C.2.1.1-Eq1
  ---------------------------------------------------------------------------------------- -------------
  **F~DL\_MidRange~** = **Round**((F~DL\_Low~ + BW~DL~/2) / ΔF~Raster~) \* ΔF~Raster~      C.2.1.1-Eq2
  **F~DL\_HighRange~** = **Floor(**(F~DL\_High~ - CBW~DL~/2) / ΔF~Raster~) \* ΔF~Raster~   C.2.1.1-Eq3

F~DL\_LowRange~ is rounded up and F~DL\_HighRange~ is rounded down to
obey to the minimum guard band according to clause 5.3.3 of TS 38.101-1
\[7\] and TS 38.101-2 \[8\].

Uplink:

  **F~UL\_LowRange~** = F~DL\_LowRange~ - F~Tx-Rx\_separation~     C.2.1.1-Eq4
  ---------------------------------------------------------------- -------------
  **F~UL\_MidRange~** = F~DL\_MidRange~ - F~Tx-Rx\_separation~     C.2.1.1-Eq5
  **F~UL\_HighRange~** = F~DL\_HighRange~ - F~Tx-Rx\_separation~   C.2.1.1-Eq6

For those FDD frequency bands with two UL sub-bands,
F~Tx-Rx\_separation~ shall be chosen using the following criteria:

\- For Low-Range and Mid-Range, use F~Tx-Rx\_separation~ for lower UL
sub-band.

**~-~** For High-Range, use F~Tx-Rx\_separation~ for higher UL sub-band.

### C.2.1.2 Determination test frequencies for of Mid-Low and Mid-High-Range for signalling tests

  **F~Mid-LowRange~** = **Round**((F~LowRange~+ (F~HighRange~ - F~LowRange~ )/3) / ΔF~Raster~) \* ΔF~Raster~        C.2.1.2-Eq1
  ----------------------------------------------------------------------------------------------------------------- -------------
  **F~Mid-HighRange~** = **Round**((F~LowRange~ + 2\*(F~HighRange~ - F~LowRange~ )/3) / ΔF~Raster~) \* ΔF~Raster~   C.2.1.2-Eq2

C.2.2 Determination of test frequencies for asymmetric NR bands and symmetric uplink and downlink channel bandwidth combinations
--------------------------------------------------------------------------------------------------------------------------------

Determination of test frequencies for asymmetric NR bands, and symmetric
uplink and downlink channel bandwidth combinations are determined using
the procedure in clause C.2.3 with ΔF~Tx-Rx~ = 0.

C.2.3 Determination of test frequencies for asymmetric uplink and downlink channel bandwidth combinations
---------------------------------------------------------------------------------------------------------

### C.2.3.1 General

The following procedure is used to calculate test frequencies for NR
bands supporting asymmetric UL and DL channel bandwidths as described
below, where CBW~UL~ and CBW~DL~ refer to the carrier's UL and DL
channel bandwidths; and BW~UL~ and BW~DL~ refer to the band's total UL
and DL bandwidths.

The procedure is also used to calculate test frequencies for symmetric
UL and DL bandwidth combinations for asymmetric NR bands.

For FDD bands supporting asymmetric uplink and downlink bandwidth
combinations a deviation of ΔF~TX-RX~ (C.2.3.1-Eq1) is to be added to
the nominal Tx-Rx carrier centre frequency separation,
F~Tx-Rx\_separation~ (TS 38.101-1 \[7\] clause 5.3.6) unless, for such
asymmetric uplink and downlink bandwidth combination, it is explicitly
stated that ΔF~TX-RX~ as defined in clause 5.3.6 does not apply
according to TS 38.101-1 \[7\] Table 7.3.2-3 (Uplink configuration for
reference sensitivity).

  ---------------------------------------- -------------
  ΔF~TX-RX~ = \|(CBW~DL~ -- CBW~UL~)/2\|   C.2.3.1-Eq1
  ---------------------------------------- -------------

For the case of asymmetric NR bands and symmetric UL and DL bandwidth
combinations no additional deviation ΔF~TX-RX~ is applied. To meet the
Tx-Rx frequency separation requirement for asymmetric NR bands where the
supported overall UL bandwidth is smaller than the supported overall DL
bandwidth, it may not be possible to cover the full DL frequency range
for all UL and DL channel bandwidth combinations. For CA when such band
is only used for DL CC the full range can be used for all DL channel
bandwidths.

To maximize the tested frequency range for the non-CA case, the UL
frequency range, as being smaller than the DL frequency range, needs to
be used as the starting point to calculate the uplink and downlink test
frequencies.

### C.2.3.2 Determination of Low-, Mid- and High-Range for asymmetric uplink and downlink bandwidth combinations

The following procedure is used to determine the test frequencies for
Low-, Mid- and High-Range for bands supporting asymmetric UL and DL
bandwidth combinations.

1\. Calculate uplink carrier centre frequencies:

  **F~UL\_LowRange~** = **Ceil**((F~UL\_Low~ + CBW~UL~/2) / ΔF~Raster~) \* ΔF~Raster~                     C.2.3.2-Eq1
  ------------------------------------------------------------------------------------------------------- -------------
  **F~UL\_MidRange~** = **Round**((F~UL\_Low~ + BW~UL\_Band~/2) / ΔF~Raster~) \* ΔF~Raster~               C.2.3.2-Eq2
  **F~UL\_HighRange~** = **Floor**((F~UL\_Low~ + BW~UL\_Band~ -- CBW~UL~/2) / ΔF~Raster~) \* ΔF~Raster~   C.2.3.2-Eq3

For those FDD frequency bands with two UL sub-bands, for Low- and
Mid-Range, use lower sub-band and for High-Range use higher sub-band. In
these cases, BW~UL\_Band~ refers to the sub-band.

2\. Calculate the downlink frequencies:

Calculate the DL carrier centre frequencies from the UL frequencies in
step 1.

  **F~DL\_LowRange~** = F~UL\_LowRange~ + F~Tx-Rx\_separation~ + ΔF~Tx-Rx~     C.2.3.2-Eq4
  ---------------------------------------------------------------------------- -------------
  **F~DL\_MidRange~** = F~UL\_MidRange~ + F~Tx-Rx\_separation~ + ΔF~Tx-Rx~     C.2.3.2-Eq5
  **F~DL\_HighRange~** = F~UL\_HighRange~ + F~Tx-Rx\_separation~ + ΔF~Tx-Rx~   C.2.3.2-Eq6

For those FDD frequency bands where TX-RX carrier centre frequency
separation can have multiple values, F~Tx-Rx\_separation~ shall be
chosen using the following criteria:

\- For Low-Range, use F~Tx-Rx\_separation~ that minimizes
**F~DL\_LowRange.~**for each SCS.

\- For Mid-Range, use F~Tx-Rx\_separation~ closer to F~DL\_LowRange~ +
(F~DL\_HighRange\ --~ F~DL\_LowRange~)/2.

**~-~** For High-Range, use F~Tx-Rx\_separation~ that maximizes
**F~DL\_HighRange~** for each SCS.

3\. Check that the calculated centre test frequencies in step 2 for the
BW~DL~ fits within the bands DL frequency range:

If F~DL\_LowRange~ - CBW~DL~/2 is smaller than the lowest frequency of
the band then recalculate the minimum F~DL\_LowRange~ and modify the
associated **F~UL\_LowRange,~ F~DL\_MidRange~ and F~UL\_MidRange~** as:

  F~DL\_LowRange~ = Ceil((F~DL\_Low~ + CBW~DL~/2) / ΔF~Raster~) \* ΔF~Raster~                          C.2.3.2-Eq7
  ---------------------------------------------------------------------------------------------------- --------------
  F~UL\_LowRange~ = F~DL\_LowRange~ - F~Tx-Rx\_separation~ - ΔF~Tx-Rx~                                 C.2.3.2-Eq8
  **F~DL\_MidRange~** = **Round**((F~DL\_LowRange~ + F~DL\_HighRange~)/2 / ΔF~Raster~))\* ΔF~Raster~   C.2.3.2-Eq8a
  **F~UL\_MidRange~ =** F~DL\_MidRange~ - F~Tx-Rx\_separation~ - ΔF~Tx-Rx~                             C.2.3.2-Eq8b

If F~DL\_HighRange~ + CBW~DL~/2 is larger than the higher frequency of
the band then recalculate the maximum F~DL\_HighRange~ and modify the
associated **F~UL\_HighRange,~ F~DL\_MidRange~ and F~UL\_MidRange~** as:

  **F~DL\_HighRange~** = **Floor**((F~DL\_Low~ + BW~DL\_Band~ -- CBW~DL~/2) / ΔF~Raster~) \* ΔF~Raster~   C.2.3.2-Eq9
  ------------------------------------------------------------------------------------------------------- --------------
  F~UL\_HighRange~ = F~DL\_HighRange~ - F~Tx-Rx\_separation~ - ΔF~Tx-Rx~                                  C.2.3.2-Eq10
  **F~DL\_MidRange~** = **Round**((F~DL\_LowRange~ + F~DL\_HighRange~)/2 / ΔF~Raster~))\* ΔF~Raster~      C.2.3.2-Eq11
  **F~UL\_MidRange~ =** F~DL\_MidRange~ - F~Tx-Rx\_separation~ - ΔF~Tx-Rx~                                C.2.3.2-Eq12

### C.2.3.3 Determination of test frequencies for a Mid range adjacent inter-frequency cell for FR2 RRM multicell testing

The following procedure is used to determine the test frequencies for
Mid-Range adjacent inter-frequency cell used for RRM FR2 NR multi-cell
in NR SA and EN-DC test cases. The reason for using an adjacent
inter-frequency cell to the Mid-range cell for FR2 instead of using Low-
or High- Range test frequencies as used for FR1 is to reduce test system
complexity.

In addition to the definition of parameters in clause C.1 the following
parameters are used to calculate the test frequencies for the Mid
adjacent inter-frequency cell:

  Parameter       Description
  --------------- ------------------------------------------------------
  F~Mid~          Carrier centre frequency (MHz) of the Mid-range cell
  CBW~Mid~        Channel bandwidth (MHz) of the Mid-range cell
  CBW~Adjecent~   Channel bandwidth (MHz) of the adjacent cell

1\. Calculate the Mid-range adjacent cell carrier centre frequencies:

  ------------------------------------------------------------------------------------------------------------ -------------
  **F~MidRangeAdjecentCell~** = **Ceil**((F~Mid~ + (CBW~Mid~ + CBW~Adjecent~)/2) / ΔF~Raster~) \* ΔF~Raster~   C.2.3.3-Eq1
  ------------------------------------------------------------------------------------------------------------ -------------

2\. Calculate SSB and CORESET\#0 parameters as described in clause C.4.

C.2.4 Frequency determination for NR CA and NR DC configurations
----------------------------------------------------------------

### C.2.4.1 Determination of test frequencies for NR Inter-band CA and NR DC

Test frequencies for NR Inter-band CA configurations and NR DC use the
single carrier test frequencies for each of the included NR bands in the
configuration as specified in clause 4.3.1.1.1 for FR1 bands and in
clause 4.3.1.2.1 for FR2 bands.

### C.2.4.2 Determination of test frequencies for NR Intra-band Contiguous CA

#### C.2.4.2.1 General

By default, test frequencies for NR Intra-band Contiguous CA in clause
4.3.1 are specified using the nominal channel spacing between the
carrier components as specified in TS 38.101-1 \[7\] clause 5.4A.1 for
FR1 and TS 38.101-2 \[8\] clause 5.4A.1 for FR2. In addition, some NR
bands may have test frequencies specified based on an adjusted channel
spacing as specified in in TS 38.101-1 \[7\] clause 5.4A.1 for FR1 and
TS 38.101-2 \[8\] clause 5.4A.1 for FR2.

The test frequencies for NR Intra-band Contiguous CA with SCS=15kHz or
SCS=30 kHz for FR1 and with SCS=60 kHZ or SCS=120 kHz for FR2 is
calculated for each CC such that the specific test cases can decide
which CC is used as PCell. This means that all CC test frequencies is
calculated with a CORESET\#0 as specified in clause C.3.2.

The test frequencies for CCs with SCS=60 kHz for FR1 and with SCS=240
kHz for FR2 is calculated without CORESET\#0 as specified in C.3.3. CCs
with SCS=60 kHz for FR1 and with SCS=240 kHz for FR2 can only be used
for NR Intra-band Contiguous CA configurations with mixed numerologies.

Note: For NR Intra-band Contiguous CA configurations for bands where Tx
frequency range is lower than Rx frequency range the RAN4 requirements
for reference sensitivity testing is specified having the PCC frequency
lower than the SCC frequencies such that UL PRB maximise the Tx-Rx
separation. This means that CC1 shall be used as PCell in the reference
test case for bands where Tx frequency range is lower than Rx frequency
range; and highest CC shall be used as PCell in the reference test case
for bands where Tx frequency range is higher than Rx frequency range.

In addition to the definition of parameters in clause C.1 the following
parameters are used to calculate carrier components (CC) test
frequencies for NR Intra-band Contiguous and Non-contiguous CA
configurations:

  Parameter                    Description
  ---------------------------- ---------------------------------------------------------------------
  N~CC~                        Number of CCs in the for NR Intra-band configuration
  CCBW~DL~**(i)**              Channel bandwidth (MHz) of downlink CC(i), where i = 1 to N~CC~
  F~Channel\_Spacing~**(i)**   Channel spacing between CC(i) and CC(i+1), where i = 1 to (N~CC~-1)

#### C.2.4.2.2 Determination of test frequencies for Low-, Mid- and High-Range

Downlink CC(1), lowest frequency CC:

F~DL\_LowRange**\_CC**~**(1)** is rounded up and
F~DL\_HighRange**\_CC**~**(1)** is rounded down to obey to the minimum
guard band according to clause 5.3.3 of TS 38.101-1 \[7\] and TS
38.101-2 \[8\].

  F~DL\_LowRange\_CC~(1) = Ceil((F~DL\_Low~ + CCBW~DL~(1) / 2) / ΔF~Raster~) \* ΔF~Raster~                                                     C.2.4.2.2-Eq1
  -------------------------------------------------------------------------------------------------------------------------------------------- ---------------
  F~DL\_MidRange\_CC~(1) = Round((F~DL\_Low~ + BW~DL~/2 -- ∑~k=1\ to\ (Ncc)~ CCBW~DL~ (k)/2 + CCBW~DL~(1)/2) / ΔF~Raster~) \* ΔF~Raster~       C.2.4.2.2-Eq2
  F~DL\_HighRange\_CC~(1) = Floor((F~DL\_High~ - CCBW~DL~(N~CC~)/2-- ∑~k=1\ to\ (Ncc-1)~ F~Channel\_Spacing~(k)) / ΔF~Raster~) \* ΔF~Raster~   C.2.4.2.2-Eq3

Downlink CC(2) to CC(N~CC~), in increasing frequency order:

  F~DL\_LowRange\_CC~(i) = F~DL\_LowRange\_CC~(i-1) + F~Channel\_Spacing~(i)), i=2 to N~CC~     C.2.4.2.2-Eq4
  --------------------------------------------------------------------------------------------- ---------------
  F~DL\_MidRange\_CC~(i) = F~DL\_MidRange\_CC~(i-1) + F~Channel\_Spacing~(i)), i=2 to N~CC~     C.2.4.2.2-Eq5
  F~DL\_HighRange\_CC~(i) = F~DL\_HighRange\_CC~(i-1) + F~Channel\_Spacing~(i)), i=2 to N~CC~   C.2.4.2.2-Eq6

Uplink CC(i), i=1 to N~CC~:

  **F~UL\_LowRange\_CC~(i)** = F~DL\_LowRange\_CC~**(i)** - F~Tx-Rx\_separation~         C.2.4.2.2-Eq7
  -------------------------------------------------------------------------------------- ---------------
  **F~UL\_MidRange\_CC~(i)** = F~DL\_MidRange**\_CC**~**(i)** - F~Tx-Rx\_separation~     C.2.4.2.2-Eq8
  **F~UL\_HighRange\_CC~(i)** = F~DL\_HighRange**\_CC**~**(i)** - F~Tx-Rx\_separation~   C.2.4.2.2-Eq9

### C.2.4.2A Determination of test frequencies for FR1 NR Intra-band Contiguous CA without UL CA for bands with uplink bandwidth less than downlink bandwidth

#### C.2.4.2A.1 General

By default, test frequencies for FR1 NR Intra-band Contiguous CA for
bands with uplink bandwidth less than downlink bandwidth in clause 4.3.1
(e.g. n66 and n70) are specified with CC1 used as PCC and all additional
CCs are specified as SCCs without UL to enable the SCCs for High range
to extend into the upper DL BW beyond the UL BW. The nominal channel
spacing between the carrier components is calculated as specified in TS
38.101-1 \[7\] clause 5.4A.1.

In addition to the definition of parameters in clause C.1 the defintion
of parameters N~CC~, CCBW~DL~ and F~Channel\_Spacing~ in clause
C.2.4.2.1, and ΔF~TX-RX~ in clause C.2.3.1 are used to calculate the
test frequencies.

#### C.2.4.2A.2 Determination of test frequencies for Low-, Mid- and High-Range

1\. Calculate UL carrier centre frequencies for Low and High ranges:

  **F~UL\_LowRange~** = **Ceil**((F~UL\_Low~ + CBW~UL~/2) / ΔF~Raster~) \* ΔF~Raster~                     C.2.4.2A.2-Eq1
  ------------------------------------------------------------------------------------------------------- ----------------
  **F~UL\_HighRange~** = **Floor**((F~UL\_Low~ + BW~UL\_Band~ -- CBW~UL~/2) / ΔF~Raster~) \* ΔF~Raster~   C.2.4.2A.2-Eq2

2\. Calculate the DL CC(1) carrier centre frequencies from the UL
frequencies in step 1 for Low and High ranges:

  **ΔF~TX-RX~** = \|(CBW~DL~(1) -- CBW~UL~)/2\|                                            C.2.4.2A.2-Eq3
  ---------------------------------------------------------------------------------------- ----------------
  **s** = +1 if F~UL\_Low~ \<= F~DL\_Low~ else -1                                          C.2.4.2A.2-Eq4
  **F~DL\_LowRange\_CC~(1)** = F~UL\_LowRange~ + s\*(F~Tx-Rx\_separation~ + ΔF~Tx-Rx~)     C.2.4.2A.2-Eq5
  **F~DL\_HighRange\_CC~(1)** = F~UL\_HighRange~ + s\*(F~Tx-Rx\_separation~ + ΔF~Tx-Rx~)   C.2.4.2A.2-Eq6

3\. Check that DL aggregated CBW for the High range fits into the DL
bandwidth.

  --------------------------------------------------------------------------------------------------------------------------- ----------------
  **F~DL\_HighRange\_max~** = Floor((F~DL\_HighRange\_CC~(1) + ∑~k=1\ to\ Ncc-1~ F~Channel\_Spacing~(k)+ CCBW~DL~(N~CC~)/2)   C.2.4.2A.2-Eq7
  --------------------------------------------------------------------------------------------------------------------------- ----------------

If F~DL\_HighRange\_max~ is less or equal to F~DL\_High~ then goto step
4 else modify F~DL\_HighRange\_CC1~ such that the full aggregated CBW is
located at the DL bandwidth high edge and recalculate
**F~UL\_HighRange~**.

  **F~DL\_HighRange\_CC~(1)** = F~DL\_High~ - CCBW~DL~(N~CC~)/2 - **∑~k=1\ to\ (Ncc-2)~ F~Channel\_Spacing~(k)**   C.2.4.2A.2-Eq8
  ---------------------------------------------------------------------------------------------------------------- ----------------
  **F~UL\_HighRange\ ~**= **F~DL\_HighRange\_CC~(1)** -- s\*(F~Tx-Rx\_separation~ + ΔF~Tx-Rx~)                     C.2.4.2A.2-Eq9

4\. Calculate the F~UL\_MidRange~ and F~DL\_MidRange\_CC(1):~

  **F~DL\_MidRange\_CC~**(1) = Round((F~DL\_LowRange\_CC~(1) + F~DL\_HighRange\_CC~(1))/2) / ΔF~Raster~) \* ΔF~Raster~   C.2.4.2A.2-Eq10
  ---------------------------------------------------------------------------------------------------------------------- -----------------
  **F~UL\_MidRange\ ~**= **FU~DL\_MidRange\_CC~(1)** -- s\*(F~Tx-Rx\_separation~ + ΔF~Tx-Rx~)                            C.2.4.2A.2-Eq11

5\. Calulate DL CC(2) to CC(N~CC~), in increasing frequency order:

  F~DL\_LowRange\_CC~(i) = F~DL\_LowRange\_CC~(i-1) + F~Channel\_Spacing~(i), i=2 to N~CC~     C.2.4.2A.2-Eq12
  -------------------------------------------------------------------------------------------- -----------------
  F~DL\_MidRange\_CC~(i) = F~DL\_MidRange\_CC~(i-1) + F~Channel\_Spacing~(i), i=2 to N~CC~     C.2.4.2A.2-Eq13
  F~DL\_HighRange\_CC~(i) = F~DL\_HighRange\_CC~(i-1) + F~Channel\_Spacing~(i), i=2 to N~CC~   C.2.4.2A.2-Eq14

### C.2.4.3 Determination of test frequencies for NR Intra-band Non-Contiguous CA

#### C.2.4.3.1 General

The default test frequencies in clause 4.3.1 for NR Intra-band
Non-Contiguous CA are based on maximum Wgap between the carrier
components of the different bands taking the UE capability of maximum
supported frequency separation between the lower edge of lowest
component carrier and upper edge of highest component carrier for UL for
FR1, and UL and DL for FR2.

Test frequencies with Wgap different from maximum Wgap are specified in
the specific test cases using them.

In addition to the definition of parameters in clause C.1 the following
parameters are used to calculate carrier components (CC) test
frequencies for NR Intra-band Contiguous and Non-contiguous CA
configurations:

  Parameter          Description
  ------------------ ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
  N~SB~              Number of sub-block in the for NR Intra-band non-contiguous configuration
  SBCBW~DL~**(i)**   Downlink channel bandwidth (MHz) of sub-block SB(i), where i = 1 to N~SB~
  maxFsBW            Maximum frequency separation bandwidth between the lower edge of lowest component carrier and upper edge of highest component carrier.
  maxWgap            maxWgap is the maximum separation in MHz between each sub-block in the NR Intra-band non-contiguous configuration within maxFsBW for a given sub-block combination.

#### C.2.4.3.1A Selection of maximum frequency separation for FR1

Select the maxFsBW dependent on the type of configuration and aggregated
CBW for the sub-block combination in Table C.2.4.3.1A-1:

Table C.2.4.3.1A-1: Selecting maxFsBW for FR1

  Type of configuration   Aggregated CBW             maxFsBW
  ----------------------- -------------------------- --------------------------------
  Without UL CA           All                        Full NR bandwidth
  With UL CA              \<100 MHz                  Min(Full NR bandwidth,100 MHz)
                          \>=100 MHz and \<200 MHz   Min(Full NR bandwidth,200 MHz)
                          \>=200 MHz and \<600 MHz   Min(Full NR bandwidth,600 MHz=
                          =600 MHz                   Full NR bandwidth

#### C.2.4.3.1B Selection of maximum frequency separation for FR2

Select the maxFsBW dependent on the type of configuration and aggregated
CBW for the sub-block combination in Table C.2.4.3.1B-1:

Table C.2.4.3.1B-1: Selecting maxFsBW for FR2

+----------------------------+----------------------------+----------+
| Type of configuration      | Aggregated CBW             | maxFsBW  |
|                            |                            |          |
|                            |                            | (Note 1) |
+============================+============================+==========+
| With non-contiguous UL CA  | \<400 MHz                  | 400 MHz  |
+----------------------------+----------------------------+----------+
|                            | \>=400 MHz and \<600 MHz   | 600 MHz  |
+----------------------------+----------------------------+----------+
|                            | \>=600 MHz and \<800 MHz   | 800 MHz  |
+----------------------------+----------------------------+----------+
|                            | \>=800 MHz and \<1000 MHz  | 1000 MHz |
+----------------------------+----------------------------+----------+
|                            | \>=1000 MHz and \<1200 MHz | 1200 MHz |
+----------------------------+----------------------------+----------+
|                            | \>=1200 MHz and \<1400 MHz | 1400 MHz |
+----------------------------+----------------------------+----------+
|                            | \>=1400 MHz                | N/A      |
+----------------------------+----------------------------+----------+
| Without non-contiguous UL  | \<400 MHz                  | 400 MHz  |
| CA                         |                            |          |
+----------------------------+----------------------------+----------+
|                            | \>=400 MHz and \<600 MHz   | 600 MHz  |
+----------------------------+----------------------------+----------+
|                            | \>=600 MHz and \<800 MHz   | 800 MHz  |
+----------------------------+----------------------------+----------+
|                            | \>=800 MHz and \<1000 MHz  | 1000 MHz |
+----------------------------+----------------------------+----------+
|                            | \>=1000 MHz and \<1200 MHz | 1200 MHz |
+----------------------------+----------------------------+----------+
|                            | \>=1200 MHz and \<1400 MHz | 1400 MHz |
+----------------------------+----------------------------+----------+
|                            | \>=1400 MHz and \<1600 MHz | 1600 MHz |
+----------------------------+----------------------------+----------+
|                            | \>=1600 MHz and \<1800 MHz | 1800 MHz |
+----------------------------+----------------------------+----------+
|                            | \>=1800 MHz and \<2000 MHz | 2000 MHz |
+----------------------------+----------------------------+----------+
|                            | \>=2000 MHz and \<2200 MHz | 2200 MHz |
+----------------------------+----------------------------+----------+
|                            | \>=2200 MHz and \<2400 MHz | 2400 MHz |
+----------------------------+----------------------------+----------+
| Note 1: For FR2 intra-band |                            |          |
| non-contiguous CA          |                            |          |
| configurations with        |                            |          |
| non-contiguous UL CA the   |                            |          |
| selected value of maxFsBW  |                            |          |
| is based on applicable     |                            |          |
| frequency separation       |                            |          |
| classes for UL             |                            |          |
| non-contiguous operation   |                            |          |
| in TS 38.101-2 \[8\],Table |                            |          |
| 5.3A.4-2. For FR2          |                            |          |
| intra-band non-contiguous  |                            |          |
| CA configurations without  |                            |          |
| non-contiguous UL CA the   |                            |          |
| selected value of maxFsBW  |                            |          |
| is based on applicable     |                            |          |
| frequency separation       |                            |          |
| classes for DL             |                            |          |
| non-contiguous operation   |                            |          |
| in TS 38.101-2 \[8\],Table |                            |          |
| 5.3A.4-2.                  |                            |          |
+----------------------------+----------------------------+----------+

#### C.2.4.3.2 Determination of test frequencies for a sub-block combination

Editor\'s note: The number of test points for FR2 intra-band
non-contiguous CA configurations is under investigation, e.g. "Low" and
"High", or "Mid".

1\. Calculate the maxWgap value between sub-blocks for the sub-block
combination:

  ---------------------------------------------------------------------- ---------------
  maxWgap = (maxFsBW -- **∑~k=1\ to\ NSB\ ~**SBCBW~DL~(k)) / (N~SB~-1)   C.2.4.3.3-Eq1
  ---------------------------------------------------------------------- ---------------

2\. Calculate test frequencies for all sub-blocks in the sub-block
combination:

If the maxFsBW is smaller than the full bandwidth of the NR band then
calculate test frequencies for both Low and High range. Else only for
the Low range.

For Low range the test frequencies are calculated such that the lower
edge of the lowest component carrier of the lowest frequency sub-block
is located at the lower edge of the NR bandwidth. The sub-blocks are
separated by the calculated maxWgap in step 1.

For High range the test frequencies are calculated such that the upper
edge of the highest component carrier of the highest frequency sub-block
is located at the upper edge frequency of the NR bandwidth. The
sub-blocks are separated by the calculated maxWgap in step 1.

Within each sub-block the test frequencies and parameters of the
sub-block are calculated based on the location of the sub-block and the
relevant principles in clause C.2, C3 and C4 for the type of component
carriers in the sub-block.

The test frequencies for CCs with SCS=60 kHz for FR1 and with SCS=240
kHz for FR2 is calculated without CORESET\#0 as specified in C.3.3. CCs
with SCS=60 kHz for FR1 and with SCS=240 kHz for FR2 can only be used
for NR Intra-band Non-Contiguous CA configurations with mixed
numerologies.

#### C.2.4.3.3 Void

#### C.2.4.3.4 Determination of CBW combinations to add in initial test frequency tables

There is a need, for some bands, to limit the number of initial CBW
combinations in the tables for the test frequencies for UL CA, clause
4.3.1.1.5: NR intra-band non-contiguous CA configurations in FR1 and
clause clause 4.3.1.2.4: NR intra-band non-contiguous CA configurations
in FR2. If the total number of CBW combination exceeds a value of 35
combinations, the number of combinations should be reduced according to
the steps described in this clause. The intention is to include the CBW
combinations that is the most likely to be needed for testing.

The determination of which CBW combinations to add in the initial
tables, is based on two statements stated in test cases:

1\. Initial conditions for test: Lowest NRB\_agg, Highest NRB\_agg.

2\. If the UE supports multiple CC Combinations in the CA Configuration
with the same NRB\_agg, only the combination with the highest NRB\_PCC
is tested.

The determination of initial CBW combinations to add in new tables for
the test frequencies shall follow below steps:

1\. One, and only one, combination for each possible value of aggregated
CBW for a specific BCS. The maximum aggregated BW in table will be
limited to Maximum supported Aggregated CBW as stated in 38.521-1
\[14\], Table 5.5A.2-1. The aggregated BW of the combinations will be
restricted to even 10 MHZ values.

2\. Each combination according to step 1 above shall be configured to
use the highest NRB\_PCC (CBW) possible, to comply with statement 2
above.

C.2.5 Frequency determination for supplemental uplink
-----------------------------------------------------

### C.2.5.1 General

The following procedure is used to calculate test frequencies for NR
supplemental uplink as described below, where CBW~UL~ refers to the
carrier's UL channel bandwidths and BW~UL~ refers to the band's total UL
bandwidths.

### C.2.5.2 Determination of Low-, Mid- and High-Range for supplemental uplink bands

The following procedure is used to determine the uplink carrier centre
frequencies for Low-, Mid- and High-Range for supplemental uplink bands.

  **F~UL\_LowRange~** = **Ceil**((F~UL\_Low~ + CBW~UL~/2) / ΔF~Raster~) \* ΔF~Raster~                     C.2.5.2-Eq1
  ------------------------------------------------------------------------------------------------------- -------------
  **F~UL\_MidRange~** = **Round**((F~UL\_Low~ + BW~UL\_Band~/2) / ΔF~Raster~) \* ΔF~Raster~               C.2.5.2-Eq2
  **F~UL\_HighRange~** = **Floor**((F~UL\_Low~ + BW~UL\_Band~ -- CBW~UL~/2) / ΔF~Raster~) \* ΔF~Raster~   C.2.5.2-Eq3

C.2.6 Frequency determination for EN-DC configurations
------------------------------------------------------

### C.2.6.1 Determination of test frequencies for EN-DC Inter-band 

Test frequencies for EN-DC inter-band configurations use the Low and
High ranges test frequencies for each of the included single carrier
E-UTRA and NR bands, and E-UTRA and NR CA configurations in the
configuration as specified E-UTRA in TS 36.508 \[2\], clause 4.3.1 and
for NR in clause 4.3.1.1 for FR1 bands and in clause 4.3.1.2 for FR2
bands.

### C.2.6.2 Determination of test frequencies for EN\_DC Intra-band Contiguous CA

#### C.2.6.2.1 General

By default, test frequencies for EN-DC Intra-band Contiguous CA in
clause 4.3.1 are specified using the nominal channel spacing between the
E-UTRA and NR carrier components as specified in TS 38.101-3 \[9\],
clause 5.4B.1.

The test frequencies for EN\_DC Intra-band Contiguous CA is calculated
for Low and High ranges for the following two cases:

\- with NR CC at the band edge; and

\- with E-UTRA CC at the band edge.

In addition to the definition of parameters in clause C.1 the following
parameters are used to calculate carrier components (CC) test
frequencies for EN\_DC Intra-band Contiguous:

+--------------------------------+------------------------------------+
| Parameter                      | Description                        |
+================================+====================================+
| N~NR\_CC~                      | Number of NR CCs in the EN-DC      |
|                                | Intra-band configuration           |
+--------------------------------+------------------------------------+
| N~EUTRA\_CC~                   | Number of E-UTRA CCs in the EN-DC  |
|                                | Intra-band configuration           |
+--------------------------------+------------------------------------+
| CCBW~NR\_DL~(i)                | Channel bandwidth (MHz) of         |
|                                | downlink NR CC(i), where i = 1 to  |
|                                | N~NR\_CC~                          |
+--------------------------------+------------------------------------+
| CCBW~EUTRA\_DL~(m)             | Channel bandwidth (MHz) of         |
|                                | downlink E-UTRA CC(m), where m = 1 |
|                                | to N~EUTRA\_CC~                    |
+--------------------------------+------------------------------------+
| F~NR\_EUTRA\_Channel\_Spacing~ | Nominal channel spacing between    |
|                                | adjacent NR and E-UTRA CCs as      |
|                                | defined in TS 38.101-3 \[9\],      |
|                                | 5.4B.1.                            |
+--------------------------------+------------------------------------+
| F~EUTRA\_Channel\_Spacing~(m)  | Nominal channel spacing between    |
|                                | E-UTRA adjacent contiguous CC(m)   |
|                                | and CC(m+1), where m = 1 to        |
|                                | (N~EUTRA\_CC~-1) as defined in TS  |
|                                | 36.101 \[48\], 5.7.1A.             |
+--------------------------------+------------------------------------+
| F~NR\_Channel\_Spacing~(i)     | Nominal channel spacing between NR |
|                                | adjacent contiguous CC(i) and      |
|                                | CC(i+1), where i = 1 to            |
|                                | (N~NR\_CC~-1) as defined in TS     |
|                                | 38.101-1 \[7\] clause 5.4A.1 for   |
|                                | FR1 and TS 38.101-2 \[8\] clause   |
|                                | 5.4A.1 for FR2                     |
+--------------------------------+------------------------------------+
| LCMΔF~Raster~                  | Least Common Multiple of NR        |
|                                | ΔF~Raster~ and E-UTRA ΔF~Raster~   |
|                                | equals to                          |
|                                |                                    |
|                                | 300 kHz for E-UTRA ΔF~Raster~ =    |
|                                | 100 kHz and NR ΔF~Raster~ = 15kHz, |
|                                | 30kHz and 60kHz.                   |
+--------------------------------+------------------------------------+

#### C.2.6.2.2 Determination of test frequencies for Low-, Mid- and High-Range with NR at band edges

Downlink NR CC(1), lowest frequency CC:

F~NR\_DL\_LowRange**\_CC**~**(1)** is rounded up and
F~NR\_DL\_HighRange**\_CC**~**(1)** is rounded down to obey to the
minimum guard band according to clause 5.3.3 of TS 38.101-1 \[7\] and TS
38.101-2 \[8\].

The NR test frequencies are calculated such that both the NR CC and
E-UTRA CC adjacent to each other are located at the NR and E-UTRA
frequency raster respectively.

+-----------------------------------------------------+---------------+
| F~NR\_DL\_LowRange\_CC~(1) = Ceil((F~DL\_Low~ +     | C.2.6.2.2-Eq1 |
| CCBW~NR\_DL~(1) / 2 +                               |               |
| F~NR\_EUTRA\_Channel\_Spacing~) / LCMΔF~Raster~) \* |               |
| LCMΔF~Raster~ - F~NR\_EUTRA\_Channel\_Spacing~,     |               |
| where                                               |               |
|                                                     |               |
| F~NR\_EUTRA\_Channel\_Spacing~ =                    |               |
| Round((CCBW~EUTRA\_DL~(1) +                         |               |
| CCBW~NR\_DL~(N~NR\_CC~))/(2\*ΔF~Raster~))\*         |               |
| ΔF~Raster~                                          |               |
+=====================================================+===============+
| F~NR\_DL\_MidRange\_CC~(1) = Round((F~DL\_Low~ +    | C.2.6.2.2-Eq2 |
| BW~DL~/2 -- (∑~i=1\ to~ N~NR\_CC~ CCBW~NR\_DL~ (i)  |               |
| + ∑~m=1\ to~ N~EUTRA\_CC~ CCBW~EUTRA\_DL~(m))/2 +   |               |
| CCBW~NR\_DL~(1))/2) +                               |               |
| F~NR\_EUTRA\_Channel\_Spacing~ / LCMΔF~Raster~) \*  |               |
| LCMΔF~Raster~ - F~NR\_EUTRA\_Channel\_Spacing~,     |               |
| where                                               |               |
|                                                     |               |
| F~NR\_EUTRA\_Channel\_Spacing~ =                    |               |
| Round((CCBW~EUTRA\_DL~(1) +                         |               |
| CCBW~NR\_DL~(N~NR\_CC~))/(2\*ΔF~Raster~))\*         |               |
| ΔF~Raster~                                          |               |
+-----------------------------------------------------+---------------+
| F~NR\_DL\_HighRange\_CC~(1) = Floor((F~DL\_High~ -  | C.2.6.2.2-Eq3 |
| CCBW~NR\_DL~(N~NR\_CC~)/2-- ∑~i=1\ to\ (NNR\_CC-1)~ |               |
| F~NR\_Channel\_Spacing~(i) -                        |               |
| F~NR\_EUTRA\_Channel\_Spacing~) / LCMΔF~Raster~) \* |               |
| LCMΔF~Raster~ + F~NR\_EUTRA\_Channel\_Spacing~,     |               |
| where                                               |               |
|                                                     |               |
| F~NR\_EUTRA\_Channel\_Spacing~ =                    |               |
| Round((CCBW~EUTRA\_DL~(N~EUTRA\_CC~) +              |               |
| CCBW~NR\_DL~(1))/(2\*ΔF~Raster~))\* ΔF~Raster~      |               |
+-----------------------------------------------------+---------------+

Downlink NR CC(2) to CC(N~NR\_CC~), in increasing frequency order:

  F~NR\_DL\_LowRange\_CC~(k) = F~DL\_LowRange\_CC~(k-1) + ∑F~NR\_Channel\_Spacing~(k), k=2 to N~DL\_CC~     C.2.6.2.2-Eq4
  --------------------------------------------------------------------------------------------------------- ---------------
  F~NR\_DL\_MidRange\_CC~(k) = F~DL\_MidRange\_CC~(k-1) + ∑F~NR\_Channel\_Spacing~(k), k=2 to N~DL\_CC~     C.2.6.2.2-Eq5
  F~NR\_DL\_HighRange\_CC~(k) = F~DL\_HighRange\_CC~(k-1) + ∑F~NR\_Channel\_Spacing~(k), k=2 to N~DL\_CC~   C.2.6.2.2-Eq6

Uplink NR CC(k), k=1 to N~CC~:

  F~NR\_UL\_LowRange\_CC~(k) = F~NR\_DL\_LowRange\_CC~(k) - F~Tx-Rx\_separation~     C.2**.**6**.**2.2-Eq7
  ---------------------------------------------------------------------------------- -----------------------
  F~NR\_UL\_MidRange\_CC~(k) = F~NR\_DL\_MidRange\_CC~(k) - F~Tx-Rx\_separation~     C.2**.**6**.**2.2-Eq8
  F~NR\_UL\_HighRange\_CC~(k) = F~NR\_DL\_HighRange\_CC~(k) - F~Tx-Rx\_separation~   C.2**.**6**.**2.2-Eq9

Downlink E-UTRA CC(1), lowest frequency CC:

ΔF~NR\_EUTRA\_Channel\_Spacing~ is selected in each formula
C.2.6.2.2-Eq10, C.2.6.2.2-Eq11 and C.2.6.2.2-Eq12 selected such that
F~EUTRA\_DL\_LowRange\_CC~(1), F~EUTRA\_DL\_MidRange\_CC~(1) and
F~EUTRA\_DL\_HighRange\_CC~(1) are located on the E-UTRA band frequency
raster.

  F~EUTRA\_DL\_LowRange\_CC~(1) = F~NR\_DL\_LowRange\_CC~(N~DL\_CC~) + F~NR\_EUTRA\_Channel\_Spacing~                                                                                                                     C.2.6.2.2-Eq10
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------
  F~EUTRA\_DL\_MidRange\_CC~(1) = F~NR\_DL\_MidRange\_CC~(N~DL\_CC~) + F~NR\_EUTRA\_Channel\_Spacing~                                                                                                                     C.2.6.2.2-Eq11
  F~EUTRA\_DL\_HighRange\_CC~(1) = F~NR\_DL\_HighRange\_CC~(N~DL\_CC~) - ∑~i=1\ to\ (NNR\_CC-1)~ F~NR\_Channel\_Spacing~(i) - F~NR\_EUTRA\_Channel\_Spacing~ - ∑~i=1\ to\ (NEUTRA\_CC-1)~ F~EUTRA\_Channel\_Spacing~(i)   C.2.6.2.2-Eq12

Downlink E-UTRA CC(2) to CC(N~EUTRA\_CC~), in increasing frequency
order:

  F~EUTRA\_DL\_LowRange\_CC~(k) = F~EUTRA\_DL\_LowRange\_CC~(k-1) + ∑F~EUTRA\_Channel\_Spacing~(k), k=2 to N~EUTRA\_CC~     C.2.6.2.2-Eq13
  ------------------------------------------------------------------------------------------------------------------------- ----------------
  F~EUTRA\_DL\_MidRange\_CC~(k) = F~EUTRA\_DL\_MidRange\_CC~(k-1) + ∑F~EUTRA\_Channel\_Spacing~(k), k=2 to N~EUTRA\_CC~     C.2.6.2.2-Eq14
  F~EUTRA\_DL\_HighRange\_CC~(k) = F~EUTRA\_DL\_HighRange\_CC~(k-1) + ∑F~EUTRA\_Channel\_Spacing~(k), k=2 to N~EUTRA\_CC~   C.2.6.2.2-Eq15

Uplink E-UTRA CC(k), k=1 to N~EUTRA\_CC~:

  F~EUTRA\_UL\_LowRange\_CC~(k) = F~EUTRA\_DL\_LowRange\_CC~(k) - F~Tx-Rx\_separation~     C.2**.**6**.**2.2-Eq16
  ---------------------------------------------------------------------------------------- ------------------------
  F~EUTRA\_UL\_MidRange\_CC~(k) = F~EUTRA\_DL\_MidRange\_CC~(k) - F~Tx-Rx\_separation~     C.2**.**6**.**2.2-Eq17
  F~EUTRA\_UL\_HighRange\_CC~(k) = F~EUTRA\_DL\_HighRange\_CC~(k) - F~Tx-Rx\_separation~   C.2**.**6**.**2.2-Eq18

#### C.2.6.2.3 Determination of test frequencies for Low-, Mid- and High-Range with E-UTRA at band edges

To get the NR carrier on the synchcronisation raster the calculations of
the E-UTRA carrier components needs to be based on the location of the
NR carrier.

Downlink NR CC(1), lowest frequency CC:

F~NR\_DL\_LowRange**\_CC**~**(1)** is rounded up and
F~NR\_DL\_HighRange**\_CC**~**(1)** is rounded down to obey to the
minimum guard band according to clause 5.3.3 of TS 38.101-1 \[7\] and TS
38.101-2 \[8\].

+-----------------------------------------------------+---------------+
| F~NR\_DL\_LowRange\_CC~(1) = Ceil((F~DL\_Low~ +     | C.2.6.2.3-Eq1 |
| ∑~m=1\ to~ N~EUTRA\_CC~                             |               |
| CCBW~EUTRA\_DL~(m)+CCBW~NR\_DL~(1) / 2 -            |               |
| F~NR\_EUTRA\_Channel\_Spacing~) / LCMΔF~Raster~) \* |               |
| LCMΔF~Raster\ +~ F~NR\_EUTRA\_Channel\_Spacing~,    |               |
| where                                               |               |
|                                                     |               |
| F~NR\_EUTRA\_Channel\_Spacing~ =                    |               |
| Round((CCBW~EUTRA\_DL~(N~EUTRA\_CC~) +              |               |
| CCBW~NR\_DL~(1))/(2\*ΔF~Raster~))\* ΔF~Raster~      |               |
+=====================================================+===============+
| F~NR\_DL\_MidRange\_CC~(1) = same formula as        | C.2.6.2.3-Eq2 |
| C.2.6.2.2-Eq2                                       |               |
+-----------------------------------------------------+---------------+
| F~NR\_DL\_HighRange\_CC~(1) = Floor((F~DL\_High~ -- | C.2.6.2.3-Eq3 |
| (∑~m=1\ to~ N~EUTRA\_CC~ CCBW~EUTRA\_DL~(m) +       |               |
| ∑~i=1\ to~ N~NR\_CC~ CCBW~NR\_DL~(i))               |               |
| +CCBW~NR\_DL~(1) / 2 +                              |               |
| F~NR\_EUTRA\_Channel\_Spacing~) / LCMΔF~Raster~) \* |               |
| LCMΔF~Raster~ - F~NR\_EUTRA\_Channel\_Spacing~,     |               |
| where                                               |               |
|                                                     |               |
| F~NR\_EUTRA\_Channel\_Spacing~ =                    |               |
| Round((CCBW~EUTRA\_DL~(1) +                         |               |
| CCBW~NR\_DL~(N~NR\_CC~))/(2\*ΔF~Raster~))\*         |               |
| ΔF~Raster~                                          |               |
+-----------------------------------------------------+---------------+

Downlink NR CC(2) to CC(N~NR\_CC~), in increasing frequency order:

  F~NR\_DL\_LowRange\_CC~(k) = same formula as C.2.6.2.2-Eq4    C.2.6.2.3-Eq4
  ------------------------------------------------------------- ---------------
  F~NR\_DL\_MidRange\_CC~(k) = same formula as C.2.6.2.2-Eq5    C.2.6.2.3-Eq5
  F~NR\_DL\_HighRange\_CC~(k) = same formula as C.2.6.2.2-Eq6   C.2.6.2.3-Eq6

Uplink NR CC(k), k=1 to N~CC~:

  **F~NR\_UL\_LowRange\_CC~(k)** = same formula as C.2.6.2.2-Eq7    C.2**.**6**.**2.3-Eq7
  ----------------------------------------------------------------- -----------------------
  **F~NR\_UL\_MidRange\_CC~(k)** = same formula as C.2.6.2.2-Eq8    C.2**.**6**.**2.3-Eq8
  **F~NR\_UL\_HighRange\_CC~(k)** = same formula as C.2.6.2.2-Eq9   C.2**.**6**.**2.3-Eq9

Downlink E-UTRA CC(1), lowest frequency CC:

  F~EUTRA\_DL\_LowRange\_CC~(1) = F~NR\_DL\_LowRange\_CC~(1) - F~NR\_EUTRA\_Channel\_Spacing~ - ∑~m=1\ to\ (NEUTRA\_CC\ -\ 1)~ F~EUTRA\_Channel\_Spacing~(m)                                                              C.2.6.2.3-Eq10
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------
  F~EUTRA\_DL\_MidRange\_CC~(1) = same formula as C.2.6.2.2-Eq11                                                                                                                                                          C.2.6.2.3-Eq11
  F~EUTRA\_DL\_HighRange\_CC~(1) = F~NR\_DL\_HighRange\_CC~(N~DL\_CC~) + ∑~i=1\ to\ (NNR\_CC-1)~ F~NR\_Channel\_Spacing~(i) + F~NR\_EUTRA\_Channel\_Spacing~ + ∑~i=1\ to\ (NEUTRA\_CC-1)~ F~EUTRA\_Channel\_Spacing~(i)   C.2.6.2.3-Eq12

Downlink E-UTRA CC(2) to CC(N~EUTRA\_CC~), in increasing frequency
order:

  F~EUTRA\_DL\_LowRange\_CC~(k) = same formula as C.2.6.2.2-Eq13    C.2.6.2.3-Eq13
  ----------------------------------------------------------------- ----------------
  F~EUTRA\_DL\_MidRange\_CC~(k) = same formula as C.2.6.2.2-Eq14    C.2.6.2.3-Eq14
  F~EUTRA\_DL\_HighRange\_CC~(k) = same formula as C.2.6.2.2-Eq15   C.2.6.2.3-Eq15

Uplink E-UTRA CC(k), k=1 to N~EUTRA\_CC~:

  **F~EUTRA\_UL\_LowRange\_CC~(k)** = same formula as C.2.6.2.2-Eq16            C.2**.**6**.**2.3-Eq16
  ----------------------------------------------------------------------------- ------------------------
  **F~EUTRA\_UL\_MidRange\_CC~(k)** = same formula as C.2.6.2.2-Eq17            C.2**.**6**.**2.3-Eq17
  **F~EUTRA\_UL\_HighRange\_CC~(k)** = **same formula as C.2.**6**.2.2-Eq18**   C.2**.**6**.**2.3-Eq18

### C.2.6.3 Determination of test frequencies for EN-DC Intra-band non-contiguous

Test frequencies for EN-DC Intra-band non-contiguous configurations use
the Low and High ranges test frequencies for each of the included single
carrier E-UTRA and NR bands, and E-UTRA and NR CA configurations in the
configuration as specified E-UTRA in TS 36.508 \[2\], clause 4.3.1 and
for NR in clause 4.3.1.1 for FR1 bands and in clause 4.3.1.2 for FR2
bands.

The following cases of test frequencies are specified for relevant
E-UTRA and NR CBW combinations, and NR SCS:

\- Low with maxWgap (NR - E-UTRA): NR Low range and E-UTRA High range

\- High with maxWgap (E-UTRA - NR): NR High range and E-UTRA Low range

C.3 Determination of SSB and CORESET\#0
=======================================

C.3.1 General
-------------

The requirements to be met and the principles used for determining the
SSB and CORESET\#0 for a PCell are:

1\. The complete SSB and CORESET\#0 shall be within the carrier's
channel bandwidth.

2\. The SSB centre frequency (SSref) shall be on the synchronisation
raster.

3\. The SSB shall be kept as close as possible to the carrier's lower
edge centre frequency.

4\. CORESET\#0 configuration is selected using lowest number of RBs and
symbols in applicable table in TS 38.213 \[22\], clause 13.

5\. The first SSB subcarrier shall be aligned with the defined resource
grid given by SCS indicated by *subCarrierSpacingCommon* in the MIB.

C.3.2 Determination of SSB, CORESET\#0 and signalling parameters for a PCell
----------------------------------------------------------------------------

Calculation of SSB and CORESET\#0 parameters is limited to FR1 carriers
with SCS=15 kHz or SCS=30 kHz, and to FR2 carriers with SCS=60 kHz or
SCS=120 kHz. CORESET\#0 is required for a carrier to be used as a PCell.

The following procedure is used to determine an SSB on the
synchronisation raster (GSCN) and a CORESET\#0 configuration (k~SSB,~
Offset~RBs~ and *OffsetToPointA*) as close as possible to the carrier's
lower edge. See figure C1-1 and clause C.1 for definition of parameters
referenced in the procedure.

1\. Determine SSB and CORESET\#0:

1a. Calculate the lower of F~SSref~, F~SSref\_Min~, correspondent to SSB
lowest subcarrier being at the same frequency as the carrier's lowest
subcarrier; and the higher limit of F~SSref~, F~SSref\_Max~,
correspondent to SSB highest subcarrier being at the same frequency as
the carrier's highest subcarrier F~SSref\_Max~

  F~carrierLow~ = see formula for F~carrierLow~ in Table C.1-1
  ----------------------------------------------------------------------------
  F~SSref\_Min~ = F~carrierLow~ + CRB~size~ \* Offset~RBs,min~ + BW~SSB~ / 2
  F~SSref\_Max~ = F~carrierLow~ + ΔF~carrierBandwidth~ - BW~SSB~ / 2

1b. Calculate GSCN~MIN~ correspondent to F~SSref\_Min~ in accordance to
TS 38.101-1 \[7\], clause 5.4.3.1 for FR1 and TS 38.101-2 \[7\], clause
5.4.3.1 for FR2 and select the closest valid GSCN value with GSCN \>=
GSCN~MIN~ for the carrier in according to the carrier's synchronisation
raster as specified in clause 5.4.3.3 in TS 38.101-1 \[7\] and TS
38.101-2 \[8\].

1c. Calculate the F~SSref~ for the selected GSCN value in step 1b in
accordance to TS 38.101-1 \[7\], clause 5.4.3.1 for FR1 and TS 38.101-2
\[7\], clause 5.4.3.1 for FR2.

1d. Calculate the frequency F~offsetToPointA~, which is the lowest
subcarrier of the lowest resource block with the subcarrier spacing
being a multiple of resource blocks expressed in terms of common PRB
size and overlaps with the SS/PBCH block subcarrier 0 of the first
resource block of the SS/PBCH block, F~SSBlow~ (TS 38.211 \[3\], clause
7.4.3.1):

  F~SSBlow~ = F~SSref~ - BW~SSB~ / 2
  -----------------------------------------------------------------------------------------------------------------
  F~offsetToPointA~ = CRB~size~ \* Floor(Round((F~SSBlow~ - F~carrierLow~) / CRB~size~),5) + F~carrierLow~ Note 1

Note 1: The "Round" operation is needed to avoid that platforms using
"float" representation will give erroneous results. Hence, the need for
the "Round" operation is platform dependant. The "Round" operation is to
be done to 5 decimals. It is needed to avoid that a calculated value of
for example 5.9999999999 is Floored to the value of 5.

1e. Calculate the maximum Offset~RBs~ value with F~CORESET0Low~ \>=
F~carrierLow~:

  ----------------------------------------------------------------------------------
  Max\_Offset~RBs~ = Round((F~offsetToPointA~ - F~carrierLow~) / CRB~size~) Note 2
  ----------------------------------------------------------------------------------

Note 2: The "Round" operation is needed to avoid that platforms using
"float" representation will give erroneous results. Hence, the need for
the "Round" operation is platform dependant. It is needed to make sure
that the Max\_Offset~RBs~ is an integer. For example a calculated value
of Max\_Offset~RBs~ = 5.9999999999 shall result in a Max\_Offset~RBs~ =
6.

1f. Select the largest valid Offset~RBs~ value equal or smaller than the
calculated max value, Max\_Offset~RBs~ in step 1e within the applicable
values for the carrier in TS 38.213 \[4\], table 13-1 to 13-10 limited
to the table indexes with number of RBs and number of symbols equal to
the minimum value of in the table and minimum value of for the selected
.If a valid Offset~RBs~ value is found, then continue from step 1g.

If no valid Offset~RBs~ value is found, then select the next valid GSCN
with F~SSref~ \<= F~SSref\_Max~ within the valid GSCN range for the
carrier and repeat steps 1b to 1f.

If no valid Offset~RBs~ value found within the valid GSCN range then
will the carrier not be possible to use as PCell and F~SSref~, k~SSB~,
F~PointA~, *OffsetToCarrier* and *OffsetToPointA* are calculated as
described in clause C.3.3 and the procedure is completed.

1g. Calculate k~SSB~

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------
  k~SSB~ = (F~SSBlow~ - F~offsetToPointA~) / {15 kHz for FR1, *subCarrierSpacingCommon* (MIB) for FR2} (TS 38.211 \[3\], clause 7.4.3.1).
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------
  N = SCS~SSB~ / {15 kHz for FR1; *subCarrierSpacingCommon* (MIB) for FR2}.\
  k~SSB~ MOD N \<\> 0 indicates that the SSB subcarriers are not aligned with the resource grid given by the SCS indicated by subCarrierSpacingCommon in the MIB.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------

If k~SSB~ is an integer and k~SSB~ MOD N = 0, then continue from step 2.

If k~SSB~ is not an integer value or k~SSB~ MOD N \<\> 0, then select
the next valid GSCN with F~SSref~ \< F~SSref\_Max~ within the valid GSCN
range for the carrier and repeat steps 1b to 1g.\
\
If N \> 1 and no valid k~SSB~ value found within the valid GSCN range
for the currently selected carrier frequency F~carrier~ then shift
F~carrier~ up by ΔF~Raster~ for Low range; or down by ΔF~Raster~ for
Mid, Mid-Low, Mid-High and High ranges and repeat steps 1a to 1g for a
maximum shift of 3 \* ΔF~Raster~ (see clause C.3.1, Note 1). Cases
requiring more than 3\*ΔF~Raster~ shifts shall be analyzed individually
and, if eventually agreed, marked in section 4.3 to have been obtained
applying certain exceptions over this section C.3.2. In case of an
exception, for Mid, Mid-Low and Mid-High, shifting frequency up can also
be considered to achieve the frequency closer to the ideal case.\
\
If no valid k~SSB~ value found within the valid GSCN range then will the
carrier not be possible to use as PCell and F~SSref~, k~SSB~, F~PointA~,
*OffsetToCarrier* and *OffsetToPointA* are calculated as described in
clause C.3.2 and the procedure is completed.

2\. Determine OffsetToCarrier

Select offsetToCarrier value for the carrier in accordance to Table
C.3.2-1.

Table C.3.2-1: Downlink and uplink *offsetToCarrier* default values for
different frequency ranges

  Frequency range                                                                                                                                                                              *Downlink* offsetToCarrier   *Uplink* offsetToCarrier
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------- --------------------------
  Low range                                                                                                                                                                                    0                            0
  Mid range                                                                                                                                                                                    102                          504
  High range                                                                                                                                                                                   504                          6
  Mid-Low range                                                                                                                                                                                12                           36
  Mid-High range                                                                                                                                                                               24                           114
  Note: Different values of *offsetToCarrier* have been selected for Low, Mid-Low, Mid, Mid-High and High ranges to achieve enhanced test coverage of the *offsetToCarrier* range of values.                                

In case low, mid and high range are exactly the same frequency, *use
offsetToCarrier* associated to low range.

2b. Determine F~pointA~:

  ------------------------------------------------------------
  F~PointA~ = F~carrierLow~ - *offsetToCarrier* \* PRB~size~
  ------------------------------------------------------------

3\. Calculate ΔF~OffsetCORESET-0-Carrier~:

The ΔF~OffsetCORESET-0-Carrier~ value is used to calculate the Offset
Carrier CORESET\#0 parameter included in the test frequency tables in
sub-clauses 4.3.1 and 6.2.3.

  -------------------------------------------------------------------------------------------
  ΔF~OffsetCORESET-0-Carrier~ = F~offsetToPointA~ - Offset~RB~ \* CRB~size~ - F~carrierLow~
  -------------------------------------------------------------------------------------------

4\. Calculate signalling parameters:

+-------------------------+-------------------------------------------+
| IE field                | Value                                     |
+=========================+===========================================+
| ssb-SubcarrierOffset    | Set to the 4 least significant bits of    |
|                         | k~SSB~. For the case k~SSB~ \> 15 the     |
|                         | extended by an additional most            |
|                         | significant bit encoded within PBCH as    |
|                         | specified in TS 38.213 \[22\].            |
|                         |                                           |
|                         | The IE field *ssb-SubcarrierOffset* is    |
|                         | signalled in the MIB.                     |
+-------------------------+-------------------------------------------+
| controlResourceSetZero  | S*et to the index associated with the     |
|                         | selected* Offset~RBs~ value in the        |
|                         | applicable table, 13-1 to 13-10, in TS    |
|                         | 38.213 \[22\].                            |
|                         |                                           |
|                         | The IE field *controlResourceSetZero* is  |
|                         | signalled in the IE pdcch-ConfigSIB1 in   |
|                         | the MIB.                                  |
+-------------------------+-------------------------------------------+
| absoluteFrequencySSB    | Set to F~SSref~ expressed in *ARFCN* as   |
|                         | defined in TS 38.101-1 \[15\] and TS      |
|                         | 38.101-2 \[39\], clause 5.4.2.            |
+-------------------------+-------------------------------------------+
| absoluteFrequencyPointA | *Set to* F~PointA~ expressed in *ARFCN*   |
|                         | as defined in TS 38.101-1 \[15\] and TS   |
|                         | 38.101-2 \[39\], clause 5.4.2.            |
+-------------------------+-------------------------------------------+
| offsetToPointA          | (F~OffsetToPointA~ - F~PointA~) /         |
|                         | (12\*{15 kHz for FR1; 60 kHz for FR2}).   |
|                         |                                           |
|                         | The IE field o*ffsetToPointA* is          |
|                         | signalled in IE *FrequencyInfoDL-SIB*.    |
+-------------------------+-------------------------------------------+
| offsetToCarrier         | Set to value calculated in step 2a.       |
|                         |                                           |
|                         | The IE field o*ffsetToCarrier* is         |
|                         | signalled in IE *SCS-SpecificCarrier*.    |
+-------------------------+-------------------------------------------+

C.3.3 Determination of SSB and signalling parameters for a carrier without CORESET\#0
-------------------------------------------------------------------------------------

The following procedure is used for calculation of SSB and signalling
parameters for a carrier without a CORESET\#0.

1\. Calculate F~SSref~, k~SSB~ and F~PointA~ with the SSB lowest
subcarrier at the carrier's lowest subcarrier (Δ**F~OffsetSSB-Carrier~**
in Figure C.1-1 = 0):

  F~SSref~ = F~carrierLow~ + BW~SSB~ / 2
  --------------------------------------------------------------------------------------------------------------------------
  k~SSB~ = {31 for FR1; 15 for FR2} indicating that no CORESET\#0 is present for the carrier (TS 38.213 \[4\], clause 13).
  *offsetToCarrier* = target value for *offsetToCarrier* dependent on frequency range as specified in Table C.3.2-1.
  F~PointA~ = FcarrierLow - *offsetToCarrier* \* PRB~size~

2\. Calculate signalling parameters:

+-------------------------+-------------------------------------------+
| IE field                | Value                                     |
+=========================+===========================================+
| ssb-SubcarrierOffset    | *S*et to the 4 least significant bits of  |
|                         | k~SSB~. For the case k~SSB~ \> 15 the     |
|                         | extended by an additional most            |
|                         | significant bit encoded within PBCH as    |
|                         | specified in TS 38.213 \[22\].            |
|                         |                                           |
|                         | The IE field *ssb-SubcarrierOffset* is    |
|                         | signalled in the MIB.                     |
+-------------------------+-------------------------------------------+
| controlResourceSetZero  | S*et to 0 indicating that no CORESET\#0   |
|                         | exist (*TS 38.213 \[22\], clause 13). The |
|                         | IE field *controlResourceSetZero* is      |
|                         | signalled in the IE pdcch-ConfigSIB1 in   |
|                         | the MIB.                                  |
+-------------------------+-------------------------------------------+
| searchSpaceZero         | S*et to 0 indicating that no CORESET\#0   |
|                         | exist (*TS 38.213 \[22\], clause 13). The |
|                         | IE field *searchSpaceZero* is signalled   |
|                         | in the IE pdcch-ConfigSIB1 in the MIB.    |
+-------------------------+-------------------------------------------+
| absoluteFrequencySSB    | Set to F~SSref~ expressed in *ARFCN* as   |
|                         | defined in TS 38.101-1 \[15\] and TS      |
|                         | 38.101-2 \[39\], clause 5.4.2.            |
+-------------------------+-------------------------------------------+
| absoluteFrequencyPointA | *Set to* F~PointA~ expressed in *ARFCN*   |
|                         | as defined in TS 38.101-1 \[15\] and TS   |
|                         | 38.101-2 \[39\], clause 5.4.2.            |
+-------------------------+-------------------------------------------+
| offsetToCarrier         | Set to offsetToCarrier target value       |
|                         | selected in step 1.                       |
+-------------------------+-------------------------------------------+

C.4 Determination of SSB and CORESET\#0 for RRM testing with SSB SCS 120 kHz and 240 kHz
========================================================================================

C.4.1 General
-------------

The requirements to be met and the principles used for determining the
SSB and CORESET\#0 for a PCell used in RRM test cases are:

1\. The complete SSB and CORESET\#0 shall be within the carrier's
channel bandwidth.

2\. The SSB centre frequency (SSref) shall be on the synchronisation
raster.

3\. The SSB shall be kept as close as possible to the carrier's lower
edge centre frequency.

4\. The CORESET\#0 configuration is selected using 24 RBs and
Offset~RBs~ = 0 according to Table 13-8 and Index 0 for SCS~SSB~ =120
KHz and Table 13-10 and Index 0 for SCS~SSB~ =240 kHz.

5\. The first SSB subcarrier shall be aligned with the defined resource
grid given by SCS indicated by *subCarrierSpacingCommon* in the MIB.

C.4.2 Determination of SSB, CORESET\#0 and signalling parameters
----------------------------------------------------------------

The following procedure is used to determine an SSB on the
synchronisation raster (GSCN) and a CORESET\#0 configuration (k~SSB,~
Offset~RBs~ = 0 and *OffsetToPointA*) as close as possible to the
carrier's lower edge. See figure C1-1 and clause C.1 for definition of
parameters referenced in the procedure.

1\. The target test frequencies for Low, Mid and High ranges are
calculated as described in clause C.2.1.1.

For each of Low, Mid and High ranges do:

2\. Determine SSB and CORESET\#0:

2a. Calculate the lower of F~SSref~, F~SSref\_Min~, correspondent to SSB
lowest subcarrier being at the same frequency as the carrier's lowest
subcarrier; and the higher limit of F~SSref~, F~SSref\_Max~,
correspondent to SSB highest subcarrier being at the same frequency as
the carrier's highest subcarrier F~SSref\_Min~

  F~carrierLow~ = see formula for F~carrierLow~ in Table C.1-1
  ----------------------------------------------------------------------------
  F~SSref\_Min~ = F~carrierLow~ + CRB~size~ \* Offset~RBs,min~ + BW~SSB~ / 2
  F~SSref\_Max~ = F~carrierLow~ + ΔF~carrierBandwidth~ - BW~SSB~ / 2

2b. Calculate GSCN~MIN~ correspondent to F~SSref\_Min~ in accordance to
TS 38.101-2 \[7\], clause 5.4.3.1 and select the closest valid GSCN
value with GSCN \>= GSCN~MIN~ for the carrier in according to the
carrier's synchronisation raster as specified in clause 5.4.3.3 in TS
38.101-2 \[8\].

2c. Calculate the F~SSref~ for the selected GSCN value in step 2b in
accordance to TS 38.101-2 \[7\], clause 5.4.3.1 for FR2.

2d. Calculate the frequency F~SSBlow~ and shift the carrier frequency to
achieve F~carrierLow~ equal or as close as possible F~SSBlow~ on the
carrier's frequency raster.

  F~SSBlow~ = F~SSref~ - BW~SSB~ / 2
  -------------------------------------------------------------------------------------------
  F~carrier~ = calculated using the formula in clause C.2.1.1 with F~DL\_Low~ = F~SSBlow~
  F~carrierLow~ = see formula for F~carrierLow~ in Table C.1-1 with new value of F~carrier~

2e. Calculate k~SSB~

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------
  k~SSB~ = (F~SSBlow~ - F~carrierLow~) / *subCarrierSpacingCommon* (MIB, FR2) (TS 38.211 \[3\], clause 7.4.3.1).
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------
  N = SCS~SSB~ / *subCarrierSpacingCommon* (MIB, FR2).\
  k~SSB~ MOD N \<\> 0 indicates that the SSB subcarriers are not aligned with the resource grid given by the SCS indicated by subCarrierSpacingCommon in the MIB.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------

If k~SSB~ is an integer and k~SSB~ MOD N = 0, then continue from step 3
else modify the carrier frequency to get valid value of k~SSB~ and
k~SSB~ MOD N = 0.

3\. Calculate Point A frequency, ΔF~offsetToCarrier~ and
ΔF~OffsetToPointA~:\
The CORESET\#0 configuration is selected using 24 RBs and Offset~RBs~ =
0 according to Table 13-8 and Index 0 for SCS~SSB~ =120 KHz and Table
13-10 and Index 0 for SCS~SSB~ =240 kHz (see C.4.1). This means that
F~OffsetToPointA~ = F~carrierLow~. By selecting Point A *equal to*
F~carrierLow~ *this gives:*

  *FPointA* = F~carrierLow~
  ---------------------------
  ΔF~offsetToCarrier~ = 0
  ΔF~OffsetToPointA~ = 0

4\. Calculate signalling parameters:

+-------------------------+-------------------------------------------+
| IE field                | Value                                     |
+=========================+===========================================+
| ssb-SubcarrierOffset    | Set to the 4 least significant bits of    |
|                         | k~SSB~.                                   |
|                         |                                           |
|                         | The IE field *ssb-SubcarrierOffset* is    |
|                         | signalled in the MIB.                     |
+-------------------------+-------------------------------------------+
| controlResourceSetZero  | 0 (Index=0 in table 13-8 for SCS~SSB~     |
|                         | =120 KHz and table 13-10 for SCS~SSB~     |
|                         | =240 KHz in TS 38.213 \[22\].             |
|                         |                                           |
|                         | The IE field *controlResourceSetZero* is  |
|                         | signalled in the IE pdcch-ConfigSIB1 in   |
|                         | the MIB.                                  |
+-------------------------+-------------------------------------------+
| absoluteFrequencySSB    | Set to F~SSref~ expressed in *ARFCN* as   |
|                         | defined in TS 38.101-1 \[15\] and TS      |
|                         | 38.101-2 \[39\], clause 5.4.2.            |
+-------------------------+-------------------------------------------+
| absoluteFrequencyPointA | *Set to* F~PointA~ expressed in *ARFCN*   |
|                         | as defined in TS 38.101-1 \[15\] and TS   |
|                         | 38.101-2 \[39\], clause 5.4.2.            |
+-------------------------+-------------------------------------------+
| offsetToPointA          | 0                                         |
|                         |                                           |
|                         | The IE field o*ffsetToPointA* is          |
|                         | signalled in IE *FrequencyInfoDL-SIB*.    |
+-------------------------+-------------------------------------------+
| offsetToCarrier         | 0                                         |
|                         |                                           |
|                         | The IE field o*ffsetToCarrier* is         |
|                         | signalled in IE *SCS-SpecificCarrier*.    |
+-------------------------+-------------------------------------------+

C.5 Determination of test frequencies and S-SSB for V2X bands
=============================================================

C.5.1 General
-------------

Figure C.5.1-1 shows carrier and S-SSB on V2X bands and related
parameters.

Figure C.5.1-1: location of S-SSB within a channel

The parameters referenced in Figure C.5.1-1 are defined in Table
C.5.1-1.

Table C.5.1-1: Definition of parameters for V2X bands

  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Parameter                  Description
  -------------------------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  F~SL\_PointA~              Reference Point A frequency.

  F~SL\_carrier~             F~SL\_carrier~ is the centre frequency of a carrier corresponding to its NR-ARFCN value.

  F~SL\_carrierLow~          F~SL\_carrierLow~ is the centre frequency of lowest subcarrier of the carrier.\
                             F~SL\_carrierLow~ = F~SL\_carrier~ - 12 \* SCS~SL\_Carrier~ \* (N~RB~ / 2) with N~RB~ according to section 5.3E.1 of TS 38.101-1 for the channel bandwidth of the carrier.

  ΔF~SL\_carrierBandwidth~   ΔF~SL\_carrierBandwidth~ is the carrier's channel bandwidth as provided in *carrierBandwidth* to the UE (*sl-SCS-SpecificCarrierList-r16*).

  ΔF~SL\_OffsetToCarrier~    ΔF~SL\_OffsetToCarrier~ is the frequency offset between Point A and the lower edge of the carrier. ΔF~SL\_OffsetToCarrier~ = *offsetToCarrier* \* CRB~size~, where CRB~size~ according to the subcarrier spacing of the carrier. *offsetToCarrier* is signalled to the UE (*sl-SCS-SpecificCarrierList-r16*).

  F~SL\_SSref~               Centre frequency of subcarrier with index 66 in the S-SS/PSBCH block, corresponding to NR-ARFCN value signalled to the UE by *sl-AbsoluteFrequencySSB-r16*.
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Additional parameters used in this annex are defined in Table C.5.1-2.

Table C.5.1-2: Definition of additional parameters used in section C.5.2

  -------------------------------------------------------------------------------------------------------------------------------
  SCS~SL\_Carrier~   subcarrier spacing for the carrier (*sl-SCS-SpecificCarrierList-r16*):\
                     FR1: 15kHz, 30kHz or 60kHz according to TS 38.101-1 \[7\] Table 5.3.5-1
  ------------------ ------------------------------------------------------------------------------------------------------------
  CRB~size~          Common Resource Block size = 12 \* SCS~SL\_Carrier~.

  F~SL\_Low~         Lowest frequency of the frequency range of the V2X band as defined in clause 5.2E.1 of TS 38.101-1 \[7\].

  F~SL\_High~        Highest frequency of the frequency range of the V2X band as defined in clause 5.2E.1 of TS 38.101-1 \[7\].

  ΔF~SL\_Raster~     Frequency raster of the band as defined in clause 5.4E.2.3 of TS 38.101-1 \[7\].

  BW~SL~             Bandwidth of V2X operation frequency range of the band.

  CBW~SL~            UE V2X operation channel bandwidth (MHz) of the carrier according to section 5.3E.1 of TS 38.101-1 \[7\].

  BW~SL\_SSB~        **Bandwidth of the SSB.** BW~SL\_SSB~ = 11 \* SCS~SL\_Carrier~ \* 20
  -------------------------------------------------------------------------------------------------------------------------------

C.5.2 Determination of test frequencies and S-SSB for V2X bands
---------------------------------------------------------------

The carrier test frequencies are determined considering the channel
raster according to clause 5.4.2.3 in TS 38.101-1 \[7\] for FR1.

The complete S-SSB shall be within a bandwidth of the SL BWP. The
subcarrier with index 0 in the S-SSB shall be aligned with a subcarrier
with index 0 in an RB of the SL BWP.

1\. Determine sidelink carrier centre frequencies and the frequency of
the carrier's lowest subcarrier:

  **F**~SL\_LowRange~ = **Ceil**((F~SL\_Low~ + CBW~SL~/2) / ΔF~SL\_Raster~) \* ΔF~SL\_Raster~       C.5.2-Eq1
  ------------------------------------------------------------------------------------------------- -----------
  **F**~SL\_MidRange~ = **Round**((F~SL\_Low~ + BW~SL~/2) / ΔF~SL\_Raster\_~) \* ΔF~SL\_Raster~     C.5.2-Eq2
  **F**~SL\_HighRange~ = **Floor(**(F~SL\_High~ -- CBW~SL~/2) / ΔF~SL\_Raster~) \* ΔF~SL\_Raster~   C.5.2-Eq3
  **F**~SL\_carrierLow~ = see formula for F~SL\_carrierLow~ in Table C.1-1                          

2\. Determine OffsetToCarrier

Select offsetToCarrier value for the carrier in accordance to Table
C.5.2-1.

Table C.5.2-1: Sidelink *offsetToCarrier* default values for different
frequency ranges

+---------------------------------------------------+-----------------+
| Frequency range                                   | Sidelink        |
|                                                   |                 |
|                                                   | offsetToCarrier |
+===================================================+=================+
| Low range                                         | 0               |
+---------------------------------------------------+-----------------+
| Mid range                                         | 504             |
+---------------------------------------------------+-----------------+
| High range                                        | 6               |
+---------------------------------------------------+-----------------+
| Mid-Low range                                     | 36              |
+---------------------------------------------------+-----------------+
| Mid-High range                                    | 114             |
+---------------------------------------------------+-----------------+
| Note: Different values of *offsetToCarrier* have  |                 |
| been selected for Low, Mid-Low, Mid, Mid-High and |                 |
| High ranges to achieve enhanced test coverage of  |                 |
| the *offsetToCarrier* range of values.            |                 |
+---------------------------------------------------+-----------------+

3\. Determine F~SL\_PointA~:

  --------------------------------------------------------------------
  F~SL\_PointA~ = F~SL\_carrierLow~ - *offsetToCarrier* \* CRB~size~
  --------------------------------------------------------------------

4\. Determine the centre frequencies of S-SSB for the lowest, mid and
highest possible location of F~SL\_SSref~:

  F~SL\_SSref\_Low~ = F~carrierLow~ + BW~SL\_SSB~ / 2
  ------------------------------------------------------------------------------------------
  F~SL\_SSref\_Mid~ = F~carrierLow~ + (**Floor**(N~RB~/2) -- 5) \* CRB~size~ + BW~SSB~ / 2
  F~SL\_SSref\_High~ = F~carrierLow~ + (N~RB~ -- 11) \* CRB~size~ + BW~SSB~ / 2

5\. Calculate signalling parameters:

+--------------------------------+------------------------------------+
| IE field                       | Value                              |
+================================+====================================+
| sl-AbsoluteFrequencySSB-r16    | Set to F~SL\_SSref~ expressed in   |
|                                | *ARFCN* as defined in TS 38.101-1  |
|                                | \[15\] clause 5.4E.2.              |
+--------------------------------+------------------------------------+
| sl-AbsoluteFrequencyPointA-r16 | *Set to* F~SL\_PointA~ expressed   |
|                                | in *ARFCN* as defined in TS        |
|                                | 38.101-1 \[15\] clause 5.4E.2.     |
+--------------------------------+------------------------------------+
| offsetToCarrier                | Set to value calculated in step 2. |
|                                |                                    |
|                                | The IE field offsetToCarrier *is   |
|                                | signalled in IE*                   |
|                                | sl-SCS-SpecificCarrierList-r16.    |
+--------------------------------+------------------------------------+

########  Annex D (informative): Change history

  ---------------- --------------------- ----------- ------ ----- ----- --------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------
  Change history                                                                                                                                                                                                                              
  Date             Meeting               TDoc        CR     Rev   Cat   Subject/Comment                                                                                                                                                       New version
  2017-12          RAN5\#77              R5-176995   \-     \-    \-    TP on clauses of test equipment requirement in 38.508-1                                                                                                               0.1.0
  2017-12          RAN5\#77              R5-176779   \-     \-    \-    Add references                                                                                                                                                        0.1.0
  2017-12          RAN5\#77              R5-176917   \-     \-    \-    Introduce general chapter for generic procedures                                                                                                                      0.1.0
  2017-12          RAN5\#77              R5-176918   \-     \-    \-    Add generic procedures RRC\_IDLE and RRC\_CONNECTED                                                                                                                   0.1.0
  2017-12          RAN5\#77              R5-176920   \-     \-    \-    Introduce RRC chapters                                                                                                                                                0.1.0
  2018-01          RAN5\#1-5G-NR Adhoc   R5-180066   \-     \-    \-    Definition of downlink physical layer parameters for NR                                                                                                               0.2.0
  2018-03          RAN5\#78              R5-181697   \-     \-    \-    Addition of the environmental information into TS 38.508-1                                                                                                            0.3.0
  2018-03          RAN5\#78              R5-180265   \-     \-    \-    Introduce chapter for reference configurations                                                                                                                        0.3.0
  2018-03          RAN5\#78              R5-181311   \-     \-    \-    Update the general chapter                                                                                                                                            0.3.0
  2018-03          RAN5\#78              R5-180382   \-     \-    \-    Update RRCReconfiguration                                                                                                                                             0.3.0
  2018-03          RAN5\#78              R5-180383   \-     \-    \-    Add draft RRC messages                                                                                                                                                0.3.0
  2018-03          RAN5\#78              R5-180577   \-     \-    \-    Update chapter for test frequencies                                                                                                                                   0.3.0
  2018-03          RAN5\#78              R5-180709   \-     \-    \-    Add CellGroupConfig                                                                                                                                                   0.3.0
  2018-03          RAN5\#78              R5-180773   \-     \-    \-    Add radioBearerConfig                                                                                                                                                 0.3.0
  2018-03          RAN5\#78              R5-180775   \-     \-    \-    Add draft Radio resource control information elements                                                                                                                 0.3.0
  2018-03          RAN5\#78              R5-180966   \-     \-    \-    Update RRC Connected state                                                                                                                                            0.3.0
  2018-03          RAN5\#78              R5-181035   \-     \-    \-    Update RRC IDLE state                                                                                                                                                 0.3.0
  2018-03          RAN5\#78              R5-180253   \-     \-    \-    Revised WID on: UE Conformance Test Aspects - 5G system with NR and LTE                                                                                               0.3.0
  2018-04          RAN5\#1-5G-NR Adhoc   R5-181812   \-     \-    \-    Update Radio resource control information elements                                                                                                                    0.4.0
  2018-04          RAN5\#1-5G-NR Adhoc   R5-182109   \-     \-    \-    Update CellGroupConfig                                                                                                                                                0.4.0
  2018-04          RAN5\#1-5G-NR Adhoc   R5-182064   \-     \-    \-    Update radioBearerConfig                                                                                                                                              0.4.0
  2018-04          RAN5\#1-5G-NR Adhoc   R5-182062   \-     \-    \-    Update MIB                                                                                                                                                            0.4.0
  2018-04          RAN5\#1-5G-NR Adhoc   R5-182063   \-     \-    \-    Introduce radio conditions                                                                                                                                            0.4.0
  2018-04          RAN5\#1-5G-NR Adhoc   R5-181786   \-     \-    \-    Update RRCReconfiguration                                                                                                                                             0.4.0
  2018-04          RAN5\#1-5G-NR Adhoc   R5-181971   \-     \-    \-    Add Other information elements                                                                                                                                        0.4.0
  2018-04          RAN5\#1-5G-NR Adhoc   R5-182065   \-     \-    \-    Update chapter 4.5.1 General                                                                                                                                          0.4.0
  2018-04          RAN5\#1-5G-NR Adhoc   R5-181813   \-     \-    \-    Update RRC IDLE state                                                                                                                                                 0.4.0
  2018-04          RAN5\#1-5G-NR Adhoc   R5-182066   \-     \-    \-    Update RRC CONNECTED state                                                                                                                                            0.4.0
  2018-04          RAN5\#1-5G-NR Adhoc   R5-182110   \-     \-    \-    Text proposal to add clause 4.4 reference system configurations to TS 38.508-1                                                                                        0.4.0
  2018-04          RAN5\#1-5G-NR Adhoc   R5-182067   \-     \-    \-    TP for definition of physical channel allocations in 38.508-1                                                                                                         0.4.0
  2018-04          RAN5\#1-5G-NR Adhoc   R5-182091   \-     \-    \-    TP for clauses of signal level                                                                                                                                        0.4.0
  2018-04          RAN5\#1-5G-NR Adhoc   R5-181972   \-     \-    \-    TP for updating of Downlink physical layer parameters                                                                                                                 0.4.0
  2018-04          RAN5\#1-5G-NR Adhoc   R5-181893   \-     \-    \-    Addition of UE capability information elements                                                                                                                        0.4.0
  2018-04          RAN5\#1-5G-NR Adhoc   R5-181973   \-     \-    \-    TP for adding Mid channel BW definition in TS 38.508-1                                                                                                                0.4.0
  2018-04          RAN5\#1-5G-NR Adhoc   R5-181974   \-     \-    \-    Addition of SRB3                                                                                                                                                      0.4.0
  2018-04          RAN5\#1-5G-NR Adhoc   R5-182068   \-     \-    \-    Update MeasConfig information elements                                                                                                                                0.4.0
  2018-05          RAN5\#79              R5-183082   \-     \-    \-    Update radio resource control information elements                                                                                                                    1.0.0
  2018-05          RAN5\#79              R5-182288   \-     \-    \-    TP for updating of downlink physical layer parameters in 38.508-1                                                                                                     1.0.0
  2018-05          RAN5\#79              R5-182349   \-     \-    \-    Corrections to clause 4.4 reference system configurations                                                                                                             1.0.0
  2018-05          RAN5\#79              R5-182792   \-     \-    \-    TP for clauses of Supported Channels for a NR cell                                                                                                                    1.0.0
  2018-05          RAN5\#79              R5-183218   \-     \-    \-    pCR update chapter for test frequencies - EN-DC                                                                                                                       1.0.0
  2018-05          RAN5\#79              R5-183234   \-     \-    \-    TP for updating of physical channel allocation part in 38.508-1                                                                                                       1.0.0
  2018-05          RAN5\#79              R5-183256   \-     \-    \-    pCR update chapter for test frequencies - FR1                                                                                                                         1.0.0
  2018-05          RAN5\#79              R5-183916   \-     \-    \-    TP for Annex A in TS 38.508-1 and adding a set of Connection Diagrams                                                                                                 1.0.0
  2018-05          RAN5\#79              R5-183920   \-     \-    \-    Introduction of Environmental conditions for FR1                                                                                                                      1.0.0
  2018-05          RAN5\#79              R5-182249   \-     \-    \-    Add reference to NR cell table                                                                                                                                        1.0.0
  2018-05          RAN5\#79              R5-183210   \-     \-    \-    Update PDCCH                                                                                                                                                          1.0.0
  2018-05          RAN5\#79              R5-182312   \-     \-    \-    Update chapter 4.5.1 General                                                                                                                                          1.0.0
  2018-05          RAN5\#79              R5-182313   \-     \-    \-    Update RRC CONNECTED state                                                                                                                                            1.0.0
  2018-05          RAN5\#79              R5-183087   \-     \-    \-    Addition of new RRCReconfiguration definition for AM/UM bearers                                                                                                       1.0.0
  2018-05          RAN5\#79              R5-183088   \-     \-    \-    Updates to UE capability information elements                                                                                                                         1.0.0
  2018-05          RAN5\#79              R5-183250   \-     \-    \-    Updates to UE capability information elements                                                                                                                         1.0.0
  2018-05          RAN5\#79              R5-183083   \-     \-    \-    Update RACH                                                                                                                                                           1.0.0
  2018-05          RAN5\#79              R5-183084   \-     \-    \-    Update ARFCN                                                                                                                                                          1.0.0
  2018-05          RAN5\#79              R5-183211   \-     \-    \-    Update BWP-UplinkDedicated                                                                                                                                            1.0.0
  2018-05          RAN5\#79              R5-183212   \-     \-    \-    Update serving cell                                                                                                                                                   1.0.0
  2018-05          RAN5\#79              R5-183214   \-     \-    \-    Update RadioBearerConfig                                                                                                                                              1.0.0
  2018-05          RAN5\#79              R5-183215   \-     \-    \-    Update RRCReconfiguration                                                                                                                                             1.0.0
  2018-05          RAN5\#79              R5-182381   \-     \-    \-    Update MIB                                                                                                                                                            1.0.0
  2018-05          RAN5\#79              R5-183090   \-     \-    \-    Update RRCReconfiguration for measurements                                                                                                                            1.0.0
  2018-05          RAN5\#79              R5-183264   \-     \-    \-    Corrections to clause 4.5                                                                                                                                             1.0.0
  2018-05          RAN5\#79              R5-183249   \-     \-    \-    Correction to the Table CellGroupConfig                                                                                                                               1.0.0
  2018-05          RAN5\#79              R5-183255   \-     \-    \-    Update of FR1 signal levels                                                                                                                                           1.0.0
  2018-05          RAN5\#79              R5-183216   \-     \-    \-    Update CellGroupConfig and some related information elements                                                                                                          1.0.0
  2018-05          RAN5\#79              R5-183086   \-     \-    \-    Update CSI-MeasConfig                                                                                                                                                 1.0.0
  2018-05          RAN5\#79              R5-183260   \-     \-    \-    Update some information elements related to MeasConfig                                                                                                                1.0.0
  2018-06          RAN\#80               RP-181207   \-     \-    \-    put under revision control as v15.0.0 with small editorial changes                                                                                                    15.0.0
  2018-09          RAN\#81               R5-184087   0004   \-    F     Update chapter 3                                                                                                                                                      15.1.0
  2018-09          RAN\#81               R5-184297   0012   \-    F     Addition of Mid channel bandwidth definition for several missing bands                                                                                                15.1.0
  2018-09          RAN\#81               R5-184327   0014   \-    F     Adding condition for CP-OFDM waveform                                                                                                                                 15.1.0
  2018-09          RAN\#81               R5-184347   0019   \-    F     Modified RRC\_IDLE procedure to allow multi PDN configuration throughout the test case                                                                                15.1.0
  2018-09          RAN\#81               R5-184471   0044   \-    F     Introduction of test frequencies for NR band n77                                                                                                                      15.1.0
  2018-09          RAN\#81               R5-184472   0045   \-    F     Introduction of test frequencies for NR band n78                                                                                                                      15.1.0
  2018-09          RAN\#81               R5-184473   0046   \-    F     Introduction of test frequencies for NR band n79                                                                                                                      15.1.0
  2018-09          RAN\#81               R5-184474   0047   \-    F     Introduction of test frequencies for NR band n257                                                                                                                     15.1.0
  2018-09          RAN\#81               R5-184475   0048   \-    F     Introduction of test frequencies for NR band n258                                                                                                                     15.1.0
  2018-09          RAN\#81               R5-184476   0049   \-    F     Introduction of test frequencies for NR band n260                                                                                                                     15.1.0
  2018-09          RAN\#81               R5-184477   0050   \-    F     Introduction of test frequencies for NR band n261                                                                                                                     15.1.0
  2018-09          RAN\#81               R5-184599   0056   \-    F     Add IE SS-RSSI-Measurement                                                                                                                                            15.1.0
  2018-09          RAN\#81               R5-184617   0059   \-    F     Update MIB                                                                                                                                                            15.1.0
  2018-09          RAN\#81               R5-184630   0072   \-    F     Editorial Update in clause 4.6.3                                                                                                                                      15.1.0
  2018-09          RAN\#81               R5-184783   0079   \-    F     Introduce 5GMM messages                                                                                                                                               15.1.0
  2018-09          RAN\#81               R5-184785   0080   \-    F     Introduce 5GSM messages                                                                                                                                               15.1.0
  2018-09          RAN\#81               R5-184806   0081   \-    F     Mid test CH BW for n71                                                                                                                                                15.1.0
  2018-09          RAN\#81               R5-185028   0002   1     F     Add SRB1 and SRB2 with NR PDCP                                                                                                                                        15.1.0
  2018-09          RAN\#81               R5-185029   0003   1     F     Update serving cell                                                                                                                                                   15.1.0
  2018-09          RAN\#81               R5-185030   0005   1     F     Introduce SA RRC messages                                                                                                                                             15.1.0
  2018-09          RAN\#81               R5-185031   0006   1     F     Correct IE FrequencyInfoDL                                                                                                                                            15.1.0
  2018-09          RAN\#81               R5-185032   0007   1     F     Introduce SA system information blocks                                                                                                                                15.1.0
  2018-09          RAN\#81               R5-185033   0008   1     F     Introduce SA other information elements                                                                                                                               15.1.0
  2018-09          RAN\#81               R5-185035   0013   1     F     Correct IE GSCN-ValueNR                                                                                                                                               15.1.0
  2018-09          RAN\#81               R5-185036   0017   1     F     Update of FR1 signal levels                                                                                                                                           15.1.0
  2018-09          RAN\#81               R5-185037   0022   1     F     Addition of IP Connectivity check procedure                                                                                                                           15.1.0
  2018-09          RAN\#81               R5-185038   0053   1     F     Introduce SA radio resource control information elements                                                                                                              15.1.0
  2018-09          RAN\#81               R5-185039   0054   1     F     Update IE PhysicalCellGroupConfig                                                                                                                                     15.1.0
  2018-09          RAN\#81               R5-185040   0055   1     F     Introduce cell configurations and timer tolerances chapter headers                                                                                                    15.1.0
  2018-09          RAN\#81               R5-185041   0057   1     F     Add IE SSB-MTC                                                                                                                                                        15.1.0
  2018-09          RAN\#81               R5-185042   0058   1     F     Update BWP                                                                                                                                                            15.1.0
  2018-09          RAN\#81               R5-185043   0060   1     F     Update PDSCH-Config                                                                                                                                                   15.1.0
  2018-09          RAN\#81               R5-185044   0062   1     F     Update PUCCH and PUSCH configuration                                                                                                                                  15.1.0
  2018-09          RAN\#81               R5-185045   0063   1     F     Update RACH configuration                                                                                                                                             15.1.0
  2018-09          RAN\#81               R5-185046   0065   1     F     Update CellGroupConfig                                                                                                                                                15.1.0
  2018-09          RAN\#81               R5-185047   0066   1     F     Update CSI-MeasConfig                                                                                                                                                 15.1.0
  2018-09          RAN\#81               R5-185048   0067   1     F     Update MeasConfig                                                                                                                                                     15.1.0
  2018-09          RAN\#81               R5-185049   0068   1     F     Update other information elements                                                                                                                                     15.1.0
  2018-09          RAN\#81               R5-185050   0070   1     F     Update RadioBearerConfig                                                                                                                                              15.1.0
  2018-09          RAN\#81               R5-185051   0073   1     F     Specifying content for MeasResultSCG-Failure                                                                                                                          15.1.0
  2018-09          RAN\#81               R5-185052   0075   1     F     Editorial correction to band representation of non-contiguous EN-DC band combination                                                                                  15.1.0
  2018-09          RAN\#81               R5-185053   0076   1     F     Correction to RLC-Config IE                                                                                                                                           15.1.0
  2018-09          RAN\#81               R5-185054   0077   1     F     Correction to RadioBearerConfig-DRB                                                                                                                                   15.1.0
  2018-09          RAN\#81               R5-185055   0078   1     F     Corrections and updates to BandCombinationList and Feature Set IEs                                                                                                    15.1.0
  2018-09          RAN\#81               R5-185056   0084   1     F     Corrections and updates to UE Capability IEs                                                                                                                          15.1.0
  2018-09          RAN\#81               R5-185085   0087   \-    F     Addition of UM condition to RLC-Bearer-Config IE                                                                                                                      15.1.0
  2018-09          RAN\#81               R5-185133   0086   1     F     Correction of clause 4.3.3.2.3                                                                                                                                        15.1.0
  2018-09          RAN\#81               R5-185163   0018   1     F     Modified RRC\_Connected procedure for Multi PDN throughout the test case.                                                                                             15.1.0
  2018-09          RAN\#81               R5-185165   0020   1     F     Update EN-DC Generic Procedure Parameter for Multi-PDN addition throughout Test Case                                                                                  15.1.0
  2018-09          RAN\#81               R5-185168   0082   1     F     Introduction of OTA signalling test environment                                                                                                                       15.1.0
  2018-09          RAN\#81               R5-185171   0009   2     F     Updates to PDCCH and SearchSpace configurations                                                                                                                       15.1.0
  2018-09          RAN\#81               R5-185173   0016   1     F     Test Frequencies                                                                                                                                                      15.1.0
  2018-09          RAN\#81               R5-185177   0051   1     F     Introduction of test frequencies for signalling testing in clause 6                                                                                                   15.1.0
  2018-09          RAN\#81               R5-185250   0023   1     F     Introduction of test frequencies for NR band n1                                                                                                                       15.1.0
  2018-09          RAN\#81               R5-185251   0024   1     F     Introduction of test frequencies for NR band n2                                                                                                                       15.1.0
  2018-09          RAN\#81               R5-185252   0025   1     F     Introduction of test frequencies for NR band n3                                                                                                                       15.1.0
  2018-09          RAN\#81               R5-185253   0026   1     F     Introduction of test frequencies for NR band n5                                                                                                                       15.1.0
  2018-09          RAN\#81               R5-185254   0027   1     F     Introduction of test frequencies for NR band n7                                                                                                                       15.1.0
  2018-09          RAN\#81               R5-185255   0028   1     F     Introduction of test frequencies for NR band n8                                                                                                                       15.1.0
  2018-09          RAN\#81               R5-185256   0029   1     F     Introduction of test frequencies for NR band n12                                                                                                                      15.1.0
  2018-09          RAN\#81               R5-185257   0030   1     F     Introduction of test frequencies for NR band n20                                                                                                                      15.1.0
  2018-09          RAN\#81               R5-185258   0031   1     F     Introduction of test frequencies for NR band n25                                                                                                                      15.1.0
  2018-09          RAN\#81               R5-185259   0032   1     F     Introduction of test frequencies for NR band n28                                                                                                                      15.1.0
  2018-09          RAN\#81               R5-185260   0033   1     F     Introduction of test frequencies for NR band n34                                                                                                                      15.1.0
  2018-09          RAN\#81               R5-185261   0034   1     F     Introduction of test frequencies for NR band n38                                                                                                                      15.1.0
  2018-09          RAN\#81               R5-185262   0035   1     F     Introduction of test frequencies for NR band n39                                                                                                                      15.1.0
  2018-09          RAN\#81               R5-185263   0036   1     F     Introduction of test frequencies for NR band n40                                                                                                                      15.1.0
  2018-09          RAN\#81               R5-185264   0037   1     F     Update of test frequencies for NR band n41                                                                                                                            15.1.0
  2018-09          RAN\#81               R5-185265   0038   1     F     Introduction of test frequencies for NR band n51                                                                                                                      15.1.0
  2018-09          RAN\#81               R5-185266   0039   1     F     Introduction of test frequencies for NR band n66                                                                                                                      15.1.0
  2018-09          RAN\#81               R5-185267   0040   1     F     Introduction of test frequencies for NR band n70                                                                                                                      15.1.0
  2018-09          RAN\#81               R5-185268   0041   1     F     Update of test frequencies for NR band n71                                                                                                                            15.1.0
  2018-09          RAN\#81               R5-185269   0042   1     F     Introduction of test frequencies for NR band n75                                                                                                                      15.1.0
  2018-09          RAN\#81               R5-185270   0043   1     F     Introduction of test frequencies for NR band n76                                                                                                                      15.1.0
  2018-09          RAN\#81               R5-185443   0052   1     F     Correction to power level for FR1 RF tests                                                                                                                            15.1.0
  2018-09          RAN\#81               R5-185557   0085   1     F     FR2\_UE\_BeamlockProcedure\_38.508-1                                                                                                                                  15.1.0
  2018-12          RAN\#82               R5-186453   0239   \-    F     Updates to clause 4.3.3, physical channel allocations                                                                                                                 15.2.0
  2018-12          RAN\#82               R5-186457   0240   \-    F     Correction to E-UTRA test frequency for intra-band contiguous configuration for band 41                                                                               15.2.0
  2018-12          RAN\#82               R5-186468   0241   \-    F     E-UTRA test frequencies for EN-DC intra-band contiguous configurations for band 71                                                                                    15.2.0
  2018-12          RAN\#82               R5-186491   0245   \-    F     Update chapter 4.5 for RF connected procedure                                                                                                                         15.2.0
  2018-12          RAN\#82               R5-186508   0249   \-    F     FR2 UE and TE radiated connection diagram                                                                                                                             15.2.0
  2018-12          RAN\#82               R5-186575   0251   \-    F     Update IE ServingCellConfig                                                                                                                                           15.2.0
  2018-12          RAN\#82               R5-186612   0252   \-    F     Add CounterCheck                                                                                                                                                      15.2.0
  2018-12          RAN\#82               R5-186613   0253   \-    F     Update DLInformationTransfer                                                                                                                                          15.2.0
  2018-12          RAN\#82               R5-186641   0255   \-    F     Update IE SchedulingRequestResourceConfig                                                                                                                             15.2.0
  2018-12          RAN\#82               R5-186665   0258   \-    F     Update LocationMeasurementIndication                                                                                                                                  15.2.0
  2018-12          RAN\#82               R5-186666   0259   \-    F     Update MeasurementReport                                                                                                                                              15.2.0
  2018-12          RAN\#82               R5-186677   0261   \-    F     Resubmission of update to 38.508 for mid channel bandwidth                                                                                                            15.2.0
  2018-12          RAN\#82               R5-186682   0262   \-    F     Update MobilityFromNRCommand                                                                                                                                          15.2.0
  2018-12          RAN\#82               R5-186691   0264   \-    F     Update Paging                                                                                                                                                         15.2.0
  2018-12          RAN\#82               R5-186692   0265   \-    F     Update RRCReestablishment                                                                                                                                             15.2.0
  2018-12          RAN\#82               R5-186714   0267   \-    F     Update RRCReject                                                                                                                                                      15.2.0
  2018-12          RAN\#82               R5-186719   0268   \-    F     Updates related to introduction of test frequencies                                                                                                                   15.2.0
  2018-12          RAN\#82               R5-186722   0271   \-    F     Update SecurityAlgorithmConfig                                                                                                                                        15.2.0
  2018-12          RAN\#82               R5-186723   0272   \-    F     Updates to MeasResults                                                                                                                                                15.2.0
  2018-12          RAN\#82               R5-186734   0273   \-    F     Update RRCRelease                                                                                                                                                     15.2.0
  2018-12          RAN\#82               R5-186744   0274   \-    F     Update RRCResume                                                                                                                                                      15.2.0
  2018-12          RAN\#82               R5-186825   0279   \-    F     Correction of test frequencies for NR band n1                                                                                                                         15.2.0
  2018-12          RAN\#82               R5-186826   0280   \-    F     Correction of test frequencies for NR band n2                                                                                                                         15.2.0
  2018-12          RAN\#82               R5-186827   0281   \-    F     Correction of test frequencies for NR band n3                                                                                                                         15.2.0
  2018-12          RAN\#82               R5-186828   0282   \-    F     Correction of test frequencies for NR band n5                                                                                                                         15.2.0
  2018-12          RAN\#82               R5-186829   0283   \-    F     Correction of test frequencies for NR band n7                                                                                                                         15.2.0
  2018-12          RAN\#82               R5-186830   0284   \-    F     Correction of test frequencies for NR band n8                                                                                                                         15.2.0
  2018-12          RAN\#82               R5-186831   0285   \-    F     Correction of test frequencies for NR band n12                                                                                                                        15.2.0
  2018-12          RAN\#82               R5-186832   0286   \-    F     Correction of test frequencies for NR band n20                                                                                                                        15.2.0
  2018-12          RAN\#82               R5-186833   0287   \-    F     Correction of test frequencies for NR band n25                                                                                                                        15.2.0
  2018-12          RAN\#82               R5-186834   0288   \-    F     Correction of test frequencies for NR band n28                                                                                                                        15.2.0
  2018-12          RAN\#82               R5-186835   0289   \-    F     Correction of test frequencies for NR band n34                                                                                                                        15.2.0
  2018-12          RAN\#82               R5-186836   0290   \-    F     Correction of test frequencies for NR band n38                                                                                                                        15.2.0
  2018-12          RAN\#82               R5-186837   0291   \-    F     Correction of test frequencies for NR band n39                                                                                                                        15.2.0
  2018-12          RAN\#82               R5-186838   0292   \-    F     Correction of test frequencies for NR band n40                                                                                                                        15.2.0
  2018-12          RAN\#82               R5-186839   0293   \-    F     Correction of test frequencies for NR band n41                                                                                                                        15.2.0
  2018-12          RAN\#82               R5-186840   0294   \-    F     Correction of test frequencies for NR band n51                                                                                                                        15.2.0
  2018-12          RAN\#82               R5-186841   0295   \-    F     Introduction of test frequencies for NR band n66                                                                                                                      15.2.0
  2018-12          RAN\#82               R5-186842   0296   \-    F     Introduction of test frequencies for NR band n70                                                                                                                      15.2.0
  2018-12          RAN\#82               R5-186844   0298   \-    F     Correction of test frequencies for NR band n75                                                                                                                        15.2.0
  2018-12          RAN\#82               R5-186845   0299   \-    F     Correction of test frequencies for NR band n76                                                                                                                        15.2.0
  2018-12          RAN\#82               R5-186846   0300   \-    F     Correction of test frequencies for NR band n77                                                                                                                        15.2.0
  2018-12          RAN\#82               R5-186847   0301   \-    F     Correction of test frequencies for NR band n78                                                                                                                        15.2.0
  2018-12          RAN\#82               R5-186848   0302   \-    F     Correction of test frequencies for NR band n79                                                                                                                        15.2.0
  2018-12          RAN\#82               R5-186850   0304   \-    F     Correction of test frequencies for NR band n258                                                                                                                       15.2.0
  2018-12          RAN\#82               R5-186851   0305   \-    F     Correction of test frequencies for NR band n260                                                                                                                       15.2.0
  2018-12          RAN\#82               R5-186852   0306   \-    F     Correction of test frequencies for NR band n261                                                                                                                       15.2.0
  2018-12          RAN\#82               R5-186855   0309   \-    F     Introduction of preamble test states                                                                                                                                  15.2.0
  2018-12          RAN\#82               R5-186857   0311   \-    F     Introduction DCI format 1\_0 for paging, SI and random access                                                                                                         15.2.0
  2018-12          RAN\#82               R5-186858   0312   \-    F     Correction to DCI format 1\_1                                                                                                                                         15.2.0
  2018-12          RAN\#82               R5-186859   0313   \-    F     Update IE RateMatchPattern                                                                                                                                            15.2.0
  2018-12          RAN\#82               R5-186861   0315   \-    F     Correction of generic procedure parameter naming for test loop function                                                                                               15.2.0
  2018-12          RAN\#82               R5-186862   0316   \-    F     Correction of test procedures to activate and deactivate UE Beamlock Function                                                                                         15.2.0
  2018-12          RAN\#82               R5-186893   0318   \-    F     Corrections to the notes in the OTA signal level tables                                                                                                               15.2.0
  2018-12          RAN\#82               R5-186911   0320   \-    F     Add RRCSetupComplete                                                                                                                                                  15.2.0
  2018-12          RAN\#82               R5-186912   0321   \-    F     Add RRCSetupRequest                                                                                                                                                   15.2.0
  2018-12          RAN\#82               R5-186913   0322   \-    F     Add RRCSystemInfoRequest                                                                                                                                              15.2.0
  2018-12          RAN\#82               R5-186916   0323   \-    F     Add SecurityModeCommand                                                                                                                                               15.2.0
  2018-12          RAN\#82               R5-186918   0324   \-    F     Update SystemInformation                                                                                                                                              15.2.0
  2018-12          RAN\#82               R5-186920   0325   \-    F     Add UEAssistanceInformation                                                                                                                                           15.2.0
  2018-12          RAN\#82               R5-186921   0326   \-    F     Update UECapabilityEnquiry                                                                                                                                            15.2.0
  2018-12          RAN\#82               R5-186922   0327   \-    F     Update ULInformationTransfer                                                                                                                                          15.2.0
  2018-12          RAN\#82               R5-186923   0328   \-    F     Update IE PTRS-UplinkConfig                                                                                                                                           15.2.0
  2018-12          RAN\#82               R5-186925   0330   \-    F     Update RRCResumeRequest                                                                                                                                               15.2.0
  2018-12          RAN\#82               R5-186929   0331   \-    F     Update PTRS-DownlinkConfig                                                                                                                                            15.2.0
  2018-12          RAN\#82               R5-186936   0335   \-    F     Update PUCCH-SpatialRelationInfo                                                                                                                                      15.2.0
  2018-12          RAN\#82               R5-186987   0342   \-    F     Addition of SIB3 message\_Resubmission of 185792                                                                                                                      15.2.0
  2018-12          RAN\#82               R5-186988   0343   \-    F     Addition of SIB5 message\_Resubmission of 186054                                                                                                                      15.2.0
  2018-12          RAN\#82               R5-186989   0344   \-    F     Addition of SIB6 - SIB8 message\_Resubmission of 186055                                                                                                               15.2.0
  2018-12          RAN\#82               R5-186990   0345   \-    F     Addition of SIB9 message\_Resubmission of 186056                                                                                                                      15.2.0
  2018-12          RAN\#82               R5-187026   0348   \-    F     Addition of P-Max in Test environment for RF test                                                                                                                     15.2.0
  2018-12          RAN\#82               R5-187028   0350   \-    F     Addition of test frequencies for SUL band n80                                                                                                                         15.2.0
  2018-12          RAN\#82               R5-187030   0352   \-    F     Addition of test frequencies for SUL band n82                                                                                                                         15.2.0
  2018-12          RAN\#82               R5-187031   0353   \-    F     Addition of test frequencies for SUL band n83                                                                                                                         15.2.0
  2018-12          RAN\#82               R5-187032   0354   \-    F     Addition of test frequencies for SUL band n84                                                                                                                         15.2.0
  2018-12          RAN\#82               R5-187033   0355   \-    F     Addition of test frequencies for SUL band n86                                                                                                                         15.2.0
  2018-12          RAN\#82               R5-187110   0358   \-    F     Correction to default message contents for SRB3 configuration                                                                                                         15.2.0
  2018-12          RAN\#82               R5-187159   0361   \-    F     Updates to Configuration Update 5GMM messages                                                                                                                         15.2.0
  2018-12          RAN\#82               R5-187160   0362   \-    F     Updates to De-registration 5GMM messages                                                                                                                              15.2.0
  2018-12          RAN\#82               R5-187161   0363   \-    F     Updates to Identity 5GMM messages                                                                                                                                     15.2.0
  2018-12          RAN\#82               R5-187162   0364   \-    F     Updates to NAS Transport 5GMM messages                                                                                                                                15.2.0
  2018-12          RAN\#82               R5-187163   0365   \-    F     Updates to Notification 5GMM messages                                                                                                                                 15.2.0
  2018-12          RAN\#82               R5-187164   0366   \-    F     Updates to PDU session authentication 5GSM messages                                                                                                                   15.2.0
  2018-12          RAN\#82               R5-187166   0368   \-    F     Updates to PDU session modification 5GSM messages                                                                                                                     15.2.0
  2018-12          RAN\#82               R5-187172   0374   \-    F     Removal of Editor's Notes in section 4.6.3                                                                                                                            15.2.0
  2018-12          RAN\#82               R5-187175   0377   \-    F     Addition and updates to Information Elements in section 4.6.5                                                                                                         15.2.0
  2018-12          RAN\#82               R5-187270   0381   \-    F     Updating 4.2.1 General functional requirements                                                                                                                        15.2.0
  2018-12          RAN\#82               R5-187271   0382   \-    F     Update the section for test equipment requirements for TRx                                                                                                            15.2.0
  2018-12          RAN\#82               R5-187272   0383   \-    F     FR2 downlink signal level(38.508-1)                                                                                                                                   15.2.0
  2018-12          RAN\#82               R5-187413   0389   \-    F     Uplink RNTI to valid value in TS 38.508-1                                                                                                                             15.2.0
  2018-12          RAN\#82               R5-187415   0390   \-    F     Update maxPayloadMinus1 in PUCCH config in TS 38.508-1                                                                                                                15.2.0
  2018-12          RAN\#82               R5-187420   0393   \-    F     Addition of connection diagram for 2 TX UL MIMO                                                                                                                       15.2.0
  2018-12          RAN\#82               R5-187557   0396   \-    F     Addition of low and high test channel bandwidth in 38.508                                                                                                             15.2.0
  2018-12          RAN\#82               R5-188205   0397   1     F     Updates to Annex B to add Permitted OTA Test Methods                                                                                                                  15.2.0
  2018-12          RAN\#82               R5-187610   0398   \-    F     Corrections to IEs part of PDSCH-ServingCellConfig, ServingCellConfig and ServingCellConfigCommon                                                                     15.2.0
  2018-12          RAN\#82               R5-187659   0243   1     F     Wordings for Uplink NAS messages                                                                                                                                      15.2.0
  2018-12          RAN\#82               R5-187660   0247   1     F     Default cell configurations for NAS                                                                                                                                   15.2.0
  2018-12          RAN\#82               R5-187661   0248   1     F     Update IE SI-SchedulingInfo                                                                                                                                           15.2.0
  2018-12          RAN\#82               R5-187662   0349   1     F     Addition of Combinations of system information blocks in 4.4.3.1.2                                                                                                    15.2.0
  2018-12          RAN\#82               R5-187664   0263   1     F     Correction to various Radio resource control IEs                                                                                                                      15.2.0
  2018-12          RAN\#82               R5-187665   0308   1     F     Correction to DCI formats 0\_0 and 0\_1                                                                                                                               15.2.0
  2018-12          RAN\#82               R5-187666   0310   1     F     Introduction of SDL and SUL cells in simulated cells in clause 4.4.2                                                                                                  15.2.0
  2018-12          RAN\#82               R5-187667   0314   1     F     Correction to RRC\_IDLE procedure                                                                                                                                     15.2.0
  2018-12          RAN\#82               R5-187668   0332   1     F     Update CSI related information elements                                                                                                                               15.2.0
  2018-12          RAN\#82               R5-187669   0333   1     F     Update ServingCellConfigCommon and TDD-UL-DL-Config                                                                                                                   15.2.0
  2018-12          RAN\#82               R5-187670   0334   1     F     Update SRS-Config                                                                                                                                                     15.2.0
  2018-12          RAN\#82               R5-187671   0336   1     F     Update some information elements for measurements                                                                                                                     15.2.0
  2018-12          RAN\#82               R5-187672   0337   1     F     Update CellGroupConfig and related information elements                                                                                                               15.2.0
  2018-12          RAN\#82               R5-187673   0338   1     F     CR of NR 508-1 clause 4.6.2\_SIB2, SIB4                                                                                                                               15.2.0
  2018-12          RAN\#82               R5-187674   0339   1     F     CR of NR 508-1 Table 4.4.2-2\_Default NR Cells parameters                                                                                                             15.2.0
  2018-12          RAN\#82               R5-187675   0341   1     F     Update RLC-Config                                                                                                                                                     15.2.0
  2018-12          RAN\#82               R5-187676   0357   1     F     Specifying Test procedure to check that UE is camped on a new NR cell belonging to a new TA                                                                           15.2.0
  2018-12          RAN\#82               R5-187677   0360   1     F     Updates to Authentication 5GMM messages                                                                                                                               15.2.0
  2018-12          RAN\#82               R5-187678   0369   1     F     Updates to PDU session release 5GSM messages                                                                                                                          15.2.0
  2018-12          RAN\#82               R5-187679   0371   1     F     Updates to Security mode 5GMM messages                                                                                                                                15.2.0
  2018-12          RAN\#82               R5-187680   0375   1     F     Addition of new Information Elements in section 4.6.3                                                                                                                 15.2.0
  2018-12          RAN\#82               R5-187681   0379   1     F     Updates to SIG OTA Calibration for FR2                                                                                                                                15.2.0
  2018-12          RAN\#82               R5-187682   0394   1     F     Addition of default QoS configurations                                                                                                                                15.2.0
  2018-12          RAN\#82               R5-187720   0319   2     F     Uplink PTRS disable for RF testing                                                                                                                                    15.2.0
  2018-12          RAN\#82               R5-188238   0242   2     F     Addition to E-UTRA test frequencies for intra-band contiguous configuration for band 41                                                                               15.2.0
  2018-12          RAN\#82               R5-187723   0303   1     F     Correction of test frequencies for NR band n257                                                                                                                       15.2.0
  2018-12          RAN\#82               R5-187724   0269   1     F     New annex for NR test frequency calculations                                                                                                                          15.2.0
  2018-12          RAN\#82               R5-187725   0297   1     F     Correction of test frequencies for NR band n71                                                                                                                        15.2.0
  2018-12          RAN\#82               R5-187745   0238   1     F     Update SIB1                                                                                                                                                           15.2.0
  2018-12          RAN\#82               R5-187747   0257   1     F     Correction to Signal levels for conducted testing                                                                                                                     15.2.0
  2018-12          RAN\#82               R5-187748   0270   1     F     Updates to E-UTRA RRC\_CONNECTED generic procedure                                                                                                                    15.2.0
  2018-12          RAN\#82               R5-187750   0275   1     F     Add RRCResumeComplete                                                                                                                                                 15.2.0
  2018-12          RAN\#82               R5-187751   0278   1     F     Update chapter 4.5.3 RRC\_INACTIVE                                                                                                                                    15.2.0
  2018-12          RAN\#82               R5-187752   0307   1     F     Correction of test frequencies for signalling testing in clause 6                                                                                                     15.2.0
  2018-12          RAN\#82               R5-187753   0317   1     F     Specifying Test procedure to check that UE is in RRC\_IDLE state on a certain NR cell                                                                                 15.2.0
  2018-12          RAN\#82               R5-187754   0329   1     F     Update IE RLF-TimersAndConstants                                                                                                                                      15.2.0
  2018-12          RAN\#82               R5-187755   0346   1     F     Add RRCSetup                                                                                                                                                          15.2.0
  2018-12          RAN\#82               R5-187756   0347   1     F     Update RRCReconfiguration                                                                                                                                             15.2.0
  2018-12          RAN\#82               R5-187757   0356   1     F     Update IE RadioBearerConfig                                                                                                                                           15.2.0
  2018-12          RAN\#82               R5-187759   0370   1     F     Updates to Registration 5GMM messages                                                                                                                                 15.2.0
  2018-12          RAN\#82               R5-187760   0372   1     F     Updates to Security protected 5GS NAS and 5GMM status messages                                                                                                        15.2.0
  2018-12          RAN\#82               R5-187761   0373   1     F     Updates to Service Request 5GMM messages                                                                                                                              15.2.0
  2018-12          RAN\#82               R5-187762   0376   1     F     Addition and updates to Information Elements in section 4.6.4                                                                                                         15.2.0
  2018-12          RAN\#82               R5-187763   0388   1     F     Addition of 5GS related new EFs to Test UICC definition                                                                                                               15.2.0
  2018-12          RAN\#82               R5-187764   0395   1     F     Update IE CellGroupConfig                                                                                                                                             15.2.0
  2018-12          RAN\#82               R5-187802   0384   1     F     Updating power levels for LTE Anchor Link                                                                                                                             15.2.0
  2018-12          RAN\#82               R5-187887   0351   1     F     Addition of test frequencies for SUL band n81                                                                                                                         15.2.0
  2018-12          RAN\#82               R5-188031   0391   1     F     Addition of 2TX\_UL\_MIMO condition                                                                                                                                   15.2.0
  2018-12          RAN\#82               R5-188107   0367   2     F     Updates to PDU session establishment 5GSM messages                                                                                                                    15.2.0
  2018-12          RAN\#82               R5-188122   0260   2     F     Update chapter 4.5.2 RRC\_IDLE                                                                                                                                        15.2.0
  2018-12          RAN\#82               R5-188123   0250   1     F     Update chapter 4.5.4 RRC\_CONNECTED                                                                                                                                   15.2.0
  2019-03          RAN\#83               R5-191047   0526   \-    F     Update IE PDCCH-ConfigCommon                                                                                                                                          15.3.0
  2019-03          RAN\#83               R5-191048   0527   \-    F     Update IE RadioBearerConfig                                                                                                                                           15.3.0
  2019-03          RAN\#83               R5-191094   0529   \-    F     Updates of test channel bandwidth in TS 38.508-1                                                                                                                      15.3.0
  2019-03          RAN\#83               R5-191129   0530   \-    F     Update IE SDAP-Config                                                                                                                                                 15.3.0
  2019-03          RAN\#83               R5-191145   0531   \-    F     Update IE CellGroupId                                                                                                                                                 15.3.0
  2019-03          RAN\#83               R5-191155   0532   \-    F     Correction to temperature and voltage of Common test environments                                                                                                     15.3.0
  2019-03          RAN\#83               R5-191187   0534   \-    F     Updates for Other SI support                                                                                                                                          15.3.0
  2019-03          RAN\#83               R5-191189   0536   \-    F     Correction to RadioBearerConfig                                                                                                                                       15.3.0
  2019-03          RAN\#83               R5-191191   0538   \-    F     Correction to SystemInformation                                                                                                                                       15.3.0
  2019-03          RAN\#83               R5-191192   0539   \-    F     Correction to PUCCH-Config                                                                                                                                            15.3.0
  2019-03          RAN\#83               R5-191193   0540   \-    F     Correction to SIB3 and SIB4                                                                                                                                           15.3.0
  2019-03          RAN\#83               R5-191194   0541   \-    F     Correction of PUSCH-TimeDomainResourceAllocationList                                                                                                                  15.3.0
  2019-03          RAN\#83               R5-191195   0542   \-    F     Corrections and clarifications regarding DCI formats 0\_1 and 1\_1                                                                                                    15.3.0
  2019-03          RAN\#83               R5-191219   0545   \-    F     Updates to Authentication 5GMM messages                                                                                                                               15.3.0
  2019-03          RAN\#83               R5-191220   0546   \-    F     Updates to Configuration Update 5GMM messages                                                                                                                         15.3.0
  2019-03          RAN\#83               R5-191221   0547   \-    F     Updates to De-registration 5GMM messages                                                                                                                              15.3.0
  2019-03          RAN\#83               R5-191222   0548   \-    F     Updates to NAS transport 5GMM messages                                                                                                                                15.3.0
  2019-03          RAN\#83               R5-191223   0549   \-    F     Updates to PDU session establishment 5GSM messages                                                                                                                    15.3.0
  2019-03          RAN\#83               R5-191224   0550   \-    F     Updates to PDU session modification 5GSM messages                                                                                                                     15.3.0
  2019-03          RAN\#83               R5-191225   0551   \-    F     Updates to PDU session release 5GSM messages                                                                                                                          15.3.0
  2019-03          RAN\#83               R5-191226   0552   \-    F     Updates to Registration 5GMM messages                                                                                                                                 15.3.0
  2019-03          RAN\#83               R5-191227   0553   \-    F     Updates to Security Mode 5GMM messages                                                                                                                                15.3.0
  2019-03          RAN\#83               R5-191228   0554   \-    F     Updates to Security Protected 5GS NAS message                                                                                                                         15.3.0
  2019-03          RAN\#83               R5-191229   0555   \-    F     Updates to Service Request 5GMM messages                                                                                                                              15.3.0
  2019-03          RAN\#83               R5-191233   0556   \-    F     Update IE BWP-Id                                                                                                                                                      15.3.0
  2019-03          RAN\#83               R5-191234   0557   \-    F     Add IE RejectWaitTime                                                                                                                                                 15.3.0
  2019-03          RAN\#83               R5-191235   0558   \-    F     Update IE ShortMAC-I                                                                                                                                                  15.3.0
  2019-03          RAN\#83               R5-191236   0559   \-    F     Update IE UE-TimersAndConstants                                                                                                                                       15.3.0
  2019-03          RAN\#83               R5-191237   0560   \-    F     Update IE PUCCH-ConfigCommon                                                                                                                                          15.3.0
  2019-03          RAN\#83               R5-191242   0561   \-    F     Addition of Positioning specifications                                                                                                                                15.3.0
  2019-03          RAN\#83               R5-191243   0562   \-    F     Update AS security Algorithm for RF testing                                                                                                                           15.3.0
  2019-03          RAN\#83               R5-191274   0563   \-    F     Update of structure of test frequency clauses                                                                                                                         15.3.0
  2019-03          RAN\#83               R5-191280   0564   \-    F     Correction to UL configuration                                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191281   0565   \-    F     Correction to default value of IE's in PDSCH-Config in Table 4.6.3-75                                                                                                 15.3.0
  2019-03          RAN\#83               R5-191301   0568   \-    F     Correction of test frequencies for signalling testing in clause 6                                                                                                     15.3.0
  2019-03          RAN\#83               R5-191302   0569   \-    F     Correction of test frequencies for EN-DC configuration DC\_(n)41                                                                                                      15.3.0
  2019-03          RAN\#83               R5-191304   0571   \-    F     Correction of test frequencies for NR band n1                                                                                                                         15.3.0
  2019-03          RAN\#83               R5-191305   0572   \-    F     Correction of test frequencies for NR band n2                                                                                                                         15.3.0
  2019-03          RAN\#83               R5-191306   0573   \-    F     Correction of test frequencies for NR band n3                                                                                                                         15.3.0
  2019-03          RAN\#83               R5-191307   0574   \-    F     Correction of test frequencies for NR band n5                                                                                                                         15.3.0
  2019-03          RAN\#83               R5-191308   0575   \-    F     Correction of test frequencies for NR band n7                                                                                                                         15.3.0
  2019-03          RAN\#83               R5-191309   0576   \-    F     Correction of test frequencies for NR band n8                                                                                                                         15.3.0
  2019-03          RAN\#83               R5-191310   0577   \-    F     Correction of test frequencies for NR band n12                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191311   0578   \-    F     Correction of test frequencies for NR band n20                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191312   0579   \-    F     Correction of test frequencies for NR band n25                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191313   0580   \-    F     Correction of test frequencies for NR band n28                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191314   0581   \-    F     Correction of test frequencies for NR band n34                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191315   0582   \-    F     Correction of test frequencies for NR band n38                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191316   0583   \-    F     Correction of test frequencies for NR band n39                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191317   0584   \-    F     Correction of test frequencies for NR band n40                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191318   0585   \-    F     Correction of test frequencies for NR band n41                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191319   0586   \-    F     Introduction of test frequencies for NR band n50                                                                                                                      15.3.0
  2019-03          RAN\#83               R5-191320   0587   \-    F     Correction of test frequencies for NR band n51                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191321   0588   \-    F     Correction of test frequencies for NR band n66                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191322   0589   \-    F     Correction of test frequencies for NR band n70                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191323   0590   \-    F     Correction of test frequencies for NR band n71                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191324   0591   \-    F     Introduction of test frequencies for NR band n74                                                                                                                      15.3.0
  2019-03          RAN\#83               R5-191325   0592   \-    F     Correction of test frequencies for NR band n75                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191326   0593   \-    F     Correction of test frequencies for NR band n76                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191327   0594   \-    F     Correction of test frequencies for NR band n77                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191328   0595   \-    F     Correction of test frequencies for NR band n78                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191329   0596   \-    F     Correction of test frequencies for NR band n79                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191330   0597   \-    F     Correction of test frequencies for NR band n257                                                                                                                       15.3.0
  2019-03          RAN\#83               R5-191331   0598   \-    F     Correction of test frequencies for NR band n258                                                                                                                       15.3.0
  2019-03          RAN\#83               R5-191332   0599   \-    F     Correction of test frequencies for NR band n260                                                                                                                       15.3.0
  2019-03          RAN\#83               R5-191333   0600   \-    F     Correction of test frequencies for NR band n261                                                                                                                       15.3.0
  2019-03          RAN\#83               R5-191334   0601   \-    F     Correction of DCI format 1\_0                                                                                                                                         15.3.0
  2019-03          RAN\#83               R5-191352   0603   \-    F     Update CounterCheckResponse                                                                                                                                           15.3.0
  2019-03          RAN\#83               R5-191354   0604   \-    F     Add FailureInformation                                                                                                                                                15.3.0
  2019-03          RAN\#83               R5-191355   0605   \-    F     Update LocationMeasurementIndication                                                                                                                                  15.3.0
  2019-03          RAN\#83               R5-191356   0606   \-    F     Updates to section 4.8.3 (test USIM parameters)                                                                                                                       15.3.0
  2019-03          RAN\#83               R5-191360   0607   \-    F     Update MeasurementReport                                                                                                                                              15.3.0
  2019-03          RAN\#83               R5-191361   0608   \-    F     Update MobilityFromNRCommand                                                                                                                                          15.3.0
  2019-03          RAN\#83               R5-191364   0609   \-    F     Update Paging                                                                                                                                                         15.3.0
  2019-03          RAN\#83               R5-191366   0610   \-    F     Update RRCSetupComplete                                                                                                                                               15.3.0
  2019-03          RAN\#83               R5-191368   0611   \-    F     Update SecurityModeComplete                                                                                                                                           15.3.0
  2019-03          RAN\#83               R5-191370   0612   \-    F     Update SecurityModeFailure                                                                                                                                            15.3.0
  2019-03          RAN\#83               R5-191371   0613   \-    F     Update UEAssistanceInformation                                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191372   0614   \-    F     Update UECapabilityInformation                                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-191384   0616   \-    F     Correction to SecurityConfig of RadioBearerConfig                                                                                                                     15.3.0
  2019-03          RAN\#83               R5-191385   0617   \-    F     Correction to SIB9                                                                                                                                                    15.3.0
  2019-03          RAN\#83               R5-191386   0618   \-    F     Correction to SRS-Config of BWP-UplinkDedicated                                                                                                                       15.3.0
  2019-03          RAN\#83               R5-191446   0620   \-    F     Correction of default configuration of RRC IEs in 38.508-1                                                                                                            15.3.0
  2019-03          RAN\#83               R5-191450   0621   \-    F     Addition of NR system information combination SIB6, SIB7                                                                                                              15.3.0
  2019-03          RAN\#83               R5-191538   0624   \-    F     Update ULInformationTransfer                                                                                                                                          15.3.0
  2019-03          RAN\#83               R5-191539   0625   \-    F     Update IE QuantityConfig and CSI-ReportConfig                                                                                                                         15.3.0
  2019-03          RAN\#83               R5-191620   0629   \-    F     Clarification for NR inter-band measurement test case configuration                                                                                                   15.3.0
  2019-03          RAN\#83               R5-191762   0637   \-    F     Editorial update in MeasObjectNR and ReportConfigNR                                                                                                                   15.3.0
  2019-03          RAN\#83               R5-191763   0638   \-    F     Update ReportConfigNR and TimeToTrigger                                                                                                                               15.3.0
  2019-03          RAN\#83               R5-192271   0570   1     F     Correction of test frequencies for EN-DC configuration DC\_(n)71                                                                                                      15.3.0
  2019-03          RAN\#83               R5-192272   0602   1     F     Update chapter 4.5 RRC Connected initiation                                                                                                                           15.3.0
  2019-03          RAN\#83               R5-192273   0626   1     F     Update RRCRelease                                                                                                                                                     15.3.0
  2019-03          RAN\#83               R5-192274   0615   1     F     Correction to NR SchedulingRequestResourceConfig                                                                                                                      15.3.0
  2019-03          RAN\#83               R5-192275   0627   1     F     Update IE I-RNTI-Value                                                                                                                                                15.3.0
  2019-03          RAN\#83               R5-192276   0628   1     F     Update IE ShortI-RNTI-Value                                                                                                                                           15.3.0
  2019-03          RAN\#83               R5-192277   0630   1     F     Updates to test environments for Signalling test                                                                                                                      15.3.0
  2019-03          RAN\#83               R5-192278   0633   1     F     Addition of USIM Profiles for Signaling TC                                                                                                                            15.3.0
  2019-03          RAN\#83               R5-192279   0636   1     F     Update QoS Configuration                                                                                                                                              15.3.0
  2019-03          RAN\#83               R5-192280   0643   1     F     Update to of Generic procedure E-UTRA RRC\_IDLE                                                                                                                       15.3.0
  2019-03          RAN\#83               R5-192281   0644   1     F     Introduction of EAP AKA                                                                                                                                               15.3.0
  2019-03          RAN\#83               R5-192290   0655   \-    F     Update chapter 4.5 RRC\_INACTIVE                                                                                                                                      15.3.0
  2019-03          RAN\#83               R5-192363   0631   1     F     Updating P-Max IE                                                                                                                                                     15.3.0
  2019-03          RAN\#83               R5-192364   0632   2     F     Updating IEs part of SearchSpace                                                                                                                                      15.3.0
  2019-03          RAN\#83               R5-192400   0528   1     F     Setup diagram for receiver test using spectrum analyzer                                                                                                               15.3.0
  2019-03          RAN\#83               R5-192541   0622   1     F     Connection diagrams for RRM tests                                                                                                                                     15.3.0
  2019-03          RAN\#83               R5-192542   0646   1     F     Antenna Connection diagram for UE part for RRM                                                                                                                        15.3.0
  2019-03          RAN\#83               R5-192543   0649   1     F     Connection diagram for FR1 demod test cases                                                                                                                           15.3.0
  2019-03          RAN\#83               R5-192705   0645   1     F     Introduction of Non 3GPP Access over WLAN                                                                                                                             15.3.0
  2019-03          RAN\#83               R5-192735   0533   1     F     Correction to PUSCH-Config                                                                                                                                            15.3.0
  2019-03          RAN\#83               R5-192736   0535   1     F     Addition of details on Test State 0                                                                                                                                   15.3.0
  2019-03          RAN\#83               R5-192737   0537   1     F     Correction of CellGroupConfig tables and logical channel identities                                                                                                   15.3.0
  2019-03          RAN\#83               R5-192738   0543   1     F     Additions and updates to UE capability Information Elements                                                                                                           15.3.0
  2019-03          RAN\#83               R5-192739   0544   1     F     Updates and additions of default QoS configurations                                                                                                                   15.3.0
  2019-03          RAN\#83               R5-192740   0566   1     F     Update chapter 4.5 General for PDUs                                                                                                                                   15.3.0
  2019-03          RAN\#83               R5-192741   0567   1     F     Update of Annex C on calculation of test frequencies                                                                                                                  15.3.0
  2019-03          RAN\#83               R5-192742   0619   1     F     Correction to schedulingRequestID Configuration                                                                                                                       15.3.0
  2019-03          RAN\#83               R5-192743   0639   1     F     Addition of Switch/Power UE procedures                                                                                                                                15.3.0
  2019-03          RAN\#83               R5-192744   0640   1     F     Update to Test procedure to check that UE is camped on a new cell belonging to a new TA                                                                               15.3.0
  2019-03          RAN\#83               R5-192745   0641   1     F     Update to Test procedure to check that UE is in state 5GC RRC\_IDLE on a certain cell                                                                                 15.3.0
  2019-03          RAN\#83               R5-192846   0648   1     F     Updates to Annex B to add Permitted OTA Test Methods                                                                                                                  15.3.0
  2019-03          RAN\#83               \-          \-     \-    \-    Editorial updates of table numbering                                                                                                                                  15.3.0
  2019-06          RAN\#84               R5-193537   0680   \-    F     Remove unused DCI formats from 38.508-1                                                                                                                               15.4.0
  2019-06          RAN\#84               R5-193540   0681   \-    F     Adding setup diagram for Receiver performance tests 2x2                                                                                                               15.4.0
  2019-06          RAN\#84               R5-193542   0682   \-    F     Remove brackets from parameters for DCI formats for scheduling                                                                                                        15.4.0
  2019-06          RAN\#84               R5-193613   0691   \-    F     Update default configuration of QuantityConfig                                                                                                                        15.4.0
  2019-06          RAN\#84               R5-193681   0693   \-    F     Update chapter 4.5.3 RRC\_INACTIVE procedures                                                                                                                         15.4.0
  2019-06          RAN\#84               R5-193682   0694   \-    F     Update chapter 4.5.4 RRC\_CONNECTED procedures                                                                                                                        15.4.0
  2019-06          RAN\#84               R5-193683   0695   \-    F     Update chapter 4.5.5 SWITCHED\_OFF procedures                                                                                                                         15.4.0
  2019-06          RAN\#84               R5-193690   0696   \-    F     Resubmission: Connection diagram for 1x2 Demod test cases                                                                                                             15.4.0
  2019-06          RAN\#84               R5-193734   0701   \-    F     Update IE I-RNTI-Value                                                                                                                                                15.4.0
  2019-06          RAN\#84               R5-193735   0702   \-    F     Update IE ShortI-RNTI-Value                                                                                                                                           15.4.0
  2019-06          RAN\#84               R5-193746   0710   \-    F     Update IE SubcarrierSpacing                                                                                                                                           15.4.0
  2019-06          RAN\#84               R5-193813   0711   \-    F     Update of USIM EF5GS3GPPLOCI & EF5GSN3GPPLOCI                                                                                                                         15.4.0
  2019-06          RAN\#84               R5-193828   0713   \-    F     Add IE MultiFrequencyBandListNR-SIB                                                                                                                                   15.4.0
  2019-06          RAN\#84               R5-193829   0714   \-    F     Add IE NR-NS-PmaxList                                                                                                                                                 15.4.0
  2019-06          RAN\#84               R5-193843   0716   \-    F     Update IE ServingCellConfig                                                                                                                                           15.4.0
  2019-06          RAN\#84               R5-193862   0717   \-    F     Corrections to References                                                                                                                                             15.4.0
  2019-06          RAN\#84               R5-193980   0725   \-    F     New test procedure for Registration Reject                                                                                                                            15.4.0
  2019-06          RAN\#84               R5-193981   0726   \-    F     Updates to test procedure 4.9.1                                                                                                                                       15.4.0
  2019-06          RAN\#84               R5-194038   0728   \-    F     Editorial Correction - USIM Profiles for Signaling TC                                                                                                                 15.4.0
  2019-06          RAN\#84               R5-194040   0729   \-    F     Correction to QoS Configuration                                                                                                                                       15.4.0
  2019-06          RAN\#84               R5-194086   0733   \-    F     Update K2 value to align with RF DL RMC                                                                                                                               15.4.0
  2019-06          RAN\#84               R5-194087   0734   \-    F     Update aggregationlevel2 in SearchSpace IE                                                                                                                            15.4.0
  2019-06          RAN\#84               R5-194303   0740   \-    F     TDD-UL-DL-Config for FR1 SCS 60kHz                                                                                                                                    15.4.0
  2019-06          RAN\#84               R5-194359   0742   \-    F     Removal of column for Number of PDU sessions established from tables for Test States                                                                                  15.4.0
  2019-06          RAN\#84               R5-194362   0743   \-    F     Editorial correction to test frequency clauses                                                                                                                        15.4.0
  2019-06          RAN\#84               R5-194364   0744   \-    F     Update of test frequencies for EN-DC combination DC\_41A\_n41A                                                                                                        15.4.0
  2019-06          RAN\#84               R5-194367   0745   \-    F     Common procedure to configure SCC for CA RF testing                                                                                                                   15.4.0
  2019-06          RAN\#84               R5-194369   0746   \-    F     Introduction of test frequencies for inter-band Rel-15 EN-DC two bands configurations                                                                                 15.4.0
                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                              
                                                                                                                                                                                                                                              
  2019-06          RAN\#84               R5-194420   0751   \-    F     Update IE BWP-Downlink                                                                                                                                                15.4.0
  2019-06          RAN\#84               R5-194435   0752   \-    F     Update IE BWP-Id                                                                                                                                                      15.4.0
  2019-06          RAN\#84               R5-194438   0755   \-    F     Updates to UE 4.6.5 Other Information Elements                                                                                                                        15.4.0
  2019-06          RAN\#84               R5-194441   0757   \-    F     Update IE BWP-Uplink                                                                                                                                                  15.4.0
  2019-06          RAN\#84               R5-194479   0758   \-    F     Editorial updates to 4.7.1 Contents of 5GMM messages                                                                                                                  15.4.0
  2019-06          RAN\#84               R5-194480   0759   \-    F     Editorial updates to 4.7.2 Contents of 5GSM messages                                                                                                                  15.4.0
  2019-06          RAN\#84               R5-194510   0762   \-    F     Update of Switch off - Power off procedure in RRC\_CONNECTED                                                                                                          15.4.0
  2019-06          RAN\#84               R5-194539   0767   \-    F     Introduction of test frequencies for EN-DC CA configuration DC\_30A\_n260(A-I)                                                                                        15.4.0
  2019-06          RAN\#84               R5-194541   0768   \-    F     Antenna Connection diagram for TE part for RRM                                                                                                                        15.4.0
  2019-06          RAN\#84               R5-194709   0785   \-    F     Update 38.508 RF and RRM clauses with agreed recommendation to configure UE as non-IMS                                                                                15.4.0
  2019-06          RAN\#84               R5-194783   0774   \-    F     Introduction of test frequencies for NR band n50 and signalling testing                                                                                               15.4.0
  2019-06          RAN\#84               R5-194784   0775   \-    F     Introduction of test frequencies for NR band n74 and signalling testing                                                                                               15.4.0
  2019-06          RAN\#84               R5-194790   0778   \-    F     Updates to power allocations                                                                                                                                          15.4.0
  2019-06          RAN\#84               R5-194791   0779   \-    F     Update of DownlinkConfigCommonSIB                                                                                                                                     15.4.0
  2019-06          RAN\#84               R5-194794   0684   1     F     Update IE PDSCH-Config                                                                                                                                                15.4.0
  2019-06          RAN\#84               R5-194795   0687   1     F     Update NR MeasObjectNR                                                                                                                                                15.4.0
  2019-06          RAN\#84               R5-194796   0690   1     F     Update default configuration of ReportConfigNR                                                                                                                        15.4.0
  2019-06          RAN\#84               R5-194797   0692   1     F     Update chapter 4.5.2 RRC\_IDLE procedures                                                                                                                             15.4.0
  2019-06          RAN\#84               R5-194798   0704   1     F     Correction to the note associated to the Table 4.7.1-2                                                                                                                15.4.0
  2019-06          RAN\#84               R5-194800   0708   1     F     Update IE MIB                                                                                                                                                         15.4.0
  2019-06          RAN\#84               R5-194801   0709   1     F     Update IE SchedulingRequestResourceConfig                                                                                                                             15.4.0
  2019-06          RAN\#84               R5-194802   0712   1     F     Correct clause numbers in 4.5A                                                                                                                                        15.4.0
  2019-06          RAN\#84               R5-194803   0718   1     F     Update IE ServingCellConfigCommon                                                                                                                                     15.4.0
  2019-06          RAN\#84               R5-194804   0721   1     F     Update IE FrequencyInfoUL                                                                                                                                             15.4.0
  2019-06          RAN\#84               R5-194805   0722   1     F     Update IE FrequencyInfoUL-SIB                                                                                                                                         15.4.0
  2019-06          RAN\#84               R5-194806   0723   1     F     Update generic procedures chapter general                                                                                                                             15.4.0
  2019-06          RAN\#84               R5-194807   0724   1     F     Update chapter 4.5.2 RRC\_IDLE Initiation                                                                                                                             15.4.0
  2019-06          RAN\#84               R5-194808   0730   1     F     Updates to RadioBearerConfig                                                                                                                                          15.4.0
  2019-06          RAN\#84               R5-194809   0732   1     F     Updates to PhysicalCellGroupConfig                                                                                                                                    15.4.0
  2019-06          RAN\#84               R5-194810   0739   1     F     New test procedure for RRC\_CONNECTED                                                                                                                                 15.4.0
  2019-06          RAN\#84               R5-194811   0741   1     F     Updated IE MeasObjectEUTRA and ReportConfigInterRAT                                                                                                                   15.4.0
  2019-06          RAN\#84               R5-194812   0753   1     F     Updates to Registration 5GMM messages                                                                                                                                 15.4.0
  2019-06          RAN\#84               R5-194813   0754   1     F     Updates to UE 4.6.4 UE Capability Information Elements                                                                                                                15.4.0
  2019-06          RAN\#84               R5-194814   0760   1     F     New Test procedure for UE for Tracking area updating / inter-system change from N1 mode to S1 mode in 5GMM/EMM-IDLE mode                                              15.4.0
  2019-06          RAN\#84               R5-194817   0777   1     F     New Test procedure for UE for Tracking area updating / inter-system change from S1 mode to N1 mode in 5GMM/EMM-IDLE mode                                              15.4.0
  2019-06          RAN\#84               R5-194821   0780   \-    F     Introducing conditions for Handover in RRCReconfiguration and RadioBearerConfig                                                                                       15.4.0
  2019-06          RAN\#84               R5-194824   0781   \-    F     Updates to Service Request 5GMM message                                                                                                                               15.4.0
  2019-06          RAN\#84               R5-194879   0735   1     F     Updates to Multi-Cell SIG OTA testing for FR2                                                                                                                         15.4.0
  2019-06          RAN\#84               R5-194881   0763   1     F     Introduction of test frequencies for NR CA configuration CA\_n257B                                                                                                    15.4.0
  2019-06          RAN\#84               R5-194882   0764   1     F     Introduction of test frequencies for NR CA configuration CA\_n260B                                                                                                    15.4.0
  2019-06          RAN\#84               R5-194883   0765   1     F     Introduction of test frequencies for NR CA configuration CA\_n260I                                                                                                    15.4.0
  2019-06          RAN\#84               R5-194884   0766   1     F     Introduction of test frequencies for NR CA configuration CA\_n261B                                                                                                    15.4.0
  2019-06          RAN\#84               R5-194885   0782   1     F     Introduction of test frequencies for NR CA configuration CA\_n260(A-I)                                                                                                15.4.0
  2019-06          RAN\#84               R5-194889   0737   1     F     corrections to Non 3GPP Access over WLAN procedures                                                                                                                   15.4.0
  2019-06          RAN\#84               R5-194894   0783   \-    F     Update FFS in ResumeCause                                                                                                                                             15.4.0
  2019-06          RAN\#84               R5-194896   0784   \-    F     Updates to reference QoS configurations for EPS interworking                                                                                                          15.4.0
  2019-06          RAN\#84               R5-194902   0685   1     F     Correction of Setup Diagrams for Receiver tests using Signal Generator in 38.508-1                                                                                    15.4.0
  2019-06          RAN\#84               R5-195095   0750   1     F     Introduction of Connection diagram for 2x4 and 4x4 Demod test cases                                                                                                   15.4.0
  2019-06          RAN\#84               R5-195322   0686   1     F     Update NR SIB1                                                                                                                                                        15.4.0
  2019-06          RAN\#84               R5-195323   0703   1     F     Update IE CommonCellGroupConfig                                                                                                                                       15.4.0
  2019-06          RAN\#84               R5-195324   0715   1     F     Update default configuration of MeasGapConfig                                                                                                                         15.4.0
  2019-06          RAN\#84               R5-195325   0719   1     F     Addition of Switch off / Power off procedure in RRC\_INACTIVE                                                                                                         15.4.0
  2019-06          RAN\#84               R5-195326   0720   1     F     Update of SIB5                                                                                                                                                        15.4.0
  2019-06          RAN\#84               R5-195327   0731   1     F     Updates to RLC-BearerConfig                                                                                                                                           15.4.0
  2019-06          RAN\#84               R5-195328   0756   1     F     Updates to PDU session establishment 5GSM messages                                                                                                                    15.4.0
  2019-06          RAN\#84               R5-195329   0773   1     F     Introduction of test frequencies for inter-RAT signalling testing                                                                                                     15.4.0
  2019-06          RAN\#84               R5-195330   0776   1     F     Correction to PUSCH-Config                                                                                                                                            15.4.0
  2019-06          RAN\#84               R5-195426   0727   2     F     38.508-1 implementation of FR2 UL demod OTA tests using single pol Rx TE                                                                                              15.4.0
  2019-06          RAN\#84               R5-195427   0772   2     F     Addition of message contents needed for DEMOD test cases                                                                                                              15.4.0
  2019-06          RAN\#84               R5-194370   0747   \-    F     Introduction of test frequencies for inter-band Rel-16 EN-DC two bands configurations                                                                                 16.0.0
  2019-06          RAN\#84               R5-194371   0748   \-    F     Introduction of test frequencies for inter-band Rel-16 EN-DC five bands configurations                                                                                16.0.0
  2019-06          RAN\#84               R5-194373   0749   \-    F     Introduction of test frequencies for NR CA configuration CA\_n41C                                                                                                     16.0.0
  2019-09          RAN\#85               R5-195696   0795   \-    F     Update IE PDCP-Config                                                                                                                                                 16.1.0
  2019-09          RAN\#85               R5-195711   0797   \-    F     Add IE CGI-InfoEUTRA                                                                                                                                                  16.1.0
  2019-09          RAN\#85               R5-195729   0798   \-    F     Update IE CGI-Info                                                                                                                                                    16.1.0
  2019-09          RAN\#85               R5-195730   0799   \-    F     Update IE MeasResults                                                                                                                                                 16.1.0
  2019-09          RAN\#85               R5-195731   0800   \-    F     Update of 4.3.1.0A mid test CBW in 38.508-1                                                                                                                           16.1.0
  2019-09          RAN\#85               R5-195747   0803   \-    F     Update IE MeasResultCellListSFTD                                                                                                                                      16.1.0
  2019-09          RAN\#85               R5-195748   0804   \-    F     Add IE MeasResultCellListSFTD-EUTRA                                                                                                                                   16.1.0
  2019-09          RAN\#85               R5-195749   0805   \-    F     Add IE MeasResult2EUTRA                                                                                                                                               16.1.0
  2019-09          RAN\#85               R5-195750   0806   \-    F     Add IE MeasResult2NR                                                                                                                                                  16.1.0
  2019-09          RAN\#85               R5-195751   0807   \-    F     Add IE SK-Counter                                                                                                                                                     16.1.0
  2019-09          RAN\#85               R5-195752   0808   \-    F     Update IE SS-RSSI-Measurement                                                                                                                                         16.1.0
  2019-09          RAN\#85               R5-195792   0811   \-    F     Update MeasurementReport                                                                                                                                              16.1.0
  2019-09          RAN\#85               R5-195885   0814   \-    F     Update RRCResume                                                                                                                                                      16.1.0
  2019-09          RAN\#85               R5-195886   0815   \-    F     Editorial update RRCReconfigurationComplete                                                                                                                           16.1.0
  2019-09          RAN\#85               R5-195887   0816   \-    F     Editorial update RRCReject                                                                                                                                            16.1.0
  2019-09          RAN\#85               R5-195888   0817   \-    F     Editorial update RRCRelease                                                                                                                                           16.1.0
  2019-09          RAN\#85               R5-195889   0818   \-    F     Add SCGFailureInformation                                                                                                                                             16.1.0
  2019-09          RAN\#85               R5-195890   0819   \-    F     Add SCGFailureInformationEUTRA                                                                                                                                        16.1.0
  2019-09          RAN\#85               R5-195895   0820   \-    F     Update UECapabilityEnquiry                                                                                                                                            16.1.0
  2019-09          RAN\#85               R5-195909   0821   \-    F     Editorial update UECapabilityInformation                                                                                                                              16.1.0
  2019-09          RAN\#85               R5-195910   0822   \-    F     Add ULInformationTransferMRDC                                                                                                                                         16.1.0
  2019-09          RAN\#85               R5-195926   0823   \-    F     Editorial update RRC IEs                                                                                                                                              16.1.0
  2019-09          RAN\#85               R5-195927   0824   \-    F     Editorial update S-NSSAI                                                                                                                                              16.1.0
  2019-09          RAN\#85               R5-195944   0826   \-    F     Correction to ReportConfigNR                                                                                                                                          16.1.0
  2019-09          RAN\#85               R5-195945   0827   \-    F     Updates to default configurations for 5GC NAS test cases                                                                                                              16.1.0
  2019-09          RAN\#85               R5-196030   0829   \-    F     Handling of thresholds in FR2 when Events A3 and A6 are inter-frequency                                                                                               16.1.0
  2019-09          RAN\#85               R5-196031   0830   \-    F     Adding references to TS 38.508-1                                                                                                                                      16.1.0
  2019-09          RAN\#85               R5-196136   0836   \-    F     Addition new NR cell for SS-RSRP RRM tests                                                                                                                            16.1.0
  2019-09          RAN\#85               R5-196148   0837   \-    F     Update of Annex C for selecting SSB location for cells not selectable as PCell                                                                                        16.1.0
  2019-09          RAN\#85               R5-196158   0838   \-    F     Correction of references to test frequency tables                                                                                                                     16.1.0
  2019-09          RAN\#85               R5-196159   0839   \-    F     Correction of clause numbers for test frequencies for Non-3GPP Access                                                                                                 16.1.0
  2019-09          RAN\#85               R5-196168   0840   \-    F     Correction of test frequency parameters for SSB location for NR band n1 and SCS 60kHz                                                                                 16.1.0
  2019-09          RAN\#85               R5-196169   0841   \-    F     Correction of test frequency parameters for SSB location for NR band n2 and SCS 60kHz                                                                                 16.1.0
  2019-09          RAN\#85               R5-196170   0842   \-    F     Correction of test frequency parameters for SSB location for NR band n3 and SCS 60kHz                                                                                 16.1.0
  2019-09          RAN\#85               R5-196171   0843   \-    F     Correction of test frequency parameters for SSB location for NR band n7 and SCS 60kHz                                                                                 16.1.0
  2019-09          RAN\#85               R5-196172   0844   \-    F     Correction of test frequency parameters for SSB location for NR band n25 and SCS 60kHz                                                                                16.1.0
  2019-09          RAN\#85               R5-196174   0846   \-    F     Correction of test frequency parameters for SSB location for NR band n38 and SCS 60kHz                                                                                16.1.0
  2019-09          RAN\#85               R5-196175   0847   \-    F     Correction of test frequency parameters for SSB location for NR band n39 and SCS 60kHz                                                                                16.1.0
  2019-09          RAN\#85               R5-196176   0848   \-    F     Correction of test frequency parameters for SSB location for NR band n40 and SCS 60kHz                                                                                16.1.0
  2019-09          RAN\#85               R5-196177   0849   \-    F     Correction of test frequency parameters for SSB location for NR band n41 and SCS 60kHz                                                                                16.1.0
  2019-09          RAN\#85               R5-196178   0850   \-    F     Correction of test frequency parameters for SSB location for NR band n50 and SCS 60kHz                                                                                16.1.0
  2019-09          RAN\#85               R5-196179   0851   \-    F     Correction of test frequency parameters for SSB location for NR band n66 and SCS 60kHz                                                                                16.1.0
  2019-09          RAN\#85               R5-196180   0852   \-    F     Correction of test frequency parameters for SSB location for NR band n70 and SCS 60kHz                                                                                16.1.0
  2019-09          RAN\#85               R5-196181   0853   \-    F     Correction of test frequency parameters for SSB location for NR band n74 and SCS 60kHz                                                                                16.1.0
  2019-09          RAN\#85               R5-196182   0854   \-    F     Correction of test frequency parameters for SSB location for NR band n75 and SCS 15kHz and SCS 60kHz                                                                  16.1.0
  2019-09          RAN\#85               R5-196183   0855   \-    F     Correction of test frequency parameters for SSB location for NR band n77 and SCS 60kHz                                                                                16.1.0
  2019-09          RAN\#85               R5-196184   0856   \-    F     Correction of test frequency parameters for SSB location for NR band n78 and SCS 60kHz                                                                                16.1.0
  2019-09          RAN\#85               R5-196185   0857   \-    F     Correction of test frequency parameters for SSB location for NR band n79 and SCS 60kHz                                                                                16.1.0
  2019-09          RAN\#85               R5-196197   0860   \-    F     Update IE ServingCellConfigCommon                                                                                                                                     16.1.0
  2019-09          RAN\#85               R5-196198   0861   \-    F     Update IE SubcarrierSpacing                                                                                                                                           16.1.0
  2019-09          RAN\#85               R5-196262   0863   \-    F     Editorial update IE RLC-BearerConfig                                                                                                                                  16.1.0
  2019-09          RAN\#85               R5-196289   0864   \-    F     Update chapter 4.5A.2 UE-requested PDU session establishment procedure                                                                                                16.1.0
  2019-09          RAN\#85               R5-196310   0867   \-    F     Addition of SUL bands for protocol testing in clause 6.2.3.1                                                                                                          16.1.0
  2019-09          RAN\#85               R5-196311   0868   \-    F     Update of test frequency parameters for NR CA configuration CA\_n41C                                                                                                  16.1.0
  2019-09          RAN\#85               R5-196315   0872   \-    F     Update of test frequency parameters for NR CA configuration CA\_n260(A-I)                                                                                             16.1.0
  2019-09          RAN\#85               R5-196316   0873   \-    F     Introduction of test frequencies for NR CA configuration CA\_n261B and CA\_n261C                                                                                      16.1.0
  2019-09          RAN\#85               R5-196317   0874   \-    F     Update of test frequency table for EN-DC configuration DC\_41A\_n41A for BCS1                                                                                         16.1.0
  2019-09          RAN\#85               R5-196318   0875   \-    F     Correction of test frequency parameters for EN-DC configuration DC\_(n)41AA                                                                                           16.1.0
  2019-09          RAN\#85               R5-196319   0876   \-    F     Correction of test frequency parameters for EN-DC configuration DC\_(n)71AA                                                                                           16.1.0
  2019-09          RAN\#85               R5-196468   0885   \-    F     Introduction of test frequencies for NR CA configuration CA\_n258B and CA\_n258C                                                                                      16.1.0
  2019-09          RAN\#85               R5-196469   0886   \-    F     Introduction of test frequencies for NR CA configuration CA\_n258G to CA\_n258M                                                                                       16.1.0
  2019-09          RAN\#85               R5-196470   0887   \-    F     Introduction of test frequencies for NR CA configuration CA\_n260G to CA\_n260I                                                                                       16.1.0
  2019-09          RAN\#85               R5-196472   0889   \-    F     Introduction of test frequencies for NR CA configuration CA\_n261G to CA\_n261I                                                                                       16.1.0
  2019-09          RAN\#85               R5-196473   0890   \-    F     Introduction of test frequencies for NR CA configuration CA\_n261O to CA\_n261Q                                                                                       16.1.0
  2019-09          RAN\#85               R5-196490   0894   \-    F     Introduction of test frequencies for NR CA configuration CA\_n78C                                                                                                     16.1.0
  2019-09          RAN\#85               R5-196539   0895   \-    F     Update to 38.508-1 for Demod specific message contents                                                                                                                16.1.0
  2019-09          RAN\#85               R5-196581   0897   \-    F     Removing brackets from values for DCI formats                                                                                                                         16.1.0
  2019-09          RAN\#85               R5-196597   0899   \-    F     Cleanup of editor note of EFOPL5G                                                                                                                                     16.1.0
  2019-09          RAN\#85               R5-196637   0900   \-    F     Update of default messages for EMERGENCY services test scenarios                                                                                                      16.1.0
  2019-09          RAN\#85               R5-196641   0904   \-    F     Update of Test procedure for UE for Tracking area updating / Inter-system change from S1 mode to N1 mode in 5GMM/EMM-IDLE mode                                        16.1.0
  2019-09          RAN\#85               R5-196654   0905   \-    F     Editorial correction of reference test conditions                                                                                                                     16.1.0
  2019-09          RAN\#85               R5-196751   0911   \-    F     AP\#82.01: Update default DCI format to 0\_1 / 1\_1 in TS 38.508-1 for SIG test cases                                                                                 16.1.0
  2019-09          RAN\#85               R5-196824   0917   \-    F     Updates to UE 4.6.4 UE Capability Information Elements                                                                                                                16.1.0
  2019-09          RAN\#85               R5-196825   0918   \-    F     Addition of default test control messages                                                                                                                             16.1.0
  2019-09          RAN\#85               R5-196873   0922   \-    F     Introduction of test frequencies for NR CA configuration CA\_n258D to CA\_n258F                                                                                       16.1.0
  2019-09          RAN\#85               R5-196874   0923   \-    F     Introduction of test frequencies for NR CA configuration CA\_n260D to CA\_n260F                                                                                       16.1.0
  2019-09          RAN\#85               R5-196875   0924   \-    F     Introduction of test frequencies for NR CA configuration CA\_n260O to CA\_n260Q                                                                                       16.1.0
  2019-09          RAN\#85               R5-196942   0927   \-    F     Correction of clause 2 and 4.3 in 38.508-1                                                                                                                            16.1.0
  2019-09          RAN\#85               R5-196980   0786   1     F     Using generic procedure for IMS registration to 5GS                                                                                                                   16.1.0
  2019-09          RAN\#85               R5-196981   0788   1     F     Update of SIB2                                                                                                                                                        16.1.0
  2019-09          RAN\#85               R5-196982   0790   1     F     Update of SIB5                                                                                                                                                        16.1.0
  2019-09          RAN\#85               R5-196984   0792   1     F     Update of frequency definition for Inter-RAT test cases                                                                                                               16.1.0
  2019-09          RAN\#85               R5-196985   0793   1     F     Update IE CellGroupConfig                                                                                                                                             16.1.0
  2019-09          RAN\#85               R5-196986   0858   1     F     Update MIB                                                                                                                                                            16.1.0
  2019-09          RAN\#85               R5-196987   0865   1     F     Update chapter 4.5.4 RRC\_CONNECTED procedures                                                                                                                        16.1.0
  2019-09          RAN\#85               R5-196988   0831   1     F     Addition of IE MasterKeyUpdate                                                                                                                                        16.1.0
  2019-09          RAN\#85               R5-196990   0833   1     F     USIM Configuration for Signalling Test Cases                                                                                                                          16.1.0
  2019-09          RAN\#85               R5-196991   0835   1     F     Correction to SIG OTA UE Orientation procedure                                                                                                                        16.1.0
  2019-09          RAN\#85               R5-196992   0878   1     F     Addition of New Test Procedure - Response\\No response to Paging for 5GC NAS testing                                                                                  16.1.0
  2019-09          RAN\#85               R5-196994   0913   1     F     Update IE ServingCellConfig                                                                                                                                           16.1.0
  2019-09          RAN\#85               R5-196995   0910   1     F     Corrections to DCI\_1\_0 configuration                                                                                                                                16.1.0
  2019-09          RAN\#85               R5-196996   0919   1     F     Updates to generic procedure using SERVICE REQUEST procedure                                                                                                          16.1.0
  2019-09          RAN\#85               R5-196997   0901   1     F     Introduction of Test Procedure for IMS Emergency call establishment in 5GC NORMAL-SERVICE                                                                             16.1.0
  2019-09          RAN\#85               R5-196998   0903   1     F     Update of Test procedure for UE for Tracking area updating / Inter-system change from N1 mode to S1 mode in 5GMM/EMM-IDLE mode                                        16.1.0
  2019-09          RAN\#85               R5-197014   0928   \-    F     Addition of NR CA test frequencies for protocol testing in clause 6.2.3                                                                                               16.1.0
  2019-09          RAN\#85               R5-197099   0929   \-    F     Correction to Switch off-Power off procedure in RRC\_CONNECTED                                                                                                        16.1.0
  2019-09          RAN\#85               R5-197104   0884   1     F     Introduction of test frequencies for NR CA configuration CA\_n257G to CA\_n257M                                                                                       16.1.0
  2019-09          RAN\#85               R5-197106   0892   1     F     Update of EN-DC inter-band configurations in clause 4.3.1                                                                                                             16.1.0
  2019-09          RAN\#85               R5-197139   0891   2     F     Update of NR CA inter-band configurations in clause 4.3.1                                                                                                             16.1.0
  2019-09          RAN\#85               R5-197226   0915   1     F     changes for Non 3GPP Access over WLAN                                                                                                                                 16.1.0
  2019-09          RAN\#85               R5-197230   0883   1     F     Introduction of test frequencies for NR CA configuration CA\_n257D to CA\_n257F                                                                                       16.1.0
  2019-09          RAN\#85               R5-197231   0869   1     F     Update of test frequency parameters for NR CA configuration CA\_n257B and CA\_n257C                                                                                   16.1.0
  2019-09          RAN\#85               R5-197232   0870   1     F     Introduction of test frequencies for NR CA configuration CA\_n260B and CA\_n260C                                                                                      16.1.0
  2019-09          RAN\#85               R5-197233   0888   1     F     Introduction of test frequencies for NR CA configuration CA\_n260J to CA\_n260M                                                                                       16.1.0
  2019-09          RAN\#85               R5-197234   0813   1     F     Update RRCReconfiguration                                                                                                                                             16.1.0
  2019-09          RAN\#85               R5-197235   0796   1     F     Update RadioBearerConfig-DRB                                                                                                                                          16.1.0
  2019-09          RAN\#85               R5-197236   0825   1     F     Update RRCReconfiguration-HO                                                                                                                                          16.1.0
  2019-09          RAN\#85               R5-197241   0791   1     F     Update of EUTRA-AllowedMeasBandwidth                                                                                                                                  16.1.0
  2019-09          RAN\#85               R5-197243   0809   1     F     Addition of Delta to signalling threshold in System Information in FR2                                                                                                16.1.0
  2019-09          RAN\#85               R5-197244   0866   1     F     Correction to REGISTRATION REJECT message                                                                                                                             16.1.0
  2019-09          RAN\#85               R5-197246   0902   1     F     Introduction of Test Procedure for IMS Emergency call establishment in 5GC LIMITED-SERVICE or NO-SUPI                                                                 16.1.0
  2019-09          RAN\#85               R5-197296   0898   2     F     Update of PHR-Config                                                                                                                                                  16.1.0
  2019-09          RAN\#85               R5-197300   0787   1     F     4x2 Connection Diagram for demodulation tests                                                                                                                         16.1.0
  2019-09          RAN\#85               R5-197301   0862   1     F     Correction to Section 5.4.2 Message definition for Performance Test                                                                                                   16.1.0
  2019-09          RAN\#85               R5-197302   0882   1     F     Addition of FR2 CA connection diagram                                                                                                                                 16.1.0
  2019-09          RAN\#85               R5-197303   0920   1     F     Corrections to test frequencies and formulas                                                                                                                          16.1.0
  2019-09          RAN\#85               R5-197304   0896   1     F     Removing IOT bit information from test channel bandwidth tables                                                                                                       16.1.0
  2019-09          RAN\#85               R5-197305   0908   1     F     Addition of SMTC Configuration for RRM test cases                                                                                                                     16.1.0
  2019-09          RAN\#85               R5-197507   0906   1     F     Addition of TDD UL DL Config for RRM test cases                                                                                                                       16.1.0
  2019-09          RAN\#85               R5-197508   0907   1     F     Addition of FilterCoefficient configuration for RRM test cases                                                                                                        16.1.0
  2019-09          RAN\#85               R5-197638   0881   2     F     Addition of FR1 CA connection diagram                                                                                                                                 16.1.0
  2019-10          RAN\#85               \-          \-     \-    \-    Implementation fixes                                                                                                                                                  16.1.1
  2019-12          RAN\#86               R5-197727   0932   \-    F     Editorial update IE BWP-Id                                                                                                                                            16.2.0
  2019-12          RAN\#86               R5-197751   0933   \-    F     Editorial update IE PDSCH-TimeDomainResourceAllocationList                                                                                                            16.2.0
  2019-12          RAN\#86               R5-197835   0937   \-    F     Correction to IE ReportConfigNR                                                                                                                                       16.2.0
  2019-12          RAN\#86               R5-197897   0940   \-    F     Editorial update IE CodebookConfig                                                                                                                                    16.2.0
  2019-12          RAN\#86               R5-197932   0946   \-    F     Editorial update IE PDSCH-Config                                                                                                                                      16.2.0
  2019-12          RAN\#86               R5-197967   0948   \-    F     Update of Annex C on calculation of test frequencies and parameters                                                                                                   16.2.0
  2019-12          RAN\#86               R5-197968   0949   \-    F     Correction of test frequency parameters for NR band n1                                                                                                                16.2.0
  2019-12          RAN\#86               R5-197969   0950   \-    F     Correction of test frequency parameters for NR band n2                                                                                                                16.2.0
  2019-12          RAN\#86               R5-197970   0951   \-    F     Correction of test frequency parameters for NR band n3                                                                                                                16.2.0
  2019-12          RAN\#86               R5-197971   0952   \-    F     Correction of test frequency parameters for NR band n5                                                                                                                16.2.0
  2019-12          RAN\#86               R5-197972   0953   \-    F     Correction of test frequency parameters for NR band n7                                                                                                                16.2.0
  2019-12          RAN\#86               R5-197973   0954   \-    F     Correction of test frequency parameters for NR band n8                                                                                                                16.2.0
  2019-12          RAN\#86               R5-197974   0955   \-    F     Correction of test frequency parameters for NR band n12                                                                                                               16.2.0
  2019-12          RAN\#86               R5-197975   0956   \-    F     Correction of test frequency parameters for NR band n20                                                                                                               16.2.0
  2019-12          RAN\#86               R5-197976   0957   \-    F     Correction of test frequency parameters for NR band n25                                                                                                               16.2.0
  2019-12          RAN\#86               R5-197977   0958   \-    F     Correction of test frequency parameters for NR band n28                                                                                                               16.2.0
  2019-12          RAN\#86               R5-197978   0959   \-    F     Correction of test frequency parameters for NR band n34                                                                                                               16.2.0
  2019-12          RAN\#86               R5-197979   0960   \-    F     Correction of test frequency parameters for NR band n38                                                                                                               16.2.0
  2019-12          RAN\#86               R5-197980   0961   \-    F     Correction of test frequency parameters for NR band n39                                                                                                               16.2.0
  2019-12          RAN\#86               R5-197981   0962   \-    F     Correction of test frequency parameters for NR band n40                                                                                                               16.2.0
  2019-12          RAN\#86               R5-197982   0963   \-    F     Correction of test frequency parameters for NR band n41                                                                                                               16.2.0
  2019-12          RAN\#86               R5-197983   0964   \-    F     Correction of test frequency parameters for NR band n50                                                                                                               16.2.0
  2019-12          RAN\#86               R5-197984   0965   \-    F     Correction of test frequency parameters for NR band n51                                                                                                               16.2.0
  2019-12          RAN\#86               R5-197985   0966   \-    F     Correction of test frequency parameters for NR band n66                                                                                                               16.2.0
  2019-12          RAN\#86               R5-197986   0967   \-    F     Correction of test frequency parameters for NR band n70                                                                                                               16.2.0
  2019-12          RAN\#86               R5-197987   0968   \-    F     Correction of test frequency parameters for NR band n71                                                                                                               16.2.0
  2019-12          RAN\#86               R5-197988   0969   \-    F     Correction of test frequency parameters for NR band n74                                                                                                               16.2.0
  2019-12          RAN\#86               R5-197989   0970   \-    F     Correction of test frequency parameters for NR band n75 (SDL)                                                                                                         16.2.0
  2019-12          RAN\#86               R5-197990   0971   \-    F     Correction of test frequency parameters for NR band n76 (SDL)                                                                                                         16.2.0
  2019-12          RAN\#86               R5-197991   0972   \-    F     Correction of test frequency parameters for NR band n77                                                                                                               16.2.0
  2019-12          RAN\#86               R5-197992   0973   \-    F     Correction of test frequency parameters for NR band n78                                                                                                               16.2.0
  2019-12          RAN\#86               R5-197993   0974   \-    F     Correction of test frequency parameters for NR band n79                                                                                                               16.2.0
  2019-12          RAN\#86               R5-197994   0975   \-    F     Editorial correction to note 1 in frequency tables for NR bands n257, n258, n260 and n261                                                                             16.2.0
  2019-12          RAN\#86               R5-197997   0978   \-    F     Introduction of test frequencies for NR CA configuration CA\_n261D to CA\_n261F                                                                                       16.2.0
  2019-12          RAN\#86               R5-197998   0979   \-    F     Introduction of test frequencies for NR CA configuration CA\_n261J to CA\_n261M                                                                                       16.2.0
  2019-12          RAN\#86               R5-198016   0983   \-    F     Introduction of test frequencies parameters for Rel-16 NR CA configuration CA\_n66B                                                                                   16.2.0
  2019-12          RAN\#86               R5-198017   0984   \-    F     Introduction of test frequencies parameters for Rel-16 NR CA configuration CA\_n66(2A)                                                                                16.2.0
  2019-12          RAN\#86               R5-198018   0985   \-    F     Introduction of test frequencies and parameters for NR band n29                                                                                                       16.2.0
  2019-12          RAN\#86               R5-198019   0986   \-    F     Introduction of test frequencies and parameters for NR band n65                                                                                                       16.2.0
  2019-12          RAN\#86               R5-198028   0988   \-    F     Add 4Rx connection diagram for RRM measurement tests                                                                                                                  16.2.0
  2019-12          RAN\#86               R5-198057   0993   \-    F     Editorial update IE RateMatchPattern                                                                                                                                  16.2.0
  2019-12          RAN\#86               R5-198058   0994   \-    F     Editorial update IE SchedulingRequestResourceConfig                                                                                                                   16.2.0
  2019-12          RAN\#86               R5-198082   0999   \-    F     Introduce general chapter in 4.6                                                                                                                                      16.2.0
  2019-12          RAN\#86               R5-198120   1004   \-    F     Correction of test frequencies parameters for Rel-15 EN-DC configuration DC\_(n)41AA                                                                                  16.2.0
  2019-12          RAN\#86               R5-198121   1005   \-    F     Correction of test frequencies parameters for Rel-15 EN-DC configuration DC\_(n)71AA                                                                                  16.2.0
  2019-12          RAN\#86               R5-198125   1009   \-    F     Introduction of test frequencies and parameters for NR band n48                                                                                                       16.2.0
  2019-12          RAN\#86               R5-198126   1010   \-    F     Introduction of test frequencies for NR band b41 and CBW 30MHz                                                                                                        16.2.0
  2019-12          RAN\#86               R5-198131   1012   \-    F     Update of USIM Configuration 15 for forbidden PLMN                                                                                                                    16.2.0
  2019-12          RAN\#86               R5-198133   1014   \-    F     Update IE ServingCellConfigCommonSIB                                                                                                                                  16.2.0
  2019-12          RAN\#86               R5-198141   1015   \-    F     Clarification on default radio configuration of NAS cells                                                                                                             16.2.0
  2019-12          RAN\#86               R5-198217   1019   \-    F     Correction of test frequency parameters for protocol testing and NR bands with scs=15kHz                                                                              16.2.0
  2019-12          RAN\#86               R5-198223   1021   \-    F     Add IE BetaOffsets                                                                                                                                                    16.2.0
  2019-12          RAN\#86               R5-198224   1022   \-    F     Update IE PUSCH-Config                                                                                                                                                16.2.0
  2019-12          RAN\#86               R5-198250   1023   \-    F     Update IE CSI-FrequencyOccupation                                                                                                                                     16.2.0
  2019-12          RAN\#86               R5-198251   1024   \-    F     Update IE PHR-Config                                                                                                                                                  16.2.0
  2019-12          RAN\#86               R5-198258   1026   \-    F     Editorial update IE DRX-Config                                                                                                                                        16.2.0
  2019-12          RAN\#86               R5-198282   1027   \-    F     Update to Connection diagram for 2x4 and 4x4 Demod test cases                                                                                                         16.2.0
  2019-12          RAN\#86               R5-198286   1028   \-    F     Correction of mapping of frequency ranges to NR test frequencies for NR SA                                                                                            16.2.0
  2019-12          RAN\#86               R5-198304   1029   \-    F     Editorial update IE LogicalChannelConfig                                                                                                                              16.2.0
  2019-12          RAN\#86               R5-198370   1035   \-    F     Connection diagram for FR2 Demod and CSI test cases                                                                                                                   16.2.0
  2019-12          RAN\#86               R5-198480   1039   \-    F     Editorial update IE PDCCH-ConfigCommon                                                                                                                                16.2.0
  2019-12          RAN\#86               R5-198485   1041   \-    F     Editorial update IE PDCP-Config                                                                                                                                       16.2.0
  2019-12          RAN\#86               R5-198506   1044   \-    F     Addition of RRCReconfiguration for Speech call setup                                                                                                                  16.2.0
  2019-12          RAN\#86               R5-198507   1045   \-    F     Editorial updates to section 4.7.0                                                                                                                                    16.2.0
  2019-12          RAN\#86               R5-198508   1046   \-    F     New reference QoS configurations for IMS voice and video                                                                                                              16.2.0
  2019-12          RAN\#86               R5-198509   1047   \-    F     Updates to REGISTRATION ACCEPT 5GMM message                                                                                                                           16.2.0
  2019-12          RAN\#86               R5-198510   1048   \-    F     Updates to test control messages                                                                                                                                      16.2.0
  2019-12          RAN\#86               R5-198540   1051   \-    F     Update of REGISTRATION ACCEPT for IMS emergency support                                                                                                               16.2.0
  2019-12          RAN\#86               R5-198544   1053   \-    F     Update of Table 4.6.3-162 SearchSpace in 38.508-1                                                                                                                     16.2.0
  2019-12          RAN\#86               R5-198638   1058   \-    F     Corrections on test frequencies for NR CA band n260 in 38.508-1                                                                                                       16.2.0
  2019-12          RAN\#86               R5-198649   1059   \-    F     Corrections on test frequencies for NR CA band n261 in 38.508-1                                                                                                       16.2.0
  2019-12          RAN\#86               R5-198659   1062   \-    F     Update TCI State Cell parameter in Demod section                                                                                                                      16.2.0
  2019-12          RAN\#86               R5-198718   1067   \-    F     Updates to RSRP-Range, RSRQ-Range and SINR-Range                                                                                                                      16.2.0
  2019-12          RAN\#86               R5-198847   0941   1     F     Corrections to DCI\_1\_1 configuration                                                                                                                                16.2.0
  2019-12          RAN\#86               R5-198848   0931   1     F     Update IE PUSCH-TimeDomainResourceAllocationList                                                                                                                      16.2.0
  2019-12          RAN\#86               R5-198850   0934   1     F     Correction to IE MasterKeyUpdate                                                                                                                                      16.2.0
  2019-12          RAN\#86               R5-198851   0935   1     F     Update of NR SIBs                                                                                                                                                     16.2.0
  2019-12          RAN\#86               R5-198852   0936   1     F     Correction to USIM configuration                                                                                                                                      16.2.0
  2019-12          RAN\#86               R5-198853   0938   1     F     Correction to IE ReportConfigInterRAT                                                                                                                                 16.2.0
  2019-12          RAN\#86               R5-198854   0942   1     F     Correction to Table 4.9.9.2.3-1 for Inter-system change from S1 mode to N1 mode in 5GMM-IDLE mode                                                                     16.2.0
  2019-12          RAN\#86               R5-198856   0982   1     F     Addition of frequency configurations for NR MFBI testing                                                                                                              16.2.0
  2019-12          RAN\#86               R5-198857   0992   1     F     Editorial update IE CSI-AperiodicTriggerStateList                                                                                                                     16.2.0
  2019-12          RAN\#86               R5-198858   0998   1     F     Editorial update IE ServingCellConfig                                                                                                                                 16.2.0
  2019-12          RAN\#86               R5-198859   1000   1     F     Editorial update IE SecurityAlgorithmConfig                                                                                                                           16.2.0
  2019-12          RAN\#86               R5-198860   1002   1     F     Update IE SRS-Config                                                                                                                                                  16.2.0
  2019-12          RAN\#86               R5-198861   1001   1     F     Update of Generic Test Procedures for IMS Emergency call establishment 4.9.11 and 4.9.12 to reflect the fact that they can be used in multiple states and scenarios   16.2.0
  2019-12          RAN\#86               R5-198862   1013   1     F     Update IE ServingCellConfigCommon                                                                                                                                     16.2.0
  2019-12          RAN\#86               R5-198863   1016   1     F     Update IE CSI-RS-ResourceMapping                                                                                                                                      16.2.0
  2019-12          RAN\#86               R5-198865   1032   1     F     Update RRCReconfiguration                                                                                                                                             16.2.0
  2019-12          RAN\#86               R5-198866   1033   1     F     Update chapter 4.5.1 General                                                                                                                                          16.2.0
  2019-12          RAN\#86               R5-198867   1034   1     F     Update to PDU SESSION ESTABLISHMENT ACCEPT and Reference QoS flow descriptions to align EPS bearer id format                                                          16.2.0
  2019-12          RAN\#86               R5-198869   1061   1     F     New Test Procedures for IMS Emergency call release                                                                                                                    16.2.0
  2019-12          RAN\#86               R5-198870   1063   1     F     Update chapter 4.5.2 RRC\_IDLE                                                                                                                                        16.2.0
  2019-12          RAN\#86               R5-198871   1072   1     F     Update of RRCReconfiguration for measurement configuration                                                                                                            16.2.0
  2019-12          RAN\#86               R5-198955   0995   1     F     Update procedure for NR RF CA testing                                                                                                                                 16.2.0
  2019-12          RAN\#86               R5-198956   0996   1     F     Update procedure for EN-DC RF CA testing                                                                                                                              16.2.0
  2019-12          RAN\#86               R5-198957   1036   1     F     Update to 38.508-1 for DEMOD message contents                                                                                                                         16.2.0
  2019-12          RAN\#86               R5-198958   0991   1     F     Update IE PUCCH-Config                                                                                                                                                16.2.0
  2019-12          RAN\#86               R5-198959   0976   1     F     Introduction of test frequencies for Rel-15 EN-DC inter-band configurations                                                                                           16.2.0
  2019-12          RAN\#86               R5-198960   0980   1     F     Introduction of test frequencies for Rel-16 NR inter-band CA configurations                                                                                           16.2.0
  2019-12          RAN\#86               R5-198961   0987   1     F     Introduction of test frequencies for NR configuration CA\_n29A-n66A                                                                                                   16.2.0
  2019-12          RAN\#86               R5-198962   1003   1     F     Introduction of test frequencies for Rel-15 NR DC configurations                                                                                                      16.2.0
  2019-12          RAN\#86               R5-198997   1068   1     F     Introduction of test frequencies and parameters for NR bands n29, n48 and n65 for protocol testing                                                                    16.2.0
  2019-12          RAN\#86               R5-199008   0997   1     F     Editorial update WLAN table 4.5.2.2-3                                                                                                                                 16.2.0
  2019-12          RAN\#86               R5-199013   0943   1     F     Correction to SMTC and GAP for inter frequency cell                                                                                                                   16.2.0
  2019-12          RAN\#86               R5-199015   0981   1     F     Correction of test frequencies for NR CA and EN-DC protocol testing                                                                                                   16.2.0
  2019-12          RAN\#86               R5-199016   1049   1     F     Updates to Test Procedure 4.9.11                                                                                                                                      16.2.0
  2019-12          RAN\#86               R5-199017   1050   1     F     Updates to Test Procedure 4.9.12                                                                                                                                      16.2.0
  2019-12          RAN\#86               R5-199020   1079   \-    F     Update default setting of deriveSSB-IndexFromCell                                                                                                                     16.2.0
  2019-12          RAN\#86               R5-199021   1011   1     F     Update IE TDD-UL-DL-Config                                                                                                                                            16.2.0
  2019-12          RAN\#86               R5-199022   1070   1     F     Updates to Signalling Reference test conditions                                                                                                                       16.2.0
  2019-12          RAN\#86               R5-199026   1025   2     F     Update IE CellGroupConfig                                                                                                                                             16.2.0
  2019-12          RAN\#86               R5-199071   0944   2     F     Update of SUL related messages                                                                                                                                        16.2.0
  2019-12          RAN\#86               R5-199075   1080   1     F     Correction to NR RRC\_IDLE mode procedure                                                                                                                             16.2.0
  2019-12          RAN\#86               R5-199093   1065   2     F     Update chapter 4.5.4 RRC\_CONNECTED                                                                                                                                   16.2.0
  2019-12          RAN\#86               R5-199094   1069   1     F     Updates for handling of Multiple PDU sessions / Multiple DRBs                                                                                                         16.2.0
  2019-12          RAN\#86               R5-199103   1076   2     F     Adding new generic procedure for UE-requested PDU session modification after the first S1 to N1 mode change                                                           16.2.0
  2019-12          RAN\#86               R5-199300   1042   1     F     Corrections on category of EN-DC configurations for test frequencies in 38.508-1                                                                                      16.2.0
  2019-12          RAN\#86               R5-199301   1054   1     F     Addition of ServingCellConfigCommon for RRM tests                                                                                                                     16.2.0
  2019-12          RAN\#86               R5-199302   1057   1     F     Corrections on test frequencies for NR CA band n257 in 38.508-1                                                                                                       16.2.0
  2019-12          RAN\#86               R5-199303   1060   1     F     Corrections on test frequencies for NR CA band n258 in 38.508-1                                                                                                       16.2.0
  2019-12          RAN\#86               R5-199304   1066   1     F     Update Radio resource control information elements for RRM to add CSI-RS for Tracking                                                                                 16.2.0
  2019-12          RAN\#86               R5-199423   1077   \-    F     Update ra-responseWindow in TS 38.508-1                                                                                                                               16.2.0
  2019-12          RAN\#86               R5-199481   0989   1     F     Addition of FR1 NR CA and NR 4Rx connection diagrams                                                                                                                  16.2.0
  2019-12          RAN\#86               R5-199511   1078   \-    F     Update of quiet zone size                                                                                                                                             16.2.0
  2019-12          RAN\#86               R5-199545   1020   1     F     Addition of multi-AoA capabilities for IFF                                                                                                                            16.2.0
  2020-03          RAN\#87               R5-200135   1120         F     Removal of Correction to SIG OTA UE Orientation procedure                                                                                                             16.3.0
  2020-03          RAN\#87               R5-200147   1130         F     Update to USIM config 6.4.1-11                                                                                                                                        16.3.0
  2020-03          RAN\#87               R5-200244   1133         F     Correction to nAndPagingFrameOffset                                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200296   1136         F     Addition of generic procedure for IMS MO speech setup                                                                                                                 16.3.0
  2020-03          RAN\#87               R5-200297   1137         F     Addition of generic procedure for IMS MT speech setup                                                                                                                 16.3.0
  2020-03          RAN\#87               R5-200298   1138         F     Addition of generic procedure for IMS MO call release                                                                                                                 16.3.0
  2020-03          RAN\#87               R5-200299   1139         F     Addition of generic procedure for IMS MT call release                                                                                                                 16.3.0
  2020-03          RAN\#87               R5-200349   1142         F     Correction to frequencyBandList in SIB4                                                                                                                               16.3.0
  2020-03          RAN\#87               R5-200431   1146         F     Correction to CSI-FrequencyOccupation                                                                                                                                 16.3.0
  2020-03          RAN\#87               R5-200432   1147         F     Correction to default setting of additionalPmax                                                                                                                       16.3.0
  2020-03          RAN\#87               R5-200433   1148         F     Correction to powerControlOffset for performance tests                                                                                                                16.3.0
  2020-03          RAN\#87               R5-200434   1149         F     Correction to RACH configuration for RRM tests                                                                                                                        16.3.0
  2020-03          RAN\#87               R5-200435   1150         F     Correction to TDD UL-DL Config for performance test cases                                                                                                             16.3.0
  2020-03          RAN\#87               R5-200477   1154         F     Update to Registration REQ and Authentication Response message                                                                                                        16.3.0
  2020-03          RAN\#87               R5-200499   1157         F     Correction of test frequency tables for NR band n1                                                                                                                    16.3.0
  2020-03          RAN\#87               R5-200500   1158         F     Correction of test frequency tables for NR band n2                                                                                                                    16.3.0
  2020-03          RAN\#87               R5-200501   1159         F     Correction of test frequency tables for NR band n3                                                                                                                    16.3.0
  2020-03          RAN\#87               R5-200502   1160         F     Correction of test frequency tables for NR band n7                                                                                                                    16.3.0
  2020-03          RAN\#87               R5-200503   1161         F     Correction of test frequency tables for NR band n25                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200504   1162         F     Correction of test frequency tables for NR band n28                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200505   1163         F     Correction of test frequency tables for NR band n34                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200506   1164         F     Correction of test frequency tables for NR band n38                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200507   1165         F     Correction of test frequency tables for NR band n39                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200508   1166         F     Correction of test frequency tables for NR band n40                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200510   1168         F     Correction of test frequency tables for NR band n50                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200511   1169         F     Correction of test frequency tables for NR band n66                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200512   1170         F     Correction of test frequency tables for NR band n70                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200513   1171         F     Correction of test frequency tables for NR band n71                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200514   1172         F     Correction of test frequency tables for NR band n74                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200515   1173         F     Correction of test frequency tables for NR band n75                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200531   1189         F     Correction of test frequency tables for NR band n29                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200532   1190         F     Correction of test frequency tables for NR band n48                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200533   1191         F     Correction of test frequency tables for NR band n65                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200597   1200         F     Introduction of test frequencies for inter-band Rel-16 EN-DC configurations in 38.508-1                                                                               16.3.0
  2020-03          RAN\#87               R5-200605   1202         F     Addition of test frequencies for n95 SUL band                                                                                                                         16.3.0
  2020-03          RAN\#87               R5-200645   1206         F     Updates to 4.6.4 UE Capability Information Elements                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200646   1207         F     Correction to QoS rule number 7                                                                                                                                       16.3.0
  2020-03          RAN\#87               R5-200647   1208         F     Correction to IMS emergency call release procedures                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-201246   1209   1     F     TRS configuration messages definition for RF in 38.508-1                                                                                                              16.3.0
  2020-03          RAN\#87               R5-200678   1210         F     Update of IE ControlResourceSet to introduce band and channel bandwidth specific values for frequencyDomainResources                                                  16.3.0
  2020-03          RAN\#87               R5-200703   1213         F     Correction to IE BeamFailureRecoveryConfig                                                                                                                            16.3.0
  2020-03          RAN\#87               R5-200774   1215         F     Editorial update IE MeasConfig                                                                                                                                        16.3.0
  2020-03          RAN\#87               R5-200775   1216         F     Editorial update IE radioLinkMonitoringRS-Id                                                                                                                          16.3.0
  2020-03          RAN\#87               R5-200804   1218         F     Correction of test frequency tables for NR band n5                                                                                                                    16.3.0
  2020-03          RAN\#87               R5-200805   1219         F     Correction of test frequency tables for NR band n8                                                                                                                    16.3.0
  2020-03          RAN\#87               R5-200806   1220         F     Correction of test frequency tables for NR band n12                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200807   1221         F     Correction of test frequency tables for NR band n20                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200808   1222         F     Correction of test frequency tables for NR band n51                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200900   1197   1     F     Corrections on test frequencies for EN-DC band combinations including FR1 and FR2 in 38.508-1                                                                         16.3.0
  2020-03          RAN\#87               R5-200901   1198   1     F     Corrections on test frequencies for EN-DC band combinations including FR2 in 38.508-1                                                                                 16.3.0
  2020-03          RAN\#87               R5-200902   1199   1     F     Corrections on uplink EN-DC configurations for test frequencies in 38.508-1                                                                                           16.3.0
  2020-03          RAN\#87               R5-200921   1132   1     F     Addition of Rel-16 inter-band CA and EN-DC FR1 two bands test configurations                                                                                          16.3.0
  2020-03          RAN\#87               R5-200930   1081   1     F     Update SIB1                                                                                                                                                           16.3.0
  2020-03          RAN\#87               R5-200931   1082   1     F     Update CounterCheck                                                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200932   1083   1     F     Editorial update DLInformationTransfer                                                                                                                                16.3.0
  2020-03          RAN\#87               R5-200933   1084   1     F     Editorial update FailureInformation                                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200934   1085   1     F     Editorial update MeasurementReport                                                                                                                                    16.3.0
  2020-03          RAN\#87               R5-200935   1086   1     F     Editorial update MobilityFromNRCommand                                                                                                                                16.3.0
  2020-03          RAN\#87               R5-200936   1087   1     F     Editorial update Paging                                                                                                                                               16.3.0
  2020-03          RAN\#87               R5-200937   1088   1     F     Editorial update RRCReestablishment                                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200938   1090   1     F     Editorial update RRCReconfigurationComplete                                                                                                                           16.3.0
  2020-03          RAN\#87               R5-200939   1091   1     F     Editorial update RRCReject                                                                                                                                            16.3.0
  2020-03          RAN\#87               R5-200940   1092   1     F     Editorial update RRCRelease                                                                                                                                           16.3.0
  2020-03          RAN\#87               R5-200941   1093   1     F     Editorial update RRCResumeComplete                                                                                                                                    16.3.0
  2020-03          RAN\#87               R5-200942   1094   1     F     Editorial update RRCSetup                                                                                                                                             16.3.0
  2020-03          RAN\#87               R5-200943   1096   1     F     Editorial update SCGFailureInformation                                                                                                                                16.3.0
  2020-03          RAN\#87               R5-200944   1097   1     F     Editorial update SecurityMode                                                                                                                                         16.3.0
  2020-03          RAN\#87               R5-200945   1098   1     F     Update SystemInformation                                                                                                                                              16.3.0
  2020-03          RAN\#87               R5-200946   1099   1     F     Editorial update UEAssistanceInformation                                                                                                                              16.3.0
  2020-03          RAN\#87               R5-200947   1100   1     F     Editorial update UECapability                                                                                                                                         16.3.0
  2020-03          RAN\#87               R5-200948   1101   1     F     Editorial update ULInformation                                                                                                                                        16.3.0
  2020-03          RAN\#87               R5-200949   1103   1     F     Editorial update IE RLC-BearerConfig                                                                                                                                  16.3.0
  2020-03          RAN\#87               R5-200951   1108   1     F     Add IE TDD-UL-DL-ConfigDedicated                                                                                                                                      16.3.0
  2020-03          RAN\#87               R5-200952   1111   1     F     Update IE ServingCellConfig                                                                                                                                           16.3.0
  2020-03          RAN\#87               R5-200953   1112   1     F     Update IE ServingCellConfigCommonSIB                                                                                                                                  16.3.0
  2020-03          RAN\#87               R5-200954   1113   1     F     Update IE DMRS-DownlinkConfig                                                                                                                                         16.3.0
  2020-03          RAN\#87               R5-200955   1114   1     F     Update IE FrequencyInfoUL                                                                                                                                             16.3.0
  2020-03          RAN\#87               R5-200956   1118   1     F     Update chapter 4.5.1 General                                                                                                                                          16.3.0
  2020-03          RAN\#87               R5-200957   1122   1     F     Update chapter 4.5.4 RRC\_CONNECTED                                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-200958   1125   1     F     Update IE CellGroupId                                                                                                                                                 16.3.0
  2020-03          RAN\#87               R5-200959   1126   1     F     Update IE ServCellIndex                                                                                                                                               16.3.0
  2020-03          RAN\#87               R5-200960   1127   1     F     Update IE SK-Counter                                                                                                                                                  16.3.0
  2020-03          RAN\#87               R5-200961   1128   1     F     Update IE SDAP-Config                                                                                                                                                 16.3.0
  2020-03          RAN\#87               R5-200965   1145   1     F     Correction to CORESET and search space configuration                                                                                                                  16.3.0
  2020-03          RAN\#87               R5-200966   1193   1     F     Addition of NR SUL connection diagrams                                                                                                                                16.3.0
  2020-03          RAN\#87               R5-200967   1201   1     F     Clarification to high test channel bandwidth table                                                                                                                    16.3.0
  2020-03          RAN\#87               R5-200968   1203   1     F     Addition of missing EN-DC test frequencies                                                                                                                            16.3.0
  2020-03          RAN\#87               R5-200996   1124   1     F     Correction to PUCCH-Config for Format1 and Format2                                                                                                                    16.3.0
  2020-03          RAN\#87               R5-201005   1131   1     F     Update of Annex C on calculation of test frequencies to achieve full bandwidth testing of NR bands                                                                    16.3.0
  2020-03          RAN\#87               R5-201020   1155   1     F     Update SIG test frequencies in clause 6.2.3.x                                                                                                                         16.3.0
  2020-03          RAN\#87               R5-201021   1167   1     F     Correction of test frequency tables for NR band n41                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-201022   1174   1     F     Correction of test frequency tables for NR band n77                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-201023   1175   1     F     Correction of test frequency tables for NR band n78                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-201024   1176   1     F     Correction of test frequency tables for NR band n79                                                                                                                   16.3.0
  2020-03          RAN\#87               R5-201025   1177   1     F     Correction of test frequency tables for NR band n257                                                                                                                  16.3.0
  2020-03          RAN\#87               R5-201026   1178   1     F     Correction of test frequency tables for NR band n258                                                                                                                  16.3.0
  2020-03          RAN\#87               R5-201027   1179   1     F     Correction of test frequency tables for NR band n260                                                                                                                  16.3.0
  2020-03          RAN\#87               R5-201028   1180   1     F     Correction of test frequency tables for NR band n261                                                                                                                  16.3.0
  2020-03          RAN\#87               R5-201029   1192   1     F     Update of clause 4.4.2 on simulated cells                                                                                                                             16.3.0
  2020-03          RAN\#87               R5-201061   1153   1     F     Addition of a few R16s inter-band EN-DC FR1 test configurations                                                                                                       16.3.0
  2020-03          RAN\#87               R5-201065   1194   1     F     Addition of test channel bandwidth for NR bands in 38.508-1                                                                                                           16.3.0
  2020-03          RAN\#87               R5-201092   1123   1     F     Updates to NR FR1 and LTE Power levels in OTA                                                                                                                         16.3.0
  2020-03          RAN\#87               R5-201093   1224   1     F     Message content Updates for Carrier Aggregation                                                                                                                       16.3.0
  2020-03          RAN\#87               R5-201108   1143   1     F     Correction to EUTRA-AllowedMeasBandwidth                                                                                                                              16.3.0
  2020-03          RAN\#87               R5-201116   1204   1     F     Updates to 4.7.3 Contents of EAP-AKA messages in 38.508-1                                                                                                             16.3.0
  2020-03          RAN\#87               R5-201148   1134   1     F     Updates to default SSB index of intra-frequency NR cells                                                                                                              16.3.0
  2020-03          RAN\#87               R5-201159   1151   1     F     Correction to test frequencies for n257 intra-band contiguous CA                                                                                                      16.3.0
  2020-03          RAN\#87               R5-201173   1117   1     F     Update IE TDD-UL-DL-Config                                                                                                                                            16.3.0
  2020-03          RAN\#87               R5-201174   1095   1     F     Update RRCSystemInfoRequest                                                                                                                                           16.3.0
  2020-03          RAN\#87               R5-201175   1106   1     F     Update IE RLF-TimersAndConstants                                                                                                                                      16.3.0
  2020-03          RAN\#87               R5-201176   1107   1     F     Update IE SCS-SpecificCarrier                                                                                                                                         16.3.0
  2020-03          RAN\#87               R5-201177   1109   1     F     Update chapter 4.6.0                                                                                                                                                  16.3.0
  2020-03          RAN\#87               R5-201179   1116   1     F     Update IE MeasObjectNR                                                                                                                                                16.3.0
  2020-03          RAN\#87               R5-201189   1214   1     F     Addition of IFF DFF Hybrid Setup for FR2 2AoA RRM test                                                                                                                16.3.0
  2020-03          RAN\#87               R5-201194   1141   1     F     Update to Common Coreset RB IE and section 5-6 Demod message contents                                                                                                 16.3.0
  2020-03          RAN\#87               R5-201195   1144   1     F     Update of DCI 1\_0 and DCI\_1\_1 configuration                                                                                                                        16.3.0
  2020-03          RAN\#87               R5-201197   1152   1     F     Correction to TRS configuration for RRM tests                                                                                                                         16.3.0
  2020-03          RAN\#87               R5-201202   1205   1     F     Update to Switch Off/ Power off procedure in RRC\_CONNECTED mode                                                                                                      16.3.0
  2020-03          RAN\#87               R5-201203   1129   1     F     Update to PDCP-Config                                                                                                                                                 16.3.0
  2020-03          RAN\#87               R5-201217   1217   1     F     Updates to PsDU session modification procedures                                                                                                                       16.3.0
  2020-03          RAN\#87               R5-201221   1089   1     F     Update RRCReconfiguration                                                                                                                                             16.3.0
  2020-03          RAN\#87               R5-201222   1121   1     F     Update IE CellGroupConfig                                                                                                                                             16.3.0
  2020-03          RAN\#87               R5-201232   1140   2     F     CR to 38.508-1 to introduce DFF Range Length                                                                                                                          16.3.0
  2020-03          RAN\#87               R5-201234   1110   2     F     Update IE ServingCellConfigCommon                                                                                                                                     16.3.0
  2020-03          RAN\#87               R5-201148   1134   1     F     Add new missing column of Table 4.4.2-2                                                                                                                               16.3.1
  2020-06          RAN\#88               R5-201320   1225   \-    F     Update IE CellGroupConfig                                                                                                                                             16.4.0
  2020-06          RAN\#88               R5-201322   1227   \-    F     Update of default value of frequencyDomainResources in ControlResourceSet IE                                                                                          16.4.0
  2020-06          RAN\#88               R5-201331   1228   \-    F     Correction to Table 4.9.6.1-1-Switch off in Idle                                                                                                                      16.4.0
  2020-06          RAN\#88               R5-201333   1230   \-    F     Addition of 4.9.6.3A Switch off Power off procedure in RRC\_CONNECTED with T3540 started                                                                              16.4.0
  2020-06          RAN\#88               R5-201335   1232   \-    F     Update to USIM config 6.4.1-1                                                                                                                                         16.4.0
  2020-06          RAN\#88               R5-201336   1233   \-    F     Update to USIM Table 6.4.1-10                                                                                                                                         16.4.0
  2020-06          RAN\#88               R5-201337   1234   \-    F     Correction to Table 7.3.1-7 NZP-CSI-RS-Resource for TRS                                                                                                               16.4.0
  2020-06          RAN\#88               R5-201446   1235   \-    F     Fixing wrong reference for RRC\_CONNECTED state on WLAN access                                                                                                        16.4.0
  2020-06          RAN\#88               R5-201572   1253   \-    F     Corrections to default content of DCI messages                                                                                                                        16.4.0
  2020-06          RAN\#88               RP-201138   1258   1     F     Correction to IE SearchSpace                                                                                                                                          16.4.0
  2020-06          RAN\#88               R5-201731   1265   \-    F     Addition of NR SUL connection diagram in A.3.1.4                                                                                                                      16.4.0
  2020-06          RAN\#88               R5-201800   1267   \-    F     Addition of USIM configuration for TC 6.3.1.8 and TC 6.3.1.9                                                                                                          16.4.0
  2020-06          RAN\#88               R5-201837   1268   \-    F     Update of test channel bandwidths for band n48                                                                                                                        16.4.0
  2020-06          RAN\#88               R5-201932   1271   \-    F     Removing brackets from mid test channel BWs for FR2                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-201956   1273   \-    F     Correction of clause 4.4.2 on simulated cells                                                                                                                         16.4.0
  2020-06          RAN\#88               R5-201958   1275   \-    F     Correction to Annex C on calculation of kSSB to align SSB and RMSI subcarriers                                                                                        16.4.0
  2020-06          RAN\#88               R5-201959   1276   \-    F     Removal of definition of frequencyDomainResources value dependent on CORESET\#0 configuration in Annex C.                                                             16.4.0
  2020-06          RAN\#88               R5-201961   1278   \-    F     Correction of test frequency tables for NR band n1                                                                                                                    16.4.0
  2020-06          RAN\#88               R5-201962   1279   \-    F     Correction of test frequency tables for NR band n2                                                                                                                    16.4.0
  2020-06          RAN\#88               R5-201963   1280   \-    F     Correction of test frequency tables for NR band n3                                                                                                                    16.4.0
  2020-06          RAN\#88               R5-201964   1281   \-    F     Correction of test frequency tables for NR band n5                                                                                                                    16.4.0
  2020-06          RAN\#88               R5-201965   1282   \-    F     Correction of test frequency tables for NR band n7                                                                                                                    16.4.0
  2020-06          RAN\#88               R5-201966   1283   \-    F     Correction of test frequency tables for NR band n8                                                                                                                    16.4.0
  2020-06          RAN\#88               R5-201967   1284   \-    F     Correction of test frequency tables for NR band n12                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-201968   1285   \-    F     Correction of test frequency tables for NR band n20                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-201969   1286   \-    F     Correction of test frequency tables for NR band n25                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-201970   1287   \-    F     Correction of test frequency tables for NR band n28                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-201971   1288   \-    F     Correction of test frequency tables for NR band n34                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-201972   1289   \-    F     Correction of test frequency tables for NR band n38                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-201973   1290   \-    F     Correction of test frequency tables for NR band n39                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-201974   1291   \-    F     Correction of test frequency tables for NR band n40                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-201975   1292   \-    F     Correction of test frequency tables for NR band n41                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-201976   1293   \-    F     Correction of test frequency tables for NR band n50                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-201977   1294   \-    F     Correction of test frequency tables for NR band n51                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-201978   1295   \-    F     Correction of test frequency tables for NR band n66                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-201979   1296   \-    F     Correction of test frequency tables for NR band n70                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-201980   1297   \-    F     Correction of test frequency tables for NR band n71                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-201981   1298   \-    F     Correction of test frequency tables for NR band n74                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-201982   1299   \-    F     Correction of test frequency tables for NR band n77                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-201983   1300   \-    F     Correction of test frequency tables for NR band n78                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-201984   1301   \-    F     Correction of test frequency tables for NR band n79                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-201989   1306   \-    F     Corrections of test frequency tables for CA\_n41C                                                                                                                     16.4.0
  2020-06          RAN\#88               R5-201990   1307   \-    F     Corrections of test frequency tables for CA\_n78C                                                                                                                     16.4.0
  2020-06          RAN\#88               R5-201991   1308   \-    F     Editorial correction to test frequency clause numbering                                                                                                               16.4.0
  2020-06          RAN\#88               R5-201995   1312   \-    F     Correction of test frequency tables for CA\_n66B                                                                                                                      16.4.0
  2020-06          RAN\#88               R5-201997   1314   \-    F     Introduction of test frequencies for NR band n26                                                                                                                      16.4.0
  2020-06          RAN\#88               R5-201998   1315   \-    F     Introduction of test frequencies for NR band 26 for protocol testing                                                                                                  16.4.0
  2020-06          RAN\#88               R5-201999   1316   \-    F     Correction of test frequency tables for NR band n29                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-202000   1317   \-    F     Correction of test frequency tables for NR band n48                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-202001   1318   \-    F     Correction of test frequency tables for NR band n65                                                                                                                   16.4.0
  2020-06          RAN\#88               R5-202024   1327   \-    F     Update IE PDCP-Config                                                                                                                                                 16.4.0
  2020-06          RAN\#88               R5-202123   1330   \-    F     CR to 38.508-1 to clarify the test zone/quiet zone                                                                                                                    16.4.0
  2020-06          RAN\#88               R5-202186   1333   \-    F     Addition of locationAndBandwidth in BWP for FR1 in 38.508-1                                                                                                           16.4.0
  2020-06          RAN\#88               R5-202210   1335   \-    F     Corrections on test frequencies for inter-band EN-DC configurations within FR1 for five bands in 38.508-1                                                             16.4.0
  2020-06          RAN\#88               R5-202212   1336   \-    F     Corrections of test frequency tables for CA\_n257x                                                                                                                    16.4.0
  2020-06          RAN\#88               R5-202213   1337   \-    F     Corrections of test frequency tables for CA\_n258x                                                                                                                    16.4.0
  2020-06          RAN\#88               R5-202214   1338   \-    F     Corrections of test frequency tables for CA\_n260x                                                                                                                    16.4.0
  2020-06          RAN\#88               R5-202215   1339   \-    F     Corrections of test frequency tables for CA\_n261x                                                                                                                    16.4.0
  2020-06          RAN\#88               R5-202244   1343   \-    F     Correction to nrofRBs under TRS CSI-FrequencyOccupation for Demod test cases with 10 MHz CBW                                                                          16.4.0
  2020-06          RAN\#88               R5-202284   1351   \-    F     Correction to configuration bwp-id parameter in TCI-State IE                                                                                                          16.4.0
  2020-06          RAN\#88               R5-202409   1354   \-    F     Update PDCCH-ControlResourceSet for RRM testing                                                                                                                       16.4.0
  2020-06          RAN\#88               R5-202410   1355   \-    F     Addition Physical Layer Parameter section for RRM testing                                                                                                             16.4.0
  2020-06          RAN\#88               R5-202449   1356   \-    F     Correction of test frequencies for DC n71AA                                                                                                                           16.4.0
  2020-06          RAN\#88               R5-202486   1358   \-    F     Correction to content of EF5GSN3GPPLOCI                                                                                                                               16.4.0
  2020-06          RAN\#88               R5-202525   1360   \-    F     Correction to System Information Combination for PWS                                                                                                                  16.4.0
  2020-06          RAN\#88               R5-202531   1353   1     F     Addition of R16 new channel bandwidths for n1 in 38.508-1                                                                                                             16.4.0
  2020-06          RAN\#88               R5-202534   1266   1     F     Removal of USIM configuration 14                                                                                                                                      16.4.0
  2020-06          RAN\#88               R5-202549   1350   1     F     Aligning the tabular representation of ASN.1 with PRD13 sections 4.8 and 5                                                                                            16.4.0
  2020-06          RAN\#88               R5-202554   1252   1     F     Updates to PDCCH-ConfigCommon                                                                                                                                         16.4.0
  2020-06          RAN\#88               R5-202561   1226   1     F     Update IE default content for control resource set establishment and common search space mapping                                                                      16.4.0
  2020-06          RAN\#88               R5-202562   1229   1     F     Update to 4.9.6.3 Switch off Power off procedure in RRC\_CONNECTED                                                                                                    16.4.0
  2020-06          RAN\#88               R5-202563   1231   1     F     Correction to Table 4.9.7.2.3-1-Tracking Area Update Request                                                                                                          16.4.0
  2020-06          RAN\#88               R5-202564   1236   1     F     Correction to Table 4.5.2.2-2-Adding second SMC procedure for Selected EPS NAS security algorithms IE                                                                 16.4.0
  2020-06          RAN\#88               R5-202565   1237   1     F     Clarification to ROUND for negative Threshold values in SIB1 and SIB4                                                                                                 16.4.0
  2020-06          RAN\#88               R5-202573   1251   1     F     Updates to test frequency definitions for SDL NR bands                                                                                                                16.4.0
  2020-06          RAN\#88               R5-202574   1257   1     F     Correction to condition SRB\_NR\_PDCP in RadioBearerConfig                                                                                                            16.4.0
  2020-06          RAN\#88               R5-202575   1260   1     F     Correction to UECapabilityEnquiry in case of EN-DC interband CA                                                                                                       16.4.0
  2020-06          RAN\#88               R5-202576   1262   1     F     Updates to PDCP-Config                                                                                                                                                16.4.0
  2020-06          RAN\#88               R5-202577   1274   1     F     Clarifications of Annex C on calculation of test frequencies                                                                                                          16.4.0
  2020-06          RAN\#88               R5-202578   1277   1     F     Update SIG test frequencies in clause 6.2.3.x                                                                                                                         16.4.0
  2020-06          RAN\#88               R5-202579   1302   1     F     Correction of test frequency tables for NR band n257                                                                                                                  16.4.0
  2020-06          RAN\#88               R5-202580   1303   1     F     Correction of test frequency tables for NR band n258                                                                                                                  16.4.0
  2020-06          RAN\#88               R5-202581   1304   1     F     Correction of test frequency tables for NR band n260                                                                                                                  16.4.0
  2020-06          RAN\#88               R5-202582   1305   1     F     Correction of test frequency tables for NR band n261                                                                                                                  16.4.0
  2020-06          RAN\#88               R5-202583   1322   1     F     Introduction of protocol testing applicability for EN-DC inter-band, NR-CA inter-band and NR DC test frequency tables                                                 16.4.0
  2020-06          RAN\#88               R5-202585   1331   1     F     Correction to Reference QoS rules                                                                                                                                     16.4.0
  2020-06          RAN\#88               R5-202586   1346   1     F     Updates to Generic Test Procedure for IMS MT speech call establishment                                                                                                16.4.0
  2020-06          RAN\#88               R5-202587   1347   1     F     Updates to Generic Test Procedure for IMS MO call release                                                                                                             16.4.0
  2020-06          RAN\#88               R5-202588   1349   1     F     Aligning the tabular representation of ASN.1 with PRD13 section 4.6                                                                                                   16.4.0
  2020-06          RAN\#88               R5-202589   1359   1     F     Update the default USIM configurations                                                                                                                                16.4.0
  2020-06          RAN\#88               R5-202590   1361   1     F     Addition of Generic procedure to check user plane connectivity for CA tests                                                                                           16.4.0
  2020-06          RAN\#88               R5-202703   1255   1     F     Clarifications on the QoQZ validation procedure for RRM                                                                                                               16.4.0
  2020-06          RAN\#88               R5-202708   1254   1     F     TRS - PowerControlOffset correction for UE RF testing                                                                                                                 16.4.0
  2020-06          RAN\#88               R5-202820   1352   1     F     Correction to PRB-Id for secondHopPRB                                                                                                                                 16.4.0
  2020-06          RAN\#88               R5-202859   1329   1     F     Updates on FR2 inter-band EN-DC configurations for test frequencies in 38.508-1                                                                                       16.4.0
  2020-06          RAN\#88               R5-202879   1332   1     F     Addition of BW to Table 4.6.3-33                                                                                                                                      16.4.0
  2020-06          RAN\#88               R5-202880   1334   1     F     Clarification of disabling Tx diversity for FR2 UE                                                                                                                    16.4.0
  2020-06          RAN\#88               R5-202881   1341   1     F     Restructuring 38.508-1 message contents for Demod and CSI reporting test cases                                                                                        16.4.0
  2020-06          RAN\#88               R5-202882   1342   1     F     Update of PUCCH-ResourceId for Demod test cases                                                                                                                       16.4.0
  2020-06          RAN\#88               R5-202883   1348   1     F     Configuration of p-ZP-CSI-RS-ResourceSet for PDSCH Demod test cases                                                                                                   16.4.0
  2020-06          RAN\#88               R5-202956   1270   1     F     Update of default test channel BW                                                                                                                                     16.4.0
  2020-06          RAN\#88               R5-202962   1269   2     F     Updating DCI related messages                                                                                                                                         16.4.0
  2020-06          RAN\#88               R5-202967   1344   1     F     Update to default value of PDSCH-to-HARQ\_feedback timing indicator (k1)                                                                                              16.4.0
  2020-06          RAN\#88               R5-203056   1313   1     F     Introduction of test frequencies for Rel-16 NR CA configuration CA\_n66B and CA\_n66(2A) in cl 6.2.3.4                                                                16.4.0
  2020-06          RAN\#88               R5-203057   1319   1     F     Addition of test frequencies for additional channel bandwidths for NR band n66                                                                                        16.4.0
  2020-06          RAN\#88               R5-203078   1325   1     F     Updates to Generic Test Procedure for IMS MO speech call establishment                                                                                                16.4.0
  2020-06          RAN\#88               R5-203079   1326   2     F     Update NR-DC in chapter 4                                                                                                                                             16.4.0
  2020-09          RAN\#89               R5-203275   1364   \-    F     Editorial update IE ARFCN-ValueNR                                                                                                                                     16.5.0
  2020-09          RAN\#89               R5-203277   1366   \-    F     Add IEs ARFCN-ValueUTRA-FDD, AvailabilityCombinationsPerCell, AvailabilityIndicator and BAP-Routing-ID                                                                16.5.0
  2020-09          RAN\#89               R5-203278   1367   \-    F     n26 Default CH BW in 38.508-1                                                                                                                                         16.5.0
  2020-09          RAN\#89               R5-203287   1368   \-    F     Correction PRB-Id for PUCCH secondHopPRB                                                                                                                              16.5.0
  2020-09          RAN\#89               R5-203320   1369   \-    F     Add IE BeamFailureRecoverySCellConfig                                                                                                                                 16.5.0
  2020-09          RAN\#89               R5-203339   1372   \-    F     Add IE CGI-InfoEUTRALogging                                                                                                                                           16.5.0
  2020-09          RAN\#89               R5-203340   1373   \-    F     Add IEs CGI-Info-Logging and CLI-RSSI-Range                                                                                                                           16.5.0
  2020-09          RAN\#89               R5-203341   1374   \-    F     Add IEs CommonLocationInfo, CondReconfigId, CondReconfigToAddModList and ConditionalReconfiguration                                                                   16.5.0
  2020-09          RAN\#89               R5-203342   1375   \-    F     Add IEs ConfiguredGrantConfigIndex and ConfiguredGrantConfigIndexMAC                                                                                                  16.5.0
  2020-09          RAN\#89               R5-203343   1376   \-    F     Add IE DRX-ConfigSecondaryGroup                                                                                                                                       16.5.0
  2020-09          RAN\#89               R5-203344   1377   \-    F     Add IE HighSpeedConfig                                                                                                                                                16.5.0
  2020-09          RAN\#89               R5-203345   1378   \-    F     Add IE InvalidSymbolPattern                                                                                                                                           16.5.0
  2020-09          RAN\#89               R5-203346   1379   \-    F     Add IEs LBT-FailureRecoveryConfig and LocationInfo                                                                                                                    16.5.0
  2020-09          RAN\#89               R5-203347   1380   \-    F     Add IE MeasIdleConfig                                                                                                                                                 16.5.0
  2020-09          RAN\#89               R5-203348   1381   \-    F     Add IE MeasObjectCLI                                                                                                                                                  16.5.0
  2020-09          RAN\#89               R5-203349   1382   \-    F     Add IE MeasObjectNR-SL                                                                                                                                                16.5.0
  2020-09          RAN\#89               R5-203350   1383   \-    F     Add IE MeasObjectUTRA-FDD                                                                                                                                             16.5.0
  2020-09          RAN\#89               R5-203351   1384   \-    F     Add IEs MeasResultIdleEUTRA and MeasResultIdleNR                                                                                                                      16.5.0
  2020-09          RAN\#89               R5-203355   1387   \-    F     Add IEs MsgA-ConfigCommon and MsgA-PUSCH-Config                                                                                                                       16.5.0
  2020-09          RAN\#89               R5-203356   1388   \-    F     Add IEs NeedForGapsConfigNR and NeedForGapsInfoNR                                                                                                                     16.5.0
  2020-09          RAN\#89               R5-203357   1389   \-    F     Correction to Table 4.5.2.2-2-second SMC procedure for Selected EPS NAS security algorithms IE                                                                        16.5.0
  2020-09          RAN\#89               R5-203359   1391   \-    F     Correction to Table 4.6.3-141 ReportConfigInterRAT                                                                                                                    16.5.0
  2020-09          RAN\#89               R5-203446   1395   \-    F     Add IEs NPN-Identity and NPN-IdentityInfoList                                                                                                                         16.5.0
  2020-09          RAN\#89               R5-203449   1396   \-    F     Add IE PLMN-IdentityList2                                                                                                                                             16.5.0
  2020-09          RAN\#89               R5-203450   1397   \-    F     Add IE PUCCH-ConfigurationList                                                                                                                                        16.5.0
  2020-09          RAN\#89               R5-203451   1398   \-    F     Add IE PUCCH-SpatialRelationInfo-Id                                                                                                                                   16.5.0
  2020-09          RAN\#89               R5-203455   1399   \-    F     Corrections to 4.5.1                                                                                                                                                  16.5.0
  2020-09          RAN\#89               R5-203456   1400   \-    F     Updating usages of TS 34.229-1 to TS 34.229-5                                                                                                                         16.5.0
  2020-09          RAN\#89               R5-203467   1401   \-    F     Add IE RACH-ConfigCommonTwoStepRA                                                                                                                                     16.5.0
  2020-09          RAN\#89               R5-203470   1402   \-    F     Add IE RACH-ConfigGenericTwoStepRA                                                                                                                                    16.5.0
  2020-09          RAN\#89               R5-203471   1403   \-    F     Add IE ReferenceTimeInfo                                                                                                                                              16.5.0
  2020-09          RAN\#89               R5-203472   1404   \-    F     Add IE RepetitionSchemeConfig                                                                                                                                         16.5.0
  2020-09          RAN\#89               R5-203476   1405   \-    F     Add IE ReportConfigNR-SL                                                                                                                                              16.5.0
  2020-09          RAN\#89               R5-203500   1410   \-    F     Update to Table 4.6.3-74: MeasObjectEUTRA                                                                                                                             16.5.0
  2020-09          RAN\#89               R5-203506   1411   \-    F     Add IE RSSI-Range                                                                                                                                                     16.5.0
  2020-09          RAN\#89               R5-203507   1412   \-    F     Add IEs SemiStaticChannelAccessConfig and Sensor-LocationInfo                                                                                                         16.5.0
  2020-09          RAN\#89               R5-203508   1413   \-    F     Add IE SI-RequestConfig                                                                                                                                               16.5.0
  2020-09          RAN\#89               R5-203509   1414   \-    F     Add IEs SPS-ConfigIndex, SPS-PUCCH-AN and SPS-PUCCH-AN-List                                                                                                           16.5.0
  2020-09          RAN\#89               R5-203510   1415   \-    F     Add IE SRS-RSRP-Range                                                                                                                                                 16.5.0
  2020-09          RAN\#89               R5-203533   1417   \-    F     Update to PDSCH-ServingCellConfig                                                                                                                                     16.5.0
  2020-09          RAN\#89               R5-203534   1418   \-    F     Updates to CellGroupConfig and RNTI-Value for NR-DC                                                                                                                   16.5.0
  2020-09          RAN\#89               R5-203557   1420   \-    F     Add IEs UL-DelayValueConfig and UplinkCancellation                                                                                                                    16.5.0
  2020-09          RAN\#89               R5-203575   1422   \-    F     Add chapter Positioning System information blocks                                                                                                                     16.5.0
  2020-09          RAN\#89               R5-203577   1423   \-    F     Add IEs SIB10, SIB11, SIB12, SIB13 and SIB14                                                                                                                          16.5.0
  2020-09          RAN\#89               R5-203582   1424   \-    F     Add messages DedicatedSIBRequest, DLDedicatedMessageSegment, DLInformationTransferMRDC and IABOtherInformation                                                        16.5.0
  2020-09          RAN\#89               R5-203634   1429   \-    F     Introduction of test frequencies for additional Rel-16 EN-DC inter-band configurations                                                                                16.5.0
  2020-09          RAN\#89               R5-203662   1432   \-    F     Removal of USIM profile \#16                                                                                                                                          16.5.0
  2020-09          RAN\#89               R5-203671   1433   \-    F     Update of PDSCH-to-HARQ\_feedback timing indicator (k1) value                                                                                                         16.5.0
  2020-09          RAN\#89               R5-203681   1436   \-    F     Editorial correction typos in annex C.2.3.2                                                                                                                           16.5.0
  2020-09          RAN\#89               R5-203704   1438   \-    F     Correction to Table 4.6.3-87 NZP-CSI-RS-ResourceSet                                                                                                                   16.5.0
  2020-09          RAN\#89               R5-203719   1441   \-    F     Add messages LoggedMeasurementConfiguration, MCGFailureInformation and SidelinkUEInformationNR                                                                        16.5.0
  2020-09          RAN\#89               R5-203725   1442   \-    F     Add messages UEInformationRequest, UEInformationResponse, ULDedicatedMessageSegment and ULInformationTransferIRAT                                                     16.5.0
  2020-09          RAN\#89               R5-203729   1443   \-    F     Update IE RACH-ConfigGeneric                                                                                                                                          16.5.0
  2020-09          RAN\#89               R5-203730   1444   \-    F     Scheduling Request Resource config for RRM test cases                                                                                                                 16.5.0
  2020-09          RAN\#89               R5-203731   1445   \-    F     OSI scheduling config for RRM test cases                                                                                                                              16.5.0
  2020-09          RAN\#89               R5-203755   1447   \-    F     Update IE SchedulingRequestResourceConfig                                                                                                                             16.5.0
  2020-09          RAN\#89               R5-203767   1449   \-    F     Addition of test frequencies for new Rel-16 CBW for NR band n77                                                                                                       16.5.0
  2020-09          RAN\#89               R5-203768   1450   \-    F     Addition of test frequencies for new Rel-16 CBW for NR band n78                                                                                                       16.5.0
  2020-09          RAN\#89               R5-203769   1451   \-    F     Introduction of test frequencies for Rel-16 NR band n30                                                                                                               16.5.0
  2020-09          RAN\#89               R5-203793   1454   \-    F     Correction of n29 test frequencies for protocol testing                                                                                                               16.5.0
  2020-09          RAN\#89               R5-203794   1455   \-    F     Introduction of n30 test frequencies for protocol testing                                                                                                             16.5.0
  2020-09          RAN\#89               R5-203796   1456   \-    F     Correction of EN-DC test frequency information for protocol testing                                                                                                   16.5.0
  2020-09          RAN\#89               R5-203813   1457   \-    F     Correction to PUCCH-Config                                                                                                                                            16.5.0
  2020-09          RAN\#89               R5-203815   1458   \-    F     FR2 PUSCH K2 values alignment to TS 38.214                                                                                                                            16.5.0
  2020-09          RAN\#89               R5-203908   1463   \-    F     Corrections on test frequencies for NR FR2 CA band n261                                                                                                               16.5.0
  2020-09          RAN\#89               R5-203998   1467   \-    F     Addition of test frequencies for new Rel-16 CBW 25 and 50 MHz for NR band n1                                                                                          16.5.0
  2020-09          RAN\#89               R5-204021   1469   \-    F     Correction of n51 and n76 test frequencies for protocol testing                                                                                                       16.5.0
  2020-09          RAN\#89               R5-204032   1470   \-    F     Introduction of n259 test frequencies for protocol testing                                                                                                            16.5.0
  2020-09          RAN\#89               R5-204038   1471   \-    F     Corrections of test frequency tables for EN-DC configuration DC\_(n)41AA                                                                                              16.5.0
  2020-09          RAN\#89               R5-204039   1472   \-    F     Corrections of test frequency tables for EN-DC configuration DC\_(n)71AA                                                                                              16.5.0
  2020-09          RAN\#89               R5-204041   1473   \-    F     Addition of test channel bandwidths for n1 new CBW in 38.508-1 R16                                                                                                    16.5.0
  2020-09          RAN\#89               R5-204049   1475   \-    F     Correction to the procedure for determination of SSB and CORESET0                                                                                                     16.5.0
  2020-09          RAN\#89               R5-204052   1478   \-    F     PUCCH Resource ID for CSI TCs                                                                                                                                         16.5.0
  2020-09          RAN\#89               R5-204053   1479   \-    F     Correction to PDCCH-ConfigCommon for performance tests                                                                                                                16.5.0
  2020-09          RAN\#89               R5-204150   1484   \-    F     Update Table 5.4.2.0-2: ServingCellConfigCommon                                                                                                                       16.5.0
  2020-09          RAN\#89               R5-204167   1488   \-    F     Corrections of test frequency tables for CA\_n260(A-I)                                                                                                                16.5.0
  2020-09          RAN\#89               R5-204168   1489   \-    F     Update Table 7.3.1-4: ServingCellConfigCommon                                                                                                                         16.5.0
  2020-09          RAN\#89               R5-204223   1491   \-    F     Update missing SMTC configurations in RRM message contents                                                                                                            16.5.0
  2020-09          RAN\#89               R5-204238   1493   \-    F     Correction to default contents of RRCReestablishmentRequest message                                                                                                   16.5.0
  2020-09          RAN\#89               R5-204325   1495   \-    F     Adding procedure for establishment of multiple additional PDN connections in EPS (S1 mode)                                                                            16.5.0
  2020-09          RAN\#89               R5-204327   1497   \-    F     Updates to Test procedure for UE for Tracking area updating / Inter-system change from N1 mode to S1 mode in 5GMM/EMM-IDLE mode                                       16.5.0
  2020-09          RAN\#89               R5-204329   1499   \-    F     Update of 4.5A.2 UE-requested PDU session establishment procedure                                                                                                     16.5.0
  2020-09          RAN\#89               R5-204330   1500   \-    F     Updates Procedure to UE-requested PDU session modification after the first S1 to N1 mode change                                                                       16.5.0
  2020-09          RAN\#89               R5-204331   1501   \-    F     Void 4.9.14 Procedure for UE-requested PDU session modification after the first S1 to N1 mode change                                                                  16.5.0
  2020-09          RAN\#89               R5-204346   1502   \-    F     Introduction of test frequencies for Rel-16 NR band n259                                                                                                              16.5.0
  2020-09          RAN\#89               R5-204378   1427   1     F     Correction to NR inter-band CA configurations in FR1                                                                                                                  16.5.0
  2020-09          RAN\#89               R5-204384   1409   1     F     Correction to test procedure for UE for Tracking area updating / Inter-system change from S1 mode to N1 mode in 5GMM/EMM-IDLE mode                                    16.5.0
  2020-09          RAN\#89               R5-204386   1390   1     F     Correction to Table 4.6.1-17 RRCResume                                                                                                                                16.5.0
  2020-09          RAN\#89               R5-204387   1406   1     F     Corrections to generic procedures for MO and MT speech call establishment                                                                                             16.5.0
  2020-09          RAN\#89               R5-204388   1407   1     F     Correction to USIM configurations 7 and 13                                                                                                                            16.5.0
  2020-09          RAN\#89               R5-204389   1408   1     F     Correction to switch off / power off procedures for IMS                                                                                                               16.5.0
  2020-09          RAN\#89               R5-204390   1421   1     F     Correction of description of NGEN-DC in table 4.5.1-1                                                                                                                 16.5.0
  2020-09          RAN\#89               R5-204391   1425   1     F     Correction to UE-CapabilityRAT-RequestList and UE-CapabilityRequestFilterNR                                                                                           16.5.0
  2020-09          RAN\#89               R5-204392   1439   1     F     Addition of Generic Test Procedure for IMS MO SMS in 5GC                                                                                                              16.5.0
  2020-09          RAN\#89               R5-204393   1440   1     F     Addition of Generic Test Procedure for IMS MT SMS in 5GC                                                                                                              16.5.0
  2020-09          RAN\#89               R5-204394   1446   1     F     Update IE RLC-BearerConfig                                                                                                                                            16.5.0
  2020-09          RAN\#89               R5-204395   1481   1     F     Update IE SIB2                                                                                                                                                        16.5.0
  2020-09          RAN\#89               R5-204396   1482   1     F     New procedure for PDU Session Release                                                                                                                                 16.5.0
  2020-09          RAN\#89               R5-204397   1483   1     F     Update to FreqBandList                                                                                                                                                16.5.0
  2020-09          RAN\#89               R5-204398   1490   1     F     Update IE ServingCellConfigCommon                                                                                                                                     16.5.0
  2020-09          RAN\#89               R5-204399   1494   1     F     Adding generic procedure E-UTRA RRC\_IDLE with unrestricted number of PDN connections                                                                                 16.5.0
  2020-09          RAN\#89               R5-204400   1496   1     F     Update of PDU SESSION ESTABLISHMENT ACCEPT for multi PDU-PDN handling                                                                                                 16.5.0
  2020-09          RAN\#89               R5-204401   1498   1     F     Updates of Test procedure for UE for Tracking area updating / Inter-system change from S1 mode to N1 mode in 5GMM/EMM-IDLE mode                                       16.5.0
  2020-09          RAN\#89               R5-204507   1371   1     F     Add IEs BH-RLC-ChannelConfig, BH-LogicalChannelIdentity, BH-LogicalChannelIdentity-Ext and BH-RLC-ChannelID                                                           16.5.0
  2020-09          RAN\#89               R5-204508   1386   1     F     Add IEs MeasResultsSL and MeasTriggerQuantityEUTRA                                                                                                                    16.5.0
  2020-09          RAN\#89               R5-204509   1416   1     F     Modification to InterRAT-Parameters to add the UE capability nr-HO-ToEN-DC-r16                                                                                        16.5.0
  2020-09          RAN\#89               R5-204510   1419   1     F     Add IE SSB-PositionQCL-Relation                                                                                                                                       16.5.0
  2020-09          RAN\#89               R5-204704   1503   \-    F     Adding the test frequency for DC\_3A-7A\_n78A                                                                                                                         16.5.0
  2020-09          RAN\#89               R5-204706   1504   \-    F     Adding the test frequency for DC\_28A\_n3A                                                                                                                            16.5.0
  2020-09          RAN\#89               R5-204708   1435   1     F     Updating indicator for SUL FR1 test cases                                                                                                                             16.5.0
  2020-09          RAN\#89               R5-204709   1437   1     F     Update frequencyDomainResources and nrofcandidates                                                                                                                    16.5.0
  2020-09          RAN\#89               R5-204751   1428   1     F     Introduction of test frequencies for additional Rel-15 band EN-DC inter-band configurations                                                                           16.5.0
  2020-09          RAN\#89               R5-204752   1460   1     F     Correction to TCI-state related configurations                                                                                                                        16.5.0
  2020-09          RAN\#89               R5-204753   1461   1     F     Correction to CSI-RS related configurations                                                                                                                           16.5.0
  2020-09          RAN\#89               R5-204754   1468   1     F     Update on test frequencies for EN-DC configurations including FR2                                                                                                     16.5.0
  2020-09          RAN\#89               R5-204755   1485   1     F     Corrections of test frequency tables for CA\_n258x                                                                                                                    16.5.0
  2020-09          RAN\#89               R5-204756   1486   1     F     Corrections of test frequency tables for CA\_n260x                                                                                                                    16.5.0
  2020-09          RAN\#89               R5-204757   1487   1     F     Corrections of test frequency tables for CA\_n261x                                                                                                                    16.5.0
  2020-09          RAN\#89               R5-204758   1492   1     F     Add SSB subcarrier spacing configurations in RRM message contents                                                                                                     16.5.0
  2020-09          RAN\#89               R5-204800   1362   1     F     Introduction of test frequencies for Rel-16 inter-band EN-DC combinations within FR1                                                                                  16.5.0
  2020-09          RAN\#89               R5-204852   1434   1     F     Jumbo CR for update to Demod message contents                                                                                                                         16.5.0
  2020-09          RAN\#89               R5-204896   1370   1     F     Addition of test frequencies for n28 with CBW of 30MHz                                                                                                                16.5.0
  2020-09          RAN\#89               R5-204899   1448   1     F     Adding default value for IE rbg-Size for demodulation and CSI reporting tests                                                                                         16.5.0
  2020-09          RAN\#89               R5-204900   1462   1     F     Introduction of definition of Mid, Low, High test channel bandwidth and removal of NOTEs that incorrectly permit UE not to support mandatory BWs                      16.5.0
  2020-09          RAN\#89               R5-204901   1476   1     F     Correction to message configuration for performance tests                                                                                                             16.5.0
  2020-10          RAN\#89               R5-204325   1495   \-    F     Addition of missing Table 4.5A.2B.2.2-2 and specific message contents of R5-204325                                                                                    16.5.1
  2020-12          RAN\#90               R5-205093   1507   \-    F     Add IE BandCombinationListSidelink                                                                                                                                    16.6.0
  2020-12          RAN\#90               R5-205096   1508   \-    F     Add IE CarrierAggregationVariant                                                                                                                                      16.6.0
  2020-12          RAN\#90               R5-205104   1509   \-    F     Add IEs FreqSeparationClassDL-Only and HighSpeedParameters                                                                                                            16.6.0
  2020-12          RAN\#90               R5-205130   1514   \-    F     Add IE PowSav-Parameters                                                                                                                                              16.6.0
  2020-12          RAN\#90               R5-205167   1519   \-    F     Add IE OLPC-SRS-Pos                                                                                                                                                   16.6.0
  2020-12          RAN\#90               R5-205172   1521   \-    F     Add IEs SidelinkParameters, SON-Parameters and SpatialRelationsSRS-Pos                                                                                                16.6.0
  2020-12          RAN\#90               R5-205178   1522   \-    F     Add IE UE-BasedPerfMeas-Parameters                                                                                                                                    16.6.0
  2020-12          RAN\#90               R5-205181   1523   \-    F     Add IE SharedSpectrumChAccessParamsPerBand                                                                                                                            16.6.0
  2020-12          RAN\#90               R5-205186   1524   \-    F     Add IEs AbsoluteTimeInfo, AreaConfiguration and BT-NameList                                                                                                           16.6.0
  2020-12          RAN\#90               R5-205187   1525   \-    F     Add IEs IAB-IP-Address, IAB-IP-AddressIndex and IAB-IP-Usage                                                                                                          16.6.0
  2020-12          RAN\#90               R5-205188   1526   \-    F     Add IEs LoggingDuration, LoggingInterval, LogMeasResultListBT and LogMeasResultListWLAN                                                                               16.6.0
  2020-12          RAN\#90               R5-205189   1527   \-    F     Add IE PhysCellIdUTRA-FDD                                                                                                                                             16.6.0
  2020-12          RAN\#90               R5-205190   1528   \-    F     Add IEs Sensor-NameList, TraceReference and UE-MeasurementsAvailable-r16                                                                                              16.6.0
  2020-12          RAN\#90               R5-205191   1529   \-    F     Add IEs UTRA-FDD-Q-OffsetRange, VisitedCellInfoList and WLAN-NameList                                                                                                 16.6.0
  2020-12          RAN\#90               R5-205215   1533   \-    F     Update chapter 4.5.1 General                                                                                                                                          16.6.0
  2020-12          RAN\#90               R5-205249   1537   \-    F     Introduction of test frequencies for NR Band n53 signalling testing                                                                                                   16.6.0
  2020-12          RAN\#90               R5-205250   1538   \-    F     Introduction of test channel BWs for NR Band n53                                                                                                                      16.6.0
  2020-12          RAN\#90               R5-205288   1539   \-    F     Addition of IE DCP-Config-r16                                                                                                                                         16.6.0
  2020-12          RAN\#90               R5-205332   1542   \-    F     Updates to generic procedure NR-DC RRC\_CONNECTED                                                                                                                     16.6.0
  2020-12          RAN\#90               R5-205334   1544   \-    F     Updates to RadioBearerConfig in Table 4.6.3-132                                                                                                                       16.6.0
  2020-12          RAN\#90               R5-205336   1546   \-    F     Updates to RRCReconfiguration in Table 4.6.1-13                                                                                                                       16.6.0
  2020-12          RAN\#90               R5-205339   1549   \-    F     Updates to RRCReconfiguration-NR-DC in Table 4.8.1-1CA                                                                                                                16.6.0
  2020-12          RAN\#90               R5-205403   1554   \-    F     Addition of PC5 RRC messages for sidelink communication                                                                                                               16.6.0
  2020-12          RAN\#90               R5-205404   1555   \-    F     Addition of sidelink IEs for Uu RRC and PC5 RRC                                                                                                                       16.6.0
  2020-12          RAN\#90               R5-205532   1573   \-    F     Clarifications to Annex C and CORESET1                                                                                                                                16.6.0
  2020-12          RAN\#90               R5-205661   1580   \-    F     Update of Annex C on calculating test frequencies for RRM testing                                                                                                     16.6.0
  2020-12          RAN\#90               R5-205701   1588   \-    F     Update RF test channel bandwidths for n14 and n30                                                                                                                     16.6.0
  2020-12          RAN\#90               R5-205725   1594   \-    F     Correction to test channel bandwidth for NR band n40 and n50                                                                                                          16.6.0
  2020-12          RAN\#90               R5-205728   1597   \-    F     Adding test frequencies for CA\_n78B                                                                                                                                  16.6.0
  2020-12          RAN\#90               R5-205771   1602   \-    F     Addition of test frequencies for a few Rel-16 EN-DC configurations                                                                                                    16.6.0
  2020-12          RAN\#90               R5-205832   1603   \-    F     Connection diagrams for radiated RRM Tests                                                                                                                            16.6.0
  2020-12          RAN\#90               R5-205874   1607   \-    F     Correction of test frequency of CA\_n41C                                                                                                                              16.6.0
  2020-12          RAN\#90               R5-205875   1608   \-    F     Correction of test frequency of CA\_n66B                                                                                                                              16.6.0
  2020-12          RAN\#90               R5-205881   1610   \-    F     Addition of test frequency for 40MHz of band n38                                                                                                                      16.6.0
  2020-12          RAN\#90               R5-205926   1612   \-    F     Correction to nrofRBs IE for CSI-FrequencyOccupation                                                                                                                  16.6.0
  2020-12          RAN\#90               R5-205932   1614   \-    F     Addition of IE configuration for ULFPTx to clause 5                                                                                                                   16.6.0
  2020-12          RAN\#90               R5-205937   1615   \-    F     Update of 4.9.12 Generic Test Procedure for IMS Emergency call establishment in 5GC without IMS emergency registration and editorials                                 16.6.0
  2020-12          RAN\#90               R5-205939   1617   \-    F     Update for Flexible PDU-PDN - Default messages                                                                                                                        16.6.0
  2020-12          RAN\#90               R5-205940   1618   \-    F     Update for Flexible PDU-PDN - DNN Configurations                                                                                                                      16.6.0
  2020-12          RAN\#90               R5-205997   1621   \-    F     Correction of test frequencies for NR band n1                                                                                                                         16.6.0
  2020-12          RAN\#90               R5-205998   1622   \-    F     Editorial correction to NR-DC test frequency clause 4.3.1                                                                                                             16.6.0
  2020-12          RAN\#90               R5-206002   1626   \-    F     Correction of FR1 NR band test frequency tables for protocol testing                                                                                                  16.6.0
  2020-12          RAN\#90               R5-206003   1627   \-    F     Correction of FR2 NR band test frequency tables for protocol testing                                                                                                  16.6.0
  2020-12          RAN\#90               R5-206004   1628   \-    F     Change of default SCS for NR CA test frequencies for FR2 protocol testing                                                                                             16.6.0
  2020-12          RAN\#90               R5-206008   1632   \-    F     Editorial correction to NR CA test frequencies for FR1 protocol testing                                                                                               16.6.0
  2020-12          RAN\#90               R5-206019   1637   \-    F     Correction of test frequencies for CA\_n260 of intra-band non-contiguous A-I                                                                                          16.6.0
  2020-12          RAN\#90               R5-206046   1642   \-    F     Clarify usage of SSB-Ids for RRM test cases                                                                                                                           16.6.0
  2020-12          RAN\#90               R5-206048   1644   \-    F     Clarification on the conditions in DCI format 1\_1 table for RRM                                                                                                      16.6.0
  2020-12          RAN\#90               R5-206060   1645   \-    F     Correction to 4.9.17 IMS MO release                                                                                                                                   16.6.0
  2020-12          RAN\#90               R5-206061   1646   \-    F     Correction to 4.9.18 IMS MT release                                                                                                                                   16.6.0
  2020-12          RAN\#90               R5-206065   1650   \-    F     Alignment of Rel-16 5GSM messages                                                                                                                                     16.6.0
  2020-12          RAN\#90               R5-206066   1651   \-    F     Addition of new SSTs                                                                                                                                                  16.6.0
  2020-12          RAN\#90               R5-206067   1652   \-    F     Update IE SIB2                                                                                                                                                        16.6.0
  2020-12          RAN\#90               R5-206078   1654   \-    F     Update IE SIB4                                                                                                                                                        16.6.0
  2020-12          RAN\#90               R5-206086   1655   \-    F     Addition of common message contents for sustained downlink data rate tests                                                                                            16.6.0
  2020-12          RAN\#90               R5-206087   1656   \-    F     Correction to Default RRM TRS qcl-info and PDCCH TCI State                                                                                                            16.6.0
  2020-12          RAN\#90               R5-206112   1657   \-    F     Update requirements of test equipment for RF test                                                                                                                     16.6.0
  2020-12          RAN\#90               R5-206113   1658   \-    F     Update requirements of test equipment for RRM tests                                                                                                                   16.6.0
  2020-12          RAN\#90               R5-206115   1659   \-    F     Update requirements of reference test conditions for RRM tests                                                                                                        16.6.0
  2020-12          RAN\#90               R5-206157   1663   \-    F     CSI-measConfig applicable for RRM testing                                                                                                                             16.6.0
  2020-12          RAN\#90               R5-206158   1664   \-    F     Editorial update IE CellAccessRelatedInfo-EUTRA-5GC                                                                                                                   16.6.0
  2020-12          RAN\#90               R5-206164   1666   \-    F     Editorial update IE CellAccessRelatedInfo-EUTRA-EPC                                                                                                                   16.6.0
  2020-12          RAN\#90               R5-206266   1671   \-    F     Corrections to test procedures in subclause 4.9                                                                                                                       16.6.0
  2020-12          RAN\#90               R5-206288   1510   1     F     Corrections to UE-requested PDU session establishment procedure                                                                                                       16.6.0
  2020-12          RAN\#90               R5-206289   1515   1     F     Update of 4.9.7 Test procedure for UE for Tracking area updating / Inter-system change from N1 mode to S1 mode in 5GMM/EMM-IDLE mode                                  16.6.0
  2020-12          RAN\#90               R5-206290   1516   1     F     Update of 4.9.9 Test procedure for UE for Tracking area updating / Inter-system change from S1 mode to N1 mode in 5GMM/EMM-IDLE mode                                  16.6.0
  2020-12          RAN\#90               R5-206291   1517   1     F     Update of 4.5.2 RRC\_IDLE                                                                                                                                             16.6.0
  2020-12          RAN\#90               R5-206292   1532   1     F     Correction to Test procedure 4.9.5                                                                                                                                    16.6.0
  2020-12          RAN\#90               R5-206293   1534   1     F     Corrections to generic procedures regarding IMS usage                                                                                                                 16.6.0
  2020-12          RAN\#90               R5-206294   1540   1     F     Update Generic Test Procedures for IMS MO, MT speech call                                                                                                             16.6.0
  2020-12          RAN\#90               R5-206295   1543   1     F     Updates to generic procedure parameters in Table 4.5.1-1                                                                                                              16.6.0
  2020-12          RAN\#90               R5-206296   1616   1     F     Update for Flexible PDU-PDN - Session-Connection establishment                                                                                                        16.6.0
  2020-12          RAN\#90               R5-206297   1541   1     F     Updates to CellGroupConfig in Table 4.6.3-19                                                                                                                          16.6.0
  2020-12          RAN\#90               R5-206298   1545   1     F     Updates to RadioBearerConfig in Table 4.6.3-132 for NR-DC                                                                                                             16.6.0
  2020-12          RAN\#90               R5-206299   1547   1     F     Updates to RRCReconfiguration in Table 4.6.1-13 for NR-DC                                                                                                             16.6.0
  2020-12          RAN\#90               R5-206300   1548   1     F     Updates to RRCReconfigurationComplete                                                                                                                                 16.6.0
  2020-12          RAN\#90               R5-206301   1586   1     F     Update IE SSB-ToMeasure                                                                                                                                               16.6.0
  2020-12          RAN\#90               R5-206302   1620   1     F     Correction to PDCCH-ConfigCommon                                                                                                                                      16.6.0
  2020-12          RAN\#90               R5-206303   1665   1     F     Messages Exceptions corrections for SUL cases                                                                                                                         16.6.0
  2020-12          RAN\#90               R5-206304   1670   1     F     Update to ims-EmergencySupport indication of SIB1                                                                                                                     16.6.0
  2020-12          RAN\#90               R5-206305   1595   1     F     Correction to test frequencies for signalling testing                                                                                                                 16.6.0
  2020-12          RAN\#90               R5-206306   1625   1     F     Introducing test frequencies for CA\_n261(2A) for protocol testing                                                                                                    16.6.0
  2020-12          RAN\#90               R5-206307   1629   1     F     Introduction of NR-DC test frequencies for protocol testing                                                                                                           16.6.0
  2020-12          RAN\#90               R5-206308   1661   1     F     Update requirements of test equipment for Signalling test                                                                                                             16.6.0
  2020-12          RAN\#90               R5-206309   1531   1     F     Correction to Table 4.8.1-1A RRCReconfiguration-HO                                                                                                                    16.6.0
  2020-12          RAN\#90               R5-206388   1631   1     F     Introduction of n14 test frequencies for protocol testing                                                                                                             16.6.0
  2020-12          RAN\#90               R5-206394   1552   1     F     Adding ReferenceTimeInfo IE config for IIoT test                                                                                                                      16.6.0
  2020-12          RAN\#90               R5-206403   1559   1     F     Update to RRC messages and IEs for R16 Mobility Enhancement                                                                                                           16.6.0
  2020-12          RAN\#90               R5-206407   1553   1     F     Correction to Uu RRC messages and SIBs for sidelink communication                                                                                                     16.6.0
  2020-12          RAN\#90               R5-206408   1556   1     F     Addition of V2X default configuration\_USIM                                                                                                                           16.6.0
  2020-12          RAN\#90               R5-206409   1557   1     F     Addition of V2X default configuration\_NAS Messages                                                                                                                   16.6.0
  2020-12          RAN\#90               R5-206419   1575   1     F     Updates to default contents of NAS messages for Rel-16 RACS                                                                                                           16.6.0
  2020-12          RAN\#90               R5-206420   1576   1     F     Updates to default contents of RRC messages for Rel-16 RACS                                                                                                           16.6.0
  2020-12          RAN\#90               R5-206426   1649   1     F     Alignment of Rel-16 5GMM messages                                                                                                                                     16.6.0
  2020-12          RAN\#90               R5-206427   1668   1     F     Updates to DLDedicatedMessageSegment message                                                                                                                          16.6.0
  2020-12          RAN\#90               R5-206621   1589   1     F     Correction to test frequencies for NR band n34                                                                                                                        16.6.0
  2020-12          RAN\#90               R5-206622   1590   1     F     Correction to test frequencies for NR band n38                                                                                                                        16.6.0
  2020-12          RAN\#90               R5-206623   1591   1     F     Correction to test frequencies for NR band n39                                                                                                                        16.6.0
  2020-12          RAN\#90               R5-206624   1592   1     F     Correction to test frequencies for NR band n40                                                                                                                        16.6.0
  2020-12          RAN\#90               R5-206625   1593   1     F     Correction to test frequencies for NR band n50                                                                                                                        16.6.0
  2020-12          RAN\#90               R5-206626   1609   1     F     Correction of test frequency of CA\_n78C                                                                                                                              16.6.0
  2020-12          RAN\#90               R5-206628   1611   1     F     Update to DEMOD message contents                                                                                                                                      16.6.0
  2020-12          RAN\#90               R5-206629   1669   1     F     Single PDN and PDU configuration for EN-DC RF testing                                                                                                                 16.6.0
  2020-12          RAN\#90               R5-206630   1619   1     F     Addition of aperiodic CSI-RS reference configuration for RRM test                                                                                                     16.6.0
  2020-12          RAN\#90               R5-206631   1623   1     F     Introduction of test frequencies for SCS=60 kHz and EN-DC configurations DC\_41X\_n41A                                                                                16.6.0
  2020-12          RAN\#90               R5-206632   1505   1     F     Message contents for iRAT periodical measurements                                                                                                                     16.6.0
  2020-12          RAN\#90               R5-206633   1638   1     F     Minor corrections of 4.1 for test environment conditions                                                                                                              16.6.0
  2020-12          RAN\#90               R5-206712   1579   1     F     Addition of UL and DL inter-band CA configurations for several FR1 bands                                                                                              16.6.0
  2020-12          RAN\#90               R5-206713   1587   1     F     Update to reference test conditions for R16 EN-DC configuration                                                                                                       16.6.0
  2020-12          RAN\#90               R5-206714   1639   1     F     Introduction of test frequencies for additional Rel-16 EN-DC inter-band configurations                                                                                16.6.0
  2020-12          RAN\#90               R5-206715   1660   1     F     Introduction of test frequencies for additional Rel-16 EN-DC inter-band configurations                                                                                16.6.0
  2020-12          RAN\#90               R5-206736   1536   1     F     Introduction of test frequencies for NR Band n53                                                                                                                      16.6.0
  2020-12          RAN\#90               R5-206737   1572   1     F     Addition of R16 new channel bandwidths for n3 in 38.508-1                                                                                                             16.6.0
  2020-12          RAN\#90               R5-206738   1630   1     F     Introduction of test frequencies for n14                                                                                                                              16.6.0
  2020-12          RAN\#90               R5-206739   1636   1     F     Correction of 4.3.1 for test channel bandwidth of NR bands                                                                                                            16.6.0
  2020-12          RAN\#90               R5-206757   1596   1     F     Adding test frequencies for CA\_n40B                                                                                                                                  16.6.0
  2020-12          RAN\#90               R5-206758   1598   1     F     Adding test frequencies for CA\_n77A-n77A                                                                                                                             16.6.0
  2020-12          RAN\#90               R5-206759   1599   1     F     Adding test frequencies for CA\_n78A-n78A                                                                                                                             16.6.0
  2020-12          RAN\#90               R5-206760   1633   1     F     Updating message contents for Uplink carrier switching                                                                                                                16.6.0
  2020-12          RAN\#90               R5-206790   1581   1     F     Introduction of test frequencies for RRM and NR band n257                                                                                                             16.6.0
  2020-12          RAN\#90               R5-206791   1582   1     F     Introduction of test frequencies for RRM and NR band n258                                                                                                             16.6.0
  2020-12          RAN\#90               R5-206792   1583   1     F     Introduction of test frequencies for RRM and NR band n260                                                                                                             16.6.0
  2020-12          RAN\#90               R5-206793   1584   1     F     Introduction of test frequencies for RRM and NR band n261                                                                                                             16.6.0
  2020-12          RAN\#90               R5-206794   1585   1     F     Introduction of test frequencies for RRM and NR band n259                                                                                                             16.6.0
  2020-12          RAN\#90               R5-206820   1667   1     F     Update to quality of quiet zone validation rule for IFF DFF hybrid setup                                                                                              16.6.0
  2020-12          RAN\#90               R5-206860   1506   1     F     SSB bitmap correction for RRM test cases                                                                                                                              16.6.0
  2020-12          RAN\#90               R5-206861   1624   1     F     Introducing test frequencies for CA\_n261(2A)                                                                                                                         16.6.0
  2020-12          RAN\#90               R5-206862   1643   1     F     Clarify the RF / RRM conditions for default messages                                                                                                                  16.6.0
  2021-03          RAN\#91               R5-210186   1678   \-    F     Update global conditions                                                                                                                                              16.7.0
  2021-03          RAN\#91               R5-210327   1688   \-    F     Update FailureInformation message                                                                                                                                     16.7.0
  2021-03          RAN\#91               R5-210328   1689   \-    F     Editorial update RRCReconfiguration message                                                                                                                           16.7.0
  2021-03          RAN\#91               R5-210359   1692   \-    F     Editorial update SidelinkUEInformationNR message                                                                                                                      16.7.0
  2021-03          RAN\#91               R5-210394   1697   \-    F     Editorial update UEAssistanceInformation message                                                                                                                      16.7.0
  2021-03          RAN\#91               R5-210414   1699   \-    F     Update UECapabilityEnquiry message                                                                                                                                    16.7.0
  2021-03          RAN\#91               R5-210468   1704   \-    F     Add new SIB combination for RRM tests with single cell                                                                                                                16.7.0
  2021-03          RAN\#91               R5-210599   1711   \-    F     Editorial correction on numbering of several Tables in 38.508-1                                                                                                       16.7.0
  2021-03          RAN\#91               R5-210616   1713   \-    F     Editorial update DLDedicatedMessageSegment message                                                                                                                    16.7.0
  2021-03          RAN\#91               R5-210623   1714   \-    F     Correction to Table 4.6.1-13 RRCReconfiguration                                                                                                                       16.7.0
  2021-03          RAN\#91               R5-210626   1717   \-    F     Correction to Table 6.4.1-11 USIM Configuration 11                                                                                                                    16.7.0
  2021-03          RAN\#91               R5-210627   1718   \-    F     Correction to Table 4.8.2.1-7 Reference QoS rule 7                                                                                                                    16.7.0
  2021-03          RAN\#91               R5-210687   1719   \-    F     Correction to Table 4.6.3-25B CondReconfigId                                                                                                                          16.7.0
  2021-03          RAN\#91               R5-210688   1720   \-    F     Correction to Table 4.6.3-25C CondReconfigToAddModList                                                                                                                16.7.0
  2021-03          RAN\#91               R5-210689   1721   \-    F     Correction to Table 4.6.3-25D ConditionalReconfiguration                                                                                                              16.7.0
  2021-03          RAN\#91               R5-210698   1723   \-    F     Addition of IE SL-PreconfigurationNR                                                                                                                                  16.7.0
  2021-03          RAN\#91               R5-210699   1724   \-    F     Addition of V2X NAS IEs                                                                                                                                               16.7.0
  2021-03          RAN\#91               R5-210701   1726   \-    F     Correction of NR SL IE SL-BWP-ConfigCommon                                                                                                                            16.7.0
  2021-03          RAN\#91               R5-210703   1728   \-    F     Correction of NR SL IE SL-ConfigDedicatedNR                                                                                                                           16.7.0
  2021-03          RAN\#91               R5-210704   1729   \-    F     Correction of NR SL IE SL-FreqConfigCommon                                                                                                                            16.7.0
  2021-03          RAN\#91               R5-210705   1730   \-    F     Correction of NR SL IE SL-LogicalChannelConfig                                                                                                                        16.7.0
  2021-03          RAN\#91               R5-210706   1731   \-    F     Correction of NR SL IE SL-MeasConfigInfo                                                                                                                              16.7.0
  2021-03          RAN\#91               R5-210707   1732   \-    F     Correction of NR SL IE SL-PDCP-Config                                                                                                                                 16.7.0
  2021-03          RAN\#91               R5-210708   1733   \-    F     Correction of NR SL IE SL-RadioBearerConfig                                                                                                                           16.7.0
  2021-03          RAN\#91               R5-210709   1734   \-    F     Correction of NR SL IE SL-ResourcePool                                                                                                                                16.7.0
  2021-03          RAN\#91               R5-210710   1735   \-    F     Correction of NR SL IE SL-RLC-BearerConfig                                                                                                                            16.7.0
  2021-03          RAN\#91               R5-210711   1736   \-    F     Correction of NR SL IE SL-RLC-Config                                                                                                                                  16.7.0
  2021-03          RAN\#91               R5-210713   1738   \-    F     Correction to NR Uu IE ARFCN-ValueNR                                                                                                                                  16.7.0
  2021-03          RAN\#91               R5-210714   1739   \-    F     Correction to NR Uu IE SCS-SpecificCarrier                                                                                                                            16.7.0
  2021-03          RAN\#91               R5-210771   1744   \-    F     Correction in CodebookConfig for 4Tx RI Demod test cases                                                                                                              16.7.0
  2021-03          RAN\#91               R5-210772   1745   \-    F     Alignment xOverhead setting with PDSCH RMCs for Demod FR2 testing                                                                                                     16.7.0
  2021-03          RAN\#91               R5-210805   1746   \-    F     Update IE SemiStaticChannelAccessConfig                                                                                                                               16.7.0
  2021-03          RAN\#91               R5-210812   1747   \-    F     Update IE ServingCellConfig                                                                                                                                           16.7.0
  2021-03          RAN\#91               R5-210824   1748   \-    F     Number of control symbols for RRM tests with 240kHz SSB SCS                                                                                                           16.7.0
  2021-03          RAN\#91               R5-210826   1750   \-    F     Editorial update IE ServingCellConfigCommon                                                                                                                           16.7.0
  2021-03          RAN\#91               R5-210873   1752   \-    F     Correction of aperiodic CSI-RS reference configuration for RRM tests                                                                                                  16.7.0
  2021-03          RAN\#91               R5-210897   1753   \-    F     Correction to test frequency parameters for band n83                                                                                                                  16.7.0
  2021-03          RAN\#91               R5-210898   1754   \-    F     Correction to test frequency parameters for band n84                                                                                                                  16.7.0
  2021-03          RAN\#91               R5-211032   1759   \-    F     Correction test frequencies for CA\_n261(2A)                                                                                                                          16.7.0
  2021-03          RAN\#91               R5-211033   1760   \-    F     Correction test frequencies for CA\_n261(2A) for protocol testing                                                                                                     16.7.0
  2021-03          RAN\#91               R5-211034   1761   \-    F     Correction of protocol applicability for test frequencies for DC\_xA\_n261(2A) configurations                                                                         16.7.0
  2021-03          RAN\#91               R5-211107   1770   \-    F     Corrections to subclauses in 38.508-1 with appropriate subclause level and heading styles                                                                             16.7.0
  2021-03          RAN\#91               R5-211116   1772   \-    F     Update of 4.3.1.1.3.41.1 for test frequency of NR intra-band contiguous CA\_n41C                                                                                      16.7.0
  2021-03          RAN\#91               R5-211117   1773   \-    F     Update of 4.3.1.1.3.66.1 for test frequency of NR intra-band contiguous CA\_n66B                                                                                      16.7.0
  2021-03          RAN\#91               R5-211118   1774   \-    F     Update of 4.3.1.1.3.78.1 for test frequency of NR intra-band contiguous CA\_n78C                                                                                      16.7.0
  2021-03          RAN\#91               R5-211121   1777   \-    F     Update of 4.3.1.3.2.1 for test frequencies for NR-DC configurations between FR1 and FR2                                                                               16.7.0
  2021-03          RAN\#91               R5-211124   1780   \-    F     Update of 4.3.1.6.1.3 for test frequencies for EN-DC band combinations including FR1 and FR2                                                                          16.7.0
  2021-03          RAN\#91               R5-211168   1784   \-    F     Updates to PDU SESSION ESTABLISHMENT ACCEPT message                                                                                                                   16.7.0
  2021-03          RAN\#91               R5-211170   1786   \-    F     Editorial update to BandCombinationListSidelink IE                                                                                                                    16.7.0
  2021-03          RAN\#91               R5-211171   1787   \-    F     Update to RRCReconfiguration-Speech IE                                                                                                                                16.7.0
  2021-03          RAN\#91               R5-211204   1791   \-    F     Editorial update IE BWP                                                                                                                                               16.7.0
  2021-03          RAN\#91               R5-211328   1796   \-    F     Correction to frequency parameters for band n53                                                                                                                       16.7.0
  2021-03          RAN\#91               R5-211335   1727   1     F     Correction of NR SL IE SL-BWP-PoolConfigCommon                                                                                                                        16.7.0
  2021-03          RAN\#91               R5-211336   1737   1     F     Correction of NR SL IE SL-SDAP-Config                                                                                                                                 16.7.0
  2021-03          RAN\#91               R5-211337   1740   1     F     Correction to PC5-RRC message RRCReconfigurationSidelink                                                                                                              16.7.0
  2021-03          RAN\#91               R5-211338   1741   1     F     Correction to PC5-RRC message UECapabilityEnquirySidelink                                                                                                             16.7.0
  2021-03          RAN\#91               R5-211339   1742   1     F     Correction to PC5-RRC message UECapabilityInformationSidelink                                                                                                         16.7.0
  2021-03          RAN\#91               R5-211369   1673   1     F     Corrections to generic test procedures for IMS                                                                                                                        16.7.0
  2021-03          RAN\#91               R5-211370   1676   1     F     Correction to generic procedure for UE-requested PDU session modification after S1 to N1 change                                                                       16.7.0
  2021-03          RAN\#91               R5-211371   1680   1     F     Correction to test procedure 4.9.7                                                                                                                                    16.7.0
  2021-03          RAN\#91               R5-211372   1698   1     F     Correction to RRC IDLE procedures                                                                                                                                     16.7.0
  2021-03          RAN\#91               R5-211374   1712   1     F     Update IE PDCCH-ConfigCommon                                                                                                                                          16.7.0
  2021-03          RAN\#91               R5-211375   1715   1     F     Correction to Table 4.6.3-185 SSB-MTC                                                                                                                                 16.7.0
  2021-03          RAN\#91               R5-211456   1722   1     F     Correction to Table 4.6.3-142 ReportConfigNR                                                                                                                          16.7.0
  2021-03          RAN\#91               R5-211462   1725   1     F     Addition of SI combination for NR SL                                                                                                                                  16.7.0
  2021-03          RAN\#91               R5-211465   1693   1     F     Updates to SIB1 and SIB10 for Rel-16 NPN                                                                                                                              16.7.0
  2021-03          RAN\#91               R5-211466   1694   1     F     Addition of System information combination for Rel-16 NPN                                                                                                             16.7.0
  2021-03          RAN\#91               R5-211467   1684   1     F     Introduction of definition of common environment for R16 NR Immediate MDT                                                                                             16.7.0
  2021-03          RAN\#91               R5-211468   1685   1     F     Updating Contents of RRC messages for Logged MDT test cases                                                                                                           16.7.0
  2021-03          RAN\#91               R5-211491   1700   1     F     Addition of Cell configurations for 5G-SRVCC from NG-RAN to UTRAN                                                                                                     16.7.0
  2021-03          RAN\#91               R5-211497   1682   1     F     Editorial update IE PhysicalCellGroupConfig                                                                                                                           16.7.0
  2021-03          RAN\#91               R5-211498   1781   1     F     Introduction of support for URLLC                                                                                                                                     16.7.0
  2021-03          RAN\#91               R5-211499   1782   1     F     Addition of QoS for URLLC                                                                                                                                             16.7.0
  2021-03          RAN\#91               R5-211548   1695   1     F     Addition of NID information for Rel-16 NPN                                                                                                                            16.7.0
  2021-03          RAN\#91               R5-211604   1794   \-    F     Introduction of test frequencies for CBW 70 MHz for n77                                                                                                               16.7.0
  2021-03          RAN\#91               R5-211605   1795   \-    F     Introduction of test frequencies for CBW 70 MHz for n78                                                                                                               16.7.0
  2021-03          RAN\#91               R5-211660   1677   1     F     Update of EN-DC inter-band configurations in clause 4.3.1                                                                                                             16.7.0
  2021-03          RAN\#91               R5-211661   1690   1     F     Addition of 3 band EN-DC Test Frequency (DC\_1A-8A\_n78A, DC\_3A-8A\_n78A)                                                                                            16.7.0
  2021-03          RAN\#91               R5-211662   1691   1     F     Addition of 4 band EN-DC Test Frequency (DC\_1A-3A-8A\_n78A)                                                                                                          16.7.0
  2021-03          RAN\#91               R5-211663   1743   1     F     Update PDSCH-TimeDomainResourceAllocationList to consider coreset0 for Demod FR2 test cases                                                                           16.7.0
  2021-03          RAN\#91               R5-211664   1763   1     F     Update message content for PMI reporting test cases                                                                                                                   16.7.0
  2021-03          RAN\#91               R5-211665   1705   1     F     Changes to RRM default message contents                                                                                                                               16.7.0
  2021-03          RAN\#91               R5-211666   1706   1     F     Add SSB Index table for RRM with SECOND\_SSB condition                                                                                                                16.7.0
  2021-03          RAN\#91               R5-211667   1751   1     F     Addition of default configuration of CSI-IM for RRM tests                                                                                                             16.7.0
  2021-03          RAN\#91               R5-211668   1790   1     F     Specify CSI-SSB-ResourceSet for RRM                                                                                                                                   16.7.0
  2021-03          RAN\#91               R5-211669   1702   1     F     Editorial rework of the conditions for CSI-FrequencyOccupation                                                                                                        16.7.0
  2021-03          RAN\#91               R5-211670   1703   1     F     Align TDD UL DL Common for RRM with TS 38.533                                                                                                                         16.7.0
  2021-03          RAN\#91               R5-211671   1707   1     F     Correct reportOffsetList in CSI-ReportConfig                                                                                                                          16.7.0
  2021-03          RAN\#91               R5-211672   1708   1     F     Specify CSI-SSB-ResourceSet                                                                                                                                           16.7.0
  2021-03          RAN\#91               R5-211673   1764   1     F     Clarification on the connection diagram for FR2 demod and RRM test cases                                                                                              16.7.0
  2021-03          RAN\#91               R5-211762   1778   1     F     Update of 4.3.1.4.1 for test frequencies for EN-DC band combinations within FR1                                                                                       16.7.0
  2021-03          RAN\#91               R5-211763   1779   1     F     Update of 4.3.1.5.1 for test frequencies for EN-DC band combinations including FR2                                                                                    16.7.0
  2021-03          RAN\#91               R5-211784   1776   1     F     Update of 4.3.1.0A for mid test channel bandwidth                                                                                                                     16.7.0
  2021-03          RAN\#91               R5-211785   1792   1     F     Correction of test frequencies for NR band n48                                                                                                                        16.7.0
  2021-03          RAN\#91               R5-211855   1758   1     F     Updating the value of P-Max for EN-DC and NR SA test cases                                                                                                            16.7.0
  2021-03          RAN\#91               R5-211856   1768   1     F     Correction to the message contents for CQI reporting tests in 5.4.2.4                                                                                                 16.7.0
  2021-03          RAN\#91               R5-211857   1769   1     F     Correction to the message contents for PMI reporting tests in 5.4.2.5                                                                                                 16.7.0
  2021-03          RAN\#91               R5-210927   1755   \-    F     Updating Rel-17 mid and highest channel bandwidth for n83 and n84                                                                                                     17.0.0
  2021-03          RAN\#91               R5-210928   1756   \-    F     Adding Rel-17 CBW 30MHz test frequencies for n83                                                                                                                      17.0.0
  2021-03          RAN\#91               R5-210929   1757   \-    F     Updating test frequencies for Rel-17 new CBWs for band n84                                                                                                            17.0.0
  2021-03          RAN\#91               R5-211836   1766   1     F     Introduction of test frequencies for n48 adding CBW 70 MHz - DL only                                                                                                  17.0.0
  2021-06          RAN\#92               R5-212203   1804   \-    F     Resubmission of Addition of SI combination for NR SL                                                                                                                  17.1.0
  2021-06          RAN\#92               R5-212213   1807   \-    F     Add IE Phy-ParametersSharedSpectrumChAccess                                                                                                                           17.1.0
  2021-06          RAN\#92               R5-212248   1811   \-    F     Correction to TCI stated of CSI-RS for TRS                                                                                                                            17.1.0
  2021-06          RAN\#92               R5-212249   1812   \-    F     Correction to physical layer parameters for demodulation tests                                                                                                        17.1.0
  2021-06          RAN\#92               R5-212250   1813   \-    F     Update of TE diagram for FR2 RRM tests with multiple NR cells                                                                                                         17.1.0
  2021-06          RAN\#92               R5-212409   1817   \-    F     Correction to IE BWP-DownlinkDedicated                                                                                                                                17.1.0
  2021-06          RAN\#92               R5-212455   1822   \-    F     Correction of NR SL IE SL-BWP-Config                                                                                                                                  17.1.0
  2021-06          RAN\#92               R5-212456   1823   \-    F     Correction of NR SL IE SL-BWP-PoolConfig                                                                                                                              17.1.0
  2021-06          RAN\#92               R5-212457   1824   \-    F     Correction of NR SL IE SL-CBR-CommonTxConfigList                                                                                                                      17.1.0
  2021-06          RAN\#92               R5-212458   1825   \-    F     Correction of NR SL IE SL-CBR-PriorityTxConfigList                                                                                                                    17.1.0
  2021-06          RAN\#92               R5-212459   1826   \-    F     Correction of NR SL IE SL-ConfiguredGrantConfig                                                                                                                       17.1.0
  2021-06          RAN\#92               R5-212460   1827   \-    F     Correction of NR SL IE SL-DestinationIdentity                                                                                                                         17.1.0
  2021-06          RAN\#92               R5-212461   1828   \-    F     Correction of NR SL IE SL-FreqConfig                                                                                                                                  17.1.0
  2021-06          RAN\#92               R5-212462   1829   \-    F     Correction of NR SL IE SL-MeasConfigCommon                                                                                                                            17.1.0
  2021-06          RAN\#92               R5-212463   1830   \-    F     Correction of NR SL IE SL-MeasIdList                                                                                                                                  17.1.0
  2021-06          RAN\#92               R5-212464   1831   \-    F     Correction of NR SL IE SL-MeasObjectList                                                                                                                              17.1.0
  2021-06          RAN\#92               R5-212465   1832   \-    F     Correction of NR SL IE SL-PSBCH-Config                                                                                                                                17.1.0
  2021-06          RAN\#92               R5-212468   1835   \-    F     Correction of NR SL IE SL-QoS-Profile                                                                                                                                 17.1.0
  2021-06          RAN\#92               R5-212469   1836   \-    F     Correction of NR SL IE SL-QuantityConfig                                                                                                                              17.1.0
  2021-06          RAN\#92               R5-212473   1840   \-    F     Correction of NR SL IE SL-ScheduledConfig                                                                                                                             17.1.0
  2021-06          RAN\#92               R5-212476   1843   \-    F     Correction of NR SL IE SL-TxPower                                                                                                                                     17.1.0
  2021-06          RAN\#92               R5-212478   1845   \-    F     Correction of NR SL IE SL-UE-SelectedConfig                                                                                                                           17.1.0
  2021-06          RAN\#92               R5-212479   1846   \-    F     Correction of NR SL IE SL-ZoneConfig                                                                                                                                  17.1.0
  2021-06          RAN\#92               R5-212616   1859   \-    F     Correction to PUCCH resource indicator value for PMI reporting requirements                                                                                           17.1.0
  2021-06          RAN\#92               R5-212642   1861   \-    F     Editorial correction of header level in clause 5.4.2.0 in 38.508-1                                                                                                    17.1.0
  2021-06          RAN\#92               R5-212688   1865   \-    F     Correction of nominal channel spacing in test frequencies for CA\_n257x                                                                                               17.1.0
  2021-06          RAN\#92               R5-212689   1866   \-    F     Correction of nominal channel spacing in test frequencies for CA\_n258x                                                                                               17.1.0
  2021-06          RAN\#92               R5-212690   1867   \-    F     Correction of nominal channel spacing in test frequencies for CA\_n260x                                                                                               17.1.0
  2021-06          RAN\#92               R5-212691   1868   \-    F     Correction of nominal channel spacing in test frequencies for CA\_n261x                                                                                               17.1.0
  2021-06          RAN\#92               R5-212692   1869   \-    F     Correction of test frequencies for CA\_n41C                                                                                                                           17.1.0
  2021-06          RAN\#92               R5-212693   1870   \-    F     Correction of test frequencies for CA\_n78C                                                                                                                           17.1.0
  2021-06          RAN\#92               R5-212694   1871   \-    F     Correction of test frequencies for DC\_(n)41AA                                                                                                                        17.1.0
  2021-06          RAN\#92               R5-212695   1872   \-    F     Editorial correction of test frequencies for protocol testing                                                                                                         17.1.0
  2021-06          RAN\#92               R5-212698   1875   \-    F     Introduction of test frequencies for n41 adding CBW 70 MHz                                                                                                            17.1.0
  2021-06          RAN\#92               R5-212699   1876   \-    F     Introduction of test frequencies for n48 adding CBW 30 MHz                                                                                                            17.1.0
  2021-06          RAN\#92               R5-212702   1879   \-    F     Introduction of principles for calculating test frequencies for NR Intra-band Contiguous CA for asymmetric bands in Annex C                                           17.1.0
  2021-06          RAN\#92               R5-212703   1880   \-    F     Correction of test frequencies for CA\_n66B                                                                                                                           17.1.0
  2021-06          RAN\#92               R5-212705   1881   \-    F     Add message contents for RRM FR2 tests with reduced RB allocation                                                                                                     17.1.0
  2021-06          RAN\#92               R5-212724   1885   \-    F     Correct number of HARQ processes for PDSCH                                                                                                                            17.1.0
  2021-06          RAN\#92               R5-212819   1892   \-    F     Correction of 4.3.1.0D for bandwidth part                                                                                                                             17.1.0
  2021-06          RAN\#92               R5-212820   1893   \-    F     Correction of 4.3.1.1.2 for test frequencies for NR FR1 inter-band CA configurations                                                                                  17.1.0
  2021-06          RAN\#92               R5-212886   1897   \-    F     Update of default SCS for n48 for protocol testing                                                                                                                    17.1.0
  2021-06          RAN\#92               R5-212890   1898   \-    F     Test frequencies definition for EN-DC band 41CA                                                                                                                       17.1.0
  2021-06          RAN\#92               R5-212892   1900   \-    F     Correction to NZP CSI-RS default configuration for RRM test                                                                                                           17.1.0
  2021-06          RAN\#92               R5-212921   1901   \-    F     Addition of GNSS requirements for NR sidelink                                                                                                                         17.1.0
  2021-06          RAN\#92               R5-212924   1904   \-    F     Addition of connection diagram of NR sidelink testing                                                                                                                 17.1.0
  2021-06          RAN\#92               R5-212946   1905   \-    F     Updating IEs for URLLC                                                                                                                                                17.1.0
  2021-06          RAN\#92               R5-212986   1906   \-    F     Introducing Rel-16 CA configuration CA\_n28A-n41A to clause 4.3.1                                                                                                     17.1.0
  2021-06          RAN\#92               R5-213003   1907   \-    F     Adding test frequency description for SUL configuration                                                                                                               17.1.0
  2021-06          RAN\#92               R5-213004   1908   \-    F     Adding connection diagrams for SUL configuration with DL CA                                                                                                           17.1.0
  2021-06          RAN\#92               R5-213054   1910   \-    F     Correction to PDU Session Authentication Command, PDU Session Authentication Complete and PDU Session Authentication Result messages.                                 17.1.0
  2021-06          RAN\#92               R5-213057   1912   \-    F     Introduction of test frequencies for CA\_n48(2A)                                                                                                                      17.1.0
  2021-06          RAN\#92               R5-213150   1917   \-    F     Updates to global conditions                                                                                                                                          17.1.0
  2021-06          RAN\#92               R5-213153   1920   \-    F     Updates to PDU SESSION ESTABLISHMENT REJECT message                                                                                                                   17.1.0
  2021-06          RAN\#92               R5-213154   1921   \-    F     Updates to PDU SESSION MODIFICATION REJECT message                                                                                                                    17.1.0
  2021-06          RAN\#92               R5-213155   1922   \-    F     Updates to QoS flows                                                                                                                                                  17.1.0
  2021-06          RAN\#92               R5-213180   1939   \-    F     Update chapter 4.5.2 RRC\_IDLE                                                                                                                                        17.1.0
  2021-06          RAN\#92               R5-213192   1940   \-    F     Update chapter 4.5.4 RRC\_CONNECTED                                                                                                                                   17.1.0
  2021-06          RAN\#92               R5-213304   1953   \-    F     Correction of test frequencies for NR band n66                                                                                                                        17.1.0
  2021-06          RAN\#92               R5-213307   1954   \-    F     Correction of common default messages for demod FR2                                                                                                                   17.1.0
  2021-06          RAN\#92               R5-213339   1956   \-    F     Update PUCCH-ConfigCommon for Demod testing                                                                                                                           17.1.0
  2021-06          RAN\#92               R5-213340   1957   \-    F     Update message content for subband CQI reporting test cases                                                                                                           17.1.0
  2021-06          RAN\#92               R5-213400   1961   \-    F     Inclusion of additional P-CSCF IP address in PDU session establishment                                                                                                17.1.0
  2021-06          RAN\#92               R5-213409   1955   1     F     Editorial updates to test procedure titles                                                                                                                            17.1.0
  2021-06          RAN\#92               R5-213416   1838   1     F     Correction of NR SL IE SL-ReportConfigList                                                                                                                            17.1.0
  2021-06          RAN\#92               R5-213417   1841   1     F     Correction of NR SL IE SL-SyncConfig                                                                                                                                  17.1.0
  2021-06          RAN\#92               R5-213418   1848   1     F     Correction to PC5-RRC message MeasurementReportSidelink                                                                                                               17.1.0
  2021-06          RAN\#92               R5-213419   1850   1     F     Correction to PC5-RRC message RRCReconfigurationFailureSidelink                                                                                                       17.1.0
  2021-06          RAN\#92               R5-213423   1857   1     F     Updates to NETWORK SLICE-SPECIFIC AUTHENTICATION COMMAND and NETWORK SLICE-SPECIFIC AUTHENTICATION COMPLETE messages                                                  17.1.0
  2021-06          RAN\#92               R5-213424   1858   1     F     Updates to NETWORK SLICE-SPECIFIC AUTHENTICATION RESULT message                                                                                                       17.1.0
  2021-06          RAN\#92               R5-213425   1924   1     F     Introduction of Always-On indication for URLLC                                                                                                                        17.1.0
  2021-06          RAN\#92               R5-213439   1816   1     F     Correction to IMS call release sequences                                                                                                                              17.1.0
  2021-06          RAN\#92               R5-213440   1886   1     F     Addition of Generic Test procedure for IMS MO Video call establishment in 5GC                                                                                         17.1.0
  2021-06          RAN\#92               R5-213441   1913   1     F     Correction to Table 4.9.12.2.2-1 for IMS Emergency call establishment in 5GC without IMS emergency registration                                                       17.1.0
  2021-06          RAN\#92               R5-213442   1914   1     F     Correction to Procedure for UE-requested PDU session modification after the first S1 to N1 mode change / Single-registration mode with N26                            17.1.0
  2021-06          RAN\#92               R5-213443   1941   1     F     Update chapter 4.5.1 General                                                                                                                                          17.1.0
  2021-06          RAN\#92               R5-213444   1887   1     F     Addition of default contents for RRCReconfiguration-Video                                                                                                             17.1.0
  2021-06          RAN\#92               R5-213445   1888   1     F     Corrections to PDCP config                                                                                                                                            17.1.0
  2021-06          RAN\#92               R5-213446   1798   1     F     Update of USIM Configurations 4, 7, 8, 10, 12 and 21                                                                                                                  17.1.0
  2021-06          RAN\#92               R5-213447   1854   1     F     Correction to Table 6.4.1-12 USIM Configuration 12                                                                                                                    17.1.0
  2021-06          RAN\#92               R5-213448   1873   1     F     Update of default SCS for n38, n39, n40 and n50 for protocol testing                                                                                                  17.1.0
  2021-06          RAN\#92               R5-213449   1942   1     F     Update maximum number of simultaneous configured cells for FR1 and FR2 in OTA                                                                                         17.1.0
  2021-06          RAN\#92               R5-213450   1951   1     F     Updates to FR1 and E-UTRA OTA signal level testing                                                                                                                    17.1.0
  2021-06          RAN\#92               R5-213451   1802   1     F     Correction and editorials to default message content specification                                                                                                    17.1.0
  2021-06          RAN\#92               R5-213452   1915   1     F     Correction to Combinations of system information blocks                                                                                                               17.1.0
  2021-06          RAN\#92               R5-213557   1819   1     F     Addition of general procedures for NR sidelink                                                                                                                        17.1.0
  2021-06          RAN\#92               R5-213558   1820   1     F     Addition of test procedure to establish sidelink unicast mode                                                                                                         17.1.0
  2021-06          RAN\#92               R5-213559   1821   1     F     Addition of test state for NR sidelink                                                                                                                                17.1.0
  2021-06          RAN\#92               R5-213560   1833   1     F     Correction of NR SL IE SL-PSSCH-TxConfigList                                                                                                                          17.1.0
  2021-06          RAN\#92               R5-213561   1834   1     F     Correction of NR SL IE SL-QoS-FlowIdentity                                                                                                                            17.1.0
  2021-06          RAN\#92               R5-213562   1837   1     F     Correction of NR SL IE SLRB-Uu-ConfigIndex                                                                                                                            17.1.0
  2021-06          RAN\#92               R5-213563   1839   1     F     Correction of NR SL IE SL-RLC-BearerConfigIndex                                                                                                                       17.1.0
  2021-06          RAN\#92               R5-213564   1844   1     F     Correction of NR SL IE SL-TypeTxSync                                                                                                                                  17.1.0
  2021-06          RAN\#92               R5-213565   1847   1     F     Correction to PC5-RRC message MasterInformationBlockSidelink                                                                                                          17.1.0
  2021-06          RAN\#92               R5-213566   1849   1     F     Correction to PC5-RRC message RRCReconfigurationCompleteSidelink                                                                                                      17.1.0
  2021-06          RAN\#92               R5-213567   1856   1     F     Update IE SL-Thres-RSRP-List                                                                                                                                          17.1.0
  2021-06          RAN\#92               R5-213573   1890   1     F     Updates to NPN-Identity for Rel-16 NPN                                                                                                                                17.1.0
  2021-06          RAN\#92               R5-213574   1891   1     F     Addition of System information combination for Rel-16 NPN                                                                                                             17.1.0
  2021-06          RAN\#92               R5-213580   1889   1     F     Updates to default contents of UECapabilityEnquiry message                                                                                                            17.1.0
  2021-06          RAN\#92               R5-213601   1855   1     F     Introduction of definition of common environment for R16 NR SON and MDT                                                                                               17.1.0
  2021-06          RAN\#92               R5-213643   1918   1     F     Addition of DNN configurations for new SSTs                                                                                                                           17.1.0
  2021-06          RAN\#92               R5-213644   1919   1     F     Updates to UE Policy Delivery messages                                                                                                                                17.1.0
  2021-06          RAN\#92               R5-213645   1923   1     F     Updates to REGISTRATION ACCEPT message                                                                                                                                17.1.0
  2021-06          RAN\#92               R5-213675   1960   1     F     Correction to procedure 4.9.9 Tracking area updating / Inter-system change from S1 mode to N1 mode in 5GMM/EMM-IDLE mode                                              17.1.0
  2021-06          RAN\#92               R5-213833   1926   1     F     Testing frequencies update for band n3                                                                                                                                17.1.0
  2021-06          RAN\#92               R5-213834   1950   1     F     CR to 38.508-1 on larger quiet zone with grey-box approach                                                                                                            17.1.0
  2021-06          RAN\#92               R5-213853   1864   1     F     Correction of test frequencies for CA\_n260(A-I)                                                                                                                      17.1.0
  2021-06          RAN\#92               R5-213854   1862   1     F     Introduction of principles for calculating test frequencies for NR Intra-band Non-Contiguous CA in Annex C                                                            17.1.0
  2021-06          RAN\#92               R5-213858   1896   1     F     Update Note about n28 Test frequency Mid range and CBW 30 MHz                                                                                                         17.1.0
  2021-06          RAN\#92               R5-213859   1925   1     F     Mid range test frequencies update in case asymmetric bandwidths                                                                                                       17.1.0
  2021-06          RAN\#92               R5-213860   1927   1     F     Testing frequencies update for band n34                                                                                                                               17.1.0
  2021-06          RAN\#92               R5-213861   1928   1     F     Testing frequencies update for band n39                                                                                                                               17.1.0
  2021-06          RAN\#92               R5-213862   1929   1     F     Testing frequencies update for band n53                                                                                                                               17.1.0
  2021-06          RAN\#92               R5-213863   1930   1     F     Testing frequencies update for band n66                                                                                                                               17.1.0
  2021-06          RAN\#92               R5-213864   1931   1     F     Testing frequencies update for band n70                                                                                                                               17.1.0
  2021-06          RAN\#92               R5-213865   1932   1     F     Testing frequencies update for band n80                                                                                                                               17.1.0
  2021-06          RAN\#92               R5-213866   1933   1     F     Testing frequencies update for band n81                                                                                                                               17.1.0
  2021-06          RAN\#92               R5-213867   1934   1     F     Testing frequencies update for band n82                                                                                                                               17.1.0
  2021-06          RAN\#92               R5-213868   1935   1     F     Testing frequencies update for band n86                                                                                                                               17.1.0
  2021-06          RAN\#92               R5-213869   1937   1     F     OffsetToCarrier alignment for cases with equal low, mid and high frequency range (n30, n39, n51, n70) and editorial corrections in annex C.3.                         17.1.0
  2021-06          RAN\#92               R5-213870   1884   1     F     Align Chapter 7 of TS 38.508-1 with Annex H of TS 38.533                                                                                                              17.1.0
  2021-06          RAN\#92               R5-213871   1944   1     F     Introduction of test frequencies for n257 for RRM Inter-freq adjacent cell                                                                                            17.1.0
  2021-06          RAN\#92               R5-213872   1945   1     F     Introduction of test frequencies for n258 for RRM Inter-freq adjacent cell                                                                                            17.1.0
  2021-06          RAN\#92               R5-213873   1947   1     F     Introduction of test frequencies for n260 for RRM Inter-freq adjacent cell                                                                                            17.1.0
  2021-06          RAN\#92               R5-213874   1948   1     F     Introduction of test frequencies for n261 for RRM Inter-freq adjacent cell                                                                                            17.1.0
  2021-06          RAN\#92               R5-213875   1863   1     F     Introduction of principles for calculating test frequencies for EN-DC configurations in Annex C                                                                       17.1.0
  2021-06          RAN\#92               R5-213876   1882   1     F     Add locationAndBandwidth for RRM FR2 tests with reduced RB allocation                                                                                                 17.1.0
  2021-06          RAN\#92               R5-213877   1936   1     F     Annex C: Clarifications to maximum and minimum offsetRBs                                                                                                              17.1.0
  2021-06          RAN\#92               R5-213878   1938   1     F     Annex C update to add SUL test frequencies calculation                                                                                                                17.1.0
  2021-06          RAN\#92               R5-213879   1949   1     F     Determination of test frequencies for a Mid range adjacent inter-frequency cell for FR2 RRM multicell testing in Annex C                                              17.1.0
  2021-06          RAN\#92               R5-213964   1877   1     F     Correction of test frequencies for CA\_n66(2A)                                                                                                                        17.1.0
  2021-06          RAN\#92               R5-213977   1946   1     F     Introduction of test frequencies for n259 for RRM Inter-freq adjacent cell                                                                                            17.1.0
  2021-06          RAN\#92               R5-213996   1902   1     F     Addition of calculation method of NR sidelink test frequencies                                                                                                        17.1.0
  2021-06          RAN\#92               R5-213997   1903   1     F     Addition of V2X test frequencies of band n47                                                                                                                          17.1.0
  2021-06          RAN\#92               R5-214017   1799   1     F     Updating test frequencies for Rel-17 EN-DC band combinations within FR1                                                                                               17.1.0
  2021-06          RAN\#92               R5-214018   1801   1     F     Add test frequencies for R17 NR inter-band CA configurations in FR1                                                                                                   17.1.0
  2021-06          RAN\#92               R5-214019   1909   1     F     Introducing Rel-17 CA configuration CA\_n28A-n79A to clause 4.3.1                                                                                                     17.1.0
  2021-06          RAN\#92               R5-214026   1809   1     F     RRC signalling for UL power boosting via suspended IBE requirements                                                                                                   17.1.0
  2021-06          RAN\#92               R5-214047   1959   1     F     Clarification on PDU configuration for RF, Demod and RRM tests                                                                                                        17.1.0
  2021-06          RAN\#92               R5-214076   1860   1     F     Update IE PDCCH-ConfigCommon for additional BWP                                                                                                                       17.1.0
  2021-06          RAN\#92               R5-214107   1883   1     F     Align RRM CSI-ResourcePeriodicityAndOffset to TS 38.133                                                                                                               17.1.0
  2021-09          RAN\#93               R5-214381   1963   \-    F     Correct dl\_DataToUL\_ACK for short DCI test cases                                                                                                                    17.2.0
  2021-09          RAN\#93               R5-214436   1967   \-    F     Correction to 38.508 Table 4.8.2.3-2: Reference QoS flow \#2                                                                                                          17.2.0
  2021-09          RAN\#93               R5-214554   1968   \-    F     Correction of default test frequencies for bands n38, n39, n40 and n50 and protocol testing                                                                           17.2.0
  2021-09          RAN\#93               R5-214611   1970   \-    F     Correction of default test frequencies for band n48 and protocol testing                                                                                              17.2.0
  2021-09          RAN\#93               R5-214622   1971   \-    F     Editorial updates to test procedure titles                                                                                                                            17.2.0
  2021-09          RAN\#93               R5-214678   1972   \-    F     Correction to k1 setting for FR2 RRM                                                                                                                                  17.2.0
  2021-09          RAN\#93               R5-214727   1974   \-    F     Introduction of test frequencies for CA\_n48B                                                                                                                         17.2.0
  2021-09          RAN\#93               R5-214728   1975   \-    F     Corrections to UEInformationRequest and UEInformationResponse                                                                                                         17.2.0
  2021-09          RAN\#93               R5-214755   1976   \-    F     Updates to System information combination for NR-DC                                                                                                                   17.2.0
  2021-09          RAN\#93               R5-214800   1979   \-    F     Correction to IEs for UE policy part                                                                                                                                  17.2.0
  2021-09          RAN\#93               R5-214808   1987   \-    F     Correction to NR V2X USIM configuration                                                                                                                               17.2.0
  2021-09          RAN\#93               R5-214853   1989   \-    F     Introduction of test frequencies for CA\_n48B and protocol testing                                                                                                    17.2.0
  2021-09          RAN\#93               R5-214900   1992   \-    F     Editorial Updates to Clause. 4.4.3.1.2 for System information combination                                                                                             17.2.0
  2021-09          RAN\#93               R5-214929   1994   \-    F     Introduction of test frequencies for CA\_n71(2A) for protocol testing                                                                                                 17.2.0
  2021-09          RAN\#93               R5-214947   1997   \-    F     Correction to Table 6.4.1-8 USIM Configuration 8                                                                                                                      17.2.0
  2021-09          RAN\#93               R5-214959   1998   \-    F     Correction of test frequencies for CA\_n66(2A) for protocol testing                                                                                                   17.2.0
  2021-09          RAN\#93               R5-214962   1999   \-    F     Alignment of test frequency tables for CA\_n48(2A), CA\_n66(2A), CA\_n77(2A) and CA\_n78(2A)                                                                          17.2.0
  2021-09          RAN\#93               R5-214977   2003   \-    F     Correction to default configuration-ControlResourceSet                                                                                                                17.2.0
  2021-09          RAN\#93               R5-214978   2004   \-    F     Correction to default configuration-SCell CSI on PCell                                                                                                                17.2.0
  2021-09          RAN\#93               R5-215071   2006   \-    F     Update to Out of Coverage procedure to trigger SL-MIMO transmission                                                                                                   17.2.0
  2021-09          RAN\#93               R5-215308   2012   \-    F     Adding test frequencies for SUL band n97                                                                                                                              17.2.0
  2021-09          RAN\#93               R5-215341   2015   \-    F     Correction to TRS configuration for RF test cases                                                                                                                     17.2.0
  2021-09          RAN\#93               R5-215456   2019   \-    F     Update of 4.3.1.4.1 for test frequencies for EN-DC configurations within FR1                                                                                          17.2.0
  2021-09          RAN\#93               R5-215462   2021   \-    F     Correction of 4.3.1.0D for locationAndBandwidth in BWP                                                                                                                17.2.0
  2021-09          RAN\#93               R5-215499   2023   \-    F     Introduction of V2X SST                                                                                                                                               17.2.0
  2021-09          RAN\#93               R5-215504   2028   \-    F     Updates to Table 4.4A.5-2                                                                                                                                             17.2.0
  2021-09          RAN\#93               R5-215518   2029   \-    F     Editorial correction: channel bandwidth and RB allocation revision in Test frequencies for CA\_n260(A-I)                                                              17.2.0
  2021-09          RAN\#93               R5-215530   2030   \-    F     Correction on Test frequencies for DC\_(n)41CA                                                                                                                        17.2.0
  2021-09          RAN\#93               R5-215541   2031   \-    F     Test frequencies update for CA\_ n257G, CA\_ n257H and CA\_ n257I                                                                                                     17.2.0
  2021-09          RAN\#93               R5-215612   2032   \-    F     Correction RF E-UTRA CONNECTED state                                                                                                                                  17.2.0
  2021-09          RAN\#93               R5-215678   2034   \-    F     RRC and NAS message handling in uplink in case of simultaneous RRC and NAS procedures                                                                                 17.2.0
  2021-09          RAN\#93               R5-215679   2035   \-    F     Enquiry of Capability and checking of UeCapabilityInformation contents for NR-DC                                                                                      17.2.0
  2021-09          RAN\#93               R5-215689   2039   \-    F     Correction to USIM Configuration 18 and 19                                                                                                                            17.2.0
  2021-09          RAN\#93               R5-215691   2040   \-    F     Update chapter 4.5.4 RRC\_CONNECTED                                                                                                                                   17.2.0
  2021-09          RAN\#93               R5-215835   1964   1     F     Correct CSI-MeasConfig for test cases with 1SSB                                                                                                                       17.2.0
  2021-09          RAN\#93               R5-215836   1965   1     F     Complete CSI-ReportConfig for RRM                                                                                                                                     17.2.0
  2021-09          RAN\#93               R5-215837   2014   1     F     Correction to CSI report configurations                                                                                                                               17.2.0
  2021-09          RAN\#93               R5-215936   2005   1     F     Update of SIB2 to add messages for relaxed RRM measurement                                                                                                            17.2.0
  2021-09          RAN\#93               R5-215969   1962   1     F     Updating Test Frequencies for Rel-17 CA,DC band combinations within FR1 into TS 38.508-1                                                                              17.2.0
  2021-09          RAN\#93               R5-215970   1993   1     F     Introduction of test frequencies for CA\_n71(2A)                                                                                                                      17.2.0
  2021-09          RAN\#93               R5-215971   2008   1     F     Addition of R17 CADC configuration into 38.508-1                                                                                                                      17.2.0
  2021-09          RAN\#93               R5-215972   2020   1     F     Update of 4.3.1.1.2 for NR inter-band CA configurations in FR1                                                                                                        17.2.0
  2021-09          RAN\#93               R5-216027   2016   1     F     Addition of Perf RI FR2 message contents                                                                                                                              17.2.0
  2021-09          RAN\#93               R5-216070   2007   1     F     Adding connection diagram for eMIMO multi-TRP demod test cases                                                                                                        17.2.0
  2021-09          RAN\#93               R5-216079   1973   1     F     Updating test frequencies for Rel-17 inter-band EN-DC configurations                                                                                                  17.2.0
  2021-09          RAN\#93               R5-216116   2009   1     F     Updates to Test Equipment connection for Demodulation Performance and CSI reporting tests                                                                             17.2.0
  2021-09          RAN\#93               R5-216122   2010   1     B     Introduction of test frequencies for n24 and n99                                                                                                                      17.2.0
  2021-09          RAN\#93               R5-216150   1977   1     F     Correction to Test Procedure for IMS MO and MT call release in 5GC                                                                                                    17.2.0
  2021-09          RAN\#93               R5-216151   2017   1     F     Correction to introduce Handling of PDU Session Release during switch off/Power off procedures                                                                        17.2.0
  2021-09          RAN\#93               R5-216152   2026   1     F     Addition of UE Configuration Update procedure                                                                                                                         17.2.0
  2021-09          RAN\#93               R5-216153   2037   1     F     Corrections for IMS video call signalling                                                                                                                             17.2.0
  2021-09          RAN\#93               R5-216154   2041   1     F     Correction to Table 4.6.3-142 and Table 4.6.3-79 for SFTD measurement reporting                                                                                       17.2.0
  2021-09          RAN\#93               R5-216155   2024   1     F     Introduction of PS Data Off                                                                                                                                           17.2.0
  2021-09          RAN\#93               R5-216156   2025   1     F     Introduction of URSP                                                                                                                                                  17.2.0
  2021-09          RAN\#93               R5-216157   2027   1     F     Updates to REGISTRATION messages                                                                                                                                      17.2.0
  2021-09          RAN\#93               R5-216158   2036   1     F     Correction to Table 4.8.2.2-1 for default Packet filter ID                                                                                                            17.2.0
  2021-09          RAN\#93               R5-216159   1969   1     F     Correction for USIM configurations                                                                                                                                    17.2.0
  2021-09          RAN\#93               R5-216160   2018   1     F     Updates to NR cell configurations for SIG                                                                                                                             17.2.0
  2021-09          RAN\#93               R5-216161   2038   1     F     Correction to reference configurations for IMS video call signalling                                                                                                  17.2.0
  2021-09          RAN\#93               R5-216243   1991   1     F     Correction of test frequencies for CA\_n66B for protocol testing                                                                                                      17.2.0
  2021-09          RAN\#93               R5-216256   2022   1     F     Introduction of MIoT SST                                                                                                                                              17.2.0
  2021-09          RAN\#93               R5-216263   1980   1     F     Correction to IEs for V2XP info                                                                                                                                       17.2.0
  2021-09          RAN\#93               R5-216264   1981   1     F     Correction to IEs for Served by E-UTRA or served by NR                                                                                                                17.2.0
  2021-09          RAN\#93               R5-216265   1982   1     F     Correction to IEs for Not served by E-UTRA and not served by NR                                                                                                       17.2.0
  2021-09          RAN\#93               R5-216266   1983   1     F     Correction to IEs for V2X service identifier to PC5 RAT and Tx profiles mapping rules                                                                                 17.2.0
  2021-09          RAN\#93               R5-216267   1984   1     F     Correction to IEs for Privacy config                                                                                                                                  17.2.0
  2021-09          RAN\#93               R5-216268   1985   1     F     Correction to IEs for V2X communication over PC5 in E-UTRA-PC5                                                                                                        17.2.0
  2021-09          RAN\#93               R5-216269   1986   1     F     Correction to IEs for V2X communication over PC5 in NR-PC5                                                                                                            17.2.0
  2021-09          RAN\#93               R5-216270   1988   1     F     Correction to UE Policy Delivery msg                                                                                                                                  17.2.0
  2021-09          RAN\#93               R5-216284   1990   1     F     Update default message contents of LoggedMeasurementConfiguration                                                                                                     17.2.0
  2021-09          RAN\#93               R5-216320   2011   1     B     Introduction of signalling test frequencies for n24 and n99                                                                                                           17.2.0
  2021-09          RAN\#93               R5-216321   2013   1     F     Adding signalling test frequencies for SUL band n97                                                                                                                   17.2.0
  2021-09          RAN\#93               R5-216327   2000   1     F     Default message content update for NR EIEI                                                                                                                            17.2.0
  2021-09          RAN\#93               R5-216328   2001   1     F     Generic procedure for eCall over IMS establishment in 5GS Normal Service                                                                                              17.2.0
  2021-09          RAN\#93               R5-216329   2002   1     F     USIM configuration for NR EIEI                                                                                                                                        17.2.0
  2021-12          RAN\#94               R5-216510   2047   \-    F     Updating Test Frequencies for Rel-16 CA,DC band combinations within FR1 into TS 38.508-1                                                                              17.3.0
  2021-12          RAN\#94               R5-216530   2048   \-    F     Addition of test frequencies for asymmetric channel bandwidths for n24                                                                                                17.3.0
  2021-12          RAN\#94               R5-216603   2051   \-    F     Addition of NR band n95                                                                                                                                               17.3.0
  2021-12          RAN\#94               R5-216636   2052   \-    F     Updates on simultaneous co-existence of NR cells                                                                                                                      17.3.0
  2021-12          RAN\#94               R5-216761   2053   \-    F     Addition of PDCCH Search Space Ext configuration in 38.508-1                                                                                                          17.3.0
  2021-12          RAN\#94               R5-216767   2054   \-    F     Updates to NETWORK SLICE-SPECIFIC AUTHENTICATION COMMAND message                                                                                                      17.3.0
  2021-12          RAN\#94               R5-216768   2055   \-    F     Updates to NETWORK SLICE-SPECIFIC AUTHENTICATION COMPLETE message                                                                                                     17.3.0
  2021-12          RAN\#94               R5-216773   2059   \-    F     Update IE SSB-PositionQCL-Relation                                                                                                                                    17.3.0
  2021-12          RAN\#94               R5-216829   2061   \-    F     Correction to IMS MO emergency call release procedure                                                                                                                 17.3.0
  2021-12          RAN\#94               R5-216851   2062   \-    F     Correction to IE Table 7.3.1-3 - SSB-MTC                                                                                                                              17.3.0
  2021-12          RAN\#94               R5-216895   2063   \-    F     Correction to IE Table 4.6.3-77A - MeasObjectUTRA-FDD                                                                                                                 17.3.0
  2021-12          RAN\#94               R5-216896   2064   \-    F     Correction to IE Table 4.6.3-79 - MeasResults                                                                                                                         17.3.0
  2021-12          RAN\#94               R5-216898   2066   \-    F     Correction to IE Table 4.6.5-16 - UTRA-FDD-Q-OffsetRange                                                                                                              17.3.0
  2021-12          RAN\#94               R5-216899   2067   \-    F     Correction to RRC message Table 4.6.1-8 - MobilityFromNRCommand                                                                                                       17.3.0
  2021-12          RAN\#94               R5-216905   2068   \-    F     Correction to IE Table 4.6.3-62A - HighSpeedConfig                                                                                                                    17.3.0
  2021-12          RAN\#94               R5-216922   2097   \-    F     Update of Table 4.7.1-7-Registration Accept                                                                                                                           17.3.0
  2021-12          RAN\#94               R5-217024   2101   \-    F     Add Reference file                                                                                                                                                    17.3.0
  2021-12          RAN\#94               R5-217025   2102   \-    F     Correction to DIRECT LINK ESTABLISHMENT REQUEST msg                                                                                                                   17.3.0
  2021-12          RAN\#94               R5-217026   2103   \-    F     Correction to DIRECT LINK ESTABLISHMENT ACCEPT msg                                                                                                                    17.3.0
  2021-12          RAN\#94               R5-217027   2104   \-    F     Correction to DIRECT LINK MODIFICATION REQUEST msg                                                                                                                    17.3.0
  2021-12          RAN\#94               R5-217028   2105   \-    F     Correction to DIRECT LINK MODIFICATION ACCEPT msg                                                                                                                     17.3.0
  2021-12          RAN\#94               R5-217029   2106   \-    F     Correction to DIRECT LINK RELEASE REQUEST msg                                                                                                                         17.3.0
  2021-12          RAN\#94               R5-217030   2107   \-    F     Correction to DIRECT LINK RELEASE ACCEPT msg                                                                                                                          17.3.0
  2021-12          RAN\#94               R5-217032   2109   \-    F     Correction to DIRECT LINK KEEPALIVE RESPONSE msg                                                                                                                      17.3.0
  2021-12          RAN\#94               R5-217035   2112   \-    F     Correction to DIRECT LINK AUTHENTICATION REJECT msg                                                                                                                   17.3.0
  2021-12          RAN\#94               R5-217038   2115   \-    F     Correction to DIRECT LINK SECURITY MODE REJECT msg                                                                                                                    17.3.0
  2021-12          RAN\#94               R5-217039   2116   \-    F     Correction to DIRECT LINK REKEYING REQUEST msg                                                                                                                        17.3.0
  2021-12          RAN\#94               R5-217040   2117   \-    F     Correction to DIRECT LINK REKEYING RESPONSE msg                                                                                                                       17.3.0
  2021-12          RAN\#94               R5-217044   2121   \-    F     Correction to DIRECT LINK IDENTIFIER UPDATE REJECT msg                                                                                                                17.3.0
  2021-12          RAN\#94               R5-217045   2122   \-    F     Correction to DIRECT LINK MODIFICATION REJECT msg                                                                                                                     17.3.0
  2021-12          RAN\#94               R5-217095   2125   \-    F     Update chapter 4.8.1 for NE-DC                                                                                                                                        17.3.0
  2021-12          RAN\#94               R5-217118   2128   \-    F     Meas exception for TRS config in RF test cases                                                                                                                        17.3.0
  2021-12          RAN\#94               R5-217243   2133   \-    F     Correction to IE Table 4.6.3-127 QuantityConfig                                                                                                                       17.3.0
  2021-12          RAN\#94               R5-217246   2134   \-    F     Correction of spec number and addition of uncertainty value for OTA testing in section 5.2.1                                                                          17.3.0
  2021-12          RAN\#94               R5-217259   2135   \-    F     Addition of 13 NR CA combinations to FR1 inter-band configurations table                                                                                              17.3.0
  2021-12          RAN\#94               R5-217286   2137   \-    F     Correction to IMS Emergency call establishment test procedure with IMS emergency registration                                                                         17.3.0
  2021-12          RAN\#94               R5-217298   2138   \-    F     Addition of test frequencies for Rel-15 EN-DC configurations                                                                                                          17.3.0
  2021-12          RAN\#94               R5-217340   2139   \-    F     Correction of 4.3.1.2.4.4.2 for test frequency for intra-band non-contiguous CA\_n260                                                                                 17.3.0
  2021-12          RAN\#94               R5-217366   2140   \-    F     Addition of default message for 16Tx PMI reporting test cases in 5.4.2.5                                                                                              17.3.0
  2021-12          RAN\#94               R5-217379   2141   \-    F     Addition of default DCI\_0\_2 for URLLC                                                                                                                               17.3.0
  2021-12          RAN\#94               R5-217390   2143   \-    F     Update to SIG test frequencies for V2X                                                                                                                                17.3.0
  2021-12          RAN\#94               R5-217430   2144   \-    F     Correction to the periodicity of CSI-RS for tracking                                                                                                                  17.3.0
  2021-12          RAN\#94               R5-217453   2146   \-    F     Updates to 4.8.4                                                                                                                                                      17.3.0
  2021-12          RAN\#94               R5-217527   2148   \-    F     message content update for HST single tap 1Tx PDSCH test cases                                                                                                        17.3.0
  2021-12          RAN\#94               R5-217555   2153   \-    F     Editorial correction in channel bandwidth clause                                                                                                                      17.3.0
  2021-12          RAN\#94               R5-217587   2155   \-    F     Addition of CA\_n1A-n3A into TS 38.508-1                                                                                                                              17.3.0
  2021-12          RAN\#94               R5-217588   2156   \-    F     Introduction of test frequencies for CA\_n48(2A) for protocol testing                                                                                                 17.3.0
  2021-12          RAN\#94               R5-217589   2157   \-    F     Introduction of test frequencies for n38 and CBWs 25 MHz and 30 MHz                                                                                                   17.3.0
  2021-12          RAN\#94               R5-217682   2160   \-    F     Editorial update to clause 4.5A.2                                                                                                                                     17.3.0
  2021-12          RAN\#94               R5-217735   2163   \-    F     Introduction of test frequencies for CA\_n260K, CA\_n260L and CA\_n260M                                                                                               17.3.0
  2021-12          RAN\#94               R5-217766   2165   \-    F     Correction to NR V2X default configuration                                                                                                                            17.3.0
  2021-12          RAN\#94               R5-217792   2043   1     F     Update chapter 4.5.4 RRC\_CONNECTED                                                                                                                                   17.3.0
  2021-12          RAN\#94               R5-217793   2044   1     F     Update chapter 4.5.1 General                                                                                                                                          17.3.0
  2021-12          RAN\#94               R5-217794   2045   1     F     Update chapter 4.5.2 RRC\_IDLE                                                                                                                                        17.3.0
  2021-12          RAN\#94               R5-217795   2060   1     F     Addition of new generic procedure for IMS MT video call establishment                                                                                                 17.3.0
  2021-12          RAN\#94               R5-217796   2130   1     F     Adding test procedure for adding video to a speech call                                                                                                               17.3.0
  2021-12          RAN\#94               R5-217797   2136   1     F     Correction to IMS MO Video call establishment test procedure                                                                                                          17.3.0
  2021-12          RAN\#94               R5-217798   2147   1     F     Adding test procedure for removing video from an ongoing call                                                                                                         17.3.0
  2021-12          RAN\#94               R5-217799   2042   1     F     Update RRCReconfiguration                                                                                                                                             17.3.0
  2021-12          RAN\#94               R5-217800   2046   1     F     Update IE CellAccessRelatedInfo                                                                                                                                       17.3.0
  2021-12          RAN\#94               R5-217801   2127   1     F     Update RRCReconfigurationComplete                                                                                                                                     17.3.0
  2021-12          RAN\#94               R5-217877   2098   1     F     Correction to default configuration of SIB12                                                                                                                          17.3.0
  2021-12          RAN\#94               R5-217878   2099   1     F     Addition of default configuration of DCI and SCI for NR SL test                                                                                                       17.3.0
  2021-12          RAN\#94               R5-217879   2100   1     F     Addition of power level setting for NR SL test                                                                                                                        17.3.0
  2021-12          RAN\#94               R5-217880   2108   1     F     Correction to DIRECT LINK KEEPALIVE REQUEST msg                                                                                                                       17.3.0
  2021-12          RAN\#94               R5-217881   2110   1     F     Correction to DIRECT LINK AUTHENTICATION REQUEST msg                                                                                                                  17.3.0
  2021-12          RAN\#94               R5-217882   2111   1     F     Correction to DIRECT LINK AUTHENTICATION RESPONSE msg                                                                                                                 17.3.0
  2021-12          RAN\#94               R5-217883   2113   1     F     Correction to DIRECT LINK SECURITY MODE COMMAND msg                                                                                                                   17.3.0
  2021-12          RAN\#94               R5-217884   2114   1     F     Correction to DIRECT LINK SECURITY MODE COMPLETE msg                                                                                                                  17.3.0
  2021-12          RAN\#94               R5-217885   2118   1     F     Correction to DIRECT LINK IDENTIFIER UPDATE REQUEST msg                                                                                                               17.3.0
  2021-12          RAN\#94               R5-217886   2119   1     F     Correction to DIRECT LINK IDENTIFIER UPDATE ACCEPT msg                                                                                                                17.3.0
  2021-12          RAN\#94               R5-217887   2120   1     F     Correction to DIRECT LINK IDENTIFIER UPDATE ACK msg                                                                                                                   17.3.0
  2021-12          RAN\#94               R5-217888   2123   1     F     Correction to DIRECT LINK ESTABLISHMENT REJECT                                                                                                                        17.3.0
  2021-12          RAN\#94               R5-217933   2050   1     F     Updates to UTRA signal levels in FR1 and OTA environment                                                                                                              17.3.0
  2021-12          RAN\#94               R5-217943   2124   1     F     Update Radio resource control information elements for NR 2-step RACH test cases                                                                                      17.3.0
  2021-12          RAN\#94               R5-217944   2161   1     F     Test Procedure for eCall over IMS establishment in 5GS eCall only Support                                                                                             17.3.0
  2021-12          RAN\#94               R5-217949   2056   1     F     Update IE MeasObjectNR                                                                                                                                                17.3.0
  2021-12          RAN\#94               R5-217950   2057   1     F     Update IE ServingCellConfigCommon                                                                                                                                     17.3.0
  2021-12          RAN\#94               R5-217951   2058   1     F     Update IE ServingCellConfigCommonSIB                                                                                                                                  17.3.0
  2021-12          RAN\#94               R5-218220   2158   1     F     Correction of test frequencies for CA\_n257x                                                                                                                          17.3.0
  2021-12          RAN\#94               R5-218221   2129   1     F     Add meas objects and report config for inter-RAT                                                                                                                      17.3.0
  2021-12          RAN\#94               R5-218267   2049   1     F     Addition of NR inter-band CA configurations for CA\_n260-n261 in FR2                                                                                                  17.3.0
  2021-12          RAN\#94               R5-218268   2151   1     F     Addition of R16 FR1+FR2 CADC configuration into 38.508-1                                                                                                              17.3.0
  2021-12          RAN\#94               R5-218269   2159   1     F     Addition of test frequencies for R16 EN-DC FR2 configurations with n260                                                                                               17.3.0
  2021-12          RAN\#94               R5-218335   2065   1     F     Correction to IE Table 4.6.3-141 - ReportConfigInterRAT                                                                                                               17.3.0
  2021-12          RAN\#94               R5-218361   2152   1     F     Addition of test frequencies for n3 CBW 50MHz                                                                                                                         17.3.0
  2021-12          RAN\#94               R5-218414   2166   1     F     Update to demod parameter CSI-RS-ResourceMapping to add 1Tx condition                                                                                                 17.3.0
  2021-12          RAN\#94               R5-218415   2164   1     F     Update to n71 test frequencies for LTE-NR coex test cases                                                                                                             17.3.0
  2021-12          RAN\#94               R5-218451   2132   1     F     Introduction\_of\_test\_frequencies\_for\_new\_EN-DC\_comb\_within\_FR1                                                                                               17.3.0
  2021-12          RAN\#94               R5-218452   2149   1     F     Introduction of test frequencies for CA\_n48B BCS1                                                                                                                    17.3.0
  2021-12          RAN\#94               R5-218470   2150   1     F     Introduction of test frequencies for CA\_n48B BCS2                                                                                                                    17.3.0
  2022-03          RAN\#95               R5-220090   2171   \-    F     Correction of clause title tyles of 4.3.1.1.1.x                                                                                                                       17.4.0
  2022-03          RAN\#95               R5-220094   2172   \-    F     Correction of test channel bandwidth for n38                                                                                                                          17.4.0
  2022-03          RAN\#95               R5-220186   2186   \-    F     Editorial update of test procedure 4.9.15                                                                                                                             17.4.0
  2022-03          RAN\#95               R5-220206   2188   \-    F     Addition of test frequencies for CA\_n3A-n41A with and without UL configuration                                                                                       17.4.0
  2022-03          RAN\#95               R5-220240   2189   \-    F     Corrections to 4.9.17 on IMS MO call release                                                                                                                          17.4.0
  2022-03          RAN\#95               R5-220248   2191   \-    F     Correct TDD pattern for FR2 RF 60kHz SCS                                                                                                                              17.4.0
  2022-03          RAN\#95               R5-220271   2192   \-    F     Addition of test frequencies for CA\_n41A-n79A with UL configuration                                                                                                  17.4.0
  2022-03          RAN\#95               R5-220308   2195   \-    F     Introduction of test frequencies for CA\_n261M                                                                                                                        17.4.0
  2022-03          RAN\#95               R5-220309   2196   \-    F     Correction of NR inter-band CA configurations for CA\_n260-n261 in FR2                                                                                                17.4.0
  2022-03          RAN\#95               R5-220311   2197   \-    F     Introduction of test frequencies for Rel-16 inter-band EN-DC two band combinations within FR1                                                                         17.4.0
  2022-03          RAN\#95               R5-220374   2198   \-    F     Introduction of test frequencies for additional Rel-17 EN-DC inter-band configurations                                                                                17.4.0
  2022-03          RAN\#95               R5-220449   2199   \-    F     Update of test frequencies for protocol testing and NR inter-band CA                                                                                                  17.4.0
  2022-03          RAN\#95               R5-220452   2200   \-    F     Correction to RF E-UTRA RRC\_CONNECTED procedure                                                                                                                      17.4.0
  2022-03          RAN\#95               R5-220541   2204   \-    F     Introduction of test frequencies for n25 adding CBWs 25MHz, 30MHz, 40MHz                                                                                              17.4.0
  2022-03          RAN\#95               R5-220567   2206   \-    F     Addition of default AT command and information element for NR SL test                                                                                                 17.4.0
  2022-03          RAN\#95               R5-220569   2208   \-    F     Correction to test procedures for establishing unicast link                                                                                                           17.4.0
  2022-03          RAN\#95               R5-220579   2218   \-    F     Correction to SIB12                                                                                                                                                   17.4.0
  2022-03          RAN\#95               R5-220580   2219   \-    F     Correction to IE SL-BWP-Config and SL-BWP-ConfigCommon                                                                                                                17.4.0
  2022-03          RAN\#95               R5-220582   2221   \-    F     Correction to IE SL-ResourcePool                                                                                                                                      17.4.0
  2022-03          RAN\#95               R5-220590   2229   \-    F     Correction to V2X service identifier to PC5 RAT and Tx profiles mapping rule                                                                                          17.4.0
  2022-03          RAN\#95               R5-220591   2230   \-    F     Correction to V2X frequencies                                                                                                                                         17.4.0
  2022-03          RAN\#95               R5-220632   2231   \-    F     Introduction\_of\_test\_frequencies\_for\_new\_EN-DC\_comb\_within\_FR1                                                                                               17.4.0
  2022-03          RAN\#95               R5-220643   2232   \-    F     Introduction of test frequencies for n2 adding CBWs 25MHz, 30MHz, 40MHz                                                                                               17.4.0
  2022-03          RAN\#95               R5-220653   2234   \-    F     Addition of test frequencies for CA\_n41C-n79A with and without UL configuration                                                                                      17.4.0
  2022-03          RAN\#95               R5-220725   2237   \-    F     Addition of default configuration for NR SL RRM test                                                                                                                  17.4.0
  2022-03          RAN\#95               R5-220760   2238   \-    F     Introduction of test frequencies for n5 adding CBW 25MHz                                                                                                              17.4.0
  2022-03          RAN\#95               R5-220761   2239   \-    F     Editorial corrections for NR CA configuration CA\_n48B                                                                                                                17.4.0
  2022-03          RAN\#95               R5-220771   2242   \-    F     Introduction of test frequencies for CA\_n66(2A) BCS1 and BCS2                                                                                                        17.4.0
  2022-03          RAN\#95               R5-220774   2243   \-    F     Corrections to test procedures 4.9.26 and 4.9.27                                                                                                                      17.4.0
  2022-03          RAN\#95               R5-220779   2245   \-    F     Update of test frequencies for n66 and asymmetric channel bandwidth combination set 1                                                                                 17.4.0
  2022-03          RAN\#95               R5-220788   2246   \-    F     Addition of V2X connection diagram                                                                                                                                    17.4.0
  2022-03          RAN\#95               R5-220797   2249   \-    F     Addition of connection diagram for 16Tx                                                                                                                               17.4.0
  2022-03          RAN\#95               R5-220808   2250   \-    F     Update to MAC-CellGroupConfig                                                                                                                                         17.4.0
  2022-03          RAN\#95               R5-220847   2253   \-    F     Addition of test frequency n53 in Table 6.2.3.1-4                                                                                                                     17.4.0
  2022-03          RAN\#95               R5-220860   2254   \-    F     Introducing Rel-17 2 band CA configurations for n24 and n41 to clause 4.3.1                                                                                           17.4.0
  2022-03          RAN\#95               R5-220861   2255   \-    F     Introducing Rel-17 2 band CA configurations for n24 and n48 to clause 4.3.1                                                                                           17.4.0
  2022-03          RAN\#95               R5-220862   2256   \-    F     Introducing Rel-17 2 band CA configurations for n24 and n77 to clause 4.3.1                                                                                           17.4.0
  2022-03          RAN\#95               R5-220916   2259   \-    F     Addition of PRB-Id setting for RRM test cases                                                                                                                         17.4.0
  2022-03          RAN\#95               R5-220955   2262   \-    F     Updates to IE UE Route Selection Policy Rules                                                                                                                         17.4.0
  2022-03          RAN\#95               R5-220960   2264   \-    F     Addition of test frequency for DC\_7C\_n78A                                                                                                                           17.4.0
  2022-03          RAN\#95               R5-220972   2265   \-    F     Addition of test frequencies for Rel-16 EN-DC configurations                                                                                                          17.4.0
  2022-03          RAN\#95               R5-220974   2266   \-    F     Correction to applicability for protocol testing for inter-band EN-DC configurations                                                                                  17.4.0
  2022-03          RAN\#95               R5-221070   2269   \-    F     USIM configurations for NR EIEI test cases                                                                                                                            17.4.0
  2022-03          RAN\#95               R5-221104   2270   \-    F     Addition of new USIM configuration for RACS test case                                                                                                                 17.4.0
  2022-03          RAN\#95               R5-221132   2271   \-    F     Updating channel bandwidths for NR band n97                                                                                                                           17.4.0
  2022-03          RAN\#95               R5-221133   2272   \-    F     Updating test frequencies for NR band n97                                                                                                                             17.4.0
  2022-03          RAN\#95               R5-221167   2275   \-    F     Update to Ciphering algo IE for FR1 NSA SDR                                                                                                                           17.4.0
  2022-03          RAN\#95               R5-221176   2276   \-    F     Introduction of test frequencies for NR CA configurations CA\_n5A-n7A, CA\_n5A-n78A and CA\_n7A-n78A                                                                  17.4.0
  2022-03          RAN\#95               R5-221186   2278   \-    F     Introduction of test frequencies for DC\_1A\_n5A, DC\_1A\_n7A, DC\_3A\_n5A, DC\_7A\_n5A, DC\_28A\_n7A                                                                 17.4.0
  2022-03          RAN\#95               R5-221255   2282   \-    F     Update K1 value for RRM TDD FR1 30kHz RMC                                                                                                                             17.4.0
  2022-03          RAN\#95               R5-221264   2284   \-    F     Correction of csi-ResourceConfigId                                                                                                                                    17.4.0
  2022-03          RAN\#95               R5-221265   2285   \-    F     Correction of DMRS-DownlinkConfig                                                                                                                                     17.4.0
  2022-03          RAN\#95               R5-221292   2287   \-    F     Addition of Setup Diagram for RRM multicell 2x2 test cases                                                                                                            17.4.0
  2022-03          RAN\#95               R5-221369   2289   \-    F     Update to PUCCH resource configuration for Scell CSI                                                                                                                  17.4.0
  2022-03          RAN\#95               R5-221377   2290   \-    F     Addition of Test frequencies for NE-DC band configurations for signalling testing                                                                                     17.4.0
  2022-03          RAN\#95               R5-221389   2291   \-    F     Correction to SIG test frequencies for intra-band non-contiguous CA                                                                                                   17.4.0
  2022-03          RAN\#95               R5-221413   2293   \-    F     Update IE SDAP-Config                                                                                                                                                 17.4.0
  2022-03          RAN\#95               R5-221419   2173   1     F     Update chapter 4.5.1 General                                                                                                                                          17.4.0
  2022-03          RAN\#95               R5-221420   2233   1     F     Correction to RRCReconfiguration message with condition REEST                                                                                                         17.4.0
  2022-03          RAN\#95               R5-221421   2277   1     F     Correction to the BWP-DownlinkDedicated                                                                                                                               17.4.0
  2022-03          RAN\#95               R5-221422   2280   1     F     NE-DC support for UECapabilityEnquiry and UECapabilityInformation messages                                                                                            17.4.0
  2022-03          RAN\#95               R5-221423   2194   1     F     Correction to IMS MO speech call establishment generic procedure                                                                                                      17.4.0
  2022-03          RAN\#95               R5-221424   2176   1     F     Correction to test procedure 4.9.11 IMS Emergency call or eCall over IMS establishment in 5GC with IMS emergency registration                                         17.4.0
  2022-03          RAN\#95               R5-221425   2177   1     F     Correction to test procedure 4.9.12 IMS Emergency call or eCall over IMS establishment in 5GC without IMS emergency registration                                      17.4.0
  2022-03          RAN\#95               R5-221426   2263   1     F     Updates to IE Route Selection Descriptors                                                                                                                             17.4.0
  2022-03          RAN\#95               R5-221491   2168   1     F     Update of NR CA configurations for Protocol testing with NR CA 3CC                                                                                                    17.4.0
  2022-03          RAN\#95               R5-221492   2169   1     F     Update of inter-band cell environment for Protocol testing with NR CA 3CC                                                                                             17.4.0
  2022-03          RAN\#95               R5-221493   2286   1     F     Modification of common test environment for EHC testing                                                                                                               17.4.0
  2022-03          RAN\#95               R5-221499   2207   1     F     Correction to generic test procedures for NR SL MIMO tests                                                                                                            17.4.0
  2022-03          RAN\#95               R5-221500   2209   1     F     Addition of test procedures for releasing unicast link                                                                                                                17.4.0
  2022-03          RAN\#95               R5-221501   2210   1     F     Addition of test procedures for data exchanging on unicast link                                                                                                       17.4.0
  2022-03          RAN\#95               R5-221502   2211   1     F     Correction to PC5 RRC message MasterInformationBlockSidelink                                                                                                          17.4.0
  2022-03          RAN\#95               R5-221503   2212   1     F     Correction to PC5 RRC message MeasurementReportSidelink                                                                                                               17.4.0
  2022-03          RAN\#95               R5-221504   2213   1     F     Correction to PC5 RRC message RRCReconfigurationSidelink                                                                                                              17.4.0
  2022-03          RAN\#95               R5-221505   2214   1     F     Correction to PC5 RRC message RRCReconfigurationCompleteSidelink                                                                                                      17.4.0
  2022-03          RAN\#95               R5-221506   2215   1     F     Correction to PC5 RRC message RRCReconfigurationFailureSidelink                                                                                                       17.4.0
  2022-03          RAN\#95               R5-221507   2216   1     F     Correction to PC5 RRC message UECapabilityEnquirySidelink                                                                                                             17.4.0
  2022-03          RAN\#95               R5-221508   2217   1     F     Correction to PC5 RRC message UECapabilityInformationSidelink                                                                                                         17.4.0
  2022-03          RAN\#95               R5-221509   2222   1     F     Correction to V2X message DIRECT LINK ESTABLISHMENT REQUEST                                                                                                           17.4.0
  2022-03          RAN\#95               R5-221510   2223   1     F     Correction to V2X message DIRECT LINK ESTABLISHMENT ACCEPT                                                                                                            17.4.0
  2022-03          RAN\#95               R5-221511   2224   1     F     Correction to V2X message DIRECT LINK RELEASE REQUEST                                                                                                                 17.4.0
  2022-03          RAN\#95               R5-221512   2225   1     F     Correction to V2X message DIRECT LINK RELEASE ACCEPT                                                                                                                  17.4.0
  2022-03          RAN\#95               R5-221513   2226   1     F     Correction to V2X message DIRECT LINK KEEPALIVE REQUEST                                                                                                               17.4.0
  2022-03          RAN\#95               R5-221514   2227   1     F     Correction to V2X message DIRECT LINK SECURITY MODE COMMAND                                                                                                           17.4.0
  2022-03          RAN\#95               R5-221515   2228   1     F     Correction to V2X message DIRECT LINK SECURITY MODE COMPLETE                                                                                                          17.4.0
  2022-03          RAN\#95               R5-221584   2251   1     F     Addition of default DCI\_1\_2 for URLLC                                                                                                                               17.4.0
  2022-03          RAN\#95               R5-221591   2203   1     F     Addition of positioning system information blocks associated parameters                                                                                               17.4.0
  2022-03          RAN\#95               R5-221667   2258   1     F     Correction to test frequency range for n14                                                                                                                            17.4.0
  2022-03          RAN\#95               R5-221668   2268   1     F     Correction of 4.3.1.2.4.4.2 for test frequencies for CA\_n260\_A-I                                                                                                    17.4.0
  2022-03          RAN\#95               R5-221669   2236   1     F     Correction to default RRC IEs for RRM                                                                                                                                 17.4.0
  2022-03          RAN\#95               R5-221670   2167   1     F     Updated the related RRC information for DSS                                                                                                                           17.4.0
  2022-03          RAN\#95               R5-221671   2190   1     F     Added FR2 connection diagram using modulated interferer                                                                                                               17.4.0
  2022-03          RAN\#95               R5-221672   2244   1     F     Correction of 4.1.1 on removal of lower humidity limit in NR test environment                                                                                         17.4.0
  2022-03          RAN\#95               R5-221757   2267   1     F     Correction of 4.3.1.1.5.48 for test frequencies of CA\_n48\_2A                                                                                                        17.4.0
  2022-03          RAN\#95               R5-221787   2283   1     F     Update of mid test channel bandwidth for band n25                                                                                                                     17.4.0
  2022-03          RAN\#95               R5-221815   2247   1     F     Update to NR sidelink preconfiguration                                                                                                                                17.4.0
  2022-03          RAN\#95               R5-221816   2248   1     F     Update to GNSS configuration for NR sidelink                                                                                                                          17.4.0
  2022-03          RAN\#95               R5-221869   2273   1     F     Updating test frequencies for NR band n1                                                                                                                              17.4.0
  2022-03          RAN\#95               R5-221871   2185   1     F     Add test frequencies for R17 NR inter-band CA configurations in FR1                                                                                                   17.4.0
  2022-03          RAN\#95               R5-221872   2187   1     F     Addition of test frequencies for NE-DC configurations DC\_n28A\_3A, DC\_n28A\_3C, DC\_n28A\_39A, DC\_n28A\_39C                                                        17.4.0
  2022-03          RAN\#95               R5-221873   2202   1     F     Update of protocol testing applicability for 3CC inter-band NR DC configurations                                                                                      17.4.0
  2022-03          RAN\#95               R5-221874   2261   1     F     Addition of several NR CA combinations to FR1 inter-band configurations table                                                                                         17.4.0
  2022-03          RAN\#95               R5-222039   2205   1     F     Correction to cl 4.5.3 RRC\_INACTIVE generic procedure                                                                                                                17.4.0
  2022-06          RAN\#96               R5-222122   2294   \-    F     Correction for Procedure for UE-requested PDU session modification after the first S1 to N1 mode change                                                               17.5.0
  2022-06          RAN\#96               R5-222173   2296   \-    F     Introduction of test frequencies for CA\_n77C BCS0 and BCS1                                                                                                           17.5.0
  2022-06          RAN\#96               R5-222175   2297   \-    F     Introduction of test frequencies for CA\_n77C for protocol testing                                                                                                    17.5.0
  2022-06          RAN\#96               R5-222283   2300   \-    F     Introduction of test frequencies for Rel-16 inter-band EN-DC three band combinations within FR1                                                                       17.5.0
  2022-06          RAN\#96               R5-222308   2302   \-    F     Introduction of NR-DC in FR1 for test setup diagrams                                                                                                                  17.5.0
  2022-06          RAN\#96               R5-222329   2303   \-    F     Correction of test frequencies for CA\_n66(2A) BCS1 and BCS2                                                                                                          17.5.0
  2022-06          RAN\#96               R5-222380   2308   \-    F     Updating RRCReconfiguration and RadioBearerConfig for NR-DC and NE-DC                                                                                                 17.5.0
  2022-06          RAN\#96               R5-222431   2310   \-    F     Correction to message contents for CQI reporting                                                                                                                      17.5.0
  2022-06          RAN\#96               R5-222460   2312   \-    F     Updates to REGISTRATION ACCEPT message                                                                                                                                17.5.0
  2022-06          RAN\#96               R5-222461   2313   \-    F     Updates to Configuration Update Command message                                                                                                                       17.5.0
  2022-06          RAN\#96               R5-222462   2314   \-    F     Updates to Registration Reject message                                                                                                                                17.5.0
  2022-06          RAN\#96               R5-222463   2315   \-    F     Updates to De-registration Request message                                                                                                                            17.5.0
  2022-06          RAN\#96               R5-222464   2316   \-    F     Update of Combinations of system information blocks for NE-DC                                                                                                         17.5.0
  2022-06          RAN\#96               R5-222502   2317   \-    F     Addition of test frequency for performance test cases                                                                                                                 17.5.0
  2022-06          RAN\#96               R5-222503   2318   \-    F     Addition of locationAndBandwidth for BW 45 MHz                                                                                                                        17.5.0
  2022-06          RAN\#96               R5-222512   2319   \-    F     Correction to generic procedure 4.9.28                                                                                                                                17.5.0
  2022-06          RAN\#96               R5-222513   2320   \-    F     Editorial update RRCReconfiguration                                                                                                                                   17.5.0
  2022-06          RAN\#96               R5-222537   2321   \-    F     Corrections to Table 7.3.1-12G                                                                                                                                        17.5.0
  2022-06          RAN\#96               R5-222565   2324   \-    F     Update IE P-Max                                                                                                                                                       17.5.0
  2022-06          RAN\#96               R5-222566   2325   \-    F     Editorial update IE FreqBandList                                                                                                                                      17.5.0
  2022-06          RAN\#96               R5-222567   2326   \-    F     Editorial update IE CellGroupConfig                                                                                                                                   17.5.0
  2022-06          RAN\#96               R5-222568   2327   \-    F     Editorial update IE CellGroupId                                                                                                                                       17.5.0
  2022-06          RAN\#96               R5-222570   2328   \-    F     Editorial update IE PDCCH-ConfigCommon                                                                                                                                17.5.0
  2022-06          RAN\#96               R5-222572   2329   \-    F     Addition of CA configuration for CA\_n29A-n71A                                                                                                                        17.5.0
  2022-06          RAN\#96               R5-222617   2331   \-    F     Addition of default message contents for NR SL Demod                                                                                                                  17.5.0
  2022-06          RAN\#96               R5-222647   2338   \-    F     Correction to sidelink IE SL-ReportConfigList                                                                                                                         17.5.0
  2022-06          RAN\#96               R5-222650   2341   \-    F     Correction to general functional requirements for RedCap test                                                                                                         17.5.0
  2022-06          RAN\#96               R5-222657   2344   \-    F     Editorial update IE SCellIndex                                                                                                                                        17.5.0
  2022-06          RAN\#96               R5-222818   2346   \-    F     Correction to V2X message                                                                                                                                             17.5.0
  2022-06          RAN\#96               R5-222836   2354   \-    F     Clarification of Annex C for calculation of SSB and CORESET\#0 for PCells                                                                                             17.5.0
  2022-06          RAN\#96               R5-222876   2370   \-    F     Removing redundant ciphering algorithm for SDR testing                                                                                                                17.5.0
  2022-06          RAN\#96               R5-222917   2372   \-    F     Connection diagram for 1x2 nDLCA Demodulation and CSI cases                                                                                                           17.5.0
  2022-06          RAN\#96               R5-222924   2373   \-    F     Addition of connection diagram for Tx Diversity support                                                                                                               17.5.0
  2022-06          RAN\#96               R5-222933   2374   \-    F     Update of auxiliary procedure 4.5A.2B                                                                                                                                 17.5.0
  2022-06          RAN\#96               R5-223025   2376   \-    F     Update of NR inter-band CA configurations in FR1                                                                                                                      17.5.0
  2022-06          RAN\#96               R5-223067   2378   \-    F     Addition of test frequency for NR inter-band CA configurations including n1                                                                                           17.5.0
  2022-06          RAN\#96               R5-223072   2379   \-    F     Introduction of test frequencies for CA\_n258G for protocol testing                                                                                                   17.5.0
  2022-06          RAN\#96               R5-223084   2382   \-    F     Corrections to usages of Annex A.6 of TS 34.229-5                                                                                                                     17.5.0
  2022-06          RAN\#96               R5-223126   2397   \-    F     Introducing band configuration DC\_20A\_n257A                                                                                                                         17.5.0
  2022-06          RAN\#96               R5-223158   2399   \-    F     Editorial update IE ServCellIndex                                                                                                                                     17.5.0
  2022-06          RAN\#96               R5-223197   2401   \-    F     Introduction of test frequencies for additional Rel-17 NR CA and EN-DC inter-band configurations                                                                      17.5.0
  2022-06          RAN\#96               R5-223222   2403   \-    F     Correction to 4.3.1.1.2.1 on test frequencies for NR inter-band CA configurations in FR1 with two bands                                                               17.5.0
  2022-06          RAN\#96               R5-223223   2404   \-    F     Correction to 4.3.1.1.2.2 on test frequencies for NR inter-band CA configurations in FR1 with three bands                                                             17.5.0
  2022-06          RAN\#96               R5-223224   2405   \-    F     Correction to 4.3.1.1.5.66 on test frequencies for NR intra-band non-contiguous CA configurations of CA\_n66 with class 2A                                            17.5.0
  2022-06          RAN\#96               R5-223225   2406   \-    F     Correction to 4.3.1.1.5.71 on test frequencies for NR intra-band non-contiguous CA configurations of CA\_n71 with class 2A                                            17.5.0
  2022-06          RAN\#96               R5-223229   2410   \-    F     Correction to 4.3.1.4.1.3 on test frequencies for inter-band EN-DC R17 configurations with three bands                                                                17.5.0
  2022-06          RAN\#96               R5-223234   2411   \-    F     Editorial correction to 4.3.1.2.2 on test frequencies for NR inter-band CA configurations in FR2 for CA\_n260-n261                                                    17.5.0
  2022-06          RAN\#96               R5-223250   2412   \-    F     Hardcoding USIM configurations                                                                                                                                        17.5.0
  2022-06          RAN\#96               R5-223341   2375   1     F     Update of Test procedure for IMS MO Emergency call release                                                                                                            17.5.0
  2022-06          RAN\#96               R5-223359   2332   1     F     Addition of test frequency for NR SL concurrent                                                                                                                       17.5.0
  2022-06          RAN\#96               R5-223360   2333   1     F     Correction to default configuration of SCI                                                                                                                            17.5.0
  2022-06          RAN\#96               R5-223361   2334   1     F     Correction to sidelink IE SL-BWP-PoolConfig                                                                                                                           17.5.0
  2022-06          RAN\#96               R5-223362   2335   1     F     Correction to sidelink IE SL-BWP-PoolConfigCommon                                                                                                                     17.5.0
  2022-06          RAN\#96               R5-223363   2336   1     F     Correction to sidelink IE SL-FreqConfig                                                                                                                               17.5.0
  2022-06          RAN\#96               R5-223364   2337   1     F     Correction to sidelink IE SL-FreqConfigCommon                                                                                                                         17.5.0
  2022-06          RAN\#96               R5-223365   2339   1     F     Correction to test procedures for unicast link establishment                                                                                                          17.5.0
  2022-06          RAN\#96               R5-223387   2330   1     F     Addition of scheduling information for positioning system information blocks                                                                                          17.5.0
  2022-06          RAN\#96               R5-223399   2295   1     F     Addition of SIB11 to common environment for early measurements                                                                                                        17.5.0
  2022-06          RAN\#96               R5-223400   2414   1     F     Modification of SIB1 in common environment for idle/inactive measurements                                                                                             17.5.0
  2022-06          RAN\#96               R5-223410   2340   1     F     Addition of abbreviations for RedCap test                                                                                                                             17.5.0
  2022-06          RAN\#96               R5-223413   2380   1     F     Updates to Test procedure 4.9.15                                                                                                                                      17.5.0
  2022-06          RAN\#96               R5-223414   2307   1     F     Editorial updates to SIBs                                                                                                                                             17.5.0
  2022-06          RAN\#96               R5-223415   2381   1     F     Updates to Data-off condition for PDU SESSION ESTABLISHMENT REQUEST message                                                                                           17.5.0
  2022-06          RAN\#96               R5-223416   2299   1     F     Resolving test frequency for n53 10 Mhz CBW                                                                                                                           17.5.0
  2022-06          RAN\#96               R5-223417   2353   1     F     Correction to Combinations of system information blocks                                                                                                               17.5.0
  2022-06          RAN\#96               R5-223480   2402   1     F     Corrections on mandatory channel bandwidths after Rel-15                                                                                                              17.5.0
  2022-06          RAN\#96               R5-223602   2415   \-    F     Correction to 4.3.1.4.1.3 on test frequencies for DC\_1A-28A\_n78C                                                                                                    17.5.0
  2022-06          RAN\#96               R5-223649   2398   1     F     Introduction of test frequencies for 3 band EN-DC configurations                                                                                                      17.5.0
  2022-06          RAN\#96               R5-223650   2400   1     F     Introduction of test frequencies for additional Rel-16 NR CA DC and EN-DC inter-band configurations                                                                   17.5.0
  2022-06          RAN\#96               R5-223651   2407   1     F     Correction to 4.3.1.1.5.77 on test frequencies for NR intra-band non-contiguous CA configurations of CA\_n77 with class 2A                                            17.5.0
  2022-06          RAN\#96               R5-223652   2408   1     F     Correction to 4.3.1.1.5.78 on test frequencies for NR intra-band non-contiguous CA configurations of CA\_n78 with class 2A                                            17.5.0
  2022-06          RAN\#96               R5-223653   2409   1     F     Correction to 4.3.1.4.1.3 on test frequencies for inter-band EN-DC R16 configurations                                                                                 17.5.0
  2022-06          RAN\#96               R5-223755   2301   1     F     Introduction of test frequencies for NR-DC in FR1                                                                                                                     17.5.0
  2022-06          RAN\#96               R5-223784   2371   1     F     Addition of RedCap default test channel bandwidth                                                                                                                     17.5.0
  2022-06          RAN\#96               R5-223792   2322   1     F     Correction to test frequency for n53                                                                                                                                  17.5.0
  2022-06          RAN\#96               R5-223793   2369   1     F     Clarification of PCC and SCC configuration for CA test cases                                                                                                          17.5.0
  2022-06          RAN\#96               R5-223795   2323   1     F     CR on Permitted Methodologies and Applicability                                                                                                                       17.5.0
  2022-06          RAN\#96               R5-223796   2377   1     F     Add new messages and procedure for test function to limit Pcell Power                                                                                                 17.5.0
  2022-09          RAN\#97               R5-223987   2416   \-    F     Correction to test procedure 4.9.11 IMS Emergency call or eCall over IMS establishment in 5GC with IMS emergency registration                                         17.6.0
  2022-09          RAN\#97               R5-224033   2417   \-    F     Introduction of test frequencies for NR-U band n46                                                                                                                    17.6.0
  2022-09          RAN\#97               R5-224034   2418   \-    F     Introduction of test frequencies for NR-U band n96                                                                                                                    17.6.0
  2022-09          RAN\#97               R5-224094   2429   \-    F     Update of MDT default RRC messages and IEs                                                                                                                            17.6.0
  2022-09          RAN\#97               R5-224139   2434   \-    F     Add IE BeamFailureRecoveryServingCellConfig                                                                                                                           17.6.0
  2022-09          RAN\#97               R5-224140   2435   \-    F     Add IE BetaOffsetsCrossPri                                                                                                                                            17.6.0
  2022-09          RAN\#97               R5-224149   2436   \-    F     Introduction of test frequencies for Rel-16 inter-band DC\_3A-7A-20A\_n8A within FR1                                                                                  17.6.0
  2022-09          RAN\#97               R5-224166   2437   \-    F     Correction to Table 4.7.2-2 PDU Session Establishment Accept                                                                                                          17.6.0
  2022-09          RAN\#97               R5-224179   2438   \-    F     Test frequencies for NR DC configurations in FR1 for signalling testing                                                                                               17.6.0
  2022-09          RAN\#97               R5-224235   2443   \-    F     Correction of the styles of the subclauses in 4.3.1.1 and 4.3.1.2                                                                                                     17.6.0
  2022-09          RAN\#97               R5-224276   2445   \-    F     Add IE CandidateBeamRS                                                                                                                                                17.6.0
  2022-09          RAN\#97               R5-224284   2446   \-    F     Add IE CFR-ConfigMulticast                                                                                                                                            17.6.0
  2022-09          RAN\#97               R5-224290   2447   \-    F     Add IEs DL-PRS-ProcessingWindowPreConfig, DMRS-BundlingPUCCH-Config and DMRS-BundlingPUSCH-Config                                                                     17.6.0
  2022-09          RAN\#97               R5-224380   2459   \-    F     Add IE FreqPriorityListNRSlicing                                                                                                                                      17.6.0
  2022-09          RAN\#97               R5-224458   2465   \-    F     Alignment CSI-ResourcePeriodicityAndOffset to CSI-RS.3.2 TDD                                                                                                          17.6.0
  2022-09          RAN\#97               R5-224459   2466   \-    F     Correction derivation path Table 7.3.1-35                                                                                                                             17.6.0
  2022-09          RAN\#97               R5-224460   2467   \-    F     Correction to 7.3.1-12G                                                                                                                                               17.6.0
  2022-09          RAN\#97               R5-224462   2469   \-    F     Definition of ZP-CSI-RS-ResourceSetId                                                                                                                                 17.6.0
  2022-09          RAN\#97               R5-224638   2478   \-    F     Clarification to Antenna ports of DCI format 1\_1 for RF TCs                                                                                                          17.6.0
  2022-09          RAN\#97               R5-224639   2479   \-    F     Correction to CSI-MeasConfig for RRM                                                                                                                                  17.6.0
  2022-09          RAN\#97               R5-224658   2482   \-    F     Add IE GapPriority                                                                                                                                                    17.6.0
  2022-09          RAN\#97               R5-224662   2484   \-    F     Add IE HysteresisLocation                                                                                                                                             17.6.0
  2022-09          RAN\#97               R5-224685   2485   \-    F     Correction to IMS MO Video call establishment test procedure in 5GC                                                                                                   17.6.0
  2022-09          RAN\#97               R5-224686   2486   \-    F     Correction to IMS MT Video call establishment test procedure in 5GC                                                                                                   17.6.0
  2022-09          RAN\#97               R5-224689   2489   \-    F     Correction to IMS MT speech call establishment test procedure in 5GC                                                                                                  17.6.0
  2022-09          RAN\#97               R5-224725   2491   \-    F     Update the SN-FieldLength of PDCP-Config and RLC-Config for RedCap test                                                                                               17.6.0
  2022-09          RAN\#97               R5-224740   2495   \-    F     Add Default configuration for DCI format 4\_1 scheduling MBS Multicast test                                                                                           17.6.0
  2022-09          RAN\#97               R5-224741   2496   \-    F     Add Default configuration for DCI format 4\_2 scheduling MBS Multicast test                                                                                           17.6.0
  2022-09          RAN\#97               R5-224762   2508   \-    F     Add IE MeasGapId                                                                                                                                                      17.6.0
  2022-09          RAN\#97               R5-224763   2509   \-    F     Add IE MeasObjectRxTxDiff                                                                                                                                             17.6.0
  2022-09          RAN\#97               R5-224816   2511   \-    F     Add IE MeasResultRxTxTimeDiff                                                                                                                                         17.6.0
  2022-09          RAN\#97               R5-224817   2512   \-    F     Add IE MRB-Identity                                                                                                                                                   17.6.0
  2022-09          RAN\#97               R5-224818   2513   \-    F     Add IEs MUSIM-GapConfig, MUSIM-GapID and MUSIM-GapInfo                                                                                                                17.6.0
  2022-09          RAN\#97               R5-224819   2514   \-    F     Add IEs NeedForGapNCSG-ConfigEUTRA, NeedForGapNCSG-ConfigNR, NeedForGapNCSG-InfoEUTRA and NeedForGapNCSG-InfoNR                                                       17.6.0
  2022-09          RAN\#97               R5-224820   2515   \-    F     Add IE NonCellDefiningSSB                                                                                                                                             17.6.0
  2022-09          RAN\#97               R5-224821   2516   \-    F     Add IE NR-DL-PRS-PDC-Info                                                                                                                                             17.6.0
  2022-09          RAN\#97               R5-224822   2517   \-    F     Add IEs NSAG-IdentityInfo and NTN-Config                                                                                                                              17.6.0
  2022-09          RAN\#97               R5-224824   2519   \-    F     Add IEs RxTxTimeDiff, SCellActivationRS-Config and SCellActivationRS-ConfigId                                                                                         17.6.0
  2022-09          RAN\#97               R5-224825   2520   \-    F     Add IE SemiStaticChannelAccessConfigUE                                                                                                                                17.6.0
  2022-09          RAN\#97               R5-224859   2521   \-    F     Add IE TCI-Info                                                                                                                                                       17.6.0
  2022-09          RAN\#97               R5-224860   2522   \-    F     Add IE UE-TimersAndConstantsRemoteUE                                                                                                                                  17.6.0
  2022-09          RAN\#97               R5-224861   2523   \-    F     Add IEs UL-ExcessDelayConfig and UE UL-GapFR2-Config                                                                                                                  17.6.0
  2022-09          RAN\#97               R5-224862   2524   \-    F     Add IEs Uplink-PowerControl, Uu-RelayRLC-ChannelConfig and Uu-RelayRLC-ChannelID                                                                                      17.6.0
  2022-09          RAN\#97               R5-224863   2525   \-    F     Add IE AppLayerMeasParameters                                                                                                                                         17.6.0
  2022-09          RAN\#97               R5-224864   2526   \-    F     Add IE FR2-2-AccessParamsPerBand                                                                                                                                      17.6.0
  2022-09          RAN\#97               R5-224877   2528   \-    F     Add IE NTN-Parameters                                                                                                                                                 17.6.0
  2022-09          RAN\#97               R5-224878   2529   \-    F     Add IE PosSRS-RRC-Inactive-OutsideInitialUL-BWP-r17                                                                                                                   17.6.0
  2022-09          RAN\#97               R5-224880   2531   \-    F     Add IE RedCapParameters                                                                                                                                               17.6.0
  2022-09          RAN\#97               R5-224881   2532   \-    F     Add IE SRS-AllPosResourcesRRC-Inactive                                                                                                                                17.6.0
  2022-09          RAN\#97               R5-224882   2533   \-    F     Add IE UE-RadioPagingInfo                                                                                                                                             17.6.0
  2022-09          RAN\#97               R5-224883   2534   \-    F     Add IE AppLayerMeasConfig                                                                                                                                             17.6.0
  2022-09          RAN\#97               R5-224909   2535   \-    F     Update IE DownlinkConfigCommonSIB                                                                                                                                     17.6.0
  2022-09          RAN\#97               R5-224912   2537   \-    F     Update IE MeasObjectNR                                                                                                                                                17.6.0
  2022-09          RAN\#97               R5-224913   2538   \-    F     Add IE MeasResultForRSSI                                                                                                                                              17.6.0
  2022-09          RAN\#97               R5-224914   2539   \-    F     Update IE MeasResults                                                                                                                                                 17.6.0
  2022-09          RAN\#97               R5-224915   2540   \-    F     Add IE MeasRSSI-ReportConfig                                                                                                                                          17.6.0
  2022-09          RAN\#97               R5-224916   2541   \-    F     Update IE ReportConfigNR                                                                                                                                              17.6.0
  2022-09          RAN\#97               R5-224917   2542   \-    F     Add IE RMTC Config                                                                                                                                                    17.6.0
  2022-09          RAN\#97               R5-224992   2545   \-    F     Add IE DedicatedInfoF1c                                                                                                                                               17.6.0
  2022-09          RAN\#97               R5-225007   2546   \-    F     Add IE MeasConfigAppLayerId                                                                                                                                           17.6.0
  2022-09          RAN\#97               R5-225092   2550   \-    F     Adding new connection diagram for SUL with UL MIMO test case                                                                                                          17.6.0
  2022-09          RAN\#97               R5-225177   2553   \-    F     Introduction of new default 5GMM messages                                                                                                                             17.6.0
  2022-09          RAN\#97               R5-225178   2554   \-    F     Introduction of new default 5GSM messages                                                                                                                             17.6.0
  2022-09          RAN\#97               R5-225180   2556   \-    F     Updates to default 5GSM messages                                                                                                                                      17.6.0
  2022-09          RAN\#97               R5-225188   2557   \-    F     CR to Correct Permitted Methodologies and Applicability                                                                                                               17.6.0
  2022-09          RAN\#97               R5-225212   2558   \-    F     Update nrofRB for 200 MHz ChBw 120 kHz SCS                                                                                                                            17.6.0
  2022-09          RAN\#97               R5-225215   2559   \-    F     Update number of HARQ processes for RRM test cases                                                                                                                    17.6.0
  2022-09          RAN\#97               R5-225271   2555   1     F     Updates to default 5GMM messages                                                                                                                                      17.6.0
  2022-09          RAN\#97               R5-225280   2494   1     F     Add Default configuration for DCI format 4\_0 scheduling MBS Broadcast test                                                                                           17.6.0
  2022-09          RAN\#97               R5-225290   2471   1     F     Correction of NR SL message contents                                                                                                                                  17.6.0
  2022-09          RAN\#97               R5-225291   2472   1     F     Correction of test procedure 4.9.31 - Connectivity check                                                                                                              17.6.0
  2022-09          RAN\#97               R5-225299   2448   1     F     Updates to Table 4.6.3-16: CellAccessRelatedInfo for NPN                                                                                                              17.6.0
  2022-09          RAN\#97               R5-225300   2456   1     F     Addition of Test Environment for legacy test cases applicable to SNPN Only UE                                                                                         17.6.0
  2022-09          RAN\#97               R5-225310   2544   1     F     Update of protocol applicability for DC\_19A\_n77(2A), DC\_19A\_n78(2A), DC\_21A\_n77(2A) and DC\_21A\_n78(2A)                                                        17.6.0
  2022-09          RAN\#97               R5-225311   2462   1     F     Correction of the scheduling information for combination NR-15                                                                                                        17.6.0
  2022-09          RAN\#97               R5-225312   2463   1     F     Addition of message contents for DedicatedSIBRequest                                                                                                                  17.6.0
  2022-09          RAN\#97               R5-225316   2425   1     F     Update default message contents of RACH-ConfigDedicated                                                                                                               17.6.0
  2022-09          RAN\#97               R5-225321   2536   1     F     Update IE LBT FailureRecoveryConfig                                                                                                                                   17.6.0
  2022-09          RAN\#97               R5-225325   2497   1     F     Add test procedures for MBS Multicast test                                                                                                                            17.6.0
  2022-09          RAN\#97               R5-225326   2502   1     F     Add SIB20 for MBS Broadcast test                                                                                                                                      17.6.0
  2022-09          RAN\#97               R5-225327   2503   1     F     Add SIB21 for MBS Broadcast test                                                                                                                                      17.6.0
  2022-09          RAN\#97               R5-225328   2504   1     F     Add MBSBroadcastConfiguration for MBS Broadcast test                                                                                                                  17.6.0
  2022-09          RAN\#97               R5-225329   2505   1     F     Add MBSInterestIndication for MBS Broadcast test                                                                                                                      17.6.0
  2022-09          RAN\#97               R5-225330   2506   1     F     Add MBS information elements for MBS test                                                                                                                             17.6.0
  2022-09          RAN\#97               R5-225333   2475   1     F     Update of MDT message and information element                                                                                                                         17.6.0
  2022-09          RAN\#97               R5-225342   2492   1     F     Addition of RedCap default test channel bandwidth for signaling MFBI test                                                                                             17.6.0
  2022-09          RAN\#97               R5-225343   2493   1     F     Addition of RedCap default test channel bandwidth for signaling test                                                                                                  17.6.0
  2022-09          RAN\#97               R5-225352   2449   1     F     Update of Table 4.6.1-30 to add message contents values for SDT in UEAssistanceInformation                                                                            17.6.0
  2022-09          RAN\#97               R5-225353   2450   1     F     Update of Table 4.6.1-28 to add message contents values for SDT in SIB1                                                                                               17.6.0
  2022-09          RAN\#97               R5-225354   2451   1     F     Update of Table 4.6.1-16 to add message contents values for SDT in RRCRelease                                                                                         17.6.0
  2022-09          RAN\#97               R5-225355   2453   1     F     Update of Table 4.6.3-96 to add message contents values for SDT in PDCCH-ConfigCommon                                                                                 17.6.0
  2022-09          RAN\#97               R5-225356   2473   1     F     Addition of SIB16 for slice based cell reselection                                                                                                                    17.6.0
  2022-09          RAN\#97               R5-225357   2474   1     F     Updates to message contents for slice specific RACH configuration                                                                                                     17.6.0
  2022-09          RAN\#97               R5-225358   2464   1     F     Add UplinkDataCompression into PDCP-Config for NR UDC test                                                                                                            17.6.0
  2022-09          RAN\#97               R5-225362   2483   1     F     Updates to test procedures 4.9.12A and 4.9.12B                                                                                                                        17.6.0
  2022-09          RAN\#97               R5-225363   2458   1     F     Add IEs DRX-ConfigSL, EphemerisInfo, FeatureCombination and FeatureCombinationPreambles                                                                               17.6.0
  2022-09          RAN\#97               R5-225364   2530   1     F     Editorial update IE RAT-Type                                                                                                                                          17.6.0
  2022-09          RAN\#97               R5-225365   2549   1     F     Updating the values for IE P-Max                                                                                                                                      17.6.0
  2022-09          RAN\#97               R5-225366   2428   1     F     Updates on UE Power Limit Messages: Option 2                                                                                                                          17.6.0
  2022-09          RAN\#97               R5-225367   2548   1     F     Introducing FR2 signal test frequencies for intra-band contiguous 3CA                                                                                                 17.6.0
  2022-09          RAN\#97               R5-225681   2441   1     F     Correction of test channel bandwidth for R16                                                                                                                          17.6.0
  2022-09          RAN\#97               R5-225682   2442   1     F     Correction of test channel bandwidth for n79                                                                                                                          17.6.0
  2022-09          RAN\#97               R5-225684   2440   1     F     Correction of test channel bandwidth for R15                                                                                                                          17.6.0
  2022-09          RAN\#97               R5-225686   2439   1     F     Update UE capability information elements for PC1.5 duty cycle                                                                                                        17.6.0
  2022-09          RAN\#97               R5-225730   2476   1     F     Addition of test frequencies for DC\_21A\_n28A                                                                                                                        17.6.0
  2022-09          RAN\#97               R5-225731   2527   1     F     Addition of configurations for many 4CA NR combinations                                                                                                               17.6.0
  2022-09          RAN\#97               R5-225766   2543   1     F     Corrections on Mid test channel bandwidth for band n66 for Redcap                                                                                                     17.6.0
  2022-09          RAN\#97               R5-225780   2468   1     F     Correction quantity config for inter-RAT to UTRA                                                                                                                      17.6.0
  2022-09          RAN\#97               R5-225781   2477   1     F     Correction to connection diagram for DL CA Demodulation and CSI test cases                                                                                            17.6.0
  2022-09          RAN\#97               R5-225782   2481   1     F     Correction to RRC message for uplink CA                                                                                                                               17.6.0
  2022-12          RAN\#98               R5-225952   2563         F     Introduction of test channel bandwidths for new NR bands n91, n92, n93 and n94                                                                                        17.7.0
  2022-12          RAN\#98               R5-225953   2564         F     Introduction of test frequencies for new NR bands n91, n92, n93 and n94                                                                                               17.7.0
  2022-12          RAN\#98               R5-225970   2566         F     Inclusive Language Review and update of IE SIB3                                                                                                                       17.7.0
  2022-12          RAN\#98               R5-225971   2567         F     Inclusive Language Review and update of IE SIB4                                                                                                                       17.7.0
  2022-12          RAN\#98               R5-225972   2568         F     Inclusive Language Review and update of IE SIB5                                                                                                                       17.7.0
  2022-12          RAN\#98               R5-225973   2569         F     Inclusive Language Review and update of IE MeasObjectEUTRA                                                                                                            17.7.0
  2022-12          RAN\#98               R5-225974   2570         F     Inclusive Language Review and update of IE MeasObjectNR                                                                                                               17.7.0
  2022-12          RAN\#98               R5-225975   2571         F     Inclusive Language Review and update of IE ReportConfigNR                                                                                                             17.7.0
  2022-12          RAN\#98               R5-226020   2572         F     Update of test procedures 4.9.12A and 4.9.12B                                                                                                                         17.7.0
  2022-12          RAN\#98               R5-226040   2573         F     Correction to test procedure 4.9.7                                                                                                                                    17.7.0
  2022-12          RAN\#98               R5-226041   2574         F     Updates to SysInfo for SCells operating on NR CA bands with no UL frequency                                                                                           17.7.0
  2022-12          RAN\#98               R5-226110   2575         F     Correction to default configurations for RedCap RRM TCs                                                                                                               17.7.0
  2022-12          RAN\#98               R5-226247   2577         F     Add IE SIB17                                                                                                                                                          17.7.0
  2022-12          RAN\#98               R5-226248   2578         F     Add IE SIB18                                                                                                                                                          17.7.0
  2022-12          RAN\#98               R5-226249   2579         F     Add IE SIB19                                                                                                                                                          17.7.0
  2022-12          RAN\#98               R5-226250   2580         F     Update IE BeamFailureRecoveryRSConfig                                                                                                                                 17.7.0
  2022-12          RAN\#98               R5-226251   2581         F     Update IE BeamFailureRecoveryServingCellConfig                                                                                                                        17.7.0
  2022-12          RAN\#98               R5-226253   2583         F     Update IE DRX-ConfigSecondaryGroup                                                                                                                                    17.7.0
  2022-12          RAN\#98               R5-226254   2584         F     Update IE FreqPriorityListSlicing                                                                                                                                     17.7.0
  2022-12          RAN\#98               R5-226255   2585         F     Add IE FreqPriorityListDedicatedSlicing                                                                                                                               17.7.0
  2022-12          RAN\#98               R5-226257   2587         F     Update IE MUSIM-GapId                                                                                                                                                 17.7.0
  2022-12          RAN\#98               R5-226259   2589         F     Add IEs PCI-ARFCN-EUTRA and PCI-ARFCN-NR                                                                                                                              17.7.0
  2022-12          RAN\#98               R5-226260   2590         F     Add IE ReferenceLocation                                                                                                                                              17.7.0
  2022-12          RAN\#98               R5-226261   2591         F     Update IE RMTC-Config                                                                                                                                                 17.7.0
  2022-12          RAN\#98               R5-226262   2592         F     Add IE ServingCellAndBWP-Id                                                                                                                                           17.7.0
  2022-12          RAN\#98               R5-226263   2593         F     Update IE TCI-ActivatedConfig                                                                                                                                         17.7.0
  2022-12          RAN\#98               R5-226264   2594         F     Add IE TAR-Config                                                                                                                                                     17.7.0
  2022-12          RAN\#98               R5-226265   2595         F     Add IEs TCI-UL-State and TCI-UL-StateId                                                                                                                               17.7.0
  2022-12          RAN\#98               R5-226266   2596         F     Add IE TimeAlignmentTimer                                                                                                                                             17.7.0
  2022-12          RAN\#98               R5-226268   2598         F     Update IE PosSRS-RRC-Inactive-OutsideInitialUL-BWP                                                                                                                    17.7.0
  2022-12          RAN\#98               R5-226269   2599         F     Add IE PRS-ProcessingCapabilityOutsideMGinPPWperType                                                                                                                  17.7.0
  2022-12          RAN\#98               R5-226270   2600         F     Add IE SimultaneousRxTxPerBandPair                                                                                                                                    17.7.0
  2022-12          RAN\#98               R5-226271   2601         F     Update IE UE-MeasurementsAvailable                                                                                                                                    17.7.0
  2022-12          RAN\#98               R5-226352   2605         F     Addition of CGI specific information elements for R15 SON\_MDT                                                                                                        17.7.0
  2022-12          RAN\#98               R5-226366   2607         F     Removal of Test freqs for R16 pending CADC configs from cl 4.3.1                                                                                                      17.7.0
  2022-12          RAN\#98               R5-226367   2608         F     Removal of Test freqs for R17 pending CADC configs from cl 4.3.1                                                                                                      17.7.0
  2022-12          RAN\#98               R5-226390   2613         F     Editorial correction for test procedure sequence in 4.7.2-2 on 38.508-1 in rel17                                                                                      17.7.0
  2022-12          RAN\#98               R5-226400   2615         F     Updates for NR CA\_n5A-n77A, CA\_n66A-n77A                                                                                                                            17.7.0
  2022-12          RAN\#98               R5-226494   2616         F     Correct typo in Table 4.6.3-68                                                                                                                                        17.7.0
  2022-12          RAN\#98               R5-226495   2617         F     Corrections to Table 7.3.1-22                                                                                                                                         17.7.0
  2022-12          RAN\#98               R5-226496   2618         F     Corrections to Table 7.3.1-31                                                                                                                                         17.7.0
  2022-12          RAN\#98               R5-226669   2625         F     Update to K1 value for FDD RRM test cases                                                                                                                             17.7.0
  2022-12          RAN\#98               R5-226684   2626         F     Addition of 2x1 antenna connection for RedCap                                                                                                                         17.7.0
  2022-12          RAN\#98               R5-226691   2627         F     n66\_2A frequency correction                                                                                                                                          17.7.0
  2022-12          RAN\#98               R5-226693   2628         F     Corrections to ssbPositionInBurst for 7.3.1-x                                                                                                                         17.7.0
  2022-12          RAN\#98               R5-226694   2629         F     Corrections to RACHConfigCommon for RRM                                                                                                                               17.7.0
  2022-12          RAN\#98               R5-226695   2630         F     Removal of Table 7.3.1-33                                                                                                                                             17.7.0
  2022-12          RAN\#98               R5-226718   2638         F     Add low-mid-high ch BWs for NR-U                                                                                                                                      17.7.0
  2022-12          RAN\#98               R5-226727   2639         F     Update of test frequency for n3 R17 CBW                                                                                                                               17.7.0
  2022-12          RAN\#98               R5-226731   2641         F     Update IE Phy-ParametersSharedSpectrumChAccess                                                                                                                        17.7.0
  2022-12          RAN\#98               R5-226863   2644         F     Updating signalling test frequencies for n79 20MHz CBW                                                                                                                17.7.0
  2022-12          RAN\#98               R5-226864   2645         F     Updating test channel bandwidths for n79                                                                                                                              17.7.0
  2022-12          RAN\#98               R5-226894   2646         F     Update of n28 test frequencies for DC\_21A\_n28A in clause 6.2.3.1                                                                                                    17.7.0
  2022-12          RAN\#98               R5-226934   2647         F     Updates to default 5GMM messages                                                                                                                                      17.7.0
  2022-12          RAN\#98               R5-226935   2648         F     Updates to default 5GSM messages                                                                                                                                      17.7.0
  2022-12          RAN\#98               R5-227084   2650         F     Update to offsetToCarrier for DC\_21A\_n28A                                                                                                                           17.7.0
  2022-12          RAN\#98               R5-227087   2651         F     Addition of locationAndBandwidth for BW 35 MHz                                                                                                                        17.7.0
  2022-12          RAN\#98               R5-227101   2653         F     Correction to definition of SRB\_NR\_PDCP                                                                                                                             17.7.0
  2022-12          RAN\#98               R5-227108   2655         F     Test frequencies updates for band n7                                                                                                                                  17.7.0
  2022-12          RAN\#98               R5-227110   2657         F     Test frequencies updates for band n25                                                                                                                                 17.7.0
  2022-12          RAN\#98               R5-227111   2658         F     Test frequencies updates for band n66                                                                                                                                 17.7.0
  2022-12          RAN\#98               R5-227138   2660         F     Update of configuration of system information blocks for MBS Broadcast TC                                                                                             17.7.0
  2022-12          RAN\#98               R5-227139   2661         F     Update of MBS IE CFR-ConfigMCCH-MTCH                                                                                                                                  17.7.0
  2022-12          RAN\#98               R5-227142   2664         F     Editoral correction of physical layer parameters for scheduling of MBS                                                                                                17.7.0
  2022-12          RAN\#98               R5-227174   2671         F     Update PC5 message for LINK IDENTIFIER UPDATE procedure                                                                                                               17.7.0
  2022-12          RAN\#98               R5-227251   2674         F     Correction of test frequencies                                                                                                                                        17.7.0
  2022-12          RAN\#98               R5-227275   2677         F     Introduction of CA\_n48A-n77A and CA\_n71A-n77A configurations                                                                                                        17.7.0
  2022-12          RAN\#98               R5-227406   2614   1     F     Addition of Test procedure for deleting configured S-NSSAI, default configured S-NSSAI and allowed S-NSSAI                                                            17.7.0
  2022-12          RAN\#98               R5-227407   2582   1     F     Update IE DL-PPW-PreConfig                                                                                                                                            17.7.0
  2022-12          RAN\#98               R5-227408   2586   1     F     Add IE LTE-NeighCellsCRS-AssistInfoList                                                                                                                               17.7.0
  2022-12          RAN\#98               R5-227409   2597   1     F     Add IEs UplinkTxDirectCurrentMoreCarrierList and UplinkTxDirectCurrentTwoCarrierList                                                                                  17.7.0
  2022-12          RAN\#98               R5-227410   2676   1     F     Updates to connectivity options                                                                                                                                       17.7.0
  2022-12          RAN\#98               R5-227449   2619   1     F     Update to cl 4.5B.1 for SNPN-only UEs                                                                                                                                 17.7.0
  2022-12          RAN\#98               R5-227473   2649   1     F     Correction to EHC parametrization in 38.508-1                                                                                                                         17.7.0
  2022-12          RAN\#98               R5-227476   2678   1     F     Addition of USIM configuration for MUSIM test cases                                                                                                                   17.7.0
  2022-12          RAN\#98               R5-227477   2679   1     F     Addition of test procedure for registration of a MUSIM UE                                                                                                             17.7.0
  2022-12          RAN\#98               R5-227480   2620   1     F     Update of Table 4.6.1-28 to add message contents values for NTN in SIB1                                                                                               17.7.0
  2022-12          RAN\#98               R5-227499   2672   1     F     Updating SIB1 content with Paging Early Indication configuration                                                                                                      17.7.0
  2022-12          RAN\#98               R5-227507   2659   1     F     Update of CLOSE UE TEST LOOP message                                                                                                                                  17.7.0
  2022-12          RAN\#98               R5-227508   2662   1     F     Update of MBS IE TMGI                                                                                                                                                 17.7.0
  2022-12          RAN\#98               R5-227509   2663   1     F     Update of Radio resource control information elements for Broadcast MBS TC                                                                                            17.7.0
  2022-12          RAN\#98               R5-227510   2665   1     F     Update of DNN configuration for PDU session associated with MBS Multicast session                                                                                     17.7.0
  2022-12          RAN\#98               R5-227511   2666   1     F     Update of Procedure for MBS Multicast session join and session establishment                                                                                          17.7.0
  2022-12          RAN\#98               R5-227512   2667   1     F     Update of Radio resource control information elements for Multicast MBS TC                                                                                            17.7.0
  2022-12          RAN\#98               R5-227518   2670   1     F     Update common configurations for RedCap UE                                                                                                                            17.7.0
  2022-12          RAN\#98               R5-227542   2609   1     F     Update of information elements for slice specific RACH configuration                                                                                                  17.7.0
  2022-12          RAN\#98               R5-227544   2610   1     F     Update of MDT information element for SON\_MDT                                                                                                                        17.7.0
  2022-12          RAN\#98               R5-227587   2654   1     F     Update TS 38.508-1 clause 4.5B for RedCap UE                                                                                                                          17.7.0
  2022-12          RAN\#98               R5-227593   2611   1     F     Addition of parameter related to SOR-CMCI for DL NAS transport and UL NAS transport message in 38.508-1                                                               17.7.0
  2022-12          RAN\#98               R5-227700   2606   1     F     Removal of Test freqs for R15 pending CADC configs from cl 4.3.1                                                                                                      17.7.0
  2022-12          RAN\#98               R5-227701   2640   1     F     Update of test frequency for n8 R17 CBW 35MHz                                                                                                                         17.7.0
  2022-12          RAN\#98               R5-227702   2643   1     F     Adding test frequencies for n79 new CBW 10MHz and 20MHz                                                                                                               17.7.0
  2022-12          RAN\#98               R5-227703   2602   1     F     Update to IE Table 4.6.3-62A - HighSpeedConfig                                                                                                                        17.7.0
  2022-12          RAN\#98               R5-227639   2603   2     F     Update IE ServingCellConfigCommon                                                                                                                                     17.7.0
  2022-12          RAN\#98               R5-227705   2604   1     F     Update IE ServingCellConfigCommonSIB                                                                                                                                  17.7.0
  2022-12          RAN\#98               R5-227706   2673   1     F     Disabling of PUCCH intra-slot frequency hopping for RF                                                                                                                17.7.0
  2022-12          RAN\#98               R5-227840   2565   1     F     Introduction of test frequencies for signalling testing for new NR bands n91, n92, n93 and n94                                                                        17.7.0
  2022-12          RAN\#98               R5-227892   2675   1     F     Updates to determination of test frequencies for NR Intra-band Non-Contiguous CA                                                                                      17.7.0
  2023-03          RAN\#99               R5-230065   2680   \-    F     Introduction of test channel bandwidths for new NR bands n100, n101                                                                                                   17.8.0
  2023-03          RAN\#99               R5-230066   2681   \-    F     Introduction of test frequencies for new NR bands n100, n101                                                                                                          17.8.0
  2023-03          RAN\#99               R5-230067   2682   \-    F     Introduction of test frequencies for signalling testing for new NR bands n100, n101                                                                                   17.8.0
  2023-03          RAN\#99               R5-230093   2683   \-    F     Addition of test frequencies for new EN-DC comb within FR1                                                                                                            17.8.0
  2023-03          RAN\#99               R5-230103   2684   \-    F     Updates to clause 4.5B.2 for RedCap test environment                                                                                                                  17.8.0
  2023-03          RAN\#99               R5-230231   2692   \-    F     Update IEs SIB16, CellReselectionPriority, FreqPriorityListSlicing, NSAG-ID and NSAG-IdentityInfo                                                                     17.8.0
  2023-03          RAN\#99               R5-230279   2696   \-    F     Corrections to Clause 6.2.3.7 Test frequencies for NR sidelink configurations for signalling testing                                                                  17.8.0
  2023-03          RAN\#99               R5-230287   2697   \-    F     Update inter-band NR CA configurations of three bands CA\_n2A-n5A-n77A, CA\_n2A-n66A-n77A, and CA\_n5A-n66A-n77A                                                      17.8.0
  2023-03          RAN\#99               R5-230457   2700   \-    F     Correction to default configuration of RRC IEs for RedCap                                                                                                             17.8.0
  2023-03          RAN\#99               R5-230587   2703   \-    F     Update IE BWP-UplinkDedicated                                                                                                                                         17.8.0
  2023-03          RAN\#99               R5-230588   2704   \-    F     Update IE LBT-FailureRecoveryConfig                                                                                                                                   17.8.0
  2023-03          RAN\#99               R5-230601   2705   \-    F     update default message contents of ReportConfigInterRAT                                                                                                               17.8.0
  2023-03          RAN\#99               R5-230675   2713   \-    F     Correction to Test Procedures for Switch off/Power off                                                                                                                17.8.0
  2023-03          RAN\#99               R5-230753   2719   \-    F     Introduction or test frequencies for n46 and n96 in clause 6.2.3.1                                                                                                    17.8.0
  2023-03          RAN\#99               R5-230754   2720   \-    F     Corrections to Annex C for test frequency calculations                                                                                                                17.8.0
  2023-03          RAN\#99               R5-230755   2721   \-    F     Update IE DownlinkConfigCommonSIB                                                                                                                                     17.8.0
  2023-03          RAN\#99               R5-230882   2723   \-    F     NTN test channel bandwidths for n256 and n255                                                                                                                         17.8.0
  2023-03          RAN\#99               R5-230884   2724   \-    F     NR NTN test frequencies for n256                                                                                                                                      17.8.0
  2023-03          RAN\#99               R5-230897   2726   \-    F     Addition of test frequency for DC\_71A\_n2A                                                                                                                           17.8.0
  2023-03          RAN\#99               R5-230966   2728   \-    F     Correction to PUCCH secondHopPRB for RF condition                                                                                                                     17.8.0
  2023-03          RAN\#99               R5-230999   2729   \-    F     Update IE BWP-UplinkCommon                                                                                                                                            17.8.0
  2023-03          RAN\#99               R5-231002   2731   \-    F     Corrections to RRC Reconfiguration for SCell addition                                                                                                                 17.8.0
  2023-03          RAN\#99               R5-231023   2733   \-    F     Addition of default RRC message configuration for measurement gap enhancements                                                                                        17.8.0
  2023-03          RAN\#99               R5-231079   2735   \-    F     Updating test frequencies for n79                                                                                                                                     17.8.0
  2023-03          RAN\#99               R5-231185   2736   \-    F     Correction to PDU SESSION ESTABLISHMENT ACCEPT message                                                                                                                17.8.0
  2023-03          RAN\#99               R5-231218   2737   \-    F     Add condition to activate dedicated BWP to ServingCellConfig                                                                                                          17.8.0
  2023-03          RAN\#99               R5-231219   2738   \-    F     Addition of scheduling information for high accuracy GNSS posSibTypes                                                                                                 17.8.0
  2023-03          RAN\#99               R5-231227   2739   \-    F     Introduction of CA\_n41A-n71A configuration.                                                                                                                          17.8.0
  2023-03          RAN\#99               R5-231236   2744   \-    F     Update IE NPN-IdentityInfoList                                                                                                                                        17.8.0
  2023-03          RAN\#99               R5-231243   2747   \-    F     Test frequencies update for bands n8 and n25                                                                                                                          17.8.0
  2023-03          RAN\#99               R5-231399   2722   1     F     Add IEs PathlossReferenceRS and PathlossReferenceRS-Id                                                                                                                17.8.0
  2023-03          RAN\#99               R5-231423   2701   1     F     Correction to PHY parameters for SL mode 1 transmission                                                                                                               17.8.0
  2023-03          RAN\#99               R5-231424   2702   1     F     Correction to RRC IEs for SL mode 1 transmission                                                                                                                      17.8.0
  2023-03          RAN\#99               R5-231447   2695   1     F     Addition of CG SDT Configuration message contents for 3GPP SDT                                                                                                        17.8.0
  2023-03          RAN\#99               R5-231448   2727   1     F     Update of the contents of RRC messages for L2 U2N relay related operation                                                                                             17.8.0
  2023-03          RAN\#99               R5-231453   2750   1     F     Adding default contents for SIB17                                                                                                                                     17.8.0
  2023-03          RAN\#99               R5-231461   2716   1     F     Addition of System information combination for Rel-17 eNPN                                                                                                            17.8.0
  2023-03          RAN\#99               R5-231467   2707   1     F     Addition of Procedure for MBS Multicast session release                                                                                                               17.8.0
  2023-03          RAN\#99               R5-231468   2708   1     F     Update of Contents of Paging for Multicast MBS TC                                                                                                                     17.8.0
  2023-03          RAN\#99               R5-231469   2709   1     F     Correction of CLOSE UE TEST LOOP message for Loop Mode C                                                                                                              17.8.0
  2023-03          RAN\#99               R5-231470   2710   1     F     Correction of PDCP-Config for MBS TC                                                                                                                                  17.8.0
  2023-03          RAN\#99               R5-231471   2711   1     F     Correction of RadioBearerConfig for MBS TC                                                                                                                            17.8.0
  2023-03          RAN\#99               R5-231472   2712   1     F     Correction of CellGroupConfig for MBS TC                                                                                                                              17.8.0
  2023-03          RAN\#99               R5-231560   2715   1     F     Updates to SIB1 and SIB18 for Rel-17 Enpn                                                                                                                             17.8.0
  2023-03          RAN\#99               R5-231570   2690   1     F     Update IE SIB2                                                                                                                                                        17.8.0
  2023-03          RAN\#99               R5-231571   2706   1     F     update default message contents of MeasResults                                                                                                                        17.8.0
  2023-03          RAN\#99               R5-231577   2691   1     F     Update IEs SIB11, ARFCN-ValueEUTRA, MeasIdleConfig and EUTRA-PhysCellIdRange                                                                                          17.8.0
  2023-03          RAN\#99               R5-231603   2717   1     F     Correction of test frequencies for n46                                                                                                                                17.8.0
  2023-03          RAN\#99               R5-231604   2718   1     F     Correction of test frequencies for n96                                                                                                                                17.8.0
  2023-03          RAN\#99               R5-231634   2694   1     F     Introduction of CA\_n41A-n66A configuration.                                                                                                                          17.8.0
  2023-03          RAN\#99               R5-231792   2686   1     F     Update of Propagation Delay Compensation tables for UE Rx-Tx measurements                                                                                             17.8.0
  2023-03          RAN\#99               R5-231793   2725   1     F     Addition of test frequencies for R16 combos                                                                                                                           17.8.0
  2023-03          RAN\#99               R5-231867   2693   1     F     Correction to high range reference test frequency for n66 DL CA                                                                                                       17.8.0
  2023-03          RAN\#99               R5-231874   2698   1     F     Addition of test frequencies for new 3CC EN-DC comb within FR1                                                                                                        17.8.0
  2023-03          RAN\#99               R5-231902   2751   1     F     Correction to introduce search space configuration changes for DCI\_2-6 transmission                                                                                  17.8.0
  2023-06          RAN\#100              R5-232056   2752   \-    F     Correction to test procedure 4.9.9                                                                                                                                    17.9.0
  2023-06          RAN\#100              R5-232337   2756   \-    F     Addition of test frequencies for new 3CC EN-DC comb within FR2                                                                                                        17.9.0
  2023-06          RAN\#100              R5-232338   2757   \-    F     Addition of test frequencies for new EN-DC comb within FR2                                                                                                            17.9.0
  2023-06          RAN\#100              R5-232350   2758   \-    F     RF message exceptions for K1 and number of HARQ processes in CA                                                                                                       17.9.0
  2023-06          RAN\#100              R5-232441   2762   \-    F     Introduction of test channel bandwidths for new NR band n13                                                                                                           17.9.0
  2023-06          RAN\#100              R5-232442   2763   \-    F     Introduction of test frequencies for new NR band n13                                                                                                                  17.9.0
  2023-06          RAN\#100              R5-232443   2764   \-    F     Introduction of test frequencies for signalling testing for new NR band n13                                                                                           17.9.0
  2023-06          RAN\#100              R5-232497   2765   \-    F     Correction to default configuration of RRC IEs for NR cov enh test                                                                                                    17.9.0
  2023-06          RAN\#100              R5-232520   2766   \-    F     NR NTN test frequencies for n255                                                                                                                                      17.9.0
  2023-06          RAN\#100              R5-232576   2767   \-    F     Correction to RRC IEs for NR sidelink test                                                                                                                            17.9.0
  2023-06          RAN\#100              R5-232654   2770   \-    F     Update of NR inter-band CA configurations in FR1 for CA\_n3A-n8A                                                                                                      17.9.0
  2023-06          RAN\#100              R5-232693   2774   \-    F     Addition of NTN freq bands to clause 6.2.3 for Default test frequencies                                                                                               17.9.0
  2023-06          RAN\#100              R5-232712   2776   \-    F     Correction NZP-CSI-RS-ResourceSet for FR1                                                                                                                             17.9.0
  2023-06          RAN\#100              R5-232723   2781   \-    F     Correction to default P-Max value for Power Class 1.5 UEs                                                                                                             17.9.0
  2023-06          RAN\#100              R5-232743   2782   \-    F     Update of the contents of RRC messages for L2 U2N relay related operation                                                                                             17.9.0
  2023-06          RAN\#100              R5-232746   2783   \-    F     Update of the contents of Sidelink information elements                                                                                                               17.9.0
  2023-06          RAN\#100              R5-232790   2786   \-    F     Addition of test frequencies of CA\_n39A-n41A config TC 4.3.1.1.2.1                                                                                                   17.9.0
  2023-06          RAN\#100              R5-232877   2787   \-    F     Addition of new CA configuration CA-n41A-n66A-n71A                                                                                                                    17.9.0
  2023-06          RAN\#100              R5-232934   2789   \-    F     Update CSI-ReportConfig IE content for RRM testing                                                                                                                    17.9.0
  2023-06          RAN\#100              R5-232946   2793   \-    F     Delete NR-19 for MBS in the Common configurations of system information blocks                                                                                        17.9.0
  2023-06          RAN\#100              R5-232970   2794   \-    F     Update Service accept NAS message                                                                                                                                     17.9.0
  2023-06          RAN\#100              R5-232971   2795   \-    F     Update RadioBearerConfig-SRB2-DRB message                                                                                                                             17.9.0
  2023-06          RAN\#100              R5-232991   2797   \-    F     Correction to RRM PDCCH TCI-State                                                                                                                                     17.9.0
  2023-06          RAN\#100              R5-232992   2798   \-    F     Correction to RRM TRS CSI-ResourceConfig                                                                                                                              17.9.0
  2023-06          RAN\#100              R5-233091   2799   \-    F     Adding uplink CA test frequencies for CA\_n77(2A)                                                                                                                     17.9.0
  2023-06          RAN\#100              R5-233135   2804   \-    F     Correction to RF or RRM condition for default messages                                                                                                                17.9.0
  2023-06          RAN\#100              R5-233142   2805   \-    F     Update to test procedure for registration of a MUSIM UE                                                                                                               17.9.0
  2023-06          RAN\#100              R5-233195   2806   \-    F     Corrections to Test frequencies for NR CA configurations for signalling testing                                                                                       17.9.0
  2023-06          RAN\#100              R5-233317   2769   1     F     Correction to introduce search space configuration changes for DCI\_2-6 transmission                                                                                  17.9.0
  2023-06          RAN\#100              R5-233369   2775   1     F     Addition of new clause for UE Position Requirements for NR NTN testing                                                                                                17.9.0
  2023-06          RAN\#100              R5-233379   2785   1     F     Addition of a new combination of system information block for SIB16                                                                                                   17.9.0
  2023-06          RAN\#100              R5-233382   2791   1     F     Addition of Procedure to check TMGI and associated MRB reception in a multicast MBS session                                                                           17.9.0
  2023-06          RAN\#100              R5-233383   2792   1     F     Update PDCCH-Config for MSS condition                                                                                                                                 17.9.0
  2023-06          RAN\#100              R5-233406   2790   1     F     Update general configuration parameter for HD-FDD UE                                                                                                                  17.9.0
  2023-06          RAN\#100              R5-233423   2777   1     F     Addition of PC5 RRC message uuMessageTransferSidelink                                                                                                                 17.9.0
  2023-06          RAN\#100              R5-233424   2778   1     F     Addition of PC5 RRC RemoteUEInformationSidelink message                                                                                                               17.9.0
  2023-06          RAN\#100              R5-233425   2780   1     F     Update of PC5 RRC message Uu-RelayRLC-ChannelConfig                                                                                                                   17.9.0
  2023-06          RAN\#100              R5-233426   2779   1     F     Update of PC5 RRC message SL-L2RelayUE-Config                                                                                                                         17.9.0
  2023-06          RAN\#100              R5-233429   2755   1     F     Add generic procedure for Switch off / Power off procedure in MA PDU session Established on NR and WLAN                                                               17.9.0
  2023-06          RAN\#100              R5-233434   2771   1     F     Updates to SIB19 for NR NTN                                                                                                                                           17.9.0
  2023-06          RAN\#100              R5-233435   2772   1     F     Update IE ServingCellConfigCommon for NR NTN                                                                                                                          17.9.0
  2023-06          RAN\#100              R5-233436   2773   1     F     Update to clause 4.4.3 Common parameters for NR NTN                                                                                                                   17.9.0
  2023-06          RAN\#100              R5-233474   2768   1     F     Correction to switch off test procedure                                                                                                                               17.9.0
  2023-06          RAN\#100              R5-233500   2808   1     F     Correction of 38.508-1 4.1.1 on lower humidity limit in temperature test environment                                                                                  17.9.0
  2023-06          RAN\#100              R5-233674   2754   1     F     Addition and update of tables for HST FR2 scenario                                                                                                                    17.9.0
  2023-06          RAN\#100              R5-233675   2807   1     F     Update to TS 38.508-1 clause 4.6.3-200BB for FR2 UL Gaps IE                                                                                                           17.9.0
  2023-06          RAN\#100              R5-233676   2809   \-    F     Correction to frequency range for ssb-PositionsInBurst and SSB-ToMeasure                                                                                              17.9.0
  2023-06          RAN\#100              R5-233699   2759   1     F     Correction of test frequency parameters for n79                                                                                                                       17.9.0
  2023-06          RAN\#100              R5-233700   2802   1     F     Updating frequency calculation in Annex C.3.2                                                                                                                         17.9.0
  2023-06          RAN\#100              R5-233734   2788   2     F     Addition of test frequency for new 3/4 band EN-DC comb                                                                                                                17.9.0
  2023-09          RAN\#101              R5-233931   2812   \-    F     Clarify default ASN.1 contents                                                                                                                                        17.10.0
  2023-09          RAN\#101              R5-233932   2813   \-    F     Update IE MAC-CellGroupConfig                                                                                                                                         17.10.0
  2023-09          RAN\#101              R5-233944   2814   \-    F     Introduction of Inter-band NR CA configuration CA\_n20A-n78A                                                                                                          17.10.0
  2023-09          RAN\#101              R5-233987   2815   \-    F     Adding 5GS registration type for Rel-17 eNPN onboarding service.                                                                                                      17.10.0
  2023-09          RAN\#101              R5-234038   2817   \-    F     Update IE PUSCH-TimeDomainResourceAllocationList                                                                                                                      17.10.0
  2023-09          RAN\#101              R5-234056   2819   \-    F     Add DC\_48A\_n46A configuration to 38.508-1                                                                                                                           17.10.0
  2023-09          RAN\#101              R5-234058   2820   \-    F     Update IE PDSCH-Config                                                                                                                                                17.10.0
  2023-09          RAN\#101              R5-234076   2821   \-    F     Addition of test frequencies for new EN-DC combos within FR2                                                                                                          17.10.0
  2023-09          RAN\#101              R5-234145   2826   \-    F     Update LoggedMeasurementConfiguration                                                                                                                                 17.10.0
  2023-09          RAN\#101              R5-234146   2827   \-    F     Update IE CellGroupConfig                                                                                                                                             17.10.0
  2023-09          RAN\#101              R5-234147   2828   \-    F     Update IE ConfiguredGrantConfig                                                                                                                                       17.10.0
  2023-09          RAN\#101              R5-234148   2829   \-    F     Update IE ControlResourceSet                                                                                                                                          17.10.0
  2023-09          RAN\#101              R5-234149   2830   \-    F     Update IE CSI-ReportConfig                                                                                                                                            17.10.0
  2023-09          RAN\#101              R5-234159   2831   \-    F     Test frequencies for band n70 and asymmetric channel bandwidths                                                                                                       17.10.0
  2023-09          RAN\#101              R5-234160   2832   \-    F     Test frequency corrections for n77                                                                                                                                    17.10.0
  2023-09          RAN\#101              R5-234161   2833   \-    F     Low and High test channel BW correction in 38.508-1                                                                                                                   17.10.0
  2023-09          RAN\#101              R5-234162   2834   \-    F     Test frequency corrections for n66                                                                                                                                    17.10.0
  2023-09          RAN\#101              R5-234191   2835   \-    F     Relative Tx Power Allocation to PRS                                                                                                                                   17.10.0
  2023-09          RAN\#101              R5-234295   2837   \-    F     Addition of test frequencies for new NRCA comb within FR1                                                                                                             17.10.0
  2023-09          RAN\#101              R5-234303   2838   \-    F     Update IE LogicalChannelConfig                                                                                                                                        17.10.0
  2023-09          RAN\#101              R5-234305   2840   \-    F     Update IE RadioBearerConfig                                                                                                                                           17.10.0
  2023-09          RAN\#101              R5-234306   2841   \-    F     Update IE RLC-BearerConfig                                                                                                                                            17.10.0
  2023-09          RAN\#101              R5-234307   2842   \-    F     Update IE RLC-Config                                                                                                                                                  17.10.0
  2023-09          RAN\#101              R5-234308   2843   \-    F     Update IE SRB-Identity                                                                                                                                                17.10.0
  2023-09          RAN\#101              R5-234310   2844   \-    F     Add radio configuration for RRCReconfiguration and SRB4                                                                                                               17.10.0
  2023-09          RAN\#101              R5-234447   2849   \-    F     Addition of several NR CA combination to inter-band configurations table                                                                                              17.10.0
  2023-09          RAN\#101              R5-234457   2850   \-    F     Correction of DCI 4-0                                                                                                                                                 17.10.0
  2023-09          RAN\#101              R5-234459   2852   \-    F     Update PDSCH-ConfigBroadcast-r17                                                                                                                                      17.10.0
  2023-09          RAN\#101              R5-234476   2854   \-    F     Correction of DCI 1-0 DCI 1-1 and DCI 1-2                                                                                                                             17.10.0
  2023-09          RAN\#101              R5-234513   2856   \-    F     Update IE PDCP-Config                                                                                                                                                 17.10.0
  2023-09          RAN\#101              R5-234514   2857   \-    F     Update IE PDSCH-ServingCellConfig                                                                                                                                     17.10.0
  2023-09          RAN\#101              R5-234515   2858   \-    F     Update IE PUCCH-Config                                                                                                                                                17.10.0
  2023-09          RAN\#101              R5-234516   2859   \-    F     Update IE PUSCH-Config                                                                                                                                                17.10.0
  2023-09          RAN\#101              R5-234520   2860   \-    F     Update IE PUSCH-ServingCellConfig                                                                                                                                     17.10.0
  2023-09          RAN\#101              R5-234521   2861   \-    F     Update IE RACH-ConfigCommon                                                                                                                                           17.10.0
  2023-09          RAN\#101              R5-234522   2862   \-    F     Update IE RACH-ConfigDedicated                                                                                                                                        17.10.0
  2023-09          RAN\#101              R5-234523   2863   \-    F     Update IE ReportConfigInterRAT                                                                                                                                        17.10.0
  2023-09          RAN\#101              R5-234527   2864   \-    F     Update IE SCS-SpecificCarrier                                                                                                                                         17.10.0
  2023-09          RAN\#101              R5-234528   2865   \-    F     Update IE ServingCellConfig                                                                                                                                           17.10.0
  2023-09          RAN\#101              R5-234529   2866   \-    F     Update IE ServingCellConfigCommon                                                                                                                                     17.10.0
  2023-09          RAN\#101              R5-234530   2867   \-    F     Update IE SRS-Config                                                                                                                                                  17.10.0
  2023-09          RAN\#101              R5-234538   2868   \-    F     Addition of test freqs for CA\_n258E.                                                                                                                                 17.10.0
  2023-09          RAN\#101              R5-234539   2869   \-    F     Addition of test freqs for CA\_n258F.                                                                                                                                 17.10.0
  2023-09          RAN\#101              R5-234540   2870   \-    F     Addition of test freqs for CA\_n258I.                                                                                                                                 17.10.0
  2023-09          RAN\#101              R5-234541   2871   \-    F     Addition of test freqs for CA\_n258J.                                                                                                                                 17.10.0
  2023-09          RAN\#101              R5-234542   2872   \-    F     Addition of test freqs for CA\_n258K.                                                                                                                                 17.10.0
  2023-09          RAN\#101              R5-234543   2873   \-    F     Addition of test freqs for CA\_n258L.                                                                                                                                 17.10.0
  2023-09          RAN\#101              R5-234544   2874   \-    F     Addition of test freqs for CA\_n258M.                                                                                                                                 17.10.0
  2023-09          RAN\#101              R5-234689   2879   \-    F     Addition of test frequencies for new EN-DC configurations within FR1                                                                                                  17.10.0
  2023-09          RAN\#101              R5-234731   2885   \-    F     Introduction of test frequency of CA\_n28A-n41A-n79A                                                                                                                  17.10.0
  2023-09          RAN\#101              R5-234905   2893   \-    F     Correction to frequency range for ssb-PositionsInBurst and SSB-ToMeasure                                                                                              17.10.0
  2023-09          RAN\#101              R5-234906   2894   \-    F     Correction to default value of csi-SSB-ResourceToAddModList for RRM test cases                                                                                        17.10.0
  2023-09          RAN\#101              R5-234935   2895   \-    F     Annex C Test frequencies calculations corrections                                                                                                                     17.10.0
  2023-09          RAN\#101              R5-234936   2896   \-    F     Test frequencies for band n2: Addition of 35 MHz channel bandwidth                                                                                                    17.10.0
  2023-09          RAN\#101              R5-234941   2899   \-    F     Test frequencies for band n5 and asymmetric channel bandwidths                                                                                                        17.10.0
  2023-09          RAN\#101              R5-234942   2900   \-    F     Test frequencies for band n8 and asymmetric channel bandwidths                                                                                                        17.10.0
  2023-09          RAN\#101              R5-234944   2902   \-    F     Test frequencies for band n25 and asymmetric channel bandwidths                                                                                                       17.10.0
  2023-09          RAN\#101              R5-234947   2905   \-    F     Test frequencies for band n71 and asymmetric channel bandwidths in Rel-15                                                                                             17.10.0
  2023-09          RAN\#101              R5-234948   2906   \-    F     Test frequencies for band n71 and asymmetric channel bandwidths in Rel-17                                                                                             17.10.0
  2023-09          RAN\#101              R5-234949   2907   \-    F     Test frequencies for band n91 and asymmetric channel bandwidths                                                                                                       17.10.0
  2023-09          RAN\#101              R5-234950   2908   \-    F     Test frequencies for band n92 and asymmetric channel bandwidths                                                                                                       17.10.0
  2023-09          RAN\#101              R5-234951   2909   \-    F     Test frequencies for band n93 and asymmetric channel bandwidths                                                                                                       17.10.0
  2023-09          RAN\#101              R5-234952   2910   \-    F     Test frequencies for band n94 and asymmetric channel bandwidths                                                                                                       17.10.0
  2023-09          RAN\#101              R5-235084   2911   \-    F     Updates on Dedicated coreset configuration for RF and RRM testing                                                                                                     17.10.0
  2023-09          RAN\#101              R5-235249   2922   \-    F     Update MIB for NCD-SSB                                                                                                                                                17.10.0
  2023-09          RAN\#101              R5-235277   2825   1     F     Correct Editorial mistake in default message contents of DLInformationTransfer                                                                                        17.10.0
  2023-09          RAN\#101              R5-235279   2855   1     F     Update SchedulingRequestResourceConfig                                                                                                                                17.10.0
  2023-09          RAN\#101              R5-235280   2886   1     F     Updates to default 5GMM messages                                                                                                                                      17.10.0
  2023-09          RAN\#101              R5-235306   2884   1     F     Correction to test procedure 4.9.31\_SL DRB connectivity check                                                                                                        17.10.0
  2023-09          RAN\#101              R5-235313   2851   1     F     Correction of DCI 4-2                                                                                                                                                 17.10.0
  2023-09          RAN\#101              R5-235336   2810   1     F     Addition of NTN freq band n255 to clause 6.2.3 for Default test frequencies                                                                                           17.10.0
  2023-09          RAN\#101              R5-235349   2822   1     F     Update default message contents of RRCReconfiguration for MDT enhance                                                                                                 17.10.0
  2023-09          RAN\#101              R5-235350   2823   1     F     Update default message contents of UEInformationRequest for MDT enhance                                                                                               17.10.0
  2023-09          RAN\#101              R5-235369   2875   1     F     Addition of default ProSe PC5 signalling messages                                                                                                                     17.10.0
  2023-09          RAN\#101              R5-235370   2876   1     F     Addition of spec reference of 24.554 for ProSe PC5 signalling messages                                                                                                17.10.0
  2023-09          RAN\#101              R5-235371   2881   1     F     Addition of test procedure for establishing unicast mode ProSe Direct communication / Peer UE side                                                                    17.10.0
  2023-09          RAN\#101              R5-235372   2882   1     F     Addition of test procedure for registration of NR sidelink U2N Relay / Relay UE side                                                                                  17.10.0
  2023-09          RAN\#101              R5-235373   2883   1     F     Addition of Generic procedures for NR sidelink U2N Relay                                                                                                              17.10.0
  2023-09          RAN\#101              R5-235375   2912   1     F     Updating PDCCH-ConfigCommon content                                                                                                                                   17.10.0
  2023-09          RAN\#101              R5-235376   2839   1     F     Update IE LogicalChannelIdentity                                                                                                                                      17.10.0
  2023-09          RAN\#101              R5-235377   2845   1     F     Add radio configuration for RadioBearerConfig and SRB4                                                                                                                17.10.0
  2023-09          RAN\#101              R5-235378   2846   1     F     Add radio configuration for CellGroupConfig and SRB4                                                                                                                  17.10.0
  2023-09          RAN\#101              R5-235391   2880   1     F     Addition of test procedure for establishing unicast mode ProSe Direct communication / Initiating UE side                                                              17.10.0
  2023-09          RAN\#101              R5-235414   2887   1     F     Addition of signaling test frequency for CA\_n77(2A)                                                                                                                  17.10.0
  2023-09          RAN\#101              R5-235415   2853   1     F     Add si-SchedulingInfo-v1700 for the TC scheduling SIB15 to SIB21                                                                                                      17.10.0
  2023-09          RAN\#101              R5-235600   2901   1     F     Test frequencies for band n24 and asymmetric channel bandwidths                                                                                                       17.10.0
  2023-09          RAN\#101              R5-235601   2897   1     F     Test frequencies for band n18                                                                                                                                         17.10.0
  2023-09          RAN\#101              R5-235602   2836   1     F     Update inter-band NR CA 3DL configurations with additional band combos                                                                                                17.10.0
  2023-09          RAN\#101              R5-235603   2921   1     F     Addition of CA\_n2(2A)-n66A frequency                                                                                                                                 17.10.0
  2023-09          RAN\#101              R5-235604   2916   1     F     Rel-16 Corrections to Table 4.3.1.0A-1 (mid test channel bandwidths) for unlicensed bands                                                                             17.10.0
  2023-09          RAN\#101              R5-235605   2918   1     F     Rel-17 Corrections to Table 4.3.1.0A-1 (mid test channel bandwidths)                                                                                                  17.10.0
  2023-09          RAN\#101              R5-235606   2913   1     F     Addition of connection diagram for FR2 spurious emissions                                                                                                             17.10.0
  2023-09          RAN\#101              R5-235780   2889   1     F     Addition of default message for unified TCI state                                                                                                                     17.10.0
  2023-09          RAN\#101              R5-235781   2891   1     F     Correction to SIB4 redCapAccessAllowed-r17 for RedCap testing                                                                                                         17.10.0
  2023-09          RAN\#101              R5-235782   2892   1     F     Correction to c-SRS default value for FR2 multiple BWP case                                                                                                           17.10.0
  2023-09          RAN\#101              R5-235822   2917   1     F     Rel-16 Corrections to Table 4.3.1.0A-1 (mid test channel bandwidths) for sidelink                                                                                     17.10.0
  2023-09          RAN\#101              R5-235823   2919   1     F     Correction to Table 4.3.1.0A-1 (mid test channel bandwidths) for RedCap Ues                                                                                           17.10.0
  2023-09          RAN\#101              R5-235841   2890   1     F     Correction to notes for RedCap CBW                                                                                                                                    17.10.0
  2023-09          RAN\#101              R5-235843   2914   1     F     Rel-15 Corrections to Table 4.3.1.0A-1 (mid test channel bandwidths)                                                                                                  17.10.0
  2023-09          RAN\#101              R5-235844   2915   1     F     Rel-16 Corrections to Table 4.3.1.0A-1 (mid test channel bandwidths)                                                                                                  17.10.0
  2023-09          RAN\#101              R5-235460   2920   2     F     Common test environments for NR-NTN testing                                                                                                                           17.10.0
  2023-09          RAN\#101              \-          \-     \-    \-    Administrative release upgrade to match the release of TS 38.508-2 which was upgraded at RAN\#101 to Rel-18 due to Rel-18 relevant CR(s)                              18.0.0
  2023-12          RAN\#102              R5-236072   2927   \-    F     Introduction of test frequencies for CA\_n1A-n3A-n28A-n78A                                                                                                            18.1.0
  2023-12          RAN\#102              R5-236171   2931   \-    F     Correction to default REGISTRATION ACCEPT message                                                                                                                     18.1.0
  2023-12          RAN\#102              R5-236197   2932   \-    F     Addition of default config for SMTC.7 and SMTC.8                                                                                                                      18.1.0
  2023-12          RAN\#102              R5-236302   2935   \-    F     Correction to SIB4 for RedCap                                                                                                                                         18.1.0
  2023-12          RAN\#102              R5-236305   2937   \-    F     Corrections to generic procedure NR RRC\_IDLE                                                                                                                         18.1.0
  2023-12          RAN\#102              R5-236333   2938   \-    F     n70 frequencies - Typo correction in offset to carrier                                                                                                                18.1.0
  2023-12          RAN\#102              R5-236346   2940   \-    F     Test frequency corrections for n66                                                                                                                                    18.1.0
  2023-12          RAN\#102              R5-236374   2944   \-    F     Update additional NR CA two bands configurations                                                                                                                      18.1.0
  2023-12          RAN\#102              R5-236401   2945   \-    F     Addition of test frequencies for new EN-DC configurations within FR1                                                                                                  18.1.0
  2023-12          RAN\#102              R5-236410   2946   \-    F     Add new table for BWP without Coreset0 in 6.2.3.1                                                                                                                     18.1.0
  2023-12          RAN\#102              R5-236411   2947   \-    F     Update Downlink physical channels and physical signals for NCD-SSB                                                                                                    18.1.0
  2023-12          RAN\#102              R5-236412   2948   \-    F     Update NonCellDefiningSSB                                                                                                                                             18.1.0
  2023-12          RAN\#102              R5-236413   2949   \-    F     Update MIB and PDCCH-ConfigSIB1 for NCD-SSB                                                                                                                           18.1.0
  2023-12          RAN\#102              R5-236480   2950   \-    F     Moving Default 5G ProSe message and IEs                                                                                                                               18.1.0
  2023-12          RAN\#102              R5-236483   2951   \-    F     Simplification of tables for test freqs for CA\_n48(2A)                                                                                                               18.1.0
  2023-12          RAN\#102              R5-236487   2955   \-    F     Introduction of Test freqs for CA\_n2(2A), BCS0                                                                                                                       18.1.0
  2023-12          RAN\#102              R5-236492   2960   \-    F     Editorial change of format for Header of clause 4.3.1.2.3.2                                                                                                           18.1.0
  2023-12          RAN\#102              R5-236774   2968   \-    F     Addition of default settings of UICC and USIM for 5G ProSe                                                                                                            18.1.0
  2023-12          RAN\#102              R5-236775   2969   \-    F     Addition of spec reference of 24.555 and 23.304 for ProSe information elements                                                                                        18.1.0
  2023-12          RAN\#102              R5-236776   2970   \-    F     Update of AT Command message for NR sidelink U2N Remote UE                                                                                                            18.1.0
  2023-12          RAN\#102              R5-236786   2971   \-    F     Update of SecurityModeComplete and RRCReconfigurationComplete message for NR sidelink U2N Relay UE                                                                    18.1.0
  2023-12          RAN\#102              R5-236801   2973   \-    F     Correction to PDCCH-ConfigCommon for performance tests for TDD patterns other than SCS 30 kHz                                                                         18.1.0
  2023-12          RAN\#102              R5-236802   2974   \-    F     Correction to CSI-FrequencyOccupation for CSI-IM-Resource                                                                                                             18.1.0
  2023-12          RAN\#102              R5-236832   2975   \-    F     Addition of SL-AccessInfo-L2U2N message for sidelink relay                                                                                                            18.1.0
  2023-12          RAN\#102              R5-236834   2976   \-    F     Addition of SL-DefaultDRX-GC-BC message for sidelink relay                                                                                                            18.1.0
  2023-12          RAN\#102              R5-236844   2977   \-    F     Update of RRC message RRCSetupRequest and RRCSetupComplete                                                                                                            18.1.0
  2023-12          RAN\#102              R5-236845   2978   \-    F     Update of Contents of UE Policy Delivery messages                                                                                                                     18.1.0
  2023-12          RAN\#102              R5-236876   2980   \-    F     Addition of aperiodic TRS configuration for fast SCell activation                                                                                                     18.1.0
  2023-12          RAN\#102              R5-236900   2983   \-    F     Addition of connection diagram for NR CA with UL MIMO                                                                                                                 18.1.0
  2023-12          RAN\#102              R5-236933   2984   \-    F     Removal of RedCap mid test channel bandwidth for n47 to 4.3.1.0A                                                                                                      18.1.0
  2023-12          RAN\#102              R5-236940   2985   \-    F     Removal of mid test channel bandwidth for n18 to 4.3.1.0A                                                                                                             18.1.0
  2023-12          RAN\#102              R5-236948   2986   \-    F     Update inter-band NR CA configuration of three bands CA\_n1A-n3A-n78A                                                                                                 18.1.0
  2023-12          RAN\#102              R5-237035   2989   \-    F     Updating SearchSpace content                                                                                                                                          18.1.0
  2023-12          RAN\#102              R5-237073   2990   \-    F     Updating test frequency for band n30                                                                                                                                  18.1.0
  2023-12          RAN\#102              R5-237299   2998   \-    F     Update the Contents of Pre-configuration for sidelink relay                                                                                                           18.1.0
  2023-12          RAN\#102              R5-237315   2999   \-    F     Corrections to test procedures 4.9.7 and 4.9.9                                                                                                                        18.1.0
  2023-12          RAN\#102              R5-237319   2936   1     F     Corrections to generic procedure E-UTRA RRC\_IDLE                                                                                                                     18.1.0
  2023-12          RAN\#102              R5-237320   2995   1     F     Change in generic procedure 4.9.9 depending on network support of N26                                                                                                 18.1.0
  2023-12          RAN\#102              R5-237323   2929   1     F     Update IE RACH-ConfigDedicated                                                                                                                                        18.1.0
  2023-12          RAN\#102              R5-237324   2930   1     F     Update IE MsgA-PUSCH-Config                                                                                                                                           18.1.0
  2023-12          RAN\#102              R5-237325   2987   1     F     Update MsgA-PUSCH-Config                                                                                                                                              18.1.0
  2023-12          RAN\#102              R5-237326   2964   1     F     Corrections for Test Procedure for eCall over IMS establishment in 5GS: eCall Only Support                                                                            18.1.0
  2023-12          RAN\#102              R5-237393   2965   1     F     Correction to default configuration of RRC IEs for CE test cases                                                                                                      18.1.0
  2023-12          RAN\#102              R5-237421   2963   1     F     Correction to USIM configuration for 5G eCall over IMS test case                                                                                                      18.1.0
  2023-12          RAN\#102              R5-237422   2942   1     F     Updates to default PCI of NR cells for signalling test cases                                                                                                          18.1.0
  2023-12          RAN\#102              R5-237475   2967   1     F     Addition of 5G ProSe information elements for UE policy part                                                                                                          18.1.0
  2023-12          RAN\#102              R5-237600   2923   1     F     Addition of test frequencies for new R16 NR CA comb within FR1                                                                                                        18.1.0
  2023-12          RAN\#102              R5-237601   2926   1     F     Addition of test frequencies for new R17 NR CA comb within FR1                                                                                                        18.1.0
  2023-12          RAN\#102              R5-237602   2928   1     F     Introduction of test frequencies for CA\_n25A-n66A-n77(2A) and CA\_n25A-n66A-n78(2A)                                                                                  18.1.0
  2023-12          RAN\#102              R5-237603   2956   1     F     Introduction of test freqs for CA\_n66(3A)                                                                                                                            18.1.0
  2023-12          RAN\#102              R5-237604   2992   1     F     Addition of Note 5 in Table 4.4.2-1 for RRM CA Intra band scenarios                                                                                                   18.1.0
  2023-12          RAN\#102              R5-237646   2941   1     F     Addition of several EN-DC combinations to inter-band configurations table                                                                                             18.1.0
  2023-12          RAN\#102              R5-237816   2933   1     F     Addition of useAutonomousGaps-r16 in Table 4.6.3-142                                                                                                                  18.1.0
  2023-12          RAN\#102              R5-237817   2943   1     F     Update additional ENDC inter-band configurations                                                                                                                      18.1.0
  2023-12          RAN\#102              R5-237818   2982   1     F     Addition of SCG activation and deactivation configuration for NR-DC                                                                                                   18.1.0
  2023-12          RAN\#102              R5-237858   2981   1     F     Addition of conditional PSCell addition configuration for NR-DC                                                                                                       18.1.0
  2023-12          RAN\#102              R5-237863   2993   1     F     Common test environment update for NR NTN RF/RRM testing                                                                                                              18.1.0
  2023-12          RAN\#102              R5-237885   2988   1     F     SMTC configuration for RRM RedCap testing                                                                                                                             18.1.0
  2023-12          RAN\#102              R5-237908   2959   1     F     Introduction of Test freqs for CA\_n77(2A), BCS1                                                                                                                      18.1.0
  2023-12          RAN\#102              R5-237909   2961   1     F     Correction of test frequencies for CA\_n48B                                                                                                                           18.1.0
  2023-12          RAN\#102              R5-237939   2939   1     F     Defined frequencies for n7 and certain Release 16 CBWs                                                                                                                18.1.0
  2024-03          RAN\#103              R5-240153   3003   \-    F     Correction to RRCReestablishment message                                                                                                                              18.2.0
  2024-03          RAN\#103              R5-240154   3004   \-    F     Correction to PEIPS in REGISTRATION ACCEPT message                                                                                                                    18.2.0
  2024-03          RAN\#103              R5-240163   3005   \-    F     Correction to Test procedure 4.9.27                                                                                                                                   18.2.0
  2024-03          RAN\#103              R5-240164   3006   \-    F     Correction to Test procedure 4.9.38                                                                                                                                   18.2.0
  2024-03          RAN\#103              R5-240165   3007   \-    F     Correction to DLInformationTransfer message                                                                                                                           18.2.0
  2024-03          RAN\#103              R5-240166   3008   \-    F     Correction to UEInformationRequest message                                                                                                                            18.2.0
  2024-03          RAN\#103              R5-240167   3009   \-    F     Editorial update of CounterCheck message                                                                                                                              18.2.0
  2024-03          RAN\#103              R5-240168   3010   \-    F     Correction to IE RadioLinkMonitoringConfig                                                                                                                            18.2.0
  2024-03          RAN\#103              R5-240172   3014   \-    F     Correction to RRCReconfiguration configuration                                                                                                                        18.2.0
  2024-03          RAN\#103              R5-240233   3016   \-    F     Update inter-band NR CA configuration of three bands CA\_n1A-n8A-n78A                                                                                                 18.2.0
  2024-03          RAN\#103              R5-240236   3017   \-    F     Correction to NR RRC\_Idle generic procedure                                                                                                                          18.2.0
  2024-03          RAN\#103              R5-240271   3020   \-    F     Correction of errors in Annex C                                                                                                                                       18.2.0
  2024-03          RAN\#103              R5-240272   3021   \-    F     Style correction for clause title of 4.3.1.1.1.100 and 4.3.1.1.1.101                                                                                                  18.2.0
  2024-03          RAN\#103              R5-240274   3022   \-    F     Addition of test frequencies for new R16 NR CA combos within FR1                                                                                                      18.2.0
  2024-03          RAN\#103              R5-240275   3023   \-    F     Addition of test frequencies for new R17 NR CA combos within FR1                                                                                                      18.2.0
  2024-03          RAN\#103              R5-240349   3027   \-    F     Correction of Default parameters for simulated SNPN cells.                                                                                                            18.2.0
  2024-03          RAN\#103              R5-240378   3028   \-    F     Update of conditional PSCell addition configuration for NR-DC                                                                                                         18.2.0
  2024-03          RAN\#103              R5-240444   3031   \-    F     Add IndirectPathFailureInformation                                                                                                                                    18.2.0
  2024-03          RAN\#103              R5-240445   3032   \-    F     Add MBSMulticastConfiguration                                                                                                                                         18.2.0
  2024-03          RAN\#103              R5-240446   3033   \-    F     Add MeasurementReportAppLayer                                                                                                                                         18.2.0
  2024-03          RAN\#103              R5-240448   3035   \-    F     Add UEPositioningAssistanceInfo                                                                                                                                       18.2.0
  2024-03          RAN\#103              R5-240460   3036   \-    F     Introduction of test frequencies for CA\_n66A-n71A-n77(2A) and CA\_n66A-n71A-n78(2A)                                                                                  18.2.0
  2024-03          RAN\#103              R5-240468   3037   \-    F     Test frequencies and channel bandwidth updates for band n71 and n25 in Rel-17                                                                                         18.2.0
  2024-03          RAN\#103              R5-240480   3040   \-    F     Removal of test procedure for Out\_of\_Coverage\_with\_Relay                                                                                                          18.2.0
  2024-03          RAN\#103              R5-240482   3042   \-    F     Update of 5G ProSe information elements of UE policies for 5G ProSe usage information reporting                                                                       18.2.0
  2024-03          RAN\#103              R5-240483   3043   \-    F     Update of 5G ProSe information elements of UE policies for 5G ProSe remote                                                                                            18.2.0
  2024-03          RAN\#103              R5-240484   3044   \-    F     Addition of PROSE PC5 DISCOVERY                                                                                                                                       18.2.0
  2024-03          RAN\#103              R5-240489   3045   \-    F     Add IEs SIB22, SIB23, SIB24 and SIB25                                                                                                                                 18.2.0
  2024-03          RAN\#103              R5-240491   3047   \-    F     Editorial update IE PosSI-SchedulingInfo                                                                                                                              18.2.0
  2024-03          RAN\#103              R5-240492   3048   \-    F     Add IE AdvancedReceiver-MU-MIMO                                                                                                                                       18.2.0
  2024-03          RAN\#103              R5-240493   3049   \-    F     Add IE Altitude                                                                                                                                                       18.2.0
  2024-03          RAN\#103              R5-240494   3050   \-    F     Add IE ATG-Config                                                                                                                                                     18.2.0
  2024-03          RAN\#103              R5-240495   3051   \-    F     Add IEs CandidateTCI-State and CandidateTCI-UL-State                                                                                                                  18.2.0
  2024-03          RAN\#103              R5-240496   3052   \-    F     Add IE CellDTXDRX-Config                                                                                                                                              18.2.0
  2024-03          RAN\#103              R5-240497   3053   \-    F     Add IE ClockQualityMetrics                                                                                                                                            18.2.0
  2024-03          RAN\#103              R5-240499   3055   \-    F     Add IE EarlyUL-SyncConfig                                                                                                                                             18.2.0
  2024-03          RAN\#103              R5-240500   3056   \-    F     Add IE EUTRA-C-RNTI                                                                                                                                                   18.2.0
  2024-03          RAN\#103              R5-240536   3057   \-    F     Editorial updates to test procedure 4.9.1                                                                                                                             18.2.0
  2024-03          RAN\#103              R5-240537   3058   \-    F     Harmonization of SCell\_add condition                                                                                                                                 18.2.0
  2024-03          RAN\#103              R5-240617   3060   \-    F     Added 30kHz SCS for SSB in n53 to 30kHz SCS test frequencies                                                                                                          18.2.0
  2024-03          RAN\#103              R5-240775   3068   \-    F     Introduction of test frequencies for CA\_n1A-n28A-n78A and CA\_n3A-n28A-n78A                                                                                          18.2.0
  2024-03          RAN\#103              R5-240856   3074   \-    F     Corrections on C.1 for the parameters for calculation of test frequencies                                                                                             18.2.0
  2024-03          RAN\#103              R5-240878   3076   \-    F     Update NR inter-band CA configurations FR1 four bands table                                                                                                           18.2.0
  2024-03          RAN\#103              R5-240971   3079   \-    F     Annex C update to asymmetric channel bandwidths test frequencies calculation                                                                                          18.2.0
  2024-03          RAN\#103              R5-240989   3081   \-    F     SIB2 updates for NR unlicensed test cases                                                                                                                             18.2.0
  2024-03          RAN\#103              R5-241092   3084   \-    F     Correction to CBW selection to avoid unintentional asymmetric CBW                                                                                                     18.2.0
  2024-03          RAN\#103              R5-241371   3096   \-    F     Add IE MeasSequence                                                                                                                                                   18.2.0
  2024-03          RAN\#103              R5-241372   3097   \-    F     Add IE MeasWindowConfig                                                                                                                                               18.2.0
  2024-03          RAN\#103              R5-241373   3098   \-    F     Add IEs N3C-IndirectPathConfigRelay and N3C-IndirectPathAddChange                                                                                                     18.2.0
  2024-03          RAN\#103              R5-241374   3099   \-    F     Add IEs NCR-AperiodicFwdConfig, NCR-FwdConfig, NCR-PeriodicityAndOffset and NCR-PeriodicFwdResourceSet                                                                18.2.0
  2024-03          RAN\#103              R5-241375   3100   \-    F     Add IEs NCR-PeriodicFwdResourceSetId, NCR-SemiPersistentFwdResourceSet and NCR-SemiPersistentFwdResourceSetId                                                         18.2.0
  2024-03          RAN\#103              R5-241480   3011   1     F     Correction to IE NRDC-Parameters                                                                                                                                      18.2.0
  2024-03          RAN\#103              R5-241481   3012   1     F     Correction to IE UE-MRDC-Capability                                                                                                                                   18.2.0
  2024-03          RAN\#103              R5-241482   3013   1     F     Correction to IE UE-NR-Capability                                                                                                                                     18.2.0
  2024-03          RAN\#103              R5-241483   3034   1     F     Editorial update SystemInformation                                                                                                                                    18.2.0
  2024-03          RAN\#103              R5-241484   3046   1     F     Editorial update IE PosSystemInformation-r16-IEs                                                                                                                      18.2.0
  2024-03          RAN\#103              R5-241485   3054   1     F     Add IEs CSI-ReportSubConfig, CSI-ReportSubConfigId and CSI-ReportSubConfigTriggerList                                                                                 18.2.0
  2024-03          RAN\#103              R5-241486   3070   1     F     Add IE HysteresisAltitude                                                                                                                                             18.2.0
  2024-03          RAN\#103              R5-241487   3071   1     F     Add IEs LTM-CandidateId, LTM-Candidate, LTM-Config and LTM-CSI-ReportConfig                                                                                           18.2.0
  2024-03          RAN\#103              R5-241488   3072   1     F     Add IEs LTM-CSI-ReportConfigId, LTM-CSI-ResourceConfig and LTM-CSI-ResourceConfigId                                                                                   18.2.0
  2024-03          RAN\#103              R5-241538   3030   1     F     Move all V2X sub-clauses from 4.7 into a new clause 4.7D                                                                                                              18.2.0
  2024-03          RAN\#103              R5-241539   3067   1     F     Correction to default configuration of frequencyInfoSL                                                                                                                18.2.0
  2024-03          RAN\#103              R5-241561   3062   1     F     Updates to Ephemeris Info for Multi-Cell NRN-NTN signalling test cases                                                                                                18.2.0
  2024-03          RAN\#103              R5-241565   3063   1     F     Updates to SIB19 Common Config for NR-NTN test cases                                                                                                                  18.2.0
  2024-03          RAN\#103              R5-241580   3105   1     F     Addition of signalling test frequencies for DC\_2A\_n2A and DC\_66A\_n66A                                                                                             18.2.0
  2024-03          RAN\#103              R5-241597   3038   1     F     Addition of test procedure for 5G ProSe U2N Relay Discovery                                                                                                           18.2.0
  2024-03          RAN\#103              R5-241598   3039   1     F     Addition of test procedure for remote Initial Access procedure under NR sidelink U2N Relay / Remote UE side                                                           18.2.0
  2024-03          RAN\#103              R5-241599   3041   1     F     Update test procedure for registration of NR sidelink U2N Relay / Relay UE side                                                                                       18.2.0
  2024-03          RAN\#103              R5-241628   3018   1     F     Correction to NR RRC\_Inactive generic procedure                                                                                                                      18.2.0
  2024-03          RAN\#103              R5-241629   3104   1     F     Updates to OTA Signalling test environment                                                                                                                            18.2.0
  2024-03          RAN\#103              R5-241630   3095   1     F     Test environment definition for GERAN in Conducted and OTA Environment                                                                                                18.2.0
  2024-03          RAN\#103              R5-241703   3080   1     F     Asymmetric channel bandwidths test frequencies updates for frequency bands n5 and n8                                                                                  18.2.0
  2024-03          RAN\#103              R5-241704   3059   1     F     RF TRx testing - P-Max configuration extension to RX tests to enable TxD                                                                                              18.2.0
  2024-03          RAN\#103              R5-241705   3077   1     F     Addition of test frequencies for DC\_2A\_n2A and DC\_66A\_n66A                                                                                                        18.2.0
  2024-03          RAN\#103              R5-241706   3083   1     F     Correction to test frequencies for CA\_n48 - 2A                                                                                                                       18.2.0
  2024-03          RAN\#103              R5-241708   3078   1     F     Update additional inter-band NR CA configurations                                                                                                                     18.2.0
  2024-03          RAN\#103              R5-241717   3085   1     F     Correction to point A value for n83                                                                                                                                   18.2.0
  2024-03          RAN\#103              R5-241718   3086   1     F     Correction to parameters for Rel-17 bands                                                                                                                             18.2.0
  2024-03          RAN\#103              R5-241719   3082   1     F     Correction to SUL configuration messages                                                                                                                              18.2.0
  2024-03          RAN\#103              R5-241722   3025   1     F     Update of RRC message RRCReconfigurationComplete, RRCSetupComplete and SecurityModeComplete for SL relay                                                              18.2.0
  2024-03          RAN\#103              R5-241723   3026   1     F     Update of Test procedure for establishing unicast mode ProSe Direct communication                                                                                     18.2.0
  2024-03          RAN\#103              R5-241869   3024   2     F     Updating test frequency for SUL band n83 20MHz CBW                                                                                                                    18.2.0
  2024-03          RAN\#103              R5-241875   3091   1     F     Addition of missing section for RRM CA Configuration                                                                                                                  18.2.0
  2024-03          RAN\#103              R5-241919   3001   1     F     Introduction of RF Test Environment for ATG                                                                                                                           18.2.0
  2024-03          RAN\#103              R5-241920   3002   1     F     Introduction of RRM Test Environment for ATG                                                                                                                          18.2.0
  2024-03          RAN\#103              R5-241921   3019   1     F     Correction of Notes in tables of test channel bandwidths                                                                                                              18.2.0
  2024-03          RAN\#103              R5-241926   3106   \-    F     Update of abbreviations for ATG                                                                                                                                       18.2.0
  2024-03          RAN\#103              R5-241927   3029   1     F     Addition of test frequencies for new EN-DC comb within FR2                                                                                                            18.2.0
  2024-03          RAN\#103              R5-241928   3075   1     F     Update for additional NR-CA and NR-DC band configurations                                                                                                             18.2.0
  2024-03          RAN\#103              R5-241944   3094   1     F     Addition of test frequencies for CA n77(2A), BCS1, UL CA..                                                                                                            18.2.0
  2024-03          RAN\#103              R5-241968   3092   1     F     Update of PDSCH Config for RF test cases                                                                                                                              18.2.0
  2024-03          RAN\#103              R5-242007   3093   1     F     Correction of test environment for NR NTN RF testing                                                                                                                  18.2.0
  2024-03          RAN\#103              R5-242016   3101   1     F     Updates to Test environment for NR NTN RRM testing                                                                                                                    18.2.0
  2024-03          RAN\#103              R5-242017   3102   1     F     Common Test environment updates for NR NTN RF, demod and RRM testing                                                                                                  18.2.0
  2024-03          RAN\#103              R5-242022   3087   1     F     Correction to message exceptions for Performance test cases                                                                                                           18.2.0
  2024-03          RAN\#103              R5-242038   3065   1     F     Correction to default configuration of SMTC for NCD-SSB                                                                                                               18.2.0
  2024-06          RAN\#104              R5-242139   3108   \-    F     Correction to RRC message MobilityFromNRCommand                                                                                                                       18.3.0
  2024-06          RAN\#104              R5-242140   3109   \-    F     Correction to IE PDCP-Config for UDC                                                                                                                                  18.3.0
  2024-06          RAN\#104              R5-242141   3110   \-    F     Correction to IE MeasIdleConfig for Idle/Inactive measurements                                                                                                        18.3.0
  2024-06          RAN\#104              R5-242142   3111   \-    F     Correction to IE CondReconfigToAddModList                                                                                                                             18.3.0
  2024-06          RAN\#104              R5-242240   3112   \-    F     Addition of test frequencies for CA\_n28A-n40A                                                                                                                        18.3.0
  2024-06          RAN\#104              R5-242241   3113   \-    F     Addition of test frequencies for CA\_n3A-n28A-n41A-n77A                                                                                                               18.3.0
  2024-06          RAN\#104              R5-242321   3115   \-    F     Editorial updates to specification references in clauses 4.5, 4.5A & 4.9                                                                                              18.3.0
  2024-06          RAN\#104              R5-242322   3116   \-    F     Editorial updates to specification references in clause 4.6                                                                                                           18.3.0
  2024-06          RAN\#104              R5-242323   3117   \-    F     Editorial updates to REGISTRATION REQUEST message                                                                                                                     18.3.0
  2024-06          RAN\#104              R5-242368   3120   \-    F     Introduction of test channel bandwidths and test frequencies for band n106                                                                                            18.3.0
  2024-06          RAN\#104              R5-242401   3123   \-    F     Add IE AppLayerIdleInactiveConfig                                                                                                                                     18.3.0
  2024-06          RAN\#104              R5-242402   3124   \-    F     Add IE EUTRA-MultiBandInfoListAerial                                                                                                                                  18.3.0
  2024-06          RAN\#104              R5-242405   3125   \-    F     Add IE MBS-NonServingInfoList                                                                                                                                         18.3.0
  2024-06          RAN\#104              R5-242406   3126   \-    F     Add IE MBS-SessionInfoListMulticast                                                                                                                                   18.3.0
  2024-06          RAN\#104              R5-242407   3127   \-    F     Add IE AerialParameters                                                                                                                                               18.3.0
  2024-06          RAN\#104              R5-242408   3128   \-    F     Add IE DL-PRS-MeasurementWithRxFH-RRC-Connected                                                                                                                       18.3.0
  2024-06          RAN\#104              R5-242409   3129   \-    F     Add IE ERedCapParameters                                                                                                                                              18.3.0
  2024-06          RAN\#104              R5-242410   3130   \-    F     Add IE NCR-Parameters                                                                                                                                                 18.3.0
  2024-06          RAN\#104              R5-242413   3133   \-    F     Update IE SharedSpectrumChAccessParamsPerBand                                                                                                                         18.3.0
  2024-06          RAN\#104              R5-242414   3134   \-    F     Add IE SharedSpectrumChAccessParamsSidelinkPerBand                                                                                                                    18.3.0
  2024-06          RAN\#104              R5-242415   3135   \-    F     Add IE SupportedAggBandwidth                                                                                                                                          18.3.0
  2024-06          RAN\#104              R5-242450   3136   \-    F     Update for additional ENDC band configurations                                                                                                                        18.3.0
  2024-06          RAN\#104              R5-242460   3137   \-    F     Update for additional NRCA band configurations                                                                                                                        18.3.0
  2024-06          RAN\#104              R5-242515   3138   \-    F     Test frequency parameters corrections for CA n48B                                                                                                                     18.3.0
  2024-06          RAN\#104              R5-242534   3140   \-    F     Correction of clause structure of CA test frequencies                                                                                                                 18.3.0
  2024-06          RAN\#104              R5-242574   3146   \-    F     Update for derivation path of test procedure 4.9.39 and 4.9.40                                                                                                        18.3.0
  2024-06          RAN\#104              R5-242590   3149   \-    F     Addition of test frequencies for new EN-DC comb within FR2                                                                                                            18.3.0
  2024-06          RAN\#104              R5-242598   3150   \-    F     Editorial correction for Editor Note and reference section number in 4.3.1                                                                                            18.3.0
  2024-06          RAN\#104              R5-242601   3151   \-    F     Addition of CBW 70MHz 90MHz and 100MHz for n40                                                                                                                        18.3.0
  2024-06          RAN\#104              R5-242603   3152   \-    F     Add IE PosSRS-BWA-RRC-Inactive                                                                                                                                        18.3.0
  2024-06          RAN\#104              R5-242604   3153   \-    F     Add IEs PosSRS-TxFrequencyHoppingRRC-Connected and PosSRS-TxFrequencyHoppingRRC-Inactive                                                                              18.3.0
  2024-06          RAN\#104              R5-242650   3156   \-    F     Add IE LTM-TCI-Info                                                                                                                                                   18.3.0
  2024-06          RAN\#104              R5-242651   3157   \-    F     Add IE N3C-RelayUE-Info                                                                                                                                               18.3.0
  2024-06          RAN\#104              R5-242652   3158   \-    F     Add IE NeedForInterruptionInfoNR                                                                                                                                      18.3.0
  2024-06          RAN\#104              R5-242653   3159   \-    F     Add IE PDU-SessionID                                                                                                                                                  18.3.0
  2024-06          RAN\#104              R5-242654   3160   \-    F     Add IE PUCCH-CSI-Resource                                                                                                                                             18.3.0
  2024-06          RAN\#104              R5-242655   3161   \-    F     Add IE QFI                                                                                                                                                            18.3.0
  2024-06          RAN\#104              R5-242656   3162   \-    F     Add IE RACH-ConfigTwoTA                                                                                                                                               18.3.0
  2024-06          RAN\#104              R5-242657   3163   \-    F     Add IE ReferenceConfiguration                                                                                                                                         18.3.0
  2024-06          RAN\#104              R5-242658   3164   \-    F     Add IE SelectedPSCellForCHO-WithSCG                                                                                                                                   18.3.0
  2024-06          RAN\#104              R5-242659   3165   \-    F     Add IE SI-RequestConfigRepetition                                                                                                                                     18.3.0
  2024-06          RAN\#104              R5-242660   3166   \-    F     Add IEs SRS-PosTx-Hopping and SRS-PosResourceSetLinkedForAggBW                                                                                                        18.3.0
  2024-06          RAN\#104              R5-242661   3167   \-    F     Add IE TN-AreaId                                                                                                                                                      18.3.0
  2024-06          RAN\#104              R5-242708   3168   \-    F     Definition of CA\_n2A-n30A, CA\_n5A-n30A, CA\_n30A-n66A and CA\_n30A-n77A applicability to protocol testing                                                           18.3.0
  2024-06          RAN\#104              R5-242714   3169   \-    F     Definition of DC\_2A-2A\_n66A, DC\_66A-66A-66A\_n77A, DC\_66A-66A-66A\_n77(2A) and DC\_66A-66A\_n2A applicability to protocol testing                                 18.3.0
  2024-06          RAN\#104              R5-242763   3172   \-    F     Add IEs SL-BWP-DiscPoolConfig and SL-BWP-DiscPoolConfigCommon                                                                                                         18.3.0
  2024-06          RAN\#104              R5-242764   3173   \-    F     Add IEs SL-BWP-PRS-PoolConfig and SL-BWP-PRS-PoolConfigCommon                                                                                                         18.3.0
  2024-06          RAN\#104              R5-242772   3175   \-    F     Update channel access configurations for shared spectrum                                                                                                              18.3.0
  2024-06          RAN\#104              R5-242786   3176   \-    F     Update of Channel bandwidth in Default NG-RAN RRC message and information elements contents                                                                           18.3.0
  2024-06          RAN\#104              R5-242799   3178   \-    F     Addition of new combination of system information blocks for 5G Prose communication                                                                                   18.3.0
  2024-06          RAN\#104              R5-242800   3179   \-    F     Editorial update of SIB12 in 4.6.2                                                                                                                                    18.3.0
  2024-06          RAN\#104              R5-242802   3181   \-    F     Update of Table 4.6.1-22 RRCSetupComplete                                                                                                                             18.3.0
  2024-06          RAN\#104              R5-242803   3182   \-    F     Update of Table 4.6.1A-2A RemoteUEInformationSidelink                                                                                                                 18.3.0
  2024-06          RAN\#104              R5-242805   3184   \-    F     Addition of 5G ProSe discovery and security messages                                                                                                                  18.3.0
  2024-06          RAN\#104              R5-242806   3185   \-    F     Update of 5G ProSe direct discovery messages                                                                                                                          18.3.0
  2024-06          RAN\#104              R5-242810   3189   \-    F     Update of Default settings of UICC and USIM for 5G ProSe                                                                                                              18.3.0
  2024-06          RAN\#104              R5-242811   3190   \-    F     Update of Test procedure for 5G ProSe U2N Relay Discovery                                                                                                             18.3.0
  2024-06          RAN\#104              R5-242858   3191   \-    F     Correction to SUL n83 test frequencies in Table 4.3.1.1.1.83-1                                                                                                        18.3.0
  2024-06          RAN\#104              R5-242919   3193   \-    F     Addition of TE and UE connection diagram for 3Tx NR CA and EN-DC                                                                                                      18.3.0
  2024-06          RAN\#104              R5-243008   3195   \-    F     Clarification of test frequency for n5 CBW 25 MHz                                                                                                                     18.3.0
  2024-06          RAN\#104              R5-243168   3200   \-    F     Editorial correction of Table 4.5.4.2-4: WLAN IPsec\_SA\_Established                                                                                                  18.3.0
  2024-06          RAN\#104              R5-243187   3203   \-    F     Add IE SL-CBR-CommonTxDedicated-SL-PRS-RP-List                                                                                                                        18.3.0
  2024-06          RAN\#104              R5-243188   3204   \-    F     Add IE SL-ConfiguredGrantConfigDedicated-SL-PRS-RP                                                                                                                    18.3.0
  2024-06          RAN\#104              R5-243217   3206   \-    F     Add IEs SL-FreqSelectionConfig and SL-IndirectPathAddChange                                                                                                           18.3.0
  2024-06          RAN\#104              R5-243286   3207   \-    F     Corrections on 4.3.1 for NTN FR1 test channel bandwidth                                                                                                               18.3.0
  2024-06          RAN\#104              R5-243294   3209   \-    F     Corrections on 4.3.1.4.1.2 for test frequency for DC\_38A\_n78A                                                                                                       18.3.0
  2024-06          RAN\#104              R5-243337   3210   \-    F     Correction on Rel-17 HST conditions in ServingCellConfigCommon                                                                                                        18.3.0
  2024-06          RAN\#104              R5-243481   3212   \-    F     Addition of DCI information for semi static channel access in shared spectrum                                                                                         18.3.0
  2024-06          RAN\#104              R5-243482   3213   \-    F     Common configuration change for SDT condition                                                                                                                         18.3.0
  2024-06          RAN\#104              R5-243489   3148   1     F     Editorial correction for generic procedure 4.5.4, 4.5.5 and 4.5.7                                                                                                     18.3.0
  2024-06          RAN\#104              R5-243490   3154   1     F     Add IE Aerial-Config                                                                                                                                                  18.3.0
  2024-06          RAN\#104              R5-243491   3155   1     F     Add IE EpochTime                                                                                                                                                      18.3.0
  2024-06          RAN\#104              R5-243492   3205   1     F     Add IEs SL-DRX-Config, SL-DRX-ConfigGC-BC, SL-DRX-ConfigUC and SL-DRX-ConfigUC-SemiStatic                                                                             18.3.0
  2024-06          RAN\#104              R5-243493   3198   1     F     Correction to IE PDCCH-ConfigCommon                                                                                                                                   18.3.0
  2024-06          RAN\#104              R5-243494   3119   1     F     Introduction of signalling test frequencies for band n85                                                                                                              18.3.0
  2024-06          RAN\#104              R5-243533   3215         F     Addition of signalling test frequencies for CA\_n48C and CA\_n5B                                                                                                      18.3.0
  2024-06          RAN\#104              R5-243536   3174   1     F     Update of Logical Channel Config Table 4.6.3-66                                                                                                                       18.3.0
  2024-06          RAN\#104              R5-243546   3216         F     Correction for test procedure 4.9.41                                                                                                                                  18.3.0
  2024-06          RAN\#104              R5-243547   3180   1     F     Update of Test procedure for 5G ProSe Layer-2 U2N Relay initial access / Remote UE side                                                                               18.3.0
  2024-06          RAN\#104              R5-243548   3183   1     F     Update of Table 4.6.1A-8 uuMessageTransferSidelink                                                                                                                    18.3.0
  2024-06          RAN\#104              R5-243549   3186   1     F     Addition of Default HTTP messages for communication with the 5G ProSe                                                                                                 18.3.0
  2024-06          RAN\#104              R5-243550   3187   1     F     Addition of Default TLS message and information element contents                                                                                                      18.3.0
  2024-06          RAN\#104              R5-243551   3188   1     F     Addition of spec reference of 3GPP TS 33.310, 33.503 and IETF RFC 5246 for 5G ProSe information elements                                                              18.3.0
  2024-06          RAN\#104              R5-243554   3142   1     F     Added Common test environment for NR-NTN test cases                                                                                                                   18.3.0
  2024-06          RAN\#104              R5-243555   3171   1     F     Addition of system information combination for inter frequency NTN scenario                                                                                           18.3.0
  2024-06          RAN\#104              R5-243566   3121   1     F     Signalling test frequencies for 3 MHz and band n106                                                                                                                   18.3.0
  2024-06          RAN\#104              R5-243574   3144   1     F     Addition of generic procedure for UUAA-MM                                                                                                                             18.3.0
  2024-06          RAN\#104              R5-243581   3197   1     F     Addition of a new section for IDC Configuration                                                                                                                       18.3.0
  2024-06          RAN\#104              R5-243597   3143   1     F     Updates to SIB19 and ephemeris information for NGSO and GSO condition                                                                                                 18.3.0
  2024-06          RAN\#104              R5-243600   3196   1     F     Update inter-band NR CA configuration for CA\_n3A-n8A-n78A                                                                                                            18.3.0
  2024-06          RAN\#104              R5-243601   3122   1     F     Addition of 3 MHz CBW test frequencies for NR Bands n26, n28, n85 and n100                                                                                            18.3.0
  2024-06          RAN\#104              R5-243602   3118   1     F     Introduction of test channel bandwidths and test frequencies for band n85                                                                                             18.3.0
  2024-06          RAN\#104              R5-243603   3177   1     F     Update of editors note for test frequencies                                                                                                                           18.3.0
  2024-06          RAN\#104              R5-243604   3199   1     F     Addition of missing TRS configurations                                                                                                                                18.3.0
  2024-06          RAN\#104              R5-243654   3214         F     Correction of test bandwidth for CA\_n2(2A)                                                                                                                           18.3.0
  2024-06          RAN\#104              R5-243750   3208   1     F     Addition to 4.3.1 for FR2 Redcap UE test channel bandwidth                                                                                                            18.3.0
  2024-06          RAN\#104              R5-243833   3194   1     F     Correction to K1 for RRM TDD SCS 15 kHz                                                                                                                               18.3.0
  2024-06          RAN\#104              R5-243882   3139   1     F     Clarification of Test frequency limitations for CA in Annex C                                                                                                         18.3.0
  2024-06          RAN\#104              R5-243900   3211   1     F     Addition of connection diagram for CSI test cases for inter-cell interference scenarios                                                                               18.3.0
  2024-06          RAN\#104              R5-243952   3201   1     F     Common configuration for SN initiated inter-SN CPC EN-DC for 38.508-1                                                                                                 18.3.0
  2024-09          RAN\#105              R5-244094   3217   \-    F     Addition of test frequencies for CA\_n28A-n41A-n77A                                                                                                                   18.4.0
  2024-09          RAN\#105              R5-244099   3218   \-    F     Add IE SL-InterUE-CoordinationConfig                                                                                                                                  18.4.0
  2024-09          RAN\#105              R5-244100   3219   \-    F     Add IE SL-LBT-FailureRecoveryConfig                                                                                                                                   18.4.0
  2024-09          RAN\#105              R5-244102   3221   \-    F     Add IEs SL-PosBWP-ConfigCommon and SL-PRS-ResourcePool                                                                                                                18.4.0
  2024-09          RAN\#105              R5-244103   3222   \-    F     Add IEs SL-RBSetConfig and SL-RelayIndicationMP                                                                                                                       18.4.0
  2024-09          RAN\#105              R5-244104   3223   \-    F     Add IEs SL-RelayUE-ConfigU2U and SL-RemoteUE-ConfigU2U                                                                                                                18.4.0
  2024-09          RAN\#105              R5-244114   3224   \-    F     Add IE SL-RLC-ChannelConfig                                                                                                                                           18.4.0
  2024-09          RAN\#105              R5-244115   3225   \-    F     Add IEs SL-ServingCellInfo and SL-SourceIdentity                                                                                                                      18.4.0
  2024-09          RAN\#105              R5-244116   3226   \-    F     Add IE SL-SRAP-ConfigU2U                                                                                                                                              18.4.0
  2024-09          RAN\#105              R5-244117   3227   \-    F     Correct IE SL-DRX-ConfigGC-BC                                                                                                                                         18.4.0
  2024-09          RAN\#105              R5-244118   3228   \-    F     Correct IE SL-AccessInfo-L2U2N                                                                                                                                        18.4.0
  2024-09          RAN\#105              R5-244137   3229   \-    F     Add IE SIB17bis                                                                                                                                                       18.4.0
  2024-09          RAN\#105              R5-244229   3236   \-    F     Correction to RRC IE RadioBearerConfig                                                                                                                                18.4.0
  2024-09          RAN\#105              R5-244231   3238   \-    F     Editorial update to RRC IE BT-NameList and WLAN-NameList                                                                                                              18.4.0
  2024-09          RAN\#105              R5-244232   3239   \-    F     Editorial correction to the table in cl. 6.1.3.3                                                                                                                      18.4.0
  2024-09          RAN\#105              R5-244313   3242   \-    F     Update IE AppLayerMeasConfig                                                                                                                                          18.4.0
  2024-09          RAN\#105              R5-244314   3243   \-    F     Update IE MeasConfigAppLayerId                                                                                                                                        18.4.0
  2024-09          RAN\#105              R5-244315   3244   \-    F     Update RRCReconfiguration configuration for SRB4                                                                                                                      18.4.0
  2024-09          RAN\#105              R5-244326   3249   \-    F     Updates for test configuration of CA\_n2A-n5A-n66A                                                                                                                    18.4.0
  2024-09          RAN\#105              R5-244331   3250   \-    F     Updates for additional test configurations                                                                                                                            18.4.0
  2024-09          RAN\#105              R5-244372   3251   \-    F     Frequency related parameters corrections for n100                                                                                                                     18.4.0
  2024-09          RAN\#105              R5-244379   3252   \-    F     CBW clarification in case of asymmetric BW                                                                                                                            18.4.0
  2024-09          RAN\#105              R5-244380   3253   \-    F     Clarification on rules to calculate Low and High DL frequency in case of asymmetric UL and DL BW                                                                      18.4.0
  2024-09          RAN\#105              R5-244386   3254   \-    F     Introduction of test channel bandwidths and test frequencies for bands n31 and n72                                                                                    18.4.0
  2024-09          RAN\#105              R5-244388   3256   \-    F     Demodulation test frequencies for bands n31 and n72                                                                                                                   18.4.0
  2024-09          RAN\#105              R5-244408   3257   \-    F     Correct IE CSI-ReportSubConfig                                                                                                                                        18.4.0
  2024-09          RAN\#105              R5-244409   3258   \-    F     Update IE FeatureCombination                                                                                                                                          18.4.0
  2024-09          RAN\#105              R5-244410   3259   \-    F     Add IE MeasurementValidityDuration                                                                                                                                    18.4.0
  2024-09          RAN\#105              R5-244461   3262   \-    F     Correction of test frequencies for CA\_n66(2A)                                                                                                                        18.4.0
  2024-09          RAN\#105              R5-244462   3263   \-    F     Removal of editors Note for CA\_n77(2A)                                                                                                                               18.4.0
  2024-09          RAN\#105              R5-244463   3264   \-    F     Addition of Round in Symbols chapter                                                                                                                                  18.4.0
  2024-09          RAN\#105              R5-244464   3265   \-    F     Addition of test frequencies for CA\_n48C                                                                                                                             18.4.0
  2024-09          RAN\#105              R5-244485   3266   \-    F     Editorial correction to ATG RF/Demod IE values                                                                                                                        18.4.0
  2024-09          RAN\#105              R5-244486   3267   \-    F     Editorial correction to ATG RRM IE values                                                                                                                             18.4.0
  2024-09          RAN\#105              R5-244527   3273   \-    F     Add IE PDCCH-RACH-DL-Info                                                                                                                                             18.4.0
  2024-09          RAN\#105              R5-244540   3274   \-    F     Addition of many 3 band EN-DC combos                                                                                                                                  18.4.0
  2024-09          RAN\#105              R5-244576   3277   \-    F     Updates to default UE Policy Delivery messages                                                                                                                        18.4.0
  2024-09          RAN\#105              R5-244602   3279   \-    F     Correction to default configurations for MCE test cases                                                                                                               18.4.0
  2024-09          RAN\#105              R5-244648   3280   \-    F     Addition of default configuration of SI-RequestConfigRepetition-r18                                                                                                   18.4.0
  2024-09          RAN\#105              R5-244693   3284   \-    F     Addition of Physical layer parameters for DCI format 0\_3                                                                                                             18.4.0
  2024-09          RAN\#105              R5-244694   3285   \-    F     Addition of Physical layer parameters for DCI format 1\_3                                                                                                             18.4.0
  2024-09          RAN\#105              R5-244696   3287   \-    F     Update of PDSCH-Config for DCI format 1\_3                                                                                                                            18.4.0
  2024-09          RAN\#105              R5-244709   3290   \-    F     Update ServingCellConfigCommonSIB DownlinkConfigCommonSIB and BWP-DownlinkCommon for MBS                                                                              18.4.0
  2024-09          RAN\#105              R5-244710   3291   \-    F     Update PDSCH-ConfigBroadcast-r17 CFR-ConfigMCCH-MTCH and MBSBroadcastConfiguration                                                                                    18.4.0
  2024-09          RAN\#105              R5-244711   3292   \-    F     Update DCI format 4-0                                                                                                                                                 18.4.0
  2024-09          RAN\#105              R5-244789   3297   \-    F     Update IE AppLayerMeasParameters                                                                                                                                      18.4.0
  2024-09          RAN\#105              R5-244791   3299   \-    F     Addition of DCI information for dynamic channel access in shared spectrum                                                                                             18.4.0
  2024-09          RAN\#105              R5-244792   3300   \-    F     Updated ChannelAccessConfig Table                                                                                                                                     18.4.0
  2024-09          RAN\#105              R5-244812   3301   \-    F     Clarification of test frequency for n70 CBW 25 MHz                                                                                                                    18.4.0
  2024-09          RAN\#105              R5-244902   3307   \-    F     Correction of test frequency for NR band n13                                                                                                                          18.4.0
  2024-09          RAN\#105              R5-244914   3308   \-    F     Update inter-band NR CA configuration of three bands CA\_n1A-n5A-n78                                                                                                  18.4.0
  2024-09          RAN\#105              R5-244923   3309   \-    F     Updates on 4.3.1.0D for bandwidth part for 3MHz BW                                                                                                                    18.4.0
  2024-09          RAN\#105              R5-244976   3312   \-    F     Update of Default NG-RAN RRC message and information elements contents table 4.6.3-142 ReportConfigNR                                                                 18.4.0
  2024-09          RAN\#105              R5-245068   3313   \-    F     Addition of test frequency for R16 Inter-band EN-DC FR1 configurations with three bands                                                                               18.4.0
  2024-09          RAN\#105              R5-245071   3314   \-    F     Addition of test frequency for Inter-band EN-DC FR1 DC\_2A-66A-66A\_n2A                                                                                               18.4.0
  2024-09          RAN\#105              R5-245215   3319   \-    F     Clarification of test frequency for n8 and n71 CBW 35 MHz                                                                                                             18.4.0
  2024-09          RAN\#105              R5-245220   3320   \-    F     Correction of BWP-UplinkDedicated                                                                                                                                     18.4.0
  2024-09          RAN\#105              R5-245313   3321   \-    F     Addition of eRedCap default test channel bandwidth                                                                                                                    18.4.0
  2024-09          RAN\#105              R5-245324   3322   \-    F     Correction to Signalling test frequency parameters for band n106                                                                                                      18.4.0
  2024-09          RAN\#105              R5-245334   3323   \-    F     Update on CSI-ReportingBand for RRM testing                                                                                                                           18.4.0
  2024-09          RAN\#105              R5-245335   3324   \-    F     Update on pdcch-DMRS-SCID for RRM testing                                                                                                                             18.4.0
  2024-09          RAN\#105              R5-245339   3325   \-    F     Update CSI-ReportConfig for PMI eTypeII test cases                                                                                                                    18.4.0
  2024-09          RAN\#105              R5-245484   3326   \-    F     Adding eUICC reference and update to common test UICC configuration                                                                                                   18.4.0
  2024-09          RAN\#105              R5-245490   3220   1     F     Add IEs SL-PagingIdentityRemoteUE and SL-PBPS-CPS-Config                                                                                                              18.4.0
  2024-09          RAN\#105              R5-245491   3237   1     F     Correction to RRC IE ReportConfigNR and ReportConfigNR-SL                                                                                                             18.4.0
  2024-09          RAN\#105              R5-245492   3296   1     F     Update 2 steps RACH message contents                                                                                                                                  18.4.0
  2024-09          RAN\#105              R5-245493   3275   1     F     Updates to default 5GMM messages                                                                                                                                      18.4.0
  2024-09          RAN\#105              R5-245494   3276   1     F     Updates to default 5GSM messages                                                                                                                                      18.4.0
  2024-09          RAN\#105              R5-245495   3231   1     F     Corrections to DNN APN configurations                                                                                                                                 18.4.0
  2024-09          RAN\#105              R5-245496   3272   1     F     Addition of a new cell combination for IDC Configuration                                                                                                              18.4.0
  2024-09          RAN\#105              R5-245544   3298   1     F     Addition of DCI configuration for dynamic channel access in shared spectrum                                                                                           18.4.0
  2024-09          RAN\#105              R5-245545   3232   1     F     Addition of Paging message contents values for 3GPP MT-SDT                                                                                                            18.4.0
  2024-09          RAN\#105              R5-245546   3233   1     F     Addition of RRCRelease message contents values for 3GPP MT-SDT                                                                                                        18.4.0
  2024-09          RAN\#105              R5-245547   3234   1     F     Addition of SIB1 message contents values for 3GPP MT-SDT                                                                                                              18.4.0
  2024-09          RAN\#105              R5-245549   3281   1     F     Addition of default configuration of SI-SchedulingInfo-v1800                                                                                                          18.4.0
  2024-09          RAN\#105              R5-245550   3282   1     F     Correction of default configuration of FeatureCombinationPreambles                                                                                                    18.4.0
  2024-09          RAN\#105              R5-245556   3303   1     F     Update of RRC message for Further NR mobility enhancements                                                                                                            18.4.0
  2024-09          RAN\#105              R5-245557   3304   1     F     Addition of RRC IEs for Further NR mobility enhancements                                                                                                              18.4.0
  2024-09          RAN\#105              R5-245581   3310   1     F     Update of the content of sidelink information elements and 5G ProSe discovery messages                                                                                18.4.0
  2024-09          RAN\#105              R5-245582   3311   1     F     Update of Default NG-RAN RRC message and information elements contents table 4.6.3-141 ReportConfigInterRAT                                                           18.4.0
  2024-09          RAN\#105              R5-245591   3240   1     F     Update MeasurementReportAppLayer message                                                                                                                              18.4.0
  2024-09          RAN\#105              R5-245592   3241   1     F     Update RRCReconfiguration message                                                                                                                                     18.4.0
  2024-09          RAN\#105              R5-245593   3245   1     F     Add configuration for application layer measurements                                                                                                                  18.4.0
  2024-09          RAN\#105              R5-245619   3255   1     F     Signalling test frequencies for bands n31 and n72                                                                                                                     18.4.0
  2024-09          RAN\#105              R5-245620   3317   1     F     Signalling test frequencies for 5MHz and band n54                                                                                                                     18.4.0
  2024-09          RAN\#105              R5-245621   3268   1     F     Update of ATG RRC messages and information elements                                                                                                                   18.4.0
  2024-09          RAN\#105              R5-245622   3278   1     F     Update to the RRC message related to R18 MUSIM                                                                                                                        18.4.0
  2024-09          RAN\#105              R5-245624   3295   1     F     Update SIB1 for adding SIB1-v1800-Ies                                                                                                                                 18.4.0
  2024-09          RAN\#105              R5-245630   3327   1     \-    Addition of Cell DTX and DRX related IEs                                                                                                                              18.4.0
  2024-09          RAN\#105              R5-245636   3286   1     F     Update of Searchspace for DCI format 1\_3 and 0\_3                                                                                                                    18.4.0
  2024-09          RAN\#105              R5-245637   3288   1     F     Update of PUSCH-Config for DCI format 0\_3                                                                                                                            18.4.0
  2024-09          RAN\#105              R5-245638   3289   1     F     Update of ServingCellConfig for DCI format 1\_3 and 0\_3                                                                                                              18.4.0
  2024-09          RAN\#105              R5-245654   3230   1     F     Corrections to test procedure for UUAA-MM                                                                                                                             18.4.0
  2024-09          RAN\#105              R5-245656   3329   1     F     Allow tester to disable IMS and set Data Centric                                                                                                                      18.4.0
  2024-09          RAN\#105              R5-245657   3261   2     F     Update on Test procedures for 5G ProSe Layer-2 U2N Relay initial access                                                                                               18.4.0
  2024-09          RAN\#105              R5-245801   3269   1     F     Addition of Test frequencies for CA\_n28A-n41C                                                                                                                        18.4.0
  2024-09          RAN\#105              R5-245802   3270   1     F     Addition of Test frequencies for CA\_n41A-n79C                                                                                                                        18.4.0
  2024-09          RAN\#105              R5-245803   3246   1     F     Updates for a few section headings format and an Editors Note                                                                                                         18.4.0
  2024-09          RAN\#105              R5-245972   3247   1     F     Update for additional Rel-16 NR-CA band configurations                                                                                                                18.4.0
  2024-09          RAN\#105              R5-245973   3248   1     F     Update for additional Rel-17 NR-CA and NR-DC band configurations                                                                                                      18.4.0
  2024-09          RAN\#105              R5-245974   3316   1     F     Introduction of test channel bandwidths and test frequencies for band n54                                                                                             18.4.0
  2024-09          RAN\#105              R5-245976   3283   1     F     Correction of notes for High Test Channel bandwidth                                                                                                                   18.4.0
  2024-09          RAN\#105              R5-245993   3315   1     F     Updates to High test channel bandwidth Informative Note 1 for FR1 and FR2                                                                                             18.4.0
  2024-09          RAN\#105              R5-246040   3306   1     F     Adding new connection diagrams for SUL operation with inter-band CA                                                                                                   18.4.0
  2024-12          RAN\#106              R5-246127   3330   \-    F     Addition of test frequencies for new R16 2CC NRCA combos with n40                                                                                                     18.5.0
  2024-12          RAN\#106              R5-246128   3331   \-    F     Addition of test frequencies for CA\_n40A-n77A                                                                                                                        18.5.0
  2024-12          RAN\#106              R5-246193   3332   \-    F     Addition of test frequencies for new 3CC NRCA combos within FR1                                                                                                       18.5.0
  2024-12          RAN\#106              R5-246255   3334   \-    F     Introduction of test channel bandwidths and test frequencies for band n105                                                                                            18.5.0
  2024-12          RAN\#106              R5-246256   3335   \-    F     Signalling test frequencies for band n105                                                                                                                             18.5.0
  2024-12          RAN\#106              R5-246257   3336   \-    F     Demodulation test frequencies for band n105                                                                                                                           18.5.0
  2024-12          RAN\#106              R5-246270   3337   \-    F     Editorial CR implementation correction for n100 Low test CBW                                                                                                          18.5.0
  2024-12          RAN\#106              R5-246283   3338   \-    F     Correction to signalling test frequencies for bands n31 and n72                                                                                                       18.5.0
  2024-12          RAN\#106              R5-246323   3339   \-    F     Update IE CandidateTCI-State                                                                                                                                          18.5.0
  2024-12          RAN\#106              R5-246324   3340   \-    F     Update IE CandidateTCI-UL-State                                                                                                                                       18.5.0
  2024-12          RAN\#106              R5-246325   3341   \-    F     Update IE EarlyUL-SyncConfig                                                                                                                                          18.5.0
  2024-12          RAN\#106              R5-246326   3342   \-    F     Update IE LTM-TCI-Info                                                                                                                                                18.5.0
  2024-12          RAN\#106              R5-246364   3345   \-    F     Correction to RRC IE RadioBearerConfig                                                                                                                                18.5.0
  2024-12          RAN\#106              R5-246365   3346   \-    F     Correction to RRC IE UE-CapabilityRequestFilterNR                                                                                                                     18.5.0
  2024-12          RAN\#106              R5-246400   3347   \-    F     Corrections to PDCCH-Config                                                                                                                                           18.5.0
  2024-12          RAN\#106              R5-246403   3348   \-    F     Updates to test procedure 4.9.44 for UUAA-MM                                                                                                                          18.5.0
  2024-12          RAN\#106              R5-246467   3351   \-    F     CR 38.508-1 Definition of many NR CA combos with 2 bands and 3 bands                                                                                                  18.5.0
  2024-12          RAN\#106              R5-246482   3353   \-    F     Update test procedure 4.9.15                                                                                                                                          18.5.0
  2024-12          RAN\#106              R5-246483   3354   \-    F     Update test procedure 4.9.16                                                                                                                                          18.5.0
  2024-12          RAN\#106              R5-246505   3356   \-    F     Introduction of Setup Diagrams for V2X receiver test cases                                                                                                            18.5.0
  2024-12          RAN\#106              R5-246580   3358   \-    F     Correction of ServingCellConfig                                                                                                                                       18.5.0
  2024-12          RAN\#106              R5-246591   3359   \-    F     Correction of PDSCH-ConfigBroadcast-r17                                                                                                                               18.5.0
  2024-12          RAN\#106              R5-246592   3360   \-    F     Correction of DCI format 4-0 for MBS broadcast                                                                                                                        18.5.0
  2024-12          RAN\#106              R5-246597   3361   \-    F     Update SIG default test frequencies for eRedCap UE                                                                                                                    18.5.0
  2024-12          RAN\#106              R5-246598   3362   \-    F     Update PDCP-Config and RLC-Config for eRedCap UE                                                                                                                      18.5.0
  2024-12          RAN\#106              R5-246599   3363   \-    F     Update SIB4 for eRedCap UE                                                                                                                                            18.5.0
  2024-12          RAN\#106              R5-246600   3364   \-    F     Update common test environment for eRedCap UE                                                                                                                         18.5.0
  2024-12          RAN\#106              R5-246631   3365   \-    F     Update NTN satellite information clause 6.3.4                                                                                                                         18.5.0
  2024-12          RAN\#106              R5-246740   3370   \-    F     Correction to test procedure 4.9.22 - Unicast link establishment                                                                                                      18.5.0
  2024-12          RAN\#106              R5-246756   3371   \-    F     Correction to default configuration of FeatureCombination                                                                                                             18.5.0
  2024-12          RAN\#106              R5-246757   3372   \-    F     Correction to default configuration of SI-RequestConfig                                                                                                               18.5.0
  2024-12          RAN\#106              R5-246785   3374   \-    F     Addition of many 3 band EN-DC combos                                                                                                                                  18.5.0
  2024-12          RAN\#106              R5-246894   3377   \-    F     Update of Table 4.6.1-13 RRCReconfiguration for Sidelink relay                                                                                                        18.5.0
  2024-12          RAN\#106              R5-246964   3381   \-    F     Correction of mistakes in C.2.6.1 and C.2.6.3                                                                                                                         18.5.0
  2024-12          RAN\#106              R5-247001   3382   \-    F     Correction to PTRS configuration for FR2 PDSCH testing                                                                                                                18.5.0
  2024-12          RAN\#106              R5-247025   3383   \-    F     Adding new connection diagrams for UE supporting 8Rx                                                                                                                  18.5.0
  2024-12          RAN\#106              R5-247042   3384   \-    F     Addition of test frequencies for CA\_n79C                                                                                                                             18.5.0
  2024-12          RAN\#106              R5-247043   3385   \-    F     Addition of test frequencies for 5 MHz BW for n41                                                                                                                     18.5.0
  2024-12          RAN\#106              R5-247044   3386   \-    F     Correction of test frequencies for CA\_n77(2A)                                                                                                                        18.5.0
  2024-12          RAN\#106              R5-247171   3388   \-    F     Correction to pdcch-DMRS-ScramblingID                                                                                                                                 18.5.0
  2024-12          RAN\#106              R5-247199   3390   \-    F     Update of Table 4.9.39.3-7 and Table 4.9.40.3-5 for test procedure for establishing unicast mode ProSe Direct communication                                           18.5.0
  2024-12          RAN\#106              R5-247202   3393   \-    F     Update of Tables for SL L2 U2N Relay UE and Remote UE                                                                                                                 18.5.0
  2024-12          RAN\#106              R5-247214   3394   \-    F     Addition of NR CA and DC configurations for shared spectrum                                                                                                           18.5.0
  2024-12          RAN\#106              R5-247215   3395   \-    F     Addition of channel bandwidths for interband CA test cases                                                                                                            18.5.0
  2024-12          RAN\#106              R5-247247   3397   \-    F     Introduction of test channel bandwidths and test frequencies for band n8, n39, n98 and n109                                                                           18.5.0
  2024-12          RAN\#106              R5-247248   3398   \-    F     Introduction of test channel bandwidths and test frequencies for Demodulation test cases for band n109                                                                18.5.0
  2024-12          RAN\#106              R5-247334   3402   \-    F     Addition of connection diagram for antenna configuration 4x1                                                                                                          18.5.0
  2024-12          RAN\#106              R5-247345   3403   \-    F     Update on message content for PMI reporting test cases                                                                                                                18.5.0
  2024-12          RAN\#106              R5-247346   3404   \-    F     Updates on message content for FR2 CQI and RI test cases                                                                                                              18.5.0
  2024-12          RAN\#106              R5-247371   3405   \-    F     Addition of test frequency for CA\_n1A-n5A                                                                                                                            18.5.0
  2024-12          RAN\#106              R5-247380   3406   \-    F     Addition of test frequency for CA\_n5A-n78A                                                                                                                           18.5.0
  2024-12          RAN\#106              R5-247388   3407   \-    F     Update inter-band NR CA configuration of three bands CA\_n3A-n5A-n78                                                                                                  18.5.0
  2024-12          RAN\#106              R5-247580   3378   1     F     Addition of Table 4.6.1A-2B NotificationMessageSidelink                                                                                                               18.5.0
  2024-12          RAN\#106              R5-247581   3379   1     F     Update of the content of sidelink information elements and Pre-configuration for Sidelink                                                                             18.5.0
  2024-12          RAN\#106              R5-247582   3391   1     F     Update of 4.9.41 Test procedure for 5G ProSe Layer-2 U2N Relay initial access / Relay UE side                                                                         18.5.0
  2024-12          RAN\#106              R5-247583   3392   1     F     Update of 4.9.42 Test procedure for 5G ProSe Layer-2 U2N Relay initial access / Remote UE side                                                                        18.5.0
  2024-12          RAN\#106              R5-247598   3375   1     F     SIB19 Updates related to NR NTN-Rel18                                                                                                                                 18.5.0
  2024-12          RAN\#106              R5-247614   3399   1     F     Introduction of test channel bandwidths and test frequencies for signalling testing for band n98 and n109                                                             18.5.0
  2024-12          RAN\#106              R5-247615   3401   1     F     Introduction of test channel bandwidths and test frequencies for signalling test for band n254                                                                        18.5.0
  2024-12          RAN\#106              R5-247629   3344   1     F     Updates to RRC message and IEs for Further NR mobility enhancements                                                                                                   18.5.0
  2024-12          RAN\#106              R5-247630   3387   1     F     Addition of RRC IEs for Further measurement gap enhancements                                                                                                          18.5.0
  2024-12          RAN\#106              R5-247663   3350   1     F     Correction to Clause 4.9.6 test procedures for Switch off / Power off UE                                                                                              18.5.0
  2024-12          RAN\#106              R5-247672   3376   1     F     SIB25 Updates related to NR NTN-Rel18                                                                                                                                 18.5.0
  2024-12          RAN\#106              R5-247678   3366   1     F     Addition of SIG Test frequencies for CA\_n79C                                                                                                                         18.5.0
  2024-12          RAN\#106              R5-247700   3352   1     F     Updates for Release 17 part of test configuration CA\_n2A-n5A-n66A-n77C                                                                                               18.5.0
  2024-12          RAN\#106              R5-247701   3355   1     F     Updates for Release 18 part of test configuration CA\_n2A-n5A-n66A-n77C                                                                                               18.5.0
  2024-12          RAN\#106              R5-247702   3367   1     F     Update Low Test Channel Bandwidth for band n41                                                                                                                        18.5.0
  2024-12          RAN\#106              R5-247703   3368   1     F     Correction to default configuration of PDSCH-Config for SDR test                                                                                                      18.5.0
  2024-12          RAN\#106              R5-247704   3373   1     F     Addition of EN-DC combo DC\_2A-5A\_n66A                                                                                                                               18.5.0
  2024-12          RAN\#106              R5-247783   3400   1     F     Introduction of test channel bandwidths and test frequencies for band n254                                                                                            18.5.0
  2024-12          RAN\#106              R5-247922   3380   1     F     Correction to default message contents for Demod tests                                                                                                                18.5.0
  2024-12          RAN\#106              R5-247997   3369   1     F     Correction to default configuration of 2-step RACH related message contents for RRM TCs                                                                               18.5.0
  2025-03          RAN\#107              R5-250041   3408   \-    F     Add IE AdditionalPCIIndex                                                                                                                                             18.6.0
  2025-03          RAN\#107              R5-250079   3411   \-    F     Update to EarlyUL-SyncConfig-r18 for Further NR mobility enhancements                                                                                                 18.6.0
  2025-03          RAN\#107              R5-250121   3413   \-    F     Addition of test CBW for band n104                                                                                                                                    18.6.0
  2025-03          RAN\#107              R5-250123   3414   \-    F     Addition of Test frequencies for CA\_n41C-n79C                                                                                                                        18.6.0
  2025-03          RAN\#107              R5-250180   3416   \-    F     Update test procedure 4.9.24                                                                                                                                          18.6.0
  2025-03          RAN\#107              R5-250183   3417   \-    F     Update test procedure 4.9.26                                                                                                                                          18.6.0
  2025-03          RAN\#107              R5-250225   3418   \-    F     Addition of test frequencies for new 4CC NRCA combo within FR1                                                                                                        18.6.0
  2025-03          RAN\#107              R5-250241   3420   \-    F     Adding demodulation test frequencies for bands n13 and n85                                                                                                            18.6.0
  2025-03          RAN\#107              R5-250273   3422   \-    F     Addition of several NR CA combination to inter-band configurations table                                                                                              18.6.0
  2025-03          RAN\#107              R5-250313   3424   \-    F     Correction of clause 4.9.12B                                                                                                                                          18.6.0
  2025-03          RAN\#107              R5-250314   3425   \-    F     Corrections of clauses 4.9.11 and 4.9.12                                                                                                                              18.6.0
  2025-03          RAN\#107              R5-250315   3426   \-    F     Updates to clause 4.5.1                                                                                                                                               18.6.0
  2025-03          RAN\#107              R5-250316   3427   \-    F     Interpretation of UL RRC IE presence and values                                                                                                                       18.6.0
  2025-03          RAN\#107              R5-250318   3429   \-    F     Correction of RRCReconfiguration-SRB2-SRB4-DRB(n, m)                                                                                                                  18.6.0
  2025-03          RAN\#107              R5-250401   3430   \-    F     Addition of signalling parameters for spectrum less than 5MHz for FR1                                                                                                 18.6.0
  2025-03          RAN\#107              R5-250446   3431   \-    F     Support of MCX                                                                                                                                                        18.6.0
  2025-03          RAN\#107              R5-250453   3433   \-    F     Addition of test frequencies for interband CA test cases                                                                                                              18.6.0
  2025-03          RAN\#107              R5-250584   3434   \-    F     Correction of Scheduling for combination NR-22                                                                                                                        18.6.0
  2025-03          RAN\#107              R5-250628   3436   \-    F     Addition of referenced specification for extreme conditions in the References section                                                                                 18.6.0
  2025-03          RAN\#107              R5-250635   3438   \-    F     Addition of test frequencies for n48(2A), BCS1                                                                                                                        18.6.0
  2025-03          RAN\#107              R5-250756   3442   \-    F     Inclination correction in orbital format GSO ephemeris files                                                                                                          18.6.0
  2025-03          RAN\#107              R5-250970   3444   \-    F     Update of Tables for Uu-RelayRLC-ChannelID and SL-RLC-ChannelID                                                                                                       18.6.0
  2025-03          RAN\#107              R5-250979   3446   \-    F     Update of Table 4.6.6-7 SL-ConfigDedicatedNR                                                                                                                          18.6.0
  2025-03          RAN\#107              R5-251024   3447   \-    F     Editorial correction to clause 4.5B.4                                                                                                                                 18.6.0
  2025-03          RAN\#107              R5-251031   3448   \-    F     Correction to test procedure 4.9.27                                                                                                                                   18.6.0
  2025-03          RAN\#107              R5-251033   3449   \-    F     Corrections to reference radio configurations in clause 4.8.1                                                                                                         18.6.0
  2025-03          RAN\#107              R5-251255   3409   1     F     Update IE CandidateTCI-State                                                                                                                                          18.6.0
  2025-03          RAN\#107              R5-251256   3410   1     F     Update IE LTM-TCI-Info                                                                                                                                                18.6.0
  2025-03          RAN\#107              R5-251257   3428   1     F     Interpretation of UL NAS IE presence and values                                                                                                                       18.6.0
  2025-03          RAN\#107              R5-251288   3451   \-    F     Update SIG default test frequencies for band n106                                                                                                                     18.6.0
  2025-03          RAN\#107              R5-251307   3445   1     F     Addition of test procedure for 5G ProSe Layer-2 U2N Relay / Remote UE RRC Reestablishment / Remote UE side                                                            18.6.0
  2025-03          RAN\#107              R5-251368   3435   1     F     Addition of default parameters for DSR testcases to common specification.                                                                                             18.6.0
  2025-03          RAN\#107              R5-251375   3412   1     F     Correction to Generic procedure 4.5.2.2-2                                                                                                                             18.6.0
  2025-03          RAN\#107              R5-251500   3439   1     F     Addition of test frequencies for CA\_n78(2A), UL CA, BCS 0,1,2                                                                                                        18.6.0
  2025-03          RAN\#107              R5-251501   3419   1     F     Adding NR CA\_n78A-n258A test frequencies to NR CA Capability table                                                                                                   18.6.0
  2025-03          RAN\#107              R5-251502   3437   1     F     Addition of test frequencies for CA\_n77(2A), BCS 4,5                                                                                                                 18.6.0
  2025-03          RAN\#107              R5-251674   3423   1     F     Test frequency corrections for 3MHz CBW                                                                                                                               18.6.0
  2025-03          RAN\#107              R5-251686   3441   1     F     Addition of test frequencies for new NR CA comb within FR1                                                                                                            18.6.0
  ---------------- --------------------- ----------- ------ ----- ----- --------------------------------------------------------------------------------------------------------------------------------------------------------------------- -------------
