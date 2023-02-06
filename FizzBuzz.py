exit = False

while exit == False: #keep program running
    try:
        int_num = int(input("Enter an integer value between 1-100: (Type 0 to exit the program): "))

        if int_num == 0:
            print("You have exited the program. Bye.\n")
            exit = True

        elif (int_num < 1) or (int_num > 100): #check is number range is between 1-100
            print("Invalid number range.\n")

        elif (int_num % 3 == 0) & (int_num % 5 == 0): #check is number is a muiltiple of 3 and 5
            print("FizzBuzz.\n")

        elif int_num % 3 == 0: #check is number is a muiltiple of only 3
            print("Fizz.\n")

        elif int_num % 5 == 0: #check is number is a muiltiple of only 5
            print("Buzz.\n")

        else: #show number if number is not a miltiple of either 3 or 5
            print("The number", int_num, "is not a multiple of 3 or 5.\n") 
            
    except ValueError: #catch error if input from user is not a number
        print("This program only accepts numerical numbers.\n")

    except: #catch any unexpected errors
        print("There was an unexpected error that quit the program.\n")
        exit = True
