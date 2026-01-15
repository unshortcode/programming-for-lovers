# Implement a function Permutation()
def Permutation(n: int, k: int) -> int:
    """
    Give n and k, calculate the Permutation statistic P(n, k)

    Parameters:
    - n (int): the total number of objects in the set
    - k (int): the number of objects to be ordered (0 <= k <= n)

    Returns:
    int: the total number of Permutations, calculated as n! / (n - k)!
    """
    if k < 0 or k > n:
        raise ValueError
    return int(factorial(n) / factorial(n - k))

def factorial(n: int) -> int:
    """
    Takes as input an integer n and returns n! = 1*2*...*(n-2)*(n-1)*n using a for loop.

    Parameters:
    - n (int): an integer
    
    Returns:
    int: n! = 1*2*n*(n-1)*(n-2)*...*2*1
    """
    if n < 0:
        raise ValueError
    p = 1
    for i in range(1, n + 1):
        p *= i
    return p

# Implement a function Combination()
def Combination(n: int, k: int) -> int:
    """
    Give n and k, calculate the Combination statistic P(n, k)

    Parameters:
    - n (int): the total number of objects in the set
    - k (int): the number of objects to be unordered (0 <= k <= n)

    Returns:
    int: the total number of Combination, calculated as n! / ((n - k) * k!)!
    """
    if k < 0 or k > n:
        raise ValueError
    return int(factorial(n) / (factorial(n - k) * factorial(k)))

def main():
    print(Combination(8, 7))

if __name__ == "__main__":
    main()