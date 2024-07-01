## Scenario 911
In this scenario, the malicious program injects messages with counterfeit measurements to fake fault-free situations only when an over-current status occurs on the 66kV bus line (measurements exceed the pre-defined threshold). The malicious program stops injecting when the actual measurements are back to normal. The scenario contains a total of ${\color{red}four}$ sub-scenarios, which are combinations of ${\color{red}two}$ attack targets and ${\color{red}two}$ attack configurations.

**QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose.**

1. **${\color{red}Two}$ attack targets**: 
   - **a**: disabling the safety protection when a short-circuit fault happens in Fault_66bus1 
   - **b**: disabling the safety protection when a short-circuit fault happens in Fault_66bus2
2. **${\color{red}Two}$ attack configurations**:
   - **9111**: injecting packets with a fixed heartbeat of 50ms
   - **9112**: injecting packets with a fixed heartbeat of 25ms

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023-SV/blob/main/Datasets/PrimaryPlant.jpg" alt="" width="800" height="510" />
