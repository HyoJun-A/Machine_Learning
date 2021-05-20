import numpy as np
import matplotlib.pyplot as plt

dogs = 1000
cats = 1000

dog_height = 35 + (5 * np.random.randn(dogs))
cat_height = 30 + (5 * np.random.randn(cats))

plt.xlabel('Height')
plt.ylabel('Number of Species')
plt.hist([dog_height, cat_height], label=['Dogs', 'Cats'], stacked=True, color=['r', 'y'])

plt.legend()
plt.show()