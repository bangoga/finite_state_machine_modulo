"""
Single Node existing for state machine. Each Node represents the state of the machine. 
State machine keeps only the information about the states.
"""
class Node:
    def __init__(self, node_a = None, node_b = None, number = 0):
        """
        node_a: transitioning node from 0 bit
        node_b: transitioning node from 1 bit
        """
        self.node_a = node_a
        self.node_b = node_b
        self.number = number
    
    def __repr__(self):
        """representing node_a transition on 0 and node_b transition on 1"""
        cls = self.__class__.__name__
        node_a = f"s{self.node_a.number}" if self.node_a else None
        node_b = f"s{self.node_b.number}" if self.node_b else None

        return f"Node(number={self.number}, node_a={node_a}, node_b={node_b})"