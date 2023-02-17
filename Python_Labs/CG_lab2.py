#prompt user for message
message = input("Enter a messsage: ")

#store message index for character in variables
char_f = message[0]
char_l = message[-1]
char_m = message[int(len(message)/2)]

char_even = message[2::2]
char_odd = message[1::2]
char_rev = message[::-1]

#Print information about user message
print("First character: " + char_f)
print("Last character: " + char_l)
print("Middle character: " + char_m)
print("Even index characters: " + char_even)
print("Odd index characters: " + char_odd)
print("Reversed message: " + char_rev)

