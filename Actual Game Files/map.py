from items import *

room_enterprise = {
    "name": "Enterprise",

    "description":
    """----------\n You are standing in what appears to be the command deck of a ship, but not a\n ship from your time.\n You are surrounded by computers that seem to be operating on their own,\n though you have no real idea of what they are for.\n After a short while you hear the humming sound of something turning on.\n After which, in the four cardinal points of the room, doors open revealing\n lit up circular pads.\n----------""",
    "exits": {"south": "Star Wars V Star Trek", "east": "Indiana Jones", "west": "Western", "north": "Mr Robot"},

    "items": [item_biscuits, item_handbook],
    "date": "Stardate 41254.7"
}

room_western = {
    "name": "Western Room",

    "description":
    """----------\n The shimmering lights around you fades and you find yourself standing in the\n centre of an old desert town.\n The single street is empty and there are several buildings on each side of\n the road.\n The time period here is definitely different as you notice several dated\n methods of transport.\n----------""",

    "exits":  {"north": "Sherlock", "east": "Enterprise", "south": "Jurassic Park"},

    "items": [],
    "date": "March 12th, 1870"
}

room_robot = {
    "name": "Mr Robot's Room",

    "description":
    """You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The reception is to the west.""",

    "exits": {"east": "Book of Eli", "south": "Enterprise", "west": "Sherlock"},

    "items": [],
    "date": "2016"
}

room_indiana = {
    "name": "The Temple of Doom",

    "description":
    """----------\n You find yourself standing at the base of a large set of stairs.\n The room around you seems ancient and the walls are covered in carvings which are completely unintelligible to you.\n Atop the stairs you can see a sort of shrine with <key item here> centered on it.\n----------""",

    "exits": {"north": "Book of Eli", "south": "Portal Room", "west": "Enterprise"},

    "items": [],
    "date": "1935"
}

room_SWVST = {
    "name": "Millennium Falcon",

    "description":
    """----------\n Once the light fades you find yourself standing in what appears to be the cockpit of yet another ship.\n Everything appears to be powered down however you hear noises coming from somewhere not far from you, objects seem to being moved and voices raised.\n You cautiously take a quick look around only to be discovered by a being you are unfamiliar with and it appears to be hostile!\n----------""",

    "exits": {"north": "Enterprise", "east": "Portal Room", "west": "Jurassic Park"},

    "items": [item_pen],
    "date": "A long time ago"
}

room_jurassic = {
    "name": "Jurassic World",

    "description":
    """----------\n Once you took a step through the exit you have now found yourself standing in a forest.\n You're surrounded by trees and thick bushes and the only sounds you can initially hear are of birds high up in the trees.\n After a short period of brief inspection you begin to get the feeling that you are being watched.\n----------""",

    "exits": {"north": "Western", "east": "Star Wars V Star Trek", "south": "Inception", "passage": "Sherlock", "trapdoor": "Portal Room"},

    "items": [item_pen],
    "date": "2015"
}

room_sherlock = {
    "name": "221B Baker Street",

    "description":
    """----------\n You take a step forward exiting the shimmering lights that soon fade away.\n Taking a glance around the room you find yourself standing by a desk located\n in a darkened library.\n For what you can see in the darkness you notice multiple bookshelves located\n around you as well as open books and notepads on the desk by your side.\n----------""",

    "exits": {"east": "Mr Robot", "south": "Western", "north": "Shawshank", "passage": "Book of Eli", "trapdoor": "Jurassic Park"},

    "items": [item_pen],
    "date": "2015"
}

room_Eli = {
    "name": "West Coast of the United States",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"north": "Fight Club", "south": "Indiana Jones", "west": "Mr Robot", "passage": "Portal Room", "trapdoor": "Sherlock"},

    "items": [item_pen],
    "date": "30 years after a nuclear apocalypse"
}

room_portal = {
    "name": "The Plains",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"north": "Indiana Jones", "south": "Matrix", "west": "Star Wars V Star Trek", "passage": "Jurassic Park", "trapdoor": "Book of Eli"},

    "items": [item_pen],
    "date": ""
}

room_matrix = {
    "name": "The Matrix",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"south": "Portal Room"},

    "items": [item_pen],
    "date": "1999... or is it?"
}

room_inception = {
    "name": "A Lucid Dream",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"south": "Jurassic Park"},

    "items": [item_pen],
    "date": "Who knows."
}

room_shawshank = {
    "name": "Shawshank State Penitentiary",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"north": "Sherlock"},

    "items": [item_pen],
    "date": "1965"
}
room_fight = {
    "name": "An underground club",

    "description":
    """----------\n After taking the exit you come to find yourself laying face first on the floor with a loud ringing sound in your ears which is followed by a wave of pain.\n It takes a few moments but you finally begin to hear again however it is faded yelling at first which gradually becomes more clear.\n Pulling yourself to your feet you find yourself standing in a darkened room surrounded by yelling spectators as you come face to face with a man who shoves you back somewhat and looks as if he is ready to fight!\n----------""",

    "exits": {"north": "Book of Eli"},

    "items": [item_pen],
    "date": "1999"
}

rooms = {
    "Enterprise": room_enterprise,
    "Western": room_western,
    "Mr Robot": room_robot,
    "Indiana Jones": room_indiana,
    "Star Wars V Star Trek": room_SWVST,
    "Jurassic Park": room_jurassic,
    "Sherlock": room_sherlock,
    "Book of Eli": room_Eli,
    "Portal Room": room_portal,
    "Matrix": room_matrix,
    "Inception": room_inception,
    "Shawshank": room_shawshank,
    "Fight Club": room_fight


}
