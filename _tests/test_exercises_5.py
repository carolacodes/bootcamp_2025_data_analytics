"""
Tests para exercises_5.py - Ejercicios de numpy, pandas y matplotlib
"""

import re

import numpy as np
import pandas as pd

from _utilities import get_annotations_and_rvalues
from exercises import exercises_5 as mod

# -----------------------------------------------------------------------------
# TESTS DE NUMPY
# -----------------------------------------------------------------------------


def test_numpy_ejercicio_1():
    """Test para numpy_ejercicio_1: calcular la media de un array"""
    try:
        func = mod.numpy_ejercicio_1  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `numpy_ejercicio_1`"

    # Test de funcionamiento
    arr1 = np.array([1, 2, 3, 4, 5])
    result1 = func(arr1)
    assert (
        result1 == 3.0
    ), f"La media de [1,2,3,4,5] debería ser 3.0, pero se obtuvo {result1}"

    arr2 = np.array([10, 20, 30])
    result2 = func(arr2)
    assert (
        result2 == 20.0
    ), f"La media de [10,20,30] debería ser 20.0, pero se obtuvo {result2}"

    # Test de consignas
    if (src := source["_source"]) is not None:
        assert ".mean" in src, "Debe usar np.mean() para calcular la media"
    else:
        assert False, "No se pudo obtener el código fuente de la función"


def test_numpy_ejercicio_2():
    """Test para numpy_ejercicio_2: crear array del 0 al 9"""
    try:
        func = mod.numpy_ejercicio_2  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `numpy_ejercicio_2`"

    # Test de funcionamiento
    result = func(np.array([]))
    expected = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert np.array_equal(
        result, expected
    ), f"Debería retornar [0,1,2,3,4,5,6,7,8,9], pero se obtuvo {result}"

    # Test de consignas
    if (src := source["_source"]) is not None:
        assert (
            ".arange" in src or ".array" in src
        ), "Debe usar np.arange() o np.array() para crear el array"
    else:
        assert False, "No se pudo obtener el código fuente de la función"


def test_numpy_ejercicio_3():
    """Test para numpy_ejercicio_3: obtener la forma de un array"""
    try:
        func = mod.numpy_ejercicio_3  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `numpy_ejercicio_3`"

    # Test de funcionamiento
    arr1 = np.array([1, 2, 3, 4, 5])
    result1 = func(arr1)
    assert result1 == (
        5,
    ), f"La forma de un array 1D de 5 elementos debería ser (5,), pero se obtuvo {result1}"

    arr2 = np.array([[1, 2], [3, 4], [5, 6]])
    result2 = func(arr2)
    assert result2 == (
        3,
        2,
    ), f"La forma de una matriz 3x2 debería ser (3, 2), pero se obtuvo {result2}"

    # Test de consignas
    if (src := source["_source"]) is not None:
        assert (
            ".shape" in src
        ), "Debe usar el atributo .shape para obtener las dimensiones"
    else:
        assert False, "No se pudo obtener el código fuente de la función"


def test_numpy_ejercicio_4():
    """Test para numpy_ejercicio_4: filtrar array con valores mayores a 5"""
    try:
        func = mod.numpy_ejercicio_4  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `numpy_ejercicio_4`"

    # Test de funcionamiento
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result = func(arr)
    expected = np.array([6, 7, 8, 9, 10])
    assert np.array_equal(
        result, expected
    ), f"Debería retornar [6,7,8,9,10], pero se obtuvo {result}"

    arr2 = np.array([1, 2, 3])
    result2 = func(arr2)
    assert len(result2) == 0, "No debería haber valores mayores a 5 en [1,2,3]"

    # Test de consignas
    if (src := source["_source"]) is not None:
        # Buscar patrones de indexación booleana: arr[arr > ...], arr[condicion], etc.
        # Buscar arr[ seguido de alguna condición con >
        has_boolean_indexing = bool(
            re.search(r"arr\s*\[\s*arr\s*>", src)
            or re.search(r"arr\s*\[\s*\w+\s*>", src)
            or re.search(r"arr\s*\[\s*[^]]*>\s*5", src)
        )
        assert (
            has_boolean_indexing
        ), "Debe usar indexación booleana para filtrar (arr[arr > 5] o similar)"
    else:
        assert False, "No se pudo obtener el código fuente de la función"


