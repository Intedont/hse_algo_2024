import collections

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        self.height = 1

    def update_height(node):
        node.height = max(Node.get_height(node.left), Node.get_height(node.right)) + 1
    
    def rotate_right(node):
        tmp = node.left
        node.left = tmp.right
        tmp.right = node
        Node.update_height(node)
        Node.update_height(tmp)
        return tmp

    def rotate_left(node):
        tmp = node.right
        node.right = tmp.left
        tmp.left = node
        Node.update_height(node)
        Node.update_height(tmp)
        return tmp

    def get_height(node):
        if(node):
            return node.height
        else:
            return 0
            
    def balance_factor(node):
        return Node.get_height(node.right) - Node.get_height(node.left)
    
    def balance(node):
        Node.update_height(node)
        if(Node.balance_factor(node) > 1):
            if(Node.balance_factor(node.right) == -1):
                node.right = Node.rotate_right(node.right)
            return Node.rotate_left(node)
        elif(Node.balance_factor(node) < -1):
            if(Node.balance_factor(node.left) == 1):
                node.left = Node.rotate_left(node.left)
            return Node.rotate_right(node)
        else:
            return node
            
    def insert(node, value):
        if(node is None):
            return Node(value)
        if(value > node.value):
            node.right = Node.insert(node.right, value)
        elif(value < node.value):
            node.left = Node.insert(node.left, value)
        return Node.balance(node)

    def find_min(node):
        if(node.left):
            return find_min(node.left)
        else:
            return node

    # Корректировка дерева после удаления ноды
    def correct_remove(node):
        if(node.left is None):
            return node.right

        node.left = Node.correct_remove(node.left)
        return balance(node)

    def remove(node, value):
        # Если такого элемента нет
        if(node is None):
            return None

        if(value < node.value):
            node.left = Node.remove(node.left, value)
        elif(value > node.value):
            node.right = Node.remove(node.right, value)
        else:
            q = node.left
            r = node.right
            
            if(r is None):
                return q
            
            min_node = Node.find_min(r)
            min_node.right = Node.correct_remove(r)

            min_node.left = q
            return Node.balance(min_node)
        
        return Node.balance(node)


class AVL():
    def __init__(self):
        self.root = Node(None)
    
    def insert(self, value):
        if(self.root.value is None):
            self.root.value = value
        else:
            self.root = Node.insert(self.root, value)

    def print_tree(self):
        queue = collections.deque([(self.root, 0)])
        output = []

        level = ([], 0)
        while queue: 
            node, level_num = queue.popleft()
            if(level_num == level[1]):
                level[0].append(node.value)
            else:
                #print(level[0])
                output.append(level[0])
                level = ([], level_num)
                level[0].append(node.value)

            if(node.left):
                queue.append((node.left, level_num + 1))
            if(node.right):
                queue.append((node.right, level_num + 1))
                
        #print(level[0])
        output.append(level[0])
        return output

    def remove(self, value):
        self.root = Node.remove(self.root, value)
        if(self.root is None):
            self.root = Node(None)
