import json
class Main():
    lista_telefone = []
    def __init__(self):
        print('hola')
        bandera = True
        while bandera:
            valor = input('Presione 1 para agendar un contacto, 2 para buscar en la agenda o 3 para salir')
            valor = int(valor)
            if valor == 1:
                self.agedar_contacto()
            elif valor == 2:
                self.buscar_contacto()
            elif valor == 3:
                bandera = False
                break

    def llamador_accion(self):
        while True:
            print("Cuando desee salir, presione 'Q'")
            nombre1 = input("Escriba un Nombre a agendar: ")
            nombre = nombre1.lower()
            if nombre == "Q" or nombre == "q": break
            telefono = input(f"Escriba el telenofo correspondiente a {nombre1}: ")
            return nombre, int(telefono)

    def agedar_contacto(self):
        nombre, telefono = self.llamador_accion()
        user = {'nombre' : (nombre), 'telefono' : int(telefono)}            
        self.lista_telefone.append(user)
        print(self.lista_telefone)
    
    def buscar_contacto(self):
        persona =  input("Escribe el nombre de quien deseas saber el telefono: ")
        listado = self.lista_telefone
        for usuario in listado:
            if persona in usuario['nombre']:
                person = usuario['nombre']
                person = person.capitalize()
                print(f"{person}: {usuario['telefono']}")
        

if __name__ == '__main__':
    f = Main()