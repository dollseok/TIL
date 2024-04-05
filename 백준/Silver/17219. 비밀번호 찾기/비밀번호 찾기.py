n,m = map(int,input().split())

dict = {}
for _ in range(n):
    site_name, password = input().split()
    dict[site_name] = password

for _ in range(m):
    print(dict[input()])