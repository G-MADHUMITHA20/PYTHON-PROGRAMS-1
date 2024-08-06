print("OPTIONS:\n1)fahrenheit to celsius\n2)celsius to fahrenheit")
option=int(input("enter option:"))
if(option==1):
           Fahrenheit=float(input("Fahrenheit="))
           convertcelsius=(Fahrenheit-32)*5/9
           print("Celsius= ",convertcelsius)
elif(option==2):
           Celsius=float(input("Celsius= "))
           convertfahrenheit=(celsius*9/5)+32
           print("Fahrenheit= ",convertfahrenheit)
else:
    print("Invalid option")
