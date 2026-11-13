# HangarCo

Aplicación web hecha con Python y Django para consultar aeronaves registradas en Colombia con matrícula vigente, usando datos abiertos.

## Fuente de datos
- Conjunto de datos: Aeronaves registradas en Colombia con matrícula vigente
- Portal: datos.gov.co (id qsim-wdzj)
- Entidad publicadora: [completar desde la ficha del dataset]
- Acceso: API (Socrata) consultada desde Django

## Requisitos
- Python 3.12 o superior
- Git

## Instalación
git clone https://github.com/miguwlx/hangarco.git
cd hangarco
python -m venv .venv
# Windows: .venv\Scripts\activate   |   Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt

## Ejecución
python manage.py runserver
Abrir http://127.0.0.1:8000

## Pruebas
python manage.py test

## Equipo
Miguel Santiago Bonilla Riascos, Diana [apellido], Yulieth [apellido]

## Limitaciones de los datos
[completar cuando Diana revise los campos]