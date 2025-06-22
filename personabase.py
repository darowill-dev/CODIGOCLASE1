from faker import Faker

get_data = Faker()
class PersonaBase ():
    def _init_(self,nombre,edad):
        self.nombre = get_data.name()
        self.edad = get_data.random_int(min=18, max=99)

        def presentarse(self):
            print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")