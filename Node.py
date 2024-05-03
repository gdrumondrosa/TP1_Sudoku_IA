import copy

class Node:
    def __init__(self, matrix):
        self.matrix = matrix
        self.children = []
        self.g = 0

    def get_zero(self):
        for l in range(9):
            for c in range(9):
                if self.matrix[l][c] == 0:
                    return [l, c]
    
    def get_actions(self):
        l = self.get_zero()[0]
        c = self.get_zero()[1]

        line_actions = []
        for i in range(1, 10):
            if i not in self.matrix[l]:
                line_actions.append(i)

        col_actions = []
        non_col_actions = []
        for line in range(9):
            non_col_actions.append(self.matrix[line][c])
        for i in range(1, 10):
            if i not in non_col_actions:
                col_actions.append(i)

        block_actions = []
        non_block_actions = []
        if l == 0 or l == 1 or l == 2:
            if c == 0 or c == 1 or c == 2:
                for line in range(3):
                    for col in range(3):
                        non_block_actions.append(self.matrix[line][col])
            elif c == 3 or c == 4 or c == 5:
                for line in range(3):
                    for col in range(3, 6):
                        non_block_actions.append(self.matrix[line][col])
            elif c == 6 or c == 7 or c == 8:
                for line in range(3):
                    for col in range(6, 9):
                        non_block_actions.append(self.matrix[line][col])
        elif l == 3 or l == 4 or l == 5:
            if c == 0 or c == 1 or c == 2:
                for line in range(3, 6):
                    for col in range(3):
                        non_block_actions.append(self.matrix[line][col])
            elif c == 3 or c == 4 or c == 5:
                for line in range(3, 6):
                    for col in range(3, 6):
                        non_block_actions.append(self.matrix[line][col])
            elif c == 6 or c == 7 or c == 8:
                for line in range(3, 6):
                    for col in range(6, 9):
                        non_block_actions.append(self.matrix[line][col])
        elif l == 6 or l == 7 or l == 8:
            if c == 0 or c == 1 or c == 2:
                for line in range(6, 9):
                    for col in range(3):
                        non_block_actions.append(self.matrix[line][col])
            elif c == 3 or c == 4 or c == 5:
                for line in range(6, 9):
                    for col in range(3, 6):
                        non_block_actions.append(self.matrix[line][col])
            elif c == 6 or c == 7 or c == 8:
                for line in range(6, 9):
                    for col in range(6, 9):
                        non_block_actions.append(self.matrix[line][col])
        for i in range(1, 10):
            if i not in non_block_actions:
                block_actions.append(i)
        
        all_actions = []
        for i in range(1, 10):
            if i in line_actions and i in col_actions and i in block_actions:
                all_actions.append(i)

        return all_actions

    def solution(self):
        for l in self.matrix:
            line_sum = 0
            for c in l:
                line_sum += c
            if line_sum != 45:
                return False
        
        for c in range(9):
            col_sum = 0
            for l in range(9):
                col_sum += self.matrix[l][c]
            if col_sum != 45:
                return False
        
        block_sum = 0
        for l in range(3):
            for c in range(3):
                block_sum += self.matrix[l][c]
        if block_sum != 45:
            return False
        
        block_sum = 0
        for l in range(3):
            for c in range(3, 6):
                block_sum += self.matrix[l][c]
        if block_sum != 45:
            return False
        
        block_sum = 0
        for l in range(3):
            for c in range(6, 9):
                block_sum += self.matrix[l][c]
        if block_sum != 45:
            return False
        
        block_sum = 0
        for l in range(3, 6):
            for c in range(3):
                block_sum += self.matrix[l][c]
        if block_sum != 45:
            return False
        
        block_sum = 0
        for l in range(3, 6):
            for c in range(3, 6):
                block_sum += self.matrix[l][c]
        if block_sum != 45:
            return False
        
        block_sum = 0
        for l in range(3, 6):
            for c in range(6, 9):
                block_sum += self.matrix[l][c]
        if block_sum != 45:
            return False

        block_sum = 0
        for l in range(6, 9):
            for c in range(3):
                block_sum += self.matrix[l][c]
        if block_sum != 45:
            return False
        
        block_sum = 0
        for l in range(6, 9):
            for c in range(3, 6):
                block_sum += self.matrix[l][c]
        if block_sum != 45:
            return False
        
        block_sum = 0
        for l in range(6, 9):
            for c in range(6, 9):
                block_sum += self.matrix[l][c]
        if block_sum != 45:
            return False
        
        return True
    
    def get_dist_to_goal(self):
        bool_map = [map(bool, row) for row in self.matrix]
        self.f = self.g + 81-sum([sum(r) for r in bool_map])

    def get_less_actions(self):
        coordinates = []
        actions = []
        for l in range(9):
            for c in range(9):
                if self.matrix[l][c] == 0:
                    line_actions = []
                    for i in range(1, 10):
                        if i not in self.matrix[l]:
                            line_actions.append(i)

                    col_actions = []
                    non_col_actions = []
                    for line in range(9):
                        non_col_actions.append(self.matrix[line][c])
                    for i in range(1, 10):
                        if i not in non_col_actions:
                            col_actions.append(i)

                    block_actions = []
                    non_block_actions = []
                    if l == 0 or l == 1 or l == 2:
                        if c == 0 or c == 1 or c == 2:
                            for line in range(3):
                                for col in range(3):
                                    non_block_actions.append(self.matrix[line][col])
                        elif c == 3 or c == 4 or c == 5:
                            for line in range(3):
                                for col in range(3, 6):
                                    non_block_actions.append(self.matrix[line][col])
                        elif c == 6 or c == 7 or c == 8:
                            for line in range(3):
                                for col in range(6, 9):
                                    non_block_actions.append(self.matrix[line][col])
                    elif l == 3 or l == 4 or l == 5:
                        if c == 0 or c == 1 or c == 2:
                            for line in range(3, 6):
                                for col in range(3):
                                    non_block_actions.append(self.matrix[line][col])
                        elif c == 3 or c == 4 or c == 5:
                            for line in range(3, 6):
                                for col in range(3, 6):
                                    non_block_actions.append(self.matrix[line][col])
                        elif c == 6 or c == 7 or c == 8:
                            for line in range(3, 6):
                                for col in range(6, 9):
                                    non_block_actions.append(self.matrix[line][col])
                    elif l == 6 or l == 7 or l == 8:
                        if c == 0 or c == 1 or c == 2:
                            for line in range(6, 9):
                                for col in range(3):
                                    non_block_actions.append(self.matrix[line][col])
                        elif c == 3 or c == 4 or c == 5:
                            for line in range(6, 9):
                                for col in range(3, 6):
                                    non_block_actions.append(self.matrix[line][col])
                        elif c == 6 or c == 7 or c == 8:
                            for line in range(6, 9):
                                for col in range(6, 9):
                                    non_block_actions.append(self.matrix[line][col])
                    for i in range(1, 10):
                        if i not in non_block_actions:
                            block_actions.append(i)
                    
                    all_actions = []
                    for i in range(1, 10):
                        if i in line_actions and i in col_actions and i in block_actions:
                            all_actions.append(i)
                    coordinates.append([l, c])
                    actions.append(all_actions)
        min_l = 10
        index = 0
        for l in range(len(actions)):
            if len(actions[l]) < min_l:
                min_l = len(actions[l])
                index = l
        return [coordinates[index], actions[index]]
