# def o(t):
#     if isinstance(type(t), dict):
#         return tostring(t)
#     def show(k, v):
#         if not tostring(k).find("^_"):
#             v = o(v)
#             return len(t)==0 and print(":%s %s", k, v) or tostring(v)
#     u = {}
#     for k, v in t.items():
#         u[1+len(u)] = show(k, v)
#     if len(t) == 0:
#         u.sort()
#     return "{" + " ".join(u) + "}"
    
# def oo(t):
#     print(o(t))
#     return t

import random, re, sys, os
from ast import Num
import se_hw2
the = se_hw2.the
help = se_hw2.help
Sym = se_hw2.Sym
Nums = se_hw2.Nums


class eg():

  def num():
    num = Nums(None,None)
    for x in range(1,101):
      num.add(x)
    mid = num.mid()
    div = num.div()
    print(mid,div)
    return (50<=mid and mid<=52) and (30.5<div and div<32)

  def bignum():
    num = Nums(None,None)
    storage = 32
    for i in range(1,1001):
      num.add(i)
    #print(sorted(num._has.values()))
    num.nums()
    return 32==len(num._has)
    
  def sym():
    sym = Sym()
    pairs = {'a', 'a', 'a', 'a', 'b', 'b', 'c'}
    for x in pairs:
      sym.add(x)
    mode, entropy = sym.mid(), sym.div()
    entropy = (1000*entropy)//1/1000
    # oo({mid=mode, div=entropy})
    return mode=='a' and 1.37<=entropy and entropy<=1.38

egd = {}
def runs(k):
    
    # if egd[k] == None: return ""
    random.seed(the["seed"])
    old = {}
    for k,v in the.items():
        old[k] = v
    
    if the["dump"] == True:
        status, out = True, egd[k]()
    else:
        status, out = False,"Error"
    for k,v in old.items():
        the[k] = v
    msg = status and ((out == "true" and "PASS") or "FAIL") or "CRASH"
    print("!!!!!!", msg, k, status)
    return out#or err?


def coerce(s):
    def fun(s1):
        if s1 == "true": return True
        if s1 == "false": return False
        return s1
    return int(s) or fun(re.match(s, "^\s*[.]*\s*"))
# for k,v in the:
#     the[k] = coerce(v)
# print(the)
def cli(t):
    for slot,v in (t.items()):
        v = str(v)
        for n,x in t.items():
            if x == "-" + (str(slot)[1:1]) or x == "--"+str(slot):
                v = v == "false" and "true" or v == "true" and "false" #or ??
        t[slot] = (v)
    if t["help"]: sys.exit(print("\n" + help +"\n"))
    return t

print("Result of eg.num() test function : ",eg.num())
print("Result of eg.bignum() test function : ",eg.bignum())
the = cli(the)
# print("---->",runs(the["eg"]))

