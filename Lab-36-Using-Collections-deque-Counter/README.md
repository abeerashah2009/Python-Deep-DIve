# Lab 36: Using Collections (deque, Counter)

## Objective

Learn how to use Python's built-in `collections` module, focusing on `deque` and `Counter`.

Understand how these specialized data structures make programs more efficient, readable, and easier to maintain.

## Tools Used

- Ubuntu 24.04 LTS
- Python 3.12.3
- Python Standard Library
- `collections` module

## Concepts Learned

### 1. Introduction to the Collections Module

The `collections` module provides specialized container data types as alternatives to common Python data structures such as lists, dictionaries, and tuples.

Some available data structures include:

- `deque`
- `Counter`
- `OrderedDict`
- `defaultdict`
- `ChainMap`
- `namedtuple`

Import and inspect the module:

```python
import collections
print(collections.__all__)
```

### 2. Understanding deque

`deque` means double-ended queue.

It allows adding and removing elements from both the beginning and the end.

Import deque:

```python
from collections import deque
```

#### Important deque Methods

| Method | Purpose |
|---|---|
| `append()` | Adds an item to the right |
| `appendleft()` | Adds an item to the left |
| `pop()` | Removes an item from the right |
| `popleft()` | Removes an item from the left |

Example:

```python
from collections import deque

d = deque()
d.append('task1')
d.append('task2')

last_task = d.pop()
print("Popped from the right:", last_task)

d.appendleft('task0')

first_task = d.popleft()
print("Popped from the left:", first_task)
print("Remaining deque:", d)
```

### 3. Using deque with maxlen

The `maxlen` parameter sets the maximum number of elements in a deque.

When the deque is full, adding another item automatically removes the oldest item from the opposite end.

Example:

```python
recent = deque(maxlen=3)

for i in range(5):
    recent.append(i)

print("Last 3 items:", recent)
```

Expected output:

```text
Last 3 items: deque([2, 3, 4], maxlen=3)
```

#### Advantages of deque

- Efficient insertion and removal at both ends.
- Append and pop operations at either end take O(1) time.
- Useful for queues, browser history, and recent-item tracking.
- `maxlen` helps maintain a fixed-size collection.

### 4. Understanding Counter

`Counter` is a specialized dictionary used to count occurrences of hashable objects.

Import Counter:

```python
from collections import Counter
```

Example:

```python
words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']

word_count = Counter(words)

print("Word Count:", word_count)
```

Expected output:

```text
Counter({'apple': 3, 'orange': 2, 'banana': 1})
```

### 5. Using most_common()

The `most_common()` method returns the most frequently occurring elements and their counts.

Example:

```python
most_common = word_count.most_common(2)
print("Most Common Words:", most_common)
```

Expected output:

```text
[('apple', 3), ('orange', 2)]
```

### 6. Using update()

The `update()` method adds new occurrences to existing counts.

Example:

```python
word_count.update(['banana', 'banana'])

print("Banana after update:", word_count['banana'])
```

Expected output:

```text
Banana after update: 3
```

#### Advantages of Counter

- Makes counting simple and readable.
- Avoids writing manual dictionary counting loops.
- Provides `most_common()` to find frequently occurring items.
- Provides `update()` to increase existing counts.

## Practical Tasks Completed

1. Checked Python version.
2. Imported and inspected the collections module.
3. Imported `deque` and `Counter`.
4. Created a deque.
5. Practised adding and removing elements from both ends.
6. Used `deque(maxlen=3)`.
7. Created a Counter for word frequency.
8. Used `most_common(2)`.
9. Updated existing counts using `update()`.
10. Verified Python syntax and program output.

## How to Run the Script

```bash
python3 collections_demo.py
```

## Verification Results

- Python version: 3.12.3
- Collections module: Available
- deque import: PASSED
- Counter import: PASSED
- Required references: 9
- Python syntax check: PASSED
- Final execution: PASSED
- Expected output: Matched

See `evidence/verification.txt` for the verification output.

## deque vs Counter

| Feature | deque | Counter |
|---|---|---|
| Main purpose | Manage elements at both ends | Count occurrences |
| Based on | Double-ended queue | Dictionary |
| Useful methods | append, pop, popleft | most_common, update |
| Common use | Queue management | Word frequency |

## Conclusion

Successfully completed Lab 36 using Python's built-in collections module.

Practised `deque` for efficient operations at both ends and `Counter` for counting repeated elements. These specialized data structures improve code clarity and are useful in real-world Python applications.

**LMS Result: 100 / 100 — Passed**
