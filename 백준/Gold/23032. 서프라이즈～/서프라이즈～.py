'''

N명의 학생이 있다. 2000 이하

임의의 연속된 학번의 학생
두 그룹으로 나눔
한그룹은 학번이 인접

두 그룹의 무게 합 차이 E를 구함

E가 최솟값이 두 그룹의 학생들에게 스테이크 제공
최솟값이 가은 경우면 두 그룹의 스테이크합이 가장 큰 그룹에게 줌

모든 학생의 학번이 인접해야함

i기준을 잡고
그 기준으로 좌우로 확인

2 1 5 2 4 4

N 은 2000까지

i 기준으로 좌우로 나누어서 두 그룹의 무게 합 차이가 최소, 그중에 최대값인 것
1 5 2 / 4 4 => 합의 차이가 0
1 5 /2 4 => 합의 차이가 0
이 둘 중에 위에것이 총합이 커서, 그렇게 결정

4중 포문을 통해서 하나하나 다 위치를 구한 후 합을 구할것 => 100퍼센트 시간초과

누적합을 통해서 최종 값을 빠르게 결정할수있도록
i 기준 시작점을 결정 => 좌우로 뻗어나감 => 최소일 때 저장

'''

n = int(input())

ls = list(map(int,input().split()))

E = 10000000000

result = 0


for i in range(1,n): # 최대 한개는 남겨야함
    left = i - 1
    right = i
    left_sum = ls[left]
    right_sum = ls[right]
    while True:
        diff = abs(right_sum-left_sum)
        if diff == E:
            result = max(result, left_sum + right_sum)
        elif diff < E:
            E = diff
            result = left_sum + right_sum

        if left_sum < right_sum:
            if left == 0:
                break
            left -= 1
            left_sum += ls[left]

        elif left_sum > right_sum:
            if right == n-1:
                break
            right += 1
            right_sum += ls[right]

        else:
            if left == 0 or right == n-1:
                break
            left -= 1
            right += 1
            left_sum += ls[left]
            right_sum += ls[right]


print(result)



