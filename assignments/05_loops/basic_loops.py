# Homework Assignment  # 5 - Basic Loops

import math

# highest number to check
n = 100

# list of primes initialization
# entry resembles a prime if primes[i] = 1
primes = [0, 1] * int(n / 2) + [1]
primes[1] = 0
primes[2] = 1

# simple prime sieve
for i in range(3, int(math.sqrt(n)) + 1):
    for j in range(2 * i, n + 1, i):
        primes[j] = 0


# fizz buzz prime
for i in range(1, n + 1):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if primes[i]:
        output += "Prime"
    if output == "":
        output += str(i)
    print(output)
