import math
import re
import sys
from collections import defaultdict
import copy

def printseats(seats):
  for s in seats:
    print(s)

def countseats(seats):
  res=0
  for row in range(len(seats)):
    for col in range(len(seats[0])):
      if(seats[row][col] == "#"):
        res+=1

  return res

def isOcc(seats, x, y):
  if(x<0 or y<0 or y>=len(seats) or x>=len(seats[0])):
    return False

  return not ((seats[y][x]=="L") or (seats[y][x]=="."))

def isOccVis(seats, x, y, dx, dy):
  if(x+dx<0 or y+dy<0 or y+dy>=len(seats) or x+dx>=len(seats[0])):
    return False

  while not(x+dx<0 or y+dy<0 or y+dy>=len(seats) or x+dx>=len(seats[0])):
    x=x+dx
    y=y+dy
    if(seats[y][x]=="#"):
      return True
    if(seats[y][x]=="L"):
      return False

  return False

def apply(seats):
  res = copy.deepcopy(seats)

  for row in range(len(seats)):
    for col in range(len(seats[0])):
        if(seats[row][col] == "L") and \
          (not isOccVis(seats, col, row,-1,-1)) and \
          (not isOccVis(seats, col, row,0,-1)) and \
          (not isOccVis(seats, col, row,1,-1)) and \
          (not isOccVis(seats, col, row,-1,0)) and \
          (not isOccVis(seats, col, row,1,0)) and \
          (not isOccVis(seats, col, row,-1,1)) and \
          (not isOccVis(seats, col, row,0,1)) and \
          (not isOccVis(seats, col, row,1,1)):
            res[row][col] = "#"

    for col in range(len(seats[0])):
        if(seats[row][col] == "#"):
          occ=0
          if isOccVis(seats, col, row, -1, -1):
            occ+=1

          if isOccVis(seats, col, row, 0, -1):
            occ +=1

          if isOccVis(seats, col, row, 1, -1):
            occ += 1
          if isOccVis(seats, col, row, -1,0):
            occ +=1
          if isOccVis(seats, col, row, 1, 0):
            occ += 1
          if isOccVis(seats, col, row, -1, 1):
            occ+=1
          if isOccVis(seats, col, row, 0, 1):
            occ+=1
          if isOccVis(seats, col, row, 1, 1):
            occ+=1
          if(occ>4):
            res[row][col] = "L"


  return res


def main():
    seats = []
    print("starts")
    with open('day11.txt') as f:
        lines = f.readlines()
        print("read")
        for ls in lines:
            l = ls.strip()
            row = []
            for c in l:
              row.append(c)

            seats.append(row)


    printseats(seats)

    print("new")
    printseats(seats)
    seats2= apply(seats)
    print("new2")
    printseats(seats2)
    seats3= apply(seats2)
    print("new3")
    printseats(seats3)

    while True:
      seats=apply(seats)
      print(countseats(seats))

if __name__ =="__main__":
    main()

