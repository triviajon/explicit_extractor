# A Simple Explicit Extractor
## based off the construction of Carter and Wegman

Constructing 2-independent hash functions, as given by Carter and Wegman.

### Explore

In `test_extractor.py` is an example of using the CW-randomness extractor to simulate the randomized algorithm for solving the Polynomial Identity Testing (PIT) problem. The PIT problem checks if two polynomials are equivalent over a field. It is a widely known example of a problem that is in the BPP complexity class, but not in P. In other words, the randomized algorithm here solves the problem with good probability and in polynomial runtime, but currently there are no known derandomized algorithms to solve this problem in polynomial time.  

In the language of randomness extractors: we provide a truly random seed (in this case, a string of bits that correspond to a hash function) and use it partially derandomize the randomized algorithm for solving PIT. With better extractors, we could use a shorter seed and still achieve close to random results. 

### Technique
- Select a field of size ![equation](https://latex.codecogs.com/svg.image?%20S) (prime p given by Carter and Wegman, ![equation](https://latex.codecogs.com/svg.image?%202%5En) given by Lemire and Kaser)
- Choose 2 random numbers modulo ![equation](https://latex.codecogs.com/svg.image?S), (![equation](https://latex.codecogs.com/svg.image?a_0,a_1%20)) [hash family construction]
- Use these numbers as the coefficients for a polynomial degree 1, i.e.
    ![equation](https://latex.codecogs.com/svg.image?h(y)=a_0&plus;a_1y%5Cmod%20S)

Note that all polynomials degree 2 (mod ![equation](https://latex.codecogs.com/svg.image?%20S)) are equally likely, and any degree 2 (mod S) polynomial is uniquely determined 
by any 2-tuple. Therefore any 2-tuple of distinct arguments is equally likely to be mapped to any 2-tuple of hash values.

Let ![equation](https://latex.codecogs.com/svg.image?%20S=2%5En).

This describes a 2-independent (pairwise) collection of hash functions ![equation](https://latex.codecogs.com/svg.image?H):
    ![equation](https://latex.codecogs.com/svg.image?%5Cforall%20x%5Cneq%20x'%5Cin%5C%7B0,1%5C%7D%5En,y,y'%5Cin%5C%7B0,1%5C%7D%5En,)
    the probability that ![equation](https://latex.codecogs.com/svg.image?h(x)=y%5Ccup%20h(x')=y') for a random ![equation](https://latex.codecogs.com/svg.image?h%5Cin%20H) is ![equation](https://latex.codecogs.com/svg.image?2%5E%7B-2n%7D)

We can describe any hash function h in H by choosing a random string of length ![equation](https://latex.codecogs.com/svg.image?2%5E%7B2n%7D). 

This can be shown to describe a randomness extractor, albiet not a useful one. It can be described as follows:

The map ![equation](https://latex.codecogs.com/svg.image?x,h%5Cxrightarrow%7B%7Dh(x)%7Ch) (where | denotes concatenation) is an extractor. 

In other words, the distribution of ![equation](https://latex.codecogs.com/svg.image?h(x)%7Ch) (![equation](https://latex.codecogs.com/svg.image?h%5Cin%20H)) is epsilon close to the uniform distribution over ![equation](https://latex.codecogs.com/svg.image?2n) bits. 

This is not useful because in order to describe ![equation](https://latex.codecogs.com/svg.image?h), we need:
 - ![equation](https://latex.codecogs.com/svg.image?n) bits of true randomness to select ![equation](https://latex.codecogs.com/svg.image?a_0)
 - ![equation](https://latex.codecogs.com/svg.image?n) bits of true randomness to select ![equation](https://latex.codecogs.com/svg.image?a_1)

However, it is of theoretical interest and is useful in many settings. 

### Build it yourself
Just compile it normally using your favorite compiler to `hash.so`. If you have GCC:

```
gcc -shared -o hash.so -fPIC hash.c
```
