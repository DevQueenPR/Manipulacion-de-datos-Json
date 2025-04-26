# API Flask para Gestión de Usuarios y Productos

Este proyecto es un servidor Flask que gestiona **Usuarios** y **Productos** mediante una API REST. Proporciona rutas para obtener información sobre el sistema, crear usuarios y productos, y obtener listas de usuarios y productos almacenados en memoria.
Se utilizó Flask, Python y Postman.

# Propuesta de estructura de datos: 

# Usuarios:

nombre: El nombre del usuario.

correo: Correo electrónico del usuario.

# Productos:

id: Identificador único del producto.

nombre: Nombre del producto.

descripcion: Una descripción breve del producto.

precio: El precio del producto.

# Formato JSON 

  {
    "nombre": "Juan Pérez",
    "correo": "juan@example.com"
  }


{
  "nombre": "Producto 3",
  "precio": 200
}


## Rutas

# Get info 
Trae la descripción y nombre guardada.

![image](https://github.com/user-attachments/assets/fc588deb-bb94-4c69-8447-83f00026c905)

# Post Crear usuario
Se le envía dos argumentos, nombre y correo, cuando las recibe, envía un mensaje.

![image](https://github.com/user-attachments/assets/2c99010a-6c07-45d8-8aba-188aa87b0cff)

# Get usuarios 
Trae todos los usuarios creados. 

![image](https://github.com/user-attachments/assets/d2b131d8-eb6d-4671-acdb-de05c7bfaafd)

# Get productos
Trae todos los productos creados. Cada uno con ID único, nombre y precio.

![image](https://github.com/user-attachments/assets/25f538bc-dcca-43ed-85ce-23aa054dc7b4)

![image](https://github.com/user-attachments/assets/28107c9d-736b-453f-8712-44d640beeb26)

# Post producto 
Crea un product nuevo a base de nombre y precio que se le envíe como parámetro. 

![image](https://github.com/user-attachments/assets/a103c1ed-2ef1-44ce-89a5-b03fa2dff9fb)
