import itertools as tt
import pickle
import subprocess

with open ('name.p', 'rb') as fn3:
    name = pickle.load(fn3)

NameLen = len(name)
NameSplit = NameLen-2

total=[]
with open ('dict.p', 'rb') as fp:
    dic = pickle.load(fp)
    
for i in range(NameLen,NameLen+1):
    x=list(set(tt.permutations(name,i)))
    for j in x:
        word="".join(j)
        if word in dic:
            total.append(word)
            
with open('s3.p', 'wb') as fs3:
    pickle.dump(total, fs3)
