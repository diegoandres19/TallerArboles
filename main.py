class Nodo:
    def __init__(self, valor):
        self.valor = valor self.izquierda = None
        self.derecha = Noneclass ArbolBinario:

    def __init__(self, raiz=None):
        self.raiz = raiz def insertar(self, valor):
            if self.raiz is None: self.raiz = Nodo(valor)
            else: self._insertar_recursivo(valor, self.raiz)
    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else: self._insertar_recursivo(valor, nodo_actual.izquierda)
                elif valor > nodo_actual.valor: if nodo_actual.derecha is None:
                    nodo_actual.derecha = Nodo(valor)
                else: self._insertar_recursivo(valor, nodo_actual.derecha)
            else: # Valor duplicado, puedes manejarlo según tus necesidades pass
                def buscar(self, valor):
                    return self._buscar_recursivo(valor, self.raiz)
                    if self.raiz else None
                def _buscar_recursivo(self, valor, nodo_actual):
                    if nodo_actual is None or nodo_actual.valor == valor:
                        return nodo_actual
                    if valor < nodo_actual.valor: return self._buscar_recursivo(valor,

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None
class ArbolBinario:
    def __init__(self, raiz=None):
        self.raiz = raiz

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else: self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.derecha)
        else:
            pass

    def buscar(self, valor):
        return self._buscar_recursivo(valor, self.raiz) if self.raiz \
        else None

    def _buscar_recursivo(self, valor, nodo_actual):
        if nodo_actual is None or nodo_actual.valor == valor:
            return nodo_actual
        if valor < nodo_actual.valor:
            return self._buscar_recursivo(valor, nodo_actual.izquierda)
        return self._buscar_recursivo(valor, nodo_actual.derecha)