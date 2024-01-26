import math

results = []
num1 = int(input("Son kiriting: "))
num2 = int(input("son kiriting: "))
small = min(num1, num2)
ceil_num = math.ceil(small / 2)
for i in range(2, ceil_num + 1):
    if num1 % i == 0 and num2 % i == 0:
        results.append(i)
print(results)
    # print(ceil_num)
    # print(i) 