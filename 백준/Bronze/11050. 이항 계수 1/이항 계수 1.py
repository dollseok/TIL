n,k = map(int,input().split())

import itertools
lst = [i for i in range(n)]

nCk = list(itertools.combinations(lst,k))

print(len(nCk))