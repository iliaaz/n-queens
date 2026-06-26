"""Unit tests for order total calculation."""

import pytest

from order_totals import calculate_total


@pytest.mark.unit
def test_calculates_total_for_multiple_line_items() -> None:
    assert calculate_total([500, 1200, 300]) == 2000


@pytest.mark.unit
def test_calculates_total_for_single_line_item() -> None:
    assert calculate_total([750]) == 750


@pytest.mark.unit
def test_rejects_empty_order() -> None:
    with pytest.raises(ValueError, match="at least one line item"):
        calculate_total([])


@pytest.mark.unit
def test_rejects_negative_line_item() -> None:
    with pytest.raises(ValueError, match="cannot be negative"):
        calculate_total([100, -50])
