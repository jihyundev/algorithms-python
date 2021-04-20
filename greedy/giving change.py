# 거스름돈
# 동전의 최소 개수 구하기 (500원, 100원, 50원, 10원)

# 첫 번째. 경우의 수를 모두 계산하여 구하는 방법
#cash = int(input("거슬러줄 돈을 10의 배수로 입력하세요."))
cash = 1520
count = 0

def calculate(n, p):
  # n은 계산해야 할 돈, p는 동전 단위
  q = n // p
  r = n % p
  return q, r

if cash // 500 > 0:
  q, r = calculate(cash, 500)
  count += q
  print("500 *", q)
  if r // 100 > 0:
    q, r = calculate(r, 100)
    count += q
    print("100 *", q)
    if r // 50 > 0:
      q, r = calculate(r, 50)
      count += q
      print("50 *", q)
      if r // 10 > 0:
        q, r = calculate(r, 10)
        count += q
        print("10 *", q)
    else:
      q, r = calculate(r, 10)
      count += q
      print("10 *", q)
  elif r // 50 > 0:
    q, r = calculate(r, 50)
    count += q
    print("50 *", q)
    if r // 10 > 0:
      q, r = calculate(r, 10)
      count += q
      print("10 *", q)
  else:
    q, r = calculate(r, 10)
    count += q
    print("10 *", q)
elif cash // 100 > 0:
  q, r = calculate(cash, 100)
  count += q
  print("100 *", q)
  if r // 50 > 0:
    q, r = calculate(r, 50)
    count += q
    print("50 *", q)
    if r // 10 > 0:
      q, r = calculate(r, 10)
      count += q
      print("10 *", q)
  else:
    q, r = calculate(r, 10)
    count += q
    print("10 *", q)
elif cash // 50 > 0:
  q, r = calculate(cash, 50)
  count += q
  print("50 *", q)
  if r // 10 > 0:
    q, r = calculate(r, 10)
    count += q
    print("10 *", q)
else:
  q, r = calculate(cash, 10)
  count += q
  print("10 *", q)
print(count)

# 두 번째. 반복문을 이용하여 몫과 나머지를 바로바로 계산하는 방법
n = 1260
count = 0
# 큰 단위 동전부터 차례대로 확인
coin_types = [500, 100, 50, 10]
for coin in coin_types:
    count += n // coin
    n %= coin
print(count)
