import random
import string

department = ["Marketing", "Accounting", "FinOps"]
department_lower = [dep_name.lower() for dep_name in department]
exit = False

#Funtion to generate random ec2 names
def generate_random_ec2(num_of_ec2, dept_name):
    ec2_names = []
    
    #Concatentes dep-name, random charters from a-z, A-Z and random numbers from 0-1000 to create ec2 name)
    for i in range(num_of_ec2): #Loop to create the number of name specifed by user
        rand_ec2_name = dept_name + "-" + "".join(random.choices(string.ascii_letters, k=5)) + str(random.randint(0,1000))    
        ec2_names.append(rand_ec2_name.capitalize())
        
    #Return list of random ec2 names
    return ec2_names

while exit == False:
    #Ask user for # of EC2s needed and department name
    num_of_ec2 = int(input("How many EC2 instance do you require names for? "))
    dept_name = str(input("Please provide the name of your Department (Type 'Exit' to exit program): ")).lower()
    
    if dept_name.lower() == "exit":
        exit = True

    else:
        if dept_name not in department_lower: #Check if user name provided is in the department list
            print("You did not input an authorized Department. You cannot use this Ec2 Name Generator.")
            print("")

        else: 
            #Call fuction to generate random ec2 names
            ec2_names = generate_random_ec2(num_of_ec2, dept_name)
    
            print("")
            print("Your EC2 names to be used are: ")
            print(ec2_names)
            print("")
