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

def isComplete(clue: list[int], line: list[int]):
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
					# do other clues each have their own match?
					len(blocks) == len(newClue) or
					# is it not possible for the second clue to be in place of the first clue?
					newClue[1] < newClue[0] or 
					# does the second clue fit in any of the regions on the left of first block found?
					not any([region[1] >= newClue[1] for region in regions if region[0] < blocks[0][0]]) and
					# is there space left for the clue on the left of the first blockregion?
					not blocks[0][0] - regions[0][0] > newClue[0]
				):
				# mark clue complete (negative sign) in list
				newClues[0+count] = -newClue[0]
			else:
				# stop cycle of checking for the leftmost clue
				checkLeft = False

		# complete clue if it matches the rightmost clue
		if newClue[-1] == blocks[-1][1] and checkRight:
			if (
					len(blocks) == len(newClue) or
					newClue[-2] < newClue[-1] or
					not any([region[1] >= newClue[-2] for region in regions if region[0] > blocks[-1][0]]) and
					not (regions[-1][0] + regions[-1][1]) - (blocks[-1][0] + blocks[-1][1]) > newClue[-1]
				):
				newClues[-(1+count)] = -newClue[-1]
			else:
				checkRight = False
		# cut clues from clue list to check for new clues on the side
		newClue = newClue[1 if checkLeft else None:-1 if checkRight else None]
		# cut numbers of completed clue from line to be able to check new clues afterwards
		if checkRight: newLine = newLine[:blocks[-1][0] - 1]
		if checkLeft: newLine = newLine[blocks[0][0] + blocks[0][1] + 1:]
		count += 1
	return newClues

cluee = [1, 2, 1, 2, 1]
linee = [1, 2, 1, 1, 0, 1, 2, 1, 1, 0, 1]

print(isComplete(cluee, linee))

# tests
assert isComplete([1, 1, 1], [0, 2, 1, 2, 1]) == [1, -1, -1]
assert isComplete([1, 1], [1, 2, 1, 0, 0]) == [-1, -1]
assert isComplete([1, 2, 1, 2, 1], [1, 2, 1, 1, 0, 1, 2, 1, 1, 0, 1]) == [-1, -2, -1, -2, -1]
assert isComplete([1, 1, 1], [1, 2, 1, 0, 0, 0]) == [-1, -1, 1]
assert isComplete([2, 2], [0, 0, 2, 1, 1, 0, 0, 0]) == [2, 2]