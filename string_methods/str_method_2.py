# -*- coding: utf-8 -*-
"""\
PythonができるStringの事。下巻：文字列メソッド
Pythonの基本を学習するためのソースコード2

5 - 14

Author:
    Hideo Tsujisaki
"""

# 確認用変数
list_strs1 = ["Porshe", "Subaru", "Ford", "Aston Martin"]
list_strs2 = ["ABC", "DEF", 333, ["柿", "栗", "桃"]]
# 5.配列の文字列を結合する
"_".join(list_strs1)
error1 = ""
try:
    print("_".join(list_strs2))
except TypeError as terr:
    error1 = terr

# 確認用変数
str_replace1 = "Moon Walker."
str_replace2 = "青汁"
# 6.置換処理
str_replace1.replace("Moon", "Sky")
str_replace2.replace("青", "豚")

# 確認用変数
str_list1 = "Apple,Banana,Orange"
str_list2 = "春夏秋冬"
str_list3 = "春,夏,秋,冬"
# 7.文字列を区切って配列に格納する
str_list1.split(",")
str_list2.split()
str_list3.split(",")

# 確認用変数
cap_str1 = "i lost my iPhone"
cap_str2 = "aaa青梗菜zzz"
# 8.先頭を大文字に、それ以外は小文字にする
cap_str1.capitalize()
cap_str2.capitalize()

# 確認用変数
yoseru_str1 = "ZZZ"
yoseru_str2 = "橙色"
# 9.右寄せにする
yoseru_str1.rjust(20, "#")
yoseru_str2.rjust(20, "-")
# 10.左寄せにする
yoseru_str1.ljust(20, "%")
yoseru_str2.ljust(20, "&")
# 11.中央寄せにする
yoseru_str1.center(20, "=")
yoseru_str2.center(20, "~")

# 確認用変数
space_str1 = " to be or not to be. "
space_str2 = "\tORA\nNGE"
space_str3 = "　吾輩も猫である。　"
# 12.空白文字を除去
space_str1.strip()
space_str2.strip()
space_str3.strip()
# 13.右にある空白文字を除去
space_str1.rstrip()
space_str2.rstrip()
space_str3.rstrip()
# 14.左にある空白文字を除去
space_str1.lstrip()
space_str2.lstrip()
space_str3.lstrip()
"""実行"""
print("5.配列の文字列を結合する")
print("_".join(list_strs1))
print(error1)
print()
print("6.置換処理")
print(str_replace1.replace("Moon", "Sky"))
print(str_replace2.replace("青", "豚"))
print()
print("7.文字列を区切って配列に格納する")
print(str_list1.split(","))
print(str_list2.split())
print(str_list3.split(","))
print()
print("8.先頭を大文字に、それ以外は小文字にする")
print(cap_str1.capitalize())
print(cap_str2.capitalize())
print()
print("9.右寄せにする")
print(yoseru_str1.rjust(20, "#"))
print(yoseru_str2.rjust(20, "-"))
print()
print("10.左寄せにする")
print(yoseru_str1.ljust(20, "%"))
print(yoseru_str2.ljust(20, "&"))
print()
print("11.中央寄せにする")
print(yoseru_str1.center(20, "="))
print(yoseru_str2.center(20, "~"))
print()
print("12.空白文字を除去")
print(space_str1.strip())
print(space_str2.strip())
print(space_str3.strip())
print()
print("13.右にある空白文字を除去")
print(space_str1.rstrip())
print(space_str2.rstrip())
print(space_str3.rstrip())
print()
print("14.左にある空白文字を除去")
print(space_str1.lstrip())
print(space_str2.lstrip())
print(space_str3.lstrip())
