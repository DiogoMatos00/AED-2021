from aed_ds.singly_linked_list import SinglyLinkedList
from aed_ds.open_hash_table import OpenHashTable



class Serie():

    def __init__(self, nomeserie: str, identificadorserie: int):
        self.nomeserie = nomeserie
        self.identificadorserie = identificadorserie
        self.num_temp = OpenHashTable(30)

    def get_nome_serie(self):
        return self.nomeserie

    def set_nome_serie(self, nomeserie):
        self.nomeserie = nomeserie

    def get_identificador_serie(self):
        return self.identificadorserie

    def get_episodios(self):
        return self.episodios
    
    def get_numtemp(self):
        return self.numtemp

    def get_episodios_alugados(self):
        return self.episodios_alugados        

    def __str__(self):
        return "[Nome serie: " + self.nomeserie + "Identificador serie: " + str(self.identificadorserie) + "]"