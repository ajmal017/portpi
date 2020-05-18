import pandas as pd

class Returns:
    def __init__(self, close_dataframe):
        self.data = close_dataframe

    
    def simple_net_returns(self):
        '''Compute and return the daily return values.'''
        daily_returns = self.data.copy()
        daily_returns.iloc[1:] = (daily_returns / daily_returns.shift(1)) - 1
        daily_returns.iloc[0,:] = 0
        return daily_returns

    
    def compound_returns(self):
        '''Calculates the compound return over k_steps'''
        pass