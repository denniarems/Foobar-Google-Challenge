def isPrime(num):
    if num == 2:
        return True
    elif num < 2 or not num % 2:
        return False
    for i in range(3, int(num ** .5 + 1), 2):
        if not num % i:
            return False
    return True


def generatePrimes(n):
    primes = [2, ]
    noOfPrimes = 1
    nextPrime = 3
    while noOfPrimes < n:
        if isPrime(nextPrime):
            primes.append(nextPrime)
            noOfPrimes += 1
        nextPrime += 2
    return primes


def solution(i):
    primeList = generatePrimes(i+5)
    minionsId = ("".join(map(str, primeList)))
    return minionsId[i:i+5]
