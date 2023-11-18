from typing import List

def polynomial_evaluation(poly: List[int], val: int) -> int:
    return sum(coeff * pow(val, exp) for exp, coeff in enumerate(poly))

def schwartz_zippel_alg(polyA: List[int], polyB: List[int], n_bits: int, s: int) -> bool:
    """
    Applies the Schwartz Zippel Lemma to probabilistically solve the polynomial identity testing problem.

    https://en.wikipedia.org/wiki/Schwartz-Zippel_lemma
    
    Arguments:
        polyA (List[int]): A list of integers describing a polynomial polyA[0] + polyA[1] * x + ...
        polyB (List[int]): A list of integers describing a polynomial polyB[0] + polyB[1] * x + ...
            polyA and polyB must have the same length.
        n_bits (int): Parameter describing field size in bits. Corresponding field is Z_{2^{n_bits}}. Must be positive.
        s (int): (n bits) describing what (random) value (mod 2^{n_bits}) to evaluate polyA and polyB at. 
    
    Returns:
        bool: If polyA == polyB in Z_{2^{n_bits}}, returns True with probability > 1/2.
              If polyA != polyB in Z_{2^{n_bits}}, returns False with probability > 1/2. 
    """

    assert len(polyA) == len(polyB), "polyA and polyB must have the same length."
    assert n_bits > 0, "n_bits must be positive"
    
    s = s % (1 << n_bits)

    res_a = polynomial_evaluation(polyA, s) % (1 << n_bits)
    res_b = polynomial_evaluation(polyB, s) % (1 << n_bits)
    
    return res_a == res_b