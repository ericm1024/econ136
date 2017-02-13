import numpy
import scipy
import matplotlib.pyplot as plt

#This function does a monte carlo simulation for a stock
def singleRun(cur_val, alpha, beta, numSteps):
    val = [cur_val]*numSteps;
    for i in range(1, len(val)-1):
        val[i+1] = val[i]*numpy.exp(alpha+beta*numpy.random.normal())
    return val

def monteCarlo(cur_val, alpha, beta, numSteps, numSims):
    sims = [[cur_val for i in range(numSteps)] for y in range(numSims)]
    for i in range(0,numSims):
        sims[i] = singleRun(cur_val, alpha, beta, numSteps)
    return sims


res = monteCarlo(10, 0.001, 0.045, 100, 100)

# plot results
plt.plot(range(0, len(res[1])), zip(*res))
plt.show()
