from blocksworld import World
from search import Search
from node import Node
import configparser
import sys
import os

def parse_problem(file):

    __location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

    try:
        config = configparser.ConfigParser()
        config.read(os.path.join(__location__, file))
    except configparser.MissingSectionHeaderError:
        print('Error reading file. Exiting...')
        exit(1)

    states = dict()
    for section in config.sections():
        states[section] = dict()
        for option in config.options(section):
            states[section][option] = config.get(section, option)

    return states

def create_world(states):

    grid_size = list(int(s) for s in states['START']['size'].strip().split(","))
    
    world_state = dict()
    goal_state = dict()

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
    
    search_method = sys.argv[1] # user must enter astar or depth or breadth

    input_file = sys.argv[2]    # input file (ini file)

    states = parse_problem(input_file)  # parse the problem & get the states (start & goal)

    blocks_world = create_world(states) # create a world object, passing the states

    search = Search(blocks_world, Node(None, dict.copy(blocks_world.start_state), 0))   # perform a search

    search.perform_search(search_method)
