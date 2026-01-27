def starting_indices(pattern: str, text: str) -> list[int]:
    """
    starting_indices returns the list containing all the starting positions of pattern in text.
    Parameters:
    - pattern (str): A given substring.
    - text (str): A given superstring.
    Returns:
    - list[int]: A list containing the starting positions of pattern in text (indices).
    """
    n = len(text)
    k = len(pattern)
    return [i for i in range(n - k + 1) if text[i:i + k] == pattern]

def pattern_count(pattern: str, text: str) -> int:
    """
    pattern_count finds the number of times the substring occurs in a given text string.
    Parameters:
    - pattern (str): The substring we are searching for in text.
    - text (str): The parent text string we are searching against.
    Returns:
    - int: The number of times that pattern occurs in text, including overlaps.
    """
    return len(starting_indices(pattern, text))

def frequency_table(text: str, k: int) -> dict[str, int]:
    """
    frequency_table finds the frequencies of each k-mer occurring in a given text, including overlaps.
    Parameters:
    - text (str): The string text to search for k-mers.
    - k (int): The size of the k-mers.
    Returns:
    - dict[str, int]: The dictionary of k-mers to their frequencies in the given text string, including overlaps.
    """
    n = len(text)
    table = {}
    for i in range(i:n-k+1):
        kmer = text[i:i+k]    
        if kmer in table:             # table[kmer] = table.get(kmer, 0) + 1
            table[kmer] += 1
        else:
            table[kmer] = 1
    return table

def find_frequent_words(text: str, k: int) -> list[str]:
    """
    find_frequent_words returns a list containing the most frequent k-mers occurring in text,           including overlaps.
    Parameters:
    - text (str): A given text for the function.
    - k (int): The size of the k-mers.
    Returns:
    - The list of the most frequent k-mers occurring in text, including overlaps.
    """
    table = frequency_table(text, k)
    max_count = max(table.values())

    return [kmer for kmer, count in table.items() if count == max_count]

def max_map_value(dictionary: dict[str, int]) -> int:
    """
    max_map_value finds the maximum value of a given dictionary.
    Parameters:
    - dictionary: A dictionary that has integers as values.
    Returns:
    - int: The maximum value in the given dictionary.
    """
    return max(dictionary.values())

def main():
    print()

if __name__ == '__main__':
    main()