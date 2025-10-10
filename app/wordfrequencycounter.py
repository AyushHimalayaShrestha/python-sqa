# word frequency counter
from collections import Counter

text = """Python is powerful and fast. Python is easy to learn.
Python is everywhere!"""

words = text.lower().split()
count = Counter(words)

for word, freq in count.items():
    print(f"{word}: {freq}")
