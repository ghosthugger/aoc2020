import math

def read():
    with open('day2.txt') as f:
        lines = f.readlines()
    res=[]
    for l in lines:
        parts = l.split()
        low,high=parts[0].split("-")
        char=parts[1].rstrip(":")
        pwd=parts[2]
        res.append([int(low), int(high), char, pwd])

    return res

def main():
    pwd = read()

    count = 0
    for p in pwd:
        low, high, char, pwd = p

        s = len(pwd.replace(char, ""))
        l = len(pwd) - len(pwd.replace(char, ""))
        if(l>=low and l<=high):
            count=count+1

    print(count)

    pwd = read()

    count=0
    for p in pwd:
        low, high, char, pwd = p

        if(low-1<=len(pwd) and high-1<=len(pwd)):
            if((pwd[low-1]==char) ^ (pwd[high-1]==char)):
                count=count+1

    print(count)
if __name__ =="__main__":
    main()

