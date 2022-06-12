# Histogram -  a histrogram is a graph showing the frequency distribution.
# example - say you ask for the height of 250 people then how we will make a histogram.
# hist() function
import numpy as np
x = np.random.normal(170, 10, 250)
print(x)

# the hist() function will read the array and produce the histogram.
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show()