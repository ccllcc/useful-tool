# Change Boolean

def change_bol(x):
    """ This function transform a True value to False value"""
    if x == True:
        return False
    else:
        return True


# Outlier calculation

def outlier_cal(df,column):
    """This function takes dataframe and its column name as input, 
    output the outliers in the column, the column must be a numerical one,
    and it is dependant on Pandas"""
    Q1 = df[column].quantile(q=0.25)
    Q3 = df[column].quantile(q=0.75)
    IQR = Q3 - Q1
    max_v = Q3 + 1.5*IQR
    min_v = Q1 - 1.5*IQR
    return df[(df[column] > max_v)|(df[column] < min_v)]