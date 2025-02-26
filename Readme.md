TEMAS:
- QUE ES  ANDRES
- FUNCIONAMIENTO   MARIA
- QUE PUEDE HACER  YO
- COMO EJECUTARLO  JULIO
- -AUTORES

**Máquina de Turing para Operaciones Matemáticas**

**¿Qué es?**

Una Máquina de Turing es un modelo teórico de computación que consiste en una cinta infinita, un cabezal de lectura/escritura y un conjunto de reglas de transición que determinan cómo se mueve el cabezal y modifica la cinta. Este modelo se utiliza para simular cualquier algoritmo computacional.

**Funcionamiento**

Esta implementación de la Máquina de Turing usa una cinta representada como una lista de caracteres y un conjunto de transiciones definido por un diccionario. La máquina ejecuta pasos siguiendo estas reglas:

Lee el símbolo actual en la cinta.

Busca la transición correspondiente en la función de transición.

Escribe un nuevo símbolo en la cinta.

Mueve el cabezal a la izquierda (L) o a la derecha (R).

Cambia al nuevo estado.

Repite hasta alcanzar un estado de aceptación o hasta que no haya una transición válida.

**¿Qué puede hacer?**

La Máquina de Turing implementada aquí puede realizar operaciones aritméticas básicas y avanzadas, incluyendo:

Suma (+)

Resta (-)

Multiplicación (*)

División entera (/)

Potenciación (^)

Raíz cuadrada (√)

Seno (sin)

La entrada y salida de los números se manejan en binario para representar la información de forma compacta en la cinta.

**¿Cómo ejecutarlo?**

El programa solicita al usuario ingresar dos números y una operación matemática. Luego:

Convierte los números a binario.

Construye la cinta de la Máquina de Turing.

Ejecuta los pasos de la máquina.

Retorna el resultado en binario y su estado final.

Para ejecutar el código, basta con ejecutar el script en Python:

python turing_machine.py

**Autores**

Este proyecto fue desarrollado como parte de un estudio sobre Máquinas de Turing y su aplicación en operaciones matemáticas utilizando Python.


¿Cómo ejecutarlo?

1️⃣ Descargar el repositorio

**https://github.com/JuanLozanoGit/MAQUINA-DE-TURING/tree/main**

2️⃣ Ejecutar el script

Ejecuta el programa en una terminal de Python:

**taller maquina turing.py**

3️⃣ Interactuar con la máquina

El programa solicitará ingresar un número y una operación matemática. Para operaciones binarias (+, -, *, /, ^), se pedirá un segundo número.
