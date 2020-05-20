import pandas as pd

class Returns:
    '''Class capable of processing returns data calculated from asset close prices.'''

    def __init__(self, close_dataframe):
        '''Creates a Returns object capable of processing asset close data.
        
        Args
        ----
        close_dataframe : pandas.DataFrame
            Dataframe where the asset close values are stored
        '''

        self.data = close_dataframe

    
    def simple_net_returns(self):
        '''Compute daily returns from the close data stored in self.
        
        Returns
        -------
        daily_returns : pandas.DataFrame
            Daily returns data stored in a dataframe
        '''

        daily_returns = self.data.copy()
        daily_returns.iloc[1:] = (daily_returns / daily_returns.shift(1)) - 1
        daily_returns.iloc[0,:] = 0
        return daily_returns

    
class Distributions():
    '''Class for working with normal distributions.'''

    def __init__(self, data):
        '''Creates distribution object and calculates the mean, standard deviation and kurtosis of the distribution.
        These parameters can be accessed from the means, stds and kurtosis properties.

        Args
        ----
        data : pandas.DataFrame
            Data which the distribution parameters will be calculated on
        '''

        self.data = data
        self.means, self.stds, self.kurtosis = Distributions.calculate_distirbution_stats(self.data)


    def calculate_distirbution_stats(data):
        '''Calculates the mean, standard deviation and kurtosis of the input dataframe.
        
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