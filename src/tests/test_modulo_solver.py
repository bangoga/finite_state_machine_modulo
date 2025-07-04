"""Used to test the app that runs and solves modulo problems"""

from app import App
import pytest


# Input for testing creation of state machine is not relevant.
@pytest.mark.parametrize(
    "input, modulo, expected_result",
    [
        ("110", 3, 0),
        ("1010", 3, 1),
        ("101101011001", 9, 7),
        ("111000111",43, 25),
    ]
)

def test_fsm(input, modulo, expected_result):
    """Testing results produced by fsm"""
    app = App(input_str=input, modulo=modulo)
    result = app.run_simulation()
    assert result == expected_result

@pytest.mark.parametrize(
    "input, modulo, edge_case_expected_result",
    [
        ("", 3, -1),
        ("000000", 5, 0),
        ("111111", 5, 3),
        ("111111", 9, 0),
        ("000000", 9, 0),
        ("1",10, 1),
    ]
)

def test_fsm_edge_cases(input, modulo, edge_case_expected_result):
    """Testing separate edge cases."""
    app = App(input_str=input, modulo=modulo)
    result = app.run_simulation()
    assert result == edge_case_expected_result

def test_fsm_bad_modulo_case():
    """Test for modulo being unexpected"""
    with pytest.raises(ValueError, match="Modulo needs to be > 0"):
        app = App(input_str="10101", modulo=0)
