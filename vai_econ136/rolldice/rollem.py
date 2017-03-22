import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

bas = (1.0/36.0)
poss = np.linspace(2.0, 12.0, num=11, dtype=float)
print "Dice outcome:"
print poss
print "Check dice 2 to 7:"
print poss[0:6]
print "Check dice 8 to 12:"
print poss[6:12]
#odds = np.zeros(11)
# print odds[3]
odds = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0]
probs = np.array(odds)
probs = probs*bas
print "Probability array:"
print probs
probtot = np.sum(probs)
print "Prob total:", probtot
money = poss*probs
print "Bin values:",
print money
total = np.sum(money)
print "Total value of bet:", total
print "Bottom to 7:"
print(money[0:6])
bottom = np.sum(money[0:6])
print "Value of 2 to 7:", bottom
print "8 to 12:"
print(money[6:12])
upper = np.sum(probs[6:12])
print "Sum of 8 to 12 probs:", upper
top = np.sum(money[6:12])
print "Value of 8 to 12:", top
index=np.arange(money)
plt.bar(index, money)


