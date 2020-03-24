![Python application](https://github.com/EndermanAPM/rest-bookstore/workflows/Python%20application/badge.svg)

# Notas:  
Changed 1:n book-order relationship to n:m to allow multiple books on a single purchase.
Also added status, order total and date to order. (VAT ignored)  
Stock merged into books because it doesn't provide additional fields to books.  
The Order endpoint returns and allows to post the nested OrderBook(s).  
This api is in no way production ready, starting with secret management, no logging, production server,
persistence of database, debug mode on.

## Additional features:
- Git/Github repository
- requirements file
- Unique constrain to prevent duplicated books on a single order
- Atomicity when handling multiple model objects.
- Filtering and ordering (additionally to searching)
- Pagination
- jwt (Instead of basic auth) **BASIC AUTH WILL NOT WORK!**
- Detailed view on order (with purchased books)
- Hyperlinked api
- dockerization
- Ci (images being build and tested every commit by Github actions)

## Missing features
- Calculated purchase total
- Proper logging

## Todo:
- tests
- pyup
- ssl?

### Una base de datos para una librería con las tablas:
- usuarios(id,nombre,edad,fecha_registro,telefono,puntos)
- compras:(id,usuario,libro)
- libros(id,titulo,genero,cantidad,precio,fecha_registro)
- generos(id_genero,nombre)
- stock(id_cantidad,cantidad)



La aplicación tiene que permitir:
- [x] Autentificación de usuario básica para (crear/editar/borrar)
- [x] Crear/editar/borrar: usuarios, libros,géneros,stock
- [x] Consultar todas las tablas
- [x] Buscar en todas las tablas por id/nombre
- [x] Las tablas de géneros y stock están conectadas con libro
- [x] El campo puntos del usuario se actualiza con 1 punto cada vez que compra

