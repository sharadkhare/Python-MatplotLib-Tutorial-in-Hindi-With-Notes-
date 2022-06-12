# linestyle or ls - is used to change the style of the plotted line
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linestyle = 'dotted')
plt.show()

# line color - c
from turtle import color
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, color = '#4CAF50')
plt.show()

# line width - lw .. width of a line
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, linewidth = '20.5' )
plt.show()

# example for multiple line
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([3, 8, 1, 10])
ypoints = np.array([6, 2, 7, 11])
plt.plot(xpoints)
plt.plot(ypoints)
plt.show()