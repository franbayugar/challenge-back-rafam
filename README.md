# Challenge Rafam Backend

 API-Rest desarrollada en Python mediante **Django Rest Framework**:

1. Tras clonar el repositorio, ejecutar el comando ` build.sh `

1. La App ya estará lista para correr localmente

## Deploy en [Render](https://challenger-rafam-back.onrender.com/)
----
Mediante la app web gratuita **Render**, se concretó un deploy de la app para poder hacer uso de la misma con datos precargados en una base de datos *PostgreSQL*

Accediendo a los endpoints se podrán verificar algunos de los ítems solicitados en el challenge:

- Listar todos los usuarios
  - api/users 
- Listar lesiones tomadas por un usario
  - api/users-lessons/search?=fran
- Listar los amigos de un usuario
  - api/users-friends/search?=fran

### Desarrollo del challenge

Inicialmente se realizó un UML para poder establecer los modelos que finalmente impactarían sobre la BBDD, llegando al a conclusión de que sería necesaria una relación Many to Many, tanto para usuarios y lecciones tomadas como para las amistades que puede llegar a tener un usuario, por lo que se debía lograr esto con una tabla intermedia.

Tras leer la documentación del framework a utilizar, se procedió a realizar la estructura general del proyecto y finalizar con parte de los unit test, únicamente del View de Course, dado que el resto de los modelos necesitaban de otros datos iniciales para poder funcionar y no llegué a descubrir como poder simularlo en el test.