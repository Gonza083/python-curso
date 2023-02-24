import os

# Obtenemos la ruta de la carpeta Descargas
ruta_descargas = os.path.expanduser('~/Downloads')

# Obtenemos los ficheros y directorios de la carpeta Descargas
elementos = os.listdir(ruta_descargas)

# Recorremos los elementos obtenidos y mostramos solo los ficheros
for elemento in elementos:
    ruta_elemento = os.path.join(ruta_descargas, elemento)
    if os.path.isfile(ruta_elemento):
        print(elemento)

# Ampliación: Listamos los tamaños de los ficheros en formato humano
for elemento in elementos:
    ruta_elemento = os.path.join(ruta_descargas, elemento)
    if os.path.isfile(ruta_elemento):
        tamano = os.path.getsize(ruta_elemento)
        tamano_formateado = ''
        for unidad in ['B', 'KB', 'MB', 'GB', 'TB']:
            if tamano < 1024.0:
                tamano_formateado = f'{tamano:.1f} {unidad}'
                break
            tamano /= 1024.0
        print(f'{elemento}: {tamano_formateado}')


# Ampliación: Recorremos de manera recursiva todos los directorios
def mostrar_ficheros_carpeta(ruta):
    elementos = os.listdir(ruta)
    for elemento in elementos:
        ruta_elemento = os.path.join(ruta, elemento)
        if os.path.isfile(ruta_elemento):
            tamano = os.path.getsize(ruta_elemento)
            tamano_formateado = ''
            for unidad in ['B', 'KB', 'MB', 'GB', 'TB']:
                if tamano < 1024.0:
                    tamano_formateado = f'{tamano:.1f} {unidad}'
                    break
                tamano /= 1024.0
            print(f'{elemento}: {tamano_formateado}')
        elif os.path.isdir(ruta_elemento):
            mostrar_ficheros_carpeta(ruta_elemento)


mostrar_ficheros_carpeta(os.path.expanduser('~/'))