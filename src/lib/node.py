"""
Single Node existing for state machine. Each Node represents the state of the machine. 
State machine keeps only the information about the states.
"""
class Node:
    def __init__(self, state, previous = None, next = None, number = 0):
        self.next_node = next
        self.previous_node = previous
        self._state = state
        self.number = number

    @property
    def state(self):
        return self._state
    
    def __repr__(self):
        cls = self.__class__.__name__
        node_a = f"s{self.previous_node.number}" if self.previous_node else None
        node_b = f"s{self.next_node.number}" if self.next_node else None

        return f"Node(number={self.number}, node_a={node_a}, node_b={node_b})"