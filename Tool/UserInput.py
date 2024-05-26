# 2024/05/22 kerong
# nothing

from Tool.WindowsAPI import key_check
import random

class User:
    def __init__(self):
        self.D = 1              # D：角色方向，0代表左，1代表右
        self.DOWN = False       # DOWN：是否按向下
        self.UP = False         # UP：是否按向上

    def get_user_action(self):
        operation, direction = key_check()

        # 根據按鍵輸入決定動作
        for d in direction:
            if d == 'Left':
                self.D = 0
            elif d =='Right':
                self.D = 1
            elif d == 'Up':
                self.UP = True
            elif d == 'Down':
                self.DOWN = True

        for op in operation:
            if op == 'C':
                return random.randint(6, 8)  # 返回一個隨機動作編號
            elif op == 'X':
                if self.UP:
                    self.UP = False
                    return 5                        # 如果是向上，返回 5（跳躍動作）
                else:
                    if self.D == 0:                 # 左
                        return 3
                    elif self.D == 1:               # 右
                        return 4
            elif op == 'Z':
                if self.UP:
                    self.UP = False
                    return 11                       # 如果是向上，返回 11（特殊動作）
                elif self.DOWN:
                    self.DOWN = False
                    return 12                       # 如果是向下，返回 12（特殊動作）
                else:
                    if self.D == 0:                 # 左
                        return 9
                    elif self.D == 1:               # 右
                        return 10
            elif op == 'Shift':
                if self.D == 0:
                    return 13
                elif self.D == 1:
                    return 14

        if 'Left' in direction:
            return 1                                # 向左移動
        elif 'Right' in direction:
            return 2                                # 向右移動

        return 0                                    # 無動作
