A, B = map(int, input().split())

# First condition: A is less than B
print(1 if A >= B else 0)

# Second condition: A is greater than B
print(1 if A > B else 0)

# Third condition: B is less than A
print(1 if B >= A else 0)

# Fourth condition: B is greater than A
print(1 if B > A else 0)

# Fifth condition: A equals B
print(1 if A == B else 0)

# Sixth condition: A is not equal to B
print(1 if A != B else 0)