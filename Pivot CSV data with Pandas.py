# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 12:37:12 2016

@author: johnnyh
"""

import pandas
import MySQLdb
#import numpy

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='kwaadnaas',
    db='py')
    

df = pandas.read_csv('c:/test/SG.csv')

df.pivot(index = [0])

print df
