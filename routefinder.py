from queue import PriorityQueue
from Graph import Graph, Node, Edge
import math as math

class map_state() :
    ## f = total estimated cost
    ## g = cost so far
    ## h = estimated cost to goal
    def __init__(self, location="", mars_graph=None,
                 prev_state=None, g=0,h=0,x=0,y=0):
        self.location = location
        self.mars_graph = mars_graph
        self.prev_state = prev_state
        # added arguments
        self.x = x
        self.y = y
        self.g = g
        self.h = h
        self.f = self.g + self.h

    def __eq__(self, other):
        return self.location == other.location

    def __hash__(self):
        return hash(self.location)

    def __repr__(self):
        return "(%s)" % (self.location)

    def __lt__(self, other):
        return self.f < other.f

    def __le__(self, other):
        return self.f <= other.f

    def is_goal(self):
        return self.location == '1,1'

# reference: https://stackabuse.com/courses/graphs-in-python-theory-and-implementation/lessons/a-star-search-algorithm/
# reference 2: https://www.simplilearn.com/tutorials/artificial-intelligence-tutorial/a-star-algorithm#:~:text=ProgramExplore%20Program-,What%20is%20an%20A*%20Algorithm%3F,can%20find%20its%20own%20course.
"""
Args:
    start_state: The starting state of the search.
    heuristic_fn: The heuristic function to estimate remaining cost
    goal_test: A function that checks if a state is the goal
    use_closed_list: Wheter to use a closed list to avoid revisiting states
Returns: 
    A list of states representing the solution path, or None if no path is found
"""
def a_star(start_state, heuristic_fn, goal_test, use_closed_list=True) :
    search_queue = PriorityQueue()
    closed_list = {}
    counter = 0
    # Starting state
    start_state.g = 0 # g(n) = 0 for start state
    start_state.h = heuristic_fn(start_state) # this or heuristic_fn instead
    start_state.f = start_state.g + start_state.h #f(n) = g(n) + h(n) delete this one
    search_queue.put((start_state.f, start_state))

    open_list = {start_state: start_state.f} # delete this
    while not search_queue.empty():
        current_f, popped_state = search_queue.get()

        if goal_test(popped_state):
            print(f"Goal found: {popped_state}")
            print(f"counter: {counter}")
            ptr = popped_state.prev_state
            while ptr is not None :
                print(ptr)
                ptr = ptr.prev_state

            return popped_state # Return the goal state

        # that's where I need to generate successors / graph.get_edges(popped_state)
        node = Node(popped_state.location)  # Create node from state's location
        edges = popped_state.mars_graph.get_edges(node)
        for edge in edges:
            succ = map_state(location=edge.dest.value, mars_graph=popped_state.mars_graph, prev_state= popped_state) # Successor Node / neighbor
            # Calculate g, h, and f for the successor
            succ.g = popped_state.g + edge.val  # Assuming each action has cost 1
            succ.h = heuristic_fn(succ)
            succ.f = succ.g + succ.h

            # if successor not in closed list or has better f(n) add to open list
            if succ in closed_list:
                continue

            else:
                closed_list[succ] = True
            counter += 1
            search_queue.put((succ.f,succ))


        #Add the node in the closed list
        # closed_list[]
    print("Test goal not found")
    print(f"States generated BFS: {counter}")
    # that's not what is asked
    return None

def is_complete(state):
    return state.is_goal()
## default heuristic - we can use this to implement uniform cost search
def h1(state) :
    return 0

## you do this - return the straight-line distance between the state and (1,1)
def sld(state) :
    loc = state.location.split(",")
    x1 = int(loc[0])
    x2 = int(loc[1])

    goal_1 = 1
    goal_2 = 1

    return math.sqrt((x1 - goal_1) ** 2 + x2 - goal_2 ** 2)

def read_mars_graph(filename):
    graph = Graph()
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                #strip the whitespace and split  the line by colon
                line = line.strip("\n")
                if not line:
                    continue # skipping empty lines
                # split by the colon to get the source and destinations
                separator = line.split(':')
                if len(separator) !=2:
                    print(f"Line incorrect: {line}")
                    continue
                # Split source node and its value
                src = separator[0].split(',')
                if len(src) != 2:
                    print(f"source incorrect: {separator[0]}")
                    continue
                src_node = src[0] + "," + src[1]
                src_node_to_add = Node(src_node)
                # add source node

                if src_node_to_add not in graph.g:
                    graph.add_node(src_node_to_add)
                # Process the destination nodes
                destinations = separator[1].strip().split() # check this line
                for dest in destinations:
                    dest_info = dest.split(',')
                    if len(dest_info) != 2:
                        print(f"Destination is incorrect: {dest}")
                        continue
                    #Destination node
                    destination_node = dest_info[0] + "," + dest_info[1] # check this line
                    dest_node_to_add = Node(destination_node)
                    # Process the destination nodes

                    if dest_node_to_add not in graph.g:
                        graph.add_node(dest_node_to_add)

                    # Create an edge between the source and destination
                    edge = Edge(src_node_to_add,dest_node_to_add)
                    graph.add_edge(edge)

    except Exception as e:
        print(f"Error processing file {file}: {e}")
    return graph
