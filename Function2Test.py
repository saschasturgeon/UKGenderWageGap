import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def fitline(filepath):
    if filepath.endswith(".csv"):  #if statement checks if the file type is a csv
        data = pd.read_csv(filepath)
        x = data.iloc[:,0]
        y = data.iloc[:,1] # data is read from the file into a dataframe and then split into two arrays
        plt.scatter(x,y) # plotted as a scatter
        slope, intercept = np.polyfit(x,y,1)
        plt.plot(x, slope*x+intercept, color = 'red') #the slope and intercepts are calculated and then plotted on the same axis
        return(slope,intercept) # slipe and intercept are returned by the function
    else:
        return("Please enter the correct file type and try again") # message returned if file type is not a csv