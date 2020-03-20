# -*- coding: utf-8 -*-
"""\
Python3の麗かな集合-1

Author:
    Hideo Tsujisaki
"""

# 宣言
set_empty = set()  # 空の集合
set_a = {1, 4, 2, 3, 5, 8, 7, 6}  # 順序は関係ない
set_f = {32, 33, 34, 35}
set_frozen = frozenset(set_f)  # イミュータブルやで
set_b = {"A", "B", set_frozen}

# 重複は取り除かれる
set_ex = {
    "A",
    "A",
    "B",
    "B",
    "C",
    "D",
    "E",
    "E",
    "F",
}

# 動作確認
print("\n＊＊＊宣言＊＊＊")
print("set_empty:=> " + str(set_empty))
print("set_a:=> " + str(set_a))
print("set_frozen:=> " + str(set_frozen))
print("set_b:=> " + str(set_b))
print("set_ex:=> " + str(set_ex))
print()
print("＊＊＊共通する操作(一部、専用を含む)、メソッド＊＊＊")
# 共通する操作(一部、専用を含む)、メソッド
set_x = {"林檎", "桃", "柿", "栗", "梨", "葡萄"}

"栗" in set_x
"季" not in set_x
print("\"栗\" in set_x:=> " + str("栗" in set_x))
print("\"季\" not in set_x:=> " + str("季" not in set_x))

# 集合の要素の数、中身
len(set_x)
print("len():=> " + str(len(set_x)))
# コピーを返す、公式ドキュメントは「浅いコピー」。
set_c = set_x.copy()
print("copy():=> " + str(set_c))
# 引数を集合に追加する。**これは集合専用っぽい。**
set_x.add("Banana")
print("add(\"Banana\"):=> " + str(set_x))
# 引数を集合から取り出す。引数が含まれていないと「KeyError」送出。
set_x.remove("桃")
print("remove(\"桃\"):=> " + str(set_x))
# 集合から取り出して返す、集合が空の場合にのみ「KeyError」送出。
set_x.pop()
print("pop():=> " + str(set_x))
# 引数が集合に含まれている場合にのみ取り除く（便利）。**これも集合専用っぽい。**
set_x.discard("Mango")
print("discard(\"Mango\"):=> " + str(set_x))
# 全ての要素を集合から取り除き、空の集合にする。
set_x.clear()
print("clear():=> " + str(set_x))
# 集合を削除する
del set_x
print("del set_x:=> ")

try:
    print(set_x)
except Exception as e:
    print(e)
