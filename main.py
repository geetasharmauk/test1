import Temp
o = input("Enter temperature conversion type: ")
if o=="C":
    C = float(input("Enter temperature in Celsius: "))
    Temp.tempF(C)
elif o=="F":
    F = float(input("Enter temperature in Farenheit: "))
    Temp.tempC(F)
else:
    print("invalid input")