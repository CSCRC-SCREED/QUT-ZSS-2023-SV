# Malicious behaviour:

Network level: When a true emergency (short-circuit) occurs around Transformers, the malicious program will start by recording all variations in measurements until the fault is isolated (the associated measurements drop to 0). In a future moment (e.g., 100 seconds after the true emergency occurs), the malicious program will modify a certain number of the original SV packets with **all** recorded measurements (**while increasing the measurement values to 1.2 times**) to replay an emergency (short-circuit) situation around Transformers.

Physical process level: Under fault-free operation, circuit breakers protecting the Transformers are ALWAYS deceived into tripping (attacks ALWAYS impact the physical process), while the power supply is ALWAYS interrupted.

Four types of events happen successively, and the approximate SmpCnt (benign) ranges of each type are listed below:
- Fault-free (0-400, 1200-2400, 3000-3400, 4200-5400)
- Attacks (2400-2560, 5400-5560)
- Emergency (400-1200, 2560-2800, 3400-4200, 5560-5800)
- DMZ (2800-3000)