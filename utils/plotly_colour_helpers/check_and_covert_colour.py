import plotly.colors


def check_and_covert_colour(color):
    """Convert a color from hex to RGB if needed."""
    # Deal with string formats
    if isinstance(color, str):
        if color.startswith('#'):
            # Check if the color is a hex value (starts with #)
            return plotly.colors.label_rgb(plotly.colors.hex_to_rgb(color))
        elif color.startswith('rgb'):
            # If the color is already in rgb/rgba format, return it as-is
            return color

    # If a tuple was given go ahead
    elif isinstance(color, tuple) and len(color) == 3:
        return color

    # Anything else not explicitly dealt with should raise an error
    else:
        raise ValueError(f"Unrecognized color format: {color}")
