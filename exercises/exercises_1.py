from typing import Any, Literal


def primeros_ejercicios() -> Any:
    """
    # Primeros ejercicios

    En futuras clases vamos a aprender/repasar la sintaxis utilizada en este archivo,
    por ahora, vamos a concentrarnos en la resolución de los ejercicios.

    A continuación se presentan una serie de ejercicios en forma de comentarios,
    deberá escribir su respuesta entre el comentario de la consigna y la sentencia
    `# yield`.

    Además deberá "descomentar" la sentencia `yield`

    ejemplo:
        ```python
        # X. Declare una variable `texto` y asígnele el valor `Hola Mundo` de tipo
        #    string.
        text = "Hola Mundo"

        yield text
        ```

    La ejecución de estos ejercicios será automatizada por lo tanto es importante
    respetar los NOMBRES de las consignas, como tampoco modificar el nombre del
    archivo o la función.
    """
    """
    NOTA: el contenido encerrado en comillas invertidas (`) representa código,
    si posa el mouse sobre la declaración *(Shift+K en neovim)* de esta función
    podrá ver como este comentario es formateado, en futuras clases también vamos 
    a hablar de esto.
    """

    # 1. Declare una variable `a` anotada con el tipo entero y asígnele el valor `10`

    a: int = 10
    yield a

    # 2. Asigne a la variable `a` el valor `20`

    a = 20
    yield a

    # 3. Declare una variable `b` anotada con el tipo entero y asígnele el valor `5`

    b: int = 5
    yield b
    # 4. Declare una variable `c` anotada con el tipo decimal (de coma flotante)
    #    y asígnele una expresión que evalúe la suma de `a` y `b` y luego multiplique
    #    esto por 3.14

    c: float = (a + b) * 3.14
    yield c

    # 5. Declare una variable `d` anotada con el tipo booleano y asígnele una expresión
    #    que evalúe si `a` es mayor a `b`

    d: bool = a > b
    yield d

    # 6. Declare una variable `e` y asígnele el valor `Hola` concatenado con `Mundo`
    #    separados por un espacio. Anótela con el tipo string literal `Hola Mundo`
    #    (Esto resultará en que la variable `e` solo podrá contener este string
    #    puntual).
    #    Nota: para este ejercicio necesitará descomentar la importación de `Literal`

    e: Literal["Hola Mundo"] = "Hola" + " " + "Mundo"
    yield e

    # 7. Declare una variable `f` anotada con el tipo lista  de enteros y asígnele una lista
    #    con los valores `1, 2, 3, 4, 5`

    f: list[int] = [1, 2, 3, 4, 5]
    yield f

    # 8. Declare una variable `g` anotada con el tipo diccionario y asígnele un
    #    diccionario con las llaves `a`, `b`, `c` y los valores `1, 2, 3`

    g: dict[str, int] = {'a': 1, 'b': 2, 'c': 3}
    yield g

    # 9. Declare una variable `h` anotada con el tipo tupla y asígnele una tupla
    #    con los valores `1, 2, 3, 4, 5`

    h: tuple[int, int, int, int, int] = (1, 2, 3, 4, 5)
    yield h

    # 10. Declare una variable `i` anotada con el tipo conjunto y asígnele un conjunto
    #     con los valores `1, 2, 3, 4, 5`
    i: set[int] = {1, 2, 3, 4, 5}
    yield i
