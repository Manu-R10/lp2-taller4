# Lenguaje de Programación 2 - Taller 4

![commits](https://badgen.net/github/commits/clubdecomputacion/lp2-taller4?icon=github) 
![last_commit](https://img.shields.io/github/last-commit/clubdecomputacion/lp2-taller4)

- ver [badgen](https://badgen.net/) o [shields](https://shields.io/) para otros tipos de _badges_

## Autor

- [@Manuel Raigosa](https://www.github.com/Manu-R10)

## Descripción del Proyecto
# GYM RAI 
Es una aplicación web diseñada para administrar los miembros y los planes de membresía de un gimnasio. El sistema tendrá dos entidades relacionadas: **Plan**, con los campos `id`, `nombre`, `precio` y `duracion_dias`; y **Miembro**, con los campos `id`, `nombre`, `edad`, `telefono` y `plan_id`. La relación será de uno a muchos, ya que un plan puede tener varios miembros inscritos. La aplicación permitirá listar los miembros, consultar sus detalles, filtrar por plan y visualizar los planes disponibles. El sistema estará desarrollado con FastAPI, SQLAlchemy y PostgreSQL, tendrá un frontend diseñado en v0.app y utilizará Nginx como reverse proxy. Los cuatro contenedores se administrarán mediante Docker Compose.


## Proceso
En este proyecto desarrollé una aplicación web para administrar un gimnasio, utilizando Docker Compose para ejecutar cuatro servicios: frontend, API, base de datos PostgreSQL y proxy inverso Nginx. Implementé una API con FastAPI y SQLAlchemy para gestionar los planes y miembros, y diseñé una interfaz web con HTML, CSS y JavaScript para consultar los datos y visualizar los detalles. Finalmente, configuré Nginx como único punto de acceso público y utilicé Git y GitHub para guardar y publicar los cambios del proyecto.


[GUIA.md](docs/GUIA.md)

