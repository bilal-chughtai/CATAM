import random
import time
from collections import defaultdict
from math import floor, sqrt, gcd, ceil
second_trial_division_used = False

def trial_division(n):
    # implements naive trial division to decide whether n is prime
    if n % 2 == 0:
        return False

    for i in range(3, floor(sqrt(n)) + 1, 2):  # only do odds
        if n % i == 0:
            return False
    return True


def modular_multiply(x, y, mod, result):
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


def modular_exponent(base, exponent, modulo):
    # takes the exponent without overflow issues, by doing so in powers of 2 at a time

    # now generate our actual base^exponent
    result = 1
    base = base % modulo
    while exponent > 0:
        if exponent % 2 == 1:
            result = modular_multiply(result, base, modulo, 0)
        exponent = floor(exponent / 2)
        base = modular_multiply(base, base, modulo, 0)
    return result


def fermat_test(a, N):
    if modular_exponent(a, N - 1, N) == 1:
        return True
    else:
        return False


def jacobi_calculate(a, b):
    result = 1
    while True:
        a = int(a % b)  # step 1

        if a % 2 == 0:  # step 2
            a = floor(a / 2)
            if b % 8 == 3 or b % 8 == 5:
                result = -result
            continue

        if a == 1:
            break

        if gcd(a, b) != 1:
            result = 0
            break

        if a % 4 == 3 and b % 4 == 3:
            result = -result
        a, b = b, a

    return result


def euler_test(a, N):
    result = modular_exponent(a, int((N - 1) / 2), N)
    if result==1 or result==N-1:
        if result == jacobi_calculate(a, N) % N:
            return True
    return False


def strong_test(a, N):
    r = 0
    s = N - 1
    while True:
        if s % 2 == 0:
            r += 1
            s = s / 2
        else:
            break

    s = int(s)

    temp = modular_exponent(a, s, N)
    if temp == 1 or temp == N - 1:
        return True
    else:
        for k in range(1, r):  # k is the power of 2 in the test
            if modular_exponent(a, (2 ** k) * s, N) == N - 1:
                return True

    # if none of these are true return false
    return False


def q1():
    ranges = [range(1900, 2000), range(1294268500, 1294268701)]
    primes = defaultdict(list)

    for testrange in range(len(ranges)):
        primes[testrange] = []
        for n in ranges[testrange]:
            if trial_division(n):
                primes[testrange].append(n)

    return primes


def q2():
    ranges = [range(1900, 2000), range(1294268500, 1294268701)]
    fermat_passed_a = defaultdict()  # holds the numbers passing the fermat test for each a
    fermat_passed = defaultdict()  # holds the numbers passing the fermat test for all a
    for testrange in range(len(ranges)):
        fermat_passed_a[testrange] = defaultdict()
        for a in range(2, 14):
            print(a)
            fermat_passed_a[testrange][a] = []
            for n in ranges[testrange]:
                if fermat_test(a, n):
                    fermat_passed_a[testrange][a].append(n)

    return fermat_passed_a


def q3i():
    pseudoprimes_base_two = []
    for n in range(1, 10 ** 6 + 1):
        if fermat_test(2, n) and not trial_division(n):
            pseudoprimes_base_two.append(n)

    def isCarmichael(n):
        composite = False
        for a in range(3, ceil(n / 2) + 1):  # we've already checked 2
            if gcd(a, n) == 1:
                if not fermat_test(a, n):
                    return False
            else:
                composite = True
        return composite  # if it gets here it must have passed all the rounds of testing

    carmichaels = []
    for n in pseudoprimes_base_two:
        if isCarmichael(n):
            carmichaels.append(n)
            print(n)

    return carmichaels, pseudoprimes_base_two


