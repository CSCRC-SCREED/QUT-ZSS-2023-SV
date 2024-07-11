## Scenario 944
In this scenario, the malicious program modifies a certain number of the original SV packets with fake measurements to spoof an emergency (short-circuit) situation around Feeders. The malicious program starts from approximately the 15th second, the 60th second, and the 105th second, respectively. The scenario contains a total of ${\color{red}eight}$ sub-scenarios, which are combinations of ${\color{red}four}$ attack targets and ${\color{red}two}$ attack configurations.

**QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose.**

1. **${\color{red}Four}$ attack targets**: 
   - **a**: spoofing a short-circuit fault happens in Fault_FDR1 to disrupt the power supply (measurements FDR1=22kV1=F_FDR1=2017)
   - **b**: spoofing a short-circuit fault happens in Fault_FDR2 to disrupt the power supply (measurements FDR2=F_FDR2=2017)
   - **c**: spoofing a short-circuit fault happens in Fault_FDR3 to disrupt the power supply (measurements FDR3=F_FDR3=2017)
   - **d**: spoofing a short-circuit fault happens in Fault_FDR4 to disrupt the power supply (measurements FDR4=22kV3=F_FDR4=2017)
2. **${\color{red}Two}$ attack configurations**:
   - **9441**: modifying the measurements of 20 SV packets
   - **9442**: modifying the measurements of 2 SV packets

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023-SV/blob/main/Datasets/PrimaryPlant.jpg" alt="" width="800" height="510" />