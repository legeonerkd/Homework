def factorial(n: int) -> int:
    if n == 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# make non-recursion implementation
def factorial_var2(n: int) -> int:
    if n == 1:
        return 1

    factorial = 1
    for num in range(2, n+1):
        factorial *= num
    return factorial