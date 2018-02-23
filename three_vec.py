class ThreeVec(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def add(self, p):
        return ThreeVec(self.x + p.x, self.y + p.y, self.z + p.z)

    def wrap(self, wrap):
        for d in (0,1,2):
            if self[d] < -wrap: self[d] = wrap
            if self[d] > wrap: self[d] = -wrap

    def __getitem__(self, d):
        if d == 0: return self.x
        if d == 1: return self.y
        if d == 2: return self.z
        raise KeyError(d)

    def __setitem__(self, d, i):
        if d == 0: self.x = i
        elif d == 1: self.y = i
        elif d == 2: self.z = i
        else: raise KeyError(d)

    def __repr__(self):
        return "<{0}, {1}, {2}>".format(self.x, self.y, self.z)

