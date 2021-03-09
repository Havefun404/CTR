# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import random

class LoadData(object):
    
    def __init__(self, path, dataset, loss_type):
        self.path = path + dataset + "/"
        self.trainfile = self.path + dataset +".train.txt"
        self.testfile = self.path + dataset + ".test.txt"
        self.validationfile = self.path + dataset + ".valid.txt"
        self.features_M = self.map_features()
        self.Train_data, self.Validation_data, self.Test_data = self.construct_data(loss_type)

    def map_features(self): 
        self.features = {}
        self.read_features(self.trainfile)
        self.read_features(self.testfile)
        self.read_features(self.validationfile)

        return  len(self.features)

    def read_features(self, file): 
        f = open(file)

        line = f.readline()
        
        i = len(self.features)
        while line:
            items = line.strip().split('\t')
        
            for item in items[1:]:
                if item not in self.features:
                    self.features[ item ] = i
                    i = i + 1
        
            line = f.readline()
        
        f.close()

    def construct_data(self, loss_type):
        X_, Y_ , Y_for_logloss= self.read_data(self.trainfile)
        
        if loss_type == 'log_loss':
            Train_data = self.construct_dataset(X_, Y_for_logloss)
        else:
            Train_data = self.construct_dataset(X_, Y_)       
        
        X_, Y_ , Y_for_logloss= self.read_data(self.validationfile)
        
        if loss_type == 'log_loss':
            Validation_data = self.construct_dataset(X_, Y_for_logloss)
        else:
            Validation_data = self.construct_dataset(X_, Y_)       
        
        X_, Y_ , Y_for_logloss = self.read_data(self.testfile)
        
        if loss_type == 'log_loss':
            Test_data = self.construct_dataset(X_, Y_for_logloss)
        else:
            Test_data = self.construct_dataset(X_, Y_)        
        
        return Train_data,  Validation_data,  Test_data

    # 读取数据，转化为模型可读类型
    def read_data(self, file):        
        f = open(file)
        
        # X_: 输入特征
        # Y_: 预测值
        # Y_for_logloss: logloss的预测值
        X_ = []
        Y_ = []
        Y_for_logloss = []
        
        line = f.readline()
        while line:
            items = line.strip().split('\t')
            Y_.append( 1.0*float(items[0]) )
            if float(items[0]) > 0:
                v = 1.0
            else:
                v = 0.0
            Y_for_logloss.append( v )

            # 输入三元组one-hot编码
            X_.append( [ self.features[item] for item in items[1:] ] )
            line = f.readline()
        f.close()
        return X_, Y_, Y_for_logloss

    def construct_dataset(self, X_, Y_):
        Data_Dic = {}
        X_lens = [ len(line) for line in X_]
        indexs = np.argsort(X_lens)
        Data_Dic['Y'] = [ Y_[i] for i in indexs]
        Data_Dic['X'] = [ X_[i] for i in indexs]
        return Data_Dic
    
    def truncate_features(self):        
        num_variable = len(self.Train_data['X'][0])
        for i in range(len(self.Train_data['X'])):
            num_variable = min([num_variable, len(self.Train_data['X'][i])])
        # truncate train, validation and test
        for i in range(len(self.Train_data['X'])):
            self.Train_data['X'][i] = self.Train_data['X'][i][0:num_variable]
        for i in range(len(self.Validation_data['X'])):
            self.Validation_data['X'][i] = self.Validation_data['X'][i][0:num_variable]
        for i in range(len(self.Test_data['X'])):
            self.Test_data['X'][i] = self.Test_data['X'][i][0:num_variable]
        return num_variable