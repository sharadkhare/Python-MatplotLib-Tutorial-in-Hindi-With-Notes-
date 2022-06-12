import matplotlib.pyplot as plt # now the pyplot package can be reffered as plt.
import numpy as np

# plotting x and y
# plot()function is used to draw points or markers in a diagram
# there are 2 parameters for specifying  points in the diagram i.e x-axis and y-axis.

xpoints = np.array([1, 8 ])
ypoints = np.array([3, 10])
plt.plot(xpoints, ypoints)
plt.show()

# the x-axis is the horizontal axis
# the y-axis is the verticl axis

#plotting without line
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8 ])
ypoints = np.array([3, 10])
plt.plot(xpoints, ypoints, 'o')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2, 6, 8 ])
ypoints = np.array([3,8, 1, 10])
plt.plot(xpoints, ypoints)
plt.show()

# Default X -Points
# if we do not specify the points in x axis then the default values 0, 1, 2, 3, 4....  will apply.
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)
plt.show()
