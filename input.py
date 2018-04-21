import pandas as pd
import sklearn
import numpy as np

def read_csv( filename ):
    # read csv file
    df = pd.read_csv( filename , header=None)
    
    # shuffle dataframe
    df = sklearn.utils.shuffle( df )

    return df


