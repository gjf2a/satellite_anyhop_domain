from satellite import *
from pyhop_anytime import *
# To install pyhop_anytime: pip3 install git+https://github.com/gjf2a/pyhop_anytime


# Every pyhop planner should have a method named start which sets up the initial task list from the goals
def start(state, goals):
    ## YOUR CODE HERE ##
    pass

## WRITE ADDITIONAL METHODS HERE ##


def make_satellite_planner():
    planner = Planner()
    planner.declare_operators(calibrate, switch_off, switch_on, take_image, turn_to)
    planner.declare_methods(start) # Include all other methods you write as parameters
    return planner


if __name__ == '__main__':
    anyhop_main(make_satellite_planner())