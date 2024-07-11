# Malicious behaviour:

Network level: the malicious program will delete the first 100 SV packets only when an over-current status occurs around Feeders (measurements exceed the pre-defined threshold).

Physical process level: if a short circuit happens around Feeders, Circuit breakers trip with a 5-second delay, and the safety protection is delayed for five seconds.

Three types of events happen successively, and the approximate SmpCnt (benign) ranges of each type are listed below:
- Fault-free (0-400, 1400-1800)
- Attacks (400-500, 1800-1900)
- Emergency (500-1200, 1900-2400)
- DMZ (1200-1400)