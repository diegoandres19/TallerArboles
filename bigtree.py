
from bigtree import Tree

class MyTree(Tree):
    def __init__(self, root_value):
        super().__init__(root_value)

    def add_child(self, parent, child_value):
        new_child = MyTree(child_value)
        parent.add_child(new_child)
        return new_child

# Crear un árbol
root = MyTree(10)

# Añadir hijos al árbol
child1 = root.add_child(root, 15)
child2 = root.add_child(root, 20)
child3 = root.add_child(root, 25)

# Añadir más hijos a un hijo específico
child1_1 = root.add_child(child1, 30)
child1_2 = root.add_child(child1, 35)

# Imprimir el árbol
root.print_tree()