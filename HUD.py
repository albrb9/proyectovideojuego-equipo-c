import arcade
import os


def dibujar_hud():
    """Dibuja en pantalla el hud si se invoca en el método on_draw"""
    barra_de_vida = arcade.load_texture("sprites_master"+os.path.sep+"VIDA.png")
    arcade.draw_texture_rectangle(100, 865, 200, 50, barra_de_vida)




