# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:41:03 2021

@author: Aravindh
"""


def Reducer(MyList):
    MyDictionary = {}
    itemList =[]
    #Iterating through list of data
    for item in MyList:
        #Adding items to dictionary maps country contains list of total products and total amount
        if item[0] in MyDictionary.keys():
            MyDictionary[item[0]].append(item[1])
        else:
            MyDictionary[item[0]] = [item[1]] 
    for key, value in MyDictionary.items():
        itemList.append(list(( key, max(value) )))
    print(itemList)