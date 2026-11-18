from collections import deque

# --- deque ---
d = deque()
d.append('task1')
d.append('task2')

last_task = d.pop()
print("Popped from the right:", last_task)

d.appendleft('task0')

first_task = d.popleft()
print("Popped from the left:", first_task)
print("Remaining deque:", d)

# A deque with maxlen drops the oldest item when full
recent = deque(maxlen=3)
for i in range(5):
    recent.append(i)
print("Last 3 items:", recent)

# --- Counter ---
from collections import Counter

words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
word_count = Counter(words)
print("Word Count:", word_count)

most_common = word_count.most_common(2)
print("Most Common Words:", most_common)

# update() adds to existing counts
word_count.update(['banana', 'banana'])
print("Banana after update:", word_count['banana'])
