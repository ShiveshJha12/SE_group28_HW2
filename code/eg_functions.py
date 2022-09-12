import random, re, sys, os
import csv
from ast import Num
import se_hw2
the = se_hw2.the
help = se_hw2.help
Sym = se_hw2.Sym
Nums = se_hw2.Nums


class eg:
  def num():
    num = Nums(None,None)
    for x in range(1,101):
      num.add(x)
    mid = num.mid()
    div = num.div()
    #temp code till we get test engine to run perfectly
    print("-----------------------------------")
    print(mid,div)
    return (50<=mid and mid<=52) and (30.5<div and div<32)

  def bignum():
    num = Nums(None,None)
    the["nums"] = 32
    for i in range(1,1001):
      num.add(i)
    #temp code till we get test engine running
    print("-----------------------------")
    print(sorted(num._has.values()))
    num.nums()
    return 32==len(num._has)
    
  def sym():
    sym = Sym(None, None)
    pairs = ['a', 'a', 'a', 'a', 'b', 'b', 'c']
    for x in pairs:
      sym.add(x)
    mode, entropy = sym.mid(), sym.div()
    entropy = (1000*entropy)//1/1000
    # oo({mid=mode, div=entropy})
    #temp printing code till we get test engine running
    print("----------------------------")
    print(":div    " + str(entropy) + "   :mid " + mode)
    return mode=='a' and 1.37<=entropy and entropy<=1.38

  def csv():
    with open('../data/data.csv', mode='r') as csv_file:
      data = csv.reader(csv_file, delimiter=',')
      count = 0
      for row in data:
        count += 1
        if(count > 10):
          break
        print('{' + ', '.join(row) + '}')
  
  def data():
    with open('../data/data.csv', mode='r') as csv_file:
      data = csv.reader(csv_file, delimiter=',')
      tmp = []
      indexes = []
      col_title = []
      weight = []
      row_count = 0
      for row in data:
          if(row_count == 0):
            col_count = 0
            for col_name in row:
              col_count += 1
              if(col_name.find('+') != -1 or col_name.find('-') != -1):
                weight.append(1) if (col_name.find('+') != -1) else weight.append(-1)
                col_title.append(col_name)
                # get the indexes of columns to caculate
                indexes.append(col_count)
                # put lists of data to calculate
                tmp.append([])
          else:
            for col in indexes:
              # add data to tmp list
              tmp[indexes.index(col)].append(float(row[col-1]))
      for col in indexes:
        print("{:at " + str(indexes[indexes.index(col)]) + 
              " :hi " + str(max(tmp[indexes.index(col)])) + 
              " :isSorted " + str(tmp[indexes.index(col)] == sorted(tmp[indexes.index(col)])) + 
              " :lo " + str(min(tmp[indexes.index(col)])) + 
              " :n " + str(len(tmp[indexes.index(col)])) + 
              " :name " + str(col_title[indexes.index(col)]) + 
              " :w " + str(weight[indexes.index(col)]) + "}")

egd = {}
def runs(k):
    # if not egd[k]: return
    # if egd[k] == None: return ""
    random.seed(the["seed"])
    old = {}
    for k,v in the.items():
        old[k] = v
    
    if the["dump"] == True:
        status, out = True, egd[k]()
    else:
      try:
        egd[k]
      except Exception as e:
        status, out = False, e
    for k,v in old.items():
        the[k] = v
    msg = status and ((out == "true" and "PASS") or "FAIL") or "CRASH"
    print("!!!!!!", msg, k, status)
    return out


def coerce(s):
    def fun(s1):
        if s1 == "true": return True
        if s1 == "false": return False
        return s1
    return int(s) or fun(re.match(s, "^\s*[.]*\s*"))

def cli(t):
    for slot,v in (t.items()):
        v = str(v)
        for n,x in t.items():
            if x == "-" + (str(slot)[1:1]) or x == "--"+str(slot):
                v = v == "false" and "true" or v == "true" and "false" or t[n+1] #or ??
        t[slot] = coerce(v)
    if t["help"]: sys.exit(print("\n" + help +"\n"))
    return t


print("eg.num(): ",eg.num())
print("eg.bignum(): ",eg.bignum())
print("eg.sym():", eg.sym())
# the = cli(the)
# runs(the["eg"])


