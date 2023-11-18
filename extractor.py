from hash_wrapper import CarterWegmanPairwiseIndependentHash

def evaluate_CWPIH_extractor(x: int, h_int: int, n: int) -> int:
    """
    Evaluates a Carter-Wegman Pairwise Independent hash function [ x, h -> h(x) | h ] at x.
    The function h is described by the string h_int, 0 <= h_x < 2^{2n} (i.e., 2n bits long) which
    describe a0 and a1 of the CWPIH function (each n bits long, over the field Z_{2^{n}}). 

    Example usage:
        >>> import extractor as e
        >>> e.evaluate_CWPIH_extractor(42, 3439, 8)
        67
    Note that this is equivalent to the example usage seen in hash_wrapper.py.

    Arguments:
        x (int): The value to evaluate the hash function at h (mod 2^{n}).
        h_int (int): An integer less than 2n bits long (0 <= h_int < 2^{2n}) describing h.
            I.e., a0 | a1 = h_int, where | denotes concatenation.
        n (int): Parameter describing field size in bits, as described above. Must be positive.

    Returns:
        int: h(x) | h_int
    """
    assert 0 <= h_int < 2**(2 * n), "h_int must be less than 2n bits long (0 <= h_int < 2^{2n})"
    assert n > 0, "n must be positive."


    x = x % 2**n
    a0 = h_int >> n
    a1 = h_int & ((1 << n) - 1)

    h = CarterWegmanPairwiseIndependentHash(a0, a1, 2**n)

    return (h(x) << n) | h_int