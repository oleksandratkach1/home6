import math

class Segment:
    def __init__(self, start=0, end=0, lo=False, ro=False, empty=False):
        self.empty = empty
        self.start = start
        self.end = end
        self.lo = lo
        self.ro = ro

    def contains(self, x):
        if self.empty: return False
        return (x > self.start if self.lo else x >= self.start) and (x < self.end if self.ro else x <= self.end)

    def is_empty(self):
        if self.empty or self.start > self.end: return True
        return self.start == self.end and (self.lo or self.ro)

    def __repr__(self):
        if self.is_empty(): return "∅"
        return f"{'(' if self.lo else '['}{self.start:.4f}, {self.end:.4f}{')' if self.ro else ']'}"


class SegmentSetIterator:
    def __init__(self, segs):
        self._items = sorted([s for s in segs if not s.is_empty()], key=lambda s: s.start)
        self._i = 0

    def __iter__(self): return self

    def __next__(self):
        if self._i >= len(self._items): raise StopIteration
        v = self._items[self._i]; self._i += 1; return v


class SegmentSet:
    def __init__(self, segs=None):
        self.segs = segs or []

    def __iter__(self): return SegmentSetIterator(self.segs)

    def _wrap(self, o):
        if isinstance(o, SegmentSet): return o
        if isinstance(o, Segment): return SegmentSet([o])
        return SegmentSet([Segment(o, o)])

    def contains(self, x): return any(s.contains(x) for s in self.segs)

    def __mul__(self, o):
        o = self._wrap(o); res = []
        for a in self.segs:
            for b in o.segs:
                s = Segment(max(a.start,b.start), min(a.end,b.end),
                    a.lo if a.start>b.start else (b.lo if b.start>a.start else a.lo or b.lo),
                    a.ro if a.end<b.end else (b.ro if b.end<a.end else a.ro or b.ro))
                if not s.is_empty(): res.append(s)
        return SegmentSet(res)

    def __add__(self, o): return SegmentSet(self.segs + self._wrap(o).segs)

    def __sub__(self, o):
        o = self._wrap(o)
        pts = sorted(set(p for s in self.segs+o.segs for p in [s.start,s.end]))
        res = []
        for i in range(len(pts)-1):
            mid = (pts[i]+pts[i+1])/2
            if self.contains(mid) and not o.contains(mid):
                res.append(Segment(pts[i], pts[i+1], not self.contains(pts[i]) or o.contains(pts[i]), not self.contains(pts[i+1]) or o.contains(pts[i+1])))
        return SegmentSet(res)

    def __truediv__(self, o): return (self - o) + (self._wrap(o) - self)

    def __repr__(self):
        s = [str(x) for x in self if not x.is_empty()]
        return " ∪ ".join(s) if s else "∅"


def solve(a, b, c, strict=False):
    D = b**2 - 4*a*c
    if D < 0: return SegmentSet([Segment(-math.inf, math.inf, True, True)]) if a > 0 else SegmentSet()
    x1 = (-b - math.sqrt(D)) / (2*a)
    x2 = (-b + math.sqrt(D)) / (2*a)
    if a > 0: return SegmentSet([Segment(-math.inf, x1, True, strict), Segment(x2, math.inf, strict, True)])
    return SegmentSet([Segment(x1, x2, strict, strict)])


inequalities = [(1, -5, 6, False), (1, -3, 2, True), (1, 1, -6, False)]

result = solve(*inequalities[0])
for ineq in inequalities[1:]:
    result = result * solve(*ineq)

print("Розв'язок:")
for seg in result:
    print(seg)