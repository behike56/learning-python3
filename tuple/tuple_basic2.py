# -*- coding: utf-8 -*-
"""\
Python3の華麗なるリスト-1

Author:
    Hideo Tsujisaki
"""
# インデックス指定、スライシングOK
print("\n＊＊＊インデックス指定、スライシングで呼び出しOK＊＊＊")
tup = (1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3)
print("tup:=> " + str(tup))
print("tup[0]:=> " + str(tup[0]))
print("tup[-1]:=> " + str(tup[-1]))
print("tup[2:4]:=> " + str(tup[2:4]))
print()

print("＊＊＊入れ子を取り出す＊＊＊")
tup_list = ([1, 2, 3, 4], ["A", "B", "C", "D"])
print("tup_list:=> " + str(tup_list))
print("tup_list[0]:=> " + str(tup_list[0]))
print("tup_list[1][3]:=> " + str(tup_list[1][3]))
print()

# 探す、数える
print("＊＊＊探す、数える＊＊＊")
print("tup.index(3):=> " + str(tup.index(3)))
print("tup.index(3, 2):=> " + str(tup.index(3, 2)))
print("tup.count(3):=> " + str(tup.count(3)))
