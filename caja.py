class Caja:
    def __init__(self, numCaja):
        self.client_attended = []
        self.num_caja = numCaja

    def add_attend_client(self, client):
        self.client_attended.append(client)

    def get_num_caja(self):
        return self.num_caja

    def get_client_attended(self):
        return self.client_attended
