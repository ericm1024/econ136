# rolldice.py  in PyGo\PyFTR
# This is the experimental model for integrating a stock distribution.
# Designed in Python 2.7.11 for Econ 136
# Dated March 1, 2017   Professor Gary R. Evans
#
import math
import numpy as np
import matplotlib.pyplot as plt
#
# Establish the testing values of our stock price (stp), strike price (strike), drift (alpha)
# and volatility (sigma). 
#
# stp = float(100.0)
# strike = float(105.0)
# Also try 100 and 105.
stp = float(80.0)
strike = float(84.0)
alpha = float(0.0)
sigma = float(0.10)
#
# Normally we would call our SN cumulative density function from our library, but it is written 
# here so others can see what we are doing. This will be used below.
# 
def csnd(point):
	return (1.0 + math.erf(point/math.sqrt(2.0)))/2.0
#
# Establish the array of Bin values as a series of multiples of standard deviations
#
# NOTE: Ask students for an easier way to populate this array with a counter.
#
# The centered-on-zero load array is appropriate, although the integer array helps check
# for bias and there is bias in this construction.
# The array's below were experimental, but I develeped a process for setting binsize quickly using linspace below.
# loadarray = [-4.5, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5]
# loadarray = [-5.0, -4.0, -3.0, -2.0, -1.0, 0.0, 1.0, 2.0, 3.0, 4.0, 5.0]
# loadarray = [-4.5, -4.0, -3.5, -3.0, -2.5, -2.0, -1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5]
# binborder = np.array(loadarray)
# Assuming symmetry, the binnumbers (num) will equal 2 X abs(deviation) X # of intervals plus 1 (4.5*2*2+1)= 19
binborder = np.linspace(-4.5, 4.5, num=19, dtype=float)
size = len(binborder)
# Temp test
print binborder, size, type(binborder)
#
# Given the stock price (stp) and sigma above, establish an array to associate a stock 
# value with each binborder.
#
binprice = np.zeros(size)
for i in range(0,size):
	binprice[i] = stp*math.exp(binborder[i]*sigma)
	
print "BinPrices:", binprice
# Establish an array of integrated probabilities (integrating from minus infinity to
# the SD mulitples). First set to zero and then make the calculations.
#
binedgeprob = np.zeros(size)
print "Size:", size
#
# Now populate the intergrated probabilities array with our calculated values.
#
print "Binborder and associated probabilities:"
for i in range(0,size):
	binedgeprob[i] = csnd(binborder[i])
	print binborder[i], binedgeprob[i]
#
print "Binborder array:"
print binedgeprob
# Now calculate the bin (spread) probabilities.
size = size - 1
binprob = np.zeros(size)
sum = 0
print "Bin spread probabilities and accumulating sums:"
for i in range(0,size):
	binprob[i] = binedgeprob[i+1] - binedgeprob[i]
	sum = sum + binprob[i]
	print binprob[i], sum
#
print "BinProb array:"
print binprob
sum = 0
sumbp = 0
# Now calculate a mid-price bin value for each bin, then multiply times the equivalent
# binprob, then check by summing.
binmidprice = np.zeros(size)
binvalue = np.zeros(size)
print "Midprice value, Bin Value, and sum."	
for i in range(0,size):
	binmidprice[i] = stp*math.exp(((binborder[i+1]+binborder[i])/2.0)*sigma)
	binvalue[i] = binmidprice[i]*binprob[i]
	sum = sum + binvalue[i]
	sumbp = sumbp + binprob[i]
	print 
	print "Range:", binborder[i], "to" , binborder[i+1]
	print "Binmidprice", binmidprice [i]
	print "Probability of being in this range: ", binprob[i]
	print "Sum of probabilities to here:", sumbp
	print "Binvalue:", binvalue[i]
	print "Sum to this point:", sum
#
#

