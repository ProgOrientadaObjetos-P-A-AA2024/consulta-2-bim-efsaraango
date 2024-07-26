class InstitucionEducativa:
    def __init__(self, nombre_inst, siglas):
        self.nombre_inst = nombre_inst
        self.siglas = siglas

    def establecer_nombre_inst(self, nombre_inst):
        self.nombre_inst = nombre_inst

    def establecer_siglas(self, siglas):
        self.siglas = siglas

    def obtener_nombre_inst(self):
        return self.nombre_inst

    def obtener_siglas(self):
        return self.siglas

    def __str__(self):
        return f"{self.nombre_inst} ({self.siglas})"
