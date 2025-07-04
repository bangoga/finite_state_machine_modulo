"""
Class used to create Nodes and form a Finite State Machine through set interactions.
"""
from lib.node import Node
class FiniteStateMachine:

    def __init__(self, input:str = "1101", modulo:int = 3):
        """
        Initialize the FSM with a binary string input and modulo base default modulo is 3.

        Args:
            input (str): Binary string representing a number. Default is "1101".
            modulo (int): Modulo base. Default is 3.
        """
        if modulo < 1:
            raise ValueError("Modulo needs to be > 0")
        
        self._input = input
        self.generated_nodes = []
        state = 0

        # generate nodes with alternating states, node_number is the remainder representation of the node.
        for node_number in range(modulo):
            node = Node(state=state, number = node_number)
            self.generated_nodes.append(node)
            state = 1 - state # alternate

        
        # set transition with general formula (Sn * 2 + Xn) % N where N is the modulo
        for node_number in range(modulo):
            # if first node, previous node is a loop back
            if node_number == 0:
                self.generated_nodes[node_number].previous_node = self.generated_nodes[node_number]
                self.generated_nodes[node_number].next_node = self.generated_nodes[(node_number+1)% modulo]

            else:
                # previous isn't previous, its just 0 transition
                # next is 1 transition
                remainder = node_number
                transition_a = ((2*remainder) + 1) % modulo
                transition_b = ((2*remainder) + 0) % modulo

                self.generated_nodes[node_number].next_node = self.generated_nodes[transition_a]
                self.generated_nodes[node_number].previous_node = self.generated_nodes[transition_b]
