import sys
import copy
import time
from Node import Node

#busca sem informação
def bfs(initial_Node):
    node = initial_Node
    if node.solution() == True:
        return node.matrix

    frontier = [node]
    explored = []
    iterations = 0
    
    while(1):
        if len(frontier) == 0:
            return -1
        node = frontier.pop(0)
        explored.append(node.matrix)
        iterations += 1
        for i in node.get_actions():
            new_matrix = copy.deepcopy(node.matrix)
            new_matrix[node.get_zero()[0]][node.get_zero()[1]] = i
            child = Node(new_matrix)
            node.children.append(child)
            if child.matrix not in explored or child not in frontier:
                if child.solution() == True:
                    return [iterations, child.matrix]
                frontier.append(child)

def ids(initial_Node):
    l = 0
    while(1):
        depth = 0
        frontier = [initial_Node]
        iterations = 0
        while len(frontier) != 0:
            node = frontier.pop()
            iterations += 1
            if node.solution() == True:
                return [iterations, node.matrix]
            if depth <= l:
                if node not in frontier:
                    for i in node.get_actions():
                        new_matrix = copy.deepcopy(node.matrix)
                        new_matrix[node.get_zero()[0]][node.get_zero()[1]] = i
                        child = Node(new_matrix)
                        node.children.append(child)
                        frontier.append(child)
            depth += 1
        l += 1

def ucs(initial_Node):
    node = initial_Node
    frontier = [node]
    explored = []
    iterations = 0

    while(1):
        if len(frontier) == 0:
            return -1
        node = frontier.pop(0)
        if node.solution() == True:
            return [iterations, node.matrix]
        explored.append(node.matrix)
        iterations += 1
        for i in node.get_actions():
            new_matrix = copy.deepcopy(node.matrix)
            new_matrix[node.get_zero()[0]][node.get_zero()[1]] = i
            child = Node(new_matrix)
            node.children.append(child)
            if child.matrix not in explored or child not in frontier:
                frontier.append(child)

#busca com informação
def ass(initial_Node):
    initial_Node.get_dist_to_goal()
    open = [initial_Node]
    closed = []
    iterations = 0

    while open != []:
        min = initial_Node.f
        cont = 0
        cont_id = 0
        current = initial_Node
        for node in open:
            if node.f < min:
                min = node.f
                current = node
                cont_id = cont
            cont += 1
        if current.solution() == True:
            return [iterations, current.matrix]
        open.pop(cont_id)
        closed.append(current)
        for i in current.get_actions():
            iterations += 1
            new_matrix = copy.deepcopy(current.matrix)
            new_matrix[current.get_zero()[0]][current.get_zero()[1]] = i
            child = Node(new_matrix)
            current.children.append(child)
            if child not in closed:
                if child not in open:
                    child.get_dist_to_goal()
                    open.append(child)
    return -1

def gbfs(initial_Node):
    node = initial_Node
    frontier = [node]
    explored = []
    iterations = 0

    while(1):
        if len(frontier) == 0:
            return -1
        node = frontier.pop(0)
        if node.solution() == True:
            return [iterations, node.matrix]
        explored.append(node.matrix)
        iterations += 1
        for i in node.get_less_actions()[1]:
            new_matrix = copy.deepcopy(node.matrix)
            new_matrix[node.get_less_actions()[0][0]][node.get_less_actions()[0][1]] = i
            child = Node(new_matrix)
            node.children.append(child)
            if child.matrix not in explored or child not in frontier:
                frontier.append(child)

#lendo entrada
algorithm = sys.argv[1]
matrix = []

for i in sys.argv[2:]:
    line = []
    for c in i:
        line.append(int(c))
    matrix.append(line)

#rodando algoritmo e print
initial_Node = Node(matrix)

if algorithm == "B":
    start = time.time()
    number_of_iterations, final_matrix = bfs(initial_Node)
    end = time.time()
elif algorithm == "I":
    start = time.time()
    number_of_iterations, final_matrix = ids(initial_Node)
    end = time.time()
elif algorithm == "U":
    start = time.time()
    number_of_iterations, final_matrix = ucs(initial_Node)
    end = time.time()
elif algorithm == "A":
    start = time.time()
    number_of_iterations, final_matrix = ass(initial_Node)
    end = time.time()
elif algorithm == "G":
    start = time.time()
    number_of_iterations, final_matrix = gbfs(initial_Node)
    end = time.time()

print(number_of_iterations, int((end-start)*1000))
for l in final_matrix:
    for c in l:
        print(c, end="")
    print(end=" ")