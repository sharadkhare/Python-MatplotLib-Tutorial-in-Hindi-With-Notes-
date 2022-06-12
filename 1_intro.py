import matplotlib
print(matplotlib.__version__)

# pyplot submodule
# Now we will draw a line in a diagram from a certain position.

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

