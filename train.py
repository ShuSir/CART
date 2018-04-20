import pandas as pd
import numpy as np

import input
from tree import tree

FILENAME = './data/pc1.csv'
stopping_sz = 20

df = input.read_csv( FILENAME )
decision_tree_classifier = tree( df, stopping_sz )

decision_tree_classifier.fit()
