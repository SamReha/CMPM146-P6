from p6_game import Simulator

global ANALYSIS     # A dictionary mapping states to the previous states that lead to them (I think!)

def _get_neighbors(sim, state):
    for move in sim.get_moves():
        new_state = sim.get_next_state(state, move)
        if new_state:
            yield new_state

def analyze(design):
    sim = Simulator(design)
    specials = design['specials']
    init = sim.get_initial_state()
    frontier = []
    frontier.append(init)
    ANALYSIS = {}    # Reset the ANALYSIS dictionary to scrub out old data.
    ANALYSIS[init] = None

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
  dst = (i,j)
  src = (1,1)
  draw_line(src,dst)