# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
stack = [] # pila
inicio = 0
fin = 0
i = 0
j = 0
pivote = None
pivote_idx = None
fase = "particion"   # "particion" | "buscarSwap" | "swapPivote" | "añadir"

def init(vals):
    global items, n, stack, inicio, fin, i, j, pivote, pivote_idx, fase
    items = list(vals)
    n = len(items)
    stack = [(0, n - 1)] 
    inicio = 0
    fin = 0
    i = 0
    j = 0
    pivote = None
    pivote_idx = None
    fase = "particion"

def step():
    global items, n, stack, inicio, fin, i, j, pivote, pivote_idx, fase

    if n < 2:
        return {"done": True}

    
    if fase == "particion":
        if not stack:
            return {"done": True}       # Finaliza cuando ya no hay subarreglos

        inicio, fin = stack.pop()

        if inicio >= fin:               # el subarreglo es trivial
            return {"done": False}

        # inicializamos la partición
        pivote = items[fin]
        i = inicio - 1
        j = inicio
        fase = "buscarSwap"
        return {"done": False}

    
    if fase == "buscarSwap": #Se recorre con J y se realiza el swap si es necesario
        if j < fin:
            if items[j] <= pivote:
                i = i + 1
                a = i
                b = j
                items[a], items[b] = items[b], items[a]
                j = j + 1
                return {"a": a, "b": b, "swap": True, "done": False}
            else:
                j = j + 1
                return {"swap": False, "done": False}

        
        fase = "swapPivote" #Finaliza el recorrido, cambio de fase

    
    if fase == "swapPivote": #Pone el pivote en su lugar
        a = i + 1
        b = fin
        items[a], items[b] = items[b], items[a]
        pivote_idx = a
        fase = "añadir"
        return {"a": a, "b": b, "swap": True, "done": False}

    
    if fase == "añadir": #Se añaden los subarreglos restantes a la pila
        # subarreglo izquierdo
        if pivote_idx - 1 > inicio:
            stack.append((inicio, pivote_idx - 1))

        # subarreglo derecho
        if pivote_idx + 1 < fin:
            stack.append((pivote_idx + 1, fin))

        fase = "particion"
        return {"swap": False, "done": False}

    return {"done": False}


# TODO: implementar UN micro-paso de tu algoritmo y devolver el dict.
    # Recordá:
    # - a, b dentro de [0, n-1]
    # - si swap=True, primero hacé el intercambio en 'items'
    # - cuando termines, devolvé {"done": True}
    
