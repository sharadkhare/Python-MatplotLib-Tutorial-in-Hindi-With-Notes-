# Create labels for a plot

import matplotlib.pyplot as plt
import numpy as np
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)
plt.xlabel("Average oxygen")
plt.ylabel("our calorie")
plt.show()

# creating title for the plot.
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.plot(x, y)
plt.title("Health Monitor")
plt.xlabel("Average oxygen")
plt.ylabel("our calorie")
plt.show()

# now we will set the font property for title and labels via "fontdict"
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif', 'color':'blue', 'size':20}
font2 = {'family':'serif', 'color':'darkred', 'size':15}

plt.plot(x, y)
plt.title("Health Monitor", fontdict=font1)
plt.xlabel("Average oxygen", fontdict=font2)
plt.ylabel("our calorie", fontdict=font2)
plt.show()

# you can also change the location of title via "loc"
import matplotlib.pyplot as plt
import numpy as np
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

font1 = {'family':'serif', 'color':'blue', 'size':20}
font2 = {'family':'serif', 'color':'darkred', 'size':15}

plt.plot(x, y)
plt.title("Health Monitor", fontdict=font1, loc='left')
plt.xlabel("Average oxygen", fontdict=font2)
plt.ylabel("our calorie", fontdict=font2)
plt.show()