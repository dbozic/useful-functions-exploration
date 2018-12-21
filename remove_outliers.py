def remove_outliers(data, series):   
    """
    This function removes outliers in the series
    by deleting all points outside 2*sigma from the mean.
    
    INPUTS

    data: dataframe to be pruned
    series: series/column based on which outliers will be removed
    
    OUTPUTS
    
    data_filtered: new dataframe with removed outliers across all series
    """
    mean = np.mean(series)
    stdev = np.std(series)
    data_filtered = data[(series > mean - 2*stdev) & (series < mean + 2*stdev)]
    return data_filtered
