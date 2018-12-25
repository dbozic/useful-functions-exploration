def pie_chart(figsize, sizes, colors, labels, explode, autopct, fontsize, legendsize, startangle):
    """
    This function makes a pie chart based on previously-calculated percentages.
    Assumes that matplotlib.pyplot has been imported as plt. 
    
    INPUTS:
    
    figsize: a tuple that represents figure size, e.g. (10,5)
    sizes: a list that represent percentages, e.g. [30, 30, 40]
    colors: a list of strings that will correspond as colors respectively, e.g. ['red', 'orange', 'green']
    labels: a list of strings that will correspond as legend respectively, e.g. ['NY', 'SF', 'LA']
    explode: a list of float that determine whether a portion of a pie will pop out, with 0s not doing so, e.g. [0.1, 0, 0]
    autopct: a string that denotes whether the number shown will have decimal points, e.g. '%1.0f%%' being an integer
    fontsize: an integer representing the size of font inside each pie slice, e.g. 19
    legendsize: an integer representing the size of the text in the legend, e.g. 19
    startangle: an integer that orients the pie, e.g. 0 or 90. 
    
    OUTPUT:
    
    a plt plot 
    """
    
    # Figure definition
    fig, ax = plt.subplots(figsize = figsize)
    
    # Pie plot
    plt.pie(sizes, autopct = autopct, colors = colors, explode = explode, startangle = startangle, 
           textprops = {'fontsize': fontsize}, shadow = True)
    plt.legend(labels, fontsize = legendsize)
    plt.axis('equal')
    plt.tight_layout()
    plt.show()
