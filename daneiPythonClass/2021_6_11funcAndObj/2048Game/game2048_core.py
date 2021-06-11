"""
2048游戏core algorithm


te=[1,2,3,4]
tem=[5,6,7,8]
te[:]=tem[::-1]    右切片  新列表  左切片 只赋值 不产生新列表
print("tem",tem)
print("te",te)
"""

def zero_to_end(list01):
    """
    将0元素移动到末尾
    :param list01:
    :return:
    """
    for i in range(-1,-len(list01)-1,-1):
        if list01[i]==0:
            del list01[i]
            list01.append(0)

def merger_sameNum(lis):
    zero_to_end(lis)
    for i in range(len(lis)-1):
        if lis[i]==0:
            return
        if lis[i]==lis[i+1]:
            lis[i]+=lis[i+1]
            del lis[i+1]
            lis.append(0)
# print(lis)

map=[
    [2,0,0,2],
    [4,4,2,2],
    [2,4,0,4],
    [0,0,2,2],
]
print(map)
def right_move(map):
    for i in range(0, len(map)):
        temp = map[i][::-1]
        merger_sameNum(temp)
        map[i][::-1]=temp

def left_move(map):
    for item in map:
        merger_sameNum(item)

# right_move(map)
def ratate_matrix(matrix,row):
    if row==len(matrix)-1:
        return
    for i in range(row,len(matrix)):
        if i!=row:
            matrix[row][i],matrix[i][row]=matrix[i][row],matrix[row][i]
    ratate_matrix(matrix,row+1)

def move_up(map):
    ratate_matrix(map,0)
    left_move(map)
    ratate_matrix(map,0)

def move_down(map):
    ratate_matrix(map,0)
    right_move(map)
    ratate_matrix(map,0)
    pass

# move_up(map)
move_down(map)
print(map)