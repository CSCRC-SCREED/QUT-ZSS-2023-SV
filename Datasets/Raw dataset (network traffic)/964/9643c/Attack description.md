# Malicious behaviour:

Network level: Except the Benign publisher program, the malicious program will be also running and publishing SV packets (50ms heartbeat) with counterfeit measurements to fake fault-free situations only when an over-current status occurs around Transformers (a measurement exceed the pre-defined threshold). The malicious program stops injecting when the measurement is back to normal.

Physical process level: if a short circuit happens around Transformers, Circuit breakers STILL trip and the safety protection is STILL functional.

Four types of events happen successively, and the approximate SmpCnt (benign) ranges of each type are listed below:
- Fault-free (0-400, 1400-1800)
- Attacks (400-500, 1800-1900)
- Emergency (500-1200, 1900-2400)
- DMZ (1200-1400)