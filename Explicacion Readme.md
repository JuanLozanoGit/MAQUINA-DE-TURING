import math

# Definimos la clase de la Máquina de Turing
class TuringMachine:
    def __init__(self, tape, initial_state, final_states, transition_function):
        self.tape = list(tape)  # Convertimos la cinta en una lista para modificarla
        self.head_position = 0  # Posición inicial del cabezal
        self.current_state = initial_state  # Estado actual de la máquina
        self.final_states = final_states  # Estados finales de la máquina
        self.transition_function = transition_function  # Tabla de transiciones

    def step(self):
        current_symbol = self.tape[self.head_position]  # Leer el símbolo en la posición del cabezal
        if (self.current_state, current_symbol) in self.transition_function:
            # Obtener la nueva configuración según la función de transición
            new_state, new_symbol, move_direction = self.transition_function[(self.current_state, current_symbol)]
            self.tape[self.head_position] = new_symbol  # Escribir nuevo símbolo en la cinta
            if move_direction == 'R':
                self.head_position += 1  # Mover el cabezal a la derecha
            elif move_direction == 'L':
                self.head_position -= 1  # Mover el cabezal a la izquierda
            self.current_state = new_state  # Actualizar el estado actual
        else:
            self.current_state = None  # Indica que la máquina se detiene

    def run(self):
        # Ejecuta la máquina hasta que llegue a un estado final o no tenga transiciones
        while self.current_state not in self.final_states and self.current_state is not None:
            self.step()
        return self.current_state, ''.join(self.tape)  # Retorna el estado final y la cinta resultante

# Funciones auxiliares para conversión de números binarios y decimales
def decimal_to_binary(n):
    return bin(n).replace("0b", "")  # Convierte un número decimal a binario sin el prefijo '0b'

def binary_to_decimal(b):
    return int(b, 2)  # Convierte un número binario a decimal

# Creación de una Máquina de Turing para operaciones aritméticas
def create_arithmetic_tm(operation, num1, num2=None):
    if operation == "+":
        result = num1 + num2  # Suma
    elif operation == "-":
        result = num1 - num2  # Resta
    elif operation == "*":
        result = num1 * num2  # Multiplicación
    elif operation == "/":
        result = num1 // num2  # División entera
    elif operation == "^":
        result = num1 ** num2  # Potencia
    elif operation == "√":
        result = int(math.sqrt(num1))  # Raíz cuadrada
    elif operation == "sin":
        result = int(math.sin(math.radians(num1)))  # Seno del ángulo en grados
    else:
        raise ValueError("Operación no válida")
    
    tape = decimal_to_binary(num1)  # Convertimos el primer número a binario
    if num2 is not None:
        tape += operation + decimal_to_binary(num2) + " "  # Agregamos el segundo número si aplica
    else:
        tape += operation + " "  # Si es operación unaria, solo agregamos el operador
    
    tm = TuringMachine(tape, "q0", {"q_accept"}, {})  # Creamos la máquina de Turing
    return tm, result

if __name__ == "__main__":
    num1 = int(input("Ingrese el primer número: "))  # Pedimos el primer número al usuario
    operation = input("Ingrese la operación (+, -, *, /, ^, √, sin): ")  # Pedimos la operación deseada
    num2 = None
    if operation in ["+", "-", "*", "/", "^"]:
        num2 = int(input("Ingrese el segundo número: "))  # Pedimos el segundo número si es necesario
    
    tm, result = create_arithmetic_tm(operation, num1, num2)  # Creamos la máquina de Turing
    final_state, final_tape = tm.run()  # Ejecutamos la máquina
    print(f"{operation} - Estado final: {final_state}")  # Mostramos el estado final
    print(f"{operation} - Resultado en binario: {decimal_to_binary(result)}")  # Mostramos el resultado en binario
