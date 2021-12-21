import math
import re
import sys
from collections import defaultdict
import copy
from collections import defaultdict

def main():

    with open('day16.txt') as f:
        lines = f.readlines()

        fields={}
        ticket=[]
        nearby=[]
        part=0
        for ls in lines:
            l=ls.strip()

            if l=="":
                pass
            elif l=="your ticket:":
                part=1
            elif l=="nearby tickets:":
                part=2
            elif(part==0):
                name, ranges_str=l.split(":")
                name=name.strip(":")
                ranges = ranges_str.split(" or ")
                fields[name]=ranges
            elif(part==1):
                ticket=l.split(",")
            elif(part==2):
                nearby.append(l.split(","))


    ranges=[]
    for f in fields.values():
        for r in f:
            low,high=r.split("-")
            ranges.append((int(low),int(high)))

    inv=[]
    for t in nearby:
        for v in t:
            passed_any=False
            for l,h in ranges:
                if int(v)<=h and int(v)>=l:
                    passed_any=True
            if not passed_any:
                inv.append(int(v))

    print(sum(inv))

    valid=[]
    inv=[]
    for t in nearby:
        passed_all = True
        for v in t:
            passed_any=False
            for l,h in ranges:
                if int(v)<=h and int(v)>=l:
                    passed_any=True
            if not passed_any:
                passed_all = False
        if passed_all:
            valid.append(t)

    print(valid)

    def isInRange(t, range):
        l,h=range
        return(int(t)<=int(h) and int(t)>=int(l))

    field_ranges={}
    for k in fields.keys():
        f=fields[k]
        ranges=[]
        for r in f:
            low,high=r.split("-")
            ranges.append((int(low),int(high)))
        field_ranges[k]=ranges


    deps=[]

    while(len(fields) > 0):
        cols={}
        for i in range(len(ticket)):
            for field in fields.keys():
                all=True
                for t in valid:
                    any_range=False
                    for fieldrange in field_ranges[field]:
                        if isInRange(t[i], fieldrange):
                            any_range=True

                    if not any_range:
                        all=False

                if all:
                    if not i in cols:
                        cols[i]=[field]
                    else:
                        cols[i].append(field)

        print(cols)
        for k in cols.keys():
            if len(cols[k])==1:
                print("found")
                print(k)
                print(cols[k])
                deps.append((k,cols[k][0]))
                fields.pop(cols[k][0])

    print(deps)

    m=1
    for d in deps:
        if d[1].startswith("departure"):
            m*=int(ticket[int(d[0])])

    print(m)


if __name__ =="__main__":
    main()
