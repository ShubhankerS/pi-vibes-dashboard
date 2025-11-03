import random

ARTS = [
    r"""
     (\_/)
     ( •_•)
    / >🌼   Chill bunny
    """,
    r"""
     /\_/\
    ( o.o )  Cat says hi
     > ^ <
    """,
    r"""
      🌲🌲🌲
    🌲🌞🌲  Forest Vibes
      🌲🌲
    """,
    r"""
     .-'''-.
    / .===. \  Mushroom Vibes
    \/ 6 6 \/
    ( \___/ )
     \_V_V_/
    """,
    r"""
     ( )   ( )   ( )
      \     |     /
       \   (_)   /
        \       /
         \___/
        ASCII pond 🌿
    """,
]

def get_random_art():
    return random.choice(ARTS)
