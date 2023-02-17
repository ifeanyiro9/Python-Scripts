temp_f = float(input("What temperature (in F) would you like converted to Celcius? "))
temp_c = round((temp_f - 32) * 5/9, 2)

print(str(temp_f) + " F is " + str(temp_c) + " C")

