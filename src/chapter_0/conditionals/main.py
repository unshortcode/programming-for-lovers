def min_2(a: int, b: int) -> int:
    """
    Takes two intergers as input and returns their minimum.

    Parameters:
    - a (int): first interger
    - b (int): second interger

    Returns:
    int: minimum of a and b
    """
    if a > b:
        return b
    else:
        return a

def which_is_greater(x: int, y: int) -> int:
    """
    Takes two integers as input and returns 1 if the first input is larger, -1 if the second input is larger, and 0 if they are equal.

    Parameters:
    - x (int): first integer
    - y (int): second integer

    Returns:
    int: 1 if x is greater than y, -1 if y is greater than x, and 0 if x and y are equal
    """
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

def same_sign(x: int, y: int) -> int:
    """
    Takes two integers as input and returns True if they have the same sign, and False if they have different signs.

    Parameters:
    - x (int): first integer
    - y (int): second integer

    Returns:
    bool: True if x and y have the same sign, False otherwise
    """
    # if x >= 0 and y >= 0:
        # return True
    # elif x <= 0 and y <= 0:
        # return True
    if x * y >= 0:
        return True
    # else:
    return False

def positive_difference(a:int, b:int) -> int:
    """
    Takes two integers as input and returns the absolute value of their difference.

    Parameters:
    - a (int): first integer
    - b (int): second integer
    
    Returns:
    int: positive difference of a and b
    """
    # if a >= b:
    #     return a - b
    # else:
    #     return b -a
    return abs(a - b)
    
def main():
    print("Conditionals in Python.")
    print("The minimum of 3 and 4 is", min_2(3, 4))

if __name__ == "__main__":
    main()
