def column_unique_values(data, exclusions):
    """
    This function goes through each column of a dataframe
    and prints how many unique values are in that column.
    It will also show what those unique values are. The
    function is particularly useful in exploratory data
    analysis for quick understanding of column content 
    within the dataframe. Assumes that pandas has
    been imported.
    
    INPUTS:
    
    data: dataframe to be analyzed. 
    exclusions: a list of columns as strings to be excluded, e.g. exclusions = ['column1', 'column2']
                If no exclusions, then input 'exclusions = []'.
    
    OUTPUT:
    
    print statements
    """
    
    # First, we select only those columns that are implicitly included
    selection = data.drop(exclusions, axis = 1)
    
    # Then we parse through every column of the dataframe
    for column in selection.columns.values:
        print('Column {x} has {y} unique values.').format(x = column, y = len(data[column].unique()))
        print('')
        print('Those unique values are:')
        print('')
        print(data[column].unique())
        print('')
        print('- - - - - - - - - - - - - - - - - -')
        print('')
