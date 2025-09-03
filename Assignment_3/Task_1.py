a=int(input("Enter a number: "))
def factorial(a):
    if a==0:
        return 1
    else:
        return a*factorial((a-1))
print(f"Factorial of {a} is:", factorial(a))

    