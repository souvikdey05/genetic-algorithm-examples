import argparse
from csv import reader
import os
from plot.line_plot import plot_line_chart
import sys
from PyQt5.QtWidgets import QApplication
from plot.window import Window

def read_csv(file):
    r"""Method to read a csv file"""
    file_data = []
    with open(file, 'r') as f:
        csv_reader = reader(f)
        header = next(csv_reader)
        # Check file as empty
        if header != None:
            # Iterate over each row after the header in the csv
            for row in csv_reader:
                # row variable is a list that represents a row in csv
                file_data.append(row)
    
    return file_data

def split_x_y(data):
    r"""Method to split the x and y axis"""
    x_data = []
    y_data = []

    for d in data:
        x_data.append(int(d[0]))
        y_data.append(float(d[1]))

    return x_data, y_data

def main() -> None:
    parser = argparse.ArgumentParser()

    parser.add_argument('--score-path', '-s', type=str, 
                        required=True, help='Path to score files for plotting.')

    parser.add_argument('--title', '-t', type=str, 
                        default='Runs Plot', help='Title of the plot.')

    options = parser.parse_args()
    
    score_path = options.score_path

    score_files = []
    for file in os.listdir(score_path):
        if file.endswith(".csv"):
            score_files.append(os.path.join(score_path, file))

    x_plot = []
    y_plot = []
    legend = []
    for idx, f in enumerate(score_files):
        file_data = read_csv(f)
        if file_data is not None and len(file_data) > 0:
            x, y = split_x_y(file_data)
            x_plot.append(x)
            y_plot.append(y)
            legend.append(f"Run {idx + 1}")
    
    x_label, y_label, title = "Generation #", "Best Fitness", ""
    fig = plot_line_chart(x_plot, y_plot, legend, x_label, y_label, title)

    # creating apyqt5 application
    # app = QApplication(sys.argv)
   
    # creating a window object
    # main = Window(fig)
       
    # showing the window
    # main.show()
   
    # loop
    # sys.exit(app.exec_())


if __name__ == "__main__":
    main()