class Node:

    def __init__(self, value):
        self.value = value
        self.child = []
        self.parent = None

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value
    
    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent

    def addChild(self, node):
        node.setParent(self)
        self.child.append(node)

    def getAllChild(self):
        return self.child
    
    

   