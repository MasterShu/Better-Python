from random import randint
from collections import Counter
import re

data = [randint(0, 20) for _ in range(30)]

countTemp = Counter(data)

moreNumber = countTemp.most_common(3)

txt = open('D:\\python\\learnPython\\res\\god.txt', encoding='utf8').read()

txtWordCount = Counter(re.split(r'\W+', txt))
moreWord = txtWordCount.most_common(10)


