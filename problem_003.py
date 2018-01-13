def primeFactors(n):
    divisor = 2
    while n > 1:
        while n % divisor == 0:
            yield divisor
            n //= divisor
        divisor += 1

def largestPrimeFactor(n):
    return max(primeFactors(n))

print(largestPrimeFactor(600851475143))