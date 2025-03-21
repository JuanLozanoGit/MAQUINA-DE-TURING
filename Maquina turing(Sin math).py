class TuringMachine:
    def __init__(self, tape, initial_state, final_states, transition_function):
        self.tape = list(tape) + [' '] * 100
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
    return bin(int(n)).replace("0b", "")

def binary_to_decimal(b):
    return int(b, 2)

# Raíz cuadrada entera usando búsqueda binaria
def sqrt_integer(n):
    if n < 0:
        raise ValueError("Raíz cuadrada de número negativo no está definida.")
    low, high = 0, n
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid < n:
            low = mid + 1
        else:
            high = mid - 1

# Aproximación de seno usando serie de Taylor (radianes)
def sin_approx(degrees, terms=10):
    x = degrees * 3.141592653589793 / 180  # Convertir a radianes
    result = 0
    for n in range(terms):
        numerator = (-1) ** n * x ** (2 * n + 1)
        denominator = factorial(2 * n + 1)
        result += numerator / denominator
    return result

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Transiciones ficticias
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
        tape = f"{decimal_to_binary(num1)} {decimal_to_binary(num2)}"
    elif operation == "-":
        result = num1 - num2
        tape = f"{decimal_to_binary(num1)} {decimal_to_binary(num2)}"
    elif operation == "*":
        result = num1 * num2
        tape = f"{decimal_to_binary(num1)} {decimal_to_binary(num2)}"
    elif operation == "/":
        if num2 == 0:
            print("Error: División por cero.")
            return None, None
        result = num1 // num2
        tape = f"{decimal_to_binary(num1)} {decimal_to_binary(num2)}"
    elif operation == "^":
        result = num1 ** num2
        tape = f"{decimal_to_binary(num1)} {decimal_to_binary(num2)}"
    elif operation == "√":
        result = sqrt_integer(num1)
        tape = f"{decimal_to_binary(num1)} √"
    elif operation == "sin":
        result = sin_approx(num1)
        tape = f"{decimal_to_binary(num1)} sin"
    else:
        raise ValueError("Operación no válida")

    transitions = transition_function_generic()
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

