import tensorflow as tf
import numpy as np

class PPO:
    def __init__(self, actor_model, critic_model, gamma=0.99, clip_epsilon=0.2, lr_actor=0.0001, lr_critic=0.0002):
        self.actor_model = actor_model  # Actor network
        self.critic_model = critic_model  # Critic network
        self.gamma = gamma
        self.clip_epsilon = clip_epsilon
        self.actor_optimizer = tf.optimizers.Adam(learning_rate=lr_actor)
        self.critic_optimizer = tf.optimizers.Adam(learning_rate=lr_critic)

    def compute_advantages(self, rewards, values, next_values, terminals):
        advantages = []
        gae = 0
        for i in reversed(range(len(rewards))):
            delta = rewards[i] + self.gamma * next_values[i] * (1 - terminals[i]) - values[i]
            gae = delta + self.gamma * gae
            advantages.insert(0, gae)
        return np.array(advantages, dtype=np.float32)

    def train_step(self, obs, actions, old_probs, rewards, next_obs, terminals):
        values = self.critic_model(obs)
        next_values = self.critic_model(next_obs)

        # Compute advantages
        advantages = self.compute_advantages(rewards, values, next_values, terminals)

        # Train Actor
        with tf.GradientTape() as actor_tape:
            logits = self.actor_model(obs)
            probs = tf.nn.softmax(logits)
            action_probs = tf.gather_nd(probs, tf.expand_dims(actions, axis=1), batch_dims=1)
            ratio = action_probs / old_probs

            # PPO clipped loss
            clip_loss = tf.minimum(
                ratio * advantages,
                tf.clip_by_value(ratio, 1 - self.clip_epsilon, 1 + self.clip_epsilon) * advantages
            )
            actor_loss = -tf.reduce_mean(clip_loss)

        # Train Critic
        with tf.GradientTape() as critic_tape:
            target_values = rewards + self.gamma * next_values * (1 - terminals)
            critic_loss = tf.reduce_mean(tf.square(values - target_values))

        # Apply Gradients
        actor_gradients = actor_tape.gradient(actor_loss, self.actor_model.trainable_variables)
        critic_gradients = critic_tape.gradient(critic_loss, self.critic_model.trainable_variables)

        self.actor_optimizer.apply_gradients(zip(actor_gradients, self.actor_model.trainable_variables))
        self.critic_optimizer.apply_gradients(zip(critic_gradients, self.critic_model.trainable_variables))

    def train(self, obs, actions, old_probs, rewards, next_obs, terminals, epochs=3):
        for _ in range(epochs):
            self.train_step(obs, actions, old_probs, rewards, next_obs, terminals)
