import math
import re
import sys
from collections import defaultdict
import copy


def main():
    s = set()
    with open('day17.txt') as f:
        lines = f.readlines()

        z=0
        x=0
        y=0
        w=0
        for ls in lines:
            l=ls.strip()
            for c in l:
                if c=="#":
                    s.add((x,y,z,w))
                x+=1
            x=0
            y+=1


    def active_n(s, p):
        x,y,z=p
        n=0
        for i in [x-1,x,x+1]:
            for j in [y-1,y,y+1]:
                for k in [z-1,z,z+1]:
                    if not (i,j,k)==p:
                        if (i,j,k) in s:
                            n+=1
        return n

    def span(s):
        minx=0
        miny=0
        minz=0
        maxx=0
        maxy=0
        maxz=0

        for p in s:
            minx=min(minx,p[0])
            miny=min(miny,p[1])
            minz=min(minz,p[2])
            maxx=max(maxx,p[0])
            maxy=max(maxy,p[1])
            maxz=max(maxz,p[2])
        return((minx,maxx,miny,maxy,minz,maxz))


    for b in range(6):
        ns = set()
        for p in s:
            n=active_n(s, p)
            if n==2 or n==3:
                ns.add(p)

        (minx,maxx,miny,maxy,minz,maxz) = span(s)
        for i in range(minx-1,maxx+2):
            for j in range(miny-1,maxy+2):
                for k in range(minz-1,maxz+2):
                    if not (i,j,k) in s:
                        if active_n(s, (i,j,k))==3:
                            ns.add((i,j,k))

        s=ns

        (minx,maxx,miny,maxy,minz,maxz) = span(s)
        for k in range(minz,maxz+1):
            print("z=")
            print(k)
            for j in range(miny,maxy+1):
                ln=""
                for i in range(minx,maxx+1):
                    if (i,j,k) in s:
                        ln=ln+"#"
                    else:
                        ln=ln+"."
                print(ln)
        print(s)

    print(len(s))

if __name__ =="__main__":
    main()
