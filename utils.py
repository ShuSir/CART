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
    return splits

def evaluate_split( df, attribute, split ):
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
    mask = df[attribute] <= split
    
    # split the dataset on the split attribute
    dfl = df[mask]
    dfr = df[~mask]
   
    # calculate weighting factors for child
    weighting_factor_left = float(dfl.shape[0])/df.shape[0]
    weighting_factor_right = float(dfr.shape[0])/df.shape[0]

    # calculate gini for left and right
    gini_left = gini_impurity(dfl)
    gini_right = gini_impurity(dfr)
    
    # calculate weighted gini for this split 
    weighted_gini = weighting_factor_left*gini_left + weighting_factor_right*gini_right
    return weighted_gini

def gini_impurity( df ):
    
    # compute positive samples and negative samples
    positive = float(len(df[df['defects'] == 1]))/df.shape[0]
    negative = 1.0 - positive
    
    gini_idx = (positive*positive) + (negative*negative)

    return gini_idx
