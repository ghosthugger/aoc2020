import math
import re
import sys
from collections import defaultdict

def runit(prog):
    acc = 0
    pc = 0
    second = defaultdict(int)

    while pc < len(prog):
        second[pc] = second[pc] +1
        if(second[pc] == 2):
#            print(acc)
            return False

        (instr, para) = prog[pc]
        if(instr=="nop"):
            pc=pc+1
        if(instr=="jmp"):
            pc=pc+para
        if(instr=="acc"):
            pc=pc+1
            acc=acc+para

    print(acc)
    return True

def main():

    acc = 0
    prog = []
    pc = 0


    with open('day8.txt') as f:
        lines = f.readlines()
        for l in lines:
            (instr, para) = l.strip().split(" ")
            prog.append((instr, int(para)))

    for i in range(len(prog)):
        perm = prog[:]
        (instr, para) = perm[i]
        if(instr=="nop"):
            instr="jmp"
        if(instr=="jmp"):
            instr = "nop"
        if(instr=="acc"):
            pass
        perm[i] = (instr,para)
        r = runit(perm)
        if(r):
            print(i)







if __name__ =="__main__":
    main()

