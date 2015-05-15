from p6_game import Simulator

#global ANALYSIS     # A dictionary mapping states to the previous states that lead to them (I think!)

def _get_neighbors(sim, state):
    for move in sim.get_moves():
        new_state = sim.get_next_state(state, move)
        if new_state:
            yield new_state
            
def _records_for_point(anal_dict, point):
    for record in anal_dict:
        some_point, _ = record
        if point == some_point:
            yield record

def analyze(design):
    sim = Simulator(design)
    specials = design['specials']
    init = sim.get_initial_state()
    frontier = []
    frontier.append(init)
    global ANALYSIS 
    ANALYSIS = {init: (None, None)}    # Reset the ANALYSIS dictionary to scrub out old data.

    while len(frontier) > 0:
        current = frontier.pop(0)
        for neighbor in _get_neighbors(sim, current):
            if neighbor not in ANALYSIS:
                # Record the unvisited state
                frontier.append(neighbor)
                ANALYSIS[neighbor] = current
                
    # Check if goal coordinate (Special 5) is reachable
    reach = False
    for state in ANALYSIS:
        position, _ = state
        if specials.get(position, 0) == 5:
            reach = True
            break  
    if reach:
        print "Special 5 is reachable!"
    else:
        print "Special 5 is NON reachable!"

def inspect((i,j), draw_line):
    src = (1,1)
    path_head_set = _records_for_point(ANALYSIS, (i,j))
    
    for path_head in path_head_set:
        _, hashing_obj = path_head
        while path_head is not (None, None):
            location, _ = path_head
            path_head = ANALYSIS.get(path_head, (None, None))
            next, _ = path_head
            try:
                draw_line(next, location, hashing_obj, hashing_obj)
            except TypeError:
                break
        