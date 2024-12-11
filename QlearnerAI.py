import random


class QLearningAI:
    def __init__(self, alpha=0.4, gamma=0.9, epsilon=0.5):
        self.q_table = {}
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon

    def get_q_value(self, state, action):
        return self.q_table.get((tuple(state), action), 0.0)

    def choose_action(self, state, available_moves):
        if random.random() < self.epsilon:
            return random.choice(available_moves)
        q_values = {move: self.get_q_value(state, move) for move in available_moves}
        max_q = max(q_values.values())
        return random.choice([move for move, q in q_values.items() if q == max_q])

    def update_q_table(self, state, action, reward, next_state, available_moves):
        current_q = self.get_q_value(state, action)
        max_next_q = max(
            [self.get_q_value(next_state, move) for move in available_moves], default=0
        )
        new_q = (1 - self.alpha) * current_q + self.alpha * (
            reward + self.gamma * max_next_q
        )
        self.q_table[(tuple(state), action)] = new_q
