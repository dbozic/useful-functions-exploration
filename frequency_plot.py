def frequency_plot(data, group_column, count_column, figsize, color, xlabel, ylabel, title, 
                   textsize, xsize, ysize, 
                   xrotation, yrotation):
    """
    This function creates a sorted frequency plot using percentages
    across each category. It assumes that numpy as np and
    matplotlib.pyplot as plt have been imported. It is most useful
    for frequency plots across categorical variables. 
    
    INPUTS:
    
    data: dataframe to be loaded
    group_column: column of the data with categorical groups as a string, e.g. 'col1'
    count_column: column of the data that contains unique members to be counted, e.g. 'member_id'
    figsize: tuple that represents size of the figure, e.g. (15, 10)
    color: color of the barplot as string, e.g. 'red'
    xlabel: name of the x-axis as string, e.g. 'Days of the week'
    ylabel: name of the y-axixs as string, e.g. '% of members per day of the week'
    title: name of the plot as string, e.g. 'Frequency plot'
    textsize: integer used as fontsize for xlabel, ylabel, title, e.g. 15
    xsize: integer used as fontsize for x-axis, e.g. 15
    ysize: integer used as fontsize for y-axis, e.g. 15
    xrotation: integer used as angle of text rotation for x-axis, e.g. 70
    yrotation: integer used as angle of text rotation for y-axis, e.g. 0 (most common) 
    
    OUTPUT:
    
    a plt plot
    """
    # Length of the column to be plotted 
    column_len = len(data)
    
    # Calculate frequency per each member of the column
    frequency = data.groupby(group_column)[[count_column]].count().divide(column_len).multiply(100).round(decimals=1).sort_values(count_column, ascending=False)
    
    # Plot
    freq_plot = frequency.plot.bar(figsize = figsize, color = color, legend = False)
    freq_plot.set_title(title, size = textsize, weight = 'bold')
    freq_plot.set_xlabel(xlabel, size = textsize, weight = 'bold')
    freq_plot.set_ylabel(ylabel, size = textsize, weight = 'bold')
    plt.xticks(fontsize = xsize, rotation = xrotation)
    plt.yticks(fontsize = ysize, rotation = yrotation)
    plt.show()
