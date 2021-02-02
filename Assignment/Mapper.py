# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:40:48 2021

@author: Aravindh
"""
import Reducer as red

MyDictionary = {}
#Item list and all prices
MyList = []
#Item list and final price
itemList =[]
def Mapper():
    #Open file for prices
    file = open("pricelist.txt","r")
    for line in file:
        data = line.strip().split("\t")
        
        if len(data) != 6:
            continue
        #Store column from text file into variables
        date, time, store, item, cost, payment = data
        #Adding Itesm and price to the lists
        MyList.append(list((  item,float(cost) )))
        

Mapper()
red.Reducer(MyList)