def get_discrete_colour(colorscale, index):
    """
    If a discrete colourscale is used then the index could go out of bounds. Use modulo operator to wrap.
    """
    return colorscale[index % (len(colorscale))]
