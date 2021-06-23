from model import Direction
from model import Location
import random
class GameCoreController:
    def __init__(self):
        self.__list_merge = None
        self.__map = map = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
        ]
    def get_randomInt(self):
        #获取所有0位置
        position_zero = self.get_empty_location()
        if len(position_zero)==0:
            return
        loc=random.choice(position_zero)
        self.__map[loc.row][loc.col]=4 if random.randint(1,10)==4 else 2



    def get_empty_location(self):
        position_zero = []
        for i in range(len(self.__map)):
            for j in range(len(self.__map[0])):
                if self.__map[i][j] == 0:
                    position_zero.append(Location(i, j))
        return position_zero

    @property
    def map(self):
        return self.__map

    def __zero_to_end(self):
        for i in range(len(self.__list_merge)-1,-1,-1):
            if self.__list_merge[i] == 0:
                del self.__list_merge[i]
                self.__list_merge.append(0)

    def __merger_sameNum(self):
        self.__zero_to_end()
        for i in range(len(self.__list_merge) - 1):
            if self.__list_merge[i] == 0:
                return
            if self.__list_merge[i] == self.__list_merge[i + 1]:
                self.__list_merge[i] += self.__list_merge[i + 1]
                del self.__list_merge[i + 1]
                self.__list_merge.append(0)

    def __right_move(self):
        for line in self.__map:
            self.__list_merge=line[::-1]
            self.__merger_sameNum()
            line[::-1]=self.__list_merge

    def __left_move(self):
        for item in self.__map:
            self.__list_merge=item
            self.__merger_sameNum()

    def __ratate_matrix(self, row):
        if row == len(self.__map) - 1:
            return
        for i in range(row, len(self.__map)):
            if i != row:
                self.__map[row][i], self.__map[i][row] = self.__map[i][row],self.__map[row][i]
        self.__ratate_matrix(row + 1)

    def __move_up(self):
        self.__ratate_matrix(0)
        self.__left_move()
        self.__ratate_matrix(0)

    def __move_down(self):
        self.__ratate_matrix( 0)
        self.__right_move()
        self.__ratate_matrix( 0)
        pass


    def move(self,dir):
        if dir==Direction.UP:
            self.__move_up()
        elif dir==Direction.DOWN:
            self.__move_down()
        elif dir==Direction.LEFT:
            self.__left_move()
        elif dir==Direction.RIGHT:
            self.__right_move()
        pass
#-------------------------------------------
if __name__=="__main__":
    gcc=GameCoreController()
    # gcc.get_randomInt()
    # gcc.get_randomInt()
    # gcc.get_randomInt()
    # gcc.get_randomInt()
    # print(gcc.map)
    pass



