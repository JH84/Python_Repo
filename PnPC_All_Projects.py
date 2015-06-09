import requests
import time
from datetime import timedelta, date
import json

def format_date(input_date, date_format='%Y-%m-%d %H:%M:%S'):
    """
    format_date(input_date, date_format) -> str

    A simple wrapper on datetime.strftime

    Args:
        input_date (datetime): The input date
        date_format (str):     The string format we'd like the output in
    Returns:
        str:                   The correctly formatted date string
    Raises:
        None
    """
    return input_date.strftime(date_format)

def format_params(filename, sites, applications, sampled_start, sampled_end, accept='text/csv', time_of_use_group='default'):
    """
    format_params(filename, sites, applications, sampled_start, sampled_end, accept) -> dict

    Format the input parameters into a dictionary that will be sent as the payload
    to the Site Export REST call.

    Args:
        filename (str):           The filename of the server-side filename created
        sites (list):             A list of all Site ObjectId's
        applications (list):      A list of all application names
        sampled_start (datetime): The start date of the export
        sampled_end (datetime):   The end date of the export
        accept (str):             The content-header response type we want
    Returns:
        params (dict):            The correctly formatted parameter dictionary
    Raises:
        None
    """
    params = {'accept': accept,
              'filename': filename,
              'site': 'in,' + json.dumps(sites),
              'application': 'in,' + json.dumps(applications),
              'sampled_start': '>=,' + format_date(sampled_start),
              'sampled_end': '<=,' + format_date(sampled_end),
              'time_of_use_group': '=,' + time_of_use_group
              }

    return params

"""
We need to specify our input parameters that will be used in the REST
call to the Site Export handler.
We need the Start & End Date of the query, a list of sites, and their application names
"""

# Get input from user for date range

year = int(raw_input("Please enter the year => "))
try:
	int(year)
except ValueError:
	print "Please only use numbers..."
	year = int(raw_input("Please enter the year => "))


month = int(raw_input("Please enter the month => "))
try:
	int(month)
except ValueError:
	print "Please only use numbers..."
	month = int(raw_input("Please enter the month => "))

day = int(raw_input("Please enter the day => "))
try:
	int(day)
except ValueError:
	print "Please only use numbers..."
	month = int(raw_input("Please enter the day => "))

ddays = int(raw_input("Please enter the number of days to export => "))
try:
	int(ddays)
except ValueError:
	print "Please only use numbers..."
	ddays = int(raw_input("Please enter the number of days to export => "))

'''--------------------------
        Pilot & NROP1 
-----------------------------'''


start_date = date(year, month, day) # - timedelta(days=7)
end_date = start_date + timedelta(days= ddays)
sites = ['52f376859a5c212ec545da9f','52f37aad9a5c212f5e3f921b','52f376569a5c212ec545da8f','52f376409a5c212ec545da89','533bbd10aecb1607d1913e6e','52f3686a9a5c212ce126ee42','52f3763b9a5c212ec545da87','52f376459a5c212ec545da8a','52f3763d9a5c212ec545da88','52f368699a5c212ce126ee41']

    # Pinelands
    # Ottery
    # Greenstone
    # Walker Drive
    # Muizenburg
    # Westgate
    # Hillcrest
    # Wierda
    # Cresta
    # The Grove

applications = ['Refrigeration','Refrigeration kWh','Refrigeration kW']
filename = ('C:/EP/DATABASE/PnP Ref/Databuilder/Blimp kWh data/' + 'PnP_Pilot_NROP1_%s_%s.csv') % (format_date(start_date, '%Y%m%d'), format_date(end_date, '%Y%m%d'))

URI = 'http://blimp-p1/rest/site_export/query/?'

params = format_params(filename, sites, applications, start_date, end_date)
response = requests.get(URI, params=params)
fout = open(filename, 'wb')
fout.write(response.text)
fout.close()
print
print 'Pilot & NROP1 Done!'

'''--------------------
        NROP2 
-----------------------'''

start_date = date(year, month, day) # - timedelta(days=7)
end_date = start_date + timedelta(days= ddays)
sites = ['52f3765b9a5c212ec545da90','52f3767a9a5c212ec545da9a','52f376789a5c212ec545da99','52f376609a5c212ec545da92','533bc2cbaecb1607d1913e70']

    # Loch Logan
    # Kingsburgh
    # The Bluff
    # Melkbos
    # Goodwood

applications = ['Refrigeration','Refrigeration kWh','Refrigeration kW']
filename = ('C:/EP/DATABASE/PnP Ref/Databuilder/Blimp kWh data/' + 'PnP_NROP2_%s_%s.csv') % (format_date(start_date, '%Y%m%d'), format_date(end_date, '%Y%m%d'))

URI = 'http://blimp-p1/rest/site_export/query/?'

params = format_params(filename, sites, applications, start_date, end_date)
response = requests.get(URI, params=params)
fout = open(filename, 'wb')
fout.write(response.text)
fout.close()
print
print 'NROP2 Done!'

'''--------------------
        NROP3 
-----------------------'''

