

import tensorflow as tf
import os


from Model import Model
from DQN import DQN
from Agent import Agent
from ReplayMemory import ReplayMemory

from Tool.GetHP import Hp_getter


window_size = (0,0,1920,1017)
station_size = (230, 230, 1670, 930)

HP_WIDTH = 768
HP_HEIGHT = 407
WIDTH = 400
HEIGHT = 200
ACTION_DIM = 7
FRAMEBUFFERSIZE = 4
INPUT_SHAPE = (FRAMEBUFFERSIZE, HEIGHT, WIDTH, 3)

LEARN_FREQ = 30
MEMORY_SIZE = 200
MEMORY_WARMUP_SIZE = 24
BATCH_SIZE = 24
LEARNING_RATE = 0.00001
GAMMA = 0.99

action_name = ["Attack", "Attack_Up",
           "Short_Jump", "Mid_Jump", "Skill_Up", 
           "Skill_Down", "Rush", "Cure"]

move_name = ["Move_Left", "Move_Right", "Turn_Left", "Turn_Right"]

DELAY_REWARD = 1


if __name__ == '__main__':

    # In case of out of memory
    config = tf.compat.v1.ConfigProto(allow_soft_placement=True)
    config.gpu_options.allow_growth = True
    sess = tf.compat.v1.Session(config = config)

    PASS_COUNT = 0                                       # pass count
    total_remind_hp = 0

    act_rmp_correct = ReplayMemory(MEMORY_SIZE, file_name='./act_memory')         # experience pool
    act_rmp_wrong = ReplayMemory(MEMORY_SIZE, file_name='./act_memory')           # experience pool
    move_rmp_correct = ReplayMemory(MEMORY_SIZE,file_name='./move_memory')        # experience pool
    move_rmp_wrong = ReplayMemory(MEMORY_SIZE,file_name='./move_memory')          # experience pool
    
    # new model, if exit save file, load it
    model = Model(INPUT_SHAPE, ACTION_DIM)  

    # Hp counter
    hp = Hp_getter()


    model.load_model()
    algorithm = DQN(model, gamma=GAMMA, learnging_rate=LEARNING_RATE)
    agent = Agent(ACTION_DIM,algorithm,e_greed=0.6,e_greed_decrement=1e-6)


    episode = 0

    for x in os.listdir(act_rmp_correct.file_name):
        file_name = act_rmp_correct.file_name + "/" + x
        act_rmp_correct.load(file_name)
        for i in range(10):
            if (len(act_rmp_correct) > MEMORY_WARMUP_SIZE):
                batch_station,batch_actions,batch_reward,batch_next_station,batch_done = act_rmp_correct.sample(BATCH_SIZE)
                algorithm.act_learn(batch_station,batch_actions,batch_reward,batch_next_station,batch_done)

    for x in os.listdir(move_rmp_correct.file_name):
        file_name = move_rmp_correct.file_name + "/" + x
        move_rmp_correct.load(file_name)
        for i in range(10):
            if (len(move_rmp_correct) > MEMORY_WARMUP_SIZE):
                batch_station,batch_actions,batch_reward,batch_next_station,batch_done = move_rmp_correct.sample(BATCH_SIZE)
                algorithm.move_learn(batch_station,batch_actions,batch_reward,batch_next_station,batch_done)

    model.save_mode()

