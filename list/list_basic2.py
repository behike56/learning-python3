# -*- coding: utf-8 -*-
"""\
Python3の華麗なるリスト-2
methods
Author:
    Hideo Tsujisaki
"""

num_list = [1, 33, 233, 567, 2093]
# 共通メソッド
print()
print("＊＊＊共通メソッド＊＊＊")
print(len(num_list))
print(type(num_list))
print(list("アイウエオ"))
num_list.remove(1)
print(num_list)
del num_list

numbers = "1,2,3,4,5,6,7,8"
numbers.split(',')
print("split" + str(numbers))
print()
# リストメソッド
print("＊＊＊リストメソッド＊＊＊")
a_list = [1, 2, 3]
b_list = [4, 5, 6]
# リストを合体させる
a_list.extend(b_list)
print("リスト合体：　" + str(a_list))

m_list = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print("index(3):=> " + str(m_list.index(3)))
print("index(3, 3):=> " + str(m_list.index(3, 3)))
print("count(2):=> " + str(m_list.count(2)))
print()
# 後ろに付け足す
m_list.append(198)
print("後ろに付け足す：=> " + str(m_list))

# 指定したところに入れる
m_list.insert(3, 99)
print("指定したところに入れる：=> " + str(m_list))
# 後ろから取り出す（削除）
m_list.pop()
print("後ろから取り出す（削除）:=> " + str(m_list))
# 指定したところを取り出す（削除）
m_list.pop(0)
print("指定したところを取り出す（削除）:=> " + str(m_list))
print()
# ソート
m_list.sort()
print("ソート:=> " + str(m_list))
# 逆にソート１
m_list.sort(reverse=True)
print("逆ソート1:=> " + str(m_list))
# 逆にソート２
m_list.reverse()
print("逆ソート2:=> " + str(m_list))
# コピー
copy_list = m_list.copy()
print("コピー:=> " + str(copy_list))
m_list.clear()
print("削除:=> " + str(m_list))
