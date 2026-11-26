**Ejercicio**

**Actividad**

# Pre-entrega: Análisis de Correlación, comportamiento del Consumidor

## Propósito

El propósito de este entregable es aplicar las técnicas de correlación de Pearson, Spearman y Kendall para identificar relaciones entre variables en un conjunto de datos transaccional simulado. Deberás determinar qué coeficiente es el más adecuado según la distribución y naturaleza de los datos.

## Entregable

**Respondé las siguientes preguntas:**

1. El archivo entregado debe ser un .ipynb ejecutable con las celdas de código y resultados visibles.
2. Se deben calcular explícitamente los tres coeficientes (Pearson, Spearman y Kendall) para al menos un par de variables.
3. El notebook debe incluir una sección de conclusiones donde se explique cuál método es el más robusto para el dataset dado.
4. Se debe incluir una visualización (como un heatmap o scatter plot) que apoye la interpretación de la correlación.

Un archivo Jupyter Notebook (.ipynb) que contenga el análisis estadístico, los cálculos de los coeficientes y las conclusiones interpretativas.

## Propósito

El propósito de este entregable es aplicar las técnicas de correlación de Pearson, Spearman y Kendall para identificar relaciones entre variables en un conjunto de datos transaccional simulado. Deberás determinar qué coeficiente es el más adecuado según la distribución y naturaleza de los datos.

## Pasos sugeridos

1. **Preparación del Entorno:** Crea un Jupyter Notebook (.ipynb) donde importarás las librerías de análisis de datos (como Pandas y Scipy/Numpy).
2. **Análisis de Supuestos:** Antes de calcular, realiza un breve análisis visual (histogramas o tests de normalidad) para decidir si una variable sigue una distribución normal. Esto es clave para elegir entre Pearson (paramétrico) o Spearman/Kendall (no paramétricos).
3. **Cálculo de Coeficientes:** Calcula e interpreta la matriz de correlación utilizando los tres métodos estudiados para comparar cómo varían los resultados ante valores atípicos (outliers) o relaciones no lineales.
4. **Documentación de Hallazgos:** Dentro del mismo notebook, utiliza celdas de Markdown para explicar por qué una correlación fuerte no implica causalidad en el contexto del negocio y justifica cuál de los tres métodos ofrece la visión más precisa de los datos analizados.

## Errores comunes

- Calcular Pearson sobre variables con distribuciones muy sesgadas o con muchos valores atípicos sin justificarlo.
- Confundir una correlación alta con una relación de causa-efecto.
- No incluir la interpretación cualitativa de los coeficientes obtenidos (ej. ¿qué significa un 0.85 en términos de negocio?).
