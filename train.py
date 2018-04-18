import pandas as pd
import numpy as np

import input
import node 
import utils

FILENAME = './data/pc1.csv'

df = input.read_csv( FILENAME )

splits = utils.get_possible_splits( df , 'loc' )
print splits
utils.evaluate_split( df, 'loc' , splits[5] )
utils.gini_impurity(df)