def test_numpy_ejercicio_5():
    """Test para numpy_ejercicio_5: sumar dos arrays elemento a elemento"""
    try:
        func = mod.numpy_ejercicio_5  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `numpy_ejercicio_5`"

    # Test de funcionamiento
    arr1 = np.array([1, 2, 3])
    arr2 = np.array([4, 5, 6])
    result = func(arr1, arr2)
    expected = np.array([5, 7, 9])
    assert np.array_equal(
        result, expected
    ), f"La suma debería ser [5,7,9], pero se obtuvo {result}"

    arr3 = np.array([10, 20])
    arr4 = np.array([30, 40])
    result2 = func(arr3, arr4)
    expected2 = np.array([40, 60])
    assert np.array_equal(
        result2, expected2
    ), f"La suma debería ser [40,60], pero se obtuvo {result2}"

    # Test de consignas
    if (src := source["_source"]) is not None:
        assert (
            "arr1+arr2" in src.replace(" ", "") or ".add" in src
        ), "Debe usar + o np.add() para sumar los arrays"
    else:
        assert False, "No se pudo obtener el código fuente de la función"


def test_numpy_ejercicio_6():
    """Test para numpy_ejercicio_6: reshape array a matriz 3x4"""
    try:
        func = mod.numpy_ejercicio_6  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `numpy_ejercicio_6`"

    # Test de funcionamiento
    arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    result = func(arr)
    assert result.shape == (
        3,
        4,
    ), f"La forma debería ser (3, 4), pero se obtuvo {result.shape}"
    assert np.array_equal(
        result[0], np.array([0, 1, 2, 3])
    ), "La primera fila es incorrecta"

    # Test de consignas
    if (src := source["_source"]) is not None:
        assert ".reshape" in src, "Debe usar np.reshape() para convertir el array"
    else:
        assert False, "No se pudo obtener el código fuente de la función"


def test_numpy_ejercicio_7():
    """Test para numpy_ejercicio_7: calcular múltiples estadísticas"""
    try:
        func = mod.numpy_ejercicio_7  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `numpy_ejercicio_7`"

    # Test de funcionamiento
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result = func(arr)

    assert isinstance(result, dict), "Debe retornar un diccionario"
    assert "media" in result, "El diccionario debe contener la clave 'media'"
    assert "desviacion" in result, "El diccionario debe contener la clave 'desviacion'"
    assert "minimo" in result, "El diccionario debe contener la clave 'minimo'"
    assert "maximo" in result, "El diccionario debe contener la clave 'maximo'"

    assert (
        abs(result["media"] - 5.5) < 0.01
    ), f"La media debería ser aproximadamente 5.5, pero se obtuvo {result['media']}"
    assert (
        result["minimo"] == 1
    ), f"El mínimo debería ser 1, pero se obtuvo {result['minimo']}"
    assert (
        result["maximo"] == 10
    ), f"El máximo debería ser 10, pero se obtuvo {result['maximo']}"

    # Test de consignas
    if (src := source["_source"]) is not None:
        assert ".mean" in src, "Debe usar np.mean() para calcular la media"
        assert ".std" in src, "Debe usar np.std() para calcular la desviación estándar"
        assert ".min" in src, "Debe usar np.min() para calcular el mínimo"
        assert ".max" in src, "Debe usar np.max() para calcular el máximo"
    else:
        assert False, "No se pudo obtener el código fuente de la función"


# -----------------------------------------------------------------------------
# TESTS DE PANDAS
# -----------------------------------------------------------------------------


def test_pandas_ejercicio_1():
    """Test para pandas_ejercicio_1: cargar CSV en DataFrame"""
    try:
        func = mod.pandas_ejercicio_1  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `pandas_ejercicio_1`"

    # Test de funcionamiento
    result = func()

    assert isinstance(result, pd.DataFrame), "Debe retornar un DataFrame"
    assert len(result) > 0, "El DataFrame no debería estar vacío"
    assert (
        "producto" in result.columns
    ), "El DataFrame debe contener la columna 'producto'"
    assert (
        "categoria" in result.columns
    ), "El DataFrame debe contener la columna 'categoria'"
    assert (
        "cantidad" in result.columns
    ), "El DataFrame debe contener la columna 'cantidad'"
    assert "total" in result.columns, "El DataFrame debe contener la columna 'total'"

    # Test de consignas
    if (src := source["_source"]) is not None:
        assert ".read_csv" in src, "Debe usar pd.read_csv() para cargar el archivo CSV"
    else:
        assert False, "No se pudo obtener el código fuente de la función"


