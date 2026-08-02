def solution(s):
    answer = 0

    same = 0
    different = 0
    x = ''

    for char in s:
        if same == 0 and different == 0:
            x = char

        if char == x:
            same += 1
        else:
            different += 1

        if same == different:
            answer += 1
            same = 0
            different = 0

    # 끝까지 읽었는데 개수가 같아지지 않은 문자열도 하나로 분리
    if same != 0 or different != 0:
        answer += 1

    return answer