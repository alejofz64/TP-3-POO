class Empleado:
    
    SALARIO_MINIMO = 202800.0  

    def __init__(self, nombre, dni, sueldo):
        self.__nombre = nombre
        self.__dni = dni
        self.__sueldo = 0.0
        self.set_sueldo(sueldo)

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_dni(self):
        return self.__dni

    def set_dni(self, dni):
        self.__dni = dni

    def get_sueldo(self):
        return self.__sueldo

    def set_sueldo(self, sueldo):
        # Regla de Negocio: El sueldo no puede ser negativo ni menor al SMVM
        if sueldo < self.SALARIO_MINIMO:
            self.__sueldo = self.SALARIO_MINIMO
        else:
            self.__sueldo = sueldo