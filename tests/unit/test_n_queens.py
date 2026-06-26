"""Unit tests for n-queens solution counting."""

from typing import Any

import pytest

from n_queens import count_solutions


@pytest.mark.unit
def test_single_queen_has_one_solution() -> None:
    assert count_solutions(1) == 1


@pytest.mark.unit
def test_four_queens_has_two_solutions() -> None:
    assert count_solutions(4) == 2


@pytest.mark.unit
def test_eight_queens_has_ninety_two_solutions() -> None:
    assert count_solutions(8) == 92


@pytest.mark.unit
def test_nine_queens_has_three_hundred_fifty_two_solutions() -> None:
    assert count_solutions(9) == 352


@pytest.mark.unit
def test_twelve_queens_has_fourteen_thousand_two_hundred_solutions() -> None:
    assert count_solutions(12) == 14200


@pytest.mark.unit
def test_five_queens_has_ten_solutions() -> None:
    assert count_solutions(5) == 10


@pytest.mark.unit
def test_two_queens_has_no_solutions() -> None:
    assert count_solutions(2) == 0


@pytest.mark.unit
def test_three_queens_has_no_solutions() -> None:
    assert count_solutions(3) == 0


@pytest.mark.unit
def test_zero_is_invalid_input() -> None:
    with pytest.raises(ValueError, match="invalid"):
        count_solutions(0)


@pytest.mark.unit
def test_negative_input_is_invalid() -> None:
    with pytest.raises(ValueError, match="invalid"):
        count_solutions(-1)


@pytest.mark.unit
def test_non_integer_input_is_invalid() -> None:
    invalid_input: Any = 4.5
    with pytest.raises(TypeError):
        count_solutions(invalid_input)
