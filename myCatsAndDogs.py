# META 2/27/2018
### ML Demo for Open House
# using my simulated dataset

from __future__ import division
import matplotlib.pyplot as plt
from matplotlib.text import TextPath
import numpy as np
import pandas as pd


### Step 1. Data Prep
# load data
data = pd.read_csv('data/myCatsAndDogs.csv') #'data/Iris_modified.csv'
data['label']=data['label'].astype('category')

# explore data
print(data.shape)
print(data.dtypes)
print(data.head())

# visualize the data
x = data.food
y = data.sleep
groups = data.groupby('label')
colors = ['crimson', 'mediumblue']

#plot
#src https://stackoverflow.com/questions/21654635/scatter-plots-in-pandas-pyplot-how-to-plot-by-category
#plt.figure(figsize=[8,8])
i = 0
fig, ax = plt.subplots()
for name, group in groups:
    letter = group.isCat.unique()
    letter = letter[0]
    ax.scatter(group.food, group.sleep, c=colors[i],  marker=TextPath((0, 0), letter), s = 400, alpha =.8, label = name)
    i+=1
##ax.legend()
plt.title("Cat?")
plt.xlabel("Food (in grams)")
plt.ylabel("Sleep (in hours)")
plt.show()


### Step 2. Train
X = data[['food','sleep']]
y = data['label']
#x_train, Y_train =
sample = [[600,22.0]]

# 2a. SVM Model
from sklearn import svm
clf1 = svm.SVC()
clf1.fit(X,y)
y_hat1 = clf1.predict(sample)
print ("predict1", y_hat1 )

# 2b. Tree Model
from sklearn import tree
from sklearn.tree import export_graphviz

clf2 = tree.DecisionTreeClassifier()
clf2 = clf2.fit(X, y)
y_hat2 = clf2.predict(sample)
print ("predict2", y_hat2)

#graphviz
classes = data.label.unique()
features = X.columns
#create decision tree
dot_data = tree.export_graphviz(clf2, out_file='vis/cats_tree.dot', class_names=classes, feature_names=features, filled=True, rounded=True) #, class_names=c.unique()

#src http://scikit-learn.org/stable/modules/tree.html
# todo
# import graphviz
# graph = graphviz.Source(dot_data)
# graph

# # converting into the pdf file from CLI
# #dot -Tpdf file_name.dot -o file_name.pdf
# import os
# export_graphviz(clf,  filled=True, rounded=True) #feature_names=iris.feature_names,
# os.system('dot -Tpng vis\cats_tree.dot -o vis\cats_tree.png')
# os.system('dot -Tpdf vis\cats_tree.dot -o vis\cats_tree.pdf')

