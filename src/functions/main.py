def sum_two_ints(a: int, b: int) -> int:
    """
    Add two integers and return their sum.

    Parameters:
    - a (int): an input integer
    - b (int): an input integer

    Returns:
    int: a + b
    """
    
    return a + b

def double_and_duplicate(x: float) -> tuple[float, float]:
    """
    Double the input variable and return two copies of it.

    Parameters:
    - x (float): an input float

    Returns:
    tuple[float, float]: Two copies of 2 * x.
    """

    return 2 * x, 2 * x

def add_one(k: int) -> int:
    """
    Add one to the input variable k and return the result.

    Parameters:
    - k (int): an input integer

    Returns:
    int: k + 1
    """

    k = k + 1
    return k

def main():
    m = 17
    print(add_one(m))
    print(m)

if __name__ == '__main__':
    main()