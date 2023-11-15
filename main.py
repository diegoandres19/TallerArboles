import matplotlib.pyplot as plt

class NodoArbol:
    def __init__(self, value, left=None, right=None):
        self.data = value
        self.left = left
        self.right = right
        
class BinarySearchTree:
    def __init__(self):
        self.__root = None
        
    def insert(self, value):
        
        if self.__root == None:
            self.__root = NodoArbol(value)
        
        else:
            self.__insert__(self.__root, value)
            
    def __insert__(self, nodo, value):
        if nodo.data == value:
            print("! dato existente, no se ingresa nada")
        elif value < nodo.data:

            if nodo.left == None:
                nodo.left = NodoArbol(value)

            else:
                self.__insert__(nodo.left, value)
        else:
            if nodo.right == None:
                nodo.right = NodoArbol(value)
            else:
                self.__insert__(nodo.right, value)
                

    def peso(self, nodo):
        if nodo == None:
            return 0
        else:
            return self.peso(nodo.left) + self.peso(nodo.right) + 1
        

    def orden(self, nodo):
        if nodo == None:
            return 0
        else:
            return max(self.orden(nodo.left), self.orden(nodo.right))+1
            

    def altura(self, nodo):
        if nodo == None:
            return 0
        else:
            return max(self.altura(nodo.left), self.altura(nodo.right))+1
        
    

tree = BinarySearchTree()


while True:
    valor = input("Ingrese el valor para el nodo (o 's' para salir): ")
    if valor == 's':
        break
    tree.insert(int(valor))

def plot_tree(node, ax, x, y, dx, dy):
    if node is None:
        return
    
    ax.text(x, y, str(node.data), ha='center', va='center', 
            bbox=dict(facecolor='white', edgecolor='black', boxstyle='circle'))
    
    left_x = x - dx/2
    right_x = x + dx/2
    child_y = y - dy
    
    if node.left is not None:
        ax.plot([x, left_x], [y, child_y], 'k-')
        plot_tree(node.left, ax, left_x, child_y, dx/2, dy)
    
    if node.right is not None:
        ax.plot([x, right_x], [y, child_y], 'k-')
        plot_tree(node.right, ax, right_x, child_y, dx/2, dy)
        

peso = tree.peso(tree._BinarySearchTree__root)
print("Peso del arbol:", peso)


orden = tree.orden(tree._BinarySearchTree__root)
print("Orden del arbol:", orden)


altura = tree.altura(tree._BinarySearchTree__root)
print("Altura del arbol:", altura)


fig, ax = plt.subplots()


plt.margins(0.1, 0.1)


plot_tree(tree._BinarySearchTree__root, ax, 0, 0, 1, 1)


plt.show()