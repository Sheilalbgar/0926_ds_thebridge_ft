# Radiografía Laboral

*Lo que no se ve del absentismo por salud en España: quién falta, por qué, dónde y cómo actuar antes.*

Análisis exploratorio de datos (EDA) sobre las bajas laborales por salud en España.

## La pregunta

¿Quién falta al trabajo por salud, por qué y dónde? ¿Se concentra en pocas personas? ¿Cuánto se podría ahorrar actuando antes?

## Lo que he encontrado

- **Cada vez hay más bajas:** 9,2 millones de bajas por enfermedad común en 2025, un **12,8 % más** que en 2023, y suben en 49 de 52 provincias.
- **1 de cada 4** trabajadores faltó al trabajo por salud en el último año.
- El **1,6 %** de los trabajadores se lleva **la mitad** de todos los días de ausencia: son bajas de 150 días o más.
- Ese grupo tiene un **perfil claro:** problemas **musculoesqueléticos y de salud mental**, muchas veces juntos. Con los dos a la vez se falta 34 días al año de media, frente a 4 sin ninguno.
- **Casi el doble** de trabajadores de baja en Canarias y Galicia (unos 70 por cada 1.000) que en Madrid (42). Y donde hay más bajas, son más cortas.
- La **industria** es el sector con más horas no trabajadas y más recaídas.
- **La oportunidad:** con un programa de incorporación al trabajo, reducir solo un 10 % los días de baja de quien repite supondría unos **1.188 millones de euros al año** (es un escenario).

## Hipótesis

| | Hipótesis | ¿Se cumple? |
|---|---|---|
| H1 | Cada vez hay más bajas | Sí |
| H2 | Hay diferencias entre comunidades y sectores | Sí |
| H3 | Los sobreesfuerzos son la primera causa de los accidentes con baja | No del todo: coincide con los golpes |
| H4 | Los problemas de espalda y de salud mental hacen faltar más | Sí |
| H5 | Unos pocos se llevan la mayoría de los días | Sí, y más de lo esperado |
| H6 | Las fuentes cuentan lo mismo por comunidad | En parte |

## Datos

Cuatro fuentes oficiales, todas de España:

| Fuente | Qué aporta | Tipo |
|---|---|---|
| [INE, tabla 6063](https://www.ine.es/jaxiT3/Tabla.htm?t=6063) (Encuesta Trimestral de Coste Laboral) | Horas no trabajadas por comunidad, sector y trimestre (2008-2026) | Agregados |
| [Seguridad Social, Estadística de Incapacidad Temporal 2023-2025](https://www.seg-social.es/wps/portal/wss/internet/EstadisticasPresupuestosEstudios/Estadisticas/EST45/EST46) | Bajas médicas por provincia: iniciadas, duración y bajas abiertas | Registros agregados |
| [Ministerio de Trabajo, Estadística de Accidentes de Trabajo 2025](https://www.mites.gob.es/estadisticas/eat/welcome.htm) | Forma del accidente y recaídas por sector | Agregados |
| [Ministerio de Sanidad, Encuesta de Salud de España 2023](https://www.sanidad.gob.es/estadisticas/microdatos.do) | Ausencia del trabajo, días y problemas de salud de cada persona | Microdatos anónimos |

En total, unas **187.000 filas** y más de **12 millones de datos**, unidos en una **tabla común** por comunidad autónoma. Son datos reales y anónimos.

## Cómo lo he hecho

1. **Ver los datos:** qué trae cada fuente, cuántos datos hay y de qué tipo es cada variable.
2. **Limpiar:** filtros, formatos, códigos, datos que faltan y outliers (que no quito, porque son bajas largas reales). Uno tablas con `merge`, `concat` y una query SQL, paso de formato ancho a largo con `melt` y guardo todo en CSV.
3. **Analizar:** univariante, bivariante y multivariante, con Matplotlib y Seaborn.
4. **Contrastar las hipótesis:** Pearson, Wilcoxon, Kruskal-Wallis, chi-cuadrado y Mann-Whitney, mirando siempre el p-valor **y** el tamaño del efecto.

## Tecnologías

Python 3.14 · pandas · NumPy · Matplotlib · Seaborn · SciPy · SQLite · Jupyter Notebook · VS Code

## Estructura

```
├── README.md
├── requirements.txt
├── EDA_laboral.ipynb      el trabajo completo, paso a paso
├── memoria.ipynb          resumen del proyecto: de la pregunta a las conclusiones
├── presentacion/          
└── data/
    ├── raw/               los archivos tal cual los descargué
    └── processed/         los datos limpios en CSV (con la tabla común)
```

## Cómo ejecutarlo

1. Instalar las librerías: `pip install -r requirements.txt`
2. Ejecutar `EDA_laboral.ipynb`, que limpia los datos y los guarda en `data/processed`.
3. Ejecutar `memoria.ipynb`, que lee los datos limpios y resume el proyecto.

## Limitaciones

- Los datos agregados dicen **dónde**, pero no **quién**; la encuesta es autodeclarada.
- Las relaciones son **asociaciones**, no causas.
- De la Seguridad Social solo hay datos comparables de 2023 a 2025.


