import re

def main():

    rules = {}
    rl=[i for i in open('day19.txt').readlines() if ":" in i]
    messages=[i for i in open('day19.txt').readlines() if not ":" in i]
    ir=[i.strip().replace("\"","").split(": ") for i in rl]
    rules.update([(k,v.split(" ")) for (k,v) in ir])
    def cre(key):
        r=rules[key]
        rec=lambda c: cre(c) if c in rules else c
        res="".join([rec(c) for c in r])
        if not ("a" in r or "b" in r):
            res="("+res+")"
        return res
    r="^"+cre("0")+"$"
    print(len([m for m in messages if re.match(r, m) is not None]))

if __name__ =="__main__":
    main()
