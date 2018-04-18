import pandas as pd
import sklearn
import numpy as np

def read_csv( filename ):
    # read csv file
    df = pd.read_csv( filename )
    
    # shuffle dataframe
    df = sklearn.utils.shuffle( df )
    df['defects'] = df['defects'].astype(int)

    return df

read_csv("./data/pc1.csv")

