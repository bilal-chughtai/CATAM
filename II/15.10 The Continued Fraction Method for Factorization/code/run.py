import random
from math import floor, sqrt, ceil, gcd


def B_smooth(B, N):
    factorization = []
    for prime in B:

        if prime == -1:
            if N < 0:
                factorization.append(-1)
                N=-N
                continue
            else:
                continue

        while N % prime == 0:
            factorization.append(prime)
            N = N / prime

    if N == 1:
        return factorization
    else:
        return False


def modular_multiply(x, y, mod, result):
    # if calling directly put result = 0
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


def sqrt_cont_frac(N, k):
    # returns the fixed part, and the repeated part of the continued fraction
    # k gives a maximum length of a
    r = [0]
    s = [1]
    a = []

    n = 0

    while True:
        xn = (r[n] + sqrt(N)) / s[n]
        new_a = int(floor(xn))
        a.append(new_a)

        if len(a) > k:
            return [a[0]], a[1:], r, s

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
        fixed, repeated, r, s = sqrt_cont_frac(N, 100)
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
        fixed, repeated, r, s = sqrt_cont_frac(N, 100)
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
        fixed, repeated, r, s = sqrt_cont_frac(N, 1000)
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
    for N in range(500, 551):  # change the range here
        if floor(sqrt(N)) == sqrt(N):
            print(str(N) + ") has no solutions (square)")
            continue
        fixed, repeated, r, s = sqrt_cont_frac(N, 1000)
        a = fixed + repeated + repeated  # i know there will be a solution within the first 2 repeated convergents so wont do more
        p, q = convergents(a)
        for i in range(len(p)):
            if verify_large_pell(p[i], q[i], N) == 1:
                print(str(N) + ") (" + str(p[i]) + "," + str(q[i]) + ")")
                break


def q5(N, k):
    # we'll compute for k convergents
    fixed, repeated, r, s = sqrt_cont_frac(N, k)
    a = fixed
    for i in range(ceil(k / len(repeated))):
        a = a + repeated
    a = a[:k + 1]
    p, q = convergents(a)

    p_modn = []
    p_squred_modn = []
    for p_value in p:
        p_modn.append(p_value % N)

        p_value_squared = modular_multiply(p_value, p_value, N, 0)
        if p_value_squared > N/2:
            p_value_squared -= N
        p_squred_modn.append(p_value_squared)

    return p_modn, p_squred_modn


def kernel(A):
    # returns a vector v in the kernel of A.
    # expect A in form [ [a_11, a_12, a_13, ...], [a_21, a_22, a_23,...]....]
    rows = len(A)
    columns = len(A[0])

    i = 0  # pivot row
    j = 0  # pivot column
    while True:

        # first find the pivot element - the max in column i
        max_element = A[i][j]
        pivot_row = i
        for k in range(i + 1, rows):
            if A[k][j] > max_element:
                max_element = A[k][j]
                pivot_row = k

        if max_element == 0:  # no pivot in column, move on to next column
            j += 1
            if j>=columns:
                break
            continue


        # swap max element row into row i
        for k in range(0, columns):
            A[pivot_row][k], A[i][k] = A[i][k], A[pivot_row][k]

        # Make all rows below this one 0 in current column
        for k in range(i + 1, rows):
            if A[k][j] == 1:  # add row i to row k

                for a in range(0, columns):
                    A[k][a] = (A[k][a] + A[i][a]) % 2

        i += 1
        j += 1

        if i >= rows or j >= columns:
            break

    #calculate where the pivot elements are, since they determine which elements are free when solving
    pivotcolumns = []
    for i in range(rows):
        for j in range(columns):
            if A[i][j]==1:
                pivotcolumns.append(j)
                break
            if j==columns-1:
                pivotcolumns.append('*') #no pivot



    rank = len(pivotcolumns) - pivotcolumns.count('*')
    nullity = columns - rank


    if nullity == 0:
        return False
    else:

        free_elements=[i for i,x in enumerate(pivotcolumns) if x == '*']
        vectors=[]
        for c in range(columns-1,-1,-1):
            if c not in pivotcolumns:
                x = [0] * columns
                x[c]=1
       # x[pivotcolumns.index('*')] = 1  # the pivotcolumns provide "fixed" elements, and the rest are free, so pick a free one and make it 1

                for i in range(rows - 1, -1, -1):
                    if pivotcolumns[
                        i] == '*':  # or pivotcolumns[i] == columns-1: - these are the free ones, which we've already fixed
                        pass
                    # do nothing
                    # '*' means free component - already set to 1 or 0
                    # columns-1 means x_i=0, so no calc needed
                    else:
                        for j in range(pivotcolumns[i] + 1, columns):

                            x[pivotcolumns[i]] = (x[pivotcolumns[i]] - A[i][j] * x[j]) % 2

                vectors.append(x)

        return vectors




