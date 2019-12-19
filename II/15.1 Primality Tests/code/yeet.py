import math


def gcd(a, b):
    if (a < b):
        return gcd(b, a)
    if (a % b == 0):
        return b
    return gcd(b, a % b)


# utility function to find pow(x, y) under
# given modulo mod
def power(x, y, mod):
    if (y == 0):
        return 1
    temp = power(x, y / 2, mod) % mod
    temp = (temp * temp) % mod
    if (y % 2 == 1):
        temp = (temp * x) % mod
    return temp

def trial_division(n):
    # implements naive trial division to decide whether n is prime
    if n%2==0:
        return False
    for i in range(3, floor(sqrt(n)) + 1,2): # only do odds
        if n % i == 0:
            if n % i == 0:
                return False
    return True


# This function receives an integer n and
# finds if it's a Carmichael number
def car(n):

    # Requires a positive integer.
    if n == 1:
        return True
    elif n % 2 != 0 and all(n % k != 0 for k in range(3, math.ceil(n ** 0.5), 2)):
        return False
    elif all(pow(k, n, n) == k for k in range(1, n)):
        return True
    else:
        return False

def bruh():
    carmichaels = []
    for n in range(1, 10 ** 6 + 1, 2):  # n must be odd
        if n % 1001 == 0:
            print(n)

        if car(n):
            carmichaels.append(n)

    return carmichaels #THJIS is super fast - figure out why

def jacobi(a, n):
    assert (n > a > 0 and n % 2 == 1)
    t = 1
    while a != 0:
        while a % 2 == 0:
            a /= 2
            r = n % 8
            if r == 3 or r == 5:
                t = -t
        a, n = n, a
        if a % 4 == n % 4 == 3:
            t = -t
        a %= n
    if n == 1:
        return t
    else:
        return 0

def jacobi_calculate(a, b):
    result = 1
    while True:
        a = int(a % b)  # step 1

        if a % 2 == 0:  # step 2
            a = int(a / 2)
            if b % 8 == 3 or b % 8 == 5:
                result = -result

        if a == 1:
            break

        if gcd(a, b) != 1:
            result = 0
            break

        if a % 4 == 3 and b % 4 == 3:
            result = -result
        temp = a
        a = b
        b = temp

    return result

def test():
    i=11
    while True:
        i += 1
        if jacobi_calculate(10, i) != jacobi(10, i):
            print(i)