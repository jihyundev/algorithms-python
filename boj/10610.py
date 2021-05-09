
# 30
# https://www.acmicpc.net/problem/10610

# 첫 번째 풀이
'''
from itertools import permutations

n = input()
maximum = -1
for i in map(''.join, permutations(n, len(n))):
  integer = int(i)
  if integer % 30 == 0:
    maximum = max(maximum, integer)
print(maximum)
# 시간초과 판정, 리스트를 따로 저장해서 sorting 하는 방식으로는 메모리 초과 판정
'''
# 두 번째 풀이
# 배수판별조건 사용

n = list(input())
n.sort(reverse=True)
sum = 0
if '0' not in n:
    print(-1)
else:
    for i in n:
        sum += int(i)
    if sum%3 != 0:
        print(-1)
    else:
        print(''.join(n))
