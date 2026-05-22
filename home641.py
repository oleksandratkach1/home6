import re

class CustomListIterator:
    def __init__(self, data):
        self._items = sorted([x for x in data if x % 2 != 0]) + sorted([x for x in data if x % 2 == 0], reverse=True)
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._items):
            raise StopIteration
        value = self._items[self._index]
        self._index += 1
        return value


class CustomList:
    def __init__(self, data=None):
        self._data = [int(x) for x in data] if data else []

    def __getitem__(self, i): return self._data[i]
    def __setitem__(self, i, v): self._data[i] = int(v)
    def __len__(self): return len(self._data)
    def __contains__(self, item): return item in self._data
    def __iter__(self): return CustomListIterator(self._data)
    def __repr__(self): return f"CustomList({self._data})"

    def __iadd__(self, other):
        self._data.extend(other._data if isinstance(other, CustomList) else [int(other)])
        return self

    def __isub__(self, other):
        for item in (other._data if isinstance(other, CustomList) else [int(other)]):
            if item in self._data: self._data.remove(item)
        return self

    def __imul__(self, times):
        self._data *= times
        return self


def main():
    with open("numbers.txt", "r", encoding="utf-8") as f:
        text = f.read()

    cl = CustomList([int(m) for m in re.findall(r'-?\d+', text)])

    print("Вивід через ітератор:")
    for num in cl:
        print(num, end=" ")
    print()

    print(f"Кількість: {len(cl)}, Сума: {sum(cl._data)}")

    check = CustomList([1, 3, 1984, 7777])
    print(f"Є хоч одне з {{1,3,1984,7777}}: {any(x in cl for x in check)}")
    print(f"Ненульових чисел: {sum(1 for x in cl._data if x != 0)}")


if __name__ == "__main__":
    main()