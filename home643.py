class CustomSetIterator:
    def __init__(self, data):
        self._items = list(data)
        self._i = 0

    def __iter__(self): return self

    def __next__(self):
        if self._i >= len(self._items): raise StopIteration
        v = self._items[self._i]; self._i += 1; return v


class CustomSet:
    def __init__(self, data=None):
        self._data = set(data) if data else set()

    def __iter__(self): return CustomSetIterator(self._data)
    def __len__(self): return len(self._data)
    def __contains__(self, x): return x in self._data

    def _wrap(self, o): return o if isinstance(o, CustomSet) else CustomSet([o])

    def __add__(self, o): return CustomSet(self._data | self._wrap(o)._data)
    def __mul__(self, o): return CustomSet(self._data & self._wrap(o)._data)
    def __sub__(self, o): return CustomSet(self._data - self._wrap(o)._data)
    def __truediv__(self, o): return CustomSet(self._data ^ self._wrap(o)._data)


import os, re

folder = "."
files = [f for f in os.listdir(folder) if f.endswith(".txt")]

sets = []
for f in files:
    with open(f, encoding="cp1251") as file:
        words = re.findall(r'\b\w+\b', file.read().lower())
    sets.append(CustomSet(words))

common = sets[0]
for s in sets[1:]: common = common * s

union = sets[0]
for s in sets[1:]: union = union + s

only_first = sets[0]
for s in sets[1:]: only_first = only_first - s

print("Спільні слова:")
for w in common: print(w)
print(f"Кількість: {len(common)}\n")

print("Всі слова:")
for w in union: print(w)
print(f"Кількість: {len(union)}\n")

print("Тільки в першому файлі:")
for w in only_first: print(w)
print(f"Кількість: {len(only_first)}")