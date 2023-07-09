# this code will print true if the number 100 is probably prime, false otherwise
def miller_rabin_primality_test(n, k):
  """ Returns True if the number is probably prime, False otherwise."""
  if n < 2:
    return False
elif n == 2:
  return True
else: 
  for i in range(k):
    a = randint(2, n - 1)
    if pow(a, n - 1, n) != 1:
      return False

  return True

if __name__ == "__main__"
  n = 100
  k = 10
  is_prime = miller_rabin_primality_test(n, k)
  print(is_prime)
