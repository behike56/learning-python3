# -*- coding: utf-8 -*-
"""\
Python3の麗かな集合-3

Author:
    Hideo Tsujisaki
"""

# 集合のメソッド
set_x = {"林檎", "桃", "柿", "栗", "梨", "葡萄"}
set_y = {"桃", "柿", "栗", "梨"}
set_z = {"薩摩芋", "無花果", "落花生", "猿梨", "木通"}
set_zz = {"パイナップル", "桃", "柿", "栗", "梨", "パプリカ"}

# ＊＊＊存在判定メソッド＊＊＊
# 集合が引数に全て含まれるかを判定
set_x.issubset(set_y)
# 集合に引数の全ての要素が含まれるかを判定
set_x.issuperset(set_y)
print("＊＊＊存在判定メソッド＊＊＊")
print("issubset():=> " + str(set_x.issubset(set_y)))
print("issuperset():=> " + str(set_x.issuperset(set_y)))
print()
# ＊＊＊新しい集合を作る＊＊＊
# 新しい集合を返す
# 和集合：.union(*others)
set_uni = set_x.union(set_y)
# 積集合：.intersection(*others)
set_inter = set_x.intersection(set_y)
# 差集合：.difference(*others)
set_diff = set_x.difference(set_z)
# 対称差集合：.symmetric_difference(others)
set_symm = set_y.symmetric_difference(set_zz)
print(" ＊＊＊新しい集合を作る＊＊＊")
print("union():=> " + str(set_uni))
print("intersection():=> " + str(set_inter))
print("difference():=> " + str(set_diff))
print("symmetric_difference():=> " + str(set_symm))
print()
# ＊＊＊集合を更新する＊＊＊
# 対象の集合を変更する
# 和集合：.update(*others)
print("＊＊＊集合を更新する＊＊＊")
set_x.update(set_y)
print("update():=> " + str(set_x))
# 積集合：.intersection_update(*others)
set_x.intersection_update(set_y)
print("intersection():=> " + str(set_x))
# 差集合：.difference_update(*others)
set_x.difference_update(set_z)
print("difference_update():=> " + str(set_x))
# 対称差集合：.symmetric_difference_update(others)
set_y.symmetric_difference_update(set_zz)
print("symmetric_difference_update():=> " + str(set_y))
