import numpy as np


class Agent:
    def __init__(self,act_dim,algorithm,e_greed=0.1,e_greed_decrement=0):
        self.act_dim = act_dim
        self.algorithm = algorithm
        self.e_greed = e_greed
        self.e_greed_decrement = e_greed_decrement


    def sample(self, station, soul):
        
        pred_move, pred_act = self.algorithm.model.predict(station)

        pred_move = pred_move.numpy()
        pred_act = pred_act.numpy()

        move = np.argmax(pred_move)
        self.e_greed = max(0.03, self.e_greed - self.e_greed_decrement)

        act = np.argmax(pred_act)
        if soul < 33:
            if act == 4 or act == 5:
                pred_act[0][4] = -30
                pred_act[0][5] = -30
        act = np.argmax(pred_act)

        self.e_greed = max(
            0.03, self.e_greed - self.e_greed_decrement)  
        return move,act