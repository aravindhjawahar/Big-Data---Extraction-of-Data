# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 19:05:09 2021

@author: Aravindh
"""


MyDictionary = {}

def Find_Dictioary_Keys(data):
    MyList = []
    for key,value in MyDictionary.items():
        if data in key:
            MyList = value
    return MyList

def Update_Dictionary(keyFind,valueFind):
    for key,value in MyDictionary.items():
        if keyFind == key:
            value = valueFind
                    
def printDictionary():
    for key, value in MyDictionary.items():
        print(key, value[0],value[1])
def Reducer(MyList):
    for listItem in MyList:
        if listItem[0] in MyDictionary.keys():
            tempList    = Find_Dictioary_Keys(listItem[0])
            tempList[0] = tempList[0] + 1
            tempList[1] = tempList[1] + listItem[2]
            Update_Dictionary( listItem[0] , tempList)
            MyDictionary[ listItem[0] ] = tempList
        else:
            milist = [1,listItem[2]]
            MyDictionary[(listItem[0])] = milist
    printDictionary()