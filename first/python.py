from random import randint
import timeit

data = [randint(-10, 10) for _ in range(10)]

sData = set(data)

# 列表
students = {x : randint(60, 100) for x in range(1,21)}
time1 = timeit.timeit('[x for x in data if x >= 0]', globals=globals())
print(time1, '2')

time = timeit.timeit('filter(lambda x: x >= 0, data)', globals=globals())

# 字典
highScore = {k:v for k,v in students.items() if  v > 90}

# 集合
newData = {x for x in sData if x % 3 == 0}
print(newData, 'newData')
print(highScore)
print(time, '1')
