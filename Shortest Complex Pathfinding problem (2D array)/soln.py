import sys
sys.stdin = open("ip.txt", "r")
sys.stdout = open("op.txt", "w")
input= __import__('sys').stdin.readline

from collections import deque

def shortestPathPathfinder(matrix, k):
	rows, cols = len(matrix), len(matrix[0])
	if rows == cols == 1: return 0
	if k > rows+cols-2: return rows+cols-2
	queue = deque([(0,0,k,0)])
	visited = set([(0,0,k)])
	while queue:
		row, col, elim, steps = queue.popleft()
		for newRow, newCol in [(row-1, col), (row, col-1), (row+1, col), (row, col+1)]:
			if (newRow>=0 and newCol>=0 and newRow<rows and newCol<cols):
				if (matrix[newRow][newCol]==1 and elim-1>=0 and (newRow, newCol, elim-1) not in visited):
					visited.add((newRow, newCol, elim-1))
					queue.append((newRow, newCol, elim-1, steps+1))
				if (matrix[newRow][newCol]==0 and (newRow, newCol, elim) not in visited):
					if (newRow, newCol)==(rows-1, cols-1):
						return steps+1
					visited.add((newRow, newCol, elim))
					queue.append((newRow, newCol, elim, steps+1))
	return -1

if __name__ == "__main__":
	matrix = [
	[0,0,0,0],
	[0,0,1,0],
	[0,1,0,1],
	[1,0,0,1],
	[0,0,0,0]
	]
	k = 1
	print("*** MATRIX ***")
	print(*matrix, sep="\n")
	print("Shortest path from top-left corner to bottom-right corner: ", shortestPathPathfinder(matrix, k))