![Python application](https://github.com/EndermanAPM/rest-bookstore/workflows/Python%20application/badge.svg)
[![Updates](https://pyup.io/repos/github/EndermanAPM/rest-bookstore/shield.svg?token=bbea8f64-35d8-4063-b999-85ca5369532b)](https://pyup.io/repos/github/EndermanAPM/rest-bookstore/)

# Notes:  
Changed 1:n book-order relationship to n:m to allow multiple books on a single purchase.  
Also added status, order total and date to order. (VAT ignored)  
Stock merged into books because it doesn't provide additional fields to books.    

This api is in no way production ready, starting with secret management, no logging, production server,
persistence of database, debug mode on. With that in mind, using the docker compose on a server with an already 
existing traefik router, ran without problems. At https://taclia.acmotos.com/api/token/
Remember that you will need the tokens to create and edit.

    curl \
      -X POST \
      -H "Content-Type: application/json" \
      -d '{"username": "foo", "password": "bar"}' \
      https://taclia.acmotos.com/api/token/


CDN will cache almost nothing (because most of the content is dynamic) but CF Argo, Automatic SSL certs, DDOS protection,
 etc are nice to have.
   
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
- CDN (Cloudflare)
- SSL
- pyup (dependency updater)
- openapi schema

## Missing
- Logging
- Code comments and documentation
- tests



## Misc:
 Una base de datos para una librería con las tablas:
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