def q3ii():
    sarrus = [341, 561, 645, 1105, 1387, 1729, 1905, 2047, 2465, 2701, 2821, 3277, 4033, 4369, 4371, 4681, 5461, 6601,
              7957, 8321, 8481, 8911, 10261, 10585, 11305, 12801, 13741, 13747, 13981, 14491, 15709, 15841, 16705,
              18705, 18721, 19951, 23001, 23377, 25761, 29341, 30121, 30889, 31417, 31609, 31621, 33153, 34945, 35333,
              39865, 41041, 41665, 42799, 46657, 49141, 49981, 52633, 55245, 57421, 60701, 60787, 62745, 63973, 65077,
              65281, 68101, 72885, 74665, 75361, 80581, 83333, 83665, 85489, 87249, 88357, 88561, 90751, 91001, 93961,
              101101, 104653, 107185, 113201, 115921, 121465, 123251, 126217, 129889, 129921, 130561, 137149, 149281,
              150851, 154101, 157641, 158369, 162193, 162401, 164737, 172081, 176149, 181901, 188057, 188461, 194221,
              196021, 196093, 204001, 206601, 208465, 212421, 215265, 215749, 219781, 220729, 223345, 226801, 228241,
              233017, 241001, 249841, 252601, 253241, 256999, 258511, 264773, 266305, 271951, 272251, 275887, 276013,
              278545, 280601, 282133, 284581, 285541, 289941, 294271, 294409, 314821, 318361, 323713, 332949, 334153,
              340561, 341497, 348161, 357761, 367081, 387731, 390937, 396271, 399001, 401401, 410041, 422659, 423793,
              427233, 435671, 443719, 448921, 449065, 451905, 452051, 458989, 464185, 476971, 481573, 486737, 488881,
              489997, 493697, 493885, 512461, 513629, 514447, 526593, 530881, 534061, 552721, 556169, 563473, 574561,
              574861, 580337, 582289, 587861, 588745, 604117, 611701, 617093, 622909, 625921, 635401, 642001, 647089,
              653333, 656601, 657901, 658801, 665281, 665333, 665401, 670033, 672487, 679729, 680627, 683761, 688213,
              710533, 711361, 721801, 722201, 722261, 729061, 738541, 741751, 742813, 743665, 745889, 748657, 757945,
              769567, 769757, 786961, 800605, 818201, 825265, 831405, 838201, 838861, 841681, 847261, 852481, 852841,
              873181, 875161, 877099, 898705, 915981, 916327, 934021, 950797, 976873, 983401, 997633]
    carmichael = [561, 1105, 1729, 2465, 2821, 6601, 8911, 10585, 15841, 29341, 41041, 46657, 52633, 62745, 63973,
                  75361, 101101, 115921, 126217, 162401, 172081, 188461, 252601, 278545, 294409, 314821, 334153, 340561,
                  399001, 410041, 449065, 488881, 512461, 530881, 552721, 656601, 658801, 670033, 748657, 825265,
                  838201, 852841, 997633]
    to_test = [x for x in sarrus if x not in carmichael]

    largestbase = 3
    culprits = []
    for n in to_test:
        a = 3
        while True:
            if fermat_test(a, n):
                a += 1
            else:
                if a > largestbase:
                    largestbase = a
                    culprits = [n]
                elif a == largestbase:
                    culprits.append(n)
                break

    return largestbase, culprits


def q4i():
    pseudoprimes_base_two = []
    for n in range(3, 10 ** 6 + 1, 2):
        if euler_test(2, n) and not trial_division(n):
            pseudoprimes_base_two.append(n)

    print(pseudoprimes_base_two)

    def isAbsoluteEuler(n):
        composite = False
        for a in range(2, n):
            if gcd(a, n) == 1:
                if not euler_test(a, n):
                    return False
            else:
                composite = True
        return composite  # if it gets here it must have passed all the rounds of testing

    absolute_euler_pseudoprimes = []
    for n in pseudoprimes_base_two:
        if isAbsoluteEuler(n):
            absolute_euler_pseudoprimes.append(n)

        # pseudoprime_for_all_coprime_a = True
        # composite = False
        # for a in range(2, n + 1):
        #     if gcd(a, n) != 1:
        #         composite = True
        #         pass
        #     elif not euler_test(a, n):
        #         pseudoprime_for_all_coprime_a = False
        #         break

    return absolute_euler_pseudoprimes, pseudoprimes_base_two


def q4ii():
    to_test = [561, 1105, 1729, 1905, 2047, 2465, 3277, 4033, 4681, 6601, 8321, 8481, 10585, 12801, 15841, 16705, 18705,
               25761, 29341, 30121, 33153, 34945, 41041, 42799, 46657, 49141, 52633, 62745, 65281, 74665, 75361, 80581,
               85489, 87249, 88357, 90751, 104653, 113201, 115921, 126217, 129921, 130561, 149281, 158369, 162401,
               164737, 172081, 188057, 196093, 208465, 215265, 220729, 223345, 233017, 252601, 253241, 256999, 266305,
               271951, 278545, 280601, 294409, 314821, 323713, 334153, 340561, 348161, 357761, 390937, 399001, 410041,
               427233, 448921, 449065, 458989, 476971, 486737, 488881, 489997, 493697, 514447, 526593, 530881, 552721,
               580337, 588745, 625921, 635401, 647089, 656601, 658801, 665281, 670033, 683761, 711361, 721801, 741751,
               745889, 748657, 800605, 818201, 825265, 838201, 838861, 841681, 852481, 852841, 873181, 875161, 877099,
               916327, 976873, 983401, 997633]
    print(len(to_test))

    largestbase = 3
    culprits = []
    for n in to_test:
        a = 3
        while True:
            if euler_test(a, n):
                a += 1
            else:
                if a > largestbase:
                    largestbase = a
                    culprits = [n]
                elif a == largestbase:
                    culprits.append(n)
                break

    return largestbase, culprits