def test_pandas_ejercicio_2():
    """Test para pandas_ejercicio_2: obtener número de filas"""
    try:
        func = mod.pandas_ejercicio_2  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `pandas_ejercicio_2`"

    # Test de funcionamiento
    df1 = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    result1 = func(df1)
    assert (
        result1 == 3
    ), f"Un DataFrame con 3 filas debería retornar 3, pero se obtuvo {result1}"

    df2 = pd.DataFrame({"x": [1], "y": [2]})
    result2 = func(df2)
    assert (
        result2 == 1
    ), f"Un DataFrame con 1 fila debería retornar 1, pero se obtuvo {result2}"

    # Test de consignas
    if (src := source["_source"]) is not None:
        assert (
            ".shape" in src
        ), "Debe usar el atributo .shape para obtener las dimensiones"
    else:
        assert False, "No se pudo obtener el código fuente de la función"


def test_pandas_ejercicio_3():
    """Test para pandas_ejercicio_3: obtener columna 'producto'"""
    try:
        func = mod.pandas_ejercicio_3  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `pandas_ejercicio_3`"

    # Test de funcionamiento
    df = pd.DataFrame(
        {
            "producto": ["Laptop", "Mouse", "Teclado"],
            "categoria": ["Electrónica", "Accesorios", "Accesorios"],
        }
    )
    result = func(df)

    assert isinstance(result, pd.Series), "Debe retornar una Serie"
    assert len(result) == 3, "La serie debe tener 3 elementos"
    assert result.iloc[0] == "Laptop", "El primer elemento debería ser 'Laptop'"

    # Test de consignas
    if (src := source["_source"]) is not None:
        assert (
            "['producto']" in src or '["producto"]' in src or ".producto" in src
        ), "Debe usar indexación de pandas (df['producto'] o df.producto) para obtener la columna"
    else:
        assert False, "No se pudo obtener el código fuente de la función"


def test_pandas_ejercicio_4():
    """Test para pandas_ejercicio_4: filtrar filas donde cantidad > 5"""
    try:
        func = mod.pandas_ejercicio_4  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `pandas_ejercicio_4`"

    # Test de funcionamiento
    df = pd.DataFrame(
        {
            "producto": ["A", "B", "C", "D"],
            "cantidad": [3, 6, 7, 2],
            "total": [100, 200, 300, 400],
        }
    )
    result = func(df)

    assert isinstance(result, pd.DataFrame), "Debe retornar un DataFrame"
    assert len(result) == 2, "Debería haber 2 filas con cantidad > 5"
    assert all(result["cantidad"] > 5), "Todas las filas deben tener cantidad > 5"

    # Test de consignas
    if (src := source["_source"]) is not None:
        assert (
            "df[" in src and ">" in src and "cantidad" in src
        ), "Debe usar indexación booleana (df[condicion]) para filtrar las filas"
    else:
        assert False, "No se pudo obtener el código fuente de la función"


def test_pandas_ejercicio_5():
    """Test para pandas_ejercicio_5: calcular promedio de columna 'total'"""
    try:
        func = mod.pandas_ejercicio_5  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `pandas_ejercicio_5`"

    # Test de funcionamiento
    df = pd.DataFrame({"producto": ["A", "B", "C"], "total": [100, 200, 300]})
    result = func(df)

    assert (
        result == 200.0
    ), f"El promedio de [100, 200, 300] debería ser 200.0, pero se obtuvo {result}"

    df2 = pd.DataFrame({"producto": ["X", "Y"], "total": [50, 150]})
    result2 = func(df2)
    assert (
        result2 == 100.0
    ), f"El promedio de [50, 150] debería ser 100.0, pero se obtuvo {result2}"

    # Test de consignas
    if (src := source["_source"]) is not None:
        assert ".mean" in src, "Debe usar el método .mean() para calcular el promedio"
    else:
        assert False, "No se pudo obtener el código fuente de la función"


def test_pandas_ejercicio_6():
    """Test para pandas_ejercicio_6: agrupar por categoría y sumar total"""
    try:
        func = mod.pandas_ejercicio_6  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `pandas_ejercicio_6`"

    # Test de funcionamiento
    df = pd.DataFrame(
        {
            "categoria": ["Electrónica", "Accesorios", "Electrónica", "Accesorios"],
            "total": [100, 200, 150, 250],
        }
    )
    result = func(df)

    assert isinstance(result, pd.DataFrame), "Debe retornar un DataFrame"
    assert (
        "categoria" in result.index or "categoria" in result.columns
    ), "Debe contener la columna 'categoria'"
    assert (
        "total" in result.columns or "total" in result.index
    ), "Debe contener la columna 'total'"

    # Verificar que la suma de Electrónica es 250 y Accesorios es 450
    if "categoria" in result.index:
        assert (
            result.loc["Electrónica", "total"] == 250
        ), "La suma de Electrónica debería ser 250"
        assert (
            result.loc["Accesorios", "total"] == 450
        ), "La suma de Accesorios debería ser 450"

    # Test de consignas
    if (src := source["_source"]) is not None:
        assert ".groupby" in src, "Debe usar .groupby() para agrupar por categoría"
        assert ".sum" in src, "Debe usar .sum() para calcular la suma de total"
    else:
        assert False, "No se pudo obtener el código fuente de la función"


