from flask import Flask, request, jsonify

app = Flask(__name__)

# Estructura de datos en memoria para usuarios
usuarios = []

# Estructura de datos para productos
productos = [
    {"id": 1, "nombre": "Producto 1", "precio": 100},
    {"id": 2, "nombre": "Producto 2", "precio": 150}
]

# Ruta GET /info
@app.route('/info', methods=['GET'])
def get_info():
    return jsonify({
        "nombre": "Servidor Capstone",
        "descripcion": "API REST para gestionar usuarios y productos"
    })

# Ruta POST /crear_usuario
@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    data = request.get_json()

    # Obtiene los datos 
    nombre = data.get('nombre')
    correo = data.get('correo')

    if not nombre or not correo:
        return jsonify({"error": "El nombre y el correo son obligatorios."}), 400

    # Crea un nuevo usuario 
    nuevo_usuario = {
        "nombre": nombre,
        "correo": correo
    }
    usuarios.append(nuevo_usuario)

    return jsonify({
        "mensaje": "Usuario creado con éxito",
        "usuario": nuevo_usuario
    })

# Ruta GET /usuarios
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    return jsonify(usuarios)

# Ruta GET /productos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    return jsonify(productos)

# Ruta POST /producto
@app.route('/producto', methods=['POST'])
def crear_producto():
    data = request.get_json()

    
    nombre = data.get('nombre')
    precio = data.get('precio')

    if not nombre or not precio:
        return jsonify({"error": "El nombre y el precio son obligatorios."}), 400

    # Crea producto
    nuevo_producto = {
        "id": len(productos) + 1,  
        "nombre": nombre,
        "precio": precio
    }
    productos.append(nuevo_producto)

    return jsonify({
        "mensaje": "Producto creado con éxito",
        "producto": nuevo_producto
    })


if __name__ == '__main__':
    app.run(debug=True)
