## Scenario 931
In this scenario, the malicious program injects SV packets with fake measurements to spoof an emergency (short-circuit) situation on the 66kV bus line. The malicious program starts from approximately the 15th second, the 60th second, and the 105th second, respectively. The scenario contains a total of ${\color{red}four}$ sub-scenarios, which are combinations of ${\color{red}two}$ attack targets and ${\color{red}two}$ attack configurations.

**QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose.**

1. **${\color{red}Two}$ attack targets**: 
   - **a**: spoofing a short-circuit fault happens in Fault_66bus1 to disrupt the power supply (measurements 66kV1=F_66KV1=2017)
   - **b**: spoofing a short-circuit fault happens in Fault_66bus2 to disrupt the power supply (measurements 66kV3=F_66KV3=2017)
2. **${\color{red}Two}$ attack configurations**:
   - **9311**: injecting 100 packets with a fixed heartbeat of 50ms 
   - **9312**: injecting 80 packets with a fixed heartbeat of 25ms

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023-SV/blob/main/Datasets/PrimaryPlant.jpg" alt="" width="800" height="510" />
