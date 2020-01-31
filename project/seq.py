#! usr/bin/python3

import keras
import pandas as pd
import numpy as np
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
from sklearn.model_selection import train_test_split  

batch_size = 128

epochs = 1

df = pd.read_csv('data.csv')
ip_df = df.drop(['Domain', 'Ip', 'Throughput', 'Unit'], axis = 1)
tp_df = df.drop(['Domain', 'Ip', 'Unit', 'Ip_bin'], axis = 1)
print(tp_df)

# get the ndarray of Y
l = tp_df.values.tolist()
ll = []
for item in l:
    item = float(item[0])
    ll.append(item)

Y = np.array(ll)
max_tp = Y.max()
Y /= max_tp

print(Y.shape)

# get the ndarray of X
l = ip_df.values.tolist()
ll = []

for item in l:
    item = list(item[0])
    ll.append(item)

X = np.array(ll)
print(X)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.15, random_state=23) 
X_train = X_train.astype('int')
X_test = X_test.astype('int')

print(f"Training data:{X_train.shape}")
print(f"Test data:{X_test.shape}")
print(X_train)
print(type(X_train))

#######
# train and test
from keras import models
from keras import layers

def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(32,)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='rmsprop', loss='mse', metrics=['mae'])
    return model

model = build_model()
model.fit(X_train, Y_train, epochs=80, batch_size=16, verbose=1)
test_mse_score, test_mae_score = model.evaluate(X_test, Y_test, verbose=1)

print(f"test_mse_score:{test_mse_score}\ttest_mae_score:{test_mae_score}")