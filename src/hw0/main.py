# Implement a function Permutation()
from email._header_value_parser import Value
import time
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

# Implement a function SumProperDivisors()
def sum_proper_divisors(n: int) -> int:
    """
    Return the sum of all proper (positive) divisors of n, i.e., divisors strictly less than n.
    
    Args:
        n: Integer input.
    
    Returns:
        The sum of all positive divisors of n that are < n.
        Returns 0 for n <= 1.
    """
    if n < 1:
        raise ValueError
    elif n == 1:
        return 0
    
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)

# Implement a function SumProperDivisorsOptimize()
def sum_proper_divisors_op(n: int) -> int:
    if n < 0:
        raise ValueError
    if n <= 1: 
        return 0  # ước 1 là chính nó nên phải bỏ đi
    total = 1  # tính sẵn với ước là 1
    for i in range(2, int(n ** 0.5) + 1):  # bỏ đi số 1, và chỉ đi tới căn bậc 2 của n + 1 
        if n % i == 0:
            k = n // i  # cặp số đối n = k * i
            if i == k:  # Số chính phương
                total += i
            else:
                total += i
                total += k
    return total

# Implement a function GCDArray()
def gcd_array(a: list[int]) -> int:
    """
    Return the greatest common divisor (GCD) of all integers in the list.
    
    Args:
        a: A non-empty list of integers (values may be negative or zero).
    
    Returns:
        The non-negative GCD of all numbers in `a`. 
    """
    if not a:
        return ValueError
    m = a[0]
    for val in a[1:]:
        m = gcd(m, val)
        if m == 1:
            return 1
    return m

def gcd(a: int, b: int) -> int:
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a

# Implement a function IsPerfect()
def is_perfect(n: int) -> bool:
    """
    Determine whether an integer n is a perfect number.
    Args:
        n: Integer to test.
    Returns:
        True if n is perfect, False otherwise.
    """
    if n == 1:
        return False
    return n == sum_proper_divisors_op(n)

# Implement a function NextPerfectNumber()
def next_perfect_number(n: int) -> int:
    """
    Return the smallest perfect number strictly greater than n.
    Args:
        n: Integer threshold.
    Returns:
        The least perfect number > n.
    """
    a = n + 1 # Ngay sau n
    while not is_perfect(a):
        a += 1
    return a

def next_perfect_number_op(n: int) -> int:
    p = 2
    while True:
        if is_prime(p):
            mersenne = 2 ** p -1

            if is_prime(mersenne):
                perfect_number = (2 ** (p - 1)) * mersenne
                if perfect_number > n:
                    return perfect_number
        p += 1

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Implement a function ListMersennePrimes()
def list_mersenne_primes(n: int) -> list[int]:
    """
    List all Mersenne primes of the form 2^p - 1 with p ≤ n.
    Args:
        n: Upper bound on the exponent p (non-negative integer).
    Returns:
        A list of all primes of the form 2^p - 1 where p is prime and p ≤ n,
        in increasing order of p.
    """
    prime_list = []
    for p in range(2, n + 1):
        if is_prime(p):
            mersenne = 2 ** p - 1
            if is_prime(mersenne):
                prime_list.append(mersenne)
    return prime_list

# Implement a function NextTwinPrimes()
def next_twin_primes(n: int) -> tuple[int, int]:
    """
    Return the smallest pair of twin primes (p, p+2) such that both p and p+2 are > n.
    Args:
        n: Integer threshold.
    Returns:
        A tuple (p, q) where q = p + 2 are twin primes and p > n.
    """
    p = n + 1
    if p < 3:
        return (3, 5)
    if p % 2 == 0: # p phải là số lẻ
        p += 1
    while True:
        if is_prime(p) and is_prime(p + 2):
            return p, p + 2
        p += 2

# Tìm các cặp số bạn bè 
def amicable_pairs(n: int) -> list[(int, int)]:
    """
    Liệt kê các cặp số bạn bè bé hơn n

    Arg:
    - n: int

    Result:
    List các cặp số bạn bè
    """
    amicable_list = []
    for a in range(220, n):
        b = sum_proper_divisors_op(a)
        if b < n:
            if sum_proper_divisors_op(b) == a and b > a:
                amicable_list.append((a, b))
    return amicable_list

def permutation_op(n: int, k: int) -> int:
    """
    Compute the permutation statistic P(n, k) = n · (n-1) · ... · (n-k+1) = n! / (n-k)!.
    Args:
        n: Total number of distinct objects (non-negative integer).
        k: Number of positions to fill (non-negative integer).
    Returns:
        The number of ways to choose and order k items from n.
    """
    p = 1
    for i in range(k):
        p *= (n - i)
    return p

def combination_op(n: int, k: int) -> int:
    """
    Compute the combination statistic C(n, k) = n! / ((n - k)! * k!) efficiently.
    Args:
        n: Total number of distinct objects (non-negative integer).
        k: Size of the subset to choose (non-negative integer).
    Returns:
        The number of ways to choose k items from n without order.
    """
    if k < 0 or k > n:
        return ValueError
    if k in (0, n):   # Tương tự `k == 0 or k == n`
        return 1

    if k > n // 2:    # Tính đối xứng C(n , k) = C(n, n - k)
        k = n - k

    p = 1
    for i in range(k):
        p = p * (n - i) // (i + 1)
    return p

def main():
    print(combination_op(1000, 998))

if __name__ == "__main__":
    main()