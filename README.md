# Refugio Huellitas — Certamen 2 TLP
## Cristian Villalobos

Aplicación web desarrollada con Django para mostrar las mascotas de Refugio Huellitas y administrarlas mediante un área protegida por autenticación.

Las dependencias de Python están declaradas en [`requirements.txt`]:

- Django 6.1.2
- asgiref 3.13.0
- sqlparse 0.6.1

## Instalación

Desde la carpeta raíz del proyecto (`CER2-TLP`):

```
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

En Windows, la activación equivalente es:

```
.venv\Scripts\activate
```

## Base de datos

El proyecto usa SQLite. La configuración está en `config/settings.py` y apunta al archivo `db.sqlite3` en la raíz del proyecto; no es necesario instalar ni configurar PostgreSQL, MySQL u otro servidor.

### Usar la base incluida

El repositorio ya incluye `db.sqlite3` con las migraciones aplicadas y datos de ejemplo. Después de instalar las dependencias, se puede comprobar el estado con:

```
python manage.py migrate
```

## Ejecutar la aplicación

Con el entorno virtual activado:

```
python manage.py runserver
```

Abrir en el navegador:

```
http://127.0.0.1:8000/
```

## Rutas principales

| Ruta | Descripción | Acceso |
| --- | --- | --- |
| `/` | Página de inicio | Público |
| `/mascotas/` | Catálogo y filtro por especie | Público |
| `/mascotas/detalle/<id>/` | Detalle de una mascota | Público |
| `/accounts/login/` | Inicio de sesión | Público |
| `/accounts/logout/` | Cierre de sesión mediante POST | Usuario autenticado |
| `/gestion-mascotas/` | Listado y búsqueda de mascotas | Usuario con permiso `view_mascota` |
| `/gestion-mascotas/agregar/` | Crear una mascota | Usuario con permiso `add_mascota` |
| `/gestion-mascotas/modificar/<id>/` | Editar una mascota | Usuario con permiso `change_mascota` |
| `/gestion-mascotas/eliminar/<id>/` | Eliminar una mascota | Usuario con permiso `delete_mascota` |
| `/admin/` | Administración de Django, especies y mascotas | Superusuario o staff autorizado |

## Plantillas HTML revisadas

- `core/templates/core/base.html`: estructura común, navegación, autenticación, CSS y JavaScript externos.
- `core/templates/core/home.html`: portada y presentación del refugio.
- `core/templates/core/listaMascota.html`: catálogo, filtro por especie y enlaces al detalle.
- `core/templates/core/detalleMascota.html`: información de una mascota y formulario visual de adopción.
- `core/templates/core/gestionMascotas.html`: tabla de gestión y filtro local por nombre.
- `core/templates/core/agregarMascota.html`: formulario para registrar mascotas.
- `core/templates/core/modificarMascota.html`: edición y eliminación de mascotas.
- `core/templates/registration/login.html`: formulario de inicio de sesión de Django.

La aplicación utiliza archivos estáticos en `core/static/` y plantillas en `core/templates/`. Las imágenes de cada mascota se guardan como URL (`URLField`), no como archivos subidos al servidor.
