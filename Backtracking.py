class backtracker:
    def __init__(self, game):
        self.game = game
        self.solve()
    
    def solve(self):
        self.problemLength = self.game.getLength()
        self.dataRange = self.game.getRange()
        self.sln = [None]*self.problemLength
        if self.solveIndex(0):
            return self.sln
        else:
            return []

    
    def solveIndex(self, index):
        if index >= self.problemLength:
            return True
        for possibility in self.dataRange:
            self.sln[index] = possibility
            if self.game.checkSln(self.sln):
                if self.solveIndex(index + 1):
                    return True
        self.sln[index] = None
        return False
    
    def getSln(self):
        return self.sln

from abc import ABC, abstractmethod

class Game(ABC):
    @abstractmethod
    def getLength(self):
        pass
    
    @abstractmethod
    def getRange(self):
        pass

    @abstractmethod
    def checkSln(self, sln):
        pass

def backtrack(game):
    solver = backtracker(game)
    return solver.getSln()