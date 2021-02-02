# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 19:04:52 2021

@author: Aravindh
"""

import pandas
import Reducer as red

MyList = []
def Mapper():
    ds = pandas.read_csv("Project.csv")
    for line in ds.index:
        price = (ds['Price'][line]).replace(",","")
        country = ds['Country'][line]
        product = ds['Product'][line]
        MyList.append( list((country,product,int(price))) )
        
            
    

   
Mapper()
red.Reducer(MyList)
red.printDictionary()


