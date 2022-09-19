x = [0, 1]
def foo(arg):
	global x
	while x[-1] < arg:
		x.append(x[-2] + x[-1])
	if arg in x:
		return True
	else:
		return False
# a = []

data = [i for i in range(10)]
# for e in data:
# 	if foo(e):
# 		a.append(True)
# 	else:
# 		a.append(False)
# a = [foo(e) for e in data]
# print(a)
a = list(map(lambda e: foo(e), data))
print(a)
# b = []
# for i in range(len(data)):
# 	if a[i] == True:
# 		b.append(data[i])
# b=[data[i] for i in range(len(data)) if a[i]==True]
b=[data[i] for i in filter(lambda i: a[i] == True, range(len(data)))]
print(b)