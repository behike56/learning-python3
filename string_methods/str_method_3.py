# -*- coding: utf-8 -*-
"""\
PythonができるStringの事。下巻：文字列メソッド
Pythonの基本を学習するためのソースコード3

15 - 22

Author:
    Hideo Tsujisaki
"""

# 確認用変数
upper_lower_str1 = "ABCDEF"
upper_lower_str2 = "AbCdEf"
upper_lower_str3 = "abcdef"
upper_lower_str4 = "abc空蝉def"
# 15.大文字の判定
upper_lower_str1.isupper()
upper_lower_str2.isupper()
upper_lower_str3.isupper()
upper_lower_str4.isupper()
# 16.小文字の判定
upper_lower_str1.islower()
upper_lower_str2.islower()
upper_lower_str3.islower()
upper_lower_str4.islower()

# 確認用変数
alpha_num_str1 = "orange"
alpha_num_str2 = "2orange"
alpha_num_str3 = "2 orange"
alpha_num_str4 = "orange蜜柑"
# 17.英字の判定
alpha_num_str1.isalpha()
alpha_num_str2.isalpha()
alpha_num_str3.isalpha()
alpha_num_str4.isalpha()
# 18.英字または数字の判定
alpha_num_str1.isalnum()
alpha_num_str2.isalnum()
alpha_num_str3.isalnum()
alpha_num_str4.isalnum()

# 確認用変数
space_str1 = " "
space_str2 = "　"
space_str3 = "\n\t"
space_str4 = " i phone "
# 19.空白文字の判定
space_str1.isspace()
space_str2.isspace()
space_str3.isspace()
space_str4.isspace()

# 確認用変数
title_str1 = "I heard there was a secret code."
title_str2 = "Lion"
title_str3 = "羅生門"
# 20.大文字始まりその他小文字の判定
title_str1.istitle()
title_str2.istitle()
title_str3.istitle()

# 確認用変数
start_end_str1 = "愛新覚羅溥儀"
start_end_str2 = "_愛新覚羅溥儀_"
# 21.始まる判定
start_end_str1.startswith("愛")
start_end_str2.startswith("愛")
# 22.終わる判定
start_end_str1.endswith("儀")
start_end_str2.endswith("儀")
"""実行出力"""
print("15.大文字の判定")
print(upper_lower_str1.isupper())
print(upper_lower_str2.isupper())
print(upper_lower_str3.isupper())
print(upper_lower_str4.isupper())
print()
print("16.小文字の判定")
print(upper_lower_str1.islower())
print(upper_lower_str2.islower())
print(upper_lower_str3.islower())
print(upper_lower_str4.islower())
print()
print("17.英字の判定")
print(alpha_num_str1.isalpha())
print(alpha_num_str2.isalpha())
print(alpha_num_str3.isalpha())
print(alpha_num_str4.isalpha())
print()
print("18.英字または数字の判定")
print(alpha_num_str1.isalnum())
print(alpha_num_str2.isalnum())
print(alpha_num_str3.isalnum())
print(alpha_num_str4.isalnum())
print()
print("19.空白文字の判定")
print(space_str1.isspace())
print(space_str2.isspace())
print(space_str3.isspace())
print(space_str4.isspace())
print()
print("20.大文字始まりその他小文字の判定")
print(title_str1.istitle())
print(title_str2.istitle())
print(title_str3.istitle())
print()
print("21.始まる判定")
print(start_end_str1.startswith("愛"))
print(start_end_str2.startswith("愛"))
print()
print("22.終わる判定")
print(start_end_str1.endswith("儀"))
print(start_end_str2.endswith("愛"))
