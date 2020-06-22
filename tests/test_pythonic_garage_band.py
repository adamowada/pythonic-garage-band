from pythonic_garage_band import __version__
from pythonic_garage_band.pythonic_garage_band import *

def test_version():
    assert __version__ == '0.1.0'


def test_guitarist_solo_one():
    test = Guitarist("Spike", "Brown chicken brown cow!")
    expected = "Spike's solo sounds like this: Brown chicken brown cow!"
    actual = test.play_solo()
    assert actual == expected


def test_guitarist_solo_two():
    test = Guitarist("Mike", "Bwaaa ri ri bwaaaaaa!")
    expected = "Mike's solo sounds like this: Bwaaa ri ri bwaaaaaa!"
    actual = test.play_solo()
    assert actual == expected


def test_drummer_solo_one():
    test = Drummer("Ringo", "tap tap tap tap ba daaa")
    expected = "Ringo's solo sounds like this: tap tap tap tap ba daaa"
    actual = test.play_solo()
    assert actual == expected


def test_bassist_solo_one():
    test = Bassist("Adam", "da do dee do dum de dooo")
    expected = "Adam's solo sounds like this: da do dee do dum de dooo"
    actual = test.play_solo()
    assert actual == expected


def test_guitarist_repr():
    test = Guitarist('Matt', 'Zhweee bap baaa!')
    expected = "Guitarist('Matt', 'Zhweee bap baaa!')"
    actual = repr(test)
    assert actual == expected


def test_bassist_repr():
    test = Bassist("Al", "doe ray mi fa so la ti doe")
    expected = "Bassist('Al', 'doe ray mi fa so la ti doe')"
    actual = repr(test)
    assert actual == expected


def test_drummer_str():
    test = Drummer("Travis", "tst tst kats-it tst tst kats-is")
    expected = "Travis: tst tst kats-it tst tst kats-is"
    actual = str(test)
    assert actual == expected


def test_band_to_list():
    actual = str(Band.to_list())
    expected = 'Warm October: Mike Matt Adam Phill Dave '
    assert actual == expected


def test_band_play_solos():
    actual = band_1.play_solos()
    expected = "Mike's solo sounds like this: Bwaaa ri ri bwaaaaaa! Matt's solo sounds like this: Zhweee bap baaa! Adam's solo sounds like this: da do dee do dum de dooo Phill's solo sounds like this: bwawawawawaaaaaaa Dave's solo sounds like this: ba-du-bi-do-ba-ba-ba-ba-ba-tshhh "
    assert actual == expected
