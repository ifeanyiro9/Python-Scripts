exit = False

while exit == False:#keep program running
    try:
        num = int(input("How many values should we process (Type 0 to exit the program): "))

        if num == 0:
            print("You have exited the program. Bye.\n") #option to exit code
            exit = True

        elif (num >= 1) & (num <= 100): #check is number range is between 1-100
            for value in range(1, num +  1):

                if (value % 3 == 0) & (value % 5 == 0): #check if number is a muiltiple of 3 and 5
                    print("FizzBuzz.\n")

                elif value % 3 == 0: #check if number is a muiltiple of only 3
                    print("Fizz.\n")

                elif value % 5 == 0: #check if number is a muiltiple of only 5
                    print("Buzz.\n")

                else: #show number if number is not a miltiple of either 3 or 5
                    print(value, "\n") 

        else:
            print("Invalid number range. Enter a valid number between 1 and 100\n")
        
    except ValueError: #catch error if input from user is not a number
        print("This program only accepts numerical numbers.\n")

    except: #catch any unexpected errors
        print("There was an unexpected error that quit the program.\n")
        exit = True