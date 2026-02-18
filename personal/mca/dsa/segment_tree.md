# Segment Tree Data Structure

## What is it for?
Segment tree solves **range query problems** — tasks like finding min, max, average, or sum in a dataset that is constantly updating.

**Example**: Stock tracking application finding min/max/sum of stock prices where values are constantly changing.

---

## Structure of Segment Tree

### Basic Properties
- Modified binary tree where data is stored using **"Divide and Conquer"** logic
- Built by splitting original data in half, repeatedly

### Node Types

| Node Type | Represents | Example |
|-----------|-----------|---------|
| **Root** | Entire data range | All stock prices from whole day [0, n-1] |
| **Leaf nodes** | Individual data points | Single stock price [i, i] |
| **Internal nodes** | Union of children's ranges | Combined range [L, R] |

### Tree Structure Example
For array `[5, 8, 6, 3, 2, 7]`:

```
                    [0,5]: 31
                   /          \
            [0,2]: 19          [3,5]: 12
           /        \           /       \
      [0,1]: 13   [2,2]: 6    [3,4]: 5   [5,5]: 7
      /     \                /      \
  [0,0]: 5  [1,1]: 8    [3,3]: 3  [4,4]: 2
```

---

## What Each Node Stores

The **structure stays the same**, but the **value changes** based on your operation:

- **For Min/Max**: Highest or lowest value in that range
- **For Sum**: Total of all numbers in that range

---

## Space Requirements

- **Original data size**: n elements
- **Segment tree size**: 4n space
- **Why**: Extra space ensures balanced binary tree even when data doesn't split evenly (e.g., 7 items)
