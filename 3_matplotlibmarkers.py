# you can use argument marker to emphasize each point with specified marker.

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o')
plt.show()

# format strings "fmt" - marker|line|color
from tkinter import Y
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, 'o:r')
plt.show()

# line refereance
# - solid line
# : dotted line
# -- dashed line
# -. dashline/dotted line

# color reference
# r red
# g green
# b blue
# c Cyan
# m magenta
# y yellow
# k black
# w white


# marker size - ms

import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

# marker edge color - mec
import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()

# Marker face color - mfc

import matplotlib.pyplot as plt
import numpy as np
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o', ms = 20, mec ='hotpink',  mfc = '#4CAF50')
plt.show()