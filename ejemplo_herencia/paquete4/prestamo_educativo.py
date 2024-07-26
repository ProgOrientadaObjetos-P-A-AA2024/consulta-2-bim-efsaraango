from paquete2.prestamo import Prestamo
from paquete4.institucion_educativa import InstitucionEducativa
from paquete1.persona import Persona

class PrestamoEducativo(Prestamo):
    def __init__(self, beneficiario, meses, ciudad, nivel_estudio, institucion, valor_carrera):
        super().__init__(beneficiario, meses, ciudad)
        self.nivel_estudio = nivel_estudio
        self.institucion = institucion
        self.valor_carrera = valor_carrera
        self.valor_mensual = 0

    def establecer_nivel_estudio(self, nivel_estudio):
        self.nivel_estudio = nivel_estudio

    def establecer_valor_carrera(self, valor_carrera):
        self.valor_carrera = valor_carrera

    def establecer_institucion(self, institucion):
        self.institucion = institucion

    def establecer_valor_mensual(self):
        self.valor_mensual = (self.valor_carrera / self.meses) - (self.valor_carrera - self.meses) * 0.10

    def __str__(self):
        return (f"{super().__str__()}\nNivel de Estudio: {self.nivel_estudio}\n"
                f"Institución: {self.institucion}\n"
                f"Valor de la Carrera: {self.valor_carrera:.2f}\n"
                f"Valor Mensual: {self.valor_mensual:.2f}")
