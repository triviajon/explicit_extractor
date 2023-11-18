import ctypes

class HashFunction(ctypes.Structure):
    _fields_ = [("a0", ctypes.c_uint64), ("a1", ctypes.c_uint64), ("S", ctypes.c_uint64)]

# Load the C library, assuming we've compiled the code to hash.so
hash_lib = ctypes.CDLL("./hash.so") 

def initialize_hash_function(a0, a1, S):
    hash_func = HashFunction(a0, a1, S)
    hash_lib.initializeHashFunction(ctypes.byref(hash_func), a0, a1, S)
    return hash_func

def evaluate_hash_function(hash_func, x):
    return hash_lib.evaluateHashFunction(ctypes.byref(hash_func), x)

class CarterWegmanPairwiseIndependentHash:
    def __init__(self, a0: int, a1: int, S: int):
        """
        As described above: generate an object to compute 
            the simple hash h(x) = a0 + a1 * x mod S, where S is a prime power.

        Example usage is as follows:
            >>> from hash_wrapper import CarterWegmanPairwiseIndependentHash
            >>> h = CarterWegmanPairwiseIndependentHash(a0=13, a1=111, S=256)
            >>> h(42)
            67
        """
        assert a0 >= 0 and isinstance(a0, int), "a0 must be a non-negative integer."
        assert a1 >= 0 and isinstance(a1, int), "a1 must be a non-negative integer."
        assert S  >  0 and isinstance(S, int), "S must be a positive integer."

        self.a0 = a0
        self.a1 = a1
        self.S = S
        self.h = initialize_hash_function(a0, a1, S)

    def __repr__(self):
        return f"CarterWegmanPairwiseIndependentHash(a0={self.a0}, a1={self.a1}, S={self.S})"
    
    def __call__(self, x):
        return evaluate_hash_function(self.h, x)
