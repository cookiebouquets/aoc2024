import math
import fileinput


DATA = []
FILE_NAME = "input.txt"


def LOAD_DATA():
    for line in fileinput.input(FILE_NAME):
        line = line.split().strip()
        DATA.append(list(map(int,line)))


    
def CHECK_SAFETY(LEVEL):
    return all(0 < LEVEL[i+1] - LEVEL[i] <= 3 for i in range(len(LEVEL) - 1)) or all(-3 <= LEVEL[i + 1] - LEVEL[i] < 0 for i in range(len(LEVEL) - 1)) 

def COUNT_SAFETY():
    COUNT = 0
    for LEVEL in DATA:
        if CHECK_SAFETY(LEVEL):
            COUNT+=1
    return COUNT

def DAMPENED_SAFETY():
    COUNT = 0
    for LEVEL in DATA:
        for i in range(len(LEVEL)):
            MOD_LEVEL = LEVEL[:i] + LEVEL[i+1:]
            if CHECK_SAFETY(MOD_LEVEL):
                COUNT +=1
                break

    return COUNT

if __name__ == "__main__":
    LOAD_DATA()
    print(COUNT_SAFETY())
    print(DAMPENED_SAFETY())
 
