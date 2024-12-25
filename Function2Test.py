def isnumber(x):
    try:
        int(x)
        if(x<0):
            return("Negative")
        elif(x>0):
            return("Positive")
        else:
            return("Neither")
    except ValueError:
        return("Not a number")

