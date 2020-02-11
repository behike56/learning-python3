# -*- coding: utf-8 -*-
"""\
PythonができるStringの事。中巻：正規表現
Pythonの基本を学習するためのソースコード3

Author:
    Hideo Tsujisaki

3桁-3桁-4桁の電話番号を想定。
受け取る文字列の中に電話番号を見つける。
"""


def is_phone_number(text):
    """\
    受け取る文字列が、DDD-DDD-DDDDの形かどうかを調べるメソッド
    Retrun:
        True or Flase
    """
    if len(text) != 12:  # 受け取った文字列が12文字かどうかを判断
        return False

    for i in range(0, 3):  # 文字列の最初の3文字が数字だけか調べる
        if not text[i].isdecimal():
            return False

    if text[3] != '-':  # 4文字目がハイフンかどうか調べる
        return False

    for i in range(4, 7):  # 5文字目から7文字目までが数字だけかどうか調べる
        if not text[i].isdecimal():
            return False

    if text[7] != '-':  # 8文字目がハイフンかどうか調べる
        return False

    for i in range(8, 12):  # 9文字目から12文字目までが数字だけかどうか調べる
        if not text[i].isdecimal():
            return False

    return True


"""\
messageの先頭から12文字を、1文字ずらしながら
is_phone_number()に渡して評価させる。
"""
message = "明日415-555-1011に電話してください。オフィスは415-555-9999です。"
for i in range(len(message)):
    chunk = message[i:i + 12]
    if is_phone_number(chunk):
        print(' 電話番号が見つかりました：' + chunk)

print("完了")
