import os
import pathlib

import numpy as np
import math
import decimal
import mpmath
from decimal import Decimal, getcontext

getcontext().prec = 50






from ast import literal_eval
Filename = ''

#Reading the hex values from the file and converting them into dec (base 10)
def ReadHex(filename,index):
    #encrypet image
    start = 0
    end = 13
    with open(filename, 'rb') as f:
        content = f.read().hex()
        ReadHex.content = content
        print(content[index-20:index])
        print(content[index-20:index])
        #print(content[16:16+16]) #hint fot how to increase in aloop
        #print(content[0:32])
        print("output (convert Hex to dec):" , int(content[index-20:index],16))
        ReadHex.Int = int(content[index-20:index],16)

        return ReadHex.Int

k=20
def training(output):
    i=0
    training.learningRate = 0.1
    # network inputs, outputs and weights
    training.input = np.array([[0.2], [0], [0]])

    training.outputs = np.array([[output], [0], [0]])

    training.weights = [0.1]

    while i< 6000:
        j=0

        while j<3:
            netoutPut = training.input[j] * training.weights[0]
            predicion = math.fabs(netoutPut[0] - training.outputs[j])  * training.learningRate
            training.weights[0] +=predicion
            # print('prediction:' , str(int(netoutPut)))
            weights_str = str(int(training.weights[0]))
            #print(weights_str)
            # print('error:' + str(math.fabs(netoutPut[0] - training.outputs[j])))
            j = j + 1
            i = i + 1

    testing()





#
#

def NetReBuildNumber(input,output):
    i=0
    NetReBuildNumber.learningRate = 0.1
    # network inputs, outputs and weights
    NetReBuildNumber.input = np.array([[input], [0], [0]])

    NetReBuildNumber.outputs = np.array([[output], [0], [0]])

    NetReBuildNumber.weights = [0.1]


    while i< 6000:
        j=0

        while j<3:
            netoutPut = math.pow(10, 0.1*NetReBuildNumber.input[j]) * NetReBuildNumber.weights[0]
            predicion = math.fabs(netoutPut[0] - NetReBuildNumber.outputs[j])  * NetReBuildNumber.learningRate
            NetReBuildNumber.weights[0] +=predicion
            # print('prediction:' , str(int(netoutPut)))
            weights_str = str(int(NetReBuildNumber.weights[0]))
            #print(weights_str)
            # print('error:' + str(math.fabs(netoutPut[0] - training.outputs[j])))
            j = j + 1
            i = i + 1

    print('net rebuild number: ', )
    outputNum = NetReBuildNumber.outputs[0]
    predictoinWeight = NetReBuildNumber.weights[0]

    sum = (predictoinWeight * NetReBuildNumber.input[0]) + math.fabs(outputNum - (predictoinWeight * NetReBuildNumber.input[0]))
    # sum = math.fabs(sum - outputNum)

    str_sum = str(int(sum))
    # print("net Prediction:" + str_sum)
    str_sum = str(int(sum))
    print("net Prediction:" + str_sum)




# #testing the accuracy  of the net
def testing():
    outputNum = training.outputs[0]
    predictoinWeight = training.weights[0]

    sum = (predictoinWeight * training.input[0] ) + math.fabs(outputNum- (predictoinWeight* training.input[0]))
    #sum = math.fabs(sum - outputNum)

    str_sum = str(int(sum))
    # print("net Prediction:" + str_sum)
    str_sum = str(int(sum))
    print("net Prediction:" + str_sum)
    str_weights = str(int(training.weights[0]))
    # print("net Weight:" ,int(str_weights,10) * (int(len(str_weights))*0.1) )
    print("net Weight(int): " + str_weights)

    str_Logweights = str(int(math.log(training.weights[0],10)))
    # print("net Weight:" ,int(str_weights,10) * (int(len(str_weights))*0.1) )
    print("LogB10 Weight(int): " + str_Logweights)
    #
    # print('reverse log to full number: ' ,math.pow(int(int(math.log(training.weights[0],10))),10))
    # NetReBuildNumber()
    print(training.weights[0])
    print(training.outputs[0])
    # NetReBuildNumber(int(training.weights[0]),outputNum)


    print()





#reading the files from the current directory
for filename in os.listdir(pathlib.Path().resolve()):
    if filename.endswith(".jpg") or filename.endswith(".JPG") or filename.endswith('.txt'):
        Filename = filename
        print(filename)

        temp = ReadHex(Filename,index=k)
        training(temp)



# testing()
k+=20




lenLeftCurrent = len(str(ReadHex.content[k - 20:k]))



lenLeftCurrent = len(str(ReadHex.content[k - 20:k]))
lenLeftGeneral = len(str(ReadHex.content[k:]))
    #mooving on to the next values to encode
while math.fabs(lenLeftGeneral- lenLeftCurrent)>20 and ReadHex.content[k-20:k] != '':
        # training.outputs[0] =ReadHex(Filename,k)

        weights = [0.1]
        training(ReadHex(Filename,k))
        # testing()
        k += 20
# lenLeftGeneral = len(str(ReadHex.content[k:]))
# print(lenLeftGeneral)
# lenLeftCurrent = len(str(ReadHex.content[k - 13:k]))
# print(math.fabs(lenLeftGeneral- lenLeftCurrent))
# if lenLeftGeneral < 13 or math.fabs(lenLeftGeneral- lenLeftCurrent)<10:#lenLeftGeneral >13 and lenLeftGeneral < 26:
#     with open(Filename, 'rb') as f:
#         content = f.read().hex()
#         ReadHex.content = content
#         print(content[k:])
#         print(content[k:])
#         #print(content[16:16+16]) #hint fot how to increase in aloop
#         #print(content[0:32])
#         print("output (in hex):" , int(content[k:],16))
#         ReadHex.Int = int(content[k:],16)
#     outputs[0] = ReadHex.Int
#     weights = [0.1]
#     training()
#     testing()




