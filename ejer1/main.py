from ejer1.entero import Entero

class Main:
    def ejecutar(self):
        print("=== PRUEBA DE CLASE ENTERO ===")
        entrada = input("Ingrese un número entero para comenzar: ")
        
        # Validación básica que no usa try-except
        if entrada.lstrip('-').isdigit():
            numero_inicial = int(entrada)
        else:
            print("Entrada no válida. Se inicializará con 0 por defecto.")
            numero_inicial = 0
            
        # Instanciamos el objeto de nuestra clase de dominio
        entero_obj = Entero(numero_inicial)
        
        while True:
            print("\n-- Menú de Opciones --")
            print(f"Número actual: {entero_obj.get_numero()}")
            print("1. Calcular el cuadrado")
            print("2. Consultar si es par")
            print("3. Consultar si es impar")
            print("4. Calcular el factorial")
            print("5. Consultar si es primo")
            print("6. Cambiar el número")
            print("7. Salir")
            
            opcion = input("Elija una opción (1-7): ")
            
            if opcion == '1':
                print(f"El cuadrado de {entero_obj.get_numero()} es: {entero_obj.cuadrado()}")
            elif opcion == '2':
                if entero_obj.es_par():
                    print("El número ES par.")
                else:
                    print("El número NO es par.")
            elif opcion == '3':
                if entero_obj.es_impar():
                    print("El número ES impar.")
                else:
                    print("El número NO es impar.")
            elif opcion == '4':
                num = entero_obj.get_numero()
                if num < 0:
                    print("El factorial no está definido para números negativos.")
                else:
                    print(f"El factorial de {num} es: {entero_obj.factorial()}")
            elif opcion == '5':
                if entero_obj.es_primo():
                    print("El número ES primo.")
                else:
                    print("El número NO es primo.")
            elif opcion == '6':
                nueva_entrada = input("Ingrese un nuevo número entero: ")
                if nueva_entrada.lstrip('-').isdigit():
                    entero_obj.set_numero(int(nueva_entrada))
                    print("El número ha sido actualizado exitosamente.")
                else:
                    print("Entrada no válida. El número actual NO fue modificado.")
            elif opcion == '7':
                print("Cerrando la aplicación... ¡Adiós!")
                break
            else:
                print("Opción inválida. Intente iterativamente seleccionando un número del 1 al 7.")

# Punto de entrada de la aplicación
app = Main()
app.ejecutar()
