'''
피로도는 표와 같음
광물 5개 캐면 사용 불가

최소한의 피로도로 광물 캐려고함
한번 사용한 곡괭이는 사용할 수 없을때까지 사용
광물은 주어진 순서대로
광물 모두 캐거나 더 사용할 곡괭이 없을 떄까지 광물 캐기
picks : 곡괭이 개수 [dia, iron, stone] 최대 5개씩
materials : 3개의 문자열 diamond, iron, stone 최대 50개

피로도 최소값 도출

풀이

5개씩 뽑아낼 것

5개씩 잘라서 딕셔너리로 이루어진 리스트로 만들기
dia, iron, stone

'''

def solution(picks, minerals):
    divide_li = []
    mine_cnt_li = [0,0,0]
    cnt = 0
    _limit = min(len(minerals), sum(picks)*5)
    
    # minerals 전체 돌면서 5개씩 자른 리스트
    for i in range(_limit):
        mine = minerals[i]
        cnt += 1
        if mine == 'diamond':
            mine_cnt_li[0] += 1
        elif mine == 'iron':
            mine_cnt_li[1] += 1
        else:
            mine_cnt_li[2] += 1
        
        if cnt == 5 or i == _limit-1:
            divide_li.append(mine_cnt_li)
            cnt = 0 
            mine_cnt_li = [0,0,0]

    
    divide_li.sort(key = lambda x : (x[0],x[1],x[2]),reverse=True)
    print(divide_li)
    
    idx = 0
    result = 0
    for dia_cnt, iron_cnt, stone_cnt in divide_li:
        while picks[idx] == 0:
            idx += 1
            
        # 피로도 계산
        if idx == 0: # 곡괭이가 dia 일 때
            result += dia_cnt + iron_cnt + stone_cnt
        elif idx == 1: # 곡괭이가 iron 일 때
            result += dia_cnt * 5 + iron_cnt + stone_cnt
        else: # 곡괭이가 stone 일 때
            result += dia_cnt * 25 + iron_cnt * 5 + stone_cnt
        
        picks[idx] -= 1

    answer = result
    return answer