from random import randrange

def MillerRabinSingleTest(n: int, witness: int) -> bool:
    exp: int = n - 1

    if pow(witness, exp, n) == 1:
        return True
    
    while exp < n - 1:
        if pow(witness, exp, n) == n - 1:
            return True
        exp <<= 1
    
    return False

def MillerRabin(n: int, trials: int) -> bool: #chance of pseudoprime is 0.25**trials
    for _i in range(trials):
        witness: int = randrange(2, n - 1) #witness must be 1 < x < n-1
        if not MillerRabinSingleTest(n, witness):
            return False
    return True

def genPrime(bits: int, rounds: int, millerRabinTrials: int) -> None:
    print(f"finding {bits} bit prime")
    for _i in range(rounds):
        n: int = (randrange(1 << (bits - 3), 1 << (bits - 2)) << 2) + 3
        if MillerRabin(n, 10):
            print("FOUND PRIME", n, "\nSIZE =", len(str(n)))
            with open("foundLargePrimes.txt", "a") as file:
                file.write(str(n) + "\n")
                file.close()
            exit()
    print("NO PRIME FOUND")

genPrime(4096, 5000, 4)
