def solution(board, h, w):
    count = 0
    n = len(board)

    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]

    for i in range(4):
        nh = h + dh[i]
        nw = w + dw[i]

        if 0 <= nh < n and 0 <= nw < n:
            if board[h][w] == board[nh][nw]:
                count += 1

    return count