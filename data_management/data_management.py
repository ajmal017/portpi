import yfinance as yf
import json
import datetime
import os
import investpy
import pandas as pd

class Data:
    def __init__(self, save_directory='raw_data'):
        '''Creates a Data object for downloading and storing data. 
        
        Args
        ----
        save_directory: String
            Directory which the data will be saved to
        '''

        self.save_directory = save_directory


    def collect_data(self, start_date='01/01/2000', end_date= datetime.date.today().strftime('%d/%m/%Y')):
        '''Downloads asset data for a given start and end time range. Stores the downloaded data.
        
        Args
        ----
        start_data: String
            Start date for collecting asset data. format should be dd/mm/yyyy
        end_date: String
            End date for asset data collection period. Default value is set to today
        '''

        ticker_raw = 'ADANA-AEFES-ULKER-AKBNK-AKGRT-AKSA-ALARK-ALGYO-ALKIM-ANACM-ANHYT-ARCLK-ASELS-AYGAZ-BRISA-BRSAN-BTCIM-BUCIM-CEMTS-CIMSA-CLEBI-DEVA-DOHOL-ECILC-ECZYT-EGEEN-ENKAI-ERBOS-EREGL-FROTO-GARAN-GOODY-GSDHO-GUBRF-GUSGR-HEKTS-IPEKE-ISCTR-ISFIN-ISGYO-KARSN-KARTN-KCHOL-KERVT-KLMSN-KORDS-KRDMD-LOGO-MGROS-NETAS-NTHOL-OTKAR-PETKM-SAHOL-SASA-SISE-SKBNK-SODA-TATGD-TCELL-THYAO-TOASO-TRCAS-TRKCM-TSKB-TUPRS-VESTL-YATAS-AGHOL-YKBNK-ZOREN-KOZAA-TTRAK-DOAS-INDES-BIMAS-VAKBN-CCOLA-KAREL-TAVHL-HALKB-ISMEN-ALBRK-TKFEN-TTKOM-GOZDE-KOZAL-AKSEN-TRGYO-EKGYO-BIZIM-TMSN-HLGYO-PGSUS-ODAS-ISDMR-MAVI-ENJSA-MPARK-SOKM'
        ticker_list = []
        for tick in ticker_raw.split('-'):
            ticker_list.append(tick)
        if 'BIST 100' not in ticker_list:
            ticker_list.insert(0,'BIST 100')

        Data._check_directory(self.save_directory)

        k = 0
        for i, ticker in enumerate(ticker_list):
            if ticker == 'BIST 100':
                data = investpy.get_index_historical_data(index=ticker, country='turkey',
                                                        from_date=start_date, to_date=end_date,
                                                        as_json=False, order='ascending')
                name = 'XU100'
            else:
                data = yf.download(ticker + '.IS', start= datetime.datetime.strptime(start_date, '%d/%m/%Y'),
                                end=datetime.datetime.strptime(end_date, '%d/%m/%Y'), interval='1d', threads = True,
                                progress=False)
                name = ticker
            data.to_csv(self.save_directory + '/' + name + '.csv')
            k += 1
        print('Downloaded: %d' %k)


    def _check_directory(dir):
        '''Check if the directory exits, otherwise create the directory
        
        Args
        ----
        dir : String
            location of the directory

        Returns
        -------
        created : Boolean
            Creation status of directory, true if directory created, false if directory already existed
        '''

        if not os.path.exists(dir):
            os.makedirs(dir)
            created = True
        else:
            created = False
        
        return created


    def compile_close_data(self, symbols, compile_start_date='2000-01-01', compile_end_date= datetime.date.today()):
        '''Merge the closing prices of the asset data.
        
        Args
        ----
        symbols: List
            List of symbols which the data will be used for
        compile_start_date: String
            Start date for data useage. Format of date yyyy-mm-dd
        compile_end_date: String
            End date for data useage. Format of date yyyy-mm-dd. Default value set for today.

        Returns
        -------
        df: pandas.DataFrame
            Compiled data frame of close prices
        '''

        '''Read stock data (adjusted close) for given symbols from CSV files.'''
        dates = pd.date_range(compile_start_date,compile_end_date)
        df = pd.DataFrame(index=dates)
        syms = symbols.copy()
        if 'XU100' not in syms:  # add XU100 for reference, if absent
            syms.insert(0, 'XU100')

        for symbol in syms:
            if symbol == 'XU100':  # drop dates XU100 did not trade
                df_temp = pd.read_csv(self._symbol_data_path(symbol), index_col='Date',
                        parse_dates=True, usecols=['Date', 'Close'], na_values=['nan'])
                df_temp = df_temp.rename(columns={'Close': symbol})
                df = df.join(df_temp)
                df = df.dropna(subset=["XU100"])
            else:
                df_temp = pd.read_csv(self._symbol_data_path(symbol), index_col='Date',
                        parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
                df_temp = df_temp.rename(columns={'Adj Close': symbol})
                df = df.join(df_temp)
        return df


    def _symbol_data_path(self, symbol):
        '''Return CSV file path for given symbol.'''
        path = os.path.join(self.save_directory, "{}.csv".format(str(symbol)))
        return path
