from pkbNode import Node


def printParent(node):
    if node.getParent() is None:
        print(node.getValue(), end=' ')
    else:
        printParent(node.getParent())
        print(node.value, end=' ')


def dfs(graph, value):
    if graph.getValue() == value:
        print('ketemu:')
        printParent(graph)
        print()
    else:
        for node in graph.getAllChild():
            dfs(node, value)

"""def dls(graph, value):
    limit=0
    if graph.getValue() == value and limit<=2:
        limit+=1
        print('ketemu:')
        printParent(graph)
        print()
    else:
        for node in graph.getAllChild():
            dfs(node, value)"""

def bfs(graph, value):
    print('BFS:')
    queue = [graph]
    for node in queue:
        print(node.value)
        if node.getValue() == value:
            print('Ketemu:')
            printParent(node)
            break
            # klo diganti pake:
            # print()-->bs ketemu semua
        else:
            queue.extend(node.getAllChild())


def main():
    y = Node('Y')
    e = Node('E')
    e.addChild(y)
    d = Node('D')
    a = Node('A')
    a.addChild(d)
    a.addChild(e)
    y2 = Node('Y')
    b = Node('B')
    b.addChild(a)
    b.addChild(y2)
    d2 = Node('D')
    y3 = Node('Y')
    b2 = Node('B')
    b2.addChild(d2)
    b2.addChild(y3)
    y4 = Node('Y')
    c = Node('C')
    c.addChild(y4)
    a2 = Node('A')
    a2.addChild(b2)
    a2.addChild(c)

    x = Node('X')
    x.addChild(a2)
    x.addChild(b)

    #bfs(x, 'Y')
    #dfs(x, 'Y')
    dls(x,'Y')


if __name__ == '__main__':
    main()
