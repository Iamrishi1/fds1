# -*- coding: utf-8 -*-
"""Friend_ASsignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yWGkiIehhsvgRva_k4cm2faC5ZmbhU2H
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_excel('data0_-773141217.xlsx',header=None,names=['Weights'])

dataset['Weights'].describe()

data = dataset['Weights']

bins = np.arange(2.2, 4.8, 0.1)
n, bins = np.histogram(data, bins=bins, density=True)
W = np.mean(data)
X = np.percentile(data, 25)


plt.bar(bins[:-1], n, width=(max_weight-min_weight)/num_bins, alpha=0.75)

plt.xlabel('Newborn weight (grams)')
plt.ylabel('Frequency')
plt.title('Distribution of Newborn Weights')
plt.text(2.1, 0.95, f'Average weight W = {W:.2f} \nX = {X:.2f}  (75% above)', fontsize=10)

plt.axvline(x=X, color='r', linestyle='--', label=f'X = {X:.2f} grams')
plt.axvline(x=W, color='g', linestyle='--', label=f'W = {W:.2f} grams')


plt.show()

