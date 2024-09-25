## Processed dataset
For each scenario/sub-scenario, the dataset contains the following three datasheets: 
1. **QUTZS_GOOSE.csv** extracts all GOOSE features of all GOOSE packets from the raw network traffic
2. **QUTZS_SV.csv** extracts all SV features of all SV packets from the raw network traffic
3. **QUTZS_final.xlsx** merges both GOOSE and SV features, and most importantly labels each row of features based on 39 types of behaviours. For every SV packet with APPID "0x4001", within 1.5 times of the SV heartbeat after the packet, the first available SV packet with APPID "0X4002" was appended. After that, according to the closest "packet arrival time", three GOOSE packets (APPIDs "0x3101", "0x3102" and "0x3103") were appended, respectively.

> The code snippet for generating QUTZS_final.xlsx is provided in **merge.py**.

> **metadata.xlsx** describes the metadata of each scenario/sub-scenario, including the number of GOOSE packets, SV packets, and samples with particular labels.