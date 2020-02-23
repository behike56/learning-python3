# -*- coding: utf-8 -*-
"""\
PythonができるStringの事。下巻：文字列メソッド
Pythonの基本を学習するためのソースコード4

23 - 13

Author:
    Hideo Tsujisaki
"""

# 確認用変数
sagasu_str = "桃色桃レンジャー"
print("23.findで探す")
print(sagasu_str.find("桃"))
print(sagasu_str.find("柿"))
print(sagasu_str.rfind("桃"))
print(sagasu_str.rfind("柿"))
print("24.indexで探す")
print(sagasu_str.index("桃"))

try:
    sagasu_str.index("柿")
except Exception as err:
    print(err)

print(sagasu_str.rindex("桃"))

try:
    sagasu_str.rindex("柿")
except Exception as err2:
    print(err2)
