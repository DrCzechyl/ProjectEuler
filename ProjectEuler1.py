# Divide 3 by each number from 3 to 1000, add to sum if remainder is 0
# Divide 5 by each number from 5 to 1000, add to sum if remainder is 0

sum = 0
for i in range(3, 1000):
    if i % 3 == 0:
        sum += i
    elif i % 5 == 0:
        sum += i
print(sum)
