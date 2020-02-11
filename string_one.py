# -*- coding: utf-8 -*-
"""\
PythonができるStringの事。上巻：文字列の基本
Pythonの基本を学習するためのソースコード

Author:
    Hideo Tsujisaki
"""

# ***文字列の宣言***
mojimoji1 = '神は言っている。ここので死ぬ定めではないと。'
mojimoji2 = "各いう私も童貞でね。"

# シングルクォートを文字として出力
mojimoji3 = "I'm so happy."
# ダブルクォートを文字として出力
mojimoji4 = '田中敦彦曰く"人生は祭りだ"'

# 三連引用符
mojimoji5 = """I am GODS child
こんなものの
ために生まれたんじゃない
"""

# 三連引用符をソースコード上見やすくする、改行させない出力
mojimoji6 = """\
I am GODS child
こんなものの
ために生まれたんじゃない
"""
# 文字列をメソッド無しで結合
mojimoji7 = "ABC" "DEF"
mojimoji8 = mojimoji2 + mojimoji3
mojimoji9 = mojimoji2 + "Hello."

# 長い文字列をソースコード上見やすくする
mojimoji10 = "聡明な伴侶を得られれば得よ。得られぬならば孤独に暮らせ。"
"悪をなさず。求めるところは少なく。林の中の象のように。ーーー仏陀"

# ***エスケープ文字***
"""
改行：\n
復帰：\r
垂直タブ：\f
ダブル：\"
シングル：\'
タブ：\t
バックスラッシュ：\\
"""

# ***文字列のインデックス指定***
index_str = "I heard there was secret code."
# 始まりは0から
index_str[0]
# マイナスのインデックスも受け付ける
index_str[-8]

# ***スライシング***
index_str[3:6]
# マイナスでもいけます
index_str[3:-7]
# 終わりがなげければ最後まで出力する
index_str[3:]
# 始まりがなければ最初から出力する
index_str[:12]
# 終わりが範囲外でもなんとかしてくれる
index_str[3:30]
# 始まりが範囲外では空文字を返し、エラーとはならない。
index_str[30:40]
"""
実行
"""
print("＊＊＊文字列の宣言＊＊＊")
print("シングルクォート：" + mojimoji1)
print("ダブルクォート：" + mojimoji2)
print()
print("---クォートを文字として出力する---")
print("シングルクォート文字：" + mojimoji3)
print("ダブルクォート文字：" + mojimoji4)
print()
print("---三連引用符。最初を改行するorしない---")
print("改行そのまま：" + mojimoji5)
print("改行をキャンセルしても上と同じ出力：" + mojimoji6)
print()
print("---文字列結合---")
print("リテラル同士：" + mojimoji7)
print("変数同士：" + mojimoji8)
print("リテラルと変数：" + mojimoji9)
print("ソースコード上は見やすく、出力は普通の結合：" + mojimoji10)
print()
print()
print("＊＊＊エスケープ文字＊＊＊")
print("改で改行" + "改\n行")
print("復帰：ABC\rDEF")
print("垂直タブ：\f")
print("ダブル：\"シングル：\'")
print("タブ：ABC\tDEF")
print("バックスラッシュ：\\")
print()
print()
print("＊＊＊インデックス指定＊＊＊")
print('index_str = "I heard there was secret code."')
print("index_str[0]：" + index_str[0])
print("index_str[-8]：" + index_str[-8])
print("index_str[3:6]：" + index_str[3:6])
print()
print()
print("＊＊＊スライシング＊＊＊")
print("index_str[3:6]：" + index_str[3:6])
print("index_str[3:-7]：" + index_str[3:-7])
print("index_str[3:]：" + index_str[3:])
print("index_str[:12]：" + index_str[:12])
print("index_str[3:30]：" + index_str[3:30])
print("index_str[30:40]：" + index_str[30:40])
