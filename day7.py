import math
import re
import sys



def tree(bag_types, bag):
    if (not bag in bag_types):
        return set([bag])

    res = []
    for b in bag_types[bag]:
        res.append(tree(bag_types, b))

    return set([bag]).union(*res)




total_bags = 0

def main():
    global total_bags

    bag_types = {}
    bag_counts = {}

    with open('day7.txt') as f:
        lines = f.readlines()
        for l in lines:
            t1 = l.strip().split(" bags contain ")
            bag = t1[0]

            if("," in t1[1][:-1]):
                content = t1[1][:-1].split(", ")
            else:
                if("no other" in t1[1][:-1]):
                    content = ["0 None"]
                else:
                    content = [t1[1][:-1]]

            content_types = [c[2:].replace("bags", "bag").replace(" bag", "") for c in content]
            content_counts = [(int(c[:1]), c[2:].replace("bags", "bag").replace(" bag", "")) for c in content]

            for b in content_types:
                if b in bag_types:
                    bag_types[b].append(bag)
                else:
                    bag_types[b] = [bag]


            bag_counts[bag] = content_counts




#    print(bag_types)

#    all = tree(bag_types, "shiny gold")
##    print (all)
#    print(len(all)-1)


    def tree2(bag_counts, bag):
        if (not bag in bag_counts):
            return 1

        res = []
        for b in bag_counts[bag]:
#            we = 0
#            if b[1] in bag_counts:
#                for b2 in bag_counts[b[1]]:
#                    we = we + int(b2[0])

            we = b[0]
            res.append(we * tree2(bag_counts, b[1]))

        return sum(res) + 1


    print(bag_counts)
    all2 = tree2(bag_counts, "shiny gold")
    print(all2-1)

if __name__ =="__main__":
    main()

