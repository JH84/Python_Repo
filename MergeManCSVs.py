# -*- coding: utf-8 -*-
"""
Created on Thu Sep 18 11:09:39 2014

@author: johnnyH
"""

import pandas
import glob
from collections import defaultdict

header_list = [0,1]                         # Create a list with the number of rows to be used as the header
index_colnum = [0]                          # Create list with index_col number so that it can be called later
all_data_df = pandas.DataFrame()            # Create an empty Dataframe to which everything will be added

csv_files_list = []                         # List for all csvs in folder
site_name_list = []                         # List for all site names in folder to be used to loop through each file 'set'

sites = defaultdict(list)
for fname in glob.glob('*.csv'):
    site_name = fname.split(' ')[0]
    sites[site_name].append(fname)

#print sites
'''
{'Tygervalley': ['Tygervalley blah.csv', 'Tygetvalley 3.csv']}

'''

for site_name, site_files in sites.iteritems():
    print site_name
    # ex: tygervalley
    print site_files
    # ex: ['Tygervalley blah.csv', 'Tygetvalley 3.csv']
    
    all_data_df = pandas.DataFrame()   
    
    for fname in site_files:
        header_list = [0,1]                         # Create a list with the number of rows to be used as the header
        index_colnum = [0]
        
        df1 = pandas.DataFrame()
        
        csvname = ('C:/test/' + fname)
        print csvname              
        in_file = pandas.read_csv(csvname ,delimiter = ';', header = header_list, skiprows = 4,
                          index_col = index_colnum , keep_date_col = True, parse_dates = True)
        
        df1 = pandas.DataFrame(in_file)
        
        all_data_df = all_data_df.combine_first(df1)
        #print all_data_df
        
    all_data_df.to_csv('output\\' + site_name + ' output.csv', na_rep = 'ND')
    print site_name + " output.csv ==>  generated"

print "Done!"
'''
#Cheese W/A 4.15C   in header breaking the process
'''
#for all_csvs in os.listdir('C:/test/'):
#    if all_csvs.endswith(".csv"):
#        print "Adding " + all_csvs + " to the list."
#
#        csv_files_list.append(all_csvs)
#        site_name = all_csvs.split(' ')[0]
#
#        #print site_name
#        if site_name in site_name_list:         # Checks if the site name is in the list already
#            print "Site name already in list"        # If name is in list, just do nothing and go to next name
#            continue
#        else:
#            site_name_list.append(site_name)    # Add name to the list if not in list
#            print "Site name added to list"
#
#print csv_files_list
#print site_name_list