# pyright: strict

import pyxel



pyxel.init(256,144, title="upgaby fight club")
pyxel.images[0].load(0, 0, "assets/lyn/lyn.png")


def update():
    pass

def draw():
    pyxel.cls(0)
    pyxel.blt(60,50,0,0,0,30,30,0)
    pass 

pyxel.run(update, draw)

