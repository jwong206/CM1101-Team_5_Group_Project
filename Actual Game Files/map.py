from items import *

room_enterprise = {
    "name": "Enterprise",

    "description":
    """----------\n You are standing in what appears to be the command deck of a ship, but not a\n ship from your time.\n You are surrounded by computers that seem to be operating on their own,\n though you have no real idea of what they are for.\n After a short while you hear the humming sound of something turning on.\n After which, in the four cardinal points of the room, doors open revealing\n lit up circular pads.\n----------""",
    "exits": {"south": "Star Wars V Star Trek", "east": "Indiana Jones", "west": "Western", "north": "Mr Robot"},

    "items": [item_biscuits, item_handbook]
}

room_western = {
    "name": "Western Room",

    "description":
    """----------\n The shimmering lights around you fades and you find yourself standing in the\n centre of an old desert town.\n The single street is empty and there are several buildings on each side of\n the road.\n The time period here is definitely different as you notice several dated\n methods of transport.\n----------""",

    "exits":  {"north": "Sherlock", "east": "Enterprise", "south": "Jurassic Park"},

    "items": []
}

room_robot = {
    "name": "Mr Robot's Room",

    "description":
    """You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The reception is to the west.""",

    "exits": {"east": "Book of Eli", "south": "Enterprise", "west": "Sherlock"},

    "items": []
}

room_indiana = {
    "name": "The Temple of Doom",

    "description":
    """You are standing in the Queen's Buildings parking lot.
You can go south to the COMSC reception, or east to the
general office.""",

    "exits": {"north": "Book of Eli", "south": "Portal Room", "west": "Enterprise"},

    "items": []
}

room_SWVST = {
    "name": "Millennium Falcon",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"north": "Enterprise", "east": "Portal Room", "west": "Jurassic Park"},

    "items": [item_pen]
}

room_jurassic = {
    "name": "Jurassic World",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"north": "Western", "east": "Star Wars V Star Trek", "south": "Inception", "passage": "Sherlock", "trapdoor": "Portal Room"},

    "items": [item_pen]
}

room_sherlock = {
    "name": "221B Baker Street",

    "description":
    """----------\n You take a step forward exiting the shimmering lights that soon fade away.\n Taking a glance around the room you find yourself standing by a desk located\n in a darkened library.\n For what you can see in the darkness you notice multiple bookshelves located\n around you as well as open books and notepads on the desk by your side.\n----------""",

    "exits": {"east": "Mr Robot", "south": "Western", "north": "Shawshank", "passage": "Book of Eli", "trapdoor": "Jurassic Park"},

    "items": [item_pen]
}

room_Eli = {
    "name": "West Coast of the United States",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"north": "Fight Club", "south": "Indiana Jones", "west": "Mr Robot", "passage": "Portal Room", "trapdoor": "Sherlock"},

    "items": [item_pen]
}

room_portal = {
    "name": "The Planes",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"north": "Indiana Jones", "south": "Matrix", "west": "Star Wars V Star Trek", "passage": "Jurassic Park", "trapdoor": "Book of Eli"},

    "items": [item_pen]
}

room_matrix = {
    "name": "The Matrix",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"south": "Portal Room"},

    "items": [item_pen]
}

room_inception = {
    "name": "A Lucid Dream",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"south": "Jurassic Park"},

    "items": [item_pen]
}

room_shawshank = {
    "name": "Shawshank State Penitentiary",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"north": "Sherlock"},

    "items": [item_pen]
}
room_fight = {
    "name": "An underground club",

    "description":
    """You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""",

    "exits": {"north": "Book of Eli"},

    "items": [item_pen]
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
