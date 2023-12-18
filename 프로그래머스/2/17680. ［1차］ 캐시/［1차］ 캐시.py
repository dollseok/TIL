"""
1. 문제
도시이름 검색 관련 맛집
DB에서 게시물 가져오는데 넘 오래걸림 -> 로직개선
캐시 교체 알고리즘

없으면 앞에부터 빠짐 -> 큐 - FIFO

캐시 안에 없으면 앞에 것이 빠지고 새로 들어가면서 5
캐시 안에 있으면 1

각 도시 이름은 영문자, 대소문자 구분 x -> 문자열 소문자로 변경해서 비교

2. 시간 복잡도
list - set을 통하여 비교 O(1) => 리스트를 세트로 만드는 과정 (O(N))
in 쓰는과정 => O(N)
스택의 길이 최대 30 -> 30개 안에서만 비교
도시 수 10만개
O(30*10만) -> 충분히 가능

3. 필요한 것
que 최대 길이 cacheSize
"""

import sys
from collections import deque

def solution(cacheSize, cities):
    time = 0
    que = deque()
    for city in cities:
        cityLower = city.lower()
        # hit 못했을 때
        if cityLower not in que:
            time += 5
            que.append(cityLower)
            if len(que) > cacheSize:
                que.popleft()     
        # hit
        else:
            time += 1
            que.remove(cityLower)
            que.append(cityLower)
            
    answer = time
    
    return answer