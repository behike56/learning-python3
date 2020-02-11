# -*- coding: utf-8 -*-
"""\
PythonができるStringの事。中巻：正規表現
Pythonの基本を学習するためのソースコード7

11 - 13

Author:
    Hideo Tsujisaki
"""

import re
# 11. ワイルドカード
# 11-1 ドットがワイルドカード。1文字にしか当たらない。
print("11-1 ドットがワイルドカード。1文字にしか当たらない。")
at_regex1 = re.compile(r".at")
print(at_regex1.findall("The cat in the hat sat on the flat mat."))
print()

# 11-2ドットとアスタリスクと改行
# 何文字でもOKになる。（改行を含まない）
print("11-2ドットとアスタリスクと改行")
at_regex2 = re.compile(r".*at")
print(at_regex2.findall("The cat in the\n hat sat on the \nflat mat."))
# 改行を含目たい場合は第２引数に「re.DOTALL」を指定する。
at_regex3 = re.compile(r".*at", re.DOTALL)
print(at_regex3.findall("The cat in the\n hat sat on the \nflat mat."))
print()

# 12.大文字、小文字を無視したマッチ
# 大文字小文字を区別する。	区別しない場合は「re.IGNORECACE」または「re.I」
print("12.大文字、小文字を無視したマッチ")
regex = re.compile(r"robocop", re.I)
print(regex.search("RoboCop").group())
print(regex.search("robocoP").group())
print(regex.search("ROBOCOp").group())
# 上記は全てマッチする
print()

# 13.sub()メソッドで置換する
# 第１引数で置換文字、第２引数は置換対象の文字、２が１になる。
print("13.sub()メソッドで置換する")
names_regex = re.compile(r"Agent \w+")
print(
    names_regex.sub("CENSORED", "Agent Alice gave the secret "
                    "document to Agent Bob."))

# マッチした文字を置換の一部として使いたい場合、グループを指定する
print("マッチした文字を置換の一部として使いたい場合、グループを指定する")
agent_names_regex = re.compile(r"Agent (\w)\w*")
# \1がグループの番号
print(
    agent_names_regex.sub(
        r"\1****", "Agent Alice told Agent Carol that"
        " Agent Eve knew Agent Bob was a double agent."))
