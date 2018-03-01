# 第一种方式 - 常亮直接赋值 
# NAME = 0
# AGE = 1
# SEX = 2
# EMAIL = 3
# 第一种方式 - 列表派发形式
NAME, AGE, SEX, EMAIL = range(4)

student = ('Tom', 28, 'male', "123@qq.com")

print(student[NAME])

# 第二种方式
from collections import namedtuple

StudentOne = namedtuple('StudentOne', ['name', 'age', 'sex', 'email'])
s = StudentOne('jack', 22, 'male', 'heel@qq.com')

print(s.email)
