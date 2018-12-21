# Samle standard deviation function

def sample_std(series):
    """
    The function returns the standard deviation of the sample based on the formula:
    s = sqrt(s2) where s2 is sample variance and where
    s2 = sum(data_point - sample_mean)^2 / (n-1)
    
    INPUT:
    
    series: data series on which to calculate sample standard deviation
    
    OUTPUT:
    
    sample_std: sample standard deviation
    """
    sample_std = np.sqrt(np.sum(np.power(series - series.mean(),2)) / (series.size-1))
    return sample_std

# Marginal error function

def marginal_error(series, alpha, sample_std):
    """
    This function returns the marginal error in the confidence interval based on the formula:
    interval = t*standard_error where
    standard_error = sample_std / sqrt(sample_size) and where
    t-statistic is calculated through the ppf method with (1 - alfa/2) signifying the portions of tails to cut.
    
    INPUT:
    
    series: data series on which to calculate the interval
    alpha: confidence level (usually 0.1, 0.05, 0.01)
    sample_std: sample standard deviation calculated through the sample_std function.
    
    OUTPUT:
    
    marginal_error: range of the interval expressed as the marginal error
    """
    marginal_error = t.ppf(1.0 - (alpha / 2.0), series.size-1) * (sample_std / np.sqrt(series.size))
    return round(marginal_error, 1)

# Mean point estimate and confidence interval

def confidence_interval(mean, marginal_error):
    """
    This function returns a tuple that contains:
    (lower end of the confidence interval, the mean, upper end of the confidence interval) at the desired confidence level. 
    
    INPUT:
    
    mean: mean point estimate of the data series
    marginal_error: marginal error calculated through the marginal_error function
    
    OUTPUT:
    
    CI: tuple that contains the point estimate as well as the lower- and upper-limit of the interval.
    """
    CI = (mean - marginal_error, mean, mean + marginal_error)
    return CI
