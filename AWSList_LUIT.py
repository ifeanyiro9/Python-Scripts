#Empty list of AWS Services
Main_AWS_Services = []

#A list of my Favorite AWS Services
Fav_AWS_Services = ["DynamoDB", "Lambda", "RDS", "EC2", "S3", "Cognito", "IAM", "Cloudformation", "Athena", "RedShift"]

#Append my favorite AWS Services to the Main_AWS_Services list
for services in Fav_AWS_Services:
    Main_AWS_Services.append(services)

#Print the length of the Main AWS Services List and list the services in the list
print("The length of the Main AWS Services List is " + str(len(Main_AWS_Services)) + " and the Services in the list are: ")
print(Main_AWS_Services)

#Pop out two services from the Main_AWS_Services list!!!
Main_AWS_Services.pop(5)
Main_AWS_Services.pop(8)
print("")
#Print the new length of the Main AWS Services List and list the services left in the list
print("After removing two services from the list, the new length of the Main AWS Services List is " + str(len(Main_AWS_Services)) + " and the new Services in the list are: ")
print(Main_AWS_Services)




