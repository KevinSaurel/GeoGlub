class Cerveza:
    def __init__(self, marca: str, precio: float):
        self.marca = marca        
        self.precio = precio      


class Juego:
    def __init__(self, nombre: str):
        self.nombre = nombre      

   
class Bar:
    def __init__(
        self,
        nombre: str,
        terraza: bool,
        tiene_tele: bool,
        cervezas: list[Cerveza],
        juegos: list[Juego],
        comentario: str = ""
    ):
        self.nombre = nombre          
        self.terraza = terraza        
        self.tiene_tele = tiene_tele  
        self.cervezas = cervezas      
        self.juegos = juegos          
        self.comentario = comentario  

   
class Usuario:
    def __init__(self, nombre: str, apellido: str, edad: int):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

  