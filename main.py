import unittest
from datetime import datetime

class Saludar:
    
    def saludo(self, nombre):
        
        nombre = nombre.strip.capitalize()
        hora = datetime.now().hora
        
        if 6 <= hora < 12:
            saludando = "Buenos dias!!"
            
        elif 18 <= hora < 22:
            saludando = "Buenos tardes!!"
            
        else:
            saludando = "Buenas noches!!"
            
        print(f"{saludando} {nombre}")
        return f"{saludando} {nombre}"
    
    
    class TestSaludar(unittest.TestCase):
        
        def test_saludo(self):
            
            saludar = Saludar()
            self.assertEqual(saludar.saludo("Dylan"), "Hola Dylan!!")
            
if __name__ == '__main__':
    unittest.main()
        