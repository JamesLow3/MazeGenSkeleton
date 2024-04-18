# ------------------------------------------------------------------------
# Please COMPLETE the IMPLEMENTATION of this class.
# Adjacent list implementation.
#
# __author__ = 'Jeffrey Chan', <YOU>
# __copyright__ = 'Copyright 2024, RMIT University'
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
#Linked List and Node class by Jeffrey Chan, RMIT, from week 2 workshop code
# ------------------------------------------------------------------------
from typing import List

from maze.util import Coordinates
from maze.graph import Graph


class Node:
    def __init__(self, value):
        self.m_value = value
        self.m_next = None
    def get_value(self):
        return self.m_value

    def get_next(self):
        return self.m_next

    def set_value(self, value):
        self.m_value = value

    def set_next(self, next):
        self.m_next = next

class LinkedList:

    def __init__(self):
        
        self.m_head= None
        self.m_length = 0
        self.m_first_element = None

    def add(self, new_value):
        new_node = Node(new_value)

        if not self.m_head:
            self.m_head = new_node
            self.m_first_element = new_node 
        else:
            new_node.set_next(self.m_head)
            self.m_head = new_node

        self.m_length += 1

    def insert(self, index, new_value):
        """
        Insert value (and corresponding node) at position 'index'.  Indices start at 0.

        @param index Position in list to add new value to.
        @param new_value Value to add to list.

        @throws IndexError Index are out of bounds.
        """
        if index >= self.m_length or index < 0:
            raise IndexError("Supplied index is invalid.")

        new_node = Node(new_value)

        if self.m_head == None:
            self.m_head = new_node
        else:
            # if index = 0, we should replace m_head with new_node
            if index == 0:
                new_node.set_next(self.m_head)
                self.m_head = new_node
            else:
                cur_node = self.m_head
                for i in range(index-1):
                    cur_node = cur_node.get_next()

                new_node.set_next(cur_node.get_next())
                cur_node.set_next(new_node);     
        self.m_length += 1

    def get(self, index):
        """
        Returns the value stored in node at position 'index' of list.

        @param index Position in list to get new value for.
        @return Value of element at specified position in list.

        @throws IndexError Index is out of bounds.
        """
        if index >= self.m_length or index < 0:
            raise IndexError("Supplied index is invalid.");

        cur_node = self.m_head
        for i in range(index): 
            cur_node = cur_node.get_next()

        return cur_node.get_value()

    def  search(self, value:Coordinates):
        temp_node = self.m_head
        for i in range(self.m_length):
            if temp_node.get_value() == value:
                return i

            temp_node = temp_node.get_next()

        return -1
    
    def remove(self, value):
        if self.m_length == 0:
            return False

        cur_node = self.m_head
        prev_node = None

        if cur_node.get_value() == value:
            self.m_head = cur_node.get_next()
            self.m_length -= 1
            return True

        prev_node = cur_node
        cur_node = cur_node.get_next()

        while cur_node:
            if cur_node.get_value() == value:
                prev_node.set_next(cur_node.get_next())
                cur_node = None
                self.m_length -= 1
                return True
            prev_node = cur_node
            cur_node = cur_node.get_next()

        return False


    def remove_by_index(self, index, dummy=None):
        if index >= self.m_length or index < 0:
            raise IndexError("Supplied index is invalid.");
        
        cur_node = self.m_head
        prev_node = None

        if index == 0:
            value = cur_node.get_value()
            self.m_head = cur_node.get_next()
        else:
            for i in range(index): 
                prev_node = cur_node
                cur_node = cur_node.get_next()

            value = cur_node.get_value()
            prev_node.set_next(cur_node.get_next())
            cur_node = None

        self.m_length -= 1      

        return -1

    def min(self):

        if self.m_length == 0:
            raise IndexError("Min is not defined for an empty list.")

        min_value = self.m_head.get_value();
        cur_node = self.m_head.get_next();

        while cur_node != None:
            if cur_node.get_value() < min_value:
                min_value = cur_node.get_value()

            cur_node = cur_node.get_next()

        return min_value

    def max(self):
        if self.m_length == 0:
            raise IndexError("Max is not defined for an empty list.")

        max_value = self.m_head.get_value()
        cur_node = self.m_head.get_next()

        while cur_node:
            if cur_node.get_value() > max_value:
                max_value = cur_node.get_value()

            cur_node = cur_node.get_next()

        return max_value

    def print(self):
        print(self)
    

