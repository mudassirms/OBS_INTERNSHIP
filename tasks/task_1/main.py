def sum_of_digits(n):
    return sum(int(digit)for digit in str(abs(n)))
num = int(input("Enter the number:"))
print("Sum of digits:", sum_of_digits(num))









