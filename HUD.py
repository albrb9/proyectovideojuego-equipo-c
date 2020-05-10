import arcade
import os


def dibujar_hud():
    """Dibuja en pantalla el hud si se invoca en el método on_draw"""
    barra_de_vida = arcade.load_texture("sprites_master" + os.path.sep + "VIDA.png")
    arcade.draw_texture_rectangle(100, 865, 200, 50, barra_de_vida)


def dibujar_pantalla_de_inicio():
    arcade.draw_lrtb_rectangle_filled(0, 900, 900, 0, arcade.color.BLACK)
    arcade.draw_text("Pulsa enter para comenzar", 0, 450, arcade.color.WOOD_BROWN, 40, 900, "center", bold=True)
    arcade.draw_text("Pulsa 'C' para ver los controles", 0, 350, arcade.color.WOOD_BROWN, 30, 900, "center")


def dibujar_controles():
    arcade.draw_lrtb_rectangle_filled(0, 900, 900, 0, arcade.color.BLACK)
    arcade.draw_text("Moverse: W,A,S,D ó las flechas", 0, 550, arcade.color.WOOD_BROWN, 20, 900, "center")
    arcade.draw_text("Disparar: Q", 0, 450, arcade.color.WOOD_BROWN, 20, 900, "center")
    arcade.draw_text("Bloquear dirección: Espacio", 0, 350, arcade.color.WOOD_BROWN, 20, 900, "center")
    arcade.draw_text("Pausar/Reaunudar el juego: P", 0, 250, arcade.color.WOOD_BROWN, 20, 900, "center")
    arcade.draw_text("Pulsa retroceso para volver", 0, 100, arcade.color.WOOD_BROWN, 20, 900, "center")

def dibujar_hud_pausado():
    arcade.draw_lrtb_rectangle_filled(0, 900, 900, 0, arcade.color.BLACK)
    arcade.draw_text("Pausado", 0, 450, arcade.color.WOOD_BROWN, 40, 900, "center", bold=True)


