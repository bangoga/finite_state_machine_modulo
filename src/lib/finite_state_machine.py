"""
Machine used to do simulation for modulo
"""
from node import Node
class FiniteStateMachine:

    def __init__(self, input:str = "1101", modulo:int = 3):
        """
        Initialize the FSM with a binary string input and modulo base default modulo is 3.

        Args:
            input (str): Binary string representing a number. Default is "1101".
            modulo (int): Modulo base. Default is 3.
        """
        self._input = input
        self._generated_nodes = []
        self.run = []
        state = 0

        for node_number in range(modulo):
            node = Node(state=state, number = node_number)
            self._generated_nodes.append(node)
            state = 1 - state # alternate

        
        # set transition with general formula (Sn * 2 + Xn) % N where N is the modulo
        # S2 * 2  + 0 


        for node_number in range(modulo):
            # if first node, previous node is a loop back
            if node_number == 0:
                self._generated_nodes[node_number].previous_node = self._generated_nodes[node_number]
                self._generated_nodes[node_number].next_node = self._generated_nodes[(node_number+1)% modulo]

            else:
                # previous isn't previous, its just 0 transition
                # next is 1 transition
                remainder = node_number
                transition_a = ((2*remainder) + 1) % modulo
                transition_b = ((2*remainder) + 0) % modulo

                self._generated_nodes[node_number].next_node = self._generated_nodes[transition_a]
                self._generated_nodes[node_number].previous_node = self._generated_nodes[transition_b]


    # Transitions are good, fix the others 
    def run_simulation(self):
        input = self._input
        self.run.append(self._generated_nodes[0])
        while input :
            input, msb = input[1:], input[0]
            node = self.run.pop()

            if msb == "1":
                self.run.append(node.next_node)

            else:
                self.run.append(node.previous_node)
            
            print(f"({node.number}) --{msb}-->({self.run[0].number}) ")
            
        final_node = self.run.pop()
        print(final_node.number)
        return final_node.number

if __name__ == "__main__":
    fsm = FiniteStateMachine(input="101101011001", modulo = 9)
    fsm.run_simulation()
