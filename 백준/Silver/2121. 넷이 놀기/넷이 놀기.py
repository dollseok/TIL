'''
점들의 개수 N
만들고 싶은 직사각형의 가로,세로 길이 a,b

N개의 좌표

네사람이 1개의 점을 선택해서, x축 , y축에 평행한 직사각형을 만드는 일

50만개의 좌표


'''
n = int(input())

w,h = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

arr.sort()

def parametricSearch(arr,dot):
    s = 0
    e = len(arr) - 1
    while s <= e:
        mid = (s+e) // 2
        if arr[mid] < dot:
            s = mid + 1
        elif arr[mid] > dot:
            e = mid - 1
        else:
            return True

    return False

cnt = 0
for dot in arr:
    leftTop = [dot[0],dot[1] + h]
    rightBottom = [dot[0] + w, dot[1]]
    rightTop = [dot[0] + w, dot[1] + h]

    if (parametricSearch(arr,leftTop) and parametricSearch(arr,rightBottom) and parametricSearch(arr,rightTop)):
        cnt += 1

print(cnt)
