import sys
import random
from decimal import Decimal


def decode(shares, pool):
    s = 0

    for i in pool:
        x1, y1 = shares[i]
        prod = Decimal(1)

        for j in pool:
            x2, _ = shares[j]
            if i != j:
                prod *= Decimal(Decimal(x2) / (x2 - x1))
        prod *= y1
        s += Decimal(prod)

    return int(round(Decimal(s), 0))


def polynom(x, coeffs):
    s = 0
    for coef_index, coef_value in enumerate(coeffs[::-1]):
        s += x**coef_index * coef_value
    return s


def encode(secret, n, t):
    greater = secret if secret > n else n
    p = random.randint(greater, greater + 100000)
    print(f"p: {p}")

    coeffs = [random.randint(0, 1000) for _ in range(t - 1)]
    coeffs.append(secret)

    shares = []

    for i in range(0, n):
        x = random.randint(0, 1000)
        shares.append((x, polynom(x, coeffs)))

    return shares


if __name__ == "__main__":
    n = int(sys.argv[1])
    t = int(sys.argv[2])
    secret = int(sys.argv[3])
    print(f"n: {n}, t: {t}, secret: {secret}")
    shares = encode(secret, n, t)
    print("Shares:")
    for i, share in enumerate(shares):
        print(f"{i}: {share}")

    pool = input("What shares you want to use to decode secret: ").split(",")
    pool = [int(x.strip()) for x in pool]
    for elem in pool:
        if elem > n:
            print(f"Share number {elem} doesn't exist")
            exit()

    decoded_secret = decode(shares, pool)
    print(f"Decoded secret = {decoded_secret}")
