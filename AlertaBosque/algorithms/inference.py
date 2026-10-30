"""Punto 2. Inferencia exacta por enumeración."""
from algorithms.probability import normalize


def enumeration_ask(network, query: str, evidence: dict) -> dict:
    """Calcula P(query | evidence) sobre la conjunta factorizada.

    Entradas: network es la red; query es el nombre de la
    variable consultada; evidence es {nombre de variable: 0 o 1}.
    Salida: {0: probabilidad, 1: probabilidad}.

    Tips:
    - Recorra network.variables en orden topológico.
    - Para una variable fijada multiplique su probabilidad; para una oculta
      sume las dos alternativas 0 y 1. Normalice al terminar.
    - Use copias del evento y no modifique evidence.
    - network.probability(variable, valor, evento) consulta la CPT;
      el evento debe contener los valores de todos los padres.
    - Puede usar una función auxiliar recursiva. Al terminar el recorrido,
      el producto sin factores restantes vale 1.
    - Evidencia imposible: ValueError. Consulta observada: distribución puntual
      solo si la evidencia es posible.
    """
    # Valida nombres de variables y dominio de la evidencia.
    network.validate_query(query, evidence)

    # TODO: Add your code here
    variables = network.variables

    def enumerar(i, evento):
        # ya no quedan variables
        if i == len(variables):
            return 1.0
        var = variables[i]
        if var in evento:
            p = network.probability(var, evento[var], evento)
            return p * enumerar(i + 1, evento)
        else:
            # variable oculta, sumo los dos casos
            suma = 0.0
            for valor in [0, 1]:
                copia = evento.copy()
                copia[var] = valor
                p = network.probability(var, valor, copia)
                suma = suma + p * enumerar(i + 1, copia)
            return suma

    # caso en que la consulta ya esta en la evidencia
    if query in evidence:
        if enumerar(0, evidence.copy()) == 0:
            raise ValueError("La evidencia es imposible")
        if evidence[query] == 1:
            return {0: 0.0, 1: 1.0}
        else:
            return {0: 1.0, 1: 0.0}

    pesos = {}
    for valor in [0, 1]:
        evento = evidence.copy()
        evento[query] = valor
        pesos[valor] = enumerar(0, evento)

    if pesos[0] + pesos[1] == 0:
        raise ValueError("La evidencia es imposible")

    return normalize(pesos)
    # FIN DEL BLOQUE DEL ESTUDIANTE
