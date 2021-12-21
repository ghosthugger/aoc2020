import math
import re
import sys
from collections import defaultdict
import copy


def rotL(wp):
    if wp[0]>=0 and wp[1]>=0:
        return (-wp[1], wp[0])
    if wp[0]<=0 and wp[1]>=0:
        return (-wp[1], wp[0])
    if wp[0]<=0 and wp[1]<=0:
        return (-wp[1], wp[0])
    if wp[0]>=0 and wp[1]<=0:
        return (-wp[1], wp[0])

    return(0,0)

def main():
    abs=[]

    N=(0,1)
    E=(1,0)
    W=(-1,0)
    S=(0,-1)

    with open('day12.txt') as f:
        lines = f.readlines()
        cur_dir=(1,0)
        pos=(10,1)
        ship=(0,0)
        for ls in lines:
            l = ls.strip()
            print(l)
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
                    pos=rotL(pos)
            elif d=="R":
                for i in range(int((360-a)/90)):
                    pos=rotL(pos)
            elif d =="F":
                ship = (ship[0]+pos[0]*a, ship[1]+pos[1]*a)

        apos=[ship[0],ship[1]]
        if ship[0]<0:
            apos[0] = -ship[0]
        if ship[1]<0:
            apos[1] = -ship[1]


        print(apos[0]+apos[1])



if __name__ =="__main__":
    main()

