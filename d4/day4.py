import fileinput

DATA = []
DIRS = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]                                                                                                      #DIRECTIONS


def READ_DATA():
    for line in fileinput.input("input.txt"):
        line.strip()
        DATA.append(line)

        
def PART_ONE():
    COUNT = 0
    for y in range(len(DATA)):
        for x in range(len(DATA)):
            for dy,dx in DIRS:
                if 0 <= y + 3*dy < len(DATA) and 0 <= x + 3*dx < len(DATA):                                                                                         #CHECK BOUNDS
                     if DATA[y][x] == "X" and DATA[y + dy][x + dx] == "M" and DATA[y + 2 * dy][x + 2 * dx] == "A" and DATA[y + 3 * dy][x + 3 * dx] == "S":          #FIND XMAS
                         COUNT+=1
    
    return COUNT


def PART_TWO():
    COUNT = 0
    for y in range(len(DATA)):
        for x in range(len(DATA)):
            if DATA[y][x] == "M":                                                                                                                                   #FIND M
                if y + 2 < len(DATA) and x + 2 < len(DATA[0]):                                                                                                      #CHECK BOUNDS
                    if DATA[y+1][x+1] == "A" and DATA[y+2][x+2] == "S":                                                                                             #CHECK IF FIRST DIAG IS MAS
                        if (DATA[y+2][x] == "M" and DATA[y][x+2] == "S") or (DATA[y+2][x] == "S" and DATA[y][x+2] == "M"):                                          #CHECK OTHER DIAGS FOR MAS OR SAM
                            COUNT +=1
                            
            if DATA[y][x] == "S":                                                                                                                                   #FIND S
                if y + 2 < len(DATA) and x + 2 < len(DATA[0]):                                                                                                      #CHECK BOUNDS
                    if DATA[y+1][x+1] == "A" and DATA[y+2][x+2] == "M":                                                                                             #CHECK IF FIRST DIAG IS SAM
                        if (DATA[y+2][x] == "S" and DATA[y][x+2] == "M") or (DATA[y+2][x] == "M" and DATA[y][x+2] == "S"):                                          #CHECK OTHER DIAGS FOR SAM OR MAS
                            COUNT +=1
    
    return COUNT
    
    
if __name__ == "__main__":
    READ_DATA()
    print(PART_ONE())
    print(PART_TWO())