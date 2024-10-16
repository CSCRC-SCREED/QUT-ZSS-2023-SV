# Malicious behaviour:

Network level: Except for the benign publisher program, the malicious program will also be running and publishing **100** SV packets (**50ms** heartbeat) with fake measurements to spoof an emergency (short-circuit) situation around Feeders. The malicious program starts from approximately the 15th second, the 60th second, and the 105th second, respectively.

Physical process level: Under fault-free operation, circuit breakers protecting the Feeders are ALWAYS decived into tripping (attacks ALWAYS impact the physical process), while the power supply is ALWAYS interrupted.

Four types of events happen successively, and the approximate SmpCnt (benign) ranges of each type are listed below:
- Fault-free (0-300, 700-1200, 1600-2100)
- Attacks (300-400, 1200-1300, 2100-2200)
- Emergency (400-500, 1300-1400, 2200-2400)
- DMZ (500-700, 1400-1600)