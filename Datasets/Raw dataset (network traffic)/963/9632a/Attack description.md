# Malicious behaviour:

Network level: When a true emergency (short-circuit) occurs on the 22kV bus line, the malicious program will start by recording all variations in measurements until the fault is isolated (the associated measurements drop to 0). In a future moment (e.g., 100 seconds after the true emergency occurs), the malicious program will modify a certain number of the original SV packets with **the first one-third** recorded measurements to replay an emergency (short-circuit) situation on the 22kV bus line.

Physical process level: Under fault-free operation, circuit breakers protecting the 22kV bus line are ALWAYS deceived into tripping (attacks ALWAYS impact the physical process), while the power supply is ALWAYS interrupted.

Four types of events happen successively, and the approximate SmpCnt (benign) ranges of each type are listed below:
- Fault-free (0-400, 1800-2400, 3200-3600)
- Attacks (2400-2420, 3600-3620)
- Emergency (400-1800, 2420-3000, 3620-4000)
- DMZ (3000-3200)