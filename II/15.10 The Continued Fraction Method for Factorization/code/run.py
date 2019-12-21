import random
from math import floor, sqrt


def B_smooth(B, N):
    factorization = []
    for prime in B:
        while N % prime == 0:
            factorization.append(prime)
            N = N / prime
    if N == 1:
        return factorization
    else:
        return False


def modular_multiply(x, y, mod, result):
    #if calling directly put result = 0
    if x * y > 10 ** 15:
        x = x % mod
        # If y odd, add 'x' to result
        if (y % 2 == 1):
            result = (result + x) % mod
        x = (x * 2) % mod
        y //= 2  # floor y/2
        result = modular_multiply(x, y, mod, result)
    else:
        return (result + (x * y)) % mod

    return result % mod


def q1():
    # the first result is wrong because of 0 being a 1 digit number - wont bother fixing
    B = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    results = []
    for d in range(1, 20):
        print(d)
        if d <= 6:
            results.append([0, 10 ** d - 10 ** (d - 1)])
            for N in range(10 ** (d - 1), 10 ** d):
                if B_smooth(B, N):
                    results[d - 1][0] += 1
        else:
            results.append([0, 900000])
            for trial in range(900000):
                N = random.randrange(10 ** (d - 1), 10 ** d)
                if B_smooth(B, N):
                    results[d - 1][0] += 1

    probs = []
    for result in results:
        probs.append(result[0] / result[1])

    return results, probs


def sqrt_cont_frac(N):
    # returns the fixed part, and the repeated part of the continued fraction
    r = [0]
    s = [1]
    a = []

    n = 0

    while True:
        xn = (r[n] + sqrt(N)) / s[n]
        new_a = int(floor(xn))
        a.append(new_a)

        if xn == new_a:
            return a, [], r, s

        new_r = a[n] * s[n] - r[n]
        new_s = (N - r[n] ** 2) / s[n] - (a[n] ** 2) * s[n] + 2 * r[n] * a[n]

        for i in range(len(r)):
            if r[i] == new_r and s[i] == new_s:
                # in this case x_n+1 = x_i so a_i, up to a_n marks the beginning of the repeated bit
                fixed = a[:i]
                repeated = a[i:]
                return fixed, repeated, r, s

        r.append(new_r)
        s.append(new_s)
        n += 1


def convergents(a):
    p = [a[0], a[1] * a[0] + 1]
    q = [1, a[1]]

    n = 2
    while n < len(a):
        p.append(a[n] * p[n - 1] + p[n - 2])
        q.append(a[n] * q[n - 1] + q[n - 2])
        n += 1
    return p, q


def q2i():
    for N in range(51):
        fixed, repeated, r, s = sqrt_cont_frac(N)
        string = str(N) + ") "
        for i in fixed:
            string += str(i) + ", "
        string = string[:-2] + " : "
        for i in repeated:
            string += str(i) + ", "
        string = string[:-2]

        print(string)


def q2ii():
    max_rs = []
    novera = []
    noverb = []
    for N in range(1, 1000):
        fixed, repeated, r, s = sqrt_cont_frac(N)
        a = max(r)
        b = max(s)
        if a == 0:
            a = 1
        if b == 0:
            b = 1
        novera.append(sqrt(N) / a)
        noverb.append(sqrt(N) / b)

        print(N, a, b, N / a, N / b)
    print(min(novera), max(novera))
    print(min(noverb), max(noverb))
    print(novera)
    print(noverb)


def q3():
    for N in [3, 5, 7, 12, 31]:
        fixed, repeated, r, s = sqrt_cont_frac(N)
        a = fixed
        for i in range(10):
            a = a + repeated
        a = a[:10]
        p, q = convergents(a)
        string = str(N) + " [" + str(len(repeated)) + "]) "
        for i in range(len(p)):
            string += str(p[i] ** 2 - N * q[i] ** 2) + ", "
        string = string[:-2]
        print(string)


def verify_large_pell(x, y, N):
    primes = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
              107, 109, 113]

    def one_prime_calc(x, y, N, p):
        xsquared = modular_multiply(x, x, p, 0)
        y_squared = modular_multiply(y, y, p, 0)
        n_y_squared = modular_multiply(N, y_squared, p, 0)
        return (xsquared - n_y_squared) % p

    if one_prime_calc(x, y, N, 2) == 0:
        return False

    threeresult = one_prime_calc(x, y, N, 3)

    if threeresult == 1:
        expected_result = 1
    elif threeresult == 2:
        expected_result = -1
    else:
        return False

    for prime in primes:
        if one_prime_calc(x, y, N, prime) != expected_result % prime:
            return False

    return expected_result

def q3ii():
    for N in range(500,551): #change the range here
        if floor(sqrt(N))==sqrt(N):
            print(str(N)+") has no solutions (square)")
            continue
        fixed, repeated, r, s = sqrt_cont_frac(N)
        a = fixed+repeated+repeated # i know there will be a solution within the first 2 repeated convergents so wont do more
        p,q=convergents(a)
        for i in range(len(p)):
            if verify_large_pell(p[i],q[i],N)==1:
                print(str(N)+") ("+str(p[i])+","+str(q[i])+")")
                break



