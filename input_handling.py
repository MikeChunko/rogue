# File name: input_handling.py
# Author: Michael Chunko
# Python Version: 3.7

# This file contains the functions to handle user input

import tcod


def handle_keys(key):
    # Fetch the character pressed
    key_char = chr(key.c)

    # Movement keys
    if key.vk == tcod.KEY_RIGHT or key_char == 'd':
        return {"move": (1, 0)}
    elif key.vk == tcod.KEY_LEFT or key_char == 'a':
        return {"move": (-1, 0)}
    elif key.vk == tcod.KEY_UP or key_char == 'w':
        return {"move": (0, -1)}
    elif key.vk == tcod.KEY_DOWN or key_char == 's':
        return {"move": (0, 1)}

    # Other keys
    if key.vk == tcod.KEY_ENTER and tcod.KEY_ALT:
        # Alt+Enter: toggle fullscreen
        return {"fullscreen": True}
    elif key.vk == tcod.KEY_ESCAPE:
        # Exit
        return {"exit": True}

    # No key pressed
    return {}
