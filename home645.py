class MatrixIterator:
    def __init__(self, data):
        self._items = [x for row in data for x in row]
        self._i = 0

    def __iter__(self): return self

    def __next__(self):
        if self._i >= len(self._items): raise StopIteration
        v = self._items[self._i]; self._i += 1; return v


class Matrix:
    def __init__(self, data): self._data = data
    def __iter__(self): return MatrixIterator(self._data)


m = Matrix([[3, 1, 4], [1, 5, 9], [2, 6, 5]])

elements = list(m)
print(f"Найбільший: {max(elements)}")
print(f"Найменший: {min(elements)}")
print(f"Сума: {sum(elements)}")
print(f"Середнє: {sum(elements)/len(elements):.2f}")