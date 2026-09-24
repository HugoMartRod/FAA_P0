import numpy as np

class EstrategiaParticionado:
    """
    Clase base que define la estructura obligatoria para cualquier 
    estrategia de validación futura.
    """
    def __init__(self):
        # Aquí guardaremos una lista de diccionarios: [{"train": [...], "test": [...]}]
        self.particiones = []

    def creaParticiones(self, numero_filas):
        # Este método lo sobreescribirán las clases hijas
        raise NotImplementedError("Este método debe ser implementado por las clases hijas")


class ValidacionSimple(EstrategiaParticionado):
    """
    Implementa la estrategia de validación simple (hold-out).
    """
    def __init__(self, proporcion_test=0.3, numero_ejecuciones=1):
        super().__init__() # Llama al constructor de la clase padre
        self.proporcion_test = proporcion_test
        self.numero_ejecuciones = numero_ejecuciones

    def creaParticiones(self, numero_filas):
        # Limpiamos particiones previas
        self.particiones = []
        
        # En la validación simple es común realizar varias ejecuciones para diferentes permutaciones
        for _ in range(self.numero_ejecuciones):
            # IMPORTANTE: Permutamos los datos para evitar sesgos en la distribución realista de las clases
            indices_aleatorios = np.random.permutation(numero_filas)
            
            # Calculamos el índice exacto donde hacer el corte
            corte = int(numero_filas * (1 - self.proporcion_test))
            
            # Separamos el array de índices permutados en dos bloques
            indices_train = indices_aleatorios[:corte].tolist()
            indices_test = indices_aleatorios[corte:].tolist()
            
            # Guardamos esta partición
            self.particiones.append({"train": indices_train, "test": indices_test})