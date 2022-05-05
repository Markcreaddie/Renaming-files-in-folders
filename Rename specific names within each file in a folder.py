import os

#select the folder whose items you want to rename
source_folder= r'D:\Documents\Arch Work\FHG\Markcreaddie jobs 2020\5264 Rose Olende\ISSUE 001\Final\Quotes - Copy'
os.chdir(source_folder)

quote_issue= "002"
quote_date= "04-05-2022"

for each_file_name in os.listdir(source_folder):
    x = each_file_name.split(" ")

#select only files starting with the word "ISSUE" and rename the issue number and date of quote
    if x[0].upper()=="ISSUE":
        x[1]=quote_issue
        x[3]=quote_date
        new_name=" ".join(x)
        print(new_name)
        os.rename(each_file_name, new_name)




