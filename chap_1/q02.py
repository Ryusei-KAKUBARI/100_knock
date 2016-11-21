#! usr/bin/env python
# _*_ coding: utf-8 _*_

from itertools import chain

word1 = "パトカー"
word2 = "タクシー"

linking = "".join(chain.from_iterable(zip(word1, word2)))
print(linking)
