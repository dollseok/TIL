from math import gcd
K, N = map(int,input().split())

lst = list(map(int,input().split()))

l = lst[0]
for a in lst[1:]:
    l = l*a // gcd(l,a)

print(l-K)