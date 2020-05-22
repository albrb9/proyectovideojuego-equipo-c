import arcade
import os


def dibujar_hud(vida, carga_fantasmal):
    """Dibuja en pantalla el hud si se invoca en el método on_draw"""
    # Vida
    if vida == 10:
        vida_x = 0
    elif vida == 9:
        vida_x = -20  # Cada barra de vida una son 20 pixeles
    elif vida == 8:
        vida_x = -40
    elif vida == 7:
        vida_x = -60
    elif vida == 6:
        vida_x = -80
    elif vida == 5:
        vida_x = -100
    elif vida == 4:
        vida_x = -120
    elif vida == 3:
        vida_x = -140
    elif vida == 2:
        vida_x = -160
    elif vida == 1:
        vida_x = -180
    else:
        return  # no tenemos que dibujar vida

    barra_de_vida = arcade.load_texture("sprites_master" + os.path.sep + "VIDA.png", x=vida_x, y=0, width=200,
                                        height=50, mirrored=True)
    arcade.draw_texture_rectangle(100, 865, 200, 50, barra_de_vida)  # centrox, centroy, ancho, alto, textura

    # Carga Fantasmal
    carga_fantasmal = str(carga_fantasmal)  # lo convertimos a String
    arcade.draw_text(carga_fantasmal, 10, 800, arcade.color.WHITE, 24)


def dibujar_contador_de_muerte(contador):
    arcade.draw_text(str(int(contador / 60)), 445, 825, arcade.color.RED_ORANGE, 40, bold=True, align="center")
    arcade.draw_text("¡Acaba con todos los enemigos de la sala!", 250, 800, arcade.color.RED_ORANGE, 20, bold=True, align="center")


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


def dibujar_hud_gameover():
    arcade.draw_lrtb_rectangle_filled(0, 900, 900, 0, arcade.color.BLACK)
    arcade.draw_text("GAME OVER", 325, 450, arcade.color.RED_DEVIL, 36, align="center", bold=True)
    arcade.draw_text("Pulsa R para reiniciar", 335, 250, arcade.color.RED_DEVIL, 24, align="center")
