from operator import le
import random
from xmlrpc.client import MAXINT
import math

import csv

help="""CSV : summarized csv file
(c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license
USAGE: lua seen.lua [OPTIONS]
OPTIONS:
 -e  --eg        start-up example                      = nothing
 -d  --dump      on test failure, exit with stack dump = false
 -f  --file      file with csv data                    = ../data/auto93.csv
 -h  --help      show help                             = false
 -n  --nums      number of nums to keep                = 512
 -s  --seed      random number seed                    = 10019
 -S  --seperator feild seperator                       = , """

the = {}
# the[x[0]] = coerce(x[1])
the["eg"] = "nothing"
the["dump"] = False
the["file"] = "data.csv"
the["help"] = help
the["nums"] = 512
the["seed"] = 10019
the["seperator"] = ','



with open('data.csv', newline='') as csvfile:
    readfile1 = csv.reader(csvfile, delimiter=' ', quotechar='|')
    set1 = []
    for row in readfile1:
        set1.append(row)

class Sym():
    def __init__(self, cpos, cname):
        self.n = 0
        self.at = cpos
        self.name = cname
        self._has = {}

    def add(self,x):
        if x != '?':
            self.n = self.n+1
            if x in self._has:
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
            self._has = {k:v for k,v in sorted(self._has.items(), key=lambda x: x[1])}

            self.isSorted = True
        return self._has

    def add(self,x):
        pos = None
        if x != '?':
            self.n = self.n+1
            self.lo = min(x, self.lo)
            self.hi = max(x, self.hi)
            if len(self._has) < the["nums"]:
                pos = 1 + len(self._has)
            elif random.random()<the["nums"]/self.n:
                pos = random.randint(0,len(self._has))
            if pos:
                self.isSorted = False
                self._has[pos] = int(x)

    def per(self,t,p):
        p = math.floor(((p or 0.5)* len(t))+ 0.5)
        return t[max(1, min(len(t), p))]

    def div(self):
        a = self.nums()
        a2 = list(a.values())
        return (self.per(a2,0.9) - self.per(a2,0.1))/2.58


    def mid(self):
        return self.per(list(self.nums().values()), 0.5)
    

class Cols():
    def __init__(self, names):
        self.names = names
        self.all = []
        self.x = []
        self.y = []
        self.klass = None
    
    def column(self):
        for c in range(len(self.names)):
            if (re.search('^[A-Z]', self.names[c])):
                self.all.append(Nums(c, self.names[c])) 
                col =  Nums(c, self.names[c])
            else:
                self.all.append(Sym(c, self.names[c]))
                col = Sym(c, self.names[c])
            if not re.search(':$', self.names[c]):
                self.y.append(Nums(c, self.names[c])) if (re.search('[!+-]')) else self.x.append(Sym(c, self.names[c]))
                if re.search('!$', self.names[c]):
                    self.klass = col

# class Row():
#     def __init__(self, t):
#         self.cells = t
#         isEvaled = False
#         cooked = copy(t)            ##copy function yet to be written in eg_functions.py
