## Scenario 952
In this scenario,  when a true emergency (short-circuit) occurs around Transformers, the malicious program starts by recording all variations in measurements until the fault is isolated (the associated measurements drop to 0). In a future moment (e.g., 100 seconds after the true emergency occurs), except for the benign publisher program, the malicious program starts again and injects SV packets with the recorded measurements to replay an emergency (short-circuit) situation around Transformers. The scenario contains a total of ${\color{red}six}$ sub-scenarios, which are combinations of ${\color{red}two}$ attack targets and ${\color{red}three}$ attack configurations.

**QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose.**

1. **${\color{red}Two}$ attack targets**: 
   - **a**: replaying a short-circuit fault happens in Fault_XFMR1 to disrupt the power supply
   - **b**: replaying a short-circuit fault happens in Fault_XFMR2 to disrupt the power supply
2. **${\color{red}Three}$ attack configurations**:
   - **9521**: injecting SV packets with all recorded measurements at a 50ms heartbeat
   - **9522**: injecting SV packets with all recorded measurements at a 25ms heartbeat
   - **9523**: injecting SV packets with the first half recorded measurements at a 25ms heartbeat

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023-SV/blob/main/Datasets/PrimaryPlant.jpg" alt="" width="800" height="510" />