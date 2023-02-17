#prompt user for message
message = input("Enter a message: ")

#change string permutation
lower = message.lower()
upper = message.upper()
capital = message.capitalize()
title = message.title()

#split string into list
list_message = message.split()

#sort the list of words in alphabetical order
sorted_list= sorted(list_message)

#print results
print("Lowercase: " + lower)
print("Uppercase: " + upper)
print("Capitalized: " + capital)
print("Title Case: " + title)
print("Words: " + str(list_message))

#print first word and last word 
print("Alphabetic First Word: " + str(sorted_list[0]))
print("Alphabetic Last Word: " + str(sorted_list[-1]))

