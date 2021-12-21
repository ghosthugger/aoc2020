import math
import re
import sys
from collections import defaultdict
import copy


def main():

    with open('day13.txt') as f:
        lines = f.readlines()

        earliest, busses = [ls.strip() for ls in lines]

    busses = busses.split(",")

    times = [int(b) for b in busses if not b =="x"]

    mods = [(divmod(int(earliest),t), t) for t in times]

    min_dep = min(mods, key=lambda e: (e[0][0]+1)*e[1])

    busid=min_dep[1]
    dep = (min_dep[0][0]+1)*min_dep[1]

    print(busid*(dep-int(earliest)))


    for i in range(1000000):
        for b in busses:
            times = [(int(b)*i, int(b)) for b in busses if not b =="x"]
            cand=[]
            for t in times:
                if t[0]>=int(earliest):
                    cand.append(t)

            if len(cand) > 0:
                depart = min(cand, key=lambda e: e[0])

                print((depart[0]-int(earliest))*depart[1])
                break

if __name__ =="__main__":
    main()

#max(players, key=lambda p: p.totalScore)




    print((1068781)%13)

    mults = [0 for d in deps]
    facts = [d[0] for d in deps]
    facts.sort()

    def incr():
        i=0
        if (facts[i]*(mults[i]+1)) > facts[i+1]:
            mults[i+1] = mults[i+1] + 1
            mults[i] = 0
            i+=1
            while (i<len(facts)-1) and (facts[i]*(mults[i])) > facts[i+1]:
                mults[i+1] = mults[i+1] + 1
                mults[i] = 0
                i+=1
        else:
            mults[i]=mults[i]+1

    #    facts=[7,19,31]
    #    mults=[0,0,0]
    #    while True:
    #        incr()
    #        print(mults)
    #        print(sum([m*f for (m,f) in zip(mults,facts)]))

    #    while True:
    #        for i in range(mults):
    #            while sum([m*f for (m,f) in zip(mults,facts)]) <= upperb:
    #                t = sum([m*f for (m,f) in zip(mults,facts)])
    #                if(test(t)):
    #                    print("found")
    #                    print(t)
    #                    break
    #                mults[i]+=1
    #            mults[i]=0

    print("upper")
    print(upperb)
    t=1068773
