r,b=list(map(int,input().split()))

max_days=0
diff=0

while r > 0 and b > 0:
    diff += 1
    r -= 1   
    b -= 1

while b > 1:
    max_days += 1
    b -= 2

while r > 1:
    max_days += 1
    r -= 2


print(diff,max_days)