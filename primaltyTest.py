import math

def sieve_of_eratosthenes(n):
    if n <= 1: return

    A = [True] * n

    for i in range(2, int(math.sqrt(n)) + 1):
        if A[i]:
            for j in range(i*2, n, i):
                A[j] = False

    res = [i for i in range(2, n) if A[i]]

    return res


def miller_selfridge_rabin(n):
    if n == 2:
        return True

    a, k = 2, 1
    q = int((n - 1) / pow(2, k))
    x, j = 0, 0

    if (n > 1) & ((n % 2) != 0):
        while (q % 2) == 0:
            k = k + 1
            q = int((n - 1) / pow(2, k))
        if pow(a, q) % n == 1 % n:
            return True
        else:
            for j in range(k):
                x = int(pow(2, j) * q)
                if (pow(a, x) % n) == ((n - 1) % n):
                    return True
    return False



def factorize(num_list):
    res = {}
    for number in num_list:
        res[number] = []
        for i in range(2, number):
            if number % i == 0:
                res[number].append(i)
    print(res)



if __name__ == "__main__":
    n = 10000
    
    sieve = sieve_of_eratosthenes(n)
    miller = []
    for i in range(3, n):
        if miller_selfridge_rabin(i):
            miller.append(i)
    # find composite numbers in miller robin list
    diff = []
    for number in miller:
        if number not in sieve:
            diff.append(number)

    print(diff)

    if diff:
        factorize(diff)


# No diffence when N = 100 or N = 1,000
# When N = 10,000, composite probable-primes are:
# [2047, 3277, 4033, 4681, 8321]
# Factorize:
# {2047: [23, 89], 3277: [29, 113], 4033: [37, 109], 4681: [31, 151], 8321: [53, 157]}
