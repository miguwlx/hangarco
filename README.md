# HangarCo

Aplicación web hecha con **Python y Django** para consultar las aeronaves registradas en Colombia con matrícula vigente, usando datos abiertos oficiales.

Proyecto del hackathon «Innovación con Datos Abiertos de Colombia» (*Construye, aprende e innova*).

## ¿Qué hace?

El usuario escribe un texto (matrícula, fabricante, modelo…) en el navegador y la aplicación muestra en una tabla las aeronaves que coinciden, con datos reales de datos.gov.co.

La aplicación maneja de forma predecible tres casos:
- Búsqueda demasiado corta (menos de 2 caracteres).
- Búsqueda sin coincidencias.
- Fallo en la consulta a la fuente de datos.

> **Hipótesis de necesidad (no confirmada con usuarios):** estudiantes, aficionados a la aviación y periodistas necesitan verificar rápidamente si una aeronave tiene matrícula vigente en Colombia y consultar sus datos básicos. Más detalle en [`docs/discovery.md`](docs/discovery.md).

## Fuente de datos

| Elemento | Detalle |
|---|---|
| Conjunto de datos | [Aeronaves registradas en Colombia con matrícula vigente](https://www.datos.gov.co/Transporte/Aeronaves-registradas-en-Colombia-con-matr-cula-vi/qsim-wdzj/about_data) |
| Identificador | `qsim-wdzj` |
| Entidad publicadora | Unidad Administrativa Especial de Aeronáutica Civil (Aerocivil), Grupo de Registro Aeronáutico |
| Portal | Portal de Datos Abiertos de Colombia (datos.gov.co) |
| Última actualización | 10 de noviembre de 2026 (frecuencia trimestral) |
| Tamaño | 1.891 filas y 8 columnas |
| Licencia | Creative Commons Attribution 4.0 International |
| Modalidad de acceso | API (Socrata): `https://www.datos.gov.co/resource/qsim-wdzj.json` |

La información es de carácter informativo y **no reemplaza el Certificado de Tradición** que se solicita en el aplicativo SIGA de Aerocivil.

### Limitaciones de los datos
- Solo incluye aeronaves con matrícula vigente a la fecha de corte; no hay histórico.
- Se actualiza trimestralmente, por lo que puede no reflejar cambios recientes.
- Algunos campos aparecen como «SIN INFORMACION» y la entidad advierte que pueden existir inconsistencias en registros históricos.
- Cuando la titularidad corresponde a una persona natural, el dato aparece como «PERSONA NATURAL»; el conjunto no publica nombres ni documentos de identidad.

## Requisitos

- Python (probado con 3.15.2)
- Git
- Conexión a internet (la aplicación consulta la API de datos.gov.co)

Versión de Django fijada en `requirements.txt` (probado con Django 6.1.3).

## Instalación

### Windows (PowerShell)

```powershell
git clone https://github.com/miguwlx/hangarco.git
cd hangarco
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Si PowerShell bloquea la activación del entorno, ejecuta antes:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

### Mac o Linux

```bash
git clone https://github.com/miguwlx/hangarco.git
cd hangarco
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Ejecución

```bash
python manage.py runserver
```

Abre http://127.0.0.1:8000 en el navegador. Para detener el servidor, presiona `Ctrl + C`.

## Pruebas

```bash
python manage.py test
```

Resultado de la última ejecución real: _[completar con el resultado real de `python manage.py test`]_

## Estructura del proyecto

| Ruta | Función |
|---|---|
| `config/` | Configuración del proyecto Django y rutas principales |
| `aircraft/services.py` | Consulta a la API de datos abiertos |
| `aircraft/views.py` | Recibe la búsqueda y prepara la respuesta |
| `aircraft/urls.py` | Rutas de la aplicación |
| `aircraft/templates/` | Páginas HTML |
| `aircraft/tests.py` | Pruebas automatizadas |
| `docs/` | Documentación del descubrimiento |

## Planificación (simulación inspirada en Scrum)

**Objetivo del Producto:** ayudar a estudiantes, aficionados a la aviación y periodistas a consultar con rapidez qué aeronaves tienen matrícula vigente en Colombia, usando datos abiertos oficiales.

**Objetivo del Sprint:** al final del bloque de desarrollo, una persona podrá buscar una aeronave por texto desde el navegador y ver resultados reales de datos.gov.co, o un mensaje claro si no hay coincidencias o falla la consulta.

**Elementos de la Lista de Producto:**
1. Buscar aeronaves por texto.
2. Ver resultados en una tabla comprensible con la fuente citada.
3. Mensajes claros ante búsquedas sin resultados o errores.

El seguimiento del trabajo está en GitHub Issues y GitHub Projects del repositorio.

### Definición de Terminado (DoD)

- [ ] Django inicia sin errores bloqueantes.
- [ ] Se puede completar el recorrido principal desde el navegador.
- [ ] La aplicación atiende el problema elegido de forma demostrable.
- [ ] Se usan datos reales cuya fuente está identificada.
- [ ] Se cumplen los criterios de aceptación del trabajo completado.
- [ ] Las entradas inválidas o los resultados vacíos no provocan fallos bloqueantes.
- [ ] Se ejecutó y registró una comprobación funcional real.
- [ ] Los cambios están revisados e integrados en la rama principal.
- [ ] El README contiene los pasos para instalar y ejecutar la aplicación.
- [ ] GitHub Issues y Projects reflejan el estado verdadero del trabajo.

## Flujo de trabajo en Git

Issue → rama → commit → Pull Request → revisión → comprobación → integración → verificación de la DoD → Done.

- Los nombres de ramas y los mensajes de commit se escriben en inglés (por ejemplo, `feature/aircraft-search`).
- Los Pull Requests mencionan el issue con `Refs #N`.
- No se publican contraseñas, tokens ni archivos secretos. La `SECRET_KEY` incluida en `config/settings.py` es la de desarrollo generada por Django y no debe usarse en producción.

## Equipo

- Miguel Santiago Bonilla Riascos
- Diana Faizury Reyes Correa
- Yulieth Tatiana Carvajal Jimenez

## Atribución

Datos: Unidad Administrativa Especial de Aeronáutica Civil (Aerocivil), publicados en el Portal de Datos Abiertos de Colombia (datos.gov.co) bajo licencia Creative Commons Attribution 4.0 International.
