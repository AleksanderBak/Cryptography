import hashlib
import timeit
import random
import string
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np
import binascii


def binaryToDecimal(binary):
    binary = int(binary)
    decimal, i = 0, 0
    while binary != 0:
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal


def generate_random_text(length):
    return "".join(random.choice(string.ascii_letters) for i in range(length))


def calculate_time(text, func):
    t = text.encode()
    start = timeit.default_timer()
    func(t)
    end = timeit.default_timer()
    return (end - start) * 1000


def md5(text):
    hash_obj = hashlib.md5()
    hash_obj.update(text)
    return hash_obj.hexdigest()


def sha1(text):
    hash_obj = hashlib.sha1()
    hash_obj.update(text)
    return hash_obj.hexdigest()


def sha224(text):
    hash_obj = hashlib.sha224()
    hash_obj.update(text)
    return hash_obj.hexdigest()


def sha256(text):
    hash_obj = hashlib.sha256()
    hash_obj.update(text)
    return hash_obj.hexdigest()


def sha384(text):
    hash_obj = hashlib.sha384()
    hash_obj.update(text)
    return hash_obj.hexdigest()


# Zad4
# inp = "test"
# text = inp.encode()
# print(md5(text))

# Zad1
# hash_functions = [md5, sha1, sha224, sha256, sha384]
# # text_lengths = [i for i in range(16, 2048, 32)]
# text_lengths = [i for i in range(1, 100001, 1000)]

# times = [[] for i in range(len(hash_functions))]

# for length in text_lengths:
#     tmp = [[] for _ in range(len(hash_functions))]
#     for i in range(20):
#         text = generate_random_text(length)
#         for i, func in enumerate(hash_functions):
#             tmp[i].append(calculate_time(text, func))
#     for z in range(len(tmp)):
#         tmp[z].remove(max(tmp[z]))
#         tmp[z].remove(min(tmp[z]))

#     res = []
#     for r in tmp:
#         res.append(sum(r) / 20)
#     for i in range(len(hash_functions)):
#         times[i].append(res[i])

# # times = [
# #     [calculate_time(generate_random_text(length), func) for length in text_lengths]
# #     for func in hash_functions
# # ]

# plt.figure()
# # plt.yscale("log")
# # plt.autoscale()
# for i, func in enumerate(hash_functions):
#     plt.plot(text_lengths, times[i], label=f"{func.__name__}")
# plt.legend()
# plt.xlim(1, 100000)
# plt.xlabel("Ilość znaków na wejściu")
# plt.ylabel("Czas (ms)")
# plt.gca().yaxis.set_major_formatter(mtick.FormatStrFormatter("%.3f"))
# plt.tight_layout()
# plt.show()


# Zad5
# def findCollision():
#     iterations = 1000
#     num_bits = 12
#     hash_dict = {}
#     col = False
#     for i in range(iterations):
#         msg = str(i).encode("utf-8")
#         hash_value = hashlib.sha256(msg).hexdigest()
#         hash_colision = hash_value[: num_bits // 4]
#         if hash_colision in hash_dict:
#             print("Znaleziona kolizja: ")
#             print("Wiadomość 1:", msg)
#             print("Wiadomość 2:", hash_dict[hash_colision])
#             print("Hash 1:", hash_value)
#             print("Hash 2:", hashlib.sha256(hash_dict[hash_colision]).hexdigest())
#             col = True
#         else:
#             hash_dict[hash_colision] = msg

#     if not col:
#         print(f"Brak kolizji na pierwszych {num_bits} bitach")


# findCollision()

# zad 6
inp = "10001111100101110010111010111110011"
print(len(inp))
origin_hash = sha256(inp.encode())
binary_origin_hash = bin(int(origin_hash, 16))[2:]

diff = []

for i in range(0, len(inp)):
    old_input = inp
    new_bit = "0" if inp[i] == "1" else "1"
    inp = inp[:i] + new_bit + inp[i + 1 :]

    hash_value = sha256(inp.encode())
    binary_hash = bin(int(hash_value, 16))[2:].zfill(256)

    num_differences = sum(
        bit1 != bit2 for bit1, bit2 in zip(binary_hash, binary_origin_hash)
    )
    diff.append(num_differences / 256)
    inp = old_input

print(f"Średnia ilość zmienionych bitów: {sum(diff) / len(diff)}%")
