# Malicious behaviour:

Network level: Except for the benign publisher program, the malicious program will also be running and publishing **80** SV packets (**25ms** heartbeat) with fake measurements to spoof an emergency (short-circuit) situation around Transformers. The malicious program starts from approximately the 15th second, the 60th second, and the 105th second, respectively.

Physical process level: Under fault-free operation, circuit breakers protecting the Transformers are ALWAYS decived into tripping (attacks ALWAYS impact the physical process), while the power supply is ALWAYS interrupted.

Four types of events happen successively, and the approximate SmpCnt (benign) ranges of each type are listed below:
- Fault-free (0-300, 640-1200, 1540-2100)
- Attacks (300-340, 1200-1240, 2100-2140)
- Emergency (340-440, 1240-1340, 2140-2400)
- DMZ (440-640, 1340-1540)