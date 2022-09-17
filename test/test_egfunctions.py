from copy import copy
import random, sys, os
#code to import package from another folder from StackOverflow: https://stackoverflow.com/a/69258641 
import inspect
import os
import sys, pytest

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)


script_dir = os.path.dirname(__file__)  # Script directory
data_path = os.path.join(script_dir, '../data/data.csv')
test_csv_path = os.path.join(script_dir, '../data/auto93.csv')

from src.se_hw2 import *

# coerce = se_hw2.coerce
# the = se_hw2.the
# help = se_hw2.help
# Sym = se_hw2.Sym
# Nums = se_hw2.Nums
# Data = se_hw2.Data
# csv_fun = se_hw2.csv_fun
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


n = 0
def test_num(do_print = 0):
  num = Nums(None,None)
  for x in range(1,101):
    num.add(x)
  mid = num.mid()
  div = num.div()
  #temp code till we get test engine to run perfectly
  if do_print != 0:
    print("-----------------------------------")
    print(mid,div)
  return (50<=mid and mid<=52) and (30.5<div and div<32)

def test_bignum(do_print = 0):
  num = Nums(None,None)
  the["nums"] = 32
  for i in range(1,1001):
    num.add(i)
  #temp code till we get test engine running
  if do_print != 0:
    print("-----------------------------")
    print(sorted(num._has.values()))
  num.nums()
  return 32==len(num._has)
  
def test_sym(do_print = 0):
  sym = Sym(None, None)
  pairs = ['a', 'a', 'a', 'a', 'b', 'b', 'c']
  for x in pairs:
    sym.add(x)
  mode, entropy = sym.mid(), sym.div()
  entropy = (1000*entropy)//1/1000
  # oo({mid=mode, div=entropy})
  #temp printing code till we get test engine running
  if do_print != 0:
    print("----------------------------")
    print(":div    " + str(entropy) + "   :mid " + mode)
  return mode=='a' and 1.37<=entropy and entropy<=1.38

def test_csv(do_print = 0):
  print("--------------")
  global n 
  n = 0
  def my_fun(t):
    global n
    if n < 10:
      if do_print != 0:
        
        print(t)
      n = n+1
    else:
      pass
  csv_fun(test_csv_path, my_fun )
  return True
#   with open('../data/data.csv', mode='r') as csv_file:
#     data = csv.reader(csv_file, delimiter=',')
#     count = 0
#     for row in data:
#       count += 1
#       if(count > 10):
#         break
#       print('{' + ', '.join(row) + '}')


def test_data(do_print = 0):
  # Data is constructor
  data = Data(test_csv_path)

  for col in (data.cols.y):
    if do_print != 0:
      print("--------------------------------------")
      print(repr(col))
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

def test_stats(do_print = 0):
  # Data is constructor
  data = Data(test_csv_path)
  
  div = lambda col : col.div()
  mid = lambda col : col.mid()
  if do_print != 0:
    print("------------------------------------")
    print("xmid " + str(data.stats(2, data.cols.x, mid)))
    print("xdiv " + str(data.stats(3, data.cols.x, div)))
    print("ymid " + str(data.stats(2, data.cols.y, mid)))
    print("ydiv " + str(data.stats(3, data.cols.y, div)))
  return True

def test_the(do_print = 0):
  if do_print != 0 :
    print(the)
  return True


global fails
fails = 0
def all():
  global fails
  fun_list =  [test_num, test_bignum, test_csv, test_sym, test_stats, test_data, test_csv, test_the]
  for fun in fun_list:
    if runs(fun) != True:
      fails = fails + 1
  return True
  # print("num(): ",test_num())
  # print("bignum(): ",test_bignum())
  # print("sym():", test_sym())
  # print("stats()", test_stats())
  # print("data()", test_data())
  # print("csv()", test_csv())
  # return test_num and test_bignum and test_csv and test_sym and test_stats and test_data and test_csv and test_the


  


egd =  [test_num, test_bignum, test_csv, test_sym, test_stats, test_data, test_csv, test_the]
def runs(k):
    # if not k(): return
    # if k not in egd: return
    random.seed(the["seed"])
    old = {}
    for key,value in the.items():
        old[key] = value
    status = True
    if the["dump"] == True:
        status, out = True, k()
    else:
      try:
        egd[egd.index(k)]()
        status, out = True, k(1)
      except Exception as e:
        status, out = False, e
        print(e)
    for key,value in old.items():
        the[key] = value
    # msg = status and ((out == True and "PASS") or "FAIL") or "CRASH"
    if status == True:
      if out == True:
        msg = "PASS"
      else:
        msg = "FAIL"
    else:
      msg = "CRASH"
    print("!!!!!!", msg, k.__name__, status)
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


def main():
  all()
  print("tests failed:", fails)
  os._exit(fails)
if __name__ == '__main__':
  main()