import pandas as pd
import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('out_final.csv')

train_size = 0.8

X = df.drop(columns = ["predicted"]).copy()
y = df["predicted"]

X_train, X_rem, y_train, y_rem = train_test_split(X, y, train_size=0.8)

test_size=0.5
X_valid, X_test, y_valid, y_test = train_test_split(X_rem, y_rem, test_size=0.5)

print(X_train.shape), print(y_train.shape)
print(X_valid.shape), print(y_valid.shape)
print(X_test.shape), print(y_test.shape)

X_train = X_train['samples'].to_list()
print(y_train)
y_train = y_train.to_list()

out_train = pd.DataFrame()
out_train['SRC'] = X_train
compression_opts = dict(method='zip', archive_name='out_train_X.csv')
out_train.to_csv('out_train_X.zip', index=False, compression=compression_opts)  

out_train = pd.DataFrame()
out_train['TRG'] = y_train
compression_opts = dict(method='zip', archive_name='out_train_Y.csv')
out_train.to_csv('out_train_Y.zip', index=False, compression=compression_opts)  

X_valid = X_valid['samples'].to_list()

y_valid = y_valid.to_list()

out_valid = pd.DataFrame()
out_valid['SRC'] = X_valid
compression_opts = dict(method='zip', archive_name='out_valid_X.csv')
out_valid.to_csv('out_valid_X.zip', index=False, compression=compression_opts)  

out_valid = pd.DataFrame()
out_valid['TRG'] = y_valid
compression_opts = dict(method='zip', archive_name='out_valid_Y.csv')
out_valid.to_csv('out_valid_Y.zip', index=False, compression=compression_opts)  

X_test = X_test['samples'].to_list()

y_test = y_test.to_list()

out_test = pd.DataFrame()
out_test['SRC'] = X_test
compression_opts = dict(method='zip', archive_name='out_test_X.csv')
out_test.to_csv('out_test_X.zip', index=False, compression=compression_opts)  

out_test = pd.DataFrame()
out_test['TRG'] = y_test
compression_opts = dict(method='zip', archive_name='out_test_Y.csv')
out_test.to_csv('out_test_Y.zip', index=False, compression=compression_opts)  