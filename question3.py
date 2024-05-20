#write a program to find the factorial of a nummber

a=int(input("Enter a number: "))
def factorial(a):
    if a==0:
        return 1
    else:
        return a*factorial(a-1)
print(f"The factorial of the given number is {factorial(a)}")