# !usr/bin/python3

import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation
from sklearn.model_selection import train_test_split  
import math

def main():
    df = pd.read_csv('panellist-data.csv')
    # df.describe().T
    # print(df)
    
    X = df[[col for col in df.columns if col != 'hspeed']]
    Y = df['hspeed']

    print(df.isnull().any())
    # print(type(Y.values))
    # index = 1
    # for item in Y:
    #     if math.isnan(item):
    #         print(index, end='\t')
    #     index += 1
            

    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.15, random_state=23) 
    
    # print(X_test)
    X_train.shape, X_test.shape 
    print("Training instances   {}, Training features   {}".format(X_train.shape[0], X_train.shape[1]))  
    print("Testing instances    {}, Testing features    {}".format(X_test.shape[0], X_test.shape[1]))  

    model = Sequential()

    model.add(Dense(output_dim = 1024, input_dim = 8, activation='relu'))
    model.add(Dense(output_dim = 1024, activation='relu'))
    model.add(Dense(output_dim = 1))

    model.compile(loss='mse', optimizer='sgd')

    for step in range(300):
        cost = model.train_on_batch(X_train, Y_train)
        if step % 100 == 0:
            print("Train cost:", cost)

    # test
    print("Testing................")
    cost = model.evaluate(X_test, Y_test, batch_size=200)
    print("Test cost:", cost)


    



if __name__ == "__main__":
    main()