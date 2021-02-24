# xudoku - Solve sudoku using an 'exact cover' algorithm

This is the sudoku code from @moygit's project 'exact_cover_np'.

The package is maintained by me, @jwg4.

I separated the code for the 'exact cover' algorithm (now available at https://github.com/jwg4/exact_cover) from the sudoku code and created this package.

## How to use the package
```
>>> import xudoku
>>> s = xudoku.Sudoku(9)
>>> s.read("tests/files/insight.csv")
>>> sol = s.solve()
>>> sol._sudo.tolist()
[[1, 3, 2, 9, 7, 4, 5, 6, 8], [5, 6, 7, 2, 1, 8, 3, 4, 9], [8, 4, 9, 5, 6, 3, 2, 7, 1], [6, 9, 4, 3, 2, 5, 1, 8, 7], [2, 5, 1, 4, 8, 7, 9, 3, 6], [3, 7, 8, 6, 9, 1, 4, 2, 5], [7, 8, 3, 1, 5, 2, 6, 9, 4], [4, 1, 6, 8, 3, 9, 7, 5, 2], [9, 2, 5, 7, 4, 6, 8, 1, 3],]
>>> s._hardness
"Hard"
