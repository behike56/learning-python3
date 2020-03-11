# -*- coding: utf-8 -*-
"""\
Python3の華麗なるリスト-2
methods
Author:
    Hideo Tsujisaki
"""

from collections import deque

# リストを作りたい
base_list = [1, 2, 3, 4, 5, 6, 7]
ex_list = [8, 9, 10, 11, 12]

list_1 = []
for i in base_list:
    if i % 2 == 0:
        list_1.append(i)

# これを内包表記によって行う
list1 = [i for i in base_list if i % 2 == 0]

# for文が2重の場合は
list_2 = []
for i in base_list:
    for j in ex_list:
        list_2.append(i * j)

# これを内包表記によって行う
list2 = [i * j for i in base_list for j in ex_list]

# ２乗数のリストを作る
# ラムダで書く場合
lam_list = list(map(lambda x: x**2, range(10)))

# 内包表記で書く場合
naihou_list = [x**2 for x in range(10)]

# リストの中にあるリスト
list_in_list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

# 入れ替える
# リスト内包の先頭の式にはあらゆる式が使える。
[[row[i] for row in list_in_list] for i in range(4)]

# これは以下と同じ
irekae_list_1 = []
for i in range(4):
    irekae_list_1.append([row[i] for row in list_in_list])

# さらにこれは以下と同じ
irekae_list = []
for i in range(4):
    irekae_list_row = []
    for row in list_in_list:
        irekae_list_row.append(row[i])
    irekae_list.append(irekae_list_row)

# 複雑なフローにはzip()関数を使った方が良い
list(zip(*list_in_list))

# ***スタック***
s_list = []
stack_l = [s_list.append(i) for i in range(20)]

for i in stack_l:
    stack_l.pop(i)
    print(stack_l)

# ***キュー***

que_list = deque(["Apple", "Banana", "mango"])
que_list.append("Orange")
que_list.append("Peach")

print(que_list.popleft())
print(que_list.popleft())
print(que_list)
