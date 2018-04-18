import pandas as pd
import numpy as np

import input
import node 
import utils

FILENAME = './data/pc1.csv'

features, labels = input.read_csv( FILENAME )

utils.get_possible_splits( features, 'loc' )
