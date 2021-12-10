# -*- coding: utf-8 -*-
"""LinearRegMultiVar.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C8LUVIDtpXEDNqx0-guEgLDWPX-AE7-b
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('house_data.csv')

dataset.insert(4,"x0",1)
print (dataset.head())

x_data = dataset.iloc[:,[4,5,6,10,12,18]]
y_data = dataset['price']
print(x_data)

#scaling
x1_max=x_data.iloc[:,1].max()
x2_max=x_data.iloc[:,2].max()
x3_max=x_data.iloc[:,3].max()
x4_max=x_data.iloc[:,4].max()
x5_max=x_data.iloc[:,5].max()
x_data.iloc[:,1]=(x_data.iloc[:,1])/(x1_max)
x_data.iloc[:,2]=(x_data.iloc[:,2])/(x2_max)
x_data.iloc[:,3]=(x_data.iloc[:,3])/(x3_max)
x_data.iloc[:,4]=(x_data.iloc[:,4])/(x4_max)
x_data.iloc[:,5]=(x_data.iloc[:,5])/(x5_max)
print(x_data)

#convert to matrix
x_data=np.array(x_data)
y_data=np.array(y_data).flatten()
print(x_data.shape)
print(y_data.shape)

#split data train & test 80/20
trainSize=int(y_data.size*.8)
print(trainSize)
xTrain=x_data[:trainSize]
xTest=x_data[trainSize:]

yTrain=y_data[:trainSize]
yTest=y_data[trainSize:]

print(xTrain,xTest)
print(len(yTrain),len(yTest))

alpha=.8
ceta=np.array([0,0,0,0,0,0])
mse=[]
def gradientDescentOneVar():
    global ceta,mse
    for i in range(100000):
        y_pred = xTrain.dot(ceta) 
        ceta = ceta - ((xTrain.T.dot(y_pred - yTrain)) * alpha * (1 / trainSize))
        ceta0,ceta1,ceta2,ceta3,ceta4,ceta5=ceta
        #mse.append(MSE(ceta0,ceta1,ceta2,ceta3,ceta4,ceta5))
    print("MSE = ",MSE(ceta0,ceta1,ceta2,ceta3,ceta4,ceta5))
    print("Theta: ",ceta)

def MSE(ceta0,ceta1,ceta2,ceta3,ceta4,ceta5):
    Esum=0
    xTrain1=xTrain[:,1]
    xTrain2=xTrain[:,2]
    xTrain3=xTrain[:,3]
    xTrain4=xTrain[:,4]
    xTrain5=xTrain[:,5]
    for i in range(trainSize):
        Esum+=pow( yTrain[i] - (ceta0 + (ceta1*xTrain1[i]) + (ceta2*xTrain2[i]) + (ceta3*xTrain3[i]) + (ceta4*xTrain4[i]) + (ceta5*xTrain5[i]) ) , 2)
    Esum=Esum*(1/(2 * trainSize))
    return Esum

gradientDescentOneVar()

def predTest():
    ytestpred = xTest.dot(ceta)
    print('Predicted price:',ytestpred)
    print('Orignal price:',yTest)

predTest()

#Trying different alphas
#alpha = .8       iteration = 100000      MSE =  26803945799.290802
#alpha = .4       iteration = 100000      MSE =  27656845318.353786
#alpha = .1       iteration = 100000      MSE =  28515275366.74755
#alpha = .01      iteration = 10000       MSE =  32704127208.611366
#alpha = .001     iteration = 50000       MSE =  36509641064.27643
#alpha = .0001    iteration = 100000      MSE =  50854593503.595795