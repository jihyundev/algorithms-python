from typing import Any, Sequence


def bin_search(a: Sequence, key: Any) -> int:
    """ 시퀀스 a에서 key와 일치하는 원소를 이진 검색 """
    pl = 0
    pr = len(a) - 1

    while True:
        pc = (pl + pr) // 2
        if a[pc] == key:
            return pc
        elif a[pc] < key:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            break
    return -1


x = [2, 100, 55, 4, 76, 23, 88, 2002, 1996, 2323, 1, 0, 0, 100, 2, 23, 32]
key_number = 100

x.sort()
print(x)
idx = bin_search(x, key_number)
if idx == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다. ')
else:
    print(f'검색값은 x[{idx}]에 있습니다. ')
