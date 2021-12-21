import re
min, max, letter, pw = re.split("[- :]+", line)


row = seatbsp[:7]
seat = seatbsp[7:]

row_range=(0,127)
for r in row:
    if(r=="F"):
        row_range=(row_range[0], math.floor((row_range[1]-row_range[0])/2) + row_range[0])
    if(r=="B"):
        row_range=(math.ceil((row_range[1]-row_range[0])/2) + row_range[0], row_range[1])

