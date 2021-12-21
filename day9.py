import math
import re
import sys
from collections import defaultdict

def main():

    res = []
    with open('day9.txt') as f:
        lines = f.readlines()
        for ls in lines:
            l = ls.strip()
            res.append(int(l))

    plen = 25
    for i in range(plen,len(res)):
        preamble = res[i-plen:i]
        n = res[i]

        sumof = False
        for x in range(len(preamble)):
            for y in range (len(preamble)):
                if x!=y:
                    if preamble[x] + preamble[y] == n:
                        sumof = True

        if(sumof == False):
            pass
#            print(n)
#            break

    r = 1492208709

    for x in range(len(res)):
        for y in range (len(res)):
            if(x<y):
                seq = res[x:y]
                s = sum(seq)
                if(s==r):
                    print(x,y)
                    print(min(seq)+max(seq))
                    break



if __name__ =="__main__":
    main()

