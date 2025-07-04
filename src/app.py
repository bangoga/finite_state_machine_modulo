"""App file used as the runner for any finite state machine"""
from lib.finite_state_machine import FiniteStateMachine

class App:
    def __init__(self, input , modulo):
        self._input = input
        self._modulo = modulo
        self.run = []
        self.finite_state_machine = FiniteStateMachine(input, modulo)
        

    def run_simulation(self):
        """Used to run simulations of a finite state machine"""
        input = self._input
        
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

if __name__ == "__main__":
    app = App(input="101101011001", modulo = 9)
    app.run_simulation()