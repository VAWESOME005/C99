import os 
import shutil

source = input("Enter a folder you want to backup: ")
source = source + "/"

destination = input("Enter the location for your backup: ")
destination = destination + '/'

files_in_folder = os.listdir(source)

for file in files_in_folder:
    
    shutil.copy(source + file, destination + file)