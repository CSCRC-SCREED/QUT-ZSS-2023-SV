import pandas as pd

GOOSEcsv = pd.read_csv('QUTZS_GOOSE.csv')
SVcsv = pd.read_csv('QUTZS_SV.csv')
SV4001 = SVcsv[SVcsv['APPID'] == '0x4001']
SV4002 = SVcsv[SVcsv['APPID'] == '0x4002']


##ColumnSize = size(Data,2);
##NoTarget = 0;
##PreTarIndex = 0;
##i = 2;
##skip_i = 0;
##while i <= size(Data,1)
##    if Data{i,4} == 1 % for every message with APPID = 1, index = i
##        j = i+1; % search from the next msg
##        if j > size(Data,1) % Avoid exceed the max range
##            break
##        end
##        while Data{j,1} - Data{i,1} < 0.125 % search range within next 125 ms
##            if (Data{j,4} == 2) && (NoTarget == 0) % APPID = 2 and the first target (12)
##                for k = 1:ColumnSize % copy values from msg j after msg i
##                    Data(i,ColumnSize+k) = Data(j,k);                  
##                end
##                PreTarIndex=j;
##                j=j+1;
##                NoTarget=NoTarget+1;
##                if j > size(Data,1) % Avoid exceed the max range
##                    break
##                end
##                if skip_i == 1 % if 1112 happens, then quit while, and re-start from the second 1
##                    break
##                end
##            elseif (Data{j,4} == 2) && (NoTarget > 0) %  APPID = 2 and NOT the first target (1222)
##                for k = 1:ColumnSize % copy values from msg i to msg (previous target), then copy values from msgj after msg (previous target)
##                    Data(PreTarIndex,k) = Data(i,k);
##                    Data(PreTarIndex,ColumnSize+k) = Data(j,k);                  
##                end
##                PreTarIndex=j;
##                j=j+1;
##                NoTarget=NoTarget+1;
##            elseif (Data{j,4} == 1) && (NoTarget == 0) % APPID = 1 and NOT find any target, continue search the next (1112)
##                j=j+1;
##                skip_i = 1;
##            elseif (Data{j,4} == 1) && (NoTarget > 0) % APPID = 1 and find at least one target,stop while to pair the next APPID 1 (12221)
##                skip_i = 0;
##                break                
##            end       
##        end
##        NoTarget = 0;
##        if skip_i == 1 % if already skip number of i, then back to i+1 (1112221)
##            i=i+1;
##            skip_i =0;
##        elseif skip_i == 0 % if not skip any i, then go to the 1 after the last 2 (122221)
##            i=j;
##        end
##    else
##        i=i+1;
##    end
##end

temp = pd.merge_asof(GOOSEcsv, SV4001, on='pkt arrival time', suffixes=('_goose','_sv1'), direction='nearest')
final = pd.merge_asof(temp, SV4002, on='pkt arrival time', suffixes=('_sv1','_sv2'), direction='nearest')
final = final.rename(columns={"MACsrc": "MACsrc_sv2", "MACdst": "MACdst_sv2", "APPID": "APPID_sv2"})
final.to_excel("QUTZS_final.xlsx")
