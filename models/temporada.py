from aed_ds.open_hash_table import OpenHashTable

class Temporada():

    def __init__(self, num_temporada):
        self.num_episodios = OpenHashTable(50)
        self.num_temporada = num_temporada

    def get_num_episodios(self):
        return self.num_episodios

    def get_num_temporada(self):
        return self.num_temporada

    def __str__(self):
        return "[Numero do episodio: " + self.num_episodios + "Numero da temporada: " + str(self.num_temporada) + "]"