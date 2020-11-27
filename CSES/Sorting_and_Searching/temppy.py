import sys
from bisect import bisect_right
n, m = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))
h.sort()
available = list(range(n + 1))
out = []
for t in list(map(int, sys.stdin.readline().split())):
    old_val = val = bisect_right(h, t)
    while val != available[val]:
        val = available[val]
    while old_val != val:
        available[old_val], old_val = val, available[val]
    if val:
        out.append(str(h[val - 1]))
        available[val] = val - 1
    else:
        out.append('-1')
print('\n'.join(out))

