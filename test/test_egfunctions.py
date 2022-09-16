from copy import copy
import random, sys, os
#code to import package from another folder from StackOverflow: https://stackoverflow.com/a/69258641 
import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from src import se_hw2

coerce = se_hw2.coerce
the = se_hw2.the
help = se_hw2.help
Sym = se_hw2.Sym
Nums = se_hw2.Nums
Data = se_hw2.Data
csv_fun = se_hw2.csv_fun
from pprint import pprint
# def o(t):
#   if(type(t) is not dict):
#     return str(t)
#   def show(k, v):
#     if not str(k).find("^_"):
#       v = o(v)
#       output_string = ":{} {}"
#       return output_string.format(k, v) if len(t) == 0 else str(v)
#   u = {}
#   for k, v in t.items():
#     u[1+len(u)] = show(k, v)
#   if len(t) == 0:
#     # sort dict u
#     u = u
#   return "{" + " ".join(u) + "}"

class eg:
  n = 0
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
    print("--------------")
    global n 
    n = 0
    def my_fun(t):
      global n
      if n < 10:
        print(t)
        n = n+1
      else:
        pass
        
    csv_fun("../data/auto93.csv", my_fun )
    return True
  #   with open('../data/data.csv', mode='r') as csv_file:
  #     data = csv.reader(csv_file, delimiter=',')
  #     count = 0
  #     for row in data:
  #       count += 1
  #       if(count > 10):
  #         break
  #       print('{' + ', '.join(row) + '}')


  def data():
    print("--------------------------------------")
    # Data is constructor
    data = Data('../data/data.csv')

    for col in (data.cols.y):
      print(vars(col))
    
    return True

    ### use the following if o(col) doesn't work
    # with open('../data/data.csv', mode='r') as csv_file:
    #   data = csv.reader(csv_file, delimiter=',')
    #   tmp = []
    #   indexes = []
    #   col_title = []
    #   weight = []
    #   row_count = 0
    #   for row in data:
    #       if(row_count == 0):
    #         col_count = 0
    #         for col_name in row:
    #           col_count += 1
    #           if(col_name.find('+') != -1 or col_name.find('-') != -1):
    #             weight.append(1) if (col_name.find('+') != -1) else weight.append(-1)
    #             col_title.append(col_name)
    #             # get the indexes of columns to caculate
    #             indexes.append(col_count)
    #             # put lists of data to calculate
    #             tmp.append([])
    #       else:
    #         for col in indexes:
    #           # add data to tmp list
    #           tmp[indexes.index(col)].append(float(row[col-1]))
    #   for col in indexes:
    #     print("{:at " + str(indexes[indexes.index(col)]) + 
    #           " :hi " + str(max(tmp[indexes.index(col)])) + 
    #           " :isSorted " + str(tmp[indexes.index(col)] == sorted(tmp[indexes.index(col)])) + 
    #           " :lo " + str(min(tmp[indexes.index(col)])) + 
    #           " :n " + str(len(tmp[indexes.index(col)])) + 
    #           " :name " + str(col_title[indexes.index(col)]) + 
    #           " :w " + str(weight[indexes.index(col)]) + "}")

  def stats():
    # Data is constructor
    print("------------------------------------")
    data = Data('../data/data.csv')
    
    div = lambda col : col.div()
    mid = lambda col : col.mid()
    print((data.stats(2, data.cols.x, mid)))
    # print("xmid " + (data.stats(2, data.cols.x, mid)))
    # print("xdiv " + (data.stats(3, data.cols.x, div)))
    # print("ymid " + (data.stats(2, data.cols.y, mid)))
    # print("ydiv " + (data.stats(3, data.cols.y, div)))

    return True
  
  def all():
    print("eg.num(): ",eg.num())
    print("eg.bignum(): ",eg.bignum())
    print("eg.sym():", eg.sym())
    print("eg.stats()", eg.stats())
    print("eg.data()", eg.data())
    print("eg.csv()", eg.csv())


  


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




def cli(t):
    for slot,v in (t.items()):
        v = str(v)
        for n,x in t.items():
            if x == "-" + (str(slot)[1:1]) or x == "--"+str(slot):
                v = v == "false" and "true" or v == "true" and "false" or sys.argv[n+1] #or ??
        t[slot] = coerce(v)
    if t["help"]: sys.exit(print("\n" + help +"\n"))
    return t

eg.all()
the = cli(the)
runs(the["eg"])
