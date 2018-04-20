from node import node 
import utils

class tree:

    def __init__( self, df, stopping_sz ):

        self.root = None
        self.df = df
        self.stopping_sz = stopping_sz
    
    def __build_tree( self, root ):
        
        if root.is_leaf(self.stopping_sz):
            return

        max_score, best_attribute, threshold = root.find_splitting_criterion()
        print "Splitting dataset on attribute {}, with threshold {}".format(best_attribute, threshold)

        root.set_splitting_criteria( best_attribute, threshold )

        left, right = root.split( best_attribute, threshold )
        root.left = left
        root.right = right 
        
        self.__build_tree(root.left)
        self.__build_tree(root.right)

    def fit( self ):
        
        if self.root == None:
            self.root = node( self.df, None )
            self.__build_tree(self.root)


