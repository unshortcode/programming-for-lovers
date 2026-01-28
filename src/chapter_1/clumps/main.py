def find_clumps(text: str, k: int, window_length: int, t: int) -> list[str]:
    """
    Finds a list of strings representing all k-mers that appear at least t times in a window of         given length in the string.
    Parameters:
    - text (str): An input string.
    - k (int): k-mer's of size k.
    - window_length (int): the size of substrings of text in which we are looking for clumps
    - t (int): The k-mers must appear at least t amount of times.
    Output:
    - list: A list of k-mers that occur at least t times in a window of length window_length in
    text.
    """
    pattern = []
    n = len(text)
    L = window_length
    for i in range(n - L + 1):
        window = text[i : i + L]
        freq_map = frequency_table(window, k)
        for s in freq_map:
            if freq_map[s] >= t and not contains(pattern, s):
                pattern.append(s)
    return pattern

def contains(text, pattern):
    for i in text:
        if i == pattern:
            return True
    return False

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
    for i in range(n-k+1):
        kmer = text[i:i+k]    
        if kmer in table:             # table[kmer] = table.get(kmer, 0) + 1
            table[kmer] += 1
        else:
            table[kmer] = 1
    return table

# Optimize
def find_clumps(text: str, k: int, window_length: int, t: int) -> list[str]:
    patterns = set()
    n = len(text)
    L = window_length

    # Initialize the first window
    first_window = text[0 : L]
    freq_map = frequency_table(first_window, k)
    
    # Check first window for clumps
    for kmer, count in freq_map.items():
        if count >= t:
            patterns.add(kmer)
            
    # Slide the window across the text
    for i in range(1, n - L + 1):
        # K-mer leaving the window
        out_kmer = text[i - 1 : i - 1 + k]
        freq_map[out_kmer] -= 1
        
        # K-mer entering the window
        in_kmer = text[i + L - k : i + L]
        freq_map[in_kmer] = freq_map.get(in_kmer, 0) + 1
        
        if freq_map[in_kmer] >= t:
            patterns.add(in_kmer)
            
    return list(patterns)

def frequency_table(text: str, k: int) -> dict[str, int]:
    table = {}
    for i in range(len(text) - k + 1):
        kmer = text[i:i+k]
        table[kmer] = table.get(kmer, 0) + 1
    return table