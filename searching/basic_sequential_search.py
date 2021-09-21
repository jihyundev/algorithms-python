from typing import Any, Sequence
import copy


def seq_search(a: Sequence, key: Any) -> int:
    """ 시퀀스 a에서 key와 값이 같은 원소를 선형 검색 (while문) """
    i = 0
    for i in range(len(a)):
        if a[i] == key:
            return i
    return -1


def sentinel_seq_search(seq: Sequence, key: Any) -> int:
    """ 시퀀스 seq 에서 key와 일치하는 원소를 선형 검색 (보초법) """
    a = copy.deepcopy(seq)
    a.append(key)
    i = 0
    while True:
        if a[i] == key:
            break
        i += 1
    return -1 if i == len(seq) else i


x = [2, 100, 55, 4, 76, 23, 88, 2002, 1996, 2323, 1, 0, 0, 100, 2, 23, 32]
key_number = 100
idx = seq_search(x, key_number)

if idx == -1:
    print('검색값을 갖는 원소가 존재하지 않습니다. ')
else:
    print(f'검색값은 x[{idx}]에 있습니다. ')
