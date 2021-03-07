class Cliente:
    def __init__(self, id, name, surname):
        self.__id = id
        self.__name = name
        self.__surname = surname
        self.atendido = False

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @id.setter
    def id(self, val):
        self.__id = val

    @name.setter
    def name(self, val):
        self.__name = val

    @surname.setter
    def surname(self, val):
        self.__surname = val

    def __repr__(self):
        return str(self.__name) + ' ' + str(self.__surname)
