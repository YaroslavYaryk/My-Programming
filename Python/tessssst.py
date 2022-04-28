# from itertools import permutations


# def get_all_combination(n: list):
#     return [int("".join(str(el) for el in elem)) for elem in permutations(n)]


# def next_smaller(n):
#     combinations = sorted(get_all_combination(
#         [int(el) for el in str(n)]), reverse=True)
#     try:
#         return combinations[combinations.index(n)+1]
#     except IndexError:
#         return -1


# print(next_smaller(1234567908))

# import requests

# r = requests.post('http://127.0.0.1:8000/api/token/',
#                   data={'username': 'yaroslav', 'password': 'proshnik31'})

# print(r.json()["refresh"])

# a = [1, 2, 2, [23, 4, [3, 2]]]


# def open_array(arr, storage=[]):
#     for el in arr:
#         if isinstance(el, list):
#             open_array(el)
#         else:
#             storage.append(el)
#     return storage


# print(open_array(a))

# from collections import Counter

# a = "doog"
# b = "ddog"


# def is_similar(a, b):
#     # return Counter(a) == Counter(b)
#     return sorted(a) == sorted(b)


# print(is_similar(a, b))
# from time import sleep

# a = 0


# def cache_func(func, result=0):
#     def inner(*args):
#         nonlocal result
#         if result:
#             print("1")
#             return result
#         else:
#             print("2")
#             result = func(*args)
#             return result

#     return inner


# @cache_func
# def func():
#     sleep(5)
#     return 125


# print(func())
# print(func())
