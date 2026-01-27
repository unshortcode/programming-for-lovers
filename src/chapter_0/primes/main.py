import math

def trivial_prime_finder(n: int) -> list[bool]:
    """
    Returns a list of boolean variables storing the primality of each nonnegative integer up to and including n.
    
    Parameters:
    - n (int): an integer
    
    Returns:
    list[bool]: a list of boolean variables storing the primality of each nonnegative integer up to and including n.
    """
    if n < 0:
        raise ValueError
    prime_booleans = [False] * (n + 1)
    for p in range(2, n + 1):
        prime_booleans[p] = is_prime(p)
    return prime_booleans

def is_prime(p: int) -> bool:
    """
    Test if p is prime.

    Parameters:
    - p (int): an integer

    Returns:
    bool: True if p is prime and False otherwise.
    """
    if p < 2:
        return False
    for k in range(2, int(math.sqrt(p)) + 1):  # math.isqrt(p) nearest integer
        if p % k == 0:
            return False
    return True

def sieve_of_eratosthenes(n: int) -> list[bool]:
    """
    Returns a list of boolean variables storing the primality of each nonnegative integer up to and including n, implementing the "sieve of Eratosthenes" algorithm.

    Parameters:
    - n (int): an integer
    
    Returns:
    list: a list of boolean variables storing the primality of each nonnegative integer up to and including n.
    """
    if n < 0:
        raise ValueError
    prime_booleans = [True] * (n + 1)
    
    prime_booleans[0] = False
    prime_booleans[1] = False

    for p in range(2, int(math.sqrt(n)) + 1):
        if prime_booleans[p]:
            prime_booleans = cross_off_multiples(prime_booleans, p)

    return prime_booleans

def cross_off_multiples(prime_booleans: list[bool], p:int) -> list[bool]:
    """
    Returns an updated list in which all variables in the list whose indices are multiples of p (greater than p) have been set to false.
    
    Parameters:
    - prime_booleans (list): a list of boolean variables storing the primality of each nonnegative integer
    - p (int): an integer
    
    Returns:
    list[bool]: a list of boolean variables storing the primality of each nonnegative integer up to and including n with multiples of p (greater than p) set to false.
    """
    n = len(prime_booleans) - 1
    for k in range(2 * p, n + 1, p):
        prime_booleans[k] = False
    return prime_booleans

def list_primes(n: int) -> list[int]:
    """
    List all prime numbers up to and (possibly) including n.
    
    Parameters:
    - n (int): an integer
    
    Returns:
    list[int]: a list containing all prime numbers up to and (possibly) including n.
    """
    prime_lists = []
    prime_booleans = sieve_of_eratosthenes(n)
    for k in range(len(prime_booleans)):
        if prime_booleans[k]:
            prime_lists.append(k)
    return prime_lists

def main():
    print("Primes.")
    prime_list = list_primes(11)
    print(prime_list)

if __name__ == "__main__":
    main()