# Trabajo Práctico 1: Engine de Go-moku

## Introducción

[Go-moku](https://es.wikipedia.org/wiki/Go-moku) es un juego de tablero estratégico tradicional. Se juega con piedras negras y blancas en un tablero de Go. El objetivo del juego es ser el primero en alinear cinco de sus propias piedras verticalmente, horizontalmente o diagonalmente.

## Objetivo

El objetivo de este trabajo práctico es desarrollar un agente inteligente capaz de jugar al Go-moku. Se evaluará la eficiencia del agente en términos de su rendimiento durante las partidas de prueba y su habilidad para implementar estrategias de juego avanzadas.

## Rating

Para evaluar el desempeño de los agentes, utilizaremos el sistema de rating Trueskill. Este sistema asigna una puntuación a cada agente en base a los enfrentamientos de cada agente contra los demás participantes.

## Recomendaciones

Antes de comenzar con la implementación de su agente, recomendamos realizar pruebas con un tablero más pequeño para facilitar la identificación y corrección de errores. Por ejemplo un tablero de 3x3 y `num_in_row=3` equivale al tatetí que es fácil debuggear, y tableros más pequeños como 9x9 suelen funcionar mucho mas rápido que uno de 15x15. Además, sugerimos utilizar un profiler durante el desarrollo de su agente. Un profiler puede ayudar a identificar los puntos de su código que consumen más tiempo de procesamiento y, por lo tanto, podría ser de gran utilidad para optimizar su implementación.

## Forma de trabajo

La forma de trabajo para este trabajo práctico será la siguiente:

1. Hacer un fork del repositorio del trabajo práctico en GitHub. Esto creará una copia del repositorio en tu cuenta de GitHub.
1. Clonar el repositorio forked en tu entorno local.
1. Desarrollar el código del agente en tu entorno local.
1. Realiza commits y pushs frecuentes a tu repositorio forked para mantener un registro de tus cambios.
1. Cuando hayas terminado, realiza un pull request desde tu repositorio forked hacia el repositorio original. Esto enviará tu código para su revisión y evaluación.

**Nota:**  La rama que se intente _mergear_ mediante el pull request debe contener exclusivamente el código fuente del agente y ningún otro archivo más. Cualquier _merge conflict_ o archivo extra será calificado negativamente.

## Entregables

El entregable para cada fase será el código del agente desarrollado en Python 3.11 . Asegúrese de que su código esté bien comentado y sea fácil de entender. No es necesario un informe, pero se espera que cualquier decisión de diseño o implementación importante esté claramente explicada en los docstrings y comentarios del código.

### Checkpoint 0: Comprendiendo las interfaces del juego

Para el primer checkpoint, es necesario demostrar que se han entendido las interfaces de juego provistas por la cátedra. Su agente deberá ser capaz de interactuar con la interfaz de juego de [OpenAI Gym/Gymnasium](https://gymnasium.farama.org/) para realizar movimientos válidos al azar en el tablero, es decir movimientos que no impliquen poner una piedra en una posición ocupada.

**Fecha de control**: Domingo 13 de Agosto a las 23:59

### Checkpoint 1: Implementación de Árbol Adversarial y Heurística de Evaluación

Para el segundo checkpoint, es necesario implementar un algoritmo de búsqueda en árbol, junto con una heurística de evaluación para el agente. El agente debería tener al menos 4.17 puntos de rating más que un jugador aleatorio (75.97% win rate) y ser capaz de ejecutar al menos un movimiento por segundo en un hilo de un procesador moderno de gama media y un tablero de 15x15.

**Fecha de control**: Domingo 27 de Agosto a las 23:59

### Entrega Final: Agente Avanzado

Para la entrega final, se espera un agente que implemente al menos dos optimizaciones adicionales a las implementaciones de Minimax y la heurística de evaluación. El agente debería tener al menos 4.17 puntos de rating más que el promedio de los minimax entregados en la etapa anterior (75.97% win rate) y ser capaz de ejecutar al menos un movimiento cada 5 segundos en un hilo de un procesador moderno de gama media y un tablero de 15x15.

Algunas optimizaciones posibles son:

1. **Monte Carlo Tree Search (MCTS)**: Técnica de búsqueda basada en simulación que explora el espacio de estados de forma asimétrica.
1. **Búsqueda quiescente**: Técnica que ayuda a evitar horizontes de búsqueda artificiales al continuar la búsqueda hasta que se alcanza una "posición quiescente".
1. **Tablas de finales**: Base de datos previamente calculada de posiciones finales ganadoras y perdedoras.
1. **Poda del árbol de búsqueda**: Reducir la cantidad de nodos explorados en el árbol de búsqueda.
1. **Iterative deepening**: Técnica que combina la profundidad limitada de búsqueda con un enfoque de primero en profundidad para obtener un algoritmo de búsqueda completo y óptimo.
1. **Tablas de Transposición**: Almacenar los resultados de los cálculos previos para reutilizarlos cuando sea posible. (no superar los 256MB de almacenamiento en caché)
1. **Otras optimizaciones**: Más optimizaciones vistas en clase son bienvenidas y serán tenidas en cuenta al momento de la evaluación.

**Fecha de entrega**: Domingo 3 de Septiembre a las 23:59

### Entregas continuas

Durante el desarrollo del trabajo práctico, el repositorio estará disponible para hacer entregas continuas de los agentes mediante PRs para que sean evaluados periódicamente contra los demás agentes. Esto permitirá evaluar el desempeño de los agentes y realizar ajustes en el código para mejorar su rendimiento.

## Especificaciones

### Interfaz de juego

Se debe crear una carpeta con el apellido del alumno como en el ejemplo `scripts/agents/turing`. Dentro de esta carpeta se debe crear un archivo `agent.py` que contenga la implementación del agente descrita a continuación. En esa misma carpeta se pueden agregar otros archivos que contengan código auxiliar.

Se debe implementar una clase con al menos los siguientes métodos:

```python
agent.action(obs)
agent.name() # Diccionario con nombre apellido y legajo del alumno
agent.__str__() # Nombre del agente (elijan lo que quieran)
```

Estos métodos se utilizarán de la siguiente manera:

```python
import gymnasium as gym
import gomoku_udesa
from agents.turing.agent import TuringAgent

env = gym.make('gomoku_udesa/Gomoku-v0', render_mode='human')
board,info = env.reset()
agent = TuringAgent()
print(agent.name())
print(str(agent))
```

```sh
>> {nombre:'Alan', apellido:'Turing', legajo:123456}
>> Tree-Runner 2049
```

```python
terminated, truncated = False, False
while not terminated and not truncated:
    action = agent.action(board)
    board, reward, terminated, truncated, info = env.step(action)
```
**Nota:** Se pondrá un límite duro al tiempo de ejecución de cada movimiento de 5 segundos, lo mismo para el constructor del agente. Si el agente no devuelve un movimiento dentro de ese tiempo, perderá la partida.

## Evaluación

El trabajo será evaluado en tres dimensiones:

1. **Correctitud de las implementaciones**: Verificación de que las implementaciones se ajustan a las especificaciones y realizan las tareas requeridas.
2. **Rendimiento del agente**: Durante el torneo organizado por la cátedra, se le asignará un rating a los agentes basado en su desempeño. El rating será calculado utilizando el sistema [TrueSkill](https://www.microsoft.com/en-us/research/project/trueskill-ranking-system/) en un torneo de tipo suizo.
3. **Calidad del código y documentación**: Se evaluará la legibilidad, modularidad y calidad general del código, así como la documentación adjunta en forma de comentarios.


El primer checkpoint debe estar aprobada para poder entregar el TP.

Para el segundo checkpoint se espera que cumplan con el objetivo antes mencionado. Si no lo cumplieran se restará entre 0 y 1 punto de la nota final. 

La nota final será calculada utilizando la siguiente fórmula:

$`
Nota = 2 \times \text{implementaciones} + 2 \times \text{calidad\_y\_documentacion} + 6 \times \frac{(\text{Rating} - \text{Rating\_min})}{(\text{Rating\_max} - \text{Rating\_min})}
`$

Donde `Rating` es el rating del agente, `Rating_min` es el rating de un agente que juega de manera aleatoria y `Rating_max` es el rating más alto de cualquier agente en el torneo.

Se proporcionarán más detalles acerca de las expectativas de cada checkpoint y la entrega final durante las clases. Este trabajo debe ser realizado individualmente. ¡Buena suerte!
