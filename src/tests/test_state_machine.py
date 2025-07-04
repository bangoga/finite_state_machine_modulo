"""Tests the correctness of the state machine and its linkage established"""
from lib.finite_state_machine import FiniteStateMachine
import pytest


# Input for testing creation of state machine is not relevant.
@pytest.mark.parametrize(
    "modulo, expected_nodes_len",
    [
        (5, 5),
        (3, 3),
        (50, 50),
    ]
)

def test_fsm_node_generation(modulo, expected_nodes_len):
    """Testing expected number of generation of nodes"""
    fsm = FiniteStateMachine(modulo=modulo)
    assert len(fsm.generated_nodes) == expected_nodes_len


modulo_5_connections = \
[
"Node(number=0, node_a=s0, node_b=s1)",
"Node(number=1, node_a=s2, node_b=s3)",
"Node(number=2, node_a=s4, node_b=s0)",
"Node(number=3, node_a=s1, node_b=s2)",
"Node(number=4, node_a=s3, node_b=s4)"
]


modulo_3_connections = \
[
"Node(number=0, node_a=s0, node_b=s1)",
"Node(number=1, node_a=s2, node_b=s0)",
"Node(number=2, node_a=s1, node_b=s2)",
]

modulo_1_connections = \
[
"Node(number=0, node_a=s0, node_b=s0)"
]

# Input for testing creation of state machine is not relevant.
@pytest.mark.parametrize(
    "modulo, expected_connections",
    [
        (5, modulo_5_connections),
        (3, modulo_3_connections),
        (1, modulo_1_connections),
    ]
)


def test_fsm_relations(modulo, expected_connections):
    """Test if the right relations are formed by FSM thats created"""
    fsm = FiniteStateMachine(modulo=modulo)

    for i,node in enumerate(fsm.generated_nodes):
        assert f'{node}' == expected_connections[i] # string repr node equal to expectations