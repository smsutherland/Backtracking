from Backtracking import Game, backtrack

class Sudoku(Game):
    def __init__(self, initialValues):
        self.initialValues = initialValues
        numValues = 0
        for i in initialValues:
            if i != None:
                numValues += 1
        self.length = 81 - numValues
    
    def getLength(self):
        return self.length

    def getRange(self):
        return range(1, 10)
    
    def checkSln(self, sln):
        fullSln = self.formSln(sln)
        for x in range(81):
            for y in self.getRelaventIndices(x):
                xVal = fullSln[x]
                yVal = fullSln[y]
                if xVal == yVal and xVal != None:
                    return False
        return True
    
    def formSln(self, sln):
        slnIndex = 0
        fullSln = []
        for x in self.initialValues:
            if x != None:
                fullSln.append(x)
            else:
                fullSln.append(sln[slnIndex])
                slnIndex += 1
        return fullSln

    def getRelaventIndices(self, index):
        if index not in range(81):
            return None
        column = index%9
        row = int(index/9)
        squarex = int(column/3)
        squarey = int(row/3)
        relaventIndices = [x for x in range(81) if x != index and (x%9 == column or int(x/9) == row or (int((x%9)/3) == squarex and int(int(x/9)/3) == squarey))]
        return relaventIndices

def printArray(array, width):
    index = 0
    print('[', end='')
    for ele in array:
        print(ele, end=', ')
        index += 1
        if index % width == 0:
            print()

mySudoku = Sudoku([None,3,None,None,None,8,None,None,5,None,None,6,None,None,7,None,8,2,None,None,None,6,2,None,4,1,None,9,None,2,None,None,None,None,7,None,3,7,None,8,9,6,None,None,None,None,None,None,None,None,None,None,3,None,None,None,3,None,6,9,None,None,None,None,None,4,3,None,2,None,None,None,7,1,None,None,None,5,None,2,None,])
sln = backtrack(mySudoku)
printArray(mySudoku.formSln(sln), 9)
