# scatter - the scatter() function plots one dot for each observation.

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

plt.scatter(x,y)
plt.show()

# now we will compare 2 plots on same figure
import matplotlib.pyplot as plt
import numpy as np

#day 1, the age and speed of 13 cars:
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
plt.scatter(x,y)

# day 2, the age and speed of 
x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
y = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112,91, 80, 85])
plt.scatter(x,y)

plt.show()

# now we will set our own color of the markers:
import matplotlib.pyplot as plt
import numpy as np

#day 1, the age and speed of 13 cars:
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
plt.scatter(x,y, color = 'hotpink')

# day 2, the age and speed of 
x = np.array([2, 2, 8, 1, 15, 8, 12, 9, 7, 3, 11, 4, 7, 14, 12])
y = np.array([100, 105, 84, 105, 90, 99, 90, 95, 94, 100, 79, 112,91, 80, 85])
plt.scatter(x,y, color = 'green')

plt.show()

# now you can also change the color of each dots
import matplotlib.pyplot as plt
import numpy as np

#day 1, the age and speed of 13 cars:
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
colors = (["red", "green", "blue", "yellow", "pink", "black", "orange", "purple", "brown", "beige", "gray", "cyan", "magenta"])
plt.scatter(x,y, c = colors)

plt.show()

# Now we will create a color array, and specify a colormap in scatter plot
import matplotlib.pyplot as plt
import numpy as np

#day 1, the age and speed of 13 cars:
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x,y, c = colors, cmap= 'viridis')


plt.show()

# you can also include colorbar in the plot
import matplotlib.pyplot as plt
import numpy as np

#day 1, the age and speed of 13 cars:
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])
colors = np.array([0, 10, 20, 30, 40, 45, 50, 55, 60, 70, 80, 90, 100])

plt.scatter(x,y, c = colors, cmap= 'viridis')
plt.colorbar()


plt.show()

# you can also change the size

import matplotlib.pyplot as plt
import numpy as np

#day 1, the age and speed of 13 cars:
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 60, 90, 10, 300, 600, 800])
plt.scatter(x,y, s = sizes)


plt.show()

# alpha- you can adjust the tranparency of the dots

import matplotlib.pyplot as plt
import numpy as np

#day 1, the age and speed of 13 cars:
x = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

sizes = np.array([20, 50, 100, 200, 500, 1000, 60, 60, 90, 10, 300, 600, 800])
plt.scatter(x,y, s = sizes, alpha=0.5)

plt.show()

# now we will combine color, size and alpha
import matplotlib.pyplot as plt
import numpy as np
x  = np.random.randint(100, size= (100))
y = np.random.randint(100, size=(100))
colors = np.random.randint(100, size= (100))
sizes = 10 * np.random.randint(100, size=(100))
plt.scatter(x,y, c=colors, s=sizes, alpha=0.5, cmap='nipy_spectral')
plt.colorbar()
plt.show()
