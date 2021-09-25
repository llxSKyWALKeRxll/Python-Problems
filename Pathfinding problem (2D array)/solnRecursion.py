def pathFinder(arr, startPos, endPos):
    if startPos == endPos:
        return [endPos]
    x, y = startPos
    if x+1 <= endPos[0] and arr[x+1][y]==1:
        a = pathFinder(arr, (x+1, y), endPos)
        if a != None:
            return [(x, y)] + a
    if y+1 <= endPos[1] and arr[x][y+1]==1:
        b = pathFinder(arr, (x, y+1), endPos)
        if b!= None:
            return [(x,y)] + b

if __name__=="__main__":
    arr = [
        [1,1,1,1,0],
        [1,0,1,0,0],
        [0,1,1,1,0],
        [0,1,0,1,0],
        [1,1,1,1,1]
    ]
    # print(*pathFinder(arr, (0,0), (4,4)), sep=" ==> ")
    print(pathFinder(arr, (0,0), (4,3)))