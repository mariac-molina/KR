from search import Problem
from search import Node
from search import breadth_first_tree_search
from search import depth_limited_search
from search import iterative_deepening_search

import time

class MissionariesCannibals(Problem):
    """ The problem of taking 3 cannibals (C) and 3 missionaries (M) across a river.
    A state is represented as a tuple of length 3,
    where element at index 0 represents number of missionaries on the wrong side
    index 1 represents number of cannibals on the wrong side
    index 2 represents number of boat on the wrong side
    """

    def __init__(self, initial=[3,3,1], goal=[0,0,0]):
        """ Define goal state and initialize a problem """
        self.initial = initial
        self.goal = goal
        Problem.__init__(self, initial, goal)

    def hasMoreCannibals(self, state):
        '''
        Returns True if :
        3 first lines : if there are more cannibals on the wrong side
        3 last lines : if there are more cannibals at destination
        '''
        return ((state[0] == 3 and state[1] == 2) or
               (state[0] == 3 and state[1] == 1) or
               (state[0] == 2 and state[1] == 1) or
               (state[0] == 0 and state[1] == 1) or
               (state[0] == 0 and state[1] == 2) or
               (state[0] == 1 and state[1] == 2))

    def isValidState(self, state):
        """
        Given a state, returns True if state if valid, False if it is invalid
        """
        test_state = state
        if test_state[2] < 0 or test_state[2] > 1:
        # if there is less than one boat or more than one boat
            return False
        elif test_state[0] < 0 or test_state[1] < 0:
        # if there is a negative number of M or C
            return False
        elif test_state[0] > 3 or test_state[1] > 3:
        # if there are more M or C than we started with
            return False
        elif self.hasMoreCannibals(test_state):
        # if there are more C on either side of river
            return False

        return True

    def isValidAction(self, state, action):
        """
        Returns True if a given action applied to a given state results in
        a valid new state
        """

        test_state = state

        if self.isValidState(self.result(test_state, action)):
            return True

        return False

    def actions(self, state):
        """ Return the actions that can be executed in the given state.
        The result would be a list, since there are only 5 possible actions
        in any given state of the environment """

        all_actions = [ [1,1,1], [2,0,1], [0,2,1], [1,0,1], [0,1,1] ]
        possible_actions = []

        for act in all_actions:
            valid = self.isValidAction(state, act)
            if valid == True:
                possible_actions.append(act)

        return possible_actions

    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        if state[2] == 0:
        # if the boat is on the opposite side (destination)
            return [ state[i] + action[i] for i in range(3)]
        elif state[2] == 1:
        # if boat on near side of the river (initial side)
            return [ state[i] - action[i] for i in range(3)]

    def goal_test(self, state):
        """ Given a state, return True if state is a goal state or False, otherwise """
        return state == self.goal

def main():
    prob = MissionariesCannibals()

    start_time_breadth = time.time()
    res_breadth  = breadth_first_tree_search(prob)
    total_time_breadth = time.time() - start_time_breadth
    print("Execution time breadth first search : ", total_time_breadth)
    print("b result : ", res_breadth.path())

    start_time_iter = time.time()
    res_iter  = iterative_deepening_search(prob)
    total_time_iter = time.time() - start_time_iter
    print("Execution time iterative deepening search : ", total_time_iter)
    print("i result : ", res_breadth.path())

if __name__ == "__main__":
    main()
