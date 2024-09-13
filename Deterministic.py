from time import time

def isPrime(n):
  for factor in usedPrimes:
    if factor > int(n ** 0.5):
      return True
    if not (n % factor):
      return False
  return True
 
def getDeltaPattern(n, Kn, fileToUse):
  newDeltaPattern = []
  lastValue = -1
  #with open(fileToUse, "r") as file:
  primesNeeded = primes[:n]
    # primesNeeded = file.read().split("\n")[:n]
  for i in range(1, Kn):
    if all(i % int(prime) for prime in primesNeeded):
      newDeltaPattern.append(i - lastValue)
      lastValue = i
  return newDeltaPattern

def findPrimes(nMax, fileToUse):
  startTime = time()
  global primes
  global usedPrimes

  primes = [2]

  primeRoot = 2
  usedPrimes = []
  usedPrimesRemovedNumbers = 0
  nonprimeCount = 0
  valuesChecked = 0
  n = 3
  newPrimes = []
  
  deltaStage = 0
  deltaPattern = [2]
  deltaProduct = 6
  deltaIndex = 0

  with open(fileToUse, mode="w") as file:
    file.write("2\n")
      
  while n <= nMax:
    #check prime
    valuesChecked += 1
    #print(n, usedPrimes, modTable[n % len(modTable)])
    if isPrime(n):
      primes.append(n)
      newPrimes.append(str(n))
      if n >= primeRoot ** 2:
        usedPrimes.append(primes[len(usedPrimes) + usedPrimesRemovedNumbers + 1])
        primeRoot = usedPrimes[-1]
      if not (len(primes) & 0xfff):
        print(f"{len(primes)}th prime found, value {n}, {(100*n)/nMax}% done")
        with open(fileToUse, mode="a") as file:
          file.write("\n".join(newPrimes) + "\n")
        newPrimes = []
    else:
      nonprimeCount += 1

    #change delta pattern, generalise this
    if n + 1 >= deltaProduct:
      print(f"delta stage to {deltaStage + 2}, delta product {deltaProduct}")
      deltaPattern = getDeltaPattern(deltaStage + 2, deltaProduct, fileToUse)
      deltaProduct *= primes[deltaStage + 2]
      deltaStage += 1
      usedPrimes = usedPrimes[1:]
      usedPrimesRemovedNumbers += 1

    #increment n
    n += deltaPattern[deltaIndex]
    deltaIndex = (deltaIndex + 1) % len(deltaPattern)
    
  print(f"\nprimes found = {len(primes)}\ncomposites checked = {nonprimeCount}\ntotal numbers checked = {valuesChecked}")
  print("time taken", (time() - startTime) * 1000)

nMax = int(input("Find primes up to: "))
fileToUse = input("Path of file to use: ")
findPrimes(nMax, fileToUse)
