import pandas as pd

df = pd.read_csv('out_final.csv')

import pandas as pd
from sklearn.model_selection import train_test_split

train_size = 0.8

X = df.drop(columns = ["predicted"]).copy()
y = df["predicted"]

X_train, X_rem, y_train, y_rem = train_test_split(X, y, train_size=0.8)

test_size=0.5
X_valid, X_test, y_valid, y_test = train_test_split(X_rem, y_rem, test_size=0.5)

print(X_train.shape), print(y_train.shape)
print(X_valid.shape), print(y_valid.shape)
print(X_test.shape), print(y_test.shape)

print("X_TRAIN", X_train)
X_train = X_train['samples'].to_list()
print("X_TRAIN", X_train)
y_train = y_train['predicted'].to_list()

out_train = pd.DataFrame()
out_train['SRC'] = X_train.to_list()
out_train['TRG'] = y_train.to_list()
out_train.to_csv('out_train_X.zip', index=False, compression=compression_opts)  

out_train = pd.DataFrame()
out_train['TRG'] = y_train.to_list()
out_train.to_csv('out_train_y.zip', index=False, compression=compression_opts)  

X_valid = X_valid['samples'].to_list()
print("X_TRAIN", X_valid)
y_valid = y_valid.to_list()

out_valid = pd.DataFrame()
out_valid['SRC'] = X_valid.to_list()
out_valid.to_csv('out_valid_X.zip', index=False, compression=compression_opts)  

out_train = pd.DataFrame()
out_train['TRG'] = y_valid.to_list()
out_train.to_csv('out_valid_y.zip', index=False, compression=compression_opts)  

X_test = X_test['samples'].to_list()
print("X_TRAIN", X_test)
y_test = y_test['predicted'].to_list()

out_test = pd.DataFrame()
out_test['SRC'] = X_test.to_list()
out_test['TRG'] = y_test.to_list()
out_test.to_csv('out_test.zip', index=False, compression=compression_opts)  