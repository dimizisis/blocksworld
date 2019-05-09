
from random import randint

class World:

    def __init__(self, start_state, goal_state, height, width):
        self.start_state = start_state
        self.goal_state = goal_state
        self.height = height
        self.width = width

    def is_goal_state(self, world_state):
        for i in self.goal_state:
            if self.goal_state[i] != world_state[i]:
                return False
        return True

    def get_moves(self, world_state):
        agent = world_state['agent']
        moves = []
        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            pos = (agent[0] + i, agent[1] + j)
            if self.check_position(pos):
                new_world_state = dict.copy(world_state)
                for k in world_state:
                    if world_state[k] == pos:
                        new_world_state[k] = agent
                        break
                new_world_state['agent'] = pos
                moves.append(new_world_state)
        return moves

    def perform_move(self, world_state):
        agent = world_state['agent']
        while True:
            i, j = [(1, 0), (0, 1), (-1, 0), (0, -1)][randint(0, 3)]
            pos = (agent[0] + i, agent[1] + j)
            if self.check_position(pos):
                break
        new_world_state = dict.copy(world_state)
        for i in world_state:
            if world_state[i] == pos:
                new_world_state[i] = agent
                break
        new_world_state['agent'] = pos
        return new_world_state

    def check_position(self, pos):
        return (0 <= pos[0] < self.width) & (0 <= pos[1] < self.height)

    def calc_cost_from_goal(self, world_state):
        cost = 0
        for i in self.goal_state:
            pos = world_state[i]
            goal_pos = self.goal_state[i]
            cost += self.h(pos, goal_pos)
        return cost

    def h(self, pos, goal_pos):
        return abs(pos[0] - goal_pos[0]) + abs(pos[1] - goal_pos[1])
