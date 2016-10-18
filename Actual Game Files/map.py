from items import *
from interactions import *

room_Hub = {
    "name": "Hub",

    "description":
    """----------\n You are standing in what appears to be the command deck of a ship however not a ship from your time.\n You are surrounded by computers that seem to be operating on their own though you have no real\n idea of what they are for.\n After a short while you hear the a humming sound as if something was turning on after which,\n in the four cardinal points of the room, doors open revealing lit up circular pads.\n The light reveals a console standing in the centre of the room, awaiting an input.\n----------""",

    "exits": {"south": "Star Wars", "east": "Indiana Jones", "west": "Shawshank", "north": "Mr Robot"},

    "items": [item_fragment1],
    "interacts": [interact_console],

    "date": "Unknown"
}

room_robot = {
    "name": "Mr Robot's Room",

    "description":
    """----------\n You enter an ancient relic of the past: A video game arcade.\n As you look around, you see computer components spread across most surfaces.\n You also spot a single functioning arcade machine.\n----------""",

    "exits": {"east": "Book of Eli", "south": "Hub", "west": "Sherlock"},

    "items": [item_phone],
    "interacts": [interact_arcade, interact_laptop],

    "date": "2016"
}

room_indiana = {
    "name": "The Temple of Doom",

    "description":
    """----------\n You find yourself standing at the base of a large set of stairs.\n The room around you seems ancient and the walls are covered in carvings which are completely\n unintelligible to you.\n Atop the stairs you can see a sort of shrine with <key item here> centered on it.\n There are several crates littered around this shrine that seem out of place.\n----------""",

    "exits": {"north": "Book of Eli", "south": "Fight Club", "west": "Hub"},

    "items": [],
    "interacts": [interact_tombstone, interact_crates],

    "date": "1935"
}

room_SW = {
    "name": "Millennium Falcon",

    "description":
    """----------\n Once you enter the room you could already tell you've found yourself in what appears to be\n another ship though nowhere near as flashy as the other.\n What a piece of junk.\n You roam the corridors and this ship until you find yourself in what looks to be a place the crew\n would use for relaxing.\n There's a mini chess-like table that has active holograms battling atop it.\n----------""",

    "exits": {"north": "Hub", "east": "Fight Club", "west": "Jurassic World"},

    "items": [],
    "interacts": [interact_bb8, interact_holochess],

    "date": "A long time ago..."
}

room_jurassic = {
    "name": "Jurassic World",

    "description":
    """----------\n Once you took a step through the exit you have now found yourself standing in a forest.\n You're surrounded by trees and thick bushes and the only sounds you can initially hear are of birds\n high up in the trees.\n You approach a small cabin which appears to not have been used in a long time.\n The tables, bed and pretty much everything is covered in dust.\n----------""",

    "exits": {"north": "Shawshank", "east": "Star Wars"},

    "items": [item_photo],
    "interacts": [],

    "date": "2020"
}

room_sherlock = {
    "name": "221B Baker Street",

    "description":
    """----------\n You take a step forward exiting the shimmering lights that soon fade away.\n Taking a glance around the room you find yourself standing by a desk located\n in a darkened library.\n For what you can see in the darkness you notice multiple bookshelves located\n around you as well as open books and notepads on the desk by your side.\n----------""",

    "exits": {"east": "Mr Robot", "south": "Shawshank"},

    "items": [item_violin],
    "interacts": [interact_book],

    "date": "2015"
}

room_Eli = {
    "name": "West Coast of the United States",

    "description":
    """----------\n You take several steps into this new area.\n As opposed to what you've already seen, this area is desolate, broken.\n The area is filled with old broken objects, small buildings completely in ruin.\n You rummage through some boxes and crates though find nothing but there's still others\n remaining to be searched.\n----------""",

    "exits": {"south": "Indiana Jones", "west": "Mr Robot"},

    "items": [item_ammo],
    "interacts": [interact_walkietalkie, interact_radio],
    "date": "30 years after a nuclear apocalypse"
}

room_shawshank = {
    "name": "Shawshank State Penitentiary",

    "description":
    """----------\n You enter the room and it becomes clear you are suddenly in a prison cell block.\n Each individual cell is opened slightly with no prisoners in sight.\n The area is littered with old clothing from both prisoners and guards.\n You approach the guard's desk to find it cluttered with magazines, torn up papers and some books.\n----------""",

    "exits": {"north": "Sherlock","south": "Jurassic World"},

    "items": [item_shirt, item_page, item_magazine],
    "interacts": [],
    "date": "1965"
}
room_fight = {
    "name": "An underground club",

    "description":
    """----------\n You find yourself now standing in what appears to be a basement.\n There is a laid out square in the centre covered in what appears to be blood stains.\n Around the room there are several large crates and large plastic containers labeled 'Fat'.\n You find several scraps of paper, some of which are entitled 'How to make soap', whilst the others\n contain completely different information.\n----------""",

    "exits": {"north": "Indiana Jones","west":"Star Wars"},

    "items": [],
    "interacts": [interact_mirror],
    "date": "1999"
}

rooms = {
    "Hub": room_Hub,
    "Mr Robot": room_robot,
    "Indiana Jones": room_indiana,
    "Star Wars": room_SW,
    "Jurassic World": room_jurassic,
    "Sherlock": room_sherlock,
    "Book of Eli": room_Eli,
    "Shawshank": room_shawshank,
    "Fight Club": room_fight
}
