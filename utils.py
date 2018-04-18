import pandas as pd

def get_possible_splits( df , attribute ):
    """ 
    helper to return all possible splits 
    
    this function returns all the possible splits
    on the given attribute on the provided dataframe 

    Parameters:
        df : dataframe to be split
        attribute : attribute to be split on

    Returns:
        splits: list of all possible splits 
    """
    ds = df.loc[:,attribute]

    # First sort the values 
    ds = ds.sort_values().drop_duplicates()
    
    # Compute averages of consecutive values 
    ds = ds.rolling(2).sum().divide(2)
    splits = ds[1:].tolist()
    
    # return the possible splits 
    print splits


def evaluate_gini_value ( df, attribute, split ):
    """
    helper function to evaluate gini value for the split

    This function gives Gini Value for the split generated 
    by 'split' on 'attribute' in the given dataframe

    Parameters:
        df : dataframe to evaluate gini index on
        attribute : attribute to split on 
        split : value of the attribute 

    Returns:
        gini_value : the gini index for split 
    """




