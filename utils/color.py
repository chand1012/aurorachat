import random
import re


def hex_to_rgb(hex_color):
    """Convert a hex color to its RGB components."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb_color):
    """Convert an RGB color to its hex representation."""
    return '#' + ''.join(f'{component:02x}' for component in rgb_color)


def hex_to_int(hex_color):
    """Convert a hex color to its integer representation."""
    return int(hex_color.lstrip('#'), 16)


def random_color_in_gradient(hex_color1, hex_color2):
    """Generate a random color within the gradient of two hex colors."""
    rgb1 = hex_to_rgb(hex_color1)
    rgb2 = hex_to_rgb(hex_color2)

    random_rgb = tuple(random.randint(
        min(rgb1[i], rgb2[i]), max(rgb1[i], rgb2[i])) for i in range(3))

    return rgb_to_hex(random_rgb)
