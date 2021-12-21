import math
import re

def read():
    with open('day4.txt') as f:
        lines = f.readlines()

    res=[]
    passport = {}
    i = 0
    for l in lines:
        i=i+1
        print(i)
        if(len(l.strip())==0):
            if(not passport):
                assert(False)

            res.append(passport)
            passport = {}
            continue
        parts = l.strip().split(" ")
        for p in parts:
            print(p)
            k, v = p.split(":")
            passport[k] = v

    return res

def valid(p):
    present = "byr" in p and "iyr" in p and "eyr" in p and "hgt" in p \
           and "hcl" in p and "ecl" in p and "pid" in p

    byr = False
    if "byr" in p:
        byr = len(p["byr"]) == 4 and (int(p["byr"]) >=1920) and (int(p["byr"]) <=2002)

    iyr = False
    if "iyr" in p:
        iyr = len(p["iyr"]) == 4 and (int(p["iyr"]) >=2010) and (int(p["iyr"]) <=2020)

    eyr = False
    if "eyr" in p:
        eyr = len(p["eyr"]) == 4 and (int(p["eyr"]) >=2020) and (int(p["eyr"]) <=2030)

    hgt = False
    if "hgt" in p:
        if(p["hgt"][-2:]=="cm"):
            hgt = (int(p["hgt"][:-2])>=150) and (int(p["hgt"][:-2])<=193)
        elif(p["hgt"][-2:]=="in"):
            hgt = (int(p["hgt"][:-2])>=59) and (int(p["hgt"][:-2])<=76)

    hcl = False
    if "hcl" in p:
        hcl = (re.match("^#[0-9a-z][0-9a-z][0-9a-z][0-9a-z][0-9a-z][0-9a-z]$", p["hcl"]) is not None)

    ecl = False
    if "ecl" in p:
        ecl = (re.match("amb|blu|brn|gry|grn|hzl|oth", p["ecl"]) is not None)

    pid = False
    if "pid" in p:
        pid = (re.match("^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]$", p["pid"]) is not None)

    return present and byr and iyr and eyr and hgt and hcl and ecl and pid


def replace(s, position, character):
    return s[:position] + character + s[position+1:]

def main():
    pps = read()


    total = 0
    count = 0
    print(pps)
    for p in pps:
        print(p)
        print(":")
        print(valid(p))
        if(valid(p)):
            count = count +1
        total = total +1
    print(count)

    print(total)

if __name__ =="__main__":
    main()

