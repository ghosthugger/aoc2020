import math
import re
import sys
from collections import defaultdict
import copy

def main():

    with open('day20.txt') as f:
        lines = f.readlines()
        mode=0
        tiles={}
        for ls in lines:
            l=ls.strip()
            if l=="":
                continue

            if mode==0:
                title=l.split(" ")[1].strip(":")
                mode=1
                rows=[]
            else:
                rows.append(l)
                if len(rows) == 10:
                    mode=0
                    tiles[int(title)]=rows

    print(len(rows))
    print(tiles)

    borders={}
    for t in tiles.keys():
        rows=tiles[t]
        top=rows[0]
        bottom=rows[9]
        right=""
        left=""
        for r in rows:
            right=right+r[-1]
            left=left+r[0]
        borders[t]=[top,right,bottom,left]

    def rotate(borders):
        top=borders[3][::-1]
        right=borders[0]
        bottom=borders[1][::-1]
        left=borders[2]
        return [top,right,bottom,left]

    all_edges=defaultdict(list)
    for t in borders.keys():
        cur_rot=borders[t]
        for rot in range(3):
            for e in cur_rot:
                all_edges[e].append(t)
            cur_rot=rotate(cur_rot)

    print("all_edges")
    print(all_edges)

    res=defaultdict(list)
    for k in all_edges.keys():
        tile_ids=all_edges[k]
        if(len(tile_ids) == 1):
            res[tile_ids[0]].append(1)

    print("tile to free edges")
    print(res)

    a=1
    corners=[]
    for r in res:
        if len(res[r])==2:
            a*=r
            corners.append(r)
    print(a)
    print(corners)

    c=corners[0]

    while True:
        right_edge_left_tile=borders[c][1]
        right_tile=all_edges[right_edge_left_tile]


if __name__ =="__main__":
    main()
