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

def apply(seats):
  res = copy.deepcopy(seats)

  for row in range(len(seats)):
    for col in range(len(seats[0])):
        if(seats[row][col] == "L") and \
          (not isOcc(seats, col-1, row-1)) and \
          (not isOcc(seats, col, row-1)) and \
          (not isOcc(seats, col+1, row-1)) and \
          (not isOcc(seats, col-1, row)) and \
          (not isOcc(seats, col+1, row)) and \
          (not isOcc(seats, col-1, row+1)) and \
          (not isOcc(seats, col, row+1)) and \
          (not isOcc(seats, col+1, row+1)):
            res[row][col] = "#"

    for col in range(len(seats[0])):
        if(seats[row][col] == "#"):
          occ=0
          if isOcc(seats, col-1, row-1):
            occ+=1

          if isOcc(seats, col, row-1):
            occ +=1

          if isOcc(seats, col+1, row-1):
            occ += 1
          if isOcc(seats, col-1, row):
            occ +=1
          if isOcc(seats, col+1, row):
            occ += 1
          if isOcc(seats, col-1, row+1):
            occ+=1
          if isOcc(seats, col, row+1):
            occ+=1
          if isOcc(seats, col+1, row+1):
            occ+=1
          if(occ>3):
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

