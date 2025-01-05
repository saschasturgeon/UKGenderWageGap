def fitline(filepath):
    if filepath.endswith(".csv"):
        data = pd.read_csv(r"filepath")
        x = data[0]
        y = data[1]
        plt.plot(x,y)
        slope, intercept = np.polyfit(x,y,1)
        plt.plot(x, slope*x+intercept, color = 'red')
        return(slope,intercept)
    else:
        return("Please enter the correct file type and try again")