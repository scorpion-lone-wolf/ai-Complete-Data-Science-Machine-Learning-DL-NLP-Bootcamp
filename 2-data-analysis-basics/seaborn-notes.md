# Seaborn Notes

## 1. Import
```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style("whitegrid")
```

## 2. Common Dataset Pattern
```python
tips = sns.load_dataset("tips")
tips.head()
```

## 3. Plot Shortcuts

### Scatter plot
```python
sns.scatterplot(x="total_bill", y="tip", data=tips, hue="sex")
plt.show()
```
- Use for relationship between two numeric variables
- `hue` adds category color

### Line plot
```python
sns.lineplot(x="size", y="total_bill", data=tips)
plt.show()
```
- Good for trends over ordered values

### Bar plot
```python
sns.barplot(x="day", y="total_bill", data=tips)
plt.show()
```
- Useful for average values by category
- `estimator="sum"` for total instead of mean

### Box plot
```python
sns.boxplot(x="day", y="total_bill", data=tips)
plt.show()
```
- Helps detect outliers

### Violin plot
```python
sns.violinplot(x="day", y="total_bill", data=tips)
plt.show()
```
- Shows distribution and density

### Histogram
```python
sns.histplot(x="total_bill", data=tips, kde=True, color="purple")
plt.show()
```
- Best for checking distribution
- `kde=True` adds density curve

### Pair plot
```python
sns.pairplot(tips)
plt.show()
```
- Shows scatter plots for all numeric pairs

### Heatmap
```python
corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()
```
- Good for correlation matrix

## 4. Useful Parameters
- `x`, `y` → columns to plot
- `data` → dataframe
- `hue` → color by category
- `color` → fixed color
- `estimator` → summary function for bar plots
- `kde` → show KDE curve
- `annot` → show value labels in heatmap
- `cmap` → color map

## 5. Labels and Titles
```python
plt.xlabel("X-axis name")
plt.ylabel("Y-axis name")
plt.title("Plot Title")
plt.show()
```

## 6. Quick Comparison Guide
| Plot | Best for | Common use |
|------|----------|-----------|
| `scatterplot` | relationship between two numeric values | trend, grouping |
| `lineplot` | change over time/order | trend analysis |
| `barplot` | category-wise summary | average/total by group |
| `boxplot` | spread and outliers | data quality check |
| `violinplot` | distribution by category | compare distributions |
| `histplot` | single variable distribution | frequency check |
| `pairplot` | many variable relationships | exploratory analysis |
| `heatmap` | correlation matrix | feature relations |

## 7. Quick Practice Tips
- Use `sns.set_style(...)` to improve readability
- Always use `plt.show()` after plotting
- Use `hue` to compare groups quickly
- Use `heatmap` after `corr()` for numeric feature insights
