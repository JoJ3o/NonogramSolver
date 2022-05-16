size = 5
clues = {"xAxis": {0 : [1], 1: [2, 2], 2: [2, 2], 3: [1], 4: [1]}, "yAxis": {0: [3], 1: [2], 2: [1], 3: [2], 4: [2, 1]}}
map = []
for x in range(size):
	map.append([])
	for y in range(size):
		map[x].append(0)

# for x in range(size):
#     columnInput = input("X" + str(x + 1) + ": ").split(" ")
#     columnItems = [int(i) for i in columnInput]
#     map["xAxis"].append(columnItems)

# for y in range(size):
#     rowInput = input("Y" + str(y + 1) + ": ").split(" ")
#     rowItems = [int(i) for i in rowInput]
#     map["yAxis"].append(rowItems)

def placeGuarantee(axis, index, clue):
	seperators = [idx * 2 + num for idx, num in enumerate(clue[:-1])]
	for i in range(size):
		cellType = 1 if (not (i in seperators)) else 2
		if axis == "xAxis":
			map[i][index] = cellType
		elif axis == "yAxis":
			map[index][i] = cellType
	clues[axis][index] = [-(num) for num in clues[axis][index]]

def placeOverlap(axis, index, clue):
	pos = size - max(clue)
	overlap = int((max(clue) - size/2) * 2)
	for i in range(overlap):
		if axis == "xAxis":
			map[pos + i][index] = 1
		elif axis == "yAxis":
			map[index][pos + i] = 1

def placeEdge(axis, index, clue):
	if axis == "xAxis":
		for cellIdx in range(size):
			if map[cellIdx][index] == 1:
				if cellIdx == 0:
					for i in range(clue[0]):
						map[i][index] = 1
					map[clue[0]][index] = 2
				elif cellIdx == size - 1:
					for i in range(clue[-1]):
						map[-(i+1)][index] = 1
					map[-(clue[-1] + 1)][index] = 2
	elif axis == "yAxis":
		for idx, cell in enumerate(map[index]):
			if cell == 1:
				if idx == 0:
					for i in range(clue[0]):
						map[index][i] = 1
					map[index][clue[0]] = 2
				elif idx == size - 1:
					for i in range(clue[-1]):
						map[index][-(i+1)] = 1
					map[index][-(clue[-1] + 1)] = 2

def getBlocks(line):
	leftBounds = [idx for idx, num in enumerate(line) if num == 1 and (idx == 0 or line[idx - 1] != 1)]
	rightBounds = [idx for idx, num in enumerate(line) if num == 1 and (idx == len(line) - 1 or line[idx + 1] != 1)]
	blocks = [(left, (right - left) + 1) for left, right in zip(leftBounds, rightBounds)]
	return blocks

def getRegions(line):
	leftBounds = [idx for idx, num in enumerate(line) if idx == 0 or line[idx - 1] == 2]
	rightBounds = [idx for idx, num in enumerate(line) if idx == len(line) - 1 or line[idx + 1] == 2]
	regions = [(left, (right - left) + 1) for left, right in zip(leftBounds, rightBounds)]
	return regions

# def completeClue(axis, index, clue):
# 	if axis == "yAxis":
# 		blocks = getBlocks(map[index])
# 		regions = getRegions(map[index])
# 		regionsBeforeBlock = 
# 		if clue[0] == blocks[0][1] and (regions[0])


def printMap(axis, index, clue):
	print("\n")
	print(axis + ":", index + 1, clue)
	for y in map:
		print(y)

for axisName, axisClues in clues.items():
	for index, clue in axisClues.items():
		if sum(clue) + (len(clue) - 1) == size:
			placeGuarantee(axisName, index, clue)
		elif max(clue) > size/2:
			placeOverlap(axisName, index, clue)
		printMap(axisName, index, clue)

while any([not all(row) for row in map]):
	oldMap = map

	for axisName, axisClues in clues.items():
		for index, clue in axisClues.items():
			if all(True if num < 0 else False for num in clue):
				continue
			completeClue(axisName, index, clue)
			# placeEdge(axisName, index, clue)
			printMap(axisName, index, clue)

	if map == oldMap:
		print("Error: looploop")
		break
