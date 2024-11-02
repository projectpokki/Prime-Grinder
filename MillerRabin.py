from random import randrange

def MillerRabin(n: int, trials: int) -> bool: #chance of pseudoprime is 0.25**trials
    if (n == 2) or (n == 3):
        return True
    if (n <= 1) or not (n & 1):
        return False
    exp: int = n - 1
    shifts: int = 0
    while not (exp & 1):
        exp >>= 1
        shifts += 1

    for _ in range(trials):
        witness: int = randrange(2, n - 1) #witness must be 1 < x < n-1

        if pow(witness, exp, n) == 1:
            continue #probably prime, skip to next trial
        
        isComposite: bool = True
        for _ in range(shifts):
            if pow(witness, exp, n) == n-1: #probably prime
                isComposite = False
                break
            exp <<= 1
        if isComposite:
            return False

    return True #probably prime

def genPrime(bits: int, rounds: int, millerRabinTrials: int) -> None:
    print(f"finding {bits} bit prime\n")
    for i in range(1, rounds):
        n: int = (randrange(1 << (bits - 3), 1 << (bits - 2)) << 2) + 3
        if MillerRabin(n, millerRabinTrials):
            print(f"FOUND PRIME\n\n{n}\n\nBIN LEN = {int.bit_length(n)}\nDEC LEN = {len(str(n))}")
            with open("foundLargePrimes.txt", "a") as file:
                file.write(str(n) + "\n")
                file.close()
            exit()
    print("NO PRIME FOUND")

genPrime(2048, 5000, 4)
