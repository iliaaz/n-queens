# Design spec

> Practice run: order line total calculator

## Summary

Add a function that calculates the total of an order from line item amounts (in cents).

## Context

- Input is a list of integer amounts in cents
- No persistence or API in scope

## Must haves

- [ ] Sum all line item amounts
- [ ] Reject empty orders
- [ ] Reject negative line items

## Nice to haves

- [ ] _None for this practice run_

## Won't do

- Tax, shipping, currency formatting
- HTTP API or database

## Scenarios

### Scenario: Valid order total

- **GIVEN** line items `[500, 1200, 300]`
- **WHEN** the total is calculated
- **THEN** the result is `2000`

### Scenario: Single line item

- **GIVEN** line items `[750]`
- **WHEN** the total is calculated
- **THEN** the result is `750`

### Scenario: Empty order rejected

- **GIVEN** an empty list of line items
- **WHEN** the total is calculated
- **THEN** a `ValueError` is raised

### Scenario: Negative line item rejected

- **GIVEN** line items `[100, -50]`
- **WHEN** the total is calculated
- **THEN** a `ValueError` is raised

## Acceptance criteria

- [ ] All must haves are implemented
- [ ] Every scenario has a unit test (positive and negative cases covered)
- [ ] Critical flows have integration tests
- [ ] Won't-do items were not built
- [ ] All tests pass
- [ ] Lint, format, and type checks pass

## Open questions

- None

## Implementation notes

- Public API: `calculate_total(items: list[int]) -> int`
