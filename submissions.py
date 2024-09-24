from mars_planner import RoverState, action_list, mission_complete, move_to_sample, remove_sample, return_to_charger
from routefinder import read_mars_graph, map_state, a_star, is_complete, sld, h1
from search_algorithms import breadth_first_search, depth_first_search

if __name__ == "__main__":
    state = RoverState()
    result = breadth_first_search(state, action_list, mission_complete)

    state = RoverState()
    result1 = depth_first_search(state, action_list, mission_complete)

    # Sub-problem 1: Move to sample
    print("Sub-problem 1: Move to Sample")
    result_move_to_sample = breadth_first_search(state, action_list, move_to_sample)

    # Sub-problem 2: Remove sample (after moving to sample)
    print("Sub-problem 2: Remove Sample")
    result_remove_sample = breadth_first_search(result_move_to_sample[0], action_list, remove_sample)

    # Sub-problem 3: Return to charger
    print("Sub-problem 3: Return to Charger")
    result_return_to_charger = breadth_first_search(result_remove_sample[0], action_list, return_to_charger)

    map_start = read_mars_graph("MarsMap")

    start_state = map_state(location="8,8", mars_graph=map_start)

    # A* with sld
    a_star(start_state, sld, is_complete, use_closed_list=True)
    print("""

        """)
    # A* with h1
    a_star(start_state, h1, is_complete, use_closed_list=True)