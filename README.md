# A Simple Explicit Extractor
## based off the construction of Carter and Wegman

Constructing 2-independent hash functions, as given by Carter and Wegman.

### Technique
- Select a field of size S (prime p given by Carter and Wegman, 2^n given by Lemire and Kaser)
- Choose 2 random numbers modulo S, (a0, a1) [hash family construction]
- Use these numbers as the coefficients for a polynomial degree 1, i.e.
    h(y) = a0 + a1*y mod S
Note that all polynomials degree 2 (mod S) are equally likely, and any degree 2 (mod S) polynomial is uniquely determined 
by any 2-tuple. Therefore any 2-tuple of distinct arguments is equally likely to be mapped to any 2-tuple of hash values.

Let S = 2^n.

This describes a 2-independent (pairwise) collection of hash functions H:
    for every x != x' in {0, 1}^n and y, y' in {0, 1}^n, 
    the probability that h(x) = y AND h(x') = y' for a random h in H is 2^{-2n}

We can describe any hash function h in H by choosing a random string in 2^{2n}. 

This can be shown to describe a randomness extractor, albiet not a useful one. It can be described as follows:

The map x, h -> h(x) | h (where | denotes concatenation) is an extractor. 

In other words, the distribution of h(x) | h (over h in H) is epsilon close to the uniform distribution over 2n bits. 

This is not useful because in order to describe h, we need:
 - n bits of true randomness to select a0
 - n bits of true randomness to select a1

However, it is of theoretical interest and is useful in many settings. 

### Build it yourself
Just compile it normally using your favorite compiler to `hash.so`. If you have GCC:

```
gcc -shared -o hash.so -fPIC hash.c
```