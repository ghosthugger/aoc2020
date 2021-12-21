import math
import re
import sys
from collections import defaultdict
import copy
from functools import reduce

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def gcd(p,q):
    # Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p%q
    return p

def is_coprime(x, y):
    return gcd(x, y) == 1

def phi_func(x):
    if x == 1:
        return 1
    else:
        n = [y for y in range(1,x) if is_coprime(x,y)]
        return len(n)

def main():

    with open('day13.txt') as f:
        lines = f.readlines()

        earliest, busses = [ls.strip() for ls in lines]

    busses = busses.split(",")

    deps = [(int(b), busses.index(b)) for b in busses if not b =="x"]


    #chinese remainders theorem

#    deps = [(17,0),(13,2),(19,3)]
    last = deps[-1]

    N=1
    for d in deps:
        N*=d[0]

    a=[]
    n=[]
    for d in deps:
        a.append(d[1])
        n.append(d[0])

    rem = chinese_remainder(n,a)
    rem = N-rem
    def test(t):
        suc=False
        for d in deps:
            if not((t+d[1])%d[0]==0):
                break
            if d==last:
                suc=True
        return suc

    print("going down")
    while rem>0:
        if test(rem):
            print("found one")
            print(rem)
        rem-=N
    print("going up")
    while rem<1000000000000000:
        if test(rem):
            print("found one")
            print(rem)
        rem+=N



    print(rem)


    acc_sum=0

    for d in deps:
        phi = phi_func(d[0])
        b=(N/d[0])
        for i in range(phi-2):
            b*=b
        acc_sum+=(d[1]*(b%d[0]))

    print(acc_sum)


    first = deps[0]
    deps = deps[1:]
    deps.sort(key=lambda k: -k[0])
    last = deps[-1]
    t=100148433924374-first[0]
    suc=False

    while not (t%first[0] == 0):
        t+=1

    pr=t
    while not suc:
        if(pr+10000000 < t):
            print(t)
            pr=t

        t+=first[0]

        for d in deps:
            if not((t+d[1])%d[0]==0):
                break
            if d==last:
                suc=True


    print(t)

#     def test(time):
#         for d in deps:
#             if not ((time+d[1])%d[0] ==0):
#                 break
#         if deps.index(d) == len(deps)-1:
#             return True
#         return False
#
#
#     upperb = 1
#     for p in deps:
#         upperb*=p[0]
#
#     tot = 100000000000000
#     t=tot
#     while not t%19 == 0:
#         t+=1
#     pr = t
#     while(not test(t)):
#         if(pr+10000000 < t):
#             print(t)
#             pr=t
#
#         min_step = max([(643-((t+19)%643)),
#                        (41-((t+9)%41)),
#                         (17-((t+36)%17)),
#                         (13-((t+37)%13)),
#                         (23-((t+42)%23)),
#                         (37-((t+56)%37)),
#                         (29-((t+79)%29)),
#                         (509-((t+50)%509))])
#         t+=min_step
#         while not t%19 == 0:
#             t+=1
# #        t = sum([m*f for (m,f) in zip(mults,facts)])
# #        mults=incr()
#
#     print(t)

if __name__ =="__main__":
    main()

#max(players, key=lambda p: p.totalScore)