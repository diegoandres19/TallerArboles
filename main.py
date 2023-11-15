class Nodo:
    def __init__(self, value):
        self.dato = value
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def agregarRecursivo(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.agregarRecursivo(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.agregarRecursivo(nodo.derecha, dato)

    def inorden(self, nodo):
        if nodo is not None:
            self.inorden(nodo.izquierda)
            print(nodo.dato, end=", ")
            self.inorden(nodo.derecha)

    def preorden(self, nodo):
        if nodo is not None:
            print(nodo.dato, end=", ")
            self.preorden(nodo.izquierda)
            self.preorden(nodo.derecha)

    def postorden(self, nodo):
        if nodo is not None:
            self.postorden(nodo.izquierda)
            self.postorden(nodo.derecha)
            print(nodo.dato, end=", ")

    def buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.dato == busqueda:
            return nodo
        if busqueda < nodo.dato:
            return self.buscar(nodo.izquierda, busqueda)
        else:
            return self.buscar(nodo.derecha, busqueda)

    def agregar(self, dato):
        self.agregarRecursivo(self.raiz, dato)

    def imprimirInorden(self):
        print("Imprimiendo árbol inorden: ")
        self.inorden(self.raiz)
        print("")

    def imprimirPreorden(self):
        print("Imprimiendo árbol preorden: ")
        self.preorden(self.raiz)
        print("")

    def imprimirPostorden(self):
        print("Imprimiendo árbol postorden: ")
        self.postorden(self.raiz)
        print("")

    def buscarDato(self, busqueda):
        return self.buscar(self.raiz, busqueda)

    def calcularAltura(self, nodo):
        if nodo is None:
            return 0
        else:
            altura_izquierda = self.calcularAltura(nodo.izquierda)
            altura_derecha = self.calcularAltura(nodo.derecha)
            return max(altura_izquierda, altura_derecha) + 1

    def obtenerAltura(self):
        return self.calcularAltura(self.raiz)

    def calcularPeso(self, nodo):
        if nodo is None:
            return 0
        else:
            peso_izquierda = self.calcularPeso(nodo.izquierda)
            peso_derecha = self.calcularPeso(nodo.derecha)
            return peso_izquierda + peso_derecha + 1

    def obtenerPeso(self):
        return self.calcularPeso(self.raiz)

arbol = Arbol(10)
def menu():
    print("1. Agregar elemento al árbol")
    print("2. Imprimir árbol inorden")
    print("3. Imprimir árbol preorden")
    print("4. Imprimir árbol postorden")
    print("5. Buscar elemento en el árbol")
    print("6. Calcular altura del árbol")
    print("7. Calcular peso del árbol")
    print("8. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        dato = int(input("Ingrese el elemento a agregar al árbol: "))
        arbol.agregar(dato)
        menu()
    elif opcion == "2":
        arbol.imprimirInorden()
        menu()

    elif opcion == "3":
        arbol.imprimirPreorden()
        menu()
    elif opcion == "4":
        arbol.imprimirPostorden()
        menu()
    elif opcion == "5":
        busqueda = int(input("Ingrese el elemento a buscar en el árbol: "))
        resultado = arbol.buscarDato(busqueda)
        if resultado:
            print(f"El elemento {busqueda} está en el árbol.")
            menu()
        else:
            print(f"El elemento {busqueda} no está en el árbol.")
            menu()
    elif opcion == "6":
        altura = arbol.obtenerAltura()
        print(f"La altura del árbol es: {altura}")
        menu()
    elif opcion == "7":
        peso = arbol.obtenerPeso()
        print(f"El peso del árbol es: {peso}")
        menu()
    elif opcion == "8":
        print("Saliendo del programa... ¡Hasta la próxima!")
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")
        menu()
menu()