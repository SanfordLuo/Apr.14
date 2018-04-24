# 判断 101-200 之间有多少个素数，并输出所有素数
# 素数的特征是除了1和其本身能被整除，其它数都不能被整除的数
for i in range(101, 201):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
