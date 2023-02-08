import os

dict_list = []

for file in os.listdir():
    file_dict = {}
    file_dict['path'] = os.path.dirname(os.path.realpath(file)) + "/" + file
    file_dict['size'] = os.path.getsize(file)
    dict_list.append(file_dict)

print(*dict_list, sep="\n")