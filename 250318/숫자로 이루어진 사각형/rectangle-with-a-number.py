n = int(input())

# Please write your code here.
def printNum(n):
    num = 1
    for i in range(n):
        row = ''
        for j in range(n):
            row += str(num) + ' '
            num += 1
            if num > 9:
                num = 1
        print(row.strip())

printNum(n)