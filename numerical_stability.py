billion = 1000000000
epsilon = 0.000001
num = billion
for i in range(1000000):
    num = num + epsilon
num = num - billion
print(num)
