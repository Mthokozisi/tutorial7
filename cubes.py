from numpy import arange

keys=arange(1,10,1)  #1-9. arange(1,11,1)
cube={}
for k in keys:
    cube[k]=k**3

print cube
del keys
