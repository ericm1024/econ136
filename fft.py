#!/usr/bin/env python
import sys
import numpy
import csv
from scipy import signal
import matplotlib.pyplot as plt

reader = csv.reader(open(sys.argv[1], 'r'))
data = []
dates = []
for line in reader:
    try:
        data.append(float(line[2]))
        dates.append(line[0] + " " + line[1])
    except Exception as e:
        pass

data = numpy.array(data)
fft = numpy.fft.fft(data)[1:]
fft = numpy.fft.fftshift(fft)
#plt.ylog()
plt.plot(range(len(fft)), fft)
plt.title("fft for " + sys.argv[1])

#f, t, Sxx = signal.spectrogram(data)
#plt.pcolormesh(t, f, Sxx)

plt.show()
