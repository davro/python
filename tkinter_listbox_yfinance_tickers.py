import tkinter as tk
from tkinter import ttk
import yfinance as yf

def get_tickers():
    # Replace 'YOUR_EXCHANGE' with the exchange you're interested in (e.g., 'NASDAQ', 'NYSE')
    tickers = ['^GSPC', '^DJI', '^IXIC', '^N225']
    return tickers

def on_listbox_select(event):
    selected_index = ticker_listbox.curselection()
    if selected_index:
        selected_ticker = ticker_listbox.get(selected_index)
        print(f"Selected Ticker: {selected_ticker}")

# Create the main Tkinter window
root = tk.Tk()
root.title("Ticker List")

# Get the list of tickers
tickers = get_tickers()

# Create a Listbox
ticker_listbox = tk.Listbox(root, selectmode=tk.SINGLE, height=len(tickers))
ticker_listbox.grid(row=0, column=0, padx=10, pady=10)

# Insert tickers into the Listbox
for ticker in tickers:
    ticker_listbox.insert(tk.END, ticker)

# Bind the Listbox to the function that will be called when an item is selected
ticker_listbox.bind("<ButtonRelease-1>", on_listbox_select)

# Start the Tkinter event loop
root.mainloop()

