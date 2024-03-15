from avl_tree import AVL, Node
import unittest


class TestTree(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_print(self):
        tree = AVL()

        self.assertEqual(tree.print_tree(), [[None]])
        tree.insert(2)
        self.assertEqual(tree.print_tree(), [[2]])

        tree.root.left = Node(2)
        tree.root.left.left = Node(3)
        tree.root.right = Node(10)
        tree.root.left.right = Node(4)
        tree.root.right.left = Node(11)
        tree.root.right.right = Node(12)

        self.assertEqual(tree.print_tree(), [[2], [2, 10], [3, 4, 11, 12]])
    
    def test_insertion(self):
        # Тестируем большие и маленькие левые повороты
        tree = AVL()
        tree.insert(0)
        tree.insert(2)
        self.assertEqual(tree.print_tree(), [[0], [2]])

        tree.insert(4)
        self.assertEqual(tree.print_tree(), [[2], [0, 4]])

        tree.insert(6)
        self.assertEqual(tree.print_tree(), [[2], [0, 4], [6]])

        tree.insert(8)
        self.assertEqual(tree.print_tree(), [[2], [0, 6], [4, 8]])

        # Большой поворот налево
        tree.insert(10)
        self.assertEqual(tree.print_tree(), [[6], [2, 8], [0, 4, 10]])

        # Поворот налево
        tree.insert(12)
        self.assertEqual(tree.print_tree(), [[6], [2, 10], [0, 4, 8, 12]])

        tree.insert(14)
        tree.insert(16)
        tree.insert(11)
        self.assertEqual(tree.print_tree(), [[6], [2, 12], [0, 4, 10, 14], [8, 11, 16]])

        # Тестируем большие и маленькие правые повороты
        tree = AVL()
        tree.insert(16)
        tree.insert(14)
        self.assertEqual(tree.print_tree(), [[16], [14]])

        # Малый правый поворот
        tree.insert(12)
        self.assertEqual(tree.print_tree(), [[14], [12, 16]])

        tree.insert(10)
        self.assertEqual(tree.print_tree(), [[14], [12, 16], [10]])

        # Малый правый поворот
        tree.insert(8)
        self.assertEqual(tree.print_tree(), [[14], [10, 16], [8, 12]])
        
        # Большой правый поворот
        tree.insert(6)
        self.assertEqual(tree.print_tree(), [[10], [8, 14], [6, 12, 16]])

        # Правый поворот
        tree.insert(4)
        self.assertEqual(tree.print_tree(), [[10], [6, 14], [4, 8, 12, 16]])

        tree.insert(2)
        self.assertEqual(tree.print_tree(), [[10], [6, 14], [4, 8, 12, 16], [2]])

        tree.insert(1)
        self.assertEqual(tree.print_tree(), [[10], [6, 14], [2, 8, 12, 16], [1, 4]])

        tree.insert(1)
        self.assertEqual(tree.print_tree(), [[10], [6, 14], [2, 8, 12, 16], [1, 4]])

        tree.insert(3)
        self.assertEqual(tree.print_tree(), [[10], [4, 14], [2, 6, 12, 16], [1, 3, 8]])


    def test_remove(self):
        tree = AVL()
        tree.insert(0)
        tree.insert(2)
        tree.insert(4)
        tree.insert(6)
        tree.insert(8)
        tree.insert(10)

        self.assertEqual(tree.print_tree(), [[6], [2, 8], [0, 4, 10]])

        # Удаляем несуществующую ноду
        tree.remove(12)
        self.assertEqual(tree.print_tree(), [[6], [2, 8], [0, 4, 10]])
        tree.remove(-1)
        self.assertEqual(tree.print_tree(), [[6], [2, 8], [0, 4, 10]])
        print(tree.print_tree())

        tree.remove(2)
        self.assertEqual(tree.print_tree(), [[6], [4, 8], [0, 10]])

        tree.remove(6)
        self.assertEqual(tree.print_tree(), [[8], [4, 10], [0]])
        self.assertEqual(tree.root.left.left.value, 0)

        tree.remove(4)
        self.assertEqual(tree.print_tree(), [[8], [0, 10]])

        tree.remove(8)
        self.assertEqual(tree.print_tree(), [[10], [0]])

        tree.remove(10)
        tree.remove(0)
        self.assertEqual(tree.print_tree(), [[None]])
        













        
