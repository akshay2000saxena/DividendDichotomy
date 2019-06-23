import pandas as pd
import pickle
alldata = pd.read_pickle('../data/sp500finaldata.pkl')
print(alldata.firm.unique())