import zipfile
import os
import glob
import time

ftype_xls = ".xls"

def unzip(zip_file):
    """
    Unzip a given 'zip_file''.
    """
    zf = zipfile.ZipFile(str(zip_names), "r")
    zf.extractall()
    print "Extracted ==>  %r" % zip_names

def cleanup():
	new_name = os.path.splitext(zip_names)[0]
	
	for extract_name in os.listdir("C:/EP/DATABASE/PnP Ref/Databuilder/CSV data/"):
		if extract_name.startswith('export_'):
			os.rename(extract_name, str(new_name) + str(ftype_xls))
			print "Renamed ==>  Done"
		
for zip_names in glob.glob('*.zip'):
	
	unzip(str(zip_names))
	cleanup()
	
print "All Done!"
time.sleep(2)
exit()