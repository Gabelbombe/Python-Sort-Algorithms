#!/usr/local/bin/python

"""
File: runtime.py 
Prints the number of calls of a recursive Fibonacci function with problem sizes that double.
"""

from counter import Counter

def fib(n, counter):

	""" Count calls of the Fibonacci function """
	counter.increment()
	if n < 3:
		return 1
	else:
		return fib(n - 1, counter) + fib(n - 2, counter)

problemSize =2 
print("%12s%15s" % ("ProblemSize", "Calls"))
for count in range(5):

	counter = Counter()

	#Algorithm start
	fib(problemSize, counter)
	#Algorithm end

	print("%12d%15d" % (problemSize, counter))
	problemSize *= 2
