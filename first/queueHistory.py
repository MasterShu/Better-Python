import shelve
from collections import deque
from random import randint

q = deque([], 5)

q.append(1)

q.append(2)
q.append(3)
q.append(4)
q.append(5)

# q已经满了, 当继续 append 时,最先进入的就出被移除队列 
q.append(6)

# 做一个简单功能的历史记录
sNumber = randint(0, 100)

history = deque([], 6)
historyFile = 'D:\\python\\learnPython\\res\\history'
def guess(k):
    if k == sNumber:
        print('right')
        return True
    if k < sNumber:
        print(' %s is less than number' % k)
    if k > sNumber:
        print('%s  is greater than number' % k)
    return False
while True:
    line = input("please input you guess number: ")
    if line.isdigit():
        k = int(line)
        history.append(k)
        dbase = shelve.open(historyFile)
        dbase[sNumber] = history
        dbase.close()
        if guess(k):
            break
    elif line == 'history' or line == 'h':
        dbase = shelve.open(historyFile)
        print(dbase[sNumber])
        dbase.close()


