#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the cleaned data
data = pd.read_csv('data_cleaning.csv')  

# Performing data analysis tasks
# For example, calculate statistics and correlations
statistics = data.describe()
correlation_matrix = data.corr()

# Generate visualizations
plt.figure(figsize=(10, 6))
sns.histplot(data['Age'], bins=10, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.savefig('videos/age.png')
plt.close()

