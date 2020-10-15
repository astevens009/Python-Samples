# Demonstrating the use of a default value

# Adding a default value for the width
def banner_text(text, width = 80):
    """Display text in a banner format

    Args:
        text (str): The text to be displayed in a formatted banner
        width (int, optional): The size of the display. Defaults to 80.

    Raises:
        ValueError: Exception thrown if the text is larger than the given width
    """
    screen_width = width
    if len(text) > screen_width - 4:
        # NOTE: Raise an exception here...
        # print("\nYIKES!\nTHE TEXT IS TOO LONG TO FIT IN THE SPECIFIED WIDTH!\n")
        raise ValueError(
            "String \"{0}\" is larger than specified width {1}".format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


# Display the banner
# banner_text("*")
# banner_text("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. In nibh mauris cursus mattis molestie.")
# banner_text("*")

banner_text("*")
banner_text("Welcome to The Matrix!")
banner_text("Check your reality at the door!")
banner_text("*")