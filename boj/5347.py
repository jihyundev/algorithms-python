
# LCM
# https://www.acmicpc.net/problem/5347

# 약수 구하기
def get_cd(num):
    i = 1
    result = []
    while i <= num:
        if num % i == 0:
            result.append(i)
        i += 1
    return result

def get_gcd(a, b):
    a_cd = get_cd(a)
    b_cd = get_cd(b)
    gcd = 1
    for i in a_cd:
        for j in b_cd:
            if i == j:
                gcd = i
    return gcd

def get_lcm(a, b):
    gcd = get_gcd(a, b)
    x, y = a//gcd, b//gcd
    lcm = gcd * x * y
    return lcm
