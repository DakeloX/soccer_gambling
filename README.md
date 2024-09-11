# Soccer Gambling API

Este es un proyecto de backend construido con Django, que consume datos de la API de Football (API-Football). El proyecto permite consultar diferentes datos relacionados con fútbol, como probabilidades, equipos, partidos, jugadores y más.

### Requisitos

- Python 3.x
- Django


### Instalación y configuración

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

### 1. Clonar el repositorio

Clona el repositorio en tu máquina local.

```bash
git clone https://github.com/DakeloX/soccer_gambling.git

```
### Crear un entorno virtual

```bash
python -m venv entorno-casino
```

###  windows

```bash
\soccer_gambling\entorno-casino\Scripts\activate   #nombres ramdon de carpeta
```

### Instalar dependencias

```bash
pip install -r requirements.txt

```
### Migrar la base de datos

```bash
python manage.py migrate
```

### Ejecutar el servidor

```bash
python manage.py runserver
```




## Endpoints disponibles
A continuación se describen algunos de los endpoints que puedes usar para obtener información desde la API de fútbol.

### 1. GET /odds/live/
Devuelve las probabilidades en vivo de los partidos.

Ejemplo de uso:

```bash

http://127.0.0.1:8000/odds/live/
```

### 2. GET /teams/countries/
Devuelve una lista de equipos por país.

Ejemplo de uso:
```bash
http://127.0.0.1:8000/teams/countries/
```

### 3. GET /fixtures/headtohead/?team1=1&team2=2
Devuelve el historial de partidos entre dos equipos específicos.

Ejemplo de uso:
```bash
http://127.0.0.1:8000/fixtures/headtohead/?team1=1&team2=2
```
### 4. GET /injuries/
Devuelve datos sobre lesiones de los jugadores.

Ejemplo de uso:

```bash
http://127.0.0.1:8000/injuries/
```

### 5. GET /players/topyellowcards/
Devuelve los jugadores con más tarjetas amarillas.

Ejemplo de uso:

```bash
http://127.0.0.1:8000/players/topyellowcards/
```

# Comandos útiles de Git


### 1. Agregar los remotos
Agrega el repositorio  como origin:

```bash

git remote add origin https://github.com/DakeloX/soccer_gambling.git

git add .

git commit -m "Descripción del cambio"

git push origin main

git pull
```


##### quejas al servicio al cliente 