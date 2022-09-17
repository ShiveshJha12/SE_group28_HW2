from configparser import NoOptionError
from operator import le
import random, os

from xmlrpc.client import MAXINT
import math
import re
import csv
import copy

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
# help:gsub("\n [-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)",
#           function(k,x) the[k]=coerce(x) end)

# the[x[0]] = coerce(x[1])
the["eg"] = "nothing"
the["dump"] = False
the["file"] = "data.csv"
the["help"] = help
the["nums"] = 512
the["seed"] = 10019
the["seperator"] = ","

script_dir = os.path.dirname(__file__)  # Script directory
data_path = os.path.join(script_dir, '../data/data.csv')

def coerce(s):
    def fun(s1):
        if s1 == "true": return True
        if s1 == "false": return False
        return s1
    try:
      return float(s)
    except:
        return s
    #   return fun(re.match(s, "^\s*[.]*\s*"))
 
def csv_fun(file_path,func):
    with open(file_path, newline='') as csvfile:
        readfile1 = csv.reader(csvfile, delimiter=',')
        # print(readfile1) #recently commented
        for row in readfile1:
            t = []
            for ele in row:
                t.append(coerce(ele))
                # print(">>>>>>>>>>>t:", t)
            func(t)


    # file = open(file_path, encoding='UTF8')
    # src = csv.reader(file, delimiter=' ')
    # sep = ','
    # for s in src:
    #     t=[]
    #     for s1 in row: #change to io read
    #         # t.append(coerce(s1))
    #         t.append(s1)
    #     func(t)



# def csv_fun(file_path, fun):
#     separator = the["seperator"]
#     with open(file_path, 'r') as f:
#         results = []
#         for line in f:
#                 entry = line.split(the["seperator"])
#                 results.append(coerce(entry))
#                 print(results)
#     return fun(results)


with open(data_path, newline='') as csvfile:
    readfile1 = csv.reader(csvfile, delimiter=' ', quotechar='|')
    set1 = []
    for row in readfile1:
        set1.append(row)

class Sym:
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

class Nums:
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
    

class Cols:
    def __init__(self, names):
        self.names = names
        self.all = []
        self.klass = None
        self.x = []
        self.y = []
        for i in range(len(names)):
            # print("!!!!!!!!!!!!!!", self.names)
            if re.search('^[A-Z]', self.names[i]):
                col = Nums(i,self.names[i])
                self.all.append(Nums(i,self.names[i]))
            else:
                col = Sym(i,self.names[i])
                self.all.append(Sym(i,self.names[i]))
            if not re.search(':$', self.names[i]):
                if re.search('[!+-]', self.names[i]):
                    self.y.append(col)
                else:
                    self.x.append(col)
                if re.search('[!$]', self.names[i]):
                    self.klass = col
            

class Row:
    def __init__(self, t):
        self.cells = t
        isEvaled = False
        cooked = copy.deepcopy(t)            ##copy function yet to be written in eg_functions.py

import numbers
class Data:
    # cols = None
    def __init__(self,src):
        self.cols = None
        self.rows = []
        if(type(src) == str):
            csv_fun(src,lambda row: self.add(row))
        else:
            for row in (src):
                # print("!!!!!!!!!!!!!", row)
                self.add(row)
    

    def add (self, xs):
        # print("!!XS!!!!", xs)
        if self.cols == None:
            self.cols = Cols(xs)
        else:
            # row = xs if xs != None else Row(xs)
            row = Row(xs)
            self.rows.append(xs if xs != None else Row(xs))
            for todo in [self.cols.x, self.cols.y]: 
                for col in todo:
                    col.add(row.cells[col.at])
 
    def stats(self, places, showCols, fun):
        showCols, fun = showCols or self.cols.y, fun or "mid"
        t = {}
        for col in showCols:
            # print("------------------------------>>>>>>>",col)
            v = fun(col)
            v = round(v, places) if (isinstance(v, numbers.Number) ) else v
            t[col.name] = v
        return t
