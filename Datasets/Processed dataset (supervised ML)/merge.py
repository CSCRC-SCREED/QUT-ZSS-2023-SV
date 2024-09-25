import pandas as pd

# read files into DataFrame
GOOSEcsv = pd.read_csv('QUTZS_GOOSE.csv')
SVcsv = pd.read_csv('QUTZS_SV.csv')

# Convert DataFrame to list
SVcsv = SVcsv.values.tolist()

number_sv = len(SVcsv) # Total number of the SV packets
sv_index = 0 # the index of the key SV packets (to find SV 0x4001)
search_index = 0 # the index of the searching SV packets (to find SV 0x4002)
matched_target_b = False # A flag indicating if a matched target (SV 0x4002) have been found
merged = [] # The merged dataset
SV_APPID_a = '0x4001'
SV_APPID_b = '0x4002'
searching_range = 0.075 # searching range is 1.5 times of the normal heartbeat (50ms in simulation) = 0.075 seconds


while sv_index < number_sv:
    # for SV packets with APPID_a
    if SVcsv[sv_index][3] == SV_APPID_a:
        # Search from the next SV packet
        search_index = sv_index + 1
        # Check-point: Exit if the search index exceeds the maximum range
        if search_index >= number_sv:
            break
        # for any packets within the time of the searching_range
        ###
        ### For example, [a1 a2 a3 b1 b2 b3 b4 a4 b5] where time(b5) - time(a1) < searching_range
        ### Final outcome should be [a1 a2 a3 b1 b2 b3 b4 a4 b5] -> [a1b1], [a2b1], [a3b1], [a3b2], [a3b3], [a3b4], [a4b5]
        ###
        while SVcsv[search_index][0] - SVcsv[sv_index][0] < searching_range:
            # if the SV packet is APPID_b
            if SVcsv[search_index][3] == SV_APPID_b:
                # if no matched target SV_APPID_b has been found
                if matched_target_b == False:
                    # Append the SV packet with APPID_b after the SV packet with APPID_a, and save it to the merged data list
                    ###
                    ### For example, [a1 a2 a3 b1] --> [a1b1]
                    ### For example, [a2 a3 b1] --> [a2b1]
                    ### For example, [a3 b1] --> [a3b1]
                    ### For example, [a4 b5] --> [a4b5]
                    ###
                    merged.append(SVcsv[sv_index])
                    merged[len(merged)-1] = merged[len(merged)-1] + SVcsv[search_index]
                    matched_target_b = True
                    ## Debug
                    ## print(f'found target consisting of 0x4001 (row {sv_index+2}) and 0x4002 (row {search_index+2})')
                    # Continue searching from the next packet
                    search_index = search_index + 1
                    # Check-point: Exit if the search index exceeds the maximum range, otherwise jump to the next iteration
                    if search_index >= number_sv:
                        break
                    else:
                        continue
                # if at least one matched target SV_APPID_b has been found
                elif matched_target_b == True:
                    # if there is another SV_APPID_a between a SV_APPID_a and a matched SV_APPID_b
                    ###
                    ### For example, [a1 a2 a3 b1 b2, where a2 is between a1 and b1,
                    ### For example, [a2 a3 b1 b2, where a3 is between a2 and b1
                    ###
                    if SVcsv[sv_index + 1][3] == SV_APPID_a:
                        # Reset the flag to accept new matching, exit the second layer of while-loop
                        matched_target_b = False
                        break
                    # Otherwise, no SV_APPID_a in the middle
                    ###
                    ### For example, [a3 b1 b2 b3 b4]
                    ###
                    elif SVcsv[sv_index + 1][3] == SV_APPID_b:
                        # Append the SV packet with APPID_b after the SV packet with APPID_a, and save it to the merged data list
                        ###
                        ### For example, [a3 b1 b2] --> [a3b2]
                        ### For example, [a3 b1 b2 b3] --> [a3b3]
                        ### For example, [a3 b1 b2 b3 b4] --> [a3b4]
                        ###
                        merged.append(SVcsv[sv_index])
                        merged[len(merged)-1] = merged[len(merged)-1] + SVcsv[search_index]
                        matched_target_b = True
                        ## Debug
                        ## print(f'found target consisting of 0x4001 (row {sv_index+2}) and 0x4002 (row {search_index+2})')
                        # Continue searching from the next packet
                        search_index = search_index + 1
                        # Check-point: Exit if the search index exceeds the maximum range, otherwise jump to the next iteration
                        if search_index >= number_sv:
                            break
                        else:
                            continue
                    else:
                         raise RuntimeError('Unknown APPID when MATCHED SV_APPID_b has been found')
                else:
                    raise RuntimeError('matched_target_b must be a Boolean')
            # if the SV packet is APPID_a
            elif SVcsv[search_index][3] == SV_APPID_a:
                # if no matched target SV_APPID_b has been found
                if matched_target_b == False:
                    ###
                    ### For example, [a1 a2
                    ### For example, [a2 a3
                    ###
                    # Continue searching from the next packet
                    search_index = search_index + 1
                    # Check-point: Exit if the search index exceeds the maximum range, otherwise jump to the next iteration
                    if search_index >= number_sv:
                        break
                    else:
                        continue
                # if at least one matched target SV_APPID_b has been found
                elif matched_target_b == True:
                    ###
                    ### For example, [a3 b1 b2 b3 b4 a4
                    ###
                    # Reset the flag to accept new matching, exit the second layer of while-loop
                    matched_target_b = False
                    break
            else:
                raise RuntimeError('Unknown APPID when NO matched SV_APPID_b has been found')
        # After finishing the second layer of while-loop, and continue finding SV_APPID_a from the next packet
        sv_index = sv_index + 1
    elif SVcsv[sv_index][3] == SV_APPID_b:
        # If the next packet is SV_APPID_b, directly skip to the next packet
        sv_index = sv_index + 1
    else:
        raise RuntimeError('Unknown APPID when finding a SV_APPID_a')

