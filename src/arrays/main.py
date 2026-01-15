def factorial_array(n: int) -> list[int]:
    """
    Generates a list of factorial values from 0! to n!.
    Parameters:
        n (int): A non-negative integer. The highest factorial to compute.
    Returns:
        list[int]: A list of length n+1 where the k-th element is k!.
                   For example, factorial_array(4) returns [1, 1, 2, 6, 24].
    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError
    l = [0] * (n+1)
    l[0] = 1
    for k in range(1, n+1):
        l[k] = l[k-1] * k
    return l

def min_integer_array(a: list[int]) -> int:
    """
    Returns the minimum value in a list of integers.
    Parameters:
        a (list[int]): A list of integers.
    Returns:
        int: The minimum value in the list.
    Raises:
        ValueError: If the list is empty.
    """
    # if len(a) == 0:              # WPS507: Forbidding unpythonic zero-length comparison. In Python, empty sequences (like lists, strings, or tuples) are "falsy."
    if not a:
        raise ValueError

    m = a[0]
    # for i in range(len(a)):
    #     if a[i] < m:
    #         m = a[i]
    for val in a:
        if val < m:
            m = val
    return m

def min_integers(*numbers: int) -> int:
    """
    Returns the minimum value among a variable number of integers.
    Parameters:
        *numbers (int): A variable number of integers.
    Returns:
        int: The minimum value among the provided numbers.
    Raises:
        ValueError: If no numbers are provided.
    """
    if not numbers:
        raise ValueError
    m = numbers[0]
    for val in numbers[1:]:
        if val < m:
            m = val
    return m

def main():
    print(factorial_array(10))
if __name__ == "__main__":
    main()