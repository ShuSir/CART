import pandas as pd
import sklearn
import numpy as np

def read_csv( filename ):
    # read csv file
    df = pd.read_csv( filename )
    
    # shuffle dataframe
    df = sklearn.utils.shuffle( df )

    # extract features and labels 
    features = df.loc[:,'loc' : 'branchCount']
    labels = df['defects'].map({True : 1, False:0})

    return features, labels

read_csv('./data/pc1.csv')
