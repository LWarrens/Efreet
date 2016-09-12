from Efreet import createclientproxyobject
aa=createclientproxyobject(["Fizz", "Fuzz"], port=1780)
bb=createclientproxyobject(["Fazz"], port=1240)
globals().update(aa)
globals().update(bb)
Fazz.update("Yellow")
Fizz.update(5, True)
Fuzz.check()
d=Fazz.get(True)
Fuzz.proxyexec("def F(x):\n\tn=2*(x+1)\n\tprint n\n\treturn n\nFuzz.func1=F")
print d + " is the result"
Fuzz.func1(9)
print d