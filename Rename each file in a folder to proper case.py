import os

#select the folder whose items you want to rename
source_folder= r'D:\Documents\Arch Work\FHG\Markcreaddie jobs 2020\5284 Njeri Muchunu\Wardrobes and vanities\ISSUE 002\Final'
os.chdir(source_folder)

#capitalize the first letter of each word for each file in the folder and convert all other letters to lower case
for each_file_name in os.listdir(source_folder):
    os.rename(each_file_name, each_file_name.title())
    print(each_file_name.title())
























