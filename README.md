# Pre-entrega: correlación y comportamiento del consumidor

| Campo | Detalle |
|---|---|
| Estudiante | Dennys Parra |
| Curso | Data Science II — Machine Learning, Coderhouse |
| Actividad | Análisis de correlación del módulo 15 |

El [notebook ejecutado](pre-entregamd15.ipynb) estudia la relación entre descuento y beneficio mediante Pearson, Spearman y Kendall. Incluye código, resultados visibles, gráficos y conclusiones.

## Datos y resultados

Se reutiliza una copia local de Sample Superstore, conjunto sintético utilizado en la pre-entrega del módulo 14. Cada fila representa una **línea de pedido**; un pedido puede contener varias líneas. El archivo tiene 9.994 filas y 21 columnas; no hay faltantes en el par `Discount` y `Profit`.

| Método | Correlación descuento-beneficio | Qué describe |
|---|---:|---|
| Pearson | −0,2195 | Asociación lineal de los valores originales. |
| Spearman | −0,5434 | Asociación monotónica entre rangos. |
| Kendall tau-b | −0,4282 | Concordancia entre pares, considerando empates. |

Los tres resultados son negativos. El análisis utiliza **Spearman como referencia exploratoria**, porque resume la tendencia por rangos y es menos sensible a la magnitud de los extremos. Kendall complementa la lectura ante los numerosos descuentos repetidos. Ninguno de los coeficientes prueba que el descuento cause cambios en el beneficio, y sus magnitudes no son directamente intercambiables.

## Reproducir el notebook

Se requiere Python 3.10 o superior. Desde esta carpeta, crea un entorno e instala las dependencias:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
jupyter lab pre-entregamd15.ipynb
```

Ejecuta las celdas en orden. El notebook lee `data/dashboard_ventas.csv` mediante una ruta relativa, por lo que Jupyter debe iniciarse desde esta carpeta. Las versiones observadas para el análisis fueron Python 3.13.9, pandas 2.2.3, SciPy 1.16.3, seaborn 0.13.2 y matplotlib 3.10.6; los requisitos son rangos compatibles, no un bloqueo exacto.

## Ejecutar las pruebas

Desde esta carpeta, con las dependencias instaladas:

```powershell
python -m unittest discover -s tests -v
```

Las pruebas ejecutan el notebook con una copia temporal del dataset y comprueban los tres coeficientes frente a SciPy, las visualizaciones, los resultados guardados y la presencia de las explicaciones. No modifican el CSV original.

## Archivos

| Archivo | Contenido |
|---|---|
| [`pre-entregamd15.ipynb`](pre-entregamd15.ipynb) | Análisis ejecutable con resultados y gráficos visibles. |
| [`data/dashboard_ventas.csv`](data/dashboard_ventas.csv) | Copia local del dataset de M14. |
| [`consigna-pre-entregamd15.md`](consigna-pre-entregamd15.md) | Consigna de la actividad. |
| [`requirements.txt`](requirements.txt) | Dependencias del notebook y las pruebas. |
| [`tests/test_entrega.py`](tests/test_entrega.py) | Pruebas reproducibles del análisis. |

La guía de estudio del profesor se encuentra fuera de esta entrega, en el espacio de estudio local.
