"""
En esta oportunidad vamos a practicar con los packages:
    - numpy
    - pandas
    - matplotlib

NOTA: Si ves una advertencia de que no se encuantran los paquetes `numpy`, `pandas`
o `matplotlib`, ejecuta:

    `uv sync`

NOTA: Los ejercicios de este archivo en adelante son generados por cursor, y están
abiertos a mejoras a través del mecanismo de PRs como todo lo anterior.
"""

# Importaciones necesarias
# from typing import Any
import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Ruta al dataset (relativa al directorio del archivo)
_current_dir = os.path.dirname(os.path.abspath(__file__))
DATASET_PATH = os.path.join(_current_dir, "exercises_5_data", "dataset.csv")

# -----------------------------------------------------------------------------
# EJERCICIOS DE NUMPY
# -----------------------------------------------------------------------------


def numpy_ejercicio_1(arr: np.ndarray) -> float:
    """
    Ejercicio 1: Calcula la media (promedio) de un array de numpy.

    Debe usar la función np.mean() para calcular el promedio de todos los elementos
    del array.

    Args:
        arr: Array de numpy con valores numéricos

    Returns:
        float: La media de todos los elementos del array
    """
    return float(np.mean(arr))


def numpy_ejercicio_2(arr: np.ndarray) -> np.ndarray:
    """
    Ejercicio 2: Crea un array de numpy con valores del 0 al 9 (inclusive).

    Debe usar np.arange() o np.array() para crear un array unidimensional
    con los valores [0, 1, 2, 3, 4, 5, 6, 7, 8, 9].

    Args:
        arr: Este parámetro no se usa, pero debe mantenerse por compatibilidad

    Returns:
        np.ndarray: Array con valores del 0 al 9
    """
    return np.arange(10)


def numpy_ejercicio_3(arr: np.ndarray) -> tuple[int, int]:
    """
    Ejercicio 3: Obtiene la forma (shape) de un array de numpy.

    Debe usar el atributo .shape del array para obtener sus dimensiones.
    Retorna una tupla con (filas, columnas) o (dimensiones).

    Args:
        arr: Array de numpy

    Returns:
        tuple: Tupla con las dimensiones del array (filas, columnas)
    """
    shape = arr.shape
    if len(shape) == 1:
        return (shape[0], 1)
    return (shape[0], shape[1])


def numpy_ejercicio_4(arr: np.ndarray) -> np.ndarray:
    """
    Ejercicio 4: Filtra un array para obtener solo los valores mayores a un umbral.

    Debe usar indexación booleana de numpy para filtrar los elementos.
    Por ejemplo, si el umbral es 5, debe retornar solo los valores > 5.

    Args:
        arr: Array de numpy con valores numéricos

    Returns:
        np.ndarray: Array filtrado con solo los valores mayores a 5
    """
    return arr[arr > 5]

def numpy_ejercicio_5(arr1: np.ndarray, arr2: np.ndarray) -> np.ndarray:
    """
    Ejercicio 5: Suma elemento a elemento dos arrays de numpy.

    Debe usar la operación de suma de numpy (puede ser + o np.add())
    para sumar los arrays elemento por elemento.

    Args:
        arr1: Primer array de numpy
        arr2: Segundo array de numpy (misma forma que arr1)

    Returns:
        np.ndarray: Array resultante de la suma elemento a elemento
    """
    return arr1 + arr2


def numpy_ejercicio_6(arr: np.ndarray) -> np.ndarray:
    """
    Ejercicio 6: Reshape un array unidimensional a una matriz 2D.

    Debe usar np.reshape() para convertir un array 1D en una matriz 2D.
    Por ejemplo, un array de 12 elementos puede convertirse en una matriz 3x4.

    Args:
        arr: Array unidimensional de numpy

    Returns:
        np.ndarray: Array reshapeado a matriz 2D (3 filas x 4 columnas)
    """
    return np.reshape(arr, (3, 4))


