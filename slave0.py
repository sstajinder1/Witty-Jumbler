import itertools as tt
import pickle
import subprocess

if __name__ == '__main__':
    with open ('name.p', 'rb') as fn0:
        name = pickle.load(fn0)

    NameLen = len(name)
    
    total=[]
    with open ('dict.p', 'rb') as fp:
        dic = pickle.load(fp)

    for i in range(1,NameLen+1):
        x=list(set(tt.permutations(name,i)))
        for j in x:
            word="".join(j)
            if word in dic:
                total.append(word)

    with open('s0.p', 'wb') as fs0:
        pickle.dump(total, fs0)
