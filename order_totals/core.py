"""Order total logic."""


def calculate_total(items: list[int]) -> int:
    """Return the sum of line item amounts in cents."""
    if not items:
        msg = "Order must contain at least one line item"
        raise ValueError(msg)
    if any(amount < 0 for amount in items):
        msg = "Line item amounts cannot be negative"
        raise ValueError(msg)
    return sum(items)
