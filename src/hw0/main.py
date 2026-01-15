# Implement a function Permutation()
from email._header_value_parser import Value
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

# Implement a function Power()
def power(a: int, b: int):
    """
    Compute a raised to the b-th power.

    Args:
        a: Base integer (can be negative, zero, or positive).
        b: Exponent integer (must be non-negative).
    
    Returns:
        The value of a^b. By convention, 0^0 returns 1.
    """
    if b == 0:
        return 1
    if a == 0:
        return 0
    
    c = a
    for _ in range(abs(b) - 1):
        a *= c
    if b > 0:
        return a
    return 1 / a

# Implement a function Power_recursion()
def power_recursion(a: int, b: int):
    if b == 0:
        return 1
    if a == 0:
        return 0
    else:
        return a * power_recursion(a, b - 1)

# Implement a function Power_divine()
def power_divine(a: int, b: int):
    if b == 0:
        return 1
    if a == 0:
        return 0
    
    half_power = power_divine(a, b // 2)
    if b % 2 == 0:
        # Nếu b chẵn: (a^(b/2)) * (a^(b/2))
        return half_power * half_power
    else:
        # Nếu b lẻ: a * (a^(b/2)) * (a^(b/2))
        return a * half_power * half_power

def main():
    print(power(10, 5), power_recursion(10, 5))
    
if __name__ == "__main__":
    main()