# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"

    from util import Stack
    stack = Stack()
    actions=[]
    visited=[]
    start_pos=problem.getStartState()
    stack.push( [start_pos, actions] )
    while not stack.isEmpty():
        top_item = stack.pop()
        position_list = top_item[0]
        actions_list = top_item[1]

        if problem.isGoalState(position_list):
            return actions_list
        if position_list not in visited:
            visited.append(position_list)
            successor_nodes=problem.getSuccessors(position_list)
            for nodes in successor_nodes:
                succ_node=nodes[0]
                succ_action=nodes[1]
                if succ_node not in visited:
                    nxt_action=actions_list+[succ_action]
                    stack.push([succ_node,nxt_action])
    '''startnode = problem.getStartState()
        #successorList = problem.getSuccessors(startnode)
    stack = util.Stack()
    visitedNode = []
    # tempList = []
    stack.push([startnode, []])
    while not stack.isEmpty():
        #successor = stack.pop()
        succ_node, succ_action = stack.pop()
        if problem.isGoalState(succ_node):
            return succ_action
        if succ_node not in visitedNode:
            visitedNode.append(succ_node)
            tempList=problem.getSuccessors(succ_node)

            for node, act, cost in tempList:
                if node not in visitedNode:
                    stack.push([node, succ_action+[act]])'''


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    from util import Queue
    queue = Queue()
    actions=[]
    visited=[]
    start_pos=problem.getStartState()
    queue.push( (start_pos, actions) )
    while not queue.isEmpty():
        top_item = queue.pop()
        position_list = top_item[0]
        actions_list = top_item[1]

        if problem.isGoalState(position_list):
            return actions_list
        if position_list not in visited:
            visited.append(position_list)
            successor_nodes=problem.getSuccessors(position_list)
            for nodes in successor_nodes:
                succ_node=nodes[0]
                succ_action=nodes[1]
                if succ_node not in visited:
                    nxt_action=actions_list+[succ_action]
                    queue.push((succ_node,nxt_action))


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    p_queue = PriorityQueue()
    actions=[]
    visited=[]
    start_pos=problem.getStartState()
    p_queue.push( (start_pos, actions),0 )
    while not p_queue.isEmpty():
        top_item = p_queue.pop()
        position_list = top_item[0]
        actions_list = top_item[1]

        if problem.isGoalState(position_list):
            return actions_list
        if position_list not in visited:
            visited.append(position_list)
            successor_nodes=problem.getSuccessors(position_list)
            for nodes in successor_nodes:
                succ_node=nodes[0]
                succ_action=nodes[1]
                if succ_node not in visited:
                    nxt_action=actions_list+[succ_action]
                    cost_of_action = problem.getCostOfActions(nxt_action)
                    p_queue.push((succ_node,nxt_action),cost_of_action)


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    from util import PriorityQueue
    p_queue = PriorityQueue()
    actions=[]
    visited=[]
    start_pos=problem.getStartState()
    p_queue.push( (start_pos, actions),0 )
    while not p_queue.isEmpty():
        top_item = p_queue.pop()
        position_list = top_item[0]
        actions_list = top_item[1]

        if problem.isGoalState(position_list):
            return actions_list
        if position_list not in visited:
            visited.append(position_list)
            successor_nodes=problem.getSuccessors(position_list)
            for nodes in successor_nodes:
                succ_node=nodes[0]
                succ_action=nodes[1]
                if succ_node not in visited:
                    nxt_action=actions_list+[succ_action]
                    cost_of_action = problem.getCostOfActions(nxt_action)
                    heuristic_cost=heuristic(succ_node,problem)
                    total_cost=cost_of_action+heuristic_cost
                    p_queue.push((succ_node,nxt_action),total_cost)


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
