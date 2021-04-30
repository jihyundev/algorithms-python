
# 나이순 정렬
# https://www.acmicpc.net/problem/10814

# 풀이 1

n = int(input())
dic = {}
for _ in range(n):
    age, name = input().split()
    dic[name] = int(age)
sort_dict = sorted(dic.items(), key=lambda item: item[1])
print(sort_dict)
for i in sort_dict:
    print(i[1] + ' ' + i[0])
# 런타임 에러 발생

# 풀이 2
n = int(input())
lst = []
for _ in range(n):
    age, name = input().split()
    lst.append([int(age), name])
lst.sort(key = lambda x : x[0])
for i in range(n):
    print(lst[i][0], lst[i][1])
