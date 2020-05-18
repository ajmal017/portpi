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

    
class Distributions():

    def __init__(self, data):
        self.returns_dataframe = data
        self.means, self.stds, self.kurtosis = Distributions.calculate_distirbution_stats(self.returns_dataframe)


    def calculate_distirbution_stats(data):
        '''Calculates the mean, standard deviation and kurtosis of the input dataframe
        
        Args
        ----
        data : pandas.DataFrame
            dataframe which the mean, standard deviation and kurtosis will be calculated on

        Returns
        -------
        means : pandas.Series
            Means of individual columns in data
        stds : pandas.Series
            Standard deviation of individual columns in data
        kurtosis : pandas.Series
            Kurtosis of individual columns in data
        '''

        means = data.mean()
        stds = data.std()
        kurtosis = data.kurtosis()
        return means, stds, kurtosis


    def __repr__(self):
        return 'means\n{}\nstandard deviations\n{}\nkurtosis\n{}'.format(self.means, self.stds, self.kurtosis)