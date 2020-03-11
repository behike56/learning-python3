# -*- coding: utf-8 -*-
"""\
Python3の数値と演算と数学モジュール
Pythonの基本を学習するためのソースコード

Author:
    Hideo Tsujisaki

型としてはint型かstr型になる。
int型としての表記と、１０進数をstr型に変換する方法がある。
演算はint型どうしとして普通にできる。
"""

# 2, 8, 16
int_bin = 0b1000
int_oct = 0o1000
int_hex = 0x1000
# 大文字でもOK
int_bin_big = 0B1000
int_oct_big = 0O1000
int_hex_big = 0X1000
# 演算もOK、正しprint()では10進数で出力される
int_sum = int_bin + int_oct + int_hex
print(int_sum)
# そのまま出力したい場合は変換関数を使う
ch_bin = bin(128)
ch_oct = oct(128)
ch_hex = hex(128)
print(ch_bin)
print(ch_oct)
print(ch_hex)

# _で区切りを付けられる
sep_int_bin = 0b0110_0101_1010
# 関数と文字列メソッドによる変換
ch_sep_int_bin_1 = format(sep_int_bin, 'b')
ch_sep_int_bin_2 = format(sep_int_bin, '#b')
print(ch_sep_int_bin_1)
print(ch_sep_int_bin_2)
