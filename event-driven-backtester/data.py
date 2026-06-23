# Import libraries
import pandas as pd
from event import MarketEvent
import queue

# Historic data handler
class HistoricCSVDataHandler:
    def __init__(self, events, csv_dir, symbol_list):
        self.events = events
        self.csv_dir = csv_dir
        self.symbol_list = symbol_list
        self.symbol_data = {}
        self.latest_symbol_data = {s: [] for s in symbol_list}
        self.continue_backtest = True
        self.open_convert_csv_files()

    def open_convert_csv_files(self):
        for s in self.symbol_list:
            df = pd.read_csv(
                f"{self.csv_dir}/{s}.csv",
                header=0,
                skiprows=[1, 2],
                index_col=0,
                parse_dates=True,
            ).sort_index()
            df.columns = ['Open', 'High', 'Low', 'Close', 'Volume']
            df = df.astype(float)
            self.symbol_data[s] = df.iterrows()

    def _get_new_bar(self, symbol):
        for b in self.symbol_data[symbol]:
            yield b

    def get_latest_bars(self, symbol, N=1):
        return self.latest_symbol_data[symbol][-N:]

    def update_bars(self):
        for s in self.symbol_list:
            try:
                bar = next(self._get_new_bar(s))
            except StopIteration:
                self.continue_backtest = False
            else:
                if bar is not None:
                    self.latest_symbol_data[s].append(bar)
        self.events.put(MarketEvent())