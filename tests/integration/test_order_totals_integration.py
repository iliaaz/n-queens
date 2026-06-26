"""Integration tests for order total workflow."""

import pytest

from order_totals import calculate_total


@pytest.mark.integration
def test_calculates_total_from_collected_line_items() -> None:
    """Simulates collecting items before calculating total."""
    collected: list[int] = []
    for amount in (250, 150, 100):
        collected.append(amount)

    assert calculate_total(collected) == 500
