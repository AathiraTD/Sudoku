# Sudoku

# Sudoku Solver in Python

This Python script provides a concise and efficient implementation of a Sudoku solver using the backtracking algorithm. It is designed to solve any 9x9 Sudoku puzzle, offering a quick and reliable solution.

## Features
- **Efficient Algorithm**: Utilizes a backtracking algorithm to explore possible solutions, reverting back only when it encounters a dead end.
- **Dynamic Board Size Handling**: While optimized for 9x9 puzzles, the solver is capable of handling any square board size that is a perfect square (e.g., 4x4, 16x16) by adjusting the `board` input accordingly.
- **Validity Checking**: Ensures that each number placed is valid according to Sudoku rules, checking against its row, column, and the smaller square it resides in.

## Dependencies
- [NumPy](https://numpy.org/): Used for array manipulation and checking conditions across rows, columns, and sub-squares.

## Usage

1. **Install NumPy**:
    Ensure that NumPy is installed in your environment. If not, you can install it using pip:
    ```sh
    pip install numpy
    ```

2. **Define Your Puzzle**:
    Input your Sudoku puzzle as a 2D NumPy array. Use `0` to represent empty cells.

    Example:
    ```python
    import numpy as np

    board = np.array([
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        ...
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ])
    ```

3. **Solve the Puzzle**:
    Initialize the `Sudoku` class with your board, and call the `solve()` method. The solved board will be printed to the console.

    ```python
    game = Sudoku(board)
    game.solve()
    print(game.board)
    ```

## Example

The repository includes an example puzzle to demonstrate the usage. Simply run the `sudoku.py` script to solve it.

## Contributing

Contributions to improve the Sudoku solver are welcome. Please ensure to follow best practices and guidelines when submitting pull requests.

## License

This project is open-sourced under the MIT License. LICENSE file to be uploaded.

## Acknowledgments

- This project is developed as part of a learning exercise in understanding algorithms and their implementation in Python.
- Special thanks to the Python and NumPy communities for providing extensive documentation and resources.

