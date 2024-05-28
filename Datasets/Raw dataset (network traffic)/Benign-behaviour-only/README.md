## Benign-behaviour-only
In sharp contrast to the mixed behaviours in Scenarios 911-974, 11 additional benign-behaviour-only scenarios were generated. These 11 scenarios include one pure fault-free scenario and ten emergency scenarios. The details of each scenario are listed below:
-  **0** : No unusual events happen. As shown in Figure 1, the 66kV high voltage line transmits power loads from two power sources. Transformer 1 receives power loads only from Source 1, and distributes power loads to Feeder 1 and Feeder 2 via a 22kV low-voltage line. Similarly, Transformer 2 receives power from Source 2, and distributes it to Feeder 3 and Feeder 4. The two transformers work in parallel without any interference. Except for CB2_66KV and CB2_22KV, which are opened, all the other eight circuit breakers are closed.
- **101**: When a short-circuit fault occurs on Fault_66bus1, associated protection mechanism acts (open CB1_66KV, CB2_66KV and CB_XFMR1; close CB2_22KV) immediately and isolates the fault effectively.
- **102**: When a short-circuit fault occurs on Fault_66bus2, associated protection mechanism acts (open CB2_66KV, CB3_66KV and CB_XFMR2; close CB2_22KV) immediately and isolates the fault effectively.
- **103**: When a short-circuit fault occurs on Fault_XFMR1, associated protection mechanism acts (open CB1_66KV, CB2_66KV and CB_XFMR1; close CB2_22KV) immediately and isolates the fault effectively. 
- **104**: When a short-circuit fault occurs on Fault_XFMR2, associated protection mechanism acts (open CB2_66KV, CB3_66KV and CB_XFMR2; close CB2_22KV) immediately and isolates the fault effectively. 
- **105**: When a short-circuit fault occurs on Fault_22bus1, associated protection mechanism acts (open CB1_22KV) immediately and isolates the fault effectively. 
- **106**: When a short-circuit fault occurs on Fault_22bus2, associated protection mechanism acts (open CB3_22KV) immediately and isolates the fault effectively.
- **107**: When a short-circuit fault occurs on Fault_FDR1, associated protection mechanism acts (open CB_FDR1) immediately and isolates the fault effectively. 
- **108**: When a short-circuit fault occurs on Fault_FDR2, associated protection mechanism acts (open CB_FDR2) immediately and isolates the fault effectively.
- **109**: When a short-circuit fault occurs on Fault_FDR3, associated protection mechanism acts (open CB_FDR3) immediately and isolates the fault effectively.
- **110**: When a short-circuit fault occurs on Fault_FDR4, associated protection mechanism acts (open CB_FDR4) immediately and isolates the fault effectively.

> The labelling of 101-110 start when the fault happens, and stops when systems start to recover (the fault was eliminated).

<img src="https://github.com/CSCRC-SCREED/QUT-ZSS-2023-SV/blob/main/Datasets/PrimaryPlant.jpg" alt="" width="800" height="510" />

*Figure 1. The primary plant simulation in MATLAB.*