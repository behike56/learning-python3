# -*- coding: utf-8 -*-
"""\
Python3の麗かな集合-2

Author:
    Hideo Tsujisaki
"""

# 集合を操作する演算子
set_x = {"林檎", "桃", "柿", "栗", "梨", "葡萄"}
set_y = {"桃", "柿", "栗", "梨"}
set_z = {"薩摩芋", "無花果", "落花生", "猿梨", "木通"}
set_zz = {"パイナップル", "桃", "柿", "栗", "梨", "パプリカ"}

# ＊＊＊存在判定＊＊＊
# 集合が引数と共通の要素を持たない場合にTrue
set_zz.isdisjoint(set_y)
# 左辺が全て右辺に含まれるか判定
set_y <= set_x
# 左辺が右辺の部分集合かを判定（真部分集合）
set_y < set_x
# 左辺が右辺の要素を全て内包するか判定（右辺が全て左辺に含まれるか判定）
set_y >= set_x
# 左辺が右辺の上位集合かを判定（真上位集合）
set_y > set_x
print("\n＊＊＊存在判定＊＊＊")
print("isdisjoint(set_y):=> " + str(set_zz.isdisjoint(set_y)))
print("<= :=> " + str(set_y <= set_x))
print("< :=> " + str(set_y < set_x))
print(">= :=> " + str(set_y >= set_x))
print("> :=> " + str(set_y > set_x))
print()

# ＊＊＊新しい集合を作る＊＊＊
# 右辺は複数指定できる
# 左辺と右辺を全て含む集合を返す：和集合
set_new1 = set_y | set_z
# 左辺と右辺に共通する要素を持つ集合を返す：積集合
set_new2 = set_x & set_new1
# 左辺含まれ、右辺に含まれない要素を持つ集合を返す：差集合
set_new3 = set_x - set_y
# 左辺と右辺のいずれか一方にのみ含まれる要素を持つ集合を返す：対称差集合
set_new4 = set_x ^ set_zz
print("＊＊＊新しい集合を作る＊＊＊")
print("| :=> " + str(set_new1))
print("& :=> " + str(set_new2))
print("- :=> " + str(set_new3))
print("^ :=> " + str(set_new4))
print()

# ＊＊＊集合を更新する＊＊＊
print("＊＊＊集合を更新する＊＊＊")
# 右辺は複数指定できる
# 左辺に右辺の要素を全て追加し左辺を更新する：和集合
set_zz |= set_y
print("|= :=> " + str(set_zz))
# 左辺と右辺に共通する要素のみ残して左辺を更新する：積集合
set_zz &= set_y
print("&= :=> " + str(set_zz))
# 左辺に含まれる右辺と同じ要素を取り除いて左辺を更新する：差集合
set_zz -= set_y
print("-= :=> " + str(set_zz))
# 左辺または右辺の一方にのみ存在する要素のみで左辺を更新する：対称差集合
set_zz ^= set_y
print("^= :=> " + str(set_zz))
