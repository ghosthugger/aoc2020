import math
import re
import sys
from collections import defaultdict
import copy


def main():
    abs=[]

    N=(0,1)
    E=(1,0)
    W=(-1,0)
    S=(0,-1)

    with open('day12.txt') as f:
        lines = f.readlines()
        cur_dir=(1,0)
        pos=(0,0)
        for ls in lines:
            l = ls.strip()

            d = l[:1]
            a = int(l[1:])
            if d in ["N", "S", "E", "W"]:
                ldir=""
                if d=="N":
                    ldir=N
                elif d=="E":
                    ldir=E
                elif d=="W":
                    ldir=W
                elif d=="S":
                    ldir=S

                pos = (pos[0]+ldir[0]*a, pos[1]+ldir[1]*a)

            elif d=="L":
                for i in range(int(a/90)):
                    if cur_dir==(1,0): #E
                        cur_dir = (0,1) #N
                    elif cur_dir==(0,1): #N
                        cur_dir=(-1,0) #W
                    elif cur_dir==(-1,0):#W
                        cur_dir=(0,-1) #S
                    elif cur_dir==S:
                        cur_dir=E
            elif d=="R":
                for i in range(int(a/90)):
                    if cur_dir==(1,0): #E
                        cur_dir = (0,-1) #S
                    elif cur_dir==(0,-1): #S
                        cur_dir=(-1,0) #W
                    elif cur_dir==(-1,0):#W
                        cur_dir=(0,1) #N
                    elif cur_dir==N:
                        cur_dir=E
            elif d =="F":
                pos = (pos[0]+cur_dir[0]*a, pos[1]+cur_dir[1]*a)

        apos=[pos[0],pos[1]]
        if pos[0]<0:
            apos[0] = -pos[0]
        if pos[1]<0:
            apos[1] = -pos[1]


        print(apos[0]+apos[1])



if __name__ =="__main__":
    main()

