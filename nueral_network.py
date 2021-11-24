import tensorflow as tf

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd




from matplotlib import pyplot
series = pd.Series.from_csv('daily-total-female-births.csv', header=0)
print(series.head())
series.plot()
plt.show()