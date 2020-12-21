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


# Normalizer & Standardizer Class

class Normalizer_Standardizer():
    """ The normalizer class receives a dataframe as its only input for initialization,
    then the class generates a list of parameters, which is stored in a list {self.params}"""

    def __init__(self,dataframe):
        self.params = []
        for i in list(dataframe.columns):
            max_v = dataframe[i].max()
            min_v = dataframe[i].min()
            mean_v = dataframe[i].mean()
            std_v = dataframe[i].std()
            self.params.append([min_v,max_v,mean_v,std_v])


    def normalize_data(self,x):
        """ The function receives a data point as an input and then outputs the normalized version. """

        normalized = []
        for i,j in enumerate(x):
            normalized_v = (j-self.params[i][0])/(self.params[i][1]-self.params[i][0])
            normalized.append(normalized_v)
        return normalized

    def standardize_data(self,x):
        """ The function receives a data point as an input and then outputs the standardized version. """

        standardized = []
        for i,j in enumerate(x):
            standardized_v = (j - self.params[i][2]) / self.params[i][3]
            standardized.append(standardized_v)
        return standardized