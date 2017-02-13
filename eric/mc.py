#!/usr/bin/env python

from numpy.random import normal as rand_normal
from math import exp
import matplotlib.pyplot as plt

def mc_simulate(p0, mu, sigma, steps=100, simulations=5, trend_line=True):
    if trend_line:
        simulations = simulations + 1
    state = [[p0] * simulations]

    for i in range(1, steps):
        if trend_line:
            state.append([state[-1][0]*exp(mu)] +
                         map(lambda x: x*exp(mu + sigma*rand_normal()),
                             state[-1][1:]))
        else:
            state.append(map(lambda x: x*exp(mu + sigma*rand_normal()),
                             state[-1]))

    return state

if __name__ == "__main__":
    data = mc_simulate(10.0, 0.001, 0.045)
    
    plt.plot(range(0, len(data)), data)
    plt.xlabel("Days from start of simulation")
    plt.ylabel("Stock value of HMCIQ")
    plt.title("Monte Carlo Simulation of HMCIQ over "+str(len(data))+" days")
    plt.show()
