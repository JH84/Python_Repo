# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 10:45:31 2016

@author: johnnyh
"""

#import csv
import xlrd
import MySQLdb

# Open the workbook

book = xlrd.open_workbook('c:/test/n1 city main.xlsx')
sheet = book.sheet_by_index(0)

#csv_data = csv.reader(file('c:/test/geld.csv'))

# Establish connection to MySQL

mydb = MySQLdb.connect(host='localhost',
    user='root',
    passwd='kwaadnaas',
    db='py')

# get the cursor, which is used to traverse the database, line by line
cursor = mydb.cursor()

# create the INSERT INTO sql query
query = """INSERT INTO testing (timestamp, supply_temp, return_temp, makeup_flow, makeup_temp, hp_energy, boiler_energy, total_energy, return_flow) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)"""

# Create a For loop to iterate through each row in the file, starting at row 2 to skip the headers

for r in range(1, sheet.nrows):
    timestamp = sheet.cell(r,0).value
    supply_temp = sheet.cell(r,1).value
    return_temp = sheet.cell(r,2).value
    makeup_cons = sheet.cell(r,3).value
    makeup_temp = sheet.cell(r,4).value
    hp_energy = sheet.cell(r,5).value
    boiler_energy = sheet.cell(r,6).value
    total_energy = sheet.cell(r,7).value
    return_flow = sheet.cell(r,8).value
    
    # assign values from each row
    values = (timestamp, supply_temp, return_temp, makeup_cons, makeup_temp, hp_energy, boiler_energy, total_energy, return_flow)
    
    # execute the sql query
    cursor.execute(query, values)
    
# close the cursor
cursor.close()

# Commit the transaction
mydb.commit()

# close the database connection
mydb.close()

# print results
print ""
print "Done"
print ""
columns = str(sheet.ncols)
rows = str(sheet.nrows)

print "Added " + columns + ", and " + rows + " rows to "
