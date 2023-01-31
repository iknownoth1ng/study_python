def gen(n):
    yield n
    yield n + 1


g = gen(1)

# for i in g:
#     print(i)

print(next(g))


# 生成器表达式
g = (i for i in range(100))
t = [i for i in range(100)]
print(g.__sizeof__())
print(t.__sizeof__())
