#include <stdlib.h>
#include <stdint.h>

typedef struct {
    uint64_t a0;
    uint64_t a1;
    uint64_t S;
} HashFunction;

void initializeHashFunction(HashFunction *hashFunc, uint64_t a0, uint64_t a1, uint64_t S) {
    hashFunc->a0 = a0 % S;
    hashFunc->a1 = a1 % S;
    hashFunc->S = S;
}

uint64_t evaluateHashFunction(const HashFunction *hashFunc, uint64_t x) {
    return (hashFunc->a0 + hashFunc->a1 * x) % hashFunc->S;
}
