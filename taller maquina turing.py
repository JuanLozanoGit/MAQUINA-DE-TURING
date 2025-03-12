import math

class TuringMachine:
    def __init__(self, tape, initial_state, final_states, transition_function):
        self.tape = list(tape)
        self.head_position = 0
        self.current_state = initial_state
        self.final_states = final_states
        self.transition_function = transition_function

    def step(self):
        current_symbol = self.tape[self.head_position]
        if (self.current_state, current_symbol) in self.transition_function:
            new_state, new_symbol, move_direction = self.transition_function[(self.current_state, current_symbol)]
            self.tape[self.head_position] = new_symbol
            if move_direction == 'R':
                self.head_position += 1
            elif move_direction == 'L':
                self.head_position -= 1
            self.current_state = new_state
        else:
            self.current_state = None

    def run(self):
        while self.current_state not in self.final_states and self.current_state is not None:
            self.step()
        return self.current_state, ''.join(self.tape)


def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def binary_to_decimal(b):
    return int(b, 2)


def create_arithmetic_tm(operation, num1, num2=None):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        result = num1 // num2
    elif operation == "^":
        result = num1 ** num2
    elif operation == "√":
        result = int(math.sqrt(num1))
    elif operation == "sin":
        result = int(math.sin(math.radians(num1)))
    else:
        raise ValueError("Operación no válida")
    
    tape = decimal_to_binary(num1)
    if num2 is not None:
        tape += operation + decimal_to_binary(num2) + " "
    else:
        tape += operation + " "
    
    tm = TuringMachine(tape, "q0", {"q_accept"}, {})
    return tm, result


if __name__ == "__main__":
    num1 = int(input("Ingrese el primer número: "))
    operation = input("Ingrese la operación (+, -, *, /, ^, √, sin): ")
    num2 = None
    if operation in ["+", "-", "*", "/", "^"]:
        num2 = int(input("Ingrese el segundo número: "))
    
    tm, result = create_arithmetic_tm(operation, num1, num2)
    final_state, final_tape = tm.run()
    print(f"{operation} - Estado final: {final_state}")
    print(f"{operation} - Resultado en binario: {decimal_to_binary(result)}")
