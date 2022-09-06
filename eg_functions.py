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

from ast import Num
import se_hw2
Sym = se_hw2.Sym
Nums = se_hw2.Nums
class eg():

  def num():
    num = Nums()
    for x in range(100):
      num.add(x)
    mid = num.mid()
    div = num.div()
    print(mid,div)
    return (50<=mid and mid<=52) and (30.5<div and div<32)

  def bignum():
    num = Nums(None,None)
    storage = 32
    for i in range(1000):
      num.add(i)
    print(sorted(num._has.values()))
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

print(eg.bignum())