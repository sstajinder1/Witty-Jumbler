import itertools as tt
import pickle
import subprocess

if __name__ == '__main__':
    with open ('name.p', 'rb') as fn1:
        name = pickle.load(fn1)

    NameLen = len(name)
    NameSplit = NameLen-2

    total=[]
    with open ('dict.p', 'rb') as fp:
        dic = pickle.load(fp)

    for i in range(1,NameSplit+1):
        x=list(set(tt.permutations(name,i)))
        for j in x:
            word="".join(j)
            if word in dic:
                total.append(word)

    with open('s1.p', 'wb') as fs1:
        pickle.dump(total, fs1)
