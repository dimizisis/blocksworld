
from random import randint


class World:

    def __init__(self, start_state, goal_state, height, width):
        self.start_state = start_state
        self.goal_state = goal_state
        self.height = height
        self.width = width

    def is_goal_state(self, world_state):
        '''
        Checks if a state is a goal state (search algorithm ends)
        :param world_state: current world state
        :return: true if it is a goal state or false if it isn't
        '''

        for i in self.goal_state:
            if self.goal_state[i] != world_state[i]:    # if one is different, goal not reached
                return False
        return True

    def get_moves(self, world_state):
        '''
        Checks acceptable moves & returns them
        :param world_state: current block world state
        :return: possible & acceptable moves
        '''

        agent = world_state['agent']    # all the moves our agent can make
        moves = []
        for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:     # for every move possible (right, down, left, up)
            pos = (agent[0] + i, agent[1] + j)
            if self.check_position(pos):    # check if position after move is acceptable
                new_world_state = dict.copy(world_state)
                for k in world_state:
                    if world_state[k] == pos:
                        new_world_state[k] = agent
                        break
                new_world_state['agent'] = pos  # agent's new position
                moves.append(new_world_state)   # append to moves list
        return moves

    def perform_move(self, world_state):
        '''
        Performs random move (for DFS)
        :param world_state: current world state
        :return: new world state
        '''

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
        '''
        Checks if position (after move) is acceptable
        :param pos: position to be checked
        :return: true if acceptable, false if not
        '''

        return (0 <= pos[0] < self.width) & (0 <= pos[1] < self.height)

    def calc_cost_from_goal(self, world_state):
        '''
        Calculates total cost from goal state (With Manhattan Distance) from a given world state
        :param world_state:
        :return: the cost
        '''
        cost = 0

        for i in self.goal_state:
            pos = world_state[i]
            goal_pos = self.goal_state[i]
            cost += self.h(pos, goal_pos)
        return cost

    def h(self, pos, goal_pos):
        '''
        Heuristic function (Manhattan Distance)
        :param pos: world_state pos
        :param goal_pos: position of goal
        :return: manhattan distance from goal
        '''

        return abs(pos[0] - goal_pos[0]) + abs(pos[1] - goal_pos[1])
