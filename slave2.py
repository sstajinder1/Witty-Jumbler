import itertools as tt
import pickle
import subprocess

with open ('name.p', 'rb') as fn2:
    name = pickle.load(fn2)

NameLen = len(name)
NameSplit = NameLen-2

total=[]
with open ('dict.p', 'rb') as fp:
    dic = pickle.load(fp)
    
for i in range(NameSplit,NameLen):
    x=list(set(tt.permutations(name,i)))
    for j in x:
        word="".join(j)
        if word in dic:
            total.append(word)

with open('s2.p', 'wb') as fs2:
    pickle.dump(total, fs2)
