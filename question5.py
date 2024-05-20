#write a program to find if the given number is prime no or not

a=int(input("Enter a number: "))
def is_prime(a):
    if a==1:
        return False
    for i in range(2,a):
        if a%i==0:
            return False
    return True
  
if is_prime(a):
    print("Prime number")
else:
    print("Not a prime number")