def numpy_ejercicio_7(arr: np.ndarray) -> dict[str, float]:
    """
    Ejercicio 7: Calcula múltiples estadísticas de un array.

    Debe calcular la media, desviación estándar, mínimo y máximo de un array
    usando las funciones np.mean(), np.std(), np.min() y np.max().
    Retorna un diccionario con las claves: 'media', 'desviacion', 'minimo', 'maximo'.

    Args:
        arr: Array de numpy con valores numéricos

    Returns:
        dict: Diccionario con las estadísticas calculadas
    """
    return {
        "media": float(np.mean(arr)),
        "desviacion": float(np.std(arr)),
        "minimo": float(np.min(arr)),
        "maximo": float(np.max(arr)),
    }


# -----------------------------------------------------------------------------
# EJERCICIOS DE PANDAS
# -----------------------------------------------------------------------------


def pandas_ejercicio_1() -> pd.DataFrame:
    """
    Ejercicio 1: Carga el dataset CSV en un DataFrame de pandas.

    Debe usar pd.read_csv() para cargar el archivo ubicado en DATASET_PATH.
    Retorna el DataFrame completo.

    Returns:
        pd.DataFrame: DataFrame con los datos del CSV
    """
    return pd.read_csv(DATASET_PATH)


def pandas_ejercicio_2(df: pd.DataFrame) -> int:
    """
    Ejercicio 2: Obtiene el número de filas y columnas del DataFrame.

    Debe usar el atributo .shape del DataFrame para obtener sus dimensiones.
    Retorna solo el número de filas (primer elemento de la tupla shape).

    Args:
        df: DataFrame de pandas

    Returns:
        int: Número de filas en el DataFrame
    """
    return int(df.shape[0])


def pandas_ejercicio_3(df: pd.DataFrame) -> pd.Series:
    """
    Ejercicio 3: Obtiene una columna específica del DataFrame.

    Debe usar la indexación de pandas (df['columna'] o df.columna) para
    obtener la columna 'producto' del DataFrame.

    Args:
        df: DataFrame de pandas

    Returns:
        pd.Series: Serie con los valores de la columna 'producto'
    """
    return df["producto"]


