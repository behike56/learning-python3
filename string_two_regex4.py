# -*- coding: utf-8 -*-
"""\
PythonができるStringの事。中巻：正規表現
Pythonの基本を学習するためのソースコード6

5-8

Author:
    Hideo Tsujisaki
"""

import re

# 5.プラス＋を用いた1回以上のマッチ。
bat_regex3 = re.compile(r"Bat(wo)+man")
mo1 = bat_regex3.search("The Adventures of Batman")
mo2 = bat_regex3.search("The Adventures of Batwoman")
mo2.group()
mo3 = bat_regex3.search("The Adventures of Batwowowowoman")
mo3.group()

# 6.波括弧{}を用いて繰り返し回数を指定する。
ha_regex = re.compile(r"(Ha){3,5}")
mo4 = ha_regex.search("HaHaHaHaHa")
# Ha1回だけだとマッチしないので「None」が返される
mo5 = ha_regex.search("Ha")

# 7.貪欲マッチ、非貪欲マッチ
# 貪欲＝最長マッチ
greedy_Ha_regex = re.compile(r"(Ha){3,5}")
mo6 = greedy_Ha_regex.search("HaHaHaHaHa")
# 非貪欲＝最短マッチ
nongreedy_Ha_regex = re.compile(r"(Ha){3,5}?")
mo7 = nongreedy_Ha_regex.search("HaHaHaHaHa")
# ?は任意グループの指定と、非貪欲マッチの指定の２つの働きがある

# 8.findall()メソッドを使う
# search()とは違って一致した全ての文字列を返す
# 比較すると。
phone_num_regex = re.compile(r"\d{3}-\d{3}-\d{4}")
mo8 = phone_num_regex.search("cell: 415-555-9999 work: 212-555-0000")
# findall()は文字列のリストを返す
mo9 = phone_num_regex.findall("cell: 415-555-9999 work: 212-555-0000")
# パターンにグループを使うとタプルのリストを返す
phone_num_regex = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
mo10 = phone_num_regex.search("cell: 415-555-9999 work: 212-555-0000")
"""実行"""
print("5.プラス＋を用いた1回以上のマッチ。")
print(mo1)
print(mo2.group())
print(mo3.group())
print()
print("6.波括弧{}を用いて繰り返し回数を指定する")
print(mo4)
print("Ha1回だけだとマッチしないので「None」が返される")
print(mo5)
print()
print("7.貪欲マッチ、非貪欲マッチ")
print("貪欲：最長マッチ")
print(mo6)
print("非貪欲：最短マッチ")
print(mo7)
print()
print("findall()メソッドを使う")
print(mo8.group())
print(str(mo9))
print(str(mo10))
