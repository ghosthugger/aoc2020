import math
import re
import sys
from collections import defaultdict
import copy
from collections import defaultdict

def set_bit(v, index, x):
    """Set the index:th bit of v to 1 if x is truthy, else to 0, and return the new value."""
    mask = 1 << index   # Compute mask, an integer with just bit 'index' set.
    v &= ~mask          # Clear the bit indicated by the mask (if x is False)
    if x:
        v |= mask         # If x was True, set the bit indicated by the mask.
    return v            # Return the result, we're done.

def main():

    with open('day14.txt') as f:
        lines = f.readlines()
        mask =""
        instr=[]
        for ls in lines:
            l=ls.strip()
            if(l[:4])=="mask":
                prts=l.split(" = ")
                mask=prts[1]
            else:
                prts=l.split(" = ")
                adr=int(prts[0][4:].rstrip("]"))
                val = int(prts[1])
                instr.append((mask, adr, val))


    mem=defaultdict(int)
    for i in instr:
        temp = i[2]

        idx=35
        for b in i[0]:
            if b=="1":
                temp=set_bit(temp,idx,True)
            elif b=="0":
                temp=set_bit(temp,idx,False)
            idx-=1

        mem[i[1]] = temp

    acc=0
    for k in mem.keys():
        acc+=mem[k]
    print(acc)
if __name__ =="__main__":
    main()
