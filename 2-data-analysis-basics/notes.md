# NumPy Basics

## 1. Import
```python
import numpy as np
```

## 2. Creating Arrays
### Core creation
- `np.array([...])` → create array from list/tuple
- `np.arange(start, stop, step)` → create array with step interval
- `np.reshape(shape)` → change array dimensions

### Special arrays
- `np.ones(shape)` → array of 1s
- `np.zeros(shape)` → array of 0s
- `np.eye(n)` → identity matrix

## 3. Array Properties
- `array.shape` → dimensions of array
- `array.ndim` → number of dimensions
- `array.size` → total number of elements
- `array.dtype` → data type

## 4. Common Operations
### Arithmetic
- `arr + arr`
- `arr - arr`
- `arr * arr`
- `arr / arr`

### Dot product
- `np.dot(a, b)`
- `a @ b`

## 5. Indexing and Slicing
- `arr[row]`
- `arr[row, col]`
- `arr[start:end]`
- `arr[row_start:row_end, col_start:col_end]`

Example pattern:
- `arr[1:-1, 1:-1]` → inner sub-matrix

## 6. Statistics
- `np.mean(arr)`
- `np.median(arr)`
- `np.std(arr)`
- `np.min(arr)`
- `np.max(arr)`
- `np.unique(arr, return_counts=True)`
- `np.argmax(arr)`

## 7. Boolean Indexing
- `arr[arr > value]` → keep values satisfying condition

## 8. Normalization Formula
```python
(X - X.min()) / (X.max() - X.min())
```

## 9. Quick Notes for Practice
- NumPy works best with vectorized operations
- Prefer array operations over Python loops when possible
- Use `shape`, `dtype`, and `ndim` to inspect data quickly

---

