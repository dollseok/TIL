n,m = map(int,input().split())
data = list(map(int,input().split()))

left = 0
right = 0
cnt = 0

while True:
    _sum = sum(data[left:right+1])
    # 결과값 검토
    if _sum == m:
        cnt += 1

    # 끝내는 부분
    if left >= n - 1 and right >= n - 1:
        break

    # 다음 단계로 넘어감
    if left == right and right < n-1:
        right += 1
    else:  # left < right
        if _sum < m:
            if right < n-1:
                right += 1
            else:
                left += 1

        elif _sum >= m:
            if left < n-1:
                left += 1


print(cnt)