## Scenario 924
In this scenario, the malicious program modifies the original SV packets with counterfeit measurements to fake fault-free situations only when an over-current status occurs around Feeders (measurements exceed the pre-defined threshold). The malicious program stops modifying after approximately 30 seconds. The scenario contains a total of ${\color{red}four}$ sub-scenarios, which are referred to ${\color{red}four}$ attack targets.

**QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose.**

1. **${\color{red}Four}$ attack targets**: 
   - **a**: disabling the safety protection when a short-circuit fault happens in Fault_FDR1
   - **b**: disabling the safety protection when a short-circuit fault happens in Fault_FDR2
   - **c**: disabling the safety protection when a short-circuit fault happens in Fault_FDR3
   - **d**: disabling the safety protection when a short-circuit fault happens in Fault_FDR4

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023-SV/blob/main/Datasets/PrimaryPlant.jpg" alt="" width="800" height="510" />
