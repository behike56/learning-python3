# -*- coding: utf-8 -*-
"""\
Python3の美麗なる辞書

Author:
    Hideo Tsujisaki
"""

# 作り方、宣言
print("\n＊＊＊作り方、宣言＊＊＊")
dict_empty = {}
dict_data = {"A": 1, "B": 2, "C": 3}

dict([("F", 6), ("G", 7)])
print("dict_empty:=> " + str(dict_empty))
print("dict_data:=> " + str(dict_data))
print("dict():=> " + str(dict(D=4, E=5)))
print()
# 呼び出し方
print("＊＊＊呼び出し方＊＊＊")
print("dict_data[\"A\"]:=> " + str(dict_data["A"]))
print("dict_data[\"B\"]:=> " + str(dict_data["B"]))
print("dict_data[\"C\"]:=> " + str(dict_data["C"]))
print()
# 値の変更
print("＊＊＊値の変更、メソッドなし＊＊＊")
dict_data["A"] = 12
print("dict_data[\"A\"] = 12:=> " + str(dict_data))
print()
# 辞書のメソッド
print("＊＊＊辞書のメソッド＊＊＊")
dict_data2 = {"A": 1, "B": 2, "C": 3}
print(".keys():=> " + str(dict_data2.keys()))
print(".values():=> " + str(dict_data2.values()))
print(".items():=> " + str(dict_data2.items()))
print(".get(\"A\"):=> " + str(dict_data2.get("A")))
# ないとnone、キーを指定したやり方dict_data2["Z"]だとエラーになるが
# get()メソッドだとエラーにならない
print("＊get()だとない場合はNoneが帰ってくる、エラーにならない。＊")
print(".get(\"Z\"):=> " + str(dict_data2.get("Z")))

# 値の変更、もしもなければ追加する
print("＊もし無ければ追加する。＊")
dict_data2.setdefault("D", 22)
print(".setdefault(\"D\", 22):=> " + str(dict_data2))
# 値の変更,　更新
dict_data3 = {"A": 33, "X": 9}
dict_data2.update(dict_data3)
print(".update(dict_data3):=> " + str(dict_data2))

# キー：値の削除
dict_data2.pop("B")
print(".pop(\"B\"):=> " + str(dict_data2))
del dict_data2["C"]
print("del dict_data2[\"C\"]:=> " + str(dict_data2))
print()

# コピー、参照渡しということを忘れるな。大元ごと変更されるお。
print("＊＊＊コピー、参照渡しということを忘れるな。大元ごと変更されるお。＊＊＊")
some_dict = {"M": 56}
some_val = some_dict
some_val["M"] = 44
print(some_dict)  # {"M" : 44}
print(some_val)  # {"M" : 44}

# copy()メソッドの場合, 値渡しのようになる
print("＊copy()メソッドの場合, 値渡しのようになる＊")
some_dict2 = {"L": 512}
some_val2 = some_dict2.copy()
some_val2["L"] = 1024
print(some_dict2)  # {"L" : 512}
print(some_val2)  # {"L" : 1024}
