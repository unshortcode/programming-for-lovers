import time
def trivial_gcd(a: int, b:int) -> int:
    """

    """
    d = 1
    m = min(a, b)
    if a == 0 or b == 0:
        return max(a, b)
    for p in range(1, m + 1):
        if a % p == 0 and b % p == 0:
            d = p
    return d

def euclid_gcd(a: int, b: int) -> int:
    """
    Returns the GCD of two integers by applying Euclid's algorithm.
    Parameters:
    - a (int): first integer
    - b (int): second integer
    Returns:
    int: GCD of a and b
    """
    if a == 0 or b == 0:
        return max(a, b)
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def main():
    x = 37820265
    y = 27314794
    # timing trivial_gcd
    start = time.time()
    trivial_gcd(x, y)
    elapsed = time.time() - start
    print(elapsed)
    start = time.time()
    euclid_gcd(x, y)
    elapsed_euclid = time.time() - start
    print(f"euclid_gcd took {elapsed_euclid:.6f} seconds")

if __name__ == "__main__":
    main()