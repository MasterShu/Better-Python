from random import randint

data = {x: randint(60,100) for x in 'qwerasdfzxcv'}

dataT = zip(data.values(), data.keys())

sortData = sorted(dataT)

sortDataOne = sorted(data.items(), key=lambda x: x[1] )