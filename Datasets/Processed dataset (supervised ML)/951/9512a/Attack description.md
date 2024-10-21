# Malicious behaviour:

Network level: When a true emergency (short-circuit) occurs on the 66kV bus line, the malicious program will start by recording all variations in measurements until the fault is isolated (the associated measurements drop to 0). In a future moment (e.g., 100 seconds after the true emergency occurs), except for the benign publisher program, the malicious program will start again and inject SV packets (**25ms** heartbeat) with **all** recorded measurements to replay an emergency (short-circuit) situation on the 66kV bus line.

Physical process level: Under fault-free operation, circuit breakers protecting the 66kV bus line are ALWAYS decived into tripping (attacks ALWAYS impact the physical process), while the power supply is ALWAYS interrupted.

Four types of events happen successively, and the approximate SmpCnt (benign) ranges of each type are listed below:
- Fault-free (0-400, 1800-2400, 3200-3600)
- Attacks (2400-2430, 3600-3630)
- Emergency (400-1800, 2430-3000, 3630-4000)
- DMZ (3000-3200)