# This code will print a list of all the prime numbers up to 100

def sieve_of_eratosthenes(n):
""" Returns a list of prime numbers up to the given maxmimum number."""
primes = []
for i in range(2, n + 1):
  primes.append(i)

for i in primes:
  for j in range(i * i, n + 1, i):
    if j in primes:
      primes.remove(j)

return primes

if __name__ == "__main__":
  primes = sieve_of_eratosthenes(100)
  print(primes)
