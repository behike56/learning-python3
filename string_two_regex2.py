# -*- coding: utf-8 -*-
"""\
PythonができるStringの事。中巻：正規表現
Pythonの基本を学習するためのソースコード4

Author:
    Hideo Tsujisaki

3桁-3桁-4桁の電話番号を想定。
受け取る文字列の中に電話番号を見つける。
"""
import re

phone_num_regex = re.compile(r"\d{3}-\d{3}-\d{4}")
mo = phone_num_regex.search("私の電話番号は415-555-4242です。")

print("Telephone Number:" + mo.group())
