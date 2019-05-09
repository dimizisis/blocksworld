from blocksworld import World
from search import Search
from node import Node
import configparser
import sys
import os


def parse_problem(file):
    '''
    Parses the problem & returns start & goal states
    :param file: path of the input file (the problem)
    :return: start & goal state
    '''

    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))   # current dir (location of .py file)

    try:
        config = configparser.ConfigParser()
        config.read(os.path.join(__location__, file))
    except configparser.MissingSectionHeaderError:
        print('Error reading file. Exiting...')
        exit(1)

    states = dict() # states contains start & goal states
    for section in config.sections():
        states[section] = dict()
        for option in config.options(section):
            states[section][option] = config.get(section, option)

    return states


def create_world(states):
    '''
    Creates blocks world, with start & goal state given
    :param states: start & goal state
    :return: a World object (blocks world)
    '''

    grid_size = list(int(s) for s in states['START']['size'].strip().split(","))    # i.e (3, 3)
    
    world_state = dict()    # dictionary format (i.e): {'size': (3,3), 'a': (2,1), 'b': (0,2), 'agent': (2,2)}
    goal_state = dict()     # dictionary format (i.e): {'a': (3,1), 'b': (2,2)}

    for item in states['START']:
        if item != 'size':
            x, y = states['START'][item].strip().split(",")
            world_state[item] = tuple([int(x), int(y)])

    for item in states['GOAL']:
        x, y = states['GOAL'][item].strip().split(",")
        goal_state[item] = tuple([int(x), int(y)])

    return World(world_state, goal_state, grid_size[0], grid_size[1])


if __name__ == '__main__':

    if len(sys.argv) != 4:
        print('Usage: python main.py <search_method> <input_file> <output_file>')
        exit(1)
    
    search_method = sys.argv[1]     # user must enter astar/best/depth/breadth

    input_file = sys.argv[2]        # input file (ini file)

    states = parse_problem(input_file)      # parse the problem & get the states (start & goal)

    blocks_world = create_world(states)     # create a world object, passing the states

    search = Search(blocks_world, Node(None, dict.copy(blocks_world.start_state), 0))   # create search object

    search.perform_search(search_method)    # perform search with given method
