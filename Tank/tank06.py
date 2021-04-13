import pygame

"""
1，新增坦克speed属性，用来控制坦克移动快慢
2，事件处理：
（1）改变坦克方向
（2）修改坦克的位置(left,top)

"""

_display = pygame.display


class MainGame():
    # 游戏主窗口
    window = None
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 500
    COLOR_BLACK = pygame.Color(0, 0, 0)
    COLOR_RED = pygame.Color(255, 0, 0)
    TANK_P1 = None

    def getTextSurface(self, text):
        # 初始化字体模块   选合适的字体
        pygame.font.init()
        # fontList=pygame.font.get_fonts()
        # print(fontList)
        font = pygame.font.SysFont("kaiti", 18)
        textSruface = font.render(text, True, MainGame.COLOR_RED)
        return textSruface
        # 使用相应的字体完成相关内容的绘制

    def __init__(self):
        pass

    def startGame(self):
        pygame.display.init()
        # self.getTextSurface('aaa')
        MainGame.window = _display.set_mode([MainGame.SCREEN_WIDTH, MainGame.SCREEN_HEIGHT])
        MainGame.TANK_P1 = Tank(400, 330)
        # 设置游戏标题
        _display.set_caption("坦克大战v1.03")
        while True:
            MainGame.window.fill(MainGame.COLOR_BLACK)
            self.getEvent()
            MainGame.window.blit(self.getTextSurface("剩余坦克数量%d" % 5), (5, 5))
            MainGame.TANK_P1.displayTank()
            _display.update()
        pass

    def getEvent(self):
        """
        1.事件处理：获取所有事件
        2.对事件进行判断处理：（1）点击关闭按钮（2）按下键盘上的某个键
        :return:

        """
        eventList = pygame.event.get()
        for event in eventList:
            if event.type == pygame.QUIT:
                self.endGame()
            # 判断按键类型是否为键盘按下，如果是，继续判断按键是哪一个，来进行对应处理
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    # 修改坦克方向
                    MainGame.TANK_P1.direction = "L"
                    MainGame.TANK_P1.move()


                elif event.key == pygame.K_d:
                    MainGame.TANK_P1.direction = "R"
                    MainGame.TANK_P1.move()
                elif event.key == pygame.K_w:
                    MainGame.TANK_P1.direction = "U"
                    MainGame.TANK_P1.move()
                elif event.key == pygame.K_s:
                    MainGame.TANK_P1.direction = "D"
                    MainGame.TANK_P1.move()
                elif event.key == pygame.K_SPACE:
                    print("发射子弹")
        pass

    def endGame(self):
        print("游戏结束")
        exit()


class Tank:

    def __init__(self, left, top):
        self.images = {
            'U': pygame.image.load("img/up.png"),
            'D': pygame.image.load("img/down.png"),
            'L': pygame.image.load("img/left.png"),
            'R': pygame.image.load("img/right.png"),
        }
        self.direction = 'U'
        self.image = self.images[self.direction]
        self.rect = self.image.get_rect()
        self.rect.left = left
        self.rect.top = top
        self.speed = 50

    def move(self):
        if self.direction == 'L':
            if self.rect.left > 0:
                self.rect.left -= self.speed
        elif self.direction == 'R':
            if self.rect.right < MainGame.SCREEN_WIDTH:
                self.rect.left += self.speed
        elif self.direction == "U":
            self.rect.top -= self.speed
        elif self.direction == 'D':
            self.rect.top += self.speed

    def shot(self):
        pass

    def displayTank(self):
        # c重新设置坦克的图片
        self.image = self.images[self.direction]
        # 将坦克加到窗口
        MainGame.window.blit(self.image, self.rect)


class MyTank(Tank):
    def __init__(self):
        pass


class classEnemyTank(Tank):
    def __init__(self):
        pass


class Bullet():
    def __init__(self):
        pass

    def move(self):
        pass

    def displayBullet(self):
        pass


class Explode():
    def __init__(self):
        pass

    def displayExplode(self):
        pass


class Wall():
    def __init__(self):
        pass

    def displayWall(self):
        pass


class Music():
    def __init__(self):
        pass

    def play(self):
        pass


MainGame().startGame()
