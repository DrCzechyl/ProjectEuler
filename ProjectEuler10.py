# Function to check to see if number is prime
def isPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False
    sqr = int(n**0.5) + 1
    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

# Function to find the sum of all primes below 2 million
def sumOfPrimes():
    sum = 0
    for i in range(2, 2000000):
        if isPrime(i):
            sum += i
    return sum

# Print the sum of all primes below 2 million
print(sumOfPrimes())
