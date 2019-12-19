from numpy import array,empty

def inverse(pi):
    """
    inverses a given permutation, input as a dictionary as below

    Args:
        pi (dict): Maps keys to values

    Returns:
        ip (dict): Inverse of pi, mapping keys to values

    """
    ip=dict()
    for key,value in pi.items():
        ip[value] = key
    return ip

def product(pi1, pi2):
    """

    Args:
        pi1 (dict): permutation
        pi2 (dict): permutation

    Returns:
        pi1pi2 (dict): permutation

    """
    pi1pi2=dict()
    for key,value in pi2.items():
        pi1pi2[key] = pi1[value]
    return pi1pi2

def stripping_algorithm(n,input_generators):
    """

    Args:
        input_generators (list): list of permutations (dicts) generating G

    Returns:
        output_generators(list): list of permutations (dicts) in reduced form generating G

    """
    A=empty((n,n), dtype=dict)
    k=len(input_generators)
    output_generators=list()
    for l in range(len(input_generators)):
        print(l)
        pi_l=input_generators[l] #create a local instance of pi_l
        i=1
        while i<=n: #i indexes rows
            if pi_l[i]!=i:
                g = A[i-1, pi_l[i]-1]
                if g is None:
                    A[i - 1, pi_l[i] - 1] = pi_l
                    break
                else:
                    pi_l=product(inverse(g),pi_l)
            i=i+1
        output_generators.append(pi_l)
    return output_generators


def main():
    pi1=dict()
    pi1[1]=2
    pi1[2]=3
    pi1[3]=4 #123
    pi1[4]=1
    pi2=dict()
    pi2[1]=3
    pi2[2]=1
    pi2[3]=2 #132
    #product(pi1,pi1)
    output=stripping_algorithm(4, [pi1,product(pi1,pi1)])
    print(output)

if __name__ == '__main__':
    main()