# Malicious behaviour:

Network level: the malicious program will modify a certain number of the original SV packets with fake measurements to spoof an emergency (short-circuit) situation around Feeders. The malicious program starts from approximately the 15th second, the 60th second, and the 105th second, respectively.

Physical process level: Under fault-free operation, circuit breakers protecting the Feeders are ALWAYS deceived into tripping (attacks ALWAYS impact the physical process), while the power supply is ALWAYS interrupted.

Four types of events happen successively, and the approximate SmpCnt (benign) ranges of each type are listed below:
- Fault-free (0-300, 602-1200, 1502-2100)
- Attacks (300-302, 1200-1202, 2100-2102)
- Emergency (302-402, 1202-1302, 2102-2400)
- DMZ (402-602, 1302-1502)