# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

items = []
n = 0
i = 0
j = 0

def init(vals):
    global items, n, i, j
    items = list(vals)
    n = len(items)
    i = 0
    j = 0

def step():
    global items, n, i, j

    if i >= n - 1:
        return {"done": True}
    
    a = j
    b = j + 1
    swap = False

    if items[a] > items[b]:
        swap = True

        items[a], items[b] = items[b], items[a]

    j += 1
    if j >= n - 1 - i:
        i += 1
        j = 0

    return {
        "a": a,
        "b": b,
        "swap": swap,
        "done": False
    }