def q5i():
    pseudoprimes_base_two = []
    for n in range(2, 10 ** 6 + 1):
        if strong_test(2, n) and not trial_division(n):
            pseudoprimes_base_two.append(n)

    print(pseudoprimes_base_two)

    def isAbsoluteStrong(n):
        composite = False
        for a in range(2, n):
            if gcd(a, n) == 1:
                if not strong_test(a, n):
                    return False
            else:
                composite = True
        return composite  # if it gets here it must have passed all the rounds of testing

    absolute_strong_pseudoprimes = []
    for n in pseudoprimes_base_two:
        if isAbsoluteStrong(n):
            absolute_strong_pseudoprimes.append(n)

        # pseudoprime_for_all_coprime_a = True
        # composite = False
        # for a in range(2, n + 1):
        #     if gcd(a, n) != 1:
        #         composite = True
        #         pass
        #     elif not strong_test(a, n):
        #         pseudoprime_for_all_coprime_a = False
        #         break
        #
        # if pseudoprime_for_all_coprime_a and composite:
        #     absolute_strong_pseudoprimes.append(n)

    return absolute_strong_pseudoprimes, pseudoprimes_base_two


def q5ii():
    to_test = [2047, 3277, 4033, 4681, 8321, 15841, 29341, 42799, 49141, 52633, 65281, 74665, 80581, 85489, 88357,
               90751, 104653, 130561, 196093, 220729, 233017, 252601, 253241, 256999, 271951, 280601, 314821, 357761,
               390937, 458989, 476971, 486737, 489997, 514447, 580337, 635401, 647089, 741751, 800605, 818201, 838861,
               873181, 877099, 916327, 976873, 983401]
    print(len(to_test))

    largestbase = 3
    culprits = []
    for n in to_test:
        a = 3
        while True:
            if strong_test(a, n):
                a += 1
            else:
                if a > largestbase:
                    largestbase = a
                    culprits = [n]
                elif a == largestbase:
                    culprits.append(n)
                break

    return largestbase, culprits


def q6():
    fermat_pseudoprimes = [0, 0, 0, 0, 0]
    euler_pseudoprimes = [0, 0, 0, 0, 0]
    strong_pseudoprimes = [0, 0, 0, 0, 0]
    primes = [0, 0, 0, 0, 0]
    k_values = [5, 6, 7, 8, 9]
    bases = [2,3]  # options [2], [3], [2,3]
    for k_index in range(5):
        k = k_values[k_index]
        for n in range(10 ** k, 10 ** k + 10 ** 5 + 1):
            if n % 1000 == 0:
                print(n)
            if not trial_division(n):  # if not prime
                if all([fermat_test(base, n) for base in bases]):
                    fermat_pseudoprimes[k_index] += 1
                if n % 2 == 1 and all([euler_test(base, n) for base in bases]):
                    euler_pseudoprimes[k_index] += 1
                if all([strong_test(base, n) for base in bases]):
                    strong_pseudoprimes[k_index] += 1
            else:  # if prime
                primes[k_index] += 1
        print(euler_pseudoprimes)

    return fermat_pseudoprimes, euler_pseudoprimes, strong_pseudoprimes, primes

    # ([28, 16, 6, 1, 0], [11, 8, 4, 0, 0], [3, 2, 0, 0, 0], [8392, 7216, 6241, 5411, 4832])


def q7():
    def rand():
        return random.randrange(3, 10 ** 10 + 1)

    def small_trial_division(n):
        for i in [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241]:
            if n % i == 0:
                return False
        return True

    def my_test(n):
        if n==3215031751:
            return False
        if not small_trial_division(n):
            return False
        for a in [2,3,5,7]:
            if not strong_test(a, n):
                return False
        #if not trial_division(n):
        #    return False #comment out this if statement for ver2
        return True


    numbers = []
    prime1 = []
    prime2 = []

    for i in range(100000):
        numbers.append(rand())

    t0 = time.perf_counter()

    for n in numbers:
        if trial_division(n):
            prime1.append(True)
        else:
            prime1.append(False)

    t1 = time.perf_counter()

    trial_div_time = t1 - t0

    t0 = time.perf_counter()

    for n in numbers:
        if my_test(n):
            prime2.append(True)
        else:
            prime2.append(False)

    t1 = time.perf_counter()

    my_time = t1 - t0

    same=(prime1==prime2)
    return trial_div_time, my_time, same


def q8():
    k = 15
    trials = 10 ** 6
    maxsuccesses = 10
    primes = 0

    def randodd():
        return random.randrange(2 ** (k - 1) + 1, 2 ** k, 2)

    def rand():
        return random.randrange(2 ** (k - 1), 2 ** k)

    results = []
    for i in range(maxsuccesses):
        results.append([0,
                        0])  # we'll store results in these lists, the first being the number of composites and the last being the total numbers tested

    # print(results)
    # for trial in range(trials):
    #  N = randodd()

    for N in range(2 ** (k - 1) + 1, 2 ** k, 2):
        # if trial % 10 ** 5 == 0:
        # print(trial)
        if trial_division(N):  # don't care about primes
            primes += 1
            for success in range(maxsuccesses):
                results[success][1] += 1  # will pass the strong test for any base
            continue
        successes = 0  # how many rounds of the strong test N has passed
        while successes < maxsuccesses:
            while True:
                a = rand()
                if gcd(a, N) == 1:
                    break
            if strong_test(a, N):
                successes += 1
                results[successes - 1][0] += 1
                results[successes - 1][1] += 1
            else:
                break

    props = []
    for i in results:
        props.append(i[0] / i[1])
    return results, props, primes


if __name__ == '__main__':
    q3()
