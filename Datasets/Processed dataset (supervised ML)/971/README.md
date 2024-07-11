## Scenario 971
In this scenario, the malicious program deletes the first 100 SV packets only when an over-current status occurs on the 66kV bus line (measurements exceed the pre-defined threshold). Such an attack will delay the predefined safety protection for about 5 seconds. The scenario contains a total of ${\color{red}two}$ sub-scenarios, which are referred to ${\color{red}two}$ attack targets.

**QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose.**

1. **${\color{red}Two}$ attack targets**: 
   - **a**: delaying the safety protection when a short-circuit fault happens in Fault_66bus1 
   - **b**: delaying the safety protection when a short-circuit fault happens in Fault_66bus2

> <sup>*</sup> Since the malicious program only deletes the legitimate SV packets, and the remaining SV packets are non-malicious, no sample is labelled as 971. However, within a 5-second period (labelled with ${\color{red}Red}$ font colour), SV packets with APPID "0x4001" were missing. These abnormal behaviours can be easily detected with a simple network monitoring method.

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023-SV/blob/main/Datasets/PrimaryPlant.jpg" alt="" width="800" height="510" />
