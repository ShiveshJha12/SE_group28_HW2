## def div() to be written
    def div(self):
        def fun(p):
            return p*math.log(p,2)
        e = 0
        for _, n in self._has.items():
            if n>0:
                e = e - fun(n/self.n)
        return e

def o(t):
    if isinstance(type(t), dict):
        return tostring(t)
    def show(k, v):
        if not tostring(k).find("^_"):
            v = o(v)
            return len(t)==0 and print(":%s %s", k, v) or tostring(v)
    u = {}
    for k, v in t.items():
        u[1+len(u)] = show(k, v)
    if len(t) == 0:
        u.sort()
    return "{" + " ".join(u) + "}"
    
def oo(t):
    print(o(t))
    return t

eg = {}

# this is the eg.sym() in lua code
# defining it as in the lua code would raise errors
# so will name function in a slightly different way for now
def eg_sym():
    sym = Sym
    pairs = {'a', 'a', 'a', 'a', 'b', 'b', 'c'}
    for _, x in pairs:
        sym.add(x)
    mode, entropy = sym.mid(), sym.div()
    entropy = (1000*entropy)//1/1000
    oo({mid=mode, div=entropy})
    return mode=='a' and 1.37<=entropy and entropy<=1.38

