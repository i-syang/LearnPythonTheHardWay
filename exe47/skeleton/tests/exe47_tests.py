from nose.tools import *
from exe47.game import Room

"""
def setup():
    print ("SETUP!")

def teardown():
    print ("TEAR DOWN!")

def test_basic():
    print ("I RAN!")

"""

def test_room():
    gold = Room("GoldRoom", "gold")
    # gold.name = "GoldRoom"
    # gold.description = "gold"
    # gold.go("gold")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Center")
    north = Room("North", "North")
    south = Room("South", "South")

    center.add_paths({'north': north, 'south': south})
    # center.paths = {'north': north, 'south': south}
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "start")
    west = Room("Trees", "Trees")
    down = Room("Dungeon", "Dungeon")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'),start)
