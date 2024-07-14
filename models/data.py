class Data():

    def __init__(self, data: int):
        self.data = data

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def __str__(self):
        return "[Data: " + str(self.data) + "]"
