# 1st way
sum = 0
for n in range(1, 101):
    if n % 2 == 0:
        sum += n

print(sum)

# 2nd way
sum2 = 0
for n in range(2, 101, 2):
    sum2 += n

print(sum2)
