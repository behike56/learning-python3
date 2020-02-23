# -*- coding: utf-8 -*-
"""\
PythonができるStringの事。下巻：文字列メソッド
Pythonの基本を学習するためのソースコード1

1 - 4

Author:
    Hideo Tsujisaki
"""
# 確認用変数
eiji_str1 = "abcdefg"
eiji_str2 = "ABCDEFG"
eiji_str3 = "AbCdEfG"
eiji_num_str = "AbC33dEfG"
kongou_str = "A千B紫C万d紅e大f車g輪"

# 1.大文字にする
eiji_str1.upper()
eiji_str2.upper()
eiji_str3.upper()
eiji_num_str.upper()
kongou_str.upper()

# 2.小文字にする
eiji_str1.lower()
eiji_str2.lower()
eiji_str3.lower()
eiji_num_str.lower()
kongou_str.lower()

# 3.大文字を小文字、小文字を大文字
eiji_str1.swapcase()
eiji_str2.swapcase()
eiji_str3.swapcase()
eiji_num_str.swapcase()
kongou_str.swapcase()

# 4.文字列型⇆バイナリ型
str_enco_bin = kongou_str.encode('utf-8')
bin_denco_str = str_enco_bin.decode()
"""実行"""
print("1.大文字にする")
print(eiji_str1.upper())
print(eiji_str2.upper())
print(eiji_str3.upper())
print(eiji_num_str.upper())
print(kongou_str.upper())
print()
print("2.小文字にする")
print(eiji_str1.lower())
print(eiji_str2.lower())
print(eiji_str3.lower())
print(eiji_num_str.lower())
print(kongou_str.lower())
print()
print("3.大文字を小文字、小文字を大文字")
print(eiji_str1.swapcase())
print(eiji_str2.swapcase())
print(eiji_str3.swapcase())
print(eiji_num_str.swapcase())
print(kongou_str.swapcase())
print()
print("4.文字列型⇆バイナリ型")
print(str_enco_bin)
print(bin_denco_str)
