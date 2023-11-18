import unittest
import random

from extractor import evaluate_CWPIH_extractor
from solve_pit import schwartz_zippel_alg

class TestCWPIHExtractor(unittest.TestCase):

    def test_pit_ne(self):
        # h_int ranges from 0 to 2^{2n}-1 and is truly randomly selected
        # we evaluate h all x ranging from 0 to 2^n - 1, counting successes
        n = 8

        # Define our polynomials over the field Z_{2^n}. For n = 8, Z_{256}
        polyA = [1, 2, 3, 4, 5] # polyA(x) = 1 + 2x + 3x^2 + 4x^3 + 5x^4
        polyB = [0, 1, 2, 3, 4] # polyB(x) = 0 + 1x + 2x^2 + 3x^3 + 4x^4
        # Clearly, these are not equal. polyA(0) == 1 != 0 == polyB(0)

        # Select h_int.
        h_int = random.randint(0, (1 << 2*n) - 1)

        num_equalities = 0
        total_attempts = (1 << n)

        for x in range(0, total_attempts):
            hx_h = evaluate_CWPIH_extractor(x, h_int, n)
            hx = hx_h >> n
            result = schwartz_zippel_alg(polyA, polyB, n, hx)
            if result: num_equalities += 1
        
        print(f"Failures: {num_equalities} (of {total_attempts})")
        self.assertTrue(num_equalities < 0.5 * total_attempts)

    def test_pit_e(self):
        # h_int ranges from 0 to 2^{2n}-1 and is truly randomly selected
        # we evaluate h all x ranging from 0 to 2^n - 1, counting successes
        n = 8

        # Define our polynomials over the field Z_{2^n}. For n = 8, Z_{256}
        polyA = [1, 2, 3, 4, 5] # polyA(x) = 1 + 2x + 3x^2 + 4x^3 + 5x^3
        polyB = [257, 258, 259, 260, 261] # polyB(x) = 257 + 258x + 259x^2 + 260x^3 + 261x^4 
        # Clearly, these are equal. polyA(0) == 1 == 257 mod 256 == polyB(0)

        # Select h_int.
        h_int = random.randint(0, (1 << 2*n) - 1)

        num_non_equalities = 0
        total_attempts = (1 << n)

        for x in range(0, total_attempts):
            hx_h = evaluate_CWPIH_extractor(x, h_int, n)
            hx = hx_h >> n
            result = schwartz_zippel_alg(polyA, polyB, n, hx)
            if not result: num_non_equalities += 1
        
        print(f"Failures: {num_non_equalities} (of {total_attempts})")
        self.assertTrue(num_non_equalities < 0.5 * total_attempts)

if __name__ == '__main__':
    unittest.main()