# -*- coding: utf-8 -*-
"""\
Python3の美麗なる辞書-2

Author:
    Hideo Tsujisaki
"""

from pprint import pprint, pformat

print("＊＊＊辞書の整形出力＊＊＊")
bunnsyo = """\
I thought what I'd do was, I'd pretend\
I was one of those deaf-mutes or should I?\
"""
print("bunnsyo:=> " + bunnsyo)
moji_dict = {}
for character in bunnsyo:
    moji_dict.setdefault(character, 0)
    moji_dict[character] += 1
print("＊＊＊pprint()＊＊＊")
pprint(moji_dict)
print("＊＊＊pformat()＊＊＊")
print(pformat(moji_dict))
print()
print("＊＊＊内包表記＊＊＊")
moji_dict2 = {}
moji_dict2 = {moji_dict2.setdefault(character, 0) for character in bunnsyo}

pprint(moji_dict)
