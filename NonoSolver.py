size = 5
clues = {"xAxis": {1 : [1], 2: [1, 3], 3: [3], 4: [2, 1], 5: [2]}, "yAxis": {1: [1, 2], 2: [2], 3: [3], 4: [2], 5: [3]}}

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
	pos = 0
	for num in clue:
		for i in range(num):
			if axis == "xAxis":
				map[pos + i][index - 1] = 1
			if axis == "yAxis":
				map[index - 1][pos + i] = 1
		# +1 for empty cell between 2 blocks
		pos += num + 1

def isOverlap(clue):
	if max(clue) > size/2:
		return True
	return False

def placeOverlap(axis, index, clue):
	pos = size - max(clue)
	overlap = int((max(clue) - size/2) * 2)
	print(overlap)
	for i in range(overlap):
		if axis == "xAxis":
			map[pos + i][index - 1] = 1
		if axis == "yAxis":
			map[index - 1][pos + i] = 1

for axisName, axisClues in clues.items():
	print(axisName, axisClues)
	for index, clue in axisClues.items():
		print(index, clue, (max(clue) - size/2) * 2)
		if (isGuarantee(clue)):
			placeGuarantee(axisName, index, clue)
		elif (isOverlap(clue)):
			placeOverlap(axisName, index, clue)

for y in map:
	print(y)


        



