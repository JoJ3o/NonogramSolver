size = 5
clues = {"xAxis": {0 : [1], 1: [1], 2: [3], 3: [2, 1], 4: [1, 2]}, "yAxis": {0: [1, 3], 1: [2], 2: [3], 3: [2], 4: [2, 1]}}

# for x in range(size):
#     columnInput = input("X" + str(x + 1) + ": ").split(" ")
#     columnItems = [int(i) for i in columnInput]
#     map["xAxis"].append(columnItems)

# for y in range(size):
#     rowInput = input("Y" + str(y + 1) + ": ").split(" ")
#     rowItems = [int(i) for i in rowInput]
#     map["yAxis"].append(rowItems)

def genMap(size):
	map = []
	for x in range(size):
		map.append([])
		for y in range(size):
			map[x].append(0)
	return map

map = genMap(size)

def isGuarantee(clue):
	clueSum = sum(clue) + (len(clue) - 1)
	if clueSum == size:
		return True
	return False

def placeGuarantee(axis, index, clue):
	seperators = [idx * 2 + num for idx, num in enumerate(clue[:-1])]
	for i in range(size):
		cellType = 1 if (not (i in seperators)) else 2
		if axis == "xAxis":
			map[i][index] = cellType
		elif axis == "yAxis":
			map[index][i] = cellType
	clues[axis][index].clear()

def isOverlap(clue):
	if max(clue) > size/2:
		return True
	return False

def placeOverlap(axis, index, clue):
	pos = size - max(clue)
	overlap = int((max(clue) - size/2) * 2)
	for i in range(overlap):
		if axis == "xAxis":
			map[pos + i][index] = 1
		elif axis == "yAxis":
			map[index][pos + i] = 1

def isSide(axis, index, clue):
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

def printMap(axis, clue):
	print("\n")
	print(axis + ":", clue)
	for y in map:
		print(y)

for axisName, axisClues in clues.items():
	for index, clue in axisClues.items():
		if (isGuarantee(clue)):
			placeGuarantee(axisName, index, clue)
		elif (isOverlap(clue)):
			placeOverlap(axisName, index, clue)
		
		if not clue:
			continue
		isSide(axisName, index, clue)
		printMap(axisName, clue)

for axisName, axisClues in clues.items():
	for index, clue in axisClues.items():
		if not clue:
			continue
		isSide(axisName, index, clue)
		printMap(axisName, clue)

print(clues)

# while any([any(row) for row in map]):
# 	pass
        



