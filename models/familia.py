class Familia():

    def __init__(self, nomefam: str, identificadorfam: int):
        self.nomefam = nomefam
        self.identificadorfam = identificadorfam

    def get_nome_familia(self):
        return self.nomefam

    def set_nome_familia(self, nomefam):
        self.nomefam = nomefam

    def get_identificador_familia(self):
        return self.identificadorfam

    def __str__(self):
        return "[Nome da familia: " + self.nomefam + "Identificador familia: " + str(self.identificadorfam) + "]"