import math

class TuringMachine:
    def __init__(self, tape, initial_state, final_states, transition_function):
        self.tape = list(tape) + [' '] * 100  # Relleno
        self.head_position = 0
        self.current_state = initial_state
        self.final_states = final_states
        self.transition_function = transition_function

    def step(self):
        current_symbol = self.tape[self.head_position]
        key = (self.current_state, current_symbol)

        if key in self.transition_function:
            new_state, new_symbol, move_direction = self.transition_function[key]
            self.tape[self.head_position] = new_symbol

            # Mostrar el movimiento
            print(move_direction, end=' ')

            if move_direction == 'R':
                self.head_position += 1
            elif move_direction == 'L':
                self.head_position -= 1

            self.current_state = new_state
        else:
            self.current_state = None

    def run(self):
        print("Movimientos de la cinta:")
        while self.current_state not in self.final_states and self.current_state is not None:
            self.step()
        print("\nFin de ejecución")
        return self.current_state, ''.join(self.tape).strip()


def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def binary_to_decimal(b):
    return int(b, 2)


# Transiciones ficticias para simular movimiento (puedes personalizar después)
def transition_function_generic():
    return {
        ('q0', '1'): ('q0', '1', 'R'),
        ('q0', '0'): ('q0', '0', 'R'),
        ('q0', ' '): ('q1', ' ', 'L'),
    }

def create_arithmetic_tm(operation, num1, num2=None):
    tape = ""
    transitions = {}
    result = None

    if operation == "+":
        result = num1 + num2
        tape = decimal_to_binary(num1) + ' ' + decimal_to_binary(num2)
        transitions = transition_function_generic()
    elif operation == "-":
        result = num1 - num2
        tape = decimal_to_binary(num1) + ' ' + decimal_to_binary(num2)
        transitions = transition_function_generic()
    elif operation == "*":
        result = num1 * num2
        tape = decimal_to_binary(num1) + ' ' + decimal_to_binary(num2)
        transitions = transition_function_generic()
    elif operation == "/":
        if num2 == 0:
            print("Error: División por cero.")
            return None, None
        result = num1 // num2
        tape = decimal_to_binary(num1) + ' ' + decimal_to_binary(num2)
        transitions = transition_function_generic()
    elif operation == "^":
        result = num1 ** num2
        tape = decimal_to_binary(num1) + ' ' + decimal_to_binary(num2)
        transitions = transition_function_generic()
    elif operation == "√":
        result = math.sqrt(num1)
        tape = decimal_to_binary(num1) + ' √'
        transitions = transition_function_generic()
    elif operation == "sin":
        result = math.sin(math.radians(num1))
        tape = decimal_to_binary(num1) + ' sin'
        transitions = transition_function_generic()
    else:
        raise ValueError("Operación no válida")

    tm = TuringMachine(tape.strip(), "q0", {"q1", "q_accept"}, transitions)
    return tm, result


if __name__ == "__main__":
    num1 = int(input("Ingrese el primer número: "))
    operation = input("Ingrese la operación (+, -, *, /, ^, √, sin): ")
    num2 = None
    if operation in ["+", "-", "*", "/", "^"]:
        num2 = int(input("Ingrese el segundo número: "))

    tm, result = create_arithmetic_tm(operation, num1, num2)

    if tm is not None and result is not None:
        final_state, final_tape = tm.run()

        print(f"\n{operation} - Estado final: {final_state}")
        print(f"{operation} - Resultado en decimal: {result}")
        print(f"{operation} - Resultado en binario: {decimal_to_binary(int(result * 1e10)) if isinstance(result, float) else decimal_to_binary(result)}")

