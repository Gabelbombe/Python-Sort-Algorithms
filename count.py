#!/usr/local/bin/python

"""
File: runtime.py 
Prints the number of iterations for problem sizes that double, using nested a loop
"""

problemSize = 100
print("%12s%15s" % ("ProblemSize", "Iterations"))
for count in range(5):

    number = 0
    work = 1

    # Algorithm start
    for j in range(problemSize):
        for k in range(problemSize):
            number += 1
            work += 1
            work -= 1
    # Algorithm end

    print("%12d%15d" % (problemSize, number))
    problemSize *= 2    