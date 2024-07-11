# Malicious behaviour:

Network level: the malicious program will modify a certain number of the original SV packets with fake measurements to spoof an emergency (short-circuit) situation around Feeders. The malicious program starts from approximately the 15th second, the 60th second, and the 105th second, respectively.

Physical process level: Under fault-free operation, circuit breakers protecting the Feeders are ALWAYS deceived into tripping (attacks ALWAYS impact the physical process), while the power supply is ALWAYS interrupted.

Four types of events happen successively, and the approximate SmpCnt (benign) ranges of each type are listed below:
- Fault-free (0-300, 620-1200, 1520-2100)
- Attacks (300-320, 1200-1220, 2100-2120)
- Emergency (320-420, 1220-1320, 2120-2400)
- DMZ (420-620, 1320-1520)