num = int(input("Enter a number: "))
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num*factorial(num - 1)
fact = factorial(num)
print(f"Factorial of {num} is {fact}")