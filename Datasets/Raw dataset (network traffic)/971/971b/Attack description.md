# Malicious behaviour:

Network level: the malicious program will delete the first 100 SV packets only when an over-current status occurs on the 66kV bus line (measurements exceed the pre-defined threshold).

Physical process level: if a short circuit happens on the 66kV bus line, Circuit breakers trip with a 5-second delay, and the safety protection is delayed for five seconds.

Three types of events happen successively, and the approximate SmpCnt (benign) ranges of each type are listed below:
- Fault-free (0-400, 2200-2600)
- Attacks (400-500, 2600-2700)
- Emergency (500-2000, 2700-3200)
- DMZ (2000-2200)