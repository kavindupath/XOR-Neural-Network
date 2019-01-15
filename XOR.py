>>> import tensorflow as tf,os,sys,numpy as np,matplotlib.pyplot as plt,sounddevice as sd,soundfile as sf,keras,importlib
Using TensorFlow backend.
>>> from keras.layers import Input,Flatten,Dense
>>> from keras.models import Sequential
>>> x=np.array([[0,0],[0,1],[1,0],[1,1]])
>>> y=np.array([0,1,1,0])
>>> mod=Sequential()
>>> mod.add(Dense(16,input_dim=2,activation="relu"))
>>> mod.add(Dense(1,activation="sigmoid"))
>>> mod.compile(loss="mean_squared_error",optimizer="adam",metrics=["binary_accuracy"])
>>> mod.fit(x,y,epochs=500,verbose=2)