start_date = date(year, month, day) # - timedelta(days=7)
end_date = start_date + timedelta(days= ddays)
sites = ['52f376889a5c212ec545daa0']

    # Mountain mill
    # 
    # 
    # 
    # 

applications = ['Refrigeration','Refrigeration kWh','Refrigeration kW']
filename = ('C:/EP/DATABASE/PnP Ref/Databuilder/Blimp kWh data/' + 'PnP_NROP3_%s_%s.csv') % (format_date(start_date, '%Y%m%d'), format_date(end_date, '%Y%m%d'))

URI = 'http://blimp-p1/rest/site_export/query/?'

params = format_params(filename, sites, applications, start_date, end_date)
response = requests.get(URI, params=params)
fout = open(filename, 'wb')
fout.write(response.text)
fout.close()
print
print 'NROP3 Done!'

'''--------------------
        NROP4 
-----------------------'''

start_date = date(year, month, day) # - timedelta(days=7)
end_date = start_date + timedelta(days= ddays)
sites = ['52f376959a5c212ec545daa7','530c5a1a9a5c21080bebf1f5','52f376959a5c212ec545daa6','533bc336aecb1607d1913e72','533bc361aecb1607d1913e73','52f368709a5c212ce126ee48']

    # Quagga
    # Tramshed
    # Southdowns
    # Kenilworth
    # Plattekloof
    # Glen Garry

applications = ['Refrigeration','Refrigeration kWh','Refrigeration kW']
filename = ('C:/EP/DATABASE/PnP Ref/Databuilder/Blimp kWh data/' + 'PnP_NROP4_%s_%s.csv') % (format_date(start_date, '%Y%m%d'), format_date(end_date, '%Y%m%d'))

URI = 'http://blimp-p1/rest/site_export/query/?'

params = format_params(filename, sites, applications, start_date, end_date)
response = requests.get(URI, params=params)
fout = open(filename, 'wb')
fout.write(response.text)
fout.close()
print
print 'NROP4 Done!'

'''--------------------
        NGB 1 
-----------------------'''

start_date = date(year, month, day) # - timedelta(days=7)
end_date = start_date + timedelta(days= ddays)
sites = ['535f9e989a5c216e53a79b9e','52f376709a5c212ec545da96','5396df809a5c2117c5dc7779','54539090aecb1641e5ab0616']

    # Diepkloof
    # Cedar Road
    # Uitenhage Penford
    # Vangate

applications = ['Refrigeration','Refrigeration kWh','Refrigeration kW']
filename = ('C:/EP/DATABASE/PnP Ref/Databuilder/Blimp kWh data/' + 'PnP_NGB1_%s_%s.csv') % (format_date(start_date, '%Y%m%d'), format_date(end_date, '%Y%m%d'))

URI = 'http://blimp-p1/rest/site_export/query/?'

params = format_params(filename, sites, applications, start_date, end_date)
response = requests.get(URI, params=params)
fout = open(filename, 'wb')
fout.write(response.text)
fout.close()
print
print 'NGB 1 Done!'

'''--------------------
        NGB 2 
-----------------------'''

start_date = date(year, month, day) # - timedelta(days=7)
end_date = start_date + timedelta(days= ddays)
sites = ['53bbd993b8dd09d5742075ac','53bbd9e8b8dd09d57d565dcf']

    # Auckland Park
    # Edenvale

applications = ['Refrigeration','Refrigeration kWh','Refrigeration kW']
filename = ('C:/EP/DATABASE/PnP Ref/Databuilder/Blimp kWh data/' + 'PnP_NGB2_%s_%s.csv') % (format_date(start_date, '%Y%m%d'), format_date(end_date, '%Y%m%d'))

URI = 'http://blimp-p1/rest/site_export/query/?'

params = format_params(filename, sites, applications, start_date, end_date)
response = requests.get(URI, params=params)
fout = open(filename, 'wb')
fout.write(response.text)
fout.close()
print
print 'NGB 2 Done!'

'''--------------------
        NGB 3
-----------------------'''

start_date = date(year, month, day) # - timedelta(days=7)
end_date = start_date + timedelta(days= ddays)
sites = ['53ba83cbb8dd09c5f3045dbf','545395aaaecb1641e5ab0626','53ba82d7b8dd09c5dc45be86','53bbda2cb8dd09d57d565dd4']

    # Lotus River
    # Secunda Mall
    # Somerset West
    # Lebo Mall

applications = ['Refrigeration','Refrigeration kWh','Refrigeration kW']
filename = ('C:/EP/DATABASE/PnP Ref/Databuilder/Blimp kWh data/' + 'PnP_NGB3_%s_%s.csv') % (format_date(start_date, '%Y%m%d'), format_date(end_date, '%Y%m%d'))

URI = 'http://blimp-p1/rest/site_export/query/?'

params = format_params(filename, sites, applications, start_date, end_date)
response = requests.get(URI, params=params)
fout = open(filename, 'wb')
fout.write(response.text)
fout.close()
print
print 'NGB 3 Done!'

print "\nAll Data exports complete!"
time.sleep(2)
