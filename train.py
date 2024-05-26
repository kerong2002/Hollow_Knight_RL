import tensorflow as tf
import time
import collections

from Model import Model
from DQN import DQN
from Agent import Agent
from ReplayMemory import ReplayMemory
from Test_Tool.get_hollow_screen import bring_window_to_front

import Tool.Helper
import Tool.Actions
from Tool.Actions import take_action, restart,take_direction
from Tool.GetHP import Hp_getter
from Tool.FrameBuffer import FrameBuffer

window_size = (0,0,1920,1017)
station_size = (230, 230, 1670, 930)

HP_WIDTH = 768
HP_HEIGHT = 407
WIDTH = 400
HEIGHT = 200
ACTION_DIM = 8
FRAMEBUFFERSIZE = 4
INPUT_SHAPE = (FRAMEBUFFERSIZE, HEIGHT, WIDTH, 3)

MEMORY_SIZE = 200
MEMORY_WARMUP_SIZE = 24
BATCH_SIZE = 10
LEARNING_RATE = 0.00001
GAMMA = 0
DEBUG_MODE = True


action_name = ["Attack", "Attack_Up",
              "Short_Jump", "Mid_Jump", "Skill_Up",
              "Skill_Down", "Rush", "Cure"]

move_name = ["Move_Left", "Move_Right", "Turn_Left", "Turn_Right"]

DELAY_REWARD = 1




def run_episode(hp, algorithm,agent,act_rmp_correct, move_rmp_correct,PASS_COUNT,paused):
    restart()
    print_debug("Run_episode")
    # learn while load game
    for i in range(8):
        if (len(move_rmp_correct) > MEMORY_WARMUP_SIZE):
            print_debug("move learning")
            batch_station,batch_actions,batch_reward,batch_next_station,batch_done = move_rmp_correct.sample(BATCH_SIZE)
            algorithm.move_learn(batch_station,batch_actions,batch_reward,batch_next_station,batch_done)   

        if (len(act_rmp_correct) > MEMORY_WARMUP_SIZE):
            print_debug("action learning")
            batch_station,batch_actions,batch_reward,batch_next_station,batch_done = act_rmp_correct.sample(BATCH_SIZE)
            algorithm.act_learn(batch_station,batch_actions,batch_reward,batch_next_station,batch_done)

    
    step = 0
    total_reward = 0

    DelayStation = collections.deque(maxlen=DELAY_REWARD + 1) # 1 more for next_station
    DelayActions = collections.deque(maxlen=DELAY_REWARD)
    DelayDirection = collections.deque(maxlen=DELAY_REWARD)
    
    while True:
        boss_hp_value = hp.get_boss_hp()
        self_hp = hp.get_self_hp()
        boss_str = "Boss hp = " + str(boss_hp_value)
        self_str = "Hero hp = " + str(self_hp)
        print_debug(boss_str)
        print_debug(self_str)
        if boss_hp_value > 800 and  boss_hp_value <= 900 and self_hp >= 1 and self_hp <= 9:
            break
        

    thread1 = FrameBuffer(1, "FrameBuffer", WIDTH, HEIGHT, maxlen=FRAMEBUFFERSIZE)
    thread1.start()

    while True:
        step += 1
        
        while(len(thread1.buffer) < FRAMEBUFFERSIZE):
            time.sleep(0.1)
        
        stations = thread1.get_buffer()
        boss_hp_value = hp.get_boss_hp()
        self_hp = hp.get_self_hp()
        # player_x, player_y = hp.get_play_location()
        # hornet_x, hornet_y = hp.get_hornet_location()
        soul = hp.get_souls()

        # hornet_skill1 = False
        # if last_hornet_y > 32 and last_hornet_y < 32.5 and hornet_y > 32 and hornet_y < 32.5:
        #     hornet_skill1 = True
        # last_hornet_y = hornet_y

        move, action = agent.sample(stations, soul)

        take_direction(move)
        take_action(action)

        next_station = thread1.get_buffer()
        next_boss_hp_value = hp.get_boss_hp()
        next_self_hp = hp.get_self_hp()

        act_reward, done = Tool.Helper.action_judge(boss_hp_value, next_boss_hp_value,self_hp, next_self_hp, action)


        DelayStation.append(stations)
        DelayActions.append(action)
        DelayDirection.append(move)

        station = next_station
        self_hp = next_self_hp
        boss_hp_value = next_boss_hp_value

        total_reward += act_reward
        paused = Tool.Helper.pause_game(paused)

        if done == 1:
            Tool.Actions.Nothing()
            time.sleep(6)
            break
        elif done == 2:
            PASS_COUNT += 1
            Tool.Actions.Nothing()
            time.sleep(6)
            break
        

    thread1.stop()

    for i in range(8):
        if (len(move_rmp_correct) > MEMORY_WARMUP_SIZE):
            # print("move learning")
            batch_station,batch_actions,batch_reward,batch_next_station,batch_done = move_rmp_correct.sample(BATCH_SIZE)
            algorithm.move_learn(batch_station,batch_actions,batch_reward,batch_next_station,batch_done)   

        if (len(act_rmp_correct) > MEMORY_WARMUP_SIZE):
            # print("action learning")
            batch_station,batch_actions,batch_reward,batch_next_station,batch_done = act_rmp_correct.sample(BATCH_SIZE)
            algorithm.act_learn(batch_station,batch_actions,batch_reward,batch_next_station,batch_done)

    return total_reward, step, PASS_COUNT, self_hp

def print_debug(str):
    if DEBUG_MODE:
        print(str)

if __name__ == '__main__':
    bring_window_to_front()
    config = tf.compat.v1.ConfigProto(allow_soft_placement=True)
    config.gpu_options.allow_growth = True      #程序按需申请内存
    sess = tf.compat.v1.Session(config = config)

    
    total_remind_hp = 0

    act_rmp_correct = ReplayMemory(MEMORY_SIZE, file_name='./actx_memory')         # experience pool
    move_rmp_correct = ReplayMemory(MEMORY_SIZE,file_name='./move_memory')         # experience pool
    
    # new model, if exit save file, load it
    print_debug("Model start")
    model = Model(INPUT_SHAPE, ACTION_DIM)
    print_debug("Model done")
    # Hp counter
    print_debug("HP search")
    hp = Hp_getter()
    print_debug("HP Get")

    print_debug("load model")
    model.load_model()
    print_debug("load done")

    print_debug("DQN start")
    algorithm = DQN(model, gamma=GAMMA, learnging_rate=LEARNING_RATE)
    print_debug("DQN done")

    print_debug("Setting agent")
    agent = Agent(ACTION_DIM, algorithm, e_greed=0.12, e_greed_decrement=1e-6)
    print_debug("Set done")
    # get user input, no need anymore
    # user = User()

    # paused at the begining
    paused = True
    print_debug("Pause game")
    paused = Tool.Helper.pause_game(paused)

    max_episode = 100
    episode = 0
    PASS_COUNT = 0
    while episode < max_episode:
        episode += 1
        train_str = str(episode) + ":"
        print_debug(train_str)
        total_reward, total_step, PASS_COUNT, remind_hp = run_episode(hp, algorithm,agent,act_rmp_correct, move_rmp_correct, PASS_COUNT, paused)
        if episode % 10 == 1:
            model.save_mode()
        if episode % 5 == 0:
            move_rmp_correct.save(move_rmp_correct.file_name)
        if episode % 5 == 0:
            act_rmp_correct.save(act_rmp_correct.file_name)
        total_remind_hp += remind_hp
        print("Episode: ", episode, ", pass_count: " , PASS_COUNT, ", hp:", total_remind_hp / episode)

