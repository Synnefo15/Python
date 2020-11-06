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


class Graf:
    a = Node('A', 4)
    b = Node('B', 5)
    c = Node('C', 6)
    d = Node('D', -1)
    e = Node('E', 2)
    f = Node('F', 4)
    g = Node('G', 2)
    h = Node('H', 1)
    i = Node('I', -1)
    j = Node('J', -1)
    k = Node('K', -1)
    l = Node('L', -1)
    x = Node('X', 0)
    y = Node('Y', 0)

    h.add_child(l, 7)
    h.add_child(y, 2)
    g.add_child(k, 3)
    g.add_child(y, 6)
    f.add_child(y, 3)
    e.add_child(y, 7)
    e.add_child(j, 4)
    c.add_child(i, 9)
    c.add_child(h, 1)
    b.add_child(g, 2)
    b.add_child(f, 5)
    a.add_child(e, 3)
    a.add_child(d, 2)
    x.add_child(c, 4)
    x.add_child(b, 3)
    x.add_child(a, 5)

    def search(self, start, goal):
        mulai = [start]

        print('jalur: ')
        while mulai:
            print('==>', mulai[0].value, end=' ')
            current_node = mulai[0]
            if current_node.value == goal:
                return
            else:
                mulai.pop(0)
                for child in current_node.childs:
                    if child.h == -1:
                        child.f = 111
                    else:
                        child.d += child.g
                        child.f = child.g + child.h

                terkecil = current_node.childs[0]

                for i in range(1, len(current_node.childs)):
                    if current_node.childs[i].f < terkecil.f:
                        terkecil = current_node.childs[i]

                mulai.append(terkecil)


tree = Graf(Graf.x)
tree.search(Graf.x, 'Y')
