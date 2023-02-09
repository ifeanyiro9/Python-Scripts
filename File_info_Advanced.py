import os

dict_list = []

def extract_info(path = '.'): #function to extract file info, defaulted to present working directory if path is not passed
    dict_list = []

    for root, dirs, files in os.walk(path): #recursively iterate over all files/directiories in path directory
        for file_name in files:
            file_dict = {}
            file_dict['path'] = os.path.join(root, file_name) #get path name of file
            file_dict['size'] = os.path.getsize(os.path.join(root, file_name)) #get file size
            dict_list.append(file_dict) #appends file info dictionary to the list
    
    return dict_list #returns list

exit = False

while exit == False: #keep program running
    try:
        path = input("Type in a path or press 'Enter' for present working directory. (Type 'Exit' to exit the program): ") #give user option to choose path to get information from
        
        if path.lower() == "exit": #option to exit program
            exit =  True

        elif path == "": #default to present working directory if no path entered
            info = extract_info()
            print(*info, sep="\n")

        else:
            info = extract_info(path) #pass custom path to function
            print(*info, sep="\n")
            
    except: #catch unexpected errors
        print("There was an issue processing your path, please try again with a correct path.")

