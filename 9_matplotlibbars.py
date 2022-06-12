# Now in this section we will create Vertical Bars bar()
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y)
plt.show()

# Now we will create a Horizontal bar
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.barh(x,y)
plt.show()

# color of the bar() and barh()
# https://matplotlib.org/stable/gallery/color/named_colors.html
# https://htmlcolorcodes.com/
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y, color="red")
plt.show()

# how we can change the bar width

import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.bar(x,y, width=0.5)
plt.show()

# for hoiziontal bar you have to use height instead of width
import matplotlib.pyplot as plt
import numpy as np
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])
plt.barh(x,y, height=0.5)
plt.show()







