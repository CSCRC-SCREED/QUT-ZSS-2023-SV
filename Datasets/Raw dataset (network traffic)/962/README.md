## Scenario 962
In this scenario,  when a true emergency (short-circuit) occurs around Transformers, the malicious program starts by recording all variations in measurements until the fault is isolated (the associated measurements drop to 0). In a future moment (e.g., 100 seconds after the true emergency occurs), the malicious program starts again and modifies a certain number of the original SV packets with the recorded measurements to replay an emergency (short-circuit) situation around Transformers. The scenario contains a total of ${\color{red}eight}$ sub-scenarios, which are combinations of ${\color{red}two}$ attack targets and ${\color{red}four}$ attack configurations.

**QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose.**

1. **${\color{red}Two}$ attack targets**: 
   - **a**: replaying a short-circuit fault happens in Fault_XFMR1 to disrupt the power supply
   - **b**: replaying a short-circuit fault happens in Fault_XFMR2 to disrupt the power supply
2. **${\color{red}Four}$ attack configurations**:
   - **9621**: modifying SV packets with all recorded measurements
   - **9622**: modifying SV packets with the first one-third recorded measurements
   - **9623**: modifying SV packets with all recorded measurements, while increasing the measurement values to 1.1 times
   - **9624**: modifying SV packets with the first quater recorded measurements, while increasing the measurement values to 1.2 times

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023-SV/blob/main/Datasets/PrimaryPlant.jpg" alt="" width="800" height="510" />
