from p6_game import Simulator

ANALYSIS = {}   # A dictionary mapping states to the previous states that lead to them (I think!)

def analyze(design):
    sim = Simulator(design)
    init = sim.get_initial_state()
    frontier = []
    frontier.append(init)
    ANALYSIS[init] = None

    while len(frontier) > 0:
        current = frontier.pop(0)
        for move in sim.get_moves():
            if move not in ANALYSIS:
                # Record the state resulting from applying our next hypothetical move to our current state
                frontier.append(sim.get_next_state(current, move))
                ANALYSIS[move] = current
                print current

def inspect((i,j), draw_line):
    pass
    