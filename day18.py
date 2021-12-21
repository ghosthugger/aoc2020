import math
import re
import sys
from collections import defaultdict
import copy




def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def charposition(string, char):
    pos = [] #list to store positions for each 'char' in 'string'
    for n in range(len(string)):
        if string[n] == char:
            pos.append(n)
    return pos


def main():

    def evalit(ex):
        ex=ex.replace(" ", "")
        i=0

        def evalit3():
            nonlocal i
            next=None
            lhs=0
            while i<len(ex):
                curr=ex[i]
                if len(ex)>i+1:
                    next=ex[i+1]
                if next==None and RepresentsInt(ex[i]):
                    return int(ex[i])
                elif RepresentsInt(ex[i]):
                    j=i
                    while j<len(ex) and RepresentsInt(ex[j]):
                        j+=1
                    lhs=int(ex[i:j])
                    i+=j-i
                elif ex[i]=="(":
                    i+=1
                    lhs=evalit3()
                elif ex[i]==")":
                    i+=1
                    return lhs
                elif ex[i]=="+":
                    i+=1
                    if ex[i]=="(":
                        i+=1
                        lhs=lhs+evalit3()
                    else:
                        j=i
                        while j<len(ex) and RepresentsInt(ex[j]):
                            j+=1
                        tmp=int(ex[i:j])
                        i+=j-i

                        lhs=lhs+int(tmp)
                elif ex[i]=="*":
                    i+=1
                    if ex[i]=="(":
                        i+=1
                        lhs=lhs*evalit3()
                    else:
                        j=i
                        while j<len(ex) and RepresentsInt(ex[j]):
                            j+=1
                        tmp=int(ex[i:j])
                        i+=j-i

                        lhs=lhs*int(tmp)
                        i+=1
            #                print(lhs)

            print(str(lhs))
            return lhs
        return(evalit3())

    def evalitNew(ex):
        ex=ex.replace(" ", "")
        i=0

        def evalit4():
            nonlocal i
            next=None
            lhs=""
            while i<len(ex):
                curr=ex[i]
                if len(ex)>i+1:
                    next=ex[i+1]
                if next==None and RepresentsInt(ex[i]):
                    return int(ex[i])
                elif RepresentsInt(ex[i]):
                    lhs=ex[i]
                    i+=1
                elif ex[i]=="(":

                    i+=1
                    lhs+="("+evalit4()
                elif ex[i]==")":

                    i+=1
                    lhs+=")"
                    return lhs
                elif ex[i]=="+":

                    i+=1
                    if ex[i]=="(":

                        i+=1
                        lhs="("+lhs+"+("+evalit4()+")"
                    else:
#                        res+="("+str(lhs)+"+"+ex[i]+")"

                        lhs="("+lhs+ "+" +ex[i]+")"
                        i+=1
                elif ex[i]=="*":

                    i+=1
                    if ex[i]=="(":

                        i+=1
                        lhs=lhs+"*("+evalit4()+")"
                    else:
                        lhs=lhs+"*"+ex[i]

                        i+=1
            #                print(lhs)

            return lhs

        value = evalit4()
        print(value)
        return(evalit(value))

    def findParLeft(str,i):
        level=1
        i-=1
        while level>0:
            if str[i]==")":
                level+=1
            if str[i]=="(":
                level-=1
            i-=1
        return i+1
    def findParRight(str,i):
        level=1
        i+=1
        while level>0:
            if str[i]=="(":
                level+=1
            if str[i]==")":
                level-=1
            i+=1
        return i-1

    def evalitLast(str):
        str=str.replace("(","")
        str=str.replace(")","")

        i=0
        prod=1
        while i<len(str):
            j=i
            while j<len(str) and RepresentsInt(str[j]):
                j+=1
            lhs=int(str[i:j])
            i+=j-i
            prod*=lhs
            i+=1

        return prod


    def repl(ex):
        ex=ex.replace(" ","")


        poses = charposition(ex,"+")
        while len(poses)>0:
            i=poses[0]
            if RepresentsInt(ex[i-1]):
                j=i-1
                while j>=0 and RepresentsInt(ex[j]):
                    j-=1
                left=j+1
                lvalue=evalit(ex[left:i])
            else:
                leftPar= findParLeft(ex,i-1)
                parex=repl(ex[leftPar+1:i-1])
                lvalue=evalitLast(parex)
                left=leftPar

            if RepresentsInt(ex[i+1]):
                j=i+1
                while j<len(ex) and RepresentsInt(ex[j]):
                    j+=1
                right=j-1
                rvalue=evalit(ex[i+1:right+1])
            else:
                rightPar= findParRight(ex,i+1)
                parex=repl(ex[i+1:rightPar+1])
                rvalue=evalitLast(parex)
                right=rightPar


            value=lvalue+rvalue
            ex=ex[:left]+str(value)+ex[right+1:]
            poses = charposition(ex,"+")
        return ex


    inp="5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
    tmp=repl(inp)
    print(evalitLast(tmp))


 #   print(evalit(inp))
 #   print("inp: "+inp)
 #   tmp=repl(inp)
 #   print("tmp: "+tmp)
 #   print(evalit(tmp))



    with open('day18.txt') as f:
        lines = f.readlines()

        s=0
        for ls in lines:
            l=ls.strip()
            s=s+evalitLast(repl(l))

        print(s)


if __name__ =="__main__":
    main()
