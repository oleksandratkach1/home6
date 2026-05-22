class MutableStringIterator:
    def __init__(self, data):
        self._items = list(data)
        self._i = 0

    def __iter__(self): return self

    def __next__(self):
        if self._i >= len(self._items): raise StopIteration
        v = self._items[self._i]; self._i += 1; return v


class MutableString:
    def __init__(self, s=""): self._data = list(s)
    def __len__(self): return len(self._data)
    def __getitem__(self, i): return self._data[i]
    def __setitem__(self, i, v): self._data[i] = v
    def __contains__(self, c): return c in self._data
    def __add__(self, o): return MutableString("".join(self._data + list(str(o))))
    def __mul__(self, n): return MutableString("".join(self._data * n))
    def __iter__(self): return MutableStringIterator(self._data)
    def __str__(self): return "".join(self._data)


replacements = {'a':'а','e':'е','i':'і','o':'о','p':'р','c':'с','x':'х','y':'у','A':'А','E':'Е','I':'І','O':'О','P':'Р','C':'С','X':'Х','Y':'У'}

with open("text.txt", "r", encoding="utf-8") as f:
    ms = MutableString(f.read())

for i, ch in enumerate(ms):
    if ch in replacements:
        ms[i] = replacements[ch]

with open("text.txt", "w", encoding="utf-8") as f:
    f.write(str(ms))

print(f"Довжина тексту: {len(ms)}")