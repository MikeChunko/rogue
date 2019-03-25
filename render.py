# File name: render.py
# Author: Michael Chunko
# Python Version: 3.7

# This file contains the functions used to render the screen

import tcod
from engine import colors


def render_all(con, entities, game_map, fov_map, fov_recalculate, screen_width, screen_height):
    # Draw the map
    draw_map(con, game_map, fov_map, fov_recalculate)

    # Draw all entities
    for entity in entities:
        draw_entity(con, entity, fov_map)

    # Draw the player stats
    tcod.console_set_default_foreground(con, tcod.white)
    tcod.console_print_ex(con, 1, screen_height - 4, tcod.BKGND_NONE, tcod.LEFT,
                          "PWR: {0}".format(entities[0].power))
    tcod.console_print_ex(con, 1, screen_height - 3, tcod.BKGND_NONE, tcod.LEFT,
                          "DEF: {0}".format(entities[0].defense))
    tcod.console_print_ex(con, 1, screen_height - 2, tcod.BKGND_NONE, tcod.LEFT,
                          "HP : {0:02}/{1:02}".format(entities[0].hp, entities[0].max_hp))

    tcod.console_blit(con, 0, 0, screen_width, screen_height, 0, 0, 0)


def clear_all(con, entities):
    for entity in entities:
        clear_entity(con, entity)


def draw_map(con, game_map, fov_map, fov_recalculate):
    if fov_recalculate:
        for y in range(game_map.height):
            for x in range(game_map.width):
                visible = tcod.map_is_in_fov(fov_map, x, y)
                wall = game_map.tiles[x][y].block_sight

                # The tile is in the FOV
                if visible:
                    # Update the tile to be seen
                    game_map.tiles[x][y].seen = True
                    if wall:
                        tcod.console_set_char_background(con, x, y, colors.get("light wall"), tcod.BKGND_SET)
                    else:
                        tcod.console_set_char_background(con, x, y, colors.get("light ground"), tcod.BKGND_SET)
                else:
                    if not game_map.tiles[x][y].seen:
                        tcod.console_set_char_background(con, x, y, colors.get("unseen"), tcod.BKGND_SET)
                    elif wall:
                        tcod.console_set_char_background(con, x, y, colors.get("dark wall"), tcod.BKGND_SET)
                    else:
                        tcod.console_set_char_background(con, x, y, colors.get("dark ground"), tcod.BKGND_SET)


def draw_entity(con, entity, fov_map):
    if tcod.map_is_in_fov(fov_map, entity.x, entity.y):
        tcod.console_set_default_foreground(con, entity.color)
        tcod.console_put_char(con, entity.x, entity.y, entity.char, tcod.BKGND_NONE)


def clear_entity(con, entity):
    tcod.console_put_char(con, entity.x, entity.y, ' ', tcod.BKGND_NONE)
