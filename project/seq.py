#! usr/bin/python3

import keras
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras.optimizers import RMSprop
from sklearn.model_selection import train_test_split  
import matplotlib.pyplot as plt
from keras import models
from keras import layers
import datetime
import tensorflow as tf


batch_size = 1
epochs = 128


### using my own data set
# df = pd.read_csv('data.csv')
# ip_df = df.drop(['Domain', 'Ip', 'Throughput', 'Unit'], axis = 1)
# tp_df = df.drop(['Domain', 'Ip', 'Unit', 'Ip_bin'], axis = 1)

### using wyl's data set
df = pd.read_csv('processed_data.csv')
ip_df = df.drop(['Id', 'Ip', 'Throughput'], axis = 1)
tp_df = df.drop(['Id', 'Ip', 'Ip_bin'], axis = 1)



# get the ndarray of Y
l = tp_df.values.tolist()
ll = []
for item in l:
    item = float(item[0])
    ll.append(item)

Y = np.array(ll)
# Y /= 1024
print(Y.shape)

# get the ndarray of X
l = ip_df.values.tolist()
ll = []

for item in l:
    item = list(item[0])
    ll.append(item)

X = np.array(ll)
X = X.astype('int')

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=100) 

print(X.shape)

print(f"Training data:{X_train.shape}")
print(f"Test data:{X_test.shape}")

#######
# train and test

def build_model():
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(32,)))
    # model.add(layers.Dense(128, activation='relu'))
    # model.add(layers.Dense(128, activation='relu'))
    # model.add(layers.Dense(128, activation='relu'))
    model.add(layers.Dense(1))
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

model = build_model()

##########
history = model.fit(X_train, Y_train, epochs=epochs, batch_size=batch_size, verbose=1)
##########

##########
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
    # model = build_model()
    history = model.fit(partial_X_train,
              partial_Y_train,
              epochs=128,
              batch_size=1,
              verbose=1)

    val_mse, val_mae = model.evaluate(val_data, val_targets, verbose=1)
    all_scores.append(val_mae)


print(f'all_scores : {all_scores}')
print(f'mean all scores : {np.mean(all_scores)}')


###
# Try to plot training & validation loss values
try:
    print("History is:")
    print(history)
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('Model loss')
    plt.ylabel('Loss')
    plt.xlabel('Epoch')
    plt.legend(['Train', 'Test'], loc='upper left')
    plt.show()
except Exception as e:
    print(e)

###

test_mse_score, test_mae_score = model.evaluate(X_test, Y_test, verbose=1)

test_output = model.evaluate(X_test, Y_test, verbose=1)

print(f"test_mse_score:{test_mse_score}\ttest_mae_score:{test_mae_score}")

print(f"Total output is {test_output}")

