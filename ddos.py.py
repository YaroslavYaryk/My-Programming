# import sys
# import math
from sys import stdout
from itertools import permutations
from math import ceil
import re
from string import ascii_uppercase

# input_string = "  '' hello  world"
# arr = sorted(input_string, key=lambda s: sum(map(ord, s)))
# res = str(arr[0])

# for i in range(1, len(arr)):

#     if arr[i] == arr[i - 1]:

#         res += arr[i]
#     else:
#         res += "\n"
#         res += arr[i]

# print(res)


# def print_words(func):
#     def inner(*args, **kwargs):

#         print("hello")
#         return func(*args, **kwargs)

#     return inner

# @print_words
# def _sum(a,b):
#     return a + b


# print(_sum(5,6))


# class Persons:
#     def __init__(self, array: tuple):
#         self.index = -1
#         self.array = array

#     def __iter__(self):
#         return self

#     def __next__(self):

#         if self.index > len(self.array) - 2:
#             raise StopIteration
#         self.index += 1
#         return self.array[self.index]


# pers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
# obj = Persons(pers)

# for el in obj:
#     print(el)


# a = [1, 2, 3, 45, 6]
# if (n := len(a)) > 4:
#     print(f"List is too long ({n} elements, expected <= 10)")


# def double_number(number):
#     while True:
#         number = yield number


# c = double_number(4)
# print(c.send(None))
# print(next(c))

# print(c.send(10))

# # for el in arr:
# #     print(el)


# def next_bigger(n):
#     arr = []
#     for el_typle in permutations([int(i) for i in str(n)]):
#         arr.append(int("".join([str(el) for el in el_typle])))
#     try:
#         arr = sorted(list(set(arr)))
#         if arr[arr.index(n) + 1] < n:
#             raise IndexError()
#         return arr[arr.index(n) + 1]
#     except IndexError:
#         return -1


# # print()

# print(next_bigger(144))


# class PaginationHelper:
#     def __init__(self, collection, items_per_page):
#         self.collection = collection
#         self.items_per_page = items_per_page

#     def item_count(self):
#         return len(self.collection)

#     def get_items_per_page(self):
#         array = []
#         for i in range(0, len(self.collection), self.items_per_page):
#             a = []
#             try:
#                 for j in range(i, i + self.items_per_page):
#                     a.append(self.collection[j])
#             except IndexError:
#                 pass
#             array.append(a)

#         return array

#     def page_count(self):
#         return ceil(self.item_count() / self.items_per_page)

#     def page_item_count(self, page_index):
#         try:
#             return self.get_items_per_page()[page_index]
#         except IndexError:
#             return -1

#     def page_index(self, item_index):
#         if not self.item_count():
#             return -1
#         if item_index < 0 or item_index > self.item_count():
#             return -1
#         res = ceil((item_index + 1) / self.items_per_page) - 1
#         return res if res <= self.page_count() else -1


# collection = range(1, 25)
# helper = PaginationHelper(collection, 10)
# # print(helper.page_count())
# print(helper.page_index())
# # print(helper.item_count())


def to_underscore(string):

    string = str(string)
    arr = []
    index = len(string) - 1
    for i in range(len(string) - 1, -1, -1):
        if string[i] in ascii_uppercase:
            arr.append(string[i : index + 1])
            index = i - 1
    res = "_".join([el.lower() for el in arr[::-1]])
    return res if res else str(string)


print(to_underscore(1))
