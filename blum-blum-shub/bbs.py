import random


def binaryToDecimal(binary):
    binary = int(binary)
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def longestSeq(array, target):
    cnt = 0
    max_seq = 0
    for bit in array:
        cnt = cnt + 1 if bit == target else 0
        max_seq = max(cnt, max_seq)
    return max_seq


def singleBitTest(result):
    ones = result.count(1)
    if ones < 9725 or ones > 10275:
        print("Single bit test: not passed")
    else:
        print("Single bit test: passed")


def seriesTest(result):
    expected = [
        [2315, 2685],
        [1114, 1386],
        [527, 723],
        [240, 384],
        [103, 209],
        [103, 209],
    ]
    real = [0 for i in range(6)]
    seqLen = 0
    for bit in result:
        if bit == 1:
            seqLen += 1
        else:
            if seqLen == 0:
                continue
            elif seqLen > 6:
                real[5] += 1
            else:
                real[seqLen - 1] += 1
            seqLen = 0
    for i in range(len(real)):
        if real[i] < expected[i][0] or real[i] > expected[i][1]:
            print("Series test: not passed")
            return False
    print("Series test: passed")
    return True


def longestSeriesTest(result):
    seq_0 = longestSeq(result, 0)
    seq_1 = longestSeq(result, 1)
    if seq_0 > 25 or seq_1 > 25:
        print("Longest series test: not passed")
    else:
        print("Longest series test: passed")


def pokerTest(result):
    nums = [0 for i in range(16)]
    for i in range(0, len(result) - 4, 4):
        test = result[i : i + 4]
        test = "".join(str(bit) for bit in test)
        nums[binaryToDecimal(test)] += 1
    sum = 0

    for j in nums:
        sum += j**2
    x = 16 / 5000 * sum - 5000

    if x > 2.16 and x < 46.17:
        print("Poker test: passed")
    else:
        print("Poker test: nod passed")


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def isCongruent(x):
    if (x % 4) != 3:
        return False
    else:
        return True


def isPrime(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


def getPrime(x):
    pr = False
    con = False
    while not pr or not con:
        x += 1
        pr = isPrime(x)
        con = isCongruent(x)
    return x


if __name__ == "__main__":
    seed = random.randint(1, 1e10)

    p = getPrime(random.randint(1, 1e10))
    q = getPrime(random.randint(1, 1e10))
    N = p * q

    while gcd(seed, N) != 1:
        seed += 1

    x = seed ^ 2 % N

    res = []
    for i in range(20000):
        x = x**2 % N
        res.append(x & 1)
    print("Tests:")
    singleBitTest(res)
    longestSeriesTest(res)
    seriesTest(res)
    pokerTest(res)
    # print("".join(str(bit) for bit in res))
