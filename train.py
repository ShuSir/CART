import pandas as pd
import numpy as np

import input
import utils
from tree import tree

FILENAME = './data/pc1.csv'
stopping_sz = 200

df = input.read_csv( FILENAME )

# split into training and testing
df_train = df.iloc[:1000 , :]
df_test = df.iloc[1001: , :]

print "Train shape : " , df_train.shape
print "Test shape : " , df_test.shape


decision_tree_classifier = tree( df, stopping_sz )
decision_tree_classifier.fit()


for idx, sample in df_test.iterrows():
    prediction = decision_tree_classifier.predict( sample )
    print prediction
