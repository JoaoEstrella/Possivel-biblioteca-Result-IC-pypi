import numpy as np

from .heuristica import Heuristica


class Pop(Heuristica):

    def __init__(self, meta, fun, ranges, nPop, nGen):

        self._objective = fun
        self.ranges = ranges
        self.minimize = True
# Realemnte devem ser zeros no vetor contador de nfc
        self.nfc = np.zeros(nGen)
        self.nG = 0
        self.nVar = ranges.shape[0]
        self.nPop = nPop
        self.nGen = nGen

        self.pList = [{'ch': np.zeros((nGen, self.nVar)),
                       'value': np.zeros(nGen),
                       'id': i}
                      for i in range(nPop)]

        self.pBest = {'ch': np.zeros((nGen, self.nVar)),
                      'value': np.zeros(nGen)}

        self.meta = meta
        self.parameters = meta.getParameters(self)

        meta.start(self)

    def __repr__(self):
        return "Pop(algo=%r, nPop=%r, nGen=%r) id: %s" % (
            self.meta.__class__.__name__, self.nPop, self.nGen, hex(id(self)))

    def __iter__(self):
        return self

    def __next__(self):
        self.nG += 1

        try:
            self.meta.nextGen(self)
            return self.pBest['value'][self.nG]
        except IndexError:
            raise StopIteration
