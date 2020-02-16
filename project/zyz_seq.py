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

df = pd.read_csv('remove0tp.csv')
ip_df = df.drop(['Throughput'], axis = 1)
tp_df = df.drop(['Ip'], axis = 1)
print(df)

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
print(type(l[0][0]))
ll = []

for item in l:
    ip = item[0]
    ip_bin = ""
    for x in ip.split('.'):
        ip_bin += format(int(x), "08b")
    
    ip_bin = list(ip_bin)
    ll.append(ip_bin)

X = np.array(ll)
print(X)

Y *= 1000
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=23) 
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


k = 4
num_val_samples = len(X_train) // k
num_epochs = 100
all_scores = []

for i in range(k):
    print(f'Processing fold # {i}')
    val_data = X_train[i * num_val_samples: (i+1) * num_val_samples]
    val_targets = Y_train[i * num_val_samples: (i+1) * num_val_samples]
    
    partial_X_train = np.concatenate(
                            [X_train[:i * num_val_samples],
                            X_train[(i+1) * num_val_samples:]],
                            axis=0)

    print(partial_X_train.shape)
    partial_Y_train = np.concatenate(
                            [Y_train[:i * num_val_samples],
                            Y_train[(i+1)*num_val_samples:]],
                            axis=0)
    model = build_model()
    model.fit(partial_X_train,
              partial_Y_train,
              epochs=num_epochs,
              batch_size=16,
              verbose=1)
    val_mse, val_mae = model.evaluate(val_data, val_targets, verbose=1)
    all_scores.append(val_mae)


print(f'all_scores : {all_scores}')
print(f'mean all scores : {np.mean(all_scores)}')


# model = build_model()
# model.fit(X_train, Y_train, epochs=80, batch_size=16, verbose=1)
test_mse_score, test_mae_score = model.evaluate(X_test, Y_test, verbose=1)

print(Y.mean())
print(f"test_mse_score:{test_mse_score}\ttest_mae_score:{test_mae_score}")