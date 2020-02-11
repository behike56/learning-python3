# -*- coding: utf-8 -*-
"""\
PythonができるStringの事。上巻：文字列の基本
Pythonの基本を学習するためのソースコード2

Author:
    Hideo Tsujisaki
"""

# ＊＊＊inとnot in＊＊＊
str_1 = "ABCDEFGHIJKLMN"
# 在るとtrue
"GHI" in str_1
# 無いとfalse
"BCA" in str_1
# 無いとtrue
"Z" not in str_1
# 在るとfalse
"M" not in str_1

# ＊＊＊スライシングのステップ＊＊＊
# １個飛ばし
str_1[2:13:2]

# ＊＊＊len(),min(),max()＊＊＊
len(str_1)
min(str_1)
max(str_1)

# ＊＊＊index()始まりを知る＊＊＊
str_1.index("G", 2, 13)
# str_1.index("G", 2, 5)

# ＊＊＊count()何個あるか数える＊＊＊
# str_1.count()
str_1.count("B")
str_1.count("Z")
"""
実行
"""
print("***inとnot in***")
print('str_1 = "ABCDEFGHIJKLMN"')
print('在るとtrue "GHI" in str_1:' "GHI" in str_1)
print('無いとfalse "BCA" in str_1:' "BCA" in str_1)
print('無いとtrue "Z" not in str_1:' "Z" not in str_1)
print('在るとfalse "M" not in str_1:' "M" not in str_1)
print()
print("***スライシングのステップ***")
print("str_1[2:13:2]:" + str(str_1[2:13:2]))
print()
print("***len(),min(),max()***")
print("len():" + str(len(str_1)))
print("min():" + str(min(str_1)))
print("max():" + str(max(str_1)))
print()
print("***index(),始まりを見つける***")
print("Gを２から１３のインデックス間で探す：" + str(str_1.index("G", 2, 13)))

try:
    print("Gを２から5のインデックス間で探す：" + str(str_1.index("G", 2, 5)))
except ValueError:
    print("Gを２から5のインデックス間で探す： ValueError!!!")

print()
print("***count(),引数が何個あるか数える***")

try:
    print("引数なし：" + str_1.count())
except TypeError:
    print("引数無し：　TypeError!!!")

print("Bを数える：" + str(str_1.count("B")))
print("Z、存在しないものだと？：" + str(str_1.count("Z")))
