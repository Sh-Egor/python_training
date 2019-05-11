a = input()
b = sorted(a, reverse=True)
if b[1] == b[0]:
    print "NO"
else:
    print b[1]
