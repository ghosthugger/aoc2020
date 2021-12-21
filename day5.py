import math
import re

def read():
    with open('day5.txt') as f:
        lines = f.readlines()

    res=[]
    for l in lines:
        res.append(l.strip())
    return res

def replace_char(s, position, character):
    return s[:position] + character + s[position+1:]

def main():
    inp_list = read()

    t="FBFBBFFRLR"
    t=t.replace("F", "0")
    t=t.replace("B", "1")
    t=t.replace("L", "0")
    t=t.replace("R", "1")

    true_t = int(t,2)

    allseats=[]
    maxid = 0
    for seatbsp in inp_list:

        row = seatbsp[:7]
        seat = seatbsp[7:]

        row_range=(0,1023)
        for r in seatbsp:
            if(r=="F" or r=="L"):
                row_range=(row_range[0], math.floor((row_range[1]-row_range[0])/2) + row_range[0])
            if(r=="B" or r=="R"):
                row_range=(math.ceil((row_range[1]-row_range[0])/2) + row_range[0], row_range[1])

        if(maxid<row_range[0]):
            maxid=row_range[0]

        allseats.append(row_range[0])

    print(maxid)
    allseats.sort()
    print(allseats)

    prev_seat=89
    for s in allseats:
        if(s-prev_seat>1):
            print(s)
        prev_seat=s

if __name__ =="__main__":
    main()

