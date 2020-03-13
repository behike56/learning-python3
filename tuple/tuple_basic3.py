# -*- coding: utf-8 -*-
"""\
Python3の流麗なるタプル-3

Author:
    Hideo Tsujisaki
"""

# 開梱：アンパッキング
# リストの場合も同様
print("\n＊＊＊開梱：アンパッキング＊＊＊")
tup_2 = (11, 12, 13, 14, 15)
print("tup_2:=> " + str(tup_2))
a, b, c, d, e, = tup_2
print("a:=> " + str(a))
print("b:=> " + str(b))
print("c:=> " + str(c))
print("d:=> " + str(d))
print("e:=> " + str(e))
print()

# 値の入れ替えにも使えるアンパッキング
print("＊＊＊値の入れ替えにも使えるアンパッキング＊＊＊")
ex_a = "Apple"
ex_b = "Beats"
ex_a, ex_b = ex_b, ex_a
print("ex_a:=> " + str(ex_a))
print("ex_b:=> " + str(ex_b))
