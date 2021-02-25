from utilities import Utilities
from cliente import Cliente
from caja import Caja
from cola import Cola
import random
import time

names = ['nombre1', 'nombre2', 'nombre3', 'nombre4']
surnames = ['apellido1', 'apellido2', 'apellido3', 'apellido4']


def main():
    caja1 = Caja(1)
    caja2 = Caja(2)
    cola = Cola([caja1, caja2])

    for i in range(4):
        print('Llego un cliente...')
        new_client = Cliente(i + 1, random.choice(names), random.choice(surnames))
        cola.add_client(new_client)
        time.sleep(2)

        print('Cliente atendido...')
        cola.remove_client()
        time.sleep(1)

    Utilities.clear()
    Utilities.eexit()


if __name__ == '__main__':
    main()
