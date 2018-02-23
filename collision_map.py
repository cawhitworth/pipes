from utils import direction_vec

class CollisionMap(object):
    def __init__(self):
        self.m = dict()

    def is_occupied(self, p):
        if p.x in self.m:
            m2 = self.m[p.x]
            if p.y in m2:
                m3 = m2[p.y]
                return p.z in m3

    def add(self, p):
        if not p.x in self.m:
            self.m[p.x] = dict()

        m2 = self.m[p.x]

        if not p.y in m2:
            m2[p.y] = dict()

        m3 = m2[p.y]

        m3[p.z] = 1

    def is_trapped(self, p, wrap):
        for direction in range(1,7):

            d = direction_vec[direction]
            pp = p.add(d)
            pp.wrap(wrap)

            if not self.is_occupied(pp):
                return False

        return True
