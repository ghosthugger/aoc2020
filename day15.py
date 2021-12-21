import math
import re
import sys
from collections import defaultdict
import copy
from collections import defaultdict
from collections import defaultdict

def rindex(lst, value):
    lst.reverse()
    i = lst.index(value)
    lst.reverse()
    return len(lst) - i - 1

def main():

    input=[0,8,15,2,12,1,4]
#    input=[0,3,6]

    prev={}

    prevs=[]
    for i in range(30000000):
        if i%100000==0:
            print(i)
        num=0
        if i<len(input):
            num=input[i]
        else:
            p=prevs[-1]
            if p in prev and len(prev[p])>1:
                li=len(prevs)
                pli=prev[p][:-1][-1]+1
#                pli2=rindex(prevs[:-1],p)+1
#                assert(pli==pli2)
                num=li-pli
            else:
                num=0

        if not num in prev:
            prev[num]=[i]
        else:
            prev[num].append(i)

        prev[num]=prev[num][-2:]
        prevs.append(num)

    print(num)
if __name__ =="__main__":
    main()
