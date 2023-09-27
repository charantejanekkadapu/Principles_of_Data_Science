#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries for analysis and visualization
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned dataset
data = pd.read_csv("data_cleaning.csv")

# Calculate correlations and create visualizations
correlation_matrix = data.corr()

# Example: Create a heatmap to visualize correlations
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.savefig("videos/CorrelationHeatmap.png")
plt.show()

