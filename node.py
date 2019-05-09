class Node:

    def __init__(self, parent=None, world_state=None, priority=None):
        self.parent = parent
        self.world_state = world_state
        self.priority = priority

    def __lt__(self, other):
        return self.priority < other.priority
