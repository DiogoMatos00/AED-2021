class alug():
    def __init__(self, id_cliente, id_serie, id_ep, id_temp):
        self.id_cliente = id_cliente
        self.id_serie = id_serie
        self.id_ep = id_ep
        self.id_temp = id_temp

    def tempo_de_aluger(self):
        #return tempo_agora - tempo_do_aluger
        return

    def pessoa_aluga(self):
        return self.id_cliente
    
    def serie_alugada(self):
        return self.id_serie

    def temporada_alugada(self):
        return self.id_ep

    def episodio_alugada(self):
        return self.id_temp