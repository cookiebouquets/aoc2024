import fileinput
import math

LIST_ONE = []
LIST_TWO = []

COUNT = 0 

FILE_NAME = "input.txt"

def readfile():
	global COUNT
	for line in fileinput.input(FILE_NAME):
		line = line.split("   ")
		LIST_ONE.append(int(line[0]))
		LIST_TWO.append(int(line[1]))
		COUNT +=1

def sortlists():
	LIST_ONE.sort()
	LIST_TWO.sort()

def calcdistance():
	DISTANCE = []
	for i in range(COUNT):
		DISTANCE.append(abs(LIST_ONE[i] - LIST_TWO[i]))

	TOTAL_DISTANCE = 0

	for item in DISTANCE:
		TOTAL_DISTANCE +=item
	return TOTAL_DISTANCE

def similarity():
	LIST_THREE = []
	for item in LIST_ONE:
		SIMILARITY = 0
		for value in LIST_TWO:
			if item == value:
				SIMILARITY +=1
		SIMILARITY = item*SIMILARITY
		LIST_THREE.append(SIMILARITY)

	TOTAL_SIMILARITY = 0
	for item in LIST_THREE:
		TOTAL_SIMILARITY+=item
	return TOTAL_SIMILARITY

if __name__ == "__main__":
	readfile()
	sortlists()
	print(calcdistance())
	print(similarity())
