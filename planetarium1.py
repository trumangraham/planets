class planet(object):

    def __init__(self, planet, description,moons, tempature):
        self.planet = planet
        self.description = description
        self.moons = moons
        self.tempature = tempature

    def __str__(self):
        return f"Planet: {self.planet} \nDescription: {self.description} \nMoons: {self.moons} \nAverage Tempature: {self.tempature} degrees"
    
