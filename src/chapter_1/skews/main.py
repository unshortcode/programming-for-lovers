def skew(symbol: str) -> int:
    """
    skew returns 1 or -1 if the given single character string is either G or C respectively (case-       insensitive), otherwise returns zero. 
    Throws an error if the given string does not have a length of one.
    Parameters:
    - symbol (str): A given one character string.
    Returns:
    - int: The symbol's respective skew score.
    """
    if symbol == "G":
        return 1
    elif symbol == "C":
        return -1
    return 0

def skew_array(genome: str) -> list[int]:
    """
    skew_array returns the list that represents the skew at each position of the genome. That is,       the i-th position in the list is the skew at the i-th position of the genome.
    Parameters:
    - genome (str): A genome string.
    Returns:
    - list[int]: A list representing the skew of the genome string.
    """
    n = len(genome)
    array = [0] * (n + 1)
    array[0] = 0
    for i in range(1, n + 1):
        array[i] = array[i - 1] + skew(genome[i - 1])
    return array

def minimum_skew(genome: str) -> list[int]:
    """
    minimum_skew finds the list of integers representing all integer indices that minimizes the skew     of the genome text.
    Parameters:
    - genome (str): A genome string.
    Returns:
    - list[int]: A list of indices that minimize the skew value of the genome text.
    """
    array = skew_array(genome)
    minimum = min(array)
    return [i for i, val in enumerate(array) if val == minimum]