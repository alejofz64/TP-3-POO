class Empresa:
    def __init__(self):
        self.__empleados = []

    def registrar_empleado(self, nuevo_empleado):
        # Valida que el DNI no se repita
        for emp in self.__empleados:
            if emp.get_dni() == nuevo_empleado.get_dni():
                return False  # El DNI ya existe, no se registra
        
        # Si termina el bucle y no lo encuentra, lo agregamos
        self.__empleados.append(nuevo_empleado)
        return True

    def empleado_que_mas_gana(self):
        # Si no hay empleados devolvemos vacío (None o null)
        if not self.__empleados:
            return None
        
        # Encontramos al empleado con el mayor sueldo
        empleado_max = self.__empleados[0]
        for emp in self.__empleados[1:]:
            if emp.get_sueldo() > empleado_max.get_sueldo():
                empleado_max = emp
                
        return empleado_max

    def sueldo_promedio(self):
        # Si no hay empleados el promedio es cero
        if not self.__empleados:
            return 0.0
            
        suma_sueldos = 0.0
        for emp in self.__empleados:
            suma_sueldos += emp.get_sueldo()
            
        return suma_sueldos / len(self.__empleados)
