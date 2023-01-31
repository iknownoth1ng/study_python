a = [i for i in range(5)]
print(a)


a = [(i, j) for i in range(5) for j in list("ABCD")]
print(a)

# 替代map函数
a = list(map(lambda x: x * 2, range(5)))
a = [i * 2 for i in range(5)]
print(a)

# 替代filter函数
a = list(filter(lambda x: x < 3, range(5)))
a = [i for i in range(5) if i < 3]
print(a)
