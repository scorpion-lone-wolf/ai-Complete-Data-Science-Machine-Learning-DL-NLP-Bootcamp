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

# Pandas Basics

## 1. Import
```python
import pandas as pd
from IPython.display import display
```

## 2. Core Objects
- `pd.Series(...)` → one-dimensional labeled data
- `pd.DataFrame(...)` → two-dimensional table-like data

## 3. Creating DataFrames
- `pd.DataFrame(dict)` → create from dictionary
- `pd.DataFrame(..., index=[...])` → set row labels

## 4. Reading Data
- `pd.read_csv("file.csv")` → read CSV file

## 5. Viewing Data
- `df.head(n)`
- `df.describe()`
- `df.columns`

## 6. Selecting Data
- `df["column_name"]`
- `df.loc[row_label, col_label]`
- `df.iloc[row_index, col_index]`

## 7. DataFrame Editing
- `df["new_col"] = ...`
- `df.drop(columns=..., inplace=True)`
- `df.rename(columns={...}, inplace=True)`

## 8. Missing Values
- `df.isnull()`
- `df.isnull().sum()`
- `df["col"].isnull().sum()`
- `df["col"].fillna(df["col"].mean())`
- `df.dropna(inplace=True)`

## 9. Apply Functions
- `df["col"].apply(lambda x: ...)`

## 10. Grouping and Aggregation
- `df.groupby("col")["value_col"].sum()`
- `df.groupby(["col1", "col2"])["value_col"].sum()`

## 11. Merging DataFrames
- `pd.merge(df1, df2, on="key", how="inner")`
- `how="left"`, `how="right"`, `how="outer"`

## 12. Quick Practice Notes
- Use `head()` to inspect data quickly
- Use `describe()` for summary statistics
- Use `loc`/`iloc` for precise access
- Use `groupby()` for grouped summaries

---

# Pandas Data Manipulation (Cheat Sheet)

## 1. Read and Inspect
```python
df = pd.read_csv("data.csv")
display(df.head(5))
display(df.describe())
```

## 2. Check Missing Values
- `df.isnull().any()`
- `df.isnull().sum()`

## 3. Fill Missing Values
```python
df["Sales"] = df["Sales"].fillna(df["Sales"].mean())
```

## 4. Rename Columns
```python
df.rename(columns={"Sales": "TotalSales"}, inplace=True)
```

## 5. Apply Logic to a Column
```python
df["Value"] = df["Value"].apply(lambda x: x * 2)
```

## 6. Group by Category
```python
df.groupby("Product")["Value"].sum()
```

## 7. Merge Tables
```python
pd.merge(df1, df2, on="col1", how="inner")
```

## 8. Useful Methods to Remember
- `head()`
- `describe()`
- `isnull()`
- `fillna()`
- `rename()`
- `apply()`
- `groupby()`
- `merge()`

---

