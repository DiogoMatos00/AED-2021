class Cliente():

    def __init__(self, nome: str, plano: str, identificador: int):
        self.nome = nome
        self.plano = plano
        self.identificador = identificador
        self.familia = None

    def get_nome(self):
        return self.nome

    def set_nome(self, nome):
        self.nome = nome

    def get_plano(self):
        return self.plano

    def set_plano(self, plano):
        self.plano = plano

    def get_identificador(self):
        return self.identificador

    def get_familia_cliente(self):
        return self.familia

    def set_familia_cliente(self, familia):
        self.familia = familia

    def __str__(self):
        return "[ Nome do cliente: " + self.nome +  " Plano do cliente: " + self.plano + " Identificador cliente: " + str(self.identificador) + "]"