def test_pandas_ejercicio_7():
    """Test para pandas_ejercicio_7: ordenar DataFrame por 'total' descendente"""
    try:
        func = mod.pandas_ejercicio_7  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `pandas_ejercicio_7`"

    # Test de funcionamiento
    df = pd.DataFrame({"producto": ["A", "B", "C"], "total": [100, 300, 200]})
    result = func(df)

    assert isinstance(result, pd.DataFrame), "Debe retornar un DataFrame"
    assert len(result) == 3, "Debe mantener todas las filas"
    assert (
        result.iloc[0]["total"] == 300
    ), "La primera fila debe tener el total más alto (300)"
    assert (
        result.iloc[1]["total"] == 200
    ), "La segunda fila debe tener el total medio (200)"
    assert (
        result.iloc[2]["total"] == 100
    ), "La tercera fila debe tener el total más bajo (100)"

    # Test de consignas
    if (src := source["_source"]) is not None:
        assert (
            ".sort_values" in src
        ), "Debe usar .sort_values() para ordenar el DataFrame"
    else:
        assert False, "No se pudo obtener el código fuente de la función"


# -----------------------------------------------------------------------------
# TESTS DE MATPLOTLIB
# -----------------------------------------------------------------------------


def test_matplotlib_ejercicio_1():
    """Test para matplotlib_ejercicio_1: crear gráfico de línea básico"""
    try:
        func = mod.matplotlib_ejercicio_1  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `matplotlib_ejercicio_1`"

    # Test de funcionamiento
    x: list[float] = [1.0, 2.0, 3.0, 4.0, 5.0]
    y: list[float] = [2.0, 4.0, 6.0, 8.0, 10.0]

    # La función no retorna nada, solo verificar que no lance error
    try:
        func(x, y)
    except Exception as e:
        assert False, f"La función debería ejecutarse sin errores, pero lanzó: {e}"

    # Test de consignas
    if (src := source["_source"]) is not None:
        assert ".plot" in src, "Debe usar plt.plot() para crear el gráfico de línea"
        assert ".show" in src, "Debe usar plt.show() para mostrar el gráfico"
    else:
        assert False, "No se pudo obtener el código fuente de la función"


def test_matplotlib_ejercicio_2():
    """Test para matplotlib_ejercicio_2: gráfico con título y etiquetas"""
    try:
        func = mod.matplotlib_ejercicio_2  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `matplotlib_ejercicio_2`"

    # Test de funcionamiento
    x: list[float] = [1.0, 2.0, 3.0]
    y: list[float] = [1.0, 4.0, 9.0]

    try:
        func(x, y)
    except Exception as e:
        assert False, f"La función debería ejecutarse sin errores, pero lanzó: {e}"

    # Test de consignas
    if (src := source["_source"]) is not None:
        assert ".plot" in src, "Debe usar plt.plot() para crear el gráfico"
        assert ".title" in src, "Debe usar plt.title() para el título"
        assert ".xlabel" in src, "Debe usar plt.xlabel() para la etiqueta del eje X"
        assert ".ylabel" in src, "Debe usar plt.ylabel() para la etiqueta del eje Y"
        assert ".show" in src, "Debe usar plt.show() para mostrar el gráfico"
    else:
        assert False, "No se pudo obtener el código fuente de la función"


def test_matplotlib_ejercicio_3():
    """Test para matplotlib_ejercicio_3: crear gráfico de barras"""
    try:
        func = mod.matplotlib_ejercicio_3  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `matplotlib_ejercicio_3`"

    # Test de funcionamiento
    values: list[float] = [10.0, 20.0, 30.0, 40.0]
    labels: list[str] = ["A", "B", "C", "D"]

    try:
        func(values, labels)
    except Exception as e:
        assert False, f"La función debería ejecutarse sin errores, pero lanzó: {e}"

    # Test de consignas
    if (src := source["_source"]) is not None:
        assert ".bar" in src, "Debe usar plt.bar() para crear el gráfico de barras"
        assert ".show" in src, "Debe usar plt.show() para mostrar el gráfico"
    else:
        assert False, "No se pudo obtener el código fuente de la función"


