'''
대회 -> 2명의 여학생 1명의 남학생
N여 M남, K명 인턴쉽
인턴쉽은 대회 참여 못함
K명은 인턴쉽 가야한다 필수로

이 인원 내에서 만들어질수있는 최대 팀의 개수

1. 팀 기준 완전 탐색
M이 최대 100 => 최대 팀수 50 => 팀수 1개일때부터 확인해서 모든 조건 만족하는지 체크

'''


N,M,K = map(int,input().split())
cnt = 0
for i in range(1,51):
    if N >= 2*i and M >= i and M+N-3*i >= K:
        cnt += 1
        continue
    else:
        break

print(cnt)