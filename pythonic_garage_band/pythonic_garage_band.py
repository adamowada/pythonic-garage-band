class Musician:

    instrument = "Unknown"

    def __init__(self, name, solo):
        self.name = name
        self.solo = solo

    def get_instrument(self):
        return self.name + " plays the " + self.instrument

    def play_solo(self):
        return self.name + "'s solo sounds like this: " + self.solo

    def __repr__(self):
        return "Musician('{}', '{}')".format(self.name, self.solo)

    def __str__(self):
        return '{}: {}'.format(self.name, self.solo)


class Guitarist(Musician):

    instrument = "Guitar"

    def __repr__(self):
        return "Guitarist('{}', '{}')".format(self.name, self.solo)

    def __str__(self):
        return '{}: {}'.format(self.name, self.solo)


class Bassist(Musician):

    instrument = "Bass"

    def __repr__(self):
        return "Bassist('{}', '{}')".format(self.name, self.solo)

    def __str__(self):
        return '{}: {}'.format(self.name, self.solo)


class Drummer(Musician):

    instrument = "Drums"

    def __repr__(self):
        return "Drummer('{}', '{}')".format(self.name, self.solo)

    def __str__(self):
        return '{}: {}'.format(self.name, self.solo)


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

    def __repr__(self):
        return 'Band("{}", "{}")'.format(self.name, self.members)

    def __str__(self):
        string = self.name + ': '
        for i in self.members:
            string += i.name + ' '
        return string

    @classmethod
    def to_list(cls):
        for i in cls.prev_bands:
            return i


guitar_1 = Guitarist("Spike", "Brown chicken brown cow!")
guitar_2 = Guitarist("Mike", "Bwaaa ri ri bwaaaaaa!")
guitar_3 = Guitarist("Matt", "Zhweee bap baaa!")

bass_1 = Bassist("Adam", "da do dee do dum de dooo")
bass_2 = Bassist("Phill", "bwawawawawaaaaaaa")
bass_3 = Bassist("Al", "doe ray mi fa so la ti doe")

drum_1 = Drummer("Dave", "ba-du-bi-do-ba-ba-ba-ba-ba-tshhh")
drum_2 = Drummer("Ringo", "tap tap tap tap ba daaa")
drum_3 = Drummer("Travis", "tst tst kats-it tst tst kats-is")

band_1 = Band("Warm October", [guitar_2, guitar_3, bass_1, bass_2, drum_1])


band_1.play_solos()
Band.to_list()
print(repr(bass_1))
print(repr(band_1))
print(str(band_1))