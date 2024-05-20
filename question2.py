# find if the given number is a palindrome or not?
a=int(input("Enter a number: "))

def is_palindrome(a):
    return str(a) == str(a)[::-1]
  
if is_palindrome(a):
    print("Palindrome")
else:
    print("Not Palindrome")