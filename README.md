# ¿Qué es Tacita?
Tacita es una suit de herramientas (licencia GPL) dependientes una de las otras. Cada script es un bot encargado de una funcionalidad. En conjunto todas ellas funcionando de forma secuencial o en paralelo nos ayudan a buscar con patrones malware en los APKs descargados y analizados.

# ¿Qué hace Tacita?
Usaremos la misma estructura de bots que Shodita, creando una familia de scripts intereactuando y dependiendo una de las otras. Los diferentes bots que crearemos son:

downloadAPK.py: encargado de descargar en el directorio llamado ‘bot’ los apks que posteriormente serán analizados.
analizeAPK.py: encargado de obtener package, directorios y archivos, permisos, librerías, activities, urls, emails, ftp, etc de todos los APKs descargados anteriormente por downloadAPK.py y almacenar la información en MongoDB.
little-cup.py: panel en consola que nos permite hacer búsquedas con patrones.

# ¿Cómo importar tacita-ejm.py?
~$ mongoimport –collection Tacita –file tacita-ejm.json

# Dependecias
- MongoDB -> sudo apt-get install mongodb
- apk_parse -> https://github.com/tdoly/apk_parse
- urllib, time, os, requests, re, pymongo

# More info
http://blog.quantika14.com/blog/2016/11/21/tacita-crear-big-data-analisis-estatico-apks/
