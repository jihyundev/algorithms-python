
# 소트인사이드
# https://www.acmicpc.net/problem/1427

# 첫 번째 풀이

n = 120039
lst = []
digit = 1

while (n // 10) > 0:
    digit += 1
    lst.insert(0, n % 10)
    n = n // 10
    print("n:", n)
lst.insert(0, n)
print("digit:", digit)
lst.sort(reverse=True)
print(lst)
result = 0
for i in range(digit):
    result += lst[-(i+1)] * (10 ** i)
print(result)

# 두 번째 풀이
n = "123454321"
lst = []
for i in n:
    lst.append(int(i))
lst.sort(reverse=True)
for i in lst:
    print(i, end="")
