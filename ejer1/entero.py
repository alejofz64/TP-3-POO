class Entero:
    def __init__(self, numero):
        self.__numero = numero

    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    def cuadrado(self):
        return self.__numero * self.__numero

    def es_par(self):
        return self.__numero % 2 == 0

    def es_impar(self):
        return not self.es_par()

    def factorial(self):
        # El factorial tradicionalmente no está definido para negativos
        if self.__numero < 0:
            return 0 
        
        resultado = 1
        for i in range(1, self.__numero + 1):
            resultado *= i
        return resultado

    def es_primo(self):
        if self.__numero <= 1:
            return False
            
        # Comprobamos divisibilidad hasta la raíz cuadrada del número
        for i in range(2, int(self.__numero ** 0.5) + 1):
            if self.__numero % i == 0:
                return False
        return True
