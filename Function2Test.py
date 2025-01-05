import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def fitline(filepath):
    if filepath.endswith(".csv"):
        data = pd.read_csv(filepath)
        x = data.iloc[:,0]
        y = data.iloc[:,1]
        plt.scatter(x,y)
        slope, intercept = np.polyfit(x,y,1)
        plt.plot(x, slope*x+intercept, color = 'red')
        return(slope,intercept)
    else:
        return("Please enter the correct file type and try again")