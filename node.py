
class node:
    
    def __init__(self, df, parent, splitting_criterion):
        self.parent = parent 
        self.df = df
        self.splitting_criterion = splitting_criterion
    
    
    def _is_leaf( self, stopping_sz ):
        if self.df.shape[0] <= stopping_sz:
            return True
        else:
            return False

    def find_splitting_criterion( self ):
        
        for attribute in list(self.df):
            splits = get_possible_splits( self.df, attribute )

            for split in splits:
                gini_value = evaluate_gini_value( self.df, attribute, split )

        pass

