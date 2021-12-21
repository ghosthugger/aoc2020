import math
import re
import sys
from collections import defaultdict
import copy


# re.match("^#[0-9a-z][0-9a-z][0-9a-z][0-9a-z][0-9a-z][0-9a-z]$", p["hcl"])

def main():

    rules = {}
    messages=[]
    with open('day19.txt') as f:
        lines = f.readlines()

        mode=0
        for ls in lines:
            l=ls.strip()

            if len(l)==0:
                mode=1

            if mode==0:
                key, value = l.split(": ")
                values = value.split(" ")

                values=[v.replace("\"","") for v in values]

                rules[key] = values
            else:
                messages.append(l)

    def createRexep(key):
        res="("
        lit=False
        for c in rules[key]:
            if c in rules:
                res+= createRexep(c)
            elif c== "|":
                res+="|"
            else:
                lit=True
                res+=c

        res = res + ")"

        if lit:
            return res[1:-1]
        else:
            return res

    r = "^"+createRexep("0")+"$"
    print(r)

    indent=0
    def printRexep(key):
        nonlocal indent
        indent+=1
        ind= " " * indent
        for c in rules[key]:
            if c in rules:
                printRexep(c)
            elif c== "|":
                print(ind+"|")
            else:
                print(ind+c)
        indent-=1

#    print("tree")
#    printRexep("42")

    a=0
    for m in messages:
        if(re.match(r, m) is not None):
            print(m)
            a+=1

    print(a)


if __name__ =="__main__":
    main()
