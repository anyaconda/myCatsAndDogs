# META 2/27/2018
### ML Demo for Open House
# using my simulated dataset

from __future__ import division
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

### Step 1. Data Prep
# load data
data = pd.read_csv('data/myCatsAndDogs.csv')
data['label']=data['label'].astype('category')

# explore data
print(data.shape)
print(data.dtypes)
print(data.head())

# visualize the data.
x = data.food
y = data.sleep
#print(data['label'].cat.categories)
c = data.label #type series
colors = c.apply(lambda x: 'royalblue' if x=='cat' else 'springgreen')
edgecolors = c.apply(lambda x: 'b' if x=='cat' else 'g')


#ref matplotlib scatterplot https://matplotlib.org/gallery/shapes_and_collections/scatter.html#sphx-glr-gallery-shapes-and-collections-scatter-py
###plt.rcParams.update(pd.tools.plotting.mpl_stylesheet)
#ref scatter symbols https://matplotlib.org/gallery/lines_bars_and_markers/scatter_symbol.html#sphx-glr-gallery-lines-bars-and-markers-scatter-symbol-py
#ref markers https://matplotlib.org/api/markers_api.html

plt.figure(figsize=[6,6])
plt.scatter(x,y, c=colors, edgecolors=edgecolors, alpha=.9, marker='o', s=100)

plt.title("Cats and Dogs")
plt.xlabel("Food (in grams)")
plt.ylabel("Sleep (in hours)")
legend1 = plt.Line2D([0,0],[0,1], color='royalblue', marker='o', linestyle='', markersize=5)
legend2 = plt.Line2D([0,0],[0,1], color='springgreen', marker='o', linestyle='', markersize=5)
plt.legend([legend1,legend2], c.unique())
plt.show()

### not used
# c.astype('int16')
# plt.xlim(0,1000)
# didn't work markers = c.apply(lambda x: r'$Y$' if x=='cat' else r'$N$')