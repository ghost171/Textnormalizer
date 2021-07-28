import pandas as pd
import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np

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
np.savetxt(r'X_train.txt', out_train.values, fmt='%s')

out_train = pd.DataFrame()
out_train['TRG'] = y_train
np.savetxt(r'Y_train.txt', out_train.values, fmt='%s')

X_valid = X_valid['samples'].to_list()

y_valid = y_valid.to_list()

out_valid = pd.DataFrame()
out_valid['SRC'] = X_valid
np.savetxt(r'X_valid.txt', out_train.values, fmt='%s')

out_valid = pd.DataFrame()
out_valid['TRG'] = y_valid
np.savetxt(r'Y_valid.txt', out_train.values, fmt='%s')

X_test = X_test['samples'].to_list()

y_test = y_test.to_list()

out_test = pd.DataFrame()
out_test['SRC'] = X_test
np.savetxt(r'X_test.txt', out_train.values, fmt='%s')

out_test = pd.DataFrame()
out_test['TRG'] = y_test
np.savetxt(r'Y_test.txt', out_train.values, fmt='%s')