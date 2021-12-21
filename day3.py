import math

def read():

    groups = []
    group = {}
    with open('day3-test.txt') as f:
        lines = f.readlines()

    res=[]
    for l in lines:
        if(len(l.strip())==0):
            groups.append(group)
            group = {}

            continue
        parts = l.strip().split(" ")
        for p in parts:
            print(p)
            k, v = p.split(":")
            passport[k] = v

    return res

def replace(s, position, character):
    return s[:position] + character + s[position+1:]
def main():
    inp = read()
    mul=[]
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    for step_right, step_down in slopes:
        height= len(inp)
        x=0
        y=0
        t=0
        while y<height-1:
            x=x+step_right
            y=y+step_down
            p=inp[y]
            width=len(p)

            res = p
            res = replace(res, x, "O")
            x = x % (width)
            if p[x]=="#":
                t=t+1
                res = replace(res, x, "X")

#            print(res)

        print(t)
        mul.append(t)

    final_res = 1
    for m in mul:
        final_res=final_res*m
    print(final_res)


if __name__ =="__main__":
    main()

