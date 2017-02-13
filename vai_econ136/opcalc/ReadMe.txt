February 8, 2017
Prepared for Econ 136
BSM-style options pricing calculators

This zip files includes the following files:

callidvex.py:  A Python 2 program for calculating a call's IDV. Robust

putidvex.py:  A Python 2 program for calculating a put's IDV. Robust

copm.py  A partially-disabled Python 2 program for calculating a call's   market price. Not thoroughly tested. 

[The student is expected to write popm.py for calculating a put's market price, using copm.py as a guide. Search the lecture notes for what signs must be flipped].

CDVunlocked.xlsx: An Excel program used to calculate call option price (same as copm.py). Robust BUT default values loaded must be overridden with new data because of how this program uses dates.

PDVunlocked.xlsx: An Excel program used to calculate put option price. Robust BUT default values loaded must be overridden with new data because of how this program uses dates.

Strangle IDV calculator: An Excel macro program using Visual Basic to calculate IDV for both a call and a put. This program is robust on Prof Evans's computer BUT default values must be overridden with new data. It is stongly recommended that this be replaced with a Python strangle program that merges callidvex.py with putidvex.py into a single program. This is provided mostly for reference. Also everything must be run in the same directory when using this.

Caution: Default solutions should not be trusted on the Excel programs. They are calculated by taking today's date and subtracting that from an expiration. An older version of the model will give you negative days to maturity (because the default expiration date has long since passed) and will calculate gibberish. 

THE TWO ROBUST PYTHON MODELS DO NOT ASK FOR DATA INPUT. The program must be opened with an editor and data provided where obviously needed. The resulting program will run well in BASH, terminal screen, or Spyder.