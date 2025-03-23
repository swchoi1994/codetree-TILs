n, m = map(int, input().split())

def mathCheck(n, m):
    maxNum = 0
    for i in range(1, min(m,n) + 1):
        if n % i == 0 and m % i == 0:
            maxNum = i
    
    print(maxNum)

mathCheck(n, m)
# Please write your code here.