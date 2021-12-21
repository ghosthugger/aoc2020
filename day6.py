import math
import re
import sys

def read():
    with open('day6.txt') as f:
        lines = f.readlines()

    groups = []
    group = []
    for l in lines:
        if(len(l.strip())==0):
            u = set.intersection(*group)
            groups.append(u)
            group = []
            continue

        group.append(set([p for p in l.strip()]))

    return groups

def main():
    inp_list = read()

    print(sum([len(g) for g in inp_list]))


#    print(sum(len(reduce(lambda s1, s2: s1 & s2, map(set, group.strip().split('\n')))) for group in open('input.txt').read().split('\n\n')))
#    print(sum(len(set.intersection(*map(lambda x:set(x),g.strip().split('\n')))) for g in sys.stdin.read().split('\n\n')))
#    print(sum(len(set.intersection(*map(set,g.strip().split('\n')))) for g in sys.stdin.read().split('\n\n')))
#    print(sum(len(set.intersection(*map(set,g.split()))) for g in sys.stdin.read().split('\n\n')))
if __name__ =="__main__":
    main()

