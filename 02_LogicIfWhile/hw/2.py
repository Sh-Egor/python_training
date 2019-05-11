a = input(">")

for i in dir(a):
    if i[0] != '_':
        print(i)
