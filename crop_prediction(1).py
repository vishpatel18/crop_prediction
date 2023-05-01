# -*- coding: utf-8 -*-
"""Crop_prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19PQE51ayrAm5kULhXQF8vdoeTtcnkZw1
"""

import numpy as np # linear algebra
import pandas as pd

import os
for dirname, _, filenames in os.walk(''):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Commented out IPython magic to ensure Python compatibility.
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
warnings.simplefilter(action='ignore', category=UserWarning)
import seaborn as sns
import matplotlib.pyplot as plt
# %matplotlib inline

"""df=pd.read_csv('Crop_recommendation.csv')
df.head()
"""

df.describe()

#Exploratory Data Analysis
#Heatmap to check null/missing values

sns.heatmap(df.isnull(),cmap="coolwarm")
plt.show()

##Let's have a closer look at the distribution of temperature and ph.

plt.figure(figsize=(12,5))
plt.subplot(1, 2, 1)
# sns.distplot(df_setosa['sepal_length'],kde=True,color='green',bins=20,hist_kws={'alpha':0.3})
sns.distplot(df['temperature'],color="purple",bins=15,hist_kws={'alpha':0.2})
plt.subplot(1, 2, 2)
sns.distplot(df['ph'],color="green",bins=15,hist_kws={'alpha':0.2})

#Rain affects soil moisture which affects ph of the soil. Here are
# the crops which are likely to be planted during this season.

sns.jointplot(x="rainfall",y="humidity",data=df[(df['temperature']<30) & (df['rainfall']>120)],hue="label")

#We can see ph values are critical when it comes to soil. A stability between 6 and 7 is preffered

sns.boxplot(y='label',x='ph',data=df)

#Another interesting analysis where Phosphorous levels are quite differentiable when it rains heavily (above 150 mm)

sns.lineplot(data = df[(df['humidity']<65)], x = "K", y = "rainfall",hue="label")

#Let's visualize the import features which are taken into consideration by decision trees.

plt.figure(figsize=(10,4), dpi=80)
c_features = len(X_train.columns)
plt.barh(range(c_features), clf.feature_importances_)
plt.xlabel("Feature importance")
plt.ylabel("Feature name")
plt.yticks(np.arange(c_features), X_train.columns)
plt.show()