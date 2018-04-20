import pandas as pd
import numpy as np

import input
import utils
from tree import tree

FILENAME = './data/pc1.csv'
stopping_sz = 20

df = input.read_csv( FILENAME )
decision_tree_classifier = tree( df, stopping_sz )
decision_tree_classifier.fit()

# mask = df["branchCount"] <= 207.0
#
# dfl = df[mask]
# dfr = df[~mask]
#
# gini_left = utils.gini_impurity( dfl )
# gini_right = utils.gini_impurity( dfr )
#
# print "gini left : {} , gini right : {}".format(gini_left, gini_right)

# print len(dfl)
