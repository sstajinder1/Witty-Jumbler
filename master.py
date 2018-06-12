import itertools as tt
import pickle
import subprocess
import time
import os

def witty_jumbler(name,msgs):

    total=[]
    if(len(name)>0):
        name = name.lower()
        name = "".join(name.split())
        if(msgs>0):
            print("Processing input: ",name)
        if(not(name.isalpha())):
            if(msgs>0):
                print("String is not alphabetic!")
            return total
    else:
        if(msgs>0):
            print("String length is zero!")
        return total

    name=list(name)
    name.sort()
    NameLen = len(name)
    NameSplit = NameLen-2
    
    if(NameLen>7):
        if(msgs>0):
            print("WARNING: String too large! This might take time")

    with open('name.p', 'wb') as fn:
        pickle.dump(name, fn)

    if(NameLen>3):
            
        s1 = subprocess.Popen(['python','slave1.py'])
        s2 = subprocess.Popen(['python','slave2.py'])
        s3 = subprocess.Popen(['python','slave3.py'])
        if(msgs>0):
            print("Processing...")
        tic = time.clock()
        while True:
            if(os.path.isfile("s1.p") and os.path.isfile("s2.p") and os.path.isfile("s3.p")):
                toc = time.clock()
                break
        dur = toc-tic
        if(msgs>0):
            print("Seconds taken :")
        if(msgs>=0):
            print(dur)
        with open ('s1.p', 'rb') as fs1:
            o1 = pickle.load(fs1)
        with open ('s2.p', 'rb') as fs2:
            o2 = pickle.load(fs2)
        with open ('s3.p', 'rb') as fs3:
            o3 = pickle.load(fs3)

        os.remove("name.p")
        os.remove("s1.p")
        os.remove("s2.p")
        os.remove("s3.p")

        total = list(set(o1+o2+o3))
        total.sort()
        total.sort(key = lambda s: len(s))
        #print(total)
        if(msgs == -1):
            return [str(dur)]+total
        else:
            return total

    elif(NameLen<=3):
        
        s0 = subprocess.Popen(['python','slave0.py'])
        if(msgs>0):
            print("Processing...")
        tic = time.clock()
        while True:
            if(os.path.isfile("s0.p")):
                toc = time.clock()
                break
        dur = toc-tic
        if(msgs>0):
            print("Seconds taken :")
        if(msgs>=0):
            print(dur)
        with open ('s0.p', 'rb') as fs0:
            o0 = pickle.load(fs0)

        os.remove("name.p")
        os.remove("s0.p")

        total = list(set(o0))
        total.sort()
        total.sort(key = lambda s: len(s))
        #print(total)
        if(msgs == -1):
            return [str(dur)]+total
        else:
            return total
