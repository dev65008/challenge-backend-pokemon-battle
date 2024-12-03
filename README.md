# Batallas Pokemon


```
Prueba técnica a nivel resolutivo.
```  

Se desarrolló una aplicación de consola que consta de una serie de configuraciones previas al uso.
Partiendo dentro de la carpeta del proyecto:

```bash
python3 -m virtualenv pokenv

source ./pokenv/bin/activate

pip3 install -r requirements.txt
```  

### Editar el archivo .env.sample y renombrarlo por .env, modificar los valores de ser necesario antes de correr la app.

*   POKEAPI_URL : url de la api de pokemones
*   BATTLE_QTY : cantidad de turnos a competir
*   RAMDOM_MAX : cantidad maxima utilizada para la funcion random

## Correr la batalla!

Para utilizar el calculador de resultados de batallas entre pokemones es necesario usar la siguiente sintaxis en terminal
```
python3 app.py pokemon1 pokemon2
```  

## Características Adicionales/adoptadas

*   Redondeo a 2 decimales
*   Archivo .env para configuraciones
*   Se codeo en inglés sin embargo las respuestas en terminal son en castellano