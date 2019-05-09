
from node import Node
import queue

class Search:
    def __init__(self, world, start_node):
        self.world = world  # BlocksWorld
        self.start_node = start_node

    def perform_search(self, method):
        if method == 'astar':
            self.a_star()
        elif method == 'breadth':
            self.bfs()
        elif method == 'depth':
            self.dfs()
        elif method == 'best':
            self.best_first()
        else:
            print('Wrong method entered, program exiting...')
            exit(1)

    def a_star(self):

        print('Starting A* Search...')

        nodes_expanded = 0
        curr_node = self.start_node
        q = queue.PriorityQueue()
        node_counter = 0
        q.put((self.world.calc_cost_from_goal(curr_node.world_state), node_counter, curr_node))
        max_stored_nodes = 1

        while True:

            value, node_counter, curr_node = q.get()

            depth = self.calc_depth(curr_node)

            if self.world.is_goal_state(curr_node.world_state):
                break

            for state in self.world.get_moves(curr_node.world_state):
                node = Node(curr_node, state, self.world.calc_cost_from_goal(curr_node.world_state))
                node_counter += 1
                q.put((self.world.calc_cost_from_goal(node.world_state) + depth + 1, node_counter, node))

            nodes_expanded += 1
            if q.qsize() > max_stored_nodes:
                max_stored_nodes = q.qsize()

            self.print_status_astar(curr_node)
        
        self.print_status_astar(curr_node)

        return curr_node

    def calc_depth(self, node):
        count = 0
        while node.parent is not None:
            count += 1
            node = node.parent
            
        return count

    def print_status_astar(self, curr_node):
        for i in curr_node.world_state:
            if i != 'agent':
                print(i, ' ', curr_node.world_state[i])
        print('----------')

    def best_first(self):

        print('Starting A* Search...')

        nodes_expanded = 0
        curr_node = self.start_node
        q = queue.PriorityQueue()
        node_counter = 0
        q.put((self.world.calc_cost_from_goal(curr_node.world_state), node_counter, curr_node))
        max_stored_nodes = 1

        while True:

            value, node_counter, curr_node = q.get()

            depth = self.calc_depth(curr_node)

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

        print('Starting Breadth-First Search...')

        nodes_expanded = 0
        curr_node = self.start_node
        q = queue.Queue()
        q.put(curr_node)
        max_stored_nodes = 1
        

        while True:

            curr_node = q.get()
            if self.world.is_goal_state(curr_node.world_state):
                break
            new_world_states = self.world.get_moves(curr_node.world_state)
            for state in new_world_states:
                node = Node(curr_node, state)
                q.put(node)

            nodes_expanded += 1
            if q.qsize() > max_stored_nodes:
                max_stored_nodes = q.qsize()

            self.print_status_bfs(curr_node)
        self.print_status_bfs(curr_node)

        return curr_node

    # For testing purposes
    def print_status_bfs(self, curr_node):
        for i in curr_node.world_state:
            if i != 'agent':
                print(i, ' ', curr_node.world_state[i])
        print('----------')

    def dfs(self):

        print('Starting Depth-First Search...')

        nodes_expanded = 0
        curr_node = self.start_node
        max_stored_nodes = 0

        while not self.world.is_goal_state(curr_node.world_state):

            new_world_state = self.world.perform_move(curr_node.world_state)
            curr_node = Node(curr_node, new_world_state)

            nodes_expanded += 1
            max_stored_nodes = nodes_expanded

            self.print_status_dfs(curr_node)
        self.print_status_astar(curr_node)

        return curr_node

    # For testing purposes
    def print_status_dfs(self, curr_node):
        for i in curr_node.world_state:
            if i != 'agent':
                print(i, ' ', curr_node.world_state[i])
        print('----------')
