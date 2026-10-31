"""Punto 1. Distribuciones discretas y decisiones de respuesta."""
import math


def normalize(weights: dict) -> dict:
    """Retorna un diccionario nuevo cuyas probabilidades suman uno.

    Entrada: weights = {resultado: peso}.
    Salida: {resultado: probabilidad}, con las mismas claves.

    Tips:
    - Conserve las claves y su orden; no modifique weights.
    - Rechace pesos negativos, no finitos, diccionarios vacíos y suma cero.
    """
    # TODO: Add your code here
    respuesta = weights
    if len(respuesta) == 0:
        return None
    if respuesta[0] < 0 or respuesta[0] == None:
        return None
    if respuesta[1] < 0 or respuesta[1] == None:
        return None
    
    suma_total = respuesta[0] + respuesta[1]
    normaliza_0 =  respuesta[0]/suma_total
    normaliza_1 = respuesta[1]/suma_total
    
    respuesta[0] = normaliza_0
    respuesta[1] = normaliza_1

    return respuesta
    # FIN DEL BLOQUE DEL ESTUDIANTE


def expected_utility(distribution: dict, utilities: dict) -> float:
    """Calcula sum_s P(s) U(s) para una acción.

    Entradas: distribution = {resultado: probabilidad} y
    utilities = {resultado: utilidad} para una sola acción.
    Salida: un número con la utilidad esperada.

    Tips:
    - distribution ya debe estar normalizada; no normalice utilidades.
    - Ambas tablas deben contener los mismos resultados posibles.
    """
    # Validación de las entradas; no modificar.
    if set(distribution) != set(utilities) or not distribution:
        raise ValueError("Probabilidades y utilidades deben tener las mismas claves")
    if any(not math.isfinite(p) or p < 0 for p in distribution.values()):
        raise ValueError("Distribución inválida")
    if not math.isclose(sum(distribution.values()), 1, abs_tol=1e-9):
        raise ValueError("La distribución debe sumar uno")
    if any(not math.isfinite(u) for u in utilities.values()):
        raise ValueError("Utilidades no finitas")
    # TODO: Add your code here
    sum_s = (distribution[0]*utilities[0]) + (distribution[1]*utilities[1])
    return sum_s
    raise NotImplementedError("Complete este bloque TODO")
    # FIN DEL BLOQUE DEL ESTUDIANTE


def best_action(distribution: dict, actions: dict) -> tuple[str, dict]:
    """Retorna (nombre de acción, utilidades esperadas por acción).

    Entradas: distribution = {resultado: probabilidad} y
    actions = {acción: {resultado: utilidad}}.
    Salida: (acción elegida, {acción: utilidad esperada}).

    Tips:
    - actions asocia cada acción con su tabla de utilidades.
    - Reutilice expected_utility y conserve la primera acción en los empates.
    """
    # Validación de las acciones; no modificar.
    if not actions:
        raise ValueError("Se requiere al menos una acción")
    # TODO: Add your code here
    max = -9999999999999999999999999999999999
    max_action = ""
    new_dict = {}
    for llave in actions:
        utilidad = expected_utility(distribution, actions[llave])
        if utilidad > max:
            max_action = llave
            max = utilidad
        new_dict[llave] = utilidad
    return max_action, new_dict
    raise NotImplementedError("Complete este bloque TODO")
    # FIN DEL BLOQUE DEL ESTUDIANTE
