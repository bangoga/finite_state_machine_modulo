"""
Class used to create Nodes and form a Finite State Machine through set interactions.
"""
from lib.node import Node
class FiniteStateMachine:

    def __init__(self, modulo:int = 3):
        """
        Initialize the FSM with a modulo base default modulo is 3.

        Args:
            modulo (int): Modulo base. Default is 3.
        """
        if modulo < 1:
            raise ValueError("Modulo needs to be > 0")
        
        self.generated_nodes = []

        # generate nodes with node_number is the remainder representation of the node.
        for node_number in range(modulo):
            node = Node(number = node_number)
            self.generated_nodes.append(node)

        
        # set transition with general formula (Sn * 2 + Xn) % N where N is the modulo
        for node_number in range(modulo):
            # if first node. Transition of 0 is a loop back
            if node_number == 0:
                self.generated_nodes[node_number].node_a = self.generated_nodes[node_number]
                self.generated_nodes[node_number].node_b = self.generated_nodes[(node_number+1)% modulo]

            else:
                # set transitions. transition a is transition on 0, transition b is transition on 1 similar to node_a, node_b
                remainder = node_number

                transition_a = ((2*remainder) + 0) % modulo
                transition_b = ((2*remainder) + 1) % modulo
                
                self.generated_nodes[node_number].node_a = self.generated_nodes[transition_a]
                self.generated_nodes[node_number].node_b = self.generated_nodes[transition_b]
