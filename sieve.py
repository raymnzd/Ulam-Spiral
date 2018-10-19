def sieve(n):
    """
    :param n: limit of sieve
    :return: unordered set of all the primes up to n
    """
    s = set()
    primes = set()
    for i in range(2, n+1):
        if i in s:
            continue
        for f in range(i ** 2, n+1, i):
            s.add(f)
        primes.add(i)
    return primes


