from abc import ABC, abstractmethod

class PasajeUrbano(ABC):
    def __init__(self, valor_fijo):
        self.valor_fijo = valor_fijo
        self.valor_pasaje = 0
        self.usuario = None
    
    def establecer_persona(self, persona):
        self.usuario = persona

    def obtener_persona(self):
        return self.usuario
    
    def establecer_valor_fijo(self, valor_fijo):
        self.valor_fijo = valor_fijo
    
    def obtener_valor_fijo(self):
        return self.valor_fijo
    
    @abstractmethod
    def establecer_valor_pasaje(self):
        pass
    
    def obtener_valor_pasaje(self):
        return self.valor_pasaje
    
    def __str__(self):
        return (f"Pasajero: {self.usuario.obtener_nombre()}\n"
                f"Cédula: {self.usuario.obtener_cedula()}\n"
                f"Edad: {self.usuario.obtener_edad()}\n"
                f"Valor Pasaje: {self.valor_pasaje:.2f}\n"
                f"---------------------\n")
