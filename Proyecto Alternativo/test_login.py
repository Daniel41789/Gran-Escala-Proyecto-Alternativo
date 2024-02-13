import unittest
import mysql.connector
from main import iniciar_sesion

class TestIniciarSesion(unittest.TestCase):
    def setUp(self):
        # Configurar la conexión a la base de datos de prueba
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Daniel4178.",
            database="micro_x_test"  # Utiliza una base de datos de prueba separada
        )
        self.cursor = self.conn.cursor()

        # Crea la tabla de usuarios de prueba y agrega algunos datos de prueba
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                usuario VARCHAR(255),
                                contraseña VARCHAR(255)
                              )''')
        self.cursor.execute('''INSERT INTO usuarios (usuario, contraseña) VALUES (%s, %s)''', ('Furina', '123'))

    def tearDown(self):
        # Cerrar la conexión y revertir cualquier cambio en la base de datos
        self.cursor.execute("DROP TABLE IF EXISTS usuarios")
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def test_iniciar_sesion_exitoso(self):
        # Ejecutar la función de inicio de sesión con credenciales válidas
        resultado = iniciar_sesion("Furina", "123", self.conn)

        # Verificar que el resultado sea True (inicio de sesión exitoso)
        self.assertTrue(resultado)

    def test_iniciar_sesion_fallido(self):
        # Ejecutar la función de inicio de sesión con credenciales inválidas
        resultado = iniciar_sesion("usuario_invalido", "contraseña_invalida", self.conn)

        # Verificar que el resultado sea False (inicio de sesión fallido)
        self.assertFalse(resultado)

if __name__ == '__main__':
    # Ejecutar las pruebas unitarias y mostrar los resultados en la terminal
    unittest.main(verbosity=2)
