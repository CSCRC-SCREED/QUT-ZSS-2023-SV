# Malicious behaviour:

Network level: When a true emergency (short-circuit) occurs around Transformers, the malicious program will start by recording all variations in measurements until the fault is isolated (the associated measurements drop to 0). In a future moment (e.g., 100 seconds after the true emergency occurs), the malicious program will modify **40** original SV packets with **the first 40** recorded measurements (**while increasing the measurement values to 1.5 times**) to replay an emergency (short-circuit) situation around Transformers.

Physical process level: Under fault-free operation, circuit breakers protecting the Transformers are ALWAYS deceived into tripping (attacks ALWAYS impact the physical process), while the power supply is ALWAYS interrupted.

Four types of events happen successively, and the approximate SmpCnt (benign) ranges of each type are listed below:
- Fault-free (0-400, 1200-2400, 3000-3400, 4200-5400)
- Attacks (2400-2440, 5400-5440)
- Emergency (400-1200, 2440-2800, 3400-4200, 5440-5800)
- DMZ (2800-3000)