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

## Rendering

When this runs, it will write-out an HTML file with an SVG written-out for the grid. This is definitely not efficient, but it's an extremely simple way to write-out a visual representation of the game's "Universe" at each tick-state.

The committed version here is set for a `100x100` grid with 50 ticks. Each written-out (read: generated) "frame" is around `700kB`, which is quite a lot for what should be `10kB` of data. Part of this is because for visual effect, each Cell is set to be rendered as a `5px`-by-`5px` square, so there's a logical factor of 25, but really the filesize is because of all the `8`-bit characters used to define an SVG `<rect />` tag per Cell, along with the other required minimal HTML.

Any SVG compatible web-browser should be able to render the generated frames. Unfortunately, automated animated is not (yet) supported.

This was a simple approach to write-out the universe in a way that doesn't require any third-party libraries or utilities -- assuming that the ubiquity of an SVG-compatible Web-Browser isn't far-fetched.

## References

- https://conwaylife.com/wiki/Conway%27s_Game_of_Life
- https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
