This model differs from the original rolldice in a number of ways:

1.  The original model rolldice version 1 had a small cumulative error that was eliminated by
the addition of the lnmeanshift function to the calculation binmidprice. The origin of the
error and this solution are difficult to explain so will be explained in lecture.

2.  Variables and functions were added to allow for calculation of drift, duration volatility,
and the log spread of the stock and strike price (not yet used in the model).

3.  The original was laid out as a series of explainable steps. In this version the steps were
consolidated and made efficient.

4.  Many of the steps, like the sum counters in the original, were made more "Pythonic."

5.  The model still only calculates the full range of the lognormal density distribution. It is ready to be converted
a call option pricing model. (Students will do that).