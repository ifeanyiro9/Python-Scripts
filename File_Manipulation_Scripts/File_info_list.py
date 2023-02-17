import os

dict_list = []

for file in os.listdir(): #loop through all the files in current path
    file_dict = {}
    file_dict['path'] = os.path.realpath(file) #get path name of file
    file_dict['size'] = os.path.getsize(file) #get size of file
    dict_list.append(file_dict) #add dictionary of file information to list

print(*dict_list, sep="\n") #print each dictionary of file information in new line
