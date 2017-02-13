import math
# This is a Py version 2.7.9 file originally written and tested in Py3.4 
# This file show how to use the Py2 error function to calculate the
# cumulative probability density function for both the standard normal
# and normal distribution.
#
# Version date: January 25, 2017
# Prof Evans
# I am an old Fortran programmer. I initialize everything and I don't care
# what you think about it.
#
	sigma = float(0.0)
	alpha = float(0.0)
	val = float(0.0)
	x = float(0.)
# Calculate a standard normal (alpha zero, sigma 1) at value 1 SD:
# CSND integrates a standard normal distribution up to some sigma.
#
	def csnd(point):
		return (1.0 + math.erf(point/math.sqrt(2.0)))/2.0
#
	sigma = 0.5
	x = csnd(sigma)
	print
	print "In the standard normal distribution, the cumulative"
	print "probability at ",sigma, "standard deviations equals", "%.5f" % x, "."
	print
	print
#
# Calculate a normal at some alpha and sigma.
# CND integrates a Gaussian distribution up to some value.
#
	def cnd(point):
		return (1.0 + math.erf((point - alpha)/(sigma*math.sqrt(2.0))))/2.0
#
	alpha = 40
	sigma = 1.5
	val = 42
	x = cnd(val)
	print "When the mean is", "%.3f" % alpha, "and the sigma is", "%.3f" % sigma, "and when"
	print "our point is", "%.3f" % val, "the cumulative probability is", "%.5f" % x, "."
