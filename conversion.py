

'''
conversion from Celsius  to Fahrenheit
C*9/5 +32 = F
conversion from Fahrenheit to Celsius
(F - 32)* 5/9 = C
'''


def conversion(degree, temp): # define the function conversion
                              # where degree is the type C for celsius
                              # or, f for Fahrenheit
                              # and, temp is the value of the temperature
    if degree == 'f':
        C = (temp -32)*5/9
        print(temp, "F converted in C is :", round(C,1))
    elif degree =='c':
        F = temp*9/5 + 32
        print(temp, "C converted in F is :",round(F,1))

    else :
        print("There is no such type of degree: ", degree)

cont = "y"
while cont == "y":
    print('Input the type ')
    deg = input("Enter c for Celsius, or f for Fahrenheit:  ")

    temperature = float(input("Enter the value for temperature: "))
    conversion (deg, temperature) # Call the function conversion
    cont = input(" Enter y if continue, or n if not")
exit