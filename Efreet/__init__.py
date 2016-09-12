from time import sleep

from Pyro4 import config, expose
from Pyro4 import Daemon,Proxy
import Pyro4
from Pyro4.core import DaemonObject
from select import select
config.REQUIRE_EXPOSE = False
#because I couldn't get pyro4 to disable expose
@expose
class ProxyAdapter(Proxy):
    def __init__(self, *args):
        super(ProxyAdapter, self).__init__(*args)
@expose
class ServerProxyObject(dict):
    def __init__(self,name):
        self.name=name
        self.box=None
        self.func1=None
        self.func2=None
        self.func3=None
    def proxyexec(self, arg, display=False):
        if display==True:print arg
        "to execute code in daemon script"
        try: exec(arg)
        except Exception as e:print "Error",e,"\n",arg
    def deliver(self):pass
    def update(self,space,display=False):
        self.box=space
        if display==True:print "storing:",self.name,"data:",self.box
    def get(self,display=False):
        if display==True:print "passing:",self.name,"data:",self.box
        return self.box
    def check(self):
        print '"'+self.name+'"',"container","\n","data:",self.box

__EFREET_DAEMON_=[]
def createserverproxyobject(names, host="localhost", port=30238, unixsocket=None, nathost=None, natport=None):
    d=Daemon(host,port,unixsocket,nathost,natport)
    locals()["{0}{1}Efreet".format(host,port)]=d
    for i in names:
        locals()[i]=ServerProxyObject(i)
        uri=locals()["{0}{1}Efreet".format(host,port)].register(locals()[i],i)
        print uri
    __EFREET_DAEMON_.append(["DAEMON{0}{1}".format(host, port), names, host, port, unixsocket, nathost, natport, locals()["{0}{1}Efreet".format(host, port)]])
    return {"__EFREET_DAEMON_":__EFREET_DAEMON_}

__spirit={}
def createclientproxyobject(i, port=30238, hostname="localhost"):
    for g in i:
        locals()[g]=Proxy("PYRO:"+str(g)+"@"+str(hostname)+":"+str(port))
        print locals()[g]
        __spirit.update({g:locals()[g]})
    return __spirit

@expose
def waitevents(*args):
    while True:
        map(lambda b: map(lambda s:b[7].events([s]),select(b[7].sockets,[],[],0)[0]), __EFREET_DAEMON_)
        for arg in args:
            arg()
