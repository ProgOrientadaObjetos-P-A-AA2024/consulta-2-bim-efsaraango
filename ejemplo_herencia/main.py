from paquete1.persona import Persona
from paquete2.prestamo import Prestamo
from paquete3.prestamo_automovil import PrestamoAutomovil
from paquete4.institucion_educativa import InstitucionEducativa
from paquete4.prestamo_educativo import PrestamoEducativo

def main():
    import locale
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    automoviles = []
    educativos = []
    bandera = True

    while bandera:
        nombre = input("Ingrese el nombre del beneficiario: ")
        apellido = input("Ingrese el apellido del beneficiario: ")
        id = input("Ingrese la identificación: ")
        beneficiario = Persona(nombre, apellido, id)

        meses = int(input("Ingrese la cantidad de meses: "))
        ciudad = input("Ingrese la ciudad del préstamo: ")

        opc = int(input("Ingrese 1 si desea un Préstamo Automóvil o 2 si desea un Préstamo Educativo: "))

        if opc == 1:
            tipo_auto = input("Ingrese el tipo de auto: ")
            marca_auto = input("Ingrese la marca del auto: ")
            nombre_g = input("Ingrese el nombre del garante: ")
            apellido_g = input("Ingrese el apellido del garante: ")
            id_g = input("Ingrese la identificación del garante: ")
            garante = Persona(nombre_g, apellido_g, id_g)
            valor_auto = float(input("Ingrese el valor del auto: "))
            prestamo_a = PrestamoAutomovil(beneficiario, meses, ciudad, tipo_auto, marca_auto, valor_auto, garante)
            automoviles.append(prestamo_a)
        elif opc == 2:
            nivel_estudio = input("Ingrese su nivel de estudio: ")
            valor_carrera = float(input("Ingrese el valor de la carrera: "))
            nombre_insti = input("Ingrese el nombre de su institución educativa: ")
            siglas = input("Ingrese las siglas de la institución: ")
            institucion = InstitucionEducativa(nombre_insti, siglas)
            prestamo_e = PrestamoEducativo(beneficiario, meses, ciudad, nivel_estudio, institucion, valor_carrera)
            educativos.append(prestamo_e)

        aux = input("Ingrese n para salir del ciclo: ")
        if aux.lower() == 'n':
            bandera = False

    for i, prestamo in enumerate(automoviles):
        prestamo.establecer_valor_mensual()
        print(f"Préstamo Automóvil {i + 1}:\n{prestamo}")

    for i, prestamo in enumerate(educativos):
        prestamo.establecer_valor_mensual()
        print(f"Préstamo Educativo {i + 1}:\n{prestamo}")

if __name__ == "__main__":
    main()