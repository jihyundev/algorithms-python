
# 10816 숫자 카드 2
# https://www.acmicpc.net/problem/10816

from typing import Sequence
from sys import stdin

_ = stdin.readline()
cards = sorted(map(int, stdin.readline().split()))

_ = stdin.readline()
numbers = list(map(int, stdin.readline().split()))


def bin_search(a: Sequence, key: int) -> int:
    counter = 0
    pl = 0
    pr = len(a) - 1
    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            counter += 1
            pc_down, pc_up = pc, pc
            while pc_down >= 1:
                pc_down -= 1
                if a[pc_down] == key:
                    counter += 1
                else:
                    break
            while pc_up < len(a) - 1:
                pc_up += 1
                if a[pc_up] == key:
                    counter += 1
                else:
                    break
            return counter
        elif a[pc] > key:
            pr = pc - 1
        else:
            pl = pc + 1
        if pl > pr:
            return counter


def bin_search2(a: Sequence, key: int) -> int:
    pl = 0
    pr = len(a) - 1
    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            pc_low, pc_high = pc, pc
            while pc_low > 0:
                pc_low -= 1
                if a[pc_low] != key:
                    pc_low += 1
                    break
            while pc_high < len(a) - 1:
                pc_high += 1
                if a[pc_high] != key:
                    pc_high -= 1
                    break
            return pc_high - pc_low + 1
        elif a[pc] > key:
            pr = pc - 1
        else:
            pl = pc + 1
        if pl > pr:
            break
    return 0


answer = ""
for num in numbers:
    result = bin_search2(cards, num)
    answer += str(result)
    answer += " "
print(answer)
