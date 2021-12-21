import math
import re
import sys
from collections import defaultdict
import copy

def main():

    with open('day20-test.txt') as f:
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

    def flip(borders):
        top=borders[2]
        right=borders[1][::-1]
        bottom=borders[0]
        left=borders[3][::-1]
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

    def match_rot(left_tile, right_tile):
        rot=0
        while right_tile[3]!=left_tile[1] and rot<4:
            right_tile=rotate(right_tile)
            rot+=1
        return rot!=4, rot

    def match_rot_col(top_tile, bottom_tile):
        rot=0
        while bottom_tile[0]!=top_tile[2] and rot<4:
            bottom_tile=rotate(bottom_tile)
            rot+=1
        return rot!=4, rot


    def puzzle_row(c):
        pussle_ok=True
        cur_tile=borders[c]
        cur_id=c
        puzz=[(cur_id,0,False)]
        while pussle_ok and len(puzz)<3:
            right_edge_left_tile=cur_tile[1]
            left_tile=cur_tile
            right_tiles=all_edges[right_edge_left_tile]

            set_edges=set(right_tiles)
            set_edges.remove(cur_id)
            set_edges.difference_update(set([p[0] for p in puzz]))
            if (len(set_edges)==1):
                cur_id=next(iter(set_edges))
                cur_tile=borders[cur_id]
                mf=False
                m, rot = match_rot(left_tile, cur_tile)

                if not m:
                    cur_tile=flip(cur_tile)
                    mf, rot = match_rot(left_tile, cur_tile)

                if not m and not mf:
                    pussle_ok=False
                else:
                    puzz.append((cur_id,rot,mf))
            else:
                pussle_ok=False

        if not pussle_ok:
            print("no fit")
        else:
            print("FIT!!!!")
        return puzz

    def puzzle_col(c):
        pussle_ok=True
        cur_tile=borders[c]
        cur_id=c
        puzz=[(cur_id,0,False)]
        while pussle_ok and len(puzz)<3:
            bottom_edge_top_tile=cur_tile[2]
            top_tile=cur_tile
            bottom_tiles=all_edges[bottom_edge_top_tile]

            set_edges=set(bottom_tiles)
            set_edges.remove(cur_id)
            set_edges.difference_update(set([p[0] for p in puzz]))
            if (len(set_edges)==1):
                cur_id=next(iter(set_edges))
                cur_tile=borders[cur_id]
                mf=False
                m, rot = match_rot_col(top_tile, cur_tile)

                if not m:
                    cur_tile=flip(cur_tile)
                    mf, rot = match_rot_col(top_tile, cur_tile)

                if not m and not mf:
                    pussle_ok=False
                else:
                    puzz.append((cur_id,rot,mf))
            else:
                pussle_ok=False

        if not pussle_ok:
            print("no fit")
        else:
            print("FIT!!!!")
        return puzz

    c=1951
    col=puzzle_col(c)
    for c in col:
        print(puzzle_row(c[0]))



if __name__ =="__main__":
    main()
