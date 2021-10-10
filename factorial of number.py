#Find the factorial of given number
#n!=1*2*3*4*5*6*.....*n
num=float(input("Enter a number:"))

factorial=1

if num==0:
    print("The factorial of 0 is 1")
    
elif num<1:
    print("Factorial does not exist for negative number")
    
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of",num,'is',factorial)
