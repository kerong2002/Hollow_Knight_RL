# 2024/05/22 kerong
# 定義訓練過程中可能需要的操作

from Tool.SendKey import PressKey, ReleaseKey
from Tool.WindowsAPI import grab_screen
import time
import cv2
import threading

# https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes?redirectedfrom=MSDN
UP_ARROW = 0x26    # 上
DOWN_ARROW = 0x28  # 下
LEFT_ARROW = 0x25  # 左
RIGHT_ARROW = 0x27 # 右

L_SHIFT = 0xA0  # 左Shift(衝刺)
A = 0x41        # A(回復)
C = 0x43        # C(跳躍)
X = 0x58        # X(攻擊)
Z = 0x5A        # Z(技能)


# 基本移動

# 沒有任何動作
def Nothing():
    ReleaseKey(LEFT_ARROW)  # 釋放左
    ReleaseKey(RIGHT_ARROW)  # 釋放右
    pass


# 向左
def Move_Left():
    PressKey(LEFT_ARROW)  # 按下左
    time.sleep(0.01)


# 向右
def Move_Right():
    PressKey(RIGHT_ARROW)  # 按下右
    time.sleep(0.01)


# 轉頭左
def Turn_Left():
    PressKey(LEFT_ARROW)  # 按下左
    time.sleep(0.01)
    ReleaseKey(LEFT_ARROW)  # 釋放左


# 轉頭右
def Turn_Right():
    PressKey(RIGHT_ARROW)  # 按下左
    time.sleep(0.01)
    ReleaseKey(RIGHT_ARROW)  # 釋放右


# ----------------------------------------------------------------------

# 其他動作
# 攻擊
def Attack():
    PressKey(X)     # 按下X
    time.sleep(0.15)
    ReleaseKey(X)   # 釋放X
    Nothing()
    time.sleep(0.01)


# 向下攻擊
# def Attack_Down():
#     PressKey(DOWN_ARROW)
#     PressKey(X)
#     time.sleep(0.05)
#     ReleaseKey(X)
#     ReleaseKey(DOWN_ARROW)
#     time.sleep(0.01)

# 向上攻擊
def Attack_Up():
    # print("Attack up--->")
    PressKey(UP_ARROW)      # 按下上
    PressKey(X)             # 按下X
    time.sleep(0.11)
    ReleaseKey(X)           # 釋放X
    ReleaseKey(UP_ARROW)    # 釋放上
    Nothing()
    time.sleep(0.01)


# 短跳躍
def Short_Jump():
    PressKey(C)             # 按下C
    PressKey(DOWN_ARROW)    # 按下下
    PressKey(X)             # 按下X
    time.sleep(0.2)
    ReleaseKey(X)           # 釋放X
    ReleaseKey(DOWN_ARROW)  # 釋放下
    ReleaseKey(C)           # 釋放C
    Nothing()


# 中跳躍
def Mid_Jump():
    PressKey(C)             # 按下C
    time.sleep(0.2)
    PressKey(X)             # 按下X
    time.sleep(0.2)
    ReleaseKey(X)           # 釋放X
    ReleaseKey(C)           # 釋放C
    Nothing()


# 技能
# 4
# def Skill():
#     PressKey(Z)
#     PressKey(X)
#     time.sleep(0.1)
#     ReleaseKey(Z)
#     ReleaseKey(X)
#     time.sleep(0.01)

# 向上技能(震撼波)
def Skill_Up():
    PressKey(UP_ARROW)      # 按下上
    PressKey(Z)             # 按下Z
    PressKey(X)             # 按下X
    time.sleep(0.15)
    ReleaseKey(UP_ARROW)    # 釋放上
    ReleaseKey(Z)           # 釋放Z
    ReleaseKey(X)           # 釋放X
    Nothing()
    time.sleep(0.15)


# 向下技能(震撼波)
def Skill_Down():
    PressKey(DOWN_ARROW)  # 按下下
    PressKey(Z)           # 按下Z
    PressKey(X)           # 按下X
    time.sleep(0.2)
    ReleaseKey(X)         # 釋放X
    ReleaseKey(DOWN_ARROW)# 釋放下
    ReleaseKey(Z)         # 釋放Z
    Nothing()
    time.sleep(0.3)


# 衝刺
def Rush():
    PressKey(L_SHIFT)    # 按下左Shift
    time.sleep(0.1)
    ReleaseKey(L_SHIFT)  # 釋放左Shift
    Nothing()
    PressKey(X)          # 按下X鍵
    time.sleep(0.03)
    ReleaseKey(X)        # 釋放X鍵


# 治療
def Cure():
    print("CURE!!!!!!!!!!!")
    PressKey(A)  # 按下A鍵
    time.sleep(1.4)
    ReleaseKey(A)  # 釋放A鍵
    time.sleep(0.1)


# 重啟新遊戲
def Look_up():
    PressKey(UP_ARROW)  # 按下上
    time.sleep(0.1)
    ReleaseKey(UP_ARROW)  # 釋放上


def restart():
    station_size = (230, 230, 1670, 930)
    while True:
        station = cv2.resize(cv2.cvtColor(grab_screen(station_size), cv2.COLOR_RGBA2RGB), (1000, 500))
        if station[187][300][0] != 0:
            print("未找到重啟")
            time.sleep(1)
        else:
            print("找到重啟")
            break
    time.sleep(1)
    Look_up()
    time.sleep(1.5)
    Look_up()
    time.sleep(1)
    while True:
        station = cv2.resize(cv2.cvtColor(grab_screen(station_size), cv2.COLOR_RGBA2RGB), (1000, 500))
        if station[187][612][0] > 200:
            print("找到開始")
            # PressKey(DOWN_ARROW)
            # time.sleep(0.1)
            # ReleaseKey(DOWN_ARROW)
            PressKey(C)
            time.sleep(0.1)
            ReleaseKey(C)
            break
        else:
            print("未找到開始")
            Look_up()
            time.sleep(0.2)


# 動作函數列表
Actions = [Attack, Attack_Up,       # 動作列表: 攻擊、向上攻擊、
           Short_Jump, Mid_Jump,    # 短跳、中跳、
           Skill_Up,                # 向上技能、
           Skill_Down, Rush, Cure]  # 向下技能、衝刺、治療

Directions = [Move_Left, Move_Right, Turn_Left, Turn_Right]  # 方向函數列表: 左移、右移、左轉、右轉


# 執行動作
def take_action(action):
    Actions[action]()  # 執行動作列表中的指定動作


def take_direction(direc):
    Directions[direc]()  # 執行方向列表中的指定方向


class TackAction(threading.Thread):
    def __init__(self, threadID, name, direction, action):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.direction = direction
        self.action = action

    def run(self):
        take_direction(self.direction)  # 執行方向操作
        take_action(self.action)        # 執行動作操作