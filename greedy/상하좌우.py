# 상하좌우
# 이코테 p.110

n = 5
data = ["R", "R", "R", "U", "D", "D"]
x, y = 1, 1

for i in range(len(data)):
    order = data[i]
    if order == "L" and y > 1:
        y -= 1
        print("L")
    elif order == "R" and y < n:
        y += 1
        print("R")
    elif order == "U" and x > 1:
        x -= 1
        print("U")
    elif order == "D" and x < n:
        x += 1
        print("D")
print(x, y)
