import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data2 = pd.read_csv(r'gender-wage-gap-UK.csv')
x = data2.iloc[:,0]
y = data2.iloc[:,1]  # reads the data into a dataframe and then splits it into two arrays
ax = plt.axes()
ax.set_facecolor("lightgrey")
plt.scatter(x,y)  #  plots the data as a scatter graph on a light grey background
slope, intercept = np.polyfit(x,y,1)
plt.plot(x, slope*x+intercept, color = 'red')  # calculates the slope and intercepts for a straight line then plots onto the same axes
plt.title('Gender Wage Gap in the UK over time')
plt.xlabel('Year')
plt.ylabel('How much less women were payed (%)')  # title and axes labels are added to complete the graph
data1 = pd.read_csv(r'female-labor-force-participation-UK.csv')
x = data1.iloc[:,0]
y = data1.iloc[:,1]  # reads the data into a dataframe and then splits it into two arrays
ax = plt.axes()
ax.set_facecolor("lightgrey")  #  plots the data as a scatter graph on a light grey background
plt.scatter(x,y)
slope, intercept = np.polyfit(x,y,1)
plt.plot(x, slope*x+intercept, color = 'red')  # calculates the slope and intercepts for a straight line then plots onto the same axes
plt.title('Percentage of Women in the UK Workforce over time')
plt.xlabel('Year')
plt.ylabel('Percentage of women 15+ in the workforce (%)') # title and axes labels are added to complete the graph