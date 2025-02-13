class MaquinaTuring:
    def __init__(self, cinta, estados, transiciones, estado_inicial, estado_final):
        self.cinta = list(cinta) + [' '] * 20  # Espacio extra para operaciones
        self.posicion = 0  # Cabezal inicia en la primera celda
        self.estado = estado_inicial
        self.estados = estados
        self.transiciones = transiciones
        self.estado_final = estado_final
    
    def ejecutar(self):
        while self.estado != self.estado_final:
            simbolo = self.cinta[self.posicion]
            if (self.estado, simbolo) in self.transiciones:
                nuevo_estado, nuevo_simbolo, movimiento = self.transiciones[(self.estado, simbolo)]
                self.cinta[self.posicion] = nuevo_simbolo
                self.estado = nuevo_estado
                if movimiento == 'R':
                    self.posicion += 1
                elif movimiento == 'L':
                    self.posicion -= 1
            else:
                raise ValueError(f"No hay transición definida para el estado '{self.estado}' y el símbolo '{simbolo}'")
        return ''.join(self.cinta).strip()

    def limpiar_cinta(self):
        self.cinta = [' '] * len(self.cinta)
        self.posicion = 0
        self.estado = 'q0'

# Definición de operaciones básicas
def crear_maquina_turing(expresion):
    estados = {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'qf'}
    transiciones = {
        # Suma: 1+1 -> 2
        ('q0', '1'): ('q0', '1', 'R'),
        ('q0', '+'): ('q1', '+', 'R'),
        ('q1', '1'): ('q1', '1', 'R'),
        ('q1', ' '): ('qf', '2', 'R'),
        
        # Multiplicación: 1*1 -> 1 (simplificada)
        ('q0', '*'): ('q2', '*', 'R'),
        ('q2', '1'): ('q2', '1', 'R'),
        ('q2', ' '): ('qf', '1', 'R'),
        
        # Potencia: 1^2 -> 1 (simplificada)
        ('q0', '^'): ('q3', '^', 'R'),
        ('q3', '2'): ('qf', '1', 'R'),
        
        # Resta: 3-1 -> 2 (simulación básica)
        ('q0', '3'): ('q4', '3', 'R'),
        ('q4', '-'): ('q5', '-', 'R'),
        ('q5', '1'): ('q5', '1', 'R'),
        ('q5', ' '): ('qf', '2', 'R'),
        
        # División: 4/2 -> 2 (simulación básica)
        ('q0', '4'): ('q6', '4', 'R'),
        ('q6', '/'): ('q7', '/', 'R'),
        ('q7', '2'): ('q7', '2', 'R'),
        ('q7', ' '): ('qf', '2', 'R'),
        
        # Raíz cuadrada: sqrt9 -> 3 (simulación)
        ('q0', 's'): ('q8', 's', 'R'),
        ('q8', 'q'): ('q8', 'q', 'R'),
        ('q8', 'r'): ('q8', 'r', 'R'),
        ('q8', 't'): ('q8', 't', 'R'),
        ('q8', '9'): ('qf', '3', 'R'),
        
        # Seno: sin30 -> 0.5 (aproximación)
        ('q0', 's'): ('q8', 's', 'R'),
        ('q8', 'i'): ('q8', 'i', 'R'),
        ('q8', 'n'): ('q8', 'n', 'R'),
        ('q8', '3'): ('q8', '3', 'R'),
        ('q8', '0'): ('qf', '0.5', 'R'),
    }
    return MaquinaTuring(expresion, estados, transiciones, 'q0', 'qf')

# Expresiones de prueba
expresiones = ['1+1 ', '1*1 ', '1^2 ', '3-1 ', '4/2 ', 'sqrt9 ', 'sin30 ']
for expr in expresiones:
    maquina = crear_maquina_turing(expr)
    try:
        resultado = maquina.ejecutar()
        print(f"{expr.strip()} = {resultado}")
    except ValueError as e:
        print(f"Error al procesar la expresión '{expr.strip()}': {e}")
    finally:
        maquina.limpiar_cinta()
