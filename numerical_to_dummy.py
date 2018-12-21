def numerical_to_dummy(data, columns, sign, reference):
    """Transforms a numerical variable into
    a dummy variable if a threshold is provided.
    Assumes operator has been imported. The logic is
    based on transforming the variable into "1" if the
    (in)equality holds true, otherwise turn into "0".
    
    For example: numerical_to_dummy(data, ['col1', 'col2'], '>', 50)
    would turn all components greater than 50 into a 1, and all others
    into a 0. 

    INPUT:

    data: dataframe of the data analyzed
    columns: list of columns as strings that need to be dummified, e.g. ['column1', 'column2']
    sign: logical operator as string, e.g.: '>' as greater than
    reference: an int or float that serves as threshold, e.g. 5 

    OUTPUT:

    data: dataframe with specified columns dummified
    """
    # We first define the operators that can be used 
    ops = {'>': operator.gt, '<': operator.lt, '>=': operator.ge, '<=': operator.le, '=': operator.eq}
    
    # And now we apply them
    for column in columns:
        data.update(data[column].apply(lambda x: 1 if ops[sign](x, reference) else 0))
    return data
