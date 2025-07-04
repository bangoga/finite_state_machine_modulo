"""App file used as the runner for any finite state machine. It defines the simulation logic."""
from lib.finite_state_machine import FiniteStateMachine

class App:
    def __init__(self, input_str: str, modulo: int):
        """
        Initialize the app with a binary input and modulo value.

        Args:
            input_str (str): Binary input string to simulate.
            modulo (int): Modulo value for the FSM.
        """
        self._input = input_str
        self._modulo = modulo
        self.finite_state_machine = FiniteStateMachine(input, modulo)
        self.run = [] # used as path taken during the run. FIFO

    def run_simulation(self) -> int:
        """
        Runs the finite state machine simulation based on the input string.

        Returns:
            int: Final state number after processing the input.
        """
        input = self._input

        # if original input has no binary information return -1
        if len(input) == 0:
            return -1
        
        self.run.append(self.finite_state_machine.generated_nodes[0])

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
