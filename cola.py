import random


class Cola:
    def __init__(self, num_caja):
        self.client = []
        self.cajas = num_caja

    def add_client(self, client):
        self.client.append(client)
        self.write_file()

    def remove_client(self):
        client = self.client.pop(0)
        self.atendido = True

        caja = random.choice(self.cajas)
        caja.add_attend_client(client)

        self.write_file()

    def write_file(self):
        file = open('log.txt', 'w')

        print('Clientes en COLA\n')

        for i in self.client:
            file.writelines(f'{i.name} {i.surname}\n')

        print('\nClientes Atendidos\n')

        for caja in self.cajas:
            file.writelines(f'\nCaja {caja.get_num_caja()}:\n')
            for client in caja.get_client_attended():
                file.writelines(f'{client.name} {client.surname}\n')

        file.close()

    def read_file(self):
        file = open('log.txt', 'r')
        file.close()
