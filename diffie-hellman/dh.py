import random


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def primeRoots(x):
    required_set = {num for num in range(1, x) if gcd(num, x)}
    return [
        g
        for g in range(1, x)
        if required_set == {pow(g, powers, x) for powers in range(1, x)}
    ]


def isPrime(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def getPrime(x):
    pr = False
    while not pr:
        x += 1
        pr = isPrime(x)
    return x


def calculateKeys(n, g):
    priv_key = random.randint(1000, 9999)
    pub_key = pow(g, priv_key, n)
    return priv_key, pub_key


def getSessionKey(priv, pub, n):
    k = pow(pub, priv, n)
    return k


if __name__ == "__main__":
    n = getPrime(random.randint(1000, 9999))
    primes = primeRoots(n)
    primes = [x for x in primes if x < n and x > 1]
    g = random.choice(primes)

    print(f"n: {n}, g = {g}")

    a_priv, a_public = calculateKeys(n, g)
    b_priv, b_public = calculateKeys(n, g)
    print(f"Private a: {a_priv}, public a: {a_public}")
    print(f"Private b: {b_priv}, public b: {b_public}")

    session_key_a = getSessionKey(a_priv, b_public, n)
    session_key_b = getSessionKey(b_priv, a_public, n)

    print(f"Session key A: {session_key_a}")
    print(f"Session key B: {session_key_b}")
