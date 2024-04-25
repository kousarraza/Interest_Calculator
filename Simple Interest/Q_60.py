# Q_60. Write a Python program to calculate simple interest 

p=float(input("Enter  the Principle amount: "))
t = float(input("Enter the Time Period: "))  
r = float(input("Enter the Rate of Interest: ")) 

simple_interest=(p*t*r)/100
print("Simple interest is: ",simple_interest)
