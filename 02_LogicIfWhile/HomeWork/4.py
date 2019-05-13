import math
a = input()
b = input()

k = 0

for i in range(0, len(b), 2):
    k = math.sqrt((b[i] - a[0])**2 + (b[i + 1] - a[1])**2) - a[2]
    if k:
        print "NO"
        break
else:
    print "YES"
