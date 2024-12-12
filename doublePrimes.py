# Esse programa serve para verificar quais são os números duplo primos (que o número e o seu avesso são primos) até uma certa faixa.
n = int(input())
primes = []
doublePrimes = []

for possiblePrime in range(2, n):
  isPrime = True
  for num in range(2, possiblePrime):
    if possiblePrime % num == 0:
      isPrime = False
  if isPrime:
    primes.append(possiblePrime)
  
def doublePrime():
  for possibleDoublePrime in primes:
    primeString = str(possibleDoublePrime)
    reversedPrime = primeString[::-1]
    intPrime = int(reversedPrime)
    isPrime = True
    for num in range(2,possibleDoublePrime):
      if intPrime % num == 0:
        isPrime = False
    if isPrime:
      doublePrimes.append(possibleDoublePrime)
    
  print(f'Lista de números duplamente primos: {doublePrimes}')

doublePrime()
