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


class Band:

    prev_bands = []

    def __init__(self, name, members=None):
        self.name = name
        if members is None:
            self.members = []
            Band.prev_bands.append(self)
        else:
            self.members = members
            Band.prev_bands.append(self)

    def play_solos(self):
        for i in self.members:
            print(i.play_solo())

    @classmethod
    def to_list(cls):
        for i in cls.prev_bands:
            return i


guitar_1 = Guitarist("Adam", "Brown chicken brown cow!")

print(guitar_1.name)
print(guitar_1.get_instrument())
print(guitar_1.play_solo())
