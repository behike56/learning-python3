# -*- coding: utf-8 -*-
"""\
PythonができるStringの事。中巻：format()の章
Pythonの基本を学習するためのソースコード

Author:
    Hideo Tsujisaki
"""

import datetime
"""\
インデックスを指定するフォーマット方法
"""
# インデックス指定1
formated_str1 = "安全性能：{0}、運動性能：{1}、燃費性能：{2}".format("A", "B", "C")
# インデックス指定2
formated_str2 = "安全性能：{0}、運動性能：{1}、燃費性能：{2}".format("C", "A", "B")
# インデックス指定3
formated_str3 = "安全性能：{2}、運動性能：{1}、燃費性能：{1}".format("C", "A", "B")
# インデックス指定しない1
formated_str3 = "安全性能：{}、運動性能：{}、燃費性能：{}".format("A", "B", "C")
# インデックス指定しない2
formated_str4 = "安全性能：{}、運動性能：{}、燃費性能：{}".format("A", "C", "B")
# 同じものを何回指定してもOK1
formated_str5 = "{0}{0}{0}{1}{1}{1}{2}{2}{2}".format("A", "C", "B")

# シーケンスをアンパック
formated_str6 = "安全性能：{2}、運動性能：{1}、燃費性能：{0}".format(*"ACB")
listed_str = ["A", "B", "C"]
formated_str7 = "安全性能：{2}、運動性能：{0}、燃費性能：{1}".format(*listed_str)
# 同じものを何回指定してもOK2
formated_str8 = "{0}{0}{0}{1}{1}{1}{2}{2}{2}".format(*listed_str)

# キーと値をメソッドに渡す
car_score1 = "総合得点::レガシィB4:{legacy}_レヴォーグ:{levorg}_WRX S4:{wrx_s4}"
formated_str9 = car_score1.format(legacy="987", levorg="986", wrx_s4="985")

# 辞書を渡してアンパック
dict_score = {"legacy": "987", "levorg": "986", "wrx_s4": "985"}
car_score2 = "総合得点::レガシィB4:{legacy}_レヴォーグ:{levorg}_WRX S4:{wrx_s4}"
formated_str10 = car_score2.format(**dict_score)

# 引数の属性へのアクセス（複素数のモジュール、cmathを使ってみる）
# cmathの属性である、realとimagを呼び出せる
cmath_num = 8 - 8j
formated_str11 = "複素数::{0}_実部:{0.real}_虚部{0.imag}".format(cmath_num)

# 引数の要素へのアクセス
list_fruits = ["apple", "mango", "ichigo", "banana", "mikan", "satsumaimo"]
formated_str12 = "赤い果物:{0[1]}、黄色い果物:{0[4]}".format(list_fruits)

# 変換フラグを使う。!sはstr()、!rはrepr()、!aはascii()
henkan_flg = "str(){!s}, repr(){!r}, ascii(){!a}"
formated_str13 = henkan_flg.format(1234, "1,234", "2345円")

# 文字よせ、<>^が寄せの指定、後ろの数字は文字数
formated_str14 = "{:<50}".format("左寄せ")
formated_str15 = "{:>50}".format("右寄せ")
formated_str16 = "{:^50}".format("中央寄せ")
# 寄せの指定の前の記号で残りの文字を埋める
formated_str17 = "{:@^50}".format("中央寄せ")

# 数値ように符号の表示を指定できる。（マイナスは外せない。）
formated_str18 = "{:+f}; {:+f}".format(10, -20)
formated_str19 = "{:f}; {:f}".format(10, -20)
formated_str20 = "{:-f}; {:-f}".format(10, -20)

# ２進数、８進数、１０進数、１６進数
formated_str21 = "２進数:{0:b}, ８進数:{0:o}, １０進数:{0:d}, １６進数:{0:x}".format(2501)
formated_str22 = "２進数:{0:b}, ８進数:{0:o}, １０進数:{0:d}, １６進数:{0:x}".format(1010)
# プレフィックス付きにする
formated_str23 = "２進数:{0:#b}, ８進数:{0:#o}, １０進数:{0:d}, １６進数:{0:#x}".format(2501)

# カンマ付き
formated_str24 = "{:,}".format(25012501)
# パーセント付き、小数点の桁数も指定
formated_str25 = "{:.3%}".format(100 / 3)

# 年月日時分秒
date = datetime.datetime(2054, 11, 11, 12, 20, 55)
formated_str26 = "{:%Y-%m-%d %H:%M:%S}".format(date)

name = "Kazundo Gouda"
# Python3.6以降 format()が不要
formated_str27 = f"My name is{name}"
# Python3.8以降　format()が不要、変数名＝変数の中身という形で出力
formated_str28 = f"My name is{name=}"
"""
実行
"""
print("***インデックスを指定するフォーマット方法***")
print(formated_str1)
print(formated_str2)
print(formated_str3)
print(formated_str4)
print(formated_str5)
print(formated_str6)
print(formated_str7)
print(formated_str8)
print()
print("***キーを指定するフォーマット方法***")
print(formated_str9)
print(formated_str10)
print(formated_str11)
print(formated_str12)
print(formated_str13)
print(formated_str14)
print(formated_str15)
print(formated_str16)
print(formated_str17)
print()
print("***数値型の表現方法***")
print(formated_str18)
print(formated_str19)
print(formated_str20)
print(formated_str21)
print(formated_str22)
print(formated_str23)
print(formated_str24)
print(formated_str25)
print()
print("***日付型の表現方法***")
print(formated_str26)
print()
print("***割と新しい書き方***")
print(formated_str27)
print(formated_str28)