def factorization(N):
    k = 500  # number of convergents we calculate initially

    factorbase=[-1,2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    # q5 does a lot of work, so lets use that

    p_mod_n, p_squared_mod_n = q5(N, k)

    ps_used=[]
    B_numbers = []
    factors = []
    numberoffactors=[]


    for i in range(len(p_mod_n)):

        if p_mod_n[i] not in B_numbers:
            factor = B_smooth(factorbase, p_squared_mod_n[i])
            # if its a B number add it to the list
            if factor:
                ps_used.append(i)
                B_numbers.append(p_mod_n[i])
                factors.append(factor)
                primecount=[]

                for prime in factorbase:
                    primecount.append(factor.count(prime))

                numberoffactors.append(primecount)


                #now the matrix has columns the entries of numberoffactors
                A = [list(x) for x in zip(*numberoffactors)] #transpose

                for i in range(len(factorbase)):
                    for j in range(len(B_numbers)):
                        A[i][j] = A[i][j] % 2

                vectors = kernel(A)
                if vectors:
                    for vector in vectors:

                        #calc x and find all primes in y
                        x=1
                        primes_in_y_squared=[0]*len(factorbase)
                        for i in range(len(vector)):
                            if vector[i]==1:
                                x=modular_multiply(x,B_numbers[i],N,0)
                                primes_in_y_squared=[sum(x) for x in zip(primes_in_y_squared,numberoffactors[i])]



                        #calc y
                        y=1
                        for i in range(len(factorbase)):
                            for j in range(int(primes_in_y_squared[i]/2)):
                                y=modular_multiply(y,factorbase[i], N, 0)

                        if x!=y and x!=(-y)%N:
                            used_B_numbers_indices = [i for i,x in enumerate(vector) if x == 1]
                            used_P_n_indices=[ps_used[i] for i in used_B_numbers_indices ]
                            used_B_numbers = [B_numbers[i] for i in used_B_numbers_indices]
                            used_factors = [numberoffactors[i] for i in used_B_numbers_indices]
                            factor1=gcd(x+y,N)
                            factor2=gcd(x-y, N)

                            if primes_in_y_squared[0]>2:
                                ystring="(-1)^" + str(int(primes_in_y_squared[0]/2)) + " x "
                            elif primes_in_y_squared[0]==2:
                                ystring = "(-1) x "
                            else:
                                ystring=""
                            for i in range(1,len(factorbase)):
                                if primes_in_y_squared[i]==2:
                                    ystring+=str(factorbase[i]) + " x "
                                elif primes_in_y_squared[i]>2:
                                    ystring += str(factorbase[i])+"^"+str(int(primes_in_y_squared[i]/2)) + " x "

                            ystring = ystring[:-3]

                            def string(my_list):
                                return ','.join(map(str, my_list))

                            print("The algorithm uses P_n for n = "+string(used_P_n_indices))
                            print("The corresponding B numbers are "+string(used_B_numbers))
                            print("Multiplying the B numbers, x_i, gives an x = "+str(x))
                            print("Multipling <x_i^2> gives a y = " + str(y) + " = " + ystring)
                            print("This gives us factors gcd(x+y,N) = "+str(factor1) + " and gcd(x-y,N) = "+ str(factor2))

                            return
















