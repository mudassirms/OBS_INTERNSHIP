def check_palindrom(n):
    n = n.replace(" "," ").lower()
    return n == n[::-1]

name = input("Enter the string: ")
if check_palindrom(name):
    print("Its a Palindrome")
else:
    print("Not a Palindrome")
