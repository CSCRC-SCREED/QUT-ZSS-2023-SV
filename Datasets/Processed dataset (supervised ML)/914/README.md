## Scenario 914
In this scenario, the malicious program injects messages with counterfeit measurements to fake fault-free situations only when an over-current status occurs around Feeders (measurements exceed the pre-defined threshold). The malicious program stops injecting when the actual measurements are back to normal. The scenario contains a total of ${\color{red}eight}$ sub-scenarios, which are combinations of ${\color{red}four}$ attack targets and ${\color{red}two}$ attack configurations.

**QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose.**

1. **${\color{red}Four}$ attack targets**: 
   - **a**: disabling the safety protection when a short-circuit fault happens in Fault_FDR1
   - **b**: disabling the safety protection when a short-circuit fault happens in Fault_FDR2
   - **c**: disabling the safety protection when a short-circuit fault happens in Fault_FDR3
   - **d**: disabling the safety protection when a short-circuit fault happens in Fault_FDR4
2. **${\color{red}Two}$ attack configurations**:
   - **9141**: injecting packets with a fixed heartbeat of 50ms
   - **9142**: injecting packets with a fixed heartbeat of 25ms

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023-SV/blob/main/Datasets/PrimaryPlant.jpg" alt="" width="800" height="510" />
