# -*- coding: utf-8 -*-
"""\
Python3の華麗なるリスト-1

Author:
    Hideo Tsujisaki
"""

# リストを作る
num_list = [1, 33, 233, 567, 2093, 88, 345, 100]
str_list = ["春", "夏", "秋", "冬"]
list_in_list_a = [["A", "B", "C"], [111, 222, 333]]
list_in_list_b = [num_list, str_list]

print("＊＊＊リストを作る＊＊＊")
print("num_list:" + str(num_list))
print("str_list:" + str(str_list))
print("list_in_list_a:" + str(list_in_list_a))
print("list_in_list_b:" + str(list_in_list_b))
print()
print()
# リストから呼び出す
print("＊＊＊リストから呼び出す＊＊＊")
print(num_list[0])
print(num_list[3])
print(num_list[-1])
print(num_list[0:3])
print(num_list[:3])
print(num_list[0:])
print(num_list[:])
print(num_list[::2])
print(list_in_list_a[0])
print(list_in_list_a[0][2])

num_list = [1, 33, 233, 567, 2093, 88, 345, 100]
# 書き換える
print("＊＊＊リストを書き換える＊＊＊")
num_list[3] = 333
print("num_list[3] = 333:=> " + str(num_list))
num_list[2:4] = [12, 13, 14]
print("num_list[2:4] = [12, 13, 14]:=> " + str(num_list))
num_list[2:4] = []
print("num_list[2:4] = []=> " + str(num_list))
num_list[:] = []
print("num_list[:] = []:=> " + str(num_list))

num_list2 = [1, 33, 233, 567, 2093, 88, 345, 100]

# 足し合わせる１
print("足し合わせる１")
new_list_a = num_list + num_list2
print(new_list_a)
# 足し合わせる２
print("足し合わせる２")
num_list += num_list2
print(num_list2)
