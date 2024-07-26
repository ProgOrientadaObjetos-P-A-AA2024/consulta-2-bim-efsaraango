from paquete2.prestamo import Prestamo
from paquete1.persona import Persona

class PrestamoAutomovil(Prestamo):
    def __init__(self, beneficiario, meses, ciudad, tipo_auto, marca_auto, valor_auto, garante):
        super().__init__(beneficiario, meses, ciudad)
        self.tipo_auto = tipo_auto
        self.marca_auto = marca_auto
        self.valor_auto = valor_auto
        self.garante = garante
        self.valor_mensual = 0

    def establecer_tipo_auto(self, tipo_auto):
        self.tipo_auto = tipo_auto

    def establecer_marca_auto(self, marca_auto):
        self.marca_auto = marca_auto

    def establecer_valor_auto(self, valor_auto):
        self.valor_auto = valor_auto

    def establecer_valor_mensual(self):
        self.valor_mensual = self.valor_auto / self.meses

    def __str__(self):
        return (f"{super().__str__()}\nTipo de Auto: {self.tipo_auto}\n"
                f"Marca de Auto: {self.marca_auto}\n"
                f"Garante: {self.garante}\n"
                f"Valor del Auto: {self.valor_auto:.2f}\n"
                f"Valor Mensual: {self.valor_mensual:.2f}")
