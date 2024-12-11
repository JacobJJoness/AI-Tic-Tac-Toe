import math
import random


class QLearningAI:
    def __init__(
        self, alpha=1.0, gamma=0.5, epsilon=1.0, decay_rate=0.001, max_trials=10000
    ):
        self.q_table = {}  # Stores Q-values
        self.alpha_initial = alpha
        self.gamma_initial = gamma
        self.epsilon_initial = epsilon
        self.decay_rate = decay_rate
        self.max_trials = max_trials
        self.trial_count = 0

    def dynamic_alpha(self):
        return self.alpha_initial / (1 + self.decay_rate * self.trial_count)

    def dynamic_gamma(self):
        return self.gamma_initial - (self.gamma_initial - 0.5) * (
            self.trial_count / self.max_trials
        )

    def dynamic_epsilon(self):
        return self.epsilon_initial * math.exp(-self.decay_rate * self.trial_count)

    def choose_action(self, state, available_moves):
        self.trial_count += 1
        epsilon = self.dynamic_epsilon()
        if random.random() < epsilon:
            # Exploration: choose a random action
            return random.choice(available_moves)
        else:
            # Exploitation: choose the best action based on Q-values
            q_values = [
                self.q_table.get((tuple(state), move), 0) for move in available_moves
            ]
            max_q = max(q_values)
            best_moves = [
                move for move, q in zip(available_moves, q_values) if q == max_q
            ]
            return random.choice(best_moves)

    def update_q_table(self, state, action, reward, next_state, available_moves):
        alpha = self.dynamic_alpha()
        gamma = self.dynamic_gamma()

        current_q = self.q_table.get((tuple(state), action), 0)
        max_future_q = max(
            [
                self.q_table.get((tuple(next_state), move), 0)
                for move in available_moves
            ],
            default=0,
        )

        # Update Q-value using the Q-learning formula
        self.q_table[(tuple(state), action)] = current_q + alpha * (
            reward + gamma * max_future_q - current_q
        )
