# Hollow_Knight_RL

# Link
https://www.youtube.com/watch?v=EeooyhH2kHc

# 🏆 Reinforcement Learning in *Hollow Knight* with Image Processing

## 📌 Overview

This project explores the application of **Deep Reinforcement Learning (DRL)** in the side-scrolling action game *Hollow Knight*. By leveraging **image processing techniques** and **deep learning models**, we aim to train an AI agent capable of autonomously navigating and making optimal decisions in the game environment.

Through this research, we contribute to **AI-driven gameplay learning**, emphasizing the potential of **vision-based reinforcement learning** in complex, dynamic gaming environments.

---

## 🎯 Objectives

- 🕹 **Train an AI agent** to autonomously play *Hollow Knight* using **Deep Reinforcement Learning**.
- 🎥 **Utilize image processing** to extract meaningful features from raw game footage.
- 🧠 **Leverage neural networks** (e.g., CNNs, ResNet) to improve **decision-making strategies**.
- 📊 **Evaluate performance** across different architectures and training strategies.

---

## ⚙️ Methodology

### 1️⃣ **Game Environment**
- The game *Hollow Knight* is used as the **training environment**.
- Gameplay footage is captured and converted into **image frames** for processing.

### 2️⃣ **Image Processing & Feature Extraction**
- **Preprocessing**: Convert game frames into grayscale, resize, and normalize pixel values.
- **Feature extraction**: Use **ResNet-based Convolutional Neural Networks (CNNs)** to analyze and extract features.
- **Frame Stacking**: Stack consecutive frames to capture motion dynamics.

### 3️⃣ **Deep Reinforcement Learning (DRL)**
- **Algorithm**: Implement **Deep Q-Network (DQN)** to enable the agent to learn through trial and error.
- **State Representation**: Use **processed image frames** as input to the neural network.
- **Action Selection**: Choose the best action based on the **Q-values** estimated by the network.
<!--
# Action
## 攻擊
| 動作名稱 |     動作函數     |    按鍵    |
|:----:|:------------:|:--------:|
|  攻擊  |   Attack()   |    X     |
| 向上攻擊 | Attack_Up()  |  UP + X  |
| 短跳躍  | Short_Jump() | C + DOWN |
| 中跳躍  |  Mid_Jump()  |    C     |
| 向上技能 |  Skill_Up()  |  UP + Z  |
| 向下技能 | Skill_Down() | DOWN + Z |
|  衝刺  |    Rush()    | 左 Shift  |
|  治療  |    Cure()    |    A     |

## 移動
|  動作名稱  |     動作函數     |      按鍵      |
|:------:|:------------:|:------------:|
| 沒有任何動作 |  Nothing()   |      無       |
|   向左   | Move_Left()  |  LEFT(long)  |
|   向右   | Move_Right() | RIGHT(long)  |
|  轉頭左   | Turn_Left()  | LEFT(short)  |
|  轉頭右   | Turn_Right() | RIGHT(short) |
-->

## References 
- [Playing Atari with Deep Reinforcement Learning](https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf)
- [Deep Reinforcement Learning with Double Q-learning](https://arxiv.org/abs/1509.06461)
- [Dueling Network Architectures for Deep Reinforcement Learning](https://arxiv.org/abs/1511.06581)
- [Spectral Normalisation for Deep Reinforcement Learning: an Optimisation Perspective](https://arxiv.org/abs/2105.05246)
- [Rainbow: Combining Improvements in Deep Reinforcement Learning](https://arxiv.org/abs/1710.02298)
- [Image Augmentation Is All You Need: Regularizing Deep Reinforcement Learning from Pixels](https://arxiv.org/abs/2004.13649)
- [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385)
- [Squeeze-and-Excitation Networks](https://arxiv.org/abs/1709.01507)
- [A ConvNet for the 2020s](https://arxiv.org/abs/2201.03545)
- [Bag of Tricks for Image Classification with Convolutional Neural Networks](https://arxiv.org/pdf/1812.01187.pdf)
- [Noisy Networks for Exploration](https://arxiv.org/abs/1706.10295)
- [The Primacy Bias in Deep Reinforcement Learning](https://arxiv.org/abs/2205.07802)
- [Prioritized Experience Replay](https://arxiv.org/abs/1511.05952)
- [Stabilizing Deep Q-Learning with ConvNets and Vision Transformers under Data Augmentation](https://arxiv.org/abs/2107.00644)
- [Averaged-DQN: Variance Reduction and Stabilization for Deep Reinforcement Learning](https://arxiv.org/abs/1611.01929)

- https://github.com/toshikwa/fqf-iqn-qrdqn.pytorch/blob/master/fqf_iqn_qrdqn/network.py
- https://github.com/pytorch/vision/blob/main/torchvision/models/vgg.py
- https://www.youtube.com/watch?v=NP8pXZdU-5U
- https://github.com/seermer/HollowKnight_RL
- https://github.com/ailec0623/DQN_HollowKnight
