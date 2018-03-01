from random import randint, sample
from functools import reduce

data = {x: randint(1, 4) for x in sample('werasdfcxv', randint(3, 9))}
data1 = {x: randint(1, 4) for x in sample('werasdfcxv', randint(3, 9))}
data2 = {x: randint(1, 4) for x in sample('werasdfcxv', randint(3, 9))}

# 第一种方式
# res = []
# for k in data:
#     if k in data1 and k in data2:
#         res.append(k)

# 第二种方式
commonKeys = data.keys() & data1.keys() & data2.keys()

# 第三种方式
commonKeysOne = reduce(lambda a,b: a & b, map(dict.keys, [data, data1, data2]))

