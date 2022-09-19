def foo(arg):
    j = ''
    for i in range(len(arg) - 1, -1, -1):
        # print(i)
        j += arg[i]
    # print(j)
    return j


data = ["iri", "ada", "viorel", "hnh"]
b = []
k = 0

for e in data:
    if e == foo(e):
        # print(e, foo(e))
        b.append(k)
    k = k + 1
    # print(k)
print(b)

b = [ind for ind, b in enumerate(data) if b[::-1] == b]
print(b)