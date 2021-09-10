import matplotlib.pyplot as plt

def plot_line_chart(x, y, legend, x_label, y_label, title):
    r"""Method to plot line chart"""
    if isinstance(y, list):
        if not isinstance(x, list):
            raise TypeError("If y is list, then x should also be list")

        if not isinstance(legend, list):
            raise TypeError("If y is list, then legend should also be list")
        
        if len(y) != len(x):
            raise TypeError("Both x and y should be of the same length")

        if len(y) != len(legend):
            raise TypeError("Both legend and y should be of the same length")

    if isinstance(y, list):
        num_of_plots = len(y)
    else:
        num_of_plots = 1
        y = [y]
        x = [x]

    fig, ax = plt.subplots(figsize=(20, 5))

    for p in range(num_of_plots):
        ax.plot(x[p], y[p])

    ax.set_title(title)
    ax.legend(legend)
    ax.xaxis.set_label_text(x_label)
    ax.yaxis.set_label_text(y_label)

    fig.savefig("fig.jpg")
    return fig
    # plt.show()
