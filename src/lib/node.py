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
        return f"s{self.number} -- (1) -->s{self.next_node.number}\ns{self.number} -- (0) -->s{self.previous_node.number}"
