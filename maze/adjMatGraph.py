# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent matrix implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------


from typing import List, Dict, Tuple

from maze.util import Coordinates
from maze.graph import Graph


class AdjMatGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self, rowNum, colNum):
        self.adj_matrix: Dict[Tuple[Coordinates, Coordinates], int] = {}
        self.vertices: List[Coordinates] = []
        self.rowNum = rowNum
        self.colNum = colNum
    def addVertex(self, label:Coordinates):
         if label not in self.vertices:
            self.vertices.append(label)
            for v in self.vertices:
                self.adj_matrix[(label, v)] = 0
                self.adj_matrix[(v, label)] = 0
    
    def addVertices(self, vertLabels:List[Coordinates]):
        for label in vertLabels:
            self.addVertex(label)

    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        if vert1 not in self.vertices or vert2 not in self.vertices:
            return False
        self.adj_matrix[(vert1, vert2)] = 2
        self.adj_matrix[(vert2, vert1)] = 2
        return True


    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        if vert1 not in self.vertices or vert2 not in self.vertices:
            return False
        if vert1.isAdjacent(vert2):
            if self.adj_matrix[(vert1, vert2)] == 1:
                self.adj_matrix[(vert1, vert2)] = 2
            else:
                self.adj_matrix[(vert1, vert2)] = 1
                
            

            if self.adj_matrix[(vert2, vert1)] == 1:
                self.adj_matrix[(vert2, vert1)] = 2
            else:
                self.adj_matrix[(vert2, vert1)] = 1
        else:
            return False
        return True
        



    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if (vert1, vert2) in self.adj_matrix:
            self.adj_matrix[(vert1, vert2)] = 0
            self.adj_matrix[(vert2, vert1)] = 0
            return True
        return False
        


    def hasVertex(self, label:Coordinates)->bool:
        return label in self.vertices



    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if self.adj_matrix[(vert1, vert2)] >= 1 and self.adj_matrix[(vert2, vert1)] >= 1:
            return True
        return False


    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        if self.adj_matrix[(vert1, vert2)] == 2 and self.adj_matrix[(vert2, vert1)] == 2:
            return True
        return False



    def neighbours(self, label:Coordinates)->List[Coordinates]:
        
        neighbours : List[Coordinates] = []

        if label.getRow()-1 >= -1:
            neighbours.append(Coordinates(label.getRow()-1, label.getCol()))
        if label.getRow()+1 <= self.rowNum:
            neighbours.append(Coordinates(label.getRow()+1, label.getCol()))
        if label.getCol()-1 >= -1:
            neighbours.append(Coordinates(label.getRow(), label.getCol()-1))
        if label.getCol()+1 <= self.colNum:
            neighbours.append(Coordinates(label.getRow(), label.getCol()+1))       
             
        return neighbours