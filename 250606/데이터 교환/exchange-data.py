a, b, c = 5,6,7
temp = b
b = a
c_temp = c
c = temp
a_temp = a
a = c_temp

print(a,b,c, sep="\n")