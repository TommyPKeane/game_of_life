# Cellular Automata (Conway's Game of Life)

OOP implementation of Cellular Automata in a 2D grid-based universe using Python and the ruleset of Conway's "Game of Life".

## Implementation

Python 3.8.x, with no external dependencies.

## How to Run

Using Python 3.8.x -- install with [pyenv](https://github.com/pyenv/pyenv) if you are on a Unix-based System (macOS or Linux variant) -- checkout this repository and navigate to the top-level directory (same path as this `README` file), and run:

```
python -m life_squares
```

This will run the "Game of Life" for a 2D Array Universe of square Cells, using a Moore neighbourhood of radius 1, based on the initialization configured in the `__main__.py` module within the `life_squares` package.

## References

- https://conwaylife.com/wiki/Conway%27s_Game_of_Life
- https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
