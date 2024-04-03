import random


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


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


def cipher(message, e, n):
    res = []
    for letter in message:
        l = pow(ord(letter), e) % n
        res.append(chr(l))
    return "".join(res)


def decipher(message, d, n):
    res = []
    for letter in message:
        l = pow(ord(letter), d) % n
        res.append(chr(l))
    return "".join(res)


if __name__ == "__main__":
    # p = getPrime(random.randint(1000, 9999))
    # q = getPrime(random.randint(1000, 9999))
    p = getPrime(random.randint(10, 99))
    q = getPrime(random.randint(10, 99))
    N = p * q
    phi = (p - 1) * (q - 1)
    e = getPrime(random.randint(1, phi - 1))

    t = 1 if e < phi // 2 else -1

    while gcd(e, phi) != 1:
        e += t

    d = pow(e, -1, phi)

    print(f"p: {p}, q: {q}, N: {N}, phi: {phi}, e: {e}, d: {d}")

    public_key = {"e": e, "n": N}
    private_key = {"d": d, "n": N}

    message = "Hey there, just wanted to say hi and hope you're having a great day!"
    print(f"Original message: {message}")
    ciph = cipher(message, public_key["e"], public_key["n"])
    print(f"Encrypted message: {ciph}")
    deciph = decipher(ciph, private_key["d"], private_key["n"])
    print(f"Decrypted message: {deciph}")
