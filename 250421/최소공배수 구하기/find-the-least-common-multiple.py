import math

def lcm(n,m):
    return abs(n * m) // math.gcd(n,m)

n, m = map(int, input().split())

print(lcm(n,m))
# Please write your code here.
