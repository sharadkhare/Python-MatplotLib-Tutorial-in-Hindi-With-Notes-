# creating the pie chart.
# pie() function

import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()

# now we will label the pie chart
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apple", "Banana", "Cherry", "mango"]

plt.pie(y, labels=mylabels)
plt.show()

# startangle parameter - the default start angle is at the x axis but you can change the start angle by specifying startangle parameter.
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apple", "Banana", "Cherry", "mango"]

plt.pie(y, labels=mylabels, startangle=90)
plt.show()

# how to explode the pie chart by a value.

import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apple", "Banana", "Cherry", "mango"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels=mylabels,explode=myexplode)
plt.show()

# the shadow parameter for creativity
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apple", "Banana", "Cherry", "mango"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels=mylabels,explode=myexplode, shadow=True)
plt.show()

# you can also specify the color for each wedge.
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apple", "Banana", "Cherry", "mango"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels=mylabels, colors=mycolors)
plt.show()

# we can also add the legend - list of explaination
import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apple", "Banana", "Cherry", "mango"]

plt.pie(y, labels=mylabels)
plt.legend()
plt.show()

# now we will add legend with header

import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = ["Apple", "Banana", "Cherry", "mango"]

plt.pie(y, labels=mylabels)
plt.legend(title = "Fruits")
plt.show()