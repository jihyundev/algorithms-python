# 곱하기 혹은 더하기
# 이코테 p.312 페이스북 인터뷰

# 첫 번째 풀이
s = str(567)
length = len(s)
lst = []
result = 1
for i in range(length):
  lst.append(int(s[i]))
print(lst)
for i in lst:
  if i == 0:
    continue
  else:
    result = result * i
print(result)
# 시간은 초과되지 않으나 리스트를 추가로 만들어야 하는 비효율성 있음
# result 값을 1로 초기화할 수 없는 케이스 존재

# 두 번째 풀이
s = str(567)
result = int(s[0])
for i in range(1, len(s)):
    num = int(s[i])
    print("num: ", num)
    if num <= 1 or result <= 1:
        result += num
        print("result", result)
    else:
        result *= num
        print("result", result)
print(result)
