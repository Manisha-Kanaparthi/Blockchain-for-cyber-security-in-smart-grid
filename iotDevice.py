import random
import time

def getSensoryFeed():
    v=random.random()
    c=random.random()
    p=v*c
    print('Voltage: {}, Current: {}, Power: {}'.format(v,c,p))
    time.sleep(1)
    return (v,c,p)