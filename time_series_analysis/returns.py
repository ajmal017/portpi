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

    
class Distributions(Returns):
    def __init__(self, close_dataframe):
        Returns.__init__(self, close_dataframe)
        self.returns_dataframe = self.simple_net_returns()
        self.calculate_distirbution_stats(self.returns_dataframe)


    def calculate_distirbution_stats(self, returns_dataframe):
        self.means = returns_dataframe.mean()
        self.stds = returns_dataframe.std()
        self.kurtosis = returns_dataframe.kurtosis()



    def __repr__(self):
        return 'means\n{}\nstandard deviations\n{}\nkurtosis\n{}'.format(self.means, self.stds, self.kurtosis)