def test_matplotlib_ejercicio_4():
    """Test para matplotlib_ejercicio_4: crear histograma"""
    try:
        func = mod.matplotlib_ejercicio_4  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `matplotlib_ejercicio_4`"

    # Test de funcionamiento
    values: list[float] = [1.0, 2.0, 2.0, 3.0, 3.0, 3.0, 4.0, 4.0, 5.0]

    try:
        func(values)
    except Exception as e:
        assert False, f"La función debería ejecutarse sin errores, pero lanzó: {e}"

    # Test de consignas
    if (src := source["_source"]) is not None:
        assert ".hist" in src, "Debe usar plt.hist() para crear el histograma"
        assert ".show" in src, "Debe usar plt.show() para mostrar el gráfico"
    else:
        assert False, "No se pudo obtener el código fuente de la función"


def test_matplotlib_ejercicio_5():
    """Test para matplotlib_ejercicio_5: gráfico con múltiples líneas"""
    try:
        func = mod.matplotlib_ejercicio_5  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `matplotlib_ejercicio_5`"

    # Test de funcionamiento
    x: list[float] = [1.0, 2.0, 3.0, 4.0]
    y1: list[float] = [1.0, 2.0, 3.0, 4.0]
    y2: list[float] = [2.0, 4.0, 6.0, 8.0]

    try:
        func(x, y1, y2)
    except Exception as e:
        assert False, f"La función debería ejecutarse sin errores, pero lanzó: {e}"

    # Test de consignas
    if (src := source["_source"]) is not None:
        # Contar cuántas veces aparece plt.plot (excluyendo comentarios y docstrings)
        # Buscar plt.plot seguido de paréntesis
        plot_matches = len(re.findall(r"plt\.plot\s*\(", src))
        assert (
            plot_matches >= 2
        ), f"Debe usar plt.plot() al menos dos veces para crear dos líneas (encontrado {plot_matches} veces)"
        assert ".legend" in src, "Debe usar plt.legend() para agregar una leyenda"
        assert ".show" in src, "Debe usar plt.show() para mostrar el gráfico"
    else:
        assert False, "No se pudo obtener el código fuente de la función"


def test_matplotlib_ejercicio_6():
    """Test para matplotlib_ejercicio_6: gráfico de barras desde DataFrame"""
    try:
        func = mod.matplotlib_ejercicio_6  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `matplotlib_ejercicio_6`"

    # Test de funcionamiento
    df = pd.DataFrame(
        {
            "categoria": ["Electrónica", "Accesorios", "Dispositivos"],
            "total": [1000, 2000, 1500],
        }
    )

    try:
        func(df)
    except Exception as e:
        assert False, f"La función debería ejecutarse sin errores, pero lanzó: {e}"

    # Test de consignas
    if (src := source["_source"]) is not None:
        assert ".groupby" in src, "Debe usar .groupby() para agrupar por categoría"
        assert ".sum" in src, "Debe usar .sum() para sumar los totales"
        assert ".bar" in src, "Debe usar plt.bar() para crear el gráfico de barras"
        assert ".title" in src, "Debe usar plt.title() para agregar un título"
        assert ".xlabel" in src, "Debe usar plt.xlabel() para la etiqueta del eje X"
        assert ".ylabel" in src, "Debe usar plt.ylabel() para la etiqueta del eje Y"
    else:
        assert False, "No se pudo obtener el código fuente de la función"


def test_matplotlib_ejercicio_7():
    """Test para matplotlib_ejercicio_7: gráfico de dispersión"""
    try:
        func = mod.matplotlib_ejercicio_7  # type: ignore # noqa
        source = get_annotations_and_rvalues(func)
    except ImportError:
        assert False, "No se pudo importar la función `matplotlib_ejercicio_7`"

    # Test de funcionamiento
    df = pd.DataFrame({"cantidad": [1, 2, 3, 4, 5], "total": [100, 200, 300, 400, 500]})

    try:
        func(df)
    except Exception as e:
        assert False, f"La función debería ejecutarse sin errores, pero lanzó: {e}"

    # Test de consignas
    if (src := source["_source"]) is not None:
        assert (
            ".scatter" in src
        ), "Debe usar plt.scatter() para crear el gráfico de dispersión"
        assert ".title" in src, "Debe usar plt.title() para agregar un título"
        assert ".xlabel" in src, "Debe usar plt.xlabel() para la etiqueta del eje X"
        assert ".ylabel" in src, "Debe usar plt.ylabel() para la etiqueta del eje Y"
        assert ".show" in src, "Debe usar plt.show() para mostrar el gráfico"
    else:
        assert False, "No se pudo obtener el código fuente de la función"
