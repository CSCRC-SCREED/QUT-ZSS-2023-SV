## Scenario 963
In this scenario,  when a true emergency (short-circuit) occurs on the 22kV bus line, the malicious program starts by recording all variations in measurements until the fault is isolated (the associated measurements drop to 0). In a future moment (e.g., 100 seconds after the true emergency occurs), the malicious program starts again and modifies a certain number of the original SV packets with the recorded measurements to replay an emergency (short-circuit) situation on the 22kV bus line. The scenario contains a total of ${\color{red}eight}$ sub-scenarios, which are combinations of ${\color{red}two}$ attack targets and ${\color{red}four}$ attack configurations.

**QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose.**

1. **${\color{red}Two}$ attack targets**: 
   - **a**: replaying a short-circuit fault happens in Fault_22bus1 to disrupt the power supply
   - **b**: replaying a short-circuit fault happens in Fault_22bus2 to disrupt the power supply
2. **${\color{red}Four}$ attack configurations**:
   - **9631**: modifying SV packets with all recorded measurements
   - **9632**: modifying SV packets with the first one-third recorded measurements
   - **9633**: modifying SV packets with all recorded measurements, while increasing the measurement values to 1.1 times
   - **9634**: modifying SV packets with the first quater recorded measurements, while increasing the measurement values to 1.2 times

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023-SV/blob/main/Datasets/PrimaryPlant.jpg" alt="" width="800" height="510" />
