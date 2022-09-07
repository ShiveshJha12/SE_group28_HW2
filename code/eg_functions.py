import random, re, sys, os
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


