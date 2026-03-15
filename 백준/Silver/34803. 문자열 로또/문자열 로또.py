L, N = map(int, input().split())

lotto_list = [input() for _ in range(N)]

K = int(input())

word_set = set()
word_list = []

for line in lotto_list:
    for i in range(L-K+1):
        l = line[i:i+K]
        word_set.add(l)
        word_list.append(l)

word_dict = {}
for i in word_set:
    word_dict[i] = 0


for w in word_list:
    word_dict[w] += 1

print(max(word_dict.values()))
    