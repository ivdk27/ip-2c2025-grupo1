# Template genérico — SKELETON
# Contrato: init(vals), step() -> {"a": int, "b": int, "swap": bool, "done": bool}

iitems = []
n = 0
gap = 0
i = 0
j = 0
Fase = "buscar"   # "buscar" | "swap" 

def init(vals):
    global items, n, gap, i, j, Fase
    items = list(vals)
    n = len(items)
    gap = n // 2 #Genera el primer gap
    i = gap
    j = 0
    Fase = "buscar" 

def step():
    global items, n, gap, i, j, Fase

    
    if Fase == "buscar": # Recorremos i desde gap hasta n-1
        if i >= n:
            gap = gap // 2 # Nuevo gap
            if gap == 0:
                
                return {"done": True}
            i = gap
            Fase = "buscar"
            return {"swap": False,"done": False}  

        
        j = i # Inicializamos j para la siguiente fase
        Fase = "swap"
        return {"swap": False, "done": False}

    
    if Fase == "swap": 
        a = j
        b = j - gap

        if b >= 0 and items[a] < items[b]:
            
            items[a], items[b] = items[b], items[a]

            j = b  # Necesario para que se siga desplazando
            return {"a": a, "b": b, "swap": True, "done": False}

        
        i = i + 1
        Fase = "buscar" #Si no hay swap, volvemos a la fase de busqueda.
    
        return {"a": a, "b": b, "swap": False, "done": False}



    
    # TODO: implementar UN micro-paso de tu algoritmo y devolver el dict.
    # Recordá:
    # - a, b dentro de [0, n-1]
    # - si swap=True, primero hacé el intercambio en 'items'
    # - cuando termines, devolvé {"done": True}
    
