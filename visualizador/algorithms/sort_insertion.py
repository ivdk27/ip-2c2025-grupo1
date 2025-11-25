# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 1        # empezamos desde el segundo elemento
j = None

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 1
    j = None

def step():
    global items, n, i, j
    # - Si i >= n: devolver {"done": True}.
    if i >= n:
        return {"done": True}
    # - Si j es None: empezar desplazamiento para el items[i] (p.ej., j = i) y devolver un highlight sin swap.
    if j == None:
        j = i
        return {"a": j, "b": j, "swap": False, "done": False}
    # - Mientras j > 0 y items[j-1] > items[j]: hacer UN swap adyacente (j-1, j) y devolverlo con swap=True.
    while j > 0 and items[j-1] > items[j]:
        items[j-1], items[j] = items[j], items[j-1]
        out = {"a":j-1, "b":j, "swap":True, "done":False}
        j=j-1
        return out
    # - Si ya no hay que desplazar: avanzar i y setear j=None.
    i =i+1
    j = None
    return {"a": i, "b": i, "swap": False, "done": False}
    return {"done": True}