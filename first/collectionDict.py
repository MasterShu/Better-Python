from collections import OrderedDict
from time import time
from random import randint

# 有序字典
d = OrderedDict()
d['jimson'] = (1, 25)
d['hube'] = (2, 35)
d['amarad'] = (3, 45)

for orderDict in d:
    print(orderDict)

# 利用 OrderDict 让字典有序
masters = list('QWERTY')
start = time()
masterDict = OrderedDict()

for i in range(6):
    input()
    master = masters.pop(randint(0, 5-i))
    end = time()
    masterDict[master] = (i + 1, end - start)

print('-'*20)

for master in masterDict:
    print(master, masterDict[master])

