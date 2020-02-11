# -*- coding: utf-8 -*-
"""\
PythonができるStringの事。中巻：正規表現
Pythonの基本を学習するためのソースコード4

1-4

Author:
    Hideo Tsujisaki

3桁-3桁-4桁の電話番号を想定。
受け取る文字列の中に電話番号を見つける。
"""

import re

# 1.丸括弧（）を用いてグルーピングする。
# 電話番号を市外局番とそれ以外に分けたい
# gourp()に引数を渡すとマッチした中の指定したグループだけを取得できる。
print("1.丸括弧（）を用いてグルーピングする。")
phone_num_regex = re.compile(r"(\d{3})-(\d{3}-\d{4})")
mo = phone_num_regex.search("私の電話番号は415-555-4242です。")
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))
# groups()で全てのグループをタプル型で取得できる。
print("groups()で全てのグループをタプル型で取得できる。")
area_code, main_number = mo.groups()
print(area_code)
print(main_number)
print()

# 2.縦線｜を用いて複数のグループとマッチする。
# 両方ある場合は最初に出現した方を取得する。
print("2.縦線｜を用いて複数のグループとマッチする。")
hero_regex = re.compile(r"Batman|Tina Fey")
mo1 = hero_regex.search("Batman and Tina Fey.")
print(mo1.group())
mo2 = hero_regex.search("Tina Fey and Batman")
print(mo2.group())
# パターンを複数指定したい場合は丸括弧を使う
# 例えばBatで始まるいくつかの単語をパターンにしたい
print("パターンを複数指定したい場合は丸括弧を使う")
bat_regex = re.compile(r"Bat(man|mobile|copter|bat)")
mo3 = bat_regex.search("Batmobile lost a wheel")
print(mo3.group(0))
print(mo3.group(1))
print()

# 3.疑問符？を用いた任意のマッチング。
# 任意のマッチングなのでマッチしてもしなくても良い場合
print("3.疑問符？を用いた任意のマッチング。")
bat_regex = re.compile(r"Bat(wo)?man")
mo4 = bat_regex.search("The Aventures of Batman")
print(mo4.group())
mo5 = bat_regex.search("The Adventures of Batwoman")
print(mo5.group())
# 市外局番の有無に関係なく検索したい場合
print("市外局番の有無に関係なく検索したい場合")
phone_regex = re.compile(r"(\d{3}-)?\d{3}-\d{4}")
mo6 = phone_regex.search("私の電話番号は415-555-4242")
print(mo6.group())
mo7 = phone_regex.search("私の電話番号は555-4242")
print(mo7.group())
print()

# 4.アスタリスク＊を用いいた0回以上のマッチ。
# ？とほぼ同じ気がする。
print("4.アスタリスク＊を用いいた0回以上のマッチ。")
bat_regex2 = re.compile(r"Bat(wo)*man")
mo8 = bat_regex2.search("The Adventures of Batman")
print(mo8.group())
mo9 = bat_regex2.search("The Adventures of Batwoman")
print(mo9.group())
mo10 = bat_regex2.search("The Adventures of Batwowowowoman")
print(mo10.group())
