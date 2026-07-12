from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    q1 = deque(cards1)
    q2 = deque(cards2)
    
    for i in goal:
        if q1 and i == q1[0]:
            q1.popleft()
            goal
        elif q2 and i == q2[0]:
            q2.popleft()
        else:
            return 'No'
    return 'Yes'
    
    
    