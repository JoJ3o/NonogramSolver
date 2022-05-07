import math

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

def isComplete():
	newClues = clue.copy()
	newClue = clue.copy()
	newLine = line.copy()
	count = 0
	checkLeft = True
	checkRight = True

	while checkLeft or checkRight:
		blocks = getBlocks(newLine)
		regions = getRegions(newLine)

		# does any clue match the found blocks?
		if not any([block[1] == num for num in newClue for block in blocks]):
			return newClues

		# complete clue if it matches the only clue
		if len(newClue) == 1:
			if newClue[0] == blocks[0][1]: newClues[0+count] = -newClue[0]
			return newClues

		# complete clue if it matches the leftmost clue
		if newClue[0] == blocks[0][1] and checkLeft:
			if (
					# is it not possible for the second clue to be in place of the first clue?
					newClue[1] < newClue[0] or 
					# do other clues each have their own match?
					len(blocks) == len(newClue) or
					# does the second clue fit in any of the regions on the left of first block found?
					not any([region[1] >= newClue[1] for region in regions if region[0] < blocks[0][0]]) and
					# no space (first clue + seperator) left on the left of blockregion
					not blocks[0][0] - regions[0][0] > newClue[0]
				):
				newClues[0+count] = -newClue[0]
				newLine = newLine[blocks[0][0] + blocks[0][1] + 1:]
			else:
				checkLeft = False

		# complete clue if it matches the rightmost clue
		if newClue[-1] == blocks[-1][1] and checkRight:
			if (
					newClue[-2] < newClue[-1] or
					len(blocks) == len(newClue) or
					not any([region[1] >= newClue[-2] for region in regions if region[0] > blocks[-1][0]]) and
					not (regions[-1][0] + regions[-1][1]) - (blocks[-1][0] + blocks[-1][1]) > newClue[-1]
				):
				newClues[-(1+count)] = -newClue[-1]
				newLine = newLine[:-(blocks[0][0] + blocks[0][1] + 1)]
			else:
				checkRight = False
		newClue = newClue[1 if checkLeft else None:-1 if checkRight else None]
		count += 1
	return newClues

# [2, 2], [0, 0, 2, 1, 1, 0, 0, 0] -> [2, 2]
clue = [1, 1, 1]
line = [1, 2, 1, 0, 0, 0]

print(isComplete())

# 11 gap left
# 11 region 3 right
# 1212