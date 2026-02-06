# Geometry-Volume-App

## Descripción general del proyecto

Este proyecto se realizo mediante Python y en este se busca calcular el volumen de distintas figuras geométricas las cuales son una caja, cono, cilindro y esfera. El proyecto sigue una esturctura modulas donde cada una de las figuras cuenta con su propio programa y contiene pruebas unitarias las cuales se realizaron utilizando pytest para confirmar el funcionamiento de los programas, estos tests incluyen casos normales y casos límite.

## Estructura del Proyecto
En primer lugar, se cuenta con la raíz del proyecto donde se encuentran los archivos y carpetas principales los cuales permiten la ejecución correcta. Los archivos aquí son:
- main.py: El archivo principal para la ecución del proyecto desde donde se importan las funciones definidas dentro del paquete de geometry para calcular los volúmenes de las figuras.

- README.md: Este archivo es el que se está leyendo actualmente y contiene la descripción general del proyecto junto a las intrucciones de ejecución.

- .gitignore: Define los archivos y las carpetas que no deben de ser rastreados por Git.

- Carpeta geometry: En esta se contiene toda la lógica del cálculo de los volumenes. Cada archivo dentro de la carpeta se utiliza para una figura diferente, aquí es donde se encuentra el box.py, con.py, cylinder.py y sphere.py. También se cuenta con el _init_.py indicando que la carpeta debe de tratarse como un paquete y el _pycache_/ que almacena archivos compilados.

-Carpeta tests: Aquí se encuentran las pruebas unitarias prar verificar el funcionamento adecuado, existe una prueba unitaria para cada figura.

Aquí hay una representación visual de la estructura:

```
geometry-volume-app/
│   .gitignore
│   main.py
│   README.md
│
├── geometry
│   │   box.py
│   │   cone.py
│   │   cylinder.py
│   │   sphere.py
│   │   __init__.py
│   │
│   └── __pycache__
│       box.cpython-312.pyc
│       cone.cpython-312.pyc
│       cylinder.cpython-312.pyc
│       sphere.cpython-312.pyc
│       __init__.cpython-312.pyc
│
└── tests
    │   test_box.py
    │   test_cone.py
    │   test_cylinder.py
    │   test_sphere.py
    │   __init__.py
```

## Como correr el main.py

1. Abre una terminal y navega hasta la carpeta raíz del proyecto, es recomendable pegar el directorio desde la carpeta:

cd geometry-volume-app

2. Asegúrate de tener python instalado por medio de:

python --version

3. Una vez confirmado, ejecuta el archivo main.py usando el siguiente comando en Windows:

python main.py

4. Prueba el programa para observar su funcionamiento adecuado.

## Como ejecutar las pruebas
 1. Es importante confirmar que se está dentro de la carpeta raíz del proyecto:

cd geometry-volume-app

2. Se recomienda el uso de un entorno virtual para aislar las dependencias:

python -m venv venv
venv\Scripts\activate

3. Se ejecuta el pytest mediante el próximo comando:

pytest

## Dependencias
Este proyecto cuenta con un paquete externo el cual es pytest para validar los cálculos. Las dependencias se definen en el requirements.txt, para poder instalar estas dependencias utiliza:

pip install -r requirements.txt