# Proyecto-Final-Python-Martin-Adrian-Ferraguti.

El presente proyecto fue desarrollado utilizando Python junto con el framework Django. <br>
Se trata de una app web cuyo objetivo funcional trata de resolver el seguimiento de las transacciones operativas de la Veterinaria { Animal Center } de Bahía Blanca.

# Video.
https://youtu.be/_bYnCR9Y77o <br>
Web de login: http://127.0.0.1:8000/AppCoder/login?next=/AppCoder/ <br>

Datos de login utilizado durante la demo: <br>
User: mferraguti <br>
Pass: pepelis84 <br>
_______________________________________________________________________________________________________________________________________________________________________
# Models.py:
En este archivo se definen los modelos utilizados en el proyecto.

Modelo Animal: 
Campos:

    -nombreAnimal: Tipo char, nombre de la mascota
    -edad: Tipo integer, edad de la mascota
    -tipo: Tipo char, ej: perro, gato, iguana, etc
    -motivo: Tipo Char, motivo de la visita al centro de salud ej: vacunas, operación, peluquería, etc
    -fecha: Tipo date, fecha de ingreso al centro de salud
    -costo: Tipo integer, monto cobrado al dueño de la mascota por el servicio prestado


Modelo Persona: 
Campos: 

    -nombre: Tipo char, corresponde al nombre del dueño de la mascota
    -apellido: Tipo char, es el apellido del dueño de la mascota
    -telefono: Tipo integer, numero de celular/telefono del dueño de la mascota


Modelo Veterinario:
Campos:

    -veterinario: Tipo char, nombre del veterinario
    -apellidoVet: Tipo char, apellido del veterinario
    -matricula: Tipo integer, numero de matrícula del veterinario

_______________________________________________________________________________________________________________________________________________________________________
# Forms.py:
En este archivo se definen los formularios usados para interactuar con la base de datos.
En total son 4 formularios, uno por cada modelo (animales, personas, veterinarios) y otro para poder registrar los nuevos usuarios 
_______________________________________________________________________________________________________________________________________________________________________


# Urls.py:
En este archivo se definen cada una de las rutas de las vistas de la presente app.
_______________________________________________________________________________________________________________________________________________________________________


# Views.py:
En este archivo se definen todas las vistas utilizadas por la app.
Para los modelos Animal y Persona/Dueño se aplica el concepto CRUD (Create, Read, Update, Delete)
_______________________________________________________________________________________________________________________________________________________________________


# Templates:
En este directorio se encuentran todos los archivos HTML usados en la app, se utilizó una platilla de BOOSTRAP y se aplicó en conjunto el concepto de herencia a cada archivo.
_______________________________________________________________________________________________________________________________________________________________________


# Unit Test:
Conforme a lo mencionado en la Clase 24 se completó el Unit Test desarrollado en la cursada "calculadora avanzada" (**UnitTest/calculadora_avanzada.py**) donde se aborda el caso "división por cero" con divisor igual a cero.
Adicional se desarrolló un segundo Unit Test donde dado una cadena de texto se determina si esta es capicúa o no siendo condición para su resolución el uso de un bucle for o while.
(**UnitTest/capicua.py**)
_______________________________________________________________________________________________________________________________________________________________________


# Datos del Autor:
Nombre completo: Martin Adrian Ferraguti <br>
Comisión: 47790 <br>
Email: martin.ferraguti@gmail.com <br>
Linkedin: https://www.linkedin.com/in/martin-ferraguti/ <br>

