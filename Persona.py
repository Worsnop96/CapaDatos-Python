from logger_base import log


class Persona:
    def __init__(self, id=None, nombre=None, apellido=None):
        self._id = id
        self._nombre=nombre
        self._apellido = apellido

    def __str__(self):
        return f''' 
        id: {self._id}, nombre: {self._nombre}, Apellido: {self._apellido}
        '''

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self,id):
        self._id = id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido=apellido

if __name__ == '__main__':
    persona1 =  Persona(nombre='carlos', apellido='joaquin')
    log.debug(persona1)