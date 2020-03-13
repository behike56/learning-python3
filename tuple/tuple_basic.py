# -*- coding: utf-8 -*-
"""\
Python3の流麗なるタプル-1

Author:
    Hideo Tsujisaki
"""

# タプルを作る, 梱包：パッキング
print("\n＊＊＊タプルを作る、梱包：パッキング＊＊＊")
tup = (1, 2, 3, 4, 5, 6, 3)
print("tup:=> " + str(tup))
tup_tup = ((7, 8, 9), (10, 11, 12))
print("tup_tup:=> " + str(tup_tup))
tup_list = ([1, 2, 3], ["A", "B", "C"])
print("tup_list:=> " + str(tup_list))
tup_one = 1,
print("tup_one:=> " + str(tup_one))
tup_tow = 1, 2,
print("tup_tow:=> " + str(tup_tow))
tup_etc = ("etc", )
print("tup_etc:=> " + str(tup_etc))
t_a = tuple([1, 3, 7])
print("t_method:=> " + str(t_a))
print()

# 新しいタプルを宣言すればタプル同士を足すことはできる
print("＊＊＊新しいタプルを宣言すればタプル同士を足すことはできる＊＊＊")
new_tup = tup + tup_etc
print("new_tup" + str(new_tup))
print()

# 消せる
print("＊＊＊消せる＊＊＊")
del tup_one

try:
    type(tup_one)
except Exception:
    print("del tup_one: tup_oneはもう消えてます。")
