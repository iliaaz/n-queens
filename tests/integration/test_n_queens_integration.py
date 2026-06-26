"""Integration tests for n-queens solution counting."""

import pytest

from n_queens import count_solutions


@pytest.mark.integration
def test_known_solution_counts_for_small_board_sizes() -> None:
    """Verify exhaustive counts across board sizes with known results."""
    expected = {1: 1, 2: 0, 3: 0, 4: 2, 5: 10, 6: 4, 7: 40, 8: 92}

    for n, solutions in expected.items():
        assert count_solutions(n) == solutions
