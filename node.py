import utils

class node:
    
    def __init__(self, df, parent):
        self.parent = parent 
        self.df = df
        
        # tree nodes left and right 
        self.left = None
        self.right = None
        
        # splitting criterion 
        self.splitting_attribute = None
        self.threshold = 0

    def set_splitting_criteria( self, attribute, threshold ):
        self.splitting_attribute = attribute
        self.threshold = threshold
    

    def is_leaf( self, stopping_sz ):
        if len(self.df) <= stopping_sz:
            return True
        else:
            return False

    def find_splitting_criterion( self ):
        
        min_score = 2.0

        best_attribute = None
        threshold = 0.0

        # consider for all attributes except label
        for attribute in list(self.df)[:-1]:
            splits = utils.get_possible_splits( self.df, attribute )
            
            for split in splits:
                split_score = utils.evaluate_split( self.df, attribute, split )
                if split_score < min_score:
                    split_score = min_score
                    best_attribute = attribute
                    threshold = split
        
        return min_score, best_attribute, threshold
        
    def split( self, attribute, threshold ):
        mask = self.df[attribute] <= threshold

        dfl = self.df[mask]
        dfr = self.df[~mask]
        
        print "Splitting in {} and {}".format(dfl.shape[0], dfr.shape[0])

        left = node( dfl , self )
        right = node( dfr , self )

        return left, right
