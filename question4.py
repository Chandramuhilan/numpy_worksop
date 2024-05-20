#write a program to find the sum of digits of a given number'

a=int(input("Enter a number: "))

def sum_of_digits(a):
    if a==0:
        return 0
    else:
        return a%10 + sum_of_digits(a//10)
      
print(f"The sum of digits of the given number is {sum_of_digits(a)}")