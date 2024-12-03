# 2024/05/22 kerong
import time
from Tool.get_hollow_screen import bring_window_to_front
from Tool.Actions import take_action, take_direction

# 定義動作名稱和方向名稱
action_name = ["Attack", "Attack_Up",
              "Short_Jump", "Mid_Jump", "Skill_Up",
              "Skill_Down", "Rush", "Cure"]

move_name = ["Move_Left", "Move_Right", "Turn_Left", "Turn_Right"]

action_index = 0
direction_index = 0
ACTION_DIM = 7
LEARNING_RATE = 0.00001  # 学习率
GAMMA = 0
HP_WIDTH = 768
HP_HEIGHT = 407
WIDTH = 400
HEIGHT = 200
ACTION_DIM = 7
FRAMEBUFFERSIZE = 4
INPUT_SHAPE = (FRAMEBUFFERSIZE, HEIGHT, WIDTH, 3)

# 通過索引執行動作
def execute_action(action_index):
    if 0 <= action_index < len(action_name):
        take_action(action_index)
    else:
        print(f"無效的動作索引: {action_index}")

# 通過索引執行方向
def execute_direction(direction_index):
    if 0 <= direction_index < len(move_name):
        take_direction(direction_index)
    else:
        print(f"無效的方向索引: {direction_index}")


# 主函數
def main():
    # model = Model(INPUT_SHAPE, ACTION_DIM)
    # algorithm = DQN(model, gamma=GAMMA, learnging_rate=LEARNING_RATE)
    # agent = Agent(ACTION_DIM, algorithm, e_greed=0.12, e_greed_decrement=1e-6)
    # move, action = agent.sample(stations, soul)
    # 例子：執行動作和方向
    for i in range(len(action_name)):
        print(action_name[i])
        execute_action(i)
        time.sleep(1)
    # execute_action(0)  # 執行 Attack
    # execute_direction(0)  # 執行 Move_Left


if __name__ == "__main__":
    bring_window_to_front()
    main()
# # 例子：執行動作和方向
# execute_action(0)  # 執行 Attack
# execute_direction(0)  # 執行 Move_Left