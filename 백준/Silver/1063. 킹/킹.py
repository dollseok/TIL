"""

체스판에서 킹이 돌밀기

"""


move = {
    "R" : [0, 1],
    "L" : [0, -1],
    "B" : [-1, 0],
    "T" : [1, 0],
    "RT": [1, 1],
    "LT": [1, -1],
    "RB": [-1, 1],
    "LB": [-1, -1],
}


location_x = {"A": 0, "B": 1, "C": 2, "D": 3, "E": 4, "F": 5, "G": 6, "H": 7}
location_y = {"1": 0, "2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7}


king,stone,N = input().split()

move_list = [input() for _ in range(int(N))]

king_location = [location_y[king[1]], location_x[king[0]]]
stone_location = [location_y[stone[1]], location_x[stone[0]]]

for m in move_list:
    move_x = move[m][1] # 0
    move_y = move[m][0] # 1
    # 움직이는데 외부
    if king_location[1] + move_x < 0 or king_location[1] + move_x > 7 or king_location[0] + move_y < 0 or king_location[0] + move_y > 7:  
        continue
    
    tmp_king_location = [king_location[0] + move_y, king_location[1] + move_x]
    # 움직이는데 stone 위치
    
    if tmp_king_location[0] == stone_location[0] and tmp_king_location[1] == stone_location[1]:
       if stone_location[1] + move_x < 0 or stone_location[1] + move_x > 7 or stone_location[0] + move_y < 0 or stone_location[0] + move_y > 7:  
          continue
       stone_location = [stone_location[0] + move_y, stone_location[1] + move_x]
    king_location = tmp_king_location

print(list(location_x)[king_location[1]] + list(location_y)[king_location[0]] )
print(list(location_x)[stone_location[1]] + list(location_y)[stone_location[0]])

