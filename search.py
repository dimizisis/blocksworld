
from node import Node
import queue


class Search:
    def __init__(self, world, start_node):
        self.world = world  # BlocksWorld
        self.start_node = start_node

    def perform_search(self, method):
        '''
        Triggers search (according to given method)
        :param method: astar/best/depth/breadth
        '''

        if method == 'astar':
            self.a_star()
        elif method == 'breadth':
            self.bfs()
        elif method == 'depth':
            self.dfs()
        elif method == 'best':
            self.best_first()
        else:
            print('Wrong method entered, program exiting...')   # if user enters a non supported method
            exit(1)

    def a_star(self):
        '''
        A* search method, returns a node (if goal state matches)
        :return: a node
        '''

        print('Starting A* Search...')

        nodes_expanded = 0  # how many nodes expanded during search (for printing)
        curr_node = self.start_node     # root node
        q = queue.PriorityQueue()   # priority queue for A* (always take the min)
        node_counter = 0    # counting nodes (for printing)
        q.put((self.world.calc_cost_from_goal(curr_node.world_state), node_counter, curr_node))     # first node to enter the queue
        max_stored_nodes = 1    # max number of nodes to enter the queue (for printing)

        while True:

            value, node_counter, curr_node = q.get()    # pop from priority queue (first iteration --> root node)

            depth = self.calc_depth(curr_node)  # calculate the depth in which the current node exists

            if self.world.is_goal_state(curr_node.world_state):     # if we are in a goal state, end
                break

            for state in self.world.get_moves(curr_node.world_state):   # for every accepted state (after move)
                node = Node(curr_node, state, self.world.calc_cost_from_goal(curr_node.world_state))
                node_counter += 1
                q.put((self.world.calc_cost_from_goal(node.world_state) + depth + 1, node_counter, node))   # insert nodes in queue

            nodes_expanded += 1     # another node expanded
            if q.qsize() > max_stored_nodes:
                max_stored_nodes = q.qsize()    # new max

            self.print_status_astar(curr_node)  # print status after each iteration
        
        self.print_status_astar(curr_node)  # print final status

        return curr_node

    def calc_depth(self, node):
        '''
        Calculates the depth for give node
        :param node: a tree node
        :return: the depth of the node given
        '''

        count = 0
        while node.parent is not None:  # while parent exists, continue until we find root node
            count += 1
            node = node.parent
            
        return count

    def print_status_astar(self, curr_node):
        '''
        Prints blocks & their positions
        :param curr_node: the node given
        '''

        for i in curr_node.world_state:
            if i != 'agent':
                print(i, ' ', curr_node.world_state[i])
        print('----------')

    def best_first(self):
        '''
        Best-First search method, returns a node (if goal state matches) (same with A*, no depth calculation)
        :return: a node
        '''

        print('Starting A* Search...')

        nodes_expanded = 0
        curr_node = self.start_node
        q = queue.PriorityQueue()
        node_counter = 0
        q.put((self.world.calc_cost_from_goal(curr_node.world_state), node_counter, curr_node))
        max_stored_nodes = 1

        while True:

            value, node_counter, curr_node = q.get()

            if self.world.is_goal_state(curr_node.world_state):
                break

            for state in self.world.get_moves(curr_node.world_state):
                node = Node(curr_node, state, self.world.calc_cost_from_goal(curr_node.world_state))
                node_counter += 1
                q.put((self.world.calc_cost_from_goal(node.world_state) + 1, node_counter, node))

            nodes_expanded += 1
            if q.qsize() > max_stored_nodes:
                max_stored_nodes = q.qsize()

            self.print_status_astar(curr_node)
        
        self.print_status_astar(curr_node)

        return curr_node

    def bfs(self):
        '''
        Breadth-First search method, returns a node (if goal state matches)
        :return: a node
        '''

        print('Starting Breadth-First Search...')

        nodes_expanded = 0
        curr_node = self.start_node     # current node --> root node
        q = queue.Queue()   # for BFS we use classic queue
        q.put(curr_node)    # root node
        max_stored_nodes = 1

        while True:

            curr_node = q.get()
            if self.world.is_goal_state(curr_node.world_state):     # if goal reached, end
                break
            new_world_states = self.world.get_moves(curr_node.world_state)
            for state in new_world_states:      # for every acceptable state
                node = Node(curr_node, state)
                q.put(node)

            nodes_expanded += 1
            if q.qsize() > max_stored_nodes:
                max_stored_nodes = q.qsize()

            self.print_status_bfs(curr_node)

        self.print_status_bfs(curr_node)

        return curr_node

    def print_status_bfs(self, curr_node):
        '''
        Prints blocks & their positions
        :param curr_node: the node given
        '''

        for i in curr_node.world_state:
            if i != 'agent':
                print(i, ' ', curr_node.world_state[i])
        print('----------')

    def dfs(self):
        '''
        Depth-First search method, returns a node (if goal state matches)
        :return: a node
        '''

        print('Starting Depth-First Search...')

        nodes_expanded = 0
        curr_node = self.start_node

        while not self.world.is_goal_state(curr_node.world_state):  # while no goal reached

            new_world_state = self.world.perform_move(curr_node.world_state)    # perform random move (random on DFS)
            curr_node = Node(curr_node, new_world_state)    # new current node

            nodes_expanded += 1     # for printing

            self.print_status_dfs(curr_node)

        self.print_status_astar(curr_node)

        return curr_node

    # For testing purposes
    def print_status_dfs(self, curr_node):
        '''
        Prints blocks & their positions
        :param curr_node: the node given
        '''

        for i in curr_node.world_state:
            if i != 'agent':
                print(i, ' ', curr_node.world_state[i])
        print('----------')
