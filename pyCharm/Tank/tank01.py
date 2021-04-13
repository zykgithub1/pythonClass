import pygame
"""
first creat game box

"""

_display=pygame.display
class MainGame():
    #游戏主窗口
    window=None
    SCREEN_WIDTH=800
    SCREEN_HEIGHT=500
    COLOR_BLACK=pygame.Color(0,0,0)
    def __init__(self):
        pass
    def startGame(self):
        pygame.display.init()
        MainGame.window=_display.set_mode([MainGame.SCREEN_WIDTH,MainGame.SCREEN_HEIGHT])
        #设置游戏标题
        _display.set_caption("坦克大战v1.03")
        while True:
            MainGame.window.fill(MainGame.COLOR_BLACK)
            _display.update()


        #创建游戏加载窗口  查看官方文档
        pass
    def endGame(self):
        print("游戏结束")
        exit()
class Tank:
    def __init__(self):
        pass
    def move(self):
        pass
    def shot(self):
        pass
    def displayTank(self):
        pass

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
