# -*- coding: utf-8 -*-
"""\
PythonができるStringの事。中巻：正規表現
Pythonの基本を学習するためのソースコード6

9 - 10

Author:
    Hideo Tsujisaki
"""

import re

# 9.文字集合と独自の集合
# \dは数字を意味する
# (1|2|3|4|5|6|7|8|9|0)の短縮系、その他の短縮型など後述する
xmas_regex = re.compile(r"\d+\s\w+")
print(
    xmas_regex.findall("12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids,"
                       "7 swans, 6 geese, 5 rings, "
                       "4 birds, 3 hens, 2 doves, 1 partridge"))
# 独自に集合を定義する
vowel_regex = re.compile(r"[aeiouAEIOU]")
print(vowel_regex.findall("RoboCop eats baby food. BABY FOOD."))
# キャレットで「それ以外」となる
vowel_regex1 = re.compile(r"[^aeiouAEIOU]")
print(vowel_regex1.findall("RoboCop eats baby food. BABY FOOD."))

# 10.キャレットとドル記号
# キャレットには「先頭に一致するものがあるかどうか」という働きもある
begins_with_hello = re.compile(r"^Hello")
print(begins_with_hello.search("Hello world!"))
print(begins_with_hello.search("He said Hello."))

# ドルは終わりに一致するものがあるかどうかをみてくれるようになる。
ends_with_number = re.compile(r"\d$")
print(ends_with_number.search("Your number is 42"))
print(ends_with_number.search("Your are 42 years old."))
# キャレットとドルで囲むと「全体の中に〜が一致するか」となる。
whole_string_is_num = re.compile(r"^\d+$")
print(whole_string_is_num.search("123456789"))
print(whole_string_is_num.search("12345xyz6789"))
print(whole_string_is_num.search("1234 56789"))
"""実行"""
print()
