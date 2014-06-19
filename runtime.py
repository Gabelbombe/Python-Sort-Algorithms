#!/usr/local/bin/python

"""
File: runtime.py 
Prints the running time for problem sizes that double using a single loop
"""

import time

problemSize = 10000000
print("%12s%16s" % ("ProblemSize", "Seconds"))
for count in range(5):

    start = time.time()
    work = 1

    for j in range(problemSize):
        for k in range(problemSize):
            work += 1
            work -= 1

    elapsed = time.time() - start

    print("%12d%16.3f" % (problemSize, elapsed))
    problemSize *= 2
