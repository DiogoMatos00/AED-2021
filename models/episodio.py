class Episodio():

    def __init__(self, identificadorserie : int, numtemp:int, numep:int, nomeep:str):
        self.identificadorserie = identificadorserie
        self.nomeep = nomeep
        self.numtemp = numtemp
        self.numep = numep

    def get_identificadorserie(self):
        return self.identificadorserie

    def get_nome_episodio(self):
        return self.nomeep

    def set_nome_episodio(self, nomeep):
        self.nomeep = nomeep

    def get_num_temporada(self):
        return self.numtemp

    def set_num_temporada(self, numtemp):
        self.numtemp = numtemp

    def get_num_episodio(self):
        return self.numep

    def set_num_episodio(self, numep):
        self.numep = numep


    def __str__(self):
        return "[Identificador serie: " + str(self.identificadorserie) + "Nome do episodio: " + self.nomeep + "Numero de temporada: " + str(self.numtemp) + "Numero do episodio: " + str(self.numep) + "]"