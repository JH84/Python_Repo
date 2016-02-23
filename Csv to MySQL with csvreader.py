# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 14:03:37 2016

@author: johnnyh
"""

#import csv
#import xlrd
import MySQLdb
import pandas

# Establish connection to MySQL

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='kwaadnaas',
    db='py')

# Open the workbook

#book = xlrd.open_workbook('c:/test/testdata.xlsx')
#sheet = book.sheet_by_index(0)

csv_df = pandas.read_csv('c:/test/geld45.csv')

print csv_df

clean_df = csv_df.where(pandas.notnull(csv_df), None)

print clean_df

clean_df.to_sql('testcreate', mydb , flavor = 'mysql', schema = 'py', if_exists = 'append', index = True, index_label = 'timestamp', chunksize = 10000)



# Commit the transaction
mydb.commit()

# close the database connection
mydb.close()

print '\n\nDone'