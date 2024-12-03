import re


DATA = ""

def READ_FILE():
    with open("input.txt","r") as f:
        DATA = f.read()
    return DATA

def FIND_MUL():
    LIST = re.findall("mul\(\d{1,3},\d{1,3}\)",DATA)
    return LIST

def MUL_LIST(NUMS):
    ANS = []
    for OPER in NUMS:
        VALUES = re.findall("\d{1,3}",OPER)
        x = int(VALUES[0])
        y = int(VALUES[1])
        ANS.append(x * y)
    return ANS

def PART_ONE(NUMS):
    return sum(NUMS)

def PART_TWO():
    LIST = re.findall("do\(\)|mul\(\d{1,3},\d{1,3}\)|don't\(\)",DATA)
    ANS = []
    CHECK = True
    for OPER in LIST:
        if OPER == "do()":
            CHECK = True
        
        if OPER == "don't()":
            CHECK = False
        
        if bool(re.match("mul\(\d{1,3},\d{1,3}\)",OPER)):
            VALUES = re.findall("\d{1,3}",OPER)
            x = int(VALUES[0])
            y = int(VALUES[1])
            if CHECK == True:
                ANS.append(x*y)
                
    return sum(ANS)

    
    



if __name__ == "__main__":
    DATA = READ_FILE()
    NUMS = FIND_MUL()
    print(PART_ONE(MUL_LIST(NUMS)))
    print(PART_TWO())