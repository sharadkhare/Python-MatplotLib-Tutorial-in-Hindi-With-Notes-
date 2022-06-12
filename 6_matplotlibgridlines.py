# adding the grid lines to a plot via "grid()"
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif', 'color':'blue', 'size':20}
font2 = {'family':'serif', 'color':'darkred', 'size':15}

plt.title("Health Monitor", fontdict=font1)
plt.xlabel("Average oxygen", fontdict=font2)
plt.ylabel("our calorie", fontdict=font2)
plt.plot(x, y)
plt.grid()

plt.show()

# now we will specify which grid lines to display via x axis or y axis. (legal values are x and y and both default value is both)
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif', 'color':'blue', 'size':20}
font2 = {'family':'serif', 'color':'darkred', 'size':15}

plt.title("Health Monitor", fontdict=font1)
plt.xlabel("Average oxygen", fontdict=font2)
plt.ylabel("our calorie", fontdict=font2)
plt.plot(x, y)
plt.grid(axis='x')

plt.show()

# setting up the line properties fro the grid
from turtle import color
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif', 'color':'blue', 'size':20}
font2 = {'family':'serif', 'color':'darkred', 'size':15}

plt.title("Health Monitor", fontdict=font1)
plt.xlabel("Average oxygen", fontdict=font2)
plt.ylabel("our calorie", fontdict=font2)
plt.plot(x, y)
plt.grid(color = 'green', linestyle = "--", linewidth = 0.5)

plt.show()


