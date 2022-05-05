import os

#select the folder whose items you want to rename
source_folder= r'D:\Documents\Arch Work\FHG\Markcreaddie jobs 2020\5284 Njeri Muchunu\Wardrobes and vanities\ISSUE 002\Final\Final'
os.chdir(source_folder)

#convert all words for each file in the folder to upper case
for f in os.listdir(source_folder):
    os.rename(f,f.upper())
    print(f.upper())
























