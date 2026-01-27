def another_factorial(n: int) -> int:
    """
    Takes as input an integer n and returns n! = 1*2*...*(n-2)*(n-1)*n using a for loop.
    Parameters:
    - n (int): an integer
    Returns:
    int: n! = 1*2*n*(n-1)*(n-2)*...*2*1
    """
    if n < 0: raise ValueError("Error: negative input given to another_factorial().")

    p = 1
    for i in range(n, 0, -1):
        p *= i
    return p

def sum_even(n: int) -> int:
    """
    Takes as input an integer k and returns the sum of all even positive integers up to and (possibly) including k.
    Parameters:
    - k (int): an integer
    Returns:
    int: sum of all even positive integers up to and (possibly) including k
    """
    if n < 0: raise ValueError
    p = 0
    for i in range (2, n+1, 2):
        p += i
    return p

def main():
    print()
    n = 0
    m = sum_even(n)
    print(m)

def say_hi_n_times(n):
    # print Hello, World! five times
    for _ in range(n):
        print("Hello, World!")

if __name__ == "__main__":
    main()