def pandas_ejercicio_4(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ejercicio 4: Filtra el DataFrame para obtener solo filas que cumplan una condición.

    Debe usar indexación booleana (df[condicion]) para filtrar las filas donde
    la columna 'cantidad' sea mayor a 5.

    Args:
        df: DataFrame de pandas

    Returns:
        pd.DataFrame: DataFrame filtrado con solo las filas donde cantidad > 5
    """
    return df.loc[df["cantidad"] > 5]


def pandas_ejercicio_5(df: pd.DataFrame) -> float:
    """
    Ejercicio 5: Calcula el promedio de una columna numérica.

    Debe usar el método .mean() de pandas sobre la columna 'total' del DataFrame.

    Args:
        df: DataFrame de pandas

    Returns:
        float: Promedio de los valores en la columna 'total'
    """
    return float(df["total"].mean())


def pandas_ejercicio_6(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ejercicio 6: Agrupa datos y calcula estadísticas por grupo.

    Debe usar .groupby() para agrupar por la columna 'categoria' y luego
    calcular la suma de la columna 'total' para cada grupo usando .sum().

    Args:
        df: DataFrame de pandas

    Returns:
        pd.DataFrame: DataFrame con los resultados del groupby (categoria y suma de total)
    """
    return df.groupby("categoria")["total"].sum().reset_index()

def pandas_ejercicio_7(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ejercicio 7: Ordena el DataFrame por una columna en orden descendente.

    Debe usar .sort_values() para ordenar el DataFrame por la columna 'total'
    en orden descendente (ascending=False).

    Args:
        df: DataFrame de pandas

    Returns:
        pd.DataFrame: DataFrame ordenado por 'total' de mayor a menor
    """
    return df.sort_values("total", ascending=False)


# -----------------------------------------------------------------------------
# EJERCICIOS DE MATPLOTLIB
# -----------------------------------------------------------------------------


def matplotlib_ejercicio_1(x: list[float], y: list[float]) -> None:
    """
    Ejercicio 1: Crea un gráfico de línea básico.

    Debe usar plt.plot() para crear un gráfico de línea con los datos x e y,
    y luego plt.show() para mostrarlo.

    Args:
        x: Lista de valores para el eje X
        y: Lista de valores para el eje Y
    """
    plt.plot(x, y)
    plt.show()


def matplotlib_ejercicio_2(x: list[float], y: list[float]) -> None:
    """
    Ejercicio 2: Crea un gráfico de línea con título y etiquetas de ejes.

    Debe usar plt.plot() para el gráfico, plt.title() para el título,
    plt.xlabel() y plt.ylabel() para las etiquetas de los ejes,
    y plt.show() para mostrarlo.

    Args:
        x: Lista de valores para el eje X
        y: Lista de valores para el eje Y
    """
    plt.plot(x, y)
    plt.title("Gráfico de línea")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


def matplotlib_ejercicio_3(values: list[float], labels: list[str]) -> None:
    """
    Ejercicio 3: Crea un gráfico de barras.

    Debe usar plt.bar() para crear un gráfico de barras con los valores y etiquetas
    proporcionados, y plt.show() para mostrarlo.

    Args:
        values: Lista de valores para las barras
        labels: Lista de etiquetas para cada barra
    """
    plt.bar(labels, values)
    plt.show()


def matplotlib_ejercicio_4(values: list[float]) -> None:
    """
    Ejercicio 4: Crea un histograma.

    Debe usar plt.hist() para crear un histograma de los valores proporcionados,
    y plt.show() para mostrarlo.

    Args:
        values: Lista de valores para el histograma
    """
    plt.hist(values)
    plt.show()


def matplotlib_ejercicio_5(x: list[float], y1: list[float], y2: list[float]) -> None:
    """
    Ejercicio 5: Crea un gráfico con múltiples líneas.

    Debe usar plt.plot() dos veces para crear dos líneas en el mismo gráfico,
    usar plt.legend() para agregar una leyenda, y plt.show() para mostrarlo.

    Args:
        x: Lista de valores para el eje X
        y1: Lista de valores para la primera línea
        y2: Lista de valores para la segunda línea
    """
    plt.plot(x, y1, label="línea 1")
    plt.plot(x, y2, label="línea 2")
    plt.legend()
    plt.show()


def matplotlib_ejercicio_6(df: pd.DataFrame) -> None:
    """
    Ejercicio 6: Crea un gráfico de barras desde un DataFrame de pandas.

    Debe agrupar el DataFrame por 'categoria' y sumar 'total', luego usar
    plt.bar() para crear el gráfico con las categorías en el eje X y los totales
    en el eje Y. Agregar título y etiquetas de ejes.

    Args:
        df: DataFrame de pandas con columnas 'categoria' y 'total'
    """
    grouped = df.groupby("categoria")["total"].sum()
    plt.bar(grouped.index.tolist(), grouped.values.tolist())
    plt.title("Total por categoría")
    plt.xlabel("Categoría")
    plt.ylabel("Total")
    plt.show()


def matplotlib_ejercicio_7(df: pd.DataFrame) -> None:
    """
    Ejercicio 7: Crea un gráfico de dispersión (scatter plot) con personalización.

    Debe usar plt.scatter() para crear un gráfico de dispersión con 'cantidad' en el eje X
    y 'total' en el eje Y. Agregar título, etiquetas de ejes, y usar plt.show().

    Args:
        df: DataFrame de pandas con columnas 'cantidad' y 'total'
    """
    plt.scatter(df["cantidad"], df["total"])
    plt.title("Cantidad vs Total")
    plt.xlabel("Cantidad")
    plt.ylabel("Total")
    plt.show()
