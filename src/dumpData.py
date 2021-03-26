"""
Dumps sim data to binary
"""

from distribution import v_dist
import pickle
import os

def absList(vDist):
    for i in range(len(vDist)):
        vDist[i] = abs(vDist[i])
    return vDist

def load():
    v = absList(v_dist(0.1,1,50,100,1,-1,1))
    try:
        os.remove('bin/data.pkl')
    except Exception:
        pass
    #f = open('bin/data.pkl','x')
    #f.close()
    f = open('bin/data.pkl','wb')
    pickle.dump(v,f)
    f.close()

load()