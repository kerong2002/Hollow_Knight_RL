# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf

class Agent:
    def __init__(self,act_dim,algorithm,e_greed=0.1,e_greed_decrement=0):
        self.act_dim = act_dim
        self.algorithm = algorithm
        self.e_greed = e_greed
        self.e_greed_decrement = e_greed_decrement


    def sample(self, station, soul):
        
        pred_move, pred_act = self.algorithm.model.predict(station)
        # print(pred_move)
        # print(self.e_greed)
        pred_move = pred_move.numpy()
        pred_act = pred_act.numpy()
        sample = np.random.rand()  
        # if sample < self.e_greed:
        #
        #     move = self.better_move(hornet_x, player_x, hornet_skill1)
        # else:
        move = np.argmax(pred_move)
        self.e_greed = max(
            0.03, self.e_greed - self.e_greed_decrement)  

        sample = np.random.rand() 
        # if sample < self.e_greed:
        #     act = self.better_action(soul, hornet_x, hornet_y, player_x, hornet_skill1)
        # else:
        act = np.argmax(pred_act)
        if soul < 33:
            if act == 4 or act == 5:
                pred_act[0][4] = -30
                pred_act[0][5] = -30
        act = np.argmax(pred_act)

        self.e_greed = max(
            0.03, self.e_greed - self.e_greed_decrement)  
        return move, act