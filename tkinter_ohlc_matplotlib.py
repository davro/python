import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class OHLCChartApp:
    def __init__(self, master):
        self.master = master
        self.master.title("OHLC Chart")

        # Create a Matplotlib figure and axis
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(1, 1, 1)

        # Sample OHLC data (replace this with your actual data)
        ohlc_data = [
            (1, 20, 10, 15),
            (2, 25, 18, 22),
            (3, 22, 12, 20),
            # Add more data points as needed
        ]

        # Extracting data for plotting
        indices = [item[0] for item in ohlc_data]
        opens = [item[1] for item in ohlc_data]
        highs = [item[2] for item in ohlc_data]
        lows = [item[3] for item in ohlc_data]
        closes = [item[1] for item in ohlc_data]

        # Plotting OHLC chart
        self.ax.plot(indices, closes, 'o-', label='Close')
        self.ax.vlines(indices, lows, highs, color='black', linewidth=2)
        self.ax.scatter(indices, opens, color='green', marker='^', label='Open')

        # Set labels and title
        self.ax.set_xlabel('Index')
        self.ax.set_ylabel('OHLC Values')
        self.ax.set_title('OHLC Chart')
        self.ax.legend()

        # Create a Tkinter canvas to embed the Matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def main():
    root = tk.Tk()
    app = OHLCChartApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

