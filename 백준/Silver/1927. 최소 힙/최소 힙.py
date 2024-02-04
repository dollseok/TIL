import sys
input = sys.stdin.readline

class Heap:
    def __init__(self):
        self.heap = [0]

    def insert(self,x):
        # 맨 마지막 원소에 추가
        self.heap.append(x)
        # 부모보다 클때까지 이동
        idx = len(self.heap) -1
        while 1 < idx:
            if self.heap[idx] < self.heap[idx//2]:
                self.swap(idx,idx//2)
                idx = idx // 2
            else:
                break

    def delete(self):
        # 배열이 비엇을 때
        if len(self.heap) == 1:
            return 0
        # 맨 처음이랑 맨 마지막 swap
        self.swap(1,-1)
        # 맨 마지막이 최소임으로 pop
        _min = self.heap.pop()
        self.heap_sort()
        return _min

    def swap(self,idx1,idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1]

    def heap_sort(self):
        # 가장 꼭대기에서 시작
        _idx = 1

        while len(self.heap) > 1:
            _next = _idx
            # 왼쪽 아래 노드가 있고, 값이 왼쪽 아래 노드가 더 작을 때
            if _idx * 2 < len(self.heap) and self.heap[_idx * 2] < self.heap[_next]:
                _next = _idx * 2

            # 오른쪽 아래 노드가 있고, 값이 오른쪽 아래 노드보다 작을 때
            if _idx * 2 + 1 < len(self.heap) and self.heap[_idx * 2 + 1] < self.heap[_next]:
                _next = _idx * 2 + 1

            # 작은 경우가 있다면 _next는 바뀌었을 것 => 위치 바꿈
            if _next != _idx:
                self.swap(_idx, _next)
                _idx = _next
            else:
                break


N = int(input())
_heap = Heap()
for _ in range(N):
    x = int(input())
    if x == 0:
        print(_heap.delete())
    else:
        _heap.insert(x)