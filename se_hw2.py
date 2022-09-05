from xmlrpc.client import MAXINT
import math

import csv
with open('Data.csv', newline='') as csvfile:
    readfile1 = csv.reader(csvfile, delimiter=' ', quotechar='|')
    set1 = []
for row in readfile1:
    set1.append(row)

class Sym():
    def _init_(self, cpos, cname):
        self.n = 0
        self.at = cpos
        self.name = cname
        self._has = {}

    def add(self,x):
        if x != '?':
            self.n = self.n+1
        else:
            if x in self._has[x]:
                self._has[x] += 1
            else:        
                self._has[x] = 1

    def mid(self):
        most = -1
        mode = ''
        for key, value in self._has.items():
            if value > most:
                mode, most = key, value
        return mode

## def div() to be written
    def div(self):
        def fun(p):
            return p*math.log(p,2)
        e = 0
        for _, n in self._has.items():
            if n>0:
                e = e - fun(n/self.n)
        return e

class Nums():
    def __init__(self, cpos, cname):
        self.n = 0
        self.at = cpos
        self.name = cname
        self. lo = MAXINT
        self. hi = -MAXINT
        self.isSorted = True
        self._has = {}

    def nums(self):
        if not self.isSorted:
            self._has = sorted(self._has.items(), key=lambda x: x[1])
            self.isSorted = True
        return self._has()

    def add(self, x, pos):
        if x != '?':
            self.n = self.n+1
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)
        ## to be written ahead

    def div(self):
        a = self.nums()
        a90 = a[int(math.ceil((a.len() * 90) / 100)) - 1]
        a10 = a[int(math.ceil((a.len() * 10) / 100)) - 1]
        return ((a90-a10/2.58))


    def mid(self):
        a = self.nums()
        len = a.len()
        return (a[len//2])



        

    
