#python delete files from the system
#input files details date and path needs to be deleted depends on date created


"""The script deleet fies based on creation date if reuired can be changed to modified date"""

import os,datetime,time,sys
from subprocess import call


file_path=input("Enter the directory to delete file :")
days_to_del=int(input("Enter age in days file removed :"))

directory_names = ['/system_backups/data/DB_PET/','/system_backups/data/SYSTEMDB/','/system_backups/H07/log/SYSTEMDB/','/system_backups/H07/log/DB_PET/',"C:\\test_script\\a\\"]

# print(file_path)
# print(directory_names)
print(100*'*')
print("Validating input data")

if file_path in directory_names and days_to_del > 31:
    print("inputs are valid ")
else :
    print ("Please enter valid day more than 31 days")
    print("invalid data actual destination path")
    exit(1)



now = time.time()
value_count=(now - (days_to_del* 86400) )
directory_path = file_path
 
# # print(now)
# # cutoff = now - (days_to_del * 86400)

# # print(time.ctime(now))
# # print(time.ctime(cutoff))


# #"C:\eSupport\eDriver\\"

# print(file_path)

# # path = "C:\eSupport\eDriver\FileList1.txt"

# # time_new=os.path.getmtime(directory_path)
 
# # print(time.ctime(time_new))
# # print(type(time_new))

# # print(os.getcwd())

count_files= 0
print("Files which are more than {} days are listed below\n--------------------\n\n".format(days_to_del))
for files in os.listdir(directory_path):
    
    if (os.path.getctime(directory_path+files)) <= value_count:
        print ("File {} is last modified on \"{}\"".format(directory_path+files,time.ctime(os.path.getctime(directory_path+files))))
        count_files=count_files+1
    #print(time.ctime(os.path.getmtime(directory_path+files))) 
        os.remove(directory_path+files)
    # if os.stat(os.path.join(path,f)).st_mtime < now - 1 * 86400:
        # print ("file is older")
        
print("\n--------------------\n")
print("{} files were deleted from directory {} on {}".format(count_files,directory_path,time.ctime(time.time())))


print(100*'*')    
#print(os.path.basename("C:\\Users\\vishwas bg\\Documents\\Projects\\"))

# print(os.path.dirname(path))  

# print(file_path)
    
    
    
