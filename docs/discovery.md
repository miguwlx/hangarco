# Descubrimiento: HangarCo

Documento de la Fase 1 del hackathon «Innovación con Datos Abiertos de Colombia».

## 1. Nombre provisional de la aplicación

**HangarCo**: consulta de aeronaves registradas en Colombia con matrícula vigente.

## 2. Problema o hipótesis de necesidad

> **Hipótesis (no confirmada con usuarios):** las personas interesadas en la aviación, los estudiantes y quienes necesitan verificar información básica de una aeronave no cuentan con una forma sencilla de consultar qué aeronaves tienen matrícula vigente en Colombia y cuáles son su fabricante, modelo y tipo de matrícula.

El conjunto de datos demuestra que la información existe y está publicada. **No demuestra por sí solo que el problema exista**: no hemos contrastado esta necesidad con usuarios reales, por eso se presenta como hipótesis.

## 3. Usuario o beneficiario potencial

- Estudiantes y aficionados a la aviación que quieren consultar datos de aeronaves colombianas.
- Periodistas o curiosos que necesitan verificar rápidamente si una matrícula figura como vigente.
- Decisión o acción que se facilita: comprobar el estado de una matrícula y ver los datos básicos de la aeronave sin revisar la tabla completa del portal.

## 4. Fuente de datos

| Elemento | Detalle |
|---|---|
| Conjunto de datos | Aeronaves registradas en Colombia con matrícula vigente |
| URL | https://www.datos.gov.co/Transporte/Aeronaves-registradas-en-Colombia-con-matr-cula-vi/qsim-wdzj/about_data |
| Identificador | `qsim-wdzj` |
| Entidad publicadora | Unidad Administrativa Especial de Aeronáutica Civil (Aerocivil), Grupo de Registro Aeronáutico |
| Propietario del conjunto | Datos Abiertos Aerocivil |
| Origen de los datos | Sistema de Información y Gestión Aeronáutica (SIGA) |
| Categoría | Transporte |
| Cobertura | Nacional |
| Última actualización | 10 de noviembre de 2026 |
| Frecuencia de actualización | Trimestral |
| Tamaño | 1.891 filas y 8 columnas |
| Cada fila representa | Una aeronave con matrícula vigente |
| Licencia | Creative Commons Attribution 4.0 International (exige atribución) |
| Acceso en la app | API (Socrata) de datos.gov.co: `https://www.datos.gov.co/resource/qsim-wdzj.json` |

## 5. Campos relevantes

| Campo | Qué representa |
|---|---|
| `numero_matricula` | Matrícula de la aeronave (ej. CCAWA) |
| `tipo_matricula` | Tipo de matrícula (ej. DEFINITIVA) |
| `estado_matricula` | Estado de la matrícula (ej. VIGENTE) |
| `fecha_inscripcion` | Fecha de inscripción, cuando está disponible (en varios registros aparece «SIN INFORMACION») |
| `marca_fabricante` | Marca o fabricante (ej. AIRBUS) |
| `modelo` | Modelo (ej. A-320-232) |
| `numero_serie` | Número de serie |
| `titularidad_y_explotacion` | Condición general de titularidad o explotación (ej. nombre de una empresa, o «PERSONA NATURAL») |

## 6. Funcionalidad principal y valor esperado

**Funcionalidad mínima:** el usuario escribe un texto (matrícula, fabricante, modelo…) y la aplicación muestra, desde el navegador, las aeronaves de datos reales que coinciden, en una tabla comprensible con la fuente citada.

**Valor esperado:** responder rápido y sin conocimientos técnicos a la pregunta «¿esta aeronave está registrada con matrícula vigente y qué datos básicos tiene?».

La app maneja de forma predecible tres casos: búsqueda demasiado corta, búsqueda sin coincidencias y fallo de la consulta a la API.

## 7. Limitaciones conocidas de los datos

- Solo incluye aeronaves con **matrícula vigente** a la fecha de corte; no hay histórico ni aeronaves canceladas.
- Se actualiza **trimestralmente**, por lo que puede no reflejar cambios recientes.
- Algunos campos pueden venir como «SIN INFORMACION», y la entidad advierte que algunos registros históricos pueden tener información no disponible o inconsistencias.
- La información es **informativa y no reemplaza el Certificado de Tradición** que se tramita en el aplicativo SIGA de Aerocivil.
- Cuando la titularidad corresponde a una persona natural, el dato aparece como «PERSONA NATURAL»; el conjunto no publica nombres ni documentos de identidad.
- Es un conjunto pequeño (1.891 registros) y sin etiquetas en el portal.
- Posibles errores del dato se reportan a datosabiertos@aerocivil.gov.co o atencionalciudadano@aerocivil.gov.co, según indica la entidad.

## 8. Riesgos de implementación

- Disponibilidad o lentitud de la API: se maneja con tiempo máximo de espera y mensaje de error.
- Campos vacíos o con «SIN INFORMACION»: se muestran con un texto claro en la tabla.
- Alcance: se prioriza el flujo de búsqueda completo y verificado sobre funciones adicionales (por ejemplo, filtros por fabricante, que quedan como mejora opcional).

## 9. Uso responsable de los datos

- Se cita la fuente (Aerocivil, datos.gov.co) en la aplicación y en el README, como exige la licencia CC BY 4.0.
- No se exponen datos personales: el propio conjunto no los publica.
- La aplicación aclara que la información es de carácter informativo.

## 10. Fuentes candidatas consideradas

- **Elegida:** Aeronaves registradas en Colombia con matrícula vigente (`qsim-wdzj`).
- **Otra fuente revisada:** Conexiones a Televisión por Suscripción y Comunitaria