# Convert list to DataFrame, specify column names
final = pd.DataFrame(merged)
final.columns= ["pkt arrival time", "MACsrc_sv1", "MACdst_sv1", "APPID_sv1", "SVlength_sv1", "noASDU_sv1", \
                "svID1_sv1", "smpCnt1_sv1", "Data1_sv1", "svID2_sv1", "smpCnt2_sv1", "Data2_sv1", "svID3_sv1", "smpCnt3_sv1", "Data3_sv1", \
                "svID4_sv1", "smpCnt4_sv1", "Data4_sv1", "svID5_sv1", "smpCnt5_sv1", "Data5_sv1", "svID6_sv1", "smpCnt6_sv1", "Data6_sv1", \
                "svID7_sv1", "smpCnt7_sv1", "Data7_sv1", "svID8_sv1", "smpCnt8_sv1", "Data8_sv1", "svID9_sv1", "smpCnt9_sv1", "Data9_sv1", \
                "svID10_sv1", "smpCnt10_sv1", "Data10_sv1", "svID11_sv1", "smpCnt11_sv1", "Data11_sv1", "svID12_sv1", "smpCnt12_sv1", "Data12_sv1",
                "svID13_sv1", "smpCnt13_sv1", "Data13_sv1",\
                "pkt arrival time_sv2", "MACsrc_sv2", "MACdst_sv2", "APPID_sv2", "SVlength_sv2", "noASDU_sv2", \
                "svID1_sv2", "smpCnt1_sv2", "Data1_sv2", "svID2_sv2", "smpCnt2_sv2", "Data2_sv2", "svID3_sv2", "smpCnt3_sv2", "Data3_sv2", \
                "svID4_sv2", "smpCnt4_sv2", "Data4_sv2", "svID5_sv2", "smpCnt5_sv2", "Data5_sv2", "svID6_sv2", "smpCnt6_sv2", "Data6_sv2", \
                "svID7_sv2", "smpCnt7_sv2", "Data7_sv2", "svID8_sv2", "smpCnt8_sv2", "Data8_sv2", "svID9_sv2", "smpCnt9_sv2", "Data9_sv2", \
                "svID10_sv2", "smpCnt10_sv2", "Data10_sv2", "svID11_sv2", "smpCnt11_sv2", "Data11_sv2", "svID12_sv2", "smpCnt12_sv2", "Data12_sv2",
                "svID13_sv2", "smpCnt13_sv2", "Data13_sv2"]

# Merge GOOSE into final datasheet
GOOSE3101 = GOOSEcsv[GOOSEcsv['APPID'] == '0x3101']
GOOSE3102 = GOOSEcsv[GOOSEcsv['APPID'] == '0x3102']
GOOSE3103 = GOOSEcsv[GOOSEcsv['APPID'] == '0x3103']

final = pd.merge_asof(final, GOOSE3101, on='pkt arrival time', direction='nearest')
final = pd.merge_asof(final, GOOSE3102, on='pkt arrival time', suffixes=('_GOOSE1',''), direction='nearest')
final = pd.merge_asof(final, GOOSE3103, on='pkt arrival time', suffixes=('_GOOSE2','_GOOSE3'), direction='nearest')

# Rename one column name, and save to .xlsx file.
final = final.rename(columns={"pkt arrival time": "pkt arrival time_sv1"})
final.to_excel("QUTZS_final.xlsx")
