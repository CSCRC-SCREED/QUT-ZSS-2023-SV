## Scenario 932
In this scenario, the malicious program injects SV packets with fake measurements to spoof an emergency (short-circuit) situation around Transformers. The malicious program starts from approximately the 15th second, the 60th second, and the 105th second, respectively. The scenario contains a total of ${\color{red}eight}$ sub-scenarios, which are combinations of ${\color{red}two}$ attack targets and ${\color{red}four}$ attack configurations.

**QUTZS.pcapng is the primary data, QUTZS_Redundant.pcapng is for redundancy purpose.**

1. **${\color{red}Two}$ attack targets**: 
   - **a**: spoofing a short-circuit fault happens in Fault_XFMR1 to disrupt the power supply
   - **b**: spoofing a short-circuit fault happens in Fault_XFMR2 to disrupt the power supply
2. **${\color{red}Four}$ attack configurations**:
   - **9321**: injecting 100 packets with a fixed heartbeat of 50ms (**a**: 66kV1=XFMR1W1=XFMR1W2=CB_XFMR1=F_XFMR1=2017 OR **b**: 66kV3=XFMR2W1=XFMR2W2=CB_XFMR2=F_XFMR2=2017)
   - **9322**: injecting 80 packets with a fixed heartbeat of 25ms (**a**: 66kV1=XFMR1W1=XFMR1W2=CB_XFMR1=F_XFMR1=2017 OR **b**: 66kV3=XFMR2W1=XFMR2W2=CB_XFMR2=F_XFMR2=2017)
   - **9323**: injecting 100 packets with a fixed heartbeat of 50ms (**a**: 66kV1=XFMR1W1=1000, XFMR1W2=1732, CB_XFMR1=0, F_XFMR1=3000 OR **b**: 66kV3=XFMR2W1=1000, XFMR2W2=1732, CB_XFMR2=0, F_XFMR2=3000)
   - **9324**: injecting 80 packets with a fixed heartbeat of 25ms (**a**: 66kV1=XFMR1W1=1000, XFMR1W2=1732, CB_XFMR1=0, F_XFMR1=3000 OR **b**: 66kV3=XFMR2W1=1000, XFMR2W2=1732, CB_XFMR2=0, F_XFMR2=3000)

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023-SV/blob/main/Datasets/PrimaryPlant.jpg" alt="" width="800" height="510" />