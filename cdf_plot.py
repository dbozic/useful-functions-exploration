def cdf(array, figsize, color, label, xlabel, ylabel, title, textsize, xsize, ysize, loc):
    """
    This function takes in an array and plots a cumulative distribution
    function-like plot, showing percentage of number of values in the array
    across the sorted values in the array, from lowest to highest. It assumes
    that numpy as np and matplotlib.pyplot as plt have been imported. 
    
    INPUT:
    
    array: array of values to be sorted and plotted
    figsize: tuple that denotes figure size, e.g. (10, 5)
    color: string that denotes the color of the plot, e.g. 'blue' or '#000000'
    label: string that denotes the label displayed in the legend, e.g. 'CDF of array'
    xlabel: string that denotes the x-axis label, e.g. 'Value in array'
    ylabel: string that denotes the y-axis label, e.g. '% of values'
    title: string that denotes the title of the plot, e.g. 'CDF of values in array'
    fontsize: int that denotes size of font used in the text on the plot, e.g. 12
    xsize: int that denotes size of font used on x-axis, e.g. 12
    ysize: int that denotes size of font used on y-axis, e.g. 12
    loc: string tha denotes the location of the legend, e.g. 'lower right'
    
    OUTPUT:
    
    a plt plot
    """
    fig, ax = plt.subplots(figsize=figsize)
    x = np.sort(array)
    y = np.array(range(len(array)))/float(len(array))*100 
    ax.plot(x, y, color = color, label = label) # plot the CDF
    ax.set_title(title, weight = 'bold', size = textsize)
    ax.set_xlabel(xlabel, weight = 'bold', size = textsize)
    ax.set_ylabel(ylabel, weight = 'bold', size = textsize)
    plt.xticks(fontsize = xsize)
    plt.yticks(fontsize = ysize)
    plt.legend(loc = loc)
