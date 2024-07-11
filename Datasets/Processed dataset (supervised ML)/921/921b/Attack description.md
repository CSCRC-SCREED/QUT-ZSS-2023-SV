# Malicious behaviour:

Network level: the malicious program will modify the original SV packets with counterfeit measurements to fake fault-free situations only when an over-current status occurs on the 66kV bus line (measurements exceed the pre-defined threshold). The malicious program stops modifying after approximately 30 seconds.

Physical process level: if a short circuit happens on the 66kV bus line, Circuit breakers NEVER trip and the safety protection ALWAYS failed (attacks ALWAYS impact the physical process).

Three types of events happen successively, and the approximate SmpCnt (benign) ranges of each type are listed below:
- Fault-free (0-400, 1000-1200, 1400-1800)
- Attacks (400-1000, 1800-2400)
- DMZ (1200-1400)