#write a program to find the maximum of two numbers
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
def maximum(a,b):
    if a>b:
        return a
    else:
        return b
      
print(f"The maximum of two numbers is {maximum(a,b)}")
      