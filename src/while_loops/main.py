def factorial(n: int) -> int:
    """
    Takes as input an integer n and returns n! = n*(n-1)*(n-2)*...*2*1 using a while loop.
    
    Parameters:
    - n (int): an integer

    Returns:
    int: n! = n*(n-1)*(n-2)*...*2*1
    """
    p = 1
    i = 1
    
    if n < 0:
        raise ValueError("Error: negative input given to factorial().")
    # while i <= n:
    #     p *= i
    #     i += 1
    # return p
    return n*(n+1)//2

def sum_first_n_integers(n: int) -> int:
    """
    Takes as input an integer n and returns the sum of the first n positive integers.

    Parameters:
    - n (int): an integer
    
    Returns:
    int: sum of the first n positive integers
    """
    if n < 0:
        raise ValueError("Error: negative input given to sum_first_n_integers")
    i = 1
    s = 0
    while i <= n:
        s += i
        i += 1
    return s

def main():
    print(sum_first_n_integers(98))

if __name__ == "__main__":
    main()