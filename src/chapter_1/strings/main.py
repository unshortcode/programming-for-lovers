def complement(dna: str) -> str:
    """
    Return the complementary DNA string.

    Args:
        dna: A DNA string.
    Returns:
        The DNA string formed by replacing A with T, T with A,
        C with G, and G with C.
    """
    mapping = {'A': 'T', 'G': 'C', 'T': 'A', 'C': 'G'}
    return ''.join(mapping[base] for base in dna)

def reverse(s: str) -> str:
    """
    Reverse a string.

    Args:
        s: A string.
    Returns:
        The string formed by reversing the order of the symbols of s.
    """
    return ''.join(s[::-1])

def reverse_complement(dna: str) -> str:
    """
    Compute the reverse complement of a DNA string.

    Args:
        dna: A DNA string.
    Returns:
        The reverse complement of the DNA string.
    """
    return reverse(complement(dna))



def main():
    print(reverse('ATGC'))

if __name__ == "__main__":
    main()