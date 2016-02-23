# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 09:47:02 2016

@author: johnnyh
"""

import pandas
import MySQLdb

# create dataframe & import csv data to DF
csv_df = pandas.read_csv('c:/test/chillers jan1.csv')

# check for duplicate rows
dedup_df = csv_df.drop_duplicates('timestamp')

# create second DF to hold melt result
long_df = pandas.melt(dedup_df, id_vars = 'timestamp', var_name = 'Application')

print long_df

# write melt result to csv
#long_df.to_csv('c:/test/pivot_chilljan1.csv')


# Establish connection to MySQL
mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='kwaadnaas',
    db='netcare')

# clean data in long_df
clean_df = long_df.where(pandas.notnull(long_df), None)

# push clean data to MySQL
clean_df.to_sql('n1citychillers', mydb , flavor = 'mysql', schema = 'netcare', if_exists = 'append', index = True, index_label = 'timestamp, Application')

# Commit the transaction
mydb.commit()

# close the database connection
mydb.close()

print "\n\n Done"