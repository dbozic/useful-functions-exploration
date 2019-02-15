def funnel_drop(values, drops, gates, figsize, linestyle, marker, markersize, color, ylabel, title, textsize, xsize, ysize, label, loc, legsize):
    """
    This function takes in a series that contains counts or percentages of members
    and plots a 2D plot that represents a funnel drop. The function assumes
    that pandas has been imported and that numbers are prepared either as whole
    numbers, decimals, or percentages. 
    
    INPUT:
    
    values: pandas series of values that represent values of members at each gate
    drops: a list that represents what numbers should be displayed on the y-axis and in which intervals, e.g. [0, 20, 40, 60, 80, 100]
    gates; a list that represents the gates in the funnel, e.g. ['invite', 'confirmation']
    figsize: tuple that denotes figure size, e.g. (10, 5)
    linestyle: string that denotes the style of line, e.g. '--'
    marker: string that denotes type of marker at each gate on the linechart, e.g. 'o'
    markersize: integer that denotes the size of the marker, e.g. 10
    color: string that denotes the color of the plot, e.g. 'blue' or '#000000'
    ylabel: string that denotes the y-axis label, e.g. '% of values'
    title: string that denotes the title of the plot, e.g. 'CDF of values in array'
    textsize: int that denotes size of font used in the text on the plot, e.g. 12
    xsize: int that denotes size of font used on x-axis, e.g. 12
    ysize: int that denotes size of font used on y-axis, e.g. 12
    label: string that denotes the label displayed in the legend, e.g. 'CDF of array'
    loc: string tha denotes the location of the legend, e.g. 'lower right'
    legsize: integer that represents the size of the legend, e.g. 12
    
    OUTPUT:
    
    a plt plot
    """
    fig, ax = plt.subplots(figsize = figsize)
    values.plot(linestyle = linestyle, marker = marker, markersize = markersize, label = label, color = color)
    # remove top and right lines
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    # groom the x-tick parameters
    ax.tick_params(axis = 'x', which = 'minor', pad = 30)
    plt.title(title, weight = 'bold', fontsize = textsize)
    plt.ylabel(ylabel, weight = 'bold', fontsize = textsize)
    plt.yticks(drops, fontsize = ysize)
    plt.xticks(np.arange(len(gates)), gates, fontsize = xsize)
    plt.legend(loc = loc, prop = {'size': legsize})
    plt.show()
