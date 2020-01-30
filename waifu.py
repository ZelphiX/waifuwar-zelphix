class Waifu:

    def __init__(self, name, points):
        self.name = name
        self.points = points
        self.waifus_list = []

    def get_name(self):
        return self.name

    def get_points(self):
        return self.points

    def get_waifus_list(self):
        return self.waifus_list

    def get_specefic_waifu(self, n):
        return self.waifus_list[n]
    
        
