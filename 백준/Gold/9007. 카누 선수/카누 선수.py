'''

목표값 k , 4개의 반 , n명의 학생 수

4개의 반을 각 sort한 후에
가장 작은 값에서 하나씩 올려서 확인

3초 꽤 길다

2중 for문으로 두개를 골라
나머지 숫자들을 누적합
- 양끝에서 오도록 최대와 최소-> 중간에서 만나도록?
- 시작점 같게? -> 둘중 큰쪽을 유지

- 1/2반 합의 개수 1000 * 1000 => 1,000,000
- 3/4반 합의 개수 
=> 이후에 투포인터
'''

t = int(input())

for _ in range(t):
    k,n = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ab = []
    for i in a:
        for j in b:
            ab.append(i+j)

    c = list(map(int,input().split()))
    d = list(map(int,input().split()))
    cd = []
    for i in c:
        for j in d:
            cd.append(i+j)

    ab = sorted(ab)
    cd = sorted(cd)

    i = 0
    j = len(cd) - 1

    tot = 40000004
    diff = 10e9

    while i < len(ab) and j >= 0:
        current = ab[i] + cd[j] - k

        if abs(current) < diff:
            diff = abs(current)
            tot = current + k
        elif abs(current) == diff:
            tot = min(current+k, tot)

        if current < 0:
            i += 1
        elif current > 0:
            j -= 1
        else:
            break
    print(tot)

