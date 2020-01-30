import waifu

class Player:


    def __init__(self, name):
        self.name = name
        self.waifus = []

    def get_name(self):
        return self.name

    def get_waifus(self):
        return self.waifus

    def add_waifu(self, waifu : waifu.Waifu):
        self.waifus.append(waifu)

    def get_specefic_desk(self, n):
        return self.waifus[n]

    def remove_waifu(self, waifu):
        self.waifus.remove(waifu)
