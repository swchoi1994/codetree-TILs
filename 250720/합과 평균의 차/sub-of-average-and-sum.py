a,b,c = map(int, input().split())

perf = (a+b+c)//3
print(a+b+c, perf, (a+b+c)-perf, sep="\n")