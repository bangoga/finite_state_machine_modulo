"""Tests the correctness of the state machine and its linkage established"""
from lib.finite_state_machine import FiniteStateMachine
import pytest


# Input for testing creation of state machine is not relevant.
@pytest.mark.parametrize(
    "input, modulo, expected_nodes_len",
    [
        ("10101", 5, 5),
        ("10101", 3, 3),
        ("10101", 50, 50),
    ]
)

def test_fsm_creation(input, modulo, expected_nodes_len):
    """Testing expected behaviour from creation of a finite state machine"""
    fsm = FiniteStateMachine(input=input, modulo=modulo)
    assert len(fsm.generated_nodes) == expected_nodes_len
