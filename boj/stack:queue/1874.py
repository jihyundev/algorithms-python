
# 1874번 스택 수열
# https://www.acmicpc.net/problem/1874

from collections import deque
from typing import Any

class Stack:
    def __init__(self):
        self.__stk = deque()
        self.ptr = 0

    def push(self, value: Any) -> None:
        self.__stk.append(value)
        self.ptr += 1

    def pop(self) -> int:
        if len(self.__stk) > 0:
            return self.__stk.pop()
        else:
            return -1

    def peek(self) -> Any:
        if len(self.__stk) > 0:
            return self.__stk[-1]
        else:
            return -1

n = 8
data = [4, 3, 6, 8, 7, 5, 2, 1]

stk = Stack()
result = []

for i in range(n):
    idx = data[i]
    if idx == stk.peek():
        stk.pop()
        result.append('-')
    elif idx > stk.ptr:
        for j in range(stk.ptr+1, idx+1):
            stk.push(j)
            result.append('+')
        stk.pop()
        result.append('-')
    else:
        result.append('NO')
        break
print(result)
if 'NO' in result:
    print('NO')
else:
    for i in result:
        print(i)
