def factorial(num):
    if(num == 0):
        return 1
    return num * factorial(num - 1)

num = input("Enter the number to find the factorial: ")

print(f"Factorial is {factorial(int(num))}")