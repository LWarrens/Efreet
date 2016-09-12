from time import sleep
from Efreet import createserverproxyobject, waitevents
def tmpsleep():
    sleep(1)
globals().update(createserverproxyobject(["Fizz", "Fuzz"], port=1780))
globals().update(createserverproxyobject(["Fazz"], port=1240))
waitevents(tmpsleep)