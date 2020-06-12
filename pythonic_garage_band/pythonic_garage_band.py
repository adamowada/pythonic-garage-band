class Musician:

    instrument = "Unknown"

    def __init__(self, name, solo):
        self.name = name
        self.solo = solo

    def get_instrument(self):
        return self.name + " plays the " + self.instrument

    def play_solo(self):
        return self.name + "'s solo sounds like this: " + self.solo


class Guitarist(Musician):

    instrument = "Guitar"


class Bassist(Musician):

    instrument = "Bass"


class Drummer(Musician):

    instrument = "Drums"


class Band(Musician):
    pass


guitar_1 = Guitarist("Adam", "Brown chicken brown cow!")

print(guitar_1.name)
print(guitar_1.get_instrument())
print(guitar_1.play_solo())
