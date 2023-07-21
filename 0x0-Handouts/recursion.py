def get_recursion_factorial(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * get_recursion_factorial(n-1)
    
def get_iterative_factorial(n):
    if n < 0:
        return -1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
            return fact
        
print(get_recursion_factorial(5))
print(get_iterative_factorial(5))
    