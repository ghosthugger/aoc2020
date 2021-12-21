import math
import re
import sys
from collections import defaultdict

def distr(seq):
    i1=0
    i2=0
    i3=0

    pj = seq[0]
    for j in seq:
        curr = j-pj
        if(curr ==1):
            i1+=1
        if(curr ==2):
            i2+=1
        if(curr ==3):
            i3+=1

        pj = j

    return(i1-1,i2,i3)

cache = {}
def tree(seq):
    if "".join((str([i for i in seq]))) in cache:
        return cache["".join((str([i for i in seq])))]

    if(len(seq)<=1):
        cache["".join((str([i for i in seq])))] = 1
        return 1
    if(seq[1]-seq[0]==3):
        tmp = tree(seq[1:])
        cache["".join((str([i for i in seq])))] = tmp
        return tmp

    i=0
    while (i < len(seq)) and seq[i]-seq[0] <= 3 :
        i+=1

    s = 0
    for j in range(1,i):
        s+=tree(seq[j:])

    cache["".join((str([i for i in seq])))] = s
    return s





def main():

    res = []
    with open('day10.txt') as f:
        lines = f.readlines()
        for ls in lines:
            l = ls.strip()

            res.append(int(l))

    print(res.sort())
    print(res)

    i1=0
    i2=0
    i3=0

    pj = 0
    for j in res:
        curr = j-pj
        if(curr ==1):
            i1+=1
        if(curr ==2):
            i2+=1
        if(curr ==3):
            i3+=1

        pj = j


    print(i1)
    print(i2)
    print(i3+1)



    print(distr(res[1:4]))

    print(distr(res[5:7]))

    print((2**2)*(2**1))

    print("tree")
#    print(tree(res[5:]))
    print(tree(res))

    i1=0
    i2=0
    i3=0
    pj = res[0]
    comb=[]
    for j in res:
        curr = j-pj
        if(curr ==1):
            i1+=1
        if(curr ==2):
            i2+=1
        if(curr ==3):
            if(i1-1 >=0):
                comb.append((i1-1,i2))
            i1=0
            i2=0

        pj = j

    print("rrangements")
    print(comb)

if __name__ =="__main__":
    main()

