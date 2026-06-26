# N-Queens

Count the number of valid solutions to the n-queens problem: placing `n` queens on an `n × n` chessboard so that no two queens attack each other.

## Usage

```python
from n_queens import count_solutions

count_solutions(8)  # 92
```

## Setup

```bash
uv sync --dev
```

## Commands

| Command | Does |
|---------|------|
| `uv run pytest -v` | Run all tests |
| `./scripts/check.sh` | Lint, format, type-check, and test |

## Tooling

[uv](https://docs.astral.sh/uv/) · [ruff](https://docs.astral.sh/ruff/) · [ty](https://docs.astral.sh/ty/) · [pytest](https://docs.pytest.org/)