class AdjListGraph(Graph):
    """
    Represents an undirected graph.  Please complete the implementations of each method.  See the documentation for the parent class
    to see what each of the overriden methods are meant to do.
    """

    def __init__(self, rowNum, colNum):
        self.vertices = []

        
    
    def addVertex(self, label:Coordinates):
        
        self.new_ll = LinkedList()
        self.new_ll.add(label)
        self.vertices.append(self.new_ll)
        
        
    # def displayLinkedLists(self):
    #     i = 0
        # while i < len(self.vertices):
        #     j = 1
        #     print("New LL number: ")
        #     print(i)
        #     print("Head Node")
        #     self.printRowCol(self.vertices[i].get(0))
        #     print()
        #     print("Adjacent nodes ")
        #     while j < self.vertices[i].m_length:
        #         print(self.vertices[i].m_length)
        #         print(i)
        #         self.printRowCol(self.vertices[i].get(j))
                
        #         print("is this running????")
        #         j = j + 1
        #     i = i + 1
        #     print()
        # i = 0
        # print("head 4 4 here!!!")
        # self.printRowCol(self.vertices[44].m_head.m_value)

        # self.vertices.find
        # while i < len(self.vertices):
        #     print("head")
        #     self.printRowCol(self.vertices[i].m_head.m_value)
        #     print("head index: ")
        #     print(i)
        #     print("head end")
        #     print()
        #     i = i + 1
        

    def addVertices(self, vertLabels:List[Coordinates]):
        i = 0
        
        while i < len(vertLabels):
            self.addVertex( vertLabels[i])
            
            i = i + 1
        
    def printRowCol(self, vert:Coordinates):
        print("Row: ")
        print(vert.getRow())
        print("Column")
        print(vert.getCol())

    def addEdge(self, vert1:Coordinates, vert2:Coordinates, addWall:bool = False)->bool:
        k = 0
        i = self.find_vertex(vert1)
        j = self.find_vertex(vert2)
        adjacents1 = []
        adjacents1 = self.neighbours(vert1)
        adjacents2 = []
        adjacents2 = self.neighbours(vert2)

        if i != -1:
            while k < len(adjacents1):
                if self.vertices[i].search(adjacents1[k]) == -1:
                    self.vertices[i].add(adjacents1[k])
                k = k + 1
        k = 0
        if j != -1:
            while k < len(adjacents2):
                if self.vertices[j].search(adjacents2[k]) == -1:
                    self.vertices[j].add(adjacents2[k])

                k = k + 1
        return True


    def updateWall(self, vert1:Coordinates, vert2:Coordinates, wallStatus:bool)->bool:
        isWall = self.getWallStatus(vert1, vert2)
        if isWall:
            self.removeEdge(vert1, vert2)
            return False
        else:
            self.addEdge(vert1, vert2, True)
            return True



    def removeEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        i = self.find_vertex(vert1)
        j = self.find_vertex(vert2)
        
        self.vertices[i].remove(vert2)
        self.vertices[j].remove(vert1)
        return True
        
        


    def hasVertex(self, label:Coordinates)->bool:
        has_vertex = False
        if self.find_vertex(label) > -1:
            has_vertex = True
        return has_vertex



    def hasEdge(self, vert1:Coordinates, vert2:Coordinates)->bool:
        has_edge = False
        i = self.find_vertex(vert1)
        j = self.find_vertex(vert2)
        if self.vertices[i].search(self.vertices[j].m_first_element.m_value) != -1 or self.vertices[j].search(self.vertices[i].m_first_element.m_value) != -1:
            has_edge = True
        return has_edge

    def getWallStatus(self, vert1:Coordinates, vert2:Coordinates)->bool:
        
        if self.hasEdge(vert1, vert2):
            return True

        else:
            return False
        
    


    def neighbours(self, label:Coordinates)->List[Coordinates]:
        neighbours = []
        row = label.getRow()
        col = label.getCol()
        above = Coordinates(row + 1, col)
        left = Coordinates(row, col - 1)
        right = Coordinates(row, col + 1)
        down = Coordinates(row - 1, col)

        if self.checkCoordinates(above):
            neighbours.append(above)
        if self.checkCoordinates(left):
            neighbours.append(left)
        if self.checkCoordinates(right):
            neighbours.append(right)
        if self.checkCoordinates(down):
            neighbours.append(down)
        
        return neighbours
        
        
    def find_vertex(self, vert:Coordinates):
        found = False
        i = 0
        while i < len(self.vertices) and found == False:
            if self.vertices[i].m_first_element.m_value == vert:
                found = True
                return i
            else: 
                i = i + 1
        return -1
    
    def checkCoordinates(self, coord:Coordinates)->bool:
        return coord.getRow() >= -1 and coord.getCol() >= -1
