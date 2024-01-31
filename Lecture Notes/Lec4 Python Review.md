# Lecture 4: Python Review

* Code setup instructions on CV
* Python Concepts and Methods on CV
    * Everything will need to know + some extra
    * Goes over everything needed for project

## Functions
```python
# Define
def add_and_subtract (x,y):
    w = x-y
    z = x+y
    return z,w

# Use
c, d = add_and_subtract(5,4)
```


* Project is about writing new functions
<br> <br>
* Will use lot of `numpy`. Good for matrices and lin alg
* Import as `np` as convention

```python
A = np.array([1,2,3]) # vect
# A.shape is (3,). A 1D array (1 index)

A = np.array([[1,2,3], [4,5,6], [7,8,9]])
# A.shape is (3,3). A 2D array (2 indeces)
```

Matrix mult, or matrix-vect: `A @ B` <br>
`np.dot(x,y)` <br>
`np.cross(x,y)` <br>

## Sympy
Does stuff with symbols
```python
x = sym.symbols('x')
q = np.array (sym.symbols("q_0:3"))
# creates 1_0, q_1, q_2
```
`RoundSmallCeofficients
SimplifyAndRound
SimplifyAndPrint`
are in utils.py


* **lecture_4_example.py**


TIPS
* Use debugger in VSCode - DO NOT use the autograder to debug
    * Set breakpoints, step, use debug console...
* Print stuff out to debug
* Will be given some test cases. Might try to write your own.