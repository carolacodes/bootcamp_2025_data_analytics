# Ejemplos Adicionales

Este directorio contiene un proyecto de `reflex` creado con:

- `reflex init --name tiny_reflex`

Y un notebook para algunas operaciones básicas de web scraping

- `web_scraping.ipynb`

## Proyecto Reflex

Este proyecto ejemplifica un proyecto básico, que conecta a nuestra base de datos
`"nortwind"` y tiene una pagina simple que muestra datos de la tabla `"customers"`,
una segunda pagina que muestra la union de las tablas `"orders"` y `"customers"`,
y una ultima pagina que muestra algunas estadísticas usando componentes integrados
de reflex.

### Iniciar el Proyecto

- Instalar nuevas dependencias (en este caso usamos el mismo entorno del proyecto):
  - `uv sync`

- Inicializamos reflex:
  - `uv run reflex init`

- Corremos el servidor de reflex:
  - `uv run reflex run`

## Notebook de Web Scrapping

### Iniciamos `jupyter`

- `uv run jupyter-notebook web_scraping.ipynb`
