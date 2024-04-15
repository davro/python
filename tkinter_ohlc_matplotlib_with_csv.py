import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import csv
from matplotlib.dates import date2num
from datetime import datetime

class OHLCChartApp:
    def __init__(self, master, csv_file):
        self.master = master
        self.master.title("OHLC Chart")

        # Create a Matplotlib figure and axis
        self.fig = Figure(figsize=(8, 6), dpi=100)
        self.ax = self.fig.add_subplot(1, 1, 1)

        # Read OHLC data from CSV file
        ohlc_data = self.read_csv(csv_file)

        # Extracting data for plotting
        dates = [item[0] for item in ohlc_data]
        opens = [item[1] for item in ohlc_data]
        highs = [item[2] for item in ohlc_data]
        lows = [item[3] for item in ohlc_data]
        closes = [item[4] for item in ohlc_data]

        # Convert date strings to datetime objects
        dates = [datetime.strptime(date, '%Y-%m-%d') for date in dates]

        # Subsample data for better performance
        subsample_factor = 10
        dates = dates[::subsample_factor]
        opens = opens[::subsample_factor]
        highs = highs[::subsample_factor]
        lows = lows[::subsample_factor]
        closes = closes[::subsample_factor]

        # Plotting OHLC chart
        self.ax.plot_date(dates, closes, 'o-', label='Close')
        self.ax.vlines(dates, lows, highs, color='black', linewidth=2)
        self.ax.scatter(dates, opens, color='green', marker='^', label='Open')

        # Set labels and title
        self.ax.set_xlabel('Date')
        self.ax.set_ylabel('OHLC Values')
        self.ax.set_title('OHLC Chart')
        self.ax.legend()

        # Format the x-axis as dates
        self.fig.autofmt_xdate()

        # Create a Tkinter canvas to embed the Matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

    def read_csv(self, file_path):
        ohlc_data = []
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            next(csv_reader)  # Skip the header row if it exists
            for row in csv_reader:
                ohlc_data.append(row)
        return ohlc_data

def main():
    root = tk.Tk()
    #csv_file_path = 'path/to/your/csv_file.csv'  # Replace with your CSV file path
    csv_file_path = '/home/davro/workspace/data/csv/bitcoin-monthly.csv'  # Replace with your CSV file path
    app = OHLCChartApp(root, csv_file_path)
    root.mainloop()

if __name__ == "__main__":
    main()





