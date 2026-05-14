from empleado import Empleado
from empresa import Empresa

class Main:
    def ejecutar(self):
        print("=== SISTEMA DE GESTIÓN DE EMPLEADOS ===")
        empresa_actual = Empresa()
        
        while True:
            print("\n-- MENÚ DE OPCIONES --")
            print("1. Registrar nuevo empleado")
            print("2. Ver el empleado que más gana")
            print("3. Ver el sueldo promedio")
            print("4. Salir")
            
            opcion = input("Elija una opción (1-4): ")
            
            if opcion == '1':
                nombre = input("Ingrese el nombre del empleado: ")
                dni = input("Ingrese el DNI del empleado: ")
                entrada_sueldo = input("Ingrese el sueldo: ")
                
                # Validación rudimentaria para cumplir con la regla de 0 excepciones (sin usar try-except)
                if entrada_sueldo.replace('.', '', 1).isdigit():
                    sueldo = float(entrada_sueldo)
                else:
                    print("Entrada de sueldo no válida. Se asignará 0 y el sistema ajustará al Mínimo Vital y Móvil.")
                    sueldo = 0.0
                    
                # Creamos el objeto empleado, el cual internamente aplicará la regla del sueldo mínimo si corresponde
                nuevo_empleado = Empleado(nombre, dni, sueldo)
                
                # Intentamos registrarlo en la empresa
                exito = empresa_actual.registrar_empleado(nuevo_empleado)
                if exito:
                    print(f">> Empleado '{nombre}' registrado existosamente.")
                    print(f">> Sueldo definitivo asignado: ${nuevo_empleado.get_sueldo():.2f}")
                else:
                    print(f">> ERROR: No se pudo registrar. Ya existe un empleado con el DNI: {dni}.")

            elif opcion == '2':
                empleado_top = empresa_actual.empleado_que_mas_gana()
                # La consola de Main es la única responsable de recibir el objeto y mostrar su información
                if empleado_top is not None:
                    print("\n[EMPLEADO CON MAYOR SUELDO]")
                    print(f"Nombre: {empleado_top.get_nombre()}")
                    print(f"DNI: {empleado_top.get_dni()}")
                    print(f"Sueldo: ${empleado_top.get_sueldo():.2f}")
                else:
                    print("No hay ningún empleado registrado por el momento.")
                    
            elif opcion == '3':
                promedio = empresa_actual.sueldo_promedio()
                if promedio > 0:
                    print(f">> El sueldo promedio mensual es: ${promedio:.2f}")
                else:
                    print("No hay empleados registrados para calcular el promedio respectivo.")
                    
            elif opcion == '4':
                print("Saliendo del sistema de gestión...")
                break
                
            else:
                print("Opción inválida. Intente de nuevo.")

# Punto de inicio

app = Main()
app.